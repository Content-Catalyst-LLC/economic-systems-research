* Information, Uncertainty, and Imperfect Markets
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/robustness_results_python.csv"
local consumer_file "`base_dir'/outputs/tables/consumer_opacity_results_python.csv"
local output_table "`base_dir'/outputs/tables/information_uncertainty_stata_results.csv"
local consumer_output "`base_dir'/outputs/tables/information_uncertainty_stata_consumers.csv"
local log_file "`base_dir'/outputs/tables/stata_information_uncertainty_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable expected_equal_weight_payoff "Expected payoff using equal scenario weights"
label variable worst_case "Worst-case payoff"
label variable payoff_range "Scenario payoff range"
label variable robustness_rank "Worst-case robustness rank"

summarize expected_equal_weight_payoff worst_case payoff_range robustness_rank

export delimited using "`output_table'", replace

capture confirm file "`consumer_file'"
if !_rc {
    import delimited "`consumer_file'", clear varnames(1)
    summarize complexity_index hidden_fee_index switching_cost_index trust_index disclosure_quality effective_intelligibility opacity_risk
    export delimited using "`consumer_output'", replace
}

log close
