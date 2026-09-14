#!/usr/bin/env python3
"""Candidate 01 falsification-first shadow prototype V0.1.

This is research-only mechanism code. It reads the frozen semantic fixture, never
becomes a live ADS authority surface, and deliberately does not read the separate
expected-result oracle.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

EXPECTED_FIXTURE_SHA256 = "77ffecc278995ef03130d962f863d46ccebac41d446de7099cc666750e8b66f7"
DEFAULT_FIXTURE = Path("docs/research/project_knowledge_candidate_01_shadow_v01/SHADOW_FIXTURE_V01.json")
DEFAULT_OUTPUT = Path("docs/research/project_knowledge_candidate_01_shadow_v01/RESULTS_V01.json")

DIRECTIONAL_RELATIONS = {"SUPPLEMENT", "SPECIALIZE", "CORRECT", "REPLACE"}
IRREDUCIBLE_SET_FACT_KEYS = {
    "all_members_required",
    "set_effective_from",
    "set_effective_to",
    "set_conflict_state",
    "set_ordering",
}


def canonical_json_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_fixture(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    digest = sha256_bytes(raw)
    if digest != EXPECTED_FIXTURE_SHA256:
        raise RuntimeError(
            f"fixture hash mismatch: expected {EXPECTED_FIXTURE_SHA256}, got {digest}"
        )
    return json.loads(raw.decode("utf-8")), digest


def procedure_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {p["source_id"]: p for p in fixture["governing_procedures"]}


def scope_matches(procedure_scope: dict[str, Any], requested_scope: dict[str, Any]) -> bool:
    for key, requested_value in requested_scope.items():
        value = procedure_scope.get(key)
        if value is None:
            continue
        if value == "global":
            continue
        if value != requested_value:
            return False
    return True


def procedures_for_action(
    fixture: dict[str, Any], action: str, requested_scope: dict[str, Any]
) -> list[dict[str, Any]]:
    return [
        p
        for p in fixture["governing_procedures"]
        if p["state"] == "current"
        and p["scope"].get("action") == action
        and scope_matches(p["scope"], requested_scope)
    ]


def constraint_signature(item: dict[str, Any]) -> tuple[Any, Any, Any]:
    return item.get("kind"), item.get("semantic_key"), item.get("semantic_value")


def validate_procedure_drift(procedure: dict[str, Any]) -> list[dict[str, Any]]:
    contract = {
        item["constraint_id"]: item
        for item in procedure["structured_action_contract"]["constraints"]
    }
    findings: list[dict[str, Any]] = []
    for assertion in procedure.get("prose_assertions", []):
        cid = assertion["constraint_id"]
        normative = contract.get(cid)
        if normative is None:
            findings.append(
                {
                    "code": "PROSE_CONTRACT_MISSING_NORMATIVE_CONSTRAINT",
                    "constraint_id": cid,
                }
            )
            continue
        if constraint_signature(assertion) != constraint_signature(normative):
            findings.append(
                {
                    "code": "PROSE_CONTRACT_SEMANTIC_MISMATCH",
                    "constraint_id": cid,
                }
            )
    return findings


def apply_procedure_mutation(
    procedure: dict[str, Any], mutation: dict[str, Any]
) -> dict[str, Any]:
    result = copy.deepcopy(procedure)
    changes = mutation["changes"]
    if "prose_text_append" in changes:
        result["prose_text"] += changes["prose_text_append"]
    if "prose_text_replace" in changes:
        repl = changes["prose_text_replace"]
        result["prose_text"] = result["prose_text"].replace(repl["old"], repl["new"])
    if "prose_assertion_add" in changes:
        result["prose_assertions"].append(copy.deepcopy(changes["prose_assertion_add"]))
    if "prose_assertion_replace" in changes:
        replacement = copy.deepcopy(changes["prose_assertion_replace"])
        cid = replacement["constraint_id"]
        result["prose_assertions"] = [
            replacement if item["constraint_id"] == cid else item
            for item in result["prose_assertions"]
        ]
    return result


def relation_edges(procedures: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    edges: list[dict[str, Any]] = []
    ids = {p["source_id"] for p in procedures}
    for procedure in procedures:
        for relation in procedure.get("source_relations", []):
            if relation.get("relation") in DIRECTIONAL_RELATIONS and relation.get("target") in ids:
                edges.append(
                    {
                        "owner": procedure["source_id"],
                        "relation": relation["relation"],
                        "target": relation["target"],
                    }
                )
    return edges


def evidence_for_participants(
    fixture: dict[str, Any], participants: list[str]
) -> dict[str, Any] | None:
    target = set(participants)
    for evidence in fixture["authority_evidence"]:
        if set(evidence["participants"]) == target:
            return evidence
    return None


def review_receipt_for_evidence(
    fixture: dict[str, Any], evidence_id: str
) -> dict[str, Any] | None:
    for receipt in fixture["admission_review_receipts"]:
        if receipt["evidence_id"] == evidence_id and receipt.get("review_completed") is True:
            return receipt
    return None


def evaluate_joint_authority_admission(
    fixture: dict[str, Any], procedures: list[dict[str, Any]]
) -> dict[str, Any]:
    participants = [p["source_id"] for p in procedures]
    edges = relation_edges(procedures)
    evidence = evidence_for_participants(fixture, participants)

    # J1: overlapping current canonical sources with non-redundant mandatory content.
    semantic_keys = [
        c["semantic_key"]
        for p in procedures
        for c in p["structured_action_contract"]["constraints"]
    ]
    j1 = (
        len(procedures) >= 2
        and all(p["authority_class"] == "canonical" and p["state"] == "current" for p in procedures)
        and len(set(semantic_keys)) == len(semantic_keys)
    )

    # J2: no natural directional ownership is available and the participants are semantically symmetric.
    roles = [p.get("semantic_role") for p in procedures]
    roles_from_evidence = evidence.get("participant_roles", []) if evidence else []
    symmetric_roles = (
        bool(roles_from_evidence)
        and len(set(roles_from_evidence)) == 1
        and all(role == roles_from_evidence[0] for role in roles_from_evidence)
    ) or (bool(roles) and None not in roles and len(set(roles)) == 1)
    j2 = not edges and symmetric_roles

    # J3: reviewed evidence contains an irreducible set-level fact beyond ordinary applicability.
    set_facts = evidence.get("set_facts", {}) if evidence else {}
    j3 = any(key in IRREDUCIBLE_SET_FACT_KEYS for key in set_facts)

    # J4: in this bounded prototype, an all-members-required or explicit set-conflict/effective fact
    # is independently relevant to governing-set activation rather than merely descriptive overlap.
    j4 = bool(
        set_facts.get("all_members_required")
        or "set_conflict_state" in set_facts
        or "set_ordering" in set_facts
        or "set_effective_from" in set_facts
    )

    # J5: explicit completed review receipt exists for the exact evidence record.
    receipt = review_receipt_for_evidence(fixture, evidence["evidence_id"]) if evidence else None
    j5 = receipt is not None

    admitted = all((j1, j2, j3, j4, j5))
    if admitted:
        return {
            "admission_status": "JOINT_AUTHORITY_ADMITTED",
            "members": participants,
            "joint_authority_objects_created": 1,
            "joint_authority_id": "JA-" + "-".join(participants),
            "gate": {"J1": j1, "J2": j2, "J3": j3, "J4": j4, "J5": j5, "J6": True},
        }

    if edges:
        return {
            "admission_status": "SOURCE_OWNED_DERIVED_CLOSURE",
            "members": participants,
            "joint_authority_objects_created": 0,
            "natural_direction_edges": edges,
            "gate": {"J1": j1, "J2": j2, "J3": j3, "J4": j4, "J5": j5, "J6": True},
        }

    return {
        "admission_status": "UNRESOLVED",
        "members": participants,
        "joint_authority_objects_created": 0,
        "gate": {"J1": j1, "J2": j2, "J3": j3, "J4": j4, "J5": j5, "J6": True},
    }


def resolve_authority_case(
    fixture: dict[str, Any], action: str, requested_scope: dict[str, Any]
) -> dict[str, Any]:
    procedures = procedures_for_action(fixture, action, requested_scope)
    sources = [p["source_id"] for p in procedures]
    admission = evaluate_joint_authority_admission(fixture, procedures)
    result = {
        "governing_sources": sources,
        "joint_authority_objects_created": admission["joint_authority_objects_created"],
        "admission_status": admission["admission_status"],
        "gate": admission["gate"],
    }
    if "members" in admission:
        result["members"] = admission["members"]
    edges = admission.get("natural_direction_edges", relation_edges(procedures))
    if len(edges) == 1:
        result["natural_direction_owner"] = edges[0]["owner"]
    if admission.get("joint_authority_id"):
        result["joint_authority_id"] = admission["joint_authority_id"]
    return result


def activated_constraints(
    fixture: dict[str, Any], action: str, requested_scope: dict[str, Any]
) -> list[dict[str, Any]]:
    procedures = procedures_for_action(fixture, action, requested_scope)
    constraints = [
        c
        for procedure in procedures
        for c in procedure["structured_action_contract"]["constraints"]
    ]
    return sorted(constraints, key=lambda item: (item["order"], item["constraint_id"]))


def check_action_attempt(
    activated: list[dict[str, Any]], emitted_constraint_ids: list[str]
) -> dict[str, Any]:
    activated_ids = [c["constraint_id"] for c in activated]
    omitted = [cid for cid in activated_ids if cid not in emitted_constraint_ids]
    positions = {cid: i for i, cid in enumerate(emitted_constraint_ids)}
    violation_ids: set[str] = set()
    present = [cid for cid in activated_ids if cid in positions]
    for i, left in enumerate(present):
        for right in present[i + 1 :]:
            if positions[left] > positions[right]:
                violation_ids.add(left)
                violation_ids.add(right)
    order_violations = [cid for cid in activated_ids if cid in violation_ids]
    return {
        "status": "FAIL_VISIBLE" if omitted or order_violations else "PASS",
        "omitted": omitted,
        "order_violations": order_violations,
        "emitted_constraint_ids": emitted_constraint_ids,
    }


def affected_views(fixture: dict[str, Any], changed_source_ids: list[str]) -> list[str]:
    changed = set(changed_source_ids)
    affected: list[str] = []
    for manifest in fixture["derived_view_manifests"]:
        if changed.intersection(manifest.get("depends_on_source_ids", [])):
            affected.append(manifest["view_id"])
    return affected


def apply_identity_events(
    fixture: dict[str, Any], passive_prefix: int
) -> tuple[dict[str, list[str]], dict[str, str], int]:
    redirects: dict[str, list[str]] = {}
    carriers = {item["semantic_id"]: item["carrier"] for item in fixture["identity_initial"]}
    for semantic_id in carriers:
        redirects[semantic_id] = [semantic_id]

    events = list(fixture["identity_events"]) + list(
        fixture["identity_passive_move_history"][:passive_prefix]
    )
    events.sort(key=lambda item: item["recorded_order"])

    for event in events:
        kind = event["type"]
        if kind == "MOVE":
            sid = event["semantic_id"]
            redirects.setdefault(sid, [sid])
            carriers[sid] = event["to_carrier"]
        elif kind == "MERGE":
            output = event["output"]
            redirects[output] = [output]
            carriers[output] = event["output_carrier"]
            for sid in event["inputs"]:
                redirects[sid] = [output]
        elif kind == "REVERSE_MERGE":
            source = event["input"]
            outputs = list(event["outputs"])
            redirects[source] = outputs
            for sid in outputs:
                redirects[sid] = [sid]
                carriers[sid] = event["output_carriers"][sid]
        elif kind == "SPLIT":
            source = event["input"]
            outputs = list(event["outputs"])
            redirects[source] = outputs
            for sid in outputs:
                redirects[sid] = [sid]
                carriers[sid] = event["output_carriers"][sid]
        else:
            raise RuntimeError(f"unknown identity event type: {kind}")

    def resolve(sid: str, trail: tuple[str, ...] = ()) -> list[str]:
        if sid in trail:
            raise RuntimeError(f"identity redirect cycle: {' -> '.join(trail + (sid,))}")
        targets = redirects.get(sid, [sid])
        if targets == [sid]:
            return [sid]
        resolved: list[str] = []
        for target in targets:
            for item in resolve(target, trail + (sid,)):
                if item not in resolved:
                    resolved.append(item)
        return resolved

    all_ids = sorted(redirects)
    index = {sid: resolve(sid) for sid in all_ids}
    current_ids = {target for targets in index.values() for target in targets}
    current_carriers = {sid: carriers[sid] for sid in sorted(current_ids) if sid in carriers}
    return index, current_carriers, len(events)


def normal_identity_lookup(index: dict[str, list[str]], semantic_id: str) -> tuple[list[str], int]:
    return list(index[semantic_id]), 1


def current_view_payload(fixture: dict[str, Any], passive_prefix: int) -> dict[str, Any]:
    identity_index, current_carriers, _ = apply_identity_events(fixture, passive_prefix)
    publish = resolve_authority_case(fixture, "publish_release", {"environment": "public_repo"})
    deploy = resolve_authority_case(fixture, "deploy_service", {"region": "eu"})
    joint = resolve_authority_case(fixture, "approve_joint_release", {"domain": "jx"})
    return {
        "authority": {
            "publish_release": publish,
            "deploy_service_eu": deploy,
            "approve_joint_release_jx": joint,
        },
        "contract": [
            c["constraint_id"]
            for c in activated_constraints(fixture, "publish_release", {"environment": "public_repo"})
        ],
        "identity": {"targets": identity_index, "current_carriers": current_carriers},
    }


def run_probe(fixture: dict[str, Any], fixture_sha: str) -> dict[str, Any]:
    procedures = procedure_map(fixture)

    drift = {"baseline_findings": validate_procedure_drift(procedures["P1"])}
    for mutation in fixture["procedure_mutations"]:
        mutated = apply_procedure_mutation(procedures[mutation["source_id"]], mutation)
        drift[mutation["mutation_id"]] = validate_procedure_drift(mutated)

    authority = {
        "publish_release": resolve_authority_case(
            fixture, "publish_release", {"environment": "public_repo"}
        ),
        "deploy_service_eu": resolve_authority_case(
            fixture, "deploy_service", {"region": "eu"}
        ),
        "approve_joint_release_jx": resolve_authority_case(
            fixture, "approve_joint_release", {"domain": "jx"}
        ),
    }

    activated = activated_constraints(
        fixture, "publish_release", {"environment": "public_repo"}
    )
    action_results = {
        "activated_constraint_ids": [c["constraint_id"] for c in activated]
    }
    for attempt in fixture["action_attempts"]:
        action_results[attempt["attempt_id"]] = check_action_attempt(
            activated, attempt["emitted_constraint_ids"]
        )

    change = fixture["change_scenarios"][0]
    incremental = {
        "change_id": change["change_id"],
        "incremental_source_scans": len(change["changed_source_ids"]),
        "authoritative_source_locations_touched": list(change["changed_source_ids"]),
        "refreshed_views": affected_views(fixture, change["changed_source_ids"]),
    }

    scale_results: dict[str, Any] = {}
    digests: list[str] = []
    for prefix in fixture["protocol"]["scale_prefix_lengths"]:
        index, current_carriers, identity_event_records = apply_identity_events(fixture, prefix)
        payload = current_view_payload(fixture, prefix)
        digest = sha256_bytes(canonical_json_bytes(payload))
        digests.append(digest)
        targets, lookup_steps = normal_identity_lookup(index, "S-M")
        scale_results[str(prefix)] = {
            "full_rebuild_source_records": len(fixture["governing_procedures"])
            + identity_event_records,
            "identity_event_records": identity_event_records,
            "normal_identity_lookup_steps": lookup_steps,
            "sample_lookup": {"semantic_id": "S-M", "targets": targets},
            "current_view_digest": digest,
            "identity_index_entries": len(index),
            "current_carrier_count": len(current_carriers),
        }

    final_index, final_carriers, _ = apply_identity_events(fixture, 200)

    return {
        "schema_version": 1,
        "probe_id": "PKA-C01-SHADOW-PROBE-V01",
        "candidate_id": fixture["candidate_id"],
        "fixture_id": fixture["fixture_id"],
        "fixture_sha256": fixture_sha,
        "shadow_only": True,
        "implementation_reads_oracle": False,
        "profile_surface": [
            "GOVERNING_PROCEDURE",
            "JOINT_AUTHORITY_DECLARATION",
            "IDENTITY_TRANSITION",
            "DERIVED_VIEW_MANIFEST",
        ],
        "contract_drift": drift,
        "authority_admission": authority,
        "action_contract": action_results,
        "refresh_and_rebuild": {
            "incremental": incremental,
            "scales": scale_results,
            "current_view_digest_equal_across_scales": len(set(digests)) == 1,
        },
        "identity": {
            "current_targets": final_index,
            "current_carriers": final_carriers,
            "normal_lookup_model": "precomputed_current_target_index",
        },
        "metrics": {
            "joint_authority_objects_created": sum(
                item["joint_authority_objects_created"] for item in authority.values()
            ),
            "generated_locations_refreshed_for_change": len(incremental["refreshed_views"]),
            "authoritative_source_locations_touched_for_change": len(
                incremental["authoritative_source_locations_touched"]
            ),
            "constraint_ids_activated": len(action_results["activated_constraint_ids"]),
            "implementation_profile_types": 4,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()

    fixture, fixture_sha = load_fixture(args.fixture)
    result = run_probe(fixture, fixture_sha)
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if not args.no_write:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
