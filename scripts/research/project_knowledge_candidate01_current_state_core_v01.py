#!/usr/bin/env python3
"""Candidate 01 Source Vault workstream + compact current-state-core shadow V0.1.

Generation consumes frozen successor-native shadow sources and real non-target evidence.
The existing global current-routing/current-state surfaces are comparison-only and may
not be opened until the generated core is complete. The separate oracle is test-only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

EXPECTED_FIXTURE_SHA256 = "4b7ac27801e7d89c0cd782c895d6d0db47693916e4aae7696eb3fc4d6081ad38"
DEFAULT_FIXTURE = Path("docs/research/project_knowledge_candidate_01_current_state_core_v01/CURRENT_STATE_CORE_FIXTURE_V01.json")
DEFAULT_OUTPUT = Path("docs/research/project_knowledge_candidate_01_current_state_core_v01/RESULTS_V01.json")
DECLARATION_RE = re.compile(
    r"<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->\r?\n(.*?)\r?\n<!-- PKA-STRUCTURED-DECLARATION-END -->",
    flags=re.DOTALL,
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def load_fixture(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    digest = sha256_bytes(raw)
    if digest != EXPECTED_FIXTURE_SHA256:
        raise RuntimeError(f"fixture hash mismatch: expected {EXPECTED_FIXTURE_SHA256}, got {digest}")
    return json.loads(raw.decode("utf-8")), digest


def git_blob(base_commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{base_commit}:{path}"])


def shadow_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["source_key"]: item for item in fixture["shadow_sources"]}


def real_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["source_key"]: item for item in fixture["real_sources"]}


def read_shadow(item: dict[str, Any], read_log: list[str]) -> dict[str, Any]:
    raw = Path(item["path"]).read_bytes()
    if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
        raise RuntimeError(f"shadow source drift: {item['source_key']}")
    match = DECLARATION_RE.search(raw.decode("utf-8"))
    if not match:
        raise RuntimeError(f"missing structured declaration: {item['source_key']}")
    declaration = json.loads(match.group(1))
    if declaration.get("shadow_only") is not True or declaration.get("authority_class") != "canonical":
        raise RuntimeError(f"invalid shadow source authority contract: {item['source_key']}")
    read_log.append(item["path"])
    return declaration


def read_real(
    fixture: dict[str, Any], source_key: str, read_log: list[str], *, allow_comparison: bool
) -> bytes:
    item = real_map(fixture)[source_key]
    if item["source_class"] == "comparison_target" and not allow_comparison:
        raise RuntimeError(f"comparison target read during generation: {item['path']}")
    raw = git_blob(fixture["real_base_commit"], item["path"])
    if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
        raise RuntimeError(f"real source drift: {source_key}")
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


def source_vault_evidence_alignment(
    source_vault: dict[str, Any], evidence: dict[str, str]
) -> dict[str, Any]:
    state = source_vault["bootstrap_state"]
    checks = {
        "registry_migrated_verified": (
            "PERMANENT_SOURCE_REGISTRY_MIGRATED_VERIFIED" in evidence["validation003"]
            and state["source_registry"] == "MIGRATED_VERIFIED"
        ),
        "alembic_head": (
            "0003_source_universe" in evidence["validation003"]
            and state["alembic_head"] == "0003_source_universe"
        ),
        "table_count": ("SQLite table count             33" in evidence["validation003"] and state["sqlite_table_count"] == 33),
        "compare_20_match": (
            "total manifest outcomes        20" in evidence["validation004"]
            and "MATCH                          20" in evidence["validation004"]
            and state["prospective_compare_total"] == 20
            and state["prospective_compare_match"] == 20
        ),
        "no_compare_mismatches": (
            state["different_artifact"] == 0
            and state["missing_local_source"] == 0
            and state["additional_local_source"] == 0
            and "non-MATCH outcomes              0" in evidence["validation004"]
        ),
        "ingestion_not_started": (
            "Source ingestion had not started" in evidence["validation004"]
            and state["source_ingestion"] == "NOT_STARTED"
        ),
        "resume_target": (
            "reviewed ingestion of the frozen 20-entry first corpus" in evidence["checkpoint274"]
            and source_vault["resume_target"] == "reviewed ingestion of the frozen 20-entry first corpus"
        ),
        "governing_procedure": (
            "docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md" in evidence["checkpoint274"]
            and source_vault["governing_procedure"] == "docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md"
        ),
        "working_audit_pending": state["working_store_integrity_audit"] == "PENDING",
        "backup_pending": state["independent_encrypted_backup_proof"] == "PENDING",
        "restore_pending": state["clean_restore_and_restored_audit"] == "PENDING",
        "course2_blocked": ("Course 2 remains blocked" in evidence["validation004"] and state["course_2"] == "BLOCKED"),
        "private_boundary": (
            "RESOLVED_PRIVATE" in evidence["runbook"] and source_vault["private_dependency_state"] == "RESOLVED_PRIVATE"
        ),
    }
    return {"all_aligned": all(checks.values()), "checks": checks}


def build_core(
    active: dict[str, Any], integration: dict[str, Any], source_vault: dict[str, Any], spec: str, outcome: str
) -> dict[str, Any]:
    anchor = active["execution_anchor"]
    sv = source_vault["bootstrap_state"]
    return {
        "schema_version": 1,
        "current_checkpoint": anchor["current_checkpoint"],
        "active_development_branch": anchor["active_development_branch"],
        "active_pr": anchor["active_pr"],
        "promoted_integration_branch": integration["promoted_branch"],
        "promoted_integration_sha": integration["promoted_commit"],
        "latest_specification": spec,
        "latest_experiment_outcome": outcome,
        "active_stage": {
            "research_id": active["research_id"],
            "objective": active["objective"],
            "selection_state": active["selection_state"],
            "current_boundary": anchor["current_semantic_boundary"],
        },
        "paused_workstreams": [
            {
                "semantic_id": source_vault["semantic_id"],
                "state": source_vault["state"],
                "resume_target": source_vault["resume_target"],
                "governing_procedure": source_vault["governing_procedure"],
                "source_ingestion": sv["source_ingestion"],
                "course_2": sv["course_2"],
            }
        ],
    }


def recoverable_semantics(
    active: dict[str, Any], integration: dict[str, Any], source_vault: dict[str, Any], spec: str, outcome: str
) -> dict[str, Any]:
    anchor = active["execution_anchor"]
    sv = source_vault["bootstrap_state"]
    return {
        "current_checkpoint": anchor["current_checkpoint"],
        "active_development_branch": anchor["active_development_branch"],
        "active_pr": anchor["active_pr"],
        "current_boundary": anchor["current_semantic_boundary"],
        "active_research_stage": active["research_id"],
        "target_architecture_selection_state": active["selection_state"],
        "promoted_integration_branch": integration["promoted_branch"],
        "promoted_integration_sha": integration["promoted_commit"],
        "latest_specification": spec,
        "latest_experiment_outcome": outcome,
        "source_vault_workstream_state": source_vault["state"],
        "source_vault_resume_target": source_vault["resume_target"],
        "source_vault_governing_procedure": source_vault["governing_procedure"],
        "source_vault_registry_status": sv["source_registry"],
        "source_vault_alembic_head": sv["alembic_head"],
        "source_vault_first_corpus_compare": {
            "total": sv["prospective_compare_total"],
            "match": sv["prospective_compare_match"],
            "different": sv["different_artifact"],
            "missing": sv["missing_local_source"],
            "additional": sv["additional_local_source"],
        },
        "source_vault_ingestion_status": sv["source_ingestion"],
        "source_vault_working_audit_status": sv["working_store_integrity_audit"],
        "source_vault_backup_status": sv["independent_encrypted_backup_proof"],
        "source_vault_restore_status": sv["clean_restore_and_restored_audit"],
        "course2_gate": sv["course_2"],
        "source_vault_resume_sequence": source_vault["resume_sequence"],
        "source_vault_private_dependency_state": source_vault["private_dependency_state"],
    }


def generate(fixture: dict[str, Any]) -> dict[str, Any]:
    reads: list[str] = []
    shadows = shadow_map(fixture)
    active = read_shadow(shadows["active_workstream"], reads)
    integration = read_shadow(shadows["integration_boundary"], reads)
    source_vault = read_shadow(shadows["source_vault_workstream"], reads)

    spec_text = read_real(fixture, "spec027", reads, allow_comparison=False).decode("utf-8")
    outcome_text = read_real(fixture, "checkpoint192", reads, allow_comparison=False).decode("utf-8")
    evidence = {
        "runbook": read_real(fixture, "source_vault_runbook", reads, allow_comparison=False).decode("utf-8"),
        "validation003": read_real(fixture, "source_vault_validation003", reads, allow_comparison=False).decode("utf-8"),
        "validation004": read_real(fixture, "source_vault_validation004", reads, allow_comparison=False).decode("utf-8"),
        "checkpoint274": read_real(fixture, "source_vault_checkpoint274", reads, allow_comparison=False).decode("utf-8"),
    }
    # Research 124 is source-bound context for the active workstream, but its prose is not
    # copied into the core. Reading it here proves the declared provenance path remains exact.
    _ = read_real(fixture, "research124", reads, allow_comparison=False)
    _ = read_real(fixture, "decomposition_audit", reads, allow_comparison=False)

    spec = parse_specification_number(spec_text)
    outcome = parse_experiment_outcome(outcome_text)
    alignment = source_vault_evidence_alignment(source_vault, evidence)
    core = build_core(active, integration, source_vault, spec, outcome)
    recoverable = recoverable_semantics(active, integration, source_vault, spec, outcome)
    missing = [item["id"] for item in fixture["must_preserve_manifest"] if item["semantic"] not in recoverable]
    forbidden = set(fixture["protocol"]["forbidden_generation_paths"])
    forbidden_reads = sorted(path for path in reads if path in forbidden)

    return {
        "source_reads": reads,
        "forbidden_generation_path_reads": forbidden_reads,
        "shadow_source_kinds": {
            "active_workstream": active["kind"],
            "integration_boundary": integration["kind"],
            "source_vault_workstream": source_vault["kind"],
        },
        "source_vault_evidence_alignment": alignment,
        "source_vault_pause_state": source_vault["state"],
        "current_state_core": core,
        "current_state_core_bytes": len(canonical_bytes(core)),
        "recoverable_semantics": recoverable,
        "must_preserve_items_recoverable": len(fixture["must_preserve_manifest"]) - len(missing),
        "must_preserve_items_missing": missing,
        "global_target_generation_fact_count": fixture["migration_accounting"]["global_target_generation_fact_count"],
    }


def compare(fixture: dict[str, Any], generated: dict[str, Any]) -> dict[str, Any]:
    reads: list[str] = []
    routing = json.loads(read_real(fixture, "current_routing_target", reads, allow_comparison=True).decode("utf-8"))
    current_state_raw = read_real(fixture, "current_state_target", reads, allow_comparison=True)
    current_state = current_state_raw.decode("utf-8")
    core = generated["current_state_core"]
    routing_subset = {
        "schema_version": core["schema_version"],
        "current_checkpoint": core["current_checkpoint"],
        "active_development_branch": core["active_development_branch"],
        "active_pr": core["active_pr"],
        "promoted_integration_branch": core["promoted_integration_branch"],
        "promoted_integration_sha": core["promoted_integration_sha"],
        "latest_specification": core["latest_specification"],
        "latest_experiment_outcome": core["latest_experiment_outcome"],
        "current_boundary": core["active_stage"]["current_boundary"],
    }
    markers = {
        "checkpoint": "**Checkpoint:** 501" in current_state,
        "active_stage": "## Current active stage: Research 124 project-development knowledge architecture redesign" in current_state,
        "target_not_selected": "Candidate 01 remains unselected" in current_state,
        "source_vault_state": "source ingestion                    NOT STARTED" in current_state,
        "source_vault_resume_target": "reviewed ingestion of the frozen 20-entry first corpus" in current_state,
        "course2_blocked": "Course 2                            BLOCKED" in current_state,
    }
    stale_pause = "When the current Research 113 Level-2 route closes" in current_state
    return {
        "comparison_reads": reads,
        "routing_subset_exact_parity": routing_subset == routing,
        "current_state_live_marker_parity": markers,
        "source_vault_old_pause_reason_detected_stale": stale_pause,
        "current_state_target_bytes": len(current_state_raw),
        "core_to_target_byte_ratio": round(generated["current_state_core_bytes"] / len(current_state_raw), 6),
    }


def verify_all_hashes(fixture: dict[str, Any]) -> bool:
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
    generated = generate(fixture)
    comparison = compare(fixture, generated)
    return {
        "schema_version": 1,
        "probe_id": "PKA-C01-CURRENT-STATE-CORE-PROBE-V01",
        "candidate_id": fixture["candidate_id"],
        "fixture_id": fixture["fixture_id"],
        "real_base_commit": fixture["real_base_commit"],
        "fixture_sha256": fixture_sha,
        "shadow_only": True,
        "implementation_reads_oracle": False,
        "all_source_hashes_match": verify_all_hashes(fixture),
        "generation": generated,
        "comparison": comparison,
        "metrics": {
            "successor_shadow_source_count": len(fixture["shadow_sources"]),
            "new_source_vault_workstream_source_count": fixture["migration_accounting"]["new_source_vault_workstream_source_count"],
            "must_preserve_item_count": len(fixture["must_preserve_manifest"]),
            "must_preserve_recoverable_count": generated["must_preserve_items_recoverable"],
            "current_state_core_bytes": generated["current_state_core_bytes"],
            "current_state_target_bytes": comparison["current_state_target_bytes"],
            "core_to_target_byte_ratio": comparison["core_to_target_byte_ratio"],
            "generation_forbidden_path_read_count": len(generated["forbidden_generation_path_reads"]),
            "global_target_generation_fact_count": generated["global_target_generation_fact_count"],
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
