"""Freeze treatment-masked source-only review packets for a fresh reviewer.

The exporter accepts only the prior gold-free B0/B1 source packet plus
the original exposed GPT-6 prose responses, and omits self-classified
coverage, labels, original answer gold and previous performance results.
Each source line is verified in its original source packet. The
reviewer must not use any other repository material or internet source.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

BASE = Path("experiments/r0_p03_navigation_probe")
SOURCE = BASE / "route_b_reasoned_b0_b1_gold_free_source_packet_v01.json"
RESPONSES = BASE / "route_b_reasoned_b0_b1_gpt6_exposed_answers_v01.json"
SOURCE_BYTES = 155794
SOURCE_SHA = "60ec37969aa3319ce195353a6f9cddb2103640b0e4f748564e0be4a4d839b508"
RESPONSES_BYTES = 56283
RESPONSES_SHA = "5e8848f444fee4234fe885d9350e872393ac20f24a043c2347e615dafccdc388"
BATCH_SIZE = 4
N = 12
ARMS = ("B0_ORIGINAL","B1_EXPOSED_SUBJECT_B0")


def original_json(path: Path, size: int, digest: str) -> dict:
    data = path.read_bytes()
    if len(data) != size or sha256(data).hexdigest() != digest:
        raise ValueError("Original packet/answer SHA mismatch: " + str(path))
    return json.loads(data)


def exported_packets() -> list[dict]:
    p = original_json(SOURCE, SOURCE_BYTES, SOURCE_SHA)
    authored = original_json(RESPONSES, RESPONSES_BYTES, RESPONSES_SHA)
    cases = p["source_only_question_packets"]
    response_index = {(a["id"],a["arm"]):a for a in authored["paired_responses"]}
    assert len(cases) == N and len(response_index) == N * len(ARMS)
    out = []
    for start in range(0,N,BATCH_SIZE):
        entries = []
        for i in range(start,start+BATCH_SIZE):
            case = cases[i]
            arm_index = {a["arm"]:a for a in case["arm_evidence"]}
            assert set(arm_index) == set(ARMS)
            # Counterbalanced order. Reviewers are not told which arm is B0.
            order = (ARMS[0],ARMS[1]) if i%2 == 0 else (ARMS[1],ARMS[0])
            variants = []
            for j,arm in enumerate(order):
                record = response_index[(case["id"],arm)]
                available = arm_index[arm]["sources"]
                claims = []
                for k,claim in enumerate(record["claims"],1):
                    cites=[]
                    for ref in claim["citations"]:
                        source = available[ref["source_rank"]-1]
                        line = next((s for s in source["original_cited_lines"]
                                     if s["line"]==ref["line"]),None)
                        assert line is not None
                        assert (source["path"]==ref["path"]
                                and source["sha256"]==ref["original_source_sha256"]
                                and line["original_line_sha256"]==ref["original_line_sha256"])
                        cites.append({"source_rank":ref["source_rank"],"line":ref["line"]})
                    claims.append({"claim_id":f"C{k:02}","statement":claim["statement"],"cited_original_line_refs":cites})
                variants.append({
                    "variant":("VARIANT_A","VARIANT_B")[j],
                    "answer":record["answer"],
                    "claims":claims,
                    "available_evidence":[
                        {"source_rank":s["source_rank"],"path":s["path"],
                         "original_source_sha256":s["sha256"],
                         "lines":s["original_cited_lines"]}
                        for s in available
                    ]
                })
            entries.append({"case_id":case["id"],"question":case["question"],"variants":variants})
        out.append({
            "packet_id":f"R0_P03_ROUTE_B_MASKED_REVIEW_P{start+1:02}_TO_P{start+BATCH_SIZE:02}_V01",
            "case_span":[f"P{start+1:02}",f"P{start+BATCH_SIZE:02}"],
            "source_git_pin":p["original_source_git_revision"],
            "independent_reviewer_has_prior_original_gold":False,
            "contains_original_reference_answers":False,
            "contains_model_author_self_coverage":False,
            "treatment_labels_masked":True,
            "question_source_arms":2,
            "cases":entries,
            "review_protocol":"ROUTE_B_TREATMENT_MASKED_CLAIM_REVIEW_CONTRACT_V01.md",
            "warning":"Only these cited original source lines may support judgments; do not supplement from repository, outside context or previous answers."
        })
    return out


def output_bytes(d: dict) -> bytes:
    return (json.dumps(d,ensure_ascii=True,sort_keys=True,indent=2)+"\n").encode("utf8")


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",action="store_true")
    args=parser.parse_args()
    for batch in exported_packets():
        first,last=batch["case_span"]
        path=BASE/f"route_b_treatment_masked_claim_review_{first.lower()}_to_{last.lower()}_v01.json"
        data=output_bytes(batch)
        if args.output:
            with path.open("xb") as f:f.write(data)
        print(json.dumps({"path":str(path),"bytes":len(data),"sha256":sha256(data).hexdigest(),"cases":len(batch["cases"]),"saved":args.output}))
if __name__=="__main__":
    main()
