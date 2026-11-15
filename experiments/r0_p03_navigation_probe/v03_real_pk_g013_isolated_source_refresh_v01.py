"""Real ADS Git-source carrier through actual production G013, isolated from authority.

The two source payloads originate in the real original ADS repository at
10cad3cb and cac152cf, not from an invented before/after document. Their
schema-valid authored semantic_source.v1 declarations are *projected* into an
ephemeral documentation root, because production discovery deliberately
excludes experiments/. The surrounding prerequisite workstream/architecture
declarations are an existing, separately identified G010 test fixture.

The production G009/G013 implementations and schemas are copied byte-for-byte
into that isolated temporary Git root. G013 executes actual snapshots,
selection, full-current generation and manifest freshness; no fake compute,
manually filled index output, or production authority switch is supplied.

Results must distinguish evidence for G013 implementation semantics from
evidence of owner qualification, formal source-world currentness, or J3 PASS.
"""
from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import tempfile

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_source_transition_v01 as transition,
    v03_real_pk_accepted_j1_projection_v01 as accepted_j1,
)
from tools.project_knowledge.adapters.gitio import commit_snapshot
from tools.project_knowledge.adapters.execution import TCB_FILES
from tools.project_knowledge.adapters.schema import SCHEMA_FILES
from tools.project_knowledge.model import (
    Profile, ViewFreshnessStatus, ViewInputSelector,
)
from tools.project_knowledge.services import refresh
from tools.project_knowledge.services.generation import generate_views, check_view_freshness
from tools.project_knowledge.services.validation import validate_repository
from tools.project_knowledge.view_definitions import source_inventory_specification
from tools.project_knowledge.views import deterministic_json
from dataclasses import replace


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path(__file__).with_name("v03_real_pk_g013_isolated_source_refresh_result_v01.json")
FIXTURE_PATH = ROOT / "tests/fixtures/project_knowledge_g010/corpus.json"
OLD = "docs/p03_real_source/initial/identity.json"
NEW = "docs/p03_real_source/current/identity.json"
TRANSITION = "docs/p03_real_source/current/representation_transition.json"
INITIAL_REFERENCE = "assets/p03_real_git_sources/initial_original_bytes.json"
CURRENT_REFERENCE = "assets/p03_real_git_sources/current_original_bytes.json"
VIEW = "p03_real_semantic_inventory"


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, check=False, capture_output=True,
        encoding="utf8", text=True,
    )
    if result.returncode:
        raise RuntimeError("ISOLATED_G013_GIT_COMMAND_FAILED:" + " ".join(args) +
                           ":" + result.stderr[-300:])
    return result.stdout.strip()


def _write(root: Path, relative: str, raw: bytes) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)


def _commit(root: Path, message: str, *, date: str) -> str:
    """Use reproducible sandbox-only Git timestamps, not claimed action times."""
    _git(root, "add", "-A")
    env = dict(os.environ)
    env["GIT_AUTHOR_DATE"] = date
    env["GIT_COMMITTER_DATE"] = date
    process = subprocess.run(
        ["git", "commit", "--quiet", "-m", message],
        cwd=root, capture_output=True, text=True, encoding="utf8",
        env=env, check=False,
    )
    if process.returncode:
        raise RuntimeError("DETERMINISTIC_ISOLATED_GIT_COMMIT_FAILED:" + process.stderr[-300:])
    return _git(root, "rev-parse", "HEAD")


def _cleanup_error(function, path, error):
    os.chmod(path, stat.S_IREAD | stat.S_IWRITE)
    function(path)


@contextmanager
def _isolated_repo():
    """Temporary real Git root, destroyed after *all* results are reduced."""
    folder = Path(tempfile.mkdtemp(prefix=".p03_g013_", dir=ROOT / "tests"))
    try:
        yield folder
    finally:
        shutil.rmtree(folder, onexc=_cleanup_error)


def _specification():
    """One actual G009 inventory generator, selected on semantic sources."""
    base = source_inventory_specification()
    return replace(
        base, view_id=VIEW,
        view_path="docs/project_knowledge/generated/p03_real_semantic_inventory.json",
        manifest_path="docs/project_knowledge/generated/manifests/p03_real_semantic_inventory.json",
        selector=ViewInputSelector(profiles=(Profile.SEMANTIC_SOURCE,)),
    )


