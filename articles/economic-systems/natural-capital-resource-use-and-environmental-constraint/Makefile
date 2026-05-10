.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_natural_capital_data.py
	python3 python/01_stock_flow_resource_waste_analysis.py
	python3 python/02_governance_burden_resilience_analysis.py

r:
	Rscript r/natural_capital_analysis.R

stata:
	stata -b do stata/natural_capital_workflow.do || stata-mp -b do stata/natural_capital_workflow.do || stata-se -b do stata/natural_capital_workflow.do

sql:
	sqlite3 data/processed/natural_capital_resource_constraint.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/natural_capital_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
