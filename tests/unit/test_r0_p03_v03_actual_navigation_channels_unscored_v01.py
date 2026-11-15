"""Safety and behavioral tests for actually distinct, non-scored B0-B3 channels.

These tests verify mechanism execution and fairness of the common source
inputs; they never convert exposed coordinator-authored queries/metadata into
independent formal test gold or a numeric Research 513 viability score.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_r0_p03_actual_navigation_channels_unscored_v01 as probe,
)


@pytest.fixture(scope="module")
def arms():
    return {a:probe.NavigationArm(a) for a in probe.PILOT_ARMS}


@pytest.fixture(scope="module")
def result():
    return json.loads(probe.RESULT.read_text("utf8"))


def test_original_git_real_pilot_data_and_four_executable_channels(arms,result):
    assert set(arms) == {"B0","B1","B2","B3"}
    assert result["corpus_source_count"]==24
    assert result["source_ref"]==probe.prior.REF
    assert result["classification"] == "EXPOSED_UNSCORED_REAL_GIT_DISTINCT_B0_B3_EXECUTION"
    assert len(set(result["distinct_mechanisms"].values()))==4
    assert result["full_original_source_byte_count"]>100_000
    assert result["passage_bm25_chunk_count"]>100
    assert result["character_limit_per_document"] is None


def test_prior_12000_character_truncation_does_not_apply(arms):
    body = arms["B0"].bm25.documents["docs/DECISIONS.md"]
    assert len(body)>12_000
    assert "D-036" in body
    assert len(probe.tokens(body))>1000


def test_same_original_source_bytes_and_all_documentary_relations_everywhere(arms,result):
    assert len({a.bm25.total_source_bytes for a in arms.values()})==1
    assert len({sha256(probe.canonical(a.bm25.documentary)).hexdigest()
                for a in arms.values()})==1
    assert len(set(result["common_core_sha256_by_arm"].values()))==1
    assert result["common_documentary_path_relation_count"]>0
    for arm in arms.values():
        assert arm.core.experimental_semantics()["production_j2_j3_qualified"] is False
        assert arm.core.experimental_semantics()["qualifying_j2_count"]==1


@pytest.mark.parametrize("key",["B0","B1","B2","B3"])
def test_all_four_return_source_bound_non_governing_candidates(arms,key):
    got=arms[key].rank("project knowledge architecture",limit=7)
    assert len(got)==7
    assert [r["rank"] for r in got]==list(range(1,8))
    assert len({r["source_path"] for r in got})==7
    assert all(
        r["source_ref"]==probe.prior.REF
        and r["authority_from_navigation"] is False
        and len(r["git_blob_oid"])==40 for r in got
    )
    assert all(r["source_path"] in arms[key].bm25.documents for r in got)


def test_b0_does_not_consume_additional_navigation_signals(arms):
    instance=arms["B0"]
    before=instance.operations.copy()
    instance.rank("governing semantic identity",limit=4)
    after=instance.operations
    assert after["lexical_rank"]==before["lexical_rank"]+1
    assert after["subject_rank"]==before["subject_rank"]
    assert after["editorial_link_rank"]==before["editorial_link_rank"]
    assert after["concern_rank"]==before["concern_rank"]


@pytest.mark.parametrize("arm,channel",[
    ("B1","subject_rank"),
    ("B2","editorial_link_rank"),
    ("B3","concern_rank"),
])
def test_real_additional_channel_called(arms,arm,channel):
    instance=arms[arm]
    before=instance.operations.copy()
    instance.rank("source governance and recovery",limit=5)
    after=instance.operations
    assert after[channel]==before[channel]+1
    for other in ["subject_rank","editorial_link_rank","concern_rank"]:
        if other!=channel:
            assert after[other]==before[other]


def test_all_nonbaseline_channels_change_some_source_rankings(result):
    assert result["exposed_diagnostic_query_count"]==7
    assert result["rankings_changed_vs_b0_count_not_accuracy"]["B0"]==0
    for arm in ("B1","B2","B3"):
        assert result["rankings_changed_vs_b0_count_not_accuracy"][arm]>0
    assert all(
        t["not_a_correctness_score"] is True
        and t["source_revisions_verified_same_all_arms"] is True
        for t in result["exposed_diagnostic_traces_not_scored"]
    )


def test_w5_catalogue_reused_as_vocab_not_historical_reference_gold(arms):
    b1=arms["B1"]
    assert b1.catalog["authority_class"]=="research_fixture"
    assert b1.catalog["source_boundary"] != probe.prior.REF
    assert b1.meta["prior_outcome_exposure"].startswith("COORDINATOR_HAS_SEEN")
    assert b1.meta["source_ref"]==probe.prior.REF


def test_b1_subject_metadata_identical_source_roster_and_allowlisted(arms):
    b1=arms["B1"]
    ids={s["id"] for s in b1.catalog["subjects"] if s["assignable"]}
    assert all(set(v).issubset(ids)
               for v in b1.meta["b1"]["subjects_by_source"].values())
    assert len(b1.meta["b1"]["subjects_by_source"])==24


def test_b3_crosscutting_concerns_are_distinct_label_vocabulary(arms):
    b3=arms["B3"]
    assert set(b3.meta["b3"]["concern_definitions"]).isdisjoint(
        {s["id"] for s in b3.catalog["subjects"]}
    )
    assert len(b3.meta["b3"]["concerns_by_source"])==24


def test_b2_extras_are_not_reused_common_documentary_mentions(arms):
    b2=arms["B2"]
    original = {(e["source"],e["target"])
                for e in b2.bm25.documentary}
    new = {(e["source"],e["target"])
           for e in b2.meta["b2"]["additional_editorial_about_links"]}
    assert len(new)>0
    assert not (original & new)
    assert all(e["claimed_relation"]=="EXPERIMENTAL_EDITORIAL_ABOUT_ONLY"
               for e in b2.meta["b2"]["additional_editorial_about_links"])


def test_duplicate_common_b2_link_fails_closed(arms):
    b2=arms["B2"]
    prior = b2.meta
    try:
        b2.meta=deepcopy(prior)
        link=b2.bm25.documentary[0]
        b2.meta["b2"]["additional_editorial_about_links"].append({
            "source":link["source"],
            "target":link["target"],
            "claimed_relation":"EXPERIMENTAL_EDITORIAL_ABOUT_ONLY",
        })
        with pytest.raises(ValueError,match="B2_DUPLICATE_NATIVE"):
            b2._validate()
    finally:
        b2.meta=prior


def test_unassignable_subject_and_unknown_concern_fail_closed(arms):
    b1=arms["B1"]
    before=b1.meta
    try:
        b1.meta=deepcopy(before)
        key=next(iter(b1.meta["b1"]["subjects_by_source"]))
        b1.meta["b1"]["subjects_by_source"][key]=["ads-system"]
        with pytest.raises(ValueError,match="B1_UNKNOWN_OR_UNASSIGNABLE"):
            b1._validate()
    finally:
        b1.meta=before
    b3=arms["B3"]
    before=b3.meta
    try:
        b3.meta=deepcopy(before)
        key=next(iter(b3.meta["b3"]["concerns_by_source"]))
        b3.meta["b3"]["concerns_by_source"][key]=["unapproved-phantom"]
        with pytest.raises(ValueError,match="B3_UNKNOWN_CONCERN"):
            b3._validate()
    finally:
        b3.meta=before


@pytest.mark.parametrize("query,limit",[
    ("",5),("    ",3),("source",0),("source",21),("source",True)
])
def test_missing_or_overbudget_query_rejected(arms,query,limit):
    with pytest.raises(ValueError,match="BLANK_QUERY|RESULT_BUDGET"):
        arms["B0"].rank(query,limit=limit)


def test_b4_is_not_forged_from_classical_lsa_or_empty_model(arms,result):
    assert "B4" not in arms
    assert result["neural_b4_current_environment"]["formal_inclusion_decision"]==(
        "REQUIRES_PREFREEZE_FEASIBILITY_DECISION"
    )
    assert result["neural_b4_current_environment"]["admission_status"]==(
        "NOT_IMPLEMENTED_OR_PREFREEZE_QUALIFIED"
    )
    with pytest.raises(ValueError,match="UNKNOWN_OR_B4_NOT_FEASIBLE"):
        probe.NavigationArm("B4")


def test_formal_independent_reference_and_60_20_not_claimed(result):
    b=result["authority_boundaries"]
    assert b["independent_reference_gold"] is False
    assert b["source_owner_natural_authoring_qualified"] is False
    assert b["formal_source_sample_60_20_selected"] is False
    assert b["no_comparator_quality_scores_observed"] is True
    assert b["formal_r0_p03"]=="INCOMPLETE"
    assert b["actual_formal_b0_b4_freeze"] is False


def test_actual_exposed_arm_author_cannot_promote_metadata_to_gold(arms):
    for instance in arms.values():
        assert instance.meta["author"]==(
            "EXPOSED_CHATGPT_COORDINATOR_NOT_SOURCE_OWNER_OR_BLIND_EVALUATOR"
        )


def test_immutable_result_reproduces_same_bytes(result):
    assert result["arm_specific_exposed_metadata_sha256"]==probe.METADATA_SHA256
    # The published trace is a deterministic output. The expected-output
    # dependency is deliberately separate from the eventual blind gold.
    data=probe.RESULT.read_bytes()
    assert json.loads(data.decode("utf8"))==result
