"""
Mincer wage equation: a tiny end-to-end demo used in the Day 5 lecture.

Illustrates the prompt-to-publication loop:
  * load the `wage1` dataset from the `wooldridge` package
  * run OLS: log(wage) ~ educ + exper + exper^2 + female
  * save a LaTeX regression table to outputs/mincer_table.tex
  * save a publication-ready education vs. log(wage) figure to outputs/mincer_figure.pdf

Verified to run end-to-end on Python 3.11 with statsmodels 0.14+ and wooldridge 0.5+.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import wooldridge as woo

OUTDIR = Path(__file__).parent / "outputs"
OUTDIR.mkdir(exist_ok=True)


def load_data() -> pd.DataFrame:
    df = woo.data("wage1").copy()
    df["exper_sq"] = df["exper"] ** 2
    df["log_wage"] = np.log(df["wage"])
    return df


def fit(df: pd.DataFrame) -> sm.regression.linear_model.RegressionResultsWrapper:
    X = sm.add_constant(df[["educ", "exper", "exper_sq", "female"]])
    y = df["log_wage"]
    return sm.OLS(y, X).fit()


def save_table(res, path: Path) -> None:
    rename = {
        "const": "Constant",
        "educ": "Education (years)",
        "exper": "Experience (years)",
        "exper_sq": r"Experience$^2$",
        "female": "Female",
    }
    coef = res.params.rename(rename)
    se = res.bse.rename(rename)
    tvals = res.tvalues.rename(rename)
    pvals = res.pvalues.rename(rename)

    def star(p: float) -> str:
        return "$^{***}$" if p < 0.01 else "$^{**}$" if p < 0.05 else "$^{*}$" if p < 0.10 else ""

    lines = [
        r"\begin{tabular}{lcccc}",
        r"\toprule",
        r"Variable & Coefficient & Std. Error & $t$-statistic & $p$-value \\",
        r"\midrule",
    ]
    for name in coef.index:
        lines.append(
            f"{name} & {coef[name]:.4f}{star(pvals[name])} & "
            f"({se[name]:.4f}) & {tvals[name]:.2f} & {pvals[name]:.3f} \\\\"
        )
    lines += [
        r"\midrule",
        f"$R^2$ & \\multicolumn{{4}}{{c}}{{{res.rsquared:.4f}}} \\\\",
        f"Adj.\\ $R^2$ & \\multicolumn{{4}}{{c}}{{{res.rsquared_adj:.4f}}} \\\\",
        f"Observations & \\multicolumn{{4}}{{c}}{{{int(res.nobs)}}} \\\\",
        r"\bottomrule",
        r"\end{tabular}",
    ]
    path.write_text("\n".join(lines) + "\n")


def save_figure(df: pd.DataFrame, res, path: Path) -> None:
    plt.rcParams["font.size"] = 13
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(df["educ"], df["log_wage"], alpha=0.25, s=12, color="#355c9e",
               label="Workers")
    edu_grid = np.linspace(df["educ"].min(), df["educ"].max(), 50)
    exper_mean = df["exper"].mean()
    female_mean = df["female"].mean()
    X_pred = sm.add_constant(pd.DataFrame({
        "educ": edu_grid,
        "exper": exper_mean,
        "exper_sq": exper_mean ** 2,
        "female": female_mean,
    }), has_constant="add")
    ax.plot(edu_grid, res.predict(X_pred), color="#990000", lw=2.2,
            label="Fitted (partial)")
    ax.set_xlabel("Years of education")
    ax.set_ylabel(r"$\log(\mathrm{wage})$")
    ax.set_title("Mincer wage equation (CPS 1976)")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def main() -> None:
    df = load_data()
    res = fit(df)
    save_table(res, OUTDIR / "mincer_table.tex")
    save_figure(df, res, OUTDIR / "mincer_figure.pdf")
    print(res.summary().as_text())
    print(f"\nTable  -> {OUTDIR / 'mincer_table.tex'}")
    print(f"Figure -> {OUTDIR / 'mincer_figure.pdf'}")


if __name__ == "__main__":
    main()
