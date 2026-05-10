# Behavioral Economics and Bounded Rationality

This folder is the article-level research package for:

**Behavioral Economics and Bounded Rationality**

It is designed as an economist-grade companion workflow for studying bounded rationality, satisficing, present bias, loss aversion, probability weighting, framing effects, defaults, social norms, administrative burden, policy take-up, and sustainable decision environments.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — behavioral choice simulations, present-bias valuation, loss-aversion curves, defaults, take-up modeling, visualization
- **R** — behavioral summaries, framing/default experiments, administrative-burden metrics, scenario graphics
- **Stata** — applied economics replication workflows and behavioral-indicator tables
- **SQL** — structured decision, option, frame, default, social-norm, and administrative-burden metadata
- **Julia** — numerical behavioral-choice simulation, dynamic present-bias models, and take-up trajectories

## Research Questions

This article companion workflow supports questions such as:

1. How does satisficing differ from global optimization when search is costly?
2. How does present bias change the valuation of delayed benefits?
3. How do loss aversion and reference points alter welfare evaluation?
4. How do probability weighting and salience alter risk perception?
5. How do defaults, framing, and administrative burden change policy take-up?
6. How do social norms and peer signals influence cooperation and compliance?
7. How can Python, R, Stata, SQL, and Julia make behavioral assumptions transparent?

## Core Model Ideas

```text
Satisficing:
Choose x* such that U(x*) ≥ U_bar
```

```text
Quasi-hyperbolic discounting:
U = u(c_0) + β Σ δ^t u(c_t)
```

```text
Loss aversion:
v(x) = x^α for x ≥ 0
v(x) = -λ(-x)^β for x < 0
```

```text
Probability weighting:
π(p) ≠ p
```

```text
Cognitive-cost adjusted utility:
U*(x) = U(x) - κC(x)
```

```text
Take-up probability:
P(take-up) = f(B, C, D, S, T)
```

## Folder Structure

```text
behavioral-economics-bounded-rationality/
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

- `data/processed/choice_options.csv`
- `data/processed/present_bias_scenarios.csv`
- `data/processed/framing_default_scenarios.csv`
- `data/processed/risk_probability_scenarios.csv`
- `data/processed/social_norm_scenarios.csv`
- `data/processed/admin_burden_scenarios.csv`
- `data/processed/behavioral_economics_bounded_rationality.sqlite`
- `outputs/tables/satisficing_choice_results_python.csv`
- `outputs/tables/present_bias_results_python.csv`
- `outputs/tables/loss_aversion_results_python.csv`
- `outputs/tables/default_take_up_results_python.csv`
- `outputs/tables/admin_burden_results_python.csv`
- `outputs/tables/social_norm_results_python.csv`
- `outputs/tables/behavioral_r_results.csv`
- `outputs/tables/behavioral_stata_results.csv`
- `outputs/tables/julia_behavioral_results.csv`
- `outputs/figures/loss_aversion_value_function_python.png`
- `outputs/figures/present_bias_discounting_python.png`
- `outputs/figures/default_take_up_python.png`
- `outputs/figures/admin_burden_take_up_python.png`
- `outputs/figures/social_norm_compliance_python.png`
- `outputs/figures/behavioral_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a full behavioral experiment package, cognitive model, or policy evaluation dataset. Its purpose is to make the article's conceptual claims computationally inspectable.
