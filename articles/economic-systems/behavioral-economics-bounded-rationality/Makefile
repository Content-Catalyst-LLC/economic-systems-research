.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_behavioral_data.py
	python3 python/01_behavioral_choice_analysis.py
	python3 python/02_defaults_burden_social_norms.py

r:
	Rscript r/behavioral_analysis.R

stata:
	stata -b do stata/behavioral_workflow.do || stata-mp -b do stata/behavioral_workflow.do || stata-se -b do stata/behavioral_workflow.do

sql:
	sqlite3 data/processed/behavioral_economics_bounded_rationality.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/behavioral_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
