# Capitalism and Its Varieties
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

regimes <- read_csv(file.path(processed_dir, "regime_scenarios.csv"), show_col_types = FALSE)
finance <- read_csv(file.path(processed_dir, "financialization_scenarios.csv"), show_col_types = FALSE)
labor <- read_csv(file.path(processed_dir, "labor_skill_systems.csv"), show_col_types = FALSE)
crisis <- read_csv(file.path(processed_dir, "crisis_sustainability.csv"), show_col_types = FALSE)

regime_results <- regimes |>
  mutate(
    profit = revenue - cost,
    wage_share = wages / output,
    profit_share = profit / output,
    institutional_advantage_score =
      0.20 * finance_patience +
      0.20 * labor_coordination +
      0.18 * welfare_buffer +
      0.18 * state_coordination +
      0.12 * innovation_radical +
      0.12 * innovation_incremental
  )

finance_results <- finance |>
  mutate(
    financialization_score =
      0.20 * asset_price_intensity +
      0.18 * household_debt +
      0.18 * corporate_leverage +
      0.18 * shareholder_payout_pressure +
      0.14 * buyback_intensity +
      0.12 * speculative_pressure,
    productive_finance_score =
      0.44 * productive_investment +
      0.20 * (1 - speculative_pressure) +
      0.18 * (1 - shareholder_payout_pressure) +
      0.18 * (1 - asset_price_intensity)
  )

labor_results <- labor |>
  mutate(
    labor_coordination_score =
      0.18 * employment_protection +
      0.20 * collective_bargaining +
      0.16 * union_density +
      0.14 * vocational_training +
      0.14 * firm_specific_skills +
      0.10 * wage_compression +
      0.08 * general_skills
  )

crisis_results <- crisis |>
  mutate(
    crisis_response_score =
      0.18 * automatic_stabilizers +
      0.16 * public_investment_capacity +
      0.18 * household_buffer +
      0.14 * financial_regulation +
      0.14 * industrial_adaptation +
      0.10 * ecological_constraint +
      0.10 * democratic_legitimacy,
    sustainable_capitalism_score =
      0.18 * public_investment_capacity +
      0.16 * household_buffer +
      0.14 * financial_regulation +
      0.18 * industrial_adaptation +
      0.18 * ecological_constraint +
      0.16 * democratic_legitimacy
  )

write_csv(regime_results, file.path(table_dir, "capitalism_varieties_r_regime_results.csv"))
write_csv(finance_results, file.path(table_dir, "capitalism_varieties_r_finance_results.csv"))
write_csv(labor_results, file.path(table_dir, "capitalism_varieties_r_labor_results.csv"))
write_csv(crisis_results, file.path(table_dir, "capitalism_varieties_r_crisis_results.csv"))

p <- ggplot(regime_results, aes(x = regime, y = institutional_advantage_score)) +
  geom_col() +
  labs(
    title = "Comparative Institutional Advantage by Capitalist Regime",
    subtitle = "Institutional advantage combines finance, labor, welfare, state coordination, and innovation.",
    x = NULL,
    y = "Composite institutional score"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "capitalism_varieties_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(regime_results)
print(finance_results)
print(labor_results)
print(crisis_results)
