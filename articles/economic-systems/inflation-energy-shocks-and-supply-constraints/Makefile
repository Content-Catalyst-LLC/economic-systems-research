.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_inflation_energy_data.py
	python3 python/01_inflation_pass_through_burden_analysis.py
	python3 python/02_bottlenecks_market_power_resilience.py

r:
	Rscript r/inflation_energy_analysis.R

stata:
	stata -b do stata/inflation_energy_workflow.do || stata-mp -b do stata/inflation_energy_workflow.do || stata-se -b do stata/inflation_energy_workflow.do

sql:
	sqlite3 data/processed/inflation_energy_shocks_supply_constraints.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/inflation_energy_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
