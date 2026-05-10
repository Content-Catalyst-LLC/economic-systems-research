# Labor, Wages, Productivity, and the Social Organization of Work
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

sectors <- read_csv(file.path(processed_dir, "sector_labor_scenarios.csv"), show_col_types = FALSE)
series <- read_csv(file.path(processed_dir, "wage_productivity_time_series.csv"), show_col_types = FALSE)
households <- read_csv(file.path(processed_dir, "household_reproduction_scenarios.csv"), show_col_types = FALSE)
time_use <- read_csv(file.path(processed_dir, "time_use_scenarios.csv"), show_col_types = FALSE)

sector_results <- sectors |>
  mutate(
    labor_productivity = output / hours_worked,
    wage_share = total_wages / output,
    average_wage = total_wages / hours_worked,
    unit_labor_cost = average_wage / labor_productivity
  )

series_results <- series |>
  mutate(
    productivity_wage_divergence = productivity_index - wage_index,
    wage_productivity_ratio = wage_index / productivity_index
  )

household_results <- households |>
  mutate(
    total_supporting_income = wage_income + social_support,
    total_reproduction_cost = household_cost + care_reproduction_cost,
    adequacy_gap = total_supporting_income - total_reproduction_cost,
    adequacy_ratio = total_supporting_income / total_reproduction_cost
  )

time_results <- time_use |>
  mutate(
    rest_recovery_time = 24 - paid_work_time - care_time - household_time - commute_time,
    total_work_burden = paid_work_time + care_time + household_time + commute_time,
    time_poverty_flag = rest_recovery_time < 8
  )

write_csv(sector_results, file.path(table_dir, "labor_r_results.csv"))
write_csv(series_results, file.path(table_dir, "labor_r_wage_productivity_series.csv"))
write_csv(household_results, file.path(table_dir, "labor_r_social_reproduction.csv"))
write_csv(time_results, file.path(table_dir, "labor_r_time_poverty.csv"))

plot_data <- series_results |>
  select(year, productivity_index, wage_index) |>
  pivot_longer(cols = c(productivity_index, wage_index), names_to = "series", values_to = "value")

p <- ggplot(plot_data, aes(x = year, y = value, color = series)) +
  geom_line(linewidth = 1) +
  labs(
    title = "Wage-Productivity Divergence",
    subtitle = "Productivity growth creates distributive possibility, but institutions shape whether wages keep pace.",
    x = "Year",
    y = "Index"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figure_dir, "labor_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(sector_results)
print(household_results)
print(time_results)
