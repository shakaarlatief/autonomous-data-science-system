"""Freeze W1 real-source build world under the separately COMMITTED W1_RULE.md.

Rule commit: b084ec8aa775426a96742ca437394f1f7b0b0b00.
Do not rewrite the rule after inspecting W1 output. This is a pre-task,
unscored engineering preparation. Historical statements are SOURCE_REPORTED,
never new J1/J2 acceptance. The future 20 heldout are NOT DRAWN here.

Historical source identities are obtained from original Git object data, not
working-tree bytes or Python imports of source files.
"""
from __future__ import annotations

from collections import Counter, deque
from hashlib import sha1, sha256
import json
from pathlib import Path
import re
import subprocess
from typing import Any

from experiments.r0_p03_navigation_probe import (
    role_frame_candidate as frame,
    v03_r0_p03_unscored_mixed_source_cohort_readiness_v01 as pilot,
)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RULE_PATH = HERE / "W1_RULE.md"
RULE_COMMIT = "b084ec8aa775426a96742ca437394f1f7b0b0b00"
PIN = "17ea403ef64092f275e3c7d6492d99929804f8e5"
OUTPUTS = {
    "manifest": HERE / "w1_manifest.json",
    "substrate": HERE / "w1_substrate.json",
    "exclusions": HERE / "w1_exclusion_log.json",
}
SEEDS = (
    "docs/DECISIONS.md",
    "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md",
    "docs/CONTINUITY.md",
    "tools/project_knowledge/identity.py",
    "tools/project_knowledge/services/refresh.py",
    "tools/project_knowledge/services/generation.py",
    "tests/unit/test_project_knowledge_identity.py",
    "tests/unit/test_project_knowledge_refresh.py",
    "schemas/project_knowledge/semantic_source.v1.schema.json",
    "docs/foundations/014_knowledge_preservation_architecture_and_evolution.md",
)
QUOTAS = {
    "governing": (9, 3),
    "orientation_foundation": (7, 2),
    "project_realization": (12, 4),
    "product_realization": (10, 3),
    "verification": (8, 3),
    "historical_evidence": (10, 3),
    "domain_collaboration": (4, 2),
}
assert sum(x[0] for x in QUOTAS.values()) == 60
assert sum(x[1] for x in QUOTAS.values()) == 20
assert len(SEEDS) == 10 and len(set(SEEDS)) == 10
SENSITIVE_HEADER = re.compile(
    r"\br0[-_]p0?3\b|\bp0?3\b|\bnavigation probe\b|\bw5\b|\bb[0-4]\b", re.I
)
HEADER_H1 = re.compile(r"^# ")
SCOPED = re.compile(r"^\*\*Scope:\*\*")
SOURCE_PATH = re.compile(
    r"(?<![A-Za-z0-9_./-])"
    r"(?:docs|tools|schemas|src|tests|scripts|frontend|migrations|experiments)/"
    r"(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+"
)
DECISION = re.compile(r"^## (D-\d{3})\. ")
HEADER = re.compile(r"^\*\*(?:Status|Authority|Scope|Parent|Supersedes):\*\*")
DEFINITION = re.compile(
    r"^\s*(?:async\s+def\s+|def\s+|class\s+|function\s+|export\s+|"
    r"CREATE\s+|name:\s*|on:\s*|jobs:\s*|test_[A-Za-z0-9_]+\s*\()",
    re.I,
)
CODE_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".mjs", ".sql", ".yml", ".yaml"}
ALLOWED_CLASSES = {
    "SOURCE_REPORTED",
    "OBSERVABLE_GIT_BLOB",
    "DEFINITION_ONLY_NOT_EXECUTION",
    "ACCEPTED_EXPERIMENT_ONLY_WEAK_ASSURANCE",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(
        value, sort_keys=True, indent=2, ensure_ascii=False,
    ) + "\n").encode("utf8")


def git(command: list[str], *, input_bytes: bytes | None = None) -> bytes:
    r = subprocess.run(
        ["git", *command], input=input_bytes, cwd=ROOT,
        capture_output=True, check=True,
    )
    return r.stdout


