# Political Economy, Power, and Distributional Conflict
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

income <- read_csv(file.path(processed_dir, "income_distribution.csv"), show_col_types = FALSE)
power <- read_csv(file.path(processed_dir, "power_groups.csv"), show_col_types = FALSE)
fiscal <- read_csv(file.path(processed_dir, "fiscal_incidence.csv"), show_col_types = FALSE)
legitimacy <- read_csv(file.path(processed_dir, "legitimacy_conflict.csv"), show_col_types = FALSE)

income_results <- income |>
  mutate(
    total_income = wages + profits + rents,
    wage_share = wages / total_income,
    profit_share = profits / total_income,
    rent_share = rents / total_income,
    net_fiscal_position = benefits_received + public_goods_value - taxes_paid,
    distributional_concentration_score = profit_share + rent_share
  )

power_results <- power |>
  mutate(
    power_asymmetry_score =
      0.20 * ownership_power +
      0.16 * organization_power +
      0.16 * access_power +
      0.14 * mobility_power +
      0.14 * voice_power +
      0.10 * media_influence +
      0.10 * legal_position
  )

fiscal_results <- fiscal |>
  mutate(
    gross_income_after_tax = market_income - taxes_paid,
    disposable_income = gross_income_after_tax + cash_transfers,
    service_adjusted_income = disposable_income + services_received,
    net_fiscal_position = cash_transfers + services_received - taxes_paid,
    post_burden_income = service_adjusted_income - debt_service - housing_cost
  )

legitimacy_results <- legitimacy |>
  mutate(
    conflict_intensity_score =
      0.22 * inequality_pressure +
      0.18 * inflation_pressure +
      0.18 * unemployment_pressure +
      0.20 * representation_gap +
      0.22 * shock_exposure,
    legitimacy_score =
      0.26 * fairness +
      0.24 * security +
      0.24 * voice +
      0.26 * institutional_trust
  )

write_csv(income_results, file.path(table_dir, "political_economy_r_income_results.csv"))
write_csv(power_results, file.path(table_dir, "political_economy_r_power_results.csv"))
write_csv(fiscal_results, file.path(table_dir, "political_economy_r_fiscal_results.csv"))
write_csv(legitimacy_results, file.path(table_dir, "political_economy_r_legitimacy_results.csv"))

p <- ggplot(income_results, aes(x = scenario, y = wage_share)) +
  geom_col() +
  labs(
    title = "Wage Share by Political-Economic Scenario",
    subtitle = "Wage shares are institutionally shaped by power, bargaining, ownership, and policy.",
    x = NULL,
    y = "Wages / total income"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "political_economy_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(income_results)
print(power_results)
print(fiscal_results)
print(legitimacy_results)
