"""Centralized, observable discovery policy; no persistent source inventory."""

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path, PurePosixPath

from ..adapters.fsio import read_worktree_bytes
from ..adapters.gitio import commit_snapshot, read_blob, read_blobs, worktree_snapshot
from ..model import Profile, RepositorySnapshot, SnapshotEntry, SnapshotMode


class PathRole(StrEnum):
    ELIGIBLE_SOURCE = "ELIGIBLE_SOURCE"
    EVIDENCE_FIXTURE = "EVIDENCE_FIXTURE"
    CAPTURE_AREA = "CAPTURE_AREA"
    GENERATED_AREA = "GENERATED_AREA"
    DISALLOWED = "DISALLOWED"


def open_snapshot(root: Path, mode: SnapshotMode, ref: str | None = None) -> RepositorySnapshot:
    """Explicit L3 entry point for the two supported discovery universes."""
    if SnapshotMode(mode) == SnapshotMode.COMMIT_SNAPSHOT:
        if ref is None:
            raise ValueError("COMMIT_SNAPSHOT requires an explicit ref")
        return commit_snapshot(root, ref)
    if ref is not None:
        raise ValueError("WORKTREE_SNAPSHOT cannot bind a ref")
    return worktree_snapshot(root)


@dataclass(frozen=True)
class DiscoveryPolicy:
    """Only documentation/root carriers can own production semantics in this slice.

    Canonical-discovery exclusion does not mean declarations are forbidden.
    Known evidence is never parsed as production declarations. Special artifact
    areas admit their own profiles without joining the production source set.
    Other excluded paths are inspected for unexpected production declarations.
    """
    production_roots: tuple[str, ...] = ("docs",)
    fixture_roots: tuple[str, ...] = (
        "tests/fixtures",
        "docs/research/project_knowledge_architecture_probe_v01",
        "docs/research/project_knowledge_architecture_probe_v02",
        "docs/research/project_knowledge_baselines",
        "docs/research/project_knowledge_candidate_01",
        "docs/research/project_knowledge_candidate_01_current_state_core_v01",
        "docs/research/project_knowledge_candidate_01_current_state_decomposition_v01",
        "docs/research/project_knowledge_candidate_01_q1_q2_cross_provider_v01",
        "docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01",
        "docs/research/project_knowledge_candidate_01_q10_final_v01",
        "docs/research/project_knowledge_candidate_01_q3_real_v01",
        "docs/research/project_knowledge_candidate_01_q4_real_v01",
        "docs/research/project_knowledge_candidate_01_q7_real_v01",
        "docs/research/project_knowledge_candidate_01_q9_migration_v01",
        "docs/research/project_knowledge_candidate_01_real_shadow_v01",
        "docs/research/project_knowledge_candidate_01_shadow_v01",
        "docs/research/project_knowledge_candidate_01_shadow_v02",
        "docs/research/project_knowledge_candidate_01_zero_seed_routing_v01",
        "docs/research/project_knowledge_real_corpus_v01",
    )
    capture_root: str = "docs/project_knowledge/captures"
    open_capture_root: str = "docs/project_knowledge/captures/open"
    historical_capture_root: str = "docs/project_knowledge/captures/historical"
    generated_root: str = "docs/project_knowledge/generated"
    manifest_root: str = "docs/project_knowledge/generated/manifests"
    excluded_components: frozenset[str] = frozenset({
        "fixtures", "generated", "results", "tmp", "temp", ".tmp",
        "__pycache__", "node_modules", ".ads-private", ".git",
    })

    def supports(self, path: str) -> bool:
        return PurePosixPath(path).suffix.lower() in {".md", ".json"}

    @staticmethod
    def _under(path: str, root: str) -> bool:
        return path == root or path.startswith(root + "/")

    def classify(self, path: str) -> PathRole:
        if any(self._under(path, root) for root in self.fixture_roots):
            return PathRole.EVIDENCE_FIXTURE
        if self._under(path, self.open_capture_root) or self._under(path, self.historical_capture_root):
            return PathRole.CAPTURE_AREA
        if self._under(path, self.capture_root):
            return PathRole.DISALLOWED
        if self._under(path, self.generated_root):
            return PathRole.GENERATED_AREA
        parts = PurePosixPath(path).parts
        if any(part in self.excluded_components for part in parts):
            return PathRole.DISALLOWED
        if len(parts) > 1 and not any(path.startswith(root + "/") for root in self.production_roots):
            return PathRole.DISALLOWED
        return PathRole.ELIGIBLE_SOURCE

    def is_excluded(self, path: str) -> bool:
        """Excluded from production source discovery, not necessarily forbidden."""
        return self.classify(path) != PathRole.ELIGIBLE_SOURCE

    def admits_profile(self, path: str, profile: Profile) -> bool:
        role = self.classify(path)
        if role == PathRole.ELIGIBLE_SOURCE:
            return profile != Profile.CAPTURE
        if role == PathRole.CAPTURE_AREA:
            return profile == Profile.CAPTURE
        if role == PathRole.GENERATED_AREA:
            return self._under(path, self.manifest_root) and profile == Profile.DERIVED_VIEW_MANIFEST
        return False

    def bounded_root(self, path: str) -> str:
        parts = PurePosixPath(path).parts
        if len(parts) == 1:
            return "<repository-root>"
        if parts[0] in self.production_roots:
            return "/".join(parts[:2]) if len(parts) > 2 else parts[0]
        return "<non-production>"


def read_snapshot_blobs(snapshot: RepositorySnapshot, policy: DiscoveryPolicy) -> dict[str, bytes]:
    """Batch only supported non-fixture regular carriers; modes remain checked on read."""
    if snapshot.mode != SnapshotMode.COMMIT_SNAPSHOT:
        return {}
    return read_blobs(snapshot.root, tuple(
        entry for entry in snapshot.entries
        if policy.supports(entry.path) and policy.classify(entry.path) != PathRole.EVIDENCE_FIXTURE
        and entry.git_mode in {"100644", "100755"}
    ))


def read_entry(snapshot: RepositorySnapshot, entry: SnapshotEntry, blobs: dict[str, bytes] | None = None) -> bytes:
    if snapshot.mode == SnapshotMode.COMMIT_SNAPSHOT:
        if blobs is not None and entry.git_mode in {"100644", "100755"}:
            # Indexing is deliberate: a missing batch object is never replaced
            # with worktree bytes or silently omitted.
            return blobs[entry.blob_id]
        return read_blob(snapshot.root, entry)
    return read_worktree_bytes(snapshot.root, entry.path)
