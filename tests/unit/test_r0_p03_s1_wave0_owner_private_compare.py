"""Fictional-only full authenticated Wave0 paired owner-private comparison tests.

All original sources, judgments, keys, ciphertexts and private reasoning
are invented synthetic fixtures in ignored pytest temporary directories.
Never reference or decrypt the actual owner-held Wave0 reports in these tests.
"""
from __future__ import annotations

from hashlib import sha1, sha256
from io import BytesIO
import json
from pathlib import Path
import subprocess
from zipfile import ZipFile

import pytest

from experiments.r0_p03_navigation_probe import (
    s1_source_status_protected_route as r,
    s1_wave0_independent_challenger_first_pass as c,
    s1_wave0_owner_private_compare as p,
)


def fake_zip(monkeypatch: pytest.MonkeyPatch) -> tuple[bytes, list[dict]]:
    contents: dict[str, bytes] = {}
    rows: list[dict] = []
    for index in range(10):
        source = f"FICTIONAL {index}\nOnly invented evidence.\n".encode()
        path = f"fictional/{index:02d}.md"
        oid = sha1(b"blob " + str(len(source)).encode() + b"\0" + source).hexdigest()
        rows.append({
            "path": path, "git_blob_oid": oid, "sha256": sha256(source).hexdigest(),
            "bytes": len(source), "admission": "REVIEW_ONLY_NOT_ADMITTED",
        })
        contents["sources/" + path] = source
    manifest = {
        "identifier": r.BATCH_ID, "source_ref": r.SOURCE_PIN,
        "selected_count": 10,
        "classification": "OWNER_LOCAL_FIRST_WAVE_REVIEW_INPUT_NOT_AUTHOR_PACKET",
        "source_manifest": rows,
    }
    m = (json.dumps(manifest, sort_keys=True) + "\n").encode()
    contents["SOURCE_MANIFEST.json"] = m
    buffer = BytesIO()
    with ZipFile(buffer, "w") as dest:
        for name, data in sorted(contents.items()):
            dest.writestr(name, data)
    blob = buffer.getvalue()
    monkeypatch.setattr(r, "BATCH_ZIP_SHA256", sha256(blob).hexdigest())
    monkeypatch.setattr(r, "BATCH_MANIFEST_SHA256", sha256(m).hexdigest())
    return blob, rows


def first_report(rows: list[dict]) -> dict:
    return {
        "format": r.FORMAT, "batch_identifier": r.BATCH_ID,
        "source_ref": r.SOURCE_PIN,
        "batch_zip_sha256": r.BATCH_ZIP_SHA256,
        "batch_manifest_sha256": r.BATCH_MANIFEST_SHA256,
        "reviewer_role": "NON_ARM_SOURCE_STATUS_REVIEWER",
        "independence_not_cryptographically_proven": True,
        "method_status": "V06_PROSPECTIVE_NOT_INDEPENDENTLY_ACCEPTED",
        "report_nonce": "a" * 32,
        "restricted_reviewer_exposure_notes": "FICTIONAL reviewer only",
        "authorization": "REVIEW_ONLY_PROPOSED_NOT_AUTHOR_RELEASE",
        "author_world": "WORLD_UNFROZEN",
        "records": [
            {
                "path": x["path"], "git_blob_oid": x["git_blob_oid"],
                "sha256": x["sha256"], "received": True, "inspected": True,
                "scope": "COMPLETE_FILE", "proposed_disposition": "HOLD_FOR_SOURCE_REVIEW",
                "proposed_claims": ["FICTIONAL_CLAIM"],
                "source_bound_private_reasoning": "REVIEWER_FICTIONAL_PRIVATE_REASON",
                "context_and_representation_gaps": ["Missing fictional context"],
                "contamination_and_author_exposure_risks": ["Invented risk"],
                "challenge_state": "CHALLENGE_PENDING",
            }
            for x in rows
        ],
    }


