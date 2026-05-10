* Monetary Policy, Central Banking, and Financial Conditions
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/policy_rate_results_python.csv"
local debt_file "`base_dir'/outputs/tables/debt_service_results_python.csv"
local output_table "`base_dir'/outputs/tables/monetary_policy_stata_results.csv"
local debt_output "`base_dir'/outputs/tables/monetary_policy_stata_debt_results.csv"
local log_file "`base_dir'/outputs/tables/stata_monetary_policy_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable nominal_rate "Nominal interest rate"
label variable expected_inflation "Expected inflation"
label variable real_rate "Real interest rate"
label variable policy_rate_rule "Stylized policy-rule rate"
label variable stance_gap "Actual minus rule-implied stance"

summarize nominal_rate expected_inflation real_rate policy_rate_rule stance_gap

export delimited using "`output_table'", replace

capture confirm file "`debt_file'"
if !_rc {
    import delimited "`debt_file'", clear varnames(1)
    summarize debt_service_ratio post_shock_dsr monetary_exposure_score repricing_share
    export delimited using "`debt_output'", replace
}

log close
