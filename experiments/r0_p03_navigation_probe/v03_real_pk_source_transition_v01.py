"""Real two-commit P03-V2 carrier transition evaluated by the production G006 engine.

The source before/after views are retrieved from immutable Git commits.
The current authored carrier contains an explicit source-local predecessor,
successor, and invariant semantic ID, but those fields are *not* a qualified
RELATIONAL J2 COVERS declaration. We translate this source-authored experiment
relationship into an isolated identity-transition.v1 value and invoke the
actual Project Knowledge identity-index implementation.

This is a source-relative OBSERVABLE identity/currentness test, not an
assertion about who created the Git commits or the historical implementation
owner's intention. Source-owner and J3 gates remain unresolved.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

from tools.project_knowledge.adapters.schema import SchemaValidator
from tools.project_knowledge.identity import (
    build_identity_index, historical_lookup, resolve_identity,
    serialize_identity_index, transition_from_source,
)
from tools.project_knowledge.model import (
    AuthorityClass, GovernedSource, HashBasis, Profile, RawDeclaration,
    SemanticId, SnapshotMode, SourceRevision,
)

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_accepted_j1_projection_v01 as accepted,
)

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "v03_real_pk_source_transition_result_v01.json"

INITIAL_COMMIT = "10cad3cb0a885135579f00f3a887a3c090f65352"
INITIAL_PARENT = "ed1c379f31fadc47a62189363720e0cfb9390afa"
REPLACEMENT_COMMIT = "cac152cfe6c2133ffd46cf7fa3b7e0b99d015cb4"
INITIAL_PATH = "experiments/r0_p03_navigation_probe/real_pk_world/initial/identity_carrier_v01.json"
REPLACEMENT_PATH = "experiments/r0_p03_navigation_probe/real_pk_world/current/identity_carrier_v01.json"
INITIAL_SHA256 = "effcbcf0bdd54576f9611a5381ab900490561cd762fb3f1985096b6ac92703b2"
REPLACEMENT_SHA256 = "d618807f510a4400ec62e1d25b931c6810e9b4928e8c348317ecd54db89d8b32"
AUTHORED_ID = "P03PKA.G006.IDENTITY.CONTINUITY"
RELATION = "REPRESENTATION_REPLACEMENT"
MODE = SnapshotMode.COMMIT_SNAPSHOT
VALIDATOR = SchemaValidator()


def git(*args: str) -> bytes:
    result = subprocess.run(["git", *args], cwd=ROOT,
                            capture_output=True, check=False)
    if result.returncode:
        raise ValueError("P03_REAL_GIT_SOURCE_UNAVAILABLE")
    return result.stdout


def git_text(*args: str) -> str:
    return git(*args).decode("utf8").strip()


def committed_carriers() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Verify both actual Git revisions before generating any derived semantics."""
    for commit, parent in (
        (INITIAL_COMMIT, INITIAL_PARENT),
        (REPLACEMENT_COMMIT, INITIAL_COMMIT),
    ):
        if git_text("rev-parse", f"{commit}^{{commit}}") != commit:
            raise ValueError("P03_REAL_SOURCE_COMMIT_DRIFT")
        if git_text("show", "-s", "--format=%P", commit) != parent:
            raise ValueError("P03_REAL_SOURCE_PARENT_DRIFT")
    changes = set(git_text("diff-tree", "--no-commit-id", "--name-only", "-r",
                           REPLACEMENT_COMMIT).splitlines())
    if changes != {INITIAL_PATH, REPLACEMENT_PATH}:
        raise ValueError("P03_REPRESENTATION_REPLACEMENT_CHANGED_WRONG_FILES")
    before_raw = git("show", f"{INITIAL_COMMIT}:{INITIAL_PATH}")
    after_raw = git("show", f"{REPLACEMENT_COMMIT}:{REPLACEMENT_PATH}")
    if (
        sha256(before_raw).hexdigest() != INITIAL_SHA256
        or sha256(after_raw).hexdigest() != REPLACEMENT_SHA256
        or before_raw == after_raw
    ):
        raise ValueError("P03_REAL_SOURCE_BYTE_EVIDENCE_CHANGED")
    if (BASE / "real_pk_world/current/identity_carrier_v01.json").read_bytes() != after_raw:
        raise ValueError("P03_CURRENT_CARRIER_WORKTREE_DRIFT")
    if subprocess.run(
        ["git", "cat-file", "-e", f"{REPLACEMENT_COMMIT}:{INITIAL_PATH}"],
        cwd=ROOT, capture_output=True,
    ).returncode == 0:
        raise ValueError("P03_OLD_SOURCE_PATH_STILL_CURRENT")
    original = json.loads(before_raw.decode("utf8"))
    current = json.loads(after_raw.decode("utf8"))
    for record in (original, current):
        if (
            record["world_id"] != accepted.EXPERIMENT_ID
            or record["production_authority"] is not False
            or record["governed_source"]["semantic_id"] != AUTHORED_ID
            or record["governed_source"]["authority_class"] != "canonical"
            or record["source_owner_claim"]["natural_owner_relational_j2_qualified"] is not False
        ):
            raise ValueError("P03_EXPERIMENT_CARRIER_SCOPE_OR_IDENTITY_CHANGED")
        if VALIDATOR.validate(RawDeclaration(record["governed_source"])):
            raise ValueError("P03_REAL_SOURCE_CARRIER_SCHEMA_INVALID")
    provenance = current["revision_provenance"]
    if provenance != {
        "event_class": "ACTUAL_PROSPECTIVE_EXPERIMENT_SOURCE_REPRESENTATION_CHANGE",
        "previous_source_path": INITIAL_PATH,
        "current_source_path": REPLACEMENT_PATH,
        "semantic_id_invariant": AUTHORED_ID,
        "prior_git_commit": INITIAL_COMMIT,
        "git_successor_commit": "UNAVAILABLE_UNTIL_COMMIT",
        "authority_claim": "EXPERIMENT_ONLY_SOURCE_RECORD_NOT_GOVERNING_PROJECT_AUTHORITY",
        "natural_owner_j2_coverage": "UNQUALIFIED",
        "successor_j1_activation": "NOT_ACTIVATED",
    }:
        raise ValueError("P03_SOURCE_LOCAL_TRANSITION_CLAIM_OR_ASSURANCE_DRIFT")
    if len(current["expanded_real_ads_source_witnesses"]) != 5:
        raise ValueError("P03_G013_REAL_SOURCE_REFERENCES_ABSENT")
    return original, current, {
        "initial_commit": INITIAL_COMMIT,
        "replacement_commit": REPLACEMENT_COMMIT,
        "initial_parent": INITIAL_PARENT,
        "initial_path": INITIAL_PATH,
        "replacement_path": REPLACEMENT_PATH,
        "initial_sha256": INITIAL_SHA256,
        "replacement_sha256": REPLACEMENT_SHA256,
        "git_changed_paths": sorted(changes),
        "both_exact_source_revisions_verified": True,
    }