def check_rule() -> dict:
    """Prove the exact rule is already bound in a committed predecessor."""
    rule_blob = git(["show", f"{RULE_COMMIT}:{RULE_PATH.relative_to(ROOT).as_posix()}"])
    if sha256(rule_blob).hexdigest() != sha256(RULE_PATH.read_bytes()).hexdigest():
        # Git worktree line-ending conversions do not change the original
        # committed rule, but the current working copy must be equivalent.
        if RULE_PATH.read_bytes().replace(b"\r\n", b"\n") != rule_blob:
            raise ValueError("W1_RULE_TEXT_DIFFERS_FROM_PRECOMMITTED_BYTES")
    # The rule commit must be an ancestor of the executing repository head.
    git(["merge-base", "--is-ancestor", RULE_COMMIT, "HEAD"])
    return {
        "rule_git_commit": RULE_COMMIT,
        "rule_sha256": sha256(rule_blob).hexdigest(),
        "source_git_revision": PIN,
    }


def sha1git(blob: bytes) -> str:
    return sha1(b"blob " + str(len(blob)).encode("ascii") + b"\0" + blob).hexdigest()


def read_all_git_blobs(roster: dict[str, str]) -> dict[str, bytes]:
    """Batch-read exact original Git blobs in one Git subprocess, without 3k calls."""
    paths = sorted(roster)
    objects = [roster[p] for p in paths]
    payload = b"".join(x.encode("ascii") + b"\n" for x in objects)
    response = git(["cat-file", "--batch"], input_bytes=payload)
    out: dict[str, bytes] = {}
    pos = 0
    for path, oid in zip(paths, objects, strict=True):
        at = response.find(b"\n", pos)
        if at < 0:
            raise ValueError("W1_GIT_BLOB_BATCH_TRUNCATED_HEADER")
        header = response[pos:at].decode("ascii")
        fields = header.split(" ")
        if len(fields) != 3 or fields[0] != oid or fields[1] != "blob":
            raise ValueError("W1_GIT_BLOB_BATCH_WRONG_OID_OR_OBJECT")
        size = int(fields[2])
        start, end = at + 1, at + 1 + size
        blob = response[start:end]
        if len(blob) != size or response[end:end + 1] != b"\n" or sha1git(blob) != oid:
            raise ValueError("W1_GIT_BLOB_BYTE_OR_HASH_CONFLICT")
        out[path] = blob
        pos = end + 1
    if pos != len(response):
        raise ValueError("W1_GIT_BLOB_BATCH_TRAILING_UNEXPECTED_DATA")
    return out


def stratum(path: str) -> str:
    if path == "docs/DECISIONS.md" or path.startswith("docs/specifications/"):
        return "governing"
    if path.startswith(("docs/foundations/", "docs/project_knowledge/")) or (
        path.startswith("docs/") and path.count("/") == 1 and path.endswith(".md")
    ):
        return "orientation_foundation"
    if path.startswith(("tools/", "scripts/", "schemas/", "migrations/")):
        return "project_realization"
    if path.startswith(("src/", "frontend/")):
        return "product_realization"
    if path.startswith("tests/"):
        return "verification"
    if path.startswith(("docs/research/", "docs/checkpoints/", "docs/local_execution/")):
        return "historical_evidence"
    if path.startswith("docs/"):
        return "domain_collaboration"
    raise ValueError("W1_RULE_UNCLASSIFIED_FRAME_PATH:" + path)


def _risk_header(text: str) -> str | None:
    lines = text.splitlines()
    h1 = next((line for line in lines if HEADER_H1.match(line)), None)
    if h1 and SENSITIVE_HEADER.search(h1):
        return "H1_PROBE_OR_NAVIGATION_EXPOSURE"
    if any(SCOPED.match(line) and SENSITIVE_HEADER.search(line)
           for line in lines[:48]):
        return "SCOPE_PROBE_OR_NAVIGATION_EXPOSURE"
    return None


def exclude_reason(path: str, text: str | None) -> str | None:
    if path in {
        "docs/CURRENT_STATE.md",
        "docs/KNOWLEDGE_MAP.md",
        "docs/ARCHITECTURE_PROGRAM_OVERVIEW.md",
    }:
        return "EXPLICIT_ACCUMULATED_P03_CONTENT_EXCLUSION"
    if path.startswith("docs/model_collaboration/") and "/messages/" in path:
        return "MODEL_COLLABORATION_MESSAGE"
    if path.startswith("experiments/r0_p03_navigation_probe/") or (
        path.startswith("tests/unit/test_r0_p03_")
    ):
        return "PROBE_EXPERIMENT_OR_TEST"
    leaking = frame.leakage_reason(path)
    if leaking:
        return "FRAME_LEAKAGE:" + leaking
    if text is None:
        return "NONEMPTY_STRICT_UTF8_REQUIRED"
    return _risk_header(text)


