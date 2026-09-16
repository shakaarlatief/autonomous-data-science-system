"""G008 store-owned conditional mutation of transient workstream content.

There is deliberately no unguarded read/write callback pair. The store must
compare the complete expected version and mutate as one indivisible operation
relative to its other writers, using its own conditional-write primitive. This
service validates requests and store attestations; it supplies neither a global
lock nor a repository writer. Store exceptions propagate, never becoming APPLIED.
"""

import hashlib
from typing import Callable

from ..model import (
    ConditionalMutationResult, Diagnostic, DiagnosticSeverity, TransientContent,
    TransientContentVersion, WorkstreamUpdateResult, WorkstreamUpdateStatus,
)
from ..workstreams import WorkstreamValidationError


def _invalid(code: str, message: str, path: str = "") -> None:
    raise WorkstreamValidationError((Diagnostic(code, DiagnosticSeverity.ERROR, path, message),))


def _validate_content(value: TransientContent, path: str) -> None:
    if (not isinstance(value, TransientContent) or not isinstance(value.version, TransientContentVersion)
            or hashlib.sha256(value.content).hexdigest() != value.version.content_digest):
        _invalid("INVALID_UPDATE_MATERIALIZATION", "Materialization requires a transient version matching its exact bytes", path)


def apply_expected_revision_update(
    expected: TransientContentVersion, replacement: TransientContent, *,
    compare_and_swap: Callable[[TransientContentVersion, TransientContent], ConditionalMutationResult],
) -> WorkstreamUpdateResult:
    """Request a conditional mutation and validate its explicit store result.

    An observation taken earlier by a caller is only an expected version. The
    callback must compare it to actual current state AT mutation, and return
    REJECTED_STALE_REVISION without mutation on mismatch. It must return its
    actual before/after materializations, not echo the requested replacement.
    Silent no-ops, inconsistent results and failed operations are never success.
    A dishonest/non-atomic store cannot be made safe by inspecting its response;
    implementing the conditional-mutation contract is the store's responsibility.

    Changed bytes keep the immutable Git seed and a separate transient digest.
    Neither the replacement nor the returned after-version claims a new commit.
    """
    if not isinstance(expected, TransientContentVersion):
        _invalid("INVALID_EXPECTED_VERSION", "Updates require a complete transient expected version")
    path = expected.base_revision.source_path
    _validate_content(replacement, path)
    if replacement.version.base_revision != expected.base_revision:
        _invalid("INVALID_UPDATE_MATERIALIZATION", "A changed copy must retain its exact immutable Git seed", path)
    if replacement.version == expected:
        _invalid("NO_WORKSTREAM_CONTENT_CHANGE", "Replacement must change the expected content version", path)

    result = compare_and_swap(expected, replacement)
    if not isinstance(result, ConditionalMutationResult):
        _invalid("INVALID_CONDITIONAL_MUTATION_RESULT", "Store must explicitly attest its conditional mutation outcome", path)
    _validate_content(result.before, path)
    _validate_content(result.after, path)
    if result.status == WorkstreamUpdateStatus.APPLIED:
        if result.before.version != expected or result.after != replacement:
            _invalid("INVALID_CONDITIONAL_MUTATION_RESULT", "Applied result must attest a matching before-version and actual replacement after-state", path)
    elif result.status == WorkstreamUpdateStatus.REJECTED_STALE_REVISION:
        if result.before.version == expected or result.after != result.before:
            _invalid("INVALID_CONDITIONAL_MUTATION_RESULT", "Stale result must attest a mismatched current version and zero mutation", path)
    else:
        _invalid("INVALID_CONDITIONAL_MUTATION_RESULT", "Store returned an unsupported mutation outcome", path)
    return WorkstreamUpdateResult(result.status, expected, result.before.version, result.after.version,
                                  result.status == WorkstreamUpdateStatus.APPLIED)
