# Economic Systems Within Planetary Boundaries
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

boundaries <- read_csv(file.path(processed_dir, "boundary_pressure.csv"), show_col_types = FALSE)
resources <- read_csv(file.path(processed_dir, "resource_use_identity.csv"), show_col_types = FALSE)
transition <- read_csv(file.path(processed_dir, "transition_capacity.csv"), show_col_types = FALSE)
accounting <- read_csv(file.path(processed_dir, "boundary_accounting.csv"), show_col_types = FALSE)

boundary_results <- boundaries |>
  mutate(
    boundary_pressure_ratio = economic_pressure / earth_system_capacity,
    overshoot_gap = pmax(boundary_pressure_ratio - 1, 0)
  )

resource_results <- resources |>
  mutate(
    resource_use = population * affluence * resource_intensity,
    resource_wellbeing_efficiency = wellbeing_index / resource_use
  )

transition_results <- transition |>
  mutate(
    transition_capacity_score =
      0.20 * state_capacity +
      0.18 * public_investment +
      0.18 * social_legitimacy +
      0.16 * technological_capability +
      0.14 * coordination +
      0.14 * adaptive_governance
  )

accounting_results <- accounting |>
  mutate(
    boundary_aware_progress =
      0.30 * wellbeing +
      0.22 * inclusion +
      0.20 * natural_capital +
      0.12 * (1 - material_throughput) +
      0.12 * (1 - ecological_pressure)
  )

write_csv(boundary_results, file.path(table_dir, "planetary_boundaries_r_boundary_results.csv"))
write_csv(resource_results, file.path(table_dir, "planetary_boundaries_r_resource_results.csv"))
write_csv(transition_results, file.path(table_dir, "planetary_boundaries_r_transition_results.csv"))
write_csv(accounting_results, file.path(table_dir, "planetary_boundaries_r_accounting_results.csv"))

p <- ggplot(boundary_results, aes(x = boundary, y = boundary_pressure_ratio)) +
  geom_col() +
  geom_hline(yintercept = 1, linetype = "dashed") +
  labs(
    title = "Boundary Pressure Ratio",
    subtitle = "Economic pressure divided by Earth-system capacity.",
    x = NULL,
    y = "Pressure / capacity"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "planetary_boundaries_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(boundary_results)
print(resource_results)
print(transition_results)
print(accounting_results)
