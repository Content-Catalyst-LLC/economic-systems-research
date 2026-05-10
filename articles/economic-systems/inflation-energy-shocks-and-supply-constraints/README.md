# Inflation, Energy Shocks, and Supply Constraints

This folder is the article-level research package for:

**Inflation, Energy Shocks, and Supply Constraints**

It is designed as an economist-grade companion workflow for studying inflation rates, energy cost pass-through, real wage erosion, household energy burden, import-price transmission, supply bottlenecks, exchange-rate exposure, market-power amplification, energy poverty, public stabilization, and resilience-oriented anti-inflation strategy.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — inflation indices, energy pass-through, real wages, household energy burden, supply bottlenecks, import-price shocks, market-power amplification, resilience policy scenarios, visualization
- **R** — inflation and burden summaries, sector pass-through graphics, household burden and resilience comparisons
- **Stata** — applied macroeconomic replication workflows and inflation/supply-shock indicator tables
- **SQL** — structured price index, energy, household, sector, supply-chain, import, market-power, and policy-resilience metadata
- **Julia** — numerical inflation pass-through, supply-constraint, bottleneck, and resilience-policy simulations

## Research Questions

This article companion workflow supports questions such as:

1. How is inflation calculated from price levels over time?
2. How do energy-cost shocks pass through into sector prices?
3. How do price increases alter real wages and household purchasing power?
4. How does household energy burden differ across income groups?
5. How do import prices respond to world-price shocks and exchange-rate movements?
6. How do supply bottlenecks constrain output and raise prices?
7. How can market concentration amplify cost pass-through?
8. How do public policy, strategic reserves, energy investment, and infrastructure resilience reduce future inflation vulnerability?
9. How can Python, R, Stata, SQL, and Julia make inflation and supply-shock assumptions transparent?

## Core Model Ideas

```text
Inflation:
π = (P_t - P_{t-1}) / P_{t-1}
```

```text
Energy pass-through:
ΔP = αΔE + βΔW + γΔM
```

```text
Real wage:
w_r = w_n / P
```

```text
Supply constraint:
Y ≤ min(K, L, E, S)
```

```text
Household energy burden:
HEB = Energy Spending / Household Income
```

```text
Import price transmission:
ΔP_m = ΔP_world + ΔER
```

```text
Resilience-adjusted inflation pressure:
π_resilience = f(energy dependence, import exposure, bottleneck severity, market power, public buffers)
```

## Folder Structure

```text
inflation-energy-shocks-and-supply-constraints/
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

- `data/processed/price_index_scenarios.csv`
- `data/processed/sector_energy_pass_through_scenarios.csv`
- `data/processed/household_energy_burden_scenarios.csv`
- `data/processed/import_price_transmission_scenarios.csv`
- `data/processed/supply_bottleneck_scenarios.csv`
- `data/processed/market_power_price_amplification_scenarios.csv`
- `data/processed/resilience_policy_scenarios.csv`
- `data/processed/inflation_energy_shocks_supply_constraints.sqlite`
- `outputs/tables/inflation_results_python.csv`
- `outputs/tables/energy_pass_through_results_python.csv`
- `outputs/tables/household_energy_burden_results_python.csv`
- `outputs/tables/import_price_transmission_results_python.csv`
- `outputs/tables/supply_bottleneck_results_python.csv`
- `outputs/tables/market_power_results_python.csv`
- `outputs/tables/resilience_policy_results_python.csv`
- `outputs/tables/inflation_energy_r_results.csv`
- `outputs/tables/inflation_energy_stata_results.csv`
- `outputs/tables/julia_inflation_energy_results.csv`
- `outputs/figures/inflation_paths_python.png`
- `outputs/figures/energy_pass_through_python.png`
- `outputs/figures/household_energy_burden_python.png`
- `outputs/figures/import_price_transmission_python.png`
- `outputs/figures/supply_bottleneck_python.png`
- `outputs/figures/market_power_amplification_python.png`
- `outputs/figures/resilience_policy_python.png`
- `outputs/figures/inflation_energy_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a central-bank forecasting system, CPI production model, official national-statistics workflow, energy-market model, or supply-chain risk platform. Its purpose is to make the article's conceptual claims computationally inspectable.
