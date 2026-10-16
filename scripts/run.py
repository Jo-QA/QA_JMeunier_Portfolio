"""Run from any working directory; preserve Robot's failure exit code."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys
from robot import run

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--suite", choices=["smoke", "regression"], default="regression")
parser.add_argument("--output", type=Path, default=ROOT / "results" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
parser.add_argument("--dry-run", action="store_true", help="Syntax/keyword check only; no browser or UI assertions")
args = parser.parse_args()
if args.output.exists() and any(args.output.iterdir()):
    parser.error("Output directory must be empty. Choose a new path to preserve previous evidence.")
args.output.mkdir(parents=True, exist_ok=True)
sys.exit(run(str(ROOT / "tests" / "ui"), include=args.suite,
             outputdir=str(args.output.resolve()), dryrun=args.dry_run,
             xunit="xunit.xml", loglevel="INFO", name="SauceDemo QA Portfolio"))
