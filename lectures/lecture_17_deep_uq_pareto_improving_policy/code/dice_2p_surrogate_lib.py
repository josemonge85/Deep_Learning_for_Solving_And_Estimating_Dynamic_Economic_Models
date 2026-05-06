"""Helpers for the two-parameter (rho, pi2) DICE-DEQN surrogate.

Ported from `02_DICE_DEQN_Library_Port.ipynb`:
  * §1   — `class P` (calibration constants)
  * §3   — exogenous functions (`population`, `tfp`, `sigma`, `theta1`, `beta_hat`, ...)
           and one-step transitions (`carbon_next`, `temperature_next`)
  * §4–5 — `build_net`, `split_policy`, `loss_fn`, `simulate`

The functions below are shared between (a) the five fixed-theta point solutions
and (b) the parameterised surrogate that takes (rho, pi2) as pseudo-states.

Network input is either 7-D (fixed) or 9-D (surrogate, last two dims =
normalized rho, pi2). The loss residual structure is identical; only the
beta_hat and damage Omega calls now depend on per-batch rho and pi2 tensors.

Note on design sets used downstream:
  * `ANCHOR_THETAS` (5 corner tags, used by Stage A point solutions and as
    Stage B replay anchors).
  * `_pt_solutions/2p/gp_anchors_25.json` (25-point reference cube, used by
    Stage D for the GP fit + Sobol indices). The two design sets are distinct.
"""
from __future__ import annotations

import math
import os
from dataclasses import dataclass
from typing import Optional, Sequence

import numpy as np
import tensorflow as tf


# ---------------------------------------------------------------------------
# Calibration constants (CDICE mmm_mmm). rho and pi2 are NOT here; they are
# per-batch parameters in the loss/simulator.
# ---------------------------------------------------------------------------
class P:
    Tstep = 1.0
    vartheta = 0.015
    psi = 0.68965517
    alpha = 0.30
    delta = 0.10
    L0 = 7403.0; Linfty = 11500.0; deltaL = 0.0268
    A0hat = 0.010295; gA0hat = 0.0217; deltaA = 0.005
    sigma0 = 0.0000955592; gSigma0 = -0.0152; deltaSigma = 0.001
    theta2 = 2.6; pback = 0.55; gback = 0.005; c2co2 = 3.666
    ELand0 = 0.00070922; deltaLand = 0.023
    fex0 = 0.5; fex1 = 1.0; Tyears = 85.0
    pi1 = 0.0; pow1 = 1.0; pow2 = 2.0
    b12_ = 0.054; b23_ = 0.0082
    MATeq = 0.607; MUOeq = 0.489; MLOeq = 1.281
    c1_ = 0.137; c3_ = 0.73; c4_ = 0.00689
    f2xco2 = 3.45; t2xco2 = 3.25; MATbase = 0.607
    k0 = 2.926; MAT0 = 0.851; MUO0 = 0.628; MLO0 = 1.323
    TAT0 = 1.1; TOC0 = 0.27; tau0 = 0.0
    b12 = Tstep * b12_; b23 = Tstep * b23_
    b21 = MATeq / MUOeq * b12_ * Tstep
    b32 = MUOeq / MLOeq * b23_ * Tstep
    c1 = Tstep * c1_; c1c3 = Tstep * c1_ * c3_
    c1f = Tstep * c1_ * f2xco2 / t2xco2
    c4 = Tstep * c4_


for _a in list(vars(P)):
    if not _a.startswith('_'):
        v = getattr(P, _a)
        if isinstance(v, (int, float)):
            setattr(P, _a, np.float32(v))

LOG2 = np.float32(math.log(2.0))
ONE_MINUS_DELTA_TSTEP = np.float32((1.0 - float(P.delta)) ** float(P.Tstep))


# ---------------------------------------------------------------------------
# Theta domain (rho, pi2). Center matches notebook 02 defaults.
# ---------------------------------------------------------------------------
RHO_MIN, RHO_MAX = np.float32(0.005), np.float32(0.025)
PI2_MIN, PI2_MAX = np.float32(0.001), np.float32(0.005)
RHO_DEFAULT = np.float32(0.015)
PI2_DEFAULT = np.float32(0.00236)

ANCHOR_THETAS: dict[str, tuple[float, float]] = {
    'pt_LL': (0.005, 0.001),
    'pt_LH': (0.005, 0.005),
    'pt_C':  (0.015, 0.003),
    'pt_HL': (0.025, 0.001),
    'pt_HH': (0.025, 0.005),
}


def normalize_theta(rho: np.ndarray | tf.Tensor,
                    pi2: np.ndarray | tf.Tensor):
    rho_n = (rho - RHO_MIN) / (RHO_MAX - RHO_MIN)
    pi2_n = (pi2 - PI2_MIN) / (PI2_MAX - PI2_MIN)
    return rho_n, pi2_n


# ---------------------------------------------------------------------------
# Friedl tau-transformation
# ---------------------------------------------------------------------------
def tau2t(tau):
    return -tf.math.log(1.0 - tau) / P.vartheta

def t2tau(t):
    return 1.0 - tf.math.exp(-P.vartheta * t)

