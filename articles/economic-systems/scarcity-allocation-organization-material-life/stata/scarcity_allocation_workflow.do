* Scarcity, Allocation, and the Organization of Material Life
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/allocation_results_python.csv"
local output_table "`base_dir'/outputs/tables/scarcity_allocation_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_scarcity_allocation_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable allocation_units "Resource units allocated"
label variable change_from_baseline "Change from baseline allocation"
label variable essentiality_weighted_allocation "Essentiality-weighted allocation"
label variable resilience_weighted_allocation "Resilience-weighted allocation"

summarize allocation_units change_from_baseline essentiality_weighted_allocation resilience_weighted_allocation

collapse (sum) allocation_units change_from_baseline essentiality_weighted_allocation resilience_weighted_allocation, by(scenario)

export delimited using "`output_table'", replace

log close
