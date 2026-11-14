"""An exact-source, fail-closed, non-scored documentary evidence-chain check.

The source-specific candidate specification and detailed witnesses are locally
ignored. The public implementation exposes only a fixed semantic *evidence
type system*, source and Git identity checks, negative controls, and safe
aggregates. It is deliberately not a V03 production ontology, an independently
authored authority oracle, a new J1 acceptance, a verified J2 REALIZES edge,
an owner's authenticated decision, or a scored Research 513 treatment.

Facts observable from document *text* are not silently promoted into verified
operative facts. Test source code is not test execution. A reported test suite
result is not an independently verified historical CI receipt. Presence of
source code beside a specification is not conformance proof.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path, PurePosixPath
import subprocess
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
ORIGINAL_PIN = "c57556a8bf993a1d327e9197acb7b7c745071cd8"
BASE = ROOT / "experiments/r0_p03_navigation_probe"
LOCAL = ROOT / ".venv/.r0_p03_historical_semantic_evidence_chain_v01"
PRIVATE_SPEC = LOCAL / "PRIVATE_EVIDENCE_CHAIN_SELECTION_V01.json"
PRIVATE_RESULT = LOCAL / "PRIVATE_VERIFIED_DOCUMENTARY_EVIDENCE_CHAIN_V01.json"
PUBLIC_RESULT = BASE / "historical_semantic_evidence_chain_aggregate_v01.json"
SELECTION_SHA256 = "0cb2495770e32d1f51cb4e3db7ad3fae5029820b7ac751af6de825fbb0cf186c"

EVIDENCE_KINDS = frozenset({
    "DECISION_RECORD_REPORT",
    "SPECIFICATION_TEXT",
    "IMPLEMENTATION_SOURCE",
    "TEST_SOURCE",
    "RESEARCH_RESULT_REPORT",
    "CHECKPOINT_REPORT",
    "UNACCEPTED_PROPOSAL",
    "DERIVED_SOURCE",
    "HISTORICAL_ROUTING",
})
# A relation below means exactly that source records contain the declared
# documentary connection. It is NOT a certified J1/J2/CI/owner fact.
RELATIONS = {
    "HISTORICAL_SELECTION_RETAINED_AS_REPORTED": {
        "DECISION_RECORD_REPORT": 4,
    },
    "CURRENT_CONTRACT_CONTEXT_AS_REPORTED": {
        "DECISION_RECORD_REPORT": 1,
        "SPECIFICATION_TEXT": 1,
    },
    "NORMATIVE_COMPONENT_AND_CODE_PRESENCE": {
        "SPECIFICATION_TEXT": 1,
        "IMPLEMENTATION_SOURCE": 1,
    },
    "TEST_SOURCE_IMPORTS_IMPLEMENTATION": {
        "TEST_SOURCE": 1,
        "IMPLEMENTATION_SOURCE": 1,
    },
    "RESEARCH_REPORT_NAMES_CODE_AND_TEST": {
        "RESEARCH_RESULT_REPORT": 1,
        "IMPLEMENTATION_SOURCE": 1,
        "TEST_SOURCE": 1,
    },
    "REPORTED_TEST_RESULTS_CONCORDANT": {
        "RESEARCH_RESULT_REPORT": 1,
        "CHECKPOINT_REPORT": 1,
    },
    "REPORTED_NO_OPERATIONAL_CUTOVER": {
        "DECISION_RECORD_REPORT": 1,
    },
    "TEST_SOURCE_HAS_NEGATIVE_AUTHORITY_CASE": {
        "TEST_SOURCE": 1,
    },
    "PROPOSAL_EXPLICITLY_REQUIRES_OWNER_DECISION": {
        "UNACCEPTED_PROPOSAL": 1,
    },
    "DERIVED_INDEX_NOT_GOVERNING_TRUTH": {
        "DERIVED_SOURCE": 1,
    },
    "HISTORICAL_GENERATED_STATE_OLDER_THAN_ROUTING": {
        "DERIVED_SOURCE": 1,
        "HISTORICAL_ROUTING": 1,
    },
}
REJECTED_AUTHORITY_KEYS = frozenset({
    "governing_effect", "accepted_effect_id", "j1_acceptance",
    "j2_realization_confirmed", "actual_historical_test_passed",
    "actual_ci_execution", "owner_act_independently_verified",
    "operative_authority", "semantic_owner_accepted",
    "source_admission", "verified_canonical_relation",
})
STATUS = "DOCUMENTARY_SOURCE_CLAIM_ONLY_UNQUALIFIED_FOR_GOVERNING_USE"
EXPECTED_WITNESSES = 19
EXPECTED_RELATIONS = 11
EXPECTED_CARRIERS = 10


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def exact_sha(path: Path, expected: str) -> bytes:
    data = path.read_bytes()
    if sha256(data).hexdigest() != expected:
        raise ValueError("Frozen private selection identity changed")
    return data


def safe_path(path: str) -> bool:
    p = PurePosixPath(path)
    return (
        isinstance(path, str) and bool(path) and path == p.as_posix()
        and not p.is_absolute() and "\\" not in path and "\x00" not in path
        and all(part not in ("", ".", "..") for part in path.split("/"))
    )


def blob_sha1(data: bytes) -> str:
    return sha1(b"blob " + str(len(data)).encode("ascii") + b"\x00" + data).hexdigest()


def current_original_tree(repo: Path) -> dict[str, str]:
    ret = subprocess.run(
        ["git", "ls-tree", "-r", "-z", ORIGINAL_PIN], cwd=repo,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=25,
    )
    tree = {}
    for part in ret.stdout.split(b"\0"):
        if not part:
            continue
        meta, path = part.split(b"\t", 1)
        _, kind, oid = meta.split(b" ", 2)
        if kind != b"blob":
            continue
        name = path.decode("utf8")
        if not safe_path(name) or name in tree:
            raise ValueError("Unsafe original source tree path")
        tree[name] = oid.decode("ascii")
    if len(tree) < 2500:
        raise ValueError("Unexpectedly small original source tree")
    return tree


def get_original_source(repo: Path, path: str, tree: dict[str, str]) -> tuple[bytes, str]:
    if not safe_path(path) or path not in tree:
        raise ValueError("Source not in fixed original Git tree")
    content = subprocess.check_output(
        ["git", "show", ORIGINAL_PIN + ":" + path],
        cwd=repo, timeout=15,
    )
    oid = blob_sha1(content)
    if tree[path] != oid:
        raise ValueError("Exact original Git blob mismatch")
    content.decode("utf8")  # Reject malformed text rather than silently replacing bytes.
    return content, oid


def source_reported_anchors(
    spec: dict, source_bodies: dict[str, tuple[bytes, str]],
) -> dict[str, dict]:
    """Every claimed line must equal the pinned Git bytes, with exact words."""
    result = {}
    for witness in spec["witnesses"]:
        if set(witness) != {
            "id", "path", "line_start", "line_end", "expected_excerpt",
            "kind", "explicit_markers",
        }:
            raise ValueError("Unexpected authority-bearing witness field")
        ident = witness["id"]
        path = witness["path"]
        kind = witness["kind"]
        a, b = witness["line_start"], witness["line_end"]
        if (
            not isinstance(ident, str) or not ident.isidentifier() or ident in result
            or kind not in EVIDENCE_KINDS or path not in source_bodies
            or not isinstance(a, int) or isinstance(a, bool)
            or not isinstance(b, int) or isinstance(b, bool)
            or a < 1 or b < a or b-a>12
        ):
            raise ValueError("Invalid documentary witness identity, location or kind")
        raw, oid = source_bodies[path]
        lines = raw.decode("utf8").splitlines()
        if b > len(lines):
            raise ValueError("Historical line span outside original source")
        exact_excerpt = "\n".join(lines[a-1:b])
        if exact_excerpt != witness["expected_excerpt"]:
            raise ValueError("Private source quote does not equal Git-pinned lines")
        markers = witness["explicit_markers"]
        if (
            not isinstance(markers, list) or not markers or len(markers)>5
            or any(not isinstance(m, str) or not m or m not in exact_excerpt for m in markers)
        ):
            raise ValueError("Documentary claim marker missing from original lines")
        result[ident] = {
            "id": ident, "kind": kind,
            "original_source_path": path, "original_git_blob_sha1": oid,
            "original_source_revision": ORIGINAL_PIN, "line_start": a,
            "line_end": b, "exact_original_excerpt": exact_excerpt,
            "evidence_interpretation": "SOURCE_DOCUMENT_TEXT_OBSERVED_NOT_INDEPENDENT_OPERATIVE_TRUTH",
        }
    if len(result) != EXPECTED_WITNESSES:
        raise ValueError("Expected exact limited original source witness count")
    return result


def validate_documentary_relations(spec: dict, anchors: dict[str, dict]) -> list[dict]:
    """Enforce explicit finite documentary relation categories, no promotions."""
    results = []
    seen = set()
    for row in spec["relations"]:
        if set(row) != {"id", "type", "witness_ids", "status"}:
            raise ValueError("Unknown extra relation field; possible authority promotion")
        ident, kind, ids = row["id"], row["type"], row["witness_ids"]
        if (
            not isinstance(ident, str) or not ident.isidentifier()
            or ident in seen or kind not in RELATIONS
            or row["status"] != STATUS
            or not isinstance(ids, list) or len(ids) != len(set(ids))
            or any(not isinstance(t, str) or t not in anchors for t in ids)
        ):
            raise ValueError("Invalid, unsupported or authority-promoted relation")
        needed = RELATIONS[kind]
        actual = Counter(anchors[t]["kind"] for t in ids)
        if actual != needed:
            raise ValueError("Source-kind requirements for documentary relation not met")
        seen.add(ident)
        results.append({
            "id": ident, "kind": kind, "evidence_class": STATUS,
            "supporting_source_witness_ids": list(ids),
            "accepted_governing_effect": False,
            "independent_owner_act_verified": False,
            "historical_ci_execution_independently_verified": False,
            "accepted_j2_realization": False,
        })
    if len(results) != EXPECTED_RELATIONS:
        raise ValueError("Incomplete fixed documentary relationship set")
    if set(RELATIONS) != {row["kind"] for row in results}:
        raise ValueError("Expected a single bounded relationship per source-reasoning category")
    return results


def inspect_negative_evidence(anchors: dict[str, dict]) -> dict:
    """Check one specific temporal discrepancy without inferring current truth."""
    old = [w for w in anchors.values() if w["kind"] == "DERIVED_SOURCE" and
           '"checkpoint":' in w["exact_original_excerpt"]]
    new = [w for w in anchors.values() if w["kind"] == "HISTORICAL_ROUTING" and
           '"current_checkpoint":' in w["exact_original_excerpt"]]
    if len(old) != 1 or len(new) != 1:
        raise ValueError("No uniquely grounded generated-versus-routing comparison")
    def number(record: dict, key: str) -> int:
        text = record["exact_original_excerpt"].strip()
        item = json.loads("{" + text.rstrip(",") + "}")
        val = item.get(key)
        if not isinstance(val, int) or isinstance(val, bool):
            raise ValueError("Invalid historical checkpoint number")
        return val
    a = number(old[0], "checkpoint")
    b = number(new[0], "current_checkpoint")
    if a >= b:
        raise ValueError("Original derived-view lag hypothesis falsified")
    return {
        "generated_checkpoint_at_original_pin": a,
        "routing_checkpoint_at_original_pin": b,
        "delta_checkpoints_not_time_or_semantic_staleness_proof": b-a,
        "interpretation": "OLDER_GENERATED_CHECKPOINT_VALUE_NOT_OPERATIVE_AUTHORITY_VERDICT",
    }


def parse_spec(spec: dict) -> dict:
    if set(spec) != {"id", "source_pin", "review_state", "witnesses", "relations"}:
        raise ValueError("Unexpected private fixture field")
    if (
        spec["id"] != "R0_P03_DOCUMENTARY_EVIDENCE_CHAIN_UNSCORED_V01"
        or spec["source_pin"] != ORIGINAL_PIN
        or spec["review_state"] != "EXPOSED_ENGINEERING_SOURCE_CANDIDATE_NOT_INDEPENDENT_GOLD"
        or not isinstance(spec["witnesses"], list)
        or not isinstance(spec["relations"], list)
        or len(spec["witnesses"]) != EXPECTED_WITNESSES
        or len(spec["relations"]) != EXPECTED_RELATIONS
    ):
        raise ValueError("Source-world scope or status changed")
    def forbidden(value: Any) -> None:
        if isinstance(value, dict):
            if REJECTED_AUTHORITY_KEYS.intersection(value):
                raise ValueError("Private fixture attempted unsupported authority admission")
            for item in value.values():
                forbidden(item)
        elif isinstance(value, list):
            for item in value:
                forbidden(item)
    forbidden(spec)
    return spec


def build(repo: Path, candidate: dict) -> tuple[dict, dict]:
    spec = parse_spec(candidate)
    tree = current_original_tree(repo)
    paths = sorted({w["path"] for w in spec["witnesses"]})
    if len(paths) != EXPECTED_CARRIERS:
        raise ValueError("Expected exact limited real-source set")
    raw = {p: get_original_source(repo,p,tree) for p in paths}
    anchors = source_reported_anchors(spec, raw)
    edges = validate_documentary_relations(spec, anchors)
    negative = inspect_negative_evidence(anchors)
    source_kinds = Counter(w["kind"] for w in anchors.values())
    relation_kinds = Counter(r["kind"] for r in edges)
    if len(relation_kinds) != EXPECTED_RELATIONS:
        raise ValueError("Missing relationship type")
    # This digest is of the local detailed report; it is not a semantic
    # canonical ID, accepted effect ID, or protected reference gold.
    detailed = {
        "id": spec["id"],
        "historical_git_pin": ORIGINAL_PIN,
        "witnesses": sorted(anchors.values(),key=lambda x:x["id"]),
        "documentary_relations": sorted(edges,key=lambda x:x["id"]),
        "negative_generated_checkpoint_comparison": negative,
        "warning": "EXPOSED_UNSCORED_DOCUMENTARY_CANDIDATE_NOT_ACCEPTED_AUTHORITY",
    }
    public = {
        "id": spec["id"],
        "historical_git_pin": ORIGINAL_PIN,
        "private_selection_sha256": SELECTION_SHA256,
        "source_carrier_count": len(paths),
        "source_witness_count": len(anchors),
        "documentary_relation_count": len(edges),
        "witness_kind_counts": dict(sorted(source_kinds.items())),
        "documentary_relation_type_counts": dict(sorted(relation_kinds.items())),
        "original_git_blob_and_source_line_exactness": "PASS",
        "negative_original_checkpoint_comparison": negative,
        "independently_attested_owner_decision": "NOT_ESTABLISHED_BY_THIS_SOURCE_SET",
        "historical_ci_execution_verified": "NOT_ESTABLISHED_BY_THIS_SOURCE_SET",
        "accepted_j1_effect_relations": 0,
        "accepted_j2_realization_relations": 0,
        "recorded_test_source_is_actual_test_pass": False,
        "reported_historical_test_result_is_independent_ci_receipt": False,
        "proposal_is_automatically_governing": False,
        "derived_index_is_automatically_governing": False,
        "source_role_semantics_independently_adjudicated": False,
        "actual_v03_common_substrate_complete": False,
        "formal_R0_P03_task_or_arm_scoring": False,
        "physical_architecture_selected": False,
        "candidate_owner_or_model_status": "EXPOSED_ENGINEERING_NOT_INDEPENDENT_REVIEW",
        "next_required_proof_classes": [
            "independently_qualified_owner_acceptance_and_currentness_scope",
            "natural_owner_realization_semantics_and_acceptance",
            "exact_historical_execution_or_receipt_bound_to_revision",
            "source_specific_lineage_and_completion_closure",
            "common_arm_substrate_semantic_parity_under_actual_release_controls",
        ],
        "architecture_reconsideration_triggers": [
            "documented_contradiction_or_insufficient_authority_for_target_assumptions",
            "needed_semantic_relation_not_representable_without_unjustified_promotion",
            "unbounded_source_closure_or_unresolvable_natural_owner",
            "implementation_or_receipt_cannot_be_proven_under_candidate_model",
            "source_format_or_privacy_boundaries_require_substrate_redesign",
            "real_common_arm_parity_fails_or_alternative_reduces_maintenance_complexity",
            "repository_workflow_or_ci_prevents_reproducible_qualification",
        ],
    }
    return public, detailed


def run() -> None:
    if PUBLIC_RESULT.exists() or PRIVATE_RESULT.exists():
        raise FileExistsError("Original frozen evidence chain already exists")
    source = exact_sha(PRIVATE_SPEC, SELECTION_SHA256)
    public, private = build(ROOT, json.loads(source))
    detail = canonical(private)
    public["private_result_bytes_receipt_only"] = len(detail)
    public["private_result_sha256_receipt_only"] = sha256(detail).hexdigest()
    safe = canonical(public)
    LOCAL.mkdir(parents=True, exist_ok=True)
    with PRIVATE_RESULT.open("xb") as out:
        out.write(detail)
    with PUBLIC_RESULT.open("xb") as out:
        out.write(safe)
    print(json.dumps({
        "public_bytes": len(safe), "public_sha256": sha256(safe).hexdigest(),
        "private_bytes": len(detail), "private_sha256": sha256(detail).hexdigest(),
        "original_source_carriers": public["source_carrier_count"],
        "original_line_witnesses": public["source_witness_count"],
        "documentary_relations": public["documentary_relation_count"],
        "historical_authority_and_ci_verified": False,
        "formal_R0_P03_scored": False,
    },sort_keys=True))


if __name__ == "__main__":
    run()
