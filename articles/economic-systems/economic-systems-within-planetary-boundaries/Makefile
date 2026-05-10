.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_planetary_boundaries_data.py
	python3 python/01_boundary_resource_sector_analysis.py
	python3 python/02_justice_transition_finance_analysis.py

r:
	Rscript r/planetary_boundaries_analysis.R

stata:
	stata -b do stata/planetary_boundaries_workflow.do || stata-mp -b do stata/planetary_boundaries_workflow.do || stata-se -b do stata/planetary_boundaries_workflow.do

sql:
	sqlite3 data/processed/economic_systems_within_planetary_boundaries.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/planetary_boundaries_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
