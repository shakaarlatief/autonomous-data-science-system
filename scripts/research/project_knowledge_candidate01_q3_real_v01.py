#!/usr/bin/env python3
"""Run Candidate 01's first real Q3 identity/relationship/temporal probe.

The probe is intentionally fixture-driven and oracle-blind. It reads the frozen
Candidate 01 shadow semantic sources plus exact real repository blobs at the
fixture's pinned commit, answers the case queries, measures representation
complexity, and evaluates the prospectively frozen H3/Object-Primary reopening
triggers. The current live repository is not mutated and the shadow sources do
not become project authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

EXPECTED_FIXTURE_SHA256 = "d30a3968e901b6f273a25ddef8d1ebbe093e1040e74f3ab80ba68ce523760ab6"
DEFAULT_FIXTURE = Path("docs/research/project_knowledge_candidate_01_q3_real_v01/Q3_REAL_FIXTURE_V01.json")
DEFAULT_OUTPUT = Path("docs/research/project_knowledge_candidate_01_q3_real_v01/RESULTS_V01.json")
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
    if fixture["protocol"]["implementation_may_read_oracle"] is not False:
        raise RuntimeError("fixture does not preserve the oracle-blind implementation contract")
    return fixture, digest


def git_blob(base_commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{base_commit}:{path}"])


def real_source_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["source_key"]: item for item in fixture["real_sources"]}


def shadow_source_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["source_key"]: item for item in fixture["shadow_sources"]}


def read_real_source(fixture: dict[str, Any], source_key: str) -> str:
    item = real_source_map(fixture)[source_key]
    raw = git_blob(fixture["real_base_commit"], item["path"])
    if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
        raise RuntimeError(f"real source drift: {source_key}")
    return raw.decode("utf-8")


def read_shadow_declaration(
    fixture: dict[str, Any], source_key: str
) -> dict[str, Any]:
    item = shadow_source_map(fixture)[source_key]
    raw = Path(item["path"]).read_bytes()
    if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
        raise RuntimeError(f"shadow source drift: {source_key}")
    match = DECLARATION_RE.search(raw.decode("utf-8"))
    if not match:
        raise RuntimeError(f"structured declaration missing: {source_key}")
    declaration = json.loads(match.group(1))
    if declaration.get("shadow_only") is not True:
        raise RuntimeError(f"shadow source lost shadow-only status: {source_key}")
    return declaration


def all_source_hashes_match(fixture: dict[str, Any]) -> bool:
    for item in fixture["real_sources"]:
        raw = git_blob(fixture["real_base_commit"], item["path"])
        if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
            return False
    for item in fixture["shadow_sources"]:
        raw = Path(item["path"]).read_bytes()
        if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
            return False
    return True


def require_all(text: str, tokens: list[str], case_id: str) -> None:
    missing = [token for token in tokens if token not in text]
    if missing:
        raise RuntimeError(f"{case_id}: real source missing expected grounded tokens: {missing}")


def resolve_case_r01(fixture: dict[str, Any]) -> dict[str, Any]:
    declaration = read_shadow_declaration(fixture, "decision_d015")
    real = read_real_source(fixture, "decisions")
    require_all(
        real,
        [
            "## D-015. Keep the currently attached learning materials outside the repository for now",
            "Superseded in architectural-uncertainty scope by D-033; durable public-Git exclusion outcome retained",
            "**Date:** 2026-08-07",
            "**Superseded in scope:** 2026-08-25",
        ],
        "Q3-R01",
    )
    relations = declaration["relations"]
    if len(relations) != 1 or relations[0]["mode"] != "REPLACE":
        raise RuntimeError("Q3-R01: unexpected successor relation structure")
    return {
        "successor_for_external_source_architecture_uncertainty": relations[0]["target"],
        "retained_outcomes": declaration["retained_outcomes"],
        "recorded_on": declaration["temporal"]["recorded_on"],
        "superseded_in_scope_on": declaration["temporal"]["superseded_in_scope_on"],
    }


def resolve_case_r02(fixture: dict[str, Any]) -> dict[str, Any]:
    declaration = read_shadow_declaration(fixture, "decision_d011")
    real = read_real_source(fixture, "decisions")
    require_all(
        real,
        [
            "## D-011. Do not select the implementation architecture yet",
            "D-028",
            "D-029",
            "D-030",
            "D-031",
            "D-032",
            "D-033",
            "still applicable to implementation subsystems not yet selected",
            "**Superseded in scope:** 2026-08-20, 2026-08-22, and 2026-08-25",
        ],
        "Q3-R02",
    )
    scope_successors = {
        relation["scope"]: relation["target"]
        for relation in declaration["relations"]
        if relation["mode"] == "REPLACE"
    }
    if len(scope_successors) != 6:
        raise RuntimeError("Q3-R02: expected six source-owned scoped successor relations")

    # Candidate 01 must not manufacture a per-successor timeline from the three
    # aggregate dates in the prose. The shadow declaration therefore records only
    # the decision's own recording date and leaves per-edge effective dates absent.
    invented_per_successor_effective_dates = any(
        any(key in relation for key in ("effective_from", "effective_on", "authority_from"))
        for relation in declaration["relations"]
    )
    return {
        "scope_successors": scope_successors,
        "residual_applicability": declaration["residual_applicability"],
        "invented_per_successor_effective_dates": invented_per_successor_effective_dates,
    }


def resolve_case_r03(fixture: dict[str, Any]) -> dict[str, Any]:
    declaration = read_shadow_declaration(fixture, "historical_intermediate")
    historical = read_real_source(fixture, "historical_intermediate")
    canonical = read_real_source(fixture, "canonical_checkpoint252")
    specification = read_real_source(fixture, "spec027")
    require_all(
        historical,
        [
            "**Original recorded identity:** `Checkpoint 252`",
            "Numbered identity retired on 2026-09-01",
            "docs/checkpoints/252_source_faithful_reintegration_interaction_integrity_gate.md",
        ],
        "Q3-R03",
    )
    require_all(
        canonical,
        ["# Checkpoint 252:", "advanced"],
        "Q3-R03",
    )
    require_all(
        specification,
        [
            "Original recorded identity` is provenance only",
            "reactivate the retired number",
            "create a second canonical checkpoint with that number",
        ],
        "Q3-R03",
    )
    git_history = subprocess.check_output(
        [
            "git",
            "log",
            "--follow",
            "--name-status",
            "--format=COMMIT %H",
            "--",
            declaration["current_carrier"],
        ]
    ).decode("utf-8")
    require_all(
        git_history,
        [
            f"COMMIT {declaration['carrier_history']['rename_commit']}",
            declaration["carrier_history"]["original_carrier"],
            declaration["current_carrier"],
        ],
        "Q3-R03",
    )
    identity_collision = (
        declaration["original_identity_disposition"] != "RETIRED_PROVENANCE_ONLY"
        or declaration["current_carrier"] == declaration["canonical_numeric_identity_owner"]
    )
    return {
        "semantic_id": declaration["semantic_id"],
        "current_carrier": declaration["current_carrier"],
        "original_recorded_identity": declaration["original_recorded_identity"],
        "original_identity_disposition": declaration["original_identity_disposition"],
        "canonical_numeric_identity_owner": declaration["canonical_numeric_identity_owner"],
        "rename_commit": declaration["carrier_history"]["rename_commit"],
        "identity_collision": identity_collision,
    }


def resolve_case_r04(fixture: dict[str, Any]) -> dict[str, Any]:
    declaration = read_shadow_declaration(fixture, "cockpit_workstream")
    real = read_real_source(fixture, "cockpit")
    require_all(
        real,
        [
            "**Status:** PAUSED / safely resumable next-generation Cockpit design and fidelity surface",
            "branch   v1-cockpit-design-exploration",
            "head     04f2a907094b8023ac7377c399a6eef1a6e1da99",
            "PAUSED",
            "not rejected",
            "not deleted",
            "not production-promoted",
        ],
        "Q3-R04",
    )
    return {
        "semantic_id": declaration["semantic_id"],
        "state": declaration["state"],
        "resume_branch": declaration["resume_anchor"]["branch"],
        "resume_head": declaration["resume_anchor"]["head"],
        "semantic_identity_preserved_while_paused": (
            declaration["state"] == "PAUSED"
            and declaration["epistemic_state"]
            == "PAUSED_NOT_REJECTED_NOT_DELETED_NOT_PROMOTED"
        ),
    }


def resolve_case_r05(fixture: dict[str, Any]) -> dict[str, Any]:
    declaration = read_shadow_declaration(fixture, "mc0013_review")
    state = json.loads(read_real_source(fixture, "mc0013_state"))
    message001 = read_real_source(fixture, "mc0013_message001")
    message003 = read_real_source(fixture, "mc0013_message003")
    require_all(
        message001,
        [
            "Claude Independent Architecture Counter-Design",
            "Independent substantive base    233eb932062a24473fcc4f4fe93160c952eea426",
            "I have not seen ChatGPT's candidate-family synthesis",
        ],
        "Q3-R05",
    )
    require_all(
        message003,
        [
            "Claude Comparative Architecture Critique",
            "Purpose                         Comparative critique",
        ],
        "Q3-R05",
    )
    if state["independence"]["status"] != declaration["current_epistemic_state"]:
        raise RuntimeError("Q3-R05: current epistemic state disagrees with frozen real STATE")
    if state["independence"]["review_base_ref"] != declaration["independent_phase"]["substantive_base"]:
        raise RuntimeError("Q3-R05: independent substantive base disagrees with frozen real STATE")
    exposures = "\n".join(state["independence"]["known_exposures"])
    require_all(
        exposures,
        [
            "Claude Message 001 is durably frozen at commit 9005b73add028398a827fdf5b251069c65a83208",
            "Comparative Phase 2 intentionally exposes Research 133 and ChatGPT Message 002",
        ],
        "Q3-R05",
    )
    return {
        "semantic_id": declaration["semantic_id"],
        "message001_role": declaration["independent_phase"]["epistemic_role"],
        "current_thread_state": declaration["current_epistemic_state"],
        "message003_and_later_role": declaration["comparative_phase"]["epistemic_role"],
        "independent_substantive_base": declaration["independent_phase"]["substantive_base"],
        "comparative_trigger": declaration["comparative_phase"]["trigger"],
    }


def resolve_real_semantics(fixture: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    resolvers = {
        "Q3-R01": resolve_case_r01,
        "Q3-R02": resolve_case_r02,
        "Q3-R03": resolve_case_r03,
        "Q3-R04": resolve_case_r04,
        "Q3-R05": resolve_case_r05,
    }
    resolved: dict[str, Any] = {}
    failures: list[str] = []
    for case in fixture["cases"]:
        case_id = case["case_id"]
        try:
            resolved[case_id] = resolvers[case_id](fixture)
        except Exception as exc:  # fail-visible case accounting is part of the experiment
            failures.append(f"{case_id}: {type(exc).__name__}: {exc}")
    return resolved, failures


def measure_complexity(fixture: dict[str, Any], query_failures: list[str]) -> dict[str, int]:
    declarations = {
        key: read_shadow_declaration(fixture, key)
        for key in shadow_source_map(fixture)
    }
    all_relations: list[tuple[str, str, str, str | None]] = []
    temporal_field_count = 0
    for declaration in declarations.values():
        for relation in declaration.get("relations", []):
            all_relations.append(
                (
                    declaration["semantic_id"],
                    relation["mode"],
                    relation["target"],
                    relation.get("scope"),
                )
            )
        temporal_field_count += len(declaration.get("temporal", {}))

    relation_counts = Counter(all_relations)
    duplicate_relation_count = sum(count - 1 for count in relation_counts.values() if count > 1)
    kinds = [declaration["kind"] for declaration in declarations.values()]

    return {
        "shadow_source_count": len(declarations),
        "source_local_relation_count": len(all_relations),
        "selective_temporal_field_count": temporal_field_count,
        "standalone_relation_source_count": sum(kind == "RELATION" for kind in kinds),
        "standalone_identity_transition_source_count": sum(
            kind in {"IDENTITY_TRANSITION", "SEMANTIC_TRANSITION"} for kind in kinds
        ),
        "joint_authority_source_count": sum(kind == "JOINT_AUTHORITY" for kind in kinds),
        "general_authoritative_registry_count": sum(
            kind in {"OBJECT_REGISTRY", "SEMANTIC_REGISTRY", "GENERAL_OBJECT_REGISTRY"}
            for kind in kinds
        ),
        "duplicated_authoritative_relation_count": duplicate_relation_count,
        # The five source profiles model only semantic units that independently need
        # structure. Related participants such as D-028..D-033 are not instantiated
        # as generic objects merely so relations can point to them.
        "universally_objectized_participant_count": 0,
        "real_semantic_query_failure_count": len(query_failures),
    }


def evaluate_h3_reopen(
    fixture: dict[str, Any], complexity: dict[str, int]
) -> tuple[bool, dict[str, bool]]:
    rules = fixture["protocol"]["h3_reopen_triggers"]
    relation_transition_sources = (
        complexity["standalone_relation_source_count"]
        + complexity["standalone_identity_transition_source_count"]
    )
    triggers = {
        "general_authoritative_object_registry_required": (
            complexity["general_authoritative_registry_count"] > 0
        ),
        "standalone_relation_or_transition_source_threshold_reached": (
            relation_transition_sources
            >= rules["standalone_relation_or_transition_source_threshold"]
        ),
        "duplicate_authoritative_relation_required": (
            complexity["duplicated_authoritative_relation_count"] > 0
        ),
        "universal_objectization_required": (
            complexity["universally_objectized_participant_count"] > 0
        ),
        "real_semantic_query_unresolvable": (
            complexity["real_semantic_query_failure_count"] > 0
        ),
    }
    return any(triggers.values()), triggers


def run_probe(fixture: dict[str, Any], fixture_sha: str) -> dict[str, Any]:
    semantics, failures = resolve_real_semantics(fixture)
    complexity = measure_complexity(fixture, failures)
    h3_reopen, h3_triggers = evaluate_h3_reopen(fixture, complexity)
    return {
        "schema_version": 1,
        "probe_id": "PKA-C01-Q3-REAL-PROBE-V01",
        "candidate_id": fixture["candidate_id"],
        "fixture_id": fixture["fixture_id"],
        "real_base_commit": fixture["real_base_commit"],
        "fixture_sha256": fixture_sha,
        "shadow_only": True,
        "implementation_reads_oracle": False,
        "all_source_hashes_match": all_source_hashes_match(fixture),
        "real_semantics_alignment": semantics,
        "real_semantic_query_failures": failures,
        "complexity": complexity,
        "h3_reopen_triggers": h3_triggers,
        "h3_reopen": h3_reopen,
        "interpretation": {
            "candidate01_real_q3_support": not failures and not h3_reopen,
            "q3_final_qualification_claimed": False,
            "unproven_real_transition_classes": ["MERGE", "SPLIT", "TOMBSTONE"],
            "architecture_family_selection_claimed": False,
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
