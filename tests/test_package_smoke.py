from __future__ import annotations

import importlib.util


def test_package_imports() -> None:
    spec = importlib.util.find_spec("ads_system")
    assert spec is not None
