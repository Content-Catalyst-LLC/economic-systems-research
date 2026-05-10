.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_externalities_public_goods_data.py
	python3 python/01_private_social_optimum_analysis.py
	python3 python/02_collective_provision_distribution_thresholds.py

r:
	Rscript r/externalities_public_goods_analysis.R

stata:
	stata -b do stata/externalities_public_goods_workflow.do || stata-mp -b do stata/externalities_public_goods_workflow.do || stata-se -b do stata/externalities_public_goods_workflow.do

sql:
	sqlite3 data/processed/externalities_public_goods_collective_provision.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/externalities_public_goods_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
