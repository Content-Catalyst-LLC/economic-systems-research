.headers on
.mode column

.print "Growth dependence"
SELECT
    scenario,
    ROUND((
      employment_dependency +
      debt_service_dependency +
      fiscal_dependency +
      asset_dependency +
      pension_dependency +
      housing_market_dependency +
      political_legitimacy_dependency
    ) / 7.0, 3) AS growth_dependence_score
FROM growth_dependence
ORDER BY growth_dependence_score DESC;

.print ""
.print "Throughput identity"
SELECT
    scenario,
    population,
    affluence,
    intensity,
    ROUND(population * affluence * intensity, 2) AS throughput_index,
    wellbeing_index,
    distribution_quality
FROM throughput_scenarios
ORDER BY throughput_index DESC;

.print ""
.print "Wellbeing beyond output"
SELECT
    scenario,
    ROUND((
      health +
      time_balance +
      security +
      equality +
      public_goods +
      ecological_quality +
      care_support +
      social_trust
    ) / 8.0, 3) AS wellbeing_score
FROM wellbeing_dashboard
ORDER BY wellbeing_score DESC;

.print ""
.print "Sufficiency"
SELECT
    system,
    needs_met,
    throughput_required,
    ROUND(needs_met / throughput_required, 3) AS sufficiency_ratio,
    ROUND(
      0.28 * needs_met +
      0.22 * (1 - throughput_required) +
      0.16 * time_security +
      0.14 * public_access +
      0.10 * care_capacity +
      0.10 * dignity,
      3
    ) AS social_sufficiency_score
FROM sufficiency
ORDER BY social_sufficiency_score DESC;

.print ""
.print "Work time and care"
SELECT
    scenario,
    paid_work_hours,
    unpaid_care_hours,
    paid_work_hours + unpaid_care_hours AS total_work_hours,
    leisure_hours,
    labor_security,
    care_support,
    time_sovereignty
FROM work_time_care
ORDER BY time_sovereignty DESC;

.print ""
.print "Finance growth dependence"
SELECT
    system,
    ROUND(
      0.18 * private_debt +
      0.18 * public_debt_pressure +
      0.20 * asset_valuation_pressure +
      0.16 * pension_return_dependency +
      0.16 * housing_speculation +
      0.12 * (1 - real_investment_alignment),
      3
    ) AS finance_growth_dependence_score
FROM finance_growth_dependence
ORDER BY finance_growth_dependence_score DESC;

.print ""
.print "Decoupling and rebound"
SELECT
    scenario,
    output_growth,
    intensity_reduction,
    additional_demand,
    ROUND(intensity_reduction - additional_demand, 3) AS net_efficiency_gain,
    absolute_throughput_change,
    wellbeing_gain
FROM decoupling_rebound
ORDER BY absolute_throughput_change ASC;

.print ""
.print "Degrowth transition credibility"
SELECT
    scenario,
    ROUND(
      0.18 * throughput_reduction +
      0.20 * redistribution +
      0.20 * public_services +
      0.16 * democratic_legitimacy +
      0.14 * macro_stabilization +
      0.12 * employment_security,
      3
    ) AS degrowth_transition_score
FROM degrowth_transition
ORDER BY degrowth_transition_score DESC;

.print ""
.print "Global justice"
SELECT
    country_group,
    ROUND(
      0.32 * material_footprint +
      0.28 * historic_responsibility +
      0.18 * adaptive_capacity +
      0.14 * transition_finance_obligation +
      0.08 * (1 - basic_needs_gap),
      3
    ) AS excess_reduction_responsibility,
    ROUND(
      0.34 * development_need +
      0.28 * basic_needs_gap +
      0.16 * (1 - adaptive_capacity) +
      0.12 * (1 - historic_responsibility) +
      0.10 * (1 - material_footprint),
      3
    ) AS development_priority_score
FROM global_justice
ORDER BY development_priority_score DESC;
