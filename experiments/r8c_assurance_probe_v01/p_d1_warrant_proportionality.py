from __future__ import annotations

import argparse
import io
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HARNESS_PATHS = [
    "experiments/r8c_assurance_probe_v01/README.md",
    "experiments/r8c_assurance_probe_v01/p_d1_claims.json",
    "experiments/r8c_assurance_probe_v01/p_d1_warrant_proportionality.py",
]


class ProbeFailure(RuntimeError):
    pass


def git_bytes(*args: str) -> bytes:
    cp = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=False)
    if cp.returncode:
        raise ProbeFailure(
            "git failed: "
            + " ".join(args)
            + "\n"
            + cp.stderr.decode("utf-8", errors="replace")
        )
    return cp.stdout


def blob(commit: str, path: str) -> bytes:
    return git_bytes("show", f"{commit}:{path}")


def sha256(data: bytes) -> str:
    import hashlib
    return hashlib.sha256(data).hexdigest()


def harness_binding(commit: str) -> dict[str, object]:
    return {
        "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
        "commit": commit,
        "files": {path: sha256(blob(commit, path)) for path in HARNESS_PATHS},
    }


def extract_source(commit: str, destination: Path) -> None:
    raw = git_bytes("archive", "--format=tar", commit)
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:") as archive:
        archive.extractall(destination)


def pytest_env(root: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join([str(root / "src"), str(root)])
    return env


def run_pytest(root: Path, nodes: list[str]) -> dict[str, object]:
    cp = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", *nodes],
        cwd=root,
        env=pytest_env(root),
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "returncode": cp.returncode,
        "stdout": cp.stdout,
        "stderr": cp.stderr,
    }


def test_count(source: str) -> int:
    return len(re.findall(r"(?m)^def test_[A-Za-z0-9_]*\(", source))


def validate_catalog(catalog: dict[str, object], source_commit: str) -> dict[str, object]:
    claims = catalog.get("claims")
    if not isinstance(claims, list):
        raise ProbeFailure("claims must be a list")
    if len(claims) != 12:
        raise ProbeFailure(f"expected 12 claims, found {len(claims)}")

    ids = [row.get("claim_id") for row in claims]
    if len(set(ids)) != len(ids):
        raise ProbeFailure("claim IDs must be unique")

    counts = {
        grain: sum(1 for row in claims if row.get("grain") == grain)
        for grain in ("INVARIANT", "SUITE", "CROSS_BOUNDARY")
    }
    if counts != {"INVARIANT": 4, "SUITE": 4, "CROSS_BOUNDARY": 4}:
        raise ProbeFailure(f"claim grain mismatch: {counts}")

    required = (
        "claim_id",
        "grain",
        "scope",
        "verifier_sources",
        "warrant_basis",
        "limitations",
        "warrant_status",
        "witness_provenance",
        "rewitness_triggers",
    )
    for row in claims:
        missing = [field for field in required if not row.get(field)]
        if missing:
            raise ProbeFailure(f"{row.get('claim_id')} missing {missing}")
        triggers = row["rewitness_triggers"]
        if not isinstance(triggers, list) or not triggers:
            raise ProbeFailure(f"{row['claim_id']} has no bounded re-witness triggers")

    invariant_rows = [row for row in claims if row["grain"] == "INVARIANT"]
    for row in invariant_rows:
        if row.get("warrant_status") != "FULL_FOR_DECLARED_SCOPE":
            raise ProbeFailure(f"{row['claim_id']} must state bounded full scope honestly")
        if not row.get("sensitivity_node") or not row.get("specificity_node"):
            raise ProbeFailure(f"{row['claim_id']} lacks executable witnesses")

    suite_rows = [row for row in claims if row["grain"] == "SUITE"]
    suite_test_counts: dict[str, int] = {}
    for row in suite_rows:
        files = row.get("covered_test_files")
        if not isinstance(files, list) or not files:
            raise ProbeFailure(f"{row['claim_id']} has no suite file mapping")
        count = 0
        for path in files:
            count += test_count(blob(source_commit, path).decode("utf-8"))
        suite_test_counts[row["claim_id"]] = count
        if count < 2:
            raise ProbeFailure(
                f"{row['claim_id']} does not demonstrate suite-level aggregation"
            )

    return {
        "claim_counts": counts,
        "suite_test_counts": suite_test_counts,
        "first_class_claim_count": len(claims),
        "covered_suite_test_function_count": sum(suite_test_counts.values()),
        "one_claim_per_test_expansion": False,
    }


