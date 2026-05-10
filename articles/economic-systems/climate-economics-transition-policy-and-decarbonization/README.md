# Climate Economics, Transition Policy, and Decarbonization

This folder is the article-level research package for:

**Climate Economics, Transition Policy, and Decarbonization**

It is designed as an economist-grade companion workflow for studying emissions identities, Kaya-style decomposition, decarbonization rates, transition investment, climate damages, vulnerability, adaptation, carbon pricing, regulation, public investment, industrial policy, energy transition, transport and building retrofit pathways, hard-to-abate sectors, just transition, global burden-sharing, credibility, finance, implementation capacity, and sustainable systems.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — emissions identities, Kaya decomposition, sector pathways, decarbonization rates, policy-mix scoring, carbon-pricing burden scenarios, transition-investment scoring, adaptation burden, just-transition indicators, global equity metrics, visualization
- **R** — climate-economics summaries, emissions-pathway graphics, transition-policy dashboards, justice and adaptation comparisons
- **Stata** — applied decarbonization and climate-policy replication workflows and indicator tables
- **SQL** — structured sector emissions, policy instruments, investment, damage, vulnerability, adaptation, labor, finance, international equity, and implementation metadata
- **Julia** — numerical simulations for emissions trajectories, capital-stock turnover, policy credibility, decarbonization rates, damages, adaptation capacity, and transition resilience

## Research Questions

1. How do output, energy intensity, and carbon intensity drive emissions?
2. Which sectors decarbonize fastest, and which remain hard to abate?
3. How fast must emissions intensity fall to meet transition targets?
4. How do carbon pricing, standards, public investment, and industrial policy interact?
5. How do climate damages vary with exposure, vulnerability, and adaptation capacity?
6. How does carbon lock-in affect transition speed?
7. How do energy reliability, affordability, and investment credibility shape transition legitimacy?
8. How do transition costs and benefits fall across workers, regions, households, and sectors?
9. How do climate finance, disclosure, and cost of capital influence investment?
10. How should global burden-sharing account for historical responsibility and development capacity?
11. How can decarbonization be evaluated by emissions, justice, resilience, credibility, and implementation together?

## Core Model Ideas

```text
Emissions identity:
E = Y × EI
```

```text
Kaya-style identity:
CO2 = Population × Income per Capita × Energy Intensity × Carbon Intensity
```

```text
Decarbonization rate:
DR = (EI_old - EI_new) / Time
```

```text
Transition investment:
TI = f(public investment, private capital, policy credibility, cost of capital)
```

```text
Climate damage:
CD = f(temperature, exposure, vulnerability, adaptation capacity)
```

```text
Just transition:
JT = f(retraining, regional investment, income support, public services)
```

## Folder Structure

```text
climate-economics-transition-policy-and-decarbonization/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official greenhouse-gas inventory, integrated assessment model, national transition plan, financial-risk model, legal analysis, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
