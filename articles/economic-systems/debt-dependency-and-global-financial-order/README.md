# Debt, Dependency, and Global Financial Order

This folder is the article-level research package for:

**Debt, Dependency, and Global Financial Order**

It is designed as an economist-grade companion workflow for studying debt-to-output ratios, external debt-service pressure, foreign-currency debt burden, exchange-rate sensitivity, reserve adequacy, interest-growth dynamics, balance-of-payments constraints, currency hierarchy, sovereign credit discipline, multilateral conditionality, private creditor power, austerity adjustment, commodity dependence, capital-flow sudden stops, debt restructuring, and sustainable development finance.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — debt sustainability metrics, FX sensitivity, external debt-service ratios, reserve adequacy, capital-flow shocks, commodity debt vulnerability, adjustment burden, restructuring scenarios, sustainable finance scores, visualization
- **R** — debt and dependency summaries, debt-service and reserve graphics, restructuring and sustainable-finance comparisons
- **Stata** — applied sovereign debt and external vulnerability replication workflows and indicator tables
- **SQL** — structured debt, currency, external account, creditor, conditionality, austerity, commodity, capital-flow, restructuring, and sustainable finance metadata
- **Julia** — numerical simulations for interest-growth dynamics, exchange-rate depreciation, sudden stops, restructuring options, and long-horizon debt trajectories

## Research Questions

1. How does the debt-to-output ratio differ from external vulnerability?
2. How much export revenue is absorbed by external debt service?
3. How does foreign-currency debt respond to exchange-rate depreciation?
4. When does the interest-growth differential intensify debt pressure?
5. How does reserve adequacy alter crisis resilience?
6. How do currency hierarchy and foreign-currency borrowing constrain policy space?
7. How do sovereign ratings, bond markets, and private creditors exercise credit discipline?
8. How do conditionality and austerity affect public capacity and development?
9. How do commodity shocks interact with debt vulnerability?
10. How do sudden stops interrupt development strategies?
11. How can restructuring scenarios compare haircuts, maturity extensions, and interest relief?
12. How can finance support sovereign capacity instead of reproducing dependency?

## Core Model Ideas

```text
Debt-to-output ratio:
DR = D / Y
```

```text
External debt-service ratio:
EDSR = External Debt Service / Export Earnings
```

```text
Foreign-currency debt burden:
FX Burden = D_fx × ER
```

```text
Interest-growth dynamic:
ΔD ≈ (r - g)D + Primary Deficit
```

```text
Reserve adequacy:
RA = Reserves / Short-Term External Obligations
```

```text
External vulnerability:
EV = f(FX debt, debt service, import dependence, capital-flow volatility, reserve adequacy)
```

```text
Dependency:
Dep = f(export concentration, foreign-currency debt, import dependence, external finance reliance, weak domestic capability)
```

```text
Sustainable development finance:
SDF = f(productive investment, domestic capability, export resilience, social protection, ecological resilience, debt manageability)
```

## Folder Structure

```text
debt-dependency-and-global-financial-order/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official debt sustainability analysis, sovereign credit model, balance-of-payments forecast, IMF/World Bank framework, restructuring recommendation, investment advice, or legal advice. Its purpose is to make the article's conceptual claims computationally inspectable.
