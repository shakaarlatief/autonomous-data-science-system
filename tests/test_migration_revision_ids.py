from __future__ import annotations

import ast
from pathlib import Path


ALEMBIC_DEFAULT_VERSION_NUM_LENGTH = 32
MIGRATION_DIRECTORY = Path("migrations/versions")


def _revision_id(path: Path) -> str:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for statement in tree.body:
        if not isinstance(statement, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == "revision"
            for target in statement.targets
        ):
            continue
        if isinstance(statement.value, ast.Constant) and isinstance(statement.value.value, str):
            return statement.value.value
    raise AssertionError(f"Migration {path} does not declare a literal revision identifier")


def test_alembic_revision_ids_fit_default_version_table() -> None:
    """Keep every migration revision portable to Alembic's default VARCHAR(32)."""

    migration_paths = sorted(MIGRATION_DIRECTORY.glob("*.py"))
    assert migration_paths, "No Alembic migration files were found"

    revision_ids = [_revision_id(path) for path in migration_paths]

    assert len(revision_ids) == len(set(revision_ids)), "Alembic revision identifiers must be unique"
    for path, revision_id in zip(migration_paths, revision_ids, strict=True):
        assert len(revision_id) <= ALEMBIC_DEFAULT_VERSION_NUM_LENGTH, (
            f"Alembic revision {revision_id!r} in {path} is {len(revision_id)} characters; "
            f"the default alembic_version.version_num column allows "
            f"{ALEMBIC_DEFAULT_VERSION_NUM_LENGTH}"
        )
