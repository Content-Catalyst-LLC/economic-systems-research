* Natural Capital, Resource Use, and Environmental Constraint
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/stock_flow_results_python.csv"
local resource_file "`base_dir'/outputs/tables/resource_use_constraint_results_python.csv"
local output_table "`base_dir'/outputs/tables/natural_capital_stata_stock_results.csv"
local resource_output "`base_dir'/outputs/tables/natural_capital_stata_resource_results.csv"
local log_file "`base_dir'/outputs/tables/stata_natural_capital_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable natural_capital_next "Next-period natural-capital stock"
label variable regeneration_gap "Degradation minus regeneration"
label variable threshold_distance "Distance from ecological threshold"
label variable stock_risk_score "Composite stock risk score"

summarize natural_capital_next regeneration_gap threshold_distance stock_risk_score

export delimited using "`output_table'", replace

capture confirm file "`resource_file'"
if !_rc {
    import delimited "`resource_file'", clear varnames(1)
    summarize resource_use_ratio waste_constraint_ratio resource_constraint_score
    export delimited using "`resource_output'", replace
}

log close
