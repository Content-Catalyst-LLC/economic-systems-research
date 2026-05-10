.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_information_uncertainty_data.py
	python3 python/01_adverse_selection_moral_hazard_signaling.py
	python3 python/02_search_opacity_robustness.py

r:
	Rscript r/information_uncertainty_analysis.R

stata:
	stata -b do stata/information_uncertainty_workflow.do || stata-mp -b do stata/information_uncertainty_workflow.do || stata-se -b do stata/information_uncertainty_workflow.do

sql:
	sqlite3 data/processed/information_uncertainty_imperfect_markets.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/information_uncertainty_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
