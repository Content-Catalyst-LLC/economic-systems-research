.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_household_welfare_data.py
	python3 python/01_budget_fragility_analysis.py
	python3 python/02_time_public_goods_resilience.py

r:
	Rscript r/consumer_choice_analysis.R

stata:
	stata -b do stata/consumer_choice_workflow.do || stata-mp -b do stata/consumer_choice_workflow.do || stata-se -b do stata/consumer_choice_workflow.do

sql:
	sqlite3 data/processed/consumer_choice_household_welfare.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/household_resilience_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
