"""Source-free contract and actual OpenSSL interoperability tests.

Every source path/body, reviewer note, report and key in this suite is an
invented test fixture under ignored pytest scratch. No actual historical source
ZIP is sent, no owner private key is read, and no production recipient is made.
"""
from __future__ import annotations

from hashlib import sha1, sha256
from io import BytesIO
import json
from pathlib import Path
import subprocess
from zipfile import ZipFile

import pytest

from experiments.r0_p03_navigation_probe import s1_source_status_protected_route as route


def _test_batch(monkeypatch: pytest.MonkeyPatch) -> tuple[bytes, list[dict]]:
    rows = []
    entries = {}
    for i in range(10):
        body = (f"FAKE SOURCE {i}\nThis is not an ADS original source.\n").encode()
        path = f"fake-namespace/{i:02d}-fictional.md"
        oid = sha1(b"blob " + str(len(body)).encode() + b"\0" + body).hexdigest()
        rows.append({
            "path": path, "git_blob_oid": oid,
            "sha256": sha256(body).hexdigest(), "bytes": len(body),
            "role_hint_not_authority": "invented_test_role",
            "lexical_risk_flags_not_verdict": [],
            "admission": "REVIEW_ONLY_NOT_ADMITTED",
        })
        entries["sources/" + path] = body
    manifest = {
        "identifier": route.BATCH_ID,
        "source_ref": route.SOURCE_PIN,
        "selected_count": 10,
        "classification": "OWNER_LOCAL_FIRST_WAVE_REVIEW_INPUT_NOT_AUTHOR_PACKET",
        "source_manifest": rows,
    }
    manifest_bytes = (json.dumps(manifest, sort_keys=True) + "\n").encode()
    entries["SOURCE_MANIFEST.json"] = manifest_bytes
    buffer = BytesIO()
    with ZipFile(buffer, "w") as out:
        for filename, data in sorted(entries.items()):
            out.writestr(filename, data)
    raw = buffer.getvalue()
    monkeypatch.setattr(route, "BATCH_ZIP_SHA256", sha256(raw).hexdigest())
    monkeypatch.setattr(route, "BATCH_MANIFEST_SHA256",
                        sha256(manifest_bytes).hexdigest())
    return raw, rows


def _test_report(rows: list[dict]) -> dict:
    return {
        "format": route.FORMAT,
        "batch_identifier": route.BATCH_ID,
        "source_ref": route.SOURCE_PIN,
        "batch_zip_sha256": route.BATCH_ZIP_SHA256,
        "batch_manifest_sha256": route.BATCH_MANIFEST_SHA256,
        "reviewer_role": "NON_ARM_SOURCE_STATUS_REVIEWER",
        "independence_not_cryptographically_proven": True,
        "method_status": "V06_PROSPECTIVE_NOT_INDEPENDENTLY_ACCEPTED",
        "report_nonce": "d" * 32,
        "restricted_reviewer_exposure_notes": "Fictional test actor; role not admitted",
        "authorization": "REVIEW_ONLY_PROPOSED_NOT_AUTHOR_RELEASE",
        "author_world": "WORLD_UNFROZEN",
        "records": [
            {
                "path": r["path"],
                "git_blob_oid": r["git_blob_oid"],
                "sha256": r["sha256"],
                "received": True,
                "inspected": False,
                "scope": "COMPLETE_FILE",
                "proposed_disposition": "HOLD_FOR_SOURCE_REVIEW",
                "proposed_claims": [],
                "source_bound_private_reasoning": "TEST_ONLY_RESTRICTED_NOTE_" + str(i),
                "context_and_representation_gaps": ["Not inspected in fake test"],
                "contamination_and_author_exposure_risks": [],
                "challenge_state": "CHALLENGE_PENDING",
            }
            for i, r in enumerate(rows)
        ],
    }


def test_complete_ten_record_fake_roundtrip(monkeypatch: pytest.MonkeyPatch) -> None:
    blob, rows = _test_batch(monkeypatch)
    actual, recovered = route.load_batch(blob)
    assert actual["selected_count"] == 10
    assert [r["path"] for r in recovered] == [r["path"] for r in rows]
    obj = _test_report(rows)
    raw = route.report_bytes(obj, rows)
    assert route.canonical(obj) == raw
    assert route.validate_report(raw, rows) == obj


