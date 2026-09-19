"""W1 G108 qualification that current continuity remains operational authority."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SPECIFICATION = ROOT / "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md"
MIGRATION = ROOT / "docs/project_knowledge/architecture/migration_and_cutover.md"
ARCHITECTURE_README = ROOT / "docs/project_knowledge/architecture/README.md"
WORKSTREAM = ROOT / "docs/project_knowledge/selected_architecture_workstream.md"
CURRENT_STATE = ROOT / "docs/CURRENT_STATE.md"
CONTINUITY = ROOT / "docs/CONTINUITY.md"
DECISIONS = ROOT / "docs/DECISIONS.md"

CURRENT_AUTHORITY = "CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE"
SWITCH_FORBIDDEN = "AUTHORITY_SWITCH_ALLOWED=false"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_g108_governing_and_successor_control_sources_preserve_exact_authority_invariant() -> None:
    for path in (SPECIFICATION, MIGRATION, WORKSTREAM):
        text = _text(path)
        assert CURRENT_AUTHORITY in text
        assert SWITCH_FORBIDDEN in text


def test_g108_current_architecture_documentation_states_w1_without_claiming_authority() -> None:
    readme = _text(ARCHITECTURE_README)
    migration = _text(MIGRATION)

    assert "W0 and W1 are accepted." in readme
    assert "W2 shadow derived views are the next migration wave and have not yet started." in readme
    assert "Current continuity remains operational authority" in readme
    assert "successor outputs remain non-authoritative" in readme
    assert "explicit qualified W8 authority-switch decision" in readme

    assert "W0 and W1 are accepted." in migration
    assert "W2 shadow derived views are next" in migration
    assert "Current continuity remains operational authority" in migration
    assert "successor outputs remain non-authoritative" in migration
    assert "no authority switch may occur before the later qualified W8 decision" in migration


def test_g108_current_continuity_surfaces_still_self_identify_as_live_continuity() -> None:
    continuity = _text(CONTINUITY)
    current_state = _text(CURRENT_STATE)

    assert "**Status:** Current canonical continuity procedure" in continuity
    for path in (
        "docs/current_routing.json",
        "docs/CURRENT_STATE.md",
        "docs/KNOWLEDGE_MAP.md",
        "docs/CONTINUITY.md",
    ):
        assert path in continuity

    assert "Current continuity remains operational authority" in current_state
    assert "`authority_switch_allowed=false`" in current_state


def test_g108_d035_selection_still_explicitly_stops_short_of_authority_switch() -> None:
    decisions = _text(DECISIONS)
    start = decisions.index("## D-035.")
    section = decisions[start:]

    assert "**Status:** Accepted / selected successor target / not yet operational authority" in section
    assert "current operational authority    existing continuity architecture" in section
    assert "authority switch allowed         no" in section


def test_g108_successor_control_sources_do_not_claim_switched_operational_authority() -> None:
    combined = "\n".join(
        _text(path)
        for path in (
            ARCHITECTURE_README,
            MIGRATION,
            WORKSTREAM,
        )
    )

    for forbidden in (
        "AUTHORITY_SWITCH_ALLOWED=true",
        "CURRENT_OPERATIONAL_AUTHORITY=SUCCESSOR",
        "CURRENT_OPERATIONAL_AUTHORITY=PKA-CANDIDATE-01",
    ):
        assert forbidden not in combined
