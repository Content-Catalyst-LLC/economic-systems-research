# Ecological Economics and the Embedded Economy

This folder is the article-level research package for:

**Ecological Economics and the Embedded Economy**

It is designed as an economist-grade companion workflow for studying the economy as a subsystem of the biosphere, material and energy throughput, ecological scale, waste and recovery, strong sustainability, ecosystem services, commons governance, care and social reproduction, ecological burden distribution, resilience, vulnerability, post-growth and degrowth scenarios, and sustainable systems.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — throughput accounting, material footprint scenarios, scale ratios, waste balances, ecological burden indices, resilience scores, social embeddedness metrics, commons governance comparisons, post-growth scenarios, visualization
- **R** — ecological-economy summaries, scale/allocation/distribution graphics, burden and resilience comparisons, article-ready figures
- **Stata** — applied ecological-economics replication workflows and indicator tables
- **SQL** — structured throughput, sectors, ecological capacity, burden distribution, care, commons, resilience, and post-growth metadata
- **Julia** — numerical simulations for throughput, ecological scale, recovery, resilience, regeneration, and post-growth transition pathways

## Research Questions

1. How large is the economy relative to ecological capacity?
2. How do energy and material throughput shape economic possibility?
3. How does waste change when recovery, recycling, and regeneration improve?
4. Which sectors generate the highest material and energy pressure?
5. How are ecological burdens distributed across income groups, territories, and infrastructure conditions?
6. How does the economy depend on unpaid care, public institutions, infrastructure, and social reproduction?
7. What forms of natural capital are weakly or non-substitutable?
8. How do commons governance arrangements affect ecological resilience?
9. How do growth, degrowth, and post-growth scenarios change throughput and wellbeing?
10. How can economic systems be evaluated by scale, allocation, distribution, resilience, and justice together?

## Core Model Ideas

```text
Throughput:
T = E + M
```

```text
Ecological scale:
S = Economic Scale / Ecological Capacity
```

```text
Waste residual:
W = T - R
```

```text
Material footprint:
MF = Domestic Extraction + Imports - Exports
```

```text
Ecological burden:
EB = f(exposure, income, infrastructure, adaptive capacity)
```

```text
Socio-ecological resilience:
SR = f(diversity, redundancy, regeneration, governance)
```

```text
Embedded economy:
EE = f(ecology, care, institutions, infrastructure, culture)
```

## Folder Structure

```text
ecological-economics-and-the-embedded-economy/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official material-flow account, environmental input-output model, life-cycle assessment, climate model, ecological-footprint calculator, legal analysis, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
