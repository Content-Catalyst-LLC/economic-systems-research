* Growth, Development, and Structural Transformation
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/growth_results_python.csv"
local sector_file "`base_dir'/outputs/tables/sector_transformation_results_python.csv"
local output_table "`base_dir'/outputs/tables/development_stata_results.csv"
local sector_output "`base_dir'/outputs/tables/development_stata_sector_results.csv"
local log_file "`base_dir'/outputs/tables/stata_development_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable output "Aggregate output"
label variable labor "Labor input"
label variable growth_rate "Output growth rate"
label variable labor_productivity "Labor productivity"
label variable cumulative_growth "Cumulative growth"

summarize output labor growth_rate labor_productivity cumulative_growth

export delimited using "`output_table'", replace

capture confirm file "`sector_file'"
if !_rc {
    import delimited "`sector_file'", clear varnames(1)
    summarize output_share labor_share sector_productivity productivity_gap_to_economy
    export delimited using "`sector_output'", replace
}

log close
