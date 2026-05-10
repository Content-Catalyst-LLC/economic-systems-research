.headers on
.mode column

.print "Sector labor productivity, wage share, and unit labor cost"
SELECT
    sector,
    ROUND(output / hours_worked, 3) AS labor_productivity,
    ROUND(total_wages / output, 3) AS wage_share,
    ROUND((total_wages / hours_worked) / (output / hours_worked), 3) AS unit_labor_cost,
    employment_quality_index,
    care_intensity
FROM sector_labor_scenarios
ORDER BY labor_productivity DESC;

.print ""
.print "Wage-productivity divergence"
SELECT
    year,
    ROUND(productivity_index, 2) AS productivity_index,
    ROUND(wage_index, 2) AS wage_index,
    ROUND(productivity_index - wage_index, 2) AS divergence_index,
    ROUND(wage_index / productivity_index, 3) AS wage_productivity_ratio
FROM wage_productivity_time_series
ORDER BY year DESC
LIMIT 10;

.print ""
.print "Social reproduction adequacy"
SELECT
    household_type,
    wage_income,
    social_support,
    household_cost,
    care_reproduction_cost,
    wage_income + social_support - household_cost - care_reproduction_cost AS adequacy_gap,
    ROUND((wage_income + social_support) / (household_cost + care_reproduction_cost), 3) AS adequacy_ratio
FROM household_reproduction_scenarios
ORDER BY adequacy_gap ASC;

.print ""
.print "Time poverty"
SELECT
    worker_group,
    paid_work_time,
    care_time,
    household_time,
    commute_time,
    ROUND(24 - paid_work_time - care_time - household_time - commute_time, 2) AS rest_recovery_time
FROM time_use_scenarios
ORDER BY rest_recovery_time ASC;

.print ""
.print "Bargaining wage scenarios"
SELECT
    scenario,
    labor_productivity,
    bargaining_power,
    institutional_support,
    outside_option,
    ROUND(1.15 + 0.52 * labor_productivity + 1.15 * bargaining_power + 0.95 * institutional_support + 0.70 * outside_option, 3) AS modeled_wage
FROM bargaining_institution_scenarios
ORDER BY modeled_wage DESC;
