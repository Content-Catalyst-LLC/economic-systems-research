.headers on
.mode column

.print "Throughput, scale, and waste"
SELECT
    scenario,
    ROUND(energy_input + material_input, 2) AS throughput,
    ROUND((energy_input + material_input) - recovered_throughput, 2) AS waste_residual,
    ROUND(recovered_throughput / (energy_input + material_input), 3) AS recovery_rate,
    ROUND(economic_scale / ecological_capacity, 3) AS scale_ratio,
    wellbeing_index
FROM throughput_scenarios
ORDER BY scale_ratio DESC;

.print ""
.print "Sector material footprint and ecological pressure"
SELECT
    sector,
    ROUND(domestic_extraction + imports - exports, 2) AS material_footprint,
    ROUND(
      0.20 * ((domestic_extraction + imports - exports) / 380.0) +
      0.18 * energy_intensity +
      0.18 * water_pressure +
      0.18 * land_pressure +
      0.16 * waste_intensity +
      0.10 * social_necessity,
      3
    ) AS ecological_pressure_score
FROM sector_footprints
ORDER BY ecological_pressure_score DESC;

.print ""
.print "Ecological burden distribution"
SELECT
    "group",
    ROUND(
      0.24 * exposure +
      0.18 * (1 - income_buffer) +
      0.18 * (1 - infrastructure) +
      0.18 * (1 - adaptive_capacity) +
      0.10 * (1 - political_voice) +
      0.12 * (1 - historical_responsibility),
      3
    ) AS ecological_burden_score
FROM ecological_burdens
ORDER BY ecological_burden_score DESC;

.print ""
.print "Embedded economy score"
SELECT
    scenario,
    ROUND(
      0.18 * ecology_integrity +
      0.18 * care_capacity +
      0.16 * public_institutions +
      0.14 * infrastructure_maintenance +
      0.14 * cultural_reciprocity +
      0.10 * (1 - market_dependence) +
      0.10 * community_resilience,
      3
    ) AS embeddedness_score
FROM embeddedness_scenarios
ORDER BY embeddedness_score DESC;

.print ""
.print "Socio-ecological resilience and commons governance"
SELECT
    system,
    ROUND(
      0.16 * diversity +
      0.14 * redundancy +
      0.16 * regeneration +
      0.16 * governance +
      0.12 * maintenance +
      0.12 * learning +
      0.08 * monitoring +
      0.06 * participation,
      3
    ) AS resilience_score
FROM resilience_commons
ORDER BY resilience_score DESC;

.print ""
.print "Post-growth scenarios"
SELECT
    scenario,
    gdp_growth,
    throughput_growth,
    efficiency_gain,
    rebound_effect,
    wellbeing_change,
    inequality_pressure,
    public_services
FROM postgrowth_scenarios
ORDER BY wellbeing_change DESC;

.print ""
.print "Critical natural capital"
SELECT
    system,
    ROUND(
      0.24 * (1 - substitutability) +
      0.22 * threshold_risk +
      0.20 * irreversibility +
      0.14 * (1 - regeneration_rate) +
      0.20 * life_support_importance,
      3
    ) AS critical_natural_capital_score
FROM strong_sustainability
ORDER BY critical_natural_capital_score DESC;
