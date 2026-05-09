# Production, Distribution, and Exchange in Human Societies

This folder is the article-level research package for:

**Production, Distribution, and Exchange in Human Societies**

It is designed as an economist-grade companion workflow for studying the three core processes through which human societies organize material life: production, distribution, and exchange. The workflow emphasizes input-output interdependence, sectoral labor shares, income-claim distribution, exchange networks, trade-dependency scenarios, public-goods provision, ecological throughput, and social reproduction.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — input-output analysis, exchange-network scenarios, distributional metrics, visualization
- **R** — statistical summaries, labor-share analysis, distribution and exchange graphics
- **Stata** — applied economics replication workflows and scenario tables
- **SQL** — structured sector, production, distribution, and exchange metadata
- **Julia** — matrix-based production solving, Leontief inverse analysis, and scenario simulation

## Research Questions

This article companion workflow supports questions such as:

1. How do production sectors depend on one another through input-output linkages?
2. How are total output, labor income, non-labor income, and ecological throughput distributed across sectors?
3. How does a change in final demand or trade exposure ripple through production and income distribution?
4. How do public goods, infrastructure, and care sectors support the wider economic system?
5. How do different exchange scenarios affect output, labor income, import dependence, and resilience?
6. How can Python, R, Stata, SQL, and Julia make production-distribution-exchange assumptions transparent?

## Core Model Ideas

```text
Social product identity:
Y = Σ(Q_i P_i)
```

```text
Production function:
Y = A · F(K, L, E, N)
```

```text
Distribution identity:
Y = W + Π + R + I
```

```text
Input-output system:
x = A x + f
x = (I - A)^(-1)f
```

```text
Labor share:
LS = W / Y
```

## Folder Structure

```text
production-distribution-exchange-human-societies/
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

- `data/processed/production_sectors.csv`
- `data/processed/input_output_matrix.csv`
- `data/processed/final_demand_exchange_scenarios.csv`
- `data/processed/production_distribution_exchange.sqlite`
- `outputs/tables/input_output_distribution_python.csv`
- `outputs/tables/exchange_scenario_results_python.csv`
- `outputs/tables/labor_share_distribution_python.csv`
- `outputs/tables/ecological_throughput_python.csv`
- `outputs/tables/production_distribution_exchange_r_results.csv`
- `outputs/tables/production_distribution_exchange_stata_results.csv`
- `outputs/tables/julia_pde_input_output_results.csv`
- `outputs/figures/sector_output_distribution_python.png`
- `outputs/figures/labor_nonlabor_income_python.png`
- `outputs/figures/exchange_scenarios_python.png`
- `outputs/figures/ecological_throughput_python.png`
- `outputs/figures/production_distribution_exchange_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a calibrated national accounts model, a complete social accounting matrix, or a formal trade model. Its purpose is to make the article's conceptual claims computationally inspectable.
