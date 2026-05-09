* Stabilization Policy Stata Workflow
* Article: Stabilization Policy: Fiscal and Monetary Tools for Managing Economic Fluctuations
*
* Purpose:
* Applied macroeconomics replication workflow for stabilization-policy analysis.
*
* Assumes Python workflow has already created:
* data/processed/stabilization_policy_quarterly_panel.csv

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/data/processed/stabilization_policy_quarterly_panel.csv"
local output_table "`base_dir'/outputs/tables/stabilization_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_stabilization_policy_workflow.log"

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
label variable gov_spending_growth_yoy_pct "Government spending growth, year over year"
label variable policy_rate_gap "Policy-rate gap"

summarize federal_funds_rate cpi_inflation_yoy_pct output_gap_pct unemployment_rate gov_spending_growth_yoy_pct
tabstat federal_funds_rate cpi_inflation_yoy_pct output_gap_pct unemployment_rate gov_spending_growth_yoy_pct, by(recession_indicator) statistics(n mean sd min max)

regress federal_funds_rate cpi_inflation_yoy_pct output_gap_pct delta_unemployment_rate recession_indicator, vce(robust)

matrix b = e(b)
matrix V = e(V)

preserve
clear
set obs 5

gen term = ""
replace term = "_cons" in 1
replace term = "cpi_inflation_yoy_pct" in 2
replace term = "output_gap_pct" in 3
replace term = "delta_unemployment_rate" in 4
replace term = "recession_indicator" in 5

gen estimate = .
replace estimate = b[1, "_cons"] in 1
replace estimate = b[1, "cpi_inflation_yoy_pct"] in 2
replace estimate = b[1, "output_gap_pct"] in 3
replace estimate = b[1, "delta_unemployment_rate"] in 4
replace estimate = b[1, "recession_indicator"] in 5

gen robust_se = .
replace robust_se = sqrt(V[1,1]) in 1
replace robust_se = sqrt(V[2,2]) in 2
replace robust_se = sqrt(V[3,3]) in 3
replace robust_se = sqrt(V[4,4]) in 4
replace robust_se = sqrt(V[5,5]) in 5

gen t_value = estimate / robust_se
export delimited using "`output_table'", replace
restore

log close
