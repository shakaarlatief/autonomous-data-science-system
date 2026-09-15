"""Read local worktree bytes without newline conversion or symlink traversal."""

from pathlib import Path

from ..model import SubstrateError, validate_source_path


def read_worktree_bytes(root: Path, source_path: str) -> bytes:
    validate_source_path(source_path)
    base = root.resolve()
    path = base
    for component in source_path.split("/"):
        path = path / component
        if path.is_symlink() or path.is_junction():
            raise SubstrateError("UNSUPPORTED_SOURCE_MODE", "Symlink/junction carriers are not supported")
    try:
        path.resolve().relative_to(base)
        return path.read_bytes()
    except (OSError, ValueError) as error:
        raise SubstrateError("SOURCE_UNAVAILABLE", f"Cannot read worktree source: {source_path}") from error
