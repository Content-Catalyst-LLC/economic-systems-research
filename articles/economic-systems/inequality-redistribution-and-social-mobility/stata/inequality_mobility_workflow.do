* Inequality, Redistribution, and Social Mobility
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/income_redistribution_results_python.csv"
local mobility_file "`base_dir'/outputs/tables/mobility_results_python.csv"
local output_table "`base_dir'/outputs/tables/inequality_mobility_stata_income_results.csv"
local mobility_output "`base_dir'/outputs/tables/inequality_mobility_stata_mobility_results.csv"
local log_file "`base_dir'/outputs/tables/stata_inequality_mobility_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable market_income "Market income"
label variable disposable_income "Disposable income"
label variable service_adjusted_income "Service-adjusted income"
label variable housing_adjusted_income "Housing-adjusted income"
label variable housing_cost_burden "Housing cost burden"

summarize market_income disposable_income service_adjusted_income housing_adjusted_income housing_cost_burden

export delimited using "`output_table'", replace

capture confirm file "`mobility_file'"
if !_rc {
    import delimited "`mobility_file'", clear varnames(1)
    summarize persistence_b predicted_child_outcome opportunity_score mobility_openness_score
    export delimited using "`mobility_output'", replace
}

log close
