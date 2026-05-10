# Growth, Development, and Structural Transformation

This folder is the article-level research package for:

**Growth, Development, and Structural Transformation**

It is designed as an economist-grade companion workflow for studying output growth, labor productivity, sectoral shares, employment reallocation, structural-change decomposition, development capability, infrastructure depth, urbanization, export diversification, inequality, energy intensity, middle-income fragility, debt exposure, and sustainable development pathways.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — growth rates, labor productivity, sectoral output and labor shares, structural-change decomposition, development capability indices, inequality and energy-intensity diagnostics, visualization
- **R** — development-path summaries, productivity and sectoral transformation graphics, capability and distribution comparisons
- **Stata** — applied development-economics replication workflows and indicator tables
- **SQL** — structured output, labor, sector, infrastructure, education, trade, inequality, energy, finance, and development-path metadata
- **Julia** — numerical simulations for productivity upgrading, labor reallocation, middle-income fragility, and sustainable transformation pathways

## Research Questions

1. How do growth rates differ from development outcomes?
2. How does labor productivity change across sectors?
3. How do sectoral output and labor shares reveal structural transformation?
4. How much growth comes from within-sector productivity versus labor reallocation?
5. How do education, health, infrastructure, security, and income combine into capability?
6. How do urbanization and infrastructure affect development capacity?
7. How does export concentration create developmental fragility?
8. How do inequality and exclusion weaken developmental durability?
9. How do energy intensity and emissions alter the meaning of growth?
10. How do debt exposure and external dependence constrain developmental sovereignty?
11. How can Python, R, Stata, SQL, and Julia make development assumptions transparent?

## Core Model Ideas

```text
Growth rate:
g = (Y_t - Y_{t-1}) / Y_{t-1}
```

```text
Labor productivity:
LP = Y / L
```

```text
Sectoral output share:
s_i = Y_i / Y
```

```text
Sectoral employment share:
e_i = L_i / L
```

```text
Structural-change contribution:
ΔY = Σ(ΔLP_i × L_i) + Σ(ΔL_i × LP_i)
```

```text
Capability index:
D = f(income, health, education, infrastructure, security)
```

```text
Energy intensity:
EI = Energy Use / Output
```

```text
Developmental fragility:
F = f(export concentration, debt exposure, inequality, energy dependence, infrastructure gaps)
```

## Folder Structure

```text
growth-development-and-structural-transformation/
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

- `data/processed/growth_path_scenarios.csv`
- `data/processed/sector_transformation_scenarios.csv`
- `data/processed/development_capability_scenarios.csv`
- `data/processed/urban_infrastructure_scenarios.csv`
- `data/processed/trade_export_diversification_scenarios.csv`
- `data/processed/inequality_inclusion_scenarios.csv`
- `data/processed/energy_ecology_scenarios.csv`
- `data/processed/debt_fragility_scenarios.csv`
- `data/processed/growth_development_structural_transformation.sqlite`
- `outputs/tables/growth_results_python.csv`
- `outputs/tables/sector_transformation_results_python.csv`
- `outputs/tables/development_capability_results_python.csv`
- `outputs/tables/urban_infrastructure_results_python.csv`
- `outputs/tables/trade_diversification_results_python.csv`
- `outputs/tables/inequality_inclusion_results_python.csv`
- `outputs/tables/energy_ecology_results_python.csv`
- `outputs/tables/debt_fragility_results_python.csv`
- `outputs/tables/development_r_results.csv`
- `outputs/tables/development_stata_results.csv`
- `outputs/tables/julia_development_results.csv`
- `outputs/figures/growth_paths_python.png`
- `outputs/figures/sectoral_output_shares_python.png`
- `outputs/figures/sectoral_labor_productivity_python.png`
- `outputs/figures/development_capability_python.png`
- `outputs/figures/urban_infrastructure_python.png`
- `outputs/figures/export_concentration_python.png`
- `outputs/figures/inequality_inclusion_python.png`
- `outputs/figures/energy_intensity_python.png`
- `outputs/figures/development_fragility_python.png`
- `outputs/figures/development_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not an official national-accounts system, growth-accounting production database, econometric development model, debt sustainability analysis, or policy-forecasting tool. Its purpose is to make the article's conceptual claims computationally inspectable.
