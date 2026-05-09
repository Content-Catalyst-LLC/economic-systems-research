* Economic Resilience Stata Workflow
* Article: Economic Resilience: Why Recessions Occur and How Economies Recover
*
* Purpose:
* Applied economics replication workflow for recession and recovery analysis.
*
* Assumes Python workflow has already created:
* data/processed/economic_resilience_quarterly_panel.csv

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/data/processed/economic_resilience_quarterly_panel.csv"
local output_table "`base_dir'/outputs/tables/okun_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_workflow.log"

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

label variable unemployment_rate "Civilian unemployment rate"
label variable real_gdp_growth_annualized "Real GDP growth, annualized"
label variable delta_unemployment_rate "Quarterly change in unemployment rate"
label variable output_gap_pct "Output gap percentage"
label variable recession_indicator "Recession indicator"

summarize unemployment_rate real_gdp_growth_annualized output_gap_pct federal_funds_rate
tabstat unemployment_rate real_gdp_growth_annualized output_gap_pct federal_funds_rate, by(recession_indicator) statistics(n mean sd min max)

regress delta_unemployment_rate real_gdp_growth_annualized, vce(robust)

matrix b = e(b)
matrix V = e(V)

preserve
clear
set obs 2

gen term = ""
replace term = "_cons" in 1
replace term = "real_gdp_growth_annualized" in 2

gen estimate = .
replace estimate = b[1, "_cons"] in 1
replace estimate = b[1, "real_gdp_growth_annualized"] in 2

gen robust_se = .
replace robust_se = sqrt(V[1,1]) in 1
replace robust_se = sqrt(V[2,2]) in 2

gen t_value = estimate / robust_se
export delimited using "`output_table'", replace
restore

log close
