.headers on
.mode column

.print "Baseline household budget and fragility"
SELECT
    household_group,
    income + transfers AS monthly_income_support,
    rent + food + transport + utilities + health AS essentials_spending,
    ROUND((rent + food + transport + utilities + health) / (income + transfers), 3) AS essentials_ratio,
    income + transfers + liquid_assets - debt_service - other_fixed_burdens -
      (rent + food + transport + utilities + health + other) AS saving,
    ROUND((rent + food + transport + utilities + health + debt_service + other_fixed_burdens) /
      (income + transfers + liquid_assets), 3) AS fragility_ratio
FROM household_profiles
ORDER BY fragility_ratio DESC;

.print ""
.print "Time poverty indicators"
SELECT
    household_group,
    paid_labor_hours,
    care_hours,
    commute_hours,
    household_admin_hours,
    ROUND(24 - paid_labor_hours - care_hours - commute_hours - household_admin_hours, 2) AS rest_discretionary_hours,
    CASE
      WHEN 24 - paid_labor_hours - care_hours - commute_hours - household_admin_hours < 8 THEN 'time poor'
      ELSE 'not time poor'
    END AS time_status
FROM household_profiles
ORDER BY rest_discretionary_hours ASC;

.print ""
.print "Public goods support scenarios"
SELECT
    scenario,
    transport_private_cost_reduction,
    health_private_cost_reduction,
    childcare_private_cost_reduction,
    time_savings_hours,
    institutional_support_index
FROM public_goods_scenarios
ORDER BY institutional_support_index DESC;
