# Monetary Policy, Central Banking, and Financial Conditions

This folder is the article-level research package for:

**Monetary Policy, Central Banking, and Financial Conditions**

It is designed as an economist-grade companion workflow for studying real interest rates, debt-service burdens, policy reaction functions, financial-conditions indices, transmission channels, asset-price repricing, banking liquidity stress, exchange-rate pressure, monetary-fiscal interaction, and sustainable-investment financing conditions.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — real rates, debt-service stress, stylized reaction functions, financial-conditions indices, asset valuation, bank liquidity, exchange-rate pressure, public-debt interaction, sustainable investment affordability, visualization
- **R** — monetary scenario summaries, financial-conditions graphics, household and firm exposure comparisons
- **Stata** — applied monetary economics replication workflows and financial-condition indicator tables
- **SQL** — structured policy-rate, balance-sheet, bank-liquidity, asset-valuation, open-economy, public-debt, and sustainable-investment metadata
- **Julia** — numerical simulations for policy-rate paths, debt-service burdens, asset repricing, liquidity stress, and investment affordability

## Research Questions

1. How do nominal rates and expected inflation determine real borrowing costs?
2. How do rising rates affect household and firm debt-service burdens?
3. How can a stylized reaction function connect inflation gaps, output gaps, and policy rates?
4. Why are financial conditions broader than the policy rate alone?
5. How do rate changes reprice long-duration assets?
6. How do reserves, liquidity, and deposit outflows affect bank stress?
7. How do exchange-rate pressures transmit open-economy constraints?
8. How does monetary tightening affect public debt service and fiscal space?
9. How do long-term yields affect resilience, infrastructure, and green-investment affordability?
10. How can Python, R, Stata, SQL, and Julia make monetary-policy assumptions transparent?

## Core Model Ideas

```text
Real rate:
r = i - π_e
```

```text
Debt-service ratio:
DSR = Debt Service / Income
```

```text
Stylized reaction function:
i = i* + a(π - π*) + b(Y - Y*)
```

```text
Present value:
PV = Σ CF_t / (1 + i)^t
```

```text
Financial conditions:
FCI = f(i, spreads, asset prices, exchange rate, lending standards)
```

```text
Liquidity coverage:
LCR = Liquid Assets / Short-Term Outflows
```

```text
Public debt service:
DS_public = i × D
```

```text
Investment affordability:
IA = Expected Social Return - Financing Cost
```

## Folder Structure

```text
monetary-policy-central-banking-and-financial-conditions/
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

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a central-bank forecasting model, official policy simulator, bank supervisory model, debt-management system, or investment-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
