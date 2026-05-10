* Political Economy, Power, and Distributional Conflict
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/income_distribution_results_python.csv"
local power_file "`base_dir'/outputs/tables/power_asymmetry_results_python.csv"
local output_table "`base_dir'/outputs/tables/political_economy_stata_income_results.csv"
local power_output "`base_dir'/outputs/tables/political_economy_stata_power_results.csv"
local log_file "`base_dir'/outputs/tables/stata_political_economy_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable wage_share "Wage income divided by total income"
label variable profit_share "Profit income divided by total income"
label variable rent_share "Rent income divided by total income"
label variable net_fiscal_position "Benefits and services minus taxes"
label variable distributional_concentration_score "Profit plus rent share"

summarize wage_share profit_share rent_share net_fiscal_position distributional_concentration_score

export delimited using "`output_table'", replace

capture confirm file "`power_file'"
if !_rc {
    import delimited "`power_file'", clear varnames(1)
    summarize ownership_power organization_power access_power mobility_power voice_power power_asymmetry_score
    export delimited using "`power_output'", replace
}

log close
