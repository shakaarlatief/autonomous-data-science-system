"""Oracle-blind, exclusive first-run execution of the frozen Q10 contract.

Qualification evidence is confined to fixture-listed Git blobs. Existing public
validators and unit tests are execution-only structural evidence. No prior Q10
output is read, and no source or authority file is written. Semantic assertions
below implement requirement conditions, not a comparison with expected answers.
"""
from __future__ import annotations

import collections
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "docs/research/project_knowledge_candidate_01_q10_final_v01/Q10_FINAL_FIXTURE_V01.json"
OUTPUT = FIXTURE.with_name("RESULTS_V01.json")
OBSERVED_FIXTURE_SHA256 = "c62b54e7cb9903a175449d89c5383ed8843b2a8da236688173201a0d429db57c"
OBSERVED_HEAD = "7ca12bbafdcff90c38878f391fe56205ea3cd012"
ITEM_IDS = [f"KA-R{i:02}" for i in range(1, 51)] + [f"KA-I{i:02}" for i in range(1, 18)]
Q10_IDS = {"KA-R30", "KA-R40", "KA-R41"}
MISSING = object()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def status():
    # Metadata-only change inventory; never obtain a diff or inspect the oracle.
    return git("status", "--porcelain=v1", "--untracked-files=all").decode().splitlines()


def get(source, pointer):
    try:
        for part in pointer.split("/") if pointer else []:
            source = source[int(part)] if isinstance(source, list) else source[part]
        return source
    except (KeyError, IndexError, TypeError, ValueError):
        return MISSING


def predicate(value, operation, expected):
    if value is MISSING:
        return False
    if operation == "eq":
        return type(value) is type(expected) and value == expected
    if operation == "le":
        return type(value) in (int, float) and value <= expected
    if operation == "ge":
        return type(value) in (int, float) and value >= expected
    if operation == "nonempty":
        return bool(value)
    if operation == "contains":
        return expected in value
    if operation == "all_true":
        return bool(value) and all(v is True for v in (value.values() if isinstance(value, dict) else value))
    raise ValueError(operation)


def assertion(data, key, pointer, operation="eq", expected=True):
    value = get(data.get(key, {}), pointer)
    return {"source_key": key, "pointer": "/" + pointer,
            "measured": None if value is MISSING else value,
            "missing": value is MISSING, "operation": operation,
            "required": expected, "satisfied": predicate(value, operation, expected)}


def verify_sources(fixture):
    records, data = [], {}
    for source in fixture["sources"]:
        record = dict(source)
        try:
            commit = git("rev-parse", source["source_commit"] + "^{commit}").decode().strip()
            blob_id = git("rev-parse", source["source_commit"] + ":" + source["path"]).decode().strip()
            raw = git("show", source["source_commit"] + ":" + source["path"])
            record.update(observed_commit=commit, observed_blob_id=blob_id,
                          observed_bytes=len(raw), observed_sha256=sha(raw))
            record["checks"] = {
                "exact_commit": commit == source["source_commit"],
                "hash_basis": source["hash_basis"] == "GIT_BLOB_BYTES_AT_COMMIT",
                "byte_count": len(raw) == source["bytes"],
                "digest": sha(raw) == source["sha256"],
            }
            record["verified"] = all(record["checks"].values())
            if record["verified"]:
                data[source["source_key"]] = json.loads(raw) if source["path"].endswith(".json") else raw.decode("utf-8")
        except Exception as exc:
            record.update(verified=False, error=str(exc))
        records.append(record)
        print(f"Frozen source {source['source_key']}: {'PASS' if record['verified'] else 'FAIL'}", flush=True)
    return records, data


def budgets(fixture, data):
    result = []
    for name, contract in fixture["budget_contract"].items():
        if name == "B01_BROAD_CURRENT_CORE":
            facts = [assertion(data, "current_core", "metrics/current_state_core_bytes", "le", contract["max_core_bytes"])]
            numerator = get(data.get("current_core", {}), "metrics/must_preserve_recoverable_count")
            denominator = get(data.get("current_core", {}), "metrics/must_preserve_item_count")
            ratio = f"{numerator}/{denominator}" if MISSING not in (numerator, denominator) else None
            facts.append({"source_key": "current_core", "pointer": "/metrics/must_preserve_recoverable_count,/metrics/must_preserve_item_count",
                          "measured": ratio, "required": contract["required_must_preserve_recoverability"],
                          "operation": "eq", "satisfied": ratio == contract["required_must_preserve_recoverability"]})
            reason = "Bound the measured mandatory core and require exact must-preserve recoverability."
        elif name == "B02_NARROW_CONSEQUENTIAL_TASK":
            facts = [assertion(data, "q125", "budget/" + path, "le", contract[limit]) for path, limit in [
                ("evidence_read_count", "max_evidence_reads"),
                ("evidence_read_bytes_from_frozen_manifest", "max_evidence_bytes"),
                ("legacy_bootstrap_read_count", "max_legacy_bootstrap_reads")]]
            reason = "Use the frozen Q10 limits directly against the recorded narrow-task reads, bytes and legacy bootstrap use."
        elif name == "B03_CROSS_PROVIDER_AUTHORITY_TASK":
            artifacts = get(data.get("cross_provider_fixture", {}), "portable_artifacts")
            packets = [] if artifacts is MISSING else [p for p in artifacts if p.get("source_class") == "portable_derived_consumption_view"]
            measures = {"packets": {"count": len(packets), "bytes": sum(p["bytes"] for p in packets)}}
            facts = [assertion(measures, "packets", "count", "le", contract["max_packet_count"]),
                     assertion(measures, "packets", "bytes", "le", contract["max_packet_materialization_bytes"])]
            for fact in facts:
                fact.update(source_key="cross_provider_fixture", pointer="/portable_artifacts (packet entries)", packet_entries=packets)
            facts += [assertion(data, "cross_provider_eval", "checks/provider_non_openai", "eq", contract["non_openai_provider_required"]),
                      assertion(data, "cross_provider_eval", "checks/packet_id_exact"),
                      assertion(data, "cross_provider_fixture", "portable_artifacts", "nonempty")]
            # Zero packets cannot establish a completed packet-based experiment.
            facts.append({"source_key": "cross_provider_fixture", "pointer": "/portable_artifacts", "measured": len(packets),
                          "required": "at least one observed packet", "satisfied": bool(packets)})
            reason = "Measure materialized packet bytes, not canonical LF bytes or the unrelated complete source corpus; verify actual non-OpenAI use from the listed evaluation."
        elif name == "B04_REAL_WORKSTREAM_STRESS":
            declarations = get(data.get("q4", {}), "source_verification")
            measured = {"q4": {"reads": len(declarations) if declarations is not MISSING else None}}
            facts = [assertion(measured, "q4", "reads", "le", contract["max_declared_source_reads"]),
                     assertion(data, "q4", "metrics/recovery_replay_count", "le", contract["max_recovery_replays"]),
                     assertion(data, "q4", "metrics/live_target_hash_before_after/unchanged", "eq", contract["live_target_mutation_forbidden"])]
            facts[0]["pointer"] = "/source_verification (declared source count)"
            reason = "Count the recorded declared source reads and recovery replays; require the measured live target to remain unchanged."
        else:
            raise ValueError(f"Unsupported frozen budget: {name}")
        result.append({"budget_id": name, "thresholds": contract, "measurements": facts,
                       "evidence_source_keys": sorted({f["source_key"] for f in facts}),
                       "disposition": "PASS" if all(f["satisfied"] for f in facts) else "FAIL", "reason": reason})
    return result


