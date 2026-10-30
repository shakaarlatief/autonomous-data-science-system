"""Fictional-only source and encrypted-challenger first-pass qualification."""
from __future__ import annotations

from hashlib import sha1, sha256
from io import BytesIO
import json
from pathlib import Path
import subprocess
from zipfile import ZipFile

import pytest

from experiments.r0_p03_navigation_probe import (
    s1_wave0_independent_challenger_first_pass as challenge,
    s1_source_status_protected_route as original,
)


def fake_batch(monkeypatch: pytest.MonkeyPatch) -> tuple[bytes, list[dict]]:
    rows = []
    files = {}
    for n in range(10):
        data = f"FICTIONAL FILE {n}\nNo real ADS original source.\n".encode()
        name = f"fake/{n:02d}.md"
        oid = sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        files[f"sources/{name}"] = data
        rows.append({
            "path": name, "git_blob_oid": oid,
            "sha256": sha256(data).hexdigest(), "bytes": len(data),
            "admission": "REVIEW_ONLY_NOT_ADMITTED",
        })
    manifest = {
        "identifier": original.BATCH_ID, "source_ref": original.SOURCE_PIN,
        "selected_count": 10,
        "classification": "OWNER_LOCAL_FIRST_WAVE_REVIEW_INPUT_NOT_AUTHOR_PACKET",
        "source_manifest": rows,
    }
    mb = (json.dumps(manifest, sort_keys=True) + "\n").encode()
    files["SOURCE_MANIFEST.json"] = mb
    buffer = BytesIO()
    with ZipFile(buffer, "w") as archive:
        for name, raw in sorted(files.items()):
            archive.writestr(name, raw)
    rawzip = buffer.getvalue()
    monkeypatch.setattr(original, "BATCH_ZIP_SHA256", sha256(rawzip).hexdigest())
    monkeypatch.setattr(original, "BATCH_MANIFEST_SHA256", sha256(mb).hexdigest())
    return rawzip, rows


def fake_report(rows: list[dict]) -> dict:
    return {
        "format": challenge.FORMAT,
        "batch_identifier": original.BATCH_ID,
        "source_ref": original.SOURCE_PIN,
        "batch_zip_sha256": original.BATCH_ZIP_SHA256,
        "batch_manifest_sha256": original.BATCH_MANIFEST_SHA256,
        "original_reviewer_ciphertext_sha256": challenge.ORIGINAL_CIPHERTEXT_SHA256,
        "candidate_role": challenge.ROLE,
        "initial_assessment_mode": challenge.MODE,
        "first_reviewer_report_seen": False,
        "first_reviewer_conclusions_seen": False,
        "prior_exposure_uncertainty": "No prior information in test fixture",
        "method_status": "V06_PROSPECTIVE_NOT_INDEPENDENTLY_ACCEPTED",
        "authorization": "REVIEW_ONLY_PROPOSED_NOT_AUTHOR_RELEASE",
        "author_world": "WORLD_UNFROZEN",
        "challenge_state": challenge.CHALLENGE,
        "report_nonce": "a" * 32,
        "restricted_independent_assessment_notes": "Fictional candidate actor only",
        "records": [
            {
                "path": entry["path"],
                "git_blob_oid": entry["git_blob_oid"],
                "sha256": entry["sha256"],
                "received": True, "inspected": False, "scope": "COMPLETE_FILE",
                "proposed_disposition": "HOLD_FOR_SOURCE_REVIEW",
                "proposed_claims": [],
                "source_bound_private_reasoning": "Fictional only, not inspected",
                "context_and_representation_gaps": ["Not inspected"],
                "contamination_and_author_exposure_risks": [],
                "challenge_state": "CHALLENGE_PENDING",
            }
            for entry in rows
        ],
    }


def test_new_role_and_schema_are_unambiguously_distinct(monkeypatch):
    z, rows = fake_batch(monkeypatch)
    report = fake_report(rows)
    assert challenge.validate_report(challenge.report_bytes(report, rows), rows) == report
    assert len(original.load_batch(z)[1]) == 10
    with pytest.raises(original.RouteHold, match="REPORT_SCHEMA_INVALID"):
        original.validate_report(challenge.report_bytes(report, rows), rows)
    report["first_reviewer_conclusions_seen"] = True
    with pytest.raises(original.RouteHold, match="INDEPENDENT_ROLE_OR_STATE_INVALID"):
        challenge.report_bytes(report, rows)


def test_duplicate_record_and_reviewer_content_prohibition(monkeypatch):
    _, rows = fake_batch(monkeypatch)
    report = fake_report(rows)
    report["records"][0] = report["records"][1]
    with pytest.raises(original.RouteHold, match="RECORD_IDENTITY_OR_STATE_INVALID"):
        challenge.report_bytes(report, rows)
    report = fake_report(rows)
    report["records"][0]["proposed_disposition"] = "CANDIDATE_EXCERPT"
    with pytest.raises(original.RouteHold, match="RECORD_SCOPE_INVALID"):
        challenge.report_bytes(report, rows)
    report = fake_report(rows)
    report["challenge_state"] = "CHALLENGED_ACCEPTED"
    with pytest.raises(original.RouteHold, match="INDEPENDENT_ROLE_OR_STATE_INVALID"):
        challenge.report_bytes(report, rows)


def test_original_report_hash_and_canonical_constraints(monkeypatch):
    _, rows = fake_batch(monkeypatch)
    report = fake_report(rows)
    report["original_reviewer_ciphertext_sha256"] = "b" * 64
    with pytest.raises(original.RouteHold, match="INDEPENDENT_ROLE_OR_STATE_INVALID"):
        challenge.report_bytes(report, rows)
    raw = challenge.report_bytes(fake_report(rows), rows)
    with pytest.raises(original.RouteHold, match="INDEPENDENT_REPORT_NONCANONICAL"):
        challenge.validate_report(raw + b"\n", rows)


def test_actual_openssl_fake_cms_roundtrip(monkeypatch, tmp_path: Path):
    z, rows = fake_batch(monkeypatch)
    openssl = original.openssl_path()
    key, cert = tmp_path / "fake-key.pem", tmp_path / "fake-cert.pem"
    p = subprocess.run([
        openssl, "req", "-new", "-x509", "-newkey", "rsa:2048",
        "-keyout", str(key), "-out", str(cert),
        "-subj", "/CN=FAKE-CHALLENGER-TEST", "-days", "1",
        "-passout", "pass:fake-test"
    ], capture_output=True, timeout=30, check=False)
    assert p.returncode == 0
    report = fake_report(rows)
    encrypted = challenge.seal(report, z, cert, openssl=openssl)
    assert b"Fictional candidate actor" not in encrypted
    path = tmp_path / challenge.OUTPUT_NAME
    path.write_bytes(encrypted)
    result = challenge.verify(path, z, cert, key, b"fake-test", openssl=openssl)
    assert result["complete_independent_source_records"] == 10
    assert result["owner_independent_challenger_cms_authenticated"] == "PASS"
    assert result["actual_adversarial_challenge"] == "PENDING"
    with pytest.raises(original.RouteHold, match="INDEPENDENT_CMS_AUTHENTICATION_FAILED"):
        challenge.verify(path, z, cert, key, b"wrong", openssl=openssl)
    altered = tmp_path / "tampered.cms"
    altered.write_bytes(encrypted[:-1] + bytes((encrypted[-1] ^ 1,)))
    with pytest.raises(original.RouteHold, match="INDEPENDENT_CMS_AUTHENTICATION_FAILED"):
        challenge.verify(altered, z, cert, key, b"fake-test", openssl=openssl)
