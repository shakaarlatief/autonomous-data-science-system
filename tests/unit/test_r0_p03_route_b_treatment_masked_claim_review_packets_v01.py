"""Prove frozen reviewer packets omit self-gold and retain exact source lines.

These tests DO NOT claim an independent review happened, or score R0-P03.
They validate the bounded input that a separately authorized model receives.
"""
from __future__ import annotations
from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.route_b_primary_b0_baseline_execution_v01 import original_contents
from experiments.r0_p03_navigation_probe.route_b_treatment_masked_claim_review_export_v01 import (
    ARMS, BASE, BATCH_SIZE, N, SOURCE, RESPONSES, exported_packets, output_bytes, original_json,
    SOURCE_BYTES, SOURCE_SHA, RESPONSES_BYTES, RESPONSES_SHA,
)

PACKETS = (
    ("p01_to_p04", 59983, "6f76a9d8cb11beb64e0b8493230bf24e3b6f87920c562368ac14e2cd458bdb3b"),
    ("p05_to_p08", 62864, "0615031623d83c7bb6aba74588d18fa9fca5877d72828bd735f5f503b1751623"),
    ("p09_to_p12", 62152, "e63afe2ebe79fc7e6ec3751d61971c6794d71cc1904057f2ee7aa691f9636804"),
)


def test_original_upstream_packet_and_authored_prose_are_byte_identical() -> None:
    assert original_json(SOURCE, SOURCE_BYTES, SOURCE_SHA)
    assert original_json(RESPONSES, RESPONSES_BYTES, RESPONSES_SHA)
    assert (BASE / "ROUTE_B_TREATMENT_MASKED_CLAIM_REVIEW_CONTRACT_V01.md").exists()


def test_exclusive_created_three_review_packets_match_reconstruction_exactly() -> None:
    expected = exported_packets()
    assert len(expected) == 3
    for spec, value in zip(PACKETS, expected):
        suffix, length, digest = spec
        filename = BASE / f"route_b_treatment_masked_claim_review_{suffix}_v01.json"
        raw = filename.read_bytes()
        assert len(raw) == length
        assert sha256(raw).hexdigest() == digest
        assert output_bytes(value) == raw
        assert raw.endswith(b"\n") and b"\r\n" not in raw


def test_complete_twelve_case_coverage_with_balanced_mask_and_no_prior_self_scores() -> None:
    packets = exported_packets()
    all_cases = [c for batch in packets for c in batch["cases"]]
    assert len(all_cases) == N == 12
    assert [c["case_id"] for c in all_cases] == [f"P{i:02}" for i in range(1, 13)]
    assert all(len(batch["cases"]) == BATCH_SIZE == 4 for batch in packets)
    assert all(len(case["variants"]) == 2 for case in all_cases)
    assert sum(len(x["claims"]) for case in all_cases for x in case["variants"]) == 47
    assert all(
        [v["variant"] for v in case["variants"]] == ["VARIANT_A", "VARIANT_B"]
        for case in all_cases
    )
    original = original_json(SOURCE, SOURCE_BYTES, SOURCE_SHA)
    authored = original_json(RESPONSES, RESPONSES_BYTES, RESPONSES_SHA)
    by_answer = {(r["id"], r["arm"]): r for r in authored["paired_responses"]}
    for i, case in enumerate(all_cases):
        source = original["source_only_question_packets"][i]
        order = ARMS if i % 2 == 0 else tuple(reversed(ARMS))
        assert case["question"] == source["question"]
        for index, arm in enumerate(order):
            variant = case["variants"][index]
            assert variant["answer"] == by_answer[(case["case_id"], arm)]["answer"]
            assert "coverage" not in variant
            assert "self_assessment" not in variant
    for suffix, _, _ in PACKETS:
        raw = (BASE / f"route_b_treatment_masked_claim_review_{suffix}_v01.json").read_text("utf8")
        forbidden = (
            '"B0_ORIGINAL"', '"B1_EXPOSED_SUBJECT_B0"', "self_coverage_counts",
            '"coverage":', "reference_answer_for_evaluation_only",
            "required_source_for_evaluation_only", "retrospective_reference_evidence_audit",
            "all_reference_excerpts_actually_cited",
        )
        assert all(text not in raw for text in forbidden)


def test_every_masked_claim_and_source_line_is_original_git_source_exact() -> None:
    batches = exported_packets()
    sources = {
        source["path"]
        for batch in batches for case in batch["cases"]
        for variant in case["variants"] for source in variant["available_evidence"]
    }
    git = original_contents(sorted(sources))
    assert len(git) >= 12
    cited = 0
    for batch in batches:
        for case in batch["cases"]:
            for variant in case["variants"]:
                records = variant["available_evidence"]
                assert len(records) <= 3
                for i, source in enumerate(records, 1):
                    assert source["source_rank"] == i
                    assert source["original_source_sha256"] == sha256(git[source["path"]]).hexdigest()
                    assert len(source["lines"]) <= 5
                    lines = git[source["path"]].decode("utf8").splitlines()
                    for item in source["lines"]:
                        assert lines[item["line"] - 1] == item["original_source_line"]
                        assert sha256(lines[item["line"] - 1].encode("utf8")).hexdigest() == item["original_line_sha256"]
                for claim in variant["claims"]:
                    assert claim["statement"] and claim["cited_original_line_refs"]
                    for witness in claim["cited_original_line_refs"]:
                        src = records[witness["source_rank"] - 1]
                        assert any(l["line"] == witness["line"] for l in src["lines"])
                        cited += 1
    assert cited == 78


def test_review_packets_make_no_false_independent_gold_claim() -> None:
    packets = exported_packets()
    for packet in packets:
        assert packet["contains_original_reference_answers"] is False
        assert packet["contains_model_author_self_coverage"] is False
        assert packet["treatment_labels_masked"] is True
        assert packet["source_git_pin"] == "47ed6344a9153dcf366769e95722840fbf1a8f8b"
        assert len(packet["cases"]) == 4
        assert packet["review_protocol"] == "ROUTE_B_TREATMENT_MASKED_CLAIM_REVIEW_CONTRACT_V01.md"