def scenario_rules(data, budget_results):
    """Each rule is a separate semantic condition tied to the frozen sources."""
    rules = {}

    def add(scenario, dimension, ids, reason, *specs):
        facts = [assertion(data, *spec) for spec in specs]
        rules[(scenario, dimension)] = {"dimension": dimension, "affected_item_ids": ids.split(),
            "evidence_source_keys": sorted({f["source_key"] for f in facts}), "facts": facts,
            "disposition": "PASS" if facts and all(f["satisfied"] for f in facts) else "FAIL", "reason": reason}

    def budget_fact(scenario, dimension, budget_id, ids, reason):
        b = next(b for b in budget_results if b["budget_id"].startswith(budget_id))
        rules[(scenario, dimension)] = {"dimension": dimension, "affected_item_ids": ids.split(),
            "evidence_source_keys": b["evidence_source_keys"], "facts": b["measurements"],
            "budget_reference": b["budget_id"], "disposition": b["disposition"], "reason": reason}

    add(1, "project_current_state_orientation", "KA-R02 KA-R04 KA-R05 KA-R35 KA-I11 KA-I15",
        "The compact core matches frozen live markers and preserves the active stage and paused Source Vault state.",
        ("current_core", "comparison/current_state_live_marker_parity", "all_true"),
        ("current_core", "comparison/routing_subset_exact_parity"))
    add(1, "route_parent_objective", "KA-R06 KA-R25 KA-R26 KA-I09 KA-I15",
        "The core exposes the parent redesign objective and a typed paused-workstream resume target; zero-seed routing has exact parity.",
        ("current_core", "generation/current_state_core/active_stage/objective", "nonempty"),
        ("current_core", "generation/current_state_core/paused_workstreams/0/resume_target", "nonempty"),
        ("zero_seed", "comparison/routing_exact_parity"))
    add(1, "important_omission", "KA-R04 KA-R05 KA-R17 KA-R43 KA-I07",
        "Every declared must-preserve unit is recoverable; the Source Vault audit, backup, restore and Course 2 constraints remain explicit.",
        ("current_core", "generation/must_preserve_items_missing", "eq", []),
        ("current_core", "generation/source_vault_evidence_alignment/checks", "all_true"))
    budget_fact(1, "context_read_tool_cost", "B01", "KA-R30 KA-R31 KA-R32 KA-I12", "Apply B01 without changing the core-size or recoverability limits.")
    add(1, "active_surface_maintenance_burden", "KA-R21 KA-R32 KA-R33 KA-R34 KA-R47 KA-R50 KA-I03 KA-I13",
        "Source-owned workstreams replace copied global generation facts; decomposition covers the complete surface and exposes pressure and drift.",
        ("zero_seed", "generation/global_live_state_generation_fact_count", "eq", 0),
        ("current_core", "generation/global_target_generation_fact_count", "eq", 0),
        ("decomposition", "audit_checks/complete_nonoverlapping_line_coverage"),
        ("decomposition", "audit_checks/drift_findings_programmatically_reproduced"))

    # The allowed integrated final result is an evidence receipt. It records the
    # earlier evaluation; no unlisted collaborator result is followed or read.
    integrated = ("q125", "checks/fresh_collaborator_oracle_evaluation_pass")
    add(2, "project_current_state_orientation", "KA-R01 KA-R03 KA-R04 KA-I01 KA-I11", "The frozen fresh-collaborator evaluation attests safe task-shaped reconstruction; the preserved result is unchanged.", integrated, ("q125", "checks/fresh_collaborator_result_preserved_exactly"))
    add(2, "governing_source_discovery_resolution", "KA-R07 KA-R08 KA-R09 KA-R13 KA-I05", "The integrated consequential-task evaluation attests governing-source activation; receipt follows the exact frozen index and source basis remains auditable.", integrated, ("q125", "source_revision_binding_finding/receipt_follows_frozen_index"), ("q125", "source_revision_binding_finding/indexed_matches_git_blob"))
    add(2, "risk_open_obligation_activation", "KA-R10 KA-I05", "The integrated evaluation supplies recorded authority/risk-task evidence; candidate section 51 identifies the tested stale-authority failure and risk activation.", integrated, ("candidate", "", "contains", "visible stale-authority failure"))
    add(2, "action_task_fidelity", "KA-R09 KA-R13 KA-I05", "The preserved consequential-task evaluation and exact promoted statement/source-basis checks support constraint fidelity within this task.", integrated, ("q125", "checks/promoted_statement_matches_capture"), ("q125", "checks/promoted_source_basis_matches_capture"))
    add(2, "uncertainty_visibility", "KA-R08 KA-R11 KA-I06", "The revision-basis ambiguity is reported rather than normalized away, alongside the evaluated fail-visible stale-authority behavior.", integrated, ("q125", "checks/source_revision_basis_ambiguity_preserved"), ("q125", "source_revision_binding_finding/finding", "eq", "SOURCE_REVISION_BASIS_AMBIGUOUS"))
    add(2, "important_omission", "KA-R01 KA-R17 KA-R18 KA-I07", "Use the recorded fresh-task evaluation plus reviewed source/statement fidelity; do not claim independent access to the unlisted underlying task output.", integrated, ("q125", "checks/explicit_promotion_review_all_checks_pass"), ("q125", "checks/promoted_source_basis_matches_capture"))
    budget_fact(2, "context_read_tool_cost", "B02", "KA-R30", "Apply B02 to the recorded read manifest totals, including zero legacy bootstrap reads.")

    add(3, "governing_source_discovery_resolution", "KA-R07 KA-R13 KA-R14 KA-R24 KA-R36 KA-I05 KA-I11", "The external evaluation checks governing IDs, resolution and retrieval non-authority for resolved and scope-incomplete actions.", *[("cross_provider_eval", "checks/" + x) for x in ["task_a_resolved_semantics", "task_a_governing_ids", "task_a_retrieval_non_authoritative", "task_b_governing_ids_empty", "task_c_governing_architecture_ids", "provider_non_openai", "fresh_session", "prior_ads_context_false"]])
    add(3, "supersession_conflict_handling", "KA-R14 KA-R16 KA-R24 KA-R49 KA-I04 KA-I06", "Partial supersession retains applicable outcomes; unresolved scope leaves no invented governing set.", *[("cross_provider_eval", "checks/" + x) for x in ["task_c_resolved_semantics", "task_c_retained_outcomes", "task_b_unresolved_semantics", "task_b_governing_ids_empty"]])
    add(3, "uncertainty_visibility", "KA-R11 KA-R36 KA-I06", "Insufficient scope remains visible, with exact provider/model and fresh-session provenance.", *[("cross_provider_eval", "checks/" + x) for x in ["task_b_missing_scope_visible", "task_b_unresolved_semantics", "exact_model_recorded", "prior_ads_context_false"]])
    add(3, "action_task_fidelity", "KA-R09 KA-R13 KA-R14 KA-R24 KA-I05", "The evaluated actions respect the public Git exclusion and keep probabilistic nominations subordinate to authority.", *[("cross_provider_eval", "checks/" + x) for x in ["task_c_public_git_exclusion", "task_a_retrieval_non_authoritative", "task_b_retrieval_non_authoritative", "task_c_retrieval_non_authoritative"]])
    add(3, "important_omission", "KA-R14 KA-R17 KA-R18 KA-R36 KA-I07", "The evaluation explicitly tests retained outcomes, governing IDs, missing scope and receipt source revision.", *[("cross_provider_eval", "checks/" + x) for x in ["task_c_retained_outcomes", "task_b_missing_scope_visible", "task_c_governing_architecture_ids", "receipt_base_commit"]])
    budget_fact(3, "context_read_tool_cost", "B03", "KA-R30 KA-R36", "Use the allowed cross-provider fixture for materialization cost and its evaluation for actual provider use.")

    add(4, "supersession_conflict_handling", "KA-R12 KA-R14 KA-R15 KA-R16 KA-R46 KA-R49 KA-I04 KA-I17", "Q3 preserves scope-specific successors, retained outcomes and collision-free carrier continuity without inventing effective dates.", ("q3", "real_semantic_query_failures", "eq", []), ("q3", "real_semantics_alignment/Q3-R01/retained_outcomes", "nonempty"), ("q3", "real_semantics_alignment/Q3-R02/scope_successors", "nonempty"), ("q3", "real_semantics_alignment/Q3-R02/invented_per_successor_effective_dates", "eq", False), ("q3", "real_semantics_alignment/Q3-R03/identity_collision", "eq", False))
    add(4, "uncertainty_visibility", "KA-R11 KA-R15 KA-R16 KA-R49 KA-I04 KA-I06", "Residual applicability and unexercised real transition classes stay explicit; no missing temporal value is guessed.", ("q3", "real_semantics_alignment/Q3-R02/residual_applicability", "nonempty"), ("q3", "interpretation/unproven_real_transition_classes", "nonempty"), ("q3", "real_semantics_alignment/Q3-R02/invented_per_successor_effective_dates", "eq", False))
    add(4, "important_omission", "KA-R12 KA-R15 KA-R16 KA-R46 KA-R49 KA-I04 KA-I17", "The actual Q3 cases retain original identity as provenance, pause continuity and independent/comparative epistemic roles. Untested transition classes are assessed separately under their conditional scope.", ("q3", "real_semantics_alignment/Q3-R03/original_identity_disposition", "eq", "RETIRED_PROVENANCE_ONLY"), ("q3", "real_semantics_alignment/Q3-R04/semantic_identity_preserved_while_paused"), ("q3", "real_semantics_alignment/Q3-R05/independent_substantive_base", "nonempty"), ("q3", "real_semantics_alignment/Q3-R05/comparative_trigger", "nonempty"), ("q3", "real_semantic_query_failures", "eq", []))

    add(5, "route_parent_objective", "KA-R06 KA-R25 KA-R26 KA-R27 KA-I09 KA-I15", "The real workstream graph records parents, multiple dependency edges and explicit pause return targets; DAG behavior is evaluated.", ("q4", "graph/acyclic"), ("q4", "graph/parent_relationships", "nonempty"), ("q4", "graph/node_states/WS-SOURCE-VAULT-BOOTSTRAP/pause_reason", "nonempty"), ("q4", "graph/node_states/WS-SOURCE-VAULT-BOOTSTRAP/return_condition", "nonempty"), ("q4", "graph/node_states/WS-SOURCE-VAULT-BOOTSTRAP/resume_target", "nonempty"), ("q4_eval", "checks/q4_dependency_list_exact"), ("q4_eval", "checks/q10_dependency_list_exact"))
    add(5, "uncertainty_visibility", "KA-R08 KA-R11 KA-R23 KA-R28 KA-R29 KA-I06 KA-I15", "Recovery distinguishes durable completed work from pending work and exposes stale revision rejection without mutation, using an explicit immutable revision descriptor.", ("q4", "cases/1/completed_steps", "nonempty"), ("q4", "cases/1/pending_steps", "nonempty"), ("q4", "cases/2/attempts/1/expected_revision_matches", "eq", False), ("q4", "cases/2/attempts/1/mutated", "eq", False), ("q4", "metrics/revision_binding_basis/hash_basis", "eq", "GIT_BLOB_BYTES_AT_COMMIT"), ("q4", "metrics/revision_binding_basis/source_commit", "nonempty"), ("q4_eval", "checks/writer_a_stale_semantics"))
    add(5, "action_task_fidelity", "KA-R27 KA-R28 KA-R29 KA-I05", "The resumed plan starts at pending work; fresh writes apply to a shadow copy and the stale attempt leaves the copy and live target intact.", ("q4", "cases/1/blind_replay_required", "eq", False), ("q4", "cases/1/interruption/recovery_unchanged"), ("q4", "cases/2/stale_attempt_mutation", "eq", False), ("q4_eval", "checks/next_resume_step"), ("q4_eval", "checks/writer_b_fresh"), ("q4_eval", "checks/writer_c_fresh"), ("q4", "cases/2/live_target/unchanged"))
    budget_fact(5, "active_surface_maintenance_burden", "B04", "KA-R27 KA-R28 KA-R29 KA-R30 KA-R33 KA-I13", "Bound the declared source neighborhood and require zero recovery replay or live mutation under B04.")

    add(6, "governing_source_discovery_resolution", "KA-R37 KA-R39 KA-R42 KA-I10 KA-I14", "Public authority stays usable and distinct from delegated private verification; required unavailable or stale private evidence blocks.", ("q7", "public_contract_checks", "all_true"), ("q7", "scenarios/Q7-S02/task_disposition", "eq", "BLOCK_REQUIRED_PRIVATE_UNVERIFIED"), ("q7", "scenarios/Q7-S03/task_disposition", "eq", "BLOCK_PRIVATE_CONTINUITY_FAIL"))
    add(6, "risk_open_obligation_activation", "KA-R10 KA-R39 KA-R42 KA-I14", "Required private uncertainty activates a block and optional retrieval failure cannot bypass authority.", ("q7", "scenarios/Q7-S02/task_disposition", "eq", "BLOCK_REQUIRED_PRIVATE_UNVERIFIED"), ("q7", "scenarios/Q7-S05/optional_retrieval_authority_bypass", "eq", False))
    add(6, "uncertainty_visibility", "KA-R11 KA-R37 KA-R39 KA-R42 KA-I06 KA-I14", "NOT_VERIFIED and FAIL remain separate from the preserved public RESOLVED_PRIVATE conclusion.", ("q7", "scenarios/Q7-S01/private_continuity_status", "eq", "NOT_VERIFIED"), ("q7", "scenarios/Q7-S03/private_continuity_status", "eq", "FAIL"), ("q7", "scenarios/Q7-S03/public_resolved_private_preserved"), ("q7", "interpretation/public_repository_integrity_reclassified_by_private_status", "eq", False))
    add(6, "important_omission", "KA-R17 KA-R37 KA-R38 KA-R39 KA-I07 KA-I10", "The public projection preserves the Course 2 block and public authority while excluding private values and paths.", ("q7", "global_private_value_leak_count", "eq", 0), ("q7", "global_private_paths_serialized_count", "eq", 0), ("q7", "scenarios/Q7-S04/public_safe_state/course_2_allowed", "eq", False), ("q7", "scenarios/Q7-S04/public_authority_preserved"))

    add(7, "route_parent_objective", "KA-R06 KA-R25 KA-R43 KA-R45 KA-I15", "The migration workstream retains a semantic identity, parent, phase and reconstructable next action.", ("q9", "self_hosting/complete"), ("q9", "self_hosting/parent", "nonempty"), ("q9", "self_hosting/next_action", "nonempty"), ("q9", "identity_and_provenance/path_used_as_semantic_identity", "eq", False))
    add(7, "governing_source_discovery_resolution", "KA-R19 KA-R20 KA-R43 KA-R44 KA-I02 KA-I08", "The old continuity architecture remains operational authority; migration is source-bound shadow work and switching is blocked.", ("q9", "policy_grounding", "all_true"), ("q9", "authority_switch/current_operational_authority", "eq", "CURRENT_CONTINUITY_ARCHITECTURE"), ("q9", "authority_switch/allowed", "eq", False), ("q9", "identity_and_provenance/migration_provenance_bound_to_real_base"))
    add(7, "uncertainty_visibility", "KA-R11 KA-R44 KA-R45 KA-I06 KA-I08", "Absent selection/acceptance and the shadow-only rollback boundary remain explicit, not an implied production cutover.", ("q9", "authority_switch/blockers", "contains", "OWNER_TARGET_ACCEPTANCE_ABSENT"), ("q9", "interpretation/production_authority_migrated", "eq", False), ("q9", "interpretation/rollback_executed_against_live_authority", "eq", False))
    add(7, "important_omission", "KA-R17 KA-R18 KA-R43 KA-R46 KA-I07 KA-I17", "All declared migration units have parity; reverse references remain intact and identity/provenance do not collapse to paths.", ("q9", "migration_unit_parity", "all_true"), ("q9", "broken_reverse_reference_target_count", "eq", 0), ("q9", "identity_and_provenance/path_used_as_semantic_identity", "eq", False), ("q9", "identity_and_provenance/migration_provenance_bound_to_real_base"))
    add(7, "active_surface_maintenance_burden", "KA-R33 KA-R43 KA-R44 KA-R45 KA-I08 KA-I13", "A lossless legacy export passes its validator with unchanged live authority; the measured migration slice is preserved as the scope of this proof.", ("q9", "rollback_export/routing_exact_parity"), ("q9", "rollback_export/legacy_validator_pass"), ("q9", "rollback_export/live_authority_mutation_detected", "eq", False), ("q9", "reverse_reference_counts", "nonempty"))

    add(8, "governing_source_discovery_resolution", "KA-R18 KA-R20 KA-R22 KA-R48 KA-I03 KA-I16", "Capture is candidate knowledge and promotion requires an explicit source-traceable review.", ("q125", "checks/promotion_transition_was_not_automatic"), ("q125", "checks/explicit_promotion_review_accepts"), ("q125", "checks/promoted_source_basis_matches_capture"), ("shadow_v02", "consolidation/capture_authority/CAP-1", "eq", "candidate"))
    add(8, "action_task_fidelity", "KA-R01 KA-R17 KA-R18 KA-R22 KA-R48 KA-I07 KA-I16", "The accepted statement matches capture, while the synthetic negative-control promotion is blocked for fidelity loss.", ("q125", "checks/promoted_statement_matches_capture"), ("q125", "checks/explicit_promotion_review_all_checks_pass"), ("shadow_v02", "consolidation/promotions/PROMOTE-BAD/status", "eq", "PROMOTION_BLOCKED_FIDELITY"))
    add(8, "uncertainty_visibility", "KA-R11 KA-R17 KA-R48 KA-I06 KA-I16", "Missing fidelity units and revision-basis uncertainty stay visible; captured material remains outside accepted views.", ("shadow_v02", "consolidation/candidates/SYN-BAD/missing_units", "nonempty"), ("shadow_v02", "consolidation/accepted_view_excludes", "contains", "CAP-1"), ("q125", "checks/source_revision_basis_ambiguity_preserved"))
    add(8, "important_omission", "KA-R01 KA-R03 KA-R17 KA-R18 KA-R21 KA-R22 KA-R48 KA-I03 KA-I07 KA-I16", "Successful consolidation has no missing units, preserves latent recovery/provenance, and carries the exact reviewed source basis into shadow promotion.", ("shadow_v02", "consolidation/candidates/SYN-GOOD/missing_units", "eq", []), ("shadow_v02", "consolidation/promotions/PROMOTE-GOOD/recoverable_latent_units", "nonempty"), ("shadow_v02", "consolidation/promotions/PROMOTE-GOOD/provenance_capture_ids", "nonempty"), ("q125", "checks/promoted_source_basis_matches_capture"))

    add(9, "project_current_state_orientation", "KA-R04 KA-R05 KA-R21 KA-R31 KA-R32 KA-R47 KA-I03 KA-I12 KA-I15", "Current views are stable across synthetic history scales and real compact-core markers match their frozen comparison boundary.", ("shadow_v01", "refresh_and_rebuild/current_view_digest_equal_across_scales"), ("current_core", "comparison/current_state_live_marker_parity", "all_true"), ("zero_seed", "comparison/routing_exact_parity"))
    add(9, "context_read_tool_cost", "KA-R30 KA-R31 KA-R32 KA-I12", "At baseline, 5x and 10x history, normal identity lookup stays one indexed step; global rebuild growth is separately reported and allowed by the requirement.", *[("shadow_v01", f"refresh_and_rebuild/scales/{scale}/normal_identity_lookup_steps", "eq", 1) for scale in [20, 100, 200]], ("shadow_v01", "refresh_and_rebuild/current_view_digest_equal_across_scales"))
    add(9, "active_surface_maintenance_burden", "KA-R21 KA-R31 KA-R32 KA-R33 KA-R34 KA-R47 KA-R50 KA-I03 KA-I12 KA-I13", "The measured ordinary change scans one owner and refreshes two dependent views; real routing uses two source touches and no global control registry.", ("shadow_v01", "refresh_and_rebuild/incremental/incremental_source_scans", "eq", 1), ("shadow_v01", "metrics/generated_locations_refreshed_for_change", "eq", 2), ("zero_seed", "metrics/manual_shadow_source_touch_count", "eq", 2), ("zero_seed", "metrics/broad_project_control_source_count", "eq", 0), ("decomposition", "audit_checks/drift_findings_programmatically_reproduced"))
    add(9, "important_omission", "KA-R17 KA-R21 KA-R31 KA-R32 KA-R43 KA-R50 KA-I03 KA-I07 KA-I12", "The real current-core must-preserve set is fully recoverable and block coverage is complete; classification alone is not proposition-level deletion permission.", ("current_core", "generation/must_preserve_items_missing", "eq", []), ("current_core", "generation/source_vault_evidence_alignment/all_aligned"), ("decomposition", "audit_checks/complete_nonoverlapping_line_coverage"), ("decomposition", "interpretation_limits", "nonempty"))
    return rules


