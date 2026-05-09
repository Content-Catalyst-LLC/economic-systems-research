.headers on
.mode column

.print "Quarterly recession summary"
SELECT
    recession_indicator,
    COUNT(*) AS observations,
    ROUND(AVG(unemployment_rate), 2) AS avg_unemployment_rate,
    ROUND(AVG(real_gdp_growth_annualized), 2) AS avg_real_gdp_growth_annualized,
    ROUND(AVG(output_gap_pct), 2) AS avg_output_gap_pct,
    ROUND(AVG(federal_funds_rate), 2) AS avg_federal_funds_rate
FROM quarterly_indicators
GROUP BY recession_indicator;

.print ""
.print "Worst quarters by output gap"
SELECT
    date,
    ROUND(output_gap_pct, 2) AS output_gap_pct,
    ROUND(unemployment_rate, 2) AS unemployment_rate,
    recession_indicator
FROM quarterly_indicators
WHERE output_gap_pct IS NOT NULL
ORDER BY output_gap_pct ASC
LIMIT 10;

.print ""
.print "Largest quarterly unemployment increases"
SELECT
    date,
    ROUND(delta_unemployment_rate, 2) AS delta_unemployment_rate,
    ROUND(real_gdp_growth_annualized, 2) AS real_gdp_growth_annualized,
    recession_indicator
FROM quarterly_indicators
WHERE delta_unemployment_rate IS NOT NULL
ORDER BY delta_unemployment_rate DESC
LIMIT 10;

.print ""
.print "Simple Okun-style covariance inputs"
SELECT
    COUNT(*) AS observations,
    ROUND(AVG(real_gdp_growth_annualized), 3) AS avg_gdp_growth,
    ROUND(AVG(delta_unemployment_rate), 3) AS avg_delta_unemployment
FROM quarterly_indicators
WHERE real_gdp_growth_annualized IS NOT NULL
  AND delta_unemployment_rate IS NOT NULL;