def tau2tauplus(tau):
    return t2tau(tau2t(tau) + P.Tstep)


# ---------------------------------------------------------------------------
# Exogenous processes (NO dependence on rho or pi2)
# ---------------------------------------------------------------------------
def population(t):
    return P.L0 + (P.Linfty - P.L0) * (1.0 - tf.exp(-P.Tstep * P.deltaL * t))

def tfp(t):
    return P.A0hat * tf.exp((P.Tstep * P.gA0hat) *
        (1.0 - tf.exp(-P.Tstep * P.deltaA * t)) / (P.Tstep * P.deltaA))

def gr_tfp(t):
    return P.gA0hat * tf.exp(-P.Tstep * P.deltaA * t)

def gr_lab(t):
    return P.deltaL / ((P.Linfty / (P.Linfty - P.L0)) *
                        tf.exp(P.Tstep * P.deltaL * t) - 1.0)

def sigma_(t):
    log_factor = np.float32(math.log(1.0 + float(P.Tstep) * float(P.deltaSigma)))
    return P.sigma0 * tf.exp(P.Tstep * P.gSigma0 / log_factor *
                    ((1.0 + P.Tstep * P.deltaSigma) ** t - 1.0))

def theta1(t):
    return P.pback * (1000.0 * P.c2co2 * sigma_(t)) * tf.exp(-P.Tstep * P.gback * t) / P.theta2

def land_emissions(t):
    return P.ELand0 * tf.exp(-P.Tstep * P.deltaLand * t)

def ext_forcing(t):
    Yr = P.Tyears / P.Tstep
    return P.fex0 + (1.0 / Yr) * (P.fex1 - P.fex0) * tf.minimum(t, Yr)


# ---- rho-dependent: discount factor ----
def beta_hat(t, rho):
    """Per-batch discount factor; rho enters here."""
    return tf.exp((-rho + (1.0 - 1.0/P.psi) * gr_tfp(t) + gr_lab(t)) * P.Tstep)


# ---- pi2-dependent: damage function ----
def Omega(TAT, pi2):
    return pi2 * tf.pow(TAT, P.pow2)

def Omega_prime(TAT, pi2):
    return P.pow2 * pi2 * tf.pow(TAT, P.pow2 - 1.0)


# ---------------------------------------------------------------------------
# State transitions (no rho/pi2 dependence)
# ---------------------------------------------------------------------------
def carbon_next(MAT, MUO, MLO, mu, k, t):
    A_ = tfp(t); L_ = population(t); sig_ = sigma_(t); EL_ = land_emissions(t)
    E_ind = (1.0 - mu) * sig_ * A_ * L_ * tf.pow(k, P.alpha)
    MAT_n = (1.0 - P.b12) * MAT + P.b21 * MUO + P.Tstep * E_ind + P.Tstep * EL_
    MUO_n = P.b12 * MAT + (1.0 - P.b21 - P.b23) * MUO + P.b32 * MLO
    MLO_n = P.b23 * MUO + (1.0 - P.b32) * MLO
    return MAT_n, MUO_n, MLO_n

def temperature_next(TAT, TOC, MAT, t):
    Forcing = P.f2xco2 * tf.math.log(tf.maximum(MAT, 1e-6) / P.MATbase) / LOG2 + ext_forcing(t)
    TAT_n = (1.0 - P.c1c3 - P.c1f) * TAT + P.c1c3 * TOC + P.c1 * Forcing
    TOC_n = P.c4 * TAT + (1.0 - P.c4) * TOC
    return TAT_n, TOC_n


# ---------------------------------------------------------------------------
# Network
# ---------------------------------------------------------------------------
S_MIN = np.array([0.5,  0.5,  0.2,  1.0,  0.0,  0.0, 0.00], dtype='float32')
S_MAX = np.array([60.0, 3.0,  3.0,  4.0, 10.0,  4.0, 0.99], dtype='float32')
N_STATE = 7


def normalize_states(x7):
    return (x7 - S_MIN) / (S_MAX - S_MIN + 1e-8)


def build_net(input_dim: int, width: int = 768, name: str = 'policy_net'):
    """input_dim=7 for fixed-theta point solutions, 9 for the (rho,pi2) surrogate."""
    return tf.keras.Sequential([
        tf.keras.layers.Input(shape=(input_dim,)),
        tf.keras.layers.Dense(width, activation='relu', kernel_initializer='glorot_uniform'),
        tf.keras.layers.Dense(width, activation='relu', kernel_initializer='glorot_uniform'),
        tf.keras.layers.Dense(8),
    ], name=name)


