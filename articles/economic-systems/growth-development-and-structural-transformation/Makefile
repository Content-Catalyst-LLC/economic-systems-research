.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_development_data.py
	python3 python/01_growth_sector_capability_analysis.py
	python3 python/02_trade_inequality_energy_fragility_analysis.py

r:
	Rscript r/development_analysis.R

stata:
	stata -b do stata/development_workflow.do || stata-mp -b do stata/development_workflow.do || stata-se -b do stata/development_workflow.do

sql:
	sqlite3 data/processed/growth_development_structural_transformation.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/development_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