def test_missing_record_and_nonauthor_role_fail_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    _, rows = _test_batch(monkeypatch)
    obj = _test_report(rows)
    obj["records"].pop()
    with pytest.raises(route.RouteHold, match="REPORT_INCOMPLETE"):
        route.report_bytes(obj, rows)
    obj = _test_report(rows)
    obj["reviewer_role"] = "PRIMARY_AUTHOR"
    with pytest.raises(route.RouteHold, match="REPORT_IDENTITY_INVALID"):
        route.report_bytes(obj, rows)


def test_uninspected_cannot_become_candidate(monkeypatch: pytest.MonkeyPatch) -> None:
    _, rows = _test_batch(monkeypatch)
    obj = _test_report(rows)
    obj["records"][0]["proposed_disposition"] = "CANDIDATE_FULL"
    with pytest.raises(route.RouteHold, match="UNINSPECTED_SOURCE_NOT_HELD"):
        route.report_bytes(obj, rows)


def test_scope_or_identity_drift_and_missing_source_fail_closed(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    blob, rows = _test_batch(monkeypatch)
    obj = _test_report(rows)
    obj["records"][1]["sha256"] = "a" * 64
    with pytest.raises(route.RouteHold, match="RECORD_IDENTITY_OR_STATE_INVALID"):
        route.report_bytes(obj, rows)
    obj = _test_report(rows)
    obj["records"][0]["scope"] = "EXACT_SPAN"
    obj["records"][0]["proposed_disposition"] = "CANDIDATE_FULL"
    with pytest.raises(route.RouteHold, match="RECORD_IDENTITY_OR_STATE_INVALID"):
        route.report_bytes(obj, rows)
    with pytest.raises(route.RouteHold, match="BATCH_ZIP_IDENTITY_INVALID"):
        route.load_batch(blob + b"append")


def test_duplicates_and_noncanonical_are_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    _, rows = _test_batch(monkeypatch)
    obj = _test_report(rows)
    raw = route.report_bytes(obj, rows)
    with pytest.raises(route.RouteHold, match="REPORT_NOT_CANONICAL"):
        route.validate_report(raw + b"\n", rows)
    with pytest.raises(route.RouteHold, match="DUPLICATE_JSON_FIELD"):
        route.safe_json(b'{"format":"x","format":"y"}')


def test_authenticated_openssl_with_fake_only_recipient(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    blob, rows = _test_batch(monkeypatch)
    openssl = route.openssl_path()
    cert = tmp_path / "fake-recipient-cert.pem"
    key = tmp_path / "fake-recipient-private-key.pem"
    keygen = subprocess.run([
        openssl, "req", "-new", "-x509", "-newkey", "rsa:2048",
        "-keyout", str(key), "-out", str(cert),
        "-subj", "/CN=FICTIONAL-R0P03-S1-RECIPIENT",
        "-days", "1", "-passout", "pass:fake-only-key"
    ], capture_output=True, timeout=30, check=False)
    assert keygen.returncode == 0
    report = _test_report(rows)
    cipher = route.seal(report, blob, cert, openssl=openssl)
    assert b"TEST_ONLY_RESTRICTED_NOTE" not in cipher
    cipher_path = tmp_path / route.CIPHERTEXT_FILENAME
    cipher_path.write_bytes(cipher)
    observed = route.verify(
        cipher_path, blob, cert, key, b"fake-only-key", openssl=openssl
    )
    assert observed == {
        "source_ref_and_batch": "PASS",
        "authenticated_ciphertext": "PASS",
        "complete_reviewer_records": 10,
        "reviewer_dispositions": "RESTRICTED_NOT_PRINTED",
        "challenge_state": "PENDING",
        "author_world": "WORLD_UNFROZEN",
        "reviewer_private_report_printed": False,
    }
    with pytest.raises(route.RouteHold, match="CMS_AUTHENTICATION_FAILED"):
        route.verify(cipher_path, blob, cert, key, b"wrong", openssl=openssl)
    with pytest.raises(route.RouteHold, match="OWNER_PASSPHRASE_INPUT_INVALID"):
        route.verify(cipher_path, blob, cert, key, b"", openssl=openssl)
    tampered = tmp_path / "test-tampered.cms"
    tampered.write_bytes(cipher[:-1] + bytes([cipher[-1] ^ 1]))
    with pytest.raises(route.RouteHold, match="CMS_AUTHENTICATION_FAILED"):
        route.verify(tampered, blob, cert, key, b"fake-only-key", openssl=openssl)