# ---------------------------------------------------------------------------
# FiLM-conditioned network. Theta enters ONLY through per-layer (gamma, beta)
# modulation, never as a direct input feature. This structurally prevents the
# "lazy learning" failure mode where the optimizer collapses to a theta-blind
# policy: at every hidden layer, the activations are reshaped by theta-driven
# scale and shift, so a theta-blind policy is no longer representable.
#
# At init the gamma/beta MLP outputs zero (last layer kernel/bias = 0), so
# the network starts as a vanilla state-only MLP and the optimizer learns to
# *introduce* theta dependence rather than fighting against an entangled
# concat input. See Perez et al. (2018) "FiLM: Visual Reasoning with a
# General Conditioning Layer" for the original formulation.
# ---------------------------------------------------------------------------
class FiLMNet(tf.keras.Model):
    """9-D input split into state[:7] and theta[7:9]; theta modulates 2 hidden layers."""

    def __init__(self, width: int = 768, theta_dim: int = 2,
                 theta_hidden: int = 64, n_out: int = 8, name: str = 'film_policy'):
        super().__init__(name=name)
        self.theta_dim = theta_dim
        self.width = width
        self.theta_h = tf.keras.layers.Dense(theta_hidden, activation='relu',
                                             kernel_initializer='glorot_uniform',
                                             name='theta_h')
        # Zero-init: at start, gamma=beta=0 -> behaves like a theta-blind net.
        self.theta_film = tf.keras.layers.Dense(4 * width,
                                                kernel_initializer='zeros',
                                                bias_initializer='zeros',
                                                name='theta_film')
        self.h1 = tf.keras.layers.Dense(width, activation=None,
                                        kernel_initializer='glorot_uniform', name='h1')
        self.h2 = tf.keras.layers.Dense(width, activation=None,
                                        kernel_initializer='glorot_uniform', name='h2')
        self.out_layer = tf.keras.layers.Dense(n_out, name='out')

    def call(self, inputs, training=None):
        state = inputs[:, : -self.theta_dim]
        theta = inputs[:, -self.theta_dim :]
        film = self.theta_film(self.theta_h(theta))
        gamma1, beta1, gamma2, beta2 = tf.split(film, 4, axis=-1)
        h1 = tf.nn.relu((1.0 + gamma1) * self.h1(state) + beta1)
        h2 = tf.nn.relu((1.0 + gamma2) * self.h2(h1) + beta2)
        return self.out_layer(h2)


def build_film_net(width: int = 768, theta_dim: int = 2, theta_hidden: int = 64,
                   n_out: int = 8, name: str = 'film_policy') -> FiLMNet:
    """Build and eagerly build-shape the FiLM net so save_weights / count_params work."""
    net = FiLMNet(width=width, theta_dim=theta_dim, theta_hidden=theta_hidden,
                  n_out=n_out, name=name)
    _ = net(tf.zeros((1, 7 + theta_dim), dtype=tf.float32))
    return net


def build_surrogate_net(arch: str, width: int = 768, name: str = 'surrogate_2p'):
    """Dispatch helper for the 9-D surrogate: 'sequential' or 'film'."""
    if arch == 'film':
        return build_film_net(width=width, name=name)
    if arch == 'sequential':
        return build_net(input_dim=9, width=width, name=name)
    raise ValueError(f"Unknown arch: {arch}")


def split_policy(raw):
    k_plus     = tf.nn.softplus(raw[:, 0:1])
    lambd_hat  = tf.nn.softplus(raw[:, 1:2])
    mu         = tf.nn.softplus(raw[:, 2:3])
    nu_AT_hat  = tf.nn.softplus(raw[:, 3:4])
    nu_UO_hat  = raw[:, 4:5]
    nu_LO_hat  = raw[:, 5:6]
    eta_AT_hat = raw[:, 6:7]
    eta_OC_hat = raw[:, 7:8]
    return k_plus, lambd_hat, mu, nu_AT_hat, nu_UO_hat, nu_LO_hat, eta_AT_hat, eta_OC_hat


def make_input(states7, rho, pi2, augmented: bool):
    """Build the network input tensor.

    states7: (B, 7) physical-state batch.
    rho, pi2: (B, 1) per-batch parameter tensors in absolute units.
    augmented: True for the 9-D surrogate, False for the 7-D fixed-theta net.
    """
    s = (states7 - S_MIN) / (S_MAX - S_MIN + 1e-8)
    if not augmented:
        return s
    rho_n = (rho - RHO_MIN) / (RHO_MAX - RHO_MIN)
    pi2_n = (pi2 - PI2_MIN) / (PI2_MAX - PI2_MIN)
    return tf.concat([s, rho_n, pi2_n], axis=1)


# ---------------------------------------------------------------------------
# DEQN loss: shared between fixed-theta and surrogate (parameterised by theta).
#
# Reduction: standard MSE if cvar_alpha == 1.0, otherwise the mean of the worst
# alpha fraction of per-sample squared residuals (the Rockafellar-Uryasev
# CVaR_alpha estimator). CVaR-alpha forces the network to drive down the
# residual at the heaviest-tailed (state, theta) batch elements rather than
# trading them off against easy ones, which is the standard remedy for
# "lazy learning" in conditional surrogates.
# ---------------------------------------------------------------------------
def _cvar_mean(per_sample: tf.Tensor, alpha: float) -> tf.Tensor:
    """Mean of the top-`alpha` fraction of `per_sample` (a 1-D tensor of >= 0).

    alpha=1.0 reduces to tf.reduce_mean. alpha=0.2 averages the worst 20%.
    """
    if alpha >= 1.0:
        return tf.reduce_mean(per_sample)
    n = tf.shape(per_sample)[0]
    n_f = tf.cast(n, tf.float32)
    k = tf.cast(tf.math.ceil(alpha * n_f), tf.int32)
    k = tf.maximum(k, 1)
    top, _ = tf.math.top_k(per_sample, k=k, sorted=False)
    return tf.reduce_mean(top)