def path_links(text: str, eligible: set[str]) -> list[tuple[int, str]]:
    found = set()
    result: list[tuple[int, str]] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        for m in SOURCE_PATH.finditer(line):
            path = m.group().rstrip(".,;:")
            if path not in eligible:
                continue
            key = (line_no, path)
            if key not in found:
                found.add(key)
                result.append(key)
    return result


def role_frame() -> tuple[dict[str, dict], dict[str, str], list[dict], dict]:
    roster = frame.committed_paths(ROOT, PIN)
    existing = {
        path: oid
        for path, oid in sorted(roster.items())
        if Path(path).suffix.lower() in frame.REVIEWABLE_SUFFIXES
        and frame.proposed_family(path)[0].startswith("REVIEW")
    }
    raw = read_all_git_blobs(existing)
    eligible: dict[str, dict] = {}
    exclusions: list[dict] = []
    for path, oid in sorted(existing.items()):
        blob = raw[path]
        try:
            text = blob.decode("utf8", "strict") if blob else None
        except UnicodeDecodeError:
            text = None
        if text == "":
            text = None
        reason = exclude_reason(path, text)
        if reason:
            exclusions.append({"source_path": path, "reason": reason})
            continue
        eligible[path] = {
            "source_path": path,
            "git_blob_oid": oid,
            "source_sha256": sha256(blob).hexdigest(),
            "byte_count": len(blob),
            "stratum": stratum(path),
            "path_role_hint_not_semantic_authority": frame.proposed_family(path)[1],
        }
    return eligible, {
        path: raw[path].decode("utf8", "strict")
        for path in eligible
    }, exclusions, {
        "tracked_at_ref": len(roster),
        "reviewable_before_text_and_exclusions": len(existing),
        "eligible_by_stratum": dict(sorted(Counter(
            row["stratum"] for row in eligible.values()
        ).items())),
    }


def expansion(
    eligible: dict[str, dict], texts: dict[str, str]
) -> tuple[dict[str, int], dict[str, dict]]:
    if not all(s in eligible for s in SEEDS):
        raise ValueError("W1_RULE_INFEASIBLE:MANDATORY_SEED_MISSING_OR_EXCLUDED:"+
                         repr([s for s in SEEDS if s not in eligible]))
    known = set(eligible)
    depths = {seed: 0 for seed in SEEDS}
    predecessor: dict[str, dict] = {}
    frontier = sorted(SEEDS)
    for layer in range(1, 5):
        next_candidates = {}
        for source in frontier:
            for line, target in path_links(texts[source], known):
                if target == source or target in depths:
                    continue
                link = {"predecessor_source": source, "predecessor_line": line,
                        "relation": "LITERAL_DOCUMENTARY_MENTION_NOT_GOVERNING"}
                key = (
                    sha256(("W1-EXPAND-v1\0"+target+"\0"+
                            eligible[target]["git_blob_oid"]).encode("utf8")).hexdigest(),
                    target, source, line,
                )
                if target not in next_candidates or key < next_candidates[target][0]:
                    next_candidates[target] = (key, link)
        ordered = sorted(
            next_candidates,
            key=lambda path: (
                sha256(("W1-EXPAND-v1\0"+path+"\0"+
                        eligible[path]["git_blob_oid"]).encode("utf8")).hexdigest(),
                path,
            ),
        )
        for target in ordered:
            depths[target] = layer
            predecessor[target] = next_candidates[target][1]
        frontier = ordered
        if not frontier:
            break
    return depths, predecessor


