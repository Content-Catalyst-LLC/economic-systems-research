.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_political_economy_data.py
	python3 python/01_distribution_power_fiscal_analysis.py
	python3 python/02_conflict_crisis_legitimacy_analysis.py

r:
	Rscript r/political_economy_analysis.R

stata:
	stata -b do stata/political_economy_workflow.do || stata-mp -b do stata/political_economy_workflow.do || stata-se -b do stata/political_economy_workflow.do

sql:
	sqlite3 data/processed/political_economy_power_distributional_conflict.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/political_economy_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
