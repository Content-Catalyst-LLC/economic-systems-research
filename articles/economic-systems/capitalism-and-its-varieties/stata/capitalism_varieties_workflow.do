* Capitalism and Its Varieties
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/regime_distribution_results_python.csv"
local finance_file "`base_dir'/outputs/tables/financialization_results_python.csv"
local output_table "`base_dir'/outputs/tables/capitalism_varieties_stata_regime_results.csv"
local finance_output "`base_dir'/outputs/tables/capitalism_varieties_stata_finance_results.csv"
local log_file "`base_dir'/outputs/tables/stata_capitalism_varieties_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable profit "Revenue minus cost"
label variable wage_share "Wage income divided by output"
label variable profit_share "Profit divided by output"
label variable institutional_advantage_score "Comparative institutional advantage score"

summarize profit wage_share profit_share institutional_advantage_score

export delimited using "`output_table'", replace

capture confirm file "`finance_file'"
if !_rc {
    import delimited "`finance_file'", clear varnames(1)
    summarize financialization_score productive_finance_score
    export delimited using "`finance_output'", replace
}

log close
