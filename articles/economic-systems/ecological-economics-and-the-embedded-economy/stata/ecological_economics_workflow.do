* Ecological Economics and the Embedded Economy
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/throughput_scale_results_python.csv"
local sector_file "`base_dir'/outputs/tables/sector_footprint_results_python.csv"
local output_table "`base_dir'/outputs/tables/ecological_economics_stata_throughput_results.csv"
local sector_output "`base_dir'/outputs/tables/ecological_economics_stata_sector_results.csv"
local log_file "`base_dir'/outputs/tables/stata_ecological_economics_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable throughput "Energy input plus material input"
label variable waste_residual "Throughput minus recovered throughput"
label variable recovery_rate "Recovered throughput divided by total throughput"
label variable scale_ratio "Economic scale divided by ecological capacity"

summarize throughput waste_residual recovery_rate scale_ratio wellbeing_index

export delimited using "`output_table'", replace

capture confirm file "`sector_file'"
if !_rc {
    import delimited "`sector_file'", clear varnames(1)
    summarize material_footprint ecological_pressure_score energy_intensity water_pressure land_pressure
    export delimited using "`sector_output'", replace
}

log close
