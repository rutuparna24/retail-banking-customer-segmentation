"""One-command pipeline.

    python run_all.py              # real UCI data (downloads it if missing)
    python run_all.py --synthetic  # offline smoke test with SYNTHETIC data (never quote its numbers)
"""
import argparse
import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent / "src"


def run(script: str, *args: str) -> None:
    print(f"\n=== {script} {' '.join(args)} ===")
    r = subprocess.run([sys.executable, str(SRC / script), *args], cwd=SRC)
    if r.returncode != 0:
        sys.exit(f"Step failed: {script}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--synthetic", action="store_true")
    synthetic = ap.parse_args().synthetic
    if synthetic:
        run("generate_synthetic_data.py")
        run("clean_data.py", "--synthetic")
    else:
        run("download_data.py")
        run("clean_data.py")
    for s in ["segment_customers.py", "build_database.py", "crosssell_analysis.py",
              "generate_insights.py", "build_excel_dashboard.py", "validate.py"]:
        run(s)
    print("\nDone. Open dashboard/Retail_Banking_Dashboard.xlsx and read reports/insights.md")