def limitations(data):
    records = []

    def add(identifier, ids, source_specs, observation, condition, reason, disposition="NON_BLOCKING_RESIDUAL_LIMITATION"):
        facts = [assertion(data, *spec) for spec in source_specs]
        established = bool(facts) and all(f["satisfied"] for f in facts)
        records.append({"limitation_id": identifier, "affected_item_ids": ids.split(),
            "evidence_source_keys": sorted({"requirements", *[f["source_key"] for f in facts]}),
            "observed_limitation": observation, "required_condition": condition,
            "facts": facts, "disposition": disposition if established else "BLOCKING_CONTRADICTION_OR_MISSING_EVIDENCE",
            "blocks_final_disposition": not established,
            "reason": reason if established else "The stated scope/compensating evidence is absent or contradicts the frozen record: " + reason})

    add("L01_REAL_TRANSITIONS_UNEXERCISED", "KA-R12 KA-R15 KA-R16 KA-R43 KA-R46 KA-R49 KA-I04 KA-I17",
        [("q3", "interpretation/unproven_real_transition_classes", "eq", ["MERGE", "SPLIT", "TOMBSTONE"]),
         ("q3", "real_semantic_query_failures", "eq", []),
         ("shadow_v01", "identity/current_targets/S-B", "eq", ["S-B1", "S-B2"]),
         ("shadow_v01", "identity/current_targets/S-M", "eq", ["S-A", "S-B1", "S-B2"]),
         ("q9", "identity_and_provenance/path_used_as_semantic_identity", "eq", False)],
        "Q3 did not exercise real MERGE, SPLIT or TOMBSTONE transitions; synthetic identity evidence is not relabeled real.",
        "R43 reconciles transition semantics where they affect identity/authority; R46/I17 require capability where continuity is deliberately declared. R15/R16/R49 are materiality-selective.",
        "The frozen Q3 cases resolve their actual relationships, time and carrier continuity, synthetic targets demonstrate split/merge capability, and Q9 preserves declared semantic IDs. The boundary does not require a real instance of every possible transition class. The absence remains a residual coverage limit, not evidence of a lost required identity.")
    add("L02_SHADOW_MIGRATION_BOUNDARY", "KA-R19 KA-R43 KA-R44 KA-R45 KA-R46 KA-I07 KA-I08 KA-I17",
        [("q9", "migration_unit_parity", "all_true"), ("q9", "rollback_export/routing_exact_parity"),
         ("q9", "rollback_export/legacy_validator_pass"), ("q9", "self_hosting/complete"),
         ("q9", "interpretation/production_authority_migrated", "eq", False),
         ("q9", "interpretation/rollback_executed_against_live_authority", "eq", False)],
        "Q9 proves ten frozen migration units, reverse-reference safety and exporter rollback only in shadow; no live cutover or live rollback occurred.",
        "R43 requires preservation of migrated meaning; R44/I08 retain old authority until a separately qualified switch; R45 requires reconstructable self-evolution capability.",
        "Parity, semantic identities and source-bound migration continuation support the tested capability. Production migration is a later governed stage; absence of a live switch satisfies the current transition boundary. This is not a whole-repository production-migration completion claim.")
    add("L03_AUTHORITY_REMAINS_CURRENT", "KA-R19 KA-R20 KA-R22 KA-R44 KA-R45 KA-I01 KA-I02 KA-I03 KA-I08 KA-I16",
        [("q9", "authority_switch/current_operational_authority", "eq", "CURRENT_CONTINUITY_ARCHITECTURE"),
         ("q9", "authority_switch/allowed", "eq", False), ("q125", "checks/current_authority_unchanged")],
        "The present continuity architecture and public repository remain authoritative. Earlier shadow promotion did not accept Candidate 01 as the project target.",
        "R19/R44/I08 demand an explicit separately accepted authority transition.",
        "Qualification may permit owner target selection; it cannot select a target or grant an authority switch. The implementation writes only research artifacts.", "OUTSIDE_REQUIRED_CONDITION_OR_SCOPE")
    add("L04_REVISION_BASIS_AMBIGUITY", "KA-R08 KA-R18 KA-R23 KA-R29 KA-R36 KA-I05 KA-I07 KA-I15",
        [("q125", "source_revision_binding_finding/finding", "eq", "SOURCE_REVISION_BASIS_AMBIGUOUS"),
         ("q125", "source_revision_binding_finding/receipt_follows_frozen_index"),
         ("q125", "source_revision_binding_finding/indexed_matches_git_blob"),
         ("candidate", "", "contains", "No validator may silently guess a normalization rule after mismatch."),
         ("q4", "metrics/revision_binding_basis/hash_basis", "eq", "GIT_BLOB_BYTES_AT_COMMIT"),
         ("q4_eval", "checks/revision_hash_basis"),
         ("matrix", "prototype_evidence_q1_q2_cross_provider_v01/materialization_semantic_equivalence_verified")],
        "The Q125 bare SHA is ambiguous across Git LF and Windows CRLF bytes. Its receipt follows the frozen index; earlier evaluator repairs are preserved.",
        "R08/R23 require observable traversal and revision/freshness binding sufficient to detect stale material; R36 requires portable durable continuity.",
        "Candidate section 50 explicitly amends descriptors. Q4 exercises commit/path/algorithm/basis/digest and the later cross-provider record distinguishes canonical and materialized bytes. This addresses the final mechanism condition without rewriting the earlier ambiguous receipt; old receipts remain bounded by their declared index provenance.")
    add("L05_MANUAL_ENGINE_PROVENANCE", "KA-R03 KA-R08 KA-R36 KA-I11",
        [("q125", "collaborator_exact_engine_provenance_recorded", "eq", False),
         ("cross_provider_eval", "checks/provider_non_openai"), ("cross_provider_eval", "checks/exact_model_recorded"),
         ("cross_provider_eval", "checks/fresh_session"), ("cross_provider_eval", "checks/prior_ads_context_false")],
        "The manual integrated run lacks exact engine/thread provenance and does not itself earn provider-portability credit.",
        "R03/I11 exclude dependence on prior conversation; R36 requires different capable collaborators to reconstruct from project-controlled state, not equal provider performance.",
        "Keep Q125 as conversation-independence evidence. The separate bounded non-OpenAI experiment supplies actual portability evidence with provider/model/freshness checks. No engine identity is invented for Q125.")
    add("L06_LABEL_VARIANCES", "KA-R11 KA-R14 KA-R24 KA-R29 KA-R36 KA-I04 KA-I06",
        [("q4_eval", "oracle_label_variance/semantic_match"),
         ("q4", "cases/2/attempts/1/mutated", "eq", False),
         ("cross_provider_eval", "status_label_variances/task_b_status/semantic_match"),
         ("cross_provider_eval", "status_label_variances/task_c_status/semantic_match"),
         ("cross_provider_eval", "checks/task_b_missing_scope_visible"),
         ("cross_provider_eval", "checks/task_c_retained_outcomes")],
        "Q4 uses REJECTED_STALE_REVISION; external task B uses UNRESOLVED_INSUFFICIENT_SCOPE and task C uses RESOLVED. Earlier literal label differences remain recorded.",
        "R11/R14/R24/R29 demand visible unresolved scope, retained authority semantics and stale-write safety, not these historical status-label spellings.",
        "The listed evaluations test semantic equivalence and the Q4 result records no stale mutation. The missing-scope and retained-outcome checks independently support those semantics; no label comparison with a Q10 oracle is performed.", "OUTSIDE_REQUIRED_CONDITION_OR_SCOPE")
    add("L07_PACKET_MATERIALIZATION", "KA-R08 KA-R23 KA-R30 KA-R36 KA-I15",
        [("matrix", "prototype_evidence_q1_q2_cross_provider_v01/portable_packet_materialization_basis", "eq", "WINDOWS_WORKTREE_CRLF_BYTES"),
         ("matrix", "prototype_evidence_q1_q2_cross_provider_v01/portable_packet_canonical_hash_basis", "eq", "GIT_BLOB_BYTES_AT_COMMIT"),
         ("matrix", "prototype_evidence_q1_q2_cross_provider_v01/materialization_semantic_equivalence_verified")],
        "Portable packet materialization and canonical Git blob have different byte identities. The packet itself is not a Q10-listed source and is not opened.",
        "B03 freezes packet materialization bytes; R23/R36 require explicit portable source binding.",
        "Use the listed cross-provider fixture's packet byte count for B03, and preserve both identity bases from the matrix. Do not normalize, substitute canonical size, or recursively read packet dependencies.")
    add("L08_DECOMPOSITION_GRANULARITY", "KA-R04 KA-R05 KA-R17 KA-R21 KA-R31 KA-R32 KA-R33 KA-R34 KA-R43 KA-R47 KA-R50 KA-I03 KA-I07 KA-I12 KA-I13",
        [("decomposition", "interpretation_limits", "nonempty"),
         ("decomposition", "audit_checks/complete_nonoverlapping_line_coverage"),
         ("current_core", "generation/must_preserve_items_missing", "eq", []),
         ("current_core", "generation/source_vault_evidence_alignment/all_aligned")],
        "Decomposition is block-level, not proposition-level. Zero E bytes does not establish absence of all unresolved propositions; four drift findings and canonical-source migration needs remain recorded.",
        "R17/R43/I07 require the target view's must-preserve fidelity before detail can be made latent; R50 is a recurring consolidation capability.",
        "The later compact-core probe supplies the specific missing Source Vault ownership and view-fidelity evidence. Its 23-unit proof supports that view, not unrestricted deletion. The original global surface is preserved and production migration still requires scoped reconciliation.")
    add("L09_MIGRATION_SEEDS_AND_SCALE_SCOPE", "KA-R02 KA-R05 KA-R06 KA-R21 KA-R25 KA-R31 KA-R32 KA-R33 KA-R34 KA-R47 KA-R50 KA-I02 KA-I03 KA-I12 KA-I13 KA-I15",
        [("real_shadow", "metrics/migration_seed_workstream_count", "eq", 1),
         ("real_shadow", "metrics/migration_seed_project_control_fact_count", "eq", 3),
         ("zero_seed", "metrics/global_live_state_generation_fact_count", "eq", 0),
         ("current_core", "metrics/global_target_generation_fact_count", "eq", 0),
         ("shadow_v01", "refresh_and_rebuild/current_view_digest_equal_across_scales"),
         ("candidate", "", "contains", "Linear full-rebuild scan cost does not by itself violate")],
        "Early real shadow used one seeded workstream and three seeded control facts. The 5x/10x passive-history scale exercise is synthetic; full rebuild scans grow with corpus size.",
        "R31/I12 concern mandatory reconstruction cost, and R33/I13 permit periodic full rebuilds while ordinary maintenance follows the affected neighborhood.",
        "Later zero-seed and compact-core results remove global target generation inputs for their measured slices. Synthetic scale invariance, source-local refresh and real compact-core/ownership evidence jointly support structural boundedness; this is not a measured production-wide 10x deployment or a universal constant-time rebuild claim.")
    add("L10_PRIVATE_FRESHNESS_FAILURE", "KA-R11 KA-R37 KA-R38 KA-R39 KA-R42 KA-I06 KA-I10 KA-I14",
        [("q7", "interpretation/private_continuity_current_against_public_target", "eq", False),
         ("q7", "scenarios/Q7-S03/task_disposition", "eq", "BLOCK_PRIVATE_CONTINUITY_FAIL"),
         ("q7", "global_private_value_leak_count", "eq", 0),
         ("q7", "interpretation/public_repository_integrity_reclassified_by_private_status", "eq", False)],
        "Private continuity was FAIL against its frozen public target; it was not repaired by the Q7 experiment.",
        "R37/R39/R42 require explicit freshness and consequence-sensitive blocking while public authority remains independent.",
        "The recorded failure activates the required private-task block and does not invent a public contradiction or leak private state. Actual private-task execution remains blocked at that historical boundary; qualification of safe degradation does not require silently converting it to verified.", "OUTSIDE_REQUIRED_CONDITION_OR_SCOPE")
    add("L11_EARLIER_REPAIRS_AND_HISTORICAL_BOUNDARIES", "KA-R08 KA-R18 KA-R23 KA-R25 KA-R27 KA-R28 KA-R36 KA-I07 KA-I15",
        [("q125", "evaluator_repair_summary", "nonempty"),
         ("matrix", "prototype_evidence_q3_real_v01/implementation_repairs_after_first_run", "eq", 1),
         ("q4", "graph/node_states/WS-Q10-FINAL/runnable", "eq", False),
         ("cross_provider_eval", "checks/fresh_session"),
         ("cross_provider_eval", "checks/task_c_retained_outcomes")],
        "Prior synthetic/Q3/Q125 repairs and earlier blocked Q4 graph states are historical evidence, not Q10 first-run repairs or Checkpoint 519 live state. Matrix historical result SHA fields may use earlier artifact/materialization bases.",
        "R08/R18/R23 require source-bound auditable evidence; R25/R28 preserve intended versus completed work at the relevant boundary.",
        "Use exact Q10 fixture blobs as source identity, retaining embedded historical provenance rather than treating it as a competing current digest. Q4's older portability/hard-case blocks describe its own frozen boundary; the later cross-provider evidence addresses those gaps. No prior result is overwritten or credited as this run's output.")
    add("L12_SERIALIZED_CONCURRENCY_SCOPE", "KA-R27 KA-R28 KA-R29 KA-R33 KA-I13",
        [("q4", "cases/2/schedule", "eq", "FIXTURE_ORDER_SERIALIZED_CAS"),
         ("q4", "cases/2/update_storage", "eq", "IN_MEMORY_ONLY"),
         ("q4", "cases/2/stale_attempt_mutation", "eq", False),
         ("q4", "cases/2/live_target/unchanged"), ("q4_eval", "checks/stale_attempt_preserves_temp_state")],
        "Q4 uses serialized compare-and-swap attempts on an in-memory copy, not a deployed multi-process contention benchmark.",
        "R29 requires detection of stale/conflicting updates and forbids silent last-writer-wins semantic corruption.",
        "The controlled stale interleaving exercises the required expected-revision rejection and no-mutation semantics on a real source binding. It establishes that safety mechanism, with deployment contention/performance remaining outside this bounded experiment.")
    return records


