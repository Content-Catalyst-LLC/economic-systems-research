* The Welfare State and Social Protection
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/household_tax_transfer_results_python.csv"
local coverage_file "`base_dir'/outputs/tables/program_coverage_results_python.csv"
local output_table "`base_dir'/outputs/tables/welfare_state_stata_household_results.csv"
local coverage_output "`base_dir'/outputs/tables/welfare_state_stata_coverage_results.csv"
local log_file "`base_dir'/outputs/tables/stata_welfare_state_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable market_income "Market income"
label variable disposable_income "Disposable income after taxes and transfers"
label variable service_adjusted_income "Disposable income plus public service value"
label variable post_cost_security_income "Income after housing and care costs"

summarize market_income disposable_income service_adjusted_income post_cost_security_income redistributive_gain

export delimited using "`output_table'", replace

capture confirm file "`coverage_file'"
if !_rc {
    import delimited "`coverage_file'", clear varnames(1)
    summarize coverage_rate replacement_rate take_up_rate effective_protection_score
    export delimited using "`coverage_output'", replace
}

log close
