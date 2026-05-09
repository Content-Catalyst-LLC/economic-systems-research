* What Is an Economic System? Stata Workflow
*
* Purpose:
* Applied economics replication workflow for system-level sector, distribution,
* and input-output results.
*
* Assumes Python workflow has already created:
* data/processed/economic_system_results.csv

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/data/processed/economic_system_results.csv"
local output_table "`base_dir'/outputs/tables/economic_system_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_economic_system_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable final_demand "Final demand"
label variable total_output "Total output required"
label variable indirect_output_requirement "Indirect output requirement"
label variable output_multiplier "Output multiplier"
label variable output_change_from_baseline "Output change from baseline"

summarize final_demand total_output indirect_output_requirement output_multiplier output_change_from_baseline

collapse (sum) final_demand total_output indirect_output_requirement output_change_from_baseline (mean) output_multiplier, by(scenario)

export delimited using "`output_table'", replace

log close