def make_loss_fn(model: tf.keras.Model, augmented: bool, cvar_alpha: float = 1.0,
                 loss_form: str = 'absolute', sensitivity_weight: float = 0.0):
    """Return a @tf.function-compiled loss closure that takes (states7, rho, pi2).

    cvar_alpha in (0, 1]. 1.0 = standard MSE. 0.2 = CVaR over the worst 20%
    of (state, theta) batch elements.

    loss_form='absolute' (default): per-sample loss is sum of eq_i**2.
    loss_form='relative': per-sample loss is sum of eq_i**2 / scale_i**2, where
    scale_i**2 is the sum of squared LHS/RHS components of FOC i. Restores
    gradient parity across regions of theta where the FOCs are intrinsically
    small in absolute terms (e.g. low pi2, where climate co-states vanish).

    sensitivity_weight > 0: add an unsupervised parameter-sensitivity loss
    enforcing d/dtheta R(p(x,theta), x, theta) ~ 0 along a random direction in
    theta space. Computed via tf.autodiff.ForwardAccumulator; normalized by
    scale_sq for consistency with the relative residual form. Directly attacks
    the basin-selection failure at low-pi2 where multiple FOC-zero policies
    locally exist (Section 13 of instructions_unsupervised.md).
    """
    cvar_alpha = float(cvar_alpha)
    use_relative = (loss_form == 'relative')
    use_sensitivity = sensitivity_weight > 0.0
    EPS_SCALE_SQ = tf.constant(1e-8, dtype=tf.float32)
    sens_w = tf.constant(float(sensitivity_weight), dtype=tf.float32)

    def _compute_foc(states7, rho, pi2):
        """Inner FOC computation. Returns (eq, scale_sq, mu) with eq and
        scale_sq of shape (B, 8) each, mu of shape (B, 1) for the bound penalty.
        Called twice when sensitivity_weight > 0 (once normally, once inside
        ForwardAccumulator for the JVP).
        """
        k   = states7[:, 0:1]; MAT = states7[:, 1:2]
        MUO = states7[:, 2:3]; MLO = states7[:, 3:4]
        TAT = states7[:, 4:5]; TOC = states7[:, 5:6]
        tau = states7[:, 6:7]
        t   = tau2t(tau)

        raw = model(make_input(states7, rho, pi2, augmented))
        k_plus, lambd_hat, mu, nu_AT, nu_UO, nu_LO, eta_AT, eta_OC = split_policy(raw)

        A_   = tfp(t); L_ = population(t); sig_ = sigma_(t)
        th1_ = theta1(t)
        _bhat = beta_hat(t, rho)
        growth_factor = tf.exp(P.Tstep * (gr_tfp(t) + gr_lab(t)))

        Omega_ = Omega(TAT, pi2)
        Theta_ = th1_ * tf.pow(mu, P.theta2)
        Theta_prime = th1_ * P.theta2 * tf.pow(mu, P.theta2 - 1.0)
        con = tf.pow(lambd_hat, -P.psi)

        MAT_p, MUO_p, MLO_p = carbon_next(MAT, MUO, MLO, mu, k, t)
        TAT_p, TOC_p = temperature_next(TAT, TOC, MAT, t)
        tau_p = tau2tauplus(tau)
        states_next = tf.concat([k_plus, MAT_p, MUO_p, MLO_p, TAT_p, TOC_p, tau_p], axis=1)
        raw_n = model(make_input(states_next, rho, pi2, augmented))
        _, lh_n, mu_n, nuAT_n, nuUO_n, nuLO_n, etAT_n, etOC_n = split_policy(raw_n)

        t_n = tau2t(tau_p)
        A_n = tfp(t_n); L_n = population(t_n); sig_n = sigma_(t_n); th1_n = theta1(t_n)
        Theta_n = th1_n * tf.pow(mu_n, P.theta2)
        Omega_p = Omega(TAT_p, pi2)
        Omega_p_prime = Omega_prime(TAT_p, pi2)

        rhs1 = _bhat * (
            lh_n * (P.Tstep * (1.0 - Theta_n - Omega_p) * P.alpha * tf.pow(k_plus, P.alpha - 1.0)
                    + ONE_MINUS_DELTA_TSTEP)
            + (-nuAT_n) * (1.0 - mu_n) * P.Tstep * sig_n * A_n * L_n * P.alpha
              * tf.pow(k_plus, P.alpha - 1.0))
        lhs1 = growth_factor * lambd_hat
        eq1 = lhs1 - rhs1
        scale1_sq = lhs1**2 + rhs1**2 + EPS_SCALE_SQ

        bT1 = P.Tstep * (1.0 - Theta_ - Omega_) * tf.pow(k, P.alpha)
        bT2 = -P.Tstep * con
        bT3 = ONE_MINUS_DELTA_TSTEP * k
        bT4 = -growth_factor * k_plus
        eq2 = bT1 + bT2 + bT3 + bT4
        scale2_sq = bT1**2 + bT2**2 + bT3**2 + bT4**2 + EPS_SCALE_SQ

        lambdMU = (-lambd_hat * P.Tstep * Theta_prime * tf.pow(k, P.alpha)
                   - (-nu_AT) * P.Tstep * sig_ * A_ * L_ * tf.pow(k, P.alpha))
        eq3 = lambdMU + (1.0 - mu) - tf.sqrt(lambdMU * lambdMU + (1.0 - mu) * (1.0 - mu) + 1e-12)
        scale3_sq = lambdMU**2 + (1.0 - mu)**2 + 1.0

        rhs4 = _bhat * (
            lh_n * (-P.Tstep * Omega_p_prime) * tf.pow(k_plus, P.alpha)
            + etAT_n * (1.0 - P.c1c3 - P.c1f) + etOC_n * P.c4)
        lhs4 = eta_AT
        eq4 = lhs4 - rhs4
        scale4_sq = lhs4**2 + rhs4**2 + EPS_SCALE_SQ

        rhs5 = _bhat * (
            (-nuAT_n) * (1.0 - P.b12) + nuUO_n * P.b12
            + etAT_n * P.c1 * P.f2xco2 / (LOG2 * tf.maximum(MAT_p, 1e-6)))
        lhs5 = -nu_AT
        eq5 = lhs5 - rhs5
        scale5_sq = lhs5**2 + rhs5**2 + EPS_SCALE_SQ

        rhs6 = _bhat * ((-nuAT_n) * P.b21 + nuUO_n * (1.0 - P.b21 - P.b23) + nuLO_n * P.b23)
        lhs6 = nu_UO
        eq6 = lhs6 - rhs6
        scale6_sq = lhs6**2 + rhs6**2 + EPS_SCALE_SQ

        rhs7 = _bhat * (nuUO_n * P.b32 + nuLO_n * (1.0 - P.b32))
        lhs7 = nu_LO
        eq7 = lhs7 - rhs7
        scale7_sq = lhs7**2 + rhs7**2 + EPS_SCALE_SQ

        rhs8 = _bhat * (etAT_n * P.c1c3 + etOC_n * (1.0 - P.c4))
        lhs8 = eta_OC
        eq8 = lhs8 - rhs8
        scale8_sq = lhs8**2 + rhs8**2 + EPS_SCALE_SQ

        eq = tf.concat([eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8], axis=-1)            # (B, 8)
        scale_sq = tf.concat([scale1_sq, scale2_sq, scale3_sq, scale4_sq,
                              scale5_sq, scale6_sq, scale7_sq, scale8_sq], axis=-1)  # (B, 8)
        return eq, scale_sq, mu

    @tf.function
    def loss_fn(states7, rho, pi2):
        states7 = tf.cast(states7, tf.float32)
        rho = tf.cast(rho, tf.float32)
        pi2 = tf.cast(pi2, tf.float32)

        if use_sensitivity:
            v_rho = tf.random.normal(tf.shape(rho))
            v_pi2 = tf.random.normal(tf.shape(pi2))
            with tf.autodiff.ForwardAccumulator(
                    primals=(rho, pi2), tangents=(v_rho, v_pi2)) as acc:
                eq, scale_sq, mu = _compute_foc(states7, rho, pi2)
            deq_dv = acc.jvp(eq)             # (B, 8) directional derivative of eq w.r.t. (rho,pi2)
        else:
            eq, scale_sq, mu = _compute_foc(states7, rho, pi2)

        if use_relative:
            per_sample = tf.reduce_mean(eq**2 / scale_sq, axis=-1)
        else:
            per_sample = tf.reduce_mean(eq**2, axis=-1)
        L_eq = _cvar_mean(per_sample, cvar_alpha)

        L_total = L_eq
        if use_sensitivity:
            sens_per_sample = tf.reduce_mean(deq_dv**2 / scale_sq, axis=-1)
            L_sens = tf.reduce_mean(sens_per_sample)
            L_total = L_total + sens_w * L_sens

        pen_mu_upper = 1e-2 * tf.reduce_mean(tf.maximum(mu - 1.0, 0.0) ** 2)
        return L_total + pen_mu_upper

    return loss_fn


