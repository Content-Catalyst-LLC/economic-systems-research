.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_labor_wages_data.py
	python3 python/01_productivity_wages_distribution_analysis.py
	python3 python/02_reproduction_time_bargaining_automation.py

r:
	Rscript r/labor_wages_analysis.R

stata:
	stata -b do stata/labor_wages_workflow.do || stata-mp -b do stata/labor_wages_workflow.do || stata-se -b do stata/labor_wages_workflow.do

sql:
	sqlite3 data/processed/labor_wages_productivity_work.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/labor_wages_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
