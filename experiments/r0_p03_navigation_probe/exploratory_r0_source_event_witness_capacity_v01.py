"""Original-Git path-only event evidence sampling, not gold/authority scoring.

A public original Git commit can independently establish the occurrence
of a content-addressed tree change. It cannot by itself establish tests
executed, verified owner authorization, current governing authority, or
a successful deployment. C01/C02 protected case content is never read.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PIN = "47ed6344a9153dcf366769e95722840fbf1a8f8b"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_r0_source_event_witness_capacity_result_v01.json"
CONTRACT = "EXPLORATORY_R0_SOURCE_EVENT_WITNESS_CAPACITY_CONTRACT_V01.md"
IDENTIFIER = "R0_P03_EVIDENCE_FIRST_GIT_EVENT_SOURCE_WITNESS_CAPACITY_V01"
PREFIX = "R0-SOURCE-EVENT-WITNESS-V01"
CLASSES = ("WORKFLOW_CHANGE", "TEST_CHANGE", "IMPLEMENTATION_CHANGE", "DOCUMENTATION_ONLY")
N_PER = 4
COMMIT_HEADER = re.compile(
    r"^@@@([0-9a-f]{40})\x1f([0-9a-f ]*)\x1f([^\x1f]+)\x1f([^\x1f]+)$"
)
CODE_SUFFIXES = (".py", ".js", ".ts", ".tsx")
DOCUMENT_SUFFIXES = (".md", ".txt", ".json", ".yml", ".yaml")


def git(*args: str) -> bytes:
    p = subprocess.run(
        ["git", *args],
        cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True, timeout=25,
    )
    return p.stdout


def git_history() -> dict[str, dict[str, Any]]:
    """Single bounded git-log traversal, with original changed file names.

    Git outputs exactly one line prefixed with @@@ for each commit and an
    isolated path-only listing. Invalid/unusual path markup fails closed,
    rather than pretending an unknown path was safely classified.
    """
    raw = git(
        "log", "--no-merges", "--root", "--no-renames",
        "--pretty=format:@@@%H%x1f%P%x1f%aI%x1f%cI",
        "--name-only", PIN,
    )
    lines = raw.decode("utf-8").splitlines()
    records: dict[str, dict[str, Any]] = {}
    current = None
    for line in lines:
        if line.startswith("@@@"):
            match = COMMIT_HEADER.fullmatch(line)
            if match is None:
                raise ValueError("Unparseable original Git commit metadata boundary")
            sha, parents_raw, authored, committed = match.groups()
            if sha in records:
                raise ValueError("Git log duplicate commit identity")
            records[sha] = {
                "commit_sha": sha,
                "parents": parents_raw.split() if parents_raw else [],
                "authored_iso_metadata_only": authored,
                "committed_iso_metadata_only": committed,
                "changed_paths": [],
            }
            current = sha
        elif line:
            if current is None or line.startswith('"') or "\t" in line or line.startswith("../"):
                raise ValueError("Unsafe or unparseable changed path returned by Git log")
            records[current]["changed_paths"].append(line)
    if len(records) < 100:
        raise ValueError("Unexpectedly small historical Git source universe")
    return records


def category(paths: list[str]) -> str:
    if not paths:
        return "OTHER_OR_UNCLASSIFIED"
    if any(p.startswith(".github/workflows/") for p in paths):
        return CLASSES[0]
    if any(p.startswith("tests/") or Path(p).name.startswith("test_")
           or Path(p).name.endswith("_test.py") for p in paths):
        return CLASSES[1]
    if any(p.startswith(("src/", "tools/", "scripts/", "frontend/", "backend/", "app/"))
           or p.lower().endswith(CODE_SUFFIXES) for p in paths):
        return CLASSES[2]
    if all(p.startswith("docs/") and p.lower().endswith(DOCUMENT_SUFFIXES)
           for p in paths):
        return CLASSES[3]
    return "OTHER_OR_UNCLASSIFIED"


def rank_hash(class_name: str, commit_sha: str) -> str:
    return sha256(f"{PREFIX}|{class_name}|{commit_sha}".encode("ascii")).hexdigest()


def select(
    history: dict[str, dict[str, Any]],
) -> tuple[dict[str, list[str]], dict[str, int]]:
    strata: dict[str, list[str]] = {c: [] for c in CLASSES}
    counts = Counter()
    for commit_sha, item in history.items():
        role = category(item["changed_paths"])
        counts[role] += 1
        if role in strata:
            strata[role].append(commit_sha)
    picked: dict[str, list[str]] = {}
    for class_name, commit_ids in strata.items():
        ranked = sorted(commit_ids, key=lambda sha: (rank_hash(class_name, sha), sha))
        picked[class_name] = ranked[:N_PER]
    return picked, dict(sorted(counts.items()))


def verify_original(sha: str, expected: dict[str, Any]) -> dict[str, Any]:
    if git("cat-file", "-t", sha).strip() != b"commit":
        raise ValueError("Selected source SHA is not an original Git commit")
    subprocess.run(
        ["git", "merge-base", "--is-ancestor", sha, PIN],
        cwd=ROOT, capture_output=True, check=True, timeout=20,
    )
    raw = git(
        "diff-tree", "--no-commit-id", "--name-only", "-r",
        "--root", "--no-renames", sha,
    )
    members = raw.decode("utf-8").splitlines()
    if sorted(members) != sorted(expected["changed_paths"]):
        raise ValueError("Independent Git original diff-tree path witness disagrees")
    return {
        "original_diff_tree_stdout_bytes": len(raw),
        "original_diff_tree_stdout_sha256": sha256(raw).hexdigest(),
        "original_diff_tree_paths_verified": True,
        "reachable_in_exact_pin": True,
        "original_git_object_type": "commit",
        "git_tree_path_change_proved": True,
        "source_file_contents_read": False,
        "source_semantic_accuracy_proved": False,
        "real_test_execution_proved_from_git_paths": False,
        "owner_signed_governing_effect_proved_from_git_paths": False,
        "operative_deployment_proved_from_git_paths": False,
        "external_ci_run_verified": False,
        "external_ci_probe_performed": False,
    }


def run() -> dict[str, Any]:
    original = git_history()
    number_from_revlist = int(
        git("rev-list", "--no-merges", "--count", PIN).decode("ascii").strip()
    )
    if len(original) != number_from_revlist:
        raise ValueError("Git log and rev-list historical population disagree")
    picked, counts = select(original)
    if sum(counts.values()) != len(original):
        raise ValueError("Git historical classification partition is incomplete")
    selected = []
    for c in CLASSES:
        for index, sha in enumerate(picked[c], 1):
            row = original[sha]
            proof = verify_original(sha, row)
            selected.append({
                "id": f"{c}-{index:02d}",
                "class_name": c,
                "commit_sha": sha,
                "ranked_priority_sha256": rank_hash(c, sha),
                "parents": row["parents"],
                "authored_iso_metadata_only": row["authored_iso_metadata_only"],
                "committed_iso_metadata_only": row["committed_iso_metadata_only"],
                "changed_paths": row["changed_paths"],
                "changed_path_count": len(row["changed_paths"]),
                "source_proof": proof,
            })
    if len({r["commit_sha"] for r in selected}) != len(selected):
        raise ValueError("Sampled a commit in multiple source-evidence strata")
    n_target = sum(min(N_PER, counts.get(c, 0)) for c in CLASSES)
    if len(selected) != n_target:
        raise ValueError("Fixed pre-result strata sample count drift")
    return {
        "identifier": IDENTIFIER,
        "contract": CONTRACT,
        "historical_git_pin": PIN,
        "source_world": {
            "all_reachable_nonmerge_commits": len(original),
            "counts_by_exclusive_path_stratum": counts,
            "sampled_by_stratum": {k: len(v) for k, v in picked.items()},
            "fixed_priority_prefix": PREFIX,
            "sample_target_per_class": N_PER,
            "unclassified_commits_retained_in_denominator": counts.get("OTHER_OR_UNCLASSIFIED", 0),
            "file_contents_or_protected_gold_inspected": False,
        },
        "selected_source_event_witnesses": selected,
        "source_status": {
            "git_change_reproducibility": "ACTUAL_COMMIT_AND_DIFF_TREE_VERIFIED",
            "original_content_evidence": "NOT_READ_IN_THIS_SAMPLE",
            "human_owner_acceptance": "UNVERIFIED",
            "actual_test_execution": "UNVERIFIED",
            "github_actions_run_association": "NOT_QUERIED",
            "operative_deployment": "UNVERIFIED",
            "current_governing_authority": "UNVERIFIED",
            "C02_PRIVATE_REFERENCES": "NOT_INSPECTED",
        },
        "limits": [
            "This is a deterministic non-random, source-path-stratified feasibility sample, not a representative statistical survey.",
            "The Git pin is only a public historical evidence horizon; not an admitted B0-B4 source corpus.",
            "A Git commit/path establishes changed path membership, not source contents, test execution, signed owner acceptance, real deployment or temporal operative truth.",
            "Some paths classified as implementation or tests can be examples or generated artifacts; semantics were intentionally not inspected.",
            "Authored/committed timestamps are mutable Git metadata, not independently witnessed real event times.",
            "External GitHub Actions or other independent execution receipts have not been queried in this source-only run.",
            "Older C01 and new C02 private questions/reviewer evidence are not read, reused, replaced or solved by this output.",
            "Further independently authored tasks, answerability qualification and protocol changes require a separately recorded owner-scoped decision.",
            "No false-authority-rate, evidence-closure-rate, task completeness, scored B0-B4 outcome or physical architecture selection is inferred.",
        ],
        "formal_r0_p03_scored": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    result = run()
    raw = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as file:
            file.write(raw)
    print(json.dumps({
        "identifier": IDENTIFIER,
        "source_world": result["source_world"],
        "sampled_commits": [r["commit_sha"] for r in result["selected_source_event_witnesses"]],
        "output_saved": args.output,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
