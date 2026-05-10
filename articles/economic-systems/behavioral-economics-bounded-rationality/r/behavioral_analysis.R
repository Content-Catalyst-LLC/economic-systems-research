# Behavioral Economics and Bounded Rationality
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

choice <- read_csv(file.path(processed_dir, "choice_options.csv"), show_col_types = FALSE)
present <- read_csv(file.path(processed_dir, "present_bias_scenarios.csv"), show_col_types = FALSE)
framing <- read_csv(file.path(processed_dir, "framing_default_scenarios.csv"), show_col_types = FALSE)

kappa <- 5

choice_results <- choice |>
  mutate(effective_utility = utility - kappa * complexity + 10 * salience)

present_results <- present |>
  filter(period > 0) |>
  group_by(scenario, beta, delta) |>
  summarise(
    present_biased_value = sum(beta * (delta^period) * future_value),
    exponential_discount_value = sum((delta^period) * future_value),
    present_bias_gap = exponential_discount_value - present_biased_value,
    .groups = "drop"
  )

logistic <- function(z) 1 / (1 + exp(-z))

framing_results <- framing |>
  mutate(
    frame_effect = case_when(
      frame == "gain" ~ 0.18,
      frame == "loss" ~ 0.28,
      TRUE ~ 0.00
    ),
    take_up_probability = logistic(
      -1.6 +
        0.020 * benefit_value -
        0.025 * admin_burden +
        1.15 * default_status +
        1.10 * trust_index +
        0.85 * salience +
        frame_effect
    )
  )

write_csv(choice_results, file.path(table_dir, "behavioral_r_results.csv"))
write_csv(present_results, file.path(table_dir, "behavioral_r_present_bias.csv"))
write_csv(framing_results, file.path(table_dir, "behavioral_r_default_take_up.csv"))

plot_data <- framing_results |>
  select(scenario, take_up_probability)

p <- ggplot(plot_data, aes(x = scenario, y = take_up_probability)) +
  geom_col() +
  labs(
    title = "Framing, Defaults, Burden, and Take-Up",
    subtitle = "Behavior changes when institutions alter salience, defaults, complexity, and trust.",
    x = NULL,
    y = "Modeled take-up probability"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "behavioral_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(choice_results)
print(present_results)
print(framing_results)
