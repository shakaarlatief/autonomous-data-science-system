"""Source/authority closure and common-projection parity engineering on 80 original files.

This is an unscored implementation diagnostic, not actual V03 J1/J2/J3
authoring and not a Research 513 B0-B4 execution. It is deliberately bounded
to the already-existing, owner-unreleased 80-original-source candidate. The
program does not change or distribute the candidate source corpus.

Critical distinctions:
- Git blob/path/line identities prove only exact archival bytes and location.
- Literal cited-file edges are DISCOVERY CANDIDATES, not semantic dependencies.
- Source-family labels are path-only review hints, not ownership or authority.
- No accepted governing effect, J2 realizes relation, executed test result,
  authoritative currentness or protected reference is inferred.
- B0..B4 "interfaces" below are synthetic *parity slots*, not implemented
  treatment arms, and their equality is not a formal treatment test.

All carrier-specific information is written only to a new Git-ignored local
artifact. Its public counterpart contains aggregate counts and file digests,
with no carrier names, quote strings, retrieved full text or question gold.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha1, sha256
from pathlib import Path, PurePosixPath
import json
import sqlite3
import subprocess
from typing import Any
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = ROOT / ".venv/.r0_p03_eighty_source_candidate_v01"
ARCHIVE = INPUT_DIR / "R0_P03_EIGHTY_SOURCE_RESTRICTED_RELEASE_CANDIDATE.zip"
RECEIPT = INPUT_DIR / "R0_P03_EIGHTY_SOURCE.safe-receipt.json"
ARCHIVE_SHA256 = "8d07e100dc9aef0934e49c089a9cbe20af3ef546eaa92f05c9e66a1ef3045e13"
RECEIPT_SHA256 = "e96fefa1eaae05fdba4e96550678eda6a83b9da9986c8567b3be5913c7113abe"
ORIGINAL_SOURCE_REF = "c57556a8bf993a1d327e9197acb7b7c745071cd8"
OUTDIR = ROOT / ".venv/.r0_p03_source_closure_common_projection_v01"
LOCAL_DETAIL = OUTDIR / "PRIVATE_SOURCE_CLOSURE_COMMON_PROJECTION_V01.json"
PUBLIC_OUTPUT = ROOT / "experiments/r0_p03_navigation_probe/source_closure_common_projection_aggregate_v01.json"
ARMS = ("B0", "B1", "B2", "B3", "B4")
FAMILY_NAMES = (
    "orientation", "governing", "historical_status", "execution_evidence",
    "product_source", "project_source", "verification", "tooling",
    "source_schema", "other",
)
LEXICAL_SMOKE_QUERIES = ("authority", "validation", "source")
SEMANTIC_UNPROVEN = {
    "natural_owner": "UNADJUDICATED",
    "governing_effect": "UNADJUDICATED",
    "authority_currentness": "UNKNOWN_NOT_PROVEN",
    "j2_realization_coverage": "UNPROVEN",
    "actual_test_execution": "UNPROVEN",
    "receipt_authenticity": "UNPROVEN",
}
OPTIONAL_ARM_FIELDS = {
    "B0": frozenset(),
    "B1": frozenset({"controlled_subject_memberships", "polyhierarchy", "preferred_navigation_route"}),
    "B2": frozenset({"editorial_about_links"}),
    "B3": frozenset({"cross_cutting_concern_assignments"}),
    "B4": frozenset({"semantic_candidate_rankings"}),
}
FORBIDDEN_AUTHORITY_PAYLOAD_KEYS = frozenset({
    "authority", "governing_status", "accepted_effect", "accepted_effect_id",
    "current_governing_summary", "natural_owner", "j1_acceptance",
    "j2_realization_coverage", "realizes", "verified_ci_execution",
    "operative_currentness", "source_authority", "source_provenance_override",
})


def forbid_authority_payload(value: Any) -> None:
    """Reject semantic/authority shadow fields inside optional navigation data."""
    if isinstance(value, dict):
        if FORBIDDEN_AUTHORITY_PAYLOAD_KEYS.intersection(value):
            raise ValueError("Optional navigation metadata cannot claim governing authority")
        for child in value.values():
            forbid_authority_payload(child)
    elif isinstance(value, list):
        for child in value:
            forbid_authority_payload(child)


def canonical(data: Any) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def original_bytes(path: Path, digest: str) -> bytes:
    data = path.read_bytes()
    if sha256(data).hexdigest() != digest:
        raise ValueError("Original input byte identity mismatch")
    return data


def safe_path(path: str) -> bool:
    p = PurePosixPath(path)
    return (
        path != "" and p.as_posix() == path and not p.is_absolute()
        and all(part not in (".", "..") for part in p.parts)
        and "\\" not in path and "\x00" not in path
    )


def git_tree(repo: Path, commit: str) -> dict[str, str]:
    """Verify original tree source OIDs without opening extra source bodies."""
    if commit != ORIGINAL_SOURCE_REF:
        raise ValueError("Unexpected original historical corpus pin")
    proc = subprocess.run(
        ["git", "ls-tree", "-r", "-z", commit],
        cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True, timeout=20,
    )
    tree = {}
    for row in proc.stdout.split(b"\x00"):
        if not row:
            continue
        meta, raw_path = row.split(b"\t", 1)
        mode, kind, oid = meta.split(b" ", 2)
        if kind != b"blob":
            continue
        name = raw_path.decode("utf8")
        if name in tree or not safe_path(name):
            raise ValueError("Invalid original Git source tree")
        tree[name] = oid.decode("ascii")
    if len(tree) < 2500:
        raise ValueError("Original Git source world unexpectedly small")
    return tree


def checked_corpus(repo: Path) -> tuple[list[dict], dict[str, bytes], dict[str, str], dict]:
    receipt = json.loads(original_bytes(RECEIPT, RECEIPT_SHA256))
    archive_bytes = original_bytes(ARCHIVE, ARCHIVE_SHA256)
    if receipt["historical_commit"] != ORIGINAL_SOURCE_REF:
        raise ValueError("Receipt source commit changed")
    if receipt["candidate_archive_sha256"] != ARCHIVE_SHA256:
        raise ValueError("Candidate archive receipt disagrees with frozen input")
    if receipt["candidate_archive_bytes"] != len(archive_bytes):
        raise ValueError("Candidate archive length mismatch")
    if receipt["candidate_original_source_count"] != 80:
        raise ValueError("Expected exact 80-source review corpus")
    if receipt["source_admissions"] != 0 or receipt["arm_scores"] != "NONE":
        raise ValueError("Candidate source release/scoring boundary unexpectedly changed")
    tree = git_tree(repo, ORIGINAL_SOURCE_REF)
    with ZipFile(ARCHIVE) as z:
        if z.testzip() is not None:
            raise ValueError("Invalid original ZIP CRC")
        names = z.namelist()
        if len(names) != len(set(names)) or any(not safe_path(n) for n in names):
            raise ValueError("Archive contains invalid, duplicate or escaping path")
        original_manifest = z.read("MANIFEST.json")
        if sha256(original_manifest).hexdigest() != receipt["candidate_manifest_sha256"]:
            raise ValueError("Original manifest hash changed")
        manifest = json.loads(original_manifest)
        if manifest["historical_commit"] != ORIGINAL_SOURCE_REF:
            raise ValueError("Original manifest revision mismatch")
        if (
            manifest["selected_source_count"] != 80
            or manifest["build_heldout_split"] != "NOT_DRAWN_BEFORE_SOURCE_ACCEPTANCE"
            or manifest["task_authorship"] != "NOT_STARTED"
            or manifest["comparative_arm_scoring"] != "NOT_STARTED"
            or manifest["author_world_release"] != "PROHIBITED_PENDING_INDEPENDENT_ORIGINAL_SOURCE_REVIEW"
        ):
            raise ValueError("Author admission or scored-stage state unexpectedly advanced")
        records = manifest["records"]
        if len(records) != 80 or len(names) != 82:
            raise ValueError("Original 80-file ZIP structure changed")
        by_path: dict[str, dict] = {}
        content: dict[str, bytes] = {}
        for row in records:
            p = row["path"]
            archive_name = row["exact_original_text"]
            if (
                not safe_path(p) or archive_name != "sources/" + p
                or archive_name not in names or p in by_path
                or row["source_family_path_hint_not_semantic_authority"] not in FAMILY_NAMES
                or row["current_authority"] != "UNKNOWN_NOT_PROVEN"
                or row["family_qualification"] != "NOT_INDEPENDENTLY_REVIEWED"
                or row["implementation_validation"] != "UNKNOWN_NOT_PROVEN"
                or row["combined_source_contamination"] != "UNKNOWN_NOT_PROVEN"
                or row["author_exposure_decision"] != "CANDIDATE_REQUIRES_INDEPENDENT_AUTHOR_WORLD_RELEASE"
            ):
                raise ValueError("Candidate role/authority field was promoted or changed")
            raw = z.read(archive_name)
            if (
                row["bytes"] != len(raw)
                or row["sha256"] != sha256(raw).hexdigest()
                or row["git_blob_oid"] != sha1(
                    b"blob " + str(len(raw)).encode("ascii") + b"\x00" + raw
                ).hexdigest()
                or tree.get(p) != row["git_blob_oid"]
            ):
                raise ValueError("Original selected Git content identity mismatch")
            content[p] = raw
            by_path[p] = row
        if set(names) != {"MANIFEST.json", "SOURCE_RELEASE_REVIEW_BRIEF.md"} | {
            "sources/" + p for p in by_path
        }:
            raise ValueError("Archive contains unapproved extra member")
    return records, content, tree, receipt


def source_reference_frontier(
    records: list[dict], tree: dict[str, str],
) -> tuple[dict, dict]:
    """Count original literal source references, not J1/J2 true relations."""
    selected = {row["path"] for row in records}
    counts = Counter()
    families = {f: Counter() for f in FAMILY_NAMES}
    local_rows = []
    outside_distinct = set()
    inside_distinct = set()
    for row in records:
        p = row["path"]
        family = row["source_family_path_hint_not_semantic_authority"]
        inside = row["literal_refs_in_selected_original"]
        outside = row["literal_refs_outside_selected_world"]
        if (
            len(inside) != len(set(inside)) or len(outside) != len(set(outside))
            or any(not safe_path(t) or t not in tree or t == p for t in inside+outside)
            or any(t not in selected for t in inside)
            or any(t in selected for t in outside)
        ):
            raise ValueError("Unqualified literal reference frontier corrupted")
        inside_distinct.update(inside)
        outside_distinct.update(outside)
        counts["inside_reference_occurrences"] += len(inside)
        counts["outside_reference_occurrences"] += len(outside)
        counts["sources_with_inside_reference"] += bool(inside)
        counts["sources_with_outside_reference"] += bool(outside)
        families[family]["carrier_count"] += 1
        families[family]["inside_reference_occurrences"] += len(inside)
        families[family]["outside_reference_occurrences"] += len(outside)
        local_rows.append({
            "original_source_path": p,
            "path_family_hypothesis": family,
            "exact_original_blob_sha1": row["git_blob_oid"],
            "literal_outgoing_refs_inside_80": sorted(inside),
            "literal_outgoing_refs_outside_80": sorted(outside),
            "natural_owner_semantics": "NOT_ESTABLISHED",
            "historical_authority_currentness": "NOT_ESTABLISHED",
            "j2_realization_or_executed_validation": "NOT_ESTABLISHED",
        })
    public = {
        "selected_carriers": len(selected),
        "git_tree_file_count": len(tree),
        "distinct_inside_reference_target_count": len(inside_distinct),
        "distinct_outside_reference_target_count": len(outside_distinct),
        "all_literal_external_targets_exist_at_exact_original_pin": True,
        "reference_totals": dict(counts),
        "family_path_hint_counts": {
            f: dict(families[f]) for f in sorted(FAMILY_NAMES)
        },
        "non_literal_dependency_closure": "NOT_ADJUDICATED",
        "task_answerability_closure": "NOT_ADJUDICATED",
        "actual_current_authority": "NOT_ADJUDICATED",
    }
    return local_rows, public


def shared_source_projection(
    records: list[dict], content: dict[str, bytes],
    *,
    original_ref: str = ORIGINAL_SOURCE_REF,
) -> dict:
    """Build only admissible *source provenance*, not accepted semantic truth."""
    carrier = []
    for row in sorted(records, key=lambda r: r["path"]):
        path = row["path"]
        original = content[path]
        carrier.append({
            "original_git_commit": original_ref,
            "original_git_blob_sha1": row["git_blob_oid"],
            "original_source_sha256": sha256(original).hexdigest(),
            "original_path_provenance_not_semantic_identity": path,
            "review_family_hint_not_accepted_role": row["source_family_path_hint_not_semantic_authority"],
            "source_byte_size": len(original),
            "source_authority": dict(SEMANTIC_UNPROVEN),
        })
    core = {
        "classification": "UNSCORED_REVIEW_CANDIDATE_NONAUTHORITATIVE",
        "historical_source_git_ref": original_ref,
        "carrier": carrier,
        "accepted_governing_effects": [],
        "accepted_lineage_currentness_relations": [],
        "accepted_j2_realization_edges": [],
        "accepted_receipt_verification_edges": [],
        "accepted_completion_relations": [],
        "literal_citation_candidates": [
            {
                "source_original_git_blob_sha1": row["git_blob_oid"],
                "literal_target_original_path": target,
                "relation_class": "LEXICAL_CITATION_ONLY_UNADJUDICATED",
            }
            for row in sorted(records, key=lambda r: r["path"])
            for target in sorted(
                row["literal_refs_in_selected_original"]
                + row["literal_refs_outside_selected_world"]
            )
        ],
        "source_role_assignment_status": "CANNOT_INFER_FROM_PATH",
        "current_governing_summary": "UNAVAILABLE_SOURCE_ADJUDICATION_REQUIRED",
        "derived_orientation": {
            "source_pin": original_ref,
            "derived": True,
            "authoritative": False,
            "freshness": "SOURCE_REVISION_BOUND_CURRENTNESS_NOT_ADJUDICATED",
            "current_governing_summary": "UNAVAILABLE_SOURCE_ADJUDICATION_REQUIRED",
            "navigation_entry_points": [],
        },
    }
    return core


def lexical_capability_check(content: dict[str, bytes]) -> dict[str, int]:
    """Actually construct a common lexical FTS5 over exactly the original bytes.

    No post-result query is picked. Only source-free per-query hit counts leave
    this process, and nothing in the indexed text is promoted to authority.
    """
    con = sqlite3.connect(":memory:")
    try:
        con.execute("CREATE VIRTUAL TABLE original_source USING fts5(path UNINDEXED, body)")
        for p, data in sorted(content.items()):
            con.execute("INSERT INTO original_source(path,body) VALUES (?,?)", (p, data.decode("utf8")))
        counts = {
            q: int(con.execute(
                "SELECT count(*) FROM original_source WHERE original_source MATCH ?",
                (q,),
            ).fetchone()[0])
            for q in LEXICAL_SMOKE_QUERIES
        }
        if any(not (0 < value <= len(content)) for value in counts.values()):
            raise ValueError("Full-text common input smoke check unexpectedly empty")
        return counts
    finally:
        con.close()


def arm_interface(
    common: dict, arm: str, augmentation: dict | None = None,
) -> dict:
    """Simulate strict non-authoritative augmentation namespace isolation.

    Does NOT implement B0/B1/B2/B3/B4 navigation algorithms. This is a
    fail-closed common-projection interface and parity smoke test.
    """
    if arm not in ARMS:
        raise ValueError("Unknown architectural interface")
    if not isinstance(augmentation, dict):
        if augmentation is not None:
            raise ValueError("Malformed extra navigation carrier")
        augmentation = {}
    allowed = OPTIONAL_ARM_FIELDS[arm]
    if any(k not in allowed for k in augmentation):
        raise ValueError("Additional metadata cannot override shared authority/carriers")
    if any(k in common for k in augmentation):
        raise ValueError("Augmentation attempted to override common source model")
    for value in augmentation.values():
        if not isinstance(value, list):
            raise ValueError("Augmentation must be bounded list of non-authoritative entries")
        forbid_authority_payload(value)
    shared_bytes = canonical(common)
    return {
        "interface": arm,
        "shared_original_source_sha256": sha256(shared_bytes).hexdigest(),
        "shared_common_projection": json.loads(shared_bytes),
        "extra_navigation": augmentation,
        "new_authority_from_extra_navigation": False,
        "implementation_status": "INTERFACE_SIMULATION_ONLY_NOT_AN_ACTUAL_ARM",
    }


def verify_common_interface_parity(common: dict) -> dict:
    """Prove strict byte parity and non-promotion across five interface slots."""
    snapshots = [arm_interface(common, arm) for arm in ARMS]
    raw = canonical(common)
    digest = sha256(raw).hexdigest()
    if any(canonical(s["shared_common_projection"]) != raw for s in snapshots):
        raise ValueError("Arm interface lost exact shared common projection")
    if {s["shared_original_source_sha256"] for s in snapshots} != {digest}:
        raise ValueError("Arm interface substrate parity failed")
    if any(s["extra_navigation"] or s["new_authority_from_extra_navigation"] for s in snapshots):
        raise ValueError("Unexpected hypothetical arm metadata accepted")
    return {
        "shared_projection_sha256": digest,
        "simulated_interface_slot_count": len(snapshots),
        "simulated_interface_slot_names": list(ARMS),
        "all_empty_augmentations_have_byte_identical_common_view": True,
        "arm_implementations_actually_tested": 0,
        "real_b0_b4_common_parity_qualification": "NOT_PERFORMED",
    }


def build(repo: Path) -> tuple[dict, dict]:
    records, raw_content, tree, receipt = checked_corpus(repo)
    local_refs, frontier = source_reference_frontier(records, tree)
    shared = shared_source_projection(records, raw_content)
    lexical = lexical_capability_check(raw_content)
    parity = verify_common_interface_parity(shared)
    aggregate = {
        "id": "R0_P03_SOURCE_CLOSURE_AND_NONAUTHORITATIVE_COMMON_PROJECTION_V01",
        "original_corpus_git_ref": ORIGINAL_SOURCE_REF,
        "candidate_archive_sha256": ARCHIVE_SHA256,
        "candidate_receipt_sha256": RECEIPT_SHA256,
        "selected_original_file_count": len(records),
        "original_bytes_verified_against_archive_and_git_tree": True,
        "candidate_archive_release_permitted": False,
        "source_admissions": 0,
        "original_source_census": frontier,
        "shared_non_authoritative_source_projection": {
            **parity,
            "source_metadata_schema_scope": "ORIGINAL_PROVENANCE_PLUS_UNADJUDICATED_LITERAL_CITATIONS_ONLY",
            "semantic_owner_authority_and_currentness_all_unproven": True,
            "accepted_governing_edges": 0,
            "accepted_realization_edges": 0,
            "accepted_receipt_edges": 0,
            "historical_source_semantic_j1_j2_j3_closure": "UNKNOWN_NOT_PROVEN",
            "source_role_family_status": "PATH_ONLY_HYPOTHESIS",
            "lexical_fts5_index_constructed_from_all_80_original_documents": True,
            "lexical_smoke_query_hit_counts": lexical,
        },
        "task_family_closure": {
            "cold_start_orientation": "UNPROVEN_NEEDS_TRUE_CURRENT_STATE_AND_DECISION_OWNER_AUTHORITY",
            "cross_plane_discovery": "UNPROVEN_NEEDS_SOURCE_OWNER_IMPLEMENTATION_AND_VALIDATION_JOIN",
            "impact_architecture_evolution": "UNPROVEN_NEEDS_VALID_EFFECT_AND_REALIZER_DEPENDENCIES",
            "exact_source_authority_recovery": "UNPROVEN_NEEDS_FORMAL_SUCCESSOR_DECISION_AND_ACTUAL_WITNESS_LINES",
        },
        "independently_authored_source_role_gold": "NONE",
        "formal_12_plus_9_tasks": "NONE",
        "real_arm_scoring": "NONE",
        "historical_owner_acts_confirmed": False,
        "physical_architecture_selected": False,
        "conclusion": (
            "80 exact original source carriers and FTS5 are mechanically usable; "
            "significant literal citation frontier is outside the candidate; "
            "none of the 80 carrier authority/realization statuses was independently "
            "admitted; five empty arm-interface slots preserve the same canonical "
            "non-authoritative source projection, but no real B0-B4 parity is proven."
        ),
    }
    local = {
        "id": aggregate["id"],
        "source_ref": ORIGINAL_SOURCE_REF,
        "candidate_original_manifest_sha256": receipt["candidate_manifest_sha256"],
        "source_only_reference_frontier": local_refs,
        "exact_common_source_projection": shared,
        "public_summary": aggregate,
        "not_scored": True,
    }
    return aggregate, local


def main() -> None:
    if PUBLIC_OUTPUT.exists() or LOCAL_DETAIL.exists():
        raise FileExistsError("Immutable first-run original and public outputs already exist")
    report, internal = build(ROOT)
    private_data = canonical(internal)
    report["private_report_sha256_receipt_only"] = sha256(private_data).hexdigest()
    report["private_report_bytes_receipt_only"] = len(private_data)
    public = canonical(report)
    OUTDIR.mkdir(parents=True, exist_ok=True)
    with LOCAL_DETAIL.open("xb") as f:
        f.write(private_data)
    with PUBLIC_OUTPUT.open("xb") as f:
        f.write(public)
    print(json.dumps({
        "public_output_bytes": len(public),
        "public_output_sha256": sha256(public).hexdigest(),
        "private_local_bytes": len(private_data),
        "private_local_sha256": sha256(private_data).hexdigest(),
        "selected_original_sources": report["selected_original_file_count"],
        "frontier": report["original_source_census"]["reference_totals"],
        "distinct_outside_sources": report["original_source_census"]["distinct_outside_reference_target_count"],
        "common_projection_sha256": report["shared_non_authoritative_source_projection"]["shared_projection_sha256"],
        "simulated_interfaces": len(ARMS),
        "actual_arm_implementations": 0,
        "source_admissions": 0,
        "scored": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
