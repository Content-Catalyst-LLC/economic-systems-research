# Finance, Leverage, and Systemic Risk

This folder is the article-level research package for:

**Finance, Leverage, and Systemic Risk**

It is designed as an economist-grade companion workflow for studying leverage amplification, debt-to-equity ratios, equity loss sensitivity, collateral haircuts, margin calls, short-term funding gaps, fire-sale spirals, network contagion, household mortgage leverage, shadow banking exposure, macroprudential buffers, climate/stranded-asset shocks, and sustainable financial resilience.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — leverage amplification, asset-shock scenarios, collateral and haircut stress, fire-sale loops, network contagion, funding gaps, household leverage, sustainable-risk shocks, visualization
- **R** — systemic-risk indicator summaries, leverage and funding-gap graphics, macroprudential scenario comparison
- **Stata** — applied financial-stability replication workflows and leverage/liquidity indicator tables
- **SQL** — structured balance-sheet, funding, collateral, network, household, climate-shock, and macroprudential metadata
- **Julia** — numerical leverage, fire-sale, contagion, and buffer simulations

## Research Questions

This article companion workflow supports questions such as:

1. How does leverage magnify equity losses when asset values fall?
2. How do collateral haircuts and margin calls create funding gaps?
3. How can forced selling generate self-reinforcing fire-sale spirals?
4. How does network interconnection transmit losses across institutions?
5. How do short-term liabilities and liquid assets shape run vulnerability?
6. How does household mortgage leverage transmit systemic stress through housing markets?
7. How do macroprudential buffers reduce amplification?
8. How do climate, stranded-asset, insurance, and infrastructure shocks interact with leverage?
9. How can Python, R, Stata, SQL, and Julia make systemic-risk assumptions transparent?

## Core Model Ideas

```text
Leverage:
Leverage = A / E
```

```text
Debt-to-equity:
D/E = D / E
```

```text
Equity loss amplification:
ΔE / E ≈ -Leverage × x
```

```text
Collateral constraint:
Borrowing ≤ (1 - h) × Collateral Value
```

```text
Fire-sale feedback:
P_{t+1} = P_t - f(Sales_t)
```

```text
Systemic risk:
Risk_system = f(Leverage, Correlation, Interconnectedness, Liquidity Fragility)
```

```text
Funding gap:
FG = ST_liab - LQ_assets
```

## Folder Structure

```text
finance-leverage-and-systemic-risk/
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

- `data/processed/institution_balance_sheets.csv`
- `data/processed/asset_shock_scenarios.csv`
- `data/processed/collateral_haircut_scenarios.csv`
- `data/processed/funding_gap_scenarios.csv`
- `data/processed/network_exposure_matrix.csv`
- `data/processed/household_leverage_scenarios.csv`
- `data/processed/macroprudential_buffer_scenarios.csv`
- `data/processed/sustainability_shock_scenarios.csv`
- `data/processed/finance_leverage_systemic_risk.sqlite`
- `outputs/tables/leverage_amplification_results_python.csv`
- `outputs/tables/collateral_haircut_results_python.csv`
- `outputs/tables/fire_sale_spiral_results_python.csv`
- `outputs/tables/funding_gap_results_python.csv`
- `outputs/tables/network_contagion_results_python.csv`
- `outputs/tables/household_leverage_results_python.csv`
- `outputs/tables/macroprudential_buffer_results_python.csv`
- `outputs/tables/sustainability_shock_results_python.csv`
- `outputs/tables/finance_leverage_r_results.csv`
- `outputs/tables/finance_leverage_stata_results.csv`
- `outputs/tables/julia_finance_leverage_results.csv`
- `outputs/figures/leverage_amplification_python.png`
- `outputs/figures/collateral_haircut_python.png`
- `outputs/figures/fire_sale_spiral_python.png`
- `outputs/figures/funding_gap_python.png`
- `outputs/figures/network_contagion_python.png`
- `outputs/figures/household_leverage_python.png`
- `outputs/figures/macroprudential_buffers_python.png`
- `outputs/figures/sustainability_shock_python.png`
- `outputs/figures/finance_leverage_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a supervisory stress-testing system, bank regulatory capital model, Basel compliance engine, crisis early-warning system, or investment-risk platform. Its purpose is to make the article's conceptual claims computationally inspectable.
