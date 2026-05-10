.headers on
.mode column

.print "Sector emissions and decarbonization"
SELECT
    sector,
    ROUND(output * energy_intensity * carbon_intensity, 2) AS emissions,
    ROUND((old_emissions_intensity - new_emissions_intensity) / years, 3) AS decarbonization_rate,
    abatement_readiness
FROM sector_emissions
ORDER BY emissions DESC;

.print ""
.print "Transition policy packages"
SELECT
    package,
    ROUND(
      0.18 * carbon_price_strength +
      0.20 * regulatory_strength +
      0.22 * public_investment +
      0.18 * industrial_policy +
      0.12 * social_protection +
      0.10 * implementation_capacity,
      3
    ) AS policy_mix_score
FROM policy_packages
ORDER BY policy_mix_score DESC;

.print ""
.print "Transition investment"
SELECT
    scenario,
    ROUND(
      0.22 * public_investment +
      0.20 * private_capital +
      0.22 * policy_credibility +
      0.16 * cost_of_capital_support +
      0.10 * permitting_capacity +
      0.10 * grid_readiness,
      3
    ) AS transition_investment_score
FROM transition_investment
ORDER BY transition_investment_score DESC;

.print ""
.print "Carbon lock-in"
SELECT
    system,
    ROUND(
      0.18 * capital_stock_life +
      0.20 * infrastructure_dependence +
      0.18 * incumbent_power +
      0.16 * consumer_switching_barrier +
      0.14 * (1 - replacement_readiness) +
      0.14 * stranded_asset_risk,
      3
    ) AS lock_in_score
FROM carbon_lock_in
ORDER BY lock_in_score DESC;

.print ""
.print "Damage and adaptation"
SELECT
    region,
    ROUND(
      0.18 * temperature_stress +
      0.18 * flood_exposure +
      0.12 * wildfire_smoke +
      0.18 * economic_exposure +
      0.18 * vulnerability +
      0.10 * (1 - adaptation_capacity) +
      0.06 * (1 - public_health_capacity),
      3
    ) AS damage_risk_score
FROM damage_adaptation
ORDER BY damage_risk_score DESC;

.print ""
.print "Just transition"
SELECT
    community,
    ROUND(
      0.16 * (1 - worker_exposure) +
      0.16 * retraining +
      0.18 * regional_investment +
      0.14 * income_support +
      0.14 * public_services +
      0.12 * new_industry_pipeline +
      0.10 * labor_standards,
      3
    ) AS just_transition_score
FROM just_transition
ORDER BY just_transition_score DESC;

.print ""
.print "Hard-to-abate sectors"
SELECT
    sector,
    ROUND(
      0.22 * process_emissions +
      0.18 * temperature_requirement +
      0.20 * (1 - technology_readiness) +
      0.14 * (1 - procurement_leverage) +
      0.12 * (1 - demand_reduction_potential) +
      0.14 * carbon_capture_relevance,
      3
    ) AS hard_to_abate_score
FROM hard_to_abate
ORDER BY hard_to_abate_score DESC;

.print ""
.print "Global equity: finance obligation and support need"
SELECT
    country_group,
    ROUND(
      0.28 * historic_responsibility +
      0.18 * current_emissions +
      0.24 * fiscal_capacity +
      0.12 * technology_capacity +
      0.10 * climate_vulnerability +
      0.08 * development_need,
      3
    ) AS finance_obligation_score,
    ROUND(
      0.28 * climate_vulnerability +
      0.24 * development_need +
      0.18 * (1 - fiscal_capacity) +
      0.14 * (1 - technology_capacity) +
      0.10 * (1 - historic_responsibility) +
      0.06 * current_emissions,
      3
    ) AS support_need_score
FROM global_equity
ORDER BY support_need_score DESC;

.print ""
.print "Implementation credibility"
SELECT
    scenario,
    ROUND(
      0.16 * target_clarity +
      0.20 * administrative_capacity +
      0.18 * fiscal_commitment +
      0.18 * policy_durability +
      0.12 * public_trust +
      0.16 * coordination_capacity,
      3
    ) AS implementation_credibility_score
FROM implementation_credibility
ORDER BY implementation_credibility_score DESC;
