* Commons, Shared Resources, and Institutional Governance
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/commons_stock_summary_python.csv"
local compliance_file "`base_dir'/outputs/tables/governance_compliance_results_python.csv"
local output_table "`base_dir'/outputs/tables/commons_stata_results.csv"
local compliance_output "`base_dir'/outputs/tables/commons_stata_compliance.csv"
local log_file "`base_dir'/outputs/tables/stata_commons_governance_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable final_stock "Final resource stock"
label variable minimum_stock "Minimum resource stock"
label variable average_harvest "Average harvest"
label variable average_regeneration "Average regeneration"
label variable periods_in_depletion_risk "Periods below critical stock threshold"

summarize final_stock minimum_stock average_harvest average_regeneration periods_in_depletion_risk

export delimited using "`output_table'", replace

capture confirm file "`compliance_file'"
if !_rc {
    import delimited "`compliance_file'", clear varnames(1)
    summarize compliance_score adaptive_governance_score governance_failure_risk monitoring_capacity legitimacy capture_risk
    export delimited using "`compliance_output'", replace
}

log close
