# Inflation, Energy Shocks, and Supply Constraints
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

prices <- read_csv(file.path(processed_dir, "price_index_scenarios.csv"), show_col_types = FALSE)
pass_through <- read_csv(file.path(processed_dir, "sector_energy_pass_through_scenarios.csv"), show_col_types = FALSE)
households <- read_csv(file.path(processed_dir, "household_energy_burden_scenarios.csv"), show_col_types = FALSE)
bottlenecks <- read_csv(file.path(processed_dir, "supply_bottleneck_scenarios.csv"), show_col_types = FALSE)

price_results <- prices |>
  group_by(scenario) |>
  arrange(period, .by_group = TRUE) |>
  mutate(
    inflation_rate = price_level / lag(price_level) - 1,
    inflation_rate = ifelse(is.na(inflation_rate), 0, inflation_rate),
    cumulative_inflation = price_level / first(price_level) - 1
  ) |>
  ungroup()

pass_results <- pass_through |>
  mutate(
    estimated_price_change =
      alpha_energy * energy_cost_change +
      beta_wage * wage_cost_change +
      gamma_materials * materials_cost_change,
    energy_share_of_pass_through =
      (alpha_energy * energy_cost_change) / estimated_price_change
  )

household_results <- households |>
  mutate(
    household_energy_burden = energy_spending / income,
    transport_fuel_burden = transport_fuel_spending / income,
    combined_energy_transport_burden = (energy_spending + transport_fuel_spending) / income,
    real_wage = ifelse(nominal_wage > 0, nominal_wage / price_level_relative, 0)
  )

bottleneck_results <- bottlenecks |>
  rowwise() |>
  mutate(
    effective_output_capacity = min(c(capital_capacity, labor_capacity, energy_capacity, logistics_capacity, supply_availability)),
    bottleneck_gap = 1 - effective_output_capacity
  ) |>
  ungroup()

write_csv(price_results, file.path(table_dir, "inflation_energy_r_results.csv"))
write_csv(pass_results, file.path(table_dir, "inflation_energy_r_pass_through.csv"))
write_csv(household_results, file.path(table_dir, "inflation_energy_r_households.csv"))
write_csv(bottleneck_results, file.path(table_dir, "inflation_energy_r_bottlenecks.csv"))

p <- ggplot(price_results, aes(x = period, y = price_level, color = scenario)) +
  geom_line(linewidth = 1) +
  labs(
    title = "Price Level Paths Under Inflation Scenarios",
    subtitle = "Energy shocks and supply bottlenecks can create persistent price pressure even without a conventional demand boom.",
    x = "Period",
    y = "Price index"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figure_dir, "inflation_energy_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(price_results)
print(pass_results)
print(household_results)
print(bottleneck_results)
