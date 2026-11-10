"""Deterministic, task-independent R0-P03 source-family rule-calibration pilot.

This creates TWO separate local-only non-arm review packets from the actual
2,539-source historical Git pin: one for independently proposing a
source-family eligibility rule, and one held aside for later falsification.
It never author-admits any source, freezes a scored world, generates questions
or gold, draws conclusions about source authority, or reads owner-private
Wave0 files. The samples cannot license population-wide admissions.

This pilot is not a random representativeness claim: it deliberately targets
eight prospective evidence/risk strata and marks unobserved context as HOLD.
The test role is policy calibration, not numerical task scoring.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path, PurePosixPath
from zipfile import ZipFile, ZipInfo, ZIP_STORED
import sys

from experiments.r0_p03_navigation_probe import (
    historical_evidence_dependency_frontier as graph,
    source_world_coverage_gate as world,
)

ID = "R0_P03_PROSPECTIVE_SOURCE_QUALIFICATION_PILOT_V1"
DIR = Path(".venv") / ".r0_p03_source_qualification_pilot_v01"
CAL = "R0_P03_SOURCE_QUALIFICATION_CALIBRATION_RESTRICTED.zip"
CHALLENGE = "R0_P03_SOURCE_QUALIFICATION_FALSIFICATION_RESTRICTED.zip"
RECEIPT = "R0_P03_SOURCE_QUALIFICATION_PILOT.safe-receipt.json"
STRATA = (
    "STATUS_CORE_CITED",
    "STATUS_CROSS_LINKED",
    "STATUS_FLAGGED",
    "STATUS_OTHER_UNREACHED",
    "STATUS_UNSUPPORTED",
    "VALIDATION_FLAGGED",
    "VALIDATION_LINKED",
    "VALIDATION_UNLINKED",
)
PER_STRATUM_PER_ROLE = 2
MAX_CONTEXT_PER_SEED = 4
MAX_BYTES_PER_PACKET = 18_000_000
SEED = "TASK_INDEPENDENT_BEFORE_PRIMARY_AUTHOR_R0_P03_V1"
FIXED_DATE = (2026, 1, 1, 0, 0, 0)

BRIEF = """RESTRICTED UNQUALIFIED R0-P03 HISTORICAL SOURCE CALIBRATION
These original pinned public Git files are a *non-scored* experiment
qualification pilot. Historical material may disclose old navigation answers,
the R0-P03 comparator design, and previous or proposed outcomes. Never hand
this packet to scored primary-task authors, gold annotators, arm engineers or
evaluators. No source here is already approved or admitted.

The first packet is CALIBRATION: assess actual source authority, temporal
claims, provenance, realization and validation support, prior-answer leakage,
and missing context. Draft a falsifiable, conservative FAMILY-LEVEL
qualification method and identify when per-source escalation is indispensable.
Do not claim a clean lexical flag proves safety.

The second packet is a separate FALSIFICATION holdout, NOT available during
calibration. After the family-level rule is frozen, independently test it on
the held-out original sources and any supplied context. Report wrongful
admissions, wrongful exclusions, unknowns, unsupported representations, and
where missing original dependencies prevent a responsible decision.

Only exact Git-pinned source blobs and bounded lexical citation context
are packaged. Omitted context is explicitly NOT VERIFIED. Citations are
mentions, not authority or proof that a validation ran/passed. This cannot
silently classify the other 1,971 critical historical records or the 406
candidate files. No scored tasks, reference answers or B0-B4 results exist.

