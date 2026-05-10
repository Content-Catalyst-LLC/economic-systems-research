* Finance, Leverage, and Systemic Risk
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/leverage_amplification_results_python.csv"
local funding_file "`base_dir'/outputs/tables/funding_gap_results_python.csv"
local output_table "`base_dir'/outputs/tables/finance_leverage_stata_results.csv"
local funding_output "`base_dir'/outputs/tables/finance_leverage_stata_funding.csv"
local log_file "`base_dir'/outputs/tables/stata_finance_leverage_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable asset_shock "Asset price shock"
label variable initial_leverage "Initial leverage"
label variable equity_before "Equity before shock"
label variable equity_after_shock "Equity after shock"
label variable equity_loss_pct "Equity loss percentage"
label variable insolvent_flag "Insolvent after shock"

summarize asset_shock initial_leverage equity_before equity_after_shock equity_loss_pct insolvent_flag

export delimited using "`output_table'", replace

capture confirm file "`funding_file'"
if !_rc {
    import delimited "`funding_file'", clear varnames(1)
    summarize raw_funding_gap rollover_adjusted_gap backstop_adjusted_gap funding_stress_flag
    export delimited using "`funding_output'", replace
}

log close
