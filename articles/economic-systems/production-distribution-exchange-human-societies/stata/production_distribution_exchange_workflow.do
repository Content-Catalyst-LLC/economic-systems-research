* Production, Distribution, and Exchange in Human Societies
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/data/processed/production_distribution_exchange_results.csv"
local output_table "`base_dir'/outputs/tables/production_distribution_exchange_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_production_distribution_exchange_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable total_output "Total output"
label variable labor_income "Labor income"
label variable non_labor_income "Non-labor income"
label variable ecological_throughput "Ecological throughput"
label variable exchange_dependency "Exchange dependency"

summarize total_output labor_income non_labor_income ecological_throughput exchange_dependency

collapse (sum) total_output labor_income non_labor_income ecological_throughput exchange_dependency, by(scenario)

gen labor_share = labor_income / total_output
gen non_labor_share = non_labor_income / total_output
gen exchange_dependency_ratio = exchange_dependency / total_output
gen throughput_per_output = ecological_throughput / total_output

export delimited using "`output_table'", replace

log close
