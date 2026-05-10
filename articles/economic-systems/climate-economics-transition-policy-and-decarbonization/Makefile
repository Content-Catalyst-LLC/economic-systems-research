.PHONY: python r stata sql julia all clean

python:
	python3 python/00_build_climate_economics_data.py
	python3 python/01_emissions_policy_investment_analysis.py
	python3 python/02_damage_justice_implementation_analysis.py

r:
	Rscript r/climate_economics_analysis.R

stata:
	stata -b do stata/climate_economics_workflow.do || stata-mp -b do stata/climate_economics_workflow.do || stata-se -b do stata/climate_economics_workflow.do

sql:
	sqlite3 data/processed/climate_economics_transition_policy_decarbonization.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/climate_economics_model.jl

all: python r sql julia

clean:
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
