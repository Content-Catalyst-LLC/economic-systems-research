# Economic Resilience, Fragility, and Adaptive Capacity
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

resilience <- read_csv(file.path(processed_dir, "resilience_scenarios.csv"), show_col_types = FALSE)
fragility <- read_csv(file.path(processed_dir, "fragility_scenarios.csv"), show_col_types = FALSE)
adaptive <- read_csv(file.path(processed_dir, "adaptive_capacity.csv"), show_col_types = FALSE)
shocks <- read_csv(file.path(processed_dir, "shock_scenarios.csv"), show_col_types = FALSE)

resilience_results <- resilience |>
  mutate(
    resilience_score =
      0.18 * buffers +
      0.18 * redundancy +
      0.18 * coordination +
      0.14 * trust +
      0.16 * learning +
      0.16 * recovery_capacity
  )

fragility_results <- fragility |>
  mutate(
    fragility_score =
      0.20 * leverage +
      0.18 * concentration +
      0.20 * exposure +
      0.18 * underinvestment +
      0.14 * inequality +
      0.10 * political_fragmentation
  )

adaptive_results <- adaptive |>
  mutate(
    adaptive_capacity_score =
      0.18 * information +
      0.18 * fiscal_space +
      0.16 * skills +
      0.16 * flexibility +
      0.16 * legitimacy +
      0.16 * implementation_capacity
  )

shock_results <- shocks |>
  mutate(
    vulnerability =
      0.26 * household_vulnerability +
      0.22 * firm_vulnerability +
      0.18 * (1 - public_capacity) +
      0.18 * (1 - infrastructure_integrity) +
      0.16 * (1 - recovery_speed),
    shock_impact = shock_magnitude * vulnerability
  )

write_csv(resilience_results, file.path(table_dir, "economic_resilience_r_resilience_results.csv"))
write_csv(fragility_results, file.path(table_dir, "economic_resilience_r_fragility_results.csv"))
write_csv(adaptive_results, file.path(table_dir, "economic_resilience_r_adaptive_results.csv"))
write_csv(shock_results, file.path(table_dir, "economic_resilience_r_shock_results.csv"))

p <- ggplot(shock_results, aes(x = shock, y = shock_impact)) +
  geom_col() +
  labs(
    title = "Shock Impact",
    subtitle = "Shock magnitude multiplied by system vulnerability.",
    x = NULL,
    y = "Shock impact index"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "economic_resilience_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(resilience_results)
print(fragility_results)
print(adaptive_results)
print(shock_results)
