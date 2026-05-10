# Methodology

## Purpose

This article companion models inflation, energy shocks, and supply constraints as interacting price, energy, input-cost, household, import, bottleneck, market-power, and resilience-policy systems.

The workflow:

1. Creates stylized price index, energy pass-through, household burden, import shock, supply bottleneck, market-power, and resilience policy scenarios.
2. Calculates inflation rates from price levels.
3. Estimates energy and input-cost pass-through into sector prices.
4. Calculates real wage erosion under price-level changes.
5. Evaluates household energy burden across income groups.
6. Models import-price transmission from world prices and exchange-rate movements.
7. Evaluates bottleneck stress across capital, labor, energy, logistics, and supply availability.
8. Evaluates price amplification under concentrated market structure.
9. Scores resilience policy options including strategic reserves, grid investment, public transit, storage, energy efficiency, and supply diversification.
10. Exports tables, figures, and a SQLite database.
11. Replicates the logic across Python, R, Stata, SQL, and Julia.

## Key Concepts

- Inflation is a sustained rise in the general price level, not a single isolated price movement.
- Energy is a system-wide input that enters transport, food, manufacturing, housing, public services, and digital infrastructure.
- Supply constraints can generate inflation without a conventional demand boom.
- Cost pass-through depends on sector structure, competition, contracts, margins, and bargaining power.
- Household energy burden reveals the distributional consequences of energy inflation.
- Import-price shocks can be intensified by exchange-rate movements.
- Market concentration can amplify price increases during supply stress.
- Resilience-oriented anti-inflation strategy requires infrastructure, energy transition, storage, redundancy, public capacity, and ecological adaptation.

## Limitations

The workflow uses stylized synthetic data for teaching and article support. Applied analysis should extend it with CPI/PCE data, energy price series, input-output tables, household expenditure surveys, sectoral price data, import price indices, exchange-rate data, market-concentration measures, infrastructure capacity data, climate-risk data, and supply-chain indicators.
