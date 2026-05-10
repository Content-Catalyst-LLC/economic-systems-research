.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_commons_governance_data.py
	python3 python/01_commons_stock_governance_analysis.py
	python3 python/02_compliance_access_institutional_integrity.py

r:
	Rscript r/commons_governance_analysis.R

stata:
	stata -b do stata/commons_governance_workflow.do || stata-mp -b do stata/commons_governance_workflow.do || stata-se -b do stata/commons_governance_workflow.do

sql:
	sqlite3 data/processed/commons_governance.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/commons_governance_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
