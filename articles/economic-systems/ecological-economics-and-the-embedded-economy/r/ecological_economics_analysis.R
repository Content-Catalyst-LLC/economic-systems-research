# Ecological Economics and the Embedded Economy
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

throughput <- read_csv(file.path(processed_dir, "throughput_scenarios.csv"), show_col_types = FALSE)
sectors <- read_csv(file.path(processed_dir, "sector_footprints.csv"), show_col_types = FALSE)
embedded <- read_csv(file.path(processed_dir, "embeddedness_scenarios.csv"), show_col_types = FALSE)
resilience <- read_csv(file.path(processed_dir, "resilience_commons.csv"), show_col_types = FALSE)

throughput_results <- throughput |>
  mutate(
    throughput = energy_input + material_input,
    waste_residual = throughput - recovered_throughput,
    recovery_rate = recovered_throughput / throughput,
    scale_ratio = economic_scale / ecological_capacity
  )

sector_results <- sectors |>
  mutate(
    material_footprint = domestic_extraction + imports - exports,
    ecological_pressure_score =
      0.20 * material_footprint / max(material_footprint) +
      0.18 * energy_intensity +
      0.18 * water_pressure +
      0.18 * land_pressure +
      0.16 * waste_intensity +
      0.10 * social_necessity
  )

embedded_results <- embedded |>
  mutate(
    embeddedness_score =
      0.18 * ecology_integrity +
      0.18 * care_capacity +
      0.16 * public_institutions +
      0.14 * infrastructure_maintenance +
      0.14 * cultural_reciprocity +
      0.10 * (1 - market_dependence) +
      0.10 * community_resilience
  )

resilience_results <- resilience |>
  mutate(
    resilience_score =
      0.16 * diversity +
      0.14 * redundancy +
      0.16 * regeneration +
      0.16 * governance +
      0.12 * maintenance +
      0.12 * learning +
      0.08 * monitoring +
      0.06 * participation
  )

write_csv(throughput_results, file.path(table_dir, "ecological_economics_r_throughput_results.csv"))
write_csv(sector_results, file.path(table_dir, "ecological_economics_r_sector_results.csv"))
write_csv(embedded_results, file.path(table_dir, "ecological_economics_r_embeddedness_results.csv"))
write_csv(resilience_results, file.path(table_dir, "ecological_economics_r_resilience_results.csv"))

p <- ggplot(throughput_results, aes(x = scenario, y = scale_ratio)) +
  geom_col() +
  labs(
    title = "Ecological Scale Ratio",
    subtitle = "Scale is measured as economic scale relative to ecological capacity.",
    x = NULL,
    y = "Economic scale / ecological capacity"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "ecological_economics_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(throughput_results)
print(sector_results)
print(embedded_results)
print(resilience_results)