EVIDENCE_MAP = {
    "prototype_evidence_real_v01": "real_shadow",
    "prototype_evidence_zero_seed_routing_v01": "zero_seed",
    "prototype_evidence_current_state_decomposition_v01": "decomposition",
    "prototype_evidence_current_state_core_v01": "current_core",
    "prototype_evidence_q3_real_v01": "q3",
    "prototype_evidence_q7_real_v01": "q7",
    "prototype_evidence_q9_migration_v01": "q9",
    "prototype_evidence_q1_q2_q5_integrated_v01": "q125",
    "prototype_evidence_q4_real_v01": "q4",
    "prototype_evidence_q1_q2_cross_provider_v01": "cross_provider_eval",
}


def real_item_evidence(data):
    records = {item: [] for item in ITEM_IDS}
    matrix = data.get("matrix", {})
    for section, key in EVIDENCE_MAP.items():
        entry = matrix.get(section, {})
        if not entry.get("evidence_class", "").startswith("REAL") or key not in data:
            continue
        for field in ["supported_mechanism_ids", "supported_with_limitation_ids"]:
            for item in entry.get(field, []):
                if item in records:
                    records[item].append({"source_key": key, "matrix_source_key": "matrix",
                        "matrix_pointer": f"/{section}/{field}", "evidence_class": entry["evidence_class"],
                        "prior_final_qualification_credit": entry.get("final_qualification_credit"),
                        "prior_support_requires_q10_assessment": True})
    return records


