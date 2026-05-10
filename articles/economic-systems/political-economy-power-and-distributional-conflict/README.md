# Political Economy, Power, and Distributional Conflict

This folder is the article-level research package for:

**Political Economy, Power, and Distributional Conflict**

It is designed as an economist-grade companion workflow for studying income shares, wage-profit-rent distribution, bargaining power, fiscal incidence, tax-benefit burdens, capital-labor conflict, creditor-debtor relations, housing rents, ownership power, inflation conflict, institutional representation, welfare-state solidarity, industrial-policy distribution, globalization, crisis burden-sharing, legitimacy, and sustainable systems.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — income distribution, wage/profit/rent shares, fiscal incidence, bargaining-power indicators, conflict-intensity scores, inflation adjustment, debt-service pressure, rent extraction, welfare buffering, globalization exposure, crisis burden-sharing, legitimacy scoring, visualization
- **R** — distributional-conflict summaries, income-share graphics, fiscal-burden comparisons, representation and power asymmetry dashboards
- **Stata** — applied political-economy and distributional-conflict replication workflows and indicator tables
- **SQL** — structured income, fiscal, labor, debt, rent, welfare, globalization, crisis, representation, and legitimacy metadata
- **Julia** — numerical simulations for wage-profit-rent distribution, bargaining power, inflation adjustment, fiscal burden, debt pressure, crisis burden-sharing, and legitimacy trajectories

## Research Questions

1. How is income divided among wages, profits, and rents?
2. How do labor institutions, ownership structures, and macroeconomic policy shape wage shares?
3. How do taxes and transfers redistribute burdens and benefits across groups?
4. How does bargaining power affect the distribution of gains from production?
5. How do creditors, debtors, landlords, firms, workers, and states exercise economic power?
6. How does inflation become a conflict over real income and adjustment?
7. How does debt create enforceable claims on future income and public budgets?
8. How do rents and ownership concentrate economic power?
9. How do welfare states mediate distributional conflict and social membership?
10. How do globalization and capital mobility reshape domestic bargaining power?
11. How do crises reveal who is rescued, who waits, and who pays?
12. How does legitimacy depend on fairness, security, voice, and institutional trust?
13. How can political economy be modeled as a system of power, claims, and distributional struggle?

## Core Model Ideas

```text
Income distribution:
Y = W + Π + R
```

```text
Wage share:
WS = W / Y
```

```text
Profit share:
PS = Π / Y
```

```text
Rent share:
RS = R / Y
```

```text
Net fiscal position:
NFP = Benefits Received - Taxes Paid
```

```text
Power asymmetry:
PA = f(ownership, organization, access, mobility, voice)
```

```text
Conflict intensity:
CI = f(inequality, inflation, unemployment, representation gaps, shock exposure)
```

```text
Legitimacy:
L = f(fairness, security, voice, institutional trust)
```

## Folder Structure

```text
political-economy-power-and-distributional-conflict/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official distributional national accounts dataset, microsimulation model, tax-benefit engine, political-risk forecast, legal analysis, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