No third-party disclosure or independent actor has been authorized by
creating these local packets. The owner must separately authorize a recipient
before any upload or external reviewer session.
"""

def canonical(obj: object) -> bytes:
    return (json.dumps(
        obj, sort_keys=True, ensure_ascii=True, separators=(",", ":"),
    ) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def classification(frontier: dict) -> tuple[dict[str, list[dict]], dict[str, str]]:
    """Prospective mutually exclusive partitions, all critical records counted."""
    records = frontier["review_candidate_records"]
    refs = frontier["references_by_source"]
    fam = {r["path"]: r["family_hint"] for r in records}
    if len(fam) != len(records):
        raise ValueError("Duplicated critical source identities")
    cross = set()
    for origin, matches in refs.items():
        for hit in matches:
            target = hit.get("target")
            if (
                hit["status"] == "EXACT_RESOLVED"
                and origin in fam and target in fam
                and fam[origin] != fam[target]
            ):
                cross.update((origin, target))
    groups: dict[str, list[dict]] = {name: [] for name in STRATA}
    for row in records:
        path = row["path"]
        family = row["family_hint"]
        signal = row["prospective_evidence_signals"]
        if family not in graph.CRITICAL or row["status"] != world.NO_ADMISSION:
            raise ValueError("Unexpected author admission or critical family")
        if signal["unsupported_representation"]:
            key = "STATUS_UNSUPPORTED"
        elif family == "historical_status":
            if signal["historical_lexical_or_path_flag"]:
                key = "STATUS_FLAGGED"
            elif signal["direct_core_mention"] or signal["two_hop_core_mention"]:
                key = "STATUS_CORE_CITED"
            elif path in cross:
                key = "STATUS_CROSS_LINKED"
            else:
                key = "STATUS_OTHER_UNREACHED"
        elif signal["historical_lexical_or_path_flag"]:
            key = "VALIDATION_FLAGGED"
        elif path in cross:
            key = "VALIDATION_LINKED"
        else:
            key = "VALIDATION_UNLINKED"
        groups[key].append(row)
    if sum(map(len, groups.values())) != len(records):
        raise ValueError("Coverage loss across critical evidence strata")
    return groups, fam


def stable_order(rows: list[dict], label: str, pin: str) -> list[dict]:
    """Freeze deterministic source identity selection before any semantic labels."""
    return sorted(rows, key=lambda r: (
        digest((SEED + "\0" + pin + "\0" + label + "\0"
                + r["path"] + "\0" + r["git_blob_oid"]).encode("utf-8")),
        r["path"],
    ))


def select(groups: dict[str, list[dict]], pin: str,
           *, per_role: int = PER_STRATUM_PER_ROLE) -> dict[str, list[dict]]:
    if type(per_role) is not int or not 1 <= per_role <= 5:
        raise ValueError("Invalid bounded pilot per-stratum size")
    if set(groups) != set(STRATA):
        raise ValueError("Missing or unexpected source stratum")
    selected = {"CALIBRATION": [], "FALSIFICATION": []}
    for label in STRATA:
        ordered = stable_order(groups[label], label, pin)
        if len(ordered) < 2 * per_role:
            raise ValueError("Insufficient stratum for prospective falsification")
        for role, begin in (("CALIBRATION", 0),
                            ("FALSIFICATION", per_role)):
            for row in ordered[begin:begin + per_role]:
                selected[role].append({"role": role, "stratum": label, **row})
    ids = {role: {r["path"] for r in rows} for role, rows in selected.items()}
    if ids["CALIBRATION"] & ids["FALSIFICATION"]:
        raise ValueError("Independent source holdout leakage")
    return selected


def neighbor_context(
    seed: str, family: str, refs: dict[str, list[dict]],
    families: dict[str, str], held_seeds: set[str],
) -> tuple[list[str], dict]:
    """Strict direct citation adjacency; not a semantic ownership graph."""
    connected = set()
    direct_out = 0
    direct_in = 0
    unresolved = Counter()
    for hit in refs.get(seed, []):
        if hit["status"] == "EXACT_RESOLVED" and hit["target"]:
            target = hit["target"]
            if target != seed:
                connected.add(target)
                direct_out += 1
        else:
            unresolved[hit["status"]] += 1
    for origin, matches in refs.items():
        if origin == seed:
            continue
        if any(x["status"] == "EXACT_RESOLVED"
               and x["target"] == seed for x in matches):
            connected.add(origin)
            direct_in += 1
    all_near = sorted(connected)
    reserved = connected & held_seeds
    allowed = connected - held_seeds
    def key(target: str) -> tuple[int, str]:
        group = families.get(target, "other")
        if family == "historical_status" and group == "execution_evidence":
            priority = 0
        elif family == "execution_evidence" and group == "historical_status":
            priority = 0
        elif group in {"governing", "orientation"}:
            priority = 1
        elif group in graph.CRITICAL:
            priority = 2
        else:
            priority = 3
        return priority, digest((SEED + "\0CTX\0" + seed + "\0" + target).encode())
    ranked = sorted(allowed, key=key)
    chosen = ranked[:MAX_CONTEXT_PER_SEED]
    return chosen, {
        "outgoing_exact_occurrence_count": direct_out,
        "incoming_document_count": direct_in,
        "distinct_adjacent_sources": len(all_near),
        "context_selected": len(chosen),
        "heldout_or_other_sample_seed_context_excluded": len(reserved),
        "additional_context_omitted": max(0, len(ranked) - len(chosen)),
        "unresolved_original_reference_occurrences": dict(sorted(unresolved.items())),
        "full_semantic_context_closure": "NOT_ESTABLISHED",
    }


def make_packet(
    role: str, samples: list[dict], *,
    ledger: dict, refs: dict[str, list[dict]],
    sources: dict[str, bytes], family_by_path: dict[str, str],
    reserved_seeds: set[str],
) -> tuple[bytes, dict]:
    if role not in {"CALIBRATION", "FALSIFICATION"}:
        raise ValueError("Unexpected review role")
    lookup = {r["path"]: r for r in ledger["source_records"]}
    manifest_rows = []
    packaged = set()
    records_by_name = {}
    for row in samples:
        path = row["path"]
        if row["role"] != role or path not in lookup:
            raise ValueError("Unqualified pilot seed")
        if any(
            row.get(key) != lookup[path].get(key)
            for key in (
                "git_blob_oid", "sha256", "family_hint",
                "visibility", "flags", "status",
            )
        ):
            raise ValueError("Pilot seed identity differs from pinned roster")
        context, coverage = neighbor_context(
            path, row["family_hint"], refs, family_by_path, reserved_seeds,
        )
        # An unsupported representation remains an original raw binary
        # and must never be claimed machine-read or source-qualified.
        included = [path] + context
        for name in included:
            origin = lookup[name]
            if (
                not world.safe_path(name) or
                name not in sources and origin["visibility"] != world.MODALITY_HOLD
            ):
                raise ValueError("Missing exact context source")
            if name in sources:
                raw = sources[name]
                if (
                    digest(raw) != origin["sha256"]
                    or len(raw) != origin["bytes"]
                    or world.sha1git(raw) != origin["git_blob_oid"]
                ):
                    raise ValueError("Context source not pinned")
                records_by_name[name] = raw
            else:
                # Historical nontext content is not present in the full-text
                # ledger and must not be fabricated. Include an explicit HOLD
                # with object ID, not a fake text representation.
                if origin["visibility"] != world.MODALITY_HOLD or name != path:
                    raise ValueError("Unsupported neighbor cannot be represented")
            packaged.add(name)
        manifest_rows.append({
            "role": role,
            "stratum": row["stratum"],
            "seed": path,
            "git_blob_oid": row["git_blob_oid"],
            "sha256": row["sha256"],
            "bytes": lookup[path]["bytes"],
            "unsupported_source": lookup[path]["visibility"] == world.MODALITY_HOLD,
            "risk_flags_are_nonauthoritative": lookup[path]["flags"],
            "context_paths": context,
            "context_diagnostic": coverage,
            "decision": "NOT_QUALIFIED_NOT_ADMITTED",
            "source_authority": "UNKNOWN",
            "author_exposure": "PROHIBITED_PENDING_INDEPENDENT_QUALIFICATION",
        })
    manifest = {
        "schema_version": 1,
        "identifier": ID,
        "role": role,
        "source_ref": ledger["source_ref"],
        "parent_roster_sha256": ledger["roster_sha256"],
        "sampling_method": "TWO_PER_EIGHT_FIXED_STRATA_PER_ROLE_SHA256_PIN_ID",
        "seed_count": len(samples),
        "readable_pinned_source_count": len(packaged & records_by_name.keys()),
        "original_files": sorted([
            {
                "path": path, "git_blob_oid": lookup[path]["git_blob_oid"],
                "sha256": digest(raw), "bytes": len(raw),
                "author_release": "NONE",
            } for path, raw in records_by_name.items()
        ], key=lambda x: x["path"]),
        "sampled_proposed_cases": manifest_rows,
        "unsupported_seed_count": sum(x["unsupported_source"]
                                      for x in manifest_rows),
        "scored_tasks": "NONE",
        "source_admissions": 0,
        "author_world": "WORLD_UNFROZEN",
        "missing_evidence_requires_hold": True,
    }
    content = BytesIO()
    with ZipFile(content, "w", allowZip64=False) as archive:
        for name, raw in [
            ("MANIFEST.json", canonical(manifest)),
            ("REVIEW_BRIEF.txt", BRIEF.encode("utf-8")),
        ] + [("sources/" + p, records_by_name[p])
             for p in sorted(records_by_name)]:
            info = ZipInfo(name, date_time=FIXED_DATE)
            info.compress_type = ZIP_STORED
            info.external_attr = 0o600 << 16
            info.create_system = 3
            archive.writestr(info, raw)
    result = content.getvalue()
    if len(result) > MAX_BYTES_PER_PACKET:
        raise ValueError("Qualification sample exceeds bounded packet size")
    if {x["role"] for x in manifest_rows} != {role}:
        raise ValueError("Leaked review role")
    return result, manifest


def compute(repo: Path) -> tuple[dict[str, bytes], dict]:
    ledger, _ = world.compute(repo)
    bodies = graph.exact_blobs(repo, ledger["source_records"])
    source_graph, _ = graph.frontier(ledger, bodies)
    groups, critical_families = classification(source_graph)
    sampled = select(groups, ledger["source_ref"])
    holdout_paths = {
        x["path"] for items in sampled.values() for x in items
    }
    all_families = {
        r["path"]: r["family_hint"] for r in ledger["source_records"]
    }
    zip_bytes = {}
    manifests = {}
    for role, name in (
        ("CALIBRATION", CAL), ("FALSIFICATION", CHALLENGE),
    ):
        raw, manifest = make_packet(
            role, sampled[role], ledger=ledger,
            refs=source_graph["references_by_source"],
            sources=bodies, family_by_path=all_families,
            reserved_seeds=holdout_paths - {
                x["path"] for x in sampled[role]
            },
        )
        zip_bytes[name] = raw
        manifests[role] = manifest
    if any(
        set(x["seed"] for x in manifests["FALSIFICATION"][
            "sampled_proposed_cases"]) &
        {r["path"] for r in manifests["CALIBRATION"]["original_files"]}
        for _ in range(1)
    ):
        raise ValueError("Falsification seed content exposed in calibration packet")
    receipt = {
        "schema_version": 1,
        "identifier": ID,
        "source_ref": ledger["source_ref"],
        "parent_roster_sha256": ledger["roster_sha256"],
        "critical_source_population": len(source_graph["review_candidate_records"]),
        "prospective_strata_population": {
            k: len(v) for k, v in sorted(groups.items())
        },
        "calibration_seed_count": len(sampled["CALIBRATION"]),
        "falsification_seed_count": len(sampled["FALSIFICATION"]),
        "per_stratum_per_role": PER_STRATUM_PER_ROLE,
        "calibration_source_file_count": len(
            manifests["CALIBRATION"]["original_files"]
        ),
        "falsification_source_file_count": len(
            manifests["FALSIFICATION"]["original_files"]
        ),
        "calibration_unsupported_seed_count": manifests["CALIBRATION"][
            "unsupported_seed_count"],
        "falsification_unsupported_seed_count": manifests["FALSIFICATION"][
            "unsupported_seed_count"],
        "packet_digests": {
            name: digest(raw) for name, raw in sorted(zip_bytes.items())
        },
        "packet_bytes": {
            name: len(raw) for name, raw in sorted(zip_bytes.items())
        },
        "calibration_exposes_falsification_seed_contents": False,
        "pilot_sampled_decisions": "NONE",
        "population_source_admissions": 0,
        "world": "WORLD_UNFROZEN",
        "scored_tasks": "NOT_STARTED",
        "interpretation": (
            "Stratified source-grounded rule calibration and separately "
            "withheld falsification only. Does not qualify sample, "
            "population or author access."
        ),
    }
    return zip_bytes, receipt


def emit(repo: Path, *, verify_only: bool) -> dict:
    repo = repo.resolve(strict=True)
    if not (repo / ".git").is_dir():
        raise ValueError("Not a Git repository")
    packets, receipt = compute(repo)
    blob = canonical(receipt)
    folder = repo / DIR
    if verify_only:
        for filename, raw in [*packets.items(), (RECEIPT, blob)]:
            path = folder / filename
            if not path.is_file() or path.read_bytes() != raw:
                raise ValueError("Qualification packet not byte reproducible")
        print("SOURCE_QUALIFICATION_PILOT_REPRODUCIBILITY=PASS")
    else:
        if any((folder / p).exists() for p in (*packets.keys(), RECEIPT)):
            raise FileExistsError("Refusing to overwrite qualification packets")
        folder.mkdir(parents=True, exist_ok=True)
        for filename, raw in [*packets.items(), (RECEIPT, blob)]:
            with (folder / filename).open("xb") as file:
                file.write(raw)
    print(json.dumps(receipt, sort_keys=True))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3) or (
        len(sys.argv) == 3 and sys.argv[2] != "--verify-only"
    ):
        raise SystemExit(
            "usage: python -m experiments.r0_p03_navigation_probe."
            "prospective_source_qualification_pilot REPO [--verify-only]"
        )
    emit(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
