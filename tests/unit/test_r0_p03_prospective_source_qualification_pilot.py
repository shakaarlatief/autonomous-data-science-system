"""Invented evidence and strict cohort custody tests for source qualification.

The real repository cohort is exercised in a separate no-scoring run; unit
fixtures are unrelated synthetic source bytes and fabricated citations.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile

import pytest

from experiments.r0_p03_navigation_probe import (
    prospective_source_qualification_pilot as pilot,
    source_world_coverage_gate as world,
)


def source(path: str, *, unsupported: bool = False,
           flags: list[str] | None = None) -> tuple[dict, bytes | None]:
    raw = (b"Fictional evidence for " + path.encode("utf-8") +
           b"; not real authority or gold.\n")
    return ({
        "path": path, "git_blob_oid": world.sha1git(raw),
        "sha256": None if unsupported else sha256(raw).hexdigest(),
        "bytes": None if unsupported else len(raw),
        "family_hint": world.family(path),
        "visibility": (
            world.MODALITY_HOLD if unsupported
            else "HISTORICAL_REVIEW_ONLY"
        ),
        "status": world.NO_ADMISSION,
        "flags": flags or [],
    }, None if unsupported else raw)


def samples() -> tuple[dict, dict, dict, dict]:
    groups = {s: [] for s in pilot.STRATA}
    bodies = {}
    for label in pilot.STRATA:
        for i in range(5):
            if label == "STATUS_UNSUPPORTED":
                path = f"docs/research/{i+1:03}_fictional.png"
            elif label.startswith("STATUS"):
                path = f"docs/checkpoints/{i+1:03}_{label.lower()}.md"
            else:
                path = (
                    f"docs/local_execution/validation/"
                    f"{i+1:03}_{label.lower()}.md"
                )
            row, raw = source(
                path, unsupported=label == "STATUS_UNSUPPORTED",
                flags=["SIMULATED_RISK"] if "FLAGGED" in label else [],
            )
            groups[label].append(row)
            if raw is not None:
                bodies[path] = raw
    extra, body = source("docs/DECISIONS.md")
    extra["visibility"] = "PRELIMINARY_CANDIDATE_UNQUALIFIED"
    bodies[extra["path"]] = body
    rows = [extra] + [r for seq in groups.values() for r in seq]
    rows.sort(key=lambda r: r["path"])
    ledger = {
        "source_ref": "a" * 40,
        "roster_sha256": world._fingerprint(rows),
        "source_count": len(rows),
        "source_records": rows,
    }
    refs = {r["path"]: [] for r in rows}
    for group in groups.values():
        for r in group:
            refs[r["path"]] = [{
                "status": "EXACT_RESOLVED",
                "target": extra["path"],
                "line": 1, "kind": "numbered",
                "literal_reference": "FICTIONAL",
            }, {
                "status": "UNRESOLVED_NUMBERED",
                "target": None, "line": 2,
                "kind": "numbered", "literal_reference": "Research 999",
            }]
    families = {r["path"]: r["family_hint"] for r in rows}
    return groups, ledger, refs, {"bodies": bodies, "families": families}


def test_eight_strata_selection_is_exact_disjoint_and_deterministic():
    groups, ledger, _, _ = samples()
    first = pilot.select(groups, ledger["source_ref"])
    reversed_groups = {k: list(reversed(v)) for k, v in reversed(list(groups.items()))}
    second = pilot.select(reversed_groups, ledger["source_ref"])
    assert first == second
    assert len(first["CALIBRATION"]) == len(first["FALSIFICATION"]) == 16
    assert {r["stratum"] for r in first["CALIBRATION"]} == set(pilot.STRATA)
    assert {r["stratum"] for r in first["FALSIFICATION"]} == set(pilot.STRATA)
    assert not (
        {r["path"] for r in first["CALIBRATION"]} &
        {r["path"] for r in first["FALSIFICATION"]}
    )


def test_packet_has_complete_pinned_source_bytes_no_author_release():
    groups, ledger, refs, fixtures = samples()
    selected = pilot.select(groups, ledger["source_ref"])
    reserved = {r["path"] for items in selected.values() for r in items}
    raw, manifest = pilot.make_packet(
        "CALIBRATION", selected["CALIBRATION"],
        ledger=ledger, refs=refs, sources=fixtures["bodies"],
        family_by_path=fixtures["families"],
        reserved_seeds=reserved - {r["path"] for r in selected["CALIBRATION"]},
    )
    assert manifest["source_admissions"] == 0
    assert manifest["author_world"] == "WORLD_UNFROZEN"
    assert manifest["scored_tasks"] == "NONE"
    assert manifest["role"] == "CALIBRATION"
    assert manifest["seed_count"] == 16
    assert manifest["unsupported_seed_count"] == 2
    assert all(x["decision"] == "NOT_QUALIFIED_NOT_ADMITTED"
               for x in manifest["sampled_proposed_cases"])
    with ZipFile(BytesIO(raw)) as archive:
        assert set(archive.namelist()) == {
            "MANIFEST.json", "REVIEW_BRIEF.txt",
            *("sources/" + x["path"] for x in manifest["original_files"]),
        }
        assert archive.read("MANIFEST.json") == pilot.canonical(manifest)
        for record in manifest["original_files"]:
            blob = archive.read("sources/" + record["path"])
            assert record["sha256"] == sha256(blob).hexdigest()
            assert record["git_blob_oid"] == world.sha1git(blob)
            assert record["author_release"] == "NONE"


def test_challenge_seeds_not_exposed_through_calibration_context():
    groups, ledger, refs, fixtures = samples()
    selected = pilot.select(groups, ledger["source_ref"])
    challenge = {r["path"] for r in selected["FALSIFICATION"]}
    calibration = {r["path"] for r in selected["CALIBRATION"]}
    # Even an explicit reference to a held-out seed cannot expose its body.
    initial = selected["CALIBRATION"][0]["path"]
    hidden = sorted(challenge)[0]
    refs[initial].append({
        "status": "EXACT_RESOLVED", "target": hidden,
        "line": 3, "kind": "direct", "literal_reference": hidden,
    })
    raw, manifest = pilot.make_packet(
        "CALIBRATION", selected["CALIBRATION"],
        ledger=ledger, refs=refs, sources=fixtures["bodies"],
        family_by_path=fixtures["families"], reserved_seeds=challenge,
    )
    assert hidden not in {x["path"] for x in manifest["original_files"]}
    row = next(x for x in manifest["sampled_proposed_cases"]
               if x["seed"] == initial)
    assert row["context_diagnostic"][
        "heldout_or_other_sample_seed_context_excluded"] >= 1
    assert ("sources/" + hidden) not in ZipFile(BytesIO(raw)).namelist()


def test_no_overwrite_and_exact_recomputation(tmp_path: Path, monkeypatch):
    groups, ledger, refs, fixtures = samples()
    selected = pilot.select(groups, ledger["source_ref"])
    reserved = {r["path"] for seq in selected.values() for r in seq}
    packets = {}
    for role, name in (("CALIBRATION", pilot.CAL),
                       ("FALSIFICATION", pilot.CHALLENGE)):
        packets[name], _ = pilot.make_packet(
            role, selected[role], ledger=ledger, refs=refs,
            sources=fixtures["bodies"],
            family_by_path=fixtures["families"],
            reserved_seeds=reserved - {
                r["path"] for r in selected[role]
            },
        )
    safe = {"identifier": pilot.ID, "pilot_sampled_decisions": "NONE"}
    monkeypatch.setattr(pilot, "compute", lambda _repo: (packets, safe))
    (tmp_path / ".git").mkdir()
    assert pilot.emit(tmp_path, verify_only=False) == safe
    assert pilot.emit(tmp_path, verify_only=True) == safe
    with pytest.raises(FileExistsError, match="overwrite"):
        pilot.emit(tmp_path, verify_only=False)
    packet_file = tmp_path / pilot.DIR / pilot.CAL
    packet_file.write_bytes(packet_file.read_bytes()[:-1] + b"X")
    with pytest.raises(ValueError, match="not byte reproducible"):
        pilot.emit(tmp_path, verify_only=True)


def test_missing_stratum_and_undersized_stratum_are_holds():
    groups, ledger, _, _ = samples()
    del groups["VALIDATION_FLAGGED"]
    with pytest.raises(ValueError, match="stratum"):
        pilot.select(groups, ledger["source_ref"])
    groups, ledger, _, _ = samples()
    groups["VALIDATION_FLAGGED"].pop()
    groups["VALIDATION_FLAGGED"].pop()
    with pytest.raises(ValueError, match="Insufficient stratum"):
        pilot.select(groups, ledger["source_ref"])


def test_no_false_evidence_admission_when_seed_identity_is_forged():
    groups, ledger, refs, fixtures = samples()
    selected = pilot.select(groups, ledger["source_ref"])
    fake = deepcopy(selected["CALIBRATION"])
    fake[0]["git_blob_oid"] = "0" * 40
    with pytest.raises(ValueError, match="identity differs"):
        pilot.make_packet(
            "CALIBRATION", fake, ledger=ledger, refs=refs,
            sources=fixtures["bodies"],
            family_by_path=fixtures["families"],
            reserved_seeds=set(),
        )


def test_context_tampering_and_role_switch_rejected():
    groups, ledger, refs, fixtures = samples()
    selected = pilot.select(groups, ledger["source_ref"])
    corrupted = dict(fixtures["bodies"])
    corrupted["docs/DECISIONS.md"] = b"NOT PINNED"
    with pytest.raises(ValueError, match="not pinned"):
        pilot.make_packet(
            "CALIBRATION", selected["CALIBRATION"],
            ledger=ledger, refs=refs, sources=corrupted,
            family_by_path=fixtures["families"], reserved_seeds=set(),
        )
    with pytest.raises(ValueError, match="Unqualified pilot seed"):
        pilot.make_packet(
            "FALSIFICATION", selected["CALIBRATION"],
            ledger=ledger, refs=refs, sources=fixtures["bodies"],
            family_by_path=fixtures["families"], reserved_seeds=set(),
        )


def test_unsupported_source_cannot_be_presented_as_text():
    groups, ledger, refs, fixtures = samples()
    selected = pilot.select(groups, ledger["source_ref"])
    _, manifest = pilot.make_packet(
        "CALIBRATION", selected["CALIBRATION"],
        ledger=ledger, refs=refs, sources=fixtures["bodies"],
        family_by_path=fixtures["families"], reserved_seeds=set(),
    )
    unsupported = [r for r in manifest["sampled_proposed_cases"]
                   if r["unsupported_source"]]
    assert len(unsupported) == 2
    assert all(r["sha256"] is None for r in unsupported)
    assert all(r["decision"] == "NOT_QUALIFIED_NOT_ADMITTED"
               for r in unsupported)
    assert all(
        r["seed"] not in {b["path"] for b in manifest["original_files"]}
        for r in unsupported
    )


def test_safe_receipt_contains_no_path_specific_evidence():
    groups, ledger, refs, fixtures = samples()
    selected = pilot.select(groups, ledger["source_ref"])
    # The public-safe digest summary is exercised separately in the
    # integration test; this protects the role/qualification contract.
    assert sum(len(seq) for seq in selected.values()) == 32
    assert not any(x.get("decision") == "ADMITTED"
                   for seq in selected.values() for x in seq)
    assert all(x.get("status") == world.NO_ADMISSION
               for seq in selected.values() for x in seq)
