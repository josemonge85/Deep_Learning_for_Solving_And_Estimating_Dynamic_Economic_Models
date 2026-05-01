#!/usr/bin/env python3
"""Regenerate per-lecture README.md from course.yml.

Each per-lecture README opens with one short framing sentence, then a
bulleted **What this lecture covers** list (one bold-led bullet per
sub-topic), then **Learning objectives** as another bulleted list.
Materials, script references, readings, and prev/next nav follow.
"""
from __future__ import annotations
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parents[2]


# Per-lecture content. Keyed by NEW block ID (B00..B16). Each entry:
#   "opener":     1-2 sentence framing of the lecture.
#   "covers":     list of bullets for "What this lecture covers". Each
#                 bullet starts with **bold lead-in** then a clause.
#   "objectives": list of "After this lecture you can ..." bullets.
CONTENT: dict[str, dict] = {
    "B00": {
        "opener": "A self-paced primer in Python and Jupyter that brings readers without prior Python exposure up to the level the rest of the course assumes. Skip this lecture entirely if you write Python every day.",
        "covers": [
            "**Jupyter notebooks.** What a notebook is, how cells work, how to run code interactively in a browser.",
            "**Python as a calculator.** Arithmetic, variables, and types (numbers, booleans, strings).",
            "**Basic data structures.** Tuples, lists, dictionaries, and basic string handling.",
            "**Control flow.** Conditionals, loops, and functions.",
            "**Object-oriented Python.** Classes, methods, and a light tour of inheritance.",
            "**Scientific Python.** NumPy arrays and linear algebra; pandas data frames; basic plotting with Matplotlib.",
        ],
        "objectives": [
            "Open and run a Jupyter notebook end-to-end on your local machine.",
            "Write Python expressions, define functions, and use the standard control-flow constructs fluently.",
            "Manipulate NumPy arrays and pandas data frames, and produce a basic Matplotlib plot.",
            "Read the course's notebooks without stumbling on Python syntax.",
        ],
    },
    "B01": {
        "opener": "The working knowledge of deep learning that the rest of the course assumes, with economics-flavoured worked examples throughout.",
        "covers": [
            "**Classical ML and the bias-variance trade-off.** Linear regression, classification, and unsupervised learning as a foundation for everything that follows.",
            "**Stochastic gradient descent.** SGD, mini-batches, momentum, and adaptive variants (Adam, RMSProp); when each one is the right default.",
            "**Deep neural networks.** Depth, width, activation choices, and the **double-descent** phenomenon on a controlled synthetic example.",
            "**Sequence models.** MLPs, LSTMs, and small Transformers compared on Edgeworth-cycle data, exposing the **memory ladder** of architectures.",
            "**Tooling.** TensorFlow and PyTorch side by side, plus TensorBoard for instrumenting a training run.",
        ],
        "objectives": [
            "Implement SGD by hand and explain mini-batch, momentum, and adaptive variants.",
            "Train an MLP and a deep neural network end-to-end in TensorFlow and in PyTorch.",
            "Reproduce double descent on a controlled synthetic problem.",
            "Compare MLP, LSTM, and small-Transformer architectures on Edgeworth-cycle data and read off the memory ladder.",
            "Use TensorBoard to instrument a training run.",
        ],
    },
    "B02": {
        "opener": "The central method of the course. **Deep Equilibrium Nets (DEQNs)** parameterize a recursive-equilibrium policy with a neural network and train it on equilibrium-residual losses, sidestepping the curse of dimensionality.",
        "covers": [
            "**The DEQN principle.** Why minimizing the squared norm of equilibrium residuals on a simulated state distribution recovers the policy, and how this differs from projection, value-function iteration, and perturbation.",
            "**Deterministic Brock-Mirman.** A hand-built DEQN on the canonical growth model, with a closed-form check.",
            "**Stochastic Brock-Mirman.** Adding productivity shocks and using Gauss-Hermite quadrature for the conditional expectations in the Euler equation.",
            "**Constraints.** Borrowing and non-negativity constraints encoded in the loss via Fischer-Burmeister complementarity.",
            "**Loss design.** A side-by-side comparison of six loss kernels (MSE, MAE, Huber, quantile, CVaR, log-cosh) trained on the same setup so the trade-offs become concrete.",
        ],
        "objectives": [
            "State the DEQN training principle and write the residual operator for a recursive equilibrium given to you.",
            "Train deterministic Brock-Mirman with a DEQN and verify the policy against the closed-form solution.",
            "Extend the Brock-Mirman DEQN to stochastic productivity with a quadrature rule of your choice.",
            "Encode borrowing and non-negativity constraints with Fischer-Burmeister complementarity.",
            "Pick a loss kernel deliberately given the residual distribution of a model.",
        ],
    },
    "B03": {
        "opener": "The first large-scale nonlinear DSGE application of DEQNs.",
        "covers": [
            "**The IRBC model.** N symmetric countries with capital, country-specific productivity shocks, and risk-sharing through a complete bond market; equilibrium is N Euler equations plus a world resource constraint.",
            "**Why DEQNs scale here.** The state space is 2N-dimensional; classical methods scale poorly with N, DEQNs do not.",
            "**Solution and validation.** Train the DEQN, recover the symmetric steady state, and validate the policy via Euler-equation residuals along a simulated path.",
            "**Comparative statics.** Read off the effect of a parameter change (e.g. doubling depreciation) directly from the trained policy.",
        ],
        "objectives": [
            "Set up the IRBC residual loss on a simulated state distribution.",
            "Train an N-country IRBC DEQN and recover the symmetric steady state.",
            "Run a comparative-statics exercise and read the result from the trained policy.",
            "Report Euler-equation residuals as a diagnostic across the simulated state distribution.",
        ],
    },
    "B04": {
        "opener": "Two of the main hyperparameter-engineering tasks for DEQN training in practice: choosing an architecture, and balancing the multi-component residual loss.",
        "covers": [
            "**Neural architecture search.** Random search and Hyperband (successive halving), implemented from scratch in pure Python.",
            "**A 10-D NAS problem.** Searching over depth, width, activation, and learning-rate decay on a DEQN benchmark.",
            "**Loss balancing.** Why different equilibrium equations on different scales kill training, and how to fix it.",
            "**Three balancing schemes.** ReLoBRaLo, SoftAdapt, and GradNorm compared head-to-head on the same multi-residual run.",
        ],
        "objectives": [
            "Implement random search and Hyperband in pure Python.",
            "Run a 10-D NAS sweep on a DEQN problem and read off the winning architecture.",
            "Compute ReLoBRaLo loss weights by hand on a small example.",
            "Compare ReLoBRaLo, SoftAdapt, and GradNorm on a shared multi-residual training run.",
        ],
    },
    "B05": {
        "opener": "The automatic-differentiation machinery that DEQN training depends on, made explicit.",
        "covers": [
            "**Lagrangian primitives.** Deriving a single per-agent primitive Π whose partial derivatives give every Euler-equation residual.",
            "**Two-tape autodiff.** Recovering each gradient with two `tf.GradientTape` (or equivalent) calls per Euler equation.",
            "**Cross-checking.** A machine-precision comparison of autodiff residuals against hand-derived residuals on Brock-Mirman.",
            "**Lifting to IRBC.** Applying the same template to the multi-country setup of the previous lecture.",
            "**Common pitfalls.** Graph mode vs eager, dtype, in-place ops, and what to do when gradients silently disappear.",
        ],
        "objectives": [
            "Derive a Lagrangian primitive analytically for a small recursive problem.",
            "Implement a two-tape autodiff Euler residual and verify it against the closed-form derivative.",
            "Apply the same template to deterministic and stochastic Brock-Mirman, and to multi-country IRBC.",
            "Diagnose autodiff numerical issues (graph mode vs eager, dtype, in-place ops).",
        ],
    },
    "B06": {
        "opener": "A modern DEQN variant where the policy reads a long shock history instead of a current-state vector. Following Azinovic-Yang-Žemlička (2025).",
        "covers": [
            "**The sequence-space idea.** Replace the high-dimensional state with the last ~80 shock realizations; the network learns the residual map directly.",
            "**Why it generalizes.** The same template handles multi-equation systems with multiple shock channels without re-engineering the input.",
            "**Brock-Mirman warm-up.** Sequence-space DEQN with an 80-step shock history; verify the policy.",
            "**Krusell-Smith benchmark.** The same template on the canonical heterogeneous-agent benchmark.",
            "**Self-study extensions.** Multi-country IRBC and a borrowed JAX tutorial port (`KrusellSmith_Tutorial_CPU.ipynb`).",
        ],
        "objectives": [
            "Build the shock-history input pipeline for a sequence-space DEQN.",
            "Train a sequence-space DEQN on Brock-Mirman with an 80-step shock history and verify the policy.",
            "Extend the same template to Krusell-Smith.",
            "Explain why sequence-space DEQNs handle multi-shock systems gracefully.",
        ],
    },
    "B07": {
        "opener": "Overlapping-generations (OLG) models with DEQNs, at two scales.",
        "covers": [
            "**Cohort structure.** One Euler equation per cohort, stacked into a single Lagrangian primitive; the DEQN training principle does not change.",
            "**Analytic small OLG.** A closed-form lifecycle savings model used as a sanity check on the DEQN solution.",
            "**The 56-period benchmark.** The standard production-scale OLG model with borrowing constraints.",
            "**Borrowing constraints.** Fischer-Burmeister complementarity used cohort-by-cohort to handle the inequality.",
            "**Diagnostics.** Lifecycle profiles, aggregate dynamics, and equilibrium residuals across cohorts.",
        ],
        "objectives": [
            "Write the cohort-stacked Lagrangian for an OLG DEQN.",
            "Train an analytic small-OLG DEQN and verify lifecycle savings against the closed form.",
            "Reproduce the 56-period OLG benchmark with borrowing constraints via Fischer-Burmeister.",
            "Read off lifecycle profiles, aggregate dynamics, and equilibrium residuals across cohorts.",
        ],
    },
    "B08": {
        "opener": "Two complementary methods for stationary distributions in heterogeneous-agent models.",
        "covers": [
            "**Young's (2010) histogram method.** Discretize the individual state, iterate a transition matrix to its fixed point; the workhorse of the discrete-time HA literature.",
            "**Continuum-of-agents DEQN.** Train the policy directly on a simulated cross-section, no histogram step required.",
            "**Aiyagari side-by-side.** Run both methods on the same model and read off the wealth distribution and aggregates.",
            "**When to choose which.** Computational cost, smoothness of the policy, and dimensionality of the individual state.",
            "**Krusell-Smith deep-learning extension.** Han-Yang-E (2023) is provided as further reading.",
        ],
        "objectives": [
            "Iterate Young's histogram method to convergence on Aiyagari and read off the wealth distribution.",
            "Train a continuum-of-agents DEQN and compare its policy against the Young-method solution.",
            "Diagnose when each method is preferable.",
        ],
    },
    "B09": {
        "opener": "Physics-Informed Neural Networks (PINNs) solve differential equations by minimizing the equation residual on collocation points.",
        "covers": [
            "**The PINN loss.** Differentiate the network output with autodiff, plug into the ODE/PDE residual, sum the squared residuals on collocation points.",
            "**Boundary conditions.** Soft (penalty in the loss) versus hard (trial solution that satisfies BCs by construction); when to use each.",
            "**A worked PDE.** A 2-D Poisson PDE solved end-to-end with a PINN.",
            "**Two economic applications.** The cake-eating Hamilton-Jacobi-Bellman equation with hard BCs, and Black-Scholes option pricing.",
            "**Optimization tricks.** Adam-then-L-BFGS schedules and FP64 for sharp PINN solutions.",
        ],
        "objectives": [
            "Write the PINN loss for a given ODE or PDE.",
            "Distinguish soft and hard boundary-condition parametrizations and choose between them.",
            "Solve a 2-D Poisson PDE with a PINN.",
            "Solve the cake-eating HJB with a hard-BC trial solution.",
            "Price a European call option with a Black-Scholes PINN.",
        ],
    },
    "B10": {
        "opener": "The continuous-time heterogeneous-agent system, paired with the master equation that closes it in general equilibrium.",
        "covers": [
            "**The HJB equation.** The individual's value function as a viscosity solution; drift, diffusion, and idiosyncratic shock terms.",
            "**The Kolmogorov forward equation.** Cross-sectional distribution dynamics and the stationary distribution.",
            "**Aiyagari in continuous time.** The canonical example, mapped to its discrete-time analog operator by operator.",
            "**Ito calculus essentials.** What you need from stochastic differential equations to read the rest of the lecture.",
            "**The master equation.** Closing the system in general equilibrium and connecting to the modern continuous-time HA literature.",
        ],
        "objectives": [
            "Write the HJB-KFE system for the Aiyagari model.",
            "Identify each operator's role (drift, diffusion, idiosyncratic shock, distribution update).",
            "State the master equation and its place in the modern HA literature.",
        ],
    },
    "B11": {
        "opener": "Two methods to solve the HJB-KFE system numerically: a finite-difference scheme on a grid, and a PINN.",
        "covers": [
            "**Upwind finite-difference.** The Achdou-Han-Lasry-Lions-Moll scheme for HJB on a state grid, paired with the KFE solver on the same grid.",
            "**Continuous-time Aiyagari.** The running example for both methods.",
            "**A PINN for the coupled system.** Built from scratch; both equations as residual losses on shared collocation points.",
            "**Side-by-side comparison.** Consumption policies and stationary distributions across the two methods.",
            "**Method choice.** When to reach for finite-difference vs PINN as state dimensionality grows.",
        ],
        "objectives": [
            "Implement an upwind finite-difference solver for the Aiyagari HJB-KFE system.",
            "Build a PINN for the coupled HJB-KFE system from scratch.",
            "Compare consumption policies and stationary distributions across the two methods.",
            "Diagnose convergence on each method and choose between them for a new problem.",
        ],
    },
    "B12": {
        "opener": "A toolkit of cheap, differentiable approximations for expensive simulators: deep surrogates, Gaussian processes, active subspaces, and GP value-function iteration.",
        "covers": [
            "**Deep surrogate models.** A neural network trained on simulator input-output pairs; when the surrogate pays for itself over direct simulation.",
            "**Gaussian processes.** GP regression with built-in uncertainty quantification; the basis for Bayesian active learning.",
            "**Bayesian active learning (BAL).** Choose the next training point to maximize information gain rather than throwing samples at a hypercube.",
            "**Active subspaces.** Linear and nonlinear dimension reduction so GPs scale to higher input dimensions.",
            "**Deep kernel learning.** Combining a neural feature map with a GP kernel for the same scaling goal.",
            "**GP value-function iteration.** GPs inside the VFI loop as a competitor to DEQN-VFI.",
        ],
        "objectives": [
            "Train a deep surrogate on a controlled test problem and validate it out-of-sample.",
            "Fit a GP regressor and run a Bayesian active-learning loop.",
            "Apply linear and nonlinear active subspaces to a 10-D test function.",
            "Run GP-VFI on a 2-D test economy and reach a stable value function.",
            "Pick a surrogate vs GP vs deep-kernel approach for a new problem.",
        ],
    },
    "B13": {
        "opener": "Structural estimation by simulated method of moments (SMM), made tractable by replacing the inner-loop model solve with a deep surrogate.",
        "covers": [
            "**SMM in one slide.** The moment-matching condition, the asymptotic distribution of the estimator, and the role of the weighting matrix.",
            "**Surrogate-based estimation.** Why the surrogate makes a brutal repeated re-solve into a cheap optimization.",
            "**Single-parameter Brock-Mirman.** Estimating the productivity persistence rho on a deep surrogate of the model.",
            "**Joint estimation.** Estimating (beta, rho) together; identification diagnostics, Jacobian rank, and asymptotic standard errors.",
            "**Sensitivity to the surrogate.** What happens to the estimator when the surrogate is wrong; switching to a GP for comparison.",
        ],
        "objectives": [
            "State the SMM moment condition and the asymptotic distribution of the estimator.",
            "Run a single-parameter SMM (rho) on a deep surrogate of Brock-Mirman.",
            "Run a joint (beta, rho) SMM and read off identification diagnostics.",
            "Replace the surrogate with a GP and compare estimation behavior.",
        ],
    },
    "B14": {
        "opener": "Integrated assessment models (IAMs), the canonical climate-economy framework: DICE and CDICE.",
        "covers": [
            "**The IAM building blocks.** A macro-growth block, a carbon cycle, temperature dynamics, and a damage function that ties climate back to output.",
            "**DICE and CDICE.** The Nordhaus DICE benchmark and the calibrated CDICE extension (Folini et al. 2024).",
            "**Carbon-cycle simulation.** Business-as-usual and a mitigation scenario; reading off the social cost of carbon.",
            "**Deterministic CDICE-DEQN.** Solve CDICE with a DEQN and verify against the production-code reference.",
            "**Stochastic CDICE-DEQN.** Add AR(1) productivity shocks and use Gauss-Hermite quadrature for the conditional expectations.",
        ],
        "objectives": [
            "Simulate the DICE carbon cycle and temperature dynamics under business-as-usual and a mitigation scenario.",
            "Read off the social cost of carbon and connect IAM building blocks to climate science.",
            "Solve deterministic CDICE with a DEQN and verify against the reference.",
            "Extend to stochastic CDICE with AR(1) productivity shocks.",
        ],
    },
    "B15": {
        "opener": "Stochastic IAMs depend on parameters whose true values are deeply uncertain. Plugging point estimates in, or averaging the uncertainty out, is misleading. This lecture builds a complete pipeline for taking that uncertainty seriously and turning it into a defensible policy menu.",
        "covers": [
            "**The deep-uncertainty problem.** Why equilibrium climate sensitivity, damage curvature, and intertemporal-substitution elasticity cannot be averaged out before optimization.",
            "**Stochastic CDICE-DEQN under Epstein-Zin.** A risk-sensitive recursive-utility solution that respects the tail.",
            "**GP surrogates for the policy outputs.** Bayesian active learning over the uncertain-parameter space.",
            "**Global sensitivity analysis.** Sobol indices and Shapley effects to localize where the policy is actually sensitive.",
            "**Constrained Pareto-improving carbon-tax policies.** Tax paths that, under every realization of the deep uncertainty (or every cohort, or every generation), leave no agent worse off than business-as-usual while strictly improving welfare for at least one. The endpoint is a defensible policy menu rather than a single number.",
        ],
        "objectives": [
            "Run a deep-UQ analysis on a stochastic IAM with Epstein-Zin preferences.",
            "Build a GP surrogate for the policy outputs of a stochastic IAM with Bayesian active learning.",
            "Compute Sobol and Shapley sensitivity indices to localize the policy-relevant uncertainty.",
            "Design constrained Pareto-improving carbon-tax paths and articulate which parameters drive them.",
        ],
    },
    "B16": {
        "opener": "Synthesis of the course: when to choose which method, and where the literature is moving.",
        "covers": [
            "**Method-choice matrix.** DEQN vs PINN vs surrogate-plus-GP vs deep UQ, indexed by state dimensionality, smoothness, presence of constraints, and need for uncertainty quantification.",
            "**The trade-offs.** Compute, sample efficiency, interpretability, and what each method gives up to scale.",
            "**Open frontiers.** Active subspaces in higher dimensions; sequence-space architectures for HA; deep-UQ at the frontier of climate-economic policy.",
            "**Where to go next.** Pointers into the script's bibliography for further self-study.",
        ],
        "objectives": [
            "Articulate when to choose DEQN, PINN, GP, or surrogate methods for a new problem.",
            "Explain the trade-offs each method faces (compute, smoothness, dimensionality, uncertainty quantification).",
            "Identify research frontiers and open problems in computational and quantitative economics.",
        ],
    },
}


