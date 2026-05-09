* Limits of Stabilization Policy Stata Workflow
* Article: Limits of Stabilization Policy: Fiscal Policy, Monetary Policy, and Macroeconomic Constraints
*
* Purpose:
* Applied macroeconomics replication workflow for stabilization-policy constraints.
*
* Assumes Python workflow has already created:
* data/processed/stabilization_constraints_quarterly_panel.csv

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/data/processed/stabilization_constraints_quarterly_panel.csv"
local output_table "`base_dir'/outputs/tables/constraints_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_stabilization_constraints_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

gen date_stata = date(date, "YMD")
format date_stata %td
gen qdate = qofd(date_stata)
format qdate %tq
tsset qdate

capture confirm variable delta_unemployment_rate
if _rc {
    gen delta_unemployment_rate = unemployment_rate - L.unemployment_rate
}

label variable federal_funds_rate "Federal funds rate"
label variable cpi_inflation_yoy_pct "CPI inflation, year over year"
label variable output_gap_pct "Output gap percentage"
label variable delta_unemployment_rate "Quarterly change in unemployment rate"
label variable recession_indicator "NBER-based recession indicator"
label variable debt_to_gdp "Federal debt as percent of GDP"
label variable interest_growth_gap "Interest-growth gap proxy"
label variable debt_stabilizing_primary_balance_pct_gdp "Debt-stabilizing primary balance proxy"

summarize federal_funds_rate cpi_inflation_yoy_pct output_gap_pct unemployment_rate debt_to_gdp interest_growth_gap
tabstat federal_funds_rate cpi_inflation_yoy_pct output_gap_pct unemployment_rate debt_to_gdp interest_growth_gap, by(recession_indicator) statistics(n mean sd min max)

regress federal_funds_rate cpi_inflation_yoy_pct output_gap_pct delta_unemployment_rate recession_indicator lower_bound_constraint_flag inflation_constraint_flag, vce(robust)

matrix b = e(b)
matrix V = e(V)

preserve
clear
set obs 7

gen term = ""
replace term = "_cons" in 1
replace term = "cpi_inflation_yoy_pct" in 2
replace term = "output_gap_pct" in 3
replace term = "delta_unemployment_rate" in 4
replace term = "recession_indicator" in 5
replace term = "lower_bound_constraint_flag" in 6
replace term = "inflation_constraint_flag" in 7

gen estimate = .
replace estimate = b[1, "_cons"] in 1
replace estimate = b[1, "cpi_inflation_yoy_pct"] in 2
replace estimate = b[1, "output_gap_pct"] in 3
replace estimate = b[1, "delta_unemployment_rate"] in 4
replace estimate = b[1, "recession_indicator"] in 5
replace estimate = b[1, "lower_bound_constraint_flag"] in 6
replace estimate = b[1, "inflation_constraint_flag"] in 7

gen robust_se = .
forvalues i = 1/7 {
    replace robust_se = sqrt(V[`i',`i']) in `i'
}

gen t_value = estimate / robust_se
export delimited using "`output_table'", replace
restore

log close
