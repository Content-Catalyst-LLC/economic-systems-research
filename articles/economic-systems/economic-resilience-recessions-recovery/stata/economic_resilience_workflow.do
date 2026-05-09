* Economic Resilience Stata Workflow
* Purpose: Applied econometric starting point for recession and recovery analysis.

clear all
set more off

local base_dir "`c(pwd)'/articles/economic-systems/economic-resilience-recessions-recovery"
local input_file "`base_dir'/outputs/economic_resilience_indicators.csv"
local output_file "`base_dir'/outputs/stata_recession_summary.csv"

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run the Python workflow first."
    exit 601
}

import delimited "`input_file'", clear varnames(1)

gen recession = recession_indicator == 1 if !missing(recession_indicator)

summarize unemployment_rate real_gdp_growth_annualized federal_funds_rate
table recession, statistic(mean unemployment_rate) statistic(mean real_gdp_growth_annualized) statistic(mean federal_funds_rate)

export delimited using "`output_file'", replace
