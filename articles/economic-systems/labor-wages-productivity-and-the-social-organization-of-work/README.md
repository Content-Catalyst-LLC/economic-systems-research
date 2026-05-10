# Labor, Wages, Productivity, and the Social Organization of Work

This folder is the article-level research package for:

**Labor, Wages, Productivity, and the Social Organization of Work**

It is designed as an economist-grade companion workflow for studying labor productivity, wage share, unit labor cost, wage-productivity divergence, bargaining power, employment quality, care burdens, social reproduction, automation shocks, time poverty, and sustainable work systems.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — productivity/wage-share calculations, wage-productivity divergence, bargaining scenarios, time poverty, care-burden indicators, automation-shock modeling, visualization
- **R** — labor-market summaries, employment-quality indicators, wage adequacy, work-time burden graphics
- **Stata** — applied labor-economics replication workflows and wage/productivity indicator tables
- **SQL** — structured labor, wage, sector, household, care, time-use, bargaining, and automation metadata
- **Julia** — numerical wage-bargaining simulation, productivity distribution, and automation-shock trajectories

## Research Questions

This article companion workflow supports questions such as:

1. How do labor productivity, wage share, and unit labor cost relate?
2. How can productivity rise while wage growth stagnates?
3. How do bargaining power and institutional support affect wage outcomes?
4. How does wage adequacy change when household costs and care costs are included?
5. How does work-time burden create time poverty even when employment is high?
6. How do automation shocks redistribute output, labor demand, and bargaining power?
7. How do employment quality, scheduling security, and care burden alter welfare analysis?
8. How can Python, R, Stata, SQL, and Julia make labor assumptions transparent?

## Core Model Ideas

```text
Labor productivity:
LP = Y / L
```

```text
Wage share:
WS = W / Y
```

```text
Unit labor cost:
ULC = w / LP
```

```text
Wage bargaining:
w = f(LP, B, I)
```

```text
Social reproduction adequacy:
w + S ≥ C_h + C_r
```

```text
Work-time allocation:
24 = T_w + T_c + T_h + T_r
```

```text
Wage-productivity divergence:
D_t = LP_t - w_t
```

## Folder Structure

```text
labor-wages-productivity-and-the-social-organization-of-work/
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

- `data/processed/sector_labor_scenarios.csv`
- `data/processed/wage_productivity_time_series.csv`
- `data/processed/household_reproduction_scenarios.csv`
- `data/processed/time_use_scenarios.csv`
- `data/processed/bargaining_institution_scenarios.csv`
- `data/processed/automation_shock_scenarios.csv`
- `data/processed/labor_wages_productivity_work.sqlite`
- `outputs/tables/productivity_wage_share_results_python.csv`
- `outputs/tables/wage_productivity_divergence_python.csv`
- `outputs/tables/social_reproduction_adequacy_python.csv`
- `outputs/tables/time_poverty_results_python.csv`
- `outputs/tables/bargaining_wage_results_python.csv`
- `outputs/tables/automation_shock_results_python.csv`
- `outputs/tables/labor_r_results.csv`
- `outputs/tables/labor_stata_results.csv`
- `outputs/tables/julia_labor_results.csv`
- `outputs/figures/productivity_wage_share_python.png`
- `outputs/figures/wage_productivity_divergence_python.png`
- `outputs/figures/social_reproduction_gap_python.png`
- `outputs/figures/time_poverty_python.png`
- `outputs/figures/bargaining_wage_scenarios_python.png`
- `outputs/figures/automation_shock_python.png`
- `outputs/figures/labor_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a full labor-economics microdata project, national-accounts decomposition, unionization dataset, time-use survey, or econometric wage model. Its purpose is to make the article's conceptual claims computationally inspectable.
