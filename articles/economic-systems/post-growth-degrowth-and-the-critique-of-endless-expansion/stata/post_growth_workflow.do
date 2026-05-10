* Post-Growth, Degrowth, and the Critique of Endless Expansion
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/growth_dependence_results_python.csv"
local throughput_file "`base_dir'/outputs/tables/throughput_results_python.csv"
local output_table "`base_dir'/outputs/tables/post_growth_stata_growth_dependence_results.csv"
local throughput_output "`base_dir'/outputs/tables/post_growth_stata_throughput_results.csv"
local log_file "`base_dir'/outputs/tables/stata_post_growth_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable growth_dependence_score "Composite growth dependence score"

summarize growth_dependence_score employment_dependency debt_service_dependency fiscal_dependency asset_dependency pension_dependency housing_market_dependency

export delimited using "`output_table'", replace

capture confirm file "`throughput_file'"
if !_rc {
    import delimited "`throughput_file'", clear varnames(1)
    summarize throughput_index wellbeing_per_throughput just_throughput_score
    export delimited using "`throughput_output'", replace
}

log close
