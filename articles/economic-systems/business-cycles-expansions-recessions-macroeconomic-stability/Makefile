.PHONY: python r stata sql julia all clean

python:
	python3 python/00_fetch_and_build_panel.py
	python3 python/01_business_cycle_episode_metrics.py
	python3 python/02_trend_cycle_and_stability.py

r:
	Rscript r/business_cycle_analysis.R

stata:
	stata -b do stata/business_cycle_workflow.do || stata-mp -b do stata/business_cycle_workflow.do || stata-se -b do stata/business_cycle_workflow.do

sql:
	sqlite3 data/processed/business_cycles.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/business_cycle_model.jl

all: python r sql julia

clean:
	rm -f data/raw/*.csv
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
