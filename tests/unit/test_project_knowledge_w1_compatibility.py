"""W1 G107 qualification that successor generation cannot overwrite live compatibility paths."""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.project_knowledge.adapters.generated_io import GENERATED_ROOT, write_generated_bytes
from tools.project_knowledge.model import SubstrateError
from tools.project_knowledge.services.cli_ops import qualified_cli_view_specifications


ROOT = Path(__file__).resolve().parents[2]
LIVE_COMPATIBILITY_PATHS = (
    "docs/CURRENT_STATE.md",
    "docs/current_routing.json",
    "docs/CONTINUITY.md",
    "docs/KNOWLEDGE_MAP.md",
)


def test_g107_live_compatibility_paths_are_disjoint_from_all_materialization_targets() -> None:
    specifications = qualified_cli_view_specifications()
    target_paths = {
        path
        for specification in specifications
        for path in (specification.view_path, specification.manifest_path)
    }

    assert all((ROOT / path).is_file() for path in LIVE_COMPATIBILITY_PATHS)
    assert target_paths
    assert all(path.startswith(GENERATED_ROOT) for path in target_paths)
    assert not set(LIVE_COMPATIBILITY_PATHS) & target_paths


@pytest.mark.parametrize("compatibility_path", LIVE_COMPATIBILITY_PATHS)
def test_g107_generated_writer_fails_closed_on_live_compatibility_paths(
    tmp_path: Path,
    compatibility_path: str,
) -> None:
    with pytest.raises(SubstrateError) as error:
        write_generated_bytes(tmp_path, compatibility_path, b"forbidden")

    assert error.value.code == "GENERATED_WRITE_FORBIDDEN"
    assert not (tmp_path / compatibility_path).exists()
