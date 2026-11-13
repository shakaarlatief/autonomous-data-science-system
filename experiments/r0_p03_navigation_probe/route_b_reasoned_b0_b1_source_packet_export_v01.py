"""Freeze 24 GPT-6 source-visible answer packets without any reference keys.

This is the exact source-quoted Checkpoint 921 data, restricted to B0/B1.
It is a model-facing context export only, not a new retrieval method.
"""
from __future__ import annotations

import json
from pathlib import Path
from hashlib import sha256

ROOT = Path("experiments/r0_p03_navigation_probe")
PRIOR = ROOT / "route_b_extractively_cited_answer_evidence_result_v01.json"
RESULT = ROOT / "route_b_reasoned_b0_b1_gold_free_source_packet_v01.json"
PRIOR_SIZE = 995317
PRIOR_SHA256 = "17f5bae16a96530008ea954e7145e3903e25386d83eeee7e69b983de91b908f8"
METHODS = ("B0_ORIGINAL", "B1_EXPOSED_SUBJECT_B0")


def packet() -> dict:
    original = PRIOR.read_bytes()
    if len(original) != PRIOR_SIZE or sha256(original).hexdigest() != PRIOR_SHA256:
        raise ValueError("Original source-only quoted evidence has changed")
    data = json.loads(original)
    cases = []
    for case in data["generated_source_only_answer_drafts"]:
        arm_inputs = []
        for name in METHODS:
            row, = [r for r in case["arm_drafts"] if r["arm"] == name]
            sources = []
            for i, source in enumerate(row["cited_source_records"], 1):
                sources.append({
                    "source_rank": i,
                    "path": source["path"],
                    "sha256": source["sha256"],
                    "original_cited_lines": [
                        {
                            "line": l["line"],
                            "original_source_line": l["original_source_line"],
                            "original_line_sha256": l["sha256_of_original_line"],
                        } for l in source["quotes"]
                    ],
                })
            arm_inputs.append({"arm": name, "sources": sources})
        cases.append({
            "id": case["id"], "question": case["question"],
            "arm_evidence": arm_inputs,
        })
    if len(cases) != 12 or any(len(c["arm_evidence"]) != 2 for c in cases):
        raise ValueError("Expected exactly twelve paired source-only questions")
    result = {
        "id": "R0_P03_ROUTE_B_GOLD_FREE_GPT6_B0_B1_EVIDENCE_PACKET_V01",
        "original_source_git_revision": data["original_source_git_pin"],
        "source_quoted_parent_sha256": PRIOR_SHA256,
        "question_count": len(cases),
        "arm_count": 2,
        "source_limit_per_arm": 3,
        "answerer_has_prior_context_exposure": True,
        "reference_answers_in_packet": False,
        "expected_reference_sources_in_packet": False,
        "source_only_question_packets": cases,
        "limitations": [
            "No source gold or reference answers are included in this exported file.",
            "The model author has previously seen related gold and source contents outside this file; packet isolation is not independent model isolation.",
            "All citation lines are copied from the frozen original Checkpoint921 source-quotation result, with original git sha and original line sha.",
            "Only the B0 and B1 exposed source-adjacent arms are included. Other seven-arm source evidence remains untouched.",
        ],
    }
    serial = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    return {"data": result, "bytes": serial.encode("utf8")}


def main() -> None:
    import argparse
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--output", action="store_true")
    flags = cli.parse_args()
    p = packet()
    if flags.output:
        with RESULT.open("xb") as f:
            f.write(p["bytes"])
    print(json.dumps({
        "size": len(p["bytes"]),
        "sha256": sha256(p["bytes"]).hexdigest(),
        "question_count": p["data"]["question_count"],
        "arm_count": p["data"]["arm_count"],
        "saved": flags.output,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
