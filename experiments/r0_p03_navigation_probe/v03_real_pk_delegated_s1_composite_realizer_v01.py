"""One prospectively delegated, executable P03 S1 G006/G013 composite realizer.

The exposed author controls this experimental orchestration and its exact Git
source roles, not the underlying historical G006/G013 production code.
Recorded-chat policy acceptance permits one forward source event with weaker
actor assurance. This module must not admit RELATIONAL J2, activate S1 or
certify J3. Those are distinct postexecution source-owner/currentness gates.
"""
from __future__ import annotations

from dataclasses import replace
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_j2_experiment_assurance_accepted_policy_rev01 as policy,
    v03_real_pk_g013_isolated_source_refresh_v01 as original_refresh,
    v03_real_pk_source_transition_v01 as original_identity,
)
from tools.project_knowledge.adapters.gitio import commit_snapshot
from tools.project_knowledge.adapters.execution import TCB_FILES
from tools.project_knowledge.adapters.schema import SCHEMA_FILES, SchemaValidator
from tools.project_knowledge.identity import (
    build_identity_index, historical_lookup, resolve_identity,
    serialize_identity_index, transition_from_source,
)
from tools.project_knowledge.model import (
    AuthorityClass, GovernedSource, Profile, RawDeclaration,
    SemanticId, SnapshotMode, ViewFreshnessStatus, ViewInputSelector,
)
from tools.project_knowledge.services import refresh
from tools.project_knowledge.services.generation import (
    check_view_freshness, generate_views,
)
from tools.project_knowledge.services.validation import validate_repository
from tools.project_knowledge.views import deterministic_json

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SCOPE_PATH = "experiments/r0_p03_navigation_probe/v03_real_pk_delegated_s1_event_scope_v01.json"
SCOPE_SHA256 = "0fefd227092177e2e444a63fdb5b1ee8a7200ca75524145fe13e2c4a52d549d7"
RUNNER_PATH = "experiments/r0_p03_navigation_probe/v03_real_pk_delegated_s1_composite_realizer_v01.py"
OUTPUT = HERE / "v03_real_pk_delegated_s1_composite_realizer_result_v01.json"
BEFORE = "experiments/r0_p03_navigation_probe/real_pk_world/prospective_s1/identity_carrier_v02.json"
AFTER = "experiments/r0_p03_navigation_probe/real_pk_world/delegated_s1/identity_carrier_v03.json"
INTENT = "experiments/r0_p03_navigation_probe/real_pk_world/delegated_s1/source_author_realizer_intent_v01.json"
BEFORE_SHA256 = "6e0e90f4cf3b210adfac2a8d762ec6527ad260e34bad32aa5ceabf87c0ad5bef"
BEFORE_COMMIT = "faf8ff2686c6b09f53d3569470cf2057c11e5971"
REALIZER = "P03PKA.EXPERIMENT_COMPOSITE_G006_G013_DELEGATED_001"
SEMANTIC_ID = "P03PKA.G006.IDENTITY.CONTINUITY"
COMPONENTS = (
    "EXPLICIT_IDENTITY_PRESERVING_MOVE",
    "AFFECTED_VIEW_REFRESH_SELECTED",
    "INCREMENTAL_EQUALS_CURRENT_FULL_BUILD",
    "STALE_DERIVED_RESULT_NOT_GOVERNING",
)
VIEW_ID = "p03_delegated_s1_inventory"


def git(*args: str) -> bytes:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if result.returncode:
        raise ValueError("P03_DELEGATED_GIT_OBJECT_UNAVAILABLE")
    return result.stdout


