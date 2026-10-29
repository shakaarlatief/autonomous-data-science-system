"""Non-scored deterministic first-wave selection tests with invented records only.

No real source contents, private reviewer responses, historical gold, B0-B4
implementation or author-target data is opened by these tests.
"""
from __future__ import annotations

from experiments.r0_p03_navigation_probe import source_status_first_wave_candidate as wave


def item(role: str, name: str, *, flagged: bool = False,
         size: int = 12, status: str = "REVIEW_ONLY_NOT_ADMITTED") -> dict:
    return {
        "path": name,
        "git_blob_oid": "a" * 40,
        "sha256": "b" * 64,
        "role_hint": role,
        "review_flags": ["SYNTHETIC_RISK"] if flagged else [],
        "bytes": size,
        "status": status,
    }


def test_deterministic_selection_does_not_depend_on_manifest_order() -> None:
    records = [
        item(role, f"fake/{i}-{role}-clean.md")
        for i, role in enumerate(wave.ROLES)
    ] + [
        item(role, f"fake/{i}-{role}-risk.md", flagged=True)
        for i, role in enumerate(wave.ROLES)
    ]
    first, missing = wave.select(records)
    reversed_result, reversed_missing = wave.select(list(reversed(records)))
    assert missing == reversed_missing == []
    assert [x["path"] for x in first] == [x["path"] for x in reversed_result]
    assert len(first) == len(wave.ROLES) * 2


def test_only_admission_held_sized_text_is_selected() -> None:
    role = wave.ROLES[0]
    records = [
        item(role, "fake/not-admitted.md", status="AUTHOR_ADMITTED"),
        item(role, "fake/unsupported.md", status="NON_TEXT_UNSUPPORTED_NOT_ADMITTED"),
        item(role, "fake/oversized.md", size=wave.MAX_SOURCE_BYTES + 1),
        item(role, "fake/accepted-input.md"),
        item(role, "fake/flagged-input.md", flagged=True),
    ]
    selected, missing = wave.select(records)
    assert {x["path"] for x in selected} == {
        "fake/accepted-input.md", "fake/flagged-input.md"
    }
    assert len(missing) == len(wave.ROLES) * 2 - 2
    assert all(x["state"] == "NO_SIZE_ELIGIBLE_REVIEW_ONLY_RECORD"
               for x in missing)


def test_missing_stratum_is_explicit_hold_not_filled_with_other_role() -> None:
    selected, missing = wave.select([
        item(wave.ROLES[0], "fake/only-unflagged.md")
    ])
    assert len(selected) == 1
    assert len(missing) == len(wave.ROLES) * 2 - 1
    assert missing[0]["role_hint"] == wave.ROLES[0]
    assert missing[0]["band"] == "flagged"


def test_duplicate_across_strata_is_rejected() -> None:
    record = item(wave.ROLES[0], "fake/same.md")
    # Two alternative records with the same path but different lexical flag
    # cannot refer to two independent evidence carriers.
    risk = {**record, "review_flags": ["SYNTHETIC_RISK"]}
    import pytest
    with pytest.raises(ValueError, match="Duplicate source"):
        wave.select([record, risk])
