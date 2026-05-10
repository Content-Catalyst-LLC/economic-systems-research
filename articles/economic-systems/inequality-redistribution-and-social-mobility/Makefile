.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_inequality_mobility_data.py
	python3 python/01_distribution_redistribution_analysis.py
	python3 python/02_mobility_security_systems_analysis.py

r:
	Rscript r/inequality_mobility_analysis.R

stata:
	stata -b do stata/inequality_mobility_workflow.do || stata-mp -b do stata/inequality_mobility_workflow.do || stata-se -b do stata/inequality_mobility_workflow.do

sql:
	sqlite3 data/processed/inequality_redistribution_social_mobility.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/inequality_mobility_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
