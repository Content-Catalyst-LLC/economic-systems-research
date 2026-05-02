#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--data-dir", default="data")
parser.add_argument("--output", default="outputs/source-audit.md")
args = parser.parse_args()

findings = []
for path in Path(args.data_dir).glob("*.csv"):
    with path.open(newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            for key, value in row.items():
                if "url" in key.lower() and value and not value.startswith(("http://", "https://")):
                    findings.append(f"- {path.name} row {i}: suspicious URL field {key}: {value}")

out = Path(args.output)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("# Source Audit\n\n" + ("\n".join(findings) if findings else "No suspicious URL fields found.\n"), encoding="utf-8")
print(f"Wrote audit to {out}")
