from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

EXPECTED_ACTION_COUNT = 89
EXPECTED_GROUP_COUNTS = {
    "repository-git": 29,
    "issues": 17,
    "actions-ci": 9,
    "pull-requests-reviews": 33,
    "permissions": 1,
}
INVENTORY = Path("docs/research/github_connector_89_action_inventory.json")


def fail(message: str) -> None:
    print(f"ERROR {message}")
    raise SystemExit(1)


def main() -> int:
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    if data.get("schemaVersion") != 1:
        fail("schemaVersion must equal 1")
    if data.get("actionCount") != EXPECTED_ACTION_COUNT:
        fail(f"actionCount must equal {EXPECTED_ACTION_COUNT}")
    if data.get("negativeChallengeNewActions") != 0:
        fail("negativeChallengeNewActions must equal 0 for the frozen 2026-09-08 baseline")

    actions = data.get("actions")
    if not isinstance(actions, list) or len(actions) != EXPECTED_ACTION_COUNT:
        fail(f"actions must contain exactly {EXPECTED_ACTION_COUNT} entries")

    ordinals = [item.get("ordinal") for item in actions]
    if ordinals != list(range(1, EXPECTED_ACTION_COUNT + 1)):
        fail("ordinals must be contiguous 1..89 in preserved qualification order")

    native = [item.get("nativeAction") for item in actions]
    target = [item.get("targetAction") for item in actions]
    if len(set(native)) != EXPECTED_ACTION_COUNT:
        fail("nativeAction values must be unique")
    if len(set(target)) != EXPECTED_ACTION_COUNT:
        fail("targetAction values must be unique")
    if any(not isinstance(value, str) or not value.startswith("GitHub.") for value in native):
        fail("every nativeAction must begin with GitHub.")
    if any(not isinstance(value, str) or not value.startswith("github.") for value in target):
        fail("every targetAction must begin with github.")
    for native_name, target_name in zip(native, target):
        if native_name.split(".", 1)[1] != target_name.split(".", 1)[1]:
            fail(f"target action suffix drift: {native_name} -> {target_name}")

    counts = Counter(item.get("domain") for item in actions)
    if dict(counts) != EXPECTED_GROUP_COUNTS:
        fail(f"domain counts drifted: {dict(counts)}")

    required_fields = {
        "ordinal", "nativeAction", "targetAction", "domain", "mutability",
        "currentRuntimeBridgeParity", "reuseBasis", "targetTransport",
    }
    for item in actions:
        if set(item) != required_fields:
            fail(f"entry {item.get('ordinal')} has wrong field set")
        if item["mutability"] not in {"read", "write"}:
            fail(f"entry {item['ordinal']} has invalid mutability")
        for field in required_fields - {"ordinal"}:
            if not isinstance(item[field], str) or not item[field]:
                fail(f"entry {item['ordinal']} has an empty string field: {field}")

    print("GITHUB_CONNECTOR_89_ACTION_INVENTORY=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
