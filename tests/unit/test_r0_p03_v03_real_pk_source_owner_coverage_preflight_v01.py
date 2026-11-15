"""Source-local J2 coverage declaration qualification boundary tests.

These cases check exact source claims and the real observations underlying
them, not a fabricated trust root or retrospective historical G006 owner
testimony. No new governing RELATIONAL J2 or satisfied J3 is admitted.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_source_owner_coverage_preflight_v01 as probe,
)


@pytest.fixture(scope="module")
def result():
    return probe.build()


def test_source_role_is_declared_unqualified_not_implicit():
    declaration = probe.source_declaration()
    assert declaration["fact_class"] == "RELATIONAL_SOURCE_LOCAL_COVERS_PROPOSAL_NOT_YET_QUALIFIED"
    assert declaration["source_owner_declaration_status"] == (
        "EXPLICIT_SOURCE_AUTHORED_PROPOSAL_PENDING_QUALIFICATION"
    )
    assert declaration["qualified_relational_j2"] is False


def test_source_local_declaration_exact_hash_and_lf_bytes():
    raw = probe.SOURCE.read_bytes()
    assert sha256(raw).hexdigest() == probe.SOURCE_SHA256
    assert b"\r\n" not in raw


def test_source_author_claim_does_not_establish_account_identity():
    d = probe.source_declaration()
    assert d["source_owner_claim"] == (
        "EXPOSED_CHATGPT_AUTHOR_OF_EXPERIMENT_SOURCE_CARRIER_AND_MOVE"
    )
    assert d["independently_authenticated_actor"] is False
    assert d["source_owner_assurance"].endswith("_NOT_INDEPENDENTLY_AUTHENTICATED")


def test_declaration_references_exact_git_current_carrier():
    d = probe.source_declaration()
    assert d["natural_owner_carrier"] == probe.transition.REPLACEMENT_PATH
    assert d["natural_owner_carrier_git_commit"] == probe.transition.REPLACEMENT_COMMIT
    assert d["natural_owner_carrier_sha256"] == probe.transition.REPLACEMENT_SHA256
    assert d["predecessor_source_commit"] == probe.transition.INITIAL_COMMIT


def test_carrier_source_scope_does_not_claim_historical_code_ownership():
    d = probe.source_declaration()
    assert d["realizer_id"] == probe.EXPECTED_REALIZER
    assert "NOT_HISTORICAL_G006_G013_CODE_OWNERSHIP" in d["realizer_scope"]


def test_exact_two_accepted_j1_component_ids_are_named():
    d = probe.source_declaration()
    assert tuple(x["id"] for x in d["component_claims"]) == probe.EXPECTED_COMPONENTS
    assert all(x["coverage"] == "FULL" for x in d["component_claims"])
    assert d["accepted_effect_id"] == probe.accepted.EXPECTED_IDS[0]


def test_s0_source_observation_is_real_not_mocked(result):
    assert result["observed_git_transition"]["initial_commit"] == probe.transition.INITIAL_COMMIT
    assert result["observed_git_transition"]["replacement_commit"] == probe.transition.REPLACEMENT_COMMIT
    assert result["source_observable_component_test_passed"] is True


def test_claim_coverage_does_not_promote_unqualified_j2(result):
    claims, = result["source_local_relational_declarations"]
    assert claims["reported_coverage"] == "FULL"
    assert claims["qualified_as_governing_relational_j2"] is False
    assert claims["source_owner_independently_authenticated"] is False
    assert result["qualified_relational_j2_count"] == 0


def test_j3_holds_and_successor_remains_dormant(result):
    assert result["j3"] == "HOLD_OWNER_RELATIONAL_QUALIFICATION"
    assert result["s1_activation"] == "NOT_ACTIVATED"


def test_no_production_or_formal_scoring_authority(result):
    assert result["formal_r0_p03"] == "INCOMPLETE"
    assert result["physical_architecture_selected"] is False


def test_source_claim_does_not_self_assert_completion():
    d = probe.source_declaration()
    assert d["j3_satisfaction_inferred"] is False
    assert "S0_TEST_PASS_IMPLIES_J3_COMPLETE" in d["prohibited_inferences"]
    assert "S1_AUTOMATICALLY_ACTIVATED_OR_SATISFIED" in d["prohibited_inferences"]


def test_tampered_owner_covers_source_hash_rejected(monkeypatch):
    raw = probe.SOURCE.read_bytes()
    class Alternative:
        def read_bytes(self):
            return raw + b"\n"
        def read_text(self, *a):
            return raw.decode("utf8")
    monkeypatch.setattr(probe, "SOURCE", Alternative())
    with pytest.raises(ValueError, match="P03_SOURCE_OWNER_COVERS_SOURCE_DRIFT"):
        probe.source_declaration()


def test_injected_owner_promotion_claim_is_not_admitted(monkeypatch):
    original = json.loads(probe.SOURCE.read_text("utf8"))
    changed = deepcopy(original)
    changed["qualified_relational_j2"] = True
    altered = json.dumps(changed, sort_keys=True, ensure_ascii=False, indent=2).encode() + b"\n"
    class Alternative:
        def read_bytes(self):
            return altered
        def read_text(self, *args):
            return altered.decode("utf8")
    monkeypatch.setattr(probe, "SOURCE", Alternative())
    monkeypatch.setattr(probe, "SOURCE_SHA256", sha256(altered).hexdigest())
    with pytest.raises(ValueError, match="P03_SOURCE_OWNER_RELATIONAL_SCOPE_OR_AUTHORITY_FALSIFIED"):
        probe.source_declaration()


def test_injected_component_id_is_rejected_after_rehash(monkeypatch):
    original = json.loads(probe.SOURCE.read_text("utf8"))
    changed = deepcopy(original)
    changed["component_claims"][1]["id"] = "FORGED_COMPONENT"
    altered = json.dumps(changed, sort_keys=True, ensure_ascii=False, indent=2).encode() + b"\n"
    class Alternative:
        def read_bytes(self):
            return altered
        def read_text(self, *args):
            return altered.decode("utf8")
    monkeypatch.setattr(probe, "SOURCE", Alternative())
    monkeypatch.setattr(probe, "SOURCE_SHA256", sha256(altered).hexdigest())
    with pytest.raises(ValueError, match="P03_COVERS_COMPONENT_OR_SOURCE_EVIDENCE_MISMATCH"):
        probe.source_declaration()


def test_durable_derived_preflight_matches_recomputed_result(result):
    assert json.loads(probe.OUTPUT.read_text("utf8")) == result


def test_no_unsigned_claim_causes_formal_architecture_selection(result):
    assert "QUALIFY_EXPERIMENT_SOURCE_OWNER_AUTHORITY" in result["next"]
    assert result["accepted_new_experiment_only_j1_count"] == 4