def load_scope() -> dict:
    """Verify immutable scope and separately owner-accepted policy, not J2."""
    raw = (ROOT / SCOPE_PATH).read_bytes()
    if sha256(raw).hexdigest() != SCOPE_SHA256:
        raise ValueError("P03_DELEGATED_SCOPE_BYTES_DRIFT")
    scope = json.loads(raw)
    admission = policy.build()
    if (
        scope["status"] != "FROZEN_PREACTION_NOT_YET_EXECUTED"
        or scope["policy"]["acceptance_commit"] != "872d461aecf1cbd4a6a18249e9e75050a5e97773"
        or scope["policy"]["proposal_sha256"] != policy.preflight.SOURCE_SHA256
        or scope["policy"]["acceptance_binding_sha256"] != policy.BINDING_SHA256
        or scope["policy"]["max_new_events"] != 1
        or scope["accepted_s1_effect_id"] != policy.preflight.EXPECTED_SOURCE_CONTEXT["accepted_j1_effect_id"]
        or scope["world_id"] != policy.preflight.EXPECTED_SOURCE_CONTEXT["world_id"]
        or scope["components"] != list(COMPONENTS)
        or scope["source_before"] != {
            "commit": BEFORE_COMMIT,
            "path": BEFORE,
            "sha256": BEFORE_SHA256,
            "authored_semantic_id": SEMANTIC_ID,
        }
        or scope["event"]["expected_paths"] != [
            {"status": s, "path": p} for s, p in
            (("D", BEFORE), ("A", AFTER), ("A", INTENT))
        ]
        or scope["event"]["event_parent_must_be_exact_frozen_scope_commit"] is not True
        or scope["event"]["production_code_changes_in_event"] is not False
        or scope["realizer"]["id"] != REALIZER
        or scope["realizer"]["executable_path"] != RUNNER_PATH
        or scope["realizer"]["historical_production_g006_g013_owner_claim"] is not False
        or scope["realizer"]["actor_assurance"] !=
            "RECORDED_CHAT_AND_EXPOSED_SESSION_NOT_INDEPENDENTLY_AUTHENTICATED"
        or scope["postevent"]["postexecution_covers_must_be_separate_commit"] is not True
        or scope["postevent"]["s1_open_reset_does_not_carry_predecessor_evidence"] is not True
        or admission["policy"]["status"] != "OWNER_ACCEPTED_PROSPECTIVE_EXPERIMENT_ONLY_POLICY"
        or admission["qualified_experimental_relational_j2"] != 0
        or admission["s1_activated"] is not False
        or admission["j3_satisfied"] is not False
    ):
        raise ValueError("P03_DELEGATED_SCOPE_OR_ACCEPTANCE_DRIFT")
    return scope


def validate_intent(intent: dict, scope: dict, freeze: str) -> None:
    """Prevent a self-serving at-action claim from masquerading as J2."""
    expected = {
        "schema_version": 1, "scope_id": scope["scope_id"],
        "policy_proposal_id": scope["policy"]["proposal_id"],
        "policy_acceptance_commit": scope["policy"]["acceptance_commit"],
        "scope_freeze_commit": freeze, "source_event_parent": freeze,
        "realizer_id": REALIZER,
        "author_role": scope["realizer"]["natural_owner_scope"],
        "author_identity_assurance": scope["realizer"]["actor_assurance"],
        "source_before_path": BEFORE, "source_after_path": AFTER,
        "semantic_id": SEMANTIC_ID,
        "accepted_s1_effect_id": scope["accepted_s1_effect_id"],
        "target_components": list(COMPONENTS),
        "relationship": "PROSPECTIVE_EXECUTION_INTENT_NOT_J2_COVERS",
        "execution_status": "NOT_EXECUTED_AT_TIME_OF_GIT_EVENT",
        "qualified_relational_j2": False,
        "s1_activated": False, "j3": "HOLD",
        "production_authority": False, "formal_b0_b4_scored": False,
    }
    if intent != expected:
        raise ValueError("P03_DELEGATED_INTENT_SCHEMA_OR_FALSE_AUTHORITY")


def validate_carrier(before: dict, after: dict, scope: dict, freeze: str) -> None:
    """Preserve authored identity and reject unearned S1/J2/J3 assertions."""
    if set(before) != set(after) or before["governed_source"] != after["governed_source"]:
        raise ValueError("P03_DELEGATED_SOURCE_RECORD_OR_SEMANTICS_CHANGED")
    if (
        after["governed_source"]["semantic_id"] != SEMANTIC_ID
        or after["world_id"] != scope["world_id"]
        or after["accepted_effect_ref"] != scope["accepted_s1_effect_id"]
        or after["asserted_implementation_coverage"] is not None
        or after["production_authority"] is not False
        or after["no_formal_task_or_score"] is not True
        or after["expanded_real_ads_source_witnesses"] != []
        or after["lifecycle_stage"] != "S1_DELEGATED_PREEXECUTION_SOURCE_NOT_ACTIVATED"
        or after["source_owner_claim"]["natural_owner_relational_j2_qualified"] is not False
        or after["source_owner_claim"]["claim_class"] !=
            "SCOPED_COMPOSITE_REALIZER_AUTHOR_NOT_INDEPENDENTLY_AUTHENTICATED"
    ):
        raise ValueError("P03_DELEGATED_PREEXECUTION_AUTHORITY_FORGERY")
    p = after["revision_provenance"]
    if (
        p["previous_source_path"] != BEFORE or p["current_source_path"] != AFTER
        or p["prior_git_commit"] != BEFORE_COMMIT
        or p["expected_action_parent"] != freeze
        or p["git_successor_commit"] != "UNAVAILABLE_UNTIL_COMMIT"
        or p["semantic_id_invariant"] != SEMANTIC_ID
        or p["natural_owner_j2_coverage"] != "UNQUALIFIED_PENDING_REAL_EXECUTION"
        or p["successor_j1_activation"] != "NOT_ACTIVATED"
        or p["source_event_scope_id"] != scope["scope_id"]
        or p["composite_realizer_id"] != REALIZER
    ):
        raise ValueError("P03_DELEGATED_CURRENT_CARRIER_PROVENANCE_INVALID")


