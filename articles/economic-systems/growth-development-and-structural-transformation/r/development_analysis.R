# Growth, Development, and Structural Transformation
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

growth <- read_csv(file.path(processed_dir, "growth_path_scenarios.csv"), show_col_types = FALSE)
sectors <- read_csv(file.path(processed_dir, "sector_transformation_scenarios.csv"), show_col_types = FALSE)
capability <- read_csv(file.path(processed_dir, "development_capability_scenarios.csv"), show_col_types = FALSE)
energy <- read_csv(file.path(processed_dir, "energy_ecology_scenarios.csv"), show_col_types = FALSE)

growth_results <- growth |>
  group_by(scenario) |>
  arrange(period, .by_group = TRUE) |>
  mutate(
    growth_rate = output / lag(output) - 1,
    growth_rate = ifelse(is.na(growth_rate), 0, growth_rate),
    labor_productivity = output / labor,
    cumulative_growth = output / first(output) - 1
  ) |>
  ungroup()

sector_results <- sectors |>
  group_by(scenario) |>
  mutate(
    total_output = sum(sector_output),
    total_labor = sum(sector_labor),
    output_share = sector_output / total_output,
    labor_share = sector_labor / total_labor,
    sector_productivity = sector_output / sector_labor
  ) |>
  ungroup()

capability_results <- capability |>
  mutate(
    capability_index =
      0.22 * income_index +
      0.20 * health_index +
      0.20 * education_index +
      0.22 * infrastructure_index +
      0.16 * security_index
  )

energy_results <- energy |>
  mutate(
    energy_intensity = energy_use / output,
    emissions_intensity = emissions / output,
    sustainable_growth_score =
      0.30 * (1 - energy_intensity / max(energy_intensity)) +
      0.30 * (1 - emissions_intensity / max(emissions_intensity)) +
      0.25 * renewable_share +
      0.15 * (1 - resource_stress)
  )

write_csv(growth_results, file.path(table_dir, "development_r_results.csv"))
write_csv(sector_results, file.path(table_dir, "development_r_sector_results.csv"))
write_csv(capability_results, file.path(table_dir, "development_r_capability_results.csv"))
write_csv(energy_results, file.path(table_dir, "development_r_energy_results.csv"))

p <- ggplot(growth_results, aes(x = period, y = output, color = scenario)) +
  geom_line(linewidth = 1) +
  labs(
    title = "Growth Paths by Development Scenario",
    subtitle = "Similar early expansion can conceal very different long-run transformation trajectories.",
    x = "Period",
    y = "Output index"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figure_dir, "development_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(growth_results)
print(sector_results)
print(capability_results)
print(energy_results)
