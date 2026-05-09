.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_scarcity_allocation_data.py
	python3 python/01_allocation_analysis.py
	python3 python/02_access_and_reproduction_constraints.py

r:
	Rscript r/scarcity_allocation_analysis.R

stata:
	stata -b do stata/scarcity_allocation_workflow.do || stata-mp -b do stata/scarcity_allocation_workflow.do || stata-se -b do stata/scarcity_allocation_workflow.do

sql:
	sqlite3 data/processed/scarcity_allocation.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/scarcity_allocation_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
