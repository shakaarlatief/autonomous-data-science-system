"""G011 capture non-authority and prospective promotion qualification."""

from dataclasses import FrozenInstanceError

import pytest

from tools.project_knowledge.authority import resolve_authority
from tools.project_knowledge.capture import CaptureValidationError, build_promotion_plan, capture_record
from tools.project_knowledge.model import (
    AuthorityClass,
    AuthorityQuery,
    AuthorityStatus,
    GovernedSource,
    HashBasis,
    Profile,
    PromotionDisposition,
    PromotionUnitDisposition,
    RawDeclaration,
    Scope,
    SemanticId,
    SnapshotMode,
    SourceRevision,
)


COMMIT = SnapshotMode.COMMIT_SNAPSHOT
LOCAL = SnapshotMode.WORKTREE_SNAPSHOT


def revision(path="docs/knowledge.md", digit="0"):
    return SourceRevision(
        path,
        "a" * 40,
        "sha256",
        HashBasis.GIT_BLOB_BYTES_AT_COMMIT,
        digit * 64,
    )


def canonical(sid="KNOWLEDGE:ONE", *, path="docs/knowledge.md", rev=None):
    current = rev or revision(path)
    data = {
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "accepted-knowledge",
        "authority_class": "canonical",
    }
    if sid is not None:
        data["semantic_id"] = sid
    raw = RawDeclaration(data)
    return GovernedSource(
        path,
        Profile.SEMANTIC_SOURCE,
        AuthorityClass.CANONICAL,
        "accepted-knowledge",
        raw,
        COMMIT,
        semantic_id=SemanticId(sid) if sid is not None else None,
        revision=current,
    )


def captured(*, provenance=(), source_references=(), summary="Unreviewed observation",
             path="docs/project_knowledge/captures/open/capture-1.json"):
    raw = RawDeclaration({
        "schema_version": "1",
        "profile": "capture.v1",
        "kind": "capture",
        "authority_class": "capture",
        "summary": summary,
        **({"provenance": list(provenance)} if provenance else {}),
        **({"source_references": list(source_references)} if source_references else {}),
    })
    source = GovernedSource(
        path,
        Profile.CAPTURE,
        AuthorityClass.CAPTURE,
        "capture",
        raw,
        LOCAL,
    )
    return capture_record(source)


def materialized(sid="UNIT:A"):
    return PromotionUnitDisposition(
        SemanticId(sid),
        PromotionDisposition.MATERIALIZED_IN_CANONICAL_SOURCE,
    )


def latent(sid="UNIT:B", refs=("docs/source.md",)):
    return PromotionUnitDisposition(
        SemanticId(sid),
        PromotionDisposition.INTENTIONALLY_LATENT_WITH_RECOVERABLE_SOURCE,
        refs,
    )


def rejected(sid="UNIT:C", rationale="Reviewed and rejected as unsupported"):
    return PromotionUnitDisposition(
        SemanticId(sid),
        PromotionDisposition.REJECTED_WITH_REVIEWED_RATIONALE,
        reviewed_rationale=rationale,
    )


def plan(capture=None, target=None, *, required=None, dispositions=None, **changes):
    capture = capture or captured(provenance=("docs/evidence.md",))
    target = target or canonical()
    required = required or (SemanticId("UNIT:A"),)
    dispositions = dispositions or (materialized(),)
    values = {
        "target_semantic_id": target.semantic_id,
        "expected_target_revision": target.revision,
        "review_disposition": "ACCEPTED_FOR_PROMOTION",
        "accepted_understanding": "Accepted synthesis that belongs in the canonical source.",
        "required_semantic_units": required,
        "unit_dispositions": dispositions,
    }
    values.update(changes)
    return build_promotion_plan(capture, (target,), **values)


def test_capture_record_preserves_both_provenance_forms_without_authority():
    item = captured(
        provenance=("docs/z.md", "docs/a.md"),
        source_references=("docs/a.md", "docs/b.md"),
    )
    assert item.source.authority_class == AuthorityClass.CAPTURE
    assert item.provenance == ("docs/a.md", "docs/z.md")
    assert item.source_references == ("docs/a.md", "docs/b.md")
    assert item.provenance_chain == ("docs/a.md", "docs/b.md", "docs/z.md")


