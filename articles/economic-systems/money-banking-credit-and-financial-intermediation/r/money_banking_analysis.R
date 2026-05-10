# Money, Banking, Credit, and Financial Intermediation
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

money <- read_csv(file.path(processed_dir, "money_aggregate_scenarios.csv"), show_col_types = FALSE)
banks <- read_csv(file.path(processed_dir, "bank_balance_sheet_scenarios.csv"), show_col_types = FALSE)
liquidity <- read_csv(file.path(processed_dir, "liquidity_stress_scenarios.csv"), show_col_types = FALSE)
credit <- read_csv(file.path(processed_dir, "credit_allocation_scenarios.csv"), show_col_types = FALSE)

money_results <- money |>
  mutate(
    money_supply = currency + deposits,
    broad_liquidity_proxy = money_supply + near_money_claims,
    deposit_share_of_money = deposits / money_supply
  )

bank_results <- banks |>
  mutate(
    leverage = assets / equity,
    capital_ratio = equity / assets,
    loan_to_deposit_ratio = loans / bank_deposits,
    liquid_asset_ratio = liquid_assets / assets
  )

liquidity_results <- liquidity |>
  mutate(
    liquidity_coverage_ratio = hqla / net_cash_outflows,
    liquidity_stress_flag = liquidity_coverage_ratio < 1
  )

credit_results <- credit |>
  mutate(
    developmental_credit_score =
      0.34 * productive_score +
      0.28 * resilience_score +
      0.22 * inclusion_score +
      0.16 * (1 - speculation_score),
    weighted_developmental_contribution = flow_share * developmental_credit_score
  )

write_csv(money_results, file.path(table_dir, "money_banking_r_money_results.csv"))
write_csv(bank_results, file.path(table_dir, "money_banking_r_results.csv"))
write_csv(liquidity_results, file.path(table_dir, "money_banking_r_liquidity.csv"))
write_csv(credit_results, file.path(table_dir, "money_banking_r_credit_allocation.csv"))

p <- ggplot(bank_results, aes(x = bank, y = leverage)) +
  geom_col() +
  labs(
    title = "Bank Leverage by Institution",
    subtitle = "Leverage magnifies both returns and fragility.",
    x = NULL,
    y = "Assets / equity"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "money_banking_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(money_results)
print(bank_results)
print(liquidity_results)
print(credit_results)
