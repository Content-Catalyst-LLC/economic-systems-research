# Debt, Dependency, and Global Financial Order
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

debt <- read_csv(file.path(processed_dir, "debt_position_scenarios.csv"), show_col_types = FALSE)
external <- read_csv(file.path(processed_dir, "external_account_scenarios.csv"), show_col_types = FALSE)
restructuring <- read_csv(file.path(processed_dir, "restructuring_scenarios.csv"), show_col_types = FALSE)
sustainable <- read_csv(file.path(processed_dir, "sustainable_finance_scenarios.csv"), show_col_types = FALSE)

debt_results <- debt |>
  mutate(
    debt_ratio = debt_stock / output,
    external_debt_service_ratio = external_debt_service / export_earnings,
    domestic_currency_fx_burden = foreign_currency_debt * exchange_rate,
    reserve_adequacy = reserves / short_term_external_obligations,
    interest_growth_pressure = (effective_interest_rate - growth_rate) * debt_stock + primary_deficit
  )

external_results <- external |>
  mutate(
    dependency_score =
      0.22 * export_concentration +
      0.20 * import_dependence +
      0.20 * external_finance_reliance +
      0.16 * capital_flow_volatility +
      0.12 * (1 - reserve_buffer) +
      0.10 * (1 - domestic_capability)
  )

restructuring_results <- restructuring |>
  mutate(
    post_restructuring_debt = initial_debt * (1 - restructuring_haircut),
    resolution_quality_score =
      0.22 * restructuring_haircut +
      0.18 * maturity_extension +
      0.18 * interest_relief +
      0.18 * social_spending_floor +
      0.16 * growth_recovery +
      0.08 * creditor_acceptance
  )

sustainable_results <- sustainable |>
  mutate(
    sustainable_finance_score =
      0.22 * productive_investment +
      0.18 * domestic_capability +
      0.18 * export_resilience +
      0.14 * social_protection +
      0.14 * ecological_resilience +
      0.14 * debt_manageability
  )

write_csv(debt_results, file.path(table_dir, "debt_dependency_r_results.csv"))
write_csv(external_results, file.path(table_dir, "debt_dependency_r_external_results.csv"))
write_csv(restructuring_results, file.path(table_dir, "debt_dependency_r_restructuring_results.csv"))
write_csv(sustainable_results, file.path(table_dir, "debt_dependency_r_sustainable_finance_results.csv"))

p <- ggplot(debt_results, aes(x = scenario, y = external_debt_service_ratio)) +
  geom_col() +
  labs(
    title = "External Debt-Service Pressure",
    subtitle = "Debt sustainability depends on export earnings, reserves, currency structure, and refinancing conditions.",
    x = NULL,
    y = "External debt service / export earnings"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "debt_dependency_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(debt_results)
print(external_results)
print(restructuring_results)
print(sustainable_results)
