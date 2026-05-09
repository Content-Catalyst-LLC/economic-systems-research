# Supply, Demand, Prices, and Economic Coordination
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

scenarios <- read_csv(file.path(processed_dir, "market_parameter_scenarios.csv"), show_col_types = FALSE)

results <- scenarios |>
  mutate(
    competitive_price = (a - c) / (b + d),
    equilibrium_price = competitive_price * (1 + markup_rate),
    equilibrium_quantity = a - b * equilibrium_price,
    demand_elasticity = -b * (equilibrium_price / equilibrium_quantity),
    supply_elasticity = d * (equilibrium_price / equilibrium_quantity),
    marginal_social_cost_price = equilibrium_price + external_cost,
    social_cost_gap = marginal_social_cost_price - equilibrium_price
  )

baseline <- results |>
  filter(scenario == "baseline") |>
  slice(1)

results <- results |>
  mutate(
    price_change_from_baseline = equilibrium_price - baseline$equilibrium_price,
    quantity_change_from_baseline = equilibrium_quantity - baseline$equilibrium_quantity
  )

write_csv(results, file.path(table_dir, "supply_demand_r_results.csv"))

plot_data <- results |>
  select(scenario, equilibrium_price, equilibrium_quantity)

p <- ggplot(plot_data, aes(x = scenario, y = equilibrium_price)) +
  geom_col() +
  labs(
    title = "Equilibrium Price Across Supply-Demand Scenarios",
    subtitle = "Demand shifts, supply shocks, rigidity, and market power alter price formation.",
    x = NULL,
    y = "Equilibrium price"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "supply_demand_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(results)