def observe_event(event_sha: str, freeze_sha: str):
    """Read exact Git trees. The source action must have one published parent."""
    if not all(re.fullmatch(r"[0-9a-f]{40}", s) for s in (event_sha, freeze_sha)):
        raise ValueError("P03_DELEGATED_COMMIT_SHA_REQUIRED")
    scope = load_scope()
    if git("rev-parse", f"{event_sha}^").decode("ascii").strip() != freeze_sha:
        raise ValueError("P03_DELEGATED_EVENT_PARENT_MISMATCH")
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor",
         scope["policy"]["acceptance_commit"], freeze_sha],
        cwd=ROOT, capture_output=True,
    )
    if ancestor.returncode:
        raise ValueError("P03_DELEGATED_FREEZE_PRECEDES_OWNER_POLICY_ACCEPTANCE")
    if (
        sha256(git("show", f"{freeze_sha}:{SCOPE_PATH}")).hexdigest() != SCOPE_SHA256
        or git("show", f"{freeze_sha}:{RUNNER_PATH}") != (ROOT / RUNNER_PATH).read_bytes()
    ):
        raise ValueError("P03_DELEGATED_SCOPE_OR_EXECUTABLE_NOT_FROZEN")
    changes = [
        tuple(line.split("\t", 1))
        for line in git("diff", "--no-renames", "--name-status",
                        freeze_sha, event_sha).decode("utf8").splitlines()
    ]
    if sorted(changes) != sorted([("D", BEFORE), ("A", AFTER), ("A", INTENT)]):
        raise ValueError("P03_DELEGATED_SOURCE_EVENT_CHANGED_WRONG_FILES")
    original = git("show", f"{freeze_sha}:{BEFORE}")
    new = git("show", f"{event_sha}:{AFTER}")
    claim = git("show", f"{event_sha}:{INTENT}")
    if (
        sha256(original).hexdigest() != BEFORE_SHA256
        or original != git("show", f"{BEFORE_COMMIT}:{BEFORE}")
    ):
        raise ValueError("P03_DELEGATED_PREVIOUS_SOURCE_REVISION_DRIFT")
    before, after, intent = map(json.loads, (original, new, claim))
    validate_intent(intent, scope, freeze_sha)
    validate_carrier(before, after, scope, freeze_sha)
    facts = {
        "source_event_commit": event_sha, "freeze_commit": freeze_sha,
        "before_sha256": sha256(original).hexdigest(),
        "after_sha256": sha256(new).hexdigest(),
        "intent_sha256": sha256(claim).hexdigest(),
        "changes": [{"status": s, "path": p} for s, p in changes],
    }
    return before, after, facts