def select_build(
    eligible: dict[str, dict],
    distance: dict[str, int],
    predecessor: dict[str, dict],
) -> tuple[list[dict], dict]:
    by_stratum: dict[str, list[str]] = {k: [] for k in QUOTAS}
    for path, row in eligible.items():
        by_stratum[row["stratum"]].append(path)
    selected: set[str] = set(SEEDS)
    result = []
    diagnostics: dict[str, dict] = {}
    for group, (build_n, future_held_n) in QUOTAS.items():
        seeds_here = sorted(p for p in SEEDS if eligible[p]["stratum"] == group)
        if len(seeds_here) > build_n or len(by_stratum[group]) < build_n + future_held_n:
            raise ValueError(
                f"W1_RULE_INFEASIBLE:STRATUM_CAPACITY:{group}:"
                f"frame={len(by_stratum[group])}:build={build_n}:held={future_held_n}"
            )
        ranked = sorted(
            (p for p in by_stratum[group] if p not in SEEDS),
            key=lambda p: (
                distance.get(p, 99),
                sha256(("W1-BUILD-v1\0"+p+"\0"+
                        eligible[p]["git_blob_oid"]).encode("utf8")).hexdigest(),
                p,
            ),
        )
        selected_here = seeds_here + ranked[:build_n-len(seeds_here)]
        if len(selected_here) != build_n:
            raise ValueError("W1_RULE_INFEASIBLE:STRATUM_BUILD_MISSING")
        for p in selected_here:
            if p in selected and p not in SEEDS:
                raise ValueError("W1_DUPLICATE_SELECTION")
            selected.add(p)
            row = dict(eligible[p])
            row.update({
                "git_source_ref": PIN,
                "build": True,
                "bfs_distance": distance.get(p, 99),
                "citation_predecessor_not_semantic_dependency": predecessor.get(p),
                "selection_class": (
                    "MANDATORY_SEED" if p in SEEDS else
                    "CITED_BFS_FRONTIER" if p in distance else
                    "DETERMINISTIC_DISCONNECTED_STRATUM_BACKFILL"
                ),
                "accepted_j1_from_source_carrier": False,
                "accepted_natural_owner_j2_from_path": False,
            })
            result.append(row)
        diagnostics[group] = {
            "frame_count": len(by_stratum[group]),
            "build_count": build_n,
            "future_heldout_capacity": len(by_stratum[group]) - build_n,
            "future_heldout_quota": future_held_n,
            "disconnected_selected_count": sum(p not in distance for p in selected_here),
            "seed_count": len(seeds_here),
        }
    if len(result) != 60 or len(set(r["source_path"] for r in result)) != 60:
        raise ValueError("W1_RULE_INFEASIBLE:WRONG_BUILD_COUNT")
    return sorted(result, key=lambda r: r["source_path"]), diagnostics


def extracted_record(
    source: dict, lines: list[str], line: int, kind: str, extra: dict | None = None
) -> dict:
    assert 1 <= line <= len(lines)
    value = lines[line - 1]
    if len(value.encode("utf8")) > 20000:
        # Source remains fully available; prohibit misleading truncated
        # *literal* claims in this derived display-only extractor.
        raise ValueError("W1_UNBOUNDED_LITERAL_EVIDENCE_LINE")
    rec = {
        "id": sha256((source["source_path"] + "\0" + str(line) + "\0" +
                      kind + "\0" + str(extra or {})).encode("utf8")).hexdigest()[:24],
        "evidence_class": kind,
        "value_exact_source_line": value,
        "source_path": source["source_path"],
        "git_blob_oid": source["git_blob_oid"],
        "source_ref": PIN,
        "source_line": line,
        "source_line_sha256": sha256(value.encode("utf8")).hexdigest(),
        "accepted_governing_effect": False,
        "qualified_j2_relation": False,
    }
    if extra:
        rec.update(extra)
    return rec


