* Money, Banking, Credit, and Financial Intermediation
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/bank_balance_sheet_results_python.csv"
local liquidity_file "`base_dir'/outputs/tables/liquidity_stress_results_python.csv"
local output_table "`base_dir'/outputs/tables/money_banking_stata_results.csv"
local liquidity_output "`base_dir'/outputs/tables/money_banking_stata_liquidity.csv"
local log_file "`base_dir'/outputs/tables/stata_money_banking_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable leverage "Assets divided by equity"
label variable capital_ratio "Equity divided by assets"
label variable loan_to_deposit_ratio "Loans divided by deposits"
label variable liquid_asset_ratio "Liquid assets divided by assets"

summarize leverage capital_ratio loan_to_deposit_ratio liquid_asset_ratio wholesale_funding_share

export delimited using "`output_table'", replace

capture confirm file "`liquidity_file'"
if !_rc {
    import delimited "`liquidity_file'", clear varnames(1)
    summarize liquidity_coverage_ratio stress_liquidity_score liquidity_stress_flag deposit_outflow_rate market_funding_rollover_rate
    export delimited using "`liquidity_output'", replace
}

log close
