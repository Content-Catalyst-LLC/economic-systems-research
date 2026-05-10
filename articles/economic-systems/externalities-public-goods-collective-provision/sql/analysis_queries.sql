.headers on
.mode column

.print "Public-good underprovision"
SELECT
    public_good,
    private_benefit + external_benefit AS social_benefit,
    social_need,
    voluntary_provision,
    social_need - voluntary_provision AS underprovision_gap,
    ROUND((private_benefit + external_benefit) / private_cost, 3) AS social_return_ratio
FROM public_good_scenarios
ORDER BY underprovision_gap DESC;

.print ""
.print "Free-rider contribution scenarios"
SELECT
    scenario,
    SUM(contribution) AS total_contribution,
    SUM(CASE WHEN contribution <= 1 AND benefit_share > 0 THEN 1 ELSE 0 END) AS free_rider_groups,
    ROUND(SUM(contribution) / COUNT(*), 2) AS average_contribution
FROM contribution_scenarios
GROUP BY scenario
ORDER BY total_contribution DESC;

.print ""
.print "Collective provision capacity"
SELECT
    scenario,
    tax_revenue + borrowing_capacity + pooled_funds AS collective_provision_capacity,
    maintenance_need + preparedness_need AS total_collective_need,
    ROUND((tax_revenue + borrowing_capacity + pooled_funds) / (maintenance_need + preparedness_need), 3) AS capacity_ratio,
    tax_revenue + borrowing_capacity + pooled_funds - maintenance_need - preparedness_need AS capacity_gap
FROM collective_finance_scenarios
ORDER BY capacity_ratio DESC;

.print ""
.print "Externality burden distribution"
SELECT
    group_name,
    income_index,
    exposure_index,
    political_voice_index,
    ROUND(
      0.52 * exposure_index +
      0.28 * (1 - income_index) +
      0.20 * (1 - political_voice_index),
      3
    ) AS burden_score
FROM burden_distribution_groups
ORDER BY burden_score DESC;
