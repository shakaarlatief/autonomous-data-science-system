"""Regression checks for the bounded D2-coupled X1 engineering experiment.

Original F09/F10 remain distinct controlled D2 cases, and all newly written
carrier declarations are explicit synthetic analogues. These are NOT scored
Research 513 tasks and cannot independently qualify the future V02 kernel.
"""
from copy import deepcopy
import hashlib
import json

import pytest

from experiments.r0_p03_navigation_probe import x1_coupled_mutation_contract_v02 as x1


@pytest.fixture
def pair():
    return x1.scenario_pair()


@pytest.fixture
def authored():
    return x1.author_declarations()


def test_exact_existing_d2_counterfactuals_differ_only_in_source_freshness(pair):
    valid, stale = pair
    a = deepcopy(valid)
    b = deepcopy(stale)
    a.pop("fixture_id")
    b.pop("fixture_id")
    changed = [key for key in a if a[key] != b[key]]
    assert changed == ["source_realization_facts_fresh"]
    assert a["source_realization_facts_fresh"] is True
    assert b["source_realization_facts_fresh"] is False


def test_original_evaluator_gives_different_realization_consequences(pair):
    valid, stale = pair
    a = x1.semantic_projection(valid)
    b = x1.semantic_projection(stale)
    assert a["current_effect_ids"] == b["current_effect_ids"] == ["S1"]
    assert a["successor_initialization"][0]["mode"] == "CARRY_FACTS_FOR_REVALIDATION"
    assert b["successor_initialization"][0]["mode"] == "OPEN_RESET"
    assert b["review_required"] is True
    assert "CARRY_STALE_FACTS" in b["reason_codes"]
    assert a["fixture_digest"] != b["fixture_digest"]


@pytest.mark.parametrize("arm", ["B0", "B1", "B2", "B3", "B4"])
def test_each_adapter_consumes_real_changed_d2_semantics(arm, pair, authored):
    valid, stale = pair
    a = x1.semantic_projection(valid)
    b = x1.semantic_projection(stale)
    left = x1.build_projection(arm, a, x1.CARRIERS, authored)
    right = x1.build_projection(arm, b, x1.CARRIERS, authored)
    assert left["authority_current_effects_read_only"] == ["S1"]
    assert right["authority_current_effects_read_only"] == ["S1"]
    assert left["j2_successor_initialization_from_d2"] != right[
        "j2_successor_initialization_from_d2"
    ]
    assert left["semantic_digest"] != right["semantic_digest"]
    assert left["derived_digest"] != right["derived_digest"]
    assert x1.verify_publication(left, a, x1.CARRIERS)
    with pytest.raises(ValueError, match="STALE_SEMANTIC_PUBLICATION"):
        x1.verify_publication(left, b, x1.CARRIERS)


def test_editorial_link_becomes_review_required_after_d2_replace(pair, authored):
    valid, _ = pair
    before = x1.build_projection(
        "B2", x1.predecessor_projection(valid), x1.CARRIERS, authored,
    )
    after = x1.build_projection(
        "B2", x1.semantic_projection(valid), x1.CARRIERS, authored,
    )
    assert before["source_links"]["carrier:code"]["effect_links"]["P1"] == (
        "CURRENT_EXPERIMENT_EFFECT"
    )
    assert after["source_links"]["carrier:code"]["effect_links"]["P1"] == (
        "REVIEW_REQUIRED"
    )
    assert "P1" not in after["authority_current_effects_read_only"]


def test_physical_path_relocation_preserves_stable_identity(pair, authored):
    valid, _ = pair
    semantic = x1.semantic_projection(valid)
    moved = deepcopy(x1.CARRIERS)
    moved["carrier:code"]["path"] = "synthetic/renamed/authority.py"
    base = x1.build_projection("B1", semantic, x1.CARRIERS, authored)
    renamed = x1.build_projection("B1", semantic, moved, authored)
    assert base == renamed


def test_source_body_change_requires_fresh_source_owner_declaration(pair, authored):
    valid, _ = pair
    semantic = x1.semantic_projection(valid)
    changed = deepcopy(x1.CARRIERS)
    changed["carrier:code"]["body"] += "\nadditional implementation source content"
    with pytest.raises(ValueError, match="STALE_SOURCE_DECLARATION"):
        x1.build_projection("B1", semantic, changed, authored)
    corrected = x1.author_declarations(changed)
    updated = x1.build_projection("B1", semantic, changed, corrected)
    old = x1.build_projection("B1", semantic, x1.CARRIERS, authored)
    assert updated["source_manifest_digest"] != old["source_manifest_digest"]
    with pytest.raises(ValueError, match="STALE_SOURCE_PUBLICATION"):
        x1.verify_publication(old, semantic, changed)


