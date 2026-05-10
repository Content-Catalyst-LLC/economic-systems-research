.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_poverty_capability_data.py
	python3 python/01_poverty_capability_inclusion_analysis.py
	python3 python/02_services_vulnerability_systems_analysis.py

r:
	Rscript r/poverty_capability_analysis.R

stata:
	stata -b do stata/poverty_capability_workflow.do || stata-mp -b do stata/poverty_capability_workflow.do || stata-se -b do stata/poverty_capability_workflow.do

sql:
	sqlite3 data/processed/poverty_capability_economic_inclusion.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/poverty_capability_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
