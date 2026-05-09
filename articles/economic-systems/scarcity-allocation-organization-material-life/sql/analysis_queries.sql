.headers on
.mode column

.print "Allocation scenario summary"
SELECT
    s.scenario,
    ROUND(SUM(s.share * 1000), 2) AS total_allocation,
    ROUND(SUM(s.share * 1000 * p.essentiality), 2) AS essentiality_weighted_total,
    ROUND(SUM(s.share * 1000 * p.resilience_value), 2) AS resilience_weighted_total
FROM allocation_scenarios s
JOIN allocation_priorities p ON s.priority = p.priority
GROUP BY s.scenario
ORDER BY resilience_weighted_total DESC;

.print ""
.print "Effective access by household group"
SELECT
    household_group,
    ROUND(need_index, 2) AS need_index,
    ROUND(income_command, 2) AS income_command,
    ROUND(price_index, 2) AS price_index,
    ROUND(institutional_access, 2) AS institutional_access,
    ROUND(
      0.35 * income_command +
      0.35 * institutional_access +
      0.20 * (1 - price_index) +
      0.10 * need_index,
      3
    ) AS effective_access
FROM access_households
ORDER BY effective_access ASC;

.print ""
.print "Ecological regeneration condition"
SELECT
    scenario,
    resource_use,
    regenerative_capacity,
    ecological_restoration,
    CASE
      WHEN resource_use <= regenerative_capacity + ecological_restoration THEN 'within regeneration plus restoration'
      ELSE 'use exceeds regeneration plus restoration'
    END AS ecological_condition
FROM reproduction_constraints;
