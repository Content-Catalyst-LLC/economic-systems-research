# Capital, Investment, and the Dynamics of Accumulation
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

capital <- read_csv(file.path(processed_dir, "capital_stock_scenarios.csv"), show_col_types = FALSE)
projects <- read_csv(file.path(processed_dir, "investment_project_scenarios.csv"), show_col_types = FALSE)
maintenance <- read_csv(file.path(processed_dir, "maintenance_scenarios.csv"), show_col_types = FALSE)

simulate_capital <- function(row, periods = 15) {
  K <- numeric(periods + 1)
  K[1] <- row$initial_capital

  for (t in 1:periods) {
    K[t + 1] <- K[t] + row$annual_investment - row$depreciation_rate * K[t]
  }

  data.frame(
    scenario = row$scenario,
    period = 0:periods,
    capital_stock = K,
    capital_intensity = K / row$labor,
    investment_rate = row$annual_investment / row$output
  )
}

paths <- bind_rows(lapply(seq_len(nrow(capital)), function(i) simulate_capital(capital[i, ])))

npv <- function(cashflows, r) {
  sum(cashflows / ((1 + r)^(0:(length(cashflows) - 1))))
}

cashflow_cols <- paste0("cashflow_year_", 0:5)

project_results <- projects |>
  rowwise() |>
  mutate(
    npv_private = npv(c_across(all_of(cashflow_cols)), private_discount_rate),
    npv_public = npv(c_across(all_of(cashflow_cols)), public_discount_rate),
    public_private_npv_gap = npv_public - npv_private
  ) |>
  ungroup() |>
  select(project, npv_private, npv_public, public_private_npv_gap)

backlog_paths <- maintenance |>
  arrange(scenario, period) |>
  group_by(scenario) |>
  mutate(
    backlog_change = new_maintenance_need - actual_maintenance,
    maintenance_backlog = first(initial_backlog) + cumsum(lag(backlog_change, default = 0))
  ) |>
  ungroup()

write_csv(paths, file.path(table_dir, "capital_r_results.csv"))
write_csv(project_results, file.path(table_dir, "capital_r_npv_results.csv"))
write_csv(backlog_paths, file.path(table_dir, "capital_r_maintenance_backlog.csv"))

p <- ggplot(paths, aes(x = period, y = capital_stock, color = scenario)) +
  geom_line(linewidth = 1) +
  labs(
    title = "Capital Stock Paths",
    subtitle = "Accumulation depends on investment, depreciation, and the preservation of serviceable assets.",
    x = "Period",
    y = "Capital stock"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figure_dir, "capital_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(paths)
print(project_results)
print(backlog_paths)
