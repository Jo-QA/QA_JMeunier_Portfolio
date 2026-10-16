"""Generate a factual ledger from a REAL Robot output.xml, never from dry-run."""
import argparse
import csv
import json
from pathlib import Path
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument("run_directory", type=Path)
args = parser.parse_args()
path = args.run_directory
root = ET.parse(path / "output.xml").getroot()
if any((m.text or "").find("Dry run") >= 0 for m in root.iter("msg")) or not (path / "environment.json").exists():
    raise SystemExit("Refusing to label dry-run/unproven browser run as real execution")
rows=[]
for test in root.findall(".//test"):
    status=test.find("status")
    rows.append({"case_id":test.attrib["name"].split()[0],"test":test.attrib["name"],
                 "status":status.attrib["status"],"start_robot_local":status.get("start", ""),
                 "elapsed_seconds":status.get("elapsed", ""),"message":status.text or ""})
with (path / "execution.csv").open("w",encoding="utf-8",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
summary={"source":"output.xml", "real_browser_metadata":"environment.json", "total":len(rows),
         "passed":sum(r["status"]=="PASS" for r in rows),"failed":sum(r["status"]=="FAIL" for r in rows),
         "skipped":sum(r["status"]=="SKIP" for r in rows), "dry_run":False}
(path / "summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary))