def run_command(command, timeout=1800):
    started = time.monotonic()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1")
    print("Executing: " + subprocess.list2cmdline(command), flush=True)
    try:
        process = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                                 encoding="utf-8", errors="replace", env=env, timeout=timeout)
        record = {"argv": command, "command": subprocess.list2cmdline(command),
                  "returncode": process.returncode, "stdout": process.stdout, "stderr": process.stderr,
                  "timed_out": False}
    except subprocess.TimeoutExpired as exc:
        def decoded(value):
            return value.decode("utf-8", "replace") if isinstance(value, bytes) else (value or "")
        record = {"argv": command, "command": subprocess.list2cmdline(command),
                  "returncode": None, "stdout": decoded(exc.stdout), "stderr": decoded(exc.stderr), "timed_out": True}
    except OSError as exc:
        record = {"argv": command, "command": subprocess.list2cmdline(command),
                  "returncode": None, "stdout": "", "stderr": str(exc), "timed_out": False}
    record["elapsed_seconds"] = round(time.monotonic() - started, 3)
    record["disposition"] = "PASS" if record["returncode"] == 0 else "FAIL"
    print(f"Command {record['disposition']}: {record['elapsed_seconds']} seconds", flush=True)
    print(record["stdout"][-2500:], flush=True)
    return record