def run_g006(before: dict, after: dict, facts: dict) -> dict:
    """Invoke production identity indexing with exact new source revisions."""
    old = original_identity._source(
        before, path=BEFORE, commit=BEFORE_COMMIT,
        digest=facts["before_sha256"], historical=True,
    )
    current = original_identity._source(
        after, path=AFTER, commit=facts["source_event_commit"],
        digest=facts["after_sha256"], historical=False,
    )
    raw = RawDeclaration({
        "schema_version": "1", "profile": "identity_transition.v1",
        "kind": "p03-delegated-source-move",
        "authority_class": "canonical", "transition_class": "REPRESENTATION_REPLACEMENT",
        "predecessors": [SEMANTIC_ID], "successors": [SEMANTIC_ID],
        "resolution_behavior": "Preserve authored identity across delegated source carrier move",
        "provenance": [BEFORE, AFTER],
    })
    if SchemaValidator().validate(raw):
        raise ValueError("P03_DELEGATED_IDENTITY_TRANSITION_SCHEMA_FAILURE")
    carrier = GovernedSource(
        carrier_path=AFTER, profile=Profile.IDENTITY_TRANSITION,
        authority_class=AuthorityClass.CANONICAL,
        kind="p03-delegated-source-move", declaration=raw,
        snapshot_mode=SnapshotMode.COMMIT_SNAPSHOT,
    )
    event = transition_from_source(carrier)
    idx = build_identity_index([old, current], [event],
                               snapshot_mode=SnapshotMode.COMMIT_SNAPSHOT)
    resolved = resolve_identity(idx, SemanticId(SEMANTIC_ID))
    hist = historical_lookup(idx, SemanticId(SEMANTIC_ID))
    reversed_idx = build_identity_index(
        [current, old], [event], snapshot_mode=SnapshotMode.COMMIT_SNAPSHOT,
    )
    if (
        not resolved.continuity_preserved
        or tuple(x.value for x in resolved.current_targets) != (SEMANTIC_ID,)
        or tuple(x.carrier_path for x in resolved.current_sources) != (AFTER,)
        or {x.carrier_path for x in hist.sources} != {BEFORE, AFTER}
        or serialize_identity_index(idx) != serialize_identity_index(reversed_idx)
    ):
        raise RuntimeError("P03_DELEGATED_PRODUCTION_G006_IDENTITY_FAILED")
    return {
        "production_g006_executed": True,
        "identity_preserved": True,
        "authored_semantic_id": SEMANTIC_ID,
        "current_carrier": AFTER,
        "historical_carriers": sorted({x.carrier_path for x in hist.sources}),
        "serialization_order_independent": True,
    }