@pytest.mark.parametrize("field,new_value", [
    ("declared_owner", "simulated:unrelated-owner"),
    ("authorship_class", "ACCEPTED_J1"),
    ("subjects", ["subject:unapproved"]),
    ("concerns", ["concern:unapproved"]),
])
def test_unguarded_source_owner_or_vocabulary_drift_is_blocked(
    field, new_value, pair, authored,
):
    valid, _ = pair
    modified = deepcopy(authored)
    modified["carrier:code"][field] = new_value
    with pytest.raises(ValueError):
        x1.build_projection(
            "B1" if field == "subjects" else "B3",
            x1.semantic_projection(valid), x1.CARRIERS, modified,
        )


def test_derived_vector_index_binds_source_and_model_version(pair, authored):
    valid, _ = pair
    semantic = x1.semantic_projection(valid)
    with pytest.raises(ValueError, match="STALE_VECTOR_MODEL_OR_SOURCE_INDEX"):
        x1.build_projection("B4", semantic, x1.CARRIERS, authored,
                            model_manifest=x1.provider_manifest(x1.CARRIERS, "obsolete-model"))
    modified = deepcopy(x1.CARRIERS)
    modified["carrier:tests"]["body"] += "\na new source fact"
    revised = x1.author_declarations(modified)
    old_manifest = x1.provider_manifest(x1.CARRIERS)
    with pytest.raises(ValueError, match="STALE_VECTOR_MODEL_OR_SOURCE_INDEX"):
        x1.build_projection("B4", semantic, modified, revised,
                            model_manifest=old_manifest)
    rebuilt = x1.build_projection("B4", semantic, modified, revised,
                                  model_manifest=x1.provider_manifest(modified))
    assert x1.verify_publication(rebuilt, semantic, modified)


def test_published_orientation_tampering_fails_closed(pair, authored):
    valid, _ = pair
    semantic = x1.semantic_projection(valid)
    original = x1.build_projection("B0", semantic, x1.CARRIERS, authored)
    tampered = {**original, "authority_current_effects_read_only": ["P1"]}
    with pytest.raises(ValueError, match="TAMPERED_DERIVED_PUBLICATION"):
        x1.verify_publication(tampered, semantic, x1.CARRIERS)


def test_metadata_cannot_smuggle_governing_acceptance(pair, authored):
    valid, _ = pair
    metadata = deepcopy(authored)
    metadata["carrier:code"]["accepted_j1"] = True
    with pytest.raises(ValueError, match="Unknown or governing field"):
        x1.build_projection("B2", x1.semantic_projection(valid), x1.CARRIERS, metadata)


def test_not_yet_qualified_unknown_effect_id_is_only_marked_for_review(pair, authored):
    """Explicitly expose a remaining missing historical-ID/typed-edge contract."""
    valid, _ = pair
    unknown = deepcopy(authored)
    unknown["carrier:code"]["about_effects"] = ["NEVER_EXISTED_IN_D2"]
    view = x1.build_projection(
        "B2", x1.semantic_projection(valid), x1.CARRIERS, unknown,
    )
    # This safe but insufficient provisional behavior cannot distinguish an
    # obsolete historical ID from one that never existed in the source world.
    assert view["source_links"]["carrier:code"]["effect_links"] == {
        "NEVER_EXISTED_IN_D2": "REVIEW_REQUIRED"
    }


def test_original_d2_source_fixture_bytes_unchanged():
    original = x1.SOURCE.read_bytes()
    a, b = x1.run(), x1.run()
    assert a == b
    assert original == x1.SOURCE.read_bytes()
    assert a["verified_production_j1_or_j2"] is False
    assert a["v02_kernel_implemented"] is False
    assert a["research_513_formal_score"] is None
    assert a["physical_target_selected"] is False


def test_receipt_reproducible_and_discloses_inconclusive_boundary():
    raw = x1.RESULT.read_bytes()
    receipt = json.loads(raw)
    assert receipt == x1.run()
    assert receipt["status"] == "COUPLED_D2_MUTATION_EVIDENCE_X1_FULL_INCONCLUSIVE"
    assert all(receipt["negative_controls_rejected"].values())
    assert len(receipt["negative_controls_rejected"]) == 9
    assert len(receipt["missing_contracts"]) >= 5
    assert hashlib.sha256(raw).hexdigest() == (
        "2f12617a93368817748f3f8bbbffa06bb8b61ddca1f9d7dcece7f33fc7f55ffe"
    )
