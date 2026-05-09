.PHONY: python r stata sql julia all clean

python:
	python3 python/00_fetch_and_build_panel.py
	python3 python/01_recession_recovery_metrics.py
	python3 python/02_okun_analysis.py

r:
	Rscript r/economic_resilience_analysis.R

stata:
	stata -b do stata/economic_resilience_workflow.do || stata-mp -b do stata/economic_resilience_workflow.do || stata-se -b do stata/economic_resilience_workflow.do

sql:
	sqlite3 data/processed/economic_resilience.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/economic_resilience_model.jl

all: python r sql julia

clean:
	rm -f data/raw/*.csv
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f *.log
	rm -f stata/*.log
