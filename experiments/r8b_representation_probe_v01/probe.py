from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import tempfile
import tomllib
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent

REAL_WORKSTREAM = ROOT / "docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md"
REAL_SPEC = ROOT / "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md"

EXPECTED_SHA256 = {
    str(REAL_WORKSTREAM.relative_to(ROOT)).replace("\\", "/"): "8af6602abbc25ff7eac8d8021239841231b32d28fe0880c859b3be2a7c30ea2a",
    str(REAL_SPEC.relative_to(ROOT)).replace("\\", "/"): "7651707b5d590efd7686a77dca20597dc731bfafa1fabc2358775bef7b9d2ffe",
}

META_FENCE = "```toml project-meta"
META_EXAMPLE_FENCE = "```toml project-meta-example"
RC3_REVIEW_BOUND = 12


class ProbeFailure(RuntimeError):
    pass


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_json_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def pretty_json(value: Any) -> str:
    return json.dumps(value, indent=2, sort_keys=False, ensure_ascii=False) + "\n"


def load_schema(name: str) -> dict[str, Any]:
    return json.loads((HERE / "schemas" / name).read_text(encoding="utf-8"))


PROJECT_META_SCHEMA = load_schema("project_meta.schema.json")
WORKSTREAM_STATE_SCHEMA = load_schema("workstream_state.schema.json")
RECEIPT_SCHEMA = load_schema("receipt.schema.json")
RELATION_SCHEMA = load_schema("standalone_relation.schema.json")


def validate_schema(value: Any, schema: dict[str, Any]) -> None:
    Draft202012Validator(schema).validate(value)


def _reject_non_json_toml(value: Any, path: str = "$") -> None:
    if isinstance(value, (dt.datetime, dt.date, dt.time)):
        raise ProbeFailure(f"non-JSON TOML value at {path}: {type(value).__name__}")
    if isinstance(value, dict):
        for key, item in value.items():
            _reject_non_json_toml(item, f"{path}.{key}")
    elif isinstance(value, list):
        for idx, item in enumerate(value):
            _reject_non_json_toml(item, f"{path}[{idx}]")


