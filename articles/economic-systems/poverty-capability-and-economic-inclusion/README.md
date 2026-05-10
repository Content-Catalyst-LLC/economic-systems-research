# Poverty, Capability, and Economic Inclusion

This folder is the article-level research package for:

**Poverty, Capability, and Economic Inclusion**

It is designed as an economist-grade companion workflow for studying income poverty, poverty gaps, multidimensional deprivation, capability conversion, economic inclusion, work and informality, housing and infrastructure security, financial inclusion, care burdens, child poverty, spatial exclusion, public services, social protection, digital access, vulnerability, and sustainable capability-building.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — poverty rates, poverty gaps, multidimensional deprivation, capability scores, inclusion scores, conversion-condition indices, vulnerability analysis, housing/infrastructure burden, work informality, financial inclusion, care burdens, digital access, visualization
- **R** — poverty and capability summaries, inclusion and vulnerability graphics, multidimensional deprivation comparisons
- **Stata** — applied poverty, inclusion, and capability replication workflows and indicator tables
- **SQL** — structured household, deprivation, services, work, housing, finance, care, child, spatial, digital, and vulnerability metadata
- **Julia** — numerical simulations for shocks, poverty transitions, capability conversion, social-protection effects, and vulnerability trajectories

## Research Questions

1. How does income poverty differ from multidimensional deprivation?
2. How much depth lies beneath a poverty headcount?
3. How do health, education, mobility, safety, time, and institutional access shape capability?
4. How do conversion conditions determine whether resources become real freedom?
5. When does employment represent inclusion, and when does it remain precarious?
6. How do housing and infrastructure shape everyday security?
7. When does financial inclusion widen capability, and when does it monetize vulnerability?
8. How do care burdens and gendered labor shape exclusion?
9. How does childhood deprivation reproduce disadvantage?
10. How does place organize poverty spatially?
11. How do digital systems create new boundaries of participation?
12. How can public services and social protection convert income support into durable capability?

## Core Model Ideas

```text
Poverty rate:
PR = P / N
```

```text
Poverty gap:
PG = Σ(z - y_i) / N
```

```text
Capability:
C = f(income, health, education, mobility, safety, time, institutional access)
```

```text
Economic inclusion:
I = f(work, finance, services, infrastructure, digital access, legal recognition)
```

```text
Conversion:
Real Freedom = Resources × Conversion Conditions
```

```text
Vulnerability:
V = f(low savings, high debt, insecure work, weak services, shock exposure)
```

```text
Social protection effect:
SPE = Vulnerability Before Support - Vulnerability After Support
```

## Folder Structure

```text
poverty-capability-and-economic-inclusion/
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

This is a stylized, reproducible teaching and research scaffold. It is not an official poverty measurement system, household survey, tax-benefit model, human-development index, capability index, benefit-eligibility system, legal tool, or policy-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
