from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import FrozenSet

ROOT = Path(__file__).resolve().parents[2]

HARNESS_PATHS = [
    "experiments/r8c_assurance_probe_v01/README.md",
    "experiments/r8c_assurance_probe_v01/p_d6_executor_capability.py",
]


class ProbeFailure(RuntimeError):
    pass


@dataclass(frozen=True)
class AssuranceRequest:
    request_id: str
    subject: str
    verifier_id: str
    required_capabilities: FrozenSet[str]
    required_trust_properties: FrozenSet[str]


@dataclass(frozen=True)
class Executor:
    executor_id: str
    actor_label: str
    surface_label: str
    capabilities: FrozenSet[str]
    trust_properties: FrozenSet[str]


def request_semantics(request: AssuranceRequest) -> dict[str, object]:
    return {
        "request_id": request.request_id,
        "subject": request.subject,
        "verifier_id": request.verifier_id,
        "required_capabilities": sorted(request.required_capabilities),
        "required_trust_properties": sorted(request.required_trust_properties),
    }


def eligibility(request: AssuranceRequest, executor: Executor) -> dict[str, object]:
    missing_capabilities = sorted(request.required_capabilities - executor.capabilities)
    missing_trust = sorted(
        request.required_trust_properties - executor.trust_properties
    )
    return {
        "executor_id": executor.executor_id,
        "eligible": not missing_capabilities and not missing_trust,
        "missing_capabilities": missing_capabilities,
        "missing_trust_properties": missing_trust,
    }


def derive_trust_tier(executor: Executor) -> str:
    props = executor.trust_properties
    if "artifact_attested" in props and {
        "isolated",
        "producer_authentic",
        "subject_bound",
    }.issubset(props):
        return "T3"
    if {
        "isolated",
        "producer_authentic",
        "subject_bound",
    }.issubset(props):
        return "T2"
    if {"isolated", "subject_bound"}.issubset(props):
        return "T2_ISOLATED_ONLY"
    if {"recorded", "subject_bound"}.issubset(props):
        return "T1"
    return "T0"


