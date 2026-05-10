# Monetary Policy, Central Banking, and Financial Conditions
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

policy <- read_csv(file.path(processed_dir, "policy_rate_scenarios.csv"), show_col_types = FALSE)
debt <- read_csv(file.path(processed_dir, "debt_service_scenarios.csv"), show_col_types = FALSE)
conditions <- read_csv(file.path(processed_dir, "financial_conditions_scenarios.csv"), show_col_types = FALSE)

policy_results <- policy |>
  mutate(
    real_rate = nominal_rate - expected_inflation,
    policy_rate_rule = neutral_rate + a_inflation * inflation_gap + b_output * output_gap,
    stance_gap = nominal_rate - policy_rate_rule
  )

debt_results <- debt |>
  mutate(
    debt_service_ratio = debt_service / income,
    additional_debt_service = debt_stock * repricing_share * rate_shock / 12,
    post_shock_debt_service = debt_service + additional_debt_service,
    post_shock_dsr = post_shock_debt_service / income
  )

conditions_results <- conditions |>
  mutate(
    financial_conditions_index =
      policy_rate +
      credit_spread +
      exchange_rate_pressure +
      lending_tightness * 0.08 +
      market_liquidity_stress * 0.08 -
      equity_price_change * 0.18
  )

write_csv(policy_results, file.path(table_dir, "monetary_policy_r_results.csv"))
write_csv(debt_results, file.path(table_dir, "monetary_policy_r_debt_results.csv"))
write_csv(conditions_results, file.path(table_dir, "monetary_policy_r_conditions_results.csv"))

p <- ggplot(conditions_results, aes(x = scenario, y = financial_conditions_index)) +
  geom_col() +
  labs(
    title = "Composite Financial Conditions Index",
    subtitle = "Effective monetary stance includes rates, spreads, exchange pressure, lending standards, liquidity stress, and asset prices.",
    x = NULL,
    y = "Composite restraint score"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "monetary_policy_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(policy_results)
print(debt_results)
print(conditions_results)
