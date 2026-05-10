# Information, Uncertainty, and Imperfect Markets

This folder is the article-level research package for:

**Information, Uncertainty, and Imperfect Markets**

It is designed as an economist-grade companion workflow for studying asymmetric information, adverse selection, moral hazard, signaling, screening, consumer opacity, disclosure, costly search, information quality, credit rationing, and robustness under deep uncertainty.

## Standard Economic Systems Stack

This repository standardizes Economic Systems article companions around:

- **Python** — adverse-selection simulations, hidden-action effort models, signal credibility, information-search value, robustness scenarios, visualization
- **R** — market-quality summaries, screening/disclosure comparisons, uncertainty and robustness graphics
- **Stata** — applied economics replication workflows and imperfect-market indicator tables
- **SQL** — structured market, type, signal, search, disclosure, risk, and uncertainty metadata
- **Julia** — numerical adverse-selection, search-cost, and robustness simulations

## Research Questions

This article companion workflow supports questions such as:

1. How does type pooling degrade market quality under asymmetric information?
2. How can adverse selection drive high-quality actors out of a market?
3. How does hidden action create moral hazard after contracts are signed?
4. When does a signal become credible because it is costly for low-quality actors to imitate?
5. How do search costs and information-processing costs limit decision quality?
6. How do disclosure, certification, warranties, audits, and screening improve market legibility?
7. How do decisions change under deep uncertainty, where probabilities are not stable or known?
8. How can Python, R, Stata, SQL, and Julia make information assumptions transparent?

## Core Model Ideas

```text
Expected utility under risk:
EU = Σ p_i u(x_i)
```

```text
Adverse selection / pooled value:
E(V) = qV_H + (1 - q)V_L
```

```text
Hidden action:
y = f(e, ε)
```

```text
Signal credibility:
c_H(s) < c_L(s)
```

```text
Knightian uncertainty:
p ∈ P
```

```text
Effective decision value:
D* = B(I) - C(I)
```

```text
Robustness under deep uncertainty:
R(a) = min_{p ∈ P} U(a, p)
```

## Folder Structure

```text
information-uncertainty-imperfect-markets/
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

- `data/processed/market_quality_types.csv`
- `data/processed/credit_risk_types.csv`
- `data/processed/signaling_scenarios.csv`
- `data/processed/information_search_scenarios.csv`
- `data/processed/uncertainty_scenarios.csv`
- `data/processed/consumer_complexity_scenarios.csv`
- `data/processed/information_uncertainty_imperfect_markets.sqlite`
- `outputs/tables/adverse_selection_results_python.csv`
- `outputs/tables/moral_hazard_results_python.csv`
- `outputs/tables/signal_credibility_results_python.csv`
- `outputs/tables/information_search_results_python.csv`
- `outputs/tables/robustness_results_python.csv`
- `outputs/tables/consumer_opacity_results_python.csv`
- `outputs/tables/information_uncertainty_r_results.csv`
- `outputs/tables/information_uncertainty_stata_results.csv`
- `outputs/tables/julia_information_uncertainty_results.csv`
- `outputs/figures/adverse_selection_pooled_value_python.png`
- `outputs/figures/moral_hazard_effort_python.png`
- `outputs/figures/signal_credibility_python.png`
- `outputs/figures/information_search_net_value_python.png`
- `outputs/figures/robustness_scenario_payoffs_python.png`
- `outputs/figures/consumer_opacity_python.png`
- `outputs/figures/information_uncertainty_r.png`

## Notes

This is a stylized, reproducible teaching and research scaffold. It is not a full econometric model, credit-risk system, antitrust dataset, supervisory stress test, or disclosure-policy evaluation. Its purpose is to make the article's conceptual claims computationally inspectable.
