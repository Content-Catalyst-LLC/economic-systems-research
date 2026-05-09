# Households, Firms, Markets, and States

This folder is the article-level research package for:

**Households, Firms, Markets, and States**

It is designed as an economist-grade companion workflow for modeling the four institutional actors that organize modern economic life: households, firms, markets, and states. The workflow emphasizes income flows, household budget constraints, firm profit and investment conditions, state fiscal capacity, market access, effective demand, public goods, risk distribution, and system reproduction.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — institutional flow modeling, scenario construction, reproduction indicators, visualization
- **R** — statistical summaries, distributional access metrics, institutional scenario graphics
- **Stata** — applied economics replication workflows and institutional-flow summaries
- **SQL** — structured actor, flow, scenario, and reproduction metadata
- **Julia** — stock-flow and dynamic reproduction simulations

## Research Questions

This article companion workflow supports questions such as:

1. How do household income, consumption, saving, debt service, and transfers interact?
2. How do firm revenue, labor costs, input costs, capital costs, profits, and investment interact?
3. How do public spending, transfers, taxes, borrowing, and debt service shape state capacity?
4. How do market access, purchasing power, prices, and institutional provision affect effective demand?
5. How are risks distributed across households, firms, markets, and states?
6. What happens to system reproduction when household stability, firm capacity, and state capacity move together?
7. How can Python, R, Stata, SQL, and Julia make institutional economic assumptions transparent?

## Core Model Ideas

```text
Income-flow identity:
Y = C + I + G + NX
```

```text
Household budget:
C_h + S_h + T + D = W + TR + rA
```

```text
Firm profit:
Π = PQ - WL - rK - M
```

```text
State budget:
G + TR + iB = T + ΔB
```

```text
Reproduction condition:
R_s = f(H, P, I)
```

## Folder Structure

```text
households-firms-markets-and-states/
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

- `data/processed/institutional_actors.csv`
- `data/processed/institutional_flow_scenarios.csv`
- `data/processed/market_access_scenarios.csv`
- `data/processed/risk_distribution_scenarios.csv`
- `data/processed/households_firms_markets_states.sqlite`
- `outputs/tables/institutional_flow_results_python.csv`
- `outputs/tables/market_access_metrics_python.csv`
- `outputs/tables/risk_reproduction_metrics_python.csv`
- `outputs/tables/hfms_r_results.csv`
- `outputs/tables/hfms_stata_results.csv`
- `outputs/tables/julia_reproduction_dynamics.csv`
- `outputs/figures/institutional_flow_balances_python.png`
- `outputs/figures/market_access_python.png`
- `outputs/figures/risk_distribution_python.png`
- `outputs/figures/reproduction_capacity_paths_python.png`
- `outputs/figures/hfms_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a complete stock-flow consistent macroeconomic model, computable general equilibrium model, or calibrated national accounts framework. Its purpose is to make the article's conceptual claims computationally inspectable.
