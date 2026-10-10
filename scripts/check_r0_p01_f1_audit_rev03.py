"""Fail-closed *structural* guard for the unfrozen R0-P01 F1 audit inventory.

The guard reads only committed reference-source blobs and generated public
candidate documents. It does not load any owner proof, import the V01/V02
owner runner, or claim approval of a semantic mapping or an F1/F2 freeze.
"""
from __future__ import annotations

import collections
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

try:
    from scripts import r0_p01_audit_inventory_rev03 as norm
except ModuleNotFoundError:
    import r0_p01_audit_inventory_rev03 as norm

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("docs/research/r0_p01_successor_design")
INVENTORY = BASE / "R0_P01_F1_NORMATIVE_AUDIT_INVENTORY_REV03_UNFROZEN.json"
BATCHES = BASE / "R0_P01_F1_NORMATIVE_AUDIT_BATCH_PLAN_REV03_UNFROZEN.json"
CATALOG = BASE / "R0_P01_F1_TEST_CATALOGUE_REV03_UNFROZEN.json"
SEEDS = BASE / "R0_P01_F1_NUMERIC_AND_B02_ORACLE_SEEDS_UNFROZEN.json"
PRIOR = BASE / "R0_P01_Q0_REQUIREMENTS_TRACE_REV02_UNFROZEN.json"
NEW_TESTS = {
    "T-NATIVE-PROMPT-VISIBILITY", "T-RP-TAIL-AFTER-CRASH",
    "T-AGENT-PRESIGN-CHECK-CLASSIFICATION",
    "T-VOLUME-SELECTED-TIE", "T-SELECT-EXACT-10",
    "T-SELECT-EXACT-15", "T-VIABILITY-MEDIAN-60",
    "T-VIABILITY-SMALL-120", "T-VIABILITY-NULL",
    "T-B02-4-OF-5-DENIED", "T-B02-POST-PASS-DENIED",
    "T-B02-CAP-DENIED",
}

def read_json(root: Path, relative: Path) -> dict[str, Any]:
    def no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        v: dict[str, Any] = {}
        for k, x in pairs:
            if k in v:
                raise ValueError(f"duplicate JSON field: {k}")
            v[k] = x
        return v
    return json.loads((root / relative).read_text(encoding="utf-8"),
                      object_pairs_hook=no_duplicates)