def test_capture_value_is_immutable():
    item = captured(provenance=("docs/evidence.md",))
    with pytest.raises(FrozenInstanceError):
        item.summary = "mutated"


def test_capture_record_requires_designated_capture_area():
    with pytest.raises(CaptureValidationError) as error:
        captured(path="docs/not-a-capture-area.json")
    assert error.value.code == "INVALID_CAPTURE_RECORD"


def test_capture_without_provenance_is_valid_capture_but_not_promotable():
    item = captured()
    assert item.source.authority_class == AuthorityClass.CAPTURE
    with pytest.raises(CaptureValidationError) as error:
        plan(item)
    assert error.value.code == "MISSING_CAPTURE_PROVENANCE"


def test_historical_capture_cannot_reenter_promotion_planning():
    item = captured(
        provenance=("docs/evidence.md",),
        path="docs/project_knowledge/captures/historical/capture-1.json",
    )
    with pytest.raises(CaptureValidationError) as error:
        plan(item)
    assert error.value.code == "CAPTURE_NOT_OPEN"


def test_capture_never_satisfies_authority_resolution():
    item = captured(provenance=("docs/evidence.md",))
    result = resolve_authority(
        AuthorityQuery("act", "subject", Scope({}), "consequential", require_freshness=False),
        (item.source,),
        snapshot_mode=LOCAL,
    )
    assert result.status == AuthorityStatus.MISSING_REQUIRED_AUTHORITY
    assert {d.code for d in result.diagnostics} == {"NO_CANONICAL_CANDIDATES"}


def test_valid_plan_binds_review_target_revision_provenance_and_complete_dispositions():
    item = captured(
        provenance=("docs/candidate.md",),
        source_references=("docs/evidence.md",),
    )
    target = canonical()
    units = (SemanticId("UNIT:C"), SemanticId("UNIT:A"), SemanticId("UNIT:B"))
    dispositions = (
        rejected(),
        materialized(),
        latent(),
    )
    result = plan(item, target, required=units, dispositions=dispositions)
    assert result.review_disposition == "ACCEPTED_FOR_PROMOTION"
    assert result.target_source is target
    assert result.expected_target_revision == target.revision
    assert tuple(s.value for s in result.required_semantic_units) == ("UNIT:A", "UNIT:B", "UNIT:C")
    assert tuple(d.semantic_unit_id.value for d in result.unit_dispositions) == ("UNIT:A", "UNIT:B", "UNIT:C")
    assert result.capture_provenance == ("docs/candidate.md", "docs/evidence.md")
    assert result.capture.source.authority_class == AuthorityClass.CAPTURE


def test_promotion_target_can_use_exact_carrier_without_durable_semantic_identity():
    target = canonical(None, path="docs/no-id.md")
    result = plan(target=target, target_carrier_path=target.carrier_path)
    assert result.target_source is target
    assert result.target_source.semantic_id is None
    assert result.expected_target_revision == target.revision


def test_promotion_target_requires_identity_or_exact_carrier():
    target = canonical(None, path="docs/no-id.md")
    with pytest.raises(CaptureValidationError) as error:
        plan(target=target)
    assert error.value.code == "INVALID_PROMOTION_TARGET"


def test_promotion_target_rejects_invalid_carrier_path():
    target = canonical(None, path="docs/no-id.md")
    with pytest.raises(CaptureValidationError) as error:
        plan(target=target, target_carrier_path="../escape")
    assert error.value.code == "INVALID_PROMOTION_TARGET"


def test_identity_and_carrier_target_selectors_must_resolve_the_same_owner():
    target = canonical()
    with pytest.raises(CaptureValidationError) as error:
        plan(target=target, target_carrier_path="docs/other.md")
    assert error.value.code == "PROMOTION_TARGET_CARDINALITY"


@pytest.mark.parametrize("review", ["", "REJECTED", "accept"])
def test_promotion_requires_explicit_accepted_review_disposition(review):
    with pytest.raises(CaptureValidationError) as error:
        plan(review_disposition=review)
    assert error.value.code == "INVALID_PROMOTION_PLAN"


