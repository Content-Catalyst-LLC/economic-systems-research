.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_macro_stability_data.py
	python3 python/01_aggregate_demand_cycle_analysis.py
	python3 python/02_balance_sheets_policy_shocks_recovery.py

r:
	Rscript r/macro_stability_analysis.R

stata:
	stata -b do stata/macro_stability_workflow.do || stata-mp -b do stata/macro_stability_workflow.do || stata-se -b do stata/macro_stability_workflow.do

sql:
	sqlite3 data/processed/macroeconomic_stability_business_cycles_crisis.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/macro_stability_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
