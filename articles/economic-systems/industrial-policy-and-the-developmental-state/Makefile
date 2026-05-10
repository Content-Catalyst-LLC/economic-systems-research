.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_industrial_policy_data.py
	python3 python/01_sector_support_finance_analysis.py
	python3 python/02_infrastructure_skills_capture_green_analysis.py

r:
	Rscript r/industrial_policy_analysis.R

stata:
	stata -b do stata/industrial_policy_workflow.do || stata-mp -b do stata/industrial_policy_workflow.do || stata-se -b do stata/industrial_policy_workflow.do

sql:
	sqlite3 data/processed/industrial_policy_developmental_state.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/industrial_policy_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