def structural(fixture, source_records, evidence):
    import xml.etree.ElementTree as ET

    python = str(ROOT / ".venv/Scripts/python.exe")
    validator = run_command([python, "-B", "scripts/check_repository_integrity.py"])
    inventory = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "tests/unit").glob("test_*.py"))
    if any("q10" in p.lower() for p in inventory):
        raise RuntimeError("A Q10 test is present: cannot run the suite without violating the blind boundary")
    # One complete, explicit partition. Temporary pytest/JUnit files are deleted
    # by their owning TemporaryDirectory, only inside this newly created path.
    temp_parent = ROOT / ".tmp"
    temp_parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="q10-final-unit-", dir=temp_parent) as directory:
        temp = Path(directory).resolve()
        if not temp.is_relative_to(temp_parent.resolve()):
            raise RuntimeError("Unit temporary directory escaped the workspace")
        junit = temp / "unit.xml"
        command = [python, "-B", "-m", "pytest", *inventory, "-q", "-p", "no:cacheprovider",
                   "--basetemp", str(temp / "pytest"), "--junitxml", str(junit)]
        unit = run_command(command)
        unit.update(partition_id="UNIT_COMPLETE", files=inventory)
        if junit.exists():
            xml_bytes = junit.read_bytes()
            xml = ET.fromstring(xml_bytes)
            cases = list(xml.iter("testcase"))
            unit["junit_sha256"] = sha(xml_bytes)
            unit["test_cases"] = [{"class": c.get("classname"), "name": c.get("name"),
                                   "outcome": "FAIL" if c.find("failure") is not None or c.find("error") is not None else "SKIP" if c.find("skipped") is not None else "PASS"} for c in cases]
            unit["counts"] = dict(collections.Counter(c["outcome"] for c in unit["test_cases"]))
            if not cases or unit["counts"].get("SKIP", 0):
                unit["disposition"] = "FAIL"
                unit["incomplete_suite_reason"] = "Missing executed cases or skipped tests leave full-suite evidence incomplete."
        else:
            unit["disposition"] = "FAIL"
            unit["incomplete_suite_reason"] = "JUnit execution record was not produced."
    after_inventory = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "tests/unit").glob("test_*.py"))
    counts = collections.Counter(unit["files"])
    coverage = {"complete_current_file_set": inventory, "partitions": [unit["partition_id"]],
                "union": sorted(counts), "duplicates": [p for p, n in counts.items() if n != 1],
                "missing": sorted(set(inventory) - counts.keys()), "extra": sorted(counts.keys() - set(inventory)),
                "inventory_unchanged": inventory == after_inventory,
                "exactly_once": bool(inventory) and all(counts[p] == 1 for p in inventory) and inventory == after_inventory}
    real_ids = sorted(item for item, refs in evidence.items() if item not in Q10_IDS and refs)
    checks = {
        "frozen_source_integrity": bool(source_records) and all(r["verified"] for r in source_records),
        "public_repository_integrity": validator["disposition"] == "PASS" and "PUBLIC_REPOSITORY_INTEGRITY=PASS" in validator["stdout"],
        "non_q10_real_evidence": len(real_ids) == fixture["structural_gate"]["qualification_matrix_non_q10_real_items_required"]
                                    and set(real_ids) == set(ITEM_IDS) - Q10_IDS,
        "full_unit_suite": unit["disposition"] == "PASS" and coverage["exactly_once"],
    }
    return {"disposition": "PASS" if all(checks.values()) else "FAIL", "checks": checks,
            "evidence_source_keys": ["matrix"], "real_item_ids": real_ids, "real_item_count": len(real_ids),
            "real_item_required_count": fixture["structural_gate"]["qualification_matrix_non_q10_real_items_required"],
            "validator": validator, "unit_partitions": [unit], "unit_partition_coverage": coverage,
            "temporary_artifacts": "Pytest basetemp and JUnit XML created inside an owned .tmp/q10-final-unit-* directory and removed after their results were captured."}


