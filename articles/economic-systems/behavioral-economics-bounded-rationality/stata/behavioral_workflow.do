* Behavioral Economics and Bounded Rationality
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/default_take_up_results_python.csv"
local admin_file "`base_dir'/outputs/tables/admin_burden_results_python.csv"
local output_table "`base_dir'/outputs/tables/behavioral_stata_results.csv"
local admin_output "`base_dir'/outputs/tables/behavioral_stata_admin_burden.csv"
local log_file "`base_dir'/outputs/tables/stata_behavioral_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable take_up_probability "Modeled take-up probability"
label variable default_status "Default status"
label variable admin_burden "Administrative burden"
label variable trust_index "Trust index"

summarize take_up_probability default_status admin_burden trust_index salience

export delimited using "`output_table'", replace

capture confirm file "`admin_file'"
if !_rc {
    import delimited "`admin_file'", clear varnames(1)
    summarize take_up_probability expected_take_up non_take_up admin_burden default_support trust_index
    export delimited using "`admin_output'", replace
}

log close
