"""One-shot, oracle-blind Q4 probe; only declared inputs and an in-memory writer.

Run from the repository root:
    python scripts/research/probe_candidate_01_q4_real_v01.py
Existing results are never read or overwritten. No transition step is executed.
"""

import copy
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "docs/research/project_knowledge_candidate_01_q4_real_v01"
FIXTURE = DIRECTORY / "Q4_REAL_FIXTURE_V01.json"
OUTPUT = DIRECTORY / "RESULTS_V01.json"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def snapshot(value):
    # Internal object-state comparison only, never source revision normalization.
    return digest(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verified_source(source, data, basis, commit=None):
    observed = digest(data)
    require(len(data) == source["bytes"] and observed == source["sha256"],
            "Frozen source verification failed: " + source["path"])
    return {**source, "observed_bytes": len(data), "observed_sha256": observed,
            "hash_basis": basis, "source_commit": commit, "verified": True}


def reconstruct_graph(dag):
    nodes = {node["semantic_id"]: node for node in dag["workstreams"]}
    require(len(nodes) == len(dag["workstreams"]), "Duplicate workstream ID")
    closures = {}

    def closure(node_id, visiting):
        require(node_id in nodes, "Missing dependency: " + node_id)
        require(node_id not in visiting, "Dependency cycle: " + node_id)
        if node_id not in closures:
            dependencies = nodes[node_id]["depends_on"]
            require(len(dependencies) == len(set(dependencies)), "Duplicate dependency")
            found = set()
            for dependency in dependencies:
                found.add(dependency)
                found.update(closure(dependency, visiting | {node_id}))
            closures[node_id] = found
        return closures[node_id]

    reports = {}
    for node_id, node in nodes.items():
        dependencies = closure(node_id, set())
        blockers = []
        for dependency in sorted(dependencies):
            source = nodes[dependency]
            if source["state"] != "COMPLETED":
                blockers.append({"node_id": dependency, "state": source["state"],
                                 "direct": dependency in node["depends_on"],
                                 "reason": source.get("blocked_reason") or
                                 source.get("pause_reason") or
                                 "Dependency has no COMPLETED state in frozen DAG"})
        runnable = node["state"] == "ACTIVE" and not blockers
        reports[node_id] = {
            "declared_state": node["state"], "depends_on": node["depends_on"],
            "dependency_closure": sorted(dependencies), "runnable": runnable,
            "effective_state": "RUNNABLE" if runnable else
            ("BLOCKED" if blockers or node["state"] == "BLOCKED" else node["state"]),
            "dependency_blockers": blockers,
            "own_blocked_reason": node.get("blocked_reason"),
            "pause_reason": node.get("pause_reason"),
            "return_condition": node.get("return_condition"),
            "resume_target": node.get("resume_target"),
        }
    return nodes, reports


def recover(transition):
    steps = transition["steps"]
    ids = [step["step_id"] for step in steps]
    require(len(ids) == len(set(ids)), "Duplicate transition step")
    receipts = {}
    for receipt in transition["durable_receipts"]:
        step_id = receipt["step_id"]
        require(step_id in ids and step_id not in receipts, "Invalid/duplicate receipt")
        require(bool(receipt.get("evidence_ref")), "Receipt lacks durable evidence reference")
        receipts[step_id] = receipt
    completed = [step for step in steps
                 if receipts.get(step["step_id"], {}).get("status") == "COMPLETED"]
    completed_ids = {step["step_id"] for step in completed}
    pending = [step for step in steps if step["step_id"] not in completed_ids]
    # Construct a continuation plan, without replaying or performing any operation.
    execution_log = []
    return {"transition_id": transition["transition_id"],
            "completed_steps": [step["step_id"] for step in completed],
            "pending_steps": [step["step_id"] for step in pending],
            "next_resume_step": pending[0]["step_id"] if pending else None,
            "resume_plan": pending, "completion_evidence": list(receipts.values()),
            "blind_replay_required": False, "execution_log": execution_log,
            "recovery_replay_count": sum(step in completed_ids for step in execution_log),
            "completion_policy": "Only frozen COMPLETED durable receipts establish completion"}


def inspect_interruption(transition, nodes, cockpit_bytes):
    interruption = transition["interruption"]
    require(interruption["operation"] == "read_only_resume_anchor_inspection",
            "Unsupported interruption operation")
    require(interruption["mutation_authorized"] is False, "Interruption is not read-only")
    node = nodes[interruption["unrelated_workstream_id"]]
    # Extract the anchor from the verified frozen source, without following links.
    text = cockpit_bytes.decode("utf-8")
    branch = re.search(r"\*\*Frozen design branch:\*\* `([^`]+)`", text)
    head = re.search(r"\*\*Frozen frontend head:\*\* `([^`]+)`", text)
    require(branch is not None and head is not None, "Frozen Cockpit anchor missing")
    anchor = branch.group(1) + "@" + head.group(1)
    return {**interruption, "inspected_state": node["state"],
            "declared_resume_target": node["resume_target"], "source_resume_anchor": anchor,
            "anchor_matches_source": anchor == node["resume_target"],
            "return_condition": node["return_condition"], "performed_operation": interruption["operation"]}


def concurrent_updates(case, frozen_bytes):
    base = copy.deepcopy(case["base_revision"])
    require(base["hash_algorithm"] == "SHA-256", "Unsupported revision algorithm")
    require(base["hash_basis"] == "GIT_BLOB_BYTES_AT_COMMIT", "Unsupported revision basis")
    require(digest(frozen_bytes) == base["content_digest"], "Base revision digest mismatch")
    current = frozen_bytes

    def revision(data):
        # The Git descriptor always describes the immutable seed. Changed copies
        # get an explicit separate digest, never a fabricated commit descriptor.
        return {"base_revision": copy.deepcopy(base),
                "copy_hash_algorithm": "SHA-256", "copy_hash_basis": "IN_MEMORY_RAW_BYTES",
                "copy_content_digest": digest(data)}

    revisions = {"BASE": revision(current)}
    attempts = []
    supported_patches = {"append_test_only_marker", "append_stale_marker", "append_fresh_marker"}
    for update in case["temp_updates"]:
        require(update["patch_kind"] in supported_patches, "Unsupported patch kind")
        expected = copy.deepcopy(revisions[update["expected_revision"]])
        before = current
        actual = revision(before)
        marker = ("\n<!-- Q4 TEMP ONLY: " + update["attempt_id"] + " / " +
                  update["patch_kind"] + " -->\n").encode("utf-8")
        # Serialized compare-and-swap models the fixture's frozen interleaving.
        # Compare the entire exact token before even constructing changed bytes.
        matches = expected == actual
        if matches:
            current = before + marker
        after = revision(current)
        attempts.append({**update, "expected_revision_descriptor": expected,
                         "actual_revision_before": actual, "revision_after": after,
                         "status": "APPLIED" if matches else "REJECTED_STALE_REVISION",
                         "expected_revision_matches": matches, "mutated": current != before,
                         "sha256_before": digest(before), "sha256_after": digest(current),
                         "bytes_before": len(before), "bytes_after": len(current),
                         "proposed_marker_utf8": marker.decode("utf-8"),
                         "marker_present_after": marker in current})
        writer = update["attempt_id"].split("-")
        require(len(writer) >= 2 and writer[0] == "WRITER", "Unsupported writer identity")
        revisions["AFTER_WRITER_" + writer[1]] = after
    return {"target_path": case["target_path"], "base_revision": base,
            "update_storage": "IN_MEMORY_ONLY", "schedule": "FIXTURE_ORDER_SERIALIZED_CAS",
            "revision_policy": "Exact immutable Git seed descriptor plus exact raw copy digest",
            "initial_copy_sha256": digest(frozen_bytes), "final_copy_sha256": digest(current),
            "attempts": attempts,
            "stale_attempt_mutation": any(a["mutated"] for a in attempts
                                          if not a["expected_revision_matches"])}


def main():
    require(not OUTPUT.exists(), "Existing result preserved; refusing another run")
    started = datetime.now(timezone.utc).isoformat()
    fixture_bytes = FIXTURE.read_bytes()
    fixture = json.loads(fixture_bytes)
    branch = git("branch", "--show-current").decode().strip()
    require(branch == "v1-source-vault-bootstrap-resume", "Wrong working branch")
    head = git("rev-parse", "HEAD").decode().strip()
    base = fixture["real_base_commit"]
    require(fixture["protocol"]["shadow_only"] and
            fixture["protocol"]["all_update_tests_temp_only"] and
            not fixture["protocol"]["implementation_may_read_oracle"], "Unsupported protocol")
    sources = {}
    verifications = []
    for source in fixture["real_sources"]:
        data = git("cat-file", "blob", base + ":" + source["path"])
        verifications.append(verified_source(source, data, "GIT_BLOB_BYTES_AT_COMMIT", base))
        sources[source["source_key"]] = data
    for source in fixture["shadow_sources"]:
        data = (ROOT / source["path"]).read_bytes()
        verifications.append(verified_source(source, data, "DECLARED_SHADOW_FILE_RAW_BYTES"))
        sources[source["source_key"]] = data
    dag = json.loads(sources["q4_dag"])
    require(dag["source_binding"] == {"source_commit": base,
                                     "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT"}, "DAG binding mismatch")
    nodes, node_reports = reconstruct_graph(dag)
    edges = [{"workstream": node_id, "depends_on": dependency}
             for node_id, node in nodes.items() for dependency in node["depends_on"]]
    cases = []
    for case in fixture["stress_cases"]:
        kind = case["kind"]
        if kind == "MULTI_DEPENDENCY_DAG":
            result = {"nodes": {node_id: node_reports[node_id] for node_id in case["node_ids"]}}
        elif kind == "INTERRUPTION_RECOVERY":
            transition = dag["transition"]
            require(case["transition_id"] == transition["transition_id"], "Transition ID mismatch")
            before = snapshot(transition)
            dag_before = snapshot(dag)
            recovery = recover(transition)
            interruption = inspect_interruption(transition, nodes, sources["cockpit"])
            interruption.update({"transition_sha256_before": before,
                                 "transition_sha256_after": snapshot(transition),
                                 "transition_mutated": before != snapshot(transition),
                                 "dag_mutated": dag_before != snapshot(dag),
                                 "recovery_unchanged": recovery == recover(transition)})
            result = {**recovery, "interruption": interruption}
        elif kind == "STALE_CONCURRENT_UPDATE":
            descriptor = case["base_revision"]
            require(descriptor["source_commit"] == base and
                    descriptor["source_path"] == case["target_path"], "Revision target mismatch")
            source = next(s for s in fixture["real_sources"] if s["path"] == case["target_path"])
            git("ls-files", "--error-unmatch", "--", case["target_path"])
            live_path = ROOT / case["target_path"]
            live_before = digest(live_path.read_bytes())
            try:
                updates = concurrent_updates(case, sources[source["source_key"]])
            finally:
                live_after = digest(live_path.read_bytes())
                print("Live target SHA-256 before=" + live_before + " after=" + live_after)
            live = {"path": case["target_path"], "hash_algorithm": "SHA-256",
                    "hash_basis": "WORKTREE_RAW_BYTES", "sha256_before": live_before,
                    "sha256_after": live_after, "unchanged": live_before == live_after}
            result = {**updates, "live_target": live}
        else:
            raise ValueError("Unsupported stress kind: " + kind)
        cases.append({"case_id": case["case_id"], "kind": kind, **result})
    metrics = {"dependency_edge_count": len(edges),
               "multi_dependency_node_count": sum(len(n["depends_on"]) > 1 for n in nodes.values()),
               "recovery_replay_count": recovery["recovery_replay_count"],
               "stale_attempt_mutation": updates["stale_attempt_mutation"],
               "live_target_hash_before_after": live,
               "revision_binding_basis": updates["base_revision"]}
    for requested, enabled in fixture["measurement_contract"].items():
        require(not enabled or requested.removeprefix("record_") in metrics,
                "Unimplemented measurement: " + requested)
    payload = {
        "schema_version": 1, "fixture_id": fixture["fixture_id"], "candidate_id": fixture["candidate_id"],
        "real_base_commit": base, "scope": "SHADOW_ONLY; no authority promotion or qualification evaluation",
        "provenance": {"started_at_utc": started, "finished_at_utc": datetime.now(timezone.utc).isoformat(),
                       "branch": branch, "execution_head": head, "python_version": platform.python_version(),
                       "python_executable": sys.executable, "argv": sys.argv, "cwd": str(Path.cwd()),
                       "command": "python scripts/research/probe_candidate_01_q4_real_v01.py",
                       "implementation_path": Path(__file__).relative_to(ROOT).as_posix(),
                       "implementation_sha256": digest(Path(__file__).read_bytes()),
                       "fixture_path": FIXTURE.relative_to(ROOT).as_posix(),
                       "fixture_sha256": digest(fixture_bytes), "fixture_bytes": len(fixture_bytes),
                       "run_ordinal": 1, "result_existed_at_start": False,
                       "output_policy": "Exclusive create; never read or overwrite prior result",
                       "oracle_reads": 0, "evaluation_artifact_reads": 0},
        "source_verification": verifications,
        "graph": {"acyclic": True, "nodes": dag["workstreams"], "dependency_edges": edges,
                  "parent_relationships": [{"child": key, "parent": node["parent"]}
                                           for key, node in nodes.items() if node.get("parent")],
                  "node_states": node_reports},
        "cases": cases, "measurement_contract": fixture["measurement_contract"], "metrics": metrics,
    }
    # Freeze the first observed output even if a semantic measurement is negative.
    serialized = (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    with OUTPUT.open("xb") as output:
        output.write(serialized)
    print("Created " + OUTPUT.relative_to(ROOT).as_posix())
    print("Result SHA-256=" + digest(serialized))
    print(json.dumps(metrics, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Q4 implementation error; stopping without retry: " + repr(error), file=sys.stderr)
        raise SystemExit(1)
