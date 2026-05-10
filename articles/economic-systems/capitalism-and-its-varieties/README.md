# Capitalism and Its Varieties

This folder is the article-level research package for:

**Capitalism and Its Varieties**

It is designed as an economist-grade companion workflow for studying comparative capitalism, liberal market economies, coordinated market economies, developmental capitalism, finance-led capitalism, welfare capitalism, labor regimes, corporate governance, financialization, housing and household vulnerability, global value chains, institutional complementarities, crisis response, inequality, power, and sustainable systems.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — regime indicators, wage shares, profit relations, financialization scores, labor coordination, welfare buffers, corporate governance, housing vulnerability, crisis response, institutional advantage, sustainability scoring, visualization
- **R** — comparative-capitalism summaries, regime typologies, institutional-complementarity graphics, cross-regime scenario tables
- **Stata** — applied comparative-capitalism replication workflows and indicator tables
- **SQL** — structured capitalism-regime, labor, finance, welfare, corporate-governance, housing, globalization, crisis, inequality, and sustainability metadata
- **Julia** — numerical simulations for wage-profit distribution, financialization, welfare buffers, crisis adjustment, institutional complementarities, and sustainable-capitalism trajectories

## Research Questions

1. How do different capitalist regimes organize labor, finance, welfare, firms, and public authority?
2. How do liberal, coordinated, developmental, finance-led, welfare, and hybrid capitalisms differ?
3. How do wage shares, profit shares, bargaining power, and financial claims vary across regimes?
4. How does financialization change firm behavior and household vulnerability?
5. How do welfare institutions buffer market risk?
6. How do labor regimes and training systems shape comparative institutional advantage?
7. How does corporate governance affect time horizons, investment, and distribution?
8. How do housing regimes transmit financialization into everyday security?
9. How do global value chains produce hybrid and dependent forms of capitalism?
10. How do capitalist systems respond differently to crisis?
11. How do institutional complementarities shape regime stability?
12. How can capitalist varieties be judged by resilience, legitimacy, inequality, and ecological sustainability?

## Core Model Ideas

```text
Profit:
π = R - C
```

```text
Wage share:
WS = W / Y
```

```text
Profit share:
PS = π / Y
```

```text
Financialization:
F = f(asset prices, debt, shareholder claims, leverage)
```

```text
Social protection:
SP = f(transfers, services, coverage, replacement rates)
```

```text
Comparative institutional advantage:
CA = f(finance type, labor regime, training system, firm coordination)
```

```text
Sustainable capitalist order:
SCO = f(productive investment, labor security, welfare buffering, ecological constraint, democratic legitimacy)
```

## Folder Structure

```text
capitalism-and-its-varieties/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official country classification system, national accounts model, firm-level dataset, econometric estimate, investment recommendation, legal analysis, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
