# What Is an Economic System?

This folder is the article-level research package for:

**What Is an Economic System?**

It is designed as an economist-grade companion workflow for modeling economic systems as institutional, productive, distributive, financial, social, and ecological structures. The workflow emphasizes input-output interdependence, allocation choices, reproduction constraints, distribution metrics, resilience indicators, and sustainability framing.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — input-output analysis, systems indicators, scenario generation, visualization
- **R** — statistical summaries, inequality and distribution metrics, input-output replication
- **Stata** — applied economics replication workflows and systems-indicator tables
- **SQL** — structured sector, institution, allocation, and scenario metadata
- **Julia** — matrix-based input-output solving, reproduction dynamics, and systems simulations

## Research Questions

This article companion workflow supports questions such as:

1. How can an economic system be represented as a structure of sectors, institutions, resource flows, and reproduction constraints?
2. How do final-demand shocks ripple through interdependent sectors?
3. How can production, consumption, investment, public provision, and restoration be represented in an allocation framework?
4. How can distributional outcomes be summarized using wage shares, household income shares, and inequality metrics?
5. How can ecological depletion and regeneration be included in a simplified reproduction model?
6. How can the same conceptual framework be implemented in Python, R, Stata, SQL, and Julia?

## Core Model Ideas

The workflow includes:

```text
Allocation identity:
Y = C + I + G + R
```

```text
Input-output system:
x = A x + f
x = (I - A)^(-1) f
```

```text
Reproduction constraints:
K(t+1) = K(t) + I(t) - δK(t)
N(t+1) = N(t) + regeneration(t) - depletion(t)
```

## Folder Structure

```text
what-is-an-economic-system/
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

- `data/processed/economic_system_sectors.csv`
- `data/processed/input_output_matrix.csv`
- `data/processed/final_demand_scenarios.csv`
- `data/processed/economic_system_results.csv`
- `data/processed/economic_system.sqlite`
- `outputs/tables/input_output_results_python.csv`
- `outputs/tables/allocation_reproduction_metrics_python.csv`
- `outputs/tables/distribution_metrics_python.csv`
- `outputs/tables/economic_system_r_results.csv`
- `outputs/tables/economic_system_stata_results.csv`
- `outputs/tables/julia_input_output_results.csv`
- `outputs/figures/input_output_total_output_python.png`
- `outputs/figures/allocation_profile_python.png`
- `outputs/figures/reproduction_constraints_python.png`
- `outputs/figures/distribution_metrics_r.png`

## Notes

This is a conceptual and computational foundation for the Economic Systems series. It is not a full national accounts model, a complete social accounting matrix, or a calibrated input-output model. It is a reproducible teaching and research scaffold for connecting institutions, production, allocation, distribution, and ecological reproduction.
