# Information, Uncertainty, and Imperfect Markets
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

signals <- read_csv(file.path(processed_dir, "signaling_scenarios.csv"), show_col_types = FALSE)
search <- read_csv(file.path(processed_dir, "information_search_scenarios.csv"), show_col_types = FALSE)
uncertainty <- read_csv(file.path(processed_dir, "uncertainty_scenarios.csv"), show_col_types = FALSE)
consumers <- read_csv(file.path(processed_dir, "consumer_complexity_scenarios.csv"), show_col_types = FALSE)

signals <- signals |>
  mutate(
    credibility_gap = signal_cost_low_type - signal_cost_high_type,
    credible_signal_score =
      0.45 * verification_strength +
      0.35 * (credibility_gap / max(credibility_gap)) +
      0.20 * signal_strength
  )

search <- search |>
  mutate(
    total_information_cost = cost_information + time_cost + processing_cost,
    net_information_value = benefit_information - total_information_cost
  )

uncertainty <- uncertainty |>
  rowwise() |>
  mutate(
    expected_equal_weight_payoff = mean(c(good_case, moderate_case, bad_case, transition_case, systemic_crisis_case)),
    worst_case = min(c(good_case, moderate_case, bad_case, transition_case, systemic_crisis_case)),
    payoff_range = max(c(good_case, moderate_case, bad_case, transition_case, systemic_crisis_case)) -
      min(c(good_case, moderate_case, bad_case, transition_case, systemic_crisis_case))
  ) |>
  ungroup()

consumers <- consumers |>
  mutate(
    effective_intelligibility =
      0.35 * disclosure_quality +
      0.25 * trust_index +
      0.20 * (1 - complexity_index) +
      0.12 * (1 - hidden_fee_index) +
      0.08 * (1 - switching_cost_index),
    opacity_risk = 1 - effective_intelligibility
  )

write_csv(signals, file.path(table_dir, "information_uncertainty_r_signals.csv"))
write_csv(search, file.path(table_dir, "information_uncertainty_r_search.csv"))
write_csv(uncertainty, file.path(table_dir, "information_uncertainty_r_results.csv"))
write_csv(consumers, file.path(table_dir, "information_uncertainty_r_consumers.csv"))

p <- ggplot(search, aes(x = information_level)) +
  geom_line(aes(y = benefit_information)) +
  geom_line(aes(y = total_information_cost)) +
  geom_line(aes(y = net_information_value)) +
  labs(
    title = "Information Search Benefit, Cost, and Net Value",
    subtitle = "More information can improve decisions, but search and processing costs eventually dominate.",
    x = "Information level",
    y = "Value"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figure_dir, "information_uncertainty_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(signals)
print(search)
print(uncertainty)
print(consumers)
