# Natural Capital, Resource Use, and Environmental Constraint

This folder is the article-level research package for:

**Natural Capital, Resource Use, and Environmental Constraint**

It is designed as an economist-grade companion workflow for studying natural-capital stocks, resource-use pressure, regeneration, depletion, waste constraints, renewable and nonrenewable resources, material dependence, soil, water, forests, minerals, energy systems, pollution sinks, commons governance, ecological burden, resilience, strategic dependence, and sustainable systems.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — natural-capital stock-flow accounting, regeneration/depletion scenarios, resource-use ratios, waste constraints, material and energy dependence, ecosystem-function scoring, resource-justice indicators, resilience scoring, visualization
- **R** — natural-capital summaries, resource-pressure graphics, renewable/nonrenewable comparison tables, environmental-constraint dashboards
- **Stata** — applied natural-capital and resource-use replication workflows and indicator tables
- **SQL** — structured natural-capital, resource-use, waste, ecosystem, mineral, energy, commons, burden, and resilience metadata
- **Julia** — numerical simulations for stock-flow change, regenerative dynamics, depletion thresholds, waste-sink pressure, and resilience trajectories

## Research Questions

1. How do natural-capital stocks change when regeneration differs from degradation?
2. Which resource systems are being used within regenerative limits and which are being depleted?
3. How do renewable and nonrenewable resource regimes differ?
4. How do waste emissions compare with absorptive capacity?
5. Which sectors create the highest material, energy, water, land, and waste pressure?
6. How do soil, water, forests, minerals, and energy systems support production?
7. How do ecosystem functions create value that market prices may understate?
8. How do substitution, efficiency, and rebound effects change environmental pressure?
9. How does resource dependence create ecological and strategic vulnerability?
10. How are ecological burdens distributed across groups and territories?
11. How do commons and property regimes shape resource outcomes?
12. How can sustainable systems preserve natural inheritance while meeting human needs?

## Core Model Ideas

```text
Natural capital stock change:
NC(t+1) = NC(t) + R - D
```

```text
Resource use ratio:
RU = Use / Regenerative Capacity
```

```text
Waste constraint:
WC = Emissions / Absorptive Capacity
```

```text
Extraction dependency:
ED = f(material intensity, energy intensity, import dependence)
```

```text
Ecological resilience:
ER = f(diversity, regeneration, redundancy, governance)
```

```text
Justice burden:
JB = f(exposure, income, public infrastructure, adaptive capacity)
```

## Folder Structure

```text
natural-capital-resource-use-and-environmental-constraint/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official natural-capital account, environmental input-output model, life-cycle assessment, resource-reserve forecast, mineral-security assessment, legal analysis, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
