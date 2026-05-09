# Economic Resilience: Why Recessions Occur and How Economies Recover

This folder is the article-level research package for:

**Economic Resilience: Why Recessions Occur and How Economies Recover**

It is designed as an economist-grade companion workflow for recession analysis, recovery measurement, demand shortfalls, labor-market stress, output gaps, and policy stabilization.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — data engineering, public data pipelines, indicator construction, visualization, reproducible outputs
- **R** — statistical analysis, econometrics, graphics, regression summaries, replication tables
- **Stata** — applied economics workflows, regression replication, time-series and policy analysis
- **SQL** — structured-data backbone, transparent query layer, reproducible indicator tables
- **Julia** — dynamic modeling, optimization, simulation, macroeconomic resilience models

## Research Questions

This article companion workflow supports questions such as:

1. How do unemployment, GDP growth, output gaps, industrial production, and monetary conditions behave around recessions?
2. How long does it take output and employment to recover after recession periods?
3. How can recession dating be combined with macroeconomic indicators in a reproducible research workflow?
4. What does an Okun-style relationship between output growth and unemployment changes look like?
5. How can Python, R, Stata, SQL, and Julia provide complementary views of the same economic system?

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
| `GDPC1` | Real gross domestic product |
| `GDPPOT` | Real potential gross domestic product |

## Folder Structure

```text
economic-resilience-recessions-recovery/
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
make julia
make sql
```

Stata is optional and depends on whether Stata is installed locally:

```bash
make stata
```

## Outputs

The workflow creates:

- `data/processed/economic_resilience_monthly_panel.csv`
- `data/processed/economic_resilience_quarterly_panel.csv`
- `data/processed/economic_resilience.sqlite`
- `outputs/tables/recession_episode_metrics.csv`
- `outputs/tables/okun_python_results.csv`
- `outputs/tables/okun_r_results.csv`
- `outputs/tables/julia_dynamic_output_gap_model.csv`
- `outputs/figures/unemployment_with_recessions.png`
- `outputs/figures/output_gap_with_recessions.png`
- `outputs/figures/okun_relationship_python.png`
- `outputs/figures/okun_relationship_r.png`

## Notes

This is not a forecasting system. It is a reproducible article companion for economic interpretation, public-data analysis, recession and recovery measurement, and applied macroeconomic teaching.
