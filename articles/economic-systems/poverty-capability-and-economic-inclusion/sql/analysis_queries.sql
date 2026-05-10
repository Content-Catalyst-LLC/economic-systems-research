.headers on
.mode column

.print "Poverty rate and poverty gap"
SELECT
    household,
    income,
    poverty_line,
    CASE WHEN income < poverty_line THEN 1 ELSE 0 END AS poverty_status,
    ROUND(MAX(poverty_line - income, 0), 2) AS poverty_gap,
    ROUND(MAX(poverty_line - income, 0) / poverty_line, 3) AS normalized_poverty_gap
FROM household_poverty_scenarios
ORDER BY income;

.print ""
.print "Multidimensional deprivation"
SELECT
    community,
    ROUND(
      (health_deprivation + education_deprivation + housing_deprivation + sanitation_deprivation +
       food_deprivation + transport_deprivation + digital_deprivation + safety_deprivation +
       institutional_exclusion) / 9,
      3
    ) AS multidimensional_deprivation_score
FROM multidimensional_deprivation
ORDER BY multidimensional_deprivation_score DESC;

.print ""
.print "Capability, conversion, and real freedom proxy"
SELECT
    scenario,
    ROUND(
      0.18 * income_score +
      0.17 * health_score +
      0.17 * education_score +
      0.14 * mobility_score +
      0.12 * safety_score +
      0.10 * time_score +
      0.12 * institutional_access,
      3
    ) AS capability_score,
    ROUND((health_score + education_score + mobility_score + safety_score + time_score + institutional_access) / 6, 3) AS conversion_condition_score,
    ROUND(income_score * ((health_score + education_score + mobility_score + safety_score + time_score + institutional_access) / 6), 3) AS real_freedom_proxy
FROM capability_scenarios
ORDER BY capability_score DESC;

.print ""
.print "Economic inclusion"
SELECT
    scenario,
    ROUND(
      0.16 * work_access +
      0.14 * finance_access +
      0.18 * service_access +
      0.16 * infrastructure_access +
      0.12 * digital_access +
      0.10 * legal_recognition +
      0.14 * participation_security,
      3
    ) AS inclusion_score
FROM inclusion_scenarios
ORDER BY inclusion_score DESC;

.print ""
.print "Work inclusion and precarity"
SELECT
    sector,
    ROUND(
      0.20 * wage_adequacy +
      0.16 * hours_stability +
      0.16 * legal_protection +
      0.16 * benefit_access +
      0.14 * skill_progression +
      0.10 * workplace_safety +
      0.08 * recognition,
      3
    ) AS work_inclusion_score
FROM work_informality_scenarios
ORDER BY work_inclusion_score DESC;

.print ""
.print "Public services and vulnerability"
SELECT
    scenario,
    ROUND(
      0.18 * healthcare_access +
      0.16 * education_quality +
      0.14 * childcare_support +
      0.12 * food_support +
      0.14 * unemployment_protection +
      0.12 * disability_support,
      3
    ) AS public_service_score,
    ROUND(
      0.24 * low_savings +
      0.20 * high_debt +
      0.22 * insecure_work +
      0.18 * shock_exposure,
      3
    ) AS base_vulnerability_pressure
FROM public_service_vulnerability_scenarios
ORDER BY public_service_score DESC;
