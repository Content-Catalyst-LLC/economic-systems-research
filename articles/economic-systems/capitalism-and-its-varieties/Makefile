.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_capitalism_varieties_data.py
	python3 python/01_regime_distribution_finance_analysis.py
	python3 python/02_institutions_crisis_sustainability_analysis.py

r:
	Rscript r/capitalism_varieties_analysis.R

stata:
	stata -b do stata/capitalism_varieties_workflow.do || stata-mp -b do stata/capitalism_varieties_workflow.do || stata-se -b do stata/capitalism_varieties_workflow.do

sql:
	sqlite3 data/processed/capitalism_and_its_varieties.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/capitalism_varieties_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
