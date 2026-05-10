# Commons, Shared Resources, and Institutional Governance
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

resources <- read_csv(file.path(processed_dir, "resource_scenarios.csv"), show_col_types = FALSE)
users <- read_csv(file.path(processed_dir, "user_extraction_profiles.csv"), show_col_types = FALSE)
governance <- read_csv(file.path(processed_dir, "governance_scenarios.csv"), show_col_types = FALSE)

fishery <- resources |>
  filter(resource == "fishery") |>
  slice(1)

regen <- function(S, r, K) {
  r * S * (1 - S / K)
}

simulate <- function(gov_row, periods = 40) {
  stock <- numeric(periods + 1)
  stock[1] <- fishery$initial_stock

  baseline_harvest <- sum(users$baseline_extraction)
  governed_harvest <- sum(users$governed_extraction)

  harvest <- ifelse(
    gov_row$scenario %in% c("open_access_weak_governance", "captured_governance"),
    baseline_harvest * gov_row$extraction_multiplier,
    governed_harvest * gov_row$extraction_multiplier
  )

  for (t in 1:periods) {
    stock[t + 1] <- max(
      0,
      stock[t] + regen(stock[t], fishery$regeneration_rate, fishery$carrying_capacity) - harvest
    )
  }

  data.frame(
    governance_scenario = gov_row$scenario,
    period = 0:periods,
    stock = stock,
    harvest = harvest
  )
}

paths <- bind_rows(lapply(seq_len(nrow(governance)), function(i) simulate(governance[i, ])))

compliance <- governance |>
  mutate(
    compliance_score =
      0.28 * monitoring_capacity +
      0.22 * rule_clarity +
      0.25 * legitimacy +
      0.15 * sanction_capacity +
      0.10 * (1 - capture_risk),
    adaptive_governance_score =
      0.35 * local_knowledge_use +
      0.35 * polycentric_coordination +
      0.20 * legitimacy +
      0.10 * monitoring_capacity
  )

summary <- paths |>
  group_by(governance_scenario) |>
  summarise(
    final_stock = last(stock),
    minimum_stock = min(stock),
    average_harvest = mean(harvest),
    .groups = "drop"
  ) |>
  left_join(compliance |> select(scenario, compliance_score, adaptive_governance_score),
            by = c("governance_scenario" = "scenario"))

write_csv(summary, file.path(table_dir, "commons_r_results.csv"))
write_csv(paths, file.path(table_dir, "commons_r_stock_paths.csv"))

p <- ggplot(paths, aes(x = period, y = stock, color = governance_scenario)) +
  geom_line() +
  labs(
    title = "Commons Stock Paths Under Governance Scenarios",
    subtitle = "Resource trajectories depend on extraction pressure, monitoring, legitimacy, and institutional design.",
    x = "Period",
    y = "Resource stock"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figure_dir, "commons_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(summary)
