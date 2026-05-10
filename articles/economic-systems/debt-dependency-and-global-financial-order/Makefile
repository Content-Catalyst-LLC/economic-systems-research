.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_debt_dependency_data.py
	python3 python/01_debt_external_vulnerability_analysis.py
	python3 python/02_adjustment_restructuring_sustainable_finance_analysis.py

r:
	Rscript r/debt_dependency_analysis.R

stata:
	stata -b do stata/debt_dependency_workflow.do || stata-mp -b do stata/debt_dependency_workflow.do || stata-se -b do stata/debt_dependency_workflow.do

sql:
	sqlite3 data/processed/debt_dependency_global_financial_order.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/debt_dependency_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
