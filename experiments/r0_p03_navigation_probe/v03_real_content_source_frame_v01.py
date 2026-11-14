"""Prospectively approved P03-V2: original-Git source-frame preadmission.

This reader pins actual repository source bytes and exact textual witnesses.
It does NOT encode V03 governing effects, source-owner J2 declarations, formal
scored tasks, hidden gold, or a selected physical architecture. Records
are an exposed coordinator's prospective seed, NOT the independently
adjudicated, arm-frozen corpus for Research 513's formal twelve tasks.

The output is deliberately source-relative. A named decision in a historical
document is not automatically a newly accepted J1 event. A test definition
is not a demonstrated test execution, and a workflow definition is not CI.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PIN = "5463b2ad2e6799339746637f38340fa2a9dc00f6"
OUTPUT = Path(__file__).with_name("v03_real_content_source_frame_result_v01.json")
# This curated role-stratified demonstration is NOT the formal 60/20 sample.
ROWS = (
    ("D035", "docs/DECISIONS.md", "HISTORICAL_SELECTED_DECISION_REPORTED",
     "## D-035. Select PKA-CANDIDATE-01 as the successor project-development knowledge architecture target"),
    ("D036", "docs/DECISIONS.md", "HISTORICAL_SELECTED_DECISION_REPORTED",
     "## D-036. Select THIN_CENTRED_HYBRID_V03 as the successor Project semantic/control architecture target"),
    ("SPEC028", "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md",
     "FROZEN_CONTRACT_TEXT", "**Authority:** Frozen implementation contract subordinate to D-035 and Requirements V0.2."),
    ("W5SUBJECT", "docs/research/217_w5_t1_v02_controlled_subject_architecture_acceptance.md",
     "HISTORICAL_NAVIGATION_EVIDENCE", "**Authority:** W5 design result only."),
    ("W5TARGET", "docs/research/218_w5_final_information_architecture_reconciliation_and_target_freeze.md",
     "HISTORICAL_NAVIGATION_PROPOSAL", "**Authority:** This record freezes the W5 target information architecture and authoring model."),
    ("CAND144", "docs/research/144_whole_architecture_candidate_repository_native_semantic_sources.md",
     "ARCHITECTURAL_CANDIDATE", "**Authority:** Candidate architecture research only."),
    ("CODE_ID", "tools/project_knowledge/identity.py", "EXACT_SOURCE_IMPLEMENTATION_BYTES",
     "def build_identity_index("),
    ("CODE_AUTH", "tools/project_knowledge/authority.py", "EXACT_SOURCE_IMPLEMENTATION_BYTES",
     "def resolve_authority("),
    ("CODE_CAPTURE", "tools/project_knowledge/capture.py", "EXACT_SOURCE_IMPLEMENTATION_BYTES",
     "def capture_record("),
    ("CODE_VIEW", "tools/project_knowledge/views.py", "EXACT_SOURCE_IMPLEMENTATION_BYTES",
     "def build_views("),
    ("TEST_ID", "tests/unit/test_project_knowledge_identity.py", "TEST_DEFINITION_NOT_EXECUTION",
     "def test_current_selective_and_unknown_identity():"),
    ("TEST_AUTH", "tests/unit/test_project_knowledge_authority.py", "TEST_DEFINITION_NOT_EXECUTION",
     "def test_scope_exact_match_truth_table("),
    ("TEST_CAPTURE", "tests/unit/test_project_knowledge_capture.py", "TEST_DEFINITION_NOT_EXECUTION",
     "def test_capture_record_preserves_both_provenance_forms_without_authority():"),
    ("DERIVED_ROUTING", "docs/current_routing.json", "DERIVED_ROUTING_STATUS_NOT_J1",
     '"current_checkpoint": 934'),
    ("CI_DEFINITION", ".github/workflows/repository-integrity.yml",
     "WORKFLOW_DEFINITION_NOT_EXECUTION", "name: Repository integrity"),
    ("CP522", "docs/checkpoints/522_candidate01_physical_architecture_v01_proposed_spec028_next.md",
     "DOCUMENTARY_CHECKPOINT_NOT_J1", "**Authority:** Research design only."),
)
# Every one of these proposed effect propositions is marked UNADMITTED.
# Its source witness supports only the exact documentary/source fact.
EFFECT_PROPOSALS = (
    {"candidate_id": "proposed:existing-target-028",
     "source_witness": "D035", "assertion": "D-035 records an architecture-selection decision",
     "status": "NOT_ADMITTED_EXPERIMENT_J1"},
    {"candidate_id": "proposed:logical-target-v03",
     "source_witness": "D036", "assertion": "D-036 records successor V03 logical-target selection",
     "status": "NOT_ADMITTED_EXPERIMENT_J1"},
    {"candidate_id": "proposed:revision-owned-identity",
     "source_witness": "CODE_ID", "assertion": "An existing implementation defines identity-index construction",
     "status": "NOT_ADMITTED_EXPERIMENT_J1"},
)


def git_bytes(path: str, *, pin: str = PIN) -> tuple[bytes, str]:
    """Read immutable exact Git blobs, independent of mutable worktree files."""
    # All source paths are fixed literal project-relative entries from ROWS.
    if path not in {row[1] for row in ROWS}:
        raise ValueError("Source path is not part of the approved seed inventory")
    if not pin or len(pin) != 40 or any(c not in "0123456789abcdef" for c in pin):
        raise ValueError("A full pinned hexadecimal source commit is required")
    p = subprocess.run(["git", "show", f"{pin}:{path}"], cwd=ROOT,
                       capture_output=True, check=False)
    if p.returncode:
        raise ValueError(f"Pinned source unavailable: {path}")
    sha = subprocess.run(["git", "hash-object", "--stdin"], cwd=ROOT,
                         input=p.stdout, capture_output=True, check=True).stdout.decode("ascii").strip()
    return p.stdout, sha


def witness_record(label: str, path: str, role: str, anchor: str) -> dict[str, Any]:
    content, blob = git_bytes(path)
    try:
        lines = content.decode("utf8", errors="strict").splitlines()
    except UnicodeDecodeError as error:
        raise ValueError(f"Non-UTF8 source: {path}") from error
    found = [(i + 1, line) for i, line in enumerate(lines) if anchor in line]
    if len(found) != 1:
        raise ValueError(f"Witness anchor must be unique at immutable source: {label}: {len(found)}")
    number, line = found[0]
    return {
        "witness_id": label,
        "source_path": path,
        "source_commit": PIN,
        "git_blob_oid": blob,
        "sha256": sha256(content).hexdigest(),
        "byte_count": len(content),
        "source_role_classification": role,
        "anchor_line": number,
        "exact_anchor": anchor,
        "witness_line_sha256": sha256(line.encode("utf8")).hexdigest(),
        "authority_verification": "SOURCE_FACT_ONLY_NOT_NEWLY_ACCEPTED_J1",
    }


def require_experimental_effect_admission(
    proposal: dict, *, owner_confirmation_record: dict | None = None,
) -> dict:
    """Fail closed until the specific experimental effect is owner-authorized.

    The user approved the P03-V2 scientific METHOD, not these proposal IDs.
    A fabricated actor/receipt or author-supplied event must never be accepted
    by this tool. A future separate, qualified admission contract is required.
    """
    if proposal not in EFFECT_PROPOSALS:
        raise ValueError("Unrecognized experimental governing proposition")
    if owner_confirmation_record is None:
        raise ValueError("EXPERIMENT_EFFECT_NOT_OWNER_RATIFIED")
    raise ValueError("EXPERIMENTAL_J1_ADMISSION_CONTRACT_NOT_IMPLEMENTED")


def build() -> dict[str, Any]:
    rows = [witness_record(*item) for item in ROWS]
    if len({r["witness_id"] for r in rows}) != len(rows):
        raise AssertionError("Duplicate source witness ID")
    roles = sorted({r["source_role_classification"] for r in rows})
    paths = sorted({r["source_path"] for r in rows})
    proposals = []
    witness_ids = {r["witness_id"] for r in rows}
    for p in EFFECT_PROPOSALS:
        if p["source_witness"] not in witness_ids:
            raise AssertionError("Unbound proposed effect witness")
        try:
            require_experimental_effect_admission(p)
        except ValueError as exc:
            if str(exc) != "EXPERIMENT_EFFECT_NOT_OWNER_RATIFIED":
                raise
        else:
            raise AssertionError("Unratified proposal was admitted")
        proposals.append(dict(p))
    return {
        "schema_version": 1,
        "experiment": "R0_P03_V2_REAL_CONTENT_PREADMISSION",
        "source_commit": PIN,
        "status": "PINNED_REAL_SOURCE_CANDIDATE_NOT_FORMAL_V03_WORLD",
        "distinct_original_git_paths": len(paths),
        "source_witness_count": len(rows),
        "roles": roles,
        "witnesses": rows,
        "effect_proposals": proposals,
        "accepted_experimental_j1_effects": [],
        "qualified_experimental_j2_relations": [],
        "formal_primary_tasks": [],
        "historical_legacy_gold": None,
        "formal_arm_scores": None,
        "scientific_admission": "HOLD",
        "unresolved_dependencies": [
            "Specific experimental J1 effect boundaries require separate owner ratification",
            "A V03-native single-world lineage/currentness/J2 contract is not yet qualified",
            "A natural-owner RELATIONAL fact and evidence-of-execution rule are not yet admitted",
            "The candidate is not the arm-frozen 60/20 formal source corpus",
            "Research 559 independent nine-case legacy gold and Level B custodial roles remain unqualified",
            "B0-B4 actual arm implementations, common-substrate parity and evaluator exposure are not frozen",
        ],
    }


def main() -> None:
    data = build()
    body = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text(encoding="utf8") != body:
            raise RuntimeError("Existing source-world receipt differs; refusing overwrite")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as handle:
            handle.write(body)
    print(json.dumps({
        "status": data["status"],
        "paths": data["distinct_original_git_paths"],
        "witnesses": data["source_witness_count"],
        "candidate_effects_unadmitted": len(data["effect_proposals"]),
        "experimental_j1_admitted": len(data["accepted_experimental_j1_effects"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
