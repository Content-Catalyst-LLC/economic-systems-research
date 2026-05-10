.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_beyond_gdp_data.py
	python3 python/01_wellbeing_inclusion_sustainability_analysis.py
	python3 python/02_dashboard_capability_governance_analysis.py

r:
	Rscript r/beyond_gdp_analysis.R

stata:
	stata -b do stata/beyond_gdp_workflow.do || stata-mp -b do stata/beyond_gdp_workflow.do || stata-se -b do stata/beyond_gdp_workflow.do

sql:
	sqlite3 data/processed/beyond_gdp_wellbeing_inclusion_sustainability.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/beyond_gdp_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
