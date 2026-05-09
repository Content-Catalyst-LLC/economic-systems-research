# Production, Distribution, and Exchange in Human Societies
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

results <- read_csv(file.path(processed_dir, "production_distribution_exchange_results.csv"), show_col_types = FALSE)

summary <- results |>
  group_by(scenario) |>
  summarise(
    total_output = sum(total_output),
    total_labor_income = sum(labor_income),
    total_non_labor_income = sum(non_labor_income),
    labor_share = total_labor_income / total_output,
    non_labor_share = total_non_labor_income / total_output,
    ecological_throughput = sum(ecological_throughput),
    exchange_dependency = sum(exchange_dependency),
    .groups = "drop"
  )

write_csv(summary, file.path(table_dir, "production_distribution_exchange_r_results.csv"))

plot_data <- summary |>
  select(scenario, labor_share, non_labor_share) |>
  pivot_longer(cols = c(labor_share, non_labor_share), names_to = "income_claim", values_to = "share")

distribution_plot <- ggplot(plot_data, aes(x = scenario, y = share, fill = income_claim)) +
  geom_col(position = "dodge") +
  labs(
    title = "Distribution of Income Claims Across Exchange Scenarios",
    subtitle = "Production changes alter labor and non-labor income shares across the system.",
    x = NULL,
    y = "Share of total output"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "production_distribution_exchange_r.png"),
  plot = distribution_plot,
  width = 9,
  height = 5,
  dpi = 300
)

print(summary)
