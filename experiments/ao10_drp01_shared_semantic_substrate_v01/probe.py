from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_annotation(annotation: dict, corpus: dict, definitions: dict, schema: dict) -> list[str]:
    errors = []
    for key in schema["required_top"]:
        if key not in annotation:
            errors.append(f"missing top-level field: {key}")

    if annotation.get("base") != corpus["base"]:
        errors.append("annotation base mismatch")

    expected_paths = [x["path"] for x in corpus["carriers"]]
    anns = annotation.get("carrier_annotations", [])
    got_paths = [x.get("path") for x in anns]
    if got_paths != expected_paths:
        errors.append("carrier annotations must exactly match frozen corpus order")

    roles = set(definitions["roles"])
    statuses = set(definitions["governing_statuses"])

    for ca in anns:
        units = ca.get("units", [])
        if not units:
            errors.append(f"{ca.get('path')}: no units")
        anchors = set()
        for u in units:
            if u.get("anchor") in anchors:
                errors.append(f"{ca.get('path')}: duplicate unit anchor")
            anchors.add(u.get("anchor"))
            role = u.get("role")
            if role not in roles:
                errors.append(f"{ca.get('path')}: invalid role {role}")
            status = u.get("governing_status")
            if role == "GOVERNING":
                if status not in statuses:
                    errors.append(f"{ca.get('path')}: GOVERNING unit missing/invalid status")
            elif status is not None:
                errors.append(f"{ca.get('path')}: non-GOVERNING unit has governing status")

    expected_primitives = definitions["candidate_primitives"]
    panns = annotation.get("primitive_annotations", [])
    if [x.get("primitive") for x in panns] != expected_primitives:
        errors.append("primitive annotations must exactly match candidate primitive order")
    seam_ids = {s["id"] for s in definitions["seams"]}
    for pa in panns:
        got = [s.get("seam_id") for s in pa.get("seams", [])]
        if set(got) != seam_ids or len(got) != len(seam_ids):
            errors.append(f"{pa.get('primitive')}: must annotate all frozen seams exactly once")
        for sa in pa.get("seams", []):
            if sa.get("required_shared_meaning") and not sa.get("source_refs"):
                errors.append(f"{pa.get('primitive')}/{sa.get('seam_id')}: shared seam needs source refs")

    expected_neg = definitions["negative_controls"]
    neg = annotation.get("negative_controls", [])
    if [x.get("concept") for x in neg] != expected_neg:
        errors.append("negative controls must exactly match frozen order")

    return errors


def reviewer_metrics(annotation: dict, definitions: dict) -> dict:
    carrier_count = len(annotation["carrier_annotations"])
    total_units = 0
    irreducible = 0
    represented_carriers = 0
    over_four = 0
    path_misuse = 0

    for ca in annotation["carrier_annotations"]:
        units = ca["units"]
        total_units += len(units)
        irreducible += sum(bool(u.get("irreducibly_multirole")) for u in units)
        if all(u.get("role") in definitions["roles"] and not u.get("irreducibly_multirole") for u in units):
            represented_carriers += 1
        if len(units) > 4:
            over_four += 1
        if ca.get("path_used_as_identity_or_authority"):
            path_misuse += 1

    admitted = []
    primitive_failures = []
    for pa in annotation["primitive_annotations"]:
        seam_count = sum(bool(x["required_shared_meaning"]) for x in pa["seams"])
        if pa["admitted"]:
            admitted.append(pa["primitive"])
            if seam_count < 2:
                primitive_failures.append(f"{pa['primitive']}: admitted with <2 seams")
            if pa.get("semantic_conflict"):
                primitive_failures.append(f"{pa['primitive']}: admitted with semantic conflict")

    neg_admitted = [x["concept"] for x in annotation["negative_controls"] if x["admitted"]]

    return {
        "carrier_count": carrier_count,
        "total_units": total_units,
        "represented_carriers": represented_carriers,
        "role_representability": represented_carriers / carrier_count,
        "carriers_over_four_units": over_four,
        "carriers_over_four_units_rate": over_four / carrier_count,
        "irreducibly_multirole_units": irreducible,
        "irreducibly_multirole_unit_rate": (irreducible / total_units) if total_units else 1.0,
        "path_misuse_count": path_misuse,
        "admitted_primitives": admitted,
        "primitive_failures": primitive_failures,
        "negative_controls_admitted": neg_admitted,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--annotation-a", required=True)
    ap.add_argument("--annotation-b", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    corpus = load(ROOT / "corpus.json")
    definitions = load(ROOT / "definitions.json")
    schema = load(ROOT / "annotation_schema.json")
    a = load(Path(args.annotation_a))
    b = load(Path(args.annotation_b))

    errors_a = validate_annotation(a, corpus, definitions, schema)
    errors_b = validate_annotation(b, corpus, definitions, schema)
    if errors_a or errors_b:
        result = {"probe":"DRP-01","primary_class":"HARNESS_INVALID","errors":{"a":errors_a,"b":errors_b}}
        out = Path(args.output); out.mkdir(parents=True, exist_ok=True)
        (out/"result.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        print(json.dumps(result,sort_keys=True))
        return 2

    ma = reviewer_metrics(a, definitions)
    mb = reviewer_metrics(b, definitions)
    set_a, set_b = set(ma["admitted_primitives"]), set(mb["admitted_primitives"])
    union = set_a | set_b
    jaccard = len(set_a & set_b) / len(union) if union else 1.0

    each_pass = []
    for m in (ma, mb):
        each_pass.append(
            m["role_representability"] >= 0.90
            and m["carriers_over_four_units_rate"] <= 0.25
            and m["irreducibly_multirole_unit_rate"] <= 0.10
            and m["path_misuse_count"] == 0
            and not m["primitive_failures"]
            and not m["negative_controls_admitted"]
        )

    # Additional pre-result robustness criterion: independent admission decisions
    # should substantially agree, otherwise the shared-substrate boundary is too
    # ambiguous for a deterministic contract.
    agreement_pass = jaccard >= 0.80
    primary = "PASS" if all(each_pass) and agreement_pass else "AMEND"

    result = {
        "probe":"DRP-01",
        "protocol":"AO10-DRP-V01",
        "primary_class":primary,
        "reviewer_a":ma,
        "reviewer_b":mb,
        "admission_set_jaccard":jaccard,
        "admission_agreement_threshold":0.80,
        "reviewer_passes":each_pass,
    }
    out=Path(args.output); out.mkdir(parents=True,exist_ok=True)
    (out/"result.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"probe":"DRP-01","primary_class":primary,"admission_jaccard":jaccard,"reviewer_passes":each_pass},sort_keys=True))
    return 0 if primary=="PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
