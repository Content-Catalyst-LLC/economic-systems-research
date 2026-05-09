# Stabilization Policy: Fiscal and Monetary Tools for Managing Economic Fluctuations

This folder is the article-level research package for:

**Stabilization Policy: Fiscal and Monetary Tools for Managing Economic Fluctuations**

It is designed as an economist-grade companion workflow for studying fiscal policy, monetary policy, automatic stabilizers, output gaps, recession response, policy timing, and macroeconomic stabilization.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — public macro data pipelines, stabilization indicators, policy-response metrics, visualization
- **R** — statistical analysis, regression workflows, policy phase summaries, publication graphics
- **Stata** — applied macroeconomics and policy-research replication workflows
- **SQL** — structured policy indicator tables and transparent query layer
- **Julia** — dynamic stabilization simulations and policy-response experiments

## Research Questions

This article companion workflow supports questions such as:

1. How do fiscal and monetary indicators behave during recessions and recoveries?
2. How does the federal funds rate change around output gaps and unemployment increases?
3. How can public spending and government-consumption indicators be compared across cycle phases?
4. What does a simple Taylor-rule-style policy gap reveal about monetary stance?
5. How can automatic-stabilizer proxies be constructed from unemployment and income-support indicators?
6. How do different stabilization-response strengths affect simulated output-gap recovery paths?

## Data Sources

The default workflow uses public FRED CSV endpoints that do not require an API key.

Core series:

| Series | Description |
|---|---|
| `USREC` | NBER-based recession indicator |
| `UNRATE` | Civilian unemployment rate |
| `PAYEMS` | Total nonfarm payroll employment |
| `FEDFUNDS` | Effective federal funds rate |
| `TB3MS` | 3-month Treasury bill rate |
| `CPIAUCSL` | Consumer price index |
| `GDPC1` | Real gross domestic product |
| `GDPPOT` | Real potential gross domestic product |
| `GCEC1` | Real government consumption expenditures and gross investment |

Optional public-finance series are included defensively where available from FRED.

## Folder Structure

```text
stabilization-policy-fiscal-monetary-tools-economic-fluctuations/
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

- `data/processed/stabilization_policy_monthly_panel.csv`
- `data/processed/stabilization_policy_quarterly_panel.csv`
- `data/processed/stabilization_policy.sqlite`
- `outputs/tables/stabilization_phase_summary_python.csv`
- `outputs/tables/policy_response_episode_metrics.csv`
- `outputs/tables/taylor_gap_python_results.csv`
- `outputs/tables/stabilization_r_results.csv`
- `outputs/tables/stabilization_stata_results.csv`
- `outputs/tables/julia_stabilization_simulation.csv`
- `outputs/figures/output_gap_and_fed_funds.png`
- `outputs/figures/unemployment_and_policy_rate.png`
- `outputs/figures/government_spending_growth.png`
- `outputs/figures/taylor_gap_scatter_python.png`
- `outputs/figures/stabilization_phase_scatter_r.png`

## Notes

This is not a policy recommendation engine. It is a reproducible article companion for macroeconomic stabilization analysis, public-data interpretation, and applied economics teaching.
