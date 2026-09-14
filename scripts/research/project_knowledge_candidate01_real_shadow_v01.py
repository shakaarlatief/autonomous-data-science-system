#!/usr/bin/env python3
"""Candidate 01 real-repository shadow parity/behavior probe V0.1.

The probe is bound to one exact Git commit. Generation uses real repository source
blobs plus explicit migration seeds frozen in the fixture. Existing global live
views are withheld from generation and are opened only afterward for parity
comparison. The separate oracle is never read by this implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

EXPECTED_FIXTURE_SHA256 = "9e8cd2ce0be7ced69eabc246414bd9aa0f21b305e03efeffd81db86c222d42bc"
DEFAULT_FIXTURE = Path("docs/research/project_knowledge_candidate_01_real_shadow_v01/REAL_SHADOW_FIXTURE_V01.json")
DEFAULT_OUTPUT = Path("docs/research/project_knowledge_candidate_01_real_shadow_v01/RESULTS_V01.json")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_fixture(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    digest = sha256_bytes(raw)
    if digest != EXPECTED_FIXTURE_SHA256:
        raise RuntimeError(f"fixture hash mismatch: expected {EXPECTED_FIXTURE_SHA256}, got {digest}")
    return json.loads(raw.decode("utf-8")), digest


def git_blob(base_commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{base_commit}:{path}"])


def manifest_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["source_key"]: item for item in fixture["source_manifest"]}


def comparison_keys(fixture: dict[str, Any]) -> set[str]:
    return set(fixture["protocol"]["comparison_targets"])


def read_source(
    fixture: dict[str, Any], source_key: str, read_log: list[str], *, allow_comparison: bool
) -> bytes:
    manifest = manifest_map(fixture)
    if source_key not in manifest:
        raise KeyError(source_key)
    if source_key in comparison_keys(fixture) and not allow_comparison:
        raise RuntimeError(f"comparison target read during generation: {source_key}")
    item = manifest[source_key]
    blob = git_blob(fixture["base_commit"], item["path"])
    if len(blob) != item["bytes"] or sha256_bytes(blob) != item["sha256"]:
        raise RuntimeError(f"source drift at frozen base: {source_key}")
    read_log.append(source_key)
    return blob


def verify_manifest(fixture: dict[str, Any]) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    for item in fixture["source_manifest"]:
        blob = git_blob(fixture["base_commit"], item["path"])
        actual_sha = sha256_bytes(blob)
        rows[item["source_key"]] = {
            "path": item["path"],
            "bytes_match": len(blob) == item["bytes"],
            "sha256_match": actual_sha == item["sha256"],
            "comparison_target": bool(item.get("comparison_target")),
        }
    return {
        "all_match": all(row["bytes_match"] and row["sha256_match"] for row in rows.values()),
        "sources": rows,
    }


def workstream_route(fixture: dict[str, Any]) -> dict[str, Any]:
    rows = {item["workstream_id"]: item for item in fixture["workstream_declarations"]}
    active = {wid for wid, item in rows.items() if item["state"] == "ACTIVE"}
    completed = {wid for wid, item in rows.items() if item["state"] == "COMPLETED"}
    eligible = {
        wid
        for wid in active
        if all(dep in completed or dep in active for dep in rows[wid].get("depends_on", []))
    }
    roots = [wid for wid in fixture_order(fixture) if wid in eligible and rows[wid].get("parent") not in eligible]
    route: list[str] = []
    current = roots[0] if roots else None
    while current:
        route.append(current)
        children = [
            wid
            for wid in fixture_order(fixture)
            if wid in eligible and rows[wid].get("parent") == current
        ]
        if not children:
            break
        current = children[-1]
    migration_seed = [
        item["workstream_id"]
        for item in fixture["workstream_declarations"]
        if item.get("source_mode") == "MIGRATION_SEED_REQUIRED"
    ]
    return {"route": route, "migration_seed_workstreams": migration_seed}


def fixture_order(fixture: dict[str, Any]) -> list[str]:
    return [item["workstream_id"] for item in fixture["workstream_declarations"]]


def parse_specification_number(text: str) -> str:
    match = re.search(r"^#\s+Specification\s+(\d{3})\b", text, flags=re.MULTILINE)
    if not match:
        raise RuntimeError("specification number not found")
    return match.group(1)


def parse_experiment_outcome(text: str) -> str:
    if "INCOMPLETE / EXECUTION INTEGRITY FAILED" in text:
        return "INCOMPLETE"
    raise RuntimeError("governed incomplete experiment outcome not found")


def parse_checkpoint_number_from_source(text: str) -> int:
    match = re.search(r"^#\s+Checkpoint\s+(\d+):", text, flags=re.MULTILINE)
    if not match:
        raise RuntimeError("checkpoint number not found")
    return int(match.group(1))


def parse_current_boundary_from_checkpoint(text: str) -> str:
    match = re.search(r"^NEXT=([A-Z0-9_]+)$", text, flags=re.MULTILINE)
    if not match or match.group(1) != "REAL_REPOSITORY_SHADOW_PARITY_AND_BEHAVIOR":
        raise RuntimeError("Checkpoint 496 NEXT boundary not found")
    return "project-knowledge-real-repository-shadow-next"


def generate_routing_projection(fixture: dict[str, Any], source_cache: dict[str, str]) -> dict[str, Any]:
    spec_key = fixture["computed_control_sources"]["latest_specification"]["source_key"]
    experiment_key = fixture["computed_control_sources"]["latest_experiment_outcome"]["source_key"]
    workstream = next(
        item for item in fixture["workstream_declarations"] if item["workstream_id"] == "WS-REAL-SHADOW"
    )
    checkpoint_text = source_cache[workstream["source_key"]]
    seed = fixture["project_control_seed"]["facts"]
    return {
        "schema_version": 1,
        "current_checkpoint": parse_checkpoint_number_from_source(checkpoint_text),
        "active_development_branch": fixture["base_branch"],
        "active_pr": seed["active_pr"],
        "promoted_integration_branch": seed["promoted_integration_branch"],
        "promoted_integration_sha": seed["promoted_integration_sha"],
        "latest_specification": parse_specification_number(source_cache[spec_key]),
        "latest_experiment_outcome": parse_experiment_outcome(source_cache[experiment_key]),
        "current_boundary": parse_current_boundary_from_checkpoint(checkpoint_text),
    }


def verify_continuity_contract(fixture: dict[str, Any], continuity_text: str) -> dict[str, Any]:
    heading = fixture["continuity_contract"]["section_heading"]
    start = continuity_text.find(heading)
    if start < 0:
        return {"aligned": False, "constraint_positions": {}, "failure": "SECTION_NOT_FOUND"}
    next_heading = continuity_text.find("\n## ", start + len(heading))
    section = continuity_text[start : next_heading if next_heading >= 0 else None]
    positions: dict[str, int] = {}
    cursor = -1
    aligned = True
    for constraint in fixture["continuity_contract"]["constraints"]:
        pos = section.find(constraint["source_token"])
        positions[constraint["constraint_id"]] = pos
        if pos < 0 or pos <= cursor:
            aligned = False
        cursor = max(cursor, pos)
    return {"aligned": aligned, "constraint_positions": positions}


def check_action_attempt(required_ids: list[str], emitted_ids: list[str]) -> dict[str, Any]:
    omitted = [cid for cid in required_ids if cid not in emitted_ids]
    positions = {cid: idx for idx, cid in enumerate(emitted_ids)}
    violation: set[str] = set()
    present = [cid for cid in required_ids if cid in positions]
    for i, left in enumerate(present):
        for right in present[i + 1 :]:
            if positions[left] > positions[right]:
                violation.add(left)
                violation.add(right)
    order_violations = [cid for cid in required_ids if cid in violation]
    return {
        "status": "FAIL_VISIBLE" if omitted or order_violations else "PASS",
        "omitted": omitted,
        "order_violations": order_violations,
    }


def generated_navigation(fixture: dict[str, Any]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}
    for declaration in fixture["navigation_declarations"]:
        for subject in declaration["subjects"]:
            index.setdefault(subject, []).append(declaration["source_key"])
    return {subject: sorted(values) for subject, values in sorted(index.items())}


def generate_shadow(fixture: dict[str, Any]) -> dict[str, Any]:
    reads: list[str] = []
    needed_keys = {
        item["source_key"] for item in fixture["workstream_declarations"]
    } | {
        fixture["continuity_contract"]["source_key"],
        fixture["computed_control_sources"]["latest_specification"]["source_key"],
        fixture["computed_control_sources"]["latest_experiment_outcome"]["source_key"],
    } | {item["source_key"] for item in fixture["navigation_declarations"]}

    cache = {
        key: read_source(fixture, key, reads, allow_comparison=False).decode("utf-8")
        for key in sorted(needed_keys)
    }
    route = workstream_route(fixture)
    routing = generate_routing_projection(fixture, cache)
    continuity = verify_continuity_contract(
        fixture, cache[fixture["continuity_contract"]["source_key"]]
    )
    required_ids = [item["constraint_id"] for item in fixture["continuity_contract"]["constraints"]]
    attempts = {
        item["attempt_id"]: check_action_attempt(required_ids, item["emitted_constraint_ids"])
        for item in fixture["continuity_action_attempts"]
    }
    project_seed = fixture["project_control_seed"]
    return {
        "source_reads": reads,
        "generation_reads_comparison_targets": bool(set(reads) & comparison_keys(fixture)),
        "workstreams": route,
        "migration_seed_project_control": {
            "source_mode": project_seed["source_mode"],
            "fact_count": len(project_seed["facts"]),
            "facts": sorted(project_seed["facts"]),
        },
        "routing_projection": routing,
        "continuity_contract": continuity,
        "continuity_action_attempts": attempts,
        "navigation_projection": generated_navigation(fixture),
        "real_capture": {
            "capture_id": fixture["real_capture_seed"]["capture_id"],
            "authority_class": fixture["real_capture_seed"]["authority_class"],
        },
    }


def compare_current_state(target_text: str, fixture: dict[str, Any]) -> dict[str, bool]:
    routing = fixture["base_commit"]  # keeps comparison function explicitly bound to frozen experiment context
    del routing
    return {
        "checkpoint": "**Checkpoint:** 496" in target_text,
        "active_branch": "**Active development branch:** `v1-source-vault-bootstrap-resume`" in target_text,
        "research124_stage": "## Current active stage: Research 124 project-development knowledge architecture redesign" in target_text,
        "next_real_shadow": "bounded real-repository shadow parity/behavior test" in target_text,
        "target_not_selected": "Candidate 01 remains unselected" in target_text or "no target architecture is selected" in target_text,
    }


def compare_knowledge_map(target_text: str, fixture: dict[str, Any]) -> dict[str, bool]:
    manifest = manifest_map(fixture)
    keys = ["result151", "checkpoint496", "candidate144"]
    return {key: manifest[key]["path"] in target_text for key in keys}


def compare_targets(fixture: dict[str, Any], generated: dict[str, Any]) -> dict[str, Any]:
    reads: list[str] = []
    routing_blob = read_source(fixture, "routing_target", reads, allow_comparison=True)
    state_text = read_source(fixture, "current_state_target", reads, allow_comparison=True).decode("utf-8")
    map_text = read_source(fixture, "knowledge_map_target", reads, allow_comparison=True).decode("utf-8")
    routing_target = json.loads(routing_blob.decode("utf-8"))
    return {
        "comparison_reads": reads,
        "routing_exact_parity": generated["routing_projection"] == routing_target,
        "current_state_semantic_parity": compare_current_state(state_text, fixture),
        "knowledge_map_membership": compare_knowledge_map(map_text, fixture),
    }


def run_probe(fixture: dict[str, Any], fixture_sha: str) -> dict[str, Any]:
    generated = generate_shadow(fixture)
    comparison = compare_targets(fixture, generated)
    manifest = verify_manifest(fixture)
    return {
        "schema_version": 1,
        "probe_id": "PKA-C01-REAL-SHADOW-PROBE-V01",
        "candidate_id": fixture["candidate_id"],
        "fixture_id": fixture["fixture_id"],
        "base_commit": fixture["base_commit"],
        "fixture_sha256": fixture_sha,
        "shadow_only": True,
        "implementation_reads_oracle": False,
        "manifest_verification": manifest,
        "generation": generated,
        "comparison": comparison,
        "metrics": {
            "generation_source_read_count": len(generated["source_reads"]),
            "generation_comparison_target_read_count": len(set(generated["source_reads"]) & comparison_keys(fixture)),
            "migration_seed_workstream_count": len(generated["workstreams"]["migration_seed_workstreams"]),
            "migration_seed_project_control_fact_count": generated["migration_seed_project_control"]["fact_count"],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()
    fixture, digest = load_fixture(args.fixture)
    result = run_probe(fixture, digest)
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if not args.no_write:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
