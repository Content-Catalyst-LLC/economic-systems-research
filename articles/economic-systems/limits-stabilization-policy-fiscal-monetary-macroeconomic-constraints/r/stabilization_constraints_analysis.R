# Limits of Stabilization Policy R Workflow
#
# Purpose:
# Analyze macroeconomic constraints on fiscal and monetary stabilization.

library(readr)
library(dplyr)
library(ggplot2)
library(broom)
library(sandwich)
library(lmtest)

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("--file=", "", file_arg[1]))
  base_dir <- normalizePath(file.path(dirname(script_path), ".."))
} else {
  base_dir <- normalizePath(getwd())
}

panel_path <- file.path(base_dir, "data", "processed", "stabilization_constraints_quarterly_panel.csv")
table_dir <- file.path(base_dir, "outputs", "tables")
figure_dir <- file.path(base_dir, "outputs", "figures")

dir.create(table_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

panel <- read_csv(panel_path, show_col_types = FALSE) |>
  mutate(
    date = as.Date(date),
    recession = recession_indicator == 1,
    phase = factor(constraint_phase)
  )

phase_summary <- panel |>
  group_by(phase) |>
  summarise(
    observations = n(),
    avg_output_gap_pct = mean(output_gap_pct, na.rm = TRUE),
    avg_inflation = mean(cpi_inflation_yoy_pct, na.rm = TRUE),
    avg_unemployment = mean(unemployment_rate, na.rm = TRUE),
    avg_federal_funds_rate = mean(federal_funds_rate, na.rm = TRUE),
    avg_debt_to_gdp = mean(debt_to_gdp, na.rm = TRUE),
    avg_interest_growth_gap = mean(interest_growth_gap, na.rm = TRUE),
    avg_debt_stabilizing_primary_balance = mean(debt_stabilizing_primary_balance_pct_gdp, na.rm = TRUE),
    .groups = "drop"
  )

write_csv(phase_summary, file.path(table_dir, "constraints_r_phase_summary.csv"))

model_df <- panel |>
  select(
    federal_funds_rate,
    cpi_inflation_yoy_pct,
    output_gap_pct,
    delta_unemployment_rate,
    recession_indicator,
    lower_bound_constraint_flag,
    inflation_constraint_flag
  ) |>
  filter(
    !is.na(federal_funds_rate),
    !is.na(cpi_inflation_yoy_pct),
    !is.na(output_gap_pct),
    !is.na(delta_unemployment_rate)
  )

constraint_model <- lm(
  federal_funds_rate ~ cpi_inflation_yoy_pct + output_gap_pct +
    delta_unemployment_rate + recession_indicator +
    lower_bound_constraint_flag + inflation_constraint_flag,
  data = model_df
)

constraint_robust <- coeftest(constraint_model, vcov = vcovHC(constraint_model, type = "HC1"))
constraint_results <- tidy(constraint_robust)
write_csv(constraint_results, file.path(table_dir, "constraints_r_results.csv"))

constraint_plot <- ggplot(panel, aes(x = output_gap_pct, y = cpi_inflation_yoy_pct, color = phase)) +
  geom_point(alpha = 0.65) +
  geom_hline(yintercept = 4.0, linewidth = 0.3) +
  geom_vline(xintercept = 0.0, linewidth = 0.3) +
  labs(
    title = "Inflation and Output-Gap Constraints",
    subtitle = "Expansionary policy faces different limits when inflation is high or slack is limited.",
    x = "Output gap (%)",
    y = "CPI inflation, year over year (%)",
    color = "Phase"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figure_dir, "constraint_phase_scatter_r.png"),
  plot = constraint_plot,
  width = 8,
  height = 5,
  dpi = 300
)

print(phase_summary)
print(constraint_results)