def test_promotion_requires_explicit_accepted_understanding():
    with pytest.raises(CaptureValidationError) as error:
        plan(accepted_understanding="   ")
    assert error.value.code == "INVALID_PROMOTION_PLAN"


@pytest.mark.parametrize("targets", [(), (canonical(), canonical(path="docs/other.md", rev=revision("docs/other.md", "1")))])
def test_promotion_target_identity_requires_exactly_one_canonical_owner(targets):
    item = captured(provenance=("docs/evidence.md",))
    with pytest.raises(CaptureValidationError) as error:
        build_promotion_plan(
            item,
            targets,
            target_semantic_id=SemanticId("KNOWLEDGE:ONE"),
            expected_target_revision=revision(),
            review_disposition="ACCEPTED_FOR_PROMOTION",
            accepted_understanding="Accepted",
            required_semantic_units=(SemanticId("UNIT:A"),),
            unit_dispositions=(materialized(),),
        )
    assert error.value.code == "PROMOTION_TARGET_CARDINALITY"


def test_promotion_rejects_stale_target_revision():
    target = canonical()
    with pytest.raises(CaptureValidationError) as error:
        plan(target=target, expected_target_revision=revision(target.carrier_path, "1"))
    assert error.value.code == "STALE_PROMOTION_TARGET"


def test_promotion_rejects_revision_bound_to_a_different_carrier():
    target = canonical(rev=revision("docs/different.md"))
    with pytest.raises(CaptureValidationError) as error:
        plan(target=target)
    assert error.value.code == "STALE_PROMOTION_TARGET"


def test_promotion_requires_exactly_one_disposition_for_every_required_unit():
    with pytest.raises(CaptureValidationError) as error:
        plan(
            required=(SemanticId("UNIT:A"), SemanticId("UNIT:B")),
            dispositions=(materialized(),),
        )
    assert error.value.code == "INVALID_PROMOTION_PLAN"


def test_promotion_rejects_duplicate_required_semantic_units():
    with pytest.raises(CaptureValidationError) as error:
        plan(
            required=(SemanticId("UNIT:A"), SemanticId("UNIT:A")),
            dispositions=(materialized(), materialized()),
        )
    assert error.value.code == "INVALID_PROMOTION_PLAN"


def test_promotion_rejects_untyped_required_semantic_units_cleanly():
    with pytest.raises(CaptureValidationError) as error:
        plan(required=("UNIT:A",), dispositions=(materialized(),))
    assert error.value.code == "INVALID_PROMOTION_PLAN"


def test_latent_disposition_requires_recoverable_source():
    with pytest.raises(ValueError, match="recoverable source"):
        latent(refs=())


def test_rejected_disposition_requires_reviewed_rationale():
    with pytest.raises(ValueError, match="reviewed rationale"):
        rejected(rationale="")


def test_accepted_promotion_must_materialize_at_least_one_unit():
    with pytest.raises(CaptureValidationError) as error:
        plan(
            required=(SemanticId("UNIT:B"), SemanticId("UNIT:C")),
            dispositions=(latent(), rejected()),
        )
    assert error.value.code == "INVALID_PROMOTION_PLAN"


def test_plan_is_representation_order_independent():
    item = captured(
        provenance=("docs/z.md", "docs/a.md"),
        source_references=("docs/b.md",),
    )
    target = canonical()
    left = plan(
        item,
        target,
        required=(SemanticId("UNIT:B"), SemanticId("UNIT:A")),
        dispositions=(latent(), materialized()),
    )
    right = plan(
        item,
        target,
        required=(SemanticId("UNIT:A"), SemanticId("UNIT:B")),
        dispositions=(materialized(), latent()),
    )
    assert left == right


def test_promotion_planning_does_not_mutate_capture_or_target():
    item = captured(provenance=("docs/evidence.md",))
    target = canonical()
    before_capture = item
    before_target = target
    result = plan(item, target)
    assert result.capture is before_capture
    assert result.target_source is before_target
    assert item.source.authority_class == AuthorityClass.CAPTURE
    assert target.authority_class == AuthorityClass.CANONICAL
