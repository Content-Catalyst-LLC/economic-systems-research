.headers on
.mode column

.print "GDP and well-being dashboard"
SELECT
    scenario,
    consumption + investment + government + net_exports AS gdp,
    ROUND((health + education + income_security + housing + safety + social_connection + environment + time_balance) / 8.0, 3) AS wellbeing_score
FROM gdp_dashboard_scenarios
ORDER BY gdp DESC;

.print ""
.print "Inclusion"
SELECT
    "group",
    ROUND(
      0.22 * distribution +
      0.18 * mobility +
      0.20 * access +
      0.18 * voice +
      0.12 * regional_equity +
      0.10 * service_reach,
      3
    ) AS inclusion_score
FROM inclusion_scenarios
ORDER BY inclusion_score DESC;

.print ""
.print "Sustainability stocks"
SELECT
    scenario,
    ROUND(
      0.26 * natural_capital +
      0.22 * human_capital +
      0.20 * institutional_trust +
      0.16 * produced_capital +
      0.08 * (1 - maintenance_gap) +
      0.08 * (1 - ecological_pressure),
      3
    ) AS sustainability_score
FROM sustainability_stocks
ORDER BY sustainability_score DESC;

.print ""
.print "Adjusted progress"
SELECT
    scenario,
    current_benefits,
    current_benefits - social_costs - ecological_costs - defensive_expenditure + unpaid_care_value + public_goods_value AS adjusted_progress,
    ROUND((current_benefits - social_costs - ecological_costs - defensive_expenditure + unpaid_care_value + public_goods_value) / current_benefits, 3) AS adjusted_progress_ratio
FROM adjusted_progress
ORDER BY adjusted_progress_ratio DESC;

.print ""
.print "Capability conversion"
SELECT
    household_type,
    ROUND(
      0.18 * resources +
      0.20 * public_goods +
      0.16 * health_conversion +
      0.16 * education_conversion +
      0.12 * transport_access +
      0.12 * care_support +
      0.06 * (1 - discrimination_barrier),
      3
    ) AS capability_score
FROM capability_conversion
ORDER BY capability_score DESC;

.print ""
.print "Care and time use"
SELECT
    "group",
    paid_work_hours + unpaid_care_hours AS total_work_hours,
    unpaid_care_hours,
    leisure_hours,
    time_stress,
    support_services
FROM care_time_use
ORDER BY time_stress DESC;

.print ""
.print "Subjective well-being"
SELECT
    community,
    income_index,
    ROUND(
      0.28 * life_satisfaction +
      0.20 * (1 - stress) +
      0.20 * meaning +
      0.18 * social_trust +
      0.14 * (1 - loneliness),
      3
    ) AS subjective_wellbeing_score
FROM subjective_wellbeing
ORDER BY subjective_wellbeing_score DESC;

.print ""
.print "Indicator governance"
SELECT
    system,
    ROUND(
      0.14 * clarity +
      0.20 * multidimensionality +
      0.16 * public_legibility +
      0.16 * (1 - gaming_risk) +
      0.20 * policy_linkage +
      0.14 * local_relevance,
      3
    ) AS governance_usefulness_score
FROM indicator_governance
ORDER BY governance_usefulness_score DESC;
