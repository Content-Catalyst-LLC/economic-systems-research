# Business Cycles: Economic Expansions, Recessions, and Macroeconomic Stability

This folder is the article-level research package for:

**Business Cycles: Economic Expansions, Recessions, and Macroeconomic Stability**

It is designed as an economist-grade companion workflow for studying expansions, peaks, recessions, troughs, recoveries, trend-cycle decomposition, macroeconomic volatility, and stabilization policy.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — data engineering, FRED pipelines, business-cycle metrics, visualization, reproducible outputs
- **R** — statistical analysis, regression workflows, trend-cycle analysis, charts, replication tables
- **Stata** — applied economics workflows, business-cycle regressions, time-series summaries
- **SQL** — structured-data backbone, transparent query layer, business-cycle episode tables
- **Julia** — dynamic modeling, simulation, macroeconomic cycle models, stabilization experiments

## Research Questions

This article companion workflow supports questions such as:

1. How long do expansions and recessions last?
2. How do output, unemployment, payroll employment, industrial production, retail sales, and income move across cycle phases?
3. How can NBER recession indicators be converted into reproducible business-cycle episode tables?
4. How does actual GDP fluctuate around estimated potential GDP?
5. What does a simple trend-cycle decomposition reveal about macroeconomic stability?
6. How can policy indicators be compared across expansions and recessions?

## Data Sources

The default workflow uses public FRED CSV endpoints that do not require an API key.

Suggested series:

| Series | Description |
|---|---|
| `USREC` | NBER-based recession indicator |
| `UNRATE` | Civilian unemployment rate |
| `PAYEMS` | Total nonfarm payroll employment |
| `INDPRO` | Industrial production index |
| `FEDFUNDS` | Effective federal funds rate |
| `CPIAUCSL` | Consumer price index |
| `RSAFS` | Retail and food services sales |
| `DSPIC96` | Real disposable personal income |
| `GDPC1` | Real gross domestic product |
| `GDPPOT` | Real potential gross domestic product |

## Folder Structure

```text
business-cycles-expansions-recessions-macroeconomic-stability/
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

- `data/processed/business_cycles_monthly_panel.csv`
- `data/processed/business_cycles_quarterly_panel.csv`
- `data/processed/business_cycles.sqlite`
- `outputs/tables/business_cycle_episode_metrics.csv`
- `outputs/tables/phase_summary_python.csv`
- `outputs/tables/cycle_volatility_metrics.csv`
- `outputs/tables/trend_cycle_decomposition.csv`
- `outputs/tables/business_cycle_r_results.csv`
- `outputs/tables/business_cycle_stata_results.csv`
- `outputs/tables/julia_cycle_simulation.csv`
- `outputs/figures/real_gdp_with_recessions.png`
- `outputs/figures/unemployment_with_cycle_phases.png`
- `outputs/figures/output_gap_cycle.png`
- `outputs/figures/trend_cycle_decomposition_python.png`
- `outputs/figures/business_cycle_phase_scatter_r.png`

## Notes

This is not a forecasting system. It is a reproducible article companion for macroeconomic interpretation, business-cycle measurement, stabilization analysis, and applied economics teaching.
