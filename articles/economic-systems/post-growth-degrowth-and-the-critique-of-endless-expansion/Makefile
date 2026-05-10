.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_post_growth_data.py
	python3 python/01_growth_throughput_wellbeing_analysis.py
	python3 python/02_sufficiency_finance_transition_analysis.py

r:
	Rscript r/post_growth_analysis.R

stata:
	stata -b do stata/post_growth_workflow.do || stata-mp -b do stata/post_growth_workflow.do || stata-se -b do stata/post_growth_workflow.do

sql:
	sqlite3 data/processed/post_growth_degrowth_endless_expansion.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/post_growth_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
