# The Future of Economic Systems in an Age of Limits
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

viability <- read_csv(file.path(processed_dir, "future_viability.csv"), show_col_types = FALSE)
throughput <- read_csv(file.path(processed_dir, "throughput_pressure.csv"), show_col_types = FALSE)
transition <- read_csv(file.path(processed_dir, "transition_capacity.csv"), show_col_types = FALSE)
wellbeing <- read_csv(file.path(processed_dir, "wellbeing_measurement.csv"), show_col_types = FALSE)

viability_results <- viability |>
  mutate(
    future_viability_score =
      0.22 * (1 - ecological_pressure) +
      0.20 * institutional_capacity +
      0.18 * social_inclusion +
      0.16 * resilience +
      0.12 * public_trust +
      0.12 * adaptive_learning
  )

throughput_results <- throughput |>
  mutate(
    throughput_pressure = population * affluence * material_intensity,
    wellbeing_per_throughput = wellbeing / throughput_pressure
  )

transition_results <- transition |>
  mutate(
    transition_capacity_score =
      0.18 * public_investment +
      0.18 * policy_credibility +
      0.16 * technology +
      0.16 * social_trust +
      0.16 * implementation_capacity +
      0.16 * coordination
  )

wellbeing_results <- wellbeing |>
  mutate(
    wellbeing_score = rowMeans(across(c(
      health,
      security,
      inclusion,
      ecological_quality,
      public_goods,
      care,
      time_balance
    )))
  )

write_csv(viability_results, file.path(table_dir, "future_systems_r_viability_results.csv"))
write_csv(throughput_results, file.path(table_dir, "future_systems_r_throughput_results.csv"))
write_csv(transition_results, file.path(table_dir, "future_systems_r_transition_results.csv"))
write_csv(wellbeing_results, file.path(table_dir, "future_systems_r_wellbeing_results.csv"))

p <- ggplot(viability_results, aes(x = scenario, y = future_viability_score)) +
  geom_col() +
  labs(
    title = "Future Viability Score",
    subtitle = "Ecological pressure, institutional capacity, inclusion, resilience, trust, and learning.",
    x = NULL,
    y = "Future viability score"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "future_economic_systems_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(viability_results)
print(throughput_results)
print(transition_results)
print(wellbeing_results)
