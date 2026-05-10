.headers on
.mode column

.print "Trade openness and trade balance"
SELECT
    scenario,
    exports,
    imports,
    output,
    ROUND((exports + imports) / output, 3) AS trade_openness,
    ROUND(exports - imports, 3) AS trade_balance,
    ROUND(0.40 * strategic_import_dependence + 0.30 * intermediate_import_share + 0.30 * energy_import_share, 3) AS import_dependence_score
FROM trade_position_scenarios
ORDER BY trade_openness DESC;

.print ""
.print "Export concentration"
WITH shares AS (
    SELECT
        scenario,
        export_category,
        export_value,
        export_value / SUM(export_value) OVER (PARTITION BY scenario) AS export_share
    FROM export_basket_scenarios
)
SELECT
    scenario,
    ROUND(SUM(export_share * export_share), 3) AS export_concentration_index,
    ROUND(1 - SUM(export_share * export_share), 3) AS diversification_score
FROM shares
GROUP BY scenario
ORDER BY export_concentration_index DESC;

.print ""
.print "Domestic value capture and value-chain command position"
SELECT
    scenario,
    gross_exports,
    domestic_value_added,
    ROUND(domestic_value_added / gross_exports, 3) AS domestic_value_capture,
    ROUND(
      0.24 * (domestic_value_added / gross_exports) +
      0.20 * lead_firm_control +
      0.20 * technology_control +
      0.16 * branding_control +
      0.12 * (1 - assembly_dependence) +
      0.08 * upgrading_potential,
      3
    ) AS command_position_score
FROM value_chain_scenarios
ORDER BY command_position_score DESC;

.print ""
.print "Terms-of-trade vulnerability"
SELECT
    scenario,
    ROUND(export_price_index / import_price_index, 3) AS terms_of_trade,
    commodity_share,
    imported_food_energy_share,
    stabilization_fund_strength
FROM terms_of_trade_scenarios
ORDER BY terms_of_trade ASC;

.print ""
.print "External financial vulnerability"
SELECT
    scenario,
    ROUND(
      0.22 * foreign_currency_debt +
      0.20 * capital_flow_volatility +
      0.18 * (1 - reserve_buffer) +
      0.16 * current_account_pressure +
      0.14 * external_financing_need +
      0.10 * (1 - policy_space),
      3
    ) AS external_vulnerability_score
FROM finance_currency_scenarios
ORDER BY external_vulnerability_score DESC;

.print ""
.print "Regional globalization advantage"
SELECT
    region,
    ROUND(
      0.20 * export_linkage +
      0.20 * productivity +
      0.18 * infrastructure_depth +
      0.16 * capital_access +
      0.14 * market_access +
      0.12 * institutional_capacity,
      3
    ) AS globalization_advantage_score
FROM regional_inequality_scenarios
ORDER BY globalization_advantage_score DESC;

.print ""
.print "Sustainable trade resilience"
SELECT
    scenario,
    ROUND(
      0.20 * supplier_diversification +
      0.22 * domestic_capability +
      0.16 * strategic_stock_buffer +
      0.16 * regional_redundancy +
      0.12 * import_substitution_capacity +
      0.14 * cooperative_trade_access,
      3
    ) AS sustainable_trade_resilience_score
FROM strategic_resilience_scenarios
ORDER BY sustainable_trade_resilience_score DESC;
