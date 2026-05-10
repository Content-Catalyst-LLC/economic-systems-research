* Economic Systems Within Planetary Boundaries
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/boundary_pressure_results_python.csv"
local resource_file "`base_dir'/outputs/tables/resource_use_identity_results_python.csv"
local output_table "`base_dir'/outputs/tables/planetary_boundaries_stata_boundary_results.csv"
local resource_output "`base_dir'/outputs/tables/planetary_boundaries_stata_resource_results.csv"
local log_file "`base_dir'/outputs/tables/stata_planetary_boundaries_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable boundary_pressure_ratio "Economic pressure divided by Earth-system capacity"
label variable overshoot_gap "Boundary pressure ratio minus one, bottom-coded at zero"
label variable boundary_priority_score "Composite boundary priority score"

summarize boundary_pressure_ratio overshoot_gap boundary_priority_score irreversibility system_connectivity

export delimited using "`output_table'", replace

capture confirm file "`resource_file'"
if !_rc {
    import delimited "`resource_file'", clear varnames(1)
    summarize resource_use resource_wellbeing_efficiency just_resource_performance
    export delimited using "`resource_output'", replace
}

log close