def execute_invariant_witnesses(
    source_commit: str,
    claims: list[dict[str, object]],
) -> dict[str, object]:
    results: dict[str, object] = {}
    with tempfile.TemporaryDirectory(prefix="p-d1-invariants-") as tmp:
        root = Path(tmp)
        extract_source(source_commit, root)
        for row in claims:
            if row["grain"] != "INVARIANT":
                continue
            sensitivity = str(row["sensitivity_node"])
            specificity = str(row["specificity_node"])
            sensitive_run = run_pytest(root, [sensitivity])
            specific_run = run_pytest(root, [specificity])
            if sensitive_run["returncode"] != 0:
                raise ProbeFailure(
                    f"sensitivity witness failed for {row['claim_id']}: "
                    + str(sensitive_run["stdout"])
                    + str(sensitive_run["stderr"])
                )
            if specific_run["returncode"] != 0:
                raise ProbeFailure(
                    f"specificity witness failed for {row['claim_id']}: "
                    + str(specific_run["stdout"])
                    + str(specific_run["stderr"])
                )
            results[str(row["claim_id"])] = {
                "sensitivity_node": sensitivity,
                "sensitivity": "PASS",
                "specificity_node": specificity,
                "specificity": "PASS",
            }
    return results


MUTATIONS = [
    {
        "mutation_id": "M1_NONCE_FIELD_REMOVED",
        "old": '"experiment_run_nonce": self.run_nonce,',
        "new": '"experiment_run_nonce_MUTATED": self.run_nonce,',
    },
    {
        "mutation_id": "M2_DUPLICATE_OUTPUT_LIST_GUARD_DISABLED",
        "old": "if len(values) != len(set(values)):\n                raise ValueError(f\"{field_name} must not contain duplicates\")",
        "new": "if False and len(values) != len(set(values)):\n                raise ValueError(f\"{field_name} must not contain duplicates\")",
    },
    {
        "mutation_id": "M3_UNSUPPORTED_BASIS_GUARD_DISABLED",
        "old": "unsupported = sorted(referenced - supplied)",
        "new": "unsupported = []",
    },
    {
        "mutation_id": "M4_DUPLICATE_KNOWLEDGE_KEY_GUARD_DISABLED",
        "old": "if len(keys) != len(set(keys)):\n            raise ValueError(\"knowledge_revisions must contain unique stable keys\")",
        "new": "if False and len(keys) != len(set(keys)):\n            raise ValueError(\"knowledge_revisions must contain unique stable keys\")",
    },
]


