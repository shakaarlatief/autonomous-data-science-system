import importlib.util,json
from pathlib import Path
R=Path(__file__).resolve().parent
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main():
 j=lambda n:json.loads((R/n).read_text(encoding="utf-8"))
 a1=j("accepted_j1.json"); sf=j("source_facts.json"); c=j("evaluator_contract.json"); k=j("evaluator_key.json")["expected"]
 a=load("a",R/"evaluator_chatgpt_a.py").evaluate(a1,sf); b=load("b",R/"evaluator_claude_b.py").evaluate(a1,sf)
 f=c["required_output_fields"]; dif={}
 for x in f:
  if not (a.get(x)==b.get(x)==k.get(x)): dif[x]={"expected":k.get(x),"a":a.get(x),"b":b.get(x)}
 checks={"a_matches_key_exact":a==k,"b_matches_key_exact":b==k,"a_b_agree_exact":a==b,"a_field_order":list(a)==f,"b_field_order":list(b)==f,"key_field_order":list(k)==f,"a_current_sorted":a.get("current_effect_ids")==sorted(a.get("current_effect_ids",[])),"b_current_sorted":b.get("current_effect_ids")==sorted(b.get("current_effect_ids",[]))}
 ok=all(checks.values()) and not dif
 out={"schema_version":1,"probe_id":"HYBRID_D1_REAL_EVENT_REPLAY_V01","checks":checks,"material_field_differences":dif,"expected":k,"evaluator_a":a,"evaluator_b":b,"summary":{"material_field_count":len(f),"material_mismatch_field_count":len(dif),"all_material_match":ok,"raw_outcome":"D1_INTEGRATED_MICROREPLAY_PLAUSIBLE" if ok else "D1_MISMATCH_REQUIRES_RECONCILIATION"}}
 (R/"result.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out["summary"],sort_keys=True))
if __name__=="__main__":main()
