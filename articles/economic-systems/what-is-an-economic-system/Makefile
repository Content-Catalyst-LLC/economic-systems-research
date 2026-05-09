.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_economic_system_data.py
	python3 python/01_input_output_analysis.py
	python3 python/02_allocation_distribution_reproduction.py

r:
	Rscript r/economic_system_analysis.R

stata:
	stata -b do stata/economic_system_workflow.do || stata-mp -b do stata/economic_system_workflow.do || stata-se -b do stata/economic_system_workflow.do

sql:
	sqlite3 data/processed/economic_system.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/economic_system_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
