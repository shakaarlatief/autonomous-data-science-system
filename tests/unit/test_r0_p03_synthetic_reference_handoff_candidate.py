"""Synthetic complete-answer delivery mechanics, never real reference custody."""
import json
from pathlib import Path

import pytest

from experiments.r0_p03_navigation_probe import (
    synthetic_output_collector_candidate as collector,
    synthetic_reference_handoff_candidate as handoff,
)


def test_21_case_packet_matches_reused_strict_collector():
    data = handoff.exact_fake_final(collector.fake_stream())
    packet = json.loads(data)
    assert len(packet["legacy"]) == 9
    assert len(packet["primary"]) == 12
    assert packet["synthetic_only"] is True


def test_duplicate_final_and_malformed_reference_refused_before_sealing():
    event = json.dumps({
        "type": "result", "subtype": "success", "is_error": False,
        "result": json.dumps(collector.fake_packet()),
    })
    with pytest.raises(collector.SyntheticOutputError):
        handoff.exact_fake_final((event + "\n" + event + "\n").encode())
    fake = collector.fake_packet()
    fake["legacy"][0]["claim"] = "REAL_REFERENCE"
    bad = json.dumps({
        "type": "result", "subtype": "success", "is_error": False,
        "result": json.dumps(fake),
    })
    with pytest.raises(collector.SyntheticOutputError):
        handoff.exact_fake_final((bad + "\n").encode())


def test_nonexistent_custody_files_and_noncanonical_digest_refused(tmp_path: Path):
    assert handoff.recipient_readback(
        tmp_path / "no.cms", tmp_path / "no.pem",
        tmp_path / "no.key", "0" * 64
    ) is False
    assert handoff.recipient_readback(
        tmp_path / "no.cms", tmp_path / "no.pem",
        tmp_path / "no.key", "INCOMPLETE"
    ) is False


def test_real_synthetic_delivery_ciphertext_and_separate_process_recovery():
    evidence = handoff.run_demo()
    assert evidence["synthetic_only"] is True
    assert evidence["fictional_legacy_slots"] == 9
    assert evidence["fictional_primary_slots"] == 12
    for key in (
        "source_stream_result_validated",
        "mock_author_received_public_certificate_only",
        "mock_delivery_ciphertext_sha256_match",
        "fresh_subprocess_exact_full_packet_recovery",
        "tampered_ciphertext_rejected",
        "wrong_commitment_rejected",
    ):
        assert evidence[key] is True
    assert evidence["mock_author_wrote_plaintext_packet_file"] is False
    assert evidence["actual_distinct_windows_principals"] is False
    assert evidence["actual_model_author_invoked"] is False
    assert evidence["owner_held_key_or_real_answer_custody_qualified"] is False
    assert evidence["hidden_gold_qualified"] is False
