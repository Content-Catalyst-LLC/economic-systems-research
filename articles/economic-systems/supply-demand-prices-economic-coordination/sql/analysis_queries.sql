.headers on
.mode column

.print "Supply-demand equilibrium scenarios"
SELECT
    scenario,
    ROUND(((a - c) / (b + d)) * (1 + markup_rate), 3) AS equilibrium_price,
    ROUND(a - b * (((a - c) / (b + d)) * (1 + markup_rate)), 3) AS equilibrium_quantity,
    ROUND(-b * ((((a - c) / (b + d)) * (1 + markup_rate)) / (a - b * (((a - c) / (b + d)) * (1 + markup_rate)))), 3) AS demand_elasticity,
    ROUND(d * ((((a - c) / (b + d)) * (1 + markup_rate)) / (a - b * (((a - c) / (b + d)) * (1 + markup_rate)))), 3) AS supply_elasticity
FROM market_parameter_scenarios
ORDER BY scenario;

.print ""
.print "Need versus effective demand"
SELECT
    group_name,
    ROUND(need_index, 2) AS need_index,
    ROUND(income_command, 2) AS income_command,
    ROUND(price_burden, 2) AS price_burden,
    ROUND(
      0.30 * need_index +
      0.30 * income_command +
      0.18 * credit_access +
      0.17 * institutional_access +
      0.05 * (1 - price_burden),
      3
    ) AS effective_demand,
    ROUND(need_index - (
      0.30 * need_index +
      0.30 * income_command +
      0.18 * credit_access +
      0.17 * institutional_access +
      0.05 * (1 - price_burden)
    ), 3) AS unmet_need_gap
FROM market_access_groups
ORDER BY unmet_need_gap DESC;

.print ""
.print "External costs and social-cost pricing"
SELECT
    sector,
    private_price,
    marginal_external_cost,
    private_price + marginal_external_cost AS marginal_social_cost,
    public_good_benefit,
    public_good_benefit - marginal_external_cost AS net_social_value_adjustment
FROM external_cost_scenarios
ORDER BY marginal_external_cost DESC;
