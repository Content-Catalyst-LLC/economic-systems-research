* Economic Resilience, Fragility, and Adaptive Capacity
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/resilience_results_python.csv"
local fragility_file "`base_dir'/outputs/tables/fragility_results_python.csv"
local output_table "`base_dir'/outputs/tables/economic_resilience_stata_resilience_results.csv"
local fragility_output "`base_dir'/outputs/tables/economic_resilience_stata_fragility_results.csv"
local log_file "`base_dir'/outputs/tables/stata_economic_resilience_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable resilience_score "Composite economic resilience score"

summarize resilience_score buffers redundancy coordination trust learning recovery_capacity

export delimited using "`output_table'", replace

capture confirm file "`fragility_file'"
if !_rc {
    import delimited "`fragility_file'", clear varnames(1)
    summarize fragility_score leverage concentration exposure underinvestment inequality political_fragmentation
    export delimited using "`fragility_output'", replace
}

log close