def _source(record: dict, *, path: str, commit: str,
            digest: str, historical: bool) -> GovernedSource:
    """Project source role at queried time; historical role is a derived view.

    Both immutable files *were* experiment-canonical at their own commit.
    When querying the successor snapshot, the old committed representation is
    projected to historical authority and the new representation to current.
    No changed filename or lexical sort is permitted to establish identity.
    """
    fields = dict(record["governed_source"])
    if historical:
        fields["authority_class"] = "historical"
    raw = RawDeclaration(fields)
    if VALIDATOR.validate(raw):
        raise ValueError("P03_PROJECTED_SOURCE_SCHEMA_INVALID")
    return GovernedSource(
        carrier_path=path,
        profile=Profile.SEMANTIC_SOURCE,
        authority_class=AuthorityClass.HISTORICAL if historical else AuthorityClass.CANONICAL,
        kind=fields["kind"],
        declaration=raw,
        snapshot_mode=MODE,
        semantic_id=SemanticId(AUTHORED_ID),
        revision=SourceRevision(
            source_path=path, source_commit=commit,
            hash_algorithm="sha256", hash_basis=HashBasis.GIT_BLOB_BYTES_AT_COMMIT,
            content_digest=digest, snapshot_mode=MODE,
        ),
    )


def _transition(current: dict) -> Any:
    """Translate the carrier's actual explicit same-ID relation, not Git inference."""
    claim = current["revision_provenance"]
    if (
        claim["event_class"] != "ACTUAL_PROSPECTIVE_EXPERIMENT_SOURCE_REPRESENTATION_CHANGE"
        or claim["semantic_id_invariant"] != AUTHORED_ID
        or claim["previous_source_path"] != INITIAL_PATH
        or claim["current_source_path"] != REPLACEMENT_PATH
        or claim["natural_owner_j2_coverage"] != "UNQUALIFIED"
        or claim["successor_j1_activation"] != "NOT_ACTIVATED"
    ):
        raise ValueError("SOURCE_CARRIER_DOES_NOT_DECLARE_THIS_EXPERIMENT_TRANSITION")
    declaration = {
        "schema_version": "1",
        "profile": "identity_transition.v1",
        "kind": "p03-experiment-source-representation-event",
        "authority_class": "canonical",
        "transition_class": RELATION,
        "predecessors": [AUTHORED_ID],
        "successors": [AUTHORED_ID],
        "resolution_behavior": (
            "A prospective source-owned replacement retains the identical "
            "authored semantic identity and historical carrier"
        ),
        "provenance": [claim["previous_source_path"], claim["current_source_path"]],
    }
    if VALIDATOR.validate(RawDeclaration(declaration)):
        raise ValueError("P03_EXPERIMENT_TRANSITION_SCHEMA_INVALID")
    event_source = GovernedSource(
        carrier_path=REPLACEMENT_PATH,
        profile=Profile.IDENTITY_TRANSITION,
        authority_class=AuthorityClass.CANONICAL,
        kind=declaration["kind"], declaration=RawDeclaration(declaration),
        snapshot_mode=MODE,
    )
    return transition_from_source(event_source)


