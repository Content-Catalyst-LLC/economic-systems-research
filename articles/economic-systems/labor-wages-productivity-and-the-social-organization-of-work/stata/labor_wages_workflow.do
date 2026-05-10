* Labor, Wages, Productivity, and the Social Organization of Work
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/productivity_wage_share_results_python.csv"
local reproduction_file "`base_dir'/outputs/tables/social_reproduction_adequacy_python.csv"
local output_table "`base_dir'/outputs/tables/labor_stata_results.csv"
local reproduction_output "`base_dir'/outputs/tables/labor_stata_social_reproduction.csv"
local log_file "`base_dir'/outputs/tables/stata_labor_wages_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable labor_productivity "Labor productivity"
label variable wage_share "Wage share"
label variable average_wage "Average wage"
label variable unit_labor_cost "Unit labor cost"
label variable employment_quality_index "Employment quality index"

summarize labor_productivity wage_share average_wage unit_labor_cost employment_quality_index care_intensity

export delimited using "`output_table'", replace

capture confirm file "`reproduction_file'"
if !_rc {
    import delimited "`reproduction_file'", clear varnames(1)
    summarize wage_income social_support household_cost care_reproduction_cost adequacy_gap adequacy_ratio reproduction_stress_flag
    export delimited using "`reproduction_output'", replace
}

log close
