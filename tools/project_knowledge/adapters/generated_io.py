"""L1 generated-artifact I/O with a fixed non-authoritative write boundary."""

import os
from pathlib import Path
import tempfile

from ..model import SubstrateError, validate_source_path


GENERATED_ROOT = "docs/project_knowledge/generated/"


def _generated_path(root: Path, source_path: str, *, create_parents: bool) -> Path | None:
    """Resolve one generated-area path without following symlinks or junctions."""
    validate_source_path(source_path)
    if not source_path.startswith(GENERATED_ROOT):
        raise SubstrateError(
            "GENERATED_WRITE_FORBIDDEN",
            "Generated-artifact I/O is confined to docs/project_knowledge/generated/.",
        )
    base = root.resolve()
    current = base
    parts = source_path.split("/")
    try:
        for component in parts[:-1]:
            current = current / component
            if current.exists():
                if current.is_symlink() or current.is_junction() or not current.is_dir():
                    raise SubstrateError(
                        "UNSUPPORTED_GENERATED_PATH",
                        "Generated-artifact parent components must be ordinary directories.",
                    )
            elif create_parents:
                current.mkdir()
            else:
                return None
        target = current / parts[-1]
        target.resolve().relative_to(base)
        return target
    except SubstrateError:
        raise
    except (OSError, ValueError) as error:
        raise SubstrateError(
            "GENERATED_ARTIFACT_UNAVAILABLE",
            "Generated-artifact path cannot be resolved safely.",
        ) from error


def read_generated_bytes(root: Path, source_path: str) -> bytes | None:
    """Read a generated artifact exactly, returning None only when it is absent."""
    target = _generated_path(root, source_path, create_parents=False)
    if target is None or not target.exists():
        return None
    if target.is_symlink() or target.is_junction() or not target.is_file():
        raise SubstrateError(
            "UNSUPPORTED_GENERATED_PATH",
            "Generated artifacts must be ordinary files.",
        )
    try:
        return target.read_bytes()
    except OSError as error:
        raise SubstrateError(
            "GENERATED_ARTIFACT_UNAVAILABLE",
            "Generated artifact cannot be read.",
        ) from error


def write_generated_bytes(root: Path, source_path: str, content: bytes) -> None:
    """Materialize immutable bytes only inside the generated-artifact boundary."""
    if type(content) is not bytes:
        raise ValueError("Generated artifact content must be immutable bytes")
    target = _generated_path(root, source_path, create_parents=True)
    if target is None:
        raise SubstrateError("GENERATED_ARTIFACT_UNAVAILABLE", "Generated target is unavailable.")
    if target.exists() and (target.is_symlink() or target.is_junction() or not target.is_file()):
        raise SubstrateError(
            "UNSUPPORTED_GENERATED_PATH",
            "Generated artifacts must be ordinary files.",
        )
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=target.parent,
            prefix=".project-knowledge-artifact-",
            delete=False,
        ) as temporary:
            temporary.write(content)
            temporary.flush()
            os.fsync(temporary.fileno())
            temporary_path = Path(temporary.name)
        os.replace(temporary_path, target)
        temporary_path = None
    except OSError as error:
        raise SubstrateError(
            "GENERATED_ARTIFACT_UNAVAILABLE",
            "Generated artifact cannot be written.",
        ) from error
    finally:
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass
