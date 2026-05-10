* Externalities, Public Goods, and Collective Provision
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/private_social_optimum_python.csv"
local pg_file "`base_dir'/outputs/tables/public_good_underprovision_python.csv"
local output_table "`base_dir'/outputs/tables/externalities_public_goods_stata_results.csv"
local pg_output "`base_dir'/outputs/tables/externalities_public_goods_stata_public_goods.csv"
local log_file "`base_dir'/outputs/tables/stata_externalities_public_goods_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable private_output "Private output"
label variable social_output "Socially efficient output"
label variable private_minus_social_output "Private minus social output"

summarize private_output social_output private_minus_social_output threshold_crossing_output

export delimited using "`output_table'", replace

capture confirm file "`pg_file'"
if !_rc {
    import delimited "`pg_file'", clear varnames(1)
    summarize social_benefit underprovision_gap private_incentive_gap social_return_ratio
    export delimited using "`pg_output'", replace
}

log close
