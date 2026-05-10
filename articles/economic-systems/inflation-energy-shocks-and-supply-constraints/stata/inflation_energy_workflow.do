* Inflation, Energy Shocks, and Supply Constraints
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/inflation_results_python.csv"
local household_file "`base_dir'/outputs/tables/household_energy_burden_results_python.csv"
local output_table "`base_dir'/outputs/tables/inflation_energy_stata_results.csv"
local household_output "`base_dir'/outputs/tables/inflation_energy_stata_household_results.csv"
local log_file "`base_dir'/outputs/tables/stata_inflation_energy_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable price_level "Price level"
label variable inflation_rate "Inflation rate"
label variable cumulative_inflation "Cumulative inflation"

summarize price_level inflation_rate cumulative_inflation

export delimited using "`output_table'", replace

capture confirm file "`household_file'"
if !_rc {
    import delimited "`household_file'", clear varnames(1)
    summarize household_energy_burden transport_fuel_burden combined_energy_transport_burden real_wage energy_poverty_flag
    export delimited using "`household_output'", replace
}

log close
