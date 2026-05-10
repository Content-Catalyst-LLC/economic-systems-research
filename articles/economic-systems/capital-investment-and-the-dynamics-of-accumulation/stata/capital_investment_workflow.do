* Capital, Investment, and the Dynamics of Accumulation
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/capital_intensity_results_python.csv"
local npv_file "`base_dir'/outputs/tables/npv_project_results_python.csv"
local output_table "`base_dir'/outputs/tables/capital_stata_results.csv"
local npv_output "`base_dir'/outputs/tables/capital_stata_npv_results.csv"
local log_file "`base_dir'/outputs/tables/stata_capital_investment_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable final_capital_stock "Final capital stock"
label variable final_capital_intensity "Final capital intensity"
label variable average_investment_rate "Average investment rate"

summarize final_capital_stock final_capital_intensity average_investment_rate

export delimited using "`output_table'", replace

capture confirm file "`npv_file'"
if !_rc {
    import delimited "`npv_file'", clear varnames(1)
    summarize npv_private npv_public public_private_npv_gap
    export delimited using "`npv_output'", replace
}

log close