def extract_source(source: dict, text: str, frame_paths: set[str]) -> tuple[list[dict], dict]:
    lines = text.splitlines()
    result = [{
        "id": "observable-" + sha256(source["source_path"].encode()).hexdigest()[:24],
        "evidence_class": "OBSERVABLE_GIT_BLOB",
        "source_path": source["source_path"],
        "source_ref": PIN,
        "git_blob_oid": source["git_blob_oid"],
        "source_sha256": source["source_sha256"],
        "byte_count": source["byte_count"],
        "accepted_governing_effect": False,
        "qualified_j2_relation": False,
    }]
    if source["source_path"] == "docs/DECISIONS.md":
        starts = [
            (i + 1, m.group(1))
            for i, line in enumerate(lines)
            if (m := DECISION.match(line))
        ]
        for j, (begin, decision_id) in enumerate(starts):
            end = starts[j + 1][0] if j + 1 < len(starts) else len(lines) + 1
            result.append(extracted_record(source, lines, begin, "SOURCE_REPORTED",
                                           {"reported_kind":"DECISION_IDENTIFIER",
                                            "source_local_id":decision_id}))
            for pos in range(begin+1,end):
                if lines[pos-1].startswith("**Status:**"):
                    result.append(extracted_record(source, lines, pos, "SOURCE_REPORTED",
                                                   {"reported_kind":"RAW_DECISION_STATUS",
                                                    "source_local_id":decision_id}))
                    break
            for pos in range(begin+1,end):
                if lines[pos-1].startswith("**Supersedes:**"):
                    result.append(extracted_record(source, lines, pos, "SOURCE_REPORTED",
                                                   {"reported_kind":"RAW_DECISION_SUPERSESSION",
                                                    "source_local_id":decision_id}))
    if source["source_path"].endswith(".md"):
        for pos, line in enumerate(lines[:48], 1):
            if HEADER.match(line):
                result.append(extracted_record(source, lines, pos, "SOURCE_REPORTED",
                                               {"reported_kind":"RAW_DOCUMENT_HEADER"}))
    all_links = [
        (line, target) for line, target in path_links(text, frame_paths)
        if target != source["source_path"]
    ]
    for line, target in all_links[:24]:
        result.append(extracted_record(
            source, lines, line, "SOURCE_REPORTED",
            {"reported_kind":"LITERAL_DOCUMENTARY_MENTION",
             "literal_target_path":target,
             "navigation_authority":False},
        ))
    suffix = Path(source["source_path"]).suffix.lower()
    defs = []
    if suffix in CODE_SUFFIXES:
        defs = [i + 1 for i, line in enumerate(lines) if DEFINITION.match(line)]
        for line in defs[:24]:
            result.append(extracted_record(
                source, lines, line, "DEFINITION_ONLY_NOT_EXECUTION",
                {"reported_kind":"CODE_OR_WORKFLOW_DEFINITION_NOT_PASS"},
            ))
    return result, {
        "source_path": source["source_path"],
        "unextracted_literal_links_are_unknown": max(0, len(all_links) - 24),
        "unextracted_definition_lines_are_unknown": max(0, len(defs) - 24),
    }


def common_s1() -> dict:
    result = pilot.source_relative_semantics()
    if (
        len(result["accepted_j1_effects"]) != 4
        or result["qualifying_j2_count"] != 1
        or result["production_j2_j3_qualified"] is not False
        or result["independent_model_actor_authentication"] is not False
    ):
        raise ValueError("W1_ACCEPTED_S1_LIMITS_VIOLATED")
    return {
        "id": "S1-ONLY-ACCEPTED-EXPERIMENTAL-CORE",
        "evidence_class": "ACCEPTED_EXPERIMENT_ONLY_WEAK_ASSURANCE",
        "experimental_only": True,
        "source_evidence_outside_build_s1_not_counted_as_carrier": True,
        "accepted_j1_effects": result["accepted_j1_effects"],
        "current_effects": result["current_effects"],
        "retired_effect": result["retired_effect"],
        "lineage": result["lineage"],
        "qualifying_j2_count": result["qualifying_j2_count"],
        "j2_assurance": result["j2_assurance"],
        "j3_status": result["j3_status"],
        "source_event_git": result["source_event_git"],
        "experimental_evidence_path":
            "experiments/r0_p03_navigation_probe/"
            "v03_real_pk_delegated_s1_j3_lifecycle_result_v01.json",
        "source_ref": PIN,
        "evidence_sha256": result["receipt_sha256"],
        "production_authority": False,
        "independent_actor_assurance": False,
    }


