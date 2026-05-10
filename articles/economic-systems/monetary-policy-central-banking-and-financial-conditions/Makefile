.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_monetary_policy_data.py
	python3 python/01_rates_debt_financial_conditions_analysis.py
	python3 python/02_asset_liquidity_open_public_investment_analysis.py

r:
	Rscript r/monetary_policy_analysis.R

stata:
	stata -b do stata/monetary_policy_workflow.do || stata-mp -b do stata/monetary_policy_workflow.do || stata-se -b do stata/monetary_policy_workflow.do

sql:
	sqlite3 data/processed/monetary_policy_central_banking_financial_conditions.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/monetary_policy_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
