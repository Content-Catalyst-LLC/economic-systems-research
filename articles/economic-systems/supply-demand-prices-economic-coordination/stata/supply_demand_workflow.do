* Supply, Demand, Prices, and Economic Coordination
* Stata Workflow

clear all
set more off

local base_dir "`c(pwd)'"
local input_file "`base_dir'/outputs/tables/equilibrium_results_python.csv"
local output_table "`base_dir'/outputs/tables/supply_demand_stata_results.csv"
local log_file "`base_dir'/outputs/tables/stata_supply_demand_workflow.log"

capture log close
log using "`log_file'", replace text

capture confirm file "`input_file'"
if _rc {
    display as error "Input file not found. Run: make python"
    exit 601
}

import delimited "`input_file'", clear varnames(1)

label variable equilibrium_price "Equilibrium price"
label variable equilibrium_quantity "Equilibrium quantity"
label variable demand_elasticity "Demand elasticity"
label variable supply_elasticity "Supply elasticity"
label variable social_cost_gap "Social cost gap"

summarize equilibrium_price equilibrium_quantity demand_elasticity supply_elasticity social_cost_gap price_change_from_baseline quantity_change_from_baseline

export delimited using "`output_table'", replace

log close
