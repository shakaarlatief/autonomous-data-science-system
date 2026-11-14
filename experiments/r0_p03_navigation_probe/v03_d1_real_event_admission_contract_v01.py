"""Original-source J1/J2/lineage admission preflight for a proposed P03-V2 world.

This module reopens the exact REAL D1 owner-reviewed development replay and its
Git event, rather than inventing a surrogate event. Its owner packet is a NEW
PROSPECTIVE P03 experiment-only reuse request, *not* a second acceptance of
the D1 effects. Original D1 acceptance applies only to the earlier replay.

The checker distinguishes:
  * verified Git parent/path/source bytes, and source-specific original claims;
  * owner-reported original D1 developer replay acceptance;
  * independently unqualified GitHub-connector transport attestation;
  * proposed P03 J1 governing effects and J2 RELATIONAL source-owner mappings;
  * a non-authoritative replay of D1's own J3 evaluator.

No payload here can admit experimental J1/J2, generate hidden gold or alter the
operational state. Accepting Research 672 M1-M6 authorized the method, not these
specific effects. The owner must review a separate, exact packet and acceptance
mechanism before the new world can become an admitted experiment.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

from experiments.ao10_hybrid_d1_replay_v01.evaluator_chatgpt_a import evaluate

ROOT = Path(__file__).resolve().parents[2]
PIN = "5463b2ad2e6799339746637f38340fa2a9dc00f6"
PACKAGE_PATH = Path(__file__).with_name("v03_d1_real_event_owner_proposal_v01.json")
RECEIPT_PATH = Path(__file__).with_name("v03_d1_real_event_admission_preflight_result_v01.json")
D1 = "experiments/ao10_hybrid_d1_replay_v01/"
MESSAGE_018 = "docs/model_collaboration/threads/MC-0029/messages/018_claude_d2_lineage_evaluator_b.md"
CORRECTION = "73f54c6a96b7a9172376b4c88deb9a5a400506d0"
ACTION = "cd0cf087a4d0ddb30920a8c753e478da8f92295c"
RECORDED_OWNER_PACKET_WORKTREE_SHA256 = (
    "2ac7ec839138189b5657da4c8f78f8c938ac3227da1c7af7f3c6f3fda7ae4fb4"
)
# Explicit allowlist prevents arbitrary files being imported as governing truth.
FILES = (
    D1 + "owner_review_packet.json",
    D1 + "accepted_j1.json",
    D1 + "source_facts.json",
    D1 + "definitions.json",
    D1 + "evaluator_chatgpt_a.py",
    "docs/research/484_d2_claude_evaluator_b_handoff_freeze.md",
    "docs/research/485_claude_collaboration_transport_correction.md",
    "docs/research/490_d1_integrated_real_event_microreplay_protocol.md",
    "docs/research/491_d1_owner_acceptance_and_j1_binding.md",
    "docs/research/495_d1_hash_basis_correction.md",
    "docs/research/499_d1_comparison_result_and_reconciliation.md",
    MESSAGE_018,
)


def canonical_bytes(value: Any) -> bytes:
    """Stable serialization for the proposed packet, not an owner signature."""
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf8")


def sha(data: bytes) -> str:
    return sha256(data).hexdigest()


def git(*argv: str, input_bytes: bytes | None = None) -> bytes:
    proc = subprocess.run(
        ["git", *argv], cwd=ROOT, input=input_bytes, capture_output=True, check=False,
    )
    if proc.returncode != 0:
        raise ValueError("ORIGINAL_GIT_EVIDENCE_UNAVAILABLE: " + " ".join(argv))
    return proc.stdout


def original_git_file(path: str) -> tuple[bytes, dict]:
    """Fetch exact PIN:file bytes. Do not read mutable worktree content."""
    if path not in FILES:
        raise ValueError("SOURCE_FILE_OUTSIDE_FROZEN_EVIDENCE_SET")
    data = git("show", f"{PIN}:{path}")
    oid = git("hash-object", "--stdin", input_bytes=data).decode("ascii").strip()
    return data, {
        "source_path": path,
        "commit": PIN,
        "git_blob_oid": oid,
        "sha256": sha(data),
        "byte_count": len(data),
    }


def source_manifest() -> list[dict]:
    return [original_git_file(path)[1] for path in FILES]


def json_from_source(path: str) -> dict:
    data, _ = original_git_file(path)
    obj = json.loads(data)
    if not isinstance(obj, dict):
        raise ValueError("EXPECTED_SOURCE_DOCUMENT_OBJECT")
    return obj


def assert_original_event_and_owner(
    accepted: dict, facts: dict, original_packet: dict, evidence: dict[str, bytes],
) -> dict:
    """Verify exact cross-source consistency; retain unresolved attestation.

    The original D1 replay's chat owner acceptance is recorded documentary
    evidence, NOT a new P03 owner act or independently authenticated identity.
    """
    record = evidence["docs/research/491_d1_owner_acceptance_and_j1_binding.md"].decode("utf8")
    if "**Owner decision:** ACCEPT" not in record:
        raise ValueError("ORIGINAL_D1_OWNER_DECISION_NOT_SOURCE_ATTESTED")
    if accepted["owner_decision"] != "ACCEPT":
        raise ValueError("ORIGINAL_D1_OWNER_DECISION_MISMATCH")
    if accepted["effects"] != original_packet["proposed_j1_effects"]:
        raise ValueError("D1_ACCEPTED_EFFECTS_DO_NOT_EQUAL_OWNER_PACKET")
    if len(accepted["effects"]) != 4 or len({row["accepted_effect_id"] for row in accepted["effects"]}) != 4:
        raise ValueError("D1_UNEXPECTED_EFFECT_SET")

    # D1 owner packet's recorded SHA was WORKTREE_CRLF, unlike the Git byte
    # basis subsequently fixed for accepted_j1/source_facts by Research 495.
    raw_packet = evidence[D1 + "owner_review_packet.json"]
    blob_sha256 = sha(raw_packet)
    reconstructed_crlf = raw_packet.replace(b"\n", b"\r\n")
    worktree_hash = sha(reconstructed_crlf)
    if (worktree_hash != RECORDED_OWNER_PACKET_WORKTREE_SHA256
            or accepted["owner_packet_sha256"] != worktree_hash
            or worktree_hash.encode("ascii") not in evidence[
                "docs/research/491_d1_owner_acceptance_and_j1_binding.md"
            ]):
        raise ValueError("ORIGINAL_OWNER_PACKET_RECORDED_HASH_BASIS_MISMATCH")
    if len(raw_packet) != 5107 or len(reconstructed_crlf) != 5193:
        raise ValueError("D1_OWNER_PACKET_ORIGINAL_BYTE_LENGTH_DRIFT")

    correction_source = evidence["docs/research/485_claude_collaboration_transport_correction.md"].decode("utf8")
    if "Claude uses the GitHub connector available in the Claude interaction" not in correction_source:
        raise ValueError("CORRECTION_SOURCE_NOT_PRESENT")
    if facts["correction"]["commit"] != CORRECTION or facts["action"]["commit"] != ACTION:
        raise ValueError("D1_ORIGINAL_EVENT_COMMIT_MISMATCH")
    action_parent = git("show", "-s", "--format=%P", ACTION).decode("ascii").strip()
    changed = git("diff-tree", "--no-commit-id", "--name-only", "-r", ACTION).decode("utf8").splitlines()
    if action_parent != CORRECTION or changed != [MESSAGE_018]:
        raise ValueError("GIT_RECEIPT_PARENT_OR_PATH_MISMATCH")
    if facts["action"]["parent"] != action_parent:
        raise ValueError("D1_FACT_PARENT_CONFLICTS_WITH_GIT")
    if facts["action"]["changed_paths"] != changed:
        raise ValueError("D1_FACT_CHANGED_PATHS_CONFLICT_WITH_GIT")
    if facts["correction"]["authorized_path"] != MESSAGE_018:
        raise ValueError("D1_FACT_AUTHORIZED_PATH_CONFLICT")
    if facts["action"]["message_transport_attestation"] != "CLAUDE_SIDE_GITHUB_CONNECTOR":
        raise ValueError("D1_FACT_TRANSPORT_ATTESTATION_CONFLICT")
    message = evidence[MESSAGE_018].decode("utf8")
    if "Transport                       Claude-side GitHub connector (Research 485)" not in message:
        raise ValueError("CLAUDE_MESSAGE_DOES_NOT_REPORT_CONNECTOR")
    lineage = next(e["lineage"] for e in accepted["effects"] if e["type"] == "LIFECYCLE")
    if lineage != {
        "relation": "REPLACE",
        "predecessor_id": facts["correction"]["predecessor_rule_id"],
        "successor_id": facts["correction"]["successor_rule_id"],
        "realization_succession": "OPEN_RESET",
    }:
        raise ValueError("D1_LINEAGE_NOT_SUPPORTED_BY_ACCEPTED_REPLAY")

    return {
        "original_d1_recorded_owner_packet_sha256": worktree_hash,
        "original_d1_recorded_sha256_basis": "WORKTREE_BYTES_CRLF",
        "same_content_git_blob_sha256": blob_sha256,
        "original_d1_packet_git_blob_length": len(raw_packet),
        "original_d1_packet_crlf_length": len(reconstructed_crlf),
        "original_owner_decision_class": "CONVERSATIONAL_OWNER_ACCEPTANCE_FOR_D1_REPLAY_ONLY",
        "original_git_action_commit": ACTION,
        "actual_git_action_parent": action_parent,
        "actual_git_changed_paths": changed,
        "source_reported_transport": "CLAUDE_SIDE_GITHUB_CONNECTOR",
        "transport_proof_class": "CLAUDE_SOURCE_ATTESTATION_NOT_INDEPENDENT_PROVIDER_PROOF",
        "original_d1_lifecycle": deepcopy(lineage),
    }


def replay_preview(accepted: dict, facts: dict) -> dict:
    """Run the original D1 evaluator; do not turn this into P03 accepted J3."""
    result = evaluate(accepted, facts)
    if (not result["acceptance_binding_valid"] or not result["lineage_relation_valid"]
            or not result["source_fact_contract_valid"]):
        raise ValueError("D1_REPLAY_ACCEPTANCE_OR_LINEAGE_CONTRADICTION")
    init = result["realization_initialization"]
    if not isinstance(init, dict) or set(init) != {"effect_id", "mode"}:
        raise ValueError("D1_V01_OUTPUT_CONTRACT_DRIFT")
    # Research 499 prospectively fixed singleton-vs-collection ambiguity.
    # This is a marked new presentation projection, not a silent historical
    # change to the original D1 raw scoring or evaluator implementations.
    output = deepcopy(result)
    output["realization_initialization"] = [init]
    return {
        "source": "D1_HISTORICAL_EVALUATOR_A_DEVELOPMENT_REPLAY",
        "d1_raw_v01_initialization_shape": "SINGLE_OBJECT",
        "research_499_reconciled_initialization_shape": "ORDERED_LIST_BY_EFFECT_ID",
        "historical_d1_disposition": "D1_AMEND_NOT_FORMAL_P03_PASS",
        "non_governing_d1_evaluator_projection": output,
    }


def build_owner_packet() -> dict:
    """Build exact new owner-review packet, with NO affirmative owner response."""
    original = {path: original_git_file(path)[0] for path in FILES}
    # The evaluator is imported from the current checkout for execution, so
    # explicitly prove its executable source matches the pinned Git bytes.
    # This rejects an accidental or malicious local evaluator edit rather than
    # silently attributing a mutated preview to the historical replay.
    local_evaluator = (ROOT / (D1 + "evaluator_chatgpt_a.py")).read_bytes()
    if local_evaluator.replace(b"\r\n", b"\n") != original[D1 + "evaluator_chatgpt_a.py"]:
        raise ValueError("EXECUTED_D1_EVALUATOR_DIFFERS_FROM_PINNED_SOURCE")
    if "D1=D1_AMEND" not in original[
        "docs/research/499_d1_comparison_result_and_reconciliation.md"
    ].decode("utf8"):
        raise ValueError("HISTORICAL_D1_AMEND_DISPOSITION_UNVERIFIED")
    j1 = json.loads(original[D1 + "accepted_j1.json"])
    facts = json.loads(original[D1 + "source_facts.json"])
    original_packet = json.loads(original[D1 + "owner_review_packet.json"])
    ver = assert_original_event_and_owner(j1, facts, original_packet, original)
    preview = replay_preview(j1, facts)
    return {
        "schema_version": 1,
        "proposal_id": "R0_P03_V2_D1_REAL_EVENT_REUSE_CANDIDATE_001",
        "proposed_world_id": "P03V2_DEVELOPMENT_WORLD_CLAUDE_COLLABORATION_V01",
        "proposal_status": "OWNER_EXPERIMENT_ONLY_ACCEPTANCE_NOT_OBSERVED",
        "source_commit": PIN,
        "source_manifest": source_manifest(),
        "original_d1_provenance": ver,
        "original_d1_historical_replay_evidence": {
            "original_event_source": "Research 485",
            "original_owner_acceptance_source": "Research 491",
            "original_output_shape_reconciliation": "Research 499",
            "original_d1_probe": j1["probe_id"],
            "original_d1_owner_review_packet_sha256_basis": "WORKTREE_BYTES_CRLF",
            "original_owner_acceptance_applies_to_new_p03_world": False,
        },
        "requested_experiment_only_j1_effects": deepcopy(j1["effects"]),
        "requested_effect_accounting": {
            "REALIZATION_TRACKED": sum(e["accounting_disposition"] == "REALIZATION_TRACKED" for e in j1["effects"]),
            "NO_REALIZATION_REQUIRED": sum(e["accounting_disposition"] == "NO_REALIZATION_REQUIRED" for e in j1["effects"]),
        },
        "proposed_lineage": deepcopy(ver["original_d1_lifecycle"]),
        "source_facts": {
            "original_d1_source_fact_fixture": facts["fixture_id"],
            "actual_git_commit_parent_and_path": "INDEPENDENTLY_VERIFIED_GIT",
            "claude_connector_transport": "SOURCE_ATTESTED_NOT_INDEPENDENTLY_PROVIDER_VERIFIED",
            "original_source_action_github_commit": ACTION,
        },
        "j2_evidence_ladder_candidate": [
            {
                "evidence_id": "J2OBS-D1-GIT-PATH",
                "class": "OBSERVABLE",
                "source": "git:" + ACTION,
                "claim": "The action commit has the exact correction parent and adds only Message 018",
                "verification": "GIT_OBJECT_VERIFIED",
                "governing_completion_consequence": False,
            },
            {
                "evidence_id": "J2ASSERT-D1-CLAUDE-TRANSPORT",
                "class": "SOURCE_REPORTED_ATTESTATION",
                "source": MESSAGE_018,
                "claim": "Claude reports its own GitHub connector transport",
                "verification": "MESSAGE_CONTENT_VERIFIED_PROVIDER_TRANSPORT_NOT_INDEPENDENTLY_OBSERVED",
                "governing_completion_consequence": False,
            },
            {
                "evidence_id": "J2REL-D1-E01-COVERAGE",
                "class": "RELATIONAL_PROPOSAL",
                "source": MESSAGE_018,
                "claim": "The actual Claude message and Git action realize E01's three required completion components",
                "verification": "NOT_ADMITTED_AS_P03_NATURAL_OWNER_RELATION",
                "target_effect_id": j1["effects"][0]["accepted_effect_id"],
                "covered_components": list(j1["effects"][0]["completion_contract"]["required_components"]),
                "governing_completion_consequence": False,
            },
        ],
        "original_d1_non_governing_j3_preview": preview,
        "request_for_new_owner_review": (
            "May these exact four previously reviewed D1 effect statements, as bound "
            "to the specified original Git source and original development acceptance, "
            "be reused as EXPERIMENT-ONLY J1 semantic inputs in the new P03-V2 "
            "development world? This does not alter D1, active project authority, "
            "J2 RELATIONAL provenance, real CI evidence or physical target selection."
        ),
        "owner_decision_options": ["ACCEPT", "AMEND", "REJECT"],
        "new_p03_owner_decision": None,
        "new_p03_accepted_j1_effect_ids": [],
        "new_p03_qualified_j2_relations": [],
        "new_p03_formal_tasks": [],
        "new_p03_formal_scores": None,
    }


def admission_check(
    packet: dict,
    *,
    owner_confirmation: dict | None = None,
    source_owner_claims: list[dict] | None = None,
) -> None:
    """Refuse both unverifiable promotion and pre-authorization to acceptance."""
    expected = build_owner_packet()
    if packet != expected:
        raise ValueError("OWNER_VISIBLE_EXPERIMENT_PACKET_CHANGED")
    if owner_confirmation is None:
        raise ValueError("P03_EXACT_OWNER_REUSE_APPROVAL_MISSING")
    # No generic agent-supplied acceptance object can create the project
    # owner's new experimental acceptance. A subsequent owner-approved route
    # must implement exact packet digest/decision/identity binding.
    raise ValueError("P03_EXPERIMENT_OWNER_ADMISSION_NOT_YET_QUALIFIED")


def build_receipt(packet: dict) -> dict:
    admission_blocked = False
    try:
        admission_check(packet)
    except ValueError as exc:
        admission_blocked = str(exc) == "P03_EXACT_OWNER_REUSE_APPROVAL_MISSING"
    if not admission_blocked:
        raise AssertionError("New P03 acceptance unexpectedly performed")
    return {
        "status": "REAL_D1_EVENT_VERIFIED_EXPERIMENT_REUSE_NOT_YET_ACCEPTED",
        "proposal_id": packet["proposal_id"],
        "owner_packet_canonical_sha256": sha(canonical_bytes(packet)),
        "owner_packet_git_source_pin": PIN,
        "original_d1_source_count": len(FILES),
        "historical_d1_effects_reviewed_in_original_context": len(packet["requested_experiment_only_j1_effects"]),
        "new_p03_accepted_effects": len(packet["new_p03_accepted_j1_effect_ids"]),
        "new_p03_qualified_j2_relations": len(packet["new_p03_qualified_j2_relations"]),
        "historical_action_parent_path_verified": True,
        "new_owner_confirmation": "NOT_OBSERVED",
        "original_d1_result_not_rescored": True,
        "formal_v03_experiment_world": "HOLD",
        "formal_r0_p03_scores": None,
        "physical_target_selected": False,
    }


def write_if_absent(path: Path, value: dict) -> None:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if path.exists():
        if path.read_text(encoding="utf8") != data:
            raise RuntimeError("IMMUTABLE_EXPERIMENT_RECORD_MISMATCH: " + str(path))
    else:
        with path.open("x", encoding="utf8", newline="\n") as output:
            output.write(data)


def main() -> None:
    packet = build_owner_packet()
    receipt = build_receipt(packet)
    write_if_absent(PACKAGE_PATH, packet)
    write_if_absent(RECEIPT_PATH, receipt)
    print(json.dumps({
        "status": receipt["status"],
        "owner_packet_canonical_sha256": receipt["owner_packet_canonical_sha256"],
        "original_d1_effects": receipt["historical_d1_effects_reviewed_in_original_context"],
        "git_source_count": receipt["original_d1_source_count"],
        "new_p03_accepted_effects": receipt["new_p03_accepted_effects"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