def reasoning_suite_mutation(source_commit: str) -> dict[str, object]:
    test_node = "tests/unit/test_reasoning.py"

    with tempfile.TemporaryDirectory(prefix="p-d1-reasoning-baseline-") as tmp:
        root = Path(tmp)
        extract_source(source_commit, root)
        baseline = run_pytest(root, [test_node])
        if baseline["returncode"] != 0:
            raise ProbeFailure(
                "reasoning baseline suite failed before mutation: "
                + str(baseline["stdout"])
                + str(baseline["stderr"])
            )

    mutation_results: list[dict[str, object]] = []
    for mutation in MUTATIONS:
        with tempfile.TemporaryDirectory(
            prefix=f"p-d1-{mutation['mutation_id'].lower()}-"
        ) as tmp:
            root = Path(tmp)
            extract_source(source_commit, root)
            target = root / "src/ads_system/application/reasoning.py"
            text = target.read_text(encoding="utf-8")
            count = text.count(str(mutation["old"]))
            if count != 1:
                raise ProbeFailure(
                    f"{mutation['mutation_id']} replacement count={count}"
                )
            target.write_text(
                text.replace(str(mutation["old"]), str(mutation["new"])),
                encoding="utf-8",
            )
            run = run_pytest(root, [test_node])
            killed = run["returncode"] != 0
            mutation_results.append(
                {
                    "mutation_id": mutation["mutation_id"],
                    "killed": killed,
                    "returncode": run["returncode"],
                    "stdout_tail": str(run["stdout"])[-1200:],
                    "stderr_tail": str(run["stderr"])[-1200:],
                }
            )

    killed_count = sum(1 for row in mutation_results if row["killed"])
    if killed_count != len(MUTATIONS):
        raise ProbeFailure(
            f"reasoning suite failed to kill all preregistered sampled mutations: "
            f"{killed_count}/{len(MUTATIONS)}"
        )

    return {
        "suite_claim": "S1_PRODUCT_REASONING_CONTRACT_SUITE",
        "baseline": "PASS",
        "sampled_mutations": mutation_results,
        "killed": killed_count,
        "total": len(MUTATIONS),
        "kill_rate": killed_count / len(MUTATIONS),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--harness-commit", required=True)
    ap.add_argument("--source-commit", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)

    catalog = json.loads(
        blob(args.harness_commit, "experiments/r8c_assurance_probe_v01/p_d1_claims.json")
    )
    if catalog.get("source_commit") != args.source_commit:
        raise ProbeFailure("catalog source commit does not match requested source commit")

    structure = validate_catalog(catalog, args.source_commit)
    claims = catalog["claims"]
    invariant_witnesses = execute_invariant_witnesses(args.source_commit, claims)
    suite_mutation = reasoning_suite_mutation(args.source_commit)

    unrelated_edit_trigger_count = 0
    for row in claims:
        for trigger in row["rewitness_triggers"]:
            if "unrelated" in str(trigger).lower():
                unrelated_edit_trigger_count += 1
    if unrelated_edit_trigger_count:
        raise ProbeFailure("warrant catalog requires re-witnessing on unrelated edits")

    if structure["first_class_claim_count"] != 12:
        raise ProbeFailure("claim count drift")
    if len(invariant_witnesses) != 4:
        raise ProbeFailure("not all invariant claims have executable witnesses")
    if suite_mutation["kill_rate"] != 1.0:
        raise ProbeFailure("suite mutation discriminator failed")

    payload = {
        "probe": "P-D1",
        "protocol": "Research 277",
        "selection_freeze": "Research 291",
        "candidate": "WARRANT-F V0.2",
        "result": "PASS",
        "harness_binding": harness_binding(args.harness_commit),
        "source_binding": {
            "commit": args.source_commit,
            "catalog_declared_commit": catalog["source_commit"],
        },
        "catalog_structure": structure,
        "invariant_witnesses": invariant_witnesses,
        "suite_mutation_adequacy": suite_mutation,
        "maintenance": {
            "unrelated_edit_rewitness_triggers": unrelated_edit_trigger_count,
            "rule": "Re-witness on semantic verifier/input/witness/scope changes or suite health triggers, not ordinary unrelated test edits.",
        },
        "warrant_status_counts": {
            "FULL_FOR_DECLARED_SCOPE": sum(
                1 for row in claims
                if row["warrant_status"] == "FULL_FOR_DECLARED_SCOPE"
            ),
            "PARTIALLY_WARRANTED": sum(
                1 for row in claims
                if row["warrant_status"] == "PARTIALLY_WARRANTED"
            ),
        },
        "interpretation": {
            "one_claim_per_test_required": False,
            "invariant_witnesses_feasible": True,
            "suite_warrant_sensitivity_demonstrated": True,
            "ordinary_unrelated_edits_require_rewitness": False,
            "target_architecture_amendment_required": False,
            "physical_migration_authorized": False,
        },
    }
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "probe": "P-D1",
                "result": "PASS",
                "claims": structure["first_class_claim_count"],
                "covered_suite_tests": structure["covered_suite_test_function_count"],
                "invariant_witnesses": len(invariant_witnesses),
                "reasoning_mutations_killed": suite_mutation["killed"],
                "reasoning_mutations_total": suite_mutation["total"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
