# Macroeconomic Stability, Business Cycles, and Crisis
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

demand <- read_csv(file.path(processed_dir, "aggregate_demand_scenarios.csv"), show_col_types = FALSE)
cycle <- read_csv(file.path(processed_dir, "business_cycle_phase_scenarios.csv"), show_col_types = FALSE)
households <- read_csv(file.path(processed_dir, "household_balance_sheet_scenarios.csv"), show_col_types = FALSE)
fiscal <- read_csv(file.path(processed_dir, "fiscal_stabilization_scenarios.csv"), show_col_types = FALSE)

demand_results <- demand |>
  mutate(
    output = consumption + investment + government_spending + net_exports,
    output_gap = (output - potential_output) / potential_output,
    consumption_share = consumption / output,
    investment_share = investment / output,
    government_share = government_spending / output
  )

cycle_results <- cycle |>
  mutate(
    output_growth = output_index / lag(output_index) - 1,
    output_growth = ifelse(is.na(output_growth), 0, output_growth),
    employment_growth = employment_index / lag(employment_index) - 1,
    employment_growth = ifelse(is.na(employment_growth), 0, employment_growth)
  )

household_results <- households |>
  mutate(
    debt_burden_ratio = debt_service / income,
    savings_buffer_months = liquid_savings / (income / 12),
    post_shock_income = income * (1 - job_loss_income_shock),
    post_shock_debt_burden_ratio = debt_service / post_shock_income
  )

fiscal_results <- fiscal |>
  mutate(
    delta_y = fiscal_multiplier * delta_g,
    stabilized_gap = initial_output_gap + (delta_y / 1000) + (0.04 * automatic_stabilizer_strength)
  )

write_csv(demand_results, file.path(table_dir, "macro_stability_r_results.csv"))
write_csv(cycle_results, file.path(table_dir, "macro_stability_r_cycle_results.csv"))
write_csv(household_results, file.path(table_dir, "macro_stability_r_household_results.csv"))
write_csv(fiscal_results, file.path(table_dir, "macro_stability_r_fiscal_results.csv"))

plot_data <- cycle_results |>
  select(year, output_index, employment_index) |>
  pivot_longer(cols = c(output_index, employment_index), names_to = "series", values_to = "value")

p <- ggplot(plot_data, aes(x = year, y = value, color = series)) +
  geom_line(linewidth = 1) +
  labs(
    title = "Business-Cycle Output and Employment Paths",
    subtitle = "Output and employment often move together, but employment can recover more slowly after crisis.",
    x = "Year",
    y = "Index"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figure_dir, "macro_stability_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(demand_results)
print(cycle_results)
print(household_results)
print(fiscal_results)
