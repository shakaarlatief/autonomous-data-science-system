"""Q0 REV02 source-unit and test-catalogue completeness checks.

This validates *structural completeness* and committed source SHA-256 bindings.
Mappings remain provisional and must be semantically adjudicated before F1.
No signed proof or owner credentials are read or created.
"""
from __future__ import annotations

from typing import Any

try:
    from scripts import r0_p01_clause_inventory as clause
except ModuleNotFoundError:
    import r0_p01_clause_inventory as clause


def validate_clause_index(
    trace: dict[str, Any], approved_units: list[dict[str, Any]]
) -> list[str]:
    """Reject missing normative units, orphan links, unmatched test IDs and
    premature approval. All semantic assignments require human peer review."""

    issues: list[str] = []
    rows = trace.get("normative_clause_index", [])
    expected = {x["unit_id"]: x for x in approved_units}
    observed = {x.get("unit_id"): x for x in rows if isinstance(x, dict)}
    if len(observed) != len(rows) or set(observed) != set(expected):
        issues.append("clause index missing, duplicated or extra normative unit")
    for name, src in expected.items():
        row = observed.get(name)
        if row is None:
            continue
        for field in ("source", "section", "subsection", "line_start", "line_end",
                      "json_path", "source_sha256"):
            if row.get(field) != src.get(field):
                issues.append(f"changed normative source clause: {name}/{field}")
        if not isinstance(row.get("requirement_ids"), list) or not row["requirement_ids"]:
            issues.append(f"unmapped normative clause: {name}")
        if row.get("mapping_review") != "REVIEW_REQUIRED_SEMANTIC_CANDIDATE":
            issues.append(f"prematurely approved clause mapping: {name}")

    requirements = trace.get("requirements", [])
    all_ids = {x.get("id") for x in requirements if isinstance(x, dict)}
    mapped = {rid for unit in rows if isinstance(unit, dict)
              for rid in unit.get("requirement_ids", [])}
    if mapped - all_ids:
        issues.append("normative clause cites nonexistent requirement")
    if all_ids - mapped:
        issues.append("orphan requirement without approved-source clause")
    ckeys = {f"C{i:02d}": x for i, x in enumerate(trace.get("security_controls", []), 1)}
    if len(ckeys) != 13 or trace.get("security_control_key_bindings") != ckeys:
        issues.append("C01..C13 missing or wrong positional control key")

    tests = {k for r in requirements if isinstance(r, dict)
             for k in r.get("synthetic_test_ids", [])}
    catalog = trace.get("test_catalogue", [])
    catalog_ids = [x.get("test_id") for x in catalog if isinstance(x, dict)]
    if len(catalog_ids) != len(catalog) or len(set(catalog_ids)) != len(catalog_ids) or set(catalog_ids) != tests:
        issues.append("test catalogue and requirements do not match bidirectionally")
    layers = {"PURE", "SCORER_ORACLE", "WINDOWS_NATIVE", "BROWSER_VIRTUAL",
              "INTEGRATED_SYNTHETIC", "OWNER_MACHINE_MANUAL"}
    for row in catalog:
        if not isinstance(row, dict):
            continue
        if row.get("layer") not in layers or not row.get("oracle_source") or not row.get("forbidden_shared_code"):
            issues.append(f"unqualified test catalogue metadata: {row.get('test_id')}")
        if row.get("execution_status") != "PLANNED_NOT_IMPLEMENTED":
            issues.append(f"premature test PASS: {row.get('test_id')}")
    frozen = trace.get("freeze_boundaries", {})
    if frozen.get("F1", {}).get("status") != "UNFROZEN" or frozen.get("F2", {}).get("status") != "UNFROZEN":
        issues.append("F1 or F2 was prematurely frozen")
    if frozen.get("attempt_002_claim_binding") != "F2_MANIFEST_HASH_REQUIRES_THIRD_OWNER_AUTHORIZATION":
        issues.append("F2 claim binding authorization is missing")
    if trace.get("B_arm_P5_rotation_dependency", {}).get("if_absent") != "FAIL / UNEXECUTED_ROTATION_TARGET_ABSENT":
        issues.append("Arm B P5 missing-key dependency is not recorded")
    if trace.get("review_status") != "INDEPENDENT_CLAUSE_SEMANTICS_REVIEW_PENDING":
        issues.append("provisional mapping not marked as review pending")
    return issues
