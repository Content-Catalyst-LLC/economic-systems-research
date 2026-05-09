# Households, Firms, Markets, and States
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

table_dir <- file.path(base_dir, "outputs", "tables")
processed_dir <- file.path(base_dir, "data", "processed")
figure_dir <- file.path(base_dir, "outputs", "figures")

dir.create(table_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

flows <- read_csv(file.path(processed_dir, "institutional_flow_scenarios.csv"), show_col_types = FALSE)

results <- flows |>
  mutate(
    household_saving = household_wages + household_transfers + asset_income -
      taxes_paid - debt_service - household_consumption,
    firm_profit = firm_revenue - labor_cost - capital_cost - input_cost,
    public_borrowing = public_spending + public_transfers + public_debt_interest - tax_revenue,
    household_stability = household_saving >= 0,
    productive_capacity = firm_profit > 0,
    institutional_capacity = public_borrowing <= 350,
    reproduction_score = as.integer(household_stability) +
      as.integer(productive_capacity) +
      as.integer(institutional_capacity)
  )

write_csv(results, file.path(table_dir, "hfms_r_results.csv"))

plot_data <- results |>
  select(scenario, household_saving, firm_profit, public_borrowing) |>
  pivot_longer(cols = c(household_saving, firm_profit, public_borrowing),
               names_to = "institutional_balance",
               values_to = "value")

flow_plot <- ggplot(plot_data, aes(x = scenario, y = value, fill = institutional_balance)) +
  geom_col(position = "dodge") +
  labs(
    title = "Households, Firms, Markets, and States: Institutional Balances",
    subtitle = "Household saving, firm profit, and public borrowing shift across scenarios.",
    x = NULL,
    y = "Flow units"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "hfms_r.png"),
  plot = flow_plot,
  width = 9,
  height = 5,
  dpi = 300
)

print(results)