def validate(
    actual: dict[str, Any], baseline: dict[str, Any], batches: dict[str, Any],
    catalog: dict[str, Any], seeds: dict[str, Any], prior: dict[str, Any],
) -> list[str]:
    """Check equality to committed normative inputs and honesty of pending state."""
    problems: list[str] = []
    expect = {x["id"]:x for x in baseline["units"]}
    seen = {x.get("id"):x for x in actual.get("units", [])}
    if len(seen) != len(actual.get("units", [])) or set(seen) != set(expect):
        problems.append("missing, duplicate or extra inherited/approved normative unit")
    for key, ref in expect.items():
        item = seen.get(key)
        if item is None:
            continue
        for field in ("source_id","text_sha256","section","heading_context",
                      "line_start","line_end","header_context","json_path",
                      "root_status","inherited"):
            if item.get(field)!=ref.get(field):
                problems.append(f"unit source mismatch {key}: {field}")
        review = item.get("review",{})
        if review.get("status")=="APPROVED":
            if not review.get("reviewer") or not review.get("review_message"):
                problems.append(f"unsubstantiated approved reviewer {key}")
            if item.get("inherited") and review.get("disposition") not in (
                "INHERITED_UNCHANGED","SUPERSEDED_BY_REV04","NOT_APPLICABLE_TO_SUCCESSOR"
            ):
                problems.append(f"missing inherited disposition {key}")
        elif review.get("status")!="PENDING_INDEPENDENT_SEMANTIC_AUDIT":
            problems.append(f"unknown review disposition {key}")
    if actual.get("source_sha256")!=baseline.get("source_sha256"):
        problems.append("frozen or accepted source bytes changed")
    if actual.get("policy_root_classification")!=baseline.get("policy_root_classification"):
        problems.append("incomplete or altered top-level policy root classification")
    if actual.get("policy_non_normative_reason")!=baseline.get("policy_non_normative_reason"):
        problems.append("policy nonnormative justification changed without review")
    if actual.get("table_syntax_context_exclusions")!=baseline.get("table_syntax_context_exclusions"):
        problems.append("table headers, separators or excluded source lines changed")
    if len(actual.get("units", [])) < 700:
        problems.append("inherited control, fixture and result corpus absent")
    control = collections.defaultdict(list)
    for x in actual.get("units", []):
        if x.get("source_id")=="V01_CONTROLS" and x.get("control_definition_candidate"):
            control[x.get("section")].append(x)
    if sorted(control)!=list(range(1,14)):
        problems.append("thirteen inherited security control definitions not anchored")
    else:
        for k, group in control.items():
            if not all(f"C{k:02d}" in x.get("candidate_requirement_ids",[]) for x in group):
                problems.append(f"control {k} not mapped to inherited definition")
    if actual.get("F1_frozen") is not False or actual.get("F2_frozen") is not False:
        problems.append("F1/F2 falsely frozen")
    if actual.get("owner_attempt_002_authorized") is not False:
        problems.append("owner execution falsely authorized")

    groups = batches.get("audit_batches", [])
    flat = [key for g in groups for key in g.get("unit_ids",[])]
    if len(flat)!=len(set(flat)) or set(flat)!=set(seen):
        problems.append("audit batches fail exact-once source-unit coverage")
    if batches.get("batch_count")!=len(groups) or batches.get("total_units")!=len(flat):
        problems.append("batch count/total inconsistent")
    if any(len(g["unit_ids"])>batches.get("batch_size_ceiling",0) for g in groups):
        problems.append("bounded audit batch size exceeded")
    for group in groups:
        raw=("\n".join(group.get("unit_ids",[]))+"\n").encode("utf-8")
        if group.get("unit_id_list_sha256")!=hashlib.sha256(raw).hexdigest():
            problems.append(f"auditor batch identity changed: {group.get('batch_id')}")
    if batches.get("F1_frozen") or batches.get("owner_execution_authorized"):
        problems.append("audit batches falsely authorize freeze/owner action")

    original = {x["test_id"] for x in prior["test_catalogue"]}
    tests = catalog.get("tests", [])
    keyed = {x.get("test_id"):x for x in tests}
    if len(keyed)!=len(tests) or set(keyed)!=original|NEW_TESTS:
        problems.append("test catalogue missing, duplicated or unplanned IDs")
    allowed_layers = {"PURE","WINDOWS_NATIVE","OWNER_MACHINE_MANUAL",
                      "INTEGRATED_SYNTHETIC","BROWSER_VIRTUAL","SCORER_ORACLE"}
    for key,row in keyed.items():
        if row.get("layer") not in allowed_layers or not row.get("expected_value_origin"):
            problems.append(f"test layer or expected-value origin absent: {key}")
        if not row.get("must_not_derive_from"):
            problems.append(f"test target independence unspecified: {key}")
        if row.get("expected_vector_or_decision_id") is not None or row.get("status")!="PLANNED_NOT_IMPLEMENTED":
            problems.append(f"false test execution/oracle claim {key}")
    for key in ["T-SSH-PROMPT","T-SSH-ABORT","T-ATOMIC-SNAPSHOTS","T-CTRL-C-NODE"]:
        if keyed.get(key,{}).get("layer")!="WINDOWS_NATIVE":
            problems.append(f"wrong native test layer {key}")
    for key in ["T-NATIVE-PROMPT-VISIBILITY","T-TARGET-MACHINE-SYNTHETIC"]:
        if keyed.get(key,{}).get("layer")!="OWNER_MACHINE_MANUAL":
            problems.append(f"missing owner-machine observation {key}")
    if catalog.get("independent_expected_vectors_exist") is not False:
        problems.append("unimplemented oracle falsely claimed available")
    if seeds.get("F1_frozen") or seeds.get("owner_attempt_002_authorized"):
        problems.append("oracle seeds falsely frozen or owner authorized")
    if seeds.get("selected_arm_volume_median_ceiling_exact")!="5400/97":
        problems.append("exact selected-arm volume boundary wrong")
    for row in seeds.get("selection_and_volume_seeds",[]):
        arm=row.get("frozen_selection")
        if arm not in ("A","B"):
            problems.append(f"bad selector row {row.get('id')}")
            continue
        minutes=Fraction(row[arm]["median_small_seconds"])*Fraction(97,60)
        if row.get("selected_projected_minutes_exact")!=str(minutes):
            problems.append(f"selected-arm projected volume computation wrong {row.get('id')}")
        if row.get("volume_gate_90min_pass") != (minutes<=90):
            problems.append(f"selected-arm volume gate wrong {row.get('id')}")
    if len(seeds.get("viability_eligibility_seeds",[]))<12 or len(seeds.get("B02_claim_stopping_seeds",[]))<12:
        problems.append("numeric/B02 seed coverage unexpectedly truncated")
    return problems

def check(root: Path = ROOT) -> list[str]:
    """Validate the complete proposal without owner-run or cryptographic calls."""
    if hashlib.sha256(b"abc").hexdigest()!="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad":
        return ["SHA-256 known-answer gate failed"]
    actual=read_json(root,INVENTORY)
    baseline=norm.inventory(root)
    batches=read_json(root,BATCHES)
    catalog=read_json(root,CATALOG)
    seeds=read_json(root,SEEDS)
    prior=read_json(root,PRIOR)
    issues=validate(actual,baseline,batches,catalog,seeds,prior)
    if batches.get("source_inventory_sha256") != hashlib.sha256((root/INVENTORY).read_bytes()).hexdigest():
        issues.append("batch plan source inventory hash differs")
    for source,key in (("REV04_CONTRACT","contract"),("REV04_POLICY","policy")):
        if actual["source_sha256"].get(source)!=actual["approved_source_sha256"].get(key):
            issues.append(f"accepted {source} byte hash differs")
    return issues

if __name__=="__main__":
    issues=check()
    if issues:
        for x in issues:
            print("R0_P01_F1_AUDIT_GUARD_FAIL:",x)
        raise SystemExit(1)
    obj=read_json(ROOT,INVENTORY)
    b=read_json(ROOT,BATCHES)
    c=read_json(ROOT,CATALOG)
    print(f"R0_P01_F1_AUDIT_STRUCTURE=PASS units={len(obj['units'])} "
          f"batches={len(b['audit_batches'])} planned_tests={len(c['tests'])}")
    print("F1_SEMANTIC_APPROVAL=NOT_GIVEN; F2=UNFROZEN; OWNER_ATTEMPT_002=NOT_AUTHORIZED")
