#!/usr/bin/env python3
"""Candidate 01 zero-seed successor-native routing shadow V0.1.

Generation consumes only two frozen successor-native shadow sources plus real
non-target control evidence at the exact frozen base commit. Existing global
routing/state/navigation surfaces are forbidden until the post-generation
comparison phase. The separate oracle is never read here.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

EXPECTED_FIXTURE_SHA256 = "25d302e1fd46afdc1f7e1d363cd8eeedc5881c055aeb2ab79655bae756364594"
DEFAULT_FIXTURE = Path("docs/research/project_knowledge_candidate_01_zero_seed_routing_v01/ZERO_SEED_ROUTING_FIXTURE_V01.json")
DEFAULT_OUTPUT = Path("docs/research/project_knowledge_candidate_01_zero_seed_routing_v01/RESULTS_V01.json")
DECLARATION_RE = re.compile(
    r"<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->\r?\n(.*?)\r?\n<!-- PKA-STRUCTURED-DECLARATION-END -->",
    flags=re.DOTALL,
)


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


def read_shadow_source(item: dict[str, Any], read_log: list[str]) -> dict[str, Any]:
    path = Path(item["path"])
    raw = path.read_bytes()
    if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
        raise RuntimeError(f"shadow source drift: {item['source_key']}")
    match = DECLARATION_RE.search(raw.decode("utf-8"))
    if not match:
        raise RuntimeError(f"structured declaration missing: {item['source_key']}")
    declaration = json.loads(match.group(1))
    if declaration.get("shadow_only") is not True:
        raise RuntimeError(f"shadow source not marked shadow-only: {item['source_key']}")
    if declaration.get("authority_class") != "canonical":
        raise RuntimeError(f"shadow canonical class missing: {item['source_key']}")
    read_log.append(item["path"])
    return declaration


def read_real_source(
    fixture: dict[str, Any], source_key: str, read_log: list[str], *, allow_comparison: bool
) -> bytes:
    item = next(entry for entry in fixture["real_sources"] if entry["source_key"] == source_key)
    if item["source_class"] == "comparison_target" and not allow_comparison:
        raise RuntimeError(f"comparison target read during generation: {item['path']}")
    raw = git_blob(fixture["real_base_commit"], item["path"])
    if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
        raise RuntimeError(f"real source drift at frozen base: {source_key}")
    read_log.append(item["path"])
    return raw


def parse_specification_number(text: str) -> str:
    match = re.search(r"^#\s+Specification\s+(\d{3})\b", text, flags=re.MULTILINE)
    if not match:
        raise RuntimeError("specification number not found")
    return match.group(1)


def parse_experiment_outcome(text: str) -> str:
    if "INCOMPLETE / EXECUTION INTEGRITY FAILED" in text:
        return "INCOMPLETE"
    raise RuntimeError("governed incomplete experiment outcome not found")


def semantic_ownership() -> dict[str, str]:
    return {
        "active_development_branch": "active_workstream.execution_anchor",
        "active_pr": "active_workstream.execution_anchor",
        "current_checkpoint": "active_workstream.execution_anchor",
        "current_boundary": "active_workstream.execution_anchor",
        "promoted_integration_branch": "integration_boundary",
        "promoted_integration_sha": "integration_boundary",
        "latest_specification": "computed:spec027",
        "latest_experiment_outcome": "computed:checkpoint192",
    }


def generate_routing(fixture: dict[str, Any]) -> dict[str, Any]:
    generation_reads: list[str] = []
    shadow_items = {item["source_key"]: item for item in fixture["shadow_sources"]}
    workstream = read_shadow_source(shadow_items["active_workstream"], generation_reads)
    integration = read_shadow_source(shadow_items["integration_boundary"], generation_reads)
    spec_text = read_real_source(fixture, "spec027", generation_reads, allow_comparison=False).decode("utf-8")
    outcome_text = read_real_source(fixture, "checkpoint192", generation_reads, allow_comparison=False).decode("utf-8")

    if workstream.get("kind") != "WORKSTREAM":
        raise RuntimeError("active workstream source has wrong kind")
    if integration.get("kind") != "PROJECT_INTEGRATION_BOUNDARY":
        raise RuntimeError("integration boundary source has wrong kind")

    anchor = workstream["execution_anchor"]
    projection = {
        "schema_version": fixture["routing_contract"]["schema_version"],
        "current_checkpoint": anchor["current_checkpoint"],
        "active_development_branch": anchor["active_development_branch"],
        "active_pr": anchor["active_pr"],
        "promoted_integration_branch": integration["promoted_branch"],
        "promoted_integration_sha": integration["promoted_commit"],
        "latest_specification": parse_specification_number(spec_text),
        "latest_experiment_outcome": parse_experiment_outcome(outcome_text),
        "current_boundary": anchor["current_semantic_boundary"],
    }
    forbidden = set(fixture["protocol"]["forbidden_generation_paths"])
    forbidden_reads = sorted(path for path in generation_reads if path in forbidden)
    return {
        "routing_projection": projection,
        "generation_reads": generation_reads,
        "forbidden_generation_path_reads": forbidden_reads,
        "shadow_source_kinds": {
            "active_workstream": workstream["kind"],
            "integration_boundary": integration["kind"],
        },
        "semantic_ownership": semantic_ownership(),
        "global_live_state_generation_fact_count": fixture["migration_accounting"]["global_live_state_generation_fact_count"],
        "manual_shadow_source_touch_count": fixture["migration_accounting"]["manual_shadow_source_touch_count"],
    }


def compare_target(fixture: dict[str, Any], projection: dict[str, Any]) -> dict[str, Any]:
    reads: list[str] = []
    target_raw = read_real_source(fixture, "routing_target", reads, allow_comparison=True)
    target = json.loads(target_raw.decode("utf-8"))
    return {
        "comparison_reads": reads,
        "routing_exact_parity": projection == target,
        "target_sha256": sha256_bytes(target_raw),
    }


def verify_all_source_hashes(fixture: dict[str, Any]) -> bool:
    for item in fixture["shadow_sources"]:
        raw = Path(item["path"]).read_bytes()
        if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
            return False
    for item in fixture["real_sources"]:
        raw = git_blob(fixture["real_base_commit"], item["path"])
        if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
            return False
    return True


def run_probe(fixture: dict[str, Any], fixture_sha: str) -> dict[str, Any]:
    generated = generate_routing(fixture)
    comparison = compare_target(fixture, generated["routing_projection"])
    return {
        "schema_version": 1,
        "probe_id": "PKA-C01-ZERO-SEED-ROUTING-PROBE-V01",
        "candidate_id": fixture["candidate_id"],
        "fixture_id": fixture["fixture_id"],
        "real_base_commit": fixture["real_base_commit"],
        "fixture_sha256": fixture_sha,
        "shadow_only": True,
        "implementation_reads_oracle": False,
        "all_source_hashes_match": verify_all_source_hashes(fixture),
        "generation": generated,
        "comparison": comparison,
        "metrics": {
            "successor_shadow_source_count": len(fixture["shadow_sources"]),
            "generation_source_read_count": len(generated["generation_reads"]),
            "generation_forbidden_path_read_count": len(generated["forbidden_generation_path_reads"]),
            "global_live_state_generation_fact_count": generated["global_live_state_generation_fact_count"],
            "manual_shadow_source_touch_count": generated["manual_shadow_source_touch_count"],
            "broad_project_control_source_count": 0,
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
