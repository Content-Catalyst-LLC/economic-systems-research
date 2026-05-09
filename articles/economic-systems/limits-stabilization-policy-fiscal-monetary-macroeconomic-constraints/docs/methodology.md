# Methodology

## Purpose

This article companion uses public macroeconomic indicators to examine the constraints that can limit stabilization policy.

The workflow is intentionally transparent:

1. Fetch macroeconomic, fiscal, and monetary indicators from public FRED CSV endpoints.
2. Build monthly and quarterly panels.
3. Convert selected monthly indicators to quarterly frequency.
4. Merge real GDP, potential GDP, inflation, unemployment, policy rates, long-term interest rates, and debt-to-GDP indicators.
5. Calculate output gaps, inflation, real GDP growth, policy-rate levels, interest-growth gaps, and debt-stabilizing balance proxies.
6. Identify recession and expansion phases.
7. Construct indicators for inflation constraints, fiscal-space constraints, lower-bound constraints, and crowding-out risk.
8. Export figures, tables, and a SQLite database.
9. Use Julia to simulate debt dynamics under different growth, interest-rate, and primary-balance assumptions.

## Key Concepts

- **Inflation constraint:** Expansionary policy may raise prices rather than real output when supply is constrained or the economy is near capacity.
- **Crowding out:** Public borrowing may raise interest rates or absorb financial resources, reducing private investment.
- **Debt sustainability:** Debt remains sustainable when the government can meet current and future obligations without default or exceptional support.
- **Lower-bound constraint:** Monetary policy may be limited when interest rates are already near zero.
- **Policy lag:** Stabilization can arrive too late if recognition, decision, implementation, or impact lags are long.

## Limitations

This workflow is designed for article support, public education, and reproducible macroeconomic analysis. It is not a complete debt-sustainability analysis, structural macroeconomic model, or central-bank policy rule.
