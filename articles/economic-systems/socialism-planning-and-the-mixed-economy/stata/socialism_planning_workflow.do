* Socialism, Planning, and the Mixed Economy
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/mixed_economy_results_python.csv"
local planning_file "`base_dir'/outputs/tables/planning_capacity_results_python.csv"
local output_table "`base_dir'/outputs/tables/socialism_planning_stata_mixed_results.csv"
local planning_output "`base_dir'/outputs/tables/socialism_planning_stata_planning_results.csv"
local log_file "`base_dir'/outputs/tables/stata_socialism_planning_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable market_allocation "Market allocation intensity"
label variable public_planning "Public planning intensity"
label variable public_provision "Public provision intensity"
label variable regulation_rights "Regulation and social rights intensity"
label variable public_purpose_score "Public purpose score"
label variable profit_dominance_score "Profit dominance score"

summarize market_allocation public_planning public_provision regulation_rights public_purpose_score profit_dominance_score

export delimited using "`output_table'", replace

capture confirm file "`planning_file'"
if !_rc {
    import delimited "`planning_file'", clear varnames(1)
    summarize state_capacity data_quality institutional_reach feedback_quality democratic_accountability planning_capacity_score
    export delimited using "`planning_output'", replace
}

log close