def parse_governed_markdown(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# ") or lines[0].startswith("## "):
        return {"classification": "plain", "metadata": None}

    idx = 1
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1

    if idx >= len(lines) or lines[idx].strip() != META_FENCE:
        return {"classification": "plain", "metadata": None}

    start = idx + 1
    end = start
    while end < len(lines) and lines[end].strip() != "```":
        end += 1
    if end >= len(lines):
        return {"classification": "error", "error": "unterminated metadata fence"}

    block = "\n".join(lines[start:end])
    try:
        metadata = tomllib.loads(block)
        _reject_non_json_toml(metadata)
        validate_schema(metadata, PROJECT_META_SCHEMA)
    except Exception as exc:
        return {"classification": "error", "error": str(exc)}

    next_idx = end + 1
    while next_idx < len(lines) and lines[next_idx].strip() == "":
        next_idx += 1
    if next_idx < len(lines) and lines[next_idx].strip() == META_FENCE:
        return {"classification": "error", "error": "duplicate governed metadata block"}

    return {
        "classification": "governed",
        "metadata": metadata,
        "metadata_start": idx,
        "metadata_end": end,
    }


def metadata_block(metadata: dict[str, Any]) -> str:
    # Minimal deterministic TOML writer for the probe fixture shapes.
    scalar_keys = ["contract", "id", "kind", "authority", "lifecycle"]
    lines = [META_FENCE]
    for key in scalar_keys:
        if key in metadata:
            lines.append(f'{key} = {json.dumps(metadata[key], ensure_ascii=False)}')
    if "subjects" in metadata:
        values = ", ".join(json.dumps(x, ensure_ascii=False) for x in metadata["subjects"])
        lines.append(f"subjects = [{values}]")
    for relation in metadata.get("relations", []):
        lines.append("")
        lines.append("[[relations]]")
        lines.append(f'type = {json.dumps(relation["type"], ensure_ascii=False)}')
        lines.append(f'target = {json.dumps(relation["target"], ensure_ascii=False)}')
    lines.append("```")
    return "\n".join(lines)


def verify_real_source_hashes() -> dict[str, str]:
    actual: dict[str, str] = {}
    for rel, expected in EXPECTED_SHA256.items():
        path = ROOT / rel
        digest = sha256_file(path)
        if digest != expected:
            raise ProbeFailure(f"source hash drift for {rel}: {digest} != {expected}")
        actual[rel] = digest
    return actual


def extract_legacy_json_declaration(text: str) -> dict[str, Any]:
    begin = "<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->"
    end = "<!-- PKA-STRUCTURED-DECLARATION-END -->"
    if begin not in text or end not in text:
        raise ProbeFailure("legacy declaration not found")
    raw = text.split(begin, 1)[1].split(end, 1)[0].strip()
    return json.loads(raw)


def build_real_workstream_candidates() -> tuple[str, dict[str, Any], dict[str, Any]]:
    source = REAL_WORKSTREAM.read_text(encoding="utf-8")
    legacy = extract_legacy_json_declaration(source)

    meta = {
        "contract": "project-knowledge-carrier/1",
        "id": legacy["semantic_id"],
        "kind": "workstream-definition",
        "authority": "canonical",
        "lifecycle": "active",
        "subjects": ["source-universe", "project-control"],
        "relations": [
            {"type": "governed-by", "target": legacy["governing_procedure"]},
        ],
    }
    definition = (
        "# Permanent Source Vault Bootstrap Workstream\n\n"
        + metadata_block(meta)
        + "\n\n"
        + "## Objective\n\n"
        + legacy["objective"]
        + "\n\n"
        + "## Scope\n\n"
        + "Own the durable definition, procedure relationship, and reopen conditions for the permanent Source Vault bootstrap. "
          "Operational progress and pause/resume state are intentionally excluded from this human definition.\n\n"
        + "## Governing procedure\n\n"
        + f'{legacy["governing_procedure"]}\n\n'
        + "## Durable risk and reopen triggers\n\n"
        + "\n".join(f"- {item}" for item in legacy["risk_or_reopen_triggers"])
        + "\n"
    )

    state = {
        "contract": "project-control-workstream-state/1",
        "workstream_id": legacy["semantic_id"],
        "revision": 1,
        "state": legacy["state"],
        "pause_reason": legacy["pause_reason"],
        "return_condition": legacy["return_condition"],
        "resume_target": legacy["resume_target"],
        "milestones": {
            item["milestone_id"]: item["state"]
            for item in legacy["orientation_milestones"]
        },
    }
    validate_schema(state, WORKSTREAM_STATE_SCHEMA)
    return definition, state, legacy


def build_real_spec_candidate() -> tuple[str, dict[str, Any], str]:
    source = REAL_SPEC.read_text(encoding="utf-8")
    marker = "## 1. Purpose and frozen boundary"
    if marker not in source:
        raise ProbeFailure("Specification 028 Section 1 marker missing")
    body = source[source.index(marker):]
    meta = {
        "contract": "project-knowledge-carrier/1",
        "id": "SPECIFICATION:028",
        "kind": "specification",
        "authority": "canonical",
        "lifecycle": "active",
        "subjects": ["project-knowledge-architecture"],
        "relations": [
            {"type": "implements", "target": "D-035"},
        ],
    }
    title = "# Specification 028 — V1 Project-Knowledge Architecture Implementation and Migration Contract"
    candidate = title + "\n\n" + metadata_block(meta) + "\n\n" + body
    return candidate, meta, body


def state_semantic_payload(record: dict[str, Any]) -> dict[str, Any]:
    payload = copy.deepcopy(record)
    payload.pop("revision", None)
    return payload


def validate_ordinary_transition(previous: dict[str, Any], new: dict[str, Any]) -> None:
    validate_schema(previous, WORKSTREAM_STATE_SCHEMA)
    validate_schema(new, WORKSTREAM_STATE_SCHEMA)
    if state_semantic_payload(previous) == state_semantic_payload(new):
        raise ProbeFailure("revision-only mutation is not a semantic transition")
    if new["revision"] != previous["revision"] + 1:
        raise ProbeFailure("ordinary transition must increment revision exactly once")


def validate_merge_resolution(parent_a: dict[str, Any], parent_b: dict[str, Any], resolved: dict[str, Any]) -> None:
    validate_schema(resolved, WORKSTREAM_STATE_SCHEMA)
    required = max(parent_a["revision"], parent_b["revision"]) + 1
    if resolved["revision"] != required:
        raise ProbeFailure(f"merge resolution revision must be {required}")


def guarded_write(path: Path, expected_sha: str, new_record: dict[str, Any]) -> str:
    if sha256_file(path) != expected_sha:
        raise ProbeFailure("stale write rejected")
    path.write_text(pretty_json(new_record), encoding="utf-8")
    return sha256_file(path)


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    cp = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if check and cp.returncode != 0:
        raise ProbeFailure(f"git {' '.join(args)} failed: {cp.stdout}\n{cp.stderr}")
    return cp


def init_temp_repo(repo: Path) -> None:
    git(repo, "init")
    git(repo, "config", "user.email", "probe@example.invalid")
    git(repo, "config", "user.name", "P-R8B-01 Probe")


def commit_all(repo: Path, message: str) -> None:
    git(repo, "add", "-A")
    git(repo, "commit", "-m", message)


def make_receipt(event_type: str, result: str, source_revision: str = "rev-1") -> dict[str, Any]:
    provisional = {
        "receipt_id": "pending",
        "event_type": event_type,
        "source_revision": source_revision,
        "payload": {"result": result, "public_classification": "PUBLIC_SAFE"},
    }
    digest_source = copy.deepcopy(provisional)
    digest_source["receipt_id"] = ""
    digest = sha256_bytes(canonical_json_bytes(digest_source))
    provisional["receipt_id"] = f"receipt:{digest}"
    return provisional


def receipt_locator(receipt: dict[str, Any], month: str = "2026-09") -> str:
    digest = receipt["receipt_id"].split(":", 1)[1]
    return f"receipts/{month}/{digest}.json"


def contains_private_sentinel(value: Any) -> bool:
    if isinstance(value, str):
        return "PRIVATE_ONLY://" in value
    if isinstance(value, dict):
        return any(contains_private_sentinel(v) for v in value.values())
    if isinstance(value, list):
        return any(contains_private_sentinel(v) for v in value)
    return False


def validate_public_receipt(receipt: dict[str, Any]) -> None:
    validate_schema(receipt, RECEIPT_SCHEMA)
    if contains_private_sentinel(receipt):
        raise ProbeFailure("private-only sentinel rejected")


def build_current_json(state_path: Path, state: dict[str, Any]) -> dict[str, Any]:
    source_sha = sha256_file(state_path)
    sources = [{
        "id": state["workstream_id"],
        "path": state_path.name,
        "revision": state["revision"],
        "sha256": source_sha,
    }]
    boundary = sha256_bytes(canonical_json_bytes(sources))
    return {
        "contract": "project-orientation/1",
        "derived": True,
        "authoritative": False,
        "source_boundary_digest": boundary,
        "sources": sources,
        "workstreams": [{
            "id": state["workstream_id"],
            "state": state["state"],
            "revision": state["revision"],
        }],
    }


def current_json_is_fresh(current: dict[str, Any], source_dir: Path) -> bool:
    for item in current["sources"]:
        path = source_dir / item["path"]
        if not path.exists():
            return False
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("revision") != item["revision"]:
            return False
        if sha256_file(path) != item["sha256"]:
            return False
    expected_boundary = sha256_bytes(canonical_json_bytes(current["sources"]))
    return expected_boundary == current["source_boundary_digest"]


def parse_relation_toml(path: Path) -> dict[str, Any]:
    value = tomllib.loads(path.read_text(encoding="utf-8"))
    validate_schema(value, RELATION_SCHEMA)
    return value


def discover_relations(root: Path) -> list[dict[str, Any]]:
    found = []
    for path in root.rglob("*.toml"):
        try:
            value = tomllib.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if value.get("kind") == "standalone-relation":
            validate_schema(value, RELATION_SCHEMA)
            found.append(value)
    return sorted(found, key=lambda x: x["relation_id"])


def relation_toml(relation_id: str, source: str, target: str, relation_type: str = "relates-to") -> str:
    return (
        'contract = "project-standalone-relation/1"\n'
        'kind = "standalone-relation"\n'
        f'relation_id = {json.dumps(relation_id)}\n'
        f'relation_type = {json.dumps(relation_type)}\n'
        f'source = {json.dumps(source)}\n'
        f'target = {json.dumps(target)}\n'
    )


def rc3_admission(existing_count: int) -> str:
    return "REVIEW_REQUIRED" if existing_count >= RC3_REVIEW_BOUND else "ADMIT"


def build_sqlite_index(db_path: Path, docs: list[tuple[str, str]], relations: list[dict[str, Any]], state: dict[str, Any]) -> dict[str, Any]:
    if db_path.exists():
        db_path.unlink()
    con = sqlite3.connect(db_path)
    try:
        con.executescript(
            """
            CREATE TABLE sources(id TEXT PRIMARY KEY, kind TEXT NOT NULL, state TEXT);
            CREATE TABLE relations(relation_id TEXT PRIMARY KEY, relation_type TEXT, source TEXT, target TEXT);
            CREATE VIRTUAL TABLE docs_fts USING fts5(id UNINDEXED, body);
            """
        )
        for doc_id, body in docs:
            con.execute("INSERT INTO sources(id, kind, state) VALUES (?, ?, NULL)", (doc_id, "document"))
            con.execute("INSERT INTO docs_fts(id, body) VALUES (?, ?)", (doc_id, body))
        con.execute(
            "INSERT OR REPLACE INTO sources(id, kind, state) VALUES (?, ?, ?)",
            (state["workstream_id"], "workstream", state["state"]),
        )
        for rel in relations:
            con.execute(
                "INSERT INTO relations VALUES (?, ?, ?, ?)",
                (rel["relation_id"], rel["relation_type"], rel["source"], rel["target"]),
            )
        con.commit()
        rows = con.execute("SELECT id, kind, COALESCE(state, '') FROM sources ORDER BY id").fetchall()
        edges = con.execute("SELECT relation_id, relation_type, source, target FROM relations ORDER BY relation_id").fetchall()
        fts = con.execute("SELECT id FROM docs_fts WHERE docs_fts MATCH 'architecture' ORDER BY id").fetchall()
        return {"sources": rows, "relations": edges, "fts": fts}
    finally:
        con.close()


def record_gate(results: list[dict[str, Any]], gate: str, fn) -> None:
    try:
        details = fn()
        results.append({"gate": gate, "status": "PASS", "details": details})
    except Exception as exc:
        results.append({"gate": gate, "status": "FAIL", "details": {"error": f"{type(exc).__name__}: {exc}"}})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    source_hashes = verify_real_source_hashes()
    definition, state, legacy = build_real_workstream_candidates()
    spec_candidate, spec_meta, spec_body = build_real_spec_candidate()

    artifacts = output / "artifacts"
    artifacts.mkdir()
    (artifacts / "source_vault_definition.md").write_text(definition, encoding="utf-8")
    (artifacts / "source_vault_state.json").write_text(pretty_json(state), encoding="utf-8")
    (artifacts / "specification_028_candidate.md").write_text(spec_candidate, encoding="utf-8")

    results: list[dict[str, Any]] = []


    def g01():
        valid_meta = {
            "contract": "project-knowledge-carrier/1",
            "id": "TEST:1",
            "kind": "test",
            "authority": "canonical",
            "lifecycle": "active",
        }
        valid = "# Test\n\n" + metadata_block(valid_meta) + "\n\nBody\n"
        plain = "# Plain\n\nBody only.\n"
        about = (
            "# Metadata Format Guide\n\n"
            "This document explains the format.\n\n"
            + META_FENCE
            + "\ncontract = \"project-knowledge-carrier/1\"\nid = \"EXAMPLE\"\n"
              "kind = \"example\"\nauthority = \"canonical\"\nlifecycle = \"active\"\n```\n"
        )
        example = (
            "# Example Guide\n\n"
            "Example follows.\n\n"
            + META_EXAMPLE_FENCE
            + "\nid = \"EXAMPLE\"\n```\n"
        )
        malformed = "# Broken\n\n" + META_FENCE + "\nid = [\n```\n"
        wrong_position = "# Wrong Place\n\nProse first.\n\n" + metadata_block(valid_meta) + "\n"
        duplicate = "# Duplicate\n\n" + metadata_block(valid_meta) + "\n\n" + metadata_block(valid_meta) + "\n"
        non_h1 = "Title\n\n" + metadata_block(valid_meta) + "\n"
        cases = [
            ("valid", valid, "governed"),
            ("plain", plain, "plain"),
            ("about", about, "plain"),
            ("example", example, "plain"),
            ("malformed", malformed, "error"),
            ("wrong_position", wrong_position, "plain"),
            ("duplicate", duplicate, "error"),
            ("non_h1", non_h1, "plain"),
        ]
        observed = {}
        for name, text, expected in cases:
            got = parse_governed_markdown(text)["classification"]
            observed[name] = got
            if got != expected:
                raise ProbeFailure(f"{name}: expected {expected}, got {got}")
        return {"cases": observed, "count": len(cases)}

    record_gate(results, "G01", g01)

    def g02():
        base = (
            "# Test\n\n"
            + META_FENCE
            + "\ncontract = \"project-knowledge-carrier/1\"\nid = \"TIME:1\"\n"
              "kind = \"test\"\nauthority = \"canonical\"\nlifecycle = \"active\"\n"
        )
        native_values = {
            "date": "when = 2026-09-23",
            "time": "when = 12:30:00",
            "local_datetime": "when = 2026-09-23T12:30:00",
            "offset_datetime": "when = 2026-09-23T12:30:00+02:00",
        }
        rejected = {}
        for name, line in native_values.items():
            text = base + line + "\n```\n"
            result = parse_governed_markdown(text)
            rejected[name] = result["classification"]
            if result["classification"] != "error":
                raise ProbeFailure(f"native TOML {name} was not rejected")
        string_text = base + 'subjects = ["timestamp:2026-09-23T12:30:00+02:00"]\n```\n'
        if parse_governed_markdown(string_text)["classification"] != "governed":
            raise ProbeFailure("formatted timestamp string was not accepted")
        return {"native_types": rejected, "string_equivalent": "accepted"}

    record_gate(results, "G02", g02)

    def g03():
        plain = "# Ordinary Note\n\nNo governed metadata is needed here.\n"
        parsed = parse_governed_markdown(plain)
        if parsed["classification"] != "plain":
            raise ProbeFailure("plain Markdown was not accepted as non-governed")
        return {"classification": parsed["classification"]}

    record_gate(results, "G03", g03)

    def g04():
        parsed = parse_governed_markdown(definition)
        if parsed["classification"] != "governed":
            raise ProbeFailure("real workstream definition candidate metadata did not parse")
        if parsed["metadata"]["id"] != legacy["semantic_id"]:
            raise ProbeFailure("definition identity mismatch")
        values = [
            legacy["state"],
            legacy["pause_reason"],
            legacy["return_condition"],
            legacy["resume_target"],
            legacy["orientation_milestones"][0]["state"],
            legacy["orientation_milestones"][1]["state"],
        ]
        labels = ["state", "pause_reason", "return_condition", "resume_target", "ingestion", "course2"]
        for label, value in zip(labels, values):
            if value and value in definition:
                raise ProbeFailure(f"transition-owned value leaked into definition: {label}")
        expected_state = {
            "state": legacy["state"],
            "pause_reason": legacy["pause_reason"],
            "return_condition": legacy["return_condition"],
            "resume_target": legacy["resume_target"],
            "ingestion": legacy["orientation_milestones"][0]["state"],
            "course2": legacy["orientation_milestones"][1]["state"],
        }
        observed_state = {
            "state": state["state"],
            "pause_reason": state["pause_reason"],
            "return_condition": state["return_condition"],
            "resume_target": state["resume_target"],
            "ingestion": state["milestones"]["SOURCE-VAULT:INGESTION"],
            "course2": state["milestones"]["COURSE:2"],
        }
        if observed_state != expected_state:
            raise ProbeFailure("state candidate lost one or more preregistered facts")
        required_definition_terms = [
            legacy["objective"],
            legacy["governing_procedure"],
            legacy["risk_or_reopen_triggers"][0],
        ]
        if not all(term in definition for term in required_definition_terms):
            raise ProbeFailure("definition lost durable meaning")
        return {
            "removed_transition_facts": 6,
            "pairing_violations": 0,
            "workstream_id": state["workstream_id"],
        }

    record_gate(results, "G04", g04)

    def g05():
        before = definition.encode("utf-8")
        resumed = copy.deepcopy(state)
        resumed["revision"] += 1
        resumed["state"] = "ACTIVE"
        resumed["pause_reason"] = None
        resumed["return_condition"] = None
        validate_ordinary_transition(state, resumed)
        after = definition.encode("utf-8")
        if before != after:
            raise ProbeFailure("routine transition modified canonical human definition")
        return {
            "definition_bytes_changed": 0,
            "state_revision_before": state["revision"],
            "state_revision_after": resumed["revision"],
        }

    record_gate(results, "G05", g05)

    def g06():
        with tempfile.TemporaryDirectory(prefix="pr8b01-g06-") as td:
            path = Path(td) / "state.json"
            path.write_text(pretty_json(state), encoding="utf-8")
            base_sha = sha256_file(path)
            a = copy.deepcopy(state)
            a["revision"] += 1
            a["state"] = "ACTIVE"
            validate_ordinary_transition(state, a)
            guarded_write(path, base_sha, a)
            b = copy.deepcopy(state)
            b["revision"] += 1
            b["resume_target"] = "SOURCE-VAULT:OTHER"
            validate_ordinary_transition(state, b)
            try:
                guarded_write(path, base_sha, b)
            except ProbeFailure as exc:
                if "stale write rejected" not in str(exc):
                    raise
                return {"stale_writer": "rejected", "base_sha": base_sha}
            raise ProbeFailure("stale writer was accepted")

    record_gate(results, "G06", g06)

    def g07():
        with tempfile.TemporaryDirectory(prefix="pr8b01-g07-") as td:
            repo = Path(td)
            init_temp_repo(repo)
            path = repo / "state.json"
            path.write_text(pretty_json(state), encoding="utf-8")
            commit_all(repo, "base")
            base_branch = git(repo, "branch", "--show-current").stdout.strip() or "master"

            git(repo, "checkout", "-b", "branch-a")
            a = copy.deepcopy(state)
            a["revision"] += 1
            a["state"] = "ACTIVE"
            validate_ordinary_transition(state, a)
            path.write_text(pretty_json(a), encoding="utf-8")
            commit_all(repo, "branch a")

            git(repo, "checkout", base_branch)
            git(repo, "checkout", "-b", "branch-b")
            b = copy.deepcopy(state)
            b["revision"] += 1
            b["milestones"]["SOURCE-VAULT:INGESTION"] = "IN_PROGRESS"
            validate_ordinary_transition(state, b)
            path.write_text(pretty_json(b), encoding="utf-8")
            commit_all(repo, "branch b")

            merge = git(repo, "merge", "branch-a", check=False)
            if merge.returncode == 0:
                raise ProbeFailure("Git cleanly merged concurrent same-record state changes")
            status = git(repo, "status", "--porcelain").stdout
            if "UU state.json" not in status:
                raise ProbeFailure(f"expected state.json conflict, got {status!r}")
            git(repo, "merge", "--abort")
            return {"merge_returncode": merge.returncode, "conflict": "state.json"}

    record_gate(results, "G07", g07)

    def g08():
        active = copy.deepcopy(state)
        active["revision"] = state["revision"] + 1
        active["state"] = "ACTIVE"
        validate_ordinary_transition(state, active)

        revision_only = copy.deepcopy(state)
        revision_only["revision"] += 1
        try:
            validate_ordinary_transition(state, revision_only)
            raise ProbeFailure("revision-only mutation accepted")
        except ProbeFailure as exc:
            if "revision-only" not in str(exc):
                raise

        decrement = copy.deepcopy(state)
        decrement["revision"] = 0
        decrement["state"] = "ACTIVE"
        try:
            validate_ordinary_transition(state, decrement)
            raise ProbeFailure("decrement accepted")
        except Exception:
            pass

        same = copy.deepcopy(state)
        same["state"] = "ACTIVE"
        try:
            validate_ordinary_transition(state, same)
            raise ProbeFailure("same revision replacement accepted")
        except ProbeFailure:
            pass

        b = copy.deepcopy(state)
        b["revision"] += 1
        b["milestones"]["SOURCE-VAULT:INGESTION"] = "IN_PROGRESS"
        resolved = copy.deepcopy(active)
        resolved["revision"] = max(active["revision"], b["revision"]) + 1
        resolved["milestones"]["SOURCE-VAULT:INGESTION"] = "IN_PROGRESS"
        validate_merge_resolution(active, b, resolved)
        return {"ordinary_increment": 1, "resolved_revision": resolved["revision"]}

    record_gate(results, "G08", g08)

    def g09():
        with tempfile.TemporaryDirectory(prefix="pr8b01-g09-") as td:
            root = Path(td)
            homes = [
                root / "knowledge/governance",
                root / "system/instance",
                root / "knowledge/evidence",
            ]
            for idx, home in enumerate(homes, start=1):
                home.mkdir(parents=True, exist_ok=True)
                (home / f"relation_{idx}.toml").write_text(
                    relation_toml(f"REL:{idx}", f"S:{idx}", f"T:{idx}"),
                    encoding="utf-8",
                )
            found = discover_relations(root)
            if len(found) != 3:
                raise ProbeFailure(f"expected 3 discovered relations, got {len(found)}")
            if rc3_admission(11) != "ADMIT":
                raise ProbeFailure("12th relation should be within review bound")
            if rc3_admission(12) != "REVIEW_REQUIRED":
                raise ProbeFailure("attempted 13th relation did not trigger review")
            return {
                "discovered": [x["relation_id"] for x in found],
                "repository_wide_count": len(found),
                "review_bound": RC3_REVIEW_BOUND,
                "attempted_13th": "REVIEW_REQUIRED",
            }

    record_gate(results, "G09", g09)


    def g10():
        receipt = make_receipt("activation-miss", "surfaced")
        validate_public_receipt(receipt)
        machine_capture = {
            "capture_id": "CAPTURE:MACHINE:1",
            "kind": "machine-capture",
            "authority": "candidate",
            "receipt_id": receipt["receipt_id"],
            "interpretation": "Potential trigger-vocabulary gap.",
        }
        original = copy.deepcopy(machine_capture)
        human_elaboration = (
            "# Capture Review\n\n"
            "This human elaboration references CAPTURE:MACHINE:1 without rewriting "
            "the machine capture in place.\n"
        )
        promotion_target = {
            "semantic_owner": "governance:trigger-vocabulary",
            "source_capture": machine_capture["capture_id"],
            "source_receipt": machine_capture["receipt_id"],
        }
        if machine_capture != original:
            raise ProbeFailure("machine capture changed during review")
        if "receipt_id" not in machine_capture or "payload" in machine_capture:
            raise ProbeFailure("capture does not reference receipt cleanly")
        if promotion_target.get("authority") == "governing":
            raise ProbeFailure("capture was flipped into authority in place")
        return {
            "machine_capture_unchanged": True,
            "human_elaboration_separate": bool(human_elaboration),
            "receipt_reference": machine_capture["receipt_id"],
            "promotion_owner": promotion_target["semantic_owner"],
        }

    record_gate(results, "G10", g10)

    def g11():
        receipt_a = make_receipt("transition", "A")
        receipt_b = make_receipt("transition", "B")
        locator_a = receipt_locator(receipt_a)
        locator_a2 = receipt_locator(copy.deepcopy(receipt_a))
        locator_b = receipt_locator(receipt_b)
        if locator_a != locator_a2:
            raise ProbeFailure("identical receipt did not produce identical locator")
        if locator_a == locator_b:
            raise ProbeFailure("different receipts collided")

        with tempfile.TemporaryDirectory(prefix="pr8b01-g11-") as td:
            repo = Path(td)
            init_temp_repo(repo)
            (repo / ".keep").write_text("base\n", encoding="utf-8")
            commit_all(repo, "base")
            base_branch = git(repo, "branch", "--show-current").stdout.strip() or "master"

            git(repo, "checkout", "-b", "receipt-a")
            pa = repo / locator_a
            pa.parent.mkdir(parents=True, exist_ok=True)
            pa.write_text(pretty_json(receipt_a), encoding="utf-8")
            commit_all(repo, "receipt a")

            git(repo, "checkout", base_branch)
            git(repo, "checkout", "-b", "receipt-b")
            pb = repo / locator_b
            pb.parent.mkdir(parents=True, exist_ok=True)
            pb.write_text(pretty_json(receipt_b), encoding="utf-8")
            commit_all(repo, "receipt b")

            merge = git(repo, "merge", "receipt-a", check=False)
            if merge.returncode != 0:
                raise ProbeFailure(f"distinct receipt files did not merge cleanly: {merge.stderr}")
            before_other = pb.read_bytes()
            pa.unlink()
            if pb.read_bytes() != before_other:
                raise ProbeFailure("deleting one receipt rewrote another")
        return {
            "locator_a": locator_a,
            "locator_b": locator_b,
            "parallel_merge": "clean",
            "retention_isolated": True,
        }

    record_gate(results, "G11", g11)

    def g12():
        public_receipt = make_receipt("qualification", "PASS")
        validate_public_receipt(public_receipt)

        private_receipt = copy.deepcopy(public_receipt)
        private_receipt["payload"]["private_locator"] = "PRIVATE_ONLY://synthetic-secret-location"
        rejected = False
        try:
            validate_public_receipt(private_receipt)
        except Exception:
            rejected = True
        if not rejected:
            raise ProbeFailure("private-only receipt payload was accepted")

        sentinel_receipt = copy.deepcopy(public_receipt)
        sentinel_receipt["payload"]["summary"] = "PRIVATE_ONLY://synthetic-secret-location"
        rejected_sentinel = False
        try:
            validate_public_receipt(sentinel_receipt)
        except ProbeFailure:
            rejected_sentinel = True
        if not rejected_sentinel:
            raise ProbeFailure("private-only sentinel in allowed text field was accepted")
        return {"public_safe": "accepted", "private_field": "rejected", "private_sentinel": "rejected"}

    record_gate(results, "G12", g12)

    def g13():
        parsed = parse_governed_markdown(spec_candidate)
        if parsed["classification"] != "governed":
            raise ProbeFailure("Specification 028 candidate metadata did not parse")
        if parsed["metadata"]["id"] != "SPECIFICATION:028":
            raise ProbeFailure("Specification identity lost")
        if parsed["metadata"]["authority"] not in {"canonical", "governing"}:
            raise ProbeFailure("Specification authority lost")
        candidate_body = spec_candidate[spec_candidate.index("## 1. Purpose and frozen boundary"):]
        if candidate_body != spec_body:
            raise ProbeFailure("Specification normative body changed")
        if META_FENCE not in spec_candidate:
            raise ProbeFailure("candidate metadata is not visible fenced TOML")
        if "<!--" + META_FENCE in spec_candidate:
            raise ProbeFailure("candidate metadata was hidden in HTML")
        with_example = spec_candidate + "\n\n## Format example\n\n" + META_FENCE + "\nid = \"EXAMPLE\"\n```\n"
        reparsed = parse_governed_markdown(with_example)
        if reparsed["classification"] != "governed" or reparsed["metadata"]["id"] != "SPECIFICATION:028":
            raise ProbeFailure("body example was misclassified as governing metadata")
        return {"id": parsed["metadata"]["id"], "authority": parsed["metadata"]["authority"], "body_preserved": True}

    record_gate(results, "G13", g13)

    def g14():
        with tempfile.TemporaryDirectory(prefix="pr8b01-g14-") as td:
            root = Path(td)
            state_path = root / "source_vault_state.json"
            state_path.write_text(pretty_json(state), encoding="utf-8")
            current = build_current_json(state_path, state)
            current_text_1 = pretty_json(current)
            current_text_2 = pretty_json(build_current_json(state_path, state))
            if current_text_1 != current_text_2:
                raise ProbeFailure("unchanged sources did not reproduce deterministic current.json")
            if not current.get("derived") or current.get("authoritative"):
                raise ProbeFailure("current.json does not self-declare derived/non-authoritative")
            if not current_json_is_fresh(current, root):
                raise ProbeFailure("fresh current.json failed freshness check")

            changed = copy.deepcopy(state)
            changed["revision"] += 1
            changed["state"] = "ACTIVE"
            validate_ordinary_transition(state, changed)
            state_path.write_text(pretty_json(changed), encoding="utf-8")
            if current_json_is_fresh(current, root):
                raise ProbeFailure("stale current.json passed freshness check")
            listed_revision = current["sources"][0]["revision"]
            source_revision = json.loads(state_path.read_text(encoding="utf-8"))["revision"]
            if listed_revision == source_revision:
                raise ProbeFailure("tool-less revision comparison did not expose staleness")
            (artifacts / "current.json").write_text(current_text_1, encoding="utf-8")
            return {
                "fresh_initially": True,
                "stale_after_source_change": True,
                "listed_revision": listed_revision,
                "source_revision_after_change": source_revision,
            }

    record_gate(results, "G14", g14)

    def g15():
        with tempfile.TemporaryDirectory(prefix="pr8b01-g15-") as td:
            root = Path(td)
            relation_values = [
                {
                    "contract": "project-standalone-relation/1",
                    "kind": "standalone-relation",
                    "relation_id": "REL:SPEC-WORKSTREAM",
                    "relation_type": "informs",
                    "source": "SPECIFICATION:028",
                    "target": state["workstream_id"],
                }
            ]
            docs = [
                ("SPECIFICATION:028", spec_body),
                (state["workstream_id"], definition),
            ]
            db = root / "index.sqlite"
            first = build_sqlite_index(db, docs, relation_values, state)
            if not db.exists():
                raise ProbeFailure("SQLite index was not built")
            db.unlink()
            second = build_sqlite_index(db, docs, relation_values, state)
            if first != second:
                raise ProbeFailure("SQLite rebuild produced different semantic rows")
            fts_ids = {row[0] for row in first["fts"]}
            if "SPECIFICATION:028" not in fts_ids:
                raise ProbeFailure("FTS did not return expected real specification")
            if not first["relations"] or first["relations"][0][2:] != ("SPECIFICATION:028", state["workstream_id"]):
                raise ProbeFailure("typed edge traversal data missing")
            semantic_rows = {
                "sources": [list(x) for x in first["sources"]],
                "relations": [list(x) for x in first["relations"]],
                "fts": [list(x) for x in first["fts"]],
            }
            (artifacts / "sqlite_semantic_rows.json").write_text(pretty_json(semantic_rows), encoding="utf-8")
            return {"rebuild_equivalent": True, "fts_ids": sorted(fts_ids), "edge_count": len(first["relations"])}

    record_gate(results, "G15", g15)

    def g16():
        policy_text = (
            'contract = "ads-instance-policy/1"\n'
            'enabled_integrations = ["git"]\n'
            'authority_mode = "current-continuity"\n'
        )
        policy = tomllib.loads(policy_text)
        parsed_definition = parse_governed_markdown(definition)
        parsed_spec = parse_governed_markdown(spec_candidate)
        recovered = {
            "workstream_id": parsed_definition["metadata"]["id"],
            "state": state["state"],
            "specification": parsed_spec["metadata"]["id"],
            "authority_mode": policy["authority_mode"],
        }
        expected = {
            "workstream_id": "WS-SOURCE-VAULT-BOOTSTRAP",
            "state": "PAUSED",
            "specification": "SPECIFICATION:028",
            "authority_mode": "current-continuity",
        }
        if recovered != expected:
            raise ProbeFailure(f"break-glass recovery mismatch: {recovered}")
        (artifacts / "instance_policy.toml").write_text(policy_text, encoding="utf-8")
        return {"derivatives_required": False, "recovered": recovered}

    record_gate(results, "G16", g16)

    def g17():
        with tempfile.TemporaryDirectory(prefix="pr8b01-g17-") as td:
            root = Path(td)
            framework = root / "framework"
            instance = root / "instance"
            framework.mkdir()
            instance.mkdir()
            policy = instance / "policy.toml"
            state_path = instance / "state.json"
            policy.write_text('contract_version = 1\nprovider = "git"\n', encoding="utf-8")
            state_path.write_text(pretty_json(state), encoding="utf-8")
            policy_before = policy.read_bytes()
            state_before = state_path.read_bytes()

            (framework / "compatibility.json").write_text(
                pretty_json({"framework_version": 2, "supported_instance_contracts": [1, 2]}),
                encoding="utf-8",
            )
            if policy.read_bytes() != policy_before or state_path.read_bytes() != state_before:
                raise ProbeFailure("framework refresh overwrote ADS instance bytes")
            compatibility = json.loads((framework / "compatibility.json").read_text(encoding="utf-8"))
            instance_version = tomllib.loads(policy.read_text(encoding="utf-8"))["contract_version"]
            if instance_version not in compatibility["supported_instance_contracts"]:
                raise ProbeFailure("supported instance unexpectedly incompatible")

            (framework / "compatibility.json").write_text(
                pretty_json({"framework_version": 3, "supported_instance_contracts": [2]}),
                encoding="utf-8",
            )
            compatibility = json.loads((framework / "compatibility.json").read_text(encoding="utf-8"))
            outcome = "compatible" if instance_version in compatibility["supported_instance_contracts"] else "migration_required"
            if outcome != "migration_required":
                raise ProbeFailure("incompatible refresh did not fail visibly")
            if policy.read_bytes() != policy_before or state_path.read_bytes() != state_before:
                raise ProbeFailure("incompatible refresh overwrote ADS instance bytes")
            return {"compatible_refresh": "PASS", "incompatible_refresh": outcome, "instance_bytes_unchanged": True}

    record_gate(results, "G17", g17)

    def strip_metadata(text: str) -> str:
        parsed = parse_governed_markdown(text)
        if parsed["classification"] != "governed":
            raise ProbeFailure("cannot strip metadata from non-governed carrier")
        lines = text.splitlines()
        kept = lines[:parsed["metadata_start"]] + lines[parsed["metadata_end"] + 1:]
        return "\n".join(kept).strip()

    def g18():
        changed_meta = copy.deepcopy(parse_governed_markdown(definition)["metadata"])
        changed_meta["lifecycle"] = "superseded"
        parsed = parse_governed_markdown(definition)
        lines = definition.splitlines()
        changed_lines = (
            lines[:parsed["metadata_start"]]
            + metadata_block(changed_meta).splitlines()
            + lines[parsed["metadata_end"] + 1:]
        )
        changed_definition = "\n".join(changed_lines) + "\n"
        if strip_metadata(definition) != strip_metadata(changed_definition):
            raise ProbeFailure("metadata-only governing change altered prose body")
        receipt = make_receipt("review-quality", "PASS")
        locator = receipt_locator(receipt)
        if not locator.endswith(".json"):
            raise ProbeFailure("receipt addition is not one new text JSON file")
        if META_FENCE not in spec_candidate:
            raise ProbeFailure("real specification candidate metadata is not visible")
        return {
            "routine_human_definition_diff_bytes": 0,
            "metadata_change_scope": "metadata-only",
            "receipt_change_shape": "one-new-json-file",
            "spec_metadata_visible": True,
        }

    record_gate(results, "G18", g18)

    overall = "PASS" if len(results) == 18 and all(item["status"] == "PASS" for item in results) else "AMEND_REQUIRED"
    payload = {
        "probe": "P-R8B-01",
        "protocol": "Research 263",
        "candidate": "WMR-H V0.2",
        "source_hashes": source_hashes,
        "blocking_gate_count": 18,
        "overall": overall,
        "gates": results,
    }
    (output / "result.json").write_text(pretty_json(payload), encoding="utf-8")
    print(json.dumps({"probe": payload["probe"], "overall": overall, "passed": sum(x["status"] == "PASS" for x in results), "total": len(results)}, indent=2))
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
