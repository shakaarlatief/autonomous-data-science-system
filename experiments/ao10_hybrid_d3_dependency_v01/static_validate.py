import ast,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def main():
    g=json.loads((ROOT/"graph.json").read_text())
    c=json.loads((ROOT/"negative_controls.json").read_text())
    assert g["probe_id"]=="HYBRID_D3_DEPENDENCY_V01"
    assert len(g["nodes"])==14
    assert len(c["controls"])==5
    ast.parse((ROOT/"check_dependency.py").read_text())
    assert not (ROOT/"result.json").exists()
    print("HYBRID_D3_STATIC_VALIDATION=PASS")
if __name__=="__main__": main()
