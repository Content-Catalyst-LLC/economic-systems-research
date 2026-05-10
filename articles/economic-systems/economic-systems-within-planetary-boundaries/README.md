# Economic Systems Within Planetary Boundaries

This folder is the article-level research package for:

**Economic Systems Within Planetary Boundaries**

It is designed as an economist-grade companion workflow for studying planetary boundaries, safe operating space, boundary pressure ratios, resource-use identities, throughput, overshoot, coupled energy-food-land-water systems, material intensity, ecological space, distribution, justice, transition capacity, state capacity, public investment, finance, boundary-aware accounting, sufficiency, stewardship, system redesign, and sustainable systems.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — boundary-pressure ratios, resource-use identities, overshoot scoring, sector pressure, coupled-system risk, justice-adjusted ecological space, transition-capacity scoring, finance-direction scoring, visualization
- **R** — boundary-pressure summaries, resource-use dashboards, transition-capacity comparison tables, justice and ecological-space graphics
- **Stata** — applied planetary-boundary replication workflows and indicator-table analysis
- **SQL** — structured boundary, resource-use, sector, justice, transition-capacity, finance, accounting, and sufficiency metadata
- **Julia** — numerical simulations for boundary pressure, resource-use trajectories, transition capacity, overshoot reduction, and safe-operating-space scenarios

## Research Questions

1. Which Earth-system processes face the greatest economic pressure relative to safe operating space?
2. How do population, affluence, and resource intensity shape total resource use?
3. Which production sectors generate the highest coupled boundary pressure?
4. How do energy, food, land, and water pressures interact rather than remain separate?
5. How is ecological space distributed across income groups, countries, sectors, and territories?
6. How do innovation, efficiency, rebound, sufficiency, and demand reduction alter boundary pressure?
7. Which forms of state capacity and public investment improve transition capability?
8. How does finance direct development toward either overshoot or resilience?
9. How should GDP, material throughput, ecological pressure, natural capital, and inclusion be measured together?
10. How can economic systems be evaluated by ecological stability, inclusion, development capability, and implementation credibility?

## Core Model Ideas

```text
Boundary pressure ratio:
BPR = Economic Pressure / Earth-System Capacity
```

```text
Resource use identity:
RU = Population × Affluence × Resource Intensity
```

```text
Transition capacity:
TC = f(state capacity, public investment, social legitimacy, technological capability)
```

```text
Justice-adjusted sustainability:
JS = f(ecological stability, inclusion, development capability)
```

```text
Boundary-aware progress:
BAP = wellbeing - ecological overshoot - exclusion risk
```

## Folder Structure

```text
economic-systems-within-planetary-boundaries/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official Stockholm Resilience Centre planetary-boundaries assessment, UNEP/IRP resource model, IPCC scenario pathway, national environmental account, legal analysis, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
