# Inequality, Redistribution, and Social Mobility

This folder is the article-level research package for:

**Inequality, Redistribution, and Social Mobility**

It is designed as an economist-grade companion workflow for studying income inequality, wealth concentration, pre-tax and post-tax distribution, redistribution through taxes and transfers, public-service valuation, labor-market bargaining power, housing-cost burden, place-based opportunity, social insurance, intergenerational mobility, opportunity formation, and economic security.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — income shares, Gini-style summaries, pre/post redistribution, wealth ratios, mobility elasticity, opportunity scores, housing burden, public-service valuation, labor bargaining, social insurance, security scoring, visualization
- **R** — inequality and redistribution summaries, mobility and opportunity graphics, housing-adjusted living-standard comparisons
- **Stata** — applied inequality and mobility replication workflows and indicator tables
- **SQL** — structured income, wealth, tax-transfer, public-service, housing, labor, education-health, mobility, and security metadata
- **Julia** — numerical simulations for redistribution, mobility persistence, wealth compounding, housing-cost burden, and security trajectories

## Research Questions

1. How do income shares differ before and after taxes and transfers?
2. How does wealth concentration differ from income inequality?
3. How do public services alter effective living standards?
4. How does housing cost burden change disposable security?
5. How do labor-market institutions affect earnings dispersion?
6. How do education, health, place, wealth, and networks shape opportunity?
7. How persistent is parental status across generations?
8. How does social insurance affect downside risk and mobility?
9. How do redistribution systems alter inequality and security?
10. How can inequality be analyzed as a systems problem rather than a single-number outcome?
11. How can Python, R, Stata, SQL, and Julia make distributional assumptions transparent?

## Core Model Ideas

```text
Income share:
s_i = Y_i / Y
```

```text
Disposable income:
DI = Market Income - Taxes + Transfers + Public Service Value
```

```text
Wealth ratio:
WR = W_top / W_bottom
```

```text
Intergenerational persistence:
Child Outcome = a + b(Parent Outcome)
```

```text
Opportunity:
O = f(education, health, wealth, place, networks)
```

```text
Security:
S = f(income, public services, insurance, housing stability, debt burden)
```

```text
Redistributive effect:
RE = Market Inequality - Disposable Inequality
```

## Folder Structure

```text
inequality-redistribution-and-social-mobility/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official poverty measurement system, tax-benefit microsimulation model, mobility database, household survey, legal tool, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
