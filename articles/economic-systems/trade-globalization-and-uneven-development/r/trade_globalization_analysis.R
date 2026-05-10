# Trade, Globalization, and Uneven Development
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

trade <- read_csv(file.path(processed_dir, "trade_position_scenarios.csv"), show_col_types = FALSE)
basket <- read_csv(file.path(processed_dir, "export_basket_scenarios.csv"), show_col_types = FALSE)
value_chain <- read_csv(file.path(processed_dir, "value_chain_scenarios.csv"), show_col_types = FALSE)
regions <- read_csv(file.path(processed_dir, "regional_inequality_scenarios.csv"), show_col_types = FALSE)

trade_results <- trade |>
  mutate(
    trade_openness = (exports + imports) / output,
    trade_balance = exports - imports,
    import_dependence_score =
      0.40 * strategic_import_dependence +
      0.30 * intermediate_import_share +
      0.30 * energy_import_share
  )

export_results <- basket |>
  group_by(scenario) |>
  mutate(
    total_exports = sum(export_value),
    export_share = export_value / total_exports
  ) |>
  summarise(
    export_concentration_index = sum(export_share^2),
    diversification_score = 1 - export_concentration_index,
    .groups = "drop"
  )

value_chain_results <- value_chain |>
  mutate(
    domestic_value_capture = domestic_value_added / gross_exports,
    command_position_score =
      0.24 * domestic_value_capture +
      0.20 * lead_firm_control +
      0.20 * technology_control +
      0.16 * branding_control +
      0.12 * (1 - assembly_dependence) +
      0.08 * upgrading_potential
  )

regional_results <- regions |>
  mutate(
    globalization_advantage_score =
      0.20 * export_linkage +
      0.20 * productivity +
      0.18 * infrastructure_depth +
      0.16 * capital_access +
      0.14 * market_access +
      0.12 * institutional_capacity
  )

write_csv(trade_results, file.path(table_dir, "trade_globalization_r_results.csv"))
write_csv(export_results, file.path(table_dir, "trade_globalization_r_export_results.csv"))
write_csv(value_chain_results, file.path(table_dir, "trade_globalization_r_value_chain_results.csv"))
write_csv(regional_results, file.path(table_dir, "trade_globalization_r_regional_results.csv"))

p <- ggplot(value_chain_results, aes(x = scenario, y = domestic_value_capture)) +
  geom_col() +
  labs(
    title = "Domestic Value Capture in Global Trade",
    subtitle = "Gross exports can conceal very different levels of domestic income and control.",
    x = NULL,
    y = "Domestic value added / gross exports"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "trade_globalization_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(trade_results)
print(export_results)
print(value_chain_results)
print(regional_results)
