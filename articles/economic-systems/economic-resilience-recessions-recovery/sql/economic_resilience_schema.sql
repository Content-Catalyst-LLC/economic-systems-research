-- Economic Resilience SQL Schema
-- Purpose: Transparent relational structure for article-level economic indicators.

CREATE TABLE IF NOT EXISTS economic_resilience_indicators (
    date TEXT PRIMARY KEY,
    unemployment_rate REAL,
    real_gdp REAL,
    federal_funds_rate REAL,
    recession_indicator INTEGER,
    real_gdp_growth_annualized REAL,
    unemployment_12m_low REAL,
    unemployment_gap_from_12m_low REAL
);

CREATE VIEW IF NOT EXISTS recession_period_summary AS
SELECT
    recession_indicator,
    COUNT(*) AS observations,
    AVG(unemployment_rate) AS avg_unemployment_rate,
    AVG(real_gdp_growth_annualized) AS avg_real_gdp_growth_annualized,
    AVG(federal_funds_rate) AS avg_federal_funds_rate
FROM economic_resilience_indicators
GROUP BY recession_indicator;
