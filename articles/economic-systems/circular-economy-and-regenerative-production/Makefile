.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_circular_economy_data.py
	python3 python/01_circularity_material_flow_analysis.py
	python3 python/02_regeneration_rebound_justice_analysis.py

r:
	Rscript r/circular_economy_analysis.R

stata:
	stata -b do stata/circular_economy_workflow.do || stata-mp -b do stata/circular_economy_workflow.do || stata-se -b do stata/circular_economy_workflow.do

sql:
	sqlite3 data/processed/circular_economy_regenerative_production.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/circular_economy_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
