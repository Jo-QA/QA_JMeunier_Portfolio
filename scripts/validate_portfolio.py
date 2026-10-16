"""Fail on broken design links or inconsistent TC/H/R identifiers."""
import csv
import re
from pathlib import Path
from urllib.parse import unquote
from robot.api import get_model

ROOT = Path(__file__).resolve().parents[1]

def read_csv(name):
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))

cases = read_csv("docs/test-cases.csv")
requirements = read_csv("docs/requirements.csv")
risks = read_csv("docs/risks.csv")
trace = read_csv("docs/traceability.csv")
assert len(cases) == 24 and len({c["id"] for c in cases}) == 24
assert {c["id"] for c in cases} == {f"TC{i:02d}" for i in range(1, 25)}
assert len(requirements) == 14 and len(risks) == 8
req_ids = {r["id"] for r in requirements}
risk_ids = {r["id"] for r in risks}
for case in cases:
    assert case["hypothese"] in req_ids, case
    assert case["risque"] in risk_ids, case
    assert case["mode"] in {"Robot", "Manuel"}
    assert all(case[k].strip() for k in ("preconditions", "etapes", "attendu"))
for risk in risks:
    assert int(risk["score"]) == int(risk["impact"]) * int(risk["probabilite"])
for row in trace:
    expected = {c["id"] for c in cases if c["hypothese"] == row["hypothese"]}
    assert expected and expected == set(row["cas"].split()), row
    auto = {c["id"] for c in cases if c["hypothese"] == row["hypothese"] and c["mode"] == "Robot"}
    assert auto == (set() if row["robot"] == "AUCUN" else set(row["robot"].split())), row
model = get_model(str(ROOT / "tests/ui/saucedemo.robot"))
robot_tests = [test for section in model.sections for test in section.body if type(test).__name__ == "TestCase"]
assert len(robot_tests) == 12
by_id = {c["id"]: c for c in cases}
actual_ids = set()
for test in robot_tests:
    case_id = test.name.split()[0]
    actual_ids.add(case_id)
    tags = {value for statement in test.body if type(statement).__name__ == "Tags" for value in statement.values}
    assert {case_id, by_id[case_id]["hypothese"], by_id[case_id]["risque"], "regression"} <= tags, test.name
assert actual_ids == {c["id"] for c in cases if c["mode"] == "Robot"}
execution_file = ROOT / "docs/case-execution-status.csv"
if execution_file.exists():
    execution = read_csv("docs/case-execution-status.csv")
    assert {row["id"] for row in execution} == set(by_id) and len(execution) == 24
    assert all(row["statut"] in {"PASS", "FAIL", "BLOCKED", "NOT RUN", "SKIP"} for row in execution)
    assert all((ROOT / row["preuve"]).exists() for row in execution if row["statut"] == "PASS")
broken = []
for source in ROOT.rglob("*.md"):
    for target in re.findall(r"\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
        if "://" in target or target.startswith(("mailto:", "#")):
            continue
        path = unquote(target.split("#", 1)[0].strip("<>"))
        if path and not (source.parent / path).exists():
            broken.append(f"{source.relative_to(ROOT)} -> {target}")
assert not broken, "Broken links: " + "; ".join(broken)
print("PASS: 24 cases, 14 hypotheses, 8 risks, 12 Robot scenarios, traceability and local Markdown links")
