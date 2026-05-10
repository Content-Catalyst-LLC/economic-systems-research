# Methodology

## Purpose

This article companion models finance, leverage, and systemic risk as balance-sheet, funding, collateral, network, and macroprudential problems.

The workflow:

1. Creates stylized institutional balance sheets and exposure data.
2. Calculates leverage, debt-to-equity, equity buffers, and loss amplification.
3. Evaluates asset-price shocks under different leverage levels.
4. Models collateral haircut shocks and margin-driven funding gaps.
5. Simulates fire-sale feedback loops over multiple periods.
6. Evaluates short-term funding gaps and liquid-asset coverage.
7. Models network contagion through an exposure matrix.
8. Evaluates household mortgage leverage and housing-price shocks.
9. Compares macroprudential buffer scenarios.
10. Evaluates climate/stranded-asset and sustainable-systems financial shocks.
11. Exports tables, figures, and a SQLite database.
12. Replicates the logic across Python, R, Stata, SQL, and Julia.

## Key Concepts

- Leverage is a structural amplifier of both returns and losses.
- Thin equity buffers make small asset losses systemically dangerous.
- Collateral haircuts and margin calls can force deleveraging.
- Fire sales are feedback loops, not isolated transactions.
- Systemic risk depends on correlation, common exposures, funding fragility, and network structure.
- Liquidity stress can destabilize apparently solvent institutions.
- Public backstops reduce crisis damage but can create moral hazard.
- Sustainable finance must evaluate whether leverage finances resilience or fragility.

## Limitations

The workflow uses stylized synthetic data for teaching and article support. Applied analysis should extend it with bank regulatory filings, supervisory datasets, interbank exposure data, derivatives data, market liquidity data, household mortgage data, climate stress-testing data, and macroprudential policy datasets.
