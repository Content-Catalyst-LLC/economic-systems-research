.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_institutional_flow_data.py
	python3 python/01_institutional_flow_analysis.py
	python3 python/02_market_access_risk_reproduction.py

r:
	Rscript r/hfms_analysis.R

stata:
	stata -b do stata/hfms_workflow.do || stata-mp -b do stata/hfms_workflow.do || stata-se -b do stata/hfms_workflow.do

sql:
	sqlite3 data/processed/households_firms_markets_states.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/hfms_reproduction_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
