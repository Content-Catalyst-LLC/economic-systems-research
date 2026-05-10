# Climate Economics, Transition Policy, and Decarbonization
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

sectors <- read_csv(file.path(processed_dir, "sector_emissions.csv"), show_col_types = FALSE)
policies <- read_csv(file.path(processed_dir, "policy_packages.csv"), show_col_types = FALSE)
investment <- read_csv(file.path(processed_dir, "transition_investment.csv"), show_col_types = FALSE)
justice <- read_csv(file.path(processed_dir, "just_transition.csv"), show_col_types = FALSE)

sector_results <- sectors |>
  mutate(
    emissions = output * energy_intensity * carbon_intensity,
    decarbonization_rate = (old_emissions_intensity - new_emissions_intensity) / years
  )

policy_results <- policies |>
  mutate(
    policy_mix_score =
      0.18 * carbon_price_strength +
      0.20 * regulatory_strength +
      0.22 * public_investment +
      0.18 * industrial_policy +
      0.12 * social_protection +
      0.10 * implementation_capacity
  )

investment_results <- investment |>
  mutate(
    transition_investment_score =
      0.22 * public_investment +
      0.20 * private_capital +
      0.22 * policy_credibility +
      0.16 * cost_of_capital_support +
      0.10 * permitting_capacity +
      0.10 * grid_readiness
  )

justice_results <- justice |>
  mutate(
    just_transition_score =
      0.16 * (1 - worker_exposure) +
      0.16 * retraining +
      0.18 * regional_investment +
      0.14 * income_support +
      0.14 * public_services +
      0.12 * new_industry_pipeline +
      0.10 * labor_standards
  )

write_csv(sector_results, file.path(table_dir, "climate_economics_r_sector_results.csv"))
write_csv(policy_results, file.path(table_dir, "climate_economics_r_policy_results.csv"))
write_csv(investment_results, file.path(table_dir, "climate_economics_r_investment_results.csv"))
write_csv(justice_results, file.path(table_dir, "climate_economics_r_justice_results.csv"))

p <- ggplot(sector_results, aes(x = sector, y = emissions)) +
  geom_col() +
  labs(
    title = "Sector Emissions",
    subtitle = "Output multiplied by energy intensity and carbon intensity.",
    x = NULL,
    y = "Emissions index"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "climate_economics_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(sector_results)
print(policy_results)
print(investment_results)
print(justice_results)
