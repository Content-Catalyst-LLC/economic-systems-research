.headers on
.mode column

.print "Inflation pass-through by sector"
SELECT
    sector,
    energy_cost_change,
    wage_cost_change,
    materials_cost_change,
    ROUND(alpha_energy * energy_cost_change + beta_wage * wage_cost_change + gamma_materials * materials_cost_change, 3) AS estimated_price_change,
    ROUND((alpha_energy * energy_cost_change) / (alpha_energy * energy_cost_change + beta_wage * wage_cost_change + gamma_materials * materials_cost_change), 3) AS energy_share_of_pass_through
FROM sector_energy_pass_through_scenarios
ORDER BY estimated_price_change DESC;

.print ""
.print "Household energy and transport burden"
SELECT
    household_group,
    income,
    energy_spending,
    transport_fuel_spending,
    ROUND(energy_spending / income, 3) AS household_energy_burden,
    ROUND(transport_fuel_spending / income, 3) AS transport_fuel_burden,
    ROUND((energy_spending + transport_fuel_spending) / income, 3) AS combined_energy_transport_burden,
    ROUND(CASE WHEN nominal_wage > 0 THEN nominal_wage / price_level_relative ELSE 0 END, 3) AS real_wage
FROM household_energy_burden_scenarios
ORDER BY combined_energy_transport_burden DESC;

.print ""
.print "Import price transmission"
SELECT
    scenario,
    world_price_change,
    exchange_rate_effect,
    ROUND(world_price_change + exchange_rate_effect, 3) AS import_price_change,
    import_dependence,
    energy_share_of_imports,
    ROUND((world_price_change + exchange_rate_effect) * import_dependence * (0.5 + energy_share_of_imports), 3) AS weighted_import_inflation_pressure
FROM import_price_transmission_scenarios
ORDER BY weighted_import_inflation_pressure DESC;

.print ""
.print "Supply bottleneck pressure"
SELECT
    scenario,
    energy_capacity,
    logistics_capacity,
    supply_availability,
    ROUND(
      0.30 * (1 - energy_capacity) +
      0.25 * (1 - logistics_capacity) +
      0.25 * (1 - supply_availability) +
      0.10 * (1 - labor_capacity) +
      0.10 * (1 - capital_capacity),
      3
    ) AS inflationary_bottleneck_pressure
FROM supply_bottleneck_scenarios
ORDER BY inflationary_bottleneck_pressure DESC;

.print ""
.print "Resilience policy scores"
SELECT
    policy,
    ROUND(
      0.24 * energy_resilience +
      0.22 * supply_diversification +
      0.18 * household_protection +
      0.18 * infrastructure_capacity +
      0.18 * public_buffer_capacity,
      3
    ) AS long_run_resilience_score,
    near_term_disinflation
FROM resilience_policy_scenarios
ORDER BY long_run_resilience_score DESC;
