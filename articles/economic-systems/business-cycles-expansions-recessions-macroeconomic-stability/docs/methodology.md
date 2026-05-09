# Methodology

## Purpose

This article companion uses public macroeconomic indicators to study business-cycle phases, recession dating, expansions, recoveries, output gaps, macroeconomic volatility, and stabilization policy.

The workflow is intentionally transparent:

1. Fetch macroeconomic time series from FRED CSV endpoints.
2. Build monthly and quarterly macroeconomic panels.
3. Convert selected monthly indicators to quarterly frequency.
4. Merge real GDP and potential GDP.
5. Calculate GDP growth, output gaps, unemployment changes, payroll growth, industrial production growth, income growth, retail-sales growth, and inflation.
6. Identify recession episodes from the NBER-based recession indicator.
7. Identify expansions as trough-to-peak periods.
8. Calculate duration, amplitude, and recovery metrics.
9. Estimate basic phase summaries and an output-gap persistence model.
10. Export figures, tables, and a SQLite database.

## Why These Measures Matter

- **Real GDP** measures aggregate output.
- **Potential GDP** provides a benchmark for output-gap analysis.
- **Unemployment rate** measures labor-market stress.
- **Payroll employment** tracks broad employment movement.
- **Industrial production** provides a production-side indicator.
- **Retail sales** provide a demand-side activity indicator.
- **Real disposable personal income** connects macro cycles to household purchasing power.
- **Federal funds rate** provides monetary-policy context.
- **Recession indicator** supports reproducible NBER-based cycle dating.

## Limitations

This workflow is designed for public education, article support, and reproducible macroeconomic analysis. It does not replace formal business-cycle dating by the NBER Business Cycle Dating Committee and should not be treated as an official recession-dating model.
