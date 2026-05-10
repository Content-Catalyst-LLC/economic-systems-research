* Circular Economy and Regenerative Production
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/material_flow_results_python.csv"
local design_file "`base_dir'/outputs/tables/product_life_design_results_python.csv"
local output_table "`base_dir'/outputs/tables/circular_economy_stata_material_results.csv"
local design_output "`base_dir'/outputs/tables/circular_economy_stata_design_results.csv"
local log_file "`base_dir'/outputs/tables/stata_circular_economy_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable circularity_ratio "Recovered material divided by total material input"
label variable waste_reduction_ratio "One minus residual waste divided by total throughput"
label variable circular_performance_score "Composite circular performance score"

summarize circularity_ratio waste_reduction_ratio circular_performance_score virgin_material_input residual_waste

export delimited using "`output_table'", replace

capture confirm file "`design_file'"
if !_rc {
    import delimited "`design_file'", clear varnames(1)
    summarize product_life_extension repairability modularity disassembly_score design_for_circularity_score
    export delimited using "`design_output'", replace
}

log close