def script_ref(entries: list[dict]) -> str:
    parts = [f"§{e['section']} ({e['title']})" for e in entries]
    return ", ".join(parts) if parts else "—"


def list_files(folder_abs: Path, kind: str) -> list[Path]:
    sub = folder_abs / kind
    if not sub.exists():
        return []
    return sorted(p for p in sub.rglob("*") if p.is_file())


def render_links(folder_abs: Path, files: list[Path]) -> str:
    if not files:
        return "_(none)_"
    return "\n".join(
        f"- [`{f.relative_to(folder_abs).as_posix()}`]({f.relative_to(folder_abs).as_posix()})"
        for f in files
    )


def render_bullets(items: list[str]) -> str:
    return "\n".join(f"- {x}" for x in items) if items else "_pending_"


def render_agenda(folder_abs: Path, slides: list[Path], code_files: list[Path],
                  num: str, block: str, script_md: str) -> str:
    """Compact 'at a glance' callout with one-click links to all materials."""
    pdfs = [s for s in slides if s.suffix == ".pdf"]
    notebooks = [c for c in code_files if c.suffix == ".ipynb"]

    if pdfs:
        slides_link = (
            f"[{pdfs[0].name}]({pdfs[0].relative_to(folder_abs).as_posix()})"
            if len(pdfs) == 1
            else f"[{pdfs[0].name}]({pdfs[0].relative_to(folder_abs).as_posix()}) "
                 f"and {len(pdfs) - 1} more under [`slides/`](slides/)"
        )
        slides_part = f"📑 **Slides:** {slides_link}"
    else:
        slides_part = None

    if notebooks:
        first = notebooks[0]
        link = f"[start here]({first.relative_to(folder_abs).as_posix()})"
        if len(notebooks) > 1:
            nb_part = f"📓 **Notebooks:** {link} ({len(notebooks)} in [`code/`](code/))"
        else:
            nb_part = f"📓 **Notebook:** {link}"
    else:
        nb_part = None

    reading_part = (
        f"📚 **Further reading:** "
        f"[curated list](../../readings/links_by_lecture/lecture_{num}_{block}.md)"
    )
    script_part = f"📖 **Script:** {script_md}"

    parts = [p for p in (slides_part, nb_part, reading_part, script_part) if p]
    return "> " + "  \n> ".join(parts)


