# Money, Banking, Credit, and Financial Intermediation

This folder is the article-level research package for:

**Money, Banking, Credit, and Financial Intermediation**

It is designed as an economist-grade companion workflow for studying money aggregates, bank balance sheets, deposit creation, leverage, loan-to-deposit ratios, liquidity coverage, credit allocation, household and firm debt stress, shadow banking, collateral hierarchy, financial fragility, and sustainable finance direction.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — money aggregates, bank balance-sheet expansion, leverage, LDR, ICR, LCR, liquidity shocks, credit allocation, sustainable-finance scoring, visualization
- **R** — banking indicator summaries, credit allocation graphics, debt-service and liquidity resilience analysis
- **Stata** — applied financial-economics replication workflows and banking/credit indicator tables
- **SQL** — structured money, bank balance-sheet, debt-service, liquidity, credit-allocation, and sustainable-finance metadata
- **Julia** — numerical balance-sheet, credit-cycle, liquidity-stress, and financial-resilience simulations

## Research Questions

This article companion workflow supports questions such as:

1. How do currency and deposits form a simple money aggregate?
2. How does bank lending expand both assets and deposit liabilities?
3. How do leverage and loan-to-deposit ratios change under credit expansion?
4. How does liquidity coverage change under withdrawal and funding-stress scenarios?
5. How do interest coverage and debt-service burdens differ across households and firms?
6. How does credit allocation differ when funds flow toward productive investment, speculation, housing, public infrastructure, or ecological transition?
7. How do collateral and monetary hierarchy shape access to safe liquidity?
8. How can Python, R, Stata, SQL, and Julia make financial assumptions transparent?

## Core Model Ideas

```text
Simple money aggregate:
M = C + D
```

```text
Bank lending:
ΔAssets = +Loan
ΔLiabilities = +Deposit
```

```text
Leverage:
Leverage = A / E
```

```text
Loan-to-deposit ratio:
LDR = Loans / Deposits
```

```text
Interest coverage:
ICR = EBIT / Interest
```

```text
Liquidity coverage:
LCR = HQLA / NCO
```

```text
Credit-output relation:
ΔY = f(ΔCredit, Confidence, Rates, Balance Sheets)
```

## Folder Structure

```text
money-banking-credit-and-financial-intermediation/
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

- `data/processed/money_aggregate_scenarios.csv`
- `data/processed/bank_balance_sheet_scenarios.csv`
- `data/processed/debt_service_scenarios.csv`
- `data/processed/liquidity_stress_scenarios.csv`
- `data/processed/credit_allocation_scenarios.csv`
- `data/processed/monetary_hierarchy_scenarios.csv`
- `data/processed/sustainable_finance_scenarios.csv`
- `data/processed/money_banking_credit_intermediation.sqlite`
- `outputs/tables/money_aggregate_results_python.csv`
- `outputs/tables/bank_balance_sheet_results_python.csv`
- `outputs/tables/deposit_creation_results_python.csv`
- `outputs/tables/debt_service_results_python.csv`
- `outputs/tables/liquidity_stress_results_python.csv`
- `outputs/tables/credit_allocation_results_python.csv`
- `outputs/tables/monetary_hierarchy_results_python.csv`
- `outputs/tables/sustainable_finance_results_python.csv`
- `outputs/tables/money_banking_r_results.csv`
- `outputs/tables/money_banking_stata_results.csv`
- `outputs/tables/julia_money_banking_results.csv`
- `outputs/figures/bank_balance_sheet_python.png`
- `outputs/figures/deposit_creation_python.png`
- `outputs/figures/debt_service_python.png`
- `outputs/figures/liquidity_stress_python.png`
- `outputs/figures/credit_allocation_python.png`
- `outputs/figures/sustainable_finance_python.png`
- `outputs/figures/money_banking_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a bank supervisory model, stress-testing engine, monetary-policy forecast, Basel compliance model, or financial-institution risk system. Its purpose is to make the article's conceptual claims computationally inspectable.