# ---------------------------------------------------------------------------
# Trajectory generation
# ---------------------------------------------------------------------------
def gen_traj(model: tf.keras.Model,
             rho: np.ndarray, pi2: np.ndarray,
             augmented: bool,
             n_traj: int = 64, n_steps: int = 300,
             rng: Optional[np.random.Generator] = None) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """On-policy trajectory generator. rho and pi2 are (n_traj,) per-trajectory arrays.

    Returns (states[n_traj * n_steps, 7], rho_full[n_traj * n_steps, 1],
             pi2_full[n_traj * n_steps, 1]).
    """
    if rng is None:
        rng = np.random.default_rng()
    rho = rho.astype('float32').reshape(-1, 1)
    pi2 = pi2.astype('float32').reshape(-1, 1)
    assert rho.shape[0] == n_traj and pi2.shape[0] == n_traj

    k0   = (float(P.k0)   * rng.uniform(0.8, 1.2, (n_traj, 1))).astype('float32')
    MAT0 = (float(P.MAT0) * rng.uniform(0.9, 1.1, (n_traj, 1))).astype('float32')
    MUO0 = np.full((n_traj, 1), float(P.MUO0), dtype='float32')
    MLO0 = np.full((n_traj, 1), float(P.MLO0), dtype='float32')
    TAT0 = (float(P.TAT0) * rng.uniform(0.8, 1.2, (n_traj, 1))).astype('float32')
    TOC0 = np.full((n_traj, 1), float(P.TOC0), dtype='float32')
    tau0 = np.full((n_traj, 1), float(P.tau0), dtype='float32')
    state = np.concatenate([k0, MAT0, MUO0, MLO0, TAT0, TOC0, tau0], axis=1)

    rho_t = tf.constant(rho, dtype=tf.float32)
    pi2_t = tf.constant(pi2, dtype=tf.float32)

    states_out = [state.copy()]
    for _ in range(n_steps - 1):
        s_t = tf.constant(state, dtype=tf.float32)
        inp = make_input(s_t, rho_t, pi2_t, augmented)
        raw = model(inp, training=False).numpy()
        # Numerically stable softplus: max(x,0) + log1p(exp(-|x|))
        def _stable_softplus(x):
            return np.maximum(x, 0.0) + np.log1p(np.exp(-np.abs(x)))
        k_plus = _stable_softplus(raw[:, 0:1])
        mu     = _stable_softplus(raw[:, 2:3])
        k = np.maximum(state[:, 0:1], 1e-6)
        MAT = state[:, 1:2]; MUO = state[:, 2:3]; MLO = state[:, 3:4]
        TAT = state[:, 4:5]; TOC = state[:, 5:6]; tau = state[:, 6:7]
        t = (-np.log(np.maximum(1.0 - tau, 1e-6)) / float(P.vartheta)).astype('float32')
        t_tf = tf.constant(t)
        A_ = tfp(t_tf).numpy(); L_ = population(t_tf).numpy()
        sig_ = sigma_(t_tf).numpy(); EL_ = land_emissions(t_tf).numpy()
        Fex_ = ext_forcing(t_tf).numpy()
        E_ind = (1.0 - mu) * sig_ * A_ * L_ * np.power(k, float(P.alpha))
        MAT_n = (1-float(P.b12))*MAT + float(P.b21)*MUO + float(P.Tstep)*E_ind + float(P.Tstep)*EL_
        MUO_n = float(P.b12)*MAT + (1-float(P.b21)-float(P.b23))*MUO + float(P.b32)*MLO
        MLO_n = float(P.b23)*MUO + (1-float(P.b32))*MLO
        Forcing = float(P.f2xco2)*np.log(np.maximum(MAT, 1e-6)/float(P.MATbase))/np.log(2.0) + Fex_
        TAT_n = (1-float(P.c1c3)-float(P.c1f))*TAT + float(P.c1c3)*TOC + float(P.c1)*Forcing
        TOC_n = float(P.c4)*TAT + (1-float(P.c4))*TOC
        tau_n = (1.0 - np.exp(-float(P.vartheta) * (t + float(P.Tstep)))).astype('float32')
        state = np.concatenate(
            [np.maximum(k_plus, 0.01), MAT_n, MUO_n, MLO_n, TAT_n, TOC_n, tau_n],
            axis=1).astype('float32')
        states_out.append(state.copy())

    states_full = np.concatenate(states_out, axis=0)
    rho_full = np.tile(rho, (n_steps, 1))
    pi2_full = np.tile(pi2, (n_steps, 1))
    return states_full, rho_full, pi2_full


