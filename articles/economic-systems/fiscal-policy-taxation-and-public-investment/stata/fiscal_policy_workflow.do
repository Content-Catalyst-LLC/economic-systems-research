* Fiscal Policy, Taxation, and Public Investment
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/fiscal_position_results_python.csv"
local tax_file "`base_dir'/outputs/tables/tax_distribution_results_python.csv"
local output_table "`base_dir'/outputs/tables/fiscal_policy_stata_results.csv"
local tax_output "`base_dir'/outputs/tables/fiscal_policy_stata_tax_results.csv"
local log_file "`base_dir'/outputs/tables/stata_fiscal_policy_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable budget_balance "Budget balance"
label variable primary_balance "Primary balance"
label variable tax_ratio "Tax-to-output ratio"
label variable spending_ratio "Spending-to-output ratio"
label variable debt_to_output "Debt-to-output ratio"
label variable next_period_debt_to_output "Next-period debt-to-output ratio"

summarize budget_balance primary_balance tax_ratio spending_ratio debt_to_output next_period_debt_to_output

export delimited using "`output_table'", replace

capture confirm file "`tax_file'"
if !_rc {
    import delimited "`tax_file'", clear varnames(1)
    summarize effective_tax_rate broad_effective_tax_rate net_transfer_position consumption_tax_rate
    export delimited using "`tax_output'", replace
}

log close
