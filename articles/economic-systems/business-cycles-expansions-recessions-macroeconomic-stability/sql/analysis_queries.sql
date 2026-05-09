.headers on
.mode column

.print "Business-cycle phase summary"
SELECT
    business_cycle_phase,
    COUNT(*) AS observations,
    ROUND(AVG(real_gdp_growth_annualized), 2) AS avg_real_gdp_growth,
    ROUND(AVG(unemployment_rate), 2) AS avg_unemployment,
    ROUND(AVG(output_gap_pct), 2) AS avg_output_gap,
    ROUND(AVG(payroll_growth_yoy_pct), 2) AS avg_payroll_growth,
    ROUND(AVG(industrial_production_yoy_pct), 2) AS avg_industrial_production_growth,
    ROUND(AVG(retail_sales_yoy_pct), 2) AS avg_retail_sales_growth,
    ROUND(AVG(real_income_yoy_pct), 2) AS avg_real_income_growth,
    ROUND(AVG(federal_funds_rate), 2) AS avg_federal_funds_rate
FROM quarterly_indicators
GROUP BY business_cycle_phase;

.print ""
.print "Largest negative GDP growth quarters"
SELECT
    date,
    ROUND(real_gdp_growth_annualized, 2) AS real_gdp_growth_annualized,
    ROUND(unemployment_rate, 2) AS unemployment_rate,
    ROUND(output_gap_pct, 2) AS output_gap_pct,
    business_cycle_phase
FROM quarterly_indicators
WHERE real_gdp_growth_annualized IS NOT NULL
ORDER BY real_gdp_growth_annualized ASC
LIMIT 12;

.print ""
.print "Deepest negative output gaps"
SELECT
    date,
    ROUND(output_gap_pct, 2) AS output_gap_pct,
    ROUND(unemployment_rate, 2) AS unemployment_rate,
    ROUND(real_gdp_growth_annualized, 2) AS real_gdp_growth_annualized,
    business_cycle_phase
FROM quarterly_indicators
WHERE output_gap_pct IS NOT NULL
ORDER BY output_gap_pct ASC
LIMIT 12;

.print ""
.print "Rolling volatility summary by phase"
SELECT
    business_cycle_phase,
    ROUND(AVG(rolling_gdp_volatility_12q), 2) AS avg_rolling_gdp_volatility,
    ROUND(AVG(rolling_unemployment_volatility_12q), 2) AS avg_rolling_unemployment_volatility
FROM quarterly_indicators
WHERE rolling_gdp_volatility_12q IS NOT NULL
GROUP BY business_cycle_phase;
