# Replication Notes

## Reproducing the Workflow

From the article folder:

```bash
make python
make r
make sql
make julia
```

## Python Dependencies

Install with:

```bash
python3 -m pip install -r requirements.txt
```

## R Dependencies

Install with:

```r
source("r/packages.R")
```

## Stata

The Stata workflow is optional and requires a licensed Stata installation. It assumes the Python workflow has already produced the core CSV files.

## Julia

The Julia workflow uses `CSV`, `DataFrames`, and `LinearAlgebra`. Instantiate the Julia environment from the `julia/` folder if desired.
