"""Local immutable content-addressed source-artifact storage."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import shutil
import tempfile
from typing import BinaryIO, Iterator

from ads_system.domain.source_universe import StagedSourceArtifact, StoredSourceArtifact

_BUFFER_SIZE = 1024 * 1024


class SourceArtifactIntegrityError(RuntimeError):
    """Raised when bytes in the immutable artifact store fail verification."""


class LocalSourceArtifactStore:
    """Filesystem implementation of Specification 023's SourceArtifactStore port."""

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root).expanduser().resolve()
        self.objects_root = self.root / "objects" / "sha256"
        self.staging_root = self.root / "staging"
        self.derived_root = self.root / "derived"
        for path in (self.objects_root, self.staging_root, self.derived_root):
            path.mkdir(parents=True, exist_ok=True)

    def object_path(self, sha256: str) -> Path:
        self._validate_digest(sha256)
        return self.objects_root / sha256[:2] / sha256[2:]

    def stage_from_path(self, source_path: str | Path) -> StagedSourceArtifact:
        source = Path(source_path)
        if not source.is_file():
            raise FileNotFoundError(source)
        digest = hashlib.sha256()
        byte_size = 0
        fd, staging_name = tempfile.mkstemp(prefix="source-", suffix=".staged", dir=self.staging_root)
        staging_path = Path(staging_name)
        try:
            with source.open("rb") as src, os.fdopen(fd, "wb") as dst:
                while True:
                    block = src.read(_BUFFER_SIZE)
                    if not block:
                        break
                    dst.write(block)
                    digest.update(block)
                    byte_size += len(block)
                dst.flush()
                os.fsync(dst.fileno())
            return StagedSourceArtifact(staging_path, digest.hexdigest(), byte_size)
        except BaseException:
            try:
                staging_path.unlink(missing_ok=True)
            finally:
                raise

    def commit(self, staged: StagedSourceArtifact) -> StoredSourceArtifact:
        final_path = self.object_path(staged.sha256)
        final_path.parent.mkdir(parents=True, exist_ok=True)
        if final_path.exists():
            # The incoming staging copy is redundant either way once a final
            # object already occupies this content-addressed path. It must
            # not survive a failed verification of that pre-existing object,
            # but the pre-existing object itself is never touched here: a
            # corrupt existing object stays visible for explicit investigation.
            try:
                self._verify_path(final_path, staged.sha256, staged.byte_size)
            finally:
                staged.staging_path.unlink(missing_ok=True)
            return StoredSourceArtifact(staged.sha256, staged.byte_size, True)
        replaced = False
        try:
            os.replace(staged.staging_path, final_path)
            replaced = True
            self._fsync_directory(final_path.parent)
            self._verify_path(final_path, staged.sha256, staged.byte_size)
        except SourceArtifactIntegrityError:
            # This invocation just placed final_path itself and proved it bad:
            # remove the known-bad object so a legitimate retry is not blocked.
            # A failure here is never a pre-existing object and never caused by
            # an unrelated fsync/OS error, so this narrow removal is safe.
            if replaced:
                final_path.unlink(missing_ok=True)
            raise
        except BaseException:
            staged.staging_path.unlink(missing_ok=True)
            raise
        return StoredSourceArtifact(staged.sha256, staged.byte_size, False)

    def put_path(self, source_path: str | Path) -> StoredSourceArtifact:
        return self.commit(self.stage_from_path(source_path))

    def open(self, sha256: str) -> BinaryIO:
        return self.object_path(sha256).open("rb")

    def exists(self, sha256: str) -> bool:
        return self.object_path(sha256).is_file()

    def verify(self, sha256: str, expected_size: int) -> bool:
        path = self.object_path(sha256)
        if not path.is_file():
            return False
        try:
            self._verify_path(path, sha256, expected_size)
        except SourceArtifactIntegrityError:
            return False
        return True

    def iter_objects(self) -> Iterator[tuple[str, int]]:
        if not self.objects_root.exists():
            return
        for prefix in sorted(self.objects_root.iterdir(), key=lambda p: p.name):
            if not prefix.is_dir() or len(prefix.name) != 2:
                continue
            for object_path in sorted(prefix.iterdir(), key=lambda p: p.name):
                if not object_path.is_file():
                    continue
                digest = prefix.name + object_path.name
                if len(digest) == 64:
                    yield digest, object_path.stat().st_size

    def copy_verified_object_to(self, sha256: str, expected_size: int, destination: Path) -> None:
        source = self.object_path(sha256)
        self._verify_path(source, sha256, expected_size)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        self._verify_path(destination, sha256, expected_size)

    @staticmethod
    def _validate_digest(sha256: str) -> None:
        if len(sha256) != 64 or any(ch not in "0123456789abcdef" for ch in sha256):
            raise ValueError("sha256 must be 64 lowercase hexadecimal characters")

    @staticmethod
    def _hash_path(path: Path) -> tuple[str, int]:
        digest = hashlib.sha256()
        size = 0
        with path.open("rb") as handle:
            while True:
                block = handle.read(_BUFFER_SIZE)
                if not block:
                    break
                digest.update(block)
                size += len(block)
        return digest.hexdigest(), size

    @classmethod
    def _verify_path(cls, path: Path, expected_digest: str, expected_size: int) -> None:
        if not path.is_file():
            raise SourceArtifactIntegrityError(f"missing artifact object: {path}")
        observed_digest, observed_size = cls._hash_path(path)
        if observed_size != expected_size:
            raise SourceArtifactIntegrityError(
                f"artifact size mismatch for {expected_digest}: expected {expected_size}, observed {observed_size}"
            )
        if observed_digest != expected_digest:
            raise SourceArtifactIntegrityError(
                f"artifact digest mismatch: expected {expected_digest}, observed {observed_digest}"
            )

    @staticmethod
    def _fsync_directory(path: Path) -> None:
        if os.name == "nt":
            # Intentional no-op: Python exposes no portable Windows equivalent
            # to POSIX directory fsync for durable rename metadata, so there
            # is nothing safe to call here on this platform.
            return
        fd = os.open(path, os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
