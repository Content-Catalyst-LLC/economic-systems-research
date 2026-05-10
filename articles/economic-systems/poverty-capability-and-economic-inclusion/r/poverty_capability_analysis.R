# Poverty, Capability, and Economic Inclusion
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

household <- read_csv(file.path(processed_dir, "household_poverty_scenarios.csv"), show_col_types = FALSE)
capability <- read_csv(file.path(processed_dir, "capability_scenarios.csv"), show_col_types = FALSE)
inclusion <- read_csv(file.path(processed_dir, "inclusion_scenarios.csv"), show_col_types = FALSE)
services <- read_csv(file.path(processed_dir, "public_service_vulnerability_scenarios.csv"), show_col_types = FALSE)

household_results <- household |>
  mutate(
    poverty_status = income < poverty_line,
    poverty_gap = pmax(poverty_line - income, 0),
    normalized_poverty_gap = poverty_gap / poverty_line,
    post_cost_income = income - housing_cost - debt_service - health_cost,
    vulnerability_score =
      0.24 * (1 - savings / max(savings)) +
      0.22 * (debt_service / income) +
      0.22 * (housing_cost / income) +
      0.14 * (health_cost / income) +
      0.18 * shock_exposure
  )

capability_results <- capability |>
  mutate(
    capability_score =
      0.18 * income_score +
      0.17 * health_score +
      0.17 * education_score +
      0.14 * mobility_score +
      0.12 * safety_score +
      0.10 * time_score +
      0.12 * institutional_access,
    conversion_condition_score =
      (health_score + education_score + mobility_score + safety_score + time_score + institutional_access) / 6,
    real_freedom_proxy = income_score * conversion_condition_score
  )

inclusion_results <- inclusion |>
  mutate(
    inclusion_score =
      0.16 * work_access +
      0.14 * finance_access +
      0.18 * service_access +
      0.16 * infrastructure_access +
      0.12 * digital_access +
      0.10 * legal_recognition +
      0.14 * participation_security
  )

services_results <- services |>
  mutate(
    public_service_score =
      0.18 * healthcare_access +
      0.16 * education_quality +
      0.14 * childcare_support +
      0.12 * food_support +
      0.14 * unemployment_protection +
      0.12 * disability_support,
    raw_vulnerability_score =
      0.24 * low_savings +
      0.20 * high_debt +
      0.22 * insecure_work +
      0.16 * (1 - public_service_score) +
      0.18 * shock_exposure,
    service_adjusted_vulnerability = raw_vulnerability_score * (1 - 0.45 * public_service_score),
    social_protection_effect = raw_vulnerability_score - service_adjusted_vulnerability
  )

write_csv(household_results, file.path(table_dir, "poverty_capability_r_household_results.csv"))
write_csv(capability_results, file.path(table_dir, "poverty_capability_r_capability_results.csv"))
write_csv(inclusion_results, file.path(table_dir, "poverty_capability_r_inclusion_results.csv"))
write_csv(services_results, file.path(table_dir, "poverty_capability_r_services_results.csv"))

p <- ggplot(capability_results, aes(x = scenario, y = capability_score)) +
  geom_col() +
  labs(
    title = "Capability Scores by Institutional Scenario",
    subtitle = "Capability depends on income, health, education, mobility, safety, time, and institutional access.",
    x = NULL,
    y = "Composite capability score"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "poverty_capability_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(household_results)
print(capability_results)
print(inclusion_results)
print(services_results)
