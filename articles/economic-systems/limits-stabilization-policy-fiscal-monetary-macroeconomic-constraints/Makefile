.PHONY: python r stata sql julia all clean

python:
	python3 python/00_fetch_and_build_constraints_panel.py
	python3 python/01_constraint_metrics.py
	python3 python/02_debt_and_monetary_constraints.py

r:
	Rscript r/stabilization_constraints_analysis.R

stata:
	stata -b do stata/stabilization_constraints_workflow.do || stata-mp -b do stata/stabilization_constraints_workflow.do || stata-se -b do stata/stabilization_constraints_workflow.do

sql:
	sqlite3 data/processed/stabilization_constraints.sqlite < sql/analysis_queries.sql

julia:
	julia --project=julia julia/debt_dynamics_constraints_model.jl

all: python r sql julia

clean:
	rm -f data/raw/*.csv
	rm -f data/processed/*.csv
	rm -f data/processed/*.sqlite
	rm -f outputs/figures/*.png
	rm -f outputs/tables/*.csv
	rm -f outputs/tables/*.txt
	rm -f *.log
	rm -f stata/*.log