def bad_surface_based_trust(executor: Executor) -> str:
    if executor.surface_label == "hosted":
        return "T2"
    if executor.surface_label == "local":
        return "T1"
    return "T0"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_bytes(commit: str, rel_path: str) -> bytes:
    cp = subprocess.run(
        ["git", "show", f"{commit}:{rel_path}"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if cp.returncode != 0:
        raise ProbeFailure(
            f"cannot read frozen Git blob {commit}:{rel_path}: "
            + cp.stderr.decode("utf-8", errors="replace")
        )
    return cp.stdout


def harness_binding(commit: str) -> dict[str, object]:
    binding: dict[str, object] = {
        "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
        "commit": commit,
        "files": {},
    }
    files = binding["files"]
    assert isinstance(files, dict)
    for rel_path in HARNESS_PATHS:
        blob = git_blob_bytes(commit, rel_path)
        files[rel_path] = sha256_bytes(blob)
    return binding


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--harness-commit", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    out = Path(args.output)
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)

    binding = harness_binding(args.harness_commit)

    subject = (
        "sha256:"
        + sha256_bytes(
            b"neutral-assurance-subject-for-p-d6"
        )
    )
    request = AssuranceRequest(
        request_id="P-D6-REQUEST-1",
        subject=subject,
        verifier_id="VERIFY:BOUNDARY:1",
        required_capabilities=frozenset(
            {
                "repository_read",
                "process_execute",
            }
        ),
        required_trust_properties=frozenset(
            {
                "subject_bound",
                "result_integrity",
            }
        ),
    )
    frozen_request = request_semantics(request)

    executors = [
        Executor(
            executor_id="exec-local-a",
            actor_label="model-A",
            surface_label="local",
            capabilities=frozenset(
                {
                    "repository_read",
                    "process_execute",
                }
            ),
            trust_properties=frozenset(
                {
                    "recorded",
                    "subject_bound",
                    "result_integrity",
                }
            ),
        ),
        Executor(
            executor_id="exec-local-b",
            actor_label="model-B",
            surface_label="local",
            capabilities=frozenset(
                {
                    "repository_read",
                    "process_execute",
                }
            ),
            trust_properties=frozenset(
                {
                    "recorded",
                    "subject_bound",
                    "result_integrity",
                }
            ),
        ),
        Executor(
            executor_id="exec-hosted-authentic",
            actor_label="automation-A",
            surface_label="hosted",
            capabilities=frozenset(
                {
                    "repository_read",
                    "process_execute",
                    "status_publish",
                }
            ),
            trust_properties=frozenset(
                {
                    "isolated",
                    "producer_authentic",
                    "subject_bound",
                    "result_integrity",
                }
            ),
        ),
        Executor(
            executor_id="exec-hosted-isolated-only",
            actor_label="automation-B",
            surface_label="hosted",
            capabilities=frozenset(
                {
                    "repository_read",
                    "process_execute",
                    "status_publish",
                }
            ),
            trust_properties=frozenset(
                {
                    "isolated",
                    "subject_bound",
                    "result_integrity",
                }
            ),
        ),
        Executor(
            executor_id="exec-git-api-only",
            actor_label="model-C",
            surface_label="git_api",
            capabilities=frozenset(
                {
                    "repository_read",
                    "status_publish",
                }
            ),
            trust_properties=frozenset(
                {
                    "subject_bound",
                    "result_integrity",
                }
            ),
        ),
        Executor(
            executor_id="exec-local-unbound",
            actor_label="model-A",
            surface_label="local",
            capabilities=frozenset(
                {
                    "repository_read",
                    "process_execute",
                }
            ),
            trust_properties=frozenset(
                {
                    "recorded",
                    "result_integrity",
                }
            ),
        ),
    ]

    observed = []
    for executor in executors:
        before = copy.deepcopy(frozen_request)
        result = eligibility(request, executor)
        after = request_semantics(request)
        if before != after:
            raise ProbeFailure(
                f"executor {executor.executor_id} mutated request semantics"
            )
        result["actor_label"] = executor.actor_label
        result["surface_label"] = executor.surface_label
        result["trust_tier"] = derive_trust_tier(executor)
        observed.append(result)

    by_id = {item["executor_id"]: item for item in observed}

    # Actor-label invariance: identical capability/trust records, different
    # actor labels, must produce the same eligibility and trust result.
    a = by_id["exec-local-a"]
    b = by_id["exec-local-b"]
    invariant_fields = (
        "eligible",
        "missing_capabilities",
        "missing_trust_properties",
        "trust_tier",
    )
    if any(a[field] != b[field] for field in invariant_fields):
        raise ProbeFailure("actor label changed planner semantics")

    # Capability failure: API-only executor lacks process execution.
    api_only = by_id["exec-git-api-only"]
    if api_only["eligible"]:
        raise ProbeFailure("missing process capability did not block selection")
    if api_only["missing_capabilities"] != ["process_execute"]:
        raise ProbeFailure("missing capability was not identified exactly")

    # Trust failure: same local actor/surface but missing subject binding.
    local_unbound = by_id["exec-local-unbound"]
    if local_unbound["eligible"]:
        raise ProbeFailure("missing trust property did not block selection")
    if local_unbound["missing_trust_properties"] != ["subject_bound"]:
        raise ProbeFailure("missing trust property was not identified exactly")

    # Surface label alone must not determine T2.
    hosted_good = by_id["exec-hosted-authentic"]
    hosted_weak = by_id["exec-hosted-isolated-only"]
    if hosted_good["trust_tier"] != "T2":
        raise ProbeFailure("authentic isolated hosted executor was not T2")
    if hosted_weak["trust_tier"] != "T2_ISOLATED_ONLY":
        raise ProbeFailure("isolated-only hosted executor was over-trusted")

    # Negative control: a deliberately wrong surface-based trust function
    # must misclassify the isolated-only hosted executor. If it does not,
    # the test case is not discriminating.
    weak_executor = next(
        item for item in executors
        if item.executor_id == "exec-hosted-isolated-only"
    )
    bad_tier = bad_surface_based_trust(weak_executor)
    good_tier = derive_trust_tier(weak_executor)
    if bad_tier == good_tier:
        raise ProbeFailure(
            "negative control failed to distinguish surface-based trust"
        )

    payload = {
        "probe": "P-D6",
        "protocol": "Research 277",
        "candidate": "WARRANT-F V0.2",
        "result": "PASS",
        "harness_binding": binding,
        "request_semantics": frozen_request,
        "executor_results": observed,
        "assertions": {
            "actor_label_invariance": "PASS",
            "missing_capability_blocks": "PASS",
            "missing_trust_blocks": "PASS",
            "hosted_label_not_t2": "PASS",
            "request_semantics_unchanged": "PASS",
            "negative_control": {
                "bad_surface_based_tier": bad_tier,
                "correct_property_based_tier": good_tier,
                "discriminates": True,
            },
        },
        "interpretation": {
            "target_architecture": "SUPPORTED",
            "current_provider_selected": False,
            "model_specific_semantics_required": False,
        },
    }
    out.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "probe": "P-D6",
                "result": "PASS",
                "executors": len(executors),
                "eligible": sum(
                    1 for item in observed if item["eligible"]
                ),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
