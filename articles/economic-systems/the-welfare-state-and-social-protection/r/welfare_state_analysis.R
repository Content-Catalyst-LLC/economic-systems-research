# The Welfare State and Social Protection
# R Workflow

library(readr)
library(dplyr)
library(ggplot2)

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("--file=", "", file_arg[1]))
  base_dir <- normalizePath(file.path(dirname(script_path), ".."))
} else {
  base_dir <- normalizePath(getwd())
}

processed_dir <- file.path(base_dir, "data", "processed")
table_dir <- file.path(base_dir, "outputs", "tables")
figure_dir <- file.path(base_dir, "outputs", "figures")

dir.create(table_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

household <- read_csv(file.path(processed_dir, "household_tax_transfer.csv"), show_col_types = FALSE)
spending <- read_csv(file.path(processed_dir, "social_spending_scenarios.csv"), show_col_types = FALSE)
coverage <- read_csv(file.path(processed_dir, "program_coverage.csv"), show_col_types = FALSE)
adaptive <- read_csv(file.path(processed_dir, "adaptive_protection.csv"), show_col_types = FALSE)

household_results <- household |>
  mutate(
    disposable_income = market_income - taxes + transfers,
    service_adjusted_income = disposable_income + service_value,
    post_cost_security_income = service_adjusted_income - housing_cost - care_cost,
    redistributive_gain = disposable_income - market_income
  )

spending_results <- spending |>
  mutate(
    social_spending_ratio = social_spending / output,
    protection_strength_score =
      0.24 * social_spending_ratio / max(social_spending_ratio) +
      0.18 * healthcare_spending / max(healthcare_spending) +
      0.18 * pensions / max(pensions) +
      0.14 * unemployment / max(unemployment) +
      0.14 * family_policy / max(family_policy) +
      0.12 * administration_quality
  )

coverage_results <- coverage |>
  mutate(
    coverage_rate = covered_population / target_population,
    replacement_rate = benefit / previous_earnings,
    effective_protection_score =
      0.28 * coverage_rate +
      0.24 * replacement_rate +
      0.18 * take_up_rate +
      0.16 * (1 - administrative_burden) +
      0.14 * (1 - stigma_cost)
  )

adaptive_results <- adaptive |>
  mutate(
    adaptive_capacity_score =
      0.18 * scale_up_capacity +
      0.18 * payment_speed +
      0.16 * registry_quality +
      0.16 * local_delivery_capacity +
      0.16 * benefit_adequacy +
      0.16 * (1 - post_shock_vulnerability),
    shock_vulnerability_reduction = baseline_exposure - post_shock_vulnerability
  )

write_csv(household_results, file.path(table_dir, "welfare_state_r_household_results.csv"))
write_csv(spending_results, file.path(table_dir, "welfare_state_r_spending_results.csv"))
write_csv(coverage_results, file.path(table_dir, "welfare_state_r_coverage_results.csv"))
write_csv(adaptive_results, file.path(table_dir, "welfare_state_r_adaptive_results.csv"))

p <- ggplot(spending_results, aes(x = scenario, y = protection_strength_score)) +
  geom_col() +
  labs(
    title = "Social Protection Strength by Welfare-State Scenario",
    subtitle = "Protection strength depends on spending, program mix, and administrative quality.",
    x = NULL,
    y = "Composite protection score"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "welfare_state_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(household_results)
print(spending_results)
print(coverage_results)
print(adaptive_results)
