# Beyond GDP: Measuring Well-Being, Inclusion, and Sustainability
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

dashboard <- read_csv(file.path(processed_dir, "gdp_dashboard_scenarios.csv"), show_col_types = FALSE)
inclusion <- read_csv(file.path(processed_dir, "inclusion_scenarios.csv"), show_col_types = FALSE)
stocks <- read_csv(file.path(processed_dir, "sustainability_stocks.csv"), show_col_types = FALSE)
adjusted <- read_csv(file.path(processed_dir, "adjusted_progress.csv"), show_col_types = FALSE)

dashboard_results <- dashboard |>
  mutate(
    gdp = consumption + investment + government + net_exports,
    wellbeing_score = rowMeans(across(c(health, education, income_security, housing, safety, social_connection, environment, time_balance))),
    gdp_wellbeing_gap = (gdp / max(gdp)) - wellbeing_score
  )

inclusion_results <- inclusion |>
  mutate(
    inclusion_score =
      0.22 * distribution +
      0.18 * mobility +
      0.20 * access +
      0.18 * voice +
      0.12 * regional_equity +
      0.10 * service_reach
  )

stocks_results <- stocks |>
  mutate(
    sustainability_score =
      0.26 * natural_capital +
      0.22 * human_capital +
      0.20 * institutional_trust +
      0.16 * produced_capital +
      0.08 * (1 - maintenance_gap) +
      0.08 * (1 - ecological_pressure)
  )

adjusted_results <- adjusted |>
  mutate(
    adjusted_progress = current_benefits - social_costs - ecological_costs - defensive_expenditure + unpaid_care_value + public_goods_value,
    adjusted_progress_ratio = adjusted_progress / current_benefits
  )

write_csv(dashboard_results, file.path(table_dir, "beyond_gdp_r_dashboard_results.csv"))
write_csv(inclusion_results, file.path(table_dir, "beyond_gdp_r_inclusion_results.csv"))
write_csv(stocks_results, file.path(table_dir, "beyond_gdp_r_sustainability_results.csv"))
write_csv(adjusted_results, file.path(table_dir, "beyond_gdp_r_adjusted_progress_results.csv"))

p <- ggplot(dashboard_results, aes(x = scenario, y = wellbeing_score)) +
  geom_col() +
  labs(
    title = "Well-Being Score",
    subtitle = "A multidimensional score placed alongside GDP.",
    x = NULL,
    y = "Composite well-being score"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "beyond_gdp_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(dashboard_results)
print(inclusion_results)
print(stocks_results)
print(adjusted_results)
