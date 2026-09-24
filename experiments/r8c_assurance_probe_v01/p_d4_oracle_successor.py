from __future__ import annotations

import argparse
import copy
import hashlib
import inspect
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS_COMMIT = "d1f9418b4315010b0b4e77cc5943921a5b0e76d0"
CORPUS_PATH = "experiments/r8c_assurance_probe_v01/p_d4_oracle_corpus.json"
CORPUS_SHA256 = "4baacd66facc321c2ada84eff57acbd71fd3c9e326d8ab93a6b7adc752a24877"
CONTRACT_COMMIT = "58ff6b2f39169e2f8470ba020848472b8b196724"
CONTRACT_PATH = "experiments/r8c_assurance_probe_v01/p_d4_successor_contract_v02.json"
CONTRACT_SHA256 = "36abb09beb186f8bdd0b3014ce8acfaa606036ab9f66955c96d0fd4f043b04aa"
HARNESS_PATHS = [
    "experiments/r8c_assurance_probe_v01/README.md",
    "experiments/r8c_assurance_probe_v01/p_d4_oracle_successor.py",
]

LEGACY_BOUNDARY_RE = re.compile(r"^[a-z]+(?:-[a-z]+)*$")
LINE_RE = re.compile(r"^[A-Za-z0-9._/-]+$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SPEC_RE = re.compile(r"^\d{3}$")


class ProbeFailure(RuntimeError):
    pass


def git_bytes(*args: str) -> bytes:
    cp = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=False)
    if cp.returncode:
        raise ProbeFailure(
            "git failed: " + " ".join(args) + "\n" + cp.stderr.decode("utf-8", errors="replace")
        )
    return cp.stdout


def blob(commit: str, path: str) -> bytes:
    return git_bytes("show", f"{commit}:{path}")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def harness_binding(commit: str) -> dict[str, object]:
    return {
        "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
        "commit": commit,
        "files": {path: sha256(blob(commit, path)) for path in HARNESS_PATHS},
    }


def load_frozen_json(commit: str, path: str, expected_sha256: str) -> dict[str, object]:
    raw = blob(commit, path)
    actual = sha256(raw)
    if actual != expected_sha256:
        raise ProbeFailure(f"frozen JSON binding mismatch for {path}: {actual}")
    return json.loads(raw)


def case_source(case: dict[str, object]) -> dict[str, object]:
    source = case.get("source") or case.get("base")
    if not isinstance(source, dict):
        raise ProbeFailure(f"{case.get('case_id')} lacks source/base binding")
    return source


def checkpoint_ids(source: dict[str, object]) -> list[int]:
    ids: list[int] = []
    for path in source["checkpoint_inventory"]["paths"]:
        name = Path(str(path)).name
        if len(name) >= 4 and name[:3].isdigit() and name[3] == "_":
            ids.append(int(name[:3]))
    return sorted(ids)


def materialize_legacy_case(case: dict[str, object]) -> dict[str, object]:
    source = case_source(case)
    commit = str(source["commit"])
    routing_bytes = blob(commit, "docs/current_routing.json")
    current_bytes = blob(commit, "docs/CURRENT_STATE.md")
    if sha256(routing_bytes) != source["routing_sha256"]:
        raise ProbeFailure(f"{case['case_id']} routing source drift")
    if sha256(current_bytes) != source["current_state_sha256"]:
        raise ProbeFailure(f"{case['case_id']} current-state source drift")

    current_text = current_bytes.decode("utf-8")
    manifest: dict[str, object] | None = None
    corrupt_suffix: str | None = None
    if case["kind"] == "MUTATION":
        manifest = json.loads(routing_bytes)
        for mutation in case["mutations"]:
            op = mutation["op"]
            if op == "SET_MANIFEST":
                manifest[str(mutation["path"])] = mutation["value"]
            elif op == "REPLACE_CURRENT_STATE":
                old = str(mutation["old"])
                new = str(mutation["new"])
                count = int(mutation["count"])
                if current_text.count(old) != count:
                    raise ProbeFailure(f"{case['case_id']} replacement count drift for {old!r}")
                current_text = current_text.replace(old, new, count)
            elif op == "CORRUPT_MANIFEST_JSON":
                corrupt_suffix = str(mutation["suffix"])
            else:
                raise ProbeFailure(f"{case['case_id']} unknown mutation {op}")
        routing_bytes = (json.dumps(manifest, indent=2) + "\n").encode("utf-8")
        if corrupt_suffix is not None:
            routing_bytes += corrupt_suffix.encode("utf-8")

    return {
        "routing_bytes": routing_bytes,
        "current_text": current_text,
        "checkpoint_ids": checkpoint_ids(source),
        "checked_branch": str(case["checked_branch"]),
    }


