.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_resilience_data.py
	python3 python/01_resilience_fragility_shock_analysis.py
	python3 python/02_household_finance_labor_ecology_analysis.py

r:
	Rscript r/economic_resilience_analysis.R

stata:
	stata -b do stata/economic_resilience_workflow.do || stata-mp -b do stata/economic_resilience_workflow.do || stata-se -b do stata/economic_resilience_workflow.do

sql:
	sqlite3 data/processed/economic_resilience_fragility_adaptive_capacity.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/economic_resilience_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
