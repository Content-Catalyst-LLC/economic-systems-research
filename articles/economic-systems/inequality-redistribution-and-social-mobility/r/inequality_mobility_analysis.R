# Inequality, Redistribution, and Social Mobility
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

income <- read_csv(file.path(processed_dir, "income_distribution.csv"), show_col_types = FALSE)
mobility <- read_csv(file.path(processed_dir, "mobility_scenarios.csv"), show_col_types = FALSE)
labor <- read_csv(file.path(processed_dir, "labor_market_scenarios.csv"), show_col_types = FALSE)
place <- read_csv(file.path(processed_dir, "housing_place_scenarios.csv"), show_col_types = FALSE)

income_results <- income |>
  mutate(
    disposable_income = market_income - taxes + transfers,
    service_adjusted_income = disposable_income + public_service_value,
    housing_adjusted_income = service_adjusted_income - housing_cost - debt_service,
    market_income_share = market_income / sum(market_income),
    disposable_income_share = disposable_income / sum(disposable_income),
    housing_cost_burden = housing_cost / disposable_income,
    redistributive_gain = disposable_income - market_income
  )

mobility_results <- mobility |>
  mutate(
    predicted_child_outcome = baseline_a + persistence_b * parent_outcome,
    opportunity_score =
      0.22 * education_access +
      0.20 * health_access +
      0.20 * place_advantage +
      0.18 * network_access +
      0.20 * family_wealth_buffer,
    mobility_openness_score = (1 - persistence_b) * 0.55 + opportunity_score * 0.45
  )

labor_results <- labor |>
  mutate(
    wage_dispersion_ratio = top_wage / bottom_wage,
    labor_security_score =
      0.22 * bargaining_power +
      0.20 * union_strength +
      0.20 * employment_security +
      0.18 * schedule_stability +
      0.20 * benefit_access
  )

place_results <- place |>
  mutate(
    housing_cost_burden = housing_cost / median_income,
    place_opportunity_score =
      0.20 * school_quality +
      0.18 * transit_access +
      0.18 * environmental_quality +
      0.20 * job_access +
      0.14 * homeownership_rate +
      0.10 * (1 - housing_cost_burden / max(housing_cost_burden))
  )

write_csv(income_results, file.path(table_dir, "inequality_mobility_r_income_results.csv"))
write_csv(mobility_results, file.path(table_dir, "inequality_mobility_r_mobility_results.csv"))
write_csv(labor_results, file.path(table_dir, "inequality_mobility_r_labor_results.csv"))
write_csv(place_results, file.path(table_dir, "inequality_mobility_r_place_results.csv"))

p <- ggplot(income_results, aes(x = group)) +
  geom_line(aes(y = market_income, group = 1), linewidth = 1) +
  geom_line(aes(y = disposable_income, group = 1), linewidth = 1) +
  geom_line(aes(y = service_adjusted_income, group = 1), linewidth = 1) +
  labs(
    title = "Market, Disposable, and Service-Adjusted Income",
    subtitle = "Redistribution includes taxes, transfers, and the effective value of public services.",
    x = NULL,
    y = "Income units"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "inequality_mobility_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(income_results)
print(mobility_results)
print(labor_results)
print(place_results)
