# Scarcity, Allocation, and the Organization of Material Life
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

scenarios <- read_csv(file.path(processed_dir, "allocation_scenarios.csv"), show_col_types = FALSE)
priorities <- read_csv(file.path(processed_dir, "allocation_priorities.csv"), show_col_types = FALSE)
households <- read_csv(file.path(processed_dir, "access_households.csv"), show_col_types = FALSE)

total_resources <- 1000

allocation_results <- scenarios |>
  left_join(priorities, by = "priority") |>
  mutate(
    allocation_units = share * total_resources,
    essentiality_weighted_allocation = allocation_units * essentiality,
    resilience_weighted_allocation = allocation_units * resilience_value
  )

scenario_summary <- allocation_results |>
  group_by(scenario) |>
  summarise(
    total_allocation = sum(allocation_units),
    essentiality_weighted_total = sum(essentiality_weighted_allocation),
    resilience_weighted_total = sum(resilience_weighted_allocation),
    .groups = "drop"
  )

write_csv(scenario_summary, file.path(table_dir, "scarcity_allocation_r_results.csv"))

access <- households |>
  mutate(
    effective_access = 0.35 * income_command +
      0.35 * institutional_access +
      0.20 * (1 - price_index) +
      0.10 * need_index,
    access_gap = need_index - effective_access,
    deprivation_flag = access_gap > 0.25,
    weighted_access_gap = access_gap * population_weight
  )

write_csv(access, file.path(table_dir, "scarcity_allocation_r_access_metrics.csv"))

plot_data <- allocation_results |>
  filter(priority %in% c("Housing", "Health", "Infrastructure", "Care", "Ecological Restoration"))

allocation_plot <- ggplot(plot_data, aes(x = priority, y = allocation_units, fill = scenario)) +
  geom_col(position = "dodge") +
  labs(
    title = "Scarcity and Allocation Across Social Priorities",
    subtitle = "Scenario choices reveal trade-offs among essential services, repair, and future capacity.",
    x = NULL,
    y = "Resource units"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "scarcity_allocation_r.png"),
  plot = allocation_plot,
  width = 9,
  height = 5,
  dpi = 300
)

print(scenario_summary)
print(access)
