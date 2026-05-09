# Scarcity, Allocation, and the Organization of Material Life

This folder is the article-level research package for:

**Scarcity, Allocation, and the Organization of Material Life**

It is designed as an economist-grade companion workflow for modeling scarcity as a social, institutional, ecological, and intertemporal allocation problem. The workflow emphasizes public-priority trade-offs, effective access, distribution-weighted welfare, ecological regeneration constraints, maintenance, depreciation, and future capacity.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — allocation scenario modeling, constraint analysis, effective-access metrics, visualization
- **R** — statistical summaries, distribution-weighted allocation analysis, scenario graphics
- **Stata** — applied economics replication workflows and allocation tables
- **SQL** — structured scenario metadata, sector priorities, constraints, and reproducible queries
- **Julia** — constrained allocation, intertemporal capacity, and regeneration/depletion simulations

## Research Questions

This article companion workflow supports questions such as:

1. How can scarcity be represented as more than a simple shortage of resources?
2. How do allocation choices shift resources across housing, health, education, infrastructure, energy, care, and ecological restoration?
3. How does effective access depend on need, income, price, and institutional provision?
4. How do present consumption, investment, maintenance, and restoration shape future capacity?
5. When does ecological use exceed regenerative capacity?
6. How can distribution-weighted welfare alter the evaluation of allocation choices?
7. How can Python, R, Stata, SQL, and Julia make scarcity and allocation assumptions transparent?

## Core Model Ideas

```text
Scarcity constraint:
R < D
```

```text
Allocation constraint:
x_1 + x_2 + ... + x_n <= R
```

```text
Intertemporal allocation:
R_t = C_t + I_t + M_t + E_t
```

```text
Ecological regeneration:
U_t <= G_t
```

```text
Effective access:
A_e = f(N, Y, P, I)
```

## Folder Structure

```text
scarcity-allocation-organization-material-life/
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

- `data/processed/allocation_priorities.csv`
- `data/processed/allocation_scenarios.csv`
- `data/processed/access_households.csv`
- `data/processed/reproduction_constraints.csv`
- `data/processed/scarcity_allocation.sqlite`
- `outputs/tables/allocation_results_python.csv`
- `outputs/tables/effective_access_metrics_python.csv`
- `outputs/tables/intertemporal_reproduction_python.csv`
- `outputs/tables/scarcity_allocation_r_results.csv`
- `outputs/tables/scarcity_allocation_stata_results.csv`
- `outputs/tables/julia_allocation_results.csv`
- `outputs/figures/allocation_scenarios_python.png`
- `outputs/figures/effective_access_python.png`
- `outputs/figures/ecological_regeneration_constraint_python.png`
- `outputs/figures/intertemporal_capacity_paths_python.png`
- `outputs/figures/scarcity_allocation_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a full public-finance model, national-planning tool, or calibrated ecological-economic model. Its purpose is to make the article's conceptual claims computationally inspectable.
