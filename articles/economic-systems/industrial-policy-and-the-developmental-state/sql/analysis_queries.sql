.headers on
.mode column

.print "Strategic sector indicators"
SELECT
    sector,
    ROUND(sector_output / total_output, 3) AS sector_output_share,
    ROUND(sector_output / sector_labor, 3) AS sector_productivity,
    ROUND(sector_exports / sector_output, 3) AS export_ratio,
    technology_depth,
    learning_potential,
    domestic_linkage_potential
FROM strategic_sector_scenarios
ORDER BY technology_depth DESC;

.print ""
.print "Support conditionality"
SELECT
    s.sector,
    s.public_support,
    ROUND(s.public_support / sec.sector_output, 3) AS support_intensity,
    s.productivity_gain,
    s.export_growth,
    s.local_supplier_share,
    s.emissions_reduction,
    s.support_duration_years
FROM support_conditionality_scenarios s
JOIN strategic_sector_scenarios sec ON s.sector = sec.sector
ORDER BY support_intensity DESC;

.print ""
.print "Development finance alignment"
SELECT
    scenario,
    patient_credit_share,
    industrial_credit_share,
    speculative_credit_share,
    fx_debt_exposure,
    ROUND(
      0.26 * patient_credit_share +
      0.24 * industrial_credit_share +
      0.20 * (1 - speculative_credit_share) +
      0.12 * (1 - fx_debt_exposure) +
      0.10 * development_bank_capacity +
      0.08 * credit_monitoring_quality,
      3
    ) AS development_finance_alignment_score
FROM development_finance_scenarios
ORDER BY development_finance_alignment_score DESC;

.print ""
.print "Infrastructure and energy readiness"
SELECT
    region,
    ROUND(
      0.20 * transport_reliability +
      0.18 * port_access +
      0.22 * energy_reliability +
      0.13 * water_reliability +
      0.14 * digital_connectivity +
      0.13 * industrial_land_readiness,
      3
    ) AS industrial_readiness_score
FROM infrastructure_energy_scenarios
ORDER BY industrial_readiness_score DESC;

.print ""
.print "Capture risk"
SELECT
    program,
    ROUND(
      0.20 * market_concentration +
      0.20 * lobbying_intensity +
      0.20 * (1 - evaluation_strength) +
      0.16 * open_ended_support +
      0.16 * performance_shortfall +
      0.08 * (1 - public_disclosure),
      3
    ) AS capture_risk_score
FROM capture_risk_scenarios
ORDER BY capture_risk_score DESC;

.print ""
.print "Green industrial policy"
SELECT
    sector,
    productivity_gain,
    emissions_reduction,
    domestic_linkage,
    employment_quality,
    resilience_value,
    material_risk
FROM green_industrial_policy_scenarios
ORDER BY emissions_reduction DESC;
