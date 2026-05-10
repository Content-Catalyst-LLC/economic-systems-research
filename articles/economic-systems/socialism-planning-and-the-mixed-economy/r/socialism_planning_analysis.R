# Socialism, Planning, and the Mixed Economy
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

mixed <- read_csv(file.path(processed_dir, "mixed_economy_scenarios.csv"), show_col_types = FALSE)
planning <- read_csv(file.path(processed_dir, "planning_capacity.csv"), show_col_types = FALSE)
decommodification <- read_csv(file.path(processed_dir, "decommodification_scenarios.csv"), show_col_types = FALSE)
crisis <- read_csv(file.path(processed_dir, "crisis_transition_globalization.csv"), show_col_types = FALSE)

mixed_results <- mixed |>
  mutate(
    mixed_economy_total = market_allocation + public_planning + public_provision + regulation_rights,
    public_purpose_score =
      0.20 * public_planning +
      0.20 * public_provision +
      0.16 * regulation_rights +
      0.16 * public_ownership_share +
      0.14 * social_rights_strength +
      0.14 * social_need_weight,
    profit_dominance_score =
      0.46 * market_allocation +
      0.34 * private_profit_weight +
      0.20 * (1 - social_rights_strength)
  )

planning_results <- planning |>
  mutate(
    planning_capacity_score =
      0.18 * state_capacity +
      0.16 * data_quality +
      0.16 * institutional_reach +
      0.16 * feedback_quality +
      0.16 * democratic_accountability +
      0.10 * coordination_authority +
      0.08 * implementation_speed
  )

decommodification_results <- decommodification |>
  mutate(
    decommodification_score =
      0.18 * healthcare_access +
      0.16 * education_access +
      0.16 * housing_security +
      0.14 * childcare_support +
      0.12 * public_transport +
      0.12 * social_insurance +
      0.12 * guaranteed_access
  )

crisis_results <- crisis |>
  mutate(
    crisis_coordination_score =
      0.20 * public_planning +
      0.18 * infrastructure_depth +
      0.18 * fiscal_capacity +
      0.16 * administrative_speed +
      0.14 * social_protection +
      0.14 * democratic_legitimacy,
    sustainable_transition_score =
      0.18 * public_planning +
      0.18 * infrastructure_depth +
      0.14 * fiscal_capacity +
      0.16 * social_protection +
      0.20 * ecological_targets +
      0.14 * democratic_legitimacy
  )

write_csv(mixed_results, file.path(table_dir, "socialism_planning_r_mixed_results.csv"))
write_csv(planning_results, file.path(table_dir, "socialism_planning_r_planning_results.csv"))
write_csv(decommodification_results, file.path(table_dir, "socialism_planning_r_decommodification_results.csv"))
write_csv(crisis_results, file.path(table_dir, "socialism_planning_r_crisis_results.csv"))

p <- ggplot(planning_results, aes(x = scenario, y = planning_capacity_score)) +
  geom_col() +
  labs(
    title = "Planning Capacity by Institutional Scenario",
    subtitle = "Planning capacity depends on state capacity, data quality, reach, feedback, accountability, and implementation.",
    x = NULL,
    y = "Composite planning score"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "socialism_planning_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(mixed_results)
print(planning_results)
print(decommodification_results)
print(crisis_results)
