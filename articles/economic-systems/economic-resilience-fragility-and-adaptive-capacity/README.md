# Economic Resilience, Fragility, and Adaptive Capacity

This folder is the article-level research package for:

**Economic Resilience, Fragility, and Adaptive Capacity**

It is designed as an economist-grade companion workflow for studying resilience, fragility, adaptive capacity, shock exposure, system vulnerability, buffers, redundancy, slack, automatic stabilizers, household resilience, firm resilience, infrastructure interdependence, supply-chain concentration, financial fragility, labor-market adaptation, ecological risk, public trust, information systems, recovery, learning, and transformational adaptation.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — resilience scoring, fragility scoring, adaptive-capacity indicators, shock-impact simulations, buffer analysis, supply-chain concentration, household resilience, infrastructure cascade scoring, recovery trajectory analysis, visualization
- **R** — resilience dashboards, fragility summaries, shock-impact graphics, household and regional resilience comparisons
- **Stata** — applied resilience and fragility replication workflows and indicator-table analysis
- **SQL** — structured shock, buffer, household, firm, supply-chain, finance, labor, ecological, public-capacity, and recovery metadata
- **Julia** — numerical simulations for shock propagation, adaptive capacity, recovery dynamics, infrastructure interdependence, and resilience investment scenarios

## Research Questions

1. Which systems have enough buffers, redundancy, coordination, trust, and learning capacity to absorb shocks?
2. Which systems are fragile because of leverage, concentration, exposure, underinvestment, and inequality?
3. How does shock impact depend on both shock magnitude and system vulnerability?
4. How are resilience and adaptive capacity distributed across households, firms, regions, and institutions?
5. When does efficiency become over-optimization?
6. How do public institutions, automatic stabilizers, and social protection reduce fragility?
7. How do debt, leverage, refinancing risk, and asset dependence amplify shocks?
8. How do infrastructure and supply-chain interdependencies create cascading risk?
9. How do ecological hazards, energy stress, and material vulnerability affect economic resilience?
10. What distinguishes rebound, recovery, adaptation, and transformation?

## Core Model Ideas

```text
Economic resilience:
ER = f(buffers, redundancy, coordination, trust, learning)
```

```text
Fragility:
FG = f(leverage, concentration, exposure, underinvestment, inequality)
```

```text
Adaptive capacity:
AC = f(information, fiscal space, skills, flexibility, legitimacy)
```

```text
Shock impact:
SI = Shock Magnitude × Vulnerability
```

```text
Recovery capacity:
RC = f(response speed, public capacity, household stability, infrastructure integrity)
```

```text
Distributional resilience:
DR = f(income security, savings, care access, housing stability, social protection)
```

## Folder Structure

```text
economic-resilience-fragility-and-adaptive-capacity/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official macroeconomic stress test, disaster-risk model, financial-stability model, supply-chain risk assessment, climate-risk model, legal analysis, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
