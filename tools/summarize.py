"""Summarize a sanitized Prowler check aggregate without contacting AWS."""
import argparse
import csv
import json
from pathlib import Path

def summarize(rows):
    totals = {"PASS": 0, "FAIL": 0, "MANUAL": 0}
    for row in rows:
        status = row["status"]
        if status not in totals:
            raise ValueError(f"Unexpected status: {status}")
        count = int(row["count"])
        if count < 0:
            raise ValueError("Counts must be nonnegative")
        totals[status] += count
    evaluated = totals["PASS"] + totals["FAIL"]
    return {"results": totals, "evaluated": evaluated,
            "pass_rate_percent": round(100 * totals["PASS"] / evaluated, 2) if evaluated else None}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path(__file__).resolve().parents[1] / "evidence" / "after-check-summary.csv")
    args = parser.parse_args()
    with args.input.open(encoding="utf-8-sig", newline="") as stream:
        print(json.dumps(summarize(csv.DictReader(stream)), indent=2))

if __name__ == "__main__":
    main()
