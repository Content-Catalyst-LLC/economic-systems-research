# Beyond GDP: Measuring Well-Being, Inclusion, and Sustainability

This folder is the article-level research package for:

**Beyond GDP: Measuring Well-Being, Inclusion, and Sustainability**

It is designed as an economist-grade companion workflow for studying GDP, well-being dashboards, inclusion metrics, inequality-adjusted progress, capabilities, subjective well-being, care and unpaid work, ecological pressure, natural-capital depletion, adjusted progress, inclusive wealth, adjusted savings, policy dashboards, indicator governance, ranking risks, and sustainable systems.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — GDP identities, multidimensional well-being dashboards, inclusion scoring, inequality-adjusted progress, sustainability stock metrics, adjusted progress, capability conversion, care visibility, dashboard sensitivity, visualization
- **R** — well-being and inclusion summaries, dashboard graphics, sustainability-stock comparisons, inequality and capability tables
- **Stata** — applied beyond-GDP replication workflows and indicator-table analysis
- **SQL** — structured well-being, inclusion, sustainability, capability, care, ecological pressure, subjective well-being, dashboard, and governance metadata
- **Julia** — numerical simulations for multidimensional progress, dashboard weighting, sustainability stock dynamics, adjusted progress, and long-run capability trajectories

## Research Questions

1. What does GDP measure, and where does it fail as a progress indicator?
2. How can well-being be represented across health, education, income security, housing, safety, social connection, and environment?
3. How do distribution, mobility, access, and voice shape inclusion?
4. How can sustainability be represented as the maintenance of natural, human, institutional, and produced capital?
5. How do ecological costs and social costs alter progress narratives?
6. How does care and unpaid labor change the interpretation of economic output?
7. How do subjective well-being and lived experience complement objective indicators?
8. How do dashboards and composite indices produce different policy interpretations?
9. How do indicator rankings risk perverse incentives?
10. How can measurement systems support better governance rather than narrow target-chasing?

## Core Model Ideas

```text
GDP identity:
GDP = C + I + G + (X - M)
```

```text
Well-being dashboard:
WB = f(health, education, income security, housing, safety, social connection, environment)
```

```text
Inclusion:
IN = f(distribution, mobility, access, voice)
```

```text
Sustainability:
SW = f(natural capital, human capital, institutional trust, produced capital)
```

```text
Adjusted progress:
AP = Current Benefits - Social Costs - Ecological Costs
```

```text
Capability:
CA = f(resources, public goods, conversion conditions)
```

## Folder Structure

```text
beyond-gdp-measuring-well-being-inclusion-and-sustainability/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official national-accounting system, OECD dashboard, UNDP Human Development Index implementation, World Bank adjusted net savings model, statistical-agency product, legal analysis, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