def compute() -> dict[str, bytes]:
    contract = check_rule()
    candidates, texts, exclusions, frame_diag = role_frame()
    distances, predecessors = expansion(candidates, texts)
    selected, per_stratum = select_build(candidates, distances, predecessors)
    complete = set(candidates)
    record_sets = []
    remainders = []
    for row in selected:
        records, remainder = extract_source(row, texts[row["source_path"]], complete)
        record_sets.extend(records)
        remainders.append(remainder)
    accepted = common_s1()
    if len([x for x in record_sets if x["evidence_class"].startswith("ACCEPTED")]) != 0:
        raise ValueError("W1_HISTORICAL_SOURCE_PROMOTED_TO_ACCEPTED")
    if any(r["evidence_class"] not in ALLOWED_CLASSES for r in record_sets):
        raise ValueError("W1_UNRECOGNIZED_EVIDENCE_CLASS")
    manifest = {
        "schema_version": 1,
        "classification": "WORLD_W1_BUILD_FROZEN_HELDOUT_RULE_FROZEN_NOT_DRAWN",
        "contract": contract,
        "build_source_count": len(selected),
        "heldout_draw_status": "NOT_DRAWN_PROHIBITED_UNTIL_POST_C_ARM",
        "heldout_future_target": 20,
        "predeclared_heldout_rule": (
            "W1_RULE.md Section 5; SHA256(W1-HELDOUT-v1 || NUL || "
            "C_arm_full_40_hex || NUL || path || NUL || git_blob_oid)"
        ),
        "source_role_parity_is_stratum_sampling_not_semantic_admission": True,
        "metadata_no_experimental_j1_acceptance_from_paths": True,
        "per_stratum": per_stratum,
        "source_records": selected,
        "historical_65_source_research217_world_separate": True,
        "primary_gold": None,
        "score": None,
    }
    substrate = {
        "schema_version":1,
        "classification": "W1_SHARED_MECHANICAL_SOURCE_RELATIVE_SEMANTIC_EVIDENCE",
        "contract": contract,
        "build_manifest_sha256": sha256(canonical(manifest)).hexdigest(),
        "source_count":len(selected),
        "source_reported_records":record_sets,
        "bounded_unextracted_unknown_remainder":remainders,
        "only_accepted_experiment_core":accepted,
        "derived_orientation":{
            "status":"GENERATED_NON_GOVERNING",
            "source_records":[
                {"path":row["source_path"],
                 "role_hint_not_authority":row["path_role_hint_not_semantic_authority"]}
                for row in selected
            ],
            "core_current_effects":accepted["current_effects"],
            "unknowns":"SOURCE_BOUNDED_UNKNOWN",
            "source_revision":PIN,
            "false_authority_prevention":True,
        },
        "no_production_acceptance_or_realization":True,
    }
    excluded = {
        "schema_version":1,
        "classification":"W1_PRIOR_TO_TASKS_EXCLUSION_EVIDENCE_NOT_GOLD",
        "contract":contract,
        "frame_counts":frame_diag,
        "reached_by_literal_citations_within_four_hops":len(distances),
        "reasons":dict(sorted(Counter(x["reason"] for x in exclusions).items())),
        "excluded_path_records":exclusions,
        "build_predeclared_future_heldout_capacity":per_stratum,
        "heldout_identity_exposed":False,
    }
    return {
        "manifest":canonical(manifest),
        "substrate":canonical(substrate),
        "exclusions":canonical(excluded),
    }