def render_lecture_readme(lec: dict, lec_index: dict[str, dict]) -> str:
    num = f"{lec['lecture']:02d}"
    block = lec["block"]
    title = lec["title"]
    folder = lec["folder"]
    folder_abs = REPO / folder

    slide_files = list_files(folder_abs, "slides")
    slides = [f for f in slide_files if f.suffix in {".pdf", ".tex"} and f.parent.name == "slides"]
    code_files = list_files(folder_abs, "code")
    figure_files = list_files(folder_abs, "figures")

    if lec["prereqs"]:
        prereq_md = ", ".join(
            f"[Lecture {lec_index[p]['lecture']:02d} ({p})](../{Path(lec_index[p]['folder']).name}/README.md)"
            for p in lec["prereqs"] if p in lec_index
        )
        meta = f"`{lec.get('compute', 'cpu-light')}` · `{lec.get('time', 'standard')}` · builds on {prereq_md}"
    else:
        meta = f"`{lec.get('compute', 'cpu-light')}` · `{lec.get('time', 'standard')}`"

    sorted_lecs = sorted(lec_index.values(), key=lambda x: x["lecture"])
    prev_link = next_link = None
    for i, l in enumerate(sorted_lecs):
        if l["block"] == block:
            if i > 0:
                pl = sorted_lecs[i - 1]
                prev_link = f"← [Previous: {pl['title']}](../{Path(pl['folder']).name}/README.md)"
            if i < len(sorted_lecs) - 1:
                nl = sorted_lecs[i + 1]
                next_link = f"→ [Next: {nl['title']}](../{Path(nl['folder']).name}/README.md)"
            break
    nav = " · ".join([p for p in (prev_link, next_link, "[Course map](../../COURSE_MAP.md)") if p])

    content = CONTENT.get(block, {"opener": "_pending_", "covers": [], "objectives": []})
    script_md = script_ref(lec.get("script") or [])
    agenda = render_agenda(folder_abs, slides, code_files, num, block, script_md)

    sections = [
        f"# Lecture {num} ({block}): {title}",
        "",
        content["opener"],
        "",
        meta,
        "",
        agenda,
        "",
        "## What this lecture covers",
        "",
        render_bullets(content["covers"]),
        "",
        "## Learning objectives",
        "",
        "After this lecture you can:",
        "",
        render_bullets(content["objectives"]),
        "",
        "## Slides",
        "",
        render_links(folder_abs, slides),
        "",
        "## Code",
        "",
        render_links(folder_abs, code_files),
    ]

    if figure_files:
        sections += ["", "## Figures", "", render_links(folder_abs, figure_files)]

    sections += [
        "",
        "## In the lecture script",
        "",
        f"{script_md}. The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).",
        "",
        "## Readings",
        "",
        f"Curated bibliography for this lecture: [`lecture_{num}_{block}.md`](../../readings/links_by_lecture/lecture_{num}_{block}.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).",
        "",
        "---",
        "",
        nav,
        "",
    ]
    return "\n".join(sections)


def main() -> None:
    with open(REPO / "course.yml") as f:
        course = yaml.safe_load(f)
    lec_index = {l["block"]: l for l in course["lectures"]}
    for lec in course["lectures"]:
        out = render_lecture_readme(lec, lec_index)
        path = REPO / lec["folder"] / "README.md"
        path.write_text(out, encoding="utf-8")
        print(f"wrote {path.relative_to(REPO)}")
    print(f"\n{len(course['lectures'])} lectures regenerated.")


if __name__ == "__main__":
    main()
