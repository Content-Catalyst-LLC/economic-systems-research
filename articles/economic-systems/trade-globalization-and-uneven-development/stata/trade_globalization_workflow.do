* Trade, Globalization, and Uneven Development
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/trade_position_results_python.csv"
local value_chain_file "`base_dir'/outputs/tables/value_chain_results_python.csv"
local output_table "`base_dir'/outputs/tables/trade_globalization_stata_results.csv"
local value_output "`base_dir'/outputs/tables/trade_globalization_stata_value_chain_results.csv"
local log_file "`base_dir'/outputs/tables/stata_trade_globalization_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable trade_openness "Trade openness"
label variable trade_balance "Trade balance"
label variable import_dependence_score "Import dependence score"

summarize exports imports output trade_openness trade_balance import_dependence_score

export delimited using "`output_table'", replace

capture confirm file "`value_chain_file'"
if !_rc {
    import delimited "`value_chain_file'", clear varnames(1)
    summarize domestic_value_capture command_position_score lead_firm_control technology_control
    export delimited using "`value_output'", replace
}

log close