def main():
    if OUTPUT.exists():
        raise FileExistsError(f"Refusing to read or overwrite existing result: {OUTPUT}")
    raw_fixture = FIXTURE.read_bytes()
    fixture_sha = sha(raw_fixture)
    if fixture_sha != OBSERVED_FIXTURE_SHA256:
        raise RuntimeError("Frozen fixture changed since pre-execution observation")
    fixture = json.loads(raw_fixture)
    head = git("rev-parse", "HEAD").decode().strip()
    branch = git("branch", "--show-current").decode().strip()
    if head != OBSERVED_HEAD or branch != "v1-source-vault-bootstrap-resume":
        raise RuntimeError("Execution boundary differs from the observed Checkpoint 519 branch/HEAD")
    initial_status = status()
    started = datetime.now(timezone.utc).isoformat()
    source_records, data = verify_sources(fixture)
    budget_results = budgets(fixture, data)
    rules = scenario_rules(data, budget_results)
    limit_records = limitations(data)
    scenarios = []
    for number, frozen in enumerate(fixture["dimension_contract"]["scenarios"], 1):
        dispositions = []
        for dimension in frozen["relevant_dimensions"]:
            row = rules.get((number, dimension))
            if row is None:
                row = {"dimension": dimension, "disposition": "FAIL", "evidence_source_keys": [],
                       "facts": [], "affected_item_ids": [], "reason": "No implemented evidence predicate for this frozen dimension."}
            row = dict(row, reference=f"{frozen['scenario_id']}/{dimension}")
            applicable = [l for l in limit_records if set(l["affected_item_ids"]) & set(row["affected_item_ids"])]
            row["preserved_limitation_ids"] = [l["limitation_id"] for l in applicable]
            row["blocking_limitation_ids"] = [l["limitation_id"] for l in applicable if l["blocks_final_disposition"]]
            if row["blocking_limitation_ids"]:
                row["disposition"] = "FAIL"
            dispositions.append(row)
        scenarios.append({"scenario_id": frozen["scenario_id"], "frozen_evidence_keys": frozen["evidence_keys"],
                          "dimensions": dispositions, "disposition": "FAIL" if any(d["disposition"] == "FAIL" for d in dispositions) else "PASS"})
    all_dimensions = [d for s in scenarios for d in s["dimensions"]]
    required_refs = {f"{s['scenario_id']}/{d}" for s in fixture["dimension_contract"]["scenarios"] for d in s["relevant_dimensions"]}
    actual_refs = [d["reference"] for d in all_dimensions]
    coverage = {"required": len(required_refs), "evaluated": len(actual_refs),
                "counts": dict(collections.Counter(d["disposition"] for d in all_dimensions)),
                "missing": sorted(required_refs - set(actual_refs)), "extra": sorted(set(actual_refs) - required_refs),
                "duplicates": [r for r, n in collections.Counter(actual_refs).items() if n != 1],
                "distinct_dimensions": sorted({d["dimension"] for d in all_dimensions})}
    complete = set(actual_refs) == required_refs and len(actual_refs) == len(required_refs)
    evidence = real_item_evidence(data)
    structural_result = structural(fixture, source_records, evidence)
    final_status = status()
    authority_unchanged = final_status == initial_status and sha(FIXTURE.read_bytes()) == fixture_sha
    structural_result["checks"]["current_authority_unchanged"] = authority_unchanged
    structural_result["disposition"] = "PASS" if all(structural_result["checks"].values()) else "FAIL"
    blocking_limits = [l["limitation_id"] for l in limit_records if l["blocks_final_disposition"]]
    behavioral = {"scenario_count": len(scenarios), "dimension_coverage": coverage,
                  "blocking_limitations": blocking_limits, "failed_dimensions": [d["reference"] for d in all_dimensions if d["disposition"] == "FAIL"],
                  "aggregate_score_used": False}
    behavioral["disposition"] = "PASS" if (complete and len(scenarios) == fixture["behavioral_gate"]["scenario_count"]
                                              and not blocking_limits and not behavioral["failed_dimensions"]) else "FAIL"
    matrix_rows = {r["id"]: r for r in data.get("matrix", {}).get("requirements", []) + data.get("matrix", {}).get("invariants", [])}
    items = []
    for item in ITEM_IDS:
        relevant = [d for d in all_dimensions if item in d["affected_item_ids"]]
        limits = [l for l in limit_records if item in l["affected_item_ids"]]
        no_blocks = not any(l["blocks_final_disposition"] for l in limits)
        no_dimension_fail = not any(d["disposition"] == "FAIL" for d in relevant)
        if item == "KA-R30":
            passes = bool(budget_results) and all(b["disposition"] == "PASS" for b in budget_results)
            reason = "Every predeclared budget must pass at its exact frozen thresholds."
        elif item == "KA-R40":
            passes = structural_result["disposition"] == behavioral["disposition"] == "PASS"
            relevant = all_dimensions
            reason = "Both current structural qualification and the complete frozen behavioral gate must pass."
        elif item == "KA-R41":
            passes = complete and len(scenarios) == fixture["behavioral_gate"]["scenario_count"] and not behavioral["aggregate_score_used"]
            relevant = all_dimensions
            reason = "All frozen scenario/dimension pairs must have explicit dispositions, with no aggregate winner score."
        else:
            passes = bool(evidence[item]) and item in matrix_rows and no_blocks and no_dimension_fail and bool(relevant)
            mechanism = matrix_rows.get(item, {}).get("mechanism", "No frozen matrix mechanism")
            reason = mechanism + ". Final credit requires item-level real evidence, no blocking limitation and passing relevant Q10 dimensions."
        failures = []
        if item not in Q10_IDS and not evidence[item]:
            failures.append("Missing item-level real evidence")
        failures.extend(l["limitation_id"] for l in limits if l["blocks_final_disposition"])
        failures.extend(d["reference"] for d in relevant if d["disposition"] == "FAIL")
        items.append({"id": item, "title": matrix_rows.get(item, {}).get("title"),
                      "final_disposition": "PASS" if passes else "FAIL",
                      "evidence": evidence[item] if item not in Q10_IDS else [{"evidence_class": "Q10_FROZEN_CONTRACT_EXECUTION", "references": ["budgets" if item == "KA-R30" else "structural_gate and behavioral_gate" if item == "KA-R40" else "dimension_coverage"]}],
                      "requirement_source_key": "requirements", "matrix_source_key": "matrix",
                      "q10_scenario_dimension_references": [d["reference"] for d in relevant],
                      "preserved_limitation_ids": [l["limitation_id"] for l in limits],
                      "blocking_findings": failures, "reason": reason})
    h3_facts = [assertion(data, "q3", "h3_reopen_triggers/" + key, "eq", False) for key in [
        "general_authoritative_object_registry_required", "standalone_relation_or_transition_source_threshold_reached",
        "duplicate_authoritative_relation_required", "universal_objectization_required", "real_semantic_query_unresolvable"]]
    h3_triggered = any(f["measured"] is True for f in h3_facts)
    failures = [r["id"] for r in items if r["final_disposition"] == "FAIL"]
    result = {
        "schema_version": 1, "result_id": "PKA-C01-Q10-FINAL-RESULT-V01", "fixture_id": fixture["fixture_id"], "candidate_id": fixture["candidate_id"],
        "provenance": {"run_ordinal": 1, "started_at_utc": started, "finished_at_utc": datetime.now(timezone.utc).isoformat(),
            "branch": branch, "execution_head": head, "command": "python -B scripts/research/qualify_candidate_01_q10_final_v01.py",
            "argv": sys.argv, "python_executable": sys.executable, "python_version": sys.version,
            "implementation_path": Path(__file__).relative_to(ROOT).as_posix(), "implementation_sha256": sha(Path(__file__).read_bytes()),
            "fixture_path": FIXTURE.relative_to(ROOT).as_posix(), "fixture_sha256_observed_before_execution": OBSERVED_FIXTURE_SHA256,
            "fixture_sha256_at_execution": fixture_sha, "fixture_bytes": len(raw_fixture),
            "result_existed_at_start": False, "output_policy": "EXCLUSIVE_CREATE_FAIL_IF_EXISTING",
            "oracle_read": False, "q10_oracle_reads": 0, "post_checkpoint_519_qualification_evidence_reads": 0,
            "post_result_semantic_repair_occurred": False, "implementation_repairs_before_first_successful_result": 1,
            "pre_execution_repair": "An AST-only coverage check found KA-R23 missing from the item/dimension mapping. Before any qualification execution, it was bound to Q4 stale-revision visibility with explicit descriptor checks. No qualification run or result existed before this correction.",
            "qualification_evidence_policy": "Only fixture-listed sources at exact declared commits. No recursive following of embedded source paths. Earlier named evaluation receipts are allowed evidence; their underlying oracles are not consulted for decisions.",
            "structural_execution_exception": "Existing validators and complete unit suite executed only for structural measurements; older unit fixtures may be read by their unchanged tests. No Q10 tests exist in the recorded current unit inventory.",
            "current_project_authority_mutated": not authority_unchanged,
            "authority_preservation_evidence": {"method": "Before/after Git status inventories identical; no tracked mutation, fixture bytes unchanged; implementation writes only its exclusive result and owned temporary test files.", "before": initial_status, "after_before_result_create": final_status},
            "commit_or_push_performed": False},
        "source_verification": source_records,
        "budgets": budget_results, "structural_gate": structural_result,
        "scenarios": scenarios, "preserved_limitations": limit_records, "behavioral_gate": behavioral,
        "final_items": items,
        "h3_object_primary_assessment": {"evidence_source_keys": ["q3", "candidate"], "facts": h3_facts,
            "evidence_complete": all(not f["missing"] for f in h3_facts), "reopening_evidence_triggered": h3_triggered,
            "reason": "Evaluate the frozen real-case complexity triggers. Candidate section 33.11 requires convergence toward a general object substrate plus demonstrated H3 simplification; an unrelated qualification failure is not automatically H3 evidence."},
        "final_boundary": {
            "final_qualified_pass_count": len(items) - len(failures), "final_qualified_failure_count": len(failures), "failed_item_ids": failures,
            "budget_pass_count": sum(b["disposition"] == "PASS" for b in budget_results),
            "structural_gate_disposition": structural_result["disposition"], "behavioral_gate_disposition": behavioral["disposition"],
            "scenario_count": len(scenarios), "dimension_coverage": coverage, "aggregate_score_used": False,
            "h3_object_primary_reopening_evidence_triggered": h3_triggered,
            "target_selection_allowed": not failures and authority_unchanged and not h3_triggered,
            "target_selected": False, "authority_switch_allowed": False,
            "current_operational_authority": "CURRENT_CONTINUITY_ARCHITECTURE",
            "governance_reason": "Owner target selection/acceptance and the later explicit authority-switch decision remain separate governed stages."},
        "files_created_or_changed": [Path(__file__).relative_to(ROOT).as_posix(), OUTPUT.relative_to(ROOT).as_posix()],
    }
    # Local completeness invariants are checked before the only result write.
    assert len(items) == 67 and {r["id"] for r in items} == set(ITEM_IDS)
    assert all(d["disposition"] in fixture["dimension_contract"]["status_values"] for d in all_dimensions)
    assert all(d["facts"] and d["evidence_source_keys"] for d in all_dimensions)
    payload = (json.dumps(result, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    with OUTPUT.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    print(json.dumps(result["final_boundary"], indent=2), flush=True)
    print("RESULT_SHA256=" + sha(payload), flush=True)
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
