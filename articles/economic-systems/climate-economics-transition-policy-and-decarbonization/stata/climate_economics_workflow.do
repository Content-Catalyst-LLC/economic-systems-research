* Climate Economics, Transition Policy, and Decarbonization
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/sector_emissions_results_python.csv"
local policy_file "`base_dir'/outputs/tables/policy_package_results_python.csv"
local output_table "`base_dir'/outputs/tables/climate_economics_stata_sector_results.csv"
local policy_output "`base_dir'/outputs/tables/climate_economics_stata_policy_results.csv"
local log_file "`base_dir'/outputs/tables/stata_climate_economics_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable emissions "Output times energy intensity times carbon intensity"
label variable decarbonization_rate "Annual change in emissions intensity"
label variable transition_priority_score "Composite transition priority score"

summarize emissions decarbonization_rate transition_priority_score abatement_readiness

export delimited using "`output_table'", replace

capture confirm file "`policy_file'"
if !_rc {
    import delimited "`policy_file'", clear varnames(1)
    summarize policy_mix_score legitimacy_risk carbon_price_strength regulatory_strength public_investment
    export delimited using "`policy_output'", replace
}

log close
