"""One real ADS knowledge-semantics candidate for accepted R0-P03-V2 M1.

This is a bounded *source qualification* and candidate-selection assay, not a
governing J1/J2/J3 event, a reconstructed historical acceptance, an arm
comparison, or independent reference gold. It deliberately RETURNS to the
Research 672-673 navigation objective and stops the previous provider receipt
line of research.

The candidate joins the real G006 semantic-identity engine with G013
full/incremental derived-view refresh and the original W5 subject architecture.
This is an actual cross-role Git history, not new synthetic carrier content.
Git chronology and historically reported accepted implementation gates must
NOT be interpreted as an accepted experimental J1 supersession or natural-
owner J2 COVERS statement. Those remain separate future admissions.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_real_content_source_frame_v01 as seed,
    v03_d1_accepted_semantic_projection_v01 as original_j1,
)

ROOT = Path(__file__).resolve().parents[2]
PIN = seed.PIN
OUTPUT = Path(__file__).with_name(
    "v03_real_pk_semantic_candidate_audit_result_v01.json"
)
G006 = "99cca3484f4dcb37128c38c2436a6dbcd6d00a0f"
G013 = "192dc161203577c11e7a7fce869634a5fccc29d8"
G006_PARENT = "256c5bfa253a9ad178e1fa578c028071cb26f6d2"
G013_PARENT = "abd752d3c604a382121e45773442de69ed4c01e1"
CANDIDATE_ID = "P03V2_PKA_IDENTITY_AND_DERIVED_REFRESH_REAL_SOURCES_V01"

# Hand-authored *eligibility inquiries* over immutable original project Git.
# Anchors are source identification witnesses, not newly authored truths.
WITNESSES = (
    ("G006_IMPLEMENTATION", "tools/project_knowledge/identity.py",
     "NATURAL_CODE_SOURCE", "def build_identity_index("),
    ("G006_MOVE_TEST", "tests/unit/test_project_knowledge_identity.py",
     "TEST_DEFINITION_NOT_EXECUTION",
     "def test_same_id_carrier_continuity_and_historical_representation(kind):"),
    ("G006_SUPERSEDE_TEST", "tests/unit/test_project_knowledge_identity.py",
     "TEST_DEFINITION_NOT_EXECUTION",
     "def test_supersede_preserves_history_and_explicit_current_successor():"),
    ("G006_DECISION_RECORD",
     "docs/research/181_w0_identity_transition_current_index_g006_result.md",
     "HISTORICAL_GATE_ACCEPTANCE_REPORTED_NOT_P03_J1",
     "**Status:** PKA-G006 ACCEPTED"),
    ("G013_REFRESH_IMPLEMENTATION", "tools/project_knowledge/services/refresh.py",
     "NATURAL_CODE_SOURCE", "def plan_view_refresh("),
    ("G013_VIEW_IMPLEMENTATION", "tools/project_knowledge/views.py",
     "NATURAL_CODE_SOURCE", "def build_views("),
    ("G013_EQUIVALENCE_TEST", "tests/unit/test_project_knowledge_refresh.py",
     "TEST_DEFINITION_NOT_EXECUTION",
     "def test_manifest_output_relocation_selects_only_that_view_and_matches_full_build(refresh_repo):"),
    ("G013_CROSS_SEMANTIC_TEST", "tests/unit/test_project_knowledge_refresh.py",
     "TEST_DEFINITION_NOT_EXECUTION",
     "def test_g006_same_identity_move_and_authored_transition_are_not_rename_heuristics(refresh_repo):"),
    ("G013_DECISION_RECORD",
     "docs/research/189_w0_full_incremental_rebuild_equivalence_g013_result.md",
     "HISTORICAL_GATE_ACCEPTANCE_REPORTED_NOT_P03_J1",
     "**Status:** PKA-G013 ACCEPTED"),
    ("SPEC_028",
     "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md",
     "ORIGINAL_FROZEN_CONTRACT_TEXT",
     "**Authority:** Frozen implementation contract subordinate to D-035 and Requirements V0.2."),
    ("D036_LOGICAL",
     "docs/DECISIONS.md",
     "HISTORICAL_LOGICAL_ARCHITECTURE_DECISION_SOURCE",
     "## D-036. Select THIN_CENTRED_HYBRID_V03 as the successor Project semantic/control architecture target"),
    ("W5_SUBJECTS",
     "docs/research/217_w5_t1_v02_controlled_subject_architecture_acceptance.md",
     "HISTORICAL_COMPARATOR_SOURCE",
     "**Authority:** W5 design result only."),
)

REQUIRED_G006_PATHS = {
    "tools/project_knowledge/identity.py",
    "tests/unit/test_project_knowledge_identity.py",
}
REQUIRED_G013_PATHS = {
    "tools/project_knowledge/services/refresh.py",
    "tests/unit/test_project_knowledge_refresh.py",
    "tools/project_knowledge/views.py",
}
REQUIRED_ORIGINAL_SUBSTRATE_ROLES = {
    "EXACT_SOURCE_IMPLEMENTATION_BYTES",
    "TEST_DEFINITION_NOT_EXECUTION",
    "HISTORICAL_NAVIGATION_EVIDENCE",
    "FROZEN_CONTRACT_TEXT",
}


def _git_bytes(*args: str) -> bytes:
    process = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, check=False,
    )
    if process.returncode:
        raise ValueError("CANDIDATE_GIT_ORIGINAL_SOURCE_UNAVAILABLE")
    return process.stdout


def _git(*args: str) -> str:
    return _git_bytes(*args).decode("utf8").strip()


def commit_facts(commit: str, expected_parent: str, required_paths: set[str]) -> dict:
    """Verify exact original Git revision, parent, changed-path provenance."""
    if _git("rev-parse", f"{commit}^{{commit}}") != commit:
        raise ValueError("CANDIDATE_ORIGINAL_COMMIT_CHANGED")
    parent = _git("show", "-s", "--format=%P", commit)
    if parent != expected_parent:
        raise ValueError("CANDIDATE_ORIGINAL_PARENT_CHANGED")
    paths = set(_git("diff-tree", "--no-commit-id", "--name-only", "-r", commit).splitlines())
    if not required_paths.issubset(paths):
        raise ValueError("CANDIDATE_ORIGINAL_IMPLEMENTATION_PATHS_ABSENT")
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", commit, PIN],
        cwd=ROOT, capture_output=True, check=False,
    )
    if ancestor.returncode:
        raise ValueError("CANDIDATE_COMMIT_NOT_IN_ORIGINAL_PIN_HISTORY")
    return {
        "commit": commit,
        "parent": parent,
        "changed_paths": sorted(paths),
        "required_path_subset_verified": True,
        "is_ancestor_of_original_source_pin": True,
        "proves_historical_p03_j1_or_j2": False,
    }


def witness(row: tuple[str, str, str, str], *, pin: str = PIN) -> dict[str, Any]:
    name, path, role, anchor = row
    if row not in WITNESSES:
        raise ValueError("CANDIDATE_UNAUTHORIZED_SOURCE_WITNESS")
    if pin != PIN:
        raise ValueError("CANDIDATE_SOURCE_PIN_NOT_APPROVED")
    original = _git_bytes("show", f"{PIN}:{path}")
    try:
        lines = original.decode("utf8", errors="strict").splitlines()
    except UnicodeDecodeError as error:
        raise ValueError("CANDIDATE_NON_UTF8_ORIGINAL_SOURCE") from error
    positions = [idx + 1 for idx, line in enumerate(lines) if anchor in line]
    if len(positions) != 1:
        raise ValueError("CANDIDATE_ORIGINAL_ANCHOR_NOT_UNIQUE")
    oid = _git("rev-parse", f"{PIN}:{path}")
    if len(oid) != 40:
        raise ValueError("CANDIDATE_INVALID_ORIGINAL_GIT_BLOB")
    return {
        "witness_id": name,
        "source_path": path,
        "source_commit": PIN,
        "source_role": role,
        "original_git_blob": oid,
        "original_sha256": sha256(original).hexdigest(),
        "original_byte_count": len(original),
        "anchor": anchor,
        "line_1based": positions[0],
        "authority": "VERIFIED_SOURCE_CONTENT_NOT_NEW_EXPERIMENT_J1_OR_J2",
    }


def evaluate() -> dict[str, Any]:
    base = seed.build()
    if base["source_commit"] != PIN or base["distinct_original_git_paths"] != 15:
        raise ValueError("PREEXISTING_ORIGINAL_SOURCE_FRAME_DRIFT")
    if not REQUIRED_ORIGINAL_SUBSTRATE_ROLES.issubset(set(base["roles"])):
        raise ValueError("PREEXISTING_SOURCE_ROLE_BOUNDARY_DRIFT")
    accepted = original_j1.build_accepted_projection()
    effects = accepted["accepted_j1"]["effects"]
    if (
        len(effects) != 4
        or accepted["j2_evidence"]["qualified_relational_count"] != 0
        or accepted["j3"]["new_experimental_completion_certified"] is not False
        or accepted["original_d1_raw_outcome"] != "D1_AMEND"
    ):
        raise ValueError("HISTORICAL_ACCEPTED_EXPERIMENT_SCOPE_DRIFT")
    entries = [witness(row) for row in WITNESSES]
    if len({e["witness_id"] for e in entries}) != len(entries):
        raise ValueError("CANDIDATE_DUPLICATED_SOURCE_WITNESS")
    paths = {e["source_path"] for e in entries}
    oldpaths = {r["source_path"] for r in base["witnesses"]}
    newpaths = paths - oldpaths
    if not newpaths:
        raise ValueError("CANDIDATE_NO_REAL_CONTENT_EXTENSION")
    original_events = {
        "G006": commit_facts(G006, G006_PARENT, REQUIRED_G006_PATHS),
        "G013": commit_facts(G013, G013_PARENT, REQUIRED_G013_PATHS),
    }
    return {
        "schema_version": 1,
        "status": "SOURCE_VERIFIED_CANDIDATE_ONLY_NOT_A_QUALIFIED_V03_WORLD",
        "world_candidate": CANDIDATE_ID,
        "scientific_method": "RESEARCH673_M1_M6_OWNER_ACCEPTED",
        "original_git_source_pin": PIN,
        "original_preexisting_source_frame": {
            "distinct_paths": base["distinct_original_git_paths"],
            "witness_count": base["source_witness_count"],
            "source_role_count": len(base["roles"]),
        },
        "additional_candidate_witnesses": entries,
        "additional_candidate_witness_count": len(entries),
        "candidate_distinct_paths": len(paths),
        "new_source_paths_not_in_original_fifteen": sorted(newpaths),
        "combined_unique_source_paths": len(paths | oldpaths),
        "original_git_implementation_events": original_events,
        "source_qualification": {
            "g006_identity_move_supersede_and_history": "GIT_CODE_AND_TEST_DEFINITIONS_PRESENT",
            "g013_refresh_and_rebuild_equivalence": "GIT_CODE_AND_TEST_DEFINITIONS_PRESENT",
            "cross_semantic_move_refresh_test": "GIT_TEST_DEFINITION_PRESENT_NOT_EXECUTION",
            "w5_subject_comparator": "ORIGINAL_HISTORICAL_W5_SOURCE_PRESENT",
            "documented_historical_gates": ["G006_REPORTED_ACCEPTED", "G013_REPORTED_ACCEPTED"],
            "historical_git_commits_form_chronology_not_j1_effect_supersession": True,
            "original_source_paths_are_not_j2_covers_declarations": True,
            "current_worktree_files_not_used_as_original_source_evidence": True,
        },
        "candidate_comparison": {
            "D1_HISTORICAL_ONLY": {
                "experiment_only_j1_accepted": len(effects),
                "qualified_j2_relational": 0,
                "historical_provider_transport": "SOURCE_ATTESTED_UNVERIFIED",
                "role": "RETAIN_AS_BOUNDED_UNKNOWN_NEGATIVE_CASE",
            },
            "G006_G013_PROJECT_KNOWLEDGE": {
                "original_source_history_observed": True,
                "cross_role_code_tests_documents": True,
                "real_identity_and_refresh_behavior_candidate": True,
                "new_owner_experiment_j1_accepted": False,
                "natural_owner_j2_covers_qualified": False,
                "role": "PREFERRED_SOURCE_CANDIDATE_NOT_YET_FORMAL_WORLD",
            },
            "GITHUB_CI_RECEIPT_CHAIN": {
                "provider_ci_outcome_source_observed": True,
                "enough_identity_lineage_and_semantic_breadth_alone": False,
                "role": "OPTIONAL_EVIDENCE_PERIPHERY_NOT_MAIN_WORLD",
            },
        },
        "next_required_substantive_steps": [
            "Design two genuinely successive, exact experiment-only accepted effect states, not inferred from chronological Git commits",
            "Present exact scoped owner packet for any newly authored experimental J1 effects; method-level Proceed is insufficient",
            "Identify actual source-carrier natural owners and a qualifying J2 COVERS declaration path without inventing testimony",
            "Execute one integrated J1/J2/lineage/currentness/J3 world with a real source revision and stale evidence negative case",
            "Freeze source sampling and ensure equal B0-B4 common semantic inputs and neutral lexical access",
            "Demonstrate the independent twelve-primary and nine-neutral-legacy Level B source/gold custody gates before formal scoring",
        ],
        "new_experiment_only_j1_effects_accepted": 0,
        "existing_d1_experiment_only_j1_effects": len(effects),
        "new_qualified_j2_relations": 0,
        "integrated_j3_completion": "NOT_RUN_HOLD_MISSING_ADMISSIONS",
        "twelve_primary_tasks_originated": False,
        "formal_b0_b4_scores": None,
        "physical_target_selected": False,
        "frozen_formal_world": False,
    }


def main() -> None:
    result = evaluate()
    content = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != content:
            raise RuntimeError("CANDIDATE_AUDIT_RECEIPT_IMMUTABLE_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as handle:
            handle.write(content)
    print(json.dumps({
        "status": result["status"],
        "source_paths": result["combined_unique_source_paths"],
        "new_paths": len(result["new_source_paths_not_in_original_fifteen"]),
        "accepted_old_j1": result["existing_d1_experiment_only_j1_effects"],
        "new_j1": result["new_experiment_only_j1_effects_accepted"],
        "qualified_j2": result["new_qualified_j2_relations"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
