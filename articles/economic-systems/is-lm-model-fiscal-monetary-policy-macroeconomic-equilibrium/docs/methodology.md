# Methodology

## Purpose

This article companion turns the IS–LM model into a reproducible computational workflow.

The workflow:

1. Defines a baseline linear IS–LM model.
2. Solves for macroeconomic equilibrium output and interest rates.
3. Creates fiscal-policy, monetary-policy, crowding-out, and liquidity-trap scenarios.
4. Calculates comparative statics and policy multipliers.
5. Produces article-ready diagrams of IS and LM curves.
6. Exports model parameters, scenario results, and figures.
7. Replicates the same logic across Python, R, Stata, SQL, and Julia.

## Baseline Linear Model

The goods-market equilibrium condition is:

```text
IS: Y = alpha - beta * r + fiscal_shift
```

The money-market equilibrium condition is:

```text
LM: r = gamma * Y - money_shift
```

The equilibrium is:

```text
Y* = (alpha + beta * money_shift + fiscal_shift) / (1 + beta * gamma)
r* = gamma * Y* - money_shift
```

## Interpretation

- A positive fiscal shift raises autonomous demand and shifts the IS curve right.
- A positive money shift lowers the interest rate associated with a given level of output and shifts the LM curve right/down.
- A larger `beta` makes investment more interest sensitive.
- A larger `gamma` makes the LM curve steeper.
- A smaller `gamma` approximates a flatter LM curve and stronger fiscal effects.
- A very small `gamma` can be used to demonstrate liquidity-trap-style intuition.

## Limitations

This is a deliberately simplified short-run model. It assumes fixed prices, linear relationships, and stylized policy shocks. It is intended for conceptual clarity and reproducible teaching, not for forecasting or full structural macroeconomic analysis.
