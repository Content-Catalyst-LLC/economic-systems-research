.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_production_distribution_exchange_data.py
	python3 python/01_input_output_distribution_analysis.py
	python3 python/02_exchange_throughput_scenarios.py

r:
	Rscript r/production_distribution_exchange_analysis.R

stata:
	stata -b do stata/production_distribution_exchange_workflow.do || stata-mp -b do stata/production_distribution_exchange_workflow.do || stata-se -b do stata/production_distribution_exchange_workflow.do

sql:
	sqlite3 data/processed/production_distribution_exchange.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/production_distribution_exchange_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
