# Fiscal Policy, Taxation, and Public Investment
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

fiscal <- read_csv(file.path(processed_dir, "fiscal_position_scenarios.csv"), show_col_types = FALSE)
taxes <- read_csv(file.path(processed_dir, "tax_distribution_scenarios.csv"), show_col_types = FALSE)
spending <- read_csv(file.path(processed_dir, "spending_composition_scenarios.csv"), show_col_types = FALSE)
maintenance <- read_csv(file.path(processed_dir, "infrastructure_maintenance_scenarios.csv"), show_col_types = FALSE)

fiscal_results <- fiscal |>
  mutate(
    budget_balance = tax_revenue - public_spending,
    primary_balance = tax_revenue - primary_spending,
    tax_ratio = tax_revenue / output,
    spending_ratio = public_spending / output,
    debt_to_output = debt_stock / output,
    interest_cost = interest_rate * debt_stock,
    next_period_debt = debt_stock + (public_spending - tax_revenue) + interest_cost,
    next_period_debt_to_output = next_period_debt / output
  )

tax_results <- taxes |>
  mutate(
    effective_tax_rate = tax_paid / income,
    total_tax_with_consumption_and_wealth = tax_paid + consumption_tax_paid + wealth_tax_paid,
    broad_effective_tax_rate = total_tax_with_consumption_and_wealth / income,
    net_transfer_position = transfer_received - total_tax_with_consumption_and_wealth
  )

spending_results <- spending |>
  mutate(
    public_investment_share = public_investment_component / spending_amount,
    current_service_share = current_service_component / spending_amount,
    weighted_resilience_contribution = spending_amount * resilience_score
  )

maintenance_results <- maintenance |>
  mutate(
    maintenance_gap = maintenance_needed - maintenance_actual,
    maintenance_gap_ratio = maintenance_gap / maintenance_needed
  )

write_csv(fiscal_results, file.path(table_dir, "fiscal_policy_r_results.csv"))
write_csv(tax_results, file.path(table_dir, "fiscal_policy_r_tax_results.csv"))
write_csv(spending_results, file.path(table_dir, "fiscal_policy_r_spending_results.csv"))
write_csv(maintenance_results, file.path(table_dir, "fiscal_policy_r_maintenance_results.csv"))

p <- ggplot(fiscal_results, aes(x = scenario, y = next_period_debt_to_output)) +
  geom_col() +
  labs(
    title = "Next-Period Public Debt to Output",
    subtitle = "Debt dynamics depend on balances, interest costs, and the output base.",
    x = NULL,
    y = "Debt / output"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "fiscal_policy_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(fiscal_results)
print(tax_results)
print(spending_results)
print(maintenance_results)