# ---------------------------------------------------------------------------
# Forward simulation under the trained policy. Same structure as notebook 02
# `simulate()` but parameterised by (rho, pi2). Note: rho enters indirectly
# only through the *trained policy*; the deterministic forward path itself
# does not depend on rho once the policy is fixed.
# ---------------------------------------------------------------------------
def simulate(model: tf.keras.Model,
             rho: float, pi2: float,
             augmented: bool,
             n_steps: int = 300) -> dict[str, np.ndarray]:
    rho = float(rho); pi2 = float(pi2)
    state = [float(P.k0), float(P.MAT0), float(P.MUO0), float(P.MLO0),
             float(P.TAT0), float(P.TOC0), float(P.tau0)]
    out: dict[str, list] = {ky: [] for ky in
        ['year', 'k_abs', 'k_eff', 'MAT_GtC', 'TAT', 'TOC',
         'mu', 'con_abs', 'scc', 'carbon_tax', 'Eind_GtCO2']}

    rho_t = tf.constant([[rho]], dtype=tf.float32)
    pi2_t = tf.constant([[pi2]], dtype=tf.float32)

    for s in range(n_steps):
        year = 2015.0 + s
        k_, MAT_, MUO_, MLO_, TAT_, TOC_, tau_ = state
        t_val = -np.log(max(1 - tau_, 1e-6)) / float(P.vartheta)
        x = tf.constant([state], dtype=tf.float32)
        inp = make_input(x, rho_t, pi2_t, augmented)
        raw = model(inp, training=False).numpy()
        kp   = np.log1p(np.exp(raw[0, 0]))
        lh   = np.log1p(np.exp(raw[0, 1]))
        mu_t = np.log1p(np.exp(raw[0, 2]))
        nuAT = np.log1p(np.exp(raw[0, 3]))
        nuUO = raw[0, 4]; etAT = raw[0, 6]
        t_tf = tf.constant([[t_val]], dtype=tf.float32)
        sig_ = sigma_(t_tf).numpy().item()
        A_   = tfp(t_tf).numpy().item()
        L_   = population(t_tf).numpy().item()
        EL_  = land_emissions(t_tf).numpy().item()
        Fex_ = ext_forcing(t_tf).numpy().item()
        th1_ = (float(P.pback) * (1000.0 * float(P.c2co2) * sig_)
                * np.exp(-float(P.Tstep) * float(P.gback) * t_val) / float(P.theta2))
        Theta_ = th1_ * mu_t**float(P.theta2)
        Omega_ = pi2 * TAT_**2
        con = lh ** (-float(P.psi))
        k_safe = max(k_, 1e-6)
        dvdk = (lh * (float(P.Tstep) * (1 - Theta_ - Omega_) * float(P.alpha)
                      * k_safe**(float(P.alpha)-1) + (1-float(P.delta))**float(P.Tstep))
                + (-nuAT) * (1 - mu_t) * float(P.Tstep) * sig_ * A_ * L_
                * float(P.alpha) * k_safe**(float(P.alpha)-1))
        dvdMAT = ((-nuAT) * (1 - float(P.b12)) + nuUO * float(P.b12)
                  + etAT * float(P.c1) * float(P.f2xco2) / (np.log(2.0) * max(MAT_, 1e-6)))
        scc = -dvdMAT / (dvdk + 1e-15) * A_ * L_ / float(P.c2co2)
        c_tax = th1_ * float(P.theta2) * mu_t**(float(P.theta2)-1) / sig_ if sig_ > 1e-15 else 0.0
        c_tax_co2 = c_tax / float(P.c2co2)
        E_ind_eff = (1 - mu_t) * sig_ * A_ * L_ * k_safe**float(P.alpha)
        E_ind_GtCO2 = E_ind_eff * 1000.0 * float(P.c2co2)
        out['year'].append(year); out['k_eff'].append(k_); out['k_abs'].append(k_ * A_ * L_)
        out['MAT_GtC'].append(MAT_ * 1000)
        out['TAT'].append(TAT_); out['TOC'].append(TOC_); out['mu'].append(mu_t)
        out['con_abs'].append(con * A_ * L_); out['scc'].append(scc)
        out['carbon_tax'].append(c_tax_co2); out['Eind_GtCO2'].append(E_ind_GtCO2)
        MAT_n = (1-float(P.b12))*MAT_ + float(P.b21)*MUO_ + float(P.Tstep)*E_ind_eff + float(P.Tstep)*EL_
        MUO_n = float(P.b12)*MAT_ + (1-float(P.b21)-float(P.b23))*MUO_ + float(P.b32)*MLO_
        MLO_n = float(P.b23)*MUO_ + (1-float(P.b32))*MLO_
        Forcing = float(P.f2xco2)*np.log(max(MAT_, 1e-6)/float(P.MATbase))/np.log(2.0) + Fex_
        TAT_n = (1-float(P.c1c3)-float(P.c1f))*TAT_ + float(P.c1c3)*TOC_ + float(P.c1)*Forcing
        TOC_n = float(P.c4)*TAT_ + (1-float(P.c4))*TOC_
        tau_n = 1.0 - np.exp(-float(P.vartheta) * (t_val + float(P.Tstep)))
        state = [max(kp, 0.01), MAT_n, MUO_n, MLO_n, TAT_n, TOC_n, tau_n]
    return {k: np.array(v) for k, v in out.items()}


