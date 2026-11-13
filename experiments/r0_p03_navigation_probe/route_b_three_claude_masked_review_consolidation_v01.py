"""Retrospective mechanical consolidation of three sealed Claude source-only reviews.

The three prior reviewer outputs and treatment-masked packets were already
committed before this aggregator was authored. This is an analysis of their
recorded evidence, not a prospective blinded evaluation, independent answer
gold, true/false authority decision or formal R0-P03 architecture score.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
from typing import Any

from experiments.r0_p03_navigation_probe.route_b_primary_b0_baseline_execution_v01 import original_contents

ROOT = Path("experiments/r0_p03_navigation_probe")
REVIEW_DIR = Path("docs/model_collaboration/threads/MC-0030/messages")
OUTPUT = ROOT / "route_b_three_claude_masked_review_consolidation_result_v01.json"
PIN = "47ed6344a9153dcf366769e95722840fbf1a8f8b"
ARMS = ("B0_ORIGINAL", "B1_EXPOSED_SUBJECT_B0")
PACKET_AND_REVIEW = (
    ("route_b_treatment_masked_claim_review_p01_to_p04_v01.json",59983,"6f76a9d8cb11beb64e0b8493230bf24e3b6f87920c562368ac14e2cd458bdb3b",
     "067_claude_r0_p03_masked_b0_b1_p01_p04_claim_review.md",26561,"528c386865b311f899e2d41c98e29ccfdb879a01e8b2553433aa7c6524ec336f"),
    ("route_b_treatment_masked_claim_review_p05_to_p08_v01.json",62864,"0615031623d83c7bb6aba74588d18fa9fca5877d72828bd735f5f503b1751623",
     "069_claude_r0_p03_masked_b0_b1_p05_p08_claim_review.md",31976,"aac51653f23d85dba319a5bcd8c78410a880a840d5d2b85240edda2bd30eb42c"),
    ("route_b_treatment_masked_claim_review_p09_to_p12_v01.json",62152,"e63afe2ebe79fc7e6ec3751d61971c6794d71cc1904057f2ee7aa691f9636804",
     "071_claude_r0_p03_masked_b0_b1_p09_p12_claim_review.md",39129,"4b3d77528e9aef20ef0e38ad5b3d38990757d4cb9d7796efdc782fc9ea1764c1"),
)
SOURCE_PACKET = ("route_b_reasoned_b0_b1_gold_free_source_packet_v01.json",155794,"60ec37969aa3319ce195353a6f9cddb2103640b0e4f748564e0be4a4d839b508")
ORIGINAL_ANSWERS = ("route_b_reasoned_b0_b1_gpt6_exposed_answers_v01.json",56283,"5e8848f444fee4234fe885d9350e872393ac20f24a043c2347e615dafccdc388")
GRADES = ("FULLY_SUPPORTED","PARTIALLY_SUPPORTED","PROPER_ABSTENTION","MISLEADING_OR_UNSUPPORTED")
CLAIM_GRADES = ("SUPPORTED","PARTIAL","UNSUPPORTED")


def frozen_bytes(path: Path, size: int, digest: str) -> bytes:
    raw=path.read_bytes()
    if len(raw)!=size or sha256(raw).hexdigest()!=digest:
        raise ValueError(f"Original immutable input changed: {path}")
    return raw


def parse_review(raw: bytes) -> dict[tuple[str,str],dict]:
    """Parse only the 8 original variant sections, not narrative summary tallies."""
    content=raw.decode("utf8")
    blocks=re.split(r"(?=^### P\d\d VARIANT_[AB]\s*$)",content,flags=re.M)
    parsed={}
    for block in blocks:
        header=re.match(r"^### (P\d\d) (VARIANT_[AB])\b",block)
        if not header:continue
        key=(header.group(1),header.group(2))
        if key in parsed:raise ValueError(f"Duplicate review section {key}")
        claim_rows=[]
        for line in block.splitlines():
            if not re.match(r"^\|\s*C\d\d",line):continue
            fields=[s.strip() for s in line.strip().strip("|").split("|")]
            claim_id=re.match(r"^(C\d\d)\b",fields[0])
            if claim_id is None:raise ValueError("Malformed original claim")
            eligible=[
                re.match(r"^\*{0,2}(SUPPORTED|PARTIAL|UNSUPPORTED)\b",field)
                for field in fields[1:5]
            ]
            grades=[x.group(1) for x in eligible if x]
            if len(grades)!=1:raise ValueError(f"Ambiguous review verdict: {key}, {line}")
            claim_rows.append({"claim_id":claim_id.group(1),"verdict":grades[0]})
        found=re.findall(
            r"(?m)^\*\*Whole(?:-answer grade:| answer:\*\*|-answer category:\*\*)\s*[\x60*]*\s*"
            r"(FULLY_SUPPORTED|PARTIALLY_SUPPORTED|PROPER_ABSTENTION|MISLEADING_OR_UNSUPPORTED)",
            block,
        )
        if len(found)!=1 or not claim_rows:
            raise ValueError(f"Review grade/claims not uniquely parseable for {key}")
        parsed[key]={"grade":found[0],"claims":claim_rows}
    if len(parsed)!=8:
        raise ValueError(f"Expected eight reviewed variants per report, found {len(parsed)}")
    return parsed


def run() -> dict[str,Any]:
    prior=json.loads(frozen_bytes(ROOT/SOURCE_PACKET[0],*SOURCE_PACKET[1:]))
    authored=json.loads(frozen_bytes(ROOT/ORIGINAL_ANSWERS[0],*ORIGINAL_ANSWERS[1:]))
    question_packet={case["id"]:case for case in prior["source_only_question_packets"]}
    authored_map={(a["id"],a["arm"]):a for a in authored["paired_responses"]}
    if len(question_packet)!=12 or len(authored_map)!=24:
        raise ValueError("Original 12x2 source and model output pairing changed")
    if prior["original_source_git_revision"]!=PIN:
        raise ValueError("Original source Git revision drift")
    full=[]
    original_packets=[]
    unique_paths=set()
    for packet_name,packet_size,packet_sha,review_name,review_size,review_sha in PACKET_AND_REVIEW:
        packet=json.loads(frozen_bytes(ROOT/packet_name,packet_size,packet_sha))
        parsed=parse_review(frozen_bytes(REVIEW_DIR/review_name,review_size,review_sha))
        original_packets.append({"review_packet":packet_name,"review_sha256":review_sha,
                                 "review_file":review_name,"packet_sha256":packet_sha,
                                 "case_ids":[c["case_id"] for c in packet["cases"]]})
        for case in packet["cases"]:
            case_id=case["case_id"]
            earlier=question_packet[case_id]
            if case["question"]!=earlier["question"]:
                raise ValueError(f"Frozen original question changed: {case_id}")
            order=ARMS if int(case_id[1:])%2==1 else ARMS[::-1]
            if len(case["variants"])!=2:
                raise ValueError("Review case lost one source treatment")
            for i,masked in enumerate(case["variants"]):
                variant=masked["variant"]
                if variant!=("VARIANT_A","VARIANT_B")[i]:
                    raise ValueError("Masked source order changed")
                key=(case_id,variant)
                if key not in parsed:raise ValueError(f"Missing reviewer judgment: {key}")
                arm=order[i]
                expected=authored_map[(case_id,arm)]
                context=next(x for x in earlier["arm_evidence"] if x["arm"]==arm)
                if masked["answer"]!=expected["answer"]:
                    raise ValueError(f"Original authored model answer altered {key}")
                if len(masked["available_evidence"])!=len(context["sources"]):
                    raise ValueError("Reviewer source budget or original source roster changed")
                for row,original in zip(masked["available_evidence"],context["sources"]):
                    if not (row["source_rank"]==original["source_rank"]
                            and row["path"]==original["path"]
                            and row["original_source_sha256"]==original["sha256"]
                            and row["lines"]==original["original_cited_lines"]):
                        raise ValueError(f"Review packet original citations drift {key}")
                    unique_paths.add(row["path"])
                if [c["claim_id"] for c in masked["claims"]]!=[
                    f"C{j:02d}" for j in range(1,len(expected["claims"])+1)]:
                    raise ValueError("Claim ID order not frozen")
                for numbered,original_claim in zip(masked["claims"],expected["claims"]):
                    if numbered["statement"]!=original_claim["statement"]:
                        raise ValueError("Model author claim changed")
                    ref_expected=[{"source_rank":r["source_rank"],"line":r["line"]} for r in original_claim["citations"]]
                    if numbered["cited_original_line_refs"]!=ref_expected:
                        raise ValueError("Claim citations changed")
                evaluated=parsed[key]
                if [x["claim_id"] for x in evaluated["claims"]]!=[
                    x["claim_id"] for x in masked["claims"]]:
                    raise ValueError("Reviewer omitted/repeated claim ID")
                full.append({
                    "question_id":case_id,
                    "variant":variant,
                    "original_method_revealed_after_all_three_reviews":arm,
                    "original_author_self_coverage":expected["coverage"],
                    "independent_model_excerpt_entailment_grade":evaluated["grade"],
                    "claim_verdicts":evaluated["claims"],
                    "original_source_paths":[s["path"] for s in masked["available_evidence"]],
                    "input_review_file":review_name,
                    "not_independent_answer_gold":True,
                    "current_operative_authority_test_outcome":"NO_FALSE_ASSERTIONS_REPORTED_BY_CLAUDE"
                })
        if set(parsed)!={(c["case_id"],v["variant"]) for c in packet["cases"] for v in c["variants"]}:
            raise ValueError("Reviewer parsed case set disagrees with frozen packet")
    if len(full)!=24 or len({(c["question_id"],c["original_method_revealed_after_all_three_reviews"]) for c in full})!=24:
        raise ValueError("Combined original twelve x two comparison incomplete")
    # Verify that every citation was an original line from the frozen Git horizon,
    # not just self-consistent text and hashes within the reviewer packet.
    git=original_contents(sorted(unique_paths))
    source_line_count=0
    for c in original_packets:
        packet=json.loads((ROOT/c["review_packet"]).read_bytes())
        for case in packet["cases"]:
            for variant in case["variants"]:
                for source in variant["available_evidence"]:
                    b=git[source["path"]]
                    if sha256(b).hexdigest()!=source["original_source_sha256"]:
                        raise ValueError("Original Git full-source SHA mismatch")
                    original_lines=b.decode("utf8").splitlines()
                    for line in source["lines"]:
                        source_line_count+=1
                        idx=line["line"]
                        if not 1<=idx<=len(original_lines) or original_lines[idx-1]!=line["original_source_line"]:
                            raise ValueError("Source text not original pinned Git line")
                        if sha256(original_lines[idx-1].encode("utf8")).hexdigest()!=line["original_line_sha256"]:
                            raise ValueError("Original Git source line hash mismatch")
    summary={}
    for key in ("all",)+ARMS:
        records=full if key=="all" else [x for x in full if x["original_method_revealed_after_all_three_reviews"]==key]
        summary[key]={
            "answers":len(records),
            "whole_answer_grade_counts":{g:sum(r["independent_model_excerpt_entailment_grade"]==g for r in records) for g in GRADES},
            "claim_verdict_counts":{v:sum(x["verdict"]==v for r in records for x in r["claim_verdicts"]) for v in CLAIM_GRADES},
            "author_self_assessment_counts":{x:sum(r["original_author_self_coverage"]==x for r in records) for x in ("SUPPORTED","PARTIAL","ABSTAIN")},
        }
    if (summary["all"]["whole_answer_grade_counts"]!={"FULLY_SUPPORTED":20,"PARTIALLY_SUPPORTED":2,
                                                          "PROPER_ABSTENTION":2,"MISLEADING_OR_UNSUPPORTED":0}
         or summary["all"]["claim_verdict_counts"]!={"SUPPORTED":45,"PARTIAL":2,"UNSUPPORTED":0}):
        raise ValueError("All-original-review totals do not match source-sealed reviewer evidence")
    return {
        "id":"R0_P03_ROUTE_B_THREE_SEPARATE_CLAUDE_MASKED_SOURCE_REVIEW_CONSOLIDATION_V01",
        "method":"RETROSPECTIVE_DESCRIPTIVE_RECONCILIATION_OF_THREE_PREVIOUSLY_SEALED_REVIEWS",
        "source_git_horizon":PIN,
        "prior_exposed_author_gpt6_answer_sha256":ORIGINAL_ANSWERS[2],
        "prior_gold_free_source_packet_sha256":SOURCE_PACKET[2],
        "source_authorship_independent":False,
        "source_excerpt_judgments_separate_model":True,
        "reviewer_fresh_sessions_reported":3,
        "different_reviewer_model_families":1,
        "reviewer_has_full_original_source":False,
        "independently_authored_reference_gold":False,
        "formal_original_R0_P03_scored":False,
        "selected_physical_architecture":False,
        "reviewed_and_sealed_input_files":original_packets,
        "original_git_source_paths_verified":len(unique_paths),
        "original_git_exact_source_lines_verified_with_multiplicity":source_line_count,
        "complete_per_question_unmasked_after_reviewer_submission":full,
        "counts":summary,
        "interpretation_limits":[
            "Claude graded entailment against the limited source lines already retrieved and selected by the exposed author, not correctness against complete independently judged source truth.",
            "Three fresh Claude Code sessions reused one model family; no inter-rater across different models, no independent reference answer, and project/runtime context exposure was disclosed.",
            "The question origin, 12-query test selection, B1 metadata authoring and answer construction were nonindependent; grades do not constitute formal primary 10/12 score.",
            "A proper abstention means the evidence did not allow a full answer; it is not a successful complete answer. A partially supported answer is not a full answer.",
            "The unmasking and aggregation happened after all three original reviewer messages were fixed; no retroactive model input changes, answer changes or altered source budgets occurred.",
            "A zero false-operative-authority finding within 24 author responses and selected excerpts is not the original formal zero-false-authority independent-gold gate.",
            "The B4 original pretrained neural encoder and qualified common V03-native substrate, original neutral nine-case legacy cohort and heldout maintenance F1 remain untested formally.",
            "R0-P03 Research513/559/576 outcome remains INCOMPLETE; no physical target selection, migration or current owner-governance change is authorized."
        ],
    }


def main() -> None:
    import argparse
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",action="store_true")
    args=p.parse_args()
    result=run()
    b=(json.dumps(result,ensure_ascii=True,sort_keys=True,indent=2)+"\n").encode("utf8")
    if args.output:
        with OUTPUT.open("xb") as f:f.write(b)
    print(json.dumps({"result_bytes":len(b),"result_sha256":sha256(b).hexdigest(),
                      "original_git_source_lines":result["original_git_exact_source_lines_verified_with_multiplicity"],
                      "counts":result["counts"],"output_created":args.output},sort_keys=True,indent=2))


if __name__=="__main__":
    main()
