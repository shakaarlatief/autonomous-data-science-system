"""Unscored, Git-pinned mixed-role corpus readiness and arm-neutral substrate audit.

The accepted R0-P03-V2 scientific method requires one real-content source
world, exact source/evidence roles and the same V03-native core for all B0-B4
comparators. A source count or path classification cannot establish any
individual carrier's semantic relevance, governing authority, currentness,
natural-owner J2 or eligibility for a formal scored sample.

This module builds a *candidate review packet*, not a selected 60/20 sample.
It intentionally cannot originate tasks, produce hidden gold, expose a
held-out split or award any navigation arm a PASS. It binds a small mixed-role
demonstration to immutable Git blob content and supplies an executable,
revision-locked lexical adapter plus a shared core projection contract.
B1-B4 navigation additions and actual arm runtimes are not implemented here.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import re
import subprocess
from typing import Any

from experiments.r0_p03_navigation_probe import (
    source_census,
    role_frame_candidate,
    v03_real_pk_delegated_s1_j3_lifecycle_v01 as j3,
)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REF = "17ea403ef64092f275e3c7d6492d99929804f8e5"
SEED = HERE / "v03_r0_p03_unscored_mixed_source_seed_v01.json"
SEED_SHA256 = "d10d1f4a5f50f082b73689f4858b2a4f003746969fb098add7e8fa9bedb7a6b4"
OUTPUT = HERE / "v03_r0_p03_unscored_mixed_source_cohort_readiness_result_v01.json"
COMMON_CONTRACT = HERE / "common_substrate_contract_candidate.json"
EXPECTED_SHARED = (
    "information_role_and_natural_owner",
    "accepted_effect_id_and_exact_governed_subject",
    "lineage_and_currentness",
    "completion",
    "j2_coverage",
    "evidence_receipts",
    "authority_class_labels",
    "lexical_full_text",
    "connector_readable_derived_orientation",
)
ARMS = ("B0", "B1", "B2", "B3", "B4")
NONCOMMON = frozenset({
    "research217_topical_memberships",
    "extra_editorial_about_links",
    "prospective_governed_navigation_concerns",
    "semantic_similarity_rankings",
})
CORE_FIELDS = frozenset({
    "source_ref", "source_witnesses", "shared_capabilities",
    "experimental_semantics", "lexical_adapter", "derived_orientation",
    "authority_boundary",
})


def canonical(value: Any) -> bytes:
    """Use unambiguous canonical UTF-8 payload bytes for parity diagnostics."""
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf8")


def source_roster() -> dict[str, str]:
    """Get committed blob OIDs directly, including workflow definitions."""
    return role_frame_candidate.committed_paths(
        ROOT, REF, roots=(*role_frame_candidate.SOURCE_ROOTS, ".github"),
    )


def git_blob(path: str, oid: str) -> bytes:
    """Read original source bytes and independently revalidate the blob OID."""
    proc = subprocess.run(
        ["git", "show", f"{REF}:{path}"], cwd=ROOT, capture_output=True,
    )
    if proc.returncode:
        raise ValueError("P03_COHORT_PINNED_GIT_SOURCE_NOT_AVAILABLE")
    data = proc.stdout
    digest = sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
    if digest != oid:
        raise ValueError("P03_COHORT_SOURCE_BLOB_IDENTITY_CONFLICT")
    return data


def load_seed() -> dict:
    """Only original literal coordinator seed is allowed, not a mutable reroll."""
    raw = SEED.read_bytes()
    if sha256(raw).hexdigest() != SEED_SHA256:
        raise ValueError("P03_COHORT_COORDINATOR_SEED_MUTATED")
    obj = json.loads(raw.decode("utf8"))
    if (
        set(obj) != {
            "schema_version", "manifest_id", "status",
            "original_git_source_ref", "provenance_class",
            "purpose", "prohibited", "sources",
        }
        or obj["schema_version"] != 1
        or obj["manifest_id"] != "P03V2_UNSCORED_MIXED_ROLE_SOURCE_SEED_001"
        or obj["original_git_source_ref"] != REF
        or obj["status"] != "NONFORMAL_ROLE_STRATIFIED_REVIEW_SEED_NOT_BUILD_OR_HELDOUT"
        or len(obj["sources"]) != 24
        or any(
            set(row) != {
                "path", "role_hypothesis", "eligibility",
                "role_is_not_accepted_authority",
            }
            or row["eligibility"] != "UNREVIEWED_SOURCE_ROLE_CANDIDATE"
            or row["role_is_not_accepted_authority"] is not True
            for row in obj["sources"]
        )
        or len({row["path"] for row in obj["sources"]}) != len(obj["sources"])
        or not any("HELDOUT" in rule for rule in obj["prohibited"])
    ):
        raise ValueError("P03_COHORT_SEED_NOT_A_CLOSED_UNSCORED_PROPOSAL")
    for row in obj["sources"]:
        path = row["path"]
        if (
            not isinstance(path, str)
            or path.startswith("/")
            or "\\" in path
            or ".." in Path(path).parts
            or path.startswith(("experiments/r0_p03_", "docs/research/69"))
        ):
            raise ValueError("P03_COHORT_SOURCE_ROLE_OR_LEAKAGE_PATH_NOT_ADMITTED")
    return obj


def witness_records(seed: dict) -> list[dict]:
    """Make byte-bound source records without upgrading path hints to truth."""
    inventory = source_roster()
    result = []
    for row in seed["sources"]:
        path = row["path"]
        if path not in inventory:
            raise ValueError("P03_COHORT_SEED_SOURCE_ABSENT_FROM_PINNED_GIT")
        oid = inventory[path]
        body = git_blob(path, oid)
        try:
            lines = body.decode("utf8", errors="strict").splitlines()
        except UnicodeDecodeError as exc:
            raise ValueError("P03_COHORT_SEED_SOURCE_NON_UTF8") from exc
        if not lines:
            raise ValueError("P03_COHORT_EMPTY_SOURCE_NOT_REVIEWED")
        result.append({
            "source_path": path,
            "source_ref": REF,
            "git_blob_oid": oid,
            "source_sha256": sha256(body).hexdigest(),
            "byte_count": len(body),
            "line_count": len(lines),
            "witness_line": 1,
            "witness_line_sha256": sha256(lines[0].encode("utf8")).hexdigest(),
            "role_hypothesis": row["role_hypothesis"],
            "role_status": row["eligibility"],
            "governing_authority_or_semantic_relevance_verified": False,
        })
    return result


def exact_lexical_hits(query: str, witnesses: list[dict], *, max_hits: int = 20) -> list[dict]:
    """A client-neutral, literal source search over precisely bounded Git blobs.

    This is executable lexical functionality, not a ranker, an answer oracle,
    accepted semantic role identification or the future full-corpus FTS engine.
    It is testable as one identical access primitive for every arm.
    """
    if (
        not isinstance(query, str)
        or not (1 <= len(query) <= 80)
        or not query.strip()
        or not isinstance(max_hits, int)
        or isinstance(max_hits, bool)
        or not 1 <= max_hits <= 100
    ):
        raise ValueError("P03_COHORT_LEXICAL_QUERY_CONTRACT")
    needle = query.casefold()
    found = []
    roster = source_roster()
    for row in sorted(witnesses, key=lambda x: x["source_path"]):
        path = row["source_path"]
        if row["source_ref"] != REF or roster.get(path) != row["git_blob_oid"]:
            raise ValueError("P03_COHORT_LEXICAL_SOURCE_PROVENANCE_CONFLICT")
        content = git_blob(path, roster[path])
        if sha256(content).hexdigest() != row["source_sha256"]:
            raise ValueError("P03_COHORT_LEXICAL_SOURCE_HASH_CONFLICT")
        for number, line in enumerate(content.decode("utf8").splitlines(), 1):
            if needle in line.casefold():
                found.append({
                    "source_path": path, "source_ref": REF,
                    "git_blob_oid": row["git_blob_oid"],
                    "line": number, "line_sha256": sha256(line.encode("utf8")).hexdigest(),
                    "match_class": "LITERAL_CASEFOLD_UNRANKED_NOT_AUTHORITY",
                })
                if len(found) == max_hits:
                    return found
    return found


def source_relative_semantics() -> dict:
    """Consume the accepted S1 result as bounded evidence, never production J1."""
    raw = j3.exact_git_file(
        REF,
        "experiments/r0_p03_navigation_probe/v03_real_pk_delegated_s1_j3_lifecycle_result_v01.json",
        "1b31365160e29b902d578222a8dc39e15c55b49e0e592448baeada13284b4341",
    )
    state = json.loads(raw.decode("utf8"))
    derived = state["derived_semantics"]
    if (
        state["world_id"] != "P03V2_PKA_IDENTITY_AND_DERIVED_REFRESH_REAL_SOURCES_V01"
        or state["status"] != "SEPARATE_EXPERIMENTAL_SOURCE_RELATIVE_J3_PREDICATE_PASS"
        or state["qualified_experiment_only_j2_count"] != 1
        or state["model_actor_independently_authenticated"] is not False
        or state["evaluator_independently_authored_blind"] is not False
        or state["formal_r0_p03"] != "INCOMPLETE"
        or state["production_authority_activated"] is not False
        or derived["current_effect_ids"] != [j3.E02, j3.E04]
        or derived["lineage_relation"] != "REPLACE"
        or derived["realization_succession"] != "OPEN_RESET"
        or derived["initial_successor_component_credit"] != 0
        or derived["previous_s0_evidence_carried"] is not False
        or derived["s1_composition"] != "ALL_REQUIRED"
        or derived["s1_component_count"] != 4
        or derived["s1_j3"] != j3.J3_PASS
        or derived["production_j3_satisfied"] is not False
    ):
        raise ValueError("P03_COHORT_EXPERIMENTAL_SEMANTIC_SOURCE_DRIFT")
    return {
        "status": "QUALIFIED_ONLY_WITHIN_BOUND_SOURCE_RELATIVE_EXPERIMENT",
        "world_id": state["world_id"],
        "source_event_git": state["source_event_commit"],
        "source_event_execution_git": state["new_event_execution_commit"],
        "accepted_j1_effects": [j3.E01, j3.E02, j3.E03, j3.E04],
        "current_effects": [j3.E02, j3.E04],
        "retired_effect": j3.E01,
        "lineage": "REPLACE / OPEN_RESET",
        "inherited_component_credit": 0,
        "qualifying_j2_count": 1,
        "j2_assurance": "EXPERIMENT_ONLY_SOURCE_RELATIVE_RELATIONAL_J2_WITH_DECLARED_WEAK_ACTOR_ASSURANCE",
        "j3_status": derived["s1_j3"],
        "component_evidence": list(j3.COMPONENT_TESTS),
        "receipt_source_ref": REF,
        "receipt_sha256": sha256(raw).hexdigest(),
        "independent_model_actor_authentication": False,
        "production_j2_j3_qualified": False,
        "nonsemantic_source_carriers_not_inferred_as_j1_j2": True,
    }


def common_projection(witnesses: list[dict], semantics: dict) -> dict:
    """Define the single neutral core without B1-B4 navigational additions."""
    contract = json.loads(COMMON_CONTRACT.read_text("utf8"))
    if (
        contract["state"] != "UNFROZEN_NONEXECUTING"
        or contract["shared_capabilities"]["all_arms"] != list(EXPECTED_SHARED)
        or set(contract["shared_capabilities"]["not_common_by_default"]) != NONCOMMON
        or set(contract["comparison_augmentations"]) != set(ARMS)
    ):
        raise ValueError("P03_COHORT_SHARED_CONTRACT_DRIFT")
    return {
        "source_ref": REF,
        "source_witnesses": witnesses,
        "shared_capabilities": list(EXPECTED_SHARED),
        "experimental_semantics": semantics,
        "lexical_adapter": {
            "mechanism": "EXACT_GIT_BLOB_LITERAL_CASEFOLD_UNRANKED",
            "source_revision": REF,
            "scope": "ONLY_24_UNSCORED_SEED_WITNESSES",
            "no_generated_navigation_authority": True,
            "same_callable_for_all_arms": True,
        },
        "derived_orientation": {
            "status": "EXPERIMENT_ONLY_DERIVED_NON_GOVERNING",
            "current_effect_ids": semantics["current_effects"],
            "source_receipt_sha256": semantics["receipt_sha256"],
            "on_source_change": "REVALIDATE_EXACT_SOURCE_DIGESTS",
            "deletion_does_not_CHANGE_GOVERNING_TRUTH": True,
        },
        "authority_boundary": {
            "experimental_v03_acceptance_not_production": True,
            "role_hypotheses_are_not_authority": True,
            "historical_carrier_does_not_imply_current_governing_truth": True,
            "generated_search_or_orientation_does_not_govern": True,
            "not_a_formal_scored_or_gold_packet": True,
        },
    }


def project_arm_common(arm: str, common: dict, additions: dict | None = None) -> bytes:
    """Render the exact same common subset; arm additions cannot overwrite it."""
    if arm not in ARMS or set(common) != CORE_FIELDS:
        raise ValueError("P03_COHORT_ARM_CORE_SCHEMA_OR_NAME_DRIFT")
    extras = {} if additions is None else additions
    if not isinstance(extras, dict):
        raise ValueError("P03_COHORT_ARM_ADDITIONS_MUST_BE_MAPPING")
    if any(
        key in CORE_FIELDS or key not in NONCOMMON
        for key in extras
    ):
        raise ValueError("P03_COHORT_ARM_ATTEMPT_TO_OVERRIDE_COMMON_AUTHORITY")
    if arm == "B0" and extras:
        raise ValueError("P03_COHORT_B0_MUST_HAVE_ZERO_ADDITIONS")
    # Existence of a constructible common projection proves only interface
    # comparability, not parity of unimplemented arm implementations.
    return canonical(common)


def build() -> dict:
    seed = load_seed()
    baseline = source_census.build_census(ROOT, REF)
    roles = role_frame_candidate.build_role_census(ROOT, REF)
    sources = witness_records(seed)
    if (
        baseline["source_ref"] != REF
        or baseline["sample_plan"]["build"] != 60
        or baseline["sample_plan"]["heldout"] != 20
        or len(baseline["strata"]) != 10
        or baseline["source_pool_size_unique_paths"] < 80
        or roles["source_ref"] != REF
        or roles["candidate_text_path_count"] < 80
        or len(sources) != 24
        or len(set(x["source_path"] for x in sources)) != len(sources)
    ):
        raise ValueError("P03_COHORT_CENSUS_CAPACITY_OR_PIN_INVALID")
    semantics = source_relative_semantics()
    common = common_projection(sources, semantics)
    rendered = {arm: sha256(project_arm_common(arm, common)).hexdigest() for arm in ARMS}
    if len(set(rendered.values())) != 1:
        raise ValueError("P03_COHORT_COMMON_ARM_BYTES_DIFFER")
    return {
        "schema_version": 1,
        "state": "UNSCORED_SOURCE_COHORT_AND_COMMON_INTERFACE_READINESS_ONLY",
        "source_git_revision": REF,
        "source_role_seed_sha256": SEED_SHA256,
        "candidate_evidence": {
            "markdown_path_count_not_semantically_eligible": baseline[
                "source_pool_size_unique_paths"
            ],
            "markdown_path_strata": len(baseline["strata"]),
            "multi_modality_reviewable_text_paths_not_semantically_eligible": roles[
                "candidate_text_path_count"
            ],
            "tracked_paths_in_role_census": roles["tracked_path_count"],
            "role_seed_path_count": len(sources),
            "seed_role_hint_counts": dict(sorted(Counter(
                x["role_hypothesis"] for x in sources
            ).items())),
            "role_seed_source_records": sources,
            "every_role_eligibility": "UNREVIEWED_CANDIDATE",
            "eligible_formal_carrier_count_established": 0,
        },
        "proposed_formal_sampling": {
            "target_build": 60, "target_heldout": 20,
            "eligibility_adjudicated": False,
            "sampling_selected": False,
            "heldout_paths_salt_or_keys_published": False,
            "historical_65_source_legacy_world_independent": True,
            "requires_independent_custodian_and_role_review": True,
        },
        "arm_neutral_interface_probe": {
            "common_core_sha256": next(iter(rendered.values())),
            "common_projection_sha256_by_arm": rendered,
            "core_fields": sorted(CORE_FIELDS),
            "shared_capabilities": list(EXPECTED_SHARED),
            "source_pinned_literal_lexical_callable_implemented": True,
            "arm_runtimes_implemented": False,
            "b1_b2_b3_b4_additions_implemented": False,
            "common_core_runtime_parity_qualified": False,
        },
        "experiment_semantic_status": semantics,
        "limits": [
            "Path and role-hypothesis counts do not show 80 semantically eligible or owner-adjudicated sources.",
            "The 24 role witnesses are a coordinator-authored, nonformal engineering seed, neither the build sample nor held-out members.",
            "Current experiment-only J1/J2/J3 source evidence is shared, with weak model-actor provenance; no historical source role is newly admitted by the seed.",
            "Only common-projection bytes and literal source access have a tested prototype; actual B0-B4 implementations/tool cost parity are not yet demonstrated.",
            "No scored primary or neutral legacy case, independent gold, protected packet, blind evaluator or physical target selection is established.",
        ],
        "formal_r0_p03": "INCOMPLETE",
        "production_authority_changed": False,
        "physical_target_selected": False,
    }


def main() -> None:
    result = build()
    content = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != content:
            raise RuntimeError("P03_COHORT_PROBE_IMMUTABLE_RESULT_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as target:
            target.write(content)
    print(json.dumps({
        "state": result["state"],
        "candidate_markdown_paths": result["candidate_evidence"][
            "markdown_path_count_not_semantically_eligible"
        ],
        "candidate_text_paths": result["candidate_evidence"][
            "multi_modality_reviewable_text_paths_not_semantically_eligible"
        ],
        "provisional_role_witnesses": result["candidate_evidence"]["role_seed_path_count"],
        "same_core_interface_hash": len(set(
            result["arm_neutral_interface_probe"]["common_projection_sha256_by_arm"].values()
        )) == 1,
        "formal_60_20_selected": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
