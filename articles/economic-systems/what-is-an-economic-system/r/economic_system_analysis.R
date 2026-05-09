# What Is an Economic System? R Workflow
#
# Purpose:
# Replicate input-output results and summarize distributional/system indicators.

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

results <- read_csv(file.path(processed_dir, "economic_system_results.csv"), show_col_types = FALSE)
sectors <- read_csv(file.path(processed_dir, "economic_system_sectors.csv"), show_col_types = FALSE)

scenario_summary <- results |>
  group_by(scenario) |>
  summarise(
    total_system_output = sum(total_output, na.rm = TRUE),
    total_final_demand = sum(final_demand, na.rm = TRUE),
    total_indirect_requirement = sum(indirect_output_requirement, na.rm = TRUE),
    avg_output_multiplier = mean(output_multiplier, na.rm = TRUE),
    .groups = "drop"
  )

write_csv(scenario_summary, file.path(table_dir, "economic_system_r_results.csv"))

baseline_distribution <- results |>
  filter(scenario == "baseline") |>
  left_join(sectors, by = "sector_code") |>
  mutate(
    labor_income = total_output * wage_share,
    capital_income = total_output * profit_share,
    ecological_pressure = total_output * ecological_intensity,
    employment_requirement = total_output * employment_intensity
  )

distribution_summary <- baseline_distribution |>
  summarise(
    total_output = sum(total_output),
    labor_income = sum(labor_income),
    capital_income = sum(capital_income),
    wage_share_system = labor_income / total_output,
    profit_share_system = capital_income / total_output,
    ecological_pressure = sum(ecological_pressure),
    employment_requirement = sum(employment_requirement)
  )

write_csv(distribution_summary, file.path(table_dir, "economic_system_r_distribution_summary.csv"))

plot_data <- scenario_summary |>
  arrange(desc(total_system_output))

system_plot <- ggplot(plot_data, aes(x = reorder(scenario, total_system_output), y = total_system_output)) +
  geom_col() +
  coord_flip() +
  labs(
    title = "Total System Output by Scenario",
    subtitle = "Input-output interdependence means final-demand changes ripple across sectors.",
    x = NULL,
    y = "Total system output"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figure_dir, "distribution_metrics_r.png"),
  plot = system_plot,
  width = 8,
  height = 5,
  dpi = 300
)

print(scenario_summary)
print(distribution_summary)
