"""G011: pure capture and prospective promotion semantics over explicit inputs.

Captures are never authority. This module performs no discovery, I/O, writes or
promotion. It validates a reviewed prospective plan against one exact canonical
target revision and complete semantic-unit dispositions.
"""

from .model import (
    OPEN_CAPTURE_ROOT, AuthorityClass, CaptureRecord, GovernedSource, PromotionPlan,
    SemanticId, SourceRevision, SubstrateError, validate_source_path,
)


class CaptureValidationError(SubstrateError):
    pass


def capture_record(source: GovernedSource) -> CaptureRecord:
    """Project a validated capture source without granting it canonical status."""
    data = source.declaration.fields
    try:
        return CaptureRecord(
            source,
            data.get("summary"),
            tuple(data.get("provenance", ())),
            tuple(data.get("source_references", ())),
        )
    except (TypeError, ValueError) as error:
        raise CaptureValidationError("INVALID_CAPTURE_RECORD", str(error)) from error


def build_promotion_plan(
    capture: CaptureRecord,
    canonical_targets,
    *,
    target_semantic_id: SemanticId | None = None,
    target_carrier_path: str | None = None,
    expected_target_revision: SourceRevision,
    review_disposition: str,
    accepted_understanding: str,
    required_semantic_units,
    unit_dispositions,
) -> PromotionPlan:
    """Build a prospective, non-mutating plan after explicit review.

    Target resolution uses an explicitly authored semantic identity and/or an
    exact current carrier path. This preserves selective identity: a canonical
    source that does not need durable semantic identity can still be the natural
    promotion target. Carrier ordering and retrieval rank have no role. Exactly
    one current canonical owner must match and its exact committed revision must
    equal the caller's expected revision. Explicit capture provenance/source
    references form the provenance chain; they do not become authority through
    this operation.
    """
    if not isinstance(capture, CaptureRecord):
        raise CaptureValidationError("INVALID_CAPTURE_RECORD", "Promotion requires a validated CaptureRecord")
    if capture.source.authority_class != AuthorityClass.CAPTURE:
        raise CaptureValidationError(
            "CAPTURE_AUTHORITY_VIOLATION",
            "Capture material is non-authoritative by definition",
        )
    if not capture.source.carrier_path.startswith(OPEN_CAPTURE_ROOT + "/"):
        raise CaptureValidationError(
            "CAPTURE_NOT_OPEN",
            "Only a capture in the designated open-capture area can enter promotion planning",
        )
    if target_semantic_id is None and target_carrier_path is None:
        raise CaptureValidationError(
            "INVALID_PROMOTION_TARGET",
            "Promotion target requires an authored semantic identity and/or an exact carrier path",
        )
    if target_semantic_id is not None and not isinstance(target_semantic_id, SemanticId):
        raise CaptureValidationError("INVALID_PROMOTION_TARGET", "Target identity must be an authored SemanticId")
    if target_carrier_path is not None:
        try:
            validate_source_path(target_carrier_path)
        except ValueError as error:
            raise CaptureValidationError("INVALID_PROMOTION_TARGET", str(error)) from error
    targets = tuple(
        source
        for source in canonical_targets
        if source.authority_class == AuthorityClass.CANONICAL
        and (target_semantic_id is None or source.semantic_id == target_semantic_id)
        and (target_carrier_path is None or source.carrier_path == target_carrier_path)
    )
    if len(targets) != 1:
        raise CaptureValidationError(
            "PROMOTION_TARGET_CARDINALITY",
            "Promotion requires exactly one natural canonical target owner",
        )
    target = targets[0]
    if (target.revision is None or target.revision != expected_target_revision
            or target.revision.source_path != target.carrier_path):
        raise CaptureValidationError(
            "STALE_PROMOTION_TARGET",
            "Promotion plan must bind the exact current canonical target revision and carrier",
        )
    provenance = capture.provenance_chain
    if not provenance:
        raise CaptureValidationError(
            "MISSING_CAPTURE_PROVENANCE",
            "Reviewed promotion requires capture/candidate provenance",
        )
    try:
        return PromotionPlan(
            capture,
            review_disposition,
            accepted_understanding,
            target,
            expected_target_revision,
            tuple(required_semantic_units),
            tuple(unit_dispositions),
            provenance,
        )
    except (TypeError, ValueError) as error:
        raise CaptureValidationError("INVALID_PROMOTION_PLAN", str(error)) from error
