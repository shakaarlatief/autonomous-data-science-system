"""Synthetic and original-frozen-fixture tests for source-only masked review.

No private reference truth, original Git source search, previous gold labels
or original reviewer results are consumed. The tests prove each candidate's
per-case source excerpts are copied exactly from its own frozen answer
context, including the originally observed cross-case reference defect.
"""
from __future__ import annotations

from hashlib import sha256
import json
import re

import pytest

from experiments.r0_p03_navigation_probe import (
    four_need_masked_source_excerpt_claim_review_v01 as mask,
    four_need_source_only_answer_case_boundary_audit_v01 as frozen,
)


def test_inputs_are_exact_original_and_review_contract_is_frozen() -> None:
    assert sha256(mask.CONTRACT.read_bytes()).hexdigest() == mask.CONTRACT_SHA256
    for tag in ("A", "B"):
        assert sha256(frozen.ANSWERS[tag][0].read_bytes()).hexdigest() == frozen.ANSWERS[tag][1]
        assert sha256(frozen.PACKETS[tag][0].read_bytes()).hexdigest() == frozen.PACKETS[tag][1]


@pytest.mark.parametrize(
    ("original", "expected_replacements", "contains_semantic_phrase"),
    [
        (
            "**Self-description: PARTIAL_FROM_SUPPLIED_EXCERPTS**\n"
            "The source self-description is not shown. Packet A describes no answer.",
            1, True,
        ),
        (
            "**Self-description: PARTIAL_FROM_SUPPLIED_EXCERPTS**\n"
            "Packet B records a possible route, with a caveat.",
            1, False,
        ),
    ],
)
def test_masking_removes_author_labels_not_substantive_evidence(
    original: str, expected_replacements: int, contains_semantic_phrase: bool,
) -> None:
    reviewed, metrics = mask.mask_original_answer_body(original)
    assert metrics["author_self_disposition_labels_removed"] == 1
    assert metrics["treatment_name_replacements"] == expected_replacements
    assert "PARTIAL_FROM_SUPPLIED_EXCERPTS" not in reviewed
    assert "Packet A" not in reviewed and "Packet B" not in reviewed
    assert ("self-description" in reviewed) == contains_semantic_phrase
    assert "the assigned packet" in reviewed


def test_original_verdict_label_missing_is_rejected() -> None:
    with pytest.raises(ValueError):
        mask.mask_original_answer_body("A passage with no author self-disposition line.")


def test_mask_is_balanced_independent_of_answer_contents() -> None:
    ids = [f"R0P03-PILOT-N0{i}" for i in range(1, 5)]
    selected = mask.deterministic_treatment_for_p(ids)
    assert len(selected) == 2
    assert selected <= set(ids)
    assert selected == mask.deterministic_treatment_for_p(list(reversed(ids)))


def test_full_original_case_local_excerpts_survive_masking_and_no_gold_is_added() -> None:
    fixture, manifest = mask.build()
    assert len(fixture["cases"]) == 4
    assert fixture["candidate_count"] == 8
    assert fixture["original_private_reference_answers_in_packet"] is False
    assert fixture["earlier_author_self_dispositions_in_packet"] is False
    assert fixture["formal_scoring_allowed"] is False
    assert manifest["self_disposition_labels_removed"] == 8
    assert manifest["explicit_treatment_name_replacements"] == 2
    assert manifest["source_contexts_count"] == 32
    assert manifest["excerpt_windows_count"] == 64
    assert manifest["balanced_candidate_label_positions"] is True
    assert "treatment_A" not in json.dumps(fixture)
    assert "treatment_B" not in json.dumps(fixture)
    assert "answer_A" not in json.dumps(fixture)
    assert "answer_B" not in json.dumps(fixture)
    for i, row in enumerate(fixture["cases"]):
        candidates = row["masked_candidates"]
        assert [c["candidate"] for c in candidates] == ["CANDIDATE_P", "CANDIDATE_Q"]
        assert len(candidates) == 2
        assert row["question_id"] == f"R0P03-PILOT-N0{i+1}"
        for item in candidates:
            assert len(item["permitted_case_local_source_excerpts"]) == 4
            assert len({(s["original_git_path"], s["original_git_blob_sha1"])
                        for s in item["permitted_case_local_source_excerpts"]}) == 4
            assert "Self-description:" not in item["response_text"]
            assert not re.search(r"Packet [AB]\b", item["response_text"])
            contexts = [
                tag for tag in ("A", "B")
                if json.loads(frozen.PACKETS[tag][0].read_bytes())["cases"][i]["source_excerpts"]
                   == item["permitted_case_local_source_excerpts"]
            ]
            assert len(contexts) >= 1
            assert item["response_text"]


def test_review_fixture_never_autofixes_existing_cross_case_reference() -> None:
    fixture, _ = mask.build()
    # The original B N03 response cites a source assigned to B N04. The
    # review fixture must retain that original claim/citation but not add
    # another case's source context to make it artificially admissible.
    n03 = fixture["cases"][2]["masked_candidates"]
    contaminated = []
    for candidate in n03:
        allowed = {
            (s["original_git_path"], s["original_git_blob_sha1"])
            for s in candidate["permitted_case_local_source_excerpts"]
        }
        references = {
            (m["path"], m["oid"])
            for m in frozen.SOURCE_REF.finditer(candidate["response_text"])
        }
        contaminated.append(bool(references - allowed))
    assert contaminated.count(True) == 1


def test_frozen_masked_review_packet_replays_exact_original_bytes() -> None:
    fixture, manifest = mask.build()
    expected_fixture = mask.encode(fixture)
    expected_manifest = mask.encode(manifest)
    assert mask.FIXTURE.read_bytes() == expected_fixture
    assert mask.MANIFEST.read_bytes() == expected_manifest
    assert sha256(expected_fixture).hexdigest() == "e53544ac31eacaf6fd64e74b67c920d9a2b0ec96bafb1a0951c5fdc43c3453a2"
    assert sha256(expected_manifest).hexdigest() == "afd02851a2795be8442b1d8e859fbcf7456c3038256ebb67bddd3306f9fbda62"
    assert manifest["fixture_sha256"] == sha256(expected_fixture).hexdigest()
    assert manifest["fixture_bytes"] == len(expected_fixture)
