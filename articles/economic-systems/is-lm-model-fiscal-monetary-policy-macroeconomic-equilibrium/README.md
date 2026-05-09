# The IS–LM Model: Fiscal Policy, Monetary Policy, and Macroeconomic Equilibrium

This folder is the article-level research package for:

**The IS–LM Model: Fiscal Policy, Monetary Policy, and Macroeconomic Equilibrium**

It is designed as an economist-grade companion workflow for modeling goods-market equilibrium, money-market equilibrium, fiscal-policy shifts, monetary-policy shifts, crowding out, liquidity traps, interest sensitivity, and short-run macroeconomic equilibrium.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — model construction, equilibrium solving, comparative statics, visualization
- **R** — statistical and graphical replication of IS–LM policy scenarios
- **Stata** — applied macroeconomics replication workflows and scenario tables
- **SQL** — structured scenario metadata, model parameters, and reproducible query tables
- **Julia** — linear-equilibrium solving, simulation, optimization, and policy experiments

## Research Questions

This article companion workflow supports questions such as:

1. How do IS and LM equations jointly determine equilibrium output and interest rates?
2. How do fiscal-policy changes shift the IS curve?
3. How do monetary-policy changes shift the LM curve?
4. How does interest sensitivity of investment affect crowding out?
5. How does money-demand sensitivity affect monetary-policy transmission?
6. What happens to policy multipliers when the LM curve is flat, steep, or near a liquidity-trap case?
7. How can an abstract macroeconomic diagram be turned into transparent computational scenarios?

## Model Structure

A simple linear IS–LM model is represented as:

```text
IS: Y = alpha - beta * r + fiscal_shift
LM: r = gamma * Y - money_shift
```

Where:

- `Y` is output
- `r` is the interest rate
- `alpha` captures autonomous demand
- `beta` captures investment sensitivity to interest rates
- `gamma` captures the responsiveness of interest rates to output through money demand
- `fiscal_shift` captures expansionary or contractionary fiscal policy
- `money_shift` captures monetary easing or tightening

The scripts solve the equilibrium:

```text
Y* = (alpha + beta * money_shift + fiscal_shift) / (1 + beta * gamma)
r* = gamma * Y* - money_shift
```

## Folder Structure

```text
is-lm-model-fiscal-monetary-policy-macroeconomic-equilibrium/
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

- `data/processed/is_lm_baseline_parameters.csv`
- `data/processed/is_lm_policy_scenarios.csv`
- `data/processed/is_lm_scenario_results.csv`
- `data/processed/is_lm_model.sqlite`
- `outputs/tables/is_lm_comparative_statics_python.csv`
- `outputs/tables/is_lm_policy_multipliers_python.csv`
- `outputs/tables/is_lm_r_results.csv`
- `outputs/tables/is_lm_stata_results.csv`
- `outputs/tables/julia_is_lm_policy_results.csv`
- `outputs/figures/is_lm_baseline_python.png`
- `outputs/figures/is_lm_fiscal_shift_python.png`
- `outputs/figures/is_lm_monetary_shift_python.png`
- `outputs/figures/is_lm_policy_multipliers_python.png`
- `outputs/figures/is_lm_scenarios_r.png`

## Notes

This workflow is a teaching and research scaffold. It intentionally uses a simple linear IS–LM model so that fiscal and monetary comparative statics remain transparent.
