* Industrial Policy and the Developmental State
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/strategic_sector_results_python.csv"
local support_file "`base_dir'/outputs/tables/support_conditionality_results_python.csv"
local output_table "`base_dir'/outputs/tables/industrial_policy_stata_results.csv"
local support_output "`base_dir'/outputs/tables/industrial_policy_stata_support_results.csv"
local log_file "`base_dir'/outputs/tables/stata_industrial_policy_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable sector_output_share "Sector output share"
label variable sector_productivity "Sector productivity"
label variable export_ratio "Export ratio"
label variable strategic_priority_score "Strategic priority score"

summarize sector_output_share sector_productivity export_ratio strategic_priority_score

export delimited using "`output_table'", replace

capture confirm file "`support_file'"
if !_rc {
    import delimited "`support_file'", clear varnames(1)
    summarize support_intensity productivity_gain export_growth performance_score conditionality_gap withdrawal_flag
    export delimited using "`support_output'", replace
}

log close