class W1CommonRuntime:
    """Equal full-byte, source/citation/semantic connector for all five labels.

    No actual navigation-arm-specific signals are exposed or inferred. B4 is
    only a common-parity label here, not a claimed neural arm.
    """

    def __init__(self, arm: str, payload: dict[str, bytes]):
        if arm not in ("B0", "B1", "B2", "B3", "B4"):
            raise ValueError("W1_UNKNOWN_ARM_LABEL")
        self.arm = arm
        self.manifest = json.loads(payload["manifest"].decode("utf8"))
        self.substrate = json.loads(payload["substrate"].decode("utf8"))
        self.rows = {r["source_path"]: r for r in self.manifest["source_records"]}
        self.contents = {}
        # Opening only the 60 exact original Git blobs is a live source
        # operation bound by original SHA; no mutable worktree reads.
        for path, row in self.rows.items():
            raw = git(["show", f"{PIN}:{path}"])
            if sha1git(raw) != row["git_blob_oid"] or sha256(raw).hexdigest() != row["source_sha256"]:
                raise ValueError("W1_COMMON_RUNTIME_ORIGINAL_GIT_SOURCE_DRIFT")
            self.contents[path] = raw.decode("utf8")

    def list_sources(self) -> list[str]:
        return sorted(self.rows)

    def read(self, path: str) -> dict:
        if path not in self.rows:
            raise ValueError("W1_SOURCE_NOT_IN_FROZEN_BUILD")
        return {"source_path":path,"content":self.contents[path],
                "source_ref":PIN,"git_blob_oid":self.rows[path]["git_blob_oid"]}

    def search(self, query: str, limit: int = 5) -> list[dict]:
        if not isinstance(query,str) or not query.strip() or len(query)>80:
            raise ValueError("W1_QUERY_LIMIT")
        if type(limit) is not int or not 1 <= limit <= 20:
            raise ValueError("W1_RESULT_BUDGET")
        needle = query.casefold()
        matches = []
        for path in sorted(self.contents):
            for i, line in enumerate(self.contents[path].splitlines(),1):
                if needle in line.casefold():
                    matches.append({"source_path":path,"source_ref":PIN,
                                    "git_blob_oid":self.rows[path]["git_blob_oid"],
                                    "line":i,"line_sha256":sha256(line.encode("utf8")).hexdigest(),
                                    "authority_from_search":False})
                    if len(matches)>=limit:
                        return matches
        return matches

    def semantics(self) -> dict:
        return self.substrate

    def common_digest(self) -> str:
        return sha256(
            b"\0".join((json.dumps(self.manifest,sort_keys=True).encode("utf8"),
                        json.dumps(self.substrate,sort_keys=True).encode("utf8")))
        ).hexdigest()


def check_common_runtime(payload: dict[str, bytes]) -> dict:
    instances = {arm:W1CommonRuntime(arm,payload) for arm in ("B0","B1","B2","B3","B4")}
    common = {arm:instance.common_digest() for arm,instance in instances.items()}
    if len(set(common.values())) != 1:
        raise ValueError("W1_COMMON_CONNECTOR_PARITY_NOT_EQUAL")
    lists = [instance.list_sources() for instance in instances.values()]
    if len({tuple(v) for v in lists}) != 1 or len(lists[0]) != 60:
        raise ValueError("W1_COMMON_CONNECTOR_ROSTER_INCONSISTENT")
    samples = (
        "docs/DECISIONS.md",
        "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md",
        "tools/project_knowledge/identity.py",
    )
    for path in samples:
        reads = [instance.read(path) for instance in instances.values()]
        if len({sha256(canonical(x)).hexdigest() for x in reads}) != 1:
            raise ValueError("W1_COMMON_READ_MISMATCH")
    searches = [instance.search("project knowledge",limit=5) for instance in instances.values()]
    if len({sha256(canonical(x)).hexdigest() for x in searches}) != 1:
        raise ValueError("W1_COMMON_LEXICAL_MISMATCH")
    if len({sha256(canonical(instance.semantics())).hexdigest()
            for instance in instances.values()}) != 1:
        raise ValueError("W1_COMMON_SEMANTIC_MISMATCH")
    return {"labels":list(instances),"common_digest":next(iter(common.values())),
            "read_list_search_semantics_parity":True,
            "full_source_bytes":True,
            "arm_specific_ranking_or_model_frozen":False}


def main() -> None:
    payload = compute()
    # Two independent generations in one invocation are byte compared before
    # writing any result. No input manifest path may be selected by tuning.
    again = compute()
    if payload != again:
        raise ValueError("W1_RULE_NONDETERMINISM")
    parity = check_common_runtime(payload)
    for key, path in OUTPUTS.items():
        if path.exists():
            if path.read_bytes() != payload[key]:
                raise ValueError("W1_CREATE_ONLY_RECEIPT_CONTENT_CONFLICT:" + key)
        else:
            with path.open("xb") as f:
                f.write(payload[key])
    manifest=json.loads(payload["manifest"])
    print(json.dumps({
        "status":manifest["classification"],
        "source_count":manifest["build_source_count"],
        "strata":{k:v["build_count"] for k,v in manifest["per_stratum"].items()},
        "disconnected_fallback":{k:v["disconnected_selected_count"]
                                  for k,v in manifest["per_stratum"].items()},
        "original_git_revision":PIN,
        "accepted_experiment_core_only":True,
        "heldout_drawn":False,
        "connector_parity":parity,
        "output_sha256":{k:sha256(v).hexdigest() for k,v in payload.items()},
    },sort_keys=True))


if __name__ == "__main__":
    main()
