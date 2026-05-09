.headers on
.mode column

.print "Production, distribution, and exchange scenario summary"
SELECT
    scenario,
    ROUND(SUM(total_output), 2) AS total_output,
    ROUND(SUM(labor_income), 2) AS labor_income,
    ROUND(SUM(non_labor_income), 2) AS non_labor_income,
    ROUND(SUM(labor_income) / SUM(total_output), 3) AS labor_share,
    ROUND(SUM(non_labor_income) / SUM(total_output), 3) AS non_labor_share,
    ROUND(SUM(exchange_dependency) / SUM(total_output), 3) AS exchange_dependency_ratio,
    ROUND(SUM(ecological_throughput) / SUM(total_output), 3) AS throughput_per_output
FROM production_distribution_exchange_results
GROUP BY scenario
ORDER BY total_output DESC;

.print ""
.print "Baseline sector distribution"
SELECT
    r.sector_code,
    s.sector,
    ROUND(r.total_output, 2) AS total_output,
    ROUND(r.labor_income, 2) AS labor_income,
    ROUND(r.non_labor_income, 2) AS non_labor_income,
    ROUND(r.ecological_throughput, 2) AS ecological_throughput,
    ROUND(r.exchange_dependency, 2) AS exchange_dependency
FROM production_distribution_exchange_results r
JOIN production_sectors s ON r.sector_code = s.sector_code
WHERE r.scenario = 'baseline'
ORDER BY r.total_output DESC;

.print ""
.print "Highest inter-industry input requirements"
SELECT
    supplying_sector,
    purchasing_sector,
    input_requirement
FROM input_output_requirements
ORDER BY input_requirement DESC
LIMIT 12;
