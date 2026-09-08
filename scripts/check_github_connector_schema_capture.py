from __future__ import annotations

import json
import sys
from pathlib import Path

INVENTORY = Path("docs/research/github_connector_89_action_inventory.json")
CAPTURE = Path("docs/research/github_connector_native_schema_capture.json")


def fail(message: str) -> None:
    print(f"ERROR {message}")
    raise SystemExit(1)


def main() -> int:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    capture = json.loads(CAPTURE.read_text(encoding="utf-8"))

    if capture.get("schemaVersion") != 1:
        fail("schemaVersion must equal 1")
    if capture.get("projection", {}).get("actionCount") != 89:
        fail("projection actionCount must equal 89")
    if capture.get("projection", {}).get("actionsInvoked") != 0:
        fail("schema capture must remain discovery-only with zero action invocations")

    actions = capture.get("actions")
    if not isinstance(actions, list):
        fail("actions must be a list")
    captured_count = capture.get("capturedCount")
    if captured_count != len(actions):
        fail("capturedCount must equal the number of captured actions")
    allowed_boundaries = {15, 30, 45, 60, 75, 89}
    if captured_count not in allowed_boundaries:
        fail(f"capturedCount must end on a planned batch boundary: {sorted(allowed_boundaries)}")
    completed_batches = 6 if captured_count == 89 else captured_count // 15
    if capture.get("batchesCompleted") != list(range(1, completed_batches + 1)):
        fail("batchesCompleted must be the contiguous completed batch prefix")
    expected_next = None if captured_count == 89 else captured_count + 1
    if capture.get("nextOrdinal") != expected_next:
        fail(f"nextOrdinal must equal {expected_next!r}")

    expected = inventory.get("actions", [])[:captured_count]
    expected_names = [item.get("nativeAction") for item in expected]
    names = [item.get("nativeAction") for item in actions]
    if names != expected_names:
        fail("captured names/order must match inventory ordinals 1..15 exactly")
    if [item.get("ordinal") for item in actions] != list(range(1, captured_count + 1)):
        fail(f"captured ordinals must be contiguous 1..{captured_count}")

    limits = capture.get("projectionWideLimitations", {})
    if limits.get("separateActionTitleExposed") is not False:
        fail("Batch 1 must preserve that no separate action title is exposed")
    if limits.get("projectedReturnType") != "any":
        fail("Batch 1 projected return type must be any")
    if limits.get("machineReadableOutputSchemaExposed") is not False:
        fail("Batch 1 must preserve absent machine-readable output schemas")
    if limits.get("structuredErrorSchemaExposed") is not False:
        fail("Batch 1 must preserve absent structured error schemas")
    if not isinstance(limits.get("capturedActionsWithPaginationInputs"), int):
        fail("capturedActionsWithPaginationInputs must be an integer")

    for item in actions:
        if item.get("titleExposed") is not False or item.get("title") is not None:
            fail(f"{item.get('nativeAction')} title projection drift")
        if item.get("resultContract", {}).get("projectedType") != "any":
            fail(f"{item.get('nativeAction')} result type must remain any")
        if item.get("errorContract", {}).get("structuredSchemaExposed") is not False:
            fail(f"{item.get('nativeAction')} error schema projection drift")
        schema = item.get("inputSchema", {})
        if schema.get("type") != "object":
            fail(f"{item.get('nativeAction')} input schema must be object")
        if not isinstance(schema.get("required"), list) or not isinstance(schema.get("optional"), list):
            fail(f"{item.get('nativeAction')} required/optional lists missing")
        if not isinstance(schema.get("properties"), dict):
            fail(f"{item.get('nativeAction')} properties missing")

    review = actions[6]
    if review["inputSchema"]["properties"]["action"].get("enum") != ["COMMENT", "APPROVE", "REQUEST_CHANGES"]:
        fail("add_review_to_pr action enum drift")
    blob = actions[9]
    if blob["inputSchema"]["properties"]["encoding"].get("enum") != ["utf-8", "base64"]:
        fail("create_blob encoding enum drift")
    if blob["inputSchema"]["properties"]["encoding"].get("default") != "utf-8":
        fail("create_blob encoding default drift")

    print("GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS")
    print(f"GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT={captured_count}_OF_89")
    return 0


if __name__ == "__main__":
    sys.exit(main())
