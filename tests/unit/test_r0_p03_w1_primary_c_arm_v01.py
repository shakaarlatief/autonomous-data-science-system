"""Adversarial W1 C_arm primary comparator tests, before formal task origination.

These regressions qualify the exact *experiment-only* implementation contract:
equal original Git source, common S1 authority and lexical access; exclusive
non-governing authored navigation metadata; context-budget parity; and
prospectively declared B4 omission. They do not score, invent gold or select
heldout carriers, nor do they turn the nine legacy tasks into new gold.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from hashlib import sha256

import pytest

from experiments.r0_p03_navigation_probe import w1_primary_c_arm_v01 as a


@pytest.fixture(scope="module")
def frozen():
    return a.make_frozen()


@pytest.fixture(scope="module")
def arms(frozen):
    return frozen[3]


def test_single_unchanged_w1_60_source_world(frozen,arms):
    contract,meta,catalog,_=frozen
    assert set(arms)=={"B0","B1","B2","B3"}
    assert contract["common_original_source_count"]==60
    assert contract["original_source_git"]==a.w1.PIN
    assert contract["common_original_source_bytes"]==822370
    assert contract["common_bm25_passage_count"]==4626
    assert contract["future_heldout_draw"]=="NOT_DRAWN"
    assert contract["protected_gold"]=="NONE"
    assert contract["post_arm_freeze_primary_authoring"]=="NOT_YET_OCCURRED"
    assert contract["formal_scored_attempts_used"]==0
    assert contract["physical_target_selected"] is False


def test_full_original_git_bytes_and_common_authority(frozen,arms):
    fingerprints={key:val.core.common_digest() for key,val in arms.items()}
    assert len(set(fingerprints.values()))==1
    sources=arms["B0"].list_sources()
    assert len(sources)==60
    for key in arms:
        assert arms[key].list_sources()==sources
        assert arms[key].semantics()==arms["B0"].semantics()
        assert arms[key].read("docs/DECISIONS.md")==arms["B0"].read("docs/DECISIONS.md")
        assert arms[key].search("reconstruction",limit=5)==arms["B0"].search(
            "reconstruction",limit=5
        )
        assert arms[key].core.semantics()["only_accepted_experiment_core"][
            "qualifying_j2_count"
        ]==1
        assert arms[key].core.semantics()["no_production_acceptance_or_realization"]


def test_b0_metadata_zero_b1_b2_b3_have_measured_counts(frozen):
    contract=frozen[0]
    cost=contract["costs_not_quality_scores"]
    assert cost["B0"]["authored_subject_memberships"]==0
    assert cost["B0"]["author_created_editorial_links"]==0
    assert cost["B0"]["authored_concern_memberships"]==0
    assert cost["B0"]["incremental_navigation_metadata_bytes_utf8"]==0
    assert cost["B1"]["authored_subject_memberships"]==120
    assert cost["B1"]["preferred_subject_routes"]==60
    assert cost["B2"]["author_created_editorial_links"]==23
    assert cost["B3"]["authored_concern_memberships"]==115
    assert cost["B3"]["authored_concern_definitions"]==5
    assert all(row["manual_annotation_minutes"]=="NOT_MEASURED_NOT_ASSUMED_FREE"
               for row in cost.values())
    assert all(row["recurring_cost"]=="NOT_YET_MEASURED_ON_HELDOUT"
               for row in cost.values())


def test_all_curated_paths_match_exact_manifest_and_source_line_witness(arms):
    a0=arms["B0"]
    m=a0.meta
    roster=set(a0.list_sources())
    assert set(m["b1_subjects_by_source"])==roster
    assert set(m["b3_concerns_by_source"])==roster
    assert set(m["source_context_anchors"])==roster
    for path in roster:
        anchor=m["source_context_anchors"][path]
        lines=a0.index.documents[path].splitlines()
        literal=lines[anchor["source_line"]-1]
        assert sha256(literal.encode("utf8")).hexdigest()==anchor["source_line_sha256"]
        assert anchor["witness_is_not_independent_label_verification"] is True
    assert not m["source_adjacent_coordinator_authorship"]["natural_owner_j2"] if (
        "natural_owner_j2" in m["source_adjacent_coordinator_authorship"]
    ) else True
    assert m["source_adjacent_coordinator_authorship"]["not_natural_owner_j2"] is True
    assert m["source_adjacent_coordinator_authorship"][
        "no_protected_task_gold_or_heldout_access"
    ] is True


def test_b1_controlled_facet_hierarchy_and_preferred_paths(arms):
    b1=arms["B1"]
    assert len([x for x in b1.catalog["subjects"] if x["assignable"]])==18
    assert len([x for x in b1.catalog["subjects"] if not x["assignable"]])==6
    matched=b1.browse_subject("project-knowledge-architecture")
    assert any(row["source_path"]=="tools/project_knowledge/identity.py"
               for row in matched["sources"])
    assert all(row["navigation_is_non_governing"] for row in matched["sources"])
    parents=[x for x in b1.catalog["subjects"] if not x["assignable"]]
    assert any(b1.browse_subject(p["id"])["sources"] for p in parents)
    assert any(len(v["subjects"])>1
               for v in b1.meta["b1_subjects_by_source"].values())


def test_b2_source_carrier_to_governing_and_no_direct_documentary_duplicates(arms):
    b2=arms["B2"]
    original=b2.index.common_documentary_edges
    all_edges=b2.meta["b2_additional_editorial_links"]
    assert len(all_edges)==23
    assert not any(
        (edge["source"],edge["governing_target"]) in original
        for edge in all_edges
    )
    assert all(
        b2.index.rows[edge["governing_target"]]["stratum"]=="governing"
        and b2.index.rows[edge["source"]]["stratum"]!="governing"
        and edge["relation"]=="NON_GOVERNING_EDITORIAL_ABOUT_ONLY"
        and edge["claims_j1_j2_j3_implementation"] is False
        and edge["source_owner_verified"] is False
        for edge in all_edges
    )
    sample=b2.browse_links("tools/project_knowledge/identity.py")
    assert sample and sample[0]["governing_target"].startswith("docs/specifications/")


def test_b2_rejects_duplicate_source_native_edge(arms):
    b2=arms["B2"]
    original=b2.meta
    try:
        b2.meta=deepcopy(original)
        source,target=next(iter(b2.index.common_documentary_edges))
        b2.meta["b2_additional_editorial_links"].append({
            "id":"INVALID","source":source,"governing_target":target,
            "relation":"NON_GOVERNING_EDITORIAL_ABOUT_ONLY",
            "claims_j1_j2_j3_implementation":False,
            "source_owner_verified":False,
        })
        with pytest.raises(ValueError,match="B2_REDUNDANT"):
            b2._validate()
    finally:
        b2.meta=original


def test_b2_rejects_false_accepted_relation(arms):
    b2=arms["B2"]
    original=b2.meta
    try:
        b2.meta=deepcopy(original)
        b2.meta["b2_additional_editorial_links"][0][
            "claims_j1_j2_j3_implementation"
        ]=True
        with pytest.raises(ValueError,match="B2_REDUNDANT"):
            b2._validate()
    finally:
        b2.meta=original


def test_b1_rejects_unassignable_subject(arms):
    b1=arms["B1"]
    before=b1.meta
    try:
        b1.meta=deepcopy(before)
        path=next(iter(b1.meta["b1_subjects_by_source"]))
        b1.meta["b1_subjects_by_source"][path]={
            "subjects":["ads-system"],"preferred_subject":"ads-system",
        }
        with pytest.raises(ValueError,match="B1_INVALID"):
            b1._validate()
    finally:
        b1.meta=before


def test_b3_concerns_are_distinct_and_bound_to_source(arms):
    b3=arms["B3"]
    vocabulary=set(b3.meta["concern_descriptions"])
    w5={s["id"] for s in b3.catalog["subjects"]}
    assert not (vocabulary&w5)
    assert len(vocabulary)==5
    found=b3.browse_concern("source-evidence-integrity")
    assert found
    assert all(row["navigation_is_non_governing"] for row in found)


def test_b3_rejects_unknown_concern(arms):
    b3=arms["B3"]
    original=b3.meta
    try:
        b3.meta=deepcopy(original)
        path=next(iter(b3.meta["b3_concerns_by_source"]))
        b3.meta["b3_concerns_by_source"][path]=["invented-governing-tag"]
        with pytest.raises(ValueError,match="B3_UNKNOWN"):
            b3._validate()
    finally:
        b3.meta=original


@pytest.mark.parametrize("arm",a.PILOT_ARMS)
def test_ranking_returns_exact_source_revision_not_governing_truth(arms,arm):
    result=arms[arm].rank("project knowledge reconstruction",limit=4)
    assert len(result)==4
    assert len(set(row["source_path"] for row in result))==4
    for i,item in enumerate(result,1):
        assert item["rank"]==i
        assert item["source_ref"]==a.w1.PIN
        assert len(item["git_blob_oid"])==40
        assert item["navigation_confers_authority"] is False


@pytest.mark.parametrize("arm,signal",[
    ("B0","lexical_rank"),
    ("B1","subject_rank"),
    ("B2","editorial_rank"),
    ("B3","concern_rank"),
])
def test_separate_navigation_signal_really_runs(arms,arm,signal):
    obj=arms[arm]
    prior=obj.operation_counts.copy()
    obj.rank("source provenance and validity",limit=4)
    after=obj.operation_counts
    assert after["lexical_rank"]==prior["lexical_rank"]+1
    if arm!="B0":
        assert after[signal]==prior[signal]+1
    for other in ("subject_rank","editorial_rank","concern_rank"):
        if other!=signal:
            assert after[other]==prior[other]


@pytest.mark.parametrize("arm",a.PILOT_ARMS)
def test_equal_context_packs_all_return_exact_line_hashes_under_budget(arms,arm):
    result=arms[arm].context_pack("project knowledge architecture",limit=6)
    assert result["sources_count"]==6
    assert result["per_source_excerpt_cap"]==2800
    assert result["total_excerpt_cap"]==6*2800
    assert result["excerpts_total_characters"]<=6*2800
    assert result["derived_index_or_ranking_confers_authority"] is False
    assert result["evidence_not_independent_gold"] is True
    for snippet in result["exact_source_line_snippets"]:
        assert snippet["source_ref"]==a.w1.PIN
        assert snippet["source_full_read_available"] is True
        assert snippet["excerpt_characters"]<=2800
        for line in snippet["complete_lines"]:
            assert sha256(line["text"].encode("utf8")).hexdigest()==line["line_sha256"]
            assert line["text"]==arms[arm].index.documents[
                snippet["source_path"]
            ].splitlines()[line["line"]-1]


@pytest.mark.parametrize("bad_query,limit",[
    ("",6),(" ",6),("x"*161,6),("source",0),("source",True),("source",9)
])
def test_query_and_context_limits_reject_invalid_calls(arms,bad_query,limit):
    with pytest.raises(ValueError,match="W1_ARM_INVALID_QUERY|W1_ARM_RESULT_LIMIT|W1_ARM_CONTEXT_PACK_BUDGET"):
        arms["B0"].context_pack(bad_query,limit=limit)


def test_neural_b4_not_passed_off_as_old_lsa(arms,frozen):
    with pytest.raises(ValueError,match="W1_ARM_NOT_BUILT_OR_UNKNOWN"):
        a.W1PrimaryArm("B4",arms["B0"].index,arms["B0"].meta,arms["B0"].catalog)
    b4=frozen[0]["b4"]
    assert b4["policy"]=="B4_OMITTED_PROSPECTIVELY_AT_W1_PRIMARY_C_ARM_FREEZE"
    assert b4["classical_lsa_is_not_neural_b4"] is True
    assert b4["no_comparative_embedding_score_was_observed"] is True
    assert b4["neural_models_ruled_out_globally"] is False


def test_index_identity_is_shared_and_metadata_cannot_change_common_semantics(arms):
    indices={id(item.index) for item in arms.values()}
    assert len(indices)==1
    digest=arms["B0"].core.common_digest()
    original=arms["B1"].meta
    try:
        arms["B1"].meta=deepcopy(original)
        a0=arms["B1"].meta["b1_subjects_by_source"]
        a0["docs/CONTINUITY.md"]["subjects"]=["tooling-integrations"]
        assert arms["B0"].core.common_digest()==digest
        assert arms["B1"].core.common_digest()==digest
    finally:
        arms["B1"].meta=original


def test_no_hidden_gold_legacy_task_or_heldout_in_arm_fixture(frozen):
    c=frozen[0]
    assert c["post_arm_freeze_primary_authoring"]=="NOT_YET_OCCURRED"
    assert c["research559_legacy_nine"]=="NOT_YET_FROZEN_DO_NOT_BUILD_LEGACY_ARMS"
    assert c["protected_gold"]=="NONE"
    assert c["future_heldout_draw"]=="NOT_DRAWN"
    assert c["formal_scored_attempts_used"]==0
    assert all(not v for v in [
        c["physical_target_selected"],c["production_authority_changed"]
    ])
