* Beyond GDP: Measuring Well-Being, Inclusion, and Sustainability
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/gdp_wellbeing_dashboard_results_python.csv"
local inclusion_file "`base_dir'/outputs/tables/inclusion_results_python.csv"
local output_table "`base_dir'/outputs/tables/beyond_gdp_stata_dashboard_results.csv"
local inclusion_output "`base_dir'/outputs/tables/beyond_gdp_stata_inclusion_results.csv"
local log_file "`base_dir'/outputs/tables/stata_beyond_gdp_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable gdp "Consumption plus investment plus government plus net exports"
label variable wellbeing_score "Composite multidimensional well-being score"
label variable gdp_wellbeing_gap "Normalized GDP minus well-being score"

summarize gdp wellbeing_score gdp_wellbeing_gap health education income_security housing environment

export delimited using "`output_table'", replace

capture confirm file "`inclusion_file'"
if !_rc {
    import delimited "`inclusion_file'", clear varnames(1)
    summarize inclusion_score distribution mobility access voice regional_equity service_reach
    export delimited using "`inclusion_output'", replace
}

log close
