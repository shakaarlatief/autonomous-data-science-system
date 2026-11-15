"""Qualify the source-relative boundary of one prospective P03 S1 J2 event.

This module is deliberately a finite experimental verifier, not a production
J2 authority resolver. It uses actual Git objects to verify that a bounded
source carrier revision and a source-author COVERS declaration appeared in
the same commit, with a previously declared parent and closed scope.

Git co-location and exact source evidence cannot independently authenticate
a model actor or grant a natural-owner realization relation. The only
permitted result is source-structural verification with a separately visible
owner-assurance HOLD until a genuine authority mechanism qualifies it.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_accepted_j1_projection_v01 as accepted,
    v03_real_pk_source_transition_v01 as previous,
)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "v03_real_pk_prospective_j2_source_assay_result_v01.json"
BRANCH = "v1-source-vault-bootstrap-resume"
BEFORE = "experiments/r0_p03_navigation_probe/real_pk_world/current/identity_carrier_v01.json"
AFTER = "experiments/r0_p03_navigation_probe/real_pk_world/prospective_s1/identity_carrier_v02.json"
CLAIM = "experiments/r0_p03_navigation_probe/real_pk_world/prospective_s1/realizes_s1_at_action_v01.json"
REALIZER = "P03PKA.EXPERIMENT_SOURCE_CARRIER_TRANSITION_002"
COMPONENTS = (
    "EXPLICIT_IDENTITY_PRESERVING_MOVE",
    "AFFECTED_VIEW_REFRESH_SELECTED",
    "INCREMENTAL_EQUALS_CURRENT_FULL_BUILD",
    "STALE_DERIVED_RESULT_NOT_GOVERNING",
)
EFFECT = "P03PKA-E02-S1-IDENTITY-REFRESH"
EXPECTED_CHANGES = (("D", BEFORE), ("A", AFTER), ("A", CLAIM))


def _git(*args: str) -> bytes:
    process = subprocess.run(
        ["git", *args], cwd=ROOT, check=False, capture_output=True,
    )
    if process.returncode:
        raise ValueError("P03_S1_ACTUAL_GIT_SOURCE_UNAVAILABLE:" + process.stderr.decode("utf8", "replace")[-300:])
    return process.stdout


def _json(raw: bytes) -> dict[str, Any]:
    try:
        data = json.loads(raw.decode("utf8"))
    except (ValueError, UnicodeError) as exc:
        raise ValueError("P03_S1_EXACT_GIT_JSON_INVALID") from exc
    if not isinstance(data, dict):
        raise ValueError("P03_S1_SOURCE_RECORD_MUST_BE_OBJECT")
    return data


def validate_claim(claim: dict[str, Any], parent: str) -> None:
    """Reject structural forgery without confusing the claim with an attestation."""
    if set(claim) != {
        "schema_version", "world_id", "record_class", "fact_class",
        "author_statement", "relational_claim", "source_action",
        "authority_exclusions", "s1_activation", "j3_status",
    }:
        raise ValueError("P03_S1_J2_CLAIM_CLOSED_SCHEMA")
    author = claim["author_statement"]
    relation = claim["relational_claim"]
    action = claim["source_action"]
    if not all(isinstance(item, dict) for item in (author, relation, action)):
        raise ValueError("P03_S1_J2_CLAIM_NESTED_SCHEMA")
    if set(author) != {
        "claimed_role", "natural_owner_scope", "claimant_identity_assurance",
        "independently_authenticated_actor", "provider_receipt_verified",
        "claim_made_before_action",
    } or set(relation) != {
        "relation", "target_accepted_effect_id", "realizer_id",
        "component_ids", "coverage_status",
    } or set(action) != {
        "operation", "expected_branch", "expected_parent_sha",
        "previous_source_commit", "previous_path", "new_path",
        "declaration_path", "commit_sha_known_before_action",
        "expected_changed_paths",
    }:
        raise ValueError("P03_S1_J2_NESTED_CLOSED_SCHEMA")
    if (
        claim["schema_version"] != 1
        or claim["world_id"] != accepted.EXPERIMENT_ID
        or claim["record_class"] != "AT_ACTION_EXPERIMENT_SOURCE_OWNER_COVERS_CANDIDATE"
        or claim["fact_class"] != "RELATIONAL_SOURCE_AUTHOR_ASSERTION"
        or claim["s1_activation"] != "NOT_ACTIVATED"
        or claim["j3_status"] != "HOLD_J2_OWNER_ASSURANCE"
        or author["claimed_role"] != "EXPOSED_CHATGPT_EXPERIMENT_SOURCE_AUTHOR"
        or author["natural_owner_scope"] != "THIS_P03_PROSPECTIVE_SOURCE_REVISION_ONLY"
        or author["claimant_identity_assurance"] != "MODEL_CONVERSATION_CLAIM_NOT_INDEPENDENTLY_AUTHENTICATED"
        or author["independently_authenticated_actor"] is not False
        or author["provider_receipt_verified"] is not False
        or author["claim_made_before_action"] is not True
        or relation["relation"] != "COVERS"
        or relation["target_accepted_effect_id"] != EFFECT
        or relation["realizer_id"] != REALIZER
        or relation["component_ids"] != list(COMPONENTS)
        or relation["coverage_status"] != "PROPOSED_PENDING_ACTUAL_EXECUTION_AND_OWNER_QUALIFICATION"
        or action["operation"] != "ACTUAL_REPRESENTATION_REPLACEMENT_WITH_COCOMMITTED_CLAIM"
        or action["expected_branch"] != BRANCH
        or action["expected_parent_sha"] != parent
        or action["previous_source_commit"] != previous.REPLACEMENT_COMMIT
        or action["previous_path"] != BEFORE
        or action["new_path"] != AFTER
        or action["declaration_path"] != CLAIM
        or action["commit_sha_known_before_action"] is not False
        or action["expected_changed_paths"] != [
            {"status": status, "path": path} for status, path in EXPECTED_CHANGES
        ]
        or claim["authority_exclusions"] != [
            "NO_INDEPENDENT_MODEL_ACTOR_PROOF",
            "NO_AUTHENTICATED_NATURAL_OWNER_RELATIONAL_J2",
            "NO_S1_ACTIVATION",
            "NO_J3_SATISFIED",
            "NO_PRODUCTION_OR_PHYSICAL_TARGET_AUTHORITY",
            "NO_FORMAL_B0_B4_SCORE",
        ]
    ):
        raise ValueError("P03_S1_J2_CLAIM_SCOPE_OR_ASSURANCE_FORGERY")


def validate_carrier(before: dict[str, Any], after: dict[str, Any], parent: str) -> None:
    """Constrain the source carrier without assigning governing effects to paths."""
    if set(after) != set(before):
        raise ValueError("P03_S1_CARRIER_REPRESENTATION_SCHEMA_CHANGED")
    if before["governed_source"] != after["governed_source"]:
        raise ValueError("P03_S1_AUTHORED_SEMANTIC_ID_OR_FIELDS_DRIFT")
    if after["governed_source"]["semantic_id"] != previous.AUTHORED_ID:
        raise ValueError("P03_S1_AUTHORED_IDENTITY_NOT_PRESERVED")
    if (
        after["accepted_effect_ref"] != EFFECT
        or after["asserted_implementation_coverage"] is not None
        or after["world_id"] != accepted.EXPERIMENT_ID
        or after["production_authority"] is not False
        or after["no_formal_task_or_score"] is not True
        or after["lifecycle_stage"] != "S1_SOURCE_CANDIDATE_NOT_GOVERNING_ACTIVATION"
    ):
        raise ValueError("P03_S1_SOURCE_CARRIER_FALSE_AUTHORITY")
    provenance = after["revision_provenance"]
    if (
        provenance["current_source_path"] != AFTER
        or provenance["previous_source_path"] != BEFORE
        or provenance["prior_git_commit"] != previous.REPLACEMENT_COMMIT
        or provenance["semantic_id_invariant"] != previous.AUTHORED_ID
        or provenance["git_successor_commit"] != "UNAVAILABLE_UNTIL_COMMIT"
        or provenance["natural_owner_j2_coverage"] != "UNQUALIFIED"
        or provenance["successor_j1_activation"] != "NOT_ACTIVATED"
        or provenance["expected_action_parent"] != parent
    ):
        raise ValueError("P03_S1_SOURCE_CARRIER_REVISION_PROVENANCE_FALSE")
    owner = after["source_owner_claim"]
    if (
        owner["actor"] != "EXPOSED_CHATGPT_COORDINATOR"
        or owner["claim_class"] != "AT_ACTION_AUTHOR_CLAIM_NOT_INDEPENDENTLY_AUTHENTICATED"
        or owner["natural_owner_relational_j2_qualified"] is not False
    ):
        raise ValueError("P03_S1_SOURCE_OWNER_AUTHENTICATION_FORGERY")


def evaluate(commit: str) -> dict[str, Any]:
    """Read one exact actual Git commit and enforce source-only authority limits."""
    if not re.fullmatch("[0-9a-f]{40}", commit):
        raise ValueError("P03_S1_COMMIT_ID_REQUIRED")
    parent = _git("rev-parse", f"{commit}^").decode("ascii").strip()
    actual = _git("diff", "--no-renames", "--name-status", parent, commit).decode("utf8").splitlines()
    changes = tuple(tuple(line.split("\t", 1)) for line in actual)
    if sorted(changes) != sorted(EXPECTED_CHANGES):
        raise ValueError("P03_S1_GIT_EVENT_UNEXPECTED_CHANGED_PATHS")
    prior_bytes = _git("show", f"{parent}:{BEFORE}")
    after_bytes = _git("show", f"{commit}:{AFTER}")
    claim_bytes = _git("show", f"{commit}:{CLAIM}")
    if sha256(prior_bytes).hexdigest() != previous.REPLACEMENT_SHA256:
        raise ValueError("P03_S1_PREVIOUS_CARRIER_DIGEST_DRIFT")
    before = _json(prior_bytes)
    after = _json(after_bytes)
    declaration = _json(claim_bytes)
    accepted_record = accepted.build()
    if (
        accepted_record["accepted_j1"]["effects"][1]["id"] != EFFECT
        or accepted_record["accepted_j1"]["effects"][1]["completion_contract"]["required_components"] != list(COMPONENTS)
        or accepted_record["currentness"]["activation_status"] != "NOT_ACTIVATED"
        or accepted_record["j2"]["qualified_count"] != 0
    ):
        raise ValueError("P03_S1_ACCEPTED_J1_OR_ASSURANCE_UNEXPECTEDLY_CHANGED")
    validate_claim(declaration, parent)
    validate_carrier(before, after, parent)
    if _git("ls-tree", "--name-only", commit, BEFORE).strip():
        raise ValueError("P03_S1_PREDECESSOR_CARRIER_STILL_CURRENT")
    return {
        "schema_version": 1,
        "status": "SOURCE_COCOMMIT_AND_GIT_TRANSITION_VERIFIED_J2_OWNER_ASSURANCE_HOLD",
        "commit": commit,
        "parent": parent,
        "git_exact_changes": [{"status": s, "path": p} for s, p in changes],
        "source_digests": {
            "previous_carrier": sha256(prior_bytes).hexdigest(),
            "prospective_carrier": sha256(after_bytes).hexdigest(),
            "cocommitted_claim": sha256(claim_bytes).hexdigest(),
        },
        "accepted_effect": EFFECT,
        "component_ids": list(COMPONENTS),
        "semantic_identity": previous.AUTHORED_ID,
        "same_authored_semantic_source": True,
        "declaration_present_in_same_commit": True,
        "git_observable_verified": True,
        "source_owner_claim_independently_authenticated": False,
        "claimed_relational_J2_qualified": False,
        "component_execution_verified_for_this_transition": False,
        "S1_activated": False,
        "J3": "HOLD_J2_OWNER_ASSURANCE_AND_NEW_EVENT_EXECUTION",
        "formal_R0_P03": "INCOMPLETE",
        "production_authority_changed": False,
        "physical_architecture_selected": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--event-commit", required=True)
    args = parser.parse_args()
    result = evaluate(args.event_commit)
    rendered = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if OUTPUT.exists() and OUTPUT.read_text("utf8") != rendered:
        raise RuntimeError("P03_S1_J2_EXACT_GIT_RECEIPT_IMMUTABLE_CONFLICT")
    if not OUTPUT.exists():
        with OUTPUT.open("x", encoding="utf8", newline="\n") as file:
            file.write(rendered)
    print(json.dumps({
        "status": result["status"], "git_commit": result["commit"],
        "qualified_relational_J2": result["claimed_relational_J2_qualified"],
        "J3": result["J3"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
