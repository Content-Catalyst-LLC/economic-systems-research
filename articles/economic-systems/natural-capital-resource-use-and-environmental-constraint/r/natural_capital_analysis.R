# Natural Capital, Resource Use, and Environmental Constraint
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

stock <- read_csv(file.path(processed_dir, "stock_flow_scenarios.csv"), show_col_types = FALSE)
resources <- read_csv(file.path(processed_dir, "resource_use_constraints.csv"), show_col_types = FALSE)
sectors <- read_csv(file.path(processed_dir, "sector_resource_pressure.csv"), show_col_types = FALSE)
governance <- read_csv(file.path(processed_dir, "governance_regimes.csv"), show_col_types = FALSE)

stock_results <- stock |>
  mutate(
    natural_capital_next = natural_capital_t + regeneration - degradation,
    regeneration_gap = degradation - regeneration,
    threshold_distance = natural_capital_next - threshold
  )

resources_results <- resources |>
  mutate(
    resource_use_ratio = ifelse(regenerative_capacity > 0, resource_use / regenerative_capacity, Inf),
    waste_constraint_ratio = emissions / absorptive_capacity
  )

sector_results <- sectors |>
  mutate(
    sector_pressure_score =
      0.18 * material_intensity +
      0.18 * energy_intensity +
      0.16 * water_intensity +
      0.14 * land_intensity +
      0.14 * waste_intensity +
      0.12 * import_dependence +
      0.08 * social_necessity
  )

governance_results <- governance |>
  mutate(
    resource_governance_score =
      0.14 * secure_tenure +
      0.16 * monitoring +
      0.16 * participation +
      0.14 * enforcement +
      0.16 * adaptive_rules +
      0.12 * equity +
      0.12 * regeneration_alignment
  )

write_csv(stock_results, file.path(table_dir, "natural_capital_r_stock_results.csv"))
write_csv(resources_results, file.path(table_dir, "natural_capital_r_resource_results.csv"))
write_csv(sector_results, file.path(table_dir, "natural_capital_r_sector_results.csv"))
write_csv(governance_results, file.path(table_dir, "natural_capital_r_governance_results.csv"))

p <- ggplot(stock_results, aes(x = system, y = natural_capital_next)) +
  geom_col() +
  labs(
    title = "Natural Capital Next Period",
    subtitle = "Natural capital changes through the balance between regeneration and degradation.",
    x = NULL,
    y = "Stock index"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "natural_capital_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(stock_results)
print(resources_results)
print(sector_results)
print(governance_results)
