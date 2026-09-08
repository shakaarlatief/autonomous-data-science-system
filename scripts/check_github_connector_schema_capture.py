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
        fail("captured names/order must match the inventory prefix exactly")
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

    if captured_count >= 30:
        tree = actions[15]
        tree_elements = tree["inputSchema"]["properties"]["tree_elements"]
        if tree_elements.get("itemSchemaGenericized") is not True or tree_elements.get("itemSchema") != "{ [key: string]: any }":
            fail("create_tree inner-entry genericization drift")
        user_content = actions[18]
        url_limits = user_content["inputSchema"]["properties"]["url"].get("semanticLimits", [])
        if not any("private-user-images.githubusercontent.com" in value for value in url_limits):
            fail("download_user_content host restriction missing")
        commit_runs = actions[24]
        if commit_runs.get("pagination", {}).get("behavior") != "FIRST_PAGE_ONLY":
            fail("fetch_commit_workflow_runs first-page-only contract drift")
        file_action = actions[25]
        file_props = file_action["inputSchema"]["properties"]
        if file_props["encoding"].get("enum") != ["utf-8", "base64"] or file_props["encoding"].get("default") != "utf-8":
            fail("fetch_file encoding enum/default drift")
        if file_props["start_line"].get("exclusiveMinimum") != 0 or file_props["end_line"].get("exclusiveMinimum") != 0:
            fail("fetch_file line-bound constraints drift")
        issue = actions[26]
        issue_rules = issue.get("conditionalRules", [])
        if not any("Exactly one of repository_full_name, repository_id, repository_url" in value for value in issue_rules):
            fail("fetch_issue repository-selector XOR missing")
        issue_comments = actions[27]
        if issue_comments.get("pagination", {}).get("behavior") != "ALL_PAGES_INTERNAL":
            fail("fetch_issue_comments all-pages contract drift")
        pr_comments = actions[29]
        if pr_comments.get("pagination", {}).get("behavior") != "UNSPECIFIED":
            fail("fetch_pr_comments unspecified pagination contract drift")

    print("GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS")
    print(f"GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT={captured_count}_OF_89")
    return 0


if __name__ == "__main__":
    sys.exit(main())
