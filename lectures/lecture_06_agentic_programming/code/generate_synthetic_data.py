"""
Generate synthetic panel data for Day 5 exercises.

Creates a balanced panel of 500 firms x 10 years (2010-2019) with:
  - Firm fixed effects (persistent heterogeneity)
  - A difference-in-differences structure:
      40% of firms are "treated", treatment begins in 2015
  - True treatment effect on log(revenue) = 0.05
  - Realistic log-normal revenue and integer employee counts

Output: data/synthetic_panel.csv

Usage:
    python generate_synthetic_data.py
"""

import os
import numpy as np

# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------
N_FIRMS = 500
YEARS = list(range(2010, 2020))  # 2010-2019 inclusive
N_YEARS = len(YEARS)
TREATMENT_SHARE = 0.40           # 40% of firms are treated
TREATMENT_START = 2015           # Post period begins in 2015
TRUE_EFFECT = 0.05               # True ATT on log(revenue)
NOISE_SD = 0.30                  # Idiosyncratic noise std dev
SEED = 20260331                  # Reproducible

# ---------------------------------------------------------------------------
# Set seed for reproducibility
# ---------------------------------------------------------------------------
rng = np.random.default_rng(SEED)

# ---------------------------------------------------------------------------
# Build panel indices
# ---------------------------------------------------------------------------
firm_ids = np.repeat(np.arange(1, N_FIRMS + 1), N_YEARS)
years = np.tile(YEARS, N_FIRMS)
n_obs = len(firm_ids)

# ---------------------------------------------------------------------------
# Treatment assignment (firm-level, time-invariant)
# ---------------------------------------------------------------------------
n_treated = int(N_FIRMS * TREATMENT_SHARE)
treated_firms = np.zeros(N_FIRMS, dtype=int)
treated_firms[:n_treated] = 1
rng.shuffle(treated_firms)

# Expand to panel level
treated = np.repeat(treated_firms, N_YEARS)

# Post-treatment indicator
post = (years >= TREATMENT_START).astype(int)

# ---------------------------------------------------------------------------
# Firm fixed effects
# ---------------------------------------------------------------------------
# Each firm has a persistent "quality" level drawn once.
# This creates realistic cross-sectional heterogeneity in revenue.
firm_fe = rng.normal(loc=0.0, scale=0.5, size=N_FIRMS)
firm_fe_expanded = np.repeat(firm_fe, N_YEARS)

# ---------------------------------------------------------------------------
# Year effects (common macro trend)
# ---------------------------------------------------------------------------
# Slight upward trend with a dip around 2012 (stylized recession echo)
year_effects = {
    2010: -0.02,
    2011:  0.00,
    2012: -0.03,
    2013:  0.01,
    2014:  0.02,
    2015:  0.03,
    2016:  0.04,
    2017:  0.05,
    2018:  0.04,
    2019:  0.03,
}
year_fe = np.array([year_effects[y] for y in years])

# ---------------------------------------------------------------------------
# Generate log(revenue)
# ---------------------------------------------------------------------------
# Data-generating process:
#   log(revenue_it) = 3.5 + firm_fe_i + year_fe_t
#                     + TRUE_EFFECT * treated_i * post_t
#                     + epsilon_it
#
# The intercept 3.5 puts revenue in a plausible range after exponentiation.
# ---------------------------------------------------------------------------
log_revenue = (
    3.5
    + firm_fe_expanded
    + year_fe
    + TRUE_EFFECT * treated * post
    + rng.normal(loc=0.0, scale=NOISE_SD, size=n_obs)
)

# Exponentiate to get revenue in levels (millions of USD, roughly)
revenue = np.exp(log_revenue)

# ---------------------------------------------------------------------------
# Generate employees (correlated with firm quality)
# ---------------------------------------------------------------------------
# Base employee count correlates with firm FE (larger firms = more employees)
log_employees = (
    4.0
    + 0.8 * firm_fe_expanded
    + 0.02 * (years - 2010)  # slight growth over time
    + rng.normal(loc=0.0, scale=0.3, size=n_obs)
)
employees = np.maximum(np.round(np.exp(log_employees)).astype(int), 1)

# ---------------------------------------------------------------------------
# Assemble and save
# ---------------------------------------------------------------------------
# Build a structured array, then save as CSV with a header line.
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "synthetic_panel.csv")

# Create header and data matrix
header = "firm_id,year,revenue,employees,treated,post"
data = np.column_stack([
    firm_ids,
    years,
    np.round(revenue, 4),
    employees,
    treated,
    post,
])

np.savetxt(output_path, data, delimiter=",", header=header,
           comments="", fmt=["%d", "%d", "%.4f", "%d", "%d", "%d"])

print(f"Saved {n_obs} observations to {output_path}")
print(f"  Firms:   {N_FIRMS}")
print(f"  Years:   {YEARS[0]}--{YEARS[-1]}")
print(f"  Treated: {n_treated} firms ({TREATMENT_SHARE*100:.0f}%)")
print(f"  True effect on log(revenue): {TRUE_EFFECT}")
print()

# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------
print("=" * 60)
print("Summary Statistics")
print("=" * 60)

for var_name, var_data in [("revenue", revenue), ("employees", employees.astype(float))]:
    print(f"\n{var_name}:")
    print(f"  mean   = {np.mean(var_data):12.2f}")
    print(f"  std    = {np.std(var_data):12.2f}")
    print(f"  min    = {np.min(var_data):12.2f}")
    print(f"  p25    = {np.percentile(var_data, 25):12.2f}")
    print(f"  median = {np.median(var_data):12.2f}")
    print(f"  p75    = {np.percentile(var_data, 75):12.2f}")
    print(f"  max    = {np.max(var_data):12.2f}")

print(f"\nlog(revenue):")
print(f"  mean   = {np.mean(log_revenue):12.4f}")
print(f"  std    = {np.std(log_revenue):12.4f}")

# Treatment group means (post-period only)
post_mask = post == 1
treated_post = log_revenue[(treated == 1) & post_mask]
control_post = log_revenue[(treated == 0) & post_mask]
treated_pre = log_revenue[(treated == 1) & ~post_mask]
control_pre = log_revenue[(treated == 0) & ~post_mask]

print(f"\nDifference-in-Differences (raw, on log revenue):")
print(f"  Treated post mean:  {np.mean(treated_post):.4f}")
print(f"  Control post mean:  {np.mean(control_post):.4f}")
print(f"  Treated pre mean:   {np.mean(treated_pre):.4f}")
print(f"  Control pre mean:   {np.mean(control_pre):.4f}")
raw_did = (np.mean(treated_post) - np.mean(control_post)) - \
          (np.mean(treated_pre) - np.mean(control_pre))
print(f"  Raw DiD estimate:   {raw_did:.4f}  (true = {TRUE_EFFECT})")
