# Industrial Policy and the Developmental State

This folder is the article-level research package for:

**Industrial Policy and the Developmental State**

It is designed as an economist-grade companion workflow for studying strategic sectors, sectoral output shares, productivity, export performance, conditional public support, development finance, credit allocation, industrial learning, domestic linkages, infrastructure readiness, energy reliability, skills systems, capture risk, regional clusters, green industrial policy, and developmental state capacity.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — sectoral priorities, productivity, export ratios, support-performance conditionality, domestic linkage scores, development finance, infrastructure readiness, capture risk, regional clusters, green industrial strategy, visualization
- **R** — industrial-policy summaries, strategic-sector comparisons, performance-conditionality graphics, regional and green industrial policy diagnostics
- **Stata** — applied industrial-policy replication workflows and sectoral indicator tables
- **SQL** — structured strategic-sector, public-support, export, finance, skills, infrastructure, regional-cluster, governance-risk, and green industrial-policy metadata
- **Julia** — numerical simulations for learning curves, conditional support withdrawal, export upgrading, linkage deepening, and green industrial policy tradeoffs

## Research Questions

1. How can sectoral output shares reveal changes in industrial structure?
2. How do productivity and learning differ across strategic sectors?
3. How can export ratios indicate whether supported sectors are entering external markets?
4. How should public support be tied to productivity, exports, employment, domestic linkages, and emissions performance?
5. How does development finance redirect investment toward long-horizon industrial capability?
6. How do infrastructure and energy reliability condition industrial success?
7. How do skills systems and labor institutions affect upgrading?
8. How can capture, rent-seeking, and policy failure be monitored?
9. How do regional clusters support supplier depth and territorial development?
10. How can green industrial policy combine productivity, decarbonization, resilience, and employment?
11. How can Python, R, Stata, SQL, and Julia make industrial-policy assumptions transparent?

## Core Model Ideas

```text
Sectoral output share:
s_i = Y_i / Y
```

```text
Sectoral productivity:
LP_i = Y_i / L_i
```

```text
Export performance:
XR_i = X_i / Y_i
```

```text
Support intensity:
SI_i = Public Support_i / Sector Output_i
```

```text
Conditional performance:
P_i = f(exports, productivity, learning, employment, domestic linkage, emissions)
```

```text
Domestic linkage:
DL = f(suppliers, skills, infrastructure, finance)
```

```text
Capability depth:
C = f(engineering, R&D, standards, maintenance, training)
```

```text
Capture risk:
CR = f(concentration, lobbying, weak evaluation, open-ended support, poor performance)
```

## Folder Structure

```text
industrial-policy-and-the-developmental-state/
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

- `data/processed/strategic_sector_scenarios.csv`
- `data/processed/support_conditionality_scenarios.csv`
- `data/processed/development_finance_scenarios.csv`
- `data/processed/infrastructure_energy_scenarios.csv`
- `data/processed/skills_labor_scenarios.csv`
- `data/processed/capture_risk_scenarios.csv`
- `data/processed/regional_cluster_scenarios.csv`
- `data/processed/green_industrial_policy_scenarios.csv`
- `data/processed/industrial_policy_developmental_state.sqlite`
- `outputs/tables/strategic_sector_results_python.csv`
- `outputs/tables/support_conditionality_results_python.csv`
- `outputs/tables/development_finance_results_python.csv`
- `outputs/tables/infrastructure_energy_results_python.csv`
- `outputs/tables/skills_labor_results_python.csv`
- `outputs/tables/capture_risk_results_python.csv`
- `outputs/tables/regional_cluster_results_python.csv`
- `outputs/tables/green_industrial_policy_results_python.csv`
- `outputs/tables/industrial_policy_r_results.csv`
- `outputs/tables/industrial_policy_stata_results.csv`
- `outputs/tables/julia_industrial_policy_results.csv`
- `outputs/figures/sectoral_priority_scores_python.png`
- `outputs/figures/productivity_export_performance_python.png`
- `outputs/figures/support_conditionality_python.png`
- `outputs/figures/development_finance_alignment_python.png`
- `outputs/figures/infrastructure_readiness_python.png`
- `outputs/figures/skills_labor_upgrading_python.png`
- `outputs/figures/capture_risk_python.png`
- `outputs/figures/regional_cluster_depth_python.png`
- `outputs/figures/green_industrial_policy_python.png`
- `outputs/figures/industrial_policy_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not an official industrial-policy evaluation system, national industrial strategy model, credit-allocation platform, subsidy audit, state-aid compliance tool, or investment-advice tool. Its purpose is to make the article's conceptual claims computationally inspectable.
