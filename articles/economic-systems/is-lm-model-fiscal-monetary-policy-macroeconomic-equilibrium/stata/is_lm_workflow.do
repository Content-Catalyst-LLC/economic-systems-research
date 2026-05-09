* IS-LM Stata Workflow
* Article: The IS-LM Model: Fiscal Policy, Monetary Policy, and Macroeconomic Equilibrium
*
* Purpose:
* Applied macroeconomics replication workflow for IS-LM policy scenarios.
*
* Assumes Python workflow has already created:
* data/processed/is_lm_scenario_results.csv

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/data/processed/is_lm_scenario_results.csv"
local output_table "`base_dir'/outputs/tables/is_lm_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_is_lm_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable equilibrium_output "IS-LM equilibrium output"
label variable equilibrium_interest_rate "IS-LM equilibrium interest rate"
label variable fiscal_multiplier_model "Model-implied fiscal multiplier"
label variable monetary_multiplier_model "Model-implied monetary multiplier"
label variable crowding_out_indicator "Positive interest-rate change from baseline"

summarize equilibrium_output equilibrium_interest_rate delta_output_from_baseline delta_interest_from_baseline fiscal_multiplier_model monetary_multiplier_model crowding_out_indicator

regress delta_output_from_baseline fiscal_shift money_shift beta gamma, vce(robust)

matrix b = e(b)
matrix V = e(V)

preserve
clear
set obs 5

gen term = ""
replace term = "_cons" in 1
replace term = "fiscal_shift" in 2
replace term = "money_shift" in 3
replace term = "beta" in 4
replace term = "gamma" in 5

gen estimate = .
replace estimate = b[1, "_cons"] in 1
replace estimate = b[1, "fiscal_shift"] in 2
replace estimate = b[1, "money_shift"] in 3
replace estimate = b[1, "beta"] in 4
replace estimate = b[1, "gamma"] in 5

gen robust_se = .
forvalues i = 1/5 {
    replace robust_se = sqrt(V[`i',`i']) in `i'
}

gen t_value = estimate / robust_se
export delimited using "`output_table'", replace
restore

log close
