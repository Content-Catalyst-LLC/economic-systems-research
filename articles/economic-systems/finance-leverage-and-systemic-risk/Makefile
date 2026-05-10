.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_finance_leverage_data.py
	python3 python/01_leverage_collateral_fire_sale_analysis.py
	python3 python/02_network_household_macroprudential_sustainability.py

r:
	Rscript r/finance_leverage_analysis.R

stata:
	stata -b do stata/finance_leverage_workflow.do || stata-mp -b do stata/finance_leverage_workflow.do || stata-se -b do stata/finance_leverage_workflow.do

sql:
	sqlite3 data/processed/finance_leverage_systemic_risk.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/finance_leverage_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
