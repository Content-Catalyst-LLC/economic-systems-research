* The Future of Economic Systems in an Age of Limits
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/future_viability_results_python.csv"
local throughput_file "`base_dir'/outputs/tables/throughput_pressure_results_python.csv"
local output_table "`base_dir'/outputs/tables/future_systems_stata_viability_results.csv"
local throughput_output "`base_dir'/outputs/tables/future_systems_stata_throughput_results.csv"
local log_file "`base_dir'/outputs/tables/stata_future_economic_systems_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable future_viability_score "Composite future viability score"

summarize future_viability_score ecological_pressure institutional_capacity social_inclusion resilience public_trust adaptive_learning

export delimited using "`output_table'", replace

capture confirm file "`throughput_file'"
if !_rc {
    import delimited "`throughput_file'", clear varnames(1)
    summarize throughput_pressure wellbeing_per_throughput viable_throughput_score
    export delimited using "`throughput_output'", replace
}

log close
