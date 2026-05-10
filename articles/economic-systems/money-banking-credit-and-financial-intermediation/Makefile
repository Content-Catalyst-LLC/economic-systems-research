.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_money_banking_data.py
	python3 python/01_money_bank_balance_sheet_analysis.py
	python3 python/02_liquidity_credit_sustainable_finance.py

r:
	Rscript r/money_banking_analysis.R

stata:
	stata -b do stata/money_banking_workflow.do || stata-mp -b do stata/money_banking_workflow.do || stata-se -b do stata/money_banking_workflow.do

sql:
	sqlite3 data/processed/money_banking_credit_intermediation.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/money_banking_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