def challenger_report(rows: list[dict]) -> dict:
    a = first_report(rows)
    a["records"][0]["proposed_disposition"] = "PROHIBIT_DESIGN_OR_GOLD"
    a["records"][0]["source_bound_private_reasoning"] = "CHALLENGER_FICTIONAL_RESTRICTED_REASON"
    return {
        "format": c.FORMAT, "batch_identifier": r.BATCH_ID,
        "source_ref": r.SOURCE_PIN,
        "batch_zip_sha256": r.BATCH_ZIP_SHA256,
        "batch_manifest_sha256": r.BATCH_MANIFEST_SHA256,
        "original_reviewer_ciphertext_sha256": c.ORIGINAL_CIPHERTEXT_SHA256,
        "candidate_role": c.ROLE, "initial_assessment_mode": c.MODE,
        "first_reviewer_report_seen": False,
        "first_reviewer_conclusions_seen": False,
        "prior_exposure_uncertainty": "FICTIONAL independent session not certified",
        "method_status": "V06_PROSPECTIVE_NOT_INDEPENDENTLY_ACCEPTED",
        "authorization": "REVIEW_ONLY_PROPOSED_NOT_AUTHOR_RELEASE",
        "author_world": "WORLD_UNFROZEN", "challenge_state": c.CHALLENGE,
        "report_nonce": "b" * 32,
        "restricted_independent_assessment_notes": "FICTIONAL challenger only",
        "records": a["records"],
    }


