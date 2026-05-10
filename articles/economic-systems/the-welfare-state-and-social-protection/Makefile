.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_welfare_state_data.py
	python3 python/01_social_spending_protection_analysis.py
	python3 python/02_life_course_adaptive_protection_analysis.py

r:
	Rscript r/welfare_state_analysis.R

stata:
	stata -b do stata/welfare_state_workflow.do || stata-mp -b do stata/welfare_state_workflow.do || stata-se -b do stata/welfare_state_workflow.do

sql:
	sqlite3 data/processed/welfare_state_social_protection.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/welfare_state_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
