# Commons, Shared Resources, and Institutional Governance

This folder is the article-level research package for:

**Commons, Shared Resources, and Institutional Governance**

It is designed as an economist-grade companion workflow for studying shared resource stocks, extraction, regeneration, monitoring, compliance, access justice, enclosure risk, polycentric governance, institutional integrity, and commons breakdown.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — stock-flow commons simulations, extraction scenarios, compliance metrics, access-justice indicators, threshold visualization
- **R** — shared-resource summaries, governance scenario comparison, institutional-integrity graphics
- **Stata** — applied economics replication workflows and commons-governance indicator tables
- **SQL** — structured resource, user, governance, extraction, access, and institutional metadata
- **Julia** — numerical stock-flow simulations, compliance dynamics, and institutional-integrity trajectories

## Research Questions

This article companion workflow supports questions such as:

1. How does extraction by multiple users affect a renewable shared resource stock over time?
2. How do monitoring, rule clarity, legitimacy, and sanctions alter compliance?
3. How does governance quality change stock trajectories relative to unmanaged access?
4. How do unequal access rights and extraction rights affect welfare and legitimacy?
5. How do enclosure and capture risks change access, resource preservation, and justice?
6. How does institutional integrity erode or recover under upkeep, conflict, capture, and neglect?
7. How can Python, R, Stata, SQL, and Julia make commons-governance assumptions transparent?

## Core Model Ideas

```text
Resource stock dynamics:
S_{t+1} = S_t + G(S_t) - H_t
```

```text
Shared extraction:
H_t = Σ h_{i,t}
```

```text
Sustainability condition:
H_t ≤ G(S_t)
```

```text
Compliance:
C = f(M, R, L, S)
```

```text
Commons welfare:
W = f(P, A, J)
```

```text
Institutional integrity:
I_{t+1} = I_t + U_t - E_t
```

## Folder Structure

```text
commons-shared-resources-institutional-governance/
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

## Outputs

The workflow creates:

- `data/processed/resource_scenarios.csv`
- `data/processed/user_extraction_profiles.csv`
- `data/processed/governance_scenarios.csv`
- `data/processed/access_justice_scenarios.csv`
- `data/processed/commons_governance.sqlite`
- `outputs/tables/commons_stock_paths_python.csv`
- `outputs/tables/governance_compliance_results_python.csv`
- `outputs/tables/access_justice_results_python.csv`
- `outputs/tables/institutional_integrity_results_python.csv`
- `outputs/tables/commons_r_results.csv`
- `outputs/tables/commons_stata_results.csv`
- `outputs/tables/julia_commons_results.csv`
- `outputs/figures/commons_stock_paths_python.png`
- `outputs/figures/harvest_regeneration_balance_python.png`
- `outputs/figures/compliance_by_governance_python.png`
- `outputs/figures/access_justice_python.png`
- `outputs/figures/institutional_integrity_python.png`
- `outputs/figures/commons_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a full natural-resource economics model, hydrological model, fisheries model, forest dynamics model, or institutional ethnography. Its purpose is to make the article's conceptual claims computationally inspectable.