def write_legacy_tree(case: dict[str, object], root: Path) -> None:
    materialized = materialize_legacy_case(case)
    (root / "docs" / "checkpoints").mkdir(parents=True, exist_ok=True)
    for checkpoint in materialized["checkpoint_ids"]:
        path = root / "docs" / "checkpoints" / f"{checkpoint:03d}_fixture.md"
        path.write_text("", encoding="utf-8")
    (root / "docs" / "current_routing.json").write_bytes(materialized["routing_bytes"])
    (root / "docs" / "CURRENT_STATE.md").write_text(
        str(materialized["current_text"]), encoding="utf-8"
    )


def replay_old_oracle(corpus: dict[str, object]) -> list[dict[str, object]]:
    oracle = corpus["oracle_binding"]
    oracle_bytes = blob(str(oracle["commit"]), str(oracle["path"]))
    if sha256(oracle_bytes) != oracle["git_blob_content_sha256"]:
        raise ProbeFailure("old oracle source binding drift")
    results: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="pd4-old-oracle-") as td:
        root = Path(td)
        oracle_path = root / "frozen_old_oracle.py"
        oracle_path.write_bytes(oracle_bytes)
        for case in corpus["cases"]:
            case_root = root / str(case["case_id"])
            case_root.mkdir()
            write_legacy_tree(case, case_root)
            cp = subprocess.run(
                [
                    sys.executable,
                    str(oracle_path),
                    "--root",
                    str(case_root),
                    "--checked-branch",
                    str(case["checked_branch"]),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            observed = "GOOD" if cp.returncode == 0 else "BAD"
            results.append(
                {
                    "case_id": case["case_id"],
                    "semantic_label": case["semantic_label"],
                    "observed": observed,
                    "returncode": cp.returncode,
                    "matches": observed == case["semantic_label"],
                }
            )
    return results


def parse_current_state_projection(text: str, expected_outcome: object) -> dict[str, object]:
    def one(pattern: str) -> str | None:
        match = re.search(pattern, text, re.MULTILINE)
        return match.group(1) if match else None

    checkpoint_raw = one(r"^\*\*Checkpoint:\*\*\s+(\d+)")
    active_branch = one(r"^\*\*Active development branch:\*\*\s+`([^`]+)`")
    active_pr_raw = one(r"^\*\*Active PR:\*\*\s+([^\r\n]+)")
    promoted_match = re.search(
        r"^\*\*Promoted V1 integration branch:\*\*\s+`([^`]+)`\s+at\s+`([^`]+)`",
        text,
        re.MULTILINE,
    )
    spec = one(r"^\*\*Latest specification:\*\*.*?Specification\s+(\d{3})")
    if active_pr_raw is None:
        active_pr: object = "__MISSING__"
    else:
        normalized = active_pr_raw.strip()
        if normalized == "none":
            active_pr = None
        elif normalized.startswith("#") and normalized[1:].isdigit():
            active_pr = int(normalized[1:])
        else:
            active_pr = normalized
    outcome = str(expected_outcome) if str(expected_outcome) in text else "__MISSING__"
    return {
        "active_checkpoint": int(checkpoint_raw) if checkpoint_raw is not None else -1,
        "declared_active_line": active_branch if active_branch is not None else "__MISSING__",
        "active_pr": active_pr,
        "integration_line": promoted_match.group(1) if promoted_match else "__MISSING__",
        "integration_revision": promoted_match.group(2) if promoted_match else "__MISSING__",
        "latest_specification": spec if spec is not None else "__MISSING__",
        "latest_experiment_outcome": outcome,
    }


def legacy_to_successor(case: dict[str, object]) -> dict[str, object]:
    materialized = materialize_legacy_case(case)
    try:
        manifest = json.loads(materialized["routing_bytes"])
    except json.JSONDecodeError:
        return {
            "translation_ok": False,
            "translation_violation": "PD4-SR1-TRANSLATABLE-STRUCTURED-FACTS",
        }

    boundary = manifest.get("current_boundary")
    semantic_boundary = (
        isinstance(boundary, str)
        and len(boundary) <= 64
        and LEGACY_BOUNDARY_RE.fullmatch(boundary) is not None
    )
    subject = {
        "version": 1,
        "route": {
            "active_checkpoint": manifest.get("current_checkpoint"),
            "available_checkpoints": materialized["checkpoint_ids"],
            "declared_active_line": manifest.get("active_development_branch"),
            "checked_line": materialized["checked_branch"],
            "active_pr": manifest.get("active_pr"),
        },
        "boundary": {
            "name": boundary,
            "stability": "SEMANTIC" if semantic_boundary else "VOLATILE",
        },
        "integration": {
            "line": manifest.get("promoted_integration_branch"),
            "revision": {
                "kind": "GIT_COMMIT",
                "value": manifest.get("promoted_integration_sha"),
            },
        },
        "knowledge": {
            "latest_specification": manifest.get("latest_specification"),
            "latest_experiment_outcome": manifest.get("latest_experiment_outcome"),
        },
        "orientation_projection": parse_current_state_projection(
            str(materialized["current_text"]), manifest.get("latest_experiment_outcome")
        ),
    }
    return {"translation_ok": True, "subject": subject}


def classify_successor(subject: dict[str, object]) -> dict[str, object]:
    violations: list[str] = []
    if subject.get("version") != 1:
        violations.append("PD4-SR1-TRANSLATABLE-STRUCTURED-FACTS")
        return {"pass": False, "violations": violations}

    route = subject.get("route")
    boundary = subject.get("boundary")
    integration = subject.get("integration")
    knowledge = subject.get("knowledge")
    orientation = subject.get("orientation_projection")
    if not all(isinstance(x, dict) for x in (route, boundary, integration, knowledge, orientation)):
        return {
            "pass": False,
            "violations": ["PD4-SR1-TRANSLATABLE-STRUCTURED-FACTS"],
        }

    active_checkpoint = route.get("active_checkpoint")
    available = route.get("available_checkpoints")
    if not isinstance(active_checkpoint, int) or isinstance(active_checkpoint, bool) or active_checkpoint < 0:
        violations.append("PD4-SR1-TRANSLATABLE-STRUCTURED-FACTS")
    if not isinstance(available, list) or not available or not all(
        isinstance(x, int) and not isinstance(x, bool) and x >= 0 for x in available
    ):
        violations.append("PD4-SR1-TRANSLATABLE-STRUCTURED-FACTS")

    if isinstance(active_checkpoint, int) and isinstance(available, list):
        if active_checkpoint not in available:
            violations.append("PD4-SR2-ROUTE-TARGET-EXISTS")
        declared = route.get("declared_active_line")
        checked = route.get("checked_line")
        if checked == declared and available and active_checkpoint != max(available):
            violations.append("PD4-SR3-BRANCH-SCOPED-FRESHNESS")

    canonical_projection = {
        "active_checkpoint": route.get("active_checkpoint"),
        "declared_active_line": route.get("declared_active_line"),
        "active_pr": route.get("active_pr"),
        "integration_line": integration.get("line"),
        "integration_revision": integration.get("revision", {}).get("value")
        if isinstance(integration.get("revision"), dict)
        else None,
        "latest_specification": knowledge.get("latest_specification"),
        "latest_experiment_outcome": knowledge.get("latest_experiment_outcome"),
    }
    if orientation != canonical_projection:
        violations.append("PD4-SR4-ORIENTATION-SEMANTIC-PARITY")

    if boundary.get("stability") != "SEMANTIC" or not isinstance(boundary.get("name"), str) or not boundary.get("name"):
        violations.append("PD4-SR5-STABLE-SEMANTIC-BOUNDARY")

    revision = integration.get("revision")
    revision_ok = (
        isinstance(revision, dict)
        and revision.get("kind") == "GIT_COMMIT"
        and isinstance(revision.get("value"), str)
        and SHA_RE.fullmatch(str(revision.get("value"))) is not None
    )
    if not revision_ok:
        violations.append("PD4-SR6-INTEGRATION-REVISION-IDENTITY")

    line_values = [route.get("declared_active_line"), route.get("checked_line"), integration.get("line")]
    lines_ok = all(isinstance(value, str) and value and LINE_RE.fullmatch(value) is not None for value in line_values)
    active_pr = route.get("active_pr")
    pr_ok = active_pr is None or (isinstance(active_pr, int) and not isinstance(active_pr, bool) and active_pr > 0)
    if not lines_ok or not pr_ok:
        violations.append("PD4-SR7-WORK-LINE-AND-PR-IDENTITY")

    spec = knowledge.get("latest_specification")
    outcome = knowledge.get("latest_experiment_outcome")
    if not isinstance(spec, str) or SPEC_RE.fullmatch(spec) is None or not isinstance(outcome, str) or not outcome.strip():
        violations.append("PD4-SR8-KNOWLEDGE-POINTER-WELL-FORMED")

    unique = sorted(set(violations))
    return {"pass": not unique, "violations": unique}


def classify_translation(translated: dict[str, object]) -> dict[str, object]:
    if not translated.get("translation_ok"):
        return {
            "pass": False,
            "violations": [str(translated["translation_violation"])],
        }
    return classify_successor(translated["subject"])


def direct_good_subject() -> dict[str, object]:
    return {
        "version": 1,
        "route": {
            "active_checkpoint": 269,
            "available_checkpoints": [268, 269],
            "declared_active_line": "v1-source-vault-bootstrap-resume",
            "checked_line": "v1-source-vault-bootstrap-resume",
            "active_pr": None,
        },
        "boundary": {"name": "repository-integrity-hardening", "stability": "SEMANTIC"},
        "integration": {
            "line": "v1-frontend-spike",
            "revision": {
                "kind": "GIT_COMMIT",
                "value": "2480109fadeee1e480ef03b82e335aacdf9adf91",
            },
        },
        "knowledge": {
            "latest_specification": "026",
            "latest_experiment_outcome": "INCOMPLETE",
        },
        "orientation_projection": {
            "active_checkpoint": 269,
            "declared_active_line": "v1-source-vault-bootstrap-resume",
            "active_pr": None,
            "integration_line": "v1-frontend-spike",
            "integration_revision": "2480109fadeee1e480ef03b82e335aacdf9adf91",
            "latest_specification": "026",
            "latest_experiment_outcome": "INCOMPLETE",
        },
    }


def successor_controls() -> dict[str, dict[str, object]]:
    base = direct_good_subject()
    controls: dict[str, dict[str, object]] = {}

    stale = copy.deepcopy(base)
    stale["route"]["active_checkpoint"] = 268
    stale["orientation_projection"]["active_checkpoint"] = 268
    controls["TRANSLATED_STALE"] = stale

    pr_zero = copy.deepcopy(base)
    pr_zero["route"]["active_pr"] = 0
    pr_zero["orientation_projection"]["active_pr"] = 0
    controls["PD4-X1-ACTIVE-PR-ZERO"] = pr_zero

    bad_line = copy.deepcopy(base)
    bad_line["route"]["declared_active_line"] = "invalid line"
    bad_line["orientation_projection"]["declared_active_line"] = "invalid line"
    controls["PD4-X2-INVALID-WORK-LINE"] = bad_line

    bad_spec = copy.deepcopy(base)
    bad_spec["knowledge"]["latest_specification"] = "28"
    bad_spec["orientation_projection"]["latest_specification"] = "28"
    controls["PD4-X3-MALFORMED-SPECIFICATION"] = bad_spec

    empty_outcome = copy.deepcopy(base)
    empty_outcome["knowledge"]["latest_experiment_outcome"] = ""
    empty_outcome["orientation_projection"]["latest_experiment_outcome"] = ""
    controls["PD4-X4-EMPTY-EXPERIMENT-OUTCOME"] = empty_outcome
    return controls


def evaluate(harness_commit: str) -> dict[str, object]:
    corpus = load_frozen_json(CORPUS_COMMIT, CORPUS_PATH, CORPUS_SHA256)
    contract = load_frozen_json(CONTRACT_COMMIT, CONTRACT_PATH, CONTRACT_SHA256)
    if contract.get("contract_id") != "R8C-PD4-ROUTING-SUCCESSOR-CONTRACT-V02":
        raise ProbeFailure("unexpected successor contract")

    old_results = replay_old_oracle(corpus)
    old_replay_pass = len(old_results) == 11 and all(row["matches"] for row in old_results)

    successor_results: list[dict[str, object]] = []
    for case in corpus["cases"]:
        translated = legacy_to_successor(case)
        result = classify_translation(translated)
        observed = "GOOD" if result["pass"] else "BAD"
        successor_results.append(
            {
                "case_id": case["case_id"],
                "semantic_label": case["semantic_label"],
                "successor_observed": observed,
                "violations": result["violations"],
                "matches": observed == case["semantic_label"],
            }
        )

    direct_good = direct_good_subject()
    direct_good_result = classify_successor(direct_good)
    controls = successor_controls()
    stale_result = classify_successor(controls["TRANSLATED_STALE"])
    expected_controls = {
        "PD4-X1-ACTIVE-PR-ZERO": "PD4-SR7-WORK-LINE-AND-PR-IDENTITY",
        "PD4-X2-INVALID-WORK-LINE": "PD4-SR7-WORK-LINE-AND-PR-IDENTITY",
        "PD4-X3-MALFORMED-SPECIFICATION": "PD4-SR8-KNOWLEDGE-POINTER-WELL-FORMED",
        "PD4-X4-EMPTY-EXPERIMENT-OUTCOME": "PD4-SR8-KNOWLEDGE-POINTER-WELL-FORMED",
    }
    control_results: dict[str, object] = {}
    for control_id, expected_claim in expected_controls.items():
        result = classify_successor(controls[control_id])
        control_results[control_id] = {
            "pass": result["pass"],
            "violations": result["violations"],
            "expected_claim": expected_claim,
            "expected_claim_detected": expected_claim in result["violations"],
        }

    classifier_source = inspect.getsource(classify_successor)
    forbidden_classifier_tokens = [
        "check_current_routing",
        "current_routing.json",
        "CURRENT_STATE.md",
        "git_bytes",
        "subprocess",
    ]
    classifier_independent = not any(token in classifier_source for token in forbidden_classifier_tokens)

    successor_parity = len(successor_results) == 11 and all(row["matches"] for row in successor_results)
    direct_good_pass = direct_good_result["pass"] is True
    stale_control_pass = (
        stale_result["pass"] is False
        and "PD4-SR3-BRANCH-SCOPED-FRESHNESS" in stale_result["violations"]
    )
    successor_only_controls_pass = all(
        row["pass"] is False and row["expected_claim_detected"]
        for row in control_results.values()
    )
    no_unique_legacy_shape_requirement = (
        old_replay_pass
        and successor_parity
        and direct_good_pass
        and stale_control_pass
        and successor_only_controls_pass
        and classifier_independent
    )

    criteria = {
        "frozen_old_oracle_replay_remains_11_of_11": old_replay_pass,
        "successor_matches_all_11_frozen_dispositions": successor_parity,
        "direct_translated_good_case_passes_without_legacy_carrier_access": direct_good_pass,
        "direct_stale_translated_control_fails_freshness_claim": stale_control_pass,
        "successor_only_semantic_completeness_controls_pass": successor_only_controls_pass,
        "successor_classifier_is_legacy_mechanism_independent": classifier_independent,
        "no_unique_frozen_requirement_depends_on_legacy_shape": no_unique_legacy_shape_requirement,
    }
    result = "PASS" if all(criteria.values()) else "AMEND"

    return {
        "probe": "P-D4",
        "protocol": "Research 277",
        "candidate": "WARRANT-F V0.2",
        "result": result,
        "corpus_binding": {
            "commit": CORPUS_COMMIT,
            "path": CORPUS_PATH,
            "git_blob_content_sha256": CORPUS_SHA256,
        },
        "successor_contract_binding": {
            "commit": CONTRACT_COMMIT,
            "path": CONTRACT_PATH,
            "git_blob_content_sha256": CONTRACT_SHA256,
        },
        "harness_binding": harness_binding(harness_commit),
        "old_oracle_results": old_results,
        "successor_results": successor_results,
        "translated_representation": {
            "direct_good_result": direct_good_result,
            "stale_negative_result": stale_result,
        },
        "successor_only_controls": control_results,
        "independence": {
            "classifier_forbidden_tokens": forbidden_classifier_tokens,
            "classifier_independent": classifier_independent,
        },
        "criteria": criteria,
        "interpretation": {
            "semantic_parity_demonstrated_on_frozen_corpus": successor_parity,
            "translated_representation_preserves_invariants": direct_good_pass and stale_control_pass,
            "legacy_mechanism_shape_required": not no_unique_legacy_shape_requirement,
            "target_architecture_amendment_required": result != "PASS",
            "current_oracle_retirement_authorized_now": False,
            "physical_migration_authorized": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--harness-commit", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = evaluate(args.harness_commit)
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "probe": payload["probe"],
                "result": payload["result"],
                "old_oracle_matches": sum(x["matches"] for x in payload["old_oracle_results"]),
                "successor_matches": sum(x["matches"] for x in payload["successor_results"]),
                "criteria_passed": sum(payload["criteria"].values()),
                "criteria_total": len(payload["criteria"]),
            },
            indent=2,
        )
    )
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
