#!/usr/bin/env python3
"""Candidate 01 broader operational shadow prototype V0.2.

Research-only executable model over the frozen V0.2 fixture. The implementation
reads the fixture only. The separate oracle is reserved for tests and must not be
referenced here.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

EXPECTED_FIXTURE_SHA256 = "6daefddd448ead145281d56da8325925cb82c71fc57418283ef21c65418ec486"
DEFAULT_FIXTURE = Path("docs/research/project_knowledge_candidate_01_shadow_v02/SHADOW_OPERATIONAL_FIXTURE_V02.json")
DEFAULT_OUTPUT = Path("docs/research/project_knowledge_candidate_01_shadow_v02/RESULTS_V02.json")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_digest(value: Any) -> str:
    data = (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")
    return sha256_bytes(data)


def load_fixture(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    digest = sha256_bytes(raw)
    if digest != EXPECTED_FIXTURE_SHA256:
        raise RuntimeError(f"fixture hash mismatch: expected {EXPECTED_FIXTURE_SHA256}, got {digest}")
    return json.loads(raw.decode("utf-8")), digest


def workstream_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["workstream_id"]: item for item in fixture["workstreams"]}


def dependencies_completed(ws: dict[str, Any], mapping: dict[str, dict[str, Any]]) -> bool:
    return all(mapping[dep]["state"] == "COMPLETED" for dep in ws.get("depends_on", []))


def return_condition_met(ws: dict[str, Any], signals: dict[str, Any], mapping: dict[str, dict[str, Any]]) -> bool:
    condition = ws.get("return_condition")
    if not condition:
        return False
    if "signal" in condition:
        return signals.get(condition["signal"]) == condition.get("equals")
    if condition.get("all_dependencies_completed") is True:
        return dependencies_completed(ws, mapping)
    return False


def route_projection(fixture: dict[str, Any], signals: dict[str, Any]) -> dict[str, Any]:
    mapping = workstream_map(fixture)
    activated_from_pause = [
        ws["workstream_id"]
        for ws in fixture["workstreams"]
        if ws["state"] == "PAUSED" and return_condition_met(ws, signals, mapping)
    ]
    effective_active = {
        ws["workstream_id"]
        for ws in fixture["workstreams"]
        if ws["state"] == "ACTIVE"
    } | set(activated_from_pause)

    children: dict[str, list[str]] = {}
    for ws in fixture["workstreams"]:
        parent = ws.get("parent")
        if parent:
            children.setdefault(parent, []).append(ws["workstream_id"])

    roots = sorted(
        wid for wid in effective_active if mapping[wid].get("parent") not in effective_active
    )
    active_leaves = sorted(
        wid
        for wid in effective_active
        if not any(child in effective_active for child in children.get(wid, []))
    )

    # Baseline mandatory route follows the single current-anchor branch rather than pulling
    # every paused/triggered sibling into ordinary bootstrap.
    mandatory_route: list[str] = []
    current = roots[0] if roots else None
    while current:
        mandatory_route.append(current)
        active_children = [
            child
            for child in children.get(current, [])
            if child in effective_active and mapping[child]["state"] == "ACTIVE"
        ]
        if not active_children:
            break
        active_children.sort(key=lambda wid: (mapping[wid].get("current_anchor") is None, wid))
        current = active_children[0]

    return {
        "mandatory_route": mandatory_route,
        "active_leaves": active_leaves,
        "signal_activated_from_pause": sorted(activated_from_pause),
        "paused_visible": [ws["workstream_id"] for ws in fixture["workstreams"] if ws["state"] == "PAUSED"],
        "blocked_visible": [ws["workstream_id"] for ws in fixture["workstreams"] if ws["state"] == "BLOCKED"],
        "multiple_dependencies": {
            ws["workstream_id"]: list(ws["depends_on"])
            for ws in fixture["workstreams"]
            if len(ws.get("depends_on", [])) > 1
        },
    }


def recover_transition(fixture: dict[str, Any], transition_id: str) -> dict[str, Any]:
    intent = next(item for item in fixture["transition_intents"] if item["transition_id"] == transition_id)
    receipts = {
        item["step_id"]: item
        for item in fixture["durable_action_receipts"]
        if item["transition_id"] == transition_id and item["status"] == "COMPLETED"
    }
    ordered_steps = [step["step_id"] for step in intent["steps"]]
    return {
        "transition_id": transition_id,
        "completed_steps": [sid for sid in ordered_steps if sid in receipts],
        "pending_steps": [sid for sid in ordered_steps if sid not in receipts],
        "blind_replay_required": False,
        "receipt_evidence": [receipts[sid]["evidence_ref"] for sid in ordered_steps if sid in receipts],
    }


def evaluate_workstream_update(fixture: dict[str, Any], attempt: dict[str, Any]) -> dict[str, Any]:
    original = copy.deepcopy(workstream_map(fixture)[attempt["workstream_id"]])
    if attempt["expected_revision"] != original["revision"]:
        return {
            "status": "STALE_REVISION",
            "actual_revision": original["revision"],
            "mutation_applied": False,
            "state_after": original,
        }
    updated = copy.deepcopy(original)
    updated.update(attempt["patch"])
    updated["revision"] += 1
    return {
        "status": "APPLIED",
        "actual_revision": original["revision"],
        "new_revision": updated["revision"],
        "mutation_applied": True,
        "current_anchor": updated.get("current_anchor"),
        "state_after": updated,
    }


def evaluate_consolidation(candidate: dict[str, Any]) -> dict[str, Any]:
    required = list(candidate["must_preserve_unit_ids"])
    disposition_ids = {item["unit_id"] for item in candidate["unit_dispositions"]}
    missing = [unit_id for unit_id in required if unit_id not in disposition_ids]
    invalid_latent = [
        item["unit_id"]
        for item in candidate["unit_dispositions"]
        if item["disposition"] == "INTENTIONALLY_LATENT_WITH_RECOVERABLE_SOURCE" and not item.get("source_ref")
    ]
    missing += [unit_id for unit_id in invalid_latent if unit_id not in missing]
    return {
        "status": "FIDELITY_FAIL" if missing else "FIDELITY_PASS",
        "missing_units": missing,
    }


def promotion_results(fixture: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    candidates = {item["candidate_id"]: item for item in fixture["consolidation_candidates"]}
    captures = {item["capture_id"]: item for item in fixture["captures"]}
    results: dict[str, Any] = {}
    promoted: list[dict[str, Any]] = []
    for request in fixture["promotion_requests"]:
        candidate = candidates[request["candidate_id"]]
        fidelity = evaluate_consolidation(candidate)
        if request["review_status"] != "ACCEPTED":
            results[request["promotion_id"]] = {"status": "PROMOTION_BLOCKED_REVIEW"}
            continue
        if fidelity["status"] != "FIDELITY_PASS":
            results[request["promotion_id"]] = {"status": "PROMOTION_BLOCKED_FIDELITY"}
            continue
        latent_units = [
            item["unit_id"]
            for item in candidate["unit_dispositions"]
            if item["disposition"] == "INTENTIONALLY_LATENT_WITH_RECOVERABLE_SOURCE"
        ]
        record = {
            "semantic_id": request["target_semantic_id"],
            "authority_class": "canonical",
            "state": "current",
            "subject": "operational-qualification",
            "provenance_capture_ids": list(candidate["source_capture_ids"]),
            "recoverable_latent_units": latent_units,
            "source_refs": sorted(
                {
                    source_ref
                    for capture_id in candidate["source_capture_ids"]
                    for source_ref in captures[capture_id]["source_refs"]
                }
            ),
        }
        promoted.append(record)
        results[request["promotion_id"]] = {
            "status": "PROMOTED",
            "semantic_id": record["semantic_id"],
            "provenance_capture_ids": record["provenance_capture_ids"],
            "recoverable_latent_units": latent_units,
        }
    return results, promoted


def narrative_candidate_captures(fixture: dict[str, Any]) -> list[str]:
    return [
        claim["claim_id"]
        for claim in fixture["generated_narrative_input"]["claims"]
        if not claim.get("supported_by_existing_canonical", False)
    ]


def navigation_index(fixture: dict[str, Any]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}
    for declaration in fixture["navigation_declarations"]:
        for subject in declaration["subjects"]:
            index.setdefault(subject, []).append(declaration["source_id"])
    return {subject: sorted(source_ids) for subject, source_ids in sorted(index.items())}


def current_state_core(fixture: dict[str, Any], promoted: list[dict[str, Any]]) -> dict[str, Any]:
    accepted = [item["semantic_id"] for item in fixture["canonical_knowledge_seed"]] + [
        item["semantic_id"] for item in promoted
    ]
    return {
        "active_workstreams": [ws["workstream_id"] for ws in fixture["workstreams"] if ws["state"] == "ACTIVE"],
        "paused_workstreams": [ws["workstream_id"] for ws in fixture["workstreams"] if ws["state"] == "PAUSED"],
        "blocked_workstreams": [ws["workstream_id"] for ws in fixture["workstreams"] if ws["state"] == "BLOCKED"],
        "accepted_knowledge": sorted(accepted),
    }


def build_derived_views(fixture: dict[str, Any], promoted: list[dict[str, Any]]) -> dict[str, Any]:
    baseline_signals = fixture["workstream_signals"][0]["values"]
    return {
        "ROUTING_CURRENT": route_projection(fixture, baseline_signals),
        "CURRENT_STATE_CORE": current_state_core(fixture, promoted),
        "NAVIGATION_INDEX": navigation_index(fixture),
    }


def private_record_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["private_dependency_id"]: item for item in fixture["private_records"]}


def public_record_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["public_id"]: item for item in fixture["public_records"]}


def evaluate_private_scenario(fixture: dict[str, Any], scenario: dict[str, Any]) -> dict[str, Any]:
    public = public_record_map(fixture)[scenario["public_record_id"]]
    dependency_id = public.get("private_dependency_id")
    private_required = scenario["action"] in public.get("private_required_for", [])

    public_output = {
        "public_id": public["public_id"],
        "public_state": public["state"],
        "public_conclusion": public["public_conclusion"],
        "private_dependency_id": dependency_id,
    }

    if private_required and scenario["private_available"]:
        private = private_record_map(fixture).get(dependency_id)
        return {
            "status": "PASS_PRIVATE_VERIFIED",
            "private_loaded": private is not None,
            "private_verification": private["private_status"] if private else "UNAVAILABLE",
            "public_output": public_output,
        }
    if private_required and not scenario["private_available"]:
        return {
            "status": "FAIL_VISIBLE_REQUIRED_PRIVATE_UNAVAILABLE",
            "private_loaded": False,
            "private_verification": "UNAVAILABLE",
            "public_output": public_output,
        }
    if public["state"] == "RESOLVED_PRIVATE" and not scenario["private_available"]:
        return {
            "status": "PASS_PUBLIC_RESOLVED_PRIVATE",
            "private_loaded": False,
            "private_verification": "NOT_VERIFIED",
            "public_state": public["state"],
            "public_output": public_output,
        }
    return {
        "status": "PASS_PUBLIC_ONLY",
        "private_loaded": False,
        "public_output": public_output,
    }


def scope_matches(source_scope: dict[str, Any], action: str, requested_scope: dict[str, Any]) -> bool:
    if source_scope.get("action") != action:
        return False
    for key, value in requested_scope.items():
        if source_scope.get(key) != value:
            return False
    return True


def resolve_authority_scenario(fixture: dict[str, Any], scenario: dict[str, Any]) -> dict[str, Any]:
    if not scenario["optional_retrieval_available"] and scenario["consequence"] == "low":
        return {
            "status": "DEGRADED_OPTIONAL_RETRIEVAL",
            "proceed_allowed": True,
            "uncertainty_visible": True,
        }

    applicable = [
        source
        for source in fixture["authority_sources"]
        if source["state"] == "current" and scope_matches(source["scope"], scenario["action"], scenario["scope"])
    ]
    available = set(scenario["available_source_ids"])
    missing = sorted(source["source_id"] for source in applicable if source.get("required") and source["source_id"] not in available)
    if missing:
        return {
            "status": "FAIL_VISIBLE_MISSING_REQUIRED_AUTHORITY",
            "missing_sources": missing,
        }

    usable = [source for source in applicable if source["source_id"] in available]
    values = {source["rule_value"] for source in usable}
    relation_edges = [
        relation
        for source in usable
        for relation in source.get("relations", [])
        if relation.get("target") in {item["source_id"] for item in usable}
    ]
    if len(values) > 1 and not relation_edges:
        return {
            "status": "UNRESOLVED_AUTHORITY_CONFLICT",
            "conflicting_sources": sorted(source["source_id"] for source in usable),
        }

    # Natural directional relations such as SUPPLEMENT mean the target is consumed before
    # the relation owner. Use a small deterministic topological walk rather than treating
    # the relation owner as the base.
    usable_ids = [source["source_id"] for source in usable]
    prerequisites: dict[str, set[str]] = {source_id: set() for source_id in usable_ids}
    for source in usable:
        for relation in source.get("relations", []):
            target = relation.get("target")
            if target in prerequisites:
                prerequisites[source["source_id"]].add(target)
    ordered: list[str] = []
    remaining = list(usable_ids)
    while remaining:
        ready = [source_id for source_id in remaining if prerequisites[source_id].issubset(ordered)]
        if not ready:
            return {
                "status": "UNRESOLVED_AUTHORITY_CONFLICT",
                "conflicting_sources": sorted(remaining),
            }
        for source_id in ready:
            ordered.append(source_id)
            remaining.remove(source_id)
    return {"status": "RESOLVED", "governing_sources": ordered}


def run_probe(fixture: dict[str, Any], fixture_sha: str) -> dict[str, Any]:
    baseline = route_projection(fixture, fixture["workstream_signals"][0]["values"])
    private_ready = route_projection(fixture, fixture["workstream_signals"][1]["values"])
    updates = {
        attempt["attempt_id"]: evaluate_workstream_update(fixture, attempt)
        for attempt in fixture["workstream_update_attempts"]
    }

    consolidation = {
        item["candidate_id"]: evaluate_consolidation(item)
        for item in fixture["consolidation_candidates"]
    }
    promotion, promoted = promotion_results(fixture)

    views_first = build_derived_views(fixture, promoted)
    views_rebuilt = build_derived_views(fixture, promoted)

    private_results = {
        scenario["scenario_id"]: evaluate_private_scenario(fixture, scenario)
        for scenario in fixture["private_scenarios"]
    }
    private_forbidden_values = [
        value
        for record in fixture["private_records"]
        for key, value in record.items()
        if key in {"private_locator", "private_marker", "detail"}
    ]
    public_render = json.dumps(private_results, sort_keys=True)
    leaked_values = sorted(value for value in private_forbidden_values if value in public_render)

    authority_results = {
        scenario["scenario_id"]: resolve_authority_scenario(fixture, scenario)
        for scenario in fixture["authority_scenarios"]
    }

    return {
        "schema_version": 1,
        "probe_id": "PKA-C01-SHADOW-OPS-PROBE-V02",
        "candidate_id": fixture["candidate_id"],
        "fixture_id": fixture["fixture_id"],
        "fixture_sha256": fixture_sha,
        "shadow_only": True,
        "implementation_reads_oracle": False,
        "workstreams": {
            "baseline": baseline,
            "private_ready": private_ready,
            "interruption_recovery": recover_transition(fixture, "TR-ADVANCE-FOUNDATION"),
            "updates": updates,
        },
        "consolidation": {
            "candidates": consolidation,
            "promotions": promotion,
            "capture_authority": {item["capture_id"]: item["authority_class"] for item in fixture["captures"]},
            "accepted_view_excludes": [item["capture_id"] for item in fixture["captures"] if item["authority_class"] != "canonical"],
            "novel_narrative_claim_capture_ids": narrative_candidate_captures(fixture),
        },
        "derived_views": {
            "routing_rebuild_equal": canonical_digest(views_first["ROUTING_CURRENT"]) == canonical_digest(views_rebuilt["ROUTING_CURRENT"]),
            "current_state_rebuild_equal": canonical_digest(views_first["CURRENT_STATE_CORE"]) == canonical_digest(views_rebuilt["CURRENT_STATE_CORE"]),
            "navigation_rebuild_equal": canonical_digest(views_first["NAVIGATION_INDEX"]) == canonical_digest(views_rebuilt["NAVIGATION_INDEX"]),
            "current_state_core": views_rebuilt["CURRENT_STATE_CORE"],
            "navigation_index": views_rebuilt["NAVIGATION_INDEX"],
            "view_digests": {key: canonical_digest(value) for key, value in views_rebuilt.items()},
        },
        "private_boundary": {
            "scenarios": private_results,
            "public_leaked_private_values": leaked_values,
        },
        "authority_uncertainty": authority_results,
        "metrics": {
            "workstream_count": len(fixture["workstreams"]),
            "paused_count": sum(ws["state"] == "PAUSED" for ws in fixture["workstreams"]),
            "multi_dependency_workstream_count": sum(len(ws.get("depends_on", [])) > 1 for ws in fixture["workstreams"]),
            "promoted_knowledge_count": len(promoted),
            "candidate_capture_count": len(fixture["captures"]),
            "derived_view_count": len(fixture["derived_view_manifests"]),
            "public_leak_count": len(leaked_values),
            "fail_visible_authority_cases": sum(result["status"].startswith("FAIL_VISIBLE") or result["status"].startswith("UNRESOLVED") for result in authority_results.values()),
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
