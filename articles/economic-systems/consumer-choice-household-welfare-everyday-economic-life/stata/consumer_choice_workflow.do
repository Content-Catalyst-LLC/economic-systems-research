* Consumer Choice, Household Welfare, and Everyday Economic Life
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/household_budget_results_python.csv"
local output_table "`base_dir'/outputs/tables/consumer_choice_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_consumer_choice_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable total_consumption "Total consumption"
label variable essentials_spending "Essentials spending"
label variable saving "Household saving"
label variable essentials_ratio "Essentials ratio"
label variable fragility_ratio "Fragility ratio"
label variable effective_access "Effective access to essentials"

summarize total_consumption essentials_spending saving essentials_ratio fragility_ratio effective_access

collapse (mean) total_consumption essentials_spending saving essentials_ratio fragility_ratio effective_access ///
         (sum) negative_saving_flag high_fragility_flag, by(scenario)

export delimited using "`output_table'", replace

log close
