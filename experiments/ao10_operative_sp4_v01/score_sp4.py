import importlib.util, json, sys
from pathlib import Path

def metrics(truth,pred):
    tp=sum(1 for k,v in truth.items() if v=="LEAK" and pred[k]=="LEAK")
    fn=sum(1 for k,v in truth.items() if v=="LEAK" and pred[k]=="NO_LEAK")
    fp=sum(1 for k,v in truth.items() if v=="NO_LEAK" and pred[k]=="LEAK")
    tn=sum(1 for k,v in truth.items() if v=="NO_LEAK" and pred[k]=="NO_LEAK")
    recall=tp/(tp+fn) if tp+fn else None
    precision=tp/(tp+fp) if tp+fp else None
    specificity=tn/(tn+fp) if tn+fp else None
    return {"tp":tp,"fn":fn,"fp":fp,"tn":tn,"recall":recall,"precision":precision,"specificity":specificity}

def load_baseline(path):
    spec=importlib.util.spec_from_file_location("sp4_baseline",path)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

if __name__=="__main__":
    root=Path(__file__).resolve().parent
    annotation_path=Path(sys.argv[1])
    packet=json.load(open(root/"reviewer_packet.json",encoding="utf-8"))
    key=json.load(open(root/"evaluator_key.json",encoding="utf-8"))
    ann=json.load(open(annotation_path,encoding="utf-8"))
    ids=[x["item_id"] for x in packet["items"]]
    truth={x["item_id"]:x["label"] for x in key["labels"]}
    if len(ann.get("annotations",[]))!=len(ids):
        raise SystemExit("annotation count mismatch")
    if len({x["item_id"] for x in ann["annotations"]})!=len(ids):
        raise SystemExit("duplicate/missing annotation ids")
    pred={x["item_id"]:x["label"] for x in ann["annotations"]}
    if set(pred)!=set(ids):
        raise SystemExit("annotation ids mismatch")
    detector_metrics=metrics(truth,pred)
    b=load_baseline(root/"lexical_baseline.py")
    baseline_pred={x["item_id"]:b.classify(x["text"]) for x in packet["items"]}
    baseline_metrics=metrics(truth,baseline_pred)
    recall=detector_metrics["recall"]
    precision=detector_metrics["precision"]
    if recall>=0.90 and precision>=0.75:
        result_class="SP4_DETECTOR_PLAUSIBLE"
    elif recall>=0.80 and precision>=0.60:
        result_class="SP4_AMEND"
    else:
        result_class="SP4_STRUCTURAL_FALLBACK_REQUIRED"
    out={
      "schema_version":1,
      "probe_id":"OPERATIVE-SP4-V01",
      "detector":ann["detector"],
      "detector_metrics":detector_metrics,
      "lexical_baseline_metrics":baseline_metrics,
      "result_class":result_class,
      "thresholds":{"plausible_recall":0.90,"plausible_precision":0.75,"amend_recall":0.80,"amend_precision":0.60},
      "detector_predictions":pred,
      "baseline_predictions":baseline_pred
    }
    (root/"SP4_RESULT_V01.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in out.items() if k not in {"detector_predictions","baseline_predictions"}},sort_keys=True))
