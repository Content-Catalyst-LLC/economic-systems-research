.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_socialism_planning_data.py
	python3 python/01_mixed_economy_planning_analysis.py
	python3 python/02_sector_crisis_sustainability_analysis.py

r:
	Rscript r/socialism_planning_analysis.R

stata:
	stata -b do stata/socialism_planning_workflow.do || stata-mp -b do stata/socialism_planning_workflow.do || stata-se -b do stata/socialism_planning_workflow.do

sql:
	sqlite3 data/processed/socialism_planning_mixed_economy.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/socialism_planning_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
