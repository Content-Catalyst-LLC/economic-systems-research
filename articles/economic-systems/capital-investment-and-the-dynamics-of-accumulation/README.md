# Capital, Investment, and the Dynamics of Accumulation

This folder is the article-level research package for:

**Capital, Investment, and the Dynamics of Accumulation**

It is designed as an economist-grade companion workflow for studying capital stocks, depreciation, investment rates, capital deepening, net present value, public and private discounting, maintenance backlogs, ownership claims, finance direction, accumulation inequality, and sustainable investment scenarios.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — capital accumulation paths, depreciation, NPV, maintenance backlog, ownership-distribution scenarios, sustainable-investment comparisons, visualization
- **R** — capital-stock summaries, maintenance and NPV graphics, public/private investment comparison
- **Stata** — applied economics replication workflows and capital/investment indicator tables
- **SQL** — structured capital stock, investment project, ownership, finance, maintenance, and sustainability metadata
- **Julia** — numerical capital accumulation, NPV, and investment-allocation simulations

## Research Questions

This article companion workflow supports questions such as:

1. How does capital evolve when investment exceeds or falls below depreciation?
2. How does capital intensity affect productive capacity without determining distribution?
3. How do public and private discount rates change project ranking?
4. How does deferred maintenance erode serviceable capital even when headline investment is positive?
5. How do output gains from accumulation split across wages, profits, taxes, and rents?
6. How does finance direction affect whether accumulation is productive, speculative, extractive, or resilient?
7. How do ownership patterns shape future income claims and inequality?
8. How can Python, R, Stata, SQL, and Julia make capital assumptions transparent?

## Core Model Ideas

```text
Capital accumulation:
K_{t+1} = K_t + I_t - δK_t
```

```text
Production:
Y = F(K, L)
```

```text
Capital intensity:
k = K / L
```

```text
Investment rate:
s = I / Y
```

```text
Net present value:
NPV = Σ (R_t - C_t) / (1 + r)^t
```

```text
Distributional split:
Y = W + Π + T + R
```

```text
Maintenance backlog:
M_{b,t+1} = M_{b,t} + N_t - M_t
```

## Folder Structure

```text
capital-investment-and-the-dynamics-of-accumulation/
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

- `data/processed/capital_stock_scenarios.csv`
- `data/processed/investment_project_scenarios.csv`
- `data/processed/maintenance_scenarios.csv`
- `data/processed/ownership_distribution_scenarios.csv`
- `data/processed/finance_direction_scenarios.csv`
- `data/processed/sustainable_investment_scenarios.csv`
- `data/processed/capital_investment_accumulation.sqlite`
- `outputs/tables/capital_accumulation_results_python.csv`
- `outputs/tables/capital_intensity_results_python.csv`
- `outputs/tables/npv_project_results_python.csv`
- `outputs/tables/maintenance_backlog_results_python.csv`
- `outputs/tables/ownership_claims_results_python.csv`
- `outputs/tables/finance_direction_results_python.csv`
- `outputs/tables/sustainable_investment_results_python.csv`
- `outputs/tables/capital_r_results.csv`
- `outputs/tables/capital_stata_results.csv`
- `outputs/tables/julia_capital_results.csv`
- `outputs/figures/capital_stock_paths_python.png`
- `outputs/figures/npv_discount_rate_sensitivity_python.png`
- `outputs/figures/maintenance_backlog_python.png`
- `outputs/figures/ownership_claims_python.png`
- `outputs/figures/finance_direction_python.png`
- `outputs/figures/sustainable_investment_score_python.png`
- `outputs/figures/capital_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a full national-accounts model, infrastructure appraisal, investment-bank valuation model, public-finance model, or integrated assessment model. Its purpose is to make the article's conceptual claims computationally inspectable.
