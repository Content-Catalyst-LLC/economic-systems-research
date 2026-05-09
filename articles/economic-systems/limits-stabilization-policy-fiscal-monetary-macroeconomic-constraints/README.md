# Limits of Stabilization Policy: Fiscal Policy, Monetary Policy, and Macroeconomic Constraints

This folder is the article-level research package for:

**Limits of Stabilization Policy: Fiscal Policy, Monetary Policy, and Macroeconomic Constraints**

It is designed as an economist-grade companion workflow for studying the constraints that limit fiscal and monetary stabilization: inflation pressure, debt sustainability, interest-rate constraints, crowding-out risk, policy lags, liquidity traps, supply constraints, and fiscal-space limits.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — public macro data pipelines, fiscal/monetary constraint indicators, figures, reproducible tables
- **R** — statistical analysis, regression workflows, constraint summaries, publication graphics
- **Stata** — applied macroeconomics and policy-research replication workflows
- **SQL** — structured constraint-indicator tables and transparent query layer
- **Julia** — debt-dynamics and policy-constraint simulations

## Research Questions

This article companion workflow supports questions such as:

1. When might fiscal stimulus be constrained by inflation, public debt, or interest-rate conditions?
2. When might monetary policy be constrained by the zero lower bound, inflation risk, or weak transmission?
3. How do output gaps, inflation, unemployment, policy rates, and debt ratios interact across cycle phases?
4. How can a simple debt-stabilizing primary-balance condition be calculated from growth, interest rates, and debt ratios?
5. How can a crowding-out proxy be constructed from long-term interest rates, debt ratios, and output gaps?
6. How do different interest-growth and fiscal-response assumptions affect simulated debt paths?

## Data Sources

The default workflow uses public FRED CSV endpoints that do not require an API key.

Core series:

| Series | Description |
|---|---|
| `USREC` | NBER-based recession indicator |
| `UNRATE` | Civilian unemployment rate |
| `FEDFUNDS` | Effective federal funds rate |
| `TB3MS` | 3-month Treasury bill rate |
| `GS10` | 10-year Treasury constant maturity rate |
| `CPIAUCSL` | Consumer price index |
| `GDPC1` | Real gross domestic product |
| `GDPPOT` | Real potential gross domestic product |
| `GFDEGDQ188S` | Federal debt as percent of GDP |

## Folder Structure

```text
limits-stabilization-policy-fiscal-monetary-macroeconomic-constraints/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
├── outputs/
│   ├── figures/
│   └── tables/
├── python/
├── r/
├── stata/
├── sql/
├── julia/
├── metadata/
├── Makefile
├── requirements.txt
└── README.md
```

## Recommended Workflow

From this article folder:

```bash
make python
make r
make sql
make julia
```

Stata is optional and depends on whether Stata is installed locally:

```bash
make stata
```

## Outputs

The workflow creates:

- `data/processed/stabilization_constraints_monthly_panel.csv`
- `data/processed/stabilization_constraints_quarterly_panel.csv`
- `data/processed/stabilization_constraints.sqlite`
- `outputs/tables/constraint_phase_summary_python.csv`
- `outputs/tables/fiscal_space_constraint_metrics.csv`
- `outputs/tables/debt_stabilizing_balance_python.csv`
- `outputs/tables/monetary_constraint_python_results.csv`
- `outputs/tables/constraints_r_results.csv`
- `outputs/tables/constraints_stata_results.csv`
- `outputs/tables/julia_debt_dynamics_simulation.csv`
- `outputs/figures/inflation_output_gap_constraints.png`
- `outputs/figures/debt_ratio_and_interest_growth_gap.png`
- `outputs/figures/policy_rate_lower_bound_context.png`
- `outputs/figures/crowding_out_proxy_python.png`
- `outputs/figures/constraint_phase_scatter_r.png`

## Notes

This is not a fiscal-sustainability certification model or a monetary-policy recommendation engine. It is a reproducible article companion for analyzing the limits, trade-offs, and constraints that shape stabilization policy.
