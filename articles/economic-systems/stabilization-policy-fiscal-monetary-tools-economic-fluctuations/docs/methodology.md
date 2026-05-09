# Methodology

## Purpose

This article companion uses public macroeconomic indicators to study stabilization policy during expansions, recessions, output-gap episodes, unemployment increases, and recoveries.

The workflow is intentionally transparent:

1. Fetch macroeconomic, fiscal, and monetary indicators from public FRED CSV endpoints.
2. Build monthly and quarterly policy panels.
3. Convert selected monthly indicators to quarterly frequency.
4. Merge real GDP, potential GDP, monetary-policy rates, inflation, unemployment, payroll employment, and government-spending indicators.
5. Calculate output gaps, inflation, real GDP growth, unemployment changes, policy-rate changes, and government-spending growth.
6. Identify recession episodes from the NBER-based recession indicator.
7. Calculate policy-response metrics around recessions.
8. Estimate a simple Taylor-rule-style monetary-policy benchmark.
9. Export figures, tables, and a SQLite database.
10. Use Julia to simulate output-gap recovery under different stabilization strengths.

## Why These Measures Matter

- **Output gap** approximates macroeconomic slack or overheating.
- **Unemployment rate** tracks labor-market stress.
- **Federal funds rate** provides monetary-policy stance.
- **Inflation** shapes monetary-policy trade-offs.
- **Government consumption and investment** provides a public-demand indicator.
- **Recession indicator** supports NBER-based stabilization timing.
- **Policy-response episodes** help compare policy behavior across downturns.

## Limitations

This workflow is designed for public education, article support, and reproducible macroeconomic analysis. It is not a complete DSGE model, fiscal multiplier estimate, or formal policy evaluation. The Taylor-rule-style benchmark is illustrative, not prescriptive.
