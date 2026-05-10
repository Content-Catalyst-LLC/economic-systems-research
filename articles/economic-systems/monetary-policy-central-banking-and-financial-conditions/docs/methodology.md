# Methodology

## Purpose

This article companion models monetary policy, central banking, and financial conditions as interacting rate, credit, liquidity, valuation, exchange-rate, public-debt, and investment systems.

The workflow:

1. Creates stylized policy-rate, debt-service, financial-conditions, asset-valuation, bank-liquidity, open-economy, public-debt, and sustainable-investment scenarios.
2. Calculates real interest rates from nominal rates and expected inflation.
3. Evaluates household and firm debt-service stress.
4. Applies a stylized policy reaction function.
5. Builds a composite financial-conditions index.
6. Estimates present-value sensitivity to rate changes.
7. Evaluates bank liquidity coverage and deposit-outflow stress.
8. Scores exchange-rate pressure and open-economy exposure.
9. Calculates public debt-service pressure under higher rates.
10. Evaluates long-horizon investment affordability under financing-cost changes.
11. Exports tables, figures, and a SQLite database.
12. Replicates the logic across Python, R, Stata, SQL, and Julia.

## Key Concepts

- Monetary policy is institutional transmission, not a frictionless lever.
- Financial conditions are broader than the policy rate.
- Real borrowing costs depend on nominal rates and expected inflation.
- Debt-service exposure depends on balance-sheet structure and repricing speed.
- Asset values are sensitive to discount rates.
- Bank liquidity stress depends on liquid assets, outflows, collateral, and confidence.
- Open economies face exchange-rate and capital-flow constraints.
- Monetary tightening affects public debt service and fiscal space.
- Sustainable investment depends on long-term funding conditions, not only policy ambition.

## Limitations

The workflow uses stylized synthetic data for teaching and article support. Applied analysis should extend it with central-bank policy series, yield curves, credit spreads, bank balance sheets, household debt surveys, firm-level finance data, exchange rates, market liquidity data, public-debt maturity profiles, and green-investment financing datasets.
