library(readr)
library(dplyr)
library(ggplot2)

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("--file=", "", file_arg[1]))
  base_dir <- normalizePath(file.path(dirname(script_path), ".."))
} else {
  base_dir <- normalizePath(file.path(getwd(), "articles/economic-systems/economic-resilience-recessions-recovery"))
}

data_path <- file.path(base_dir, "outputs", "economic_resilience_indicators.csv")
output_dir <- file.path(base_dir, "outputs")

df <- read_csv(data_path, show_col_types = FALSE) |>
  mutate(
    date = as.Date(date),
    recession = recession_indicator == 1
  )

summary_table <- df |>
  filter(!is.na(unemployment_rate)) |>
  group_by(recession) |>
  summarise(
    observations = n(),
    avg_unemployment = mean(unemployment_rate, na.rm = TRUE),
    avg_fed_funds_rate = mean(federal_funds_rate, na.rm = TRUE),
    avg_gdp_growth = mean(real_gdp_growth_annualized, na.rm = TRUE),
    .groups = "drop"
  )

write_csv(summary_table, file.path(output_dir, "recession_summary_table.csv"))

unemployment_plot <- ggplot(df, aes(x = date, y = unemployment_rate)) +
  geom_line(linewidth = 0.7) +
  labs(
    title = "Unemployment and Economic Resilience",
    subtitle = "Labor-market stress rises when demand, production, and confidence weaken.",
    x = NULL,
    y = "Unemployment rate (%)"
  ) +
  theme_minimal()

ggsave(
  filename = file.path(output_dir, "unemployment_resilience_plot.png"),
  plot = unemployment_plot,
  width = 9,
  height = 5,
  dpi = 300
)

print(summary_table)
