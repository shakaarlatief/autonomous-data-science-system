"""L2: revision checks over supplied exact blob bytes, with no repository I/O."""

import hashlib

from .model import Diagnostic, DiagnosticSeverity, SnapshotMode, SourceRevision


def validate_durable_evidence(mode: SnapshotMode, carrier_path: str = "") -> tuple[Diagnostic, ...]:
    if SnapshotMode(mode) != SnapshotMode.COMMIT_SNAPSHOT:
        return (Diagnostic(
            "NON_COMMITTED_EVIDENCE", DiagnosticSeverity.ERROR, carrier_path,
            "WORKTREE_SNAPSHOT is NON_COMMITTED and cannot bind durable repository authority.",
            remediation="Revalidate exact committed Git blobs using COMMIT_SNAPSHOT.",
        ),)
    return ()


def verify_blob_digest(revision: SourceRevision, blob_bytes: bytes) -> tuple[Diagnostic, ...]:
    if hashlib.sha256(blob_bytes).hexdigest() != revision.content_digest:
        return (Diagnostic(
            "SOURCE_DIGEST_MISMATCH", DiagnosticSeverity.ERROR, revision.source_path,
            "Exact Git blob bytes do not match the declared SHA-256 digest.",
        ),)
    return ()
