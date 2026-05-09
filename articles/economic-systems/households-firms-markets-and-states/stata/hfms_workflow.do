* Households, Firms, Markets, and States
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/institutional_flow_results_python.csv"
local output_table "`base_dir'/outputs/tables/hfms_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_hfms_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable household_saving "Household saving"
label variable firm_profit "Firm profit"
label variable public_borrowing "Public borrowing"
label variable reproduction_score "System reproduction score"

summarize household_saving firm_profit public_borrowing reproduction_score wage_share_of_firm_revenue transfer_support_ratio

export delimited using "`output_table'", replace

log close
