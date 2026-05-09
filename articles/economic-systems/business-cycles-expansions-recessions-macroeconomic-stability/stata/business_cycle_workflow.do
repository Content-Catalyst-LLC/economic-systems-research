* Business Cycles Stata Workflow
* Article: Business Cycles: Economic Expansions, Recessions, and Macroeconomic Stability
*
* Purpose:
* Applied economics replication workflow for business-cycle analysis.
*
* Assumes Python workflow has already created:
* data/processed/business_cycles_quarterly_panel.csv

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/data/processed/business_cycles_quarterly_panel.csv"
local output_table "`base_dir'/outputs/tables/business_cycle_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_business_cycle_workflow.log"

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

label variable real_gdp_growth_annualized "Real GDP growth, annualized"
label variable unemployment_rate "Civilian unemployment rate"
label variable delta_unemployment_rate "Quarterly change in unemployment rate"
label variable output_gap_pct "Output gap percentage"
label variable recession_indicator "NBER-based recession indicator"
label variable federal_funds_rate "Federal funds rate"

summarize real_gdp_growth_annualized unemployment_rate output_gap_pct federal_funds_rate
tabstat real_gdp_growth_annualized unemployment_rate output_gap_pct federal_funds_rate, by(recession_indicator) statistics(n mean sd min max)

regress real_gdp_growth_annualized delta_unemployment_rate output_gap_pct recession_indicator federal_funds_rate, vce(robust)

matrix b = e(b)
matrix V = e(V)

preserve
clear
set obs 5

gen term = ""
replace term = "_cons" in 1
replace term = "delta_unemployment_rate" in 2
replace term = "output_gap_pct" in 3
replace term = "recession_indicator" in 4
replace term = "federal_funds_rate" in 5

gen estimate = .
replace estimate = b[1, "_cons"] in 1
replace estimate = b[1, "delta_unemployment_rate"] in 2
replace estimate = b[1, "output_gap_pct"] in 3
replace estimate = b[1, "recession_indicator"] in 4
replace estimate = b[1, "federal_funds_rate"] in 5

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
