# Consumer Choice, Household Welfare, and Everyday Economic Life
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

households <- read_csv(file.path(processed_dir, "household_profiles.csv"), show_col_types = FALSE)

results <- households |>
  mutate(
    total_consumption = rent + food + transport + utilities + health + other,
    essentials_spending = rent + food + transport + utilities + health,
    saving = income + transfers + liquid_assets - debt_service - other_fixed_burdens - total_consumption,
    essentials_ratio = essentials_spending / (income + transfers),
    fragility_ratio = (essentials_spending + debt_service + other_fixed_burdens) /
      (income + transfers + liquid_assets),
    rest_discretionary_hours = 24 - paid_labor_hours - care_hours - commute_hours - household_admin_hours,
    time_poverty_flag = rest_discretionary_hours < 8
  )

summary <- results |>
  summarise(
    weighted_essentials_ratio = sum(essentials_ratio * population_weight) / sum(population_weight),
    weighted_fragility_ratio = sum(fragility_ratio * population_weight) / sum(population_weight),
    weighted_rest_hours = sum(rest_discretionary_hours * population_weight) / sum(population_weight),
    population_share_time_poor = sum(as.integer(time_poverty_flag) * population_weight) / sum(population_weight),
    population_share_negative_saving = sum(as.integer(saving < 0) * population_weight) / sum(population_weight)
  )

write_csv(results, file.path(table_dir, "consumer_choice_r_results.csv"))
write_csv(summary, file.path(table_dir, "consumer_choice_r_summary.csv"))

plot_data <- results |>
  select(household_group, essentials_ratio, fragility_ratio) |>
  pivot_longer(cols = c(essentials_ratio, fragility_ratio), names_to = "indicator", values_to = "value")

p <- ggplot(plot_data, aes(x = household_group, y = value, fill = indicator)) +
  geom_col(position = "dodge") +
  labs(
    title = "Household Essentials Burden and Fragility",
    subtitle = "Consumer choice is constrained by essentials costs, debt service, fixed burdens, and buffers.",
    x = NULL,
    y = "Ratio"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "consumer_choice_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(summary)
