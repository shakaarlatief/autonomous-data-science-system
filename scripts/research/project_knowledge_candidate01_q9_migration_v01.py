#!/usr/bin/env python3
"""Run Candidate 01's real-base Q9 migration/rollback shadow probe.

The probe is oracle-blind and strictly shadow-only. It compares migration-critical
semantics from the frozen legacy authority boundary to successor Candidate 01
sources, measures reverse references, exports legacy-compatible continuity
surfaces into temporary workspace state, validates those surfaces with the
existing routing checker, evaluates the authority-switch gate, and verifies that
the migration can preserve its own continuation state. Live authority files are
hashed before and after the probe and are never used as export destinations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

EXPECTED_FIXTURE_SHA256 = "5f6fec6c812692f8b085dde8f15ddc8c1f80a2695bf75933a80d736eeb83dfcc"
DEFAULT_FIXTURE = Path("docs/research/project_knowledge_candidate_01_q9_migration_v01/Q9_MIGRATION_FIXTURE_V01.json")
DEFAULT_OUTPUT = Path("docs/research/project_knowledge_candidate_01_q9_migration_v01/RESULTS_V01.json")
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
        raise RuntimeError(
            f"fixture hash mismatch: expected {EXPECTED_FIXTURE_SHA256}, got {digest}"
        )
    fixture = json.loads(raw.decode("utf-8"))
    protocol = fixture["protocol"]
    if protocol["implementation_may_read_oracle"] is not False:
        raise RuntimeError("fixture lost oracle-blind implementation contract")
    if protocol["authority_switch_forbidden"] is not True:
        raise RuntimeError("Q9 shadow probe must forbid authority switching")
    if protocol["rollback_export_must_not_overwrite_live_paths"] is not True:
        raise RuntimeError("Q9 rollback export must remain isolated from live authority")
    return fixture, digest


def source_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["source_key"]: item for item in fixture["real_sources"]}


def shadow_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["source_key"]: item for item in fixture["shadow_sources"]}


def git_blob(fixture: dict[str, Any], source_key: str) -> bytes:
    item = source_map(fixture)[source_key]
    raw = subprocess.check_output(
        ["git", "show", f"{fixture['real_base_commit']}:{item['path']}"]
    )
    if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
        raise RuntimeError(f"real source drift: {source_key}")
    return raw


def read_real_text(fixture: dict[str, Any], source_key: str) -> str:
    return git_blob(fixture, source_key).decode("utf-8")


def read_real_json(fixture: dict[str, Any], source_key: str) -> Any:
    return json.loads(read_real_text(fixture, source_key))


def read_shadow_declaration(fixture: dict[str, Any], source_key: str) -> dict[str, Any]:
    item = shadow_map(fixture)[source_key]
    raw = Path(item["path"]).read_bytes()
    if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
        raise RuntimeError(f"shadow source drift: {source_key}")
    match = DECLARATION_RE.search(raw.decode("utf-8"))
    if not match:
        raise RuntimeError(f"structured declaration missing: {source_key}")
    declaration = json.loads(match.group(1))
    if declaration.get("shadow_only") is not True:
        raise RuntimeError(f"shadow source lost shadow-only status: {source_key}")
    if declaration.get("authority_class") == "canonical":
        raise RuntimeError(f"Q9 migration source unexpectedly claims current canonical authority: {source_key}")
    return declaration


def all_source_hashes_match(fixture: dict[str, Any]) -> bool:
    try:
        for item in fixture["real_sources"]:
            raw = subprocess.check_output(
                ["git", "show", f"{fixture['real_base_commit']}:{item['path']}"]
            )
            if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
                return False
        for item in fixture["shadow_sources"]:
            raw = Path(item["path"]).read_bytes()
            if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
                return False
    except Exception:
        return False
    return True


def json_pointer(data: Any, pointer: str) -> Any:
    if pointer == "":
        return data
    if not pointer.startswith("/"):
        raise ValueError(f"invalid JSON pointer: {pointer}")
    value = data
    for token in pointer[1:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            value = value[int(token)]
        else:
            value = value[token]
    return value


def computed_control(fixture: dict[str, Any], control_name: str) -> Any:
    control = fixture["computed_controls"][control_name]
    text = read_real_text(fixture, control["source_key"])
    parse = control["parse"]
    if parse == "specification_number_from_title":
        match = re.search(r"^# Specification\s+(\d{3})\b", text, flags=re.MULTILINE)
        if not match:
            raise RuntimeError("could not parse latest specification number")
        return match.group(1)
    if parse == "incomplete_experiment_outcome_marker":
        if "INCOMPLETE" not in text:
            raise RuntimeError("could not establish INCOMPLETE experiment outcome")
        return "INCOMPLETE"
    raise RuntimeError(f"unknown computed-control parser: {parse}")


def transform_legacy(value: Any, transform: str | None) -> Any:
    if transform is None:
        return value
    if transform == "false_to_target_not_selected":
        if value is not False:
            raise RuntimeError("target-selection transform requires false input")
        return "TARGET_ARCHITECTURE_NOT_SELECTED"
    raise RuntimeError(f"unknown migration transform: {transform}")


def resolve_endpoint(
    fixture: dict[str, Any], endpoint: dict[str, Any], *, legacy: bool
) -> Any:
    if "computed_control" in endpoint:
        return computed_control(fixture, endpoint["computed_control"])
    source_key = endpoint["source_key"]
    if legacy:
        data = read_real_json(fixture, source_key)
    else:
        data = read_shadow_declaration(fixture, source_key)
    value = json_pointer(data, endpoint["json_pointer"])
    return transform_legacy(value, endpoint.get("transform")) if legacy else value


def migration_parity(fixture: dict[str, Any]) -> tuple[dict[str, bool], dict[str, Any]]:
    parity: dict[str, bool] = {}
    values: dict[str, Any] = {}
    for unit in fixture["migration_units"]:
        legacy_value = resolve_endpoint(fixture, unit["legacy"], legacy=True)
        successor_value = resolve_endpoint(fixture, unit["successor"], legacy=False)
        parity[unit["unit_id"]] = legacy_value == successor_value
        values[unit["unit_id"]] = {
            "semantic": unit["semantic"],
            "legacy": legacy_value,
            "successor": successor_value,
        }
    return parity, values


def validate_policy_grounding(fixture: dict[str, Any]) -> dict[str, bool]:
    checks: dict[str, bool] = {}
    for check in fixture["policy_checks"]:
        text = read_real_text(fixture, check["source_key"])
        checks[check["check_id"]] = check["must_contain"] in text
    return checks


def identity_and_provenance(fixture: dict[str, Any]) -> dict[str, Any]:
    active = read_shadow_declaration(fixture, "active_workstream")
    integration = read_shadow_declaration(fixture, "integration_boundary")
    migration = read_shadow_declaration(fixture, "migration_workstream")
    paths = {
        item["source_key"]: item["path"] for item in fixture["shadow_sources"]
    }
    ids = [active["semantic_id"], integration["semantic_id"], migration["semantic_id"]]
    path_used_as_identity = any(
        semantic_id in paths.values() or "/" in semantic_id or "\\" in semantic_id
        for semantic_id in ids
    )
    return {
        "active_workstream_semantic_id": active["semantic_id"],
        "integration_boundary_semantic_id": integration["semantic_id"],
        "migration_semantic_id": migration["semantic_id"],
        "path_used_as_semantic_identity": path_used_as_identity,
        "migration_source_commit": migration["migration_source_commit"],
        "all_sources_shadow_only": all(
            d["shadow_only"]
            for d in (active, integration, migration)
        ),
        "migration_provenance_bound_to_real_base": (
            migration["migration_source_commit"] == fixture["real_base_commit"]
            and f"current-authority-migration@{fixture['real_base_commit']}" in active["provenance"]
            and f"current-authority-migration@{fixture['real_base_commit']}" in integration["promotion_provenance"]
        ),
    }


def reverse_reference_measurements(fixture: dict[str, Any]) -> tuple[dict[str, int], int]:
    counts: dict[str, int] = {}
    for target in fixture["reverse_reference_targets"]:
        completed = subprocess.run(
            [
                "git",
                "grep",
                "-n",
                "-F",
                target,
                fixture["real_base_commit"],
                "--",
                "*.md",
                "*.json",
                "*.py",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        counts[target] = len([line for line in completed.stdout.splitlines() if line.strip()])

    migration = read_shadow_declaration(fixture, "migration_workstream")
    preserved_paths = set(migration["rollback"]["compatibility_paths"])
    # CONTINUITY remains an authored compatibility surface and is not migrated away.
    preserved_paths.add("docs/CONTINUITY.md")
    broken = sum(target not in preserved_paths for target in fixture["reverse_reference_targets"])
    return counts, broken


def build_rollback_routing(fixture: dict[str, Any]) -> dict[str, Any]:
    active = read_shadow_declaration(fixture, "active_workstream")
    integration = read_shadow_declaration(fixture, "integration_boundary")
    anchor = active["execution_anchor"]
    return {
        "schema_version": 1,
        "current_checkpoint": anchor["current_checkpoint"],
        "active_development_branch": anchor["active_development_branch"],
        "active_pr": anchor["active_pr"],
        "promoted_integration_branch": integration["promoted_branch"],
        "promoted_integration_sha": integration["promoted_commit"],
        "latest_specification": computed_control(fixture, "latest_specification"),
        "latest_experiment_outcome": computed_control(fixture, "latest_experiment_outcome"),
        "current_boundary": anchor["current_semantic_boundary"],
    }


def build_rollback_current_state(fixture: dict[str, Any], routing: dict[str, Any]) -> str:
    active = read_shadow_declaration(fixture, "active_workstream")
    migration = read_shadow_declaration(fixture, "migration_workstream")
    pr_text = "none" if routing["active_pr"] is None else f"#{routing['active_pr']}"
    return (
        "# Current State\n\n"
        f"**Checkpoint:** {routing['current_checkpoint']}\n"
        "**Date:** 2026-09-14\n"
        f"**Active development branch:** `{routing['active_development_branch']}`\n"
        f"**Active PR:** {pr_text}\n"
        f"**Promoted V1 integration branch:** `{routing['promoted_integration_branch']}` at `{routing['promoted_integration_sha']}`\n"
        f"**Latest specification:** Specification {routing['latest_specification']}\n"
        f"**Latest scientific experiment:** Specification 022 remains `{routing['latest_experiment_outcome']} / EXECUTION INTEGRITY FAILED`.\n\n"
        "## Current active stage\n\n"
        f"Research {active['research_id']}: {active['objective']}.\n"
        f"Selection state: `{active['selection_state']}`.\n"
        f"Migration phase: `{migration['migration_phase']}`.\n"
        f"Current operational authority: `{migration['current_operational_authority']}`.\n"
        f"Successor authority state: `{migration['successor_authority_state']}`.\n"
    )


def run_rollback_export(fixture: dict[str, Any]) -> dict[str, Any]:
    project_root = Path.cwd().resolve()
    live_paths = [project_root / "docs/current_routing.json", project_root / "docs/CURRENT_STATE.md"]
    before = {str(path): sha256_bytes(path.read_bytes()) for path in live_paths}

    routing = build_rollback_routing(fixture)
    legacy_routing = read_real_json(fixture, "current_routing")
    routing_exact_parity = routing == legacy_routing

    export_root = project_root / ".tmp" / "pka-c01-q9-migration-export"
    if export_root.exists():
        shutil.rmtree(export_root)
    (export_root / "docs/checkpoints").mkdir(parents=True, exist_ok=True)
    (export_root / "docs/current_routing.json").write_text(
        json.dumps(routing, indent=4) + "\n", encoding="utf-8"
    )
    (export_root / "docs/CURRENT_STATE.md").write_text(
        build_rollback_current_state(fixture, routing), encoding="utf-8"
    )
    checkpoint_item = source_map(fixture)[fixture["rollback_export_contract"]["checkpoint_source_key"]]
    checkpoint_bytes = git_blob(fixture, fixture["rollback_export_contract"]["checkpoint_source_key"])
    (export_root / "docs/checkpoints" / Path(checkpoint_item["path"]).name).write_bytes(checkpoint_bytes)

    checker_item = source_map(fixture)[fixture["rollback_export_contract"]["legacy_validator_source_key"]]
    checker_path = project_root / checker_item["path"]
    completed = subprocess.run(
        [
            sys.executable,
            str(checker_path),
            "--root",
            str(export_root),
            "--checked-branch",
            fixture["rollback_export_contract"]["checked_branch"],
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    validator_pass = completed.returncode == 0
    validator_output = (completed.stdout + completed.stderr).strip()

    shutil.rmtree(export_root)
    after = {str(path): sha256_bytes(path.read_bytes()) for path in live_paths}
    live_mutation = before != after

    return {
        "routing_exact_parity": routing_exact_parity,
        "legacy_validator_pass": validator_pass,
        "legacy_validator_output": validator_output,
        "live_authority_mutation_detected": live_mutation,
        "compatibility_path_count": len(fixture["rollback_export_contract"]["compatibility_paths"]),
        "exported_routing": routing,
    }


def public_integrity_pass() -> bool:
    completed = subprocess.run(
        [sys.executable, "scripts/check_repository_integrity.py"],
        capture_output=True,
        text=True,
        check=False,
    )
    return completed.returncode == 0 and "PUBLIC_REPOSITORY_INTEGRITY=PASS" in completed.stdout


def authority_switch_gate(
    fixture: dict[str, Any], rollback: dict[str, Any]
) -> dict[str, Any]:
    migration = read_shadow_declaration(fixture, "migration_workstream")
    qualification = migration["qualification"]
    blockers: list[str] = []
    if qualification["final_qualified_passes"] < qualification["frozen_item_count"]:
        blockers.append("FINAL_QUALIFICATION_INCOMPLETE")
    if qualification["target_selection_allowed"] is not True:
        blockers.append("TARGET_NOT_SELECTED")
    if migration.get("owner_target_acceptance") is not True:
        blockers.append("OWNER_TARGET_ACCEPTANCE_ABSENT")

    rollback_proof = (
        rollback["routing_exact_parity"]
        and rollback["legacy_validator_pass"]
        and not rollback["live_authority_mutation_detected"]
    )
    integrity_pass = public_integrity_pass()
    allowed = (
        not blockers
        and rollback_proof
        and integrity_pass
        and migration["authority_switch_requested"] is True
        and fixture["protocol"]["authority_switch_forbidden"] is False
    )
    return {
        "allowed": allowed,
        "current_operational_authority": migration["current_operational_authority"],
        "successor_authority_state": migration["successor_authority_state"],
        "authority_switch_requested": migration["authority_switch_requested"],
        "blockers": blockers,
        "rollback_proof": rollback_proof,
        "public_repository_integrity_pass": integrity_pass,
        "experiment_forbids_switch": fixture["protocol"]["authority_switch_forbidden"],
    }


def self_hosting_result(fixture: dict[str, Any]) -> dict[str, Any]:
    active = read_shadow_declaration(fixture, "active_workstream")
    migration = read_shadow_declaration(fixture, "migration_workstream")
    complete = (
        migration["parent"] == active["semantic_id"]
        and migration["semantic_id"] in active["active_children"]
        and migration["migration_phase"]
        and migration["current_operational_authority"]
        and migration["successor_authority_state"]
        and migration["next_action"]
        and "research:163" in migration["provenance"]
        and "checkpoint:508" in migration["provenance"]
    )
    return {
        "complete": bool(complete),
        "migration_phase": migration["migration_phase"],
        "parent": migration["parent"],
        "next_action": migration["next_action"],
    }


def run_probe(fixture: dict[str, Any], fixture_sha: str) -> dict[str, Any]:
    parity, values = migration_parity(fixture)
    policies = validate_policy_grounding(fixture)
    identity = identity_and_provenance(fixture)
    reverse_counts, broken_reverse = reverse_reference_measurements(fixture)
    rollback = run_rollback_export(fixture)
    switch = authority_switch_gate(fixture, rollback)
    self_hosting = self_hosting_result(fixture)

    support = (
        all_source_hashes_match(fixture)
        and all(parity.values())
        and all(policies.values())
        and identity["all_sources_shadow_only"]
        and identity["migration_provenance_bound_to_real_base"]
        and not identity["path_used_as_semantic_identity"]
        and broken_reverse == 0
        and rollback["routing_exact_parity"]
        and rollback["legacy_validator_pass"]
        and not rollback["live_authority_mutation_detected"]
        and switch["allowed"] is False
        and switch["current_operational_authority"] == "CURRENT_CONTINUITY_ARCHITECTURE"
        and switch["successor_authority_state"] == "SHADOW_ONLY"
        and self_hosting["complete"]
    )

    return {
        "schema_version": 1,
        "probe_id": "PKA-C01-Q9-MIGRATION-PROBE-V01",
        "candidate_id": fixture["candidate_id"],
        "fixture_id": fixture["fixture_id"],
        "real_base_commit": fixture["real_base_commit"],
        "fixture_sha256": fixture_sha,
        "shadow_only": True,
        "implementation_reads_oracle": False,
        "all_source_hashes_match": all_source_hashes_match(fixture),
        "migration_unit_parity": parity,
        "migration_values": values,
        "policy_grounding": policies,
        "identity_and_provenance": identity,
        "reverse_reference_counts": reverse_counts,
        "broken_reverse_reference_target_count": broken_reverse,
        "rollback_export": rollback,
        "authority_switch": switch,
        "self_hosting": self_hosting,
        "q9_shadow_subsystem_support": support,
        "interpretation": {
            "q9_final_qualification_claimed": False,
            "production_authority_migrated": False,
            "rollback_executed_against_live_authority": False,
            "target_architecture_selected": False,
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
