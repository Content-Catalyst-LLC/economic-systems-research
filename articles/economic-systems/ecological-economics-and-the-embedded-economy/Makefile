.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_ecological_economics_data.py
	python3 python/01_throughput_scale_burden_analysis.py
	python3 python/02_resilience_embeddedness_postgrowth_analysis.py

r:
	Rscript r/ecological_economics_analysis.R

stata:
	stata -b do stata/ecological_economics_workflow.do || stata-mp -b do stata/ecological_economics_workflow.do || stata-se -b do stata/ecological_economics_workflow.do

sql:
	sqlite3 data/processed/ecological_economics_embedded_economy.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/ecological_economics_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