def setup_fixture(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> dict:
    blob, rows = fake_zip(monkeypatch)
    public = tmp_path / "fictional-public.pem"
    secret = tmp_path / "fictional-encrypted-private.pem"
    openssl = r.openssl_path()
    result = subprocess.run([
        openssl, "req", "-new", "-x509", "-newkey", "rsa:2048",
        "-keyout", str(secret), "-out", str(public),
        "-subj", "/CN=FICTIONAL-OWNER-PRIVATE-COMPARISON",
        "-days", "1", "-passout", "pass:fictional-only",
    ], capture_output=True, timeout=30, check=False)
    assert result.returncode == 0
    source = tmp_path / "synthetic-only-review-batch.zip"
    source.write_bytes(blob)
    orig = tmp_path / r.CIPHERTEXT_FILENAME
    second = tmp_path / c.OUTPUT_NAME
    orig.write_bytes(r.seal(first_report(rows), blob, public, openssl=openssl))
    second.write_bytes(c.seal(challenger_report(rows), blob, public, openssl=openssl))
    monkeypatch.setattr(p, "REVIEWER_SHA", sha256(orig.read_bytes()).hexdigest())
    monkeypatch.setattr(p, "CHALLENGER_SHA", sha256(second.read_bytes()).hexdigest())
    return {
        "batch": source, "first": orig, "second": second,
        "key": secret, "cert": public,
        "out": tmp_path / p.OUTPUT_NAME, "openssl": openssl,
    }


def compare(case: dict, *, action: str, password: bytes = b"fictional-only") -> dict:
    return p.owner_operation(
        case["batch"], case["first"], case["second"],
        case["cert"], case["key"], case["out"],
        password, action=action, openssl=case["openssl"],
    )



def test_owner_wrapper_launches_repository_module_from_root() -> None:
    """Guard the real PowerShell invocation that failed before CMS decryption.

    The owner script must not use an absolute .py argument with imports of
    experiments.*, because Python otherwise starts with the nested script
    folder on sys.path instead of the repository root. This test executes the
    exact -m entry point harmlessly with --help using the repo root.
    """
    import sys

    root = Path(__file__).resolve().parents[2]
    wrapper = root / "scripts" / "r0_p03_s1_owner_wave0_private_compare.ps1"
    text = wrapper.read_text(encoding="utf-8")
    assert '$Module="experiments.r0_p03_navigation_probe.s1_wave0_owner_private_compare"' in text
    assert '$args=@("-B","-m",$Module,"--action",$Action' in text
    assert text.count("Push-Location -LiteralPath $Repo") >= 2
    assert 'OWNER_COMPARISON_MODULE_LAUNCH_FAILED' in text
    observed = subprocess.run(
        [sys.executable, "-B", "-m",
         "experiments.r0_p03_navigation_probe.s1_wave0_owner_private_compare",
         "--help"],
        cwd=root, capture_output=True, text=True, timeout=20, check=False,
    )
    assert observed.returncode == 0, observed.stderr
    assert "--action {Compare,Verify}" in observed.stdout
    assert "--reviewer-cms" in observed.stdout
    assert "--challenger-cms" in observed.stdout


def test_synthetic_full_seal_then_recompute_and_keep_inputs_unchanged(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    case = setup_fixture(monkeypatch, tmp_path)
    before = [sha256(case[name].read_bytes()).hexdigest() for name in ("first", "second")]
    sealed = compare(case, action="Compare")
    assert sealed["owner_private_comparison"] == "STORED_ENCRYPTED"
    assert sealed["paired_complete_record_count"] == 10
    assert sealed["source_specific_differences_printed"] is False
    assert case["out"].is_file()
    assert b"FICTIONAL_PRIVATE_REASON" not in case["out"].read_bytes()
    assert [sha256(case[name].read_bytes()).hexdigest() for name in ("first", "second")] == before
    check = compare(case, action="Verify")
    assert check["owner_private_comparison"] == "INDEPENDENT_RECOMPUTATION_PASS"
    assert check["private_encrypted_dossier_sha256"] == sealed["private_encrypted_dossier_sha256"]


def test_synthetic_private_dossier_contains_independent_diff_without_adjudication(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    case = setup_fixture(monkeypatch, tmp_path)
    compare(case, action="Compare")
    response = subprocess.run([
        case["openssl"], "cms", "-decrypt", "-binary", "-inform", "DER",
        "-in", str(case["out"]), "-recip", str(case["cert"]),
        "-inkey", str(case["key"]), "-passin", "stdin",
    ], input=b"fictional-only\n", capture_output=True, timeout=40, check=False)
    assert response.returncode == 0
    dossier = r.safe_json(response.stdout)
    assert dossier["format"] == p.FORMAT
    assert dossier["complete_record_count"] == 10
    assert dossier["actual_adversarial_challenge"] == "PENDING"
    first = dossier["private_paired_source_records"][0]
    assert "SOURCE_DISPOSITION_TOKEN_DIFF" in first["mechanical_exact_text_differences"]
    assert "REASONING_EXACT_TEXT_DIFF" in first["mechanical_exact_text_differences"]
    assert first["source_status_adjudication"] == "NOT_ADJUDICATED"
    assert dossier["private_paired_source_records"][1]["mechanical_exact_text_differences"] == []
    assert dossier["every_source_requires_substantive_adversarial_review"] is True


def test_wrong_password_preserves_absence_and_recovery_not_overwritten(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    case = setup_fixture(monkeypatch, tmp_path)
    with pytest.raises(r.RouteHold, match="PRIVATE_CMS_AUTHENTICATION_FAILED"):
        compare(case, action="Compare", password=b"incorrect")
    assert not case["out"].exists()
    compare(case, action="Compare")
    with pytest.raises(r.RouteHold, match="OWNER_COMPARISON_ALREADY_EXISTS"):
        compare(case, action="Compare")
    with pytest.raises(r.RouteHold, match="PRIVATE_CMS_AUTHENTICATION_FAILED"):
        compare(case, action="Verify", password=b"incorrect")


def test_tamper_or_missing_report_fails_before_private_output(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    case = setup_fixture(monkeypatch, tmp_path)
    damaged = case["second"].read_bytes()
    case["second"].write_bytes(damaged[:-1] + bytes([damaged[-1] ^ 1]))
    with pytest.raises(r.RouteHold, match="PRIVATE_CIPHERTEXT_IDENTITY_INVALID"):
        compare(case, action="Compare")
    assert not case["out"].exists()


def test_tampered_dossier_recheck_fails_and_does_not_overwrite(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    case = setup_fixture(monkeypatch, tmp_path)
    compare(case, action="Compare")
    before = case["out"].read_bytes()
    case["out"].write_bytes(before[:-1] + bytes([before[-1] ^ 1]))
    with pytest.raises(r.RouteHold, match="OWNER_COMPARISON_CMS_AUTHENTICATION_FAILED"):
        compare(case, action="Verify")
    assert case["out"].read_bytes() != before
