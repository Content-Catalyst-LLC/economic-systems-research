# Externalities, Public Goods, and Collective Provision
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

externalities <- read_csv(file.path(processed_dir, "externality_scenarios.csv"), show_col_types = FALSE)
public_goods <- read_csv(file.path(processed_dir, "public_good_scenarios.csv"), show_col_types = FALSE)
contributions <- read_csv(file.path(processed_dir, "contribution_scenarios.csv"), show_col_types = FALSE)

Q <- 1:120

schedule <- externalities |>
  tidyr::crossing(output = Q) |>
  mutate(
    MPC = mpc_intercept + mpc_slope * output,
    MEC = mec_intercept + mec_slope * output,
    MSC = MPC + MEC,
    MPB = mpb_intercept + mpb_slope * output,
    MEB = meb_intercept + meb_slope * output,
    MSB = MPB + MEB
  )

optimum <- schedule |>
  group_by(scenario) |>
  summarise(
    private_output = output[which.min(abs(MPB - MPC))],
    social_output = output[which.min(abs(MSB - MSC))],
    private_minus_social_output = private_output - social_output,
    .groups = "drop"
  )

pg_results <- public_goods |>
  mutate(
    social_benefit = private_benefit + external_benefit,
    underprovision_gap = social_need - voluntary_provision,
    social_return_ratio = social_benefit / private_cost
  )

contribution_summary <- contributions |>
  mutate(free_rider_flag = contribution <= 1 & benefit_share > 0) |>
  group_by(scenario) |>
  summarise(
    total_contribution = sum(contribution),
    free_rider_groups = sum(free_rider_flag),
    .groups = "drop"
  )

write_csv(optimum, file.path(table_dir, "externalities_public_goods_r_results.csv"))
write_csv(pg_results, file.path(table_dir, "externalities_public_goods_r_public_goods.csv"))
write_csv(contribution_summary, file.path(table_dir, "externalities_public_goods_r_contributions.csv"))

plot_data <- pg_results |>
  select(public_good, social_need, voluntary_provision) |>
  pivot_longer(cols = c(social_need, voluntary_provision), names_to = "provision_type", values_to = "value")

p <- ggplot(plot_data, aes(x = public_good, y = value, fill = provision_type)) +
  geom_col(position = "dodge") +
  labs(
    title = "Public Good Need and Voluntary Provision",
    subtitle = "Diffuse benefits and free-rider incentives can produce systematic underprovision.",
    x = NULL,
    y = "Provision index"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

ggsave(
  filename = file.path(figure_dir, "externalities_public_goods_r.png"),
  plot = p,
  width = 9,
  height = 5,
  dpi = 300
)

print(optimum)
print(pg_results)
print(contribution_summary)
