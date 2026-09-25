from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def classify_shape(event: dict, contract: dict) -> dict:
    a = contract["actionshape"]
    if event.get("source_type") != a["source_type"]:
        return {"classifiable": False, "route": a["fallback"], "shape": None}
    for field in a["required_fields"]:
        if not event.get(field):
            return {"classifiable": False, "route": a["fallback"], "shape": None}

    flags = event.get("derived_fixture_flags", {})
    consequences = [a["base_consequence"]]
    for rule in a["path_rules"]:
        if flags.get(rule["flag"], False):
            consequences.append(rule["name"])
    if event.get("commit") in a["exact_authority_transition_commits"]:
        consequences.append(a["authority_transition_shape"])

    shape = {
        "operation_family": a["base_operation_family"],
        "target_family": a["base_target_family"],
        "consequence_classes": sorted(set(consequences)),
    }
    return {"classifiable": True, "route": "DETERMINISTIC", "shape": shape}


def cooperative_evidence(event: dict) -> bool:
    f = event.get("derived_fixture_flags", {})
    return bool(
        f.get("touches_control_state")
        or f.get("touches_research_or_checkpoint")
        or f.get("publishes_collaboration_message")
    )


def classify_mediation(event: dict, contract: dict) -> dict:
    m = contract["mediation"]
    if event.get("ao_preflight_attested") is True:
        return {
            "class": "MEDIATED",
            "basis": "EXPLICIT_AO_PREFLIGHT_ATTESTATION",
            "preventive_claim_allowed": True,
        }

    if m["production_ao_preflight_available"] is False:
        if cooperative_evidence(event):
            return {
                "class": "COOPERATIVE",
                "basis": "NO_PRODUCTION_AO_PREFLIGHT_PLUS_DURABLE_PROJECT_PROTOCOL_RECORD",
                "preventive_claim_allowed": False,
            }
        return {
            "class": "UNMEDIATED",
            "basis": "NO_PRODUCTION_AO_PREFLIGHT_AND_NO_DURABLE_COOPERATIVE_RECORD",
            "preventive_claim_allowed": False,
        }

    return {
        "class": "UNKNOWN",
        "basis": "INSUFFICIENT_MEDIATION_EVIDENCE",
        "preventive_claim_allowed": False,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    corpus = load("corpus.json")
    contract = load("classification_contract.json")
    controls = load("controls.json")
    events = corpus["events"]

    shape_results = []
    mediation_results = []
    for event in events:
        s = classify_shape(event, contract)
        m = classify_mediation(event, contract)
        shape_results.append({"event_id": event["event_id"], "commit": event["commit"], **s})
        mediation_results.append({"event_id": event["event_id"], "commit": event["commit"], **m})

    n = len(events)
    classifiable = sum(x["classifiable"] for x in shape_results)
    high_total = n  # Every corpus item is a real Git history mutation.
    high_classified = classifiable

    provider_control_ok = True
    by_commit = {e["commit"]: e for e in events}
    provider_control_details = []
    for sha in controls["provider_invariance_samples"]:
        e = by_commit[sha]
        left = classify_shape({**e, "synthetic_provider": "provider-A"}, contract)
        right = classify_shape({**e, "synthetic_provider": "provider-B"}, contract)
        same = left["shape"] == right["shape"]
        provider_control_ok &= same
        provider_control_details.append({"commit": sha, "same_shape": same})

    malformed = classify_shape(controls["malformed_event"], contract)
    malformed_ok = (not malformed["classifiable"]) and malformed["route"] == "MODEL_ASSISTED_REVIEW"

    synth_med = classify_mediation(controls["synthetic_mediated_event"], contract)
    mediated_control_ok = synth_med["class"] == "MEDIATED" and synth_med["preventive_claim_allowed"]

    shape_coverage = classifiable / n
    high_coverage = high_classified / high_total
    drp05a_pass = (
        n >= 30
        and shape_coverage >= contract["thresholds"]["actionshape_coverage_min"]
        and high_coverage == contract["thresholds"]["high_consequence_coverage_required"]
        and provider_control_ok
        and malformed_ok
    )

    mediation_counts = {k: 0 for k in contract["mediation"]["classes"]}
    for x in mediation_results:
        mediation_counts[x["class"]] += 1
    mediation_classified = n - mediation_counts["UNKNOWN"]
    mediation_rate = mediation_classified / n
    mediated_share = mediation_counts["MEDIATED"] / n
    prevention_consistent = all(
        (x["class"] == "MEDIATED") == bool(x["preventive_claim_allowed"])
        for x in mediation_results
    )
    drp05b_pass = (
        mediation_rate >= contract["thresholds"]["mediation_classification_min"]
        and prevention_consistent
        and mediated_control_ok
    )
    subtype = (
        "PASS_DETECTIVE_FIRST"
        if drp05b_pass and mediated_share < contract["thresholds"]["detective_first_if_mediated_share_below"]
        else ("PASS" if drp05b_pass else None)
    )

    result = {
        "probe": "DRP-05a/DRP-05b",
        "protocol": "AO10-DRP-V01",
        "corpus_event_count": n,
        "drp05a": {
            "primary_class": "PASS" if drp05a_pass else "AMEND",
            "classifiable_count": classifiable,
            "coverage": shape_coverage,
            "high_consequence_count": high_total,
            "high_consequence_coverage": high_coverage,
            "provider_identity_invariance": provider_control_ok,
            "malformed_fallback_control": malformed_ok,
        },
        "drp05b": {
            "primary_class": "PASS" if drp05b_pass else "INCONCLUSIVE",
            "subtype": subtype,
            "classified_count": mediation_classified,
            "classification_rate": mediation_rate,
            "mediation_counts": mediation_counts,
            "mediated_share": mediated_share,
            "prevention_claims_consistent": prevention_consistent,
            "synthetic_mediated_control": mediated_control_ok,
        },
        "shape_results": shape_results,
        "mediation_results": mediation_results,
        "controls": {
            "provider_invariance": provider_control_details,
            "malformed": malformed,
            "synthetic_mediated": synth_med,
        },
    }

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    (out / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "events": n,
        "drp05a": result["drp05a"],
        "drp05b": result["drp05b"],
    }, sort_keys=True))
    return 0 if drp05a_pass and drp05b_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
