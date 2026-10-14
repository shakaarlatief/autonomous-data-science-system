"""Negative checks for fake-only, non-persistent reviewer-output handoff."""
import hashlib
import json
from pathlib import Path
import subprocess

import pytest

from experiments.r0_p03_navigation_probe.synthetic_output_collector_candidate import (
    ARCHIVE_NAME, MARKER, MEMBER_NAME, SEVEN_ZIP, SCRATCH_ROOT,
    SyntheticOutputError, extract_synthetic_final, fake_packet, fake_stream,
    run_demo, seal_synthetic_final, verify_synthetic_seal,
)


def _with_result(packet, **updates):
    result = {"type": "result", "subtype": "success", "is_error": False,
              "result": json.dumps(packet)}
    result.update(updates)
    return (json.dumps({"type": "system", "message": "synthetic"}) + "\n"
            + json.dumps(result) + "\n").encode()


def test_complete_fake_packet_and_final_only_extraction():
    payload = extract_synthetic_final(fake_stream())
    actual = json.loads(payload)
    assert actual == fake_packet()
    assert len(actual["legacy"]) == 9 and len(actual["primary"]) == 12
    assert b"SYNTHETIC_NON_FINAL_IGNORED" not in payload


@pytest.mark.parametrize("bad_stream", [
    b"",
    b"{not json}\n",
    b"[]\n",
    json.dumps({"type": "assistant", "message": "not a result"}).encode(),
    fake_stream() + fake_stream(),
    _with_result(fake_packet(), is_error=True),
    _with_result(fake_packet(), subtype="error"),
    _with_result(fake_packet(), result="not-json"),
    _with_result(fake_packet(), result={"not": "text"}),
    b"\xff\n",
])
def test_malformed_or_ambiguous_stream_fails_closed(bad_stream):
    with pytest.raises(SyntheticOutputError):
        extract_synthetic_final(bad_stream)


def test_oversized_stream_rejected_without_parser_or_archive():
    with pytest.raises(SyntheticOutputError, match="oversized"):
        extract_synthetic_final(b"x" * (512 * 1024 + 1))


def test_partial_packet_and_real_looking_claim_refused():
    packet = fake_packet()
    packet["primary"].pop()
    with pytest.raises(SyntheticOutputError):
        extract_synthetic_final(_with_result(packet))
    packet = fake_packet()
    packet["legacy"][0]["claim"] = "ACTUAL_EXPECTED_SOURCE"
    with pytest.raises(SyntheticOutputError):
        extract_synthetic_final(_with_result(packet))
    packet = fake_packet()
    packet["synthetic_only"] = False
    with pytest.raises(SyntheticOutputError):
        extract_synthetic_final(_with_result(packet))
    packet = fake_packet()
    packet["marker"] = "REAL_GOLD"
    with pytest.raises(SyntheticOutputError):
        extract_synthetic_final(_with_result(packet))


def test_synthetic_only_secret_guard_before_archive_creation(tmp_path):
    archive = tmp_path / ARCHIVE_NAME
    for bad in ["real-password", "SYNTHETIC_ONLY_ab", "", "SYNTHETIC_ONLY_"+"G"*40]:
        with pytest.raises(SyntheticOutputError):
            seal_synthetic_final(fake_stream(), archive, bad)
    assert not archive.exists()


def test_external_and_existing_destinations_rejected(tmp_path):
    password = "SYNTHETIC_ONLY_" + "a" * 40
    with pytest.raises(SyntheticOutputError):
        seal_synthetic_final(fake_stream(), tmp_path / ARCHIVE_NAME, password)
    scratch = SCRATCH_ROOT / ".r0p03-existing-guard-test"
    scratch.mkdir(exist_ok=True)
    try:
        p = scratch / ARCHIVE_NAME
        p.write_bytes(b"EXISTING_FAKE_ARCHIVE")
        with pytest.raises(SyntheticOutputError):
            seal_synthetic_final(fake_stream(), p, password)
        assert p.read_bytes() == b"EXISTING_FAKE_ARCHIVE"
    finally:
        (scratch / ARCHIVE_NAME).unlink(missing_ok=True)
        scratch.rmdir()


@pytest.mark.skipif(not SEVEN_ZIP.is_file(), reason="Requires installed 7-Zip")
def test_actual_encrypted_stdin_capture_and_separate_recovery(tmp_path):
    # Use disposable scratch inside .venv, not the pytest out-of-tree temp.
    import tempfile
    with tempfile.TemporaryDirectory(prefix=".r0p03-test-", dir=SCRATCH_ROOT) as t:
        p = Path(t) / ARCHIVE_NAME
        password = "SYNTHETIC_ONLY_" + "c" * 40
        receipt = seal_synthetic_final(fake_stream(), p, password)
        assert p.exists() and p.is_file()
        assert not (p.parent / MEMBER_NAME).exists()
        assert receipt["source_sha256"] == hashlib.sha256(
            extract_synthetic_final(fake_stream())
        ).hexdigest()
        assert verify_synthetic_seal(p, password, receipt["source_sha256"])
        assert not verify_synthetic_seal(
            p, "SYNTHETIC_ONLY_" + "e"*40, receipt["source_sha256"]
        )
        # Directly inspect the encrypted archive header without showing plaintext.
        listing = subprocess.run(
            [str(SEVEN_ZIP), "l", "-slt", "-p" + password, str(p)],
            capture_output=True, timeout=20,
        )
        assert listing.returncode == 0
        assert b"7zAES" in listing.stdout
        wrong = subprocess.run(
            [str(SEVEN_ZIP), "l", "-slt", "-p" + "SYNTHETIC_ONLY_" + "e"*40,
             str(p)],
            capture_output=True, timeout=20,
        )
        assert wrong.returncode != 0 and MEMBER_NAME.encode() not in wrong.stdout


@pytest.mark.skipif(not SEVEN_ZIP.is_file(), reason="Requires installed 7-Zip")
def test_printed_receipt_has_no_fake_answers_or_password(capsys):
    receipt = run_demo()
    print(json.dumps(receipt, sort_keys=True))
    captured = capsys.readouterr().out
    assert "FAKE_LEGACY" not in captured
    assert "FAKE_PRIMARY" not in captured
    assert "SYNTHETIC_ONLY_" not in captured
    assert receipt["exact_recovery_after_subprocess"] is True
    assert receipt["wrong_password_rejected"] is True
    assert receipt["real_output_custody_qualified"] is False
