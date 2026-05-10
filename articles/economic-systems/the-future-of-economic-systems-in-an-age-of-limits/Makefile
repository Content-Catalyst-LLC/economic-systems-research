.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_future_systems_data.py
	python3 python/01_viability_throughput_transition_analysis.py
	python3 python/02_finance_circularity_justice_legitimacy_analysis.py

r:
	Rscript r/future_economic_systems_analysis.R

stata:
	stata -b do stata/future_economic_systems_workflow.do || stata-mp -b do stata/future_economic_systems_workflow.do || stata-se -b do stata/future_economic_systems_workflow.do

sql:
	sqlite3 data/processed/future_economic_systems_age_of_limits.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/future_economic_systems_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