def build() -> dict[str, Any]:
    """Execute actual production G006 semantics on committed before/after sources."""
    accepted_state = accepted.build()
    if (
        accepted_state["accepted_j1"]["count"] != 4
        or accepted_state["j2"]["qualified_count"] != 0
        or accepted_state["currentness"]["activation_status"] != "NOT_ACTIVATED"
    ):
        raise ValueError("P03_REAL_WORLD_ACCEPTED_J1_BOUNDARY_CHANGED")
    before, after, git_facts = committed_carriers()
    historical = _source(before, path=INITIAL_PATH,
                         commit=INITIAL_COMMIT, digest=INITIAL_SHA256,
                         historical=True)
    current = _source(after, path=REPLACEMENT_PATH,
                      commit=REPLACEMENT_COMMIT, digest=REPLACEMENT_SHA256,
                      historical=False)
    event = _transition(after)
    index = build_identity_index([historical, current], [event], snapshot_mode=MODE)
    resolution = resolve_identity(index, SemanticId(AUTHORED_ID))
    history = historical_lookup(index, SemanticId(AUTHORED_ID))
    if (
        tuple(s.value for s in resolution.current_targets) != (AUTHORED_ID,)
        or not resolution.continuity_preserved
        or tuple(source.carrier_path for source in resolution.current_sources) != (REPLACEMENT_PATH,)
        or {source.carrier_path for source in history.sources} != {INITIAL_PATH, REPLACEMENT_PATH}
        or history.transition_paths != (REPLACEMENT_PATH,)
        or not history.known
    ):
        raise RuntimeError("PRODUCTION_G006_REAL_SOURCE_IDENTITY_CONTINUITY_FAILED")
    if serialize_identity_index(index) != serialize_identity_index(
        build_identity_index([current, historical], [event], snapshot_mode=MODE)
    ):
        raise RuntimeError("P03_REAL_SOURCE_IDENTITY_ORDER_DEPENDENCE")
    return {
        "schema_version": 1,
        "world_id": accepted.EXPERIMENT_ID,
        "source_role": "GIT_ORIGINAL_OBSERVABLE_AND_PRODUCTION_G006_SEMANTIC_REPLAY",
        "git": git_facts,
        "observed_source_revision": {
            "actual_source_replacement": True,
            "same_explicit_authored_semantic_id": AUTHORED_ID,
            "original_and_current_git_blob_bytes_differ": True,
            "transition_declared_in_current_carrier": True,
            "transition_class": RELATION,
        },
        "actual_g006_replay": {
            "identity_current_targets": [AUTHORED_ID],
            "current_source_path": REPLACEMENT_PATH,
            "historical_carrier_paths": sorted({s.carrier_path for s in history.sources}),
            "continuity_preserved": resolution.continuity_preserved,
            "history_known": history.known,
            "order_independent_serialization": True,
        },
        "owner_relation": {
            "at_action_author_claim_exposed": True,
            "author_claim_independently_verified": False,
            "g006_historical_implementation_owner_covers_authenticated": False,
            "qualified_relational_j2_count": 0,
            "source_observable_identity_move_not_equivalent_to_covers": True,
        },
        "accepted_j1": {
            "effect_count": 4,
            "active_effect_ids": accepted_state["accepted_j1"]["current_effect_ids"],
            "successor_effect_dormant": accepted.EXPECTED_IDS[1],
            "lineage_rule": accepted_state["currentness"]["accepted_transition_rule"],
        },
        "j3": {
            "S0": "HOLD_NATURAL_OWNER_J2_DESPITE_OBSERVED_IDENTITY_BEHAVIOR",
            "S1": "NOT_ACTIVATED",
            "source_revision_observed_but_not_qualified_j1_activation": True,
            "completion_certified": False,
        },
        "formal_primary_tasks": None,
        "formal_b0_b4_scores": None,
        "physical_architecture_selected": False,
        "production_code_changed": False,
    }


def main() -> None:
    result = build()
    content = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != content:
            raise RuntimeError("P03_REAL_SOURCE_TRANSITION_RESULT_IMMUTABILITY_VIOLATION")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as out:
            out.write(content)
    print(json.dumps({
        "status": result["source_role"],
        "identity_continuity_observed": result["actual_g006_replay"]["continuity_preserved"],
        "historical_paths": len(result["actual_g006_replay"]["historical_carrier_paths"]),
        "qualified_j2": result["owner_relation"]["qualified_relational_j2_count"],
        "j3_complete": result["j3"]["completion_certified"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