def run_g013(before: dict, after: dict, facts: dict) -> dict:
    """Execute production G013 and G009 in a separate source-valid Git root."""
    spec = replace(
        original_refresh._specification(),
        view_id=VIEW_ID,
        view_path="docs/project_knowledge/generated/p03_delegated_s1_inventory.json",
        manifest_path="docs/project_knowledge/generated/manifests/p03_delegated_s1_inventory.json",
        selector=ViewInputSelector(profiles=(Profile.SEMANTIC_SOURCE,)),
    )
    closure = set(spec.generator.implementation_files) | set(TCB_FILES) | set(SCHEMA_FILES)
    closure.add("tools/project_knowledge/services/refresh.py")
    fixture = json.loads(original_refresh.FIXTURE_PATH.read_bytes())
    raw_before = git("show", f"{facts['freeze_commit']}:{BEFORE}")
    raw_after = git("show", f"{facts['source_event_commit']}:{AFTER}")
    old = "docs/p03_delegated_s1/before/identity.json"
    new = "docs/p03_delegated_s1/after/identity.json"
    with original_refresh._isolated_repo() as root:
        original_refresh._git(root, "init", "--quiet")
        original_refresh._git(root, "config", "user.name", "P03 isolated delegated composite")
        original_refresh._git(root, "config", "user.email", "p03@example.invalid")
        original_refresh._git(root, "config", "core.autocrlf", "false")
        for path in sorted(closure):
            original_refresh._write(root, path, (ROOT / path).read_bytes())
        for path, data in fixture.items():
            original_refresh._write(root, path, deterministic_json(data))
        original_refresh._write(
            root, "assets/p03_delegated/before_git_bytes.json", raw_before
        )
        original_refresh._write(root, old, deterministic_json(before["governed_source"]))
        previous = original_refresh._commit(
            root, "Isolated previous delegated source",
            date="2026-11-15T10:00:00+0000",
        )
        if not validate_repository(commit_snapshot(root, previous)).ok:
            raise RuntimeError("P03_DELEGATED_PREVIOUS_SOURCE_ADMISSION_FAILED")
        built_before, = generate_views(commit_snapshot(root, previous), (spec,))
        (root / old).unlink()
        original_refresh._write(root, "assets/p03_delegated/after_git_bytes.json", raw_after)
        original_refresh._write(root, new, deterministic_json(after["governed_source"]))
        transition = {
            "schema_version": "1", "profile": "identity_transition.v1",
            "kind": "p03-delegated-source-move",
            "authority_class": "canonical", "transition_class": "REPRESENTATION_REPLACEMENT",
            "predecessors": [SEMANTIC_ID], "successors": [SEMANTIC_ID],
            "resolution_behavior": "Authored ID survives the delegated source carrier change",
            "provenance": [BEFORE, AFTER],
        }
        original_refresh._write(
            root, "docs/p03_delegated_s1/after/transition.json",
            deterministic_json(transition),
        )
        current = original_refresh._commit(
            root, "Isolated current delegated source",
            date="2026-11-15T10:01:00+0000",
        )
        if not validate_repository(commit_snapshot(root, current)).ok:
            raise RuntimeError("P03_DELEGATED_CURRENT_SOURCE_ADMISSION_FAILED")
        selected = refresh.refresh_views(
            root, previous, current, (spec,), previous_specifications=(spec,)
        )
        full, = generate_views(commit_snapshot(root, current), (spec,))
        if selected.plan.affected_view_ids != (VIEW_ID,) or selected.plan.full_fallback:
            raise RuntimeError("P03_DELEGATED_IMPACT_SELECTION_FAILED")
        if selected.builds != (full,):
            raise RuntimeError("P03_DELEGATED_INCREMENTAL_FULL_INEQUIVALENT")
        stale = check_view_freshness(
            commit_snapshot(root, current), (spec,), VIEW_ID,
            built_before.manifest, existing_view_bytes=built_before.view_bytes,
        )
        fresh = check_view_freshness(
            commit_snapshot(root, current), (spec,), VIEW_ID,
            full.manifest, existing_view_bytes=full.view_bytes,
        )
        if stale.status != ViewFreshnessStatus.STALE or fresh.status != ViewFreshnessStatus.FRESH:
            raise RuntimeError("P03_DELEGATED_GENERATED_FRESHNESS_FAILED")
        before_rows = [x for x in json.loads(built_before.view_bytes)["sources"]
                       if x["semantic_id"] == SEMANTIC_ID]
        after_rows = [x for x in json.loads(full.view_bytes)["sources"]
                      if x["semantic_id"] == SEMANTIC_ID]
        if (
            len(before_rows) != 1 or len(after_rows) != 1
            or before_rows[0]["source_path"] != old
            or after_rows[0]["source_path"] != new
            or before_rows[0]["content_digest"] != after_rows[0]["content_digest"]
        ):
            raise RuntimeError("P03_DELEGATED_GENERATED_SOURCE_IDENTITY_CHANGED")
        return {
            "production_g013_g009_executed": True,
            "isolated_before_commit": previous,
            "isolated_after_commit": current,
            "affected_view": VIEW_ID,
            "selection_reason": [list(x) for x in selected.plan.reasons],
            "selected_equals_full": True,
            "previous_manifest": stale.status.value,
            "current_manifest": fresh.status.value,
            "generated_current_view_sha256": sha256(full.view_bytes).hexdigest(),
            "current_manifest_sha256": sha256(full.manifest_bytes).hexdigest(),
            "source_content_digest": after_rows[0]["content_digest"],
            "G010_fixture_used_only_as_execution_prerequisite": True,
            "whole_ADS_corpus_G013_claimed": False,
        }


def execute(event_commit: str, freeze_commit: str) -> dict:
    """Execute the new event only, with no self-qualified J2/J3 result."""
    before, after, facts = observe_event(event_commit, freeze_commit)
    g006 = run_g006(before, after, facts)
    g013 = run_g013(before, after, facts)
    return {
        "schema_version": 1,
        "status": "NEW_SOURCE_RELATIVE_G006_G013_OBSERVED_NOT_J2_CERTIFIED",
        "event": facts,
        "realizer_id": REALIZER,
        "component_ids": list(COMPONENTS),
        "g006": g006,
        "g013": g013,
        "source_author_independently_authenticated": False,
        "postexecution_covers_admitted": False,
        "qualified_relational_j2": False,
        "s1_activated": False,
        "j3": "HOLD_PENDING_SOURCE_OWNER_COVERS_AND_SEPARATE_EVALUATOR",
        "formal_R0_P03": "INCOMPLETE",
        "production_modified": False,
        "physical_architecture_selected": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--event-commit", required=True)
    parser.add_argument("--scope-commit", required=True)
    args = parser.parse_args()
    result = execute(args.event_commit, args.scope_commit)
    text = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != text:
            raise RuntimeError("P03_DELEGATED_RECEIPT_IMMUTABILITY_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as out:
            out.write(text)
    print(json.dumps({
        "status": result["status"],
        "G006": result["g006"]["identity_preserved"],
        "G013": result["g013"]["selected_equals_full"],
        "J2": result["qualified_relational_j2"],
        "J3": result["j3"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