# ---------------------------------------------------------------------------
# Sampling helpers
# ---------------------------------------------------------------------------
def sobol_thetas(n: int, seed: int = 0) -> np.ndarray:
    """Return (n, 2) array of Sobol-sampled (rho, pi2) in absolute units."""
    from scipy.stats import qmc
    sampler = qmc.Sobol(d=2, scramble=True, seed=seed)
    u = sampler.random(n).astype('float32')
    rho = (RHO_MIN + (RHO_MAX - RHO_MIN) * u[:, 0:1]).astype('float32')
    pi2 = (PI2_MIN + (PI2_MAX - PI2_MIN) * u[:, 1:2]).astype('float32')
    return np.concatenate([rho, pi2], axis=1)


def build_replay_buffer(n_traj_per_corner: int = 64, n_steps: int = 300,
                        seed: int = 0, pt_width: int = 512,
                        anchor_set: Optional[dict] = None
                        ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Replay buffer of corner-solution state distributions.

    For each anchor theta in ANCHOR_THETAS, load the Stage A point-solution
    weights and roll on-policy trajectories under that *corner* net at the
    corner theta. The resulting (state, theta) pairs are the *true* state
    distribution induced by the correct policy at each corner.

    Mixing these into Stage B training fixes the v1 root cause documented in
    memory/project_day8_surrogate_v1_v2_status.md: surrogate-generated
    trajectories are too smooth in theta and fail to cover corner state
    distributions, so corner FOC residuals are evaluated on the *wrong*
    states and never get pushed down. Replay forces the surrogate to be
    Bellman-consistent at the corner state distribution.

    Returns (states, rho, pi2) of shape (5 * n_traj_per_corner * n_steps, 7),
    (..., 1), (..., 1). Roughly 96k pairs at defaults, ~5 MB.
    """
    rng = np.random.default_rng(seed)
    all_s, all_r, all_p = [], [], []
    anchors = anchor_set if anchor_set is not None else ANCHOR_THETAS
    for tag, (rho_v, pi2_v) in anchors.items():
        cw = os.path.join(ARTIFACTS_DIR, f'{tag}.weights.h5')
        if not os.path.exists(cw):
            raise FileNotFoundError(
                f'Missing corner weights: {cw}. Run Stage A before Stage B with replay.')
        corner_net = build_net(input_dim=7, width=pt_width, name=f'corner_{tag}')
        corner_net.load_weights(cw)
        rho_arr = np.full(n_traj_per_corner, rho_v, dtype='float32')
        pi2_arr = np.full(n_traj_per_corner, pi2_v, dtype='float32')
        s, r, p = gen_traj(corner_net, rho_arr, pi2_arr,
                           augmented=False,
                           n_traj=n_traj_per_corner, n_steps=n_steps, rng=rng)
        all_s.append(s); all_r.append(r); all_p.append(p)
    return (np.concatenate(all_s, axis=0),
            np.concatenate(all_r, axis=0),
            np.concatenate(all_p, axis=0))


def build_replay_buffer_with_teacher(n_traj_per_corner: int = 64, n_steps: int = 300,
                                     seed: int = 0, pt_width: int = 512,
                                     anchor_set: Optional[dict] = None
                                     ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Like build_replay_buffer, but also returns the teacher (corner-net)
    activated 8-D policy output at each replay state. Used for distillation.
    """
    rng = np.random.default_rng(seed)
    all_s, all_r, all_p, all_t = [], [], [], []
    anchors = anchor_set if anchor_set is not None else ANCHOR_THETAS
    for tag, (rho_v, pi2_v) in anchors.items():
        cw = os.path.join(ARTIFACTS_DIR, f'{tag}.weights.h5')
        if not os.path.exists(cw):
            raise FileNotFoundError(
                f'Missing corner weights: {cw}. Run Stage A before Stage B with replay.')
        corner_net = build_net(input_dim=7, width=pt_width, name=f'corner_{tag}_t')
        corner_net.load_weights(cw)
        rho_arr = np.full(n_traj_per_corner, rho_v, dtype='float32')
        pi2_arr = np.full(n_traj_per_corner, pi2_v, dtype='float32')
        s, r, p = gen_traj(corner_net, rho_arr, pi2_arr,
                           augmented=False,
                           n_traj=n_traj_per_corner, n_steps=n_steps, rng=rng)
        # Teacher output: activated 8-D policy at each (state, theta) pair.
        s_in = make_input(tf.cast(s, tf.float32),
                          tf.cast(r, tf.float32), tf.cast(p, tf.float32),
                          augmented=False)
        raw = corner_net(s_in)
        kplus, lambd, mu, nuAT, nuUO, nuLO, etAT, etOC = split_policy(raw)
        teach = tf.concat([kplus, lambd, mu, nuAT, nuUO, nuLO, etAT, etOC], axis=1).numpy()
        all_s.append(s); all_r.append(r); all_p.append(p); all_t.append(teach)
    return (np.concatenate(all_s, axis=0),
            np.concatenate(all_r, axis=0),
            np.concatenate(all_p, axis=0),
            np.concatenate(all_t, axis=0))


def curriculum_thetas(n: int, episode: int, total_episodes: int,
                      narrow_until: int = 100, seed: int = 0) -> np.ndarray:
    """Stage-B curriculum: shrink the cube around the center during early episodes."""
    from scipy.stats import qmc
    if episode < narrow_until:
        frac = 0.5 + 0.5 * (episode / narrow_until)  # 0.5 -> 1.0
    else:
        frac = 1.0
    sampler = qmc.Sobol(d=2, scramble=True, seed=seed + episode)
    u = sampler.random(n).astype('float32')
    rho_c = 0.5 * (RHO_MIN + RHO_MAX); pi2_c = 0.5 * (PI2_MIN + PI2_MAX)
    rho_w = 0.5 * (RHO_MAX - RHO_MIN) * frac; pi2_w = 0.5 * (PI2_MAX - PI2_MIN) * frac
    rho = (rho_c + (2.0 * u[:, 0:1] - 1.0) * rho_w).astype('float32')
    pi2 = (pi2_c + (2.0 * u[:, 1:2] - 1.0) * pi2_w).astype('float32')
    return np.concatenate([rho, pi2], axis=1)


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_DIR = os.path.join(HERE, '_pt_solutions', '2p')
FIGURES_DIR = os.path.join(ARTIFACTS_DIR, 'figures')


def ensure_dirs():
    os.makedirs(ARTIFACTS_DIR, exist_ok=True)
    os.makedirs(FIGURES_DIR, exist_ok=True)
