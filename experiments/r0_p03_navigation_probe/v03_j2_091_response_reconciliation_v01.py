"""Unscored reconciliation of the published Message 091 and J2 evidence classes.

The source owner cannot attest any retrospective COVERS relationship. Original
Git parent/path predicates remain OBSERVABLE; a connector transport assertion
in two same-event source records is not independent provider proof. Research
512 section 9 exempts exact OBSERVABLE facts from additional REALIZES manifests
but still requires natural-owner admission for genuine RELATIONAL coverage.

No governing J1 semantics, provider proof, J3 result or formal P03 scoring is
authored by this exposed experimental diagnostic.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

from experiments.r0_p03_navigation_probe import (
    v03_j2_natural_owner_evidence_contract_v01 as j2,
)

ROOT = Path(__file__).resolve().parents[2]
RESULT = Path(__file__).with_name("v03_j2_091_response_reconciliation_result_v01.json")
REPLY_COMMIT = "90dc870cd059fa555299505b7c7f8110dadb47f4"
REPLY_PARENT = "4284ce016dc69de82c5f724766112c3fd785fa39"
REPLY_PATH = "docs/model_collaboration/threads/MC-0030/messages/091_claude_r0_p03_d1_j2_natural_owner_declaration.md"
REPLY_GIT_BLOB = "20f7e89e567d66a1697acab79415448916e4c2ef"
REPLY_GIT_SHA256 = "c419e147ba2b1d69b89fa457b0a9483e90fcf035ffc1370d3d373204748a32de"
EXPECTED_SUMMARY = {
    "MESSAGE": "MC0030_091",
    "REPLY_TO": "MC0030_090",
    "DISPOSITION": "CANNOT_ATTEST",
    "TARGET_EFFECT": j2.E01,
    "ACCEPTED_PACKET_SHA256": j2.accepted.REVIEW_CANONICAL_SHA256,
    "COVERED_COMPONENTS": "NONE",
    "JSON_DECLARATION": "NOT_PROVIDED",
    "PROVIDER_TRANSPORT": "CANNOT_CONFIRM_TRANSPORT",
    "GIT_OBSERVABLE_REVERIFIED": "AUTHORIZED_PATH_ONLY,COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD",
    "CONTRADICTION_FOUND": "false",
    "AUTHORIAL_CONTINUITY": "NOT_ESTABLISHED_CONTEXT_COMPACTED_2026-10-13",
    "SECOND_CARRIER": "CD0CF087_COMMIT_MESSAGE_FLAGGED",
    "J2_QUALIFIED": "0",
    "J3_CERTIFIED": "false",
    "PRODUCTION_AUTHORITY": "false",
}
ORIGINAL_TRANSPORT_LINE = "Transport                       Claude-side GitHub connector (Research 485)"
ORIGINAL_TRANSPORT_COMMIT_TEXT = (
    "Interaction claude-04 via Claude-side GitHub connector (Research 485). "
    "Writes only Message 018."
)


def git(*args: str) -> bytes:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if result.returncode:
        raise ValueError("PINNED_GIT_EVIDENCE_UNAVAILABLE")
    return result.stdout


def published_reply() -> tuple[str, dict]:
    raw = git("show", f"{REPLY_COMMIT}:{REPLY_PATH}")
    if len(raw) != 11784 or sha256(raw).hexdigest() != REPLY_GIT_SHA256:
        raise ValueError("MESSAGE091_PUBLISHED_GIT_BYTES_CHANGED")
    blob = git("rev-parse", f"{REPLY_COMMIT}:{REPLY_PATH}").decode("ascii").strip()
    if blob != REPLY_GIT_BLOB:
        raise ValueError("MESSAGE091_PUBLISHED_GIT_BLOB_CHANGED")
    parent = git("show", "-s", "--format=%P", REPLY_COMMIT).decode("ascii").strip()
    paths = git("diff-tree", "--no-commit-id", "--name-status", "-r", REPLY_COMMIT).decode("utf8").splitlines()
    if parent != REPLY_PARENT or paths != ["A\t" + REPLY_PATH]:
        raise ValueError("MESSAGE091_PUBLICATION_PARENT_OR_PATH_CHANGED")
    message = git("show", "-s", "--format=%B", REPLY_COMMIT).decode("utf8")
    if not all(s in message for s in (
        "CANNOT_ATTEST", "Co-Authored-By: Claude", "Claude-Session:",
    )):
        raise ValueError("MESSAGE091_CLAUDE_COLLABORATION_TRAILER_MISSING")
    return raw.decode("utf8"), {
        "commit": REPLY_COMMIT,
        "parent": parent,
        "changed_paths": paths,
        "git_blob_oid": blob,
        "source_path": REPLY_PATH,
        "source_git_blob_sha256": sha256(raw).hexdigest(),
        "source_git_blob_bytes": len(raw),
        "provenance_class": "SHARED_GIT_CONTENT_WITH_CLAUDE_COLLABORATION_TRAILER",
        "original_action_first_hand_continuity": "NOT_ESTABLISHED",
    }


def parse_disposition(body: str) -> dict:
    """Parse a unique authored final-status block, not a fabricated claim."""
    fence = chr(96) * 3
    if body.count("MESSAGE=MC0030_091") != 1:
        raise ValueError("MESSAGE091_SUMMARY_NOT_UNIQUE")
    pattern = r"(?ms)^" + re.escape(fence + "text\n") + r"(MESSAGE=MC0030_091\n.*?)^" + re.escape(fence) + r"\s*$"
    blocks = re.findall(pattern, body)
    if len(blocks) != 1:
        raise ValueError("MESSAGE091_FINAL_DISPOSITION_MISSING")
    pairs = {}
    for line in blocks[0].strip().splitlines():
        if line.count("=") != 1:
            raise ValueError("MESSAGE091_STATUS_FIELD_NOT_SIMPLE")
        k, v = line.split("=", 1)
        if k in pairs:
            raise ValueError("MESSAGE091_DUPLICATE_STATUS_FIELD")
        pairs[k] = v
    if pairs != EXPECTED_SUMMARY:
        raise ValueError("MESSAGE091_DISPOSITION_OR_SCOPE_DRIFT")
    if re.search(r"(?m)^" + re.escape(fence) + r"json\s*$", body, re.IGNORECASE):
        raise ValueError("MESSAGE091_UNEXPECTED_COVERS_JSON")
    if "for all three E01 components" not in body or "no recollection" not in body.lower():
        raise ValueError("MESSAGE091_OWN_TESTIMONY_LIMIT_MISSING")
    return pairs


def check_repeated_transport_claim() -> dict:
    """Two original textual assertions are not two authoritative provider facts."""
    original_message = j2.git("show", f"{j2.ORIGINAL_PIN}:{j2.CLAUDE_MESSAGE}").decode("utf8")
    original_commit = git("show", "-s", "--format=%B", j2.ACTION).decode("utf8")
    if original_message.count(ORIGINAL_TRANSPORT_LINE) != 1:
        raise ValueError("ORIGINAL_MESSAGE_TRANSPORT_ATTESTATION_DRIFT")
    if original_commit.count(ORIGINAL_TRANSPORT_COMMIT_TEXT) != 1:
        raise ValueError("ORIGINAL_COMMIT_TRANSPORT_ATTESTATION_DRIFT")
    return {
        "claim_identity": "D1_EVENT_CONNECTOR_USE_SOURCE_ASSERTION",
        "original_message_text_verified": True,
        "original_commit_message_text_verified": True,
        "number_of_textual_attestation_carriers": 2,
        "number_of_independent_provider_records": 0,
        "number_of_independent_first_hand_owner_witnesses": 0,
        "underlying_transport": "UNKNOWN",
        "duplicated_admitted_natural_owner_j2_fact": False,
        "single_authoritative_provider_event_carrier_selected": False,
        "qualification_status": "TWO_SAME_EVENT_SOURCE_ASSERTIONS_NOT_PROVIDER_PROOF",
    }


def build() -> dict:
    text, publication = published_reply()
    disposition = parse_disposition(text)
    facts = j2.actual_component_evidence()
    old = j2.build()
    attestations = check_repeated_transport_claim()
    if old["accepted_j1_count"] != 4 or old["qualified_relational_components"]:
        raise ValueError("ORIGINAL_P03_J1_J2_STATE_CHANGED")
    if old["j3_completion_certified"]:
        raise ValueError("ORIGINAL_J3_HOLD_WAS_REMOVED")
    for c in ("AUTHORIZED_PATH_ONLY", "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD"):
        if facts["component_evidence"][c]["status"] != "VERIFIED_GIT":
            raise ValueError("GIT_OBSERVABLE_FACT_NO_LONGER_VERIFIED")
    if facts["component_evidence"]["TRANSPORT_ATTESTED_GITHUB_CONNECTOR"]["status"] != "ATTESTED_BY_SOURCE":
        raise ValueError("SOURCE_ATTESTATION_NO_LONGER_VERIFIED")
    return {
        "schema_version": 1,
        "status": "MESSAGE091_CANNOT_ATTEST_RECEIVED_HISTORICAL_J2_REQUEST_CLOSED",
        "publication": publication,
        "disposition": disposition,
        "accepted_experiment_only_j1": 4,
        "target_effect": j2.E01,
        "observable_git": {
            "natural_owner": "GIT_COMMIT_OBJECT",
            "verified_component_ids": ["AUTHORIZED_PATH_ONLY", "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD"],
            "additional_relational_covers_required_for_direct_observable_fact_itself": False,
            "accepted_e01_completion_predicate_mapping": "DIRECT_GIT_FACTS_ONLY",
            "j3_satisfied_from_git_alone": False,
        },
        "ephemeral_transport": {
            "component": "TRANSPORT_ATTESTED_GITHUB_CONNECTOR",
            "attestation_exists_as_original_source_text": True,
            "attestation_sources": attestations,
            "actual_connector_action_proven": False,
            "assurance_and_completion_rule_interpretation": "UNRESOLVED_DO_NOT_SILENTLY_AMEND_E01",
        },
        "natural_owner_relational": {
            "reply": "CANNOT_ATTEST",
            "new_covers_claim_present": False,
            "covered_components": [],
            "qualified_relational_facts": 0,
            "first_hand_context_retained": False,
            "reask_same_historical_action_from_other_claude_sessions": False,
        },
        "future_physical_design_trigger": {
            "status": "OPEN_J2_TYPED_FACT_AND_ASSURANCE_CONTRACT",
            "source_owned_ephemeral_event": "CONTEMPORANEOUS_DURABLE_RECEIPT_WITH_TRACEABLE_OWNER",
            "relational_coverage": "AT_ACTION_OR_TRANSACTIONALLY_LINKED_OWNER_DECLARATION_IF_REQUIRED",
            "independent_provider_evidence": "REQUIRED_ONLY_WHEN_GOVERNING_ASSURANCE_DEMANDS_IT",
            "one_natural_authoritative_carrier_class": "REQUIRED_PER_ACCEPTED_FACT_TUPLE",
            "existing_textual_attestations": "NOT_TWO_AUTHORITATIVE_FACTS",
        },
        "accepted_j1_original_statement_unchanged": True,
        "qualified_j2_relational_count": 0,
        "new_j3_satisfaction": "HOLD_J2_NATURAL_OWNER_QUALIFICATION_AND_ASSURANCE",
        "new_j3_completion_certified": False,
        "historical_d1_result": "D1_AMEND_UNCHANGED",
        "formal_p03_scores": None,
        "physical_architecture_selected": False,
        "next": "NON_RETROSPECTIVE_J2_SOURCE_EVENT_DESIGN_AND_SHARED_REAL_CONTENT_WORLD_QUALIFICATION",
    }


def main() -> None:
    value = build()
    raw = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if RESULT.exists():
        if RESULT.read_text("utf8") != raw:
            raise RuntimeError("MESSAGE091_RECONCILIATION_RECEIPT_DIFFERS")
    else:
        with RESULT.open("x", encoding="utf8", newline="\n") as fp:
            fp.write(raw)
    print(json.dumps({
        "status": value["status"],
        "git_observable_components": len(value["observable_git"]["verified_component_ids"]),
        "qualified_relational_j2": value["qualified_j2_relational_count"],
        "provider_transport_proven": value["ephemeral_transport"]["actual_connector_action_proven"],
        "j3_certified": value["new_j3_completion_certified"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
