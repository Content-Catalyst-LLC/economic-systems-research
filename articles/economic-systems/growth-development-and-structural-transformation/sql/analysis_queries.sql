.headers on
.mode column

.print "Growth and productivity"
SELECT
    scenario,
    period,
    output,
    labor,
    ROUND(output / labor, 3) AS labor_productivity
FROM growth_path_scenarios
ORDER BY scenario, period;

.print ""
.print "Sectoral shares and productivity"
WITH totals AS (
    SELECT scenario, SUM(sector_output) AS total_output, SUM(sector_labor) AS total_labor
    FROM sector_transformation_scenarios
    GROUP BY scenario
)
SELECT
    s.scenario,
    s.sector,
    ROUND(s.sector_output / t.total_output, 3) AS output_share,
    ROUND(s.sector_labor / t.total_labor, 3) AS labor_share,
    ROUND(s.sector_output / s.sector_labor, 3) AS sector_productivity
FROM sector_transformation_scenarios s
JOIN totals t ON s.scenario = t.scenario
ORDER BY s.scenario, sector_productivity DESC;

.print ""
.print "Development capability index"
SELECT
    scenario,
    ROUND(
      0.22 * income_index +
      0.20 * health_index +
      0.20 * education_index +
      0.22 * infrastructure_index +
      0.16 * security_index,
      3
    ) AS capability_index
FROM development_capability_scenarios
ORDER BY capability_index DESC;

.print ""
.print "Trade diversification"
SELECT
    scenario,
    export_concentration,
    manufacturing_export_share,
    technology_depth,
    ROUND(
      0.30 * (1 - export_concentration) +
      0.22 * manufacturing_export_share +
      0.24 * technology_depth +
      0.14 * (1 - terms_of_trade_volatility) +
      0.10 * foreign_exchange_resilience,
      3
    ) AS developmental_trade_score
FROM trade_export_diversification_scenarios
ORDER BY developmental_trade_score DESC;

.print ""
.print "Energy intensity and sustainable growth score"
SELECT
    scenario,
    output,
    energy_use,
    emissions,
    ROUND(energy_use / output, 3) AS energy_intensity,
    ROUND(emissions / output, 3) AS emissions_intensity,
    renewable_share,
    resource_stress
FROM energy_ecology_scenarios
ORDER BY energy_intensity ASC;

.print ""
.print "Developmental fragility"
SELECT
    scenario,
    external_debt_ratio,
    fx_debt_share,
    export_concentration,
    reserve_buffer,
    productivity_momentum,
    ROUND(
      0.22 * external_debt_ratio +
      0.20 * fx_debt_share +
      0.16 * short_term_debt_share +
      0.18 * export_concentration +
      0.14 * (1 - reserve_buffer) +
      0.10 * (1 - productivity_momentum),
      3
    ) AS middle_income_fragility_score
FROM debt_fragility_scenarios
ORDER BY middle_income_fragility_score DESC;
