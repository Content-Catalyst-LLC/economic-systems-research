.headers on
.mode column

.print "Scenario-level output summary"
SELECT
    scenario,
    ROUND(SUM(final_demand), 2) AS total_final_demand,
    ROUND(SUM(total_output), 2) AS total_required_output,
    ROUND(SUM(indirect_output_requirement), 2) AS total_indirect_requirement,
    ROUND(AVG(output_multiplier), 3) AS avg_output_multiplier
FROM economic_system_results
GROUP BY scenario
ORDER BY total_required_output DESC;

.print ""
.print "Baseline sector distribution and ecological pressure"
SELECT
    r.sector_code,
    s.sector,
    ROUND(r.total_output, 2) AS total_output,
    ROUND(r.total_output * s.wage_share, 2) AS labor_income,
    ROUND(r.total_output * s.profit_share, 2) AS capital_income,
    ROUND(r.total_output * s.ecological_intensity, 2) AS ecological_pressure,
    ROUND(r.total_output * s.employment_intensity, 2) AS employment_requirement
FROM economic_system_results r
JOIN sectors s ON r.sector_code = s.sector_code
WHERE r.scenario = 'baseline'
ORDER BY total_output DESC;

.print ""
.print "Allocation profiles"
SELECT
    scenario,
    ROUND(consumption_share, 3) AS consumption,
    ROUND(investment_share, 3) AS investment,
    ROUND(public_provision_share, 3) AS public_provision,
    ROUND(restoration_share, 3) AS restoration,
    ROUND(investment_share + restoration_share, 3) AS future_capacity_share
FROM allocation_profiles
ORDER BY future_capacity_share DESC;
