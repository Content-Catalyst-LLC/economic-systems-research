* Poverty, Capability, and Economic Inclusion
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/household_poverty_results_python.csv"
local capability_file "`base_dir'/outputs/tables/capability_results_python.csv"
local output_table "`base_dir'/outputs/tables/poverty_capability_stata_household_results.csv"
local capability_output "`base_dir'/outputs/tables/poverty_capability_stata_capability_results.csv"
local log_file "`base_dir'/outputs/tables/stata_poverty_capability_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable poverty_status "Below poverty line"
label variable poverty_gap "Poverty gap"
label variable normalized_poverty_gap "Poverty gap divided by poverty line"
label variable post_cost_income "Income after housing, debt service, and health costs"
label variable vulnerability_score "Composite vulnerability score"

summarize income poverty_gap normalized_poverty_gap post_cost_income vulnerability_score

export delimited using "`output_table'", replace

capture confirm file "`capability_file'"
if !_rc {
    import delimited "`capability_file'", clear varnames(1)
    summarize capability_score conversion_condition_score real_freedom_proxy
    export delimited using "`capability_output'", replace
}

log close
