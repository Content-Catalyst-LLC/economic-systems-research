* Debt, Dependency, and Global Financial Order
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/debt_position_results_python.csv"
local restructuring_file "`base_dir'/outputs/tables/restructuring_results_python.csv"
local output_table "`base_dir'/outputs/tables/debt_dependency_stata_results.csv"
local restructuring_output "`base_dir'/outputs/tables/debt_dependency_stata_restructuring_results.csv"
local log_file "`base_dir'/outputs/tables/stata_debt_dependency_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable debt_ratio "Debt-to-output ratio"
label variable external_debt_service_ratio "External debt-service ratio"
label variable domestic_currency_fx_burden "Domestic-currency burden of FX debt"
label variable reserve_adequacy "Reserve adequacy"
label variable external_vulnerability_score "External vulnerability score"

summarize debt_ratio external_debt_service_ratio domestic_currency_fx_burden reserve_adequacy external_vulnerability_score

export delimited using "`output_table'", replace

capture confirm file "`restructuring_file'"
if !_rc {
    import delimited "`restructuring_file'", clear varnames(1)
    summarize post_restructuring_debt restructuring_haircut maturity_extension interest_relief resolution_quality_score
    export delimited using "`restructuring_output'", replace
}

log close
