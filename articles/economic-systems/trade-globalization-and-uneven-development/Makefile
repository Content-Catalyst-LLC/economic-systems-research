.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_trade_globalization_data.py
	python3 python/01_trade_value_chain_analysis.py
	python3 python/02_finance_region_labor_ecology_resilience_analysis.py

r:
	Rscript r/trade_globalization_analysis.R

stata:
	stata -b do stata/trade_globalization_workflow.do || stata-mp -b do stata/trade_globalization_workflow.do || stata-se -b do stata/trade_globalization_workflow.do

sql:
	sqlite3 data/processed/trade_globalization_uneven_development.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/trade_globalization_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
