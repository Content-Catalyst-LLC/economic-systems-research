# Macroeconomic Stability, Business Cycles, and Crisis

This folder is the article-level research package for:

**Macroeconomic Stability, Business Cycles, and Crisis**

It is designed as an economist-grade companion workflow for studying aggregate demand, output gaps, business-cycle phases, investment expectations, credit cycles, balance-sheet contraction, debt deflation, fiscal multipliers, automatic stabilizers, Okun-style unemployment response, inflation pressure, open-economy shocks, macroeconomic resilience, and crisis recovery paths.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — aggregate demand accounting, output gaps, fiscal multipliers, Okun-style unemployment response, debt-service burden, credit contraction, balance-sheet recession scenarios, open-economy shocks, visualization
- **R** — macro indicator summaries, business-cycle phase graphics, fiscal-stabilization and household-security scenarios
- **Stata** — applied macroeconomics replication workflows and stabilization indicator tables
- **SQL** — structured macro demand, household, credit, policy, inflation, external shock, and crisis-recovery metadata
- **Julia** — numerical business-cycle, multiplier, debt-deflation, and recovery-path simulations

## Research Questions

This article companion workflow supports questions such as:

1. How do consumption, investment, government spending, and net exports shape output?
2. How does an output gap indicate underused or overheated capacity?
3. How do falling income, weaker expectations, and investment retrenchment amplify downturns?
4. How do household debt-service burdens turn slowdown into balance-sheet stress?
5. How do fiscal multipliers and automatic stabilizers alter recession paths?
6. How does Okun-style logic connect weak output growth to rising unemployment?
7. How can credit contraction and debt deflation create cumulative downturns?
8. How do open-economy shocks transmit through exports, import prices, rates, and capital flows?
9. How can Python, R, Stata, SQL, and Julia make macroeconomic stabilization assumptions transparent?

## Core Model Ideas

```text
National income identity:
Y = C + I + G + NX
```

```text
Output gap:
Gap = (Y - Y*) / Y*
```

```text
Consumption function:
C = a + bY_d
```

```text
Fiscal multiplier:
ΔY = k × ΔG
```

```text
Debt-service burden:
DBR = Debt Service / Income
```

```text
Debt-deflation pressure:
Real Debt Burden = Nominal Debt / Price Level
```

```text
Okun-style relation:
Δu ≈ -β(g - g*)
```

```text
Resilience score:
R = f(automatic stabilizers, fiscal space, household buffers, financial resilience, public capacity)
```

## Folder Structure

```text
macroeconomic-stability-business-cycles-and-crisis/
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

- `data/processed/aggregate_demand_scenarios.csv`
- `data/processed/business_cycle_phase_scenarios.csv`
- `data/processed/household_balance_sheet_scenarios.csv`
- `data/processed/credit_contraction_scenarios.csv`
- `data/processed/fiscal_stabilization_scenarios.csv`
- `data/processed/open_economy_shock_scenarios.csv`
- `data/processed/inflation_unemployment_policy_scenarios.csv`
- `data/processed/crisis_recovery_path_scenarios.csv`
- `data/processed/macroeconomic_stability_business_cycles_crisis.sqlite`
- `outputs/tables/aggregate_demand_results_python.csv`
- `outputs/tables/business_cycle_phase_results_python.csv`
- `outputs/tables/household_balance_sheet_results_python.csv`
- `outputs/tables/credit_contraction_results_python.csv`
- `outputs/tables/fiscal_stabilization_results_python.csv`
- `outputs/tables/open_economy_shock_results_python.csv`
- `outputs/tables/inflation_unemployment_results_python.csv`
- `outputs/tables/crisis_recovery_results_python.csv`
- `outputs/tables/macro_stability_r_results.csv`
- `outputs/tables/macro_stability_stata_results.csv`
- `outputs/tables/julia_macro_stability_results.csv`
- `outputs/figures/aggregate_demand_components_python.png`
- `outputs/figures/output_gap_python.png`
- `outputs/figures/household_balance_sheet_stress_python.png`
- `outputs/figures/credit_contraction_python.png`
- `outputs/figures/fiscal_stabilization_python.png`
- `outputs/figures/open_economy_shock_python.png`
- `outputs/figures/inflation_unemployment_policy_python.png`
- `outputs/figures/crisis_recovery_paths_python.png`
- `outputs/figures/macro_stability_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a central-bank forecasting model, DSGE model, national-accounts production system, fiscal authority model, or crisis early-warning system. Its purpose is to make the article's conceptual claims computationally inspectable.
