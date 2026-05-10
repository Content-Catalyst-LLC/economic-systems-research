# Post-Growth, Degrowth, and the Critique of Endless Expansion
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

growth <- read_csv(file.path(processed_dir, "growth_dependence.csv"), show_col_types = FALSE)
throughput <- read_csv(file.path(processed_dir, "throughput_scenarios.csv"), show_col_types = FALSE)
wellbeing <- read_csv(file.path(processed_dir, "wellbeing_dashboard.csv"), show_col_types = FALSE)
transition <- read_csv(file.path(processed_dir, "degrowth_transition.csv"), show_col_types = FALSE)

growth_results <- growth |>
  mutate(
    growth_dependence_score = rowMeans(across(c(
      employment_dependency,
      debt_service_dependency,
      fiscal_dependency,
      asset_dependency,
      pension_dependency,
      housing_market_dependency,
      political_legitimacy_dependency
    )))
  )

throughput_results <- throughput |>
  mutate(
    throughput_index = population * affluence * intensity,
    wellbeing_per_throughput = wellbeing_index / throughput_index
  )

wellbeing_results <- wellbeing |>
  mutate(
    wellbeing_score = rowMeans(across(c(
      health,
      time_balance,
      security,
      equality,
      public_goods,
      ecological_quality,
      care_support,
      social_trust
    )))
  )

transition_results <- transition |>
  mutate(
    degrowth_transition_score =
      0.18 * throughput_reduction +
      0.20 * redistribution +
      0.20 * public_services +
      0.16 * democratic_legitimacy +
      0.14 * macro_stabilization +
      0.12 * employment_security
  )

write_csv(growth_results, file.path(table_dir, "post_growth_r_growth_dependence_results.csv"))
write_csv(throughput_results, file.path(table_dir, "post_growth_r_throughput_results.csv"))
write_csv(wellbeing_results, file.path(table_dir, "post_growth_r_wellbeing_results.csv"))
write_csv(transition_results, file.path(table_dir, "post_growth_r_transition_results.csv"))

p <- ggplot(throughput_results, aes(x = scenario, y = throughput_index)) +
  geom_col() +
  labs(
    title = "Throughput Index",
    subtitle = "Population multiplied by affluence and material intensity.",
    x = NULL,
    y = "Throughput index"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "post_growth_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(growth_results)
print(throughput_results)
print(wellbeing_results)
print(transition_results)
