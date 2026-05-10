# Industrial Policy and the Developmental State
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

sectors <- read_csv(file.path(processed_dir, "strategic_sector_scenarios.csv"), show_col_types = FALSE)
support <- read_csv(file.path(processed_dir, "support_conditionality_scenarios.csv"), show_col_types = FALSE)
finance <- read_csv(file.path(processed_dir, "development_finance_scenarios.csv"), show_col_types = FALSE)
green <- read_csv(file.path(processed_dir, "green_industrial_policy_scenarios.csv"), show_col_types = FALSE)

sector_results <- sectors |>
  mutate(
    sector_output_share = sector_output / total_output,
    sector_productivity = sector_output / sector_labor,
    export_ratio = sector_exports / sector_output,
    strategic_priority_score =
      0.22 * sector_output_share / max(sector_output_share) +
      0.22 * export_ratio +
      0.22 * technology_depth +
      0.18 * learning_potential +
      0.16 * domestic_linkage_potential
  )

support_results <- support |>
  left_join(sector_results |> select(sector, sector_output), by = "sector") |>
  mutate(
    support_intensity = public_support / sector_output,
    performance_score =
      0.22 * productivity_gain / max(productivity_gain) +
      0.18 * export_growth / max(export_growth) +
      0.18 * employment_gain / max(employment_gain) +
      0.18 * local_supplier_share +
      0.16 * emissions_reduction / max(emissions_reduction) +
      0.08 * (1 - support_duration_years / max(support_duration_years))
  )

finance_results <- finance |>
  mutate(
    development_finance_alignment_score =
      0.26 * patient_credit_share +
      0.24 * industrial_credit_share +
      0.20 * (1 - speculative_credit_share) +
      0.12 * (1 - fx_debt_exposure) +
      0.10 * development_bank_capacity +
      0.08 * credit_monitoring_quality
  )

green_results <- green |>
  mutate(
    green_industrial_score =
      0.18 * productivity_gain / max(productivity_gain) +
      0.22 * emissions_reduction / max(emissions_reduction) +
      0.18 * domestic_linkage +
      0.16 * employment_quality +
      0.18 * resilience_value +
      0.08 * (1 - material_risk)
  )

write_csv(sector_results, file.path(table_dir, "industrial_policy_r_results.csv"))
write_csv(support_results, file.path(table_dir, "industrial_policy_r_support_results.csv"))
write_csv(finance_results, file.path(table_dir, "industrial_policy_r_finance_results.csv"))
write_csv(green_results, file.path(table_dir, "industrial_policy_r_green_results.csv"))

p <- ggplot(sector_results, aes(x = sector, y = strategic_priority_score)) +
  geom_col() +
  labs(
    title = "Strategic Sector Priority Scores",
    subtitle = "Sectoral priority combines scale, exports, technology depth, learning potential, and domestic linkage.",
    x = NULL,
    y = "Composite score"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "industrial_policy_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(sector_results)
print(support_results)
print(finance_results)
print(green_results)
