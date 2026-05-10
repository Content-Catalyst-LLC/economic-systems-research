* Macroeconomic Stability, Business Cycles, and Crisis
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/aggregate_demand_results_python.csv"
local household_file "`base_dir'/outputs/tables/household_balance_sheet_results_python.csv"
local output_table "`base_dir'/outputs/tables/macro_stability_stata_results.csv"
local household_output "`base_dir'/outputs/tables/macro_stability_stata_household_results.csv"
local log_file "`base_dir'/outputs/tables/stata_macro_stability_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable output "Aggregate output"
label variable potential_output "Potential output"
label variable output_gap "Output gap"
label variable consumption_share "Consumption share"
label variable investment_share "Investment share"
label variable government_share "Government spending share"

summarize output potential_output output_gap consumption_share investment_share government_share

export delimited using "`output_table'", replace

capture confirm file "`household_file'"
if !_rc {
    import delimited "`household_file'", clear varnames(1)
    summarize debt_burden_ratio savings_buffer_months post_shock_debt_burden_ratio household_macro_fragility_score
    export delimited using "`household_output'", replace
}

log close
