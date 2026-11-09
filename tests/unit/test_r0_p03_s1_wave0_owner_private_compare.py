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
    s1_wave0_adversarial_packet as outbound,
    s1_wave0_adversarial_challenge_report as challenged,
    s1_wave0_semantic_adjudication_packet as semantic_packet,
    s1_wave0_semantic_decision_report as semantic_report,
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


def setup_adversarial_synthetic(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> dict:
    """Qualify the entire real-code path using invented-only source evidence."""
    fixture = setup_fixture(monkeypatch, tmp_path)
    compare(fixture, action="Compare")
    comparison_digest = sha256(fixture["out"].read_bytes()).hexdigest()
    monkeypatch.setattr(outbound, "COMPARISON_SHA256", comparison_digest)
    monkeypatch.setattr(challenged, "PAIRED_CIPHERTEXT_HASH", comparison_digest)
    monkeypatch.setattr(challenged, "SOURCE_HASH", r.BATCH_ZIP_SHA256)
    monkeypatch.setattr(challenged, "FIRST_HASH", p.REVIEWER_SHA)
    monkeypatch.setattr(challenged, "SECOND_HASH", p.CHALLENGER_SHA)
    fixture["sender"] = (
        Path(__file__).resolve().parents[2] / "experiments" /
        "r0_p03_navigation_probe" / "s1_wave0_adversarial_challenge_report.py"
    )
    fixture["packet"] = tmp_path / outbound.NAME
    return fixture


def export_synthetic(fixture: dict, action: str = "Export") -> dict:
    return outbound.run_owner(
        action=action, batch=fixture["batch"], reviewer=fixture["first"],
        independent=fixture["second"], comparison=fixture["out"],
        cert=fixture["cert"], key=fixture["key"],
        sender=fixture["sender"], output=fixture["packet"],
        password=b"fictional-only", openssl=fixture["openssl"],
    )


def invented_substantive_report(packet: bytes) -> dict:
    manifest, pair, rows, _ = challenged.packet_inputs(packet)
    records = []
    for index, row in enumerate(rows):
        records.append({
            "path": row["path"], "git_blob_oid": row["git_blob_oid"],
            "sha256": row["sha256"],
            "original_source_inspected": True,
            "first_reviewer_reasoning_examined": True,
            "independent_first_pass_reasoning_examined": True,
            "first_reviewer_assessment": "DISPUTED" if index == 0 else "SUPPORTED",
            "independent_first_pass_assessment": "DISPUTED" if index == 0 else "SUPPORTED",
            "material_disagreement": "YES" if index == 0 else "UNCERTAIN",
            "shared_blindspot": "YES" if index == 0 else "UNCERTAIN",
            "strongest_counterargument": (
                "FICTIONAL counterargument against both original source proposals."
            ),
            "source_grounded_evidence": (
                "FICTIONAL evidence from an invented ten-source test file."
            ),
            "missing_or_uninspectable_context": (
                "No missing context was demonstrated in this fabricated fixture."
            ),
            "claim_materiality": (
                "FICTIONAL claim materiality: a contrary interpretation changes scope."
            ),
            "disclosure_materiality": (
                "FICTIONAL disclosure materiality: possible historical answer exposure."
            ),
            "provisional_outcome": "HOLD_FOR_EVIDENCE" if index == 0
                else "SUPPORTED_PROVISIONALLY",
            "restricted_reasoning": (
                "FICTIONAL RESTRICTED challenge reason; no actual source evaluated."
            ),
        })
    return {
        "format": challenged.FORMAT, "source_ref": challenged.SOURCE_REF,
        "source_zip_sha256": challenged.SOURCE_HASH,
        "private_paired_evidence_sha256": manifest["private_paired_evidence_sha256"],
        "input_packet_sha256": challenged.sha(packet),
        "role": "NON_ARM_SOURCE_STATUS_ADVERSARIAL_CHALLENGER",
        "stage": "AFTER_TWO_PRESERVED_BLIND_FIRST_PASSES",
        "first_reviewer_reasoning_seen": True,
        "independent_first_pass_reasoning_seen": True,
        "independence_limitations": (
            "FICTIONAL session, not proof of isolated model/provider identity."
        ),
        "session_exposure_notes": (
            "FICTIONAL exposure audit, no connected apps in invented exercise."
        ),
        "report_nonce": "c" * 32,
        "records": records,
        "challenge_state": "SUBSTANTIVE_CHALLENGE_REPORTED_NOT_ADJUDICATED",
        "author_world": "WORLD_UNFROZEN",
        "source_admissions": 0,
    }


def test_synthetic_adversarial_owner_export_and_recomputation(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = setup_adversarial_synthetic(monkeypatch, tmp_path)
    prior_hashes = {
        k: sha256(fixture[k].read_bytes()).hexdigest()
        for k in ("first", "second", "out")
    }
    result = export_synthetic(fixture)
    assert result["owner_adversarial_input"] == "RESTRICTED_PLAINTEXT_PACKET_CREATED"
    assert result["pinned_original_sources"] == 10
    assert result["source_specific_content_printed"] is False
    assert result["packet_sha256"] == sha256(fixture["packet"].read_bytes()).hexdigest()
    with ZipFile(fixture["packet"]) as archive:
        assert len(archive.namelist()) == 6
        assert b"FICTIONAL_PRIVATE_REASON" in archive.read(
            outbound.PAIRED_MEMBER
        )
        assert archive.read(outbound.SOURCE_ZIP_MEMBER) == fixture["batch"].read_bytes()
    independently_recomputed = export_synthetic(fixture, action="VerifyExport")
    assert independently_recomputed["owner_adversarial_input"] == (
        "INDEPENDENT_PACKET_RECOMPUTATION_PASS"
    )
    assert independently_recomputed["packet_sha256"] == result["packet_sha256"]
    assert {
        k: sha256(fixture[k].read_bytes()).hexdigest()
        for k in ("first", "second", "out")
    } == prior_hashes
    with pytest.raises(r.RouteHold, match="CHALLENGE_PACKET_ALREADY_EXISTS"):
        export_synthetic(fixture)


def test_synthetic_challenger_seals_report_and_owner_authenticates(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = setup_adversarial_synthetic(monkeypatch, tmp_path)
    export_synthetic(fixture)
    pack = fixture["packet"].read_bytes()
    report = invented_substantive_report(pack)
    assert len(report["records"]) == 10
    plaintext = challenged.validate_report(report, pack)
    encrypted = challenged.seal(report, pack, openssl=fixture["openssl"])
    assert plaintext not in encrypted
    assert b"FICTIONAL RESTRICTED challenge reason" not in encrypted
    safe = challenged.owner_verify(
        encrypted, pack, fixture["cert"], fixture["key"],
        b"fictional-only", openssl=fixture["openssl"],
    )
    assert safe["owner_challenge_cms_authenticated"] == "PASS"
    assert safe["exact_challenge_packet_bound"] == "PASS"
    assert safe["complete_source_challenge_records"] == 10
    assert safe["semantic_acceptance"] == "NOT_YET_ADJUDICATED"
    assert safe["source_specific_findings_printed"] is False


def test_synthetic_challenge_is_rejected_if_prior_comparison_tampered(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = setup_adversarial_synthetic(monkeypatch, tmp_path)
    before = fixture["out"].read_bytes()
    fixture["out"].write_bytes(before[:-1] + bytes([before[-1] ^ 0x80]))
    with pytest.raises(r.RouteHold, match="PRIVATE_CIPHERTEXT_IDENTITY_INVALID"):
        export_synthetic(fixture)
    assert not fixture["packet"].exists()


def test_synthetic_challenge_requires_complete_and_real_inspection_claims(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = setup_adversarial_synthetic(monkeypatch, tmp_path)
    export_synthetic(fixture)
    pack = fixture["packet"].read_bytes()
    report = invented_substantive_report(pack)
    report["records"][0]["original_source_inspected"] = False
    with pytest.raises(challenged.Hold, match="CHALLENGE_SOURCE_RECORD_INVALID"):
        challenged.validate_report(report, pack)
    report["records"][0]["original_source_inspected"] = True
    report["records"].pop()
    with pytest.raises(challenged.Hold, match="CHALLENGE_RECORD_COUNT_INVALID"):
        challenged.validate_report(report, pack)
    report = invented_substantive_report(pack)
    report["records"][0]["restricted_reasoning"] = ""
    with pytest.raises(challenged.Hold, match="SUBSTANTIVE_REASONING_MISSING"):
        challenged.validate_report(report, pack)


def test_synthetic_challenge_wrong_key_and_ciphertext_tamper_rejected(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = setup_adversarial_synthetic(monkeypatch, tmp_path)
    export_synthetic(fixture)
    pack = fixture["packet"].read_bytes()
    encrypted = challenged.seal(
        invented_substantive_report(pack), pack, openssl=fixture["openssl"]
    )
    with pytest.raises(challenged.Hold, match="CHALLENGE_OWNER_CMS_AUTHENTICATION_FAILED"):
        challenged.owner_verify(
            encrypted, pack, fixture["cert"], fixture["key"],
            b"not-the-passphrase", openssl=fixture["openssl"],
        )
    tampered = encrypted[:-1] + bytes([encrypted[-1] ^ 0x01])
    with pytest.raises(challenged.Hold, match="CHALLENGE_OWNER_CMS_AUTHENTICATION_FAILED"):
        challenged.owner_verify(
            tampered, pack, fixture["cert"], fixture["key"],
            b"fictional-only", openssl=fixture["openssl"],
        )


def test_synthetic_challenge_owner_launcher_uses_module_and_no_public_export() -> None:
    """Control plane and Python module-import regression, no owner files opened."""
    import sys
    root = Path(__file__).resolve().parents[2]
    wrapper = root / "scripts" / "r0_p03_s1_owner_wave0_adversarial_challenge.ps1"
    content = wrapper.read_text(encoding="utf-8")
    assert 'S1_WAVE0_OWNER_RESTRICTED_ADVERSARIAL_EXPORT_RECHECK=PASS' in content
    assert "Run-Python @(" in content
    assert 'Push-Location -LiteralPath $Repo' in content
    assert 'OWNER_EXPORT_CONFIRMATION_REQUIRED' in content
    assert 'CHALLENGE_OWNER_VERSION_ALREADY_STORED' in content
    for module in (
        "s1_wave0_adversarial_packet",
        "s1_wave0_adversarial_challenge_report",
    ):
        result = subprocess.run([
            sys.executable, "-B", "-m",
            "experiments.r0_p03_navigation_probe." + module, "--help",
        ], cwd=root, capture_output=True, text=True, timeout=15, check=False)
        assert result.returncode == 0, result.stderr
        assert result.stdout.startswith("usage:")


def test_synthetic_export_recheck_refuses_modified_plaintext_packet(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = setup_adversarial_synthetic(monkeypatch, tmp_path)
    export_synthetic(fixture)
    raw = fixture["packet"].read_bytes()
    fixture["packet"].write_bytes(raw[:-1] + bytes([raw[-1] ^ 1]))
    with pytest.raises(r.RouteHold, match="CHALLENGE_PACKET_RECOMPUTATION_MISMATCH"):
        export_synthetic(fixture, action="VerifyExport")


def test_synthetic_challenge_packet_hash_and_owner_cert_binding(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = setup_adversarial_synthetic(monkeypatch, tmp_path)
    export_synthetic(fixture)
    packet = fixture["packet"].read_bytes()
    report = invented_substantive_report(packet)
    report["input_packet_sha256"] = "0" * 64
    with pytest.raises(challenged.Hold, match="CHALLENGE_ROLE_OR_STATE_INVALID"):
        challenged.validate_report(report, packet)
    report["input_packet_sha256"] = challenged.sha(packet)
    encrypted = challenged.seal(
        report, packet, openssl=fixture["openssl"]
    )
    unrelated_cert = tmp_path / "synthetic-different-cert.pem"
    unrelated_cert.write_bytes(b"-----BEGIN CERTIFICATE-----\nFICTIONAL-NOT-VALID\n")
    with pytest.raises(challenged.Hold, match="CHALLENGE_OWNER_CERT_BINDING_INVALID"):
        challenged.owner_verify(
            encrypted, packet, unrelated_cert, fixture["key"],
            b"fictional-only", openssl=fixture["openssl"],
        )


def semantic_synthetic_setup(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> dict:
    """All sources, assessments, keypairs and adversarial claims are fictional."""
    fixture = setup_adversarial_synthetic(monkeypatch, tmp_path)
    export_synthetic(fixture)
    challenge_obj = invented_substantive_report(fixture["packet"].read_bytes())
    cipher = challenged.seal(
        challenge_obj, fixture["packet"].read_bytes(), openssl=fixture["openssl"]
    )
    fixture["challenge_cms"] = tmp_path / challenged.REPORT_NAME
    fixture["challenge_cms"].write_bytes(cipher)
    fixture["semantic_packet"] = tmp_path / semantic_packet.PACKET_NAME
    root = Path(__file__).resolve().parents[2]
    fixture["semantic_sender"] = (
        root / "experiments" / "r0_p03_navigation_probe" /
        "s1_wave0_semantic_decision_report.py"
    )
    monkeypatch.setattr(semantic_packet, "CHALLENGE_SHA256", sha256(cipher).hexdigest())
    monkeypatch.setattr(semantic_packet, "CHALLENGE_BYTES", len(cipher))
    monkeypatch.setattr(semantic_report, "CHALLENGE_CMS_SHA", sha256(cipher).hexdigest())
    monkeypatch.setattr(
        semantic_report, "COMPARISON_CMS_SHA", outbound.COMPARISON_SHA256
    )
    monkeypatch.setattr(semantic_report, "ORIGINAL_SOURCE_SHA", r.BATCH_ZIP_SHA256)
    return fixture


def semantic_synthetic_export(fixture: dict, action: str = "Export") -> dict:
    return semantic_packet.owner_export(
        action=action, source_zip=fixture["batch"], first=fixture["first"],
        independent=fixture["second"], comparison=fixture["out"],
        challenge_packet=fixture["packet"],
        challenge_cms=fixture["challenge_cms"],
        cert=fixture["cert"], key=fixture["key"],
        previous_sender=fixture["sender"], sender=fixture["semantic_sender"],
        output=fixture["semantic_packet"], password=b"fictional-only",
        openssl=fixture["openssl"],
    )


def invented_semantic_decisions(packet: bytes) -> dict:
    manifest, rows, _ = semantic_report.inspect_packet(packet)
    records = []
    for index, row in enumerate(rows):
        records.append({
            "path": row["path"],
            "git_blob_oid": row["git_blob_oid"],
            "sha256": row["sha256"],
            "original_source_inspected": True,
            "two_first_pass_records_inspected": True,
            "adversarial_challenge_inspected": True,
            "historical_authority_and_version": (
                "FICTIONAL historical authority limited to this synthetic blob."
            ),
            "supported_prior_evidence": (
                "FICTIONAL: some earlier reasoning matches this invented text."
            ),
            "disputed_or_unproven_prior_evidence": (
                "FICTIONAL: linked references were never provided by the fixture."
            ),
            "strongest_counterinterpretation": (
                "FICTIONAL counterclaim for both earlier source-status positions."
            ),
            "claim_materiality": (
                "FICTIONAL potential difference in stated project lifecycle."
            ),
            "disclosure_materiality": (
                "FICTIONAL protected answer-leakage assessment remains uncertain."
            ),
            "evidence_gaps_and_missing_representations": (
                "FICTIONAL source reference missing; evidence not available here."
            ),
            "decision": "HOLD_FOR_MATERIAL_EVIDENCE" if index == 0
                else "AUXILIARY_ONLY_EXCLUDED_FROM_AUTHOR",
            "decision_rationale": (
                "FICTIONAL decision based on bounded invented original text."
            ),
            "falsification_or_resolution_trigger": (
                "FICTIONAL exact missing reference may falsify this reasoning."
            ),
            "required_next_action": (
                "FICTIONAL hold until reference can be verified" if index == 0
                else "FICTIONAL preserve exclusion pending source-world audit"
            ),
            "author_release": "NONE",
        })
    return {
        "format": semantic_report.FORMAT,
        "input_packet_sha256": semantic_report.sha(packet),
        "original_source_sha256": semantic_report.ORIGINAL_SOURCE_SHA,
        "paired_plaintext_sha256": manifest["paired_plaintext_sha256"],
        "challenge_plaintext_sha256": manifest["challenge_plaintext_sha256"],
        "source_ref": semantic_report.SOURCE_REF,
        "role": "NON_ARM_SOURCE_STATUS_SEMANTIC_ADJUDICATOR",
        "session_exposure_and_independence_limitations": (
            "FICTIONAL separate role with no actual model independence demonstrated."
        ),
        "decision_basis_and_limits": (
            "FICTIONAL first and second reports plus challenge were invented."
        ),
        "report_nonce": "d" * 32,
        "records": records,
        "source_world": "WORLD_UNFROZEN",
        "author_release": "NONE",
        "record_status": "PROPOSED_DECISIONS_REQUIRE_OWNER_QUALIFICATION",
    }


def test_synthetic_semantic_packet_exact_recompute_and_evidence_layers(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = semantic_synthetic_setup(monkeypatch, tmp_path)
    unchanged = {
        name: sha256(fixture[name].read_bytes()).hexdigest()
        for name in ("first", "second", "out", "challenge_cms")
    }
    result = semantic_synthetic_export(fixture)
    assert result["owner_semantic_packet"] == "RESTRICTED_SEMANTIC_PACKET_CREATED"
    assert result["exact_source_count"] == 10
    assert result["private_source_specific_findings_printed"] is False
    assert semantic_synthetic_export(fixture, action="VerifyExport")[
        "owner_semantic_packet"] == "RESTRICTED_PACKET_INDEPENDENT_RECOMPUTATION_PASS"
    with ZipFile(fixture["semantic_packet"]) as archive:
        assert len(archive.namelist()) == 7
        assert b"FICTIONAL_PRIVATE_REASON" in archive.read("PAIRED_FIRST_PASSES.json")
        assert b"FICTIONAL RESTRICTED challenge reason" in archive.read(
            "SUBSTANTIVE_CHALLENGE.json"
        )
        assert archive.read("ORIGINAL_WAVE0_SOURCES.zip") == fixture["batch"].read_bytes()
    assert {
        name: sha256(fixture[name].read_bytes()).hexdigest()
        for name in ("first", "second", "out", "challenge_cms")
    } == unchanged
    with pytest.raises(r.RouteHold, match="ADJUDICATION_PACKET_ALREADY_EXISTS"):
        semantic_synthetic_export(fixture)


def test_synthetic_semantic_decisions_seal_and_owner_authenticate(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = semantic_synthetic_setup(monkeypatch, tmp_path)
    semantic_synthetic_export(fixture)
    packet = fixture["semantic_packet"].read_bytes()
    obj = invented_semantic_decisions(packet)
    raw = semantic_report.validate_report(obj, packet)
    sealed = semantic_report.seal(obj, packet, openssl=fixture["openssl"])
    assert raw not in sealed
    assert b"FICTIONAL decision" not in sealed
    summary = semantic_report.owner_verify(
        sealed, packet, fixture["cert"], fixture["key"],
        b"fictional-only", openssl=fixture["openssl"],
    )
    assert summary["owner_adjudication_cms_authenticated"] == "PASS"
    assert summary["complete_source_decisions_or_holds"] == 10
    assert summary["author_release"] == "NONE"
    assert summary["final_owner_acceptance"] == "PENDING"


def test_synthetic_semantic_rejects_missing_source_and_auto_release(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = semantic_synthetic_setup(monkeypatch, tmp_path)
    semantic_synthetic_export(fixture)
    packet = fixture["semantic_packet"].read_bytes()
    obj = invented_semantic_decisions(packet)
    obj["records"].pop()
    with pytest.raises(semantic_report.Hold, match="ADJUDICATION_RECORD_COUNT_INVALID"):
        semantic_report.validate_report(obj, packet)
    obj = invented_semantic_decisions(packet)
    obj["records"][0]["author_release"] = "ADMITTED"
    with pytest.raises(semantic_report.Hold, match="ADJUDICATION_SOURCE_RECORD_INVALID"):
        semantic_report.validate_report(obj, packet)
    obj = invented_semantic_decisions(packet)
    obj["records"][0]["original_source_inspected"] = False
    with pytest.raises(semantic_report.Hold, match="ADJUDICATION_SOURCE_RECORD_INVALID"):
        semantic_report.validate_report(obj, packet)
    obj = invented_semantic_decisions(packet)
    obj["records"][0]["required_next_action"] = "NONE"
    with pytest.raises(semantic_report.Hold, match="HOLD_REQUIRES_ACTION_OR_LIMITATION"):
        semantic_report.validate_report(obj, packet)


def test_synthetic_semantic_challenge_tamper_and_packet_mutation_rejected(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = semantic_synthetic_setup(monkeypatch, tmp_path)
    raw = fixture["challenge_cms"].read_bytes()
    fixture["challenge_cms"].write_bytes(raw[:-1] + bytes([raw[-1] ^ 0x02]))
    with pytest.raises(r.RouteHold, match="ADJUDICATION_PRIOR_CHALLENGE_INPUT_INVALID"):
        semantic_synthetic_export(fixture)
    assert not fixture["semantic_packet"].exists()
    fixture["challenge_cms"].write_bytes(raw)
    semantic_synthetic_export(fixture)
    packet = fixture["semantic_packet"].read_bytes()
    fixture["semantic_packet"].write_bytes(
        packet[:-1] + bytes([packet[-1] ^ 0x02])
    )
    with pytest.raises(r.RouteHold, match="ADJUDICATION_PACKET_RECOMPUTATION_MISMATCH"):
        semantic_synthetic_export(fixture, action="VerifyExport")


def test_synthetic_semantic_wrong_password_and_wrong_cert_rejected(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    fixture = semantic_synthetic_setup(monkeypatch, tmp_path)
    semantic_synthetic_export(fixture)
    packet = fixture["semantic_packet"].read_bytes()
    sealed = semantic_report.seal(
        invented_semantic_decisions(packet), packet, openssl=fixture["openssl"],
    )
    with pytest.raises(semantic_report.Hold, match="OWNER_ADJUDICATION_CMS_AUTHENTICATION_FAILED"):
        semantic_report.owner_verify(
            sealed, packet, fixture["cert"], fixture["key"], b"bad-passphrase",
            openssl=fixture["openssl"],
        )
    bad_cert = tmp_path / "another-public-cert.pem"
    bad_cert.write_bytes(b"-----BEGIN CERTIFICATE-----\nFICTIONAL\n")
    with pytest.raises(semantic_report.Hold, match="OWNER_CERTIFICATE_MISMATCH"):
        semantic_report.owner_verify(
            sealed, packet, bad_cert, fixture["key"], b"fictional-only",
            openssl=fixture["openssl"],
        )


def test_synthetic_semantic_owner_launcher_imports_and_explicit_disclosure() -> None:
    import sys

    root = Path(__file__).resolve().parents[2]
    wrapper = root / "scripts" / "r0_p03_s1_owner_wave0_semantic_adjudication.ps1"
    text = wrapper.read_text(encoding="utf-8")
    assert "AUTHORIZE WAVE0 SEMANTIC ADJUDICATION EXPORT" in text
    assert "SEMANTIC_OWNER_VERSION_ALREADY_EXISTS" in text
    assert "S1_WAVE0_OWNER_SEMANTIC_EXPORT_RECHECK=PASS" in text
    assert "S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_RECHECK=PASS" in text
    assert "Push-Location -LiteralPath $Repo" in text
    for name in (
        "s1_wave0_semantic_adjudication_packet",
        "s1_wave0_semantic_decision_report",
    ):
        process = subprocess.run([
            sys.executable, "-B", "-m",
            "experiments.r0_p03_navigation_probe." + name, "--help",
        ], cwd=root, capture_output=True, text=True, timeout=20, check=False)
        assert process.returncode == 0, process.stderr
        assert process.stdout.startswith("usage:")
