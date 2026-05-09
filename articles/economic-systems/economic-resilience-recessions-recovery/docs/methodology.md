# Methodology

## Purpose

This article companion uses public macroeconomic indicators to examine recession and recovery dynamics in a reproducible workflow.

The methodology is intentionally transparent:

1. Fetch macroeconomic time series from FRED CSV endpoints.
2. Build monthly and quarterly panels.
3. Convert selected monthly indicators to quarterly frequency.
4. Merge real GDP and potential GDP.
5. Calculate GDP growth, output gaps, unemployment changes, payroll growth, industrial production growth, and recession flags.
6. Identify recession episodes from the recession indicator.
7. Calculate recovery metrics, including time to regain pre-recession GDP and employment levels.
8. Estimate a simple Okun-style relationship between GDP growth and unemployment changes.
9. Export tables, figures, and a SQLite database.

## Why These Measures Matter

- **Unemployment rate** measures labor-market stress.
- **Real GDP growth** measures aggregate output movement.
- **Output gap** approximates the distance between actual and potential production.
- **Payroll employment** measures employment recovery.
- **Industrial production** provides a production-side indicator.
- **Federal funds rate** provides monetary-policy context.
- **Recession indicator** provides NBER-based recession dating.

## Limitations

This workflow is intended for teaching, article support, and reproducible analysis. It does not estimate a complete macroeconomic model. It should be extended before being used for formal forecasting or policy evaluation.
