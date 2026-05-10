.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_fiscal_policy_data.py
	python3 python/01_fiscal_position_tax_spending_analysis.py
	python3 python/02_multipliers_maintenance_local_resilience.py

r:
	Rscript r/fiscal_policy_analysis.R

stata:
	stata -b do stata/fiscal_policy_workflow.do || stata-mp -b do stata/fiscal_policy_workflow.do || stata-se -b do stata/fiscal_policy_workflow.do

sql:
	sqlite3 data/processed/fiscal_policy_taxation_public_investment.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/fiscal_policy_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
