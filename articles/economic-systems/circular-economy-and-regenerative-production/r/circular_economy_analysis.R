# Circular Economy and Regenerative Production
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

material <- read_csv(file.path(processed_dir, "material_flow_scenarios.csv"), show_col_types = FALSE)
design <- read_csv(file.path(processed_dir, "product_life_design.csv"), show_col_types = FALSE)
pathways <- read_csv(file.path(processed_dir, "value_retention_pathways.csv"), show_col_types = FALSE)
regeneration <- read_csv(file.path(processed_dir, "regenerative_production.csv"), show_col_types = FALSE)

material_results <- material |>
  mutate(
    circularity_ratio = recovered_material / total_material_input,
    virgin_material_input = total_material_input - recovered_material,
    waste_reduction_ratio = 1 - (residual_waste / total_throughput)
  )

design_results <- design |>
  mutate(
    product_life_extension = actual_product_life / baseline_product_life,
    design_for_circularity_score =
      0.18 * durability +
      0.18 * repairability +
      0.16 * modularity +
      0.16 * disassembly_score +
      0.14 * material_separability +
      0.10 * (1 - proprietary_lock_in) +
      0.08 * product_life_extension / max(product_life_extension)
  )

pathway_results <- pathways |>
  mutate(
    value_retention_score =
      0.22 * material_retention +
      0.18 * energy_retention +
      0.18 * labor_value_retention +
      0.20 * functional_retention +
      0.10 * (1 - processing_intensity) +
      0.12 * (1 - quality_loss)
  )

regeneration_results <- regeneration |>
  mutate(
    regenerative_balance = ecological_restoration - ecological_degradation,
    regenerative_production_score =
      0.20 * ((regenerative_balance - min(regenerative_balance)) / (max(regenerative_balance) - min(regenerative_balance))) +
      0.16 * soil_health +
      0.16 * water_retention +
      0.16 * biodiversity +
      0.16 * local_capability +
      0.16 * stewardship_labor
  )

write_csv(material_results, file.path(table_dir, "circular_economy_r_material_results.csv"))
write_csv(design_results, file.path(table_dir, "circular_economy_r_design_results.csv"))
write_csv(pathway_results, file.path(table_dir, "circular_economy_r_pathway_results.csv"))
write_csv(regeneration_results, file.path(table_dir, "circular_economy_r_regeneration_results.csv"))

p <- ggplot(material_results, aes(x = scenario, y = circularity_ratio)) +
  geom_col() +
  labs(
    title = "Circularity Ratio",
    subtitle = "Recovered material divided by total material input.",
    x = NULL,
    y = "Recovered material / total material input"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "circular_economy_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(material_results)
print(design_results)
print(pathway_results)
print(regeneration_results)
