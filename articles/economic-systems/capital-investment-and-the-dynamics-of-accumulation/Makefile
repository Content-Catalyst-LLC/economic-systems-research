.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_capital_investment_data.py
	python3 python/01_capital_accumulation_npv_analysis.py
	python3 python/02_maintenance_ownership_finance_sustainability.py

r:
	Rscript r/capital_investment_analysis.R

stata:
	stata -b do stata/capital_investment_workflow.do || stata-mp -b do stata/capital_investment_workflow.do || stata-se -b do stata/capital_investment_workflow.do

sql:
	sqlite3 data/processed/capital_investment_accumulation.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/capital_investment_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