def execute() -> dict:
    """Run true G013 impacted-view selection/build against exact real source versions."""
    experiment = accepted_j1.build()
    if (experiment["accepted_j1"]["count"] != 4
            or experiment["currentness"]["activation_status"] != "NOT_ACTIVATED"
            or experiment["j2"]["qualified_count"] != 0
            or experiment["j3"]["satisfaction_certified"] is not False):
        raise RuntimeError("G013_EXPERIMENT_ACCEPTED_J1_OR_AUTHORITATIVE_STATUS_DRIFT")
    s1 = experiment["accepted_j1"]["effects"][1]
    components = s1["completion_contract"]["required_components"]
    if (s1["id"] != accepted_j1.EXPECTED_IDS[1]
            or components != [
                "EXPLICIT_IDENTITY_PRESERVING_MOVE",
                "AFFECTED_VIEW_REFRESH_SELECTED",
                "INCREMENTAL_EQUALS_CURRENT_FULL_BUILD",
                "STALE_DERIVED_RESULT_NOT_GOVERNING",
            ]):
        raise RuntimeError("G013_EXACT_ACCEPTED_S1_COMPONENTS_CHANGED")
    real_move = transition.build()
    if (
        real_move["actual_g006_replay"]["continuity_preserved"] is not True
        or len(real_move["actual_g006_replay"]["historical_carrier_paths"]) != 2
        or real_move["owner_relation"]["qualified_relational_j2_count"] != 0
    ):
        raise RuntimeError("G013_REUSED_REAL_G006_SEMANTICS_NOT_VALID")
    original, current, original_facts = transition.committed_carriers()
    spec = _specification()
    if original["governed_source"]["semantic_id"] != current["governed_source"]["semantic_id"]:
        raise RuntimeError("EXPERIMENT_SOURCE_SEMANTIC_ID_CHANGED")
    if (
        original["governed_source"] != current["governed_source"]
        or original["governed_source"]["semantic_id"] != transition.AUTHORED_ID
    ):
        raise RuntimeError("G013_SOURCE_PROJECTION_DOES_NOT_PRESERVE_ORIGINAL_DECLARATION")

    closure = set(spec.generator.implementation_files) | set(TCB_FILES) | set(SCHEMA_FILES)
    closure.add("tools/project_knowledge/services/refresh.py")
    fixture_bytes = FIXTURE_PATH.read_bytes()
    # The existing G010 corpus is ONLY a validated execution prerequisite,
    # not an R0-P03 scoring corpus and not newly accepted J1 semantics.
    fixture = json.loads(fixture_bytes)
    raw_original = transition.git("show", f"{transition.INITIAL_COMMIT}:{transition.INITIAL_PATH}")
    raw_current = transition.git("show", f"{transition.REPLACEMENT_COMMIT}:{transition.REPLACEMENT_PATH}")
    if sha256(raw_original).hexdigest() != transition.INITIAL_SHA256:
        raise RuntimeError("INITIAL_REAL_SOURCE_BYTES_CHANGED")
    if sha256(raw_current).hexdigest() != transition.REPLACEMENT_SHA256:
        raise RuntimeError("CURRENT_REAL_SOURCE_BYTES_CHANGED")

    with _isolated_repo() as root:
        _git(root, "init", "--quiet")
        _git(root, "config", "user.name", "P03 G013 isolated source-state qualification")
        _git(root, "config", "user.email", "p03-isolated@example.invalid")
        _git(root, "config", "core.autocrlf", "false")
        for path in sorted(closure):
            _write(root, path, (ROOT / path).read_bytes())
        for path, data in fixture.items():
            _write(root, path, deterministic_json(data))
        _write(root, INITIAL_REFERENCE, raw_original)
        _write(root, OLD, deterministic_json(original["governed_source"]))
        previous_sha = _commit(root, "P03 isolated G013 initial real-Git-backed carrier", date="2026-11-15T07:00:00+0000")
        previous_validation = validate_repository(commit_snapshot(root, previous_sha))
        if not previous_validation.ok:
            raise RuntimeError("G013_PREVIOUS_PRODUCTION_ADMISSION_INVALID:" +
                               ",".join(d.code for d in previous_validation.diagnostics))
        before_build, = generate_views(commit_snapshot(root, previous_sha), (spec,))
        before_payload = json.loads(before_build.view_bytes.decode("utf8"))

        (root / OLD).unlink()
        _write(root, CURRENT_REFERENCE, raw_current)
        _write(root, NEW, deterministic_json(current["governed_source"]))
        claim = current["revision_provenance"]
        if (
            claim["previous_source_path"] != transition.INITIAL_PATH
            or claim["current_source_path"] != transition.REPLACEMENT_PATH
            or claim["semantic_id_invariant"] != transition.AUTHORED_ID
            or claim["successor_j1_activation"] != "NOT_ACTIVATED"
        ):
            raise RuntimeError("G013_REAL_SOURCE_CLAIM_INVALID")
        authored_transition = {
            "schema_version": "1",
            "profile": "identity_transition.v1",
            "kind": "p03-experiment-real-Git-source-representation",
            "authority_class": "canonical",
            "transition_class": "REPRESENTATION_REPLACEMENT",
            "predecessors": [transition.AUTHORED_ID],
            "successors": [transition.AUTHORED_ID],
            "resolution_behavior": "Preserve authored semantic identity across the real source carrier replacement",
            "provenance": [transition.INITIAL_PATH, transition.REPLACEMENT_PATH],
        }
        _write(root, TRANSITION, deterministic_json(authored_transition))
        current_sha = _commit(root, "P03 isolated G013 moved real-Git-backed source with authored transition", date="2026-11-15T07:01:00+0000")
        current_validation = validate_repository(commit_snapshot(root, current_sha))
        if not current_validation.ok:
            raise RuntimeError("G013_CURRENT_PRODUCTION_ADMISSION_INVALID:" +
                               ",".join(d.code for d in current_validation.diagnostics))
        result = refresh.refresh_views(
            root, previous_sha, current_sha, (spec,), previous_specifications=(spec,)
        )
        full, = generate_views(commit_snapshot(root, current_sha), (spec,))
        if result.plan.affected_view_ids != (VIEW,) or result.plan.full_fallback:
            raise RuntimeError("REAL_CARRIER_G013_IMPACT_SELECTION_FAILED")
        if result.builds != (full,):
            raise RuntimeError("REAL_CARRIER_G013_SELECTED_FULL_BYTES_DIFFER")
        # Manifest freshness uses source/current bindings, not saved output path.
        stale = check_view_freshness(
            commit_snapshot(root, current_sha), (spec,),
            VIEW, before_build.manifest, existing_view_bytes=before_build.view_bytes,
        )
        fresh = check_view_freshness(
            commit_snapshot(root, current_sha), (spec,),
            VIEW, full.manifest, existing_view_bytes=full.view_bytes,
        )
        if stale.status != ViewFreshnessStatus.STALE:
            raise RuntimeError("REAL_CARRIER_OLD_MANIFEST_NOT_MARKED_STALE")
        if fresh.status != ViewFreshnessStatus.FRESH:
            raise RuntimeError("REAL_CARRIER_CURRENT_MANIFEST_NOT_FRESH")
        after_payload = json.loads(full.view_bytes.decode("utf8"))
        before_matches = [entry for entry in before_payload["sources"]
                          if entry["semantic_id"] == transition.AUTHORED_ID]
        after_matches = [entry for entry in after_payload["sources"]
                         if entry["semantic_id"] == transition.AUTHORED_ID]
        if (
            len(before_matches) != 1 or len(after_matches) != 1
            or before_matches[0]["source_path"] != OLD
            or after_matches[0]["source_path"] != NEW
            or before_matches[0]["profile"] != "semantic_source.v1"
            or after_matches[0]["profile"] != "semantic_source.v1"
            or before_matches[0]["content_digest"] != after_matches[0]["content_digest"]
            or any(entry["source_path"] == OLD for entry in after_payload["sources"])
        ):
            raise RuntimeError("G013_OUTPUT_DOES_NOT_TRACK_REAL_SOURCE_IDENTITY_MOVE")
        return {
            "schema_version": 1,
            "status": "ACTUAL_PRODUCTION_G013_REFRESH_ON_EXACT_REAL_SOURCE_PROJECTION_PASS",
            "experimental_source": {
                "original_git_before_commit": transition.INITIAL_COMMIT,
                "original_git_after_commit": transition.REPLACEMENT_COMMIT,
                "original_before_sha256": transition.INITIAL_SHA256,
                "original_after_sha256": transition.REPLACEMENT_SHA256,
                "same_semantic_id": transition.AUTHORED_ID,
                "original_exact_bytes_copied_to_isolated_root": True,
                "governed_source_field_values_unchanged_from_actual_carrier": True,
            },
            "source_projection": {
                "before": before_matches[0],
                "after": after_matches[0],
                "previous_carrier_absent_from_current_view": True,
                "identity_unmodified_when_carrier_path_changes": True,
                "source_content_digest_unchanged": True,
            },
            "execution": {
                "actual_production_G013_api_used": True,
                "actual_production_G009_full_generator_used": True,
                "ephemeral_git_commit_before": previous_sha,
                "ephemeral_git_commit_after": current_sha,
                "previous_repository_admission": "PASS",
                "current_repository_admission": "PASS",
                "generated_view_id": VIEW,
                "G013_affected_view_ids": list(result.plan.affected_view_ids),
                "G013_reasons": [list(pair) for pair in result.plan.reasons],
                "G013_full_fallback": result.plan.full_fallback,
                "incremental_exactly_equals_full_build": result.builds == (full,),
                "previous_manifest_currentness": stale.status.value,
                "current_manifest_currentness": fresh.status.value,
                "old_view_sha256": sha256(before_build.view_bytes).hexdigest(),
                "current_view_sha256": sha256(full.view_bytes).hexdigest(),
                "new_view_manifest_sha256": sha256(full.manifest_bytes).hexdigest(),
                "old_view_bytes_differ_from_new": before_build.view_bytes != full.view_bytes,
                "output_source_input_is_complete_current_snapshot": True,
                "fixture_supporting_source_count": len(fixture),
            },
            "provenance": {
                "qualified_source_claim": "REAL_ORIGINAL_GIT_BLOB_AND_SCHEMA_FIELD_PROJECTION",
                "supporting_fixture": "tests/fixtures/project_knowledge_g010/corpus.json",
                "fixture_only_for_valid_production_execution_closure": True,
                "same_real_main_repository_full_validation_claimed": False,
                "all_19_original_sources_executed_as_single_G013_CORPUS": False,
                "temporary_sandbox_commits_not_original_ADS_Git_commits": True,
                "production_source_or_code_modified": False,
            },
            "component_observations_not_gov_j2": [
                {
                    "accepted_effect": s1["id"],
                    "component": components[0],
                    "observation": "SAME_IDENTITY_FROM_EXACT_GIT_G006_REPLAY",
                    "evidence_class": "OBSERVABLE_EXECUTED",
                    "qualified_governing_j2": False,
                },
                {
                    "accepted_effect": s1["id"],
                    "component": components[1],
                    "observation": "G013_SELECTED_AFFECTED_SEMANTIC_INVENTORY",
                    "evidence_class": "OBSERVABLE_EXECUTED",
                    "qualified_governing_j2": False,
                },
                {
                    "accepted_effect": s1["id"],
                    "component": components[2],
                    "observation": "BYTE_IDENTICAL_G013_SELECTED_AND_G009_FULL_CURRENT_BUILDS",
                    "evidence_class": "OBSERVABLE_EXECUTED",
                    "qualified_governing_j2": False,
                },
                {
                    "accepted_effect": s1["id"],
                    "component": components[3],
                    "observation": "OLD_MANIFEST_STALE_NEW_MANIFEST_FRESH",
                    "evidence_class": "OBSERVABLE_EXECUTED",
                    "qualified_governing_j2": False,
                },
            ],
            "authority": {
                "source_owner_relational_J2_qualified": False,
                "S1_accepted_transition_activated": False,
                "J3_satisfaction_certified": False,
                "formal_B0_B4_scoring_performed": False,
                "physical_architecture_selected": False,
            },
            "debug": {
                "before_view_sources": len(before_payload.get("sources", [])),
                "after_view_sources": len(after_payload.get("sources", [])),
            },
        }


def main() -> None:
    result = execute()
    text = json.dumps(result, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != text:
            raise RuntimeError("G013_REAL_SOURCE_RECEIPT_IMMUTABLE_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as f:
            f.write(text)
    print(json.dumps({
        "status": result["status"],
        "affected": result["execution"]["G013_affected_view_ids"],
        "stale": result["execution"]["previous_manifest_currentness"],
        "fresh": result["execution"]["current_manifest_currentness"],
        "J2_qualified": result["authority"]["source_owner_relational_J2_qualified"],
        "S1_activated": result["authority"]["S1_accepted_transition_activated"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
