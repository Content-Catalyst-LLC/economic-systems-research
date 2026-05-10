# Externalities, Public Goods, and Collective Provision

This folder is the article-level research package for:

**Externalities, Public Goods, and Collective Provision**

It is designed as an economist-grade companion workflow for studying spillover harms, shared benefits, public goods, free-rider problems, collective financing, burden sharing, ecological thresholds, social-cost pricing, and the institutional design of collective provision.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — social-cost curves, public-good underprovision, burden-sharing scenarios, threshold simulations, visualization
- **R** — externality/public-good summaries, contribution scenarios, distributional burden metrics, scenario graphics
- **Stata** — applied economics replication workflows and public-good indicator tables
- **SQL** — structured externality, public-good, contribution, finance, and threshold metadata
- **Julia** — numerical social optimum solving, contribution dynamics, and threshold simulations

## Research Questions

This article companion workflow supports questions such as:

1. How does private output differ from socially efficient output when marginal external costs are included?
2. How do positive externalities and public goods create underprovision?
3. How do free-rider incentives affect voluntary contribution to shared goods?
4. How do tax, subsidy, borrowing, and pooled-fund scenarios change collective provision capacity?
5. How are external costs distributed across household groups, regions, income classes, and generations?
6. How do ecological or infrastructural thresholds change the economics of delay?
7. How can Python, R, Stata, SQL, and Julia make collective-provision assumptions transparent?

## Core Model Ideas

```text
Marginal social cost:
MSC = MPC + MEC
```

```text
Marginal social benefit:
MSB = MPB + MEB
```

```text
Public-good benefit:
MSB = Σ MB_i
```

```text
Public-good contribution:
G = Σ c_i
```

```text
Corrective tax:
t* = MEC
```

```text
Collective provision capacity:
CP = T + B + O
```

```text
Threshold condition:
D_t < T_c
```

## Folder Structure

```text
externalities-public-goods-collective-provision/
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

- `data/processed/externality_scenarios.csv`
- `data/processed/public_good_scenarios.csv`
- `data/processed/contribution_scenarios.csv`
- `data/processed/collective_finance_scenarios.csv`
- `data/processed/burden_distribution_groups.csv`
- `data/processed/externalities_public_goods_collective_provision.sqlite`
- `outputs/tables/private_social_optimum_python.csv`
- `outputs/tables/public_good_underprovision_python.csv`
- `outputs/tables/free_rider_contribution_python.csv`
- `outputs/tables/burden_distribution_python.csv`
- `outputs/tables/threshold_damage_results_python.csv`
- `outputs/tables/collective_finance_results_python.csv`
- `outputs/tables/externalities_public_goods_r_results.csv`
- `outputs/tables/externalities_public_goods_stata_results.csv`
- `outputs/tables/julia_externality_public_good_results.csv`
- `outputs/figures/private_vs_social_cost_python.png`
- `outputs/figures/public_good_underprovision_python.png`
- `outputs/figures/free_rider_contributions_python.png`
- `outputs/figures/burden_distribution_python.png`
- `outputs/figures/threshold_damage_python.png`
- `outputs/figures/collective_finance_capacity_python.png`
- `outputs/figures/externalities_public_goods_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a full environmental-economics model, public-finance microsimulation, or welfare-economics package. Its purpose is to make the article's conceptual claims computationally inspectable.
