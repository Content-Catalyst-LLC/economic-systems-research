.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_is_lm_scenarios.py
	python3 python/01_is_lm_comparative_statics.py
	python3 python/02_is_lm_diagrams.py

r:
	Rscript r/is_lm_analysis.R

stata:
	stata -b do stata/is_lm_workflow.do || stata-mp -b do stata/is_lm_workflow.do || stata-se -b do stata/is_lm_workflow.do

sql:
	sqlite3 data/processed/is_lm_model.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/is_lm_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
