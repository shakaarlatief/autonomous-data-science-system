"""W1 preregistration and evidence-bound mechanical freeze regression tests.

The published W1 rule is a *prior* commit. These tests do not change the
source selection to improve any retrieval rank and never inspect primary
scored tasks, protected references or heldout identities.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path

import pytest

from experiments.r0_p03_navigation_probe import w1_freeze_v01 as w


@pytest.fixture(scope="module")
def artefacts():
    return {
        key: (path.read_bytes(), json.loads(path.read_text("utf8")))
        for key,path in w.OUTPUTS.items()
    }


@pytest.fixture(scope="module")
def build(artefacts):
    return artefacts["manifest"][1]["source_records"]


@pytest.fixture(scope="module")
def common(artefacts):
    return {
        arm:w.W1CommonRuntime(arm,{
            k:v[0] for k,v in artefacts.items()
        }) for arm in ("B0","B1","B2","B3","B4")
    }


def test_rule_was_committed_as_separate_ancestor_before_generator():
    contract=w.check_rule()
    assert contract["rule_git_commit"]==w.RULE_COMMIT
    assert contract["source_git_revision"]==w.PIN
    assert len(contract["rule_sha256"])==64
    # The implementation may run while HEAD still points at the published
    # rule-only commit; code and results are intentionally uncommitted until
    # they have passed validation.
    assert w.RULE_COMMIT != w.PIN


def test_exact_60_build_seven_role_strata_and_no_heldout(artefacts,build):
    manifest=artefacts["manifest"][1]
    assert len(build)==60==manifest["build_source_count"]
    assert len({r["source_path"] for r in build})==60
    assert manifest["heldout_draw_status"]=="NOT_DRAWN_PROHIBITED_UNTIL_POST_C_ARM"
    assert manifest["heldout_future_target"]==20
    assert manifest["primary_gold"] is None and manifest["score"] is None
    assert manifest["historical_65_source_research217_world_separate"]
    assert Counter(r["stratum"] for r in build)==Counter({
        k:v[0] for k,v in w.QUOTAS.items()
    })
    assert all(r["build"] is True for r in build)


def test_seed_anchors_all_present_and_not_counted_twice(build):
    bypath={r["source_path"]:r for r in build}
    assert set(w.SEEDS).issubset(bypath)
    assert all(bypath[p]["selection_class"]=="MANDATORY_SEED" for p in w.SEEDS)
    assert len(set(w.SEEDS))==10


def test_sources_all_reached_by_preregistered_citation_graph(build):
    assert all(0 <= r["bfs_distance"] <= 4 for r in build)
    assert not any(r["selection_class"]=="DETERMINISTIC_DISCONNECTED_STRATUM_BACKFILL"
                   for r in build)
    assert all(
        r["citation_predecessor_not_semantic_dependency"] is None
        if r["source_path"] in w.SEEDS
        else r["citation_predecessor_not_semantic_dependency"] is not None
        for r in build
    )


def test_each_original_blob_exact_sha_oid_and_length(build,common):
    first=common["B0"]
    for row in build:
        original=first.read(row["source_path"])["content"].encode("utf8")
        assert w.sha1git(original)==row["git_blob_oid"]
        assert sha256(original).hexdigest()==row["source_sha256"]
        assert len(original)==row["byte_count"]
        assert row["git_source_ref"]==w.PIN
        assert row["accepted_j1_from_source_carrier"] is False
        assert row["accepted_natural_owner_j2_from_path"] is False
        assert w.stratum(row["source_path"])==row["stratum"]


def test_zero_w1_excluded_source_paths(artefacts,build):
    exclusion=artefacts["exclusions"][1]
    omitted={r["source_path"] for r in exclusion["excluded_path_records"]}
    assert not (omitted & {r["source_path"] for r in build})
    assert exclusion["heldout_identity_exposed"] is False
    assert all(r["reason"] for r in exclusion["excluded_path_records"])
    for row in build:
        body=w.git(["show",f"{w.PIN}:{row['source_path']}"]).decode("utf8")
        assert w.exclude_reason(row["source_path"],body) is None


def test_future_heldout_quota_can_be_met_without_drawing_now(artefacts):
    manifest=artefacts["manifest"][1]
    for group,(build_n,future_heldout_n) in w.QUOTAS.items():
        row=manifest["per_stratum"][group]
        assert row["build_count"]==build_n
        assert row["future_heldout_capacity"]>=future_heldout_n
        assert row["future_heldout_quota"]==future_heldout_n
    assert "C_arm_full_40_hex" in manifest["predeclared_heldout_rule"]


def test_no_source_claim_promoted_to_accepted_effect(artefacts):
    sub=artefacts["substrate"][1]
    claims=sub["source_reported_records"]
    assert claims
    assert set(r["evidence_class"] for r in claims)<={
        "SOURCE_REPORTED","OBSERVABLE_GIT_BLOB","DEFINITION_ONLY_NOT_EXECUTION"
    }
    assert not any(r["accepted_governing_effect"] or r["qualified_j2_relation"]
                   for r in claims)
    assert sub["no_production_acceptance_or_realization"]
    assert sub["derived_orientation"]["status"]=="GENERATED_NON_GOVERNING"
    assert sub["derived_orientation"]["unknowns"]=="SOURCE_BOUNDED_UNKNOWN"


def test_original_line_and_statement_fidelity(artefacts,common):
    originals=common["B0"].contents
    sub=artefacts["substrate"][1]
    for r in sub["source_reported_records"]:
        if r["evidence_class"]=="OBSERVABLE_GIT_BLOB":
            assert r["source_sha256"]==sha256(
                originals[r["source_path"]].encode("utf8")
            ).hexdigest()
            continue
        lines=originals[r["source_path"]].splitlines()
        content=lines[r["source_line"]-1]
        assert r["value_exact_source_line"]==content
        assert r["source_line_sha256"]==sha256(content.encode("utf8")).hexdigest()
        assert r["source_ref"]==w.PIN
        assert r["git_blob_oid"]==common["B0"].rows[r["source_path"]]["git_blob_oid"]


def test_only_experimental_s1_core_is_accepted(artefacts):
    s=artefacts["substrate"][1]
    accepted=s["only_accepted_experiment_core"]
    assert accepted["evidence_class"]=="ACCEPTED_EXPERIMENT_ONLY_WEAK_ASSURANCE"
    assert len(accepted["accepted_j1_effects"])==4
    assert accepted["qualifying_j2_count"]==1
    assert accepted["production_authority"] is False
    assert accepted["independent_actor_assurance"] is False
    assert accepted["source_evidence_outside_build_s1_not_counted_as_carrier"]
    assert accepted["evidence_sha256"]==(
        "1b31365160e29b902d578222a8dc39e15c55b49e0e592448baeada13284b4341"
    )


@pytest.mark.parametrize("arm",["B0","B1","B2","B3","B4"])
def test_identical_full_source_read_list_search_semantic_connector(common,arm):
    instance=common[arm]
    assert instance.list_sources()==common["B0"].list_sources()
    assert instance.semantics()==common["B0"].semantics()
    assert instance.read("docs/DECISIONS.md")==common["B0"].read("docs/DECISIONS.md")
    assert instance.search("project knowledge",limit=4)==common["B0"].search(
        "project knowledge",limit=4
    )
    assert instance.common_digest()==common["B0"].common_digest()


@pytest.mark.parametrize("query,limit",[
    ("",5),(" ",5),("valid",0),("valid",21),("valid",True),
    ("x"*81,5),
])
def test_reader_rejects_blank_and_invalid_query_budget(common,query,limit):
    with pytest.raises(ValueError,match="W1_QUERY_LIMIT|W1_RESULT_BUDGET"):
        common["B0"].search(query,limit=limit)


def test_reader_rejects_unselected_source_and_unknown_arm(common,artefacts):
    with pytest.raises(ValueError,match="W1_SOURCE_NOT_IN_FROZEN_BUILD"):
        common["B0"].read("docs/research/697_r0_p03_finite_fresh_reviewer_route_failure_and_formal_readiness_hold.md")
    with pytest.raises(ValueError,match="W1_UNKNOWN_ARM_LABEL"):
        w.W1CommonRuntime("Z0",{k:v[0] for k,v in artefacts.items()})


def test_generated_index_not_promoted_to_governing_authority(artefacts,build):
    generated=[r for r in build if "/generated/" in r["source_path"]]
    assert generated
    for r in generated:
        assert r["accepted_j1_from_source_carrier"] is False
        assert r["accepted_natural_owner_j2_from_path"] is False
    source_r=artefacts["substrate"][1]["source_reported_records"]
    for r in source_r:
        if "/generated/" in r["source_path"]:
            assert r["evidence_class"]!="ACCEPTED_EXPERIMENT_ONLY_WEAK_ASSURANCE"


def test_excluded_probe_and_historical_w5_heading_examples():
    assert w.exclude_reason("docs/research/696_r0_p03_example.md","# Some source") is not None
    assert w.exclude_reason("docs/possible.md","# W5 subject architecture\nBody") == (
        "H1_PROBE_OR_NAVIGATION_EXPOSURE"
    )
    assert w.exclude_reason("docs/possible.md","# Normal\n**Scope:** navigation probe") == (
        "SCOPE_PROBE_OR_NAVIGATION_EXPOSURE"
    )
    assert w.exclude_reason("docs/possible.md","# Normal\nSome research P03 in body") is None


def test_rule_infeasible_does_not_silently_refill_missing_stratum(artefacts):
    rows={r["source_path"]:{
        "source_path":r["source_path"],"stratum":r["stratum"],
        "git_blob_oid":r["git_blob_oid"],
    } for r in artefacts["manifest"][1]["source_records"]}
    with pytest.raises(ValueError,match="W1_RULE_INFEASIBLE:STRATUM_CAPACITY"):
        w.select_build(rows, {k:0 for k in rows},{})


def test_manifests_reconstruct_byte_identically_and_are_create_only(artefacts):
    fresh=w.compute()
    assert set(fresh)==set(artefacts)
    for key,(raw,_) in artefacts.items():
        assert fresh[key]==raw
    assert w.compute()==fresh


def test_w1_outputs_contain_no_hidden_gold_or_scored_runs(artefacts):
    manifest=artefacts["manifest"][1]
    substrate=artefacts["substrate"][1]
    assert manifest["classification"]=="WORLD_W1_BUILD_FROZEN_HELDOUT_RULE_FROZEN_NOT_DRAWN"
    assert manifest["primary_gold"] is None and manifest["score"] is None
    assert "scores" not in substrate and "hidden_gold" not in substrate
    assert manifest["heldout_draw_status"].startswith("NOT_DRAWN")
    assert all(r["evidence_class"] in w.ALLOWED_CLASSES
               for r in substrate["source_reported_records"])
