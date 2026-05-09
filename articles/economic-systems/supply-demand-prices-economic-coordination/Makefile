.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_supply_demand_data.py
	python3 python/01_equilibrium_elasticity_analysis.py
	python3 python/02_access_externality_coordination.py

r:
	Rscript r/supply_demand_analysis.R

stata:
	stata -b do stata/supply_demand_workflow.do || stata-mp -b do stata/supply_demand_workflow.do || stata-se -b do stata/supply_demand_workflow.do

sql:
	sqlite3 data/processed/supply_demand_coordination.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/supply_demand_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
