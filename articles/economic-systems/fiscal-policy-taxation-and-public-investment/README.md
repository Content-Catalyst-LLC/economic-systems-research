# Fiscal Policy, Taxation, and Public Investment

This folder is the article-level research package for:

**Fiscal Policy, Taxation, and Public Investment**

It is designed as an economist-grade companion workflow for studying budget balances, tax ratios, debt dynamics, effective tax rates, progressivity, fiscal multipliers, automatic stabilizers, public investment shares, infrastructure maintenance gaps, local fiscal inequality, public investment returns, climate-adaptation investment, and fiscal resilience.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — budget balance, debt dynamics, tax capacity, progressivity, fiscal multipliers, public investment shares, maintenance gaps, local fiscal inequality, resilience investment, visualization
- **R** — fiscal summaries, tax distribution graphics, public investment and maintenance comparisons
- **Stata** — applied public-finance replication workflows and fiscal indicator tables
- **SQL** — structured revenue, spending, tax, debt, maintenance, local-government, public-investment, and resilience-policy metadata
- **Julia** — numerical debt, multiplier, infrastructure backlog, and public-investment return simulations

## Research Questions

This article companion workflow supports questions such as:

1. How do tax revenue and public spending determine budget balance?
2. How do deficits, interest rates, and growth alter public debt dynamics?
3. How large is tax capacity relative to output?
4. How progressive or regressive is a stylized tax structure?
5. How does public investment differ from current expenditure?
6. How do maintenance gaps accumulate as hidden public liabilities?
7. How do fiscal multipliers vary across expenditure types and economic slack?
8. How does local tax-base inequality shape territorial public capacity?
9. How do climate-adaptation and infrastructure investments alter avoided future losses?
10. How can Python, R, Stata, SQL, and Julia make fiscal assumptions transparent?

## Core Model Ideas

```text
Budget balance:
BB = T - G
```

```text
Debt dynamics:
D_{t+1} = D_t + (G_t - T_t) + iD_t
```

```text
Tax-to-output ratio:
τ = T / Y
```

```text
Public investment share:
s_pi = I_p / G
```

```text
Fiscal multiplier:
ΔY = k × ΔG
```

```text
Effective tax rate:
ETR = Tax Paid / Income
```

```text
Maintenance gap:
MG = M_needed - M_actual
```

```text
Avoided-loss return:
ALR = Avoided Future Losses / Public Investment
```

## Folder Structure

```text
fiscal-policy-taxation-and-public-investment/
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

- `data/processed/fiscal_position_scenarios.csv`
- `data/processed/tax_distribution_scenarios.csv`
- `data/processed/spending_composition_scenarios.csv`
- `data/processed/fiscal_multiplier_scenarios.csv`
- `data/processed/infrastructure_maintenance_scenarios.csv`
- `data/processed/local_fiscal_capacity_scenarios.csv`
- `data/processed/public_investment_resilience_scenarios.csv`
- `data/processed/fiscal_policy_taxation_public_investment.sqlite`
- `outputs/tables/fiscal_position_results_python.csv`
- `outputs/tables/tax_distribution_results_python.csv`
- `outputs/tables/spending_composition_results_python.csv`
- `outputs/tables/fiscal_multiplier_results_python.csv`
- `outputs/tables/infrastructure_maintenance_results_python.csv`
- `outputs/tables/local_fiscal_capacity_results_python.csv`
- `outputs/tables/public_investment_resilience_results_python.csv`
- `outputs/tables/fiscal_policy_r_results.csv`
- `outputs/tables/fiscal_policy_stata_results.csv`
- `outputs/tables/julia_fiscal_policy_results.csv`
- `outputs/figures/debt_dynamics_python.png`
- `outputs/figures/tax_progressivity_python.png`
- `outputs/figures/spending_composition_python.png`
- `outputs/figures/fiscal_multipliers_python.png`
- `outputs/figures/maintenance_gap_python.png`
- `outputs/figures/local_fiscal_capacity_python.png`
- `outputs/figures/public_investment_resilience_python.png`
- `outputs/figures/fiscal_policy_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not an official public-finance forecasting system, national budget model, tax microsimulation platform, debt sustainability analysis, or infrastructure finance appraisal system. Its purpose is to make the article's conceptual claims computationally inspectable.
