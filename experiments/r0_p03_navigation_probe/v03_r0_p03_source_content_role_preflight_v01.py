"""Git-pinned source-content role evidence, not independent semantic eligibility.

A filename, README category, Markdown Status, code docstring or workflow name
is an *authored source claim* with a recoverable exact line. This examiner
checks only what the original Git bytes demonstrably contain: document
headers and multiple per-decision statuses, syntax declarations, JSON schema
fields, TypeScript exports, and GitHub workflow source definitions. It does
not upgrade a historical decision to present authority, verify natural-owner
J2, prove test/CI execution, or select any formal build/held-out cohort.

These observations may later support a separately qualified, independent
source-eligibility adjudication. They cannot replace that adjudicator.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_r0_p03_unscored_mixed_source_cohort_readiness_v01 as prior,
)

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "v03_r0_p03_source_content_role_preflight_result_v01.json"
MIXED_DECISIONS = "docs/DECISIONS.md"
ROLE_STATES = {
    "MARKDOWN": "DOC_AUTHORIAL_STATUS_OR_EXPLANATION_NOT_CURRENTNESS_CERTIFICATION",
    "PYTHON": "SOURCE_SYNTAX_NOT_IMPLEMENTATION_EXECUTION_OR_J2",
    "TYPESCRIPT": "FRONTEND_EXPORT_SOURCE_NOT_RUNNING_UI_EVIDENCE",
    "JSON_SCHEMA": "SCHEMA_BYTES_NOT_GOVERNED_ACCEPTANCE",
    "WORKFLOW_YAML": "WORKFLOW_DEFINITION_NOT_CI_RUN_RECEIPT",
}
HEADER = re.compile(r"^\*\*(Status|Authority|Scope|Maturity|Last reviewed):\*\*\s*(.*)$")
EXPORT = re.compile(r"^\s*export\s+(?:default\s+)?(?:function|const|interface|type|class)\s+([A-Za-z_$][\w$]*)")
DECISION = re.compile(r"^##\s+(D-\d{3})\.\s+")


def anchored_line(lines: list[str], line_number: int) -> dict:
    """Bind displayed source wording to its exact original line, not a path guess."""
    line = lines[line_number - 1]
    return {
        "line": line_number,
        "raw_text": line,
        "line_sha256": sha256(line.encode("utf8")).hexdigest(),
    }


def _markdown(lines: list[str], path: str) -> dict:
    heading = anchored_line(lines, 1)
    if not lines[0].startswith("# "):
        raise ValueError("P03_CONTENT_MD_HEADING_UNEXPECTED")
    if path == MIXED_DECISIONS:
        starts = [(i + 1, m.group(1)) for i, line in enumerate(lines)
                  if (m := DECISION.match(line))]
        if not starts:
            raise ValueError("P03_CONTENT_DECISION_CARRIER_NO_ENTRIES")
        per_entry = []
        for j, (start, decision) in enumerate(starts):
            end = starts[j+1][0] if j + 1 < len(starts) else len(lines) + 1
            claims = [(k+1, lines[k]) for k in range(start, end-1)
                      if lines[k].startswith("**Status:**")]
            per_entry.append({
                "decision_id": decision,
                "header": anchored_line(lines, start),
                "claimed_status": anchored_line(lines, claims[0][0])
                    if claims else None,
            })
        statuses = sorted({entry["claimed_status"]["raw_text"].strip()
                           for entry in per_entry if entry["claimed_status"]})
        return {
            "source_format": "MARKDOWN",
            "structural_claim_type": "MULTI_DECISION_COLLECTION_NOT_ONE_STATUS",
            "first_line": heading,
            "per_entry_decision_count": len(per_entry),
            "distinct_reported_statuses": statuses,
            "decision_witnesses": per_entry,
            "whole_document_current_authority_from_this_parser": False,
            "evidence_class": ROLE_STATES["MARKDOWN"],
        }
    meta = []
    for i, line in enumerate(lines[:40], 1):
        match = HEADER.match(line)
        if match:
            meta.append({
                "field": match.group(1), "source": anchored_line(lines, i)
            })
    if not any(x["field"] == "Status" for x in meta):
        raise ValueError("P03_CONTENT_MD_STATUS_SOURCE_MISSING")
    return {
        "source_format": "MARKDOWN",
        "structural_claim_type": "DOCUMENT_HEADER_AUTHORIAL_REPORT",
        "first_line": heading,
        "reported_metadata": meta,
        "metadata_is_not_admitted_j1_or_currentness": True,
        "evidence_class": ROLE_STATES["MARKDOWN"],
    }


def _python(lines: list[str], text: str, path: str) -> dict:
    try:
        parsed = ast.parse(text, filename=path)
    except SyntaxError as exc:
        raise ValueError("P03_CONTENT_PYTHON_SYNTAX_INVALID") from exc
    symbols = [
        {"name": node.name, "line": node.lineno}
        for node in parsed.body if isinstance(
            node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
        )
    ]
    top_doc = ast.get_docstring(parsed)
    if not symbols and not top_doc:
        raise ValueError("P03_CONTENT_PYTHON_NOT_OBSERVABLE_CODE")
    witness = next(
        (anchored_line(lines, symbol["line"]) for symbol in symbols),
        anchored_line(lines, 1),
    )
    is_test = path.startswith("tests/")
    if is_test and not any(s["name"].startswith("test_") for s in symbols):
        raise ValueError("P03_CONTENT_TEST_SOURCE_HAS_NO_TEST_DECLARATION")
    return {
        "source_format": "PYTHON",
        "structural_claim_type":
            "TEST_DECLARATIONS_NOT_EXECUTION" if is_test else "PYTHON_PROGRAM_DECLARATIONS",
        "source_parses": True,
        "top_level_declaration_count": len(symbols),
        "first_declaration_names": [s["name"] for s in symbols[:8]],
        "module_docstring_present": top_doc is not None,
        "evidence_line": witness,
        "test_result_proven_by_source": False,
        "realization_of_accepted_effect_proven_by_source": False,
        "evidence_class": ROLE_STATES["PYTHON"],
    }


def _typescript(lines: list[str]) -> dict:
    exports = [
        {"name": hit.group(1), "source": anchored_line(lines, i)}
        for i, line in enumerate(lines, 1)
        if (hit := EXPORT.match(line))
    ]
    if not exports:
        raise ValueError("P03_CONTENT_TS_NO_EXPORTS")
    return {
        "source_format": "TYPESCRIPT",
        "structural_claim_type": "FRONTEND_SOURCE_EXPORTS_NOT_EXECUTION",
        "exports": exports[:12],
        "running_ui_proven_by_source": False,
        "evidence_class": ROLE_STATES["TYPESCRIPT"],
    }


def _schema(lines: list[str], text: str) -> dict:
    value = json.loads(text)
    if not (
        isinstance(value, dict)
        and value.get("$schema") == "https://json-schema.org/draft/2020-12/schema"
        and isinstance(value.get("properties"), dict)
        and value.get("title") == "Project knowledge semantic_source V1"
        and value.get("type") == "object"
    ):
        raise ValueError("P03_CONTENT_SCHEMA_NOT_EXPECTED_DECLARATION")
    title_line = next(
        (i for i, l in enumerate(lines, 1) if '"title"' in l),
        None,
    )
    if title_line is None:
        raise ValueError("P03_CONTENT_SCHEMA_TITLE_LINE_MISSING")
    return {
        "source_format": "JSON_SCHEMA",
        "structural_claim_type": "JSON_SCHEMA_DECLARATION_NOT_J1_OR_J2",
        "schema_dialect": value["$schema"],
        "declared_title": value["title"],
        "property_names": sorted(value["properties"]),
        "evidence_line": anchored_line(lines, title_line),
        "schema_is_accepted_governing_effect": False,
        "evidence_class": ROLE_STATES["JSON_SCHEMA"],
    }


def _workflow(lines: list[str]) -> dict:
    witnesses = [
        anchored_line(lines, i)
        for i, line in enumerate(lines, 1)
        if line.startswith(("name:", "on:", "jobs:"))
    ]
    if not (len(witnesses) >= 3
            and lines[0].startswith("name: Repository integrity")
            and any(x["raw_text"] == "jobs:" for x in witnesses)):
        raise ValueError("P03_CONTENT_WORKFLOW_FIELDS_MISSING")
    return {
        "source_format": "WORKFLOW_YAML",
        "structural_claim_type": "WORKFLOW_DEFINITION_NOT_PROVIDER_CI_EXECUTION",
        "definition_witnesses": witnesses,
        "actual_provider_ci_run_proven_by_source": False,
        "evidence_class": ROLE_STATES["WORKFLOW_YAML"],
    }


def inspect_record(row: dict, blob: bytes) -> dict:
    """Inspect exact source bytes; do not trust role_hypothesis as an oracle."""
    path = row["source_path"]
    if sha256(blob).hexdigest() != row["source_sha256"]:
        raise ValueError("P03_CONTENT_EXACT_BLOB_SHA_MISMATCH")
    try:
        text = blob.decode("utf8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ValueError("P03_CONTENT_NOT_UTF8") from exc
    lines = text.splitlines()
    if not lines or len(lines) != row["line_count"]:
        raise ValueError("P03_CONTENT_SOURCE_LINE_COUNT_CHANGED")
    if path.endswith(".md"):
        parsed = _markdown(lines, path)
    elif path.endswith(".py"):
        parsed = _python(lines, text, path)
    elif path.endswith((".ts", ".tsx")):
        parsed = _typescript(lines)
    elif path.endswith(".json"):
        parsed = _schema(lines, text)
    elif path.endswith((".yml", ".yaml")):
        parsed = _workflow(lines)
    else:
        raise ValueError("P03_CONTENT_UNQUALIFIED_FORMAT")
    return {
        "source_path": path,
        "source_ref": row["source_ref"],
        "source_git_blob": row["git_blob_oid"],
        "source_sha256": row["source_sha256"],
        "previous_coordinator_role_hint": row["role_hypothesis"],
        "source_observation": parsed,
        "semantic_eligibility": "NOT_ADJUDICATED",
        "accepted_authority": "NOT_INFERRED_FROM_SOURCE_CONTENT_OR_ROLE",
        "independent_source_referee": "NOT_ASSIGNED",
        "formal_cohort_membership": "NOT_SELECTED",
    }


def build() -> dict[str, Any]:
    seed = prior.load_seed()
    witnesses = prior.witness_records(seed)
    roster = prior.source_roster()
    inspected = [
        inspect_record(row, prior.git_blob(row["source_path"], roster[row["source_path"]]))
        for row in witnesses
    ]
    if len(inspected) != 24 or len({
        item["source_path"] for item in inspected
    }) != 24:
        raise ValueError("P03_CONTENT_SOURCE_FRAME_INCOMPLETE")
    kinds = Counter(x["source_observation"]["source_format"] for x in inspected)
    if kinds != Counter({
        "MARKDOWN": 11, "PYTHON": 9, "TYPESCRIPT": 2,
        "JSON_SCHEMA": 1, "WORKFLOW_YAML": 1,
    }):
        raise ValueError("P03_CONTENT_WRONG_MODALITY_BALANCE")
    return {
        "schema_version": 1,
        "status": "SOURCE_CONTENT_OBSERVED_SEMANTIC_ELIGIBILITY_STILL_UNADJUDICATED",
        "source_git_revision": prior.REF,
        "source_seed_sha256": prior.SEED_SHA256,
        "source_count": 24,
        "source_modality_counts": dict(sorted(kinds.items())),
        "verified_original_git_content_and_claim_locations": True,
        "content_role_evidence": inspected,
        "unreviewed_semantic_eligibility_count": len(inspected),
        "independent_eligibility_referee_qualified": False,
        "formal_60_20_source_set_selected": False,
        "gold_or_task_answers_generated": False,
        "navigation_arm_scores": None,
        "production_authority_changed": False,
        "limits": [
            "Headers are source-authored status claims, not independently verified currentness or governing-effect admissions.",
            "The decisions collection has per-entry mixed statuses; no whole-file ACCEPT implies every past decision is currently governing.",
            "Python syntax, TypeScript exports, a JSON schema and workflow YAML are source definitions, not proof of code execution, J2, test PASS or CI outcome.",
            "The 24 fixed records were authored by the exposed coordinator and cannot qualify independence, semantic eligibility or formal build/heldout sampling.",
            "The formal 60/20 and the separate 65-source legacy worlds remain unselected/unmodified.",
        ],
    }


def main() -> None:
    data = build()
    body = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != body:
            raise RuntimeError("P03_CONTENT_PREVIEW_RECEIPT_IMMUTABLE_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as out:
            out.write(body)
    print(json.dumps({
        "status": data["status"],
        "sources": data["source_count"],
        "formats": data["source_modality_counts"],
        "formal_eligibility_count": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
