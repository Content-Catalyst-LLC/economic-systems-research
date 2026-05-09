# Methodology

## Purpose

This article companion uses a stylized multi-sector economy to connect production, distribution, and exchange in one reproducible workflow.

The workflow:

1. Creates a synthetic sector table with labor shares, non-labor income shares, ecological intensity, employment intensity, trade exposure, and public-good dependence.
2. Creates an inter-industry input-output matrix.
3. Creates baseline and alternative final-demand/exchange scenarios.
4. Solves the Leontief input-output system.
5. Calculates total output, indirect output requirements, labor income, non-labor income, ecological throughput, and exchange-dependency indicators.
6. Summarizes distributional structure through labor share and income-claim metrics.
7. Exports figures, tables, and a SQLite database.
8. Replicates the logic across Python, R, Stata, SQL, and Julia.

## Key Concepts

- Production is organized capability, not merely technical transformation.
- Distribution is built into economic structure through wages, profits, rents, public provision, and financial claims.
- Exchange coordinates specialization but also creates dependency.
- Input-output analysis reveals interdependence among sectors.
- Labor-share analysis reveals whether gains from production flow toward labor or away from it.
- Ecological throughput shows that production and exchange remain material processes even in service and digital economies.

## Limitations

The workflow uses stylized data for teaching and article support. Applied analysis should use official input-output tables, national accounts, labor-income data, trade data, household surveys, and ecological footprint indicators.
