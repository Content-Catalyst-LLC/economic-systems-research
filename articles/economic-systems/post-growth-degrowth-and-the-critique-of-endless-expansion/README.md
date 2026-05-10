# Post-Growth, Degrowth, and the Critique of Endless Expansion

This folder is the article-level research package for:

**Post-Growth, Degrowth, and the Critique of Endless Expansion**

It is designed as an economist-grade companion workflow for studying growth dependence, throughput, resource intensity, post-growth wellbeing, degrowth transition capacity, sufficiency, shorter working time, public goods, care, distribution, debt dependence, finance, decoupling, rebound effects, global justice, asymmetric responsibility, and sustainable systems.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — growth-dependence scoring, throughput identities, wellbeing dashboards, sufficiency ratios, degrowth transition scoring, decoupling and rebound scenarios, finance-dependence analysis, justice and development indicators, visualization
- **R** — post-growth and degrowth summaries, throughput and wellbeing graphics, sufficiency comparisons, transition-policy dashboards
- **Stata** — applied post-growth replication workflows and indicator-table analysis
- **SQL** — structured growth-dependence, throughput, wellbeing, sufficiency, work-time, public-goods, finance, decoupling, global-justice, and transition metadata
- **Julia** — numerical simulations for throughput trajectories, growth dependence, decoupling, rebound, sufficiency, transition legitimacy, and wellbeing under lower material pressure

## Research Questions

1. Which institutions are most dependent on continued GDP growth for stability?
2. How do population, affluence, and intensity shape total material throughput?
3. Can wellbeing improve when GDP growth slows, if public goods, equality, time, and ecological quality improve?
4. How can sufficiency be represented as needs met per unit of throughput?
5. Which sectors should contract, stabilize, or expand under a post-growth or degrowth transition?
6. How do shorter working time, care, and public goods affect the social meaning of prosperity?
7. How do debt, asset valuations, pensions, fiscal systems, and finance reinforce growth dependence?
8. When do efficiency gains produce absolute decoupling, and when does rebound offset gains?
9. How should global responsibility distinguish excess consumption from development need?
10. What makes intentional throughput reduction socially credible rather than austerity?

## Core Model Ideas

```text
Growth dependence:
GD = f(employment, debt service, fiscal stability, asset valuation)
```

```text
Throughput:
T = Population × Affluence × Intensity
```

```text
Well-being:
WB = f(health, time, security, equality, public goods, ecological quality)
```

```text
Sufficiency:
S = Needs Met / Throughput Required
```

```text
Degrowth transition:
DT = f(throughput reduction, redistribution, public services, democratic legitimacy)
```

```text
Rebound:
R = Efficiency Gain - Additional Demand Induced
```

## Folder Structure

```text
post-growth-degrowth-and-the-critique-of-endless-expansion/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official macroeconomic forecast, national accounts model, degrowth transition plan, fiscal sustainability model, legal analysis, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
