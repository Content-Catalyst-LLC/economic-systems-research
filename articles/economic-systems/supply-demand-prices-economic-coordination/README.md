# Supply, Demand, Prices, and Economic Coordination

This folder is the article-level research package for:

**Supply, Demand, Prices, and Economic Coordination**

It is designed as an economist-grade companion workflow for modeling supply, demand, price formation, elasticities, market equilibrium, supply shocks, demand shocks, market power, external costs, missing prices, effective demand, and economic coordination under institutional and ecological constraints.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — equilibrium solving, elasticity calculations, shock scenarios, social-cost pricing, visualization
- **R** — scenario summaries, elasticity diagnostics, supply-demand graphics
- **Stata** — applied economics replication workflows and scenario tables
- **SQL** — structured market, parameter, shock, externality, and access metadata
- **Julia** — fast numerical equilibrium solving, comparative statics, and dynamic adjustment simulations

## Research Questions

This article companion workflow supports questions such as:

1. How do linear supply and demand equations determine equilibrium price and quantity?
2. How do demand shifts, supply shocks, and supply rigidity alter prices and quantities?
3. How do elasticity assumptions change the distribution of adjustment between price and quantity?
4. How do external costs alter the difference between private market price and social cost?
5. How does monetized demand differ from social need when income, credit, and institutional access differ?
6. How do market power and markup assumptions change equilibrium outcomes?
7. How can Python, R, Stata, SQL, and Julia make coordination assumptions transparent?

## Core Model Ideas

```text
Demand:
Q_d = a - bP
```

```text
Supply:
Q_s = c + dP
```

```text
Equilibrium:
P* = (a - c) / (b + d)
Q* = a - bP*
```

```text
Elasticity:
E_d = -b(P / Q_d)
E_s = d(P / Q_s)
```

```text
Social cost:
MSC = MPC + MEC
```

```text
Effective demand:
D_m = f(N, Y, C, A)
```

## Folder Structure

```text
supply-demand-prices-economic-coordination/
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

- `data/processed/market_parameter_scenarios.csv`
- `data/processed/market_access_groups.csv`
- `data/processed/external_cost_scenarios.csv`
- `data/processed/supply_demand_coordination.sqlite`
- `outputs/tables/equilibrium_results_python.csv`
- `outputs/tables/elasticity_results_python.csv`
- `outputs/tables/market_access_metrics_python.csv`
- `outputs/tables/social_cost_results_python.csv`
- `outputs/tables/supply_demand_r_results.csv`
- `outputs/tables/supply_demand_stata_results.csv`
- `outputs/tables/julia_equilibrium_results.csv`
- `outputs/figures/supply_demand_baseline_python.png`
- `outputs/figures/supply_shock_python.png`
- `outputs/figures/demand_shift_python.png`
- `outputs/figures/elasticity_profiles_python.png`
- `outputs/figures/effective_demand_access_python.png`
- `outputs/figures/social_cost_gap_python.png`
- `outputs/figures/supply_demand_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a full industrial organization model, computable general equilibrium model, or calibrated price-system model. Its purpose is to make the article's conceptual claims computationally inspectable.
