# IS-LM R Workflow
#
# Purpose:
# Replicate the IS-LM scenario table and visualize policy effects.

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

scenario_path <- file.path(base_dir, "data", "processed", "is_lm_scenario_results.csv")
table_dir <- file.path(base_dir, "outputs", "tables")
figure_dir <- file.path(base_dir, "outputs", "figures")

dir.create(table_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

scenarios <- read_csv(scenario_path, show_col_types = FALSE)

summary_table <- scenarios |>
  group_by(lm_slope_type) |>
  summarise(
    scenarios = n(),
    avg_equilibrium_output = mean(equilibrium_output),
    avg_equilibrium_interest_rate = mean(equilibrium_interest_rate),
    avg_fiscal_multiplier = mean(fiscal_multiplier_model),
    avg_monetary_multiplier = mean(monetary_multiplier_model),
    avg_crowding_out_indicator = mean(crowding_out_indicator),
    .groups = "drop"
  )

write_csv(summary_table, file.path(table_dir, "is_lm_r_results.csv"))

scenario_plot <- ggplot(
  scenarios,
  aes(x = delta_interest_from_baseline, y = delta_output_from_baseline, label = scenario)
) +
  geom_point(size = 2.5) +
  geom_text(vjust = -0.6, size = 3) +
  geom_hline(yintercept = 0, linewidth = 0.3) +
  geom_vline(xintercept = 0, linewidth = 0.3) +
  labs(
    title = "IS-LM Policy Scenarios",
    subtitle = "Output and interest-rate changes relative to baseline equilibrium",
    x = "Interest-rate change from baseline",
    y = "Output change from baseline"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figure_dir, "is_lm_scenarios_r.png"),
  plot = scenario_plot,
  width = 9,
  height = 5,
  dpi = 300
)

print(summary_table)
