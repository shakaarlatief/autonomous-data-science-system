"""Non-scored, source-ref-bound candidate R0-P03 role and modality census.

This deliberately replaces neither Research 513 nor the historical Markdown-only
feasibility module. It surveys textual public Git carriers by *potential*
information role, separates explicit evaluation leakage and auxiliary assets,
and reports candidate coverage without selecting any experimental source.

A path-family classification is only a review-routing hint. It cannot settle
source authority, currentness, accepted J1 identities, J2 realization links,
or whether a source is a legitimate gold/heldout carrier. A qualified non-arm
extractor must ground those conclusions in exact source provenance later.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

SOURCE_REF = "c57556a8bf993a1d327e9197acb7b7c745071cd8"
DIAGNOSTIC_DESIGN_REF = "912d6709e8f83591c0a5446531a8b0e38a59007d"
SOURCE_ROOTS = (
    "docs", "tools", "schemas", "src", "tests", "scripts",
    "frontend", "migrations", "experiments",
)
REVIEWABLE_SUFFIXES = frozenset({
    ".md", ".json", ".jsonl", ".py", ".ts", ".tsx", ".js", ".mjs",
    ".sql", ".toml", ".yaml", ".yml", ".txt", ".html", ".css",
    ".mako", ".ps1", ".sh",
})
REVISION = re.compile(r"[a-f0-9]{40}\Z")
NUMBERED = re.compile(r"^(\d{3})_")
MODEL_MESSAGES = re.compile(r"^docs/model_collaboration/threads/MC-0030/messages/(\d{3})_")
LEAKAGE_RESEARCH_IDS = frozenset({556, 557, 558, 559})
SPECIAL_NAVIGATION = frozenset({
    "docs/CURRENT_STATE.md",
    "docs/KNOWLEDGE_MAP.md",
    "docs/ARCHITECTURE_PROGRAM_OVERVIEW.md",
    "docs/CONTINUITY.md",
})


def numbered(path: str) -> int | None:
    hit = NUMBERED.match(path.rsplit("/", 1)[-1])
    return int(hit.group(1)) if hit else None


def leakage_reason(path: str) -> str | None:
    """Flag explicit contemporary R0-P03 content, not all historical research."""
    n = numbered(path)
    if path.startswith("experiments/r0_p03_") or path.startswith("tests/unit/test_r0_p03_"):
        return "P03_DESIGN_AND_HARNESS"
    if path.startswith("docs/research/") and (
        n in LEAKAGE_RESEARCH_IDS or "r0_p03_" in path.lower()
    ):
        return "P03_RESEARCH_DESIGN"
    if path.startswith("docs/checkpoints/") and n is not None and n >= 892:
        return "P03_CONTEMPORARY_CHECKPOINT"
    if path.startswith("docs/local_execution/validation/") and n is not None and n >= 244:
        return "P03_CONTEMPORARY_VALIDATION"
    match = MODEL_MESSAGES.match(path)
    if match and int(match.group(1)) >= 61:
        return "P03_MODEL_DESIGN_MESSAGE"
    return None


def proposed_family(path: str) -> tuple[str, str, str]:
    """Return eligibility bucket, path-derived role hint and lifecycle qualifier.

    No bucket means the path is authoritative. No code-source role proves
    REALIZES/COVERS and no existing generated view becomes current merely
    because the containing Git commit is the census reference.
    """
    if path == "docs/current_routing.json":
        return ("REVIEW", "operational_routing_source", "SOURCE_STATUS_REVIEW")
    if path in SPECIAL_NAVIGATION:
        return ("REVIEW_WITH_CONTAMINATION_CONTROL", "navigation_or_orientation", "SOURCE_STATUS_REVIEW")
    if path.startswith("docs/project_knowledge/generated/"):
        return ("REVIEW", "derived_project_knowledge_view", "DERIVED_NOT_GOVERNING")
    if path.startswith("docs/project_knowledge/"):
        return ("REVIEW", "incumbent_project_knowledge_source", "SOURCE_STATUS_REVIEW")
    if path == "docs/DECISIONS.md":
        return ("REVIEW", "governing_decision_carrier", "DECISION_SCOPE_REVIEW")
    if path.startswith("docs/specifications/"):
        return ("REVIEW", "specification_carrier", "CONTRACT_EFFECT_REVIEW")
    if path.startswith("docs/research/"):
        return ("REVIEW", "research_proposal_or_result", "ACCEPTANCE_CURRENTNESS_REVIEW")
    if path.startswith("docs/foundations/"):
        return ("REVIEW", "foundation", "ACCEPTANCE_CURRENTNESS_REVIEW")
    if path.startswith("docs/checkpoints/"):
        return ("REVIEW", "historical_progress_evidence", "HISTORICAL_CARRIER_NOT_CURRENTNESS")
    if path.startswith("docs/local_execution/") or path.startswith("docs/model_collaboration/"):
        return ("REVIEW", "engineering_or_collaboration_evidence", "EVIDENCE_SCOPE_REVIEW")
    if path.startswith("docs/source_universe/") or path.startswith("docs/cockpit/") or path.startswith("docs/methodological_knowledge/"):
        return ("REVIEW", "domain_or_structured_project_source", "SOURCE_STATUS_REVIEW")
    if path.startswith("schemas/"):
        return ("REVIEW", "machine_schema_realization", "NOT_PROVEN_COVERAGE")
    if path.startswith("tools/"):
        return ("REVIEW", "project_tool_realizer_candidate", "NOT_PROVEN_COVERAGE")
    if path.startswith("tests/"):
        return ("REVIEW", "verification_or_test_carrier", "RESULT_NOT_ASSUMED")
    if path.startswith("scripts/"):
        return ("REVIEW", "developer_tool_or_qualification", "NOT_PROVEN_COVERAGE")
    if path.startswith("migrations/"):
        return ("REVIEW", "database_migration_or_schema", "NOT_PROVEN_COVERAGE")
    if path.startswith("src/") or path.startswith("frontend/"):
        return ("REVIEW", "product_or_cross_plane_realizer", "NOT_PROVEN_COVERAGE")
    if path.startswith("experiments/"):
        return ("AUXILIARY_NOT_SAMPLED", "historical_fixture_or_probe", "NO_PROSPECTIVE_GOLD_INFERENCE")
    return ("REVIEW", "other_project_document", "SOURCE_STATUS_REVIEW")


def committed_paths(repo: Path, source_ref: str, roots: tuple[str, ...] = SOURCE_ROOTS) -> dict[str, str]:
    if not REVISION.fullmatch(source_ref):
        raise ValueError("source_ref must be an exact lowercase Git SHA")
    result = subprocess.run(
        ["git", "ls-tree", "-r", "-z", source_ref, "--", *roots],
        cwd=repo, check=True, capture_output=True,
    )
    paths = {}
    for entry in result.stdout.split(b"\0"):
        if not entry:
            continue
        meta, name = entry.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split(" ")
        path = name.decode("utf-8")
        if kind == "blob" and mode in {"100644", "100755"}:
            paths[path] = oid
    if not paths:
        raise ValueError("No Git source files at exact ref")
    return paths


def build_role_census(repo: Path, source_ref: str) -> dict[str, object]:
    tracked = committed_paths(repo, source_ref)
    groups: dict[str, Counter[str]] = defaultdict(Counter)
    lifecycle_hints: dict[str, Counter[str]] = defaultdict(Counter)
    withheld = Counter()
    provenance = []
    text_candidates = 0
    for path, oid in sorted(tracked.items()):
        if Path(path).suffix.lower() not in REVIEWABLE_SUFFIXES:
            withheld["NON_TEXT_OR_UNSUPPORTED"] += 1
            continue
        leaked = leakage_reason(path)
        if leaked:
            withheld[leaked] += 1
            continue
        bucket, role, lifecycle = proposed_family(path)
        groups[bucket][role] += 1
        lifecycle_hints[role][lifecycle] += 1
        if bucket.startswith("REVIEW"):
            text_candidates += 1
        provenance.append(f"{path}\0{oid}\n")
    return {
        "schema_version": 1,
        "classification": "UNFROZEN_ROLE_FRAME_CENSUS_NONSCORING",
        "source_ref": source_ref,
        "source_scope": list(SOURCE_ROOTS),
        "tracked_path_count": len(tracked),
        "candidate_text_path_count": text_candidates,
        "path_family_counts": {
            k: dict(sorted(v.items())) for k, v in sorted(groups.items())
        },
        "lifecycle_review_hints_by_role": {
            k: dict(sorted(v.items())) for k, v in sorted(lifecycle_hints.items())
        },
        "excluded_or_withheld_counts": dict(sorted(withheld.items())),
        "included_path_blob_digest_sha256": hashlib.sha256(
            "".join(provenance).encode("utf-8")
        ).hexdigest(),
        "limitations": [
            "Path-derived role hints do not certify currentness, governing authority, eligibility, accepted J1 identities, J2 coverage or evidence validity.",
            "Generated/derived paths must be checked against source digests and never elevated to governing authority.",
            "Contemporary R0-P03 design, tests and messages are withheld from the future closed scoring world; historical W5 has a separate 65-source immutable world.",
            "Eligible review paths are not an exact 60/20 corpus or task-source closure. No selected build or heldout path, seed, task, gold answer, evaluator or score is emitted.",
            "The source referee must separately resolve cross-plane Product/Project scope, historical status, privacy/permission and source role before any fixture freeze.",
        ],
    }


# Diagnostic signals, not task definitions, eligibility rules or semantic oracles.
TASK_SIGNALS = {
    "cold_start_current_orientation": r"\b(?:continuity|reconstruct\w*|current|orientation)\b",
    "cross_plane_discovery": r"\b(?:cross[- ]plane|cross[- ]system|product|source[- ]universe|interoperability|interchange)\b",
    "impact_analysis_evolution": r"\b(?:supersed\w*|evol\w*|migrat\w*|revis\w*|impact|successor)\b",
    "exact_source_authority_recovery": r"\b(?:authority|provenance|recover\w*|rollback|exact|integrity|verif\w*)\b",
}
CAPABILITIES = (
    "information_role_and_natural_owner", "accepted_effect_id_and_exact_governed_subject",
    "lineage_and_currentness", "completion", "j2_coverage", "evidence_receipts",
    "authority_class_labels", "lexical_full_text", "connector_readable_derived_orientation",
)
NAVIGATION_KEYS = frozenset({
    "research217_topical_memberships", "extra_editorial_about_links",
    "prospective_governed_navigation_concerns", "semantic_similarity_rankings",
    "topical_memberships", "preferred_subject", "concern_assignments", "semantic_rank",
    "controlled_topical_vocabulary", "source_owned_topical_memberships", "semantic_polyhierarchy",
    "optional_preferred_route", "editorial_carrier_to_governing_about_links",
    "bounded_cross_cutting_concern_vocabulary", "explicit_concern_assignments",
    "ranked_semantic_candidate_retrieval",
    "category_evidence", "cross_plane_relevance", "contract_scope_review", "supported_predicate_families",
})


def pinned_texts(repo: Path, roster: dict[str, str], paths: set[str]) -> dict[str, list[str]]:
    """One Git batch; verify returned blobs rather than reading mutable worktree."""
    oids = sorted({roster[p] for p in paths})
    if not oids:
        return {}
    raw = subprocess.run(["git", "cat-file", "--batch"], cwd=repo,
                         input=("\n".join(oids) + "\n").encode(),
                         capture_output=True, check=True).stdout
    decoded, offset = {}, 0
    for expected in oids:
        end = raw.index(b"\n", offset)
        oid, kind, size = raw[offset:end].decode("ascii").split()
        size = int(size)
        body = raw[end + 1:end + 1 + size]
        if (oid != expected or kind != "blob" or len(body) != size
                or hashlib.sha1(b"blob " + str(size).encode() + b"\0" + body).hexdigest() != oid
                or raw[end + 1 + size:end + 2 + size] != b"\n"):
            raise ValueError("Git batch blob integrity failure")
        decoded[oid] = body.decode("utf-8").splitlines()
        offset = end + 2 + size
    if offset != len(raw):
        raise ValueError("Unexpected Git batch trailer")
    return {p: decoded[roster[p]] for p in sorted(paths)}


def decision_events(lines: list[str]) -> list[dict]:
    starts = [(i, re.match(r"## (D-\d{3})\. ", line)) for i, line in enumerate(lines)]
    starts = [(i, m.group(1)) for i, m in starts if m]
    events = []
    for j, (start, event_id) in enumerate(starts):
        end = starts[j + 1][0] if j + 1 < len(starts) else len(lines)
        block = lines[start:end]
        status = next((x.removeprefix("**Status:**").strip() for x in block if x.startswith("**Status:**")), None)
        date = next((x.removeprefix("**Date:**").strip() for x in block if x.startswith("**Date:**")), None)
        signals = {name: [start + i + 1 for i, text in enumerate(block)
                          if re.search(pattern, text, re.I)] for name, pattern in TASK_SIGNALS.items()}
        events.append({"event_id": event_id, "line_start": start + 1, "line_end": end,
                       "raw_status": status, "raw_date": date, "lexical_signal_lines": signals,
                       "owner_mentioned": any(re.search(r"\bowner\b", x, re.I) for x in block)})
    return events


def source_metadata(lines: list[str]) -> list[dict]:
    """Literal header observations only; never infer acceptance from a path."""
    return [{"line": i + 1, "text": line} for i, line in enumerate(lines[:40])
            if re.match(r"\*\*(?:Status|Authority|Scope|Date|Supersedes|Basis):\*\*", line)]


def reference_index(roster: dict[str, str]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = defaultdict(list)
    for path in sorted(roster):
        for label, folder in (("research", "research"), ("specification", "specifications"),
                              ("foundation", "foundations"), ("checkpoint", "checkpoints")):
            if Path(path).parent.as_posix() == "docs/" + folder and numbered(path) is not None:
                index[f"{label}:{numbered(path):03}"].append(path)
    return dict(index)


def source_references(lines: list[str], origin: str, roster: dict[str, str], index: dict,
                      line_offset: int = 0) -> list[dict]:
    refs = []
    path_pattern = r"(?<![\w/])(?:docs|tools|schemas|src|tests|scripts|frontend|migrations|experiments|prototype_v0)/[^\s`<>\"\)\],;]*"
    number_pattern = r"\b(Research|Specification|Foundation|Checkpoint)\s+(\d{1,3})\b|\b(research|specification|foundation|checkpoint):(\d{1,3})\b"
    for i, line in enumerate(lines):
        tokens = [(m.group(0).rstrip(".,;:"), None) for m in re.finditer(path_pattern, line)]
        for m in re.finditer(number_pattern, line, re.I):
            label, n = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
            tokens.append((m.group(0), f"{label.lower()}:{int(n):03}"))
        for m in re.finditer(r"`([A-Z_]+\.md|pyproject\.toml)`", line):
            relative = (Path(origin).parent / m.group(1)).as_posix()
            tokens.append((relative if relative in roster else m.group(1), None))
        for m in re.finditer(r"\bpath:([A-Za-z0-9_.-]+\.(?:toml|md|json))\b", line):
            tokens.append((m.group(1), None))
        for token, numbered_ref in tokens:
            candidates = index.get(numbered_ref, []) if numbered_ref else ([token] if token in roster else [])
            status = "RESOLVED_FILE" if len(candidates) == 1 else "AMBIGUOUS_ID" if candidates else "MISSING"
            if not candidates and not numbered_ref and any(p.startswith(token.rstrip("/") + "/") for p in roster):
                status = "DIRECTORY_UNEXPANDED"
            refs.append({"line": line_offset + i + 1, "token": token,
                         "status": status, "targets": candidates})
    # A reference occurrence is evidence of a link, not a verified dependency.
    return sorted({json.dumps(r, sort_keys=True): r for r in refs}.values(), key=lambda r: (r["line"], r["token"]))


def distinct_event_capacity(category_events: dict[str, list[str]], quota: int = 3) -> int:
    """Maximum bipartite cardinality only. Never emit an assignment/task selection."""
    matched = {}
    def assign(slot, seen):
        for event in category_events[slot[0]]:
            if event in seen:
                continue
            seen.add(event)
            if event not in matched or assign(matched[event], seen):
                matched[event] = slot
                return True
        return False
    return sum(assign((category, n), set()) for category in sorted(category_events) for n in range(quota))


def shared_view_issues(views: dict[str, dict]) -> list[str]:
    issues = set()
    if set(views) not in ({"B0", "B1", "B2", "B3"}, {"B0", "B1", "B2", "B3", "B4"}):
        issues.add("ARM_SET_MISMATCH")
    def inspect(value):
        if isinstance(value, dict):
            if NAVIGATION_KEYS.intersection(value):
                issues.add("ARM_NAVIGATION_IN_SHARED_VIEW")
            for child in value.values():
                inspect(child)
        elif isinstance(value, list):
            for child in value:
                inspect(child)
    for view in views.values():
        if view.get("source_ref") != SOURCE_REF:
            issues.add("COMMON_SOURCE_REF_MISMATCH")
        if sorted(view.get("capabilities", [])) != sorted(CAPABILITIES):
            issues.add("COMMON_CAPABILITY_MISMATCH")
        inspect(view)
    if len({json.dumps(v, sort_keys=True, separators=(",", ":")) for v in views.values()}) > 1:
        issues.add("UNEQUAL_SHARED_VIEWS")
    return sorted(issues)


def authority_claim_issues(record: dict) -> list[str]:
    """Reject obvious promotions; a clean result is not an authority oracle."""
    issues = []
    if record.get("governing") and record.get("status") != "SOURCE_REVIEWED_ACCEPTED_GOVERNING":
        issues.append("UNSUPPORTED_GOVERNING_PROMOTION")
    forbidden_roles = {"unaccepted_physical_tree_research_proposal", "realizer_source_candidate",
                       "realization_schema_candidate", "test_implementation_source",
                       "incumbent_generated_identity_projection", "incumbent_generated_current_state_projection"}
    if record.get("governing") and record.get("role") in forbidden_roles:
        issues.append("NON_GOVERNING_SOURCE_ROLE")
    if record.get("governing") and not record.get("accepted_effect_reference"):
        issues.append("MISSING_ACCEPTED_EFFECT_REFERENCE")
    if record.get("accepted_j2_coverage") and (record.get("status") != "SOURCE_REVIEWED_ACCEPTED_J2"
                                               or not record.get("source_owned_coverage_reference")):
        issues.append("INFERRED_J2_COVERAGE")
    return issues


def b2_link_diagnostic(common: list[dict], extra: dict) -> str:
    def key(edge):
        return (tuple(sorted((edge["source_reference"], edge["target_reference"]))), edge.get("scope"))
    if extra.get("governing") or extra.get("accepted_j2_coverage"):
        return "INVALID_AUTHORITY_OR_COVERAGE"
    collisions = [edge for edge in common if key(extra) == key(edge)]
    if any(extra.get("semantic_relation_family") == edge.get("semantic_relation_family") for edge in collisions):
        return "DUPLICATE_OR_REVERSE_COMMON_RELATION"
    if collisions:
        return "COMMON_ENDPOINT_COLLISION_SEMANTICS_UNQUALIFIED"
    return "NON_DUPLICATE_ENDPOINTS_SEMANTICS_UNQUALIFIED"


def derived_checkpoint_status(core: dict, routing: dict) -> str:
    value = core.get("active_workstream", {}).get("execution_anchor", {}).get("checkpoint")
    current = routing.get("current_checkpoint")
    if value is None or current is None:
        return "FRESHNESS_UNVERIFIED"
    return "STALE_CHECKPOINT_MISMATCH" if value != current else "CHECKPOINT_MATCH_DIGEST_FRESHNESS_UNVERIFIED"


def build_capacity_parity_diagnostic(repo: Path, source_ref: str = SOURCE_REF) -> dict:
    if source_ref != SOURCE_REF:
        raise ValueError("Diagnostic requires the accepted historical role-frame pin")
    roster = committed_paths(repo, source_ref, ())
    frame = committed_paths(repo, source_ref)
    index = reference_index(roster)
    folder = "experiments/r0_p03_navigation_probe/"
    design_paths = {folder + name for name in ("common_substrate_contract_candidate.json",
                    "neutral_substrate_specimen_candidate.json", "independent_reference_method_candidate.json")}
    design_roster = committed_paths(repo, DIAGNOSTIC_DESIGN_REF, ())
    design = pinned_texts(repo, design_roster, design_paths)
    contract = json.loads("\n".join(design[folder + "common_substrate_contract_candidate.json"]))
    specimen = json.loads("\n".join(design[folder + "neutral_substrate_specimen_candidate.json"]))
    method = json.loads("\n".join(design[folder + "independent_reference_method_candidate.json"]))
    ledger = "docs/DECISIONS.md"
    texts = pinned_texts(repo, roster, {ledger})
    events = decision_events(texts[ledger])
    for event in events:
        event["references"] = source_references(texts[ledger][event["line_start"] - 1:event["line_end"]],
                                                ledger, roster, index, event["line_start"] - 1)
    direct = {p for e in events for r in e["references"] if r["status"] == "RESOLVED_FILE" for p in r["targets"]}
    witness_paths = {r["source_path"] for r in specimen["records"] + specimen["synthetic_relations"]}
    texts.update(pinned_texts(repo, roster, direct | witness_paths))
    neighborhoods = {p: source_references(texts[p], p, roster, index) for p in sorted(direct)}
    capacity = {}
    for category in TASK_SIGNALS:
        hinted = [e for e in events if e["lexical_signal_lines"][category]]
        linked = [e for e in hinted if any(r["status"] == "RESOLVED_FILE" for r in e["references"])]
        capacity[category] = {"lexical_hint_events": len(hinted), "hint_with_resolved_citation_events": len(linked),
                              "independently_answerable_task_count": None,
                              "qualification": "NOT_ESTABLISHED_SOURCE_CLOSURE_AND_INDEPENDENT_METHOD_REQUIRED"}
    for event in events:
        paths = {p for r in event["references"] if r["status"] == "RESOLVED_FILE" for p in r["targets"]}
        second = {p for first in paths for r in neighborhoods[first] if r["status"] == "RESOLVED_FILE" for p in r["targets"]}
        event["source_provenance"] = {"source_path": ledger, "git_blob_oid": roster[ledger], "git_commit": source_ref}
        event["referenced_path_role_hints"] = dict(Counter(proposed_family(p)[1] for p in sorted(paths)))
        event["observed_reference_neighborhood"] = {
            "direct_files": len(paths), "two_hop_files": len(paths | second | {ledger}),
            "direct_outside_role_frame": sorted(paths - set(frame)),
            "direct_auxiliary_or_quarantined": sorted(p for p in paths if leakage_reason(p) or proposed_family(p)[0] == "AUXILIARY_NOT_SAMPLED"),
            "two_hop_auxiliary_or_quarantined_count": sum(bool(leakage_reason(p)) or proposed_family(p)[0] == "AUXILIARY_NOT_SAMPLED" for p in second),
            "two_hop_exceeds_sixty": len(paths | second | {ledger}) > 60,
            "complete_task_closure": False,
        }
        event["gaps"] = ["NO_INDEPENDENT_INFORMATION_NEED_OR_MINIMAL_SOURCE_CLOSURE",
                         "STATUS_DATE_OWNER_MENTION_ARE_NOT_VERBATIM_OWNER_EVENT_ATTESTATION",
                         "NUMBER_SHORTHAND_AND_LOCAL_D_IDS_NOT_EXPANDED; TWO_HOP_FRONTIER_NOT_CLOSED"]
        if not paths:
            event["gaps"].append("NO_RESOLVED_EXTERNAL_FILE_CITATION")
        if any(r["status"] != "RESOLVED_FILE" for r in event["references"]):
            event["gaps"].append("MISSING_AMBIGUOUS_OR_DIRECTORY_REFERENCE")
    witness_results = []
    for record in specimen["records"] + specimen["synthetic_relations"]:
        path = record["source_path"]
        line = record["line_start"]
        quoted = record.get("exact_source_line", record.get("source_line"))
        valid = (roster[path] == record["git_blob_oid"] and 1 <= line <= len(texts[path])
                 and texts[path][line - 1] == quoted)
        if not valid:
            raise ValueError("Specimen citation differs from pinned source")
        witness_results.append({"id": record["id"], "source_path": path, "git_blob_oid": roster[path],
                                "line": line, "citation_exact": valid,
                                "candidate_status": record["status"], "authority_claim_issues": authority_claim_issues(record)})
    required = contract["exact_record_contract"]["carrier"]["required"]
    missing = {field: sum(field not in record for record in specimen["records"]) for field in required}
    core_path = "docs/project_knowledge/generated/current_state_core.json"
    routing_path = "docs/current_routing.json"
    core, routing = json.loads("\n".join(texts[core_path])), json.loads("\n".join(texts[routing_path]))
    statuses = dict(Counter(e["raw_status"] or "MISSING" for e in events))
    return {
        "classification": "EXPOSED_ENGINEERING_DIAGNOSTIC_NOT_TASKS_GOLD_OR_FIXTURE",
        "engineering_design_ref": DIAGNOSTIC_DESIGN_REF,
        "engineering_design_input_blobs": {p: design_roster[p] for p in sorted(design_paths)},
        "retained_scientific_gates": method["original_gate"],
        "source_ref": source_ref, "ledger_blob_oid": roster[ledger], "event_count": len(events),
        "category_signal_rules_not_eligibility": TASK_SIGNALS, "raw_status_counts": statuses,
        "category_capacity": capacity,
        "distinct_event_signal_capacity_upper_bound": distinct_event_capacity({
            c: [e["event_id"] for e in events if e["lexical_signal_lines"][c]
                and any(r["status"] == "RESOLVED_FILE" for r in e["references"])] for c in TASK_SIGNALS}),
        "events": events,
        "source_header_observations": {
            p: {"git_commit": source_ref, "git_blob_oid": roster[p],
                "path_role_hint": proposed_family(p)[1],
                "literal_metadata_first_forty_lines": source_metadata(texts[p]),
                "authority_or_task_eligibility_certified": False}
            for p in sorted(direct | witness_paths)
        },
        "substrate_audit": {
            "contract_id": contract["contract_id"], "contract_design_basis_ref": contract["source_ref"],
            "contract_design_basis_differs_from_content_pin": contract["source_ref"] != source_ref,
            "shared_capabilities_complete": sorted(contract["shared_capabilities"]["all_arms"]) == sorted(CAPABILITIES),
            "shared_capabilities": list(CAPABILITIES), "source_citation_witnesses": witness_results,
            "carrier_required_fields_absent_in_specimen": missing,
            "synthetic_j2_analogues": len(specimen["synthetic_relations"]),
            "accepted_j2_coverage_demonstrated_by_specimen": False,
            "derived_checkpoint_status": derived_checkpoint_status(core, routing),
            "derived_checkpoint": core["active_workstream"]["execution_anchor"]["checkpoint"],
            "source_routing_checkpoint": routing["current_checkpoint"],
            "B2_actual_additions": "NOT_AUTHORED_OR_QUALIFIED",
            "B1_B3_semantic_distinctness": "NOT_INFERRED_FROM_DIFFERENT_LABELS",
            "B4": "CONDITIONAL_NOT_IMPLEMENTED_OR_EQUALIZED",
            "independent_semantics_and_runtime_parity": "NOT_QUALIFIED",
        },
        "limitations": [
            "All 36 ledger events are examined; lexical signals and path-role hints are not answerability or cross-plane facts. No tasks, prompts, labels, answers or selected twelve are emitted.",
            "Maximum matching is a cardinality ceiling over cited lexical hints, not a chosen task set or independent capacity proof.",
            "Direct and two-hop reference neighborhoods are neither minimal necessary task closures nor complete dependency closures. Exceeding 60 warns against naive ingestion, not that every task is impossible.",
            "Raw accepted/superseded/proposed/implementation/test/derived interpretations and source identities remain separate. Citation equality does not establish semantic entailment or J2 acceptance.",
            "Literal source-header observations expose declared status/scope/authority, including missing headers; they are bounded to forty lines and are not source adjudication or a test-result receipt.",
            "Shared-view and B2 guards are diagnostic validators, not B0-B4 implementations, independent authority or a scorer. No runtime arm parity claim.",
            "Pinned source routing checkpoint 895 is historical evidence, not live Checkpoint 898. Level B acceptance governs this engineering work; no security infrastructure or gold custody operation occurs.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-ref", default=SOURCE_REF)
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--capacity-parity", action="store_true", help="Non-scored event/reference and substrate diagnostic at the existing pin")
    args = parser.parse_args()
    build = build_capacity_parity_diagnostic if args.capacity_parity else build_role_census
    print(json.dumps(build(args.repository.resolve(), args.source_ref), indent=2))


if __name__ == "__main__":
    main()
