"""Strict metadata-only reproducibility for a small unscored R0-P03 need pilot.

This is neither reference-answer gold, source truth, nor formal Research 513
score qualification. Frozen index construction must remain source-text-free.
"""
from __future__ import annotations

from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.fresh_reference_need_index_pilot_v01 import (
    ANCHORS, OUTPUT, PER_STRATUM, PIN, STRATA, VERSION, build,
    original_git_inventory,
)

SIZE=14075
DIGEST="c09905e2758f31086888f455aec4812c4c1a30319f5001d9ce06e74aa37f1415"


def stored() -> dict:
    raw=OUTPUT.read_bytes()
    assert len(raw)==SIZE
    assert sha256(raw).hexdigest()==DIGEST
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    return json.loads(raw)


def test_original_exact_path_only_index_replays_from_original_git() -> None:
    assert build()==stored()


def test_stratified_source_world_counts_and_non_overlap() -> None:
    d=stored()
    assert d["id"]==VERSION and d["original_source_git_pin"]==PIN
    assert len(d["items"])==52
    assert len({x["original_git_path"] for x in d["items"]})==52
    assert all(len(x["original_blob_oid"])==40 for x in d["items"])
    for name,prefix in STRATA:
        rows=[r for r in d["items"] if r["stratum"]==name]
        assert len(rows)==PER_STRATUM
        assert [r["sampling_rank"] for r in rows]==list(range(1,11))
        assert all(r["original_git_path"].startswith(prefix) for r in rows)
    assert [r["original_git_path"] for r in d["items"] if r["stratum"]=="ORIENTATION_ANCHOR"]==list(ANCHORS)


def test_all_paths_and_blob_ids_exist_only_at_frozen_historical_git() -> None:
    source=original_git_inventory()
    assert all(source.get(r["original_git_path"])==r["original_blob_oid"] for r in stored()["items"])


def test_four_predeclared_need_categories_without_answer_contents() -> None:
    d=stored()
    assert d["the_four_need_categories"]==[
        "COLD_START_CURRENT_ORIENTATION",
        "CROSS_PLANE_DISCOVERY",
        "IMPACT_ANALYSIS_ARCHITECTURE_EVOLUTION",
        "EXACT_SOURCE_AUTHORITY_RECOVERY",
    ]
    assert d["path_index_only"] is True
    assert d["original_source_bodies_present"] is False
    assert d["original_answer_text_present"] is False
    assert d["existing_twelve_B0_B1_questions_or_answers_present"] is False
    assert d["source_role_labels_are_not_authority_evidence"] is True
    assert d["original_R0_P03_scoring_result"]=="INCOMPLETE"
    for r in d["items"]:
        assert set(r)=={"stratum","sampling_rank","original_git_path","original_blob_oid"}


def test_singular_new_instruction_and_no_preexisting_question_output() -> None:
    from pathlib import Path
    directory=Path("docs/model_collaboration/threads/MC-0030/messages")
    assert len(list(directory.glob("072_*")))==1
    replies = list(directory.glob("073_*"))
    assert len(replies) <= 1
    if replies:
        assert replies[0].name == "073_claude_r0_p03_fresh_independent_need_origination_pilot.md"
    contract=Path("experiments/r0_p03_navigation_probe/FRESH_REFERENCE_NEED_ORIGINATION_PILOT_CONTRACT_V01.md")
    assert contract.is_file()
    assert "FORMAL_R0_P03_SCORING_ALLOWED=false" in contract.read_text("utf8")
