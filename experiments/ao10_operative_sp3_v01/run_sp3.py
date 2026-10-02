import json, subprocess, sys
from pathlib import Path

def run_json(cmd):
    p=subprocess.run(cmd,capture_output=True,text=True,check=True)
    return json.loads(p.stdout)

if __name__=="__main__":
    root=Path(__file__).resolve().parent
    fixtures=json.load(open(root/"predicate_fixtures.json",encoding="utf-8"))
    expected={x["fixture_id"]:x["expected"] for x in fixtures["fixtures"]}
    a=run_json([sys.executable,str(root/"predicate_engine_a.py"),str(root/"predicate_fixtures.json")])
    b=run_json([sys.executable,str(root/"predicate_engine_b.py"),str(root/"predicate_fixtures.json")])
    coverage=run_json([sys.executable,str(root/"coverage_validator.py"),str(root)])
    result={
      "fixture_count":len(expected),
      "implementation_a_matches_expected":a==expected,
      "implementation_b_matches_expected":b==expected,
      "implementations_identical":a==b,
      "positive_realizer_count":len(coverage["positives"]),
      "positive_realizers_all_valid":all(coverage["positives"].values()),
      "negative_control_count":len(coverage["negatives"]),
      "negative_controls_all_fail":all(v is False for v in coverage["negatives"].values()),
      "coverage":coverage,
      "implementation_a":a,
      "implementation_b":b,
      "expected":expected
    }
    out=root/"SP3_RESULT_V01.json"
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k not in {"implementation_a","implementation_b","expected"}},sort_keys=True))
