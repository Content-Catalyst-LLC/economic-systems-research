# Consumer Choice, Household Welfare, and Everyday Economic Life

This folder is the article-level research package for:

**Consumer Choice, Household Welfare, and Everyday Economic Life**

It is designed as an economist-grade companion workflow for modeling household choice, budget constraints, essentials burdens, debt service, time scarcity, public provision, household fragility, effective access, and welfare beyond narrow consumption expenditure.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — household budget modeling, welfare indicators, fragility analysis, inflation scenarios, visualization
- **R** — household welfare summaries, essentials-burden analysis, time-poverty metrics, scenario graphics
- **Stata** — applied economics replication workflows and household-indicator tables
- **SQL** — structured household, expense, access, public-good, and scenario metadata
- **Julia** — dynamic household balance-sheet, asset-depletion, and welfare-resilience simulations

## Research Questions

This article companion workflow supports questions such as:

1. How do household income, transfers, debt service, liquid assets, and fixed burdens shape feasible choice?
2. How do essentials burdens change under rent, food, energy, transport, and health-cost inflation?
3. How does household welfare change when public goods reduce private expenses or time burdens?
4. How does time poverty interact with monetary budgets, care work, commuting, and rest?
5. How quickly do households deplete buffers under price shocks or income shocks?
6. How do different household groups experience effective access to essentials?
7. How can Python, R, Stata, SQL, and Julia make household welfare assumptions transparent?

## Core Model Ideas

```text
Household budget constraint:
Σ p_i x_i + S = Y + TR + A_l - D - B
```

```text
Utility under constraint:
max U(x_1, x_2, ..., x_n)
subject to Σ p_i x_i ≤ Y - D
```

```text
Broader welfare:
W = f(C, T, H, A, P, R)
```

```text
Effective access to essentials:
E = (Y + TR + A_l - D) / P_e
```

```text
Time constraint:
24 = L + C_r + T_h + R
```

```text
Fragility ratio:
F = (P_e + D + B) / (Y + TR + A_l)
```

## Folder Structure

```text
consumer-choice-household-welfare-everyday-economic-life/
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

- `data/processed/household_profiles.csv`
- `data/processed/expense_categories.csv`
- `data/processed/inflation_scenarios.csv`
- `data/processed/public_goods_scenarios.csv`
- `data/processed/consumer_choice_household_welfare.sqlite`
- `outputs/tables/household_budget_results_python.csv`
- `outputs/tables/essentials_fragility_results_python.csv`
- `outputs/tables/time_poverty_results_python.csv`
- `outputs/tables/public_goods_welfare_results_python.csv`
- `outputs/tables/consumer_choice_r_results.csv`
- `outputs/tables/consumer_choice_stata_results.csv`
- `outputs/tables/julia_household_resilience_results.csv`
- `outputs/figures/essentials_burden_python.png`
- `outputs/figures/fragility_ratio_python.png`
- `outputs/figures/time_poverty_python.png`
- `outputs/figures/public_goods_welfare_python.png`
- `outputs/figures/asset_depletion_paths_python.png`
- `outputs/figures/consumer_choice_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a full household microsimulation model, consumer demand system, or calibrated welfare model. Its purpose is to make the article's conceptual claims computationally inspectable.
