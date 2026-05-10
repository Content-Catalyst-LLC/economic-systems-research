# Finance, Leverage, and Systemic Risk
# R Workflow

library(readr)
library(dplyr)
library(ggplot2)
library(tidyr)

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

institutions <- read_csv(file.path(processed_dir, "institution_balance_sheets.csv"), show_col_types = FALSE)
funding <- read_csv(file.path(processed_dir, "funding_gap_scenarios.csv"), show_col_types = FALSE)
households <- read_csv(file.path(processed_dir, "household_leverage_scenarios.csv"), show_col_types = FALSE)
buffers <- read_csv(file.path(processed_dir, "macroprudential_buffer_scenarios.csv"), show_col_types = FALSE)

institution_results <- institutions |>
  mutate(
    equity = assets - debt,
    leverage = assets / equity,
    debt_to_equity = debt / equity,
    capital_ratio = equity / assets,
    raw_funding_gap = short_term_liabilities - liquid_assets
  )

funding_results <- funding |>
  mutate(
    raw_funding_gap = short_term_liabilities - liquid_assets,
    rollover_adjusted_gap = short_term_liabilities * (1 - rollover_rate) - liquid_assets,
    backstop_adjusted_gap = rollover_adjusted_gap * (1 - emergency_liquidity_access)
  )

household_results <- households |>
  mutate(
    loan_to_value = ifelse(housing_value > 0, mortgage_debt / housing_value, 0),
    debt_service_ratio = debt_service / income,
    housing_value_after_15pct_shock = housing_value * 0.85,
    ltv_after_housing_shock = ifelse(housing_value_after_15pct_shock > 0, mortgage_debt / housing_value_after_15pct_shock, 0),
    negative_equity_flag = ltv_after_housing_shock > 1
  )

buffer_results <- buffers |>
  mutate(
    macroprudential_resilience_score =
      0.24 * (capital_buffer / max(capital_buffer)) +
      0.24 * (liquidity_buffer / max(liquidity_buffer)) +
      0.20 * (countercyclical_buffer / max(countercyclical_buffer)) +
      0.16 * (1 - loan_to_value_limit) +
      0.16 * stress_test_strength
  )

write_csv(institution_results, file.path(table_dir, "finance_leverage_r_results.csv"))
write_csv(funding_results, file.path(table_dir, "finance_leverage_r_funding.csv"))
write_csv(household_results, file.path(table_dir, "finance_leverage_r_households.csv"))
write_csv(buffer_results, file.path(table_dir, "finance_leverage_r_buffers.csv"))

p <- ggplot(institution_results, aes(x = institution, y = leverage)) +
  geom_col() +
  labs(
    title = "Leverage by Institution",
    subtitle = "Higher leverage means a thinner equity cushion relative to assets.",
    x = NULL,
    y = "Assets / equity"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "finance_leverage_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(institution_results)
print(funding_results)
print(household_results)
print(buffer_results)
