"""Pinned, non-scored source-relation/closure assessment and neutral mapping.

No task prompts, selections, expected answers, independent judgments or scores.
Literal assertions are not accepted J2 coverage or independently adjudicated truth.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from . import role_frame_candidate as frame

SOURCE_REF = frame.SOURCE_REF
DESIGN_REF = "213e6db7d02debfbde37f8e45b4297849bc6089a"
LEDGER = "docs/DECISIONS.md"
SPEC028 = "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md"
UNKNOWN = "UNKNOWN_REQUIRES_INDEPENDENT_ADJUDICATION"
# Only direct declared lineage/currentness statements qualify for this provisional
# common-relation projection. Component-to-specification declarations are preserved
# in the audit and source text, but need prospective common-vs-B2 admission review.
PROVISIONAL_COMMON_RELATION_FAMILIES = frozenset({"SOURCE_DECLARED_SCOPED_SUPERSESSION"})
CONTRACT_SCOPE_REVIEW = {
    1: "PRODUCT_PERSISTENCE", 2: "PRODUCT_PERSISTENCE_IMPLEMENTATION_TOOLKIT",
    3: "PROJECT_BUILD_ENVIRONMENT", 4: "PRODUCT_KNOWLEDGE_INTERCHANGE",
    9: "PRODUCT_RETRIEVAL", 12: "PRODUCT_HORIZON", 13: "PRODUCT_CONTEXT",
    14: "PRODUCT_REASONING", 23: "PRODUCT_SOURCE_SUBSTRATE", 28: "PROJECT_KNOWLEDGE_SUPPORT",
}

# Review recipes bind actual source assertions, not lexical event eligibility.
# Every event is assessed; these are finite engineering predicates, not tasks.
EVENT_PREDICATES = {
    "cold_start_current_orientation": {
        "D-008": (108, 116), "D-020": (294, 300), "D-022": (334, 340),
        "D-023": (357, 364), "D-035": (989, 999), "D-036": (1051, 1066),
    },
    "impact_analysis_evolution": {"D-003": (35, 39), "D-011": (148, 156),
                                  "D-015": (203, 214), "D-036": (1091, 1097)},
    "exact_source_authority_recovery": {
        "D-003": (35, 39), "D-007": (95, 99), "D-031": (639, 641),
        "D-032": (699, 722), "D-033": (815, 819), "D-034": (851, 864),
        "D-035": (989, 999), "D-036": (1041, 1066),
    },
}


def cite(roster, texts, path, start, end=None):
    end = start if end is None else end
    if not 1 <= start <= end <= len(texts[path]):
        raise ValueError("Invalid evidence span")
    return {"source_path": path, "git_commit": SOURCE_REF, "git_blob_oid": roster[path],
            "line_start": start, "line_end": end,
            "text": "\n".join(texts[path][start - 1:end])}


def numbered_references(text):
    """Explicit singular/plural IDs and bounded ranges; no implicit topic links."""
    result = []
    for m in re.finditer(r"\b(Specifications?|Foundations?|Research)\s+(\d{3})(?:[-–](\d{3}))?", text):
        kind = m[1].lower().rstrip("s")
        low, high = int(m[2]), int(m[3] or m[2])
        if high < low or high - low > 20:
            raise ValueError("Unbounded or reversed source reference range")
        result.extend((kind, n) for n in range(low, high + 1))
    return sorted(set(result))


def docstring_references(lines):
    """AST docstrings only; a comment/string/example is not a component claim."""
    tree = ast.parse("\n".join(lines))
    result = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not ast.get_docstring(node):
            continue
        expr = node.body[0]
        for i in range(expr.lineno - 1, expr.end_lineno):
            targets = [(kind, n) for kind, n in numbered_references(lines[i]) if kind == "specification"]
            if not targets:
                continue
            text = lines[i]
            if re.search(r"\b(?:not|never|may|might|could|example)\b", text, re.I):
                kind = "REFERENCE_ONLY_NOT_IMPLEMENTATION_EVIDENCE"
            elif re.search(r"\bimplements? Specification|\bimplementing Specifications?|\bimplementation of Specification", text):
                kind = "DECLARED_IMPLEMENTATION_INTENT"
            elif re.search(r"\brequired by Specification|\baccording to Specification", text):
                kind = "DECLARED_CONTRACT_DEPENDENCY"
            elif re.search(r"\b(?:services|values|adapter|repository|schema|implementation)\b.*\bfor .*Specification", text, re.I):
                kind = "DECLARED_COMPONENT_SCOPE"
            else:
                kind = "REFERENCE_ONLY_NOT_IMPLEMENTATION_EVIDENCE"
            result.append({"line": i + 1, "node": getattr(node, "name", "<module>"),
                           "kind": kind, "targets": targets})
    return sorted(result, key=lambda x: (x["line"], x["node"]))


def headers(roster, texts, path):
    return [cite(roster, texts, path, x["line"]) for x in frame.source_metadata(texts[path])]


def header_value(items, name):
    return next((x for x in items if x["text"].startswith(f"**{name}:**")), None)


def source_declaration(roster, texts, path, start=1, end=None):
    """Preserve incumbent structured facts, without calling them V03 effects."""
    end = len(texts[path]) if end is None else end
    block = texts[path][start - 1:end]
    begin = "<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->"
    finish = "<!-- PKA-STRUCTURED-DECLARATION-END -->"
    if begin in block and finish in block:
        low, high = block.index(begin) + start, block.index(finish) + start - 1
        span = cite(roster, texts, path, low + 1, high)
        return {"literal_declaration": json.loads(span["text"]), "source_basis": span,
                "accepted_v03_effect": False}
    if path.endswith(".json"):
        data = json.loads("\n".join(texts[path]))
        if isinstance(data, dict) and isinstance(data.get("authority_class"), str):
            line = next(i + 1 for i, text in enumerate(texts[path]) if re.match(r'\s*"authority_class"\s*:', text))
            return {"literal_declaration": {"authority_class": data["authority_class"]},
                    "source_basis": cite(roster, texts, path, line), "accepted_v03_effect": False}
    return {"literal_declaration": UNKNOWN, "accepted_v03_effect": False}


def closure_bundle(obligations):
    """Bound a local assertion's witnesses, never declare a minimum task corpus."""
    present = {name: bool(spans) for name, spans in obligations.items()}
    paths = {span["source_path"] for spans in obligations.values() for span in spans}
    return {"obligations": obligations, "local_witnesses_present": bool(present) and all(present.values()),
            "missing_obligations": sorted(k for k, v in present.items() if not v),
            "distinct_witness_path_count": len(paths), "minimum_task_closure": None,
            "future_task_obligations": ["independent_owner_need_or_frozen_event_rule",
                                        "question_scope_and_required_outputs",
                                        "source_role_and_permission_eligibility",
                                        "applicable_normative_dependencies_and_conflict_resolution",
                                        "authority_currentness_at_requested_time",
                                        "independent_reference_entailment"],
            "task_answerability": UNKNOWN}


def map_carrier(record_id, role, witnesses, source_headers):
    first = witnesses[0]
    return {"id": record_id, "source_path": first["source_path"], "git_commit": SOURCE_REF,
            "git_blob_oid": first["git_blob_oid"],
            "information_role": {"value": role, "status": "ENGINEERING_MAPPING_NOT_SOURCE_ACCEPTANCE"},
            "natural_owner": {"assertion_home": record_id,
                              "source_position": {k: v for k, v in first.items() if k != "text"},
                              "canonical_fact_owner": UNKNOWN},
            "evidence_class": {"value": "PINNED_SOURCE_ASSERTION", "independent_reference": False},
            "source_eligibility": {"status": "PENDING_ROLE_PERMISSION_AND_CONTAMINATION_REVIEW",
                                   "explicit_path_exclusion_hint": frame.leakage_reason(first["source_path"]),
                                   "navigation_contamination_review": first["source_path"] in frame.SPECIAL_NAVIGATION},
            "authority_currentness_basis": {"literal_source_headers": source_headers,
                                            "independently_adjudicated_authority": UNKNOWN},
            "governing_identity_reference": {"source_local_id": record_id,
                                             "v03_accepted_effect_id": UNKNOWN},
            "source_provenance": witnesses, "governing": False,
            "accepted_j2_coverage": False,
            "accepted_coverage_state": UNKNOWN,
            "completion_state": UNKNOWN, "verified_execution_receipts": UNKNOWN}


def common_mapping_issues(view, contract):
    """Shape/source safeguards supplement the existing parity guard, not an oracle."""
    issues = set(frame.shared_view_issues({a: copy.deepcopy(view) for a in ("B0", "B1", "B2", "B3")}))
    for section in ("records", "governing_effects", "shared_relations", "completion",
                    "j2_coverage", "evidence_receipts", "lexical_full_text", "derived_orientation"):
        if section not in view:
            issues.add("MISSING_COMMON_SECTION:" + section)
    for record in view.get("records", []):
        if any(field not in record for field in contract["exact_record_contract"]["carrier"]["required"]):
            issues.add("INCOMPLETE_CARRIER")
        if record.get("git_commit") != SOURCE_REF or not record.get("git_blob_oid"):
            issues.add("UNBOUND_CARRIER")
        issues.update(frame.authority_claim_issues(record))
        if record.get("governing") or record.get("accepted_j2_coverage"):
            issues.add("ENGINEERING_MAPPING_CANNOT_CREATE_ACCEPTANCE")
        provenance = record.get("source_provenance", [])
        if not provenance or any(record.get(k) != provenance[0].get(k)
                                 for k in ("source_path", "git_commit", "git_blob_oid")):
            issues.add("CARRIER_PROVENANCE_MISMATCH")
    for section, key in (("governing_effects", "governing_effect"), ("shared_relations", "shared_relation")):
        for record in view.get(section, []):
            if any(field not in record for field in contract["exact_record_contract"][key]["required"]):
                issues.add("INCOMPLETE_" + key.upper())
    if any(r.get("semantic_relation_family") == "REFERENCE_ONLY_NOT_IMPLEMENTATION_EVIDENCE"
           for r in view.get("shared_relations", [])):
        issues.add("REFERENCE_ONLY_AUDIT_LINK_IN_COMMON_RELATIONS")
    if any(r.get("semantic_relation_family") not in PROVISIONAL_COMMON_RELATION_FAMILIES
           for r in view.get("shared_relations", [])):
        issues.add("UNQUALIFIED_RELATION_IN_B0_COMMON_GRAPH")
    for effect in view.get("governing_effects", []):
        if effect.get("effect_reference", {}).get("accepted_v03_effect_id") != UNKNOWN:
            issues.add("UNSUPPORTED_V03_ACCEPTANCE_ID")
        statuses = [s["text"].removeprefix("**Status:**").strip()
                    for s in effect.get("source_provenance", []) if s["text"].startswith("**Status:**")]
        if effect.get("governing_status") not in statuses:
            issues.add("GOVERNING_STATUS_SOURCE_MISMATCH")
    orientation = view.get("derived_orientation", {})
    if any(field not in orientation for field in contract["exact_record_contract"]["derived_orientation"]["required"]):
        issues.add("INCOMPLETE_DERIVED_ORIENTATION")
    if orientation.get("derived_non_authoritative_label") is not True:
        issues.add("DERIVED_AUTHORITY_PROMOTION")
    return sorted(issues)


def provenance_issues(value, roster, texts):
    issues = set()
    if isinstance(value, dict):
        if {"line_start", "line_end", "text", "source_path"}.issubset(value):
            path = value["source_path"]
            if (path not in texts or value.get("git_commit") != SOURCE_REF
                    or value.get("git_blob_oid") != roster.get(path)
                    or not 1 <= value["line_start"] <= value["line_end"] <= len(texts[path])
                    or value["text"] != "\n".join(texts[path][value["line_start"] - 1:value["line_end"]])):
                issues.add("SOURCE_WITNESS_MISMATCH")
        for child in value.values():
            issues.update(provenance_issues(child, roster, texts))
    elif isinstance(value, list):
        for child in value:
            issues.update(provenance_issues(child, roster, texts))
    return sorted(issues)


def build_assessment(repo: Path, source_ref=SOURCE_REF):
    if source_ref != SOURCE_REF:
        raise ValueError("Retain the accepted exact content pin")
    roster = frame.committed_paths(repo, SOURCE_REF, ())
    index = frame.reference_index(roster)
    folder = "experiments/r0_p03_navigation_probe/"
    inputs = {folder + name for name in ("common_substrate_contract_candidate.json",
                                       "neutral_substrate_specimen_candidate.json")}
    design_roster = frame.committed_paths(repo, DESIGN_REF, ())
    design = frame.pinned_texts(repo, design_roster, inputs)
    contract = json.loads("\n".join(design[folder + "common_substrate_contract_candidate.json"]))
    specimen = json.loads("\n".join(design[folder + "neutral_substrate_specimen_candidate.json"]))
    code_paths = {p for p in roster if p.endswith(".py") and
                  (p.startswith("src/ads_system/") or p.startswith("tools/project_knowledge/"))}
    texts = frame.pinned_texts(repo, roster, code_paths | {LEDGER, SPEC028})
    events = frame.decision_events(texts[LEDGER])
    event_lookup = {e["event_id"]: e for e in events}
    def status_span(eid):
        event = event_lookup[eid]
        line = next(i for i in range(event["line_start"], event["line_end"] + 1)
                    if texts[LEDGER][i - 1].startswith("**Status:**"))
        return cite(roster, texts, LEDGER, line)
    code_refs = {p: docstring_references(texts[p]) for p in sorted(code_paths)}
    target_ids = {n for refs in code_refs.values() for ref in refs for _, n in ref["targets"]}
    target_paths = {p for n in target_ids for p in index.get(f"specification:{n:03}", [])}
    witness_paths = {r["source_path"] for r in specimen["records"]}
    texts.update(frame.pinned_texts(repo, roster, target_paths | witness_paths))
    plane_basis = [cite(roster, texts, SPEC028, 52, 68)]
    event_assessments, carriers, predicates, effects, lifecycle = [], {}, [], [], []
    for event in events:
        eid = event["event_id"]
        # All ledger entries, not a hand-picked task cohort.
        witness = cite(roster, texts, LEDGER, event["line_start"], min(event["line_start"] + 10, event["line_end"]))
        status = status_span(eid)
        successors = sorted(set(re.findall(r"\bD-\d{3}\b", event["raw_status"]))) if event["raw_status"].startswith("Superseded") else []
        for target_id in successors:
            target_status = [status_span(target_id)] if target_id in event_lookup else []
            lifecycle.append({"source_reference": eid, "target_reference": target_id,
                              "semantic_relation_family": "SOURCE_DECLARED_SCOPED_SUPERSESSION",
                              "source_provenance": [status],
                              "authority_basis": {"literal_status_clause": True, "independent_scope_adjudication": UNKNOWN},
                              "cross_plane_relevance": "NOT_ESTABLISHED_OR_WITHIN_PROJECT",
                              "closure": closure_bundle({"predecessor_scoped_status": [status],
                                                         "successor_status": target_status}),
                              "full_normative_or_task_closure": UNKNOWN})
        carriers[eid] = map_carrier(eid, "decision_record_source_assertion", [witness], [status])
        supported = []
        for category, recipes in EVENT_PREDICATES.items():
            if eid in recipes:
                start, end = recipes[eid]
                if not event["line_start"] <= start <= end <= event["line_end"]:
                    raise ValueError("Predicate witness outside its event")
                assertion = cite(roster, texts, LEDGER, start, end)
                obligations = {"source_assertion": [assertion], "declared_lifecycle": [status]}
                if successors:
                    obligations["named_successor_statuses"] = [status_span(s) for s in successors if s in event_lookup]
                if eid in {"D-035", "D-036"}:
                    obligations["incumbent_contract_authority"] = [cite(roster, texts, SPEC028, 6)]
                predicates.append({"event_id": eid, "category": category,
                                   "status": "EXPLICIT_EVIDENCE_GAP" if eid == "D-003" else "DECLARED_SOURCE_RELATION_NOT_INDEPENDENT_NEED",
                                   "closure": closure_bundle(obligations)})
                supported.append(category)
        origin = "OWNER_ORIGIN_NOT_ATTESTED_BY_REVIEWED_EVENT"
        origin_evidence = []
        if eid in {"D-035", "D-036"}:
            origin = "REPORTED_EXPLICIT_OWNER_SELECTION_NOT_ORIGINAL_INFORMATION_NEED"
            origin_evidence = [cite(roster, texts, LEDGER, 957 if eid == "D-035" else 1037)]
        subject = UNKNOWN
        scope = UNKNOWN
        lineage = UNKNOWN
        if eid in {"D-035", "D-036"}:
            selection = origin_evidence[0]
            subject = {"literal_selected_target": re.search(r"`([^`]+)`", selection["text"])[1],
                       "basis": selection}
            scope = {"interpretation": "SOURCE_DECLARED_LOGICAL_SELECTION_NOT_OPERATIONAL_CUTOVER",
                     "basis": cite(roster, texts, LEDGER, 989, 999) if eid == "D-035" else cite(roster, texts, LEDGER, 1051, 1066)}
            if eid == "D-036":
                lineage = {"relation": "HISTORICAL_D035_RETAINED_RECONCILIATION_REQUIRED_NOT_AUTOMATIC_SUPERSESSION",
                           "basis": cite(roster, texts, LEDGER, 1091, 1097)}
        effects.append({"effect_reference": {"source_record": eid, "accepted_v03_effect_id": UNKNOWN},
                        "exact_subject_reference": subject, "governing_status": event["raw_status"],
                        "scope": scope, "lineage_reference": lineage,
                        "status_basis": "SOURCE_DECLARED_NOT_INDEPENDENT_AUTHORITY_ADJUDICATION",
                        "source_provenance": [status]})
        event_assessments.append({"event_id": eid, "raw_status": event["raw_status"],
                                  "source_provenance": [status], "owner_event_origin": origin,
                                  "owner_origin_evidence": origin_evidence,
                                  "independent_information_need": UNKNOWN,
                                  "supported_predicate_families": supported,
                                  "other_families": "NOT_DEMONSTRATED_BY_FINITE_REVIEW_RECIPES_NOT_IMPOSSIBLE",
                                  "task_admission": "DEFER_ORIGIN_SCOPE_CLOSURE_AND_REFERENCE"})
    relations, code_inventory = lifecycle, []
    for path, refs in code_refs.items():
        code_inventory.append({"source_path": path, "git_blob_oid": roster[path],
                               "declared_reference_count": len(refs),
                               "no_reference_meaning": "NO_MATCHING_DOCSTRING_ASSERTION_NOT_NO_RELATION"})
        for ref in refs:
            for _, n in ref["targets"]:
                targets = index.get(f"specification:{n:03}", [])
                target = targets[0] if len(targets) == 1 else None
                declaration = cite(roster, texts, path, ref["line"])
                target_headers = headers(roster, texts, target) if target else []
                identity = [cite(roster, texts, target, 1)] if target else []
                authority = header_value(target_headers, "Authority")
                scope = header_value(target_headers, "Scope")
                scope_role = CONTRACT_SCOPE_REVIEW.get(n, UNKNOWN) if scope else UNKNOWN
                strong = ref["kind"] != "REFERENCE_ONLY_NOT_IMPLEMENTATION_EVIDENCE"
                # This is a concrete documentation-to-component relation under a
                # source-declared package boundary, not an accepted J2 assertion.
                cross = (path.startswith("src/ads_system/") and strong and target is not None
                         and authority is not None and scope_role.startswith("PRODUCT_"))
                closure = closure_bundle({"component_declaration": [declaration],
                                          "contract_identity": identity,
                                          "declared_authority_scope": [authority] if authority else [],
                                          "project_product_package_boundary": plane_basis})
                dependencies = []
                if authority:
                    for kind, dep in numbered_references(authority["text"]):
                        key = f"{kind}:{dep:03}"
                        candidates = index.get(key, [])
                        dependencies.append({"reference": key, "targets": candidates,
                                             "status": "EXISTS_APPLICABILITY_NOT_ADJUDICATED" if len(candidates) == 1 else "MISSING_OR_AMBIGUOUS"})
                    for decision in sorted(set(re.findall(r"\bD-\d{3}\b", authority["text"]))):
                        dependencies.append({"reference": decision, "targets": [LEDGER + "#" + decision],
                                             "status": "LOCAL_RECORD_EXISTS_APPLICABILITY_NOT_ADJUDICATED" if decision in carriers else "MISSING_OR_AMBIGUOUS"})
                relation = {"source_reference": path + "#" + ref["node"],
                            "target_reference": target or f"UNRESOLVED:specification:{n:03}",
                            "semantic_relation_family": ref["kind"], "source_provenance": [declaration],
                            "authority_basis": {"source_assertion_only": True, "contract_headers": target_headers,
                                                "accepted_j2_coverage": False},
                            "contract_scope_review": {"role": scope_role, "source_basis": scope,
                                                      "independent_adjudication": False},
                            "cross_plane_relevance": "PROJECT_CONTRACT_TO_PRODUCT_COMPONENT_CANDIDATE" if cross else "NOT_ESTABLISHED_OR_WITHIN_PROJECT",
                            "closure": closure, "normative_header_dependencies": dependencies,
                            "full_normative_or_task_closure": UNKNOWN}
                relations.append(relation)
                for carrier_path in (path, target):
                    if carrier_path and carrier_path not in carriers:
                        spans = [declaration] if carrier_path == path else identity
                        carriers[carrier_path] = map_carrier(carrier_path, "component_self_declaration" if carrier_path == path else "declared_contract",
                                                             spans, headers(roster, texts, carrier_path))
    for rec in specimen["records"]:
        span = cite(roster, texts, rec["source_path"], rec["line_start"], rec["line_end"])
        if span["git_blob_oid"] != rec["git_blob_oid"] or span["text"] != rec["exact_source_line"]:
            raise ValueError("Existing specimen citation mismatch")
        # Preserve the established engineering witness, not an independently
        # accepted role or deployed V03 entity.
        carriers[rec["id"]] = map_carrier(rec["id"], rec["role"], [span], headers(roster, texts, rec["source_path"]))
    for record_id, record in carriers.items():
        path = record["source_path"]
        if path == LEDGER:
            event_id = "D-035" if record_id == "GOV_D035" else "D-036" if record_id == "GOV_D036" else record_id
            event = event_lookup[event_id]
            declaration = source_declaration(roster, texts, path, event["line_start"], event["line_end"])
        else:
            declaration = source_declaration(roster, texts, path)
        record["source_declared_identity_and_authority_class"] = declaration
    core = json.loads("\n".join(texts["docs/project_knowledge/generated/current_state_core.json"]))
    routing = json.loads("\n".join(texts["docs/current_routing.json"]))
    source_manifest = {p: roster[p] for p in sorted(texts)}
    common_relation_fields = contract["exact_record_contract"]["shared_relation"]["required"]
    # Unaccepted code-to-contract intent, dependency and component-scope edges
    # might be B2-like navigation additions. They remain inspectable audit data
    # and equal lexical source bytes, not typed baseline B0 graph advantages.
    common_relations = [{k: r[k] for k in common_relation_fields} for r in relations
                        if r["semantic_relation_family"] in PROVISIONAL_COMMON_RELATION_FAMILIES]
    common = {"source_ref": SOURCE_REF, "capabilities": list(frame.CAPABILITIES),
              "projection_authority_rule": "This engineering projection creates no acceptance. governing=false and accepted_j2_coverage=false are no-claim flags, not revocation or proof of absence of underlying source authority/coverage. Literal source declarations/status remain scoped source evidence.",
              "records": list(carriers.values()), "shared_relations": common_relations,
              "governing_effects": effects,
              "completion": {"state": UNKNOWN, "source_status_is_not_governing_completion": True},
              "j2_coverage": {"accepted_coverage": UNKNOWN, "declared_associations": "shared_relations",
                              "existing_synthetic_analogue_is_not_accepted": True},
              "evidence_receipts": {"verified_execution_result": UNKNOWN, "source_assertions_retained": True},
              "lexical_full_text": {"source_manifest": source_manifest, "access": "pinned_texts Git reader; no arm service or ranked index"},
              "derived_orientation": {"source_head_or_checkpoint": SOURCE_REF,
                                      "generated_from_source_digests": source_manifest,
                                      "derived_non_authoritative_label": True,
                                      "current_governing_summary": {"independent_adjudication": UNKNOWN,
                                                                    "incumbent_and_selected_witnesses": ["GOV_D036", "INCUMBENT_SPEC028"]},
                                      "navigation_entry_points": [LEDGER, SPEC028],
                                      "staleness_visible": {"legacy_core": frame.derived_checkpoint_status(core, routing),
                                                            "legacy_checkpoint": core["active_workstream"]["execution_anchor"]["checkpoint"],
                                                            "pinned_routing_checkpoint": routing["current_checkpoint"],
                                                            "this_view": "SOURCE_BOUND_DIAGNOSTIC_NOT_OPERATIONAL_AUTHORITY"}}}
    views = {arm: copy.deepcopy(common) for arm in ("B0", "B1", "B2", "B3", "B4")}
    if provenance_issues([common, predicates, event_assessments], roster, texts):
        raise ValueError("Source witness mismatch")
    cross = [r for r in relations if r["cross_plane_relevance"] == "PROJECT_CONTRACT_TO_PRODUCT_COMPONENT_CANDIDATE"]
    return {"classification": "NON_SCORED_EXPOSED_ENGINEERING_NOT_TASKS_GOLD_OR_FIXTURE",
            "source_ref": SOURCE_REF, "design_ref": DESIGN_REF,
            "design_input_blobs": {p: design_roster[p] for p in sorted(inputs)},
            "assessment_rule": "Source assertions and typed relation witnesses; no lexical-event quota or selected twelve",
            "event_assessments": event_assessments, "event_predicate_witnesses": predicates,
            "code_population": code_inventory, "declared_relation_counts": dict(Counter(r["semantic_relation_family"] for r in relations)),
            "code_reference_relation_count": sum(len(ref["targets"]) for refs in code_refs.values() for ref in refs),
            "relation_audit": relations,
            "audit_only_relation_count": len(relations) - len(common_relations),
            "common_relation_admission": "ONLY_SOURCE_DECLARED_SCOPED_SUPERSESSION_PROVISIONAL; CODE_TO_CONTRACT_B0_VS_B2_UNQUALIFIED",
            "category_evidence": {**{c: {"event_predicate_count": sum(p["category"] == c for p in predicates),
                                           "explicit_gap_count": sum(p["category"] == c and p["status"] == "EXPLICIT_EVIDENCE_GAP" for p in predicates),
                                           "independently_eligible_need_count": None} for c in EVENT_PREDICATES},
                                  "cross_plane_discovery": {"source_declared_product_links": len(cross),
                                                            "distinct_contracts": len({r["target_reference"] for r in cross}),
                                                            "distinct_components": len({r["source_reference"].split("#")[0] for r in cross}),
                                                            "independently_eligible_need_count": None,
                                                            "category_definition_and_independence": UNKNOWN}},
            "known_gaps": {"D003_exact_visibility_change_event": "SOURCE_EXPLICITLY_NOT_PRESERVED_IN_THIS_RECORD",
                           "raw_owner_information_need": "NOT_ATTESTED_BY_ANY_REVIEWED_LEDGER_ENTRY",
                           "whole_repository_impossibility": "NOT_DEMONSTRATED",
                           "Research500_cross_plane_stratification": "J1_J2_J3_PROJECT_CONTROL_NOT_AUTOMATIC_PRODUCT_PROJECT_DISCOVERY"},
            "neutral_common_mapping": common, "common_mapping_issues": common_mapping_issues(common, contract),
            "equal_view_issues": frame.shared_view_issues(views),
            "equal_view_digest_sha256": hashlib.sha256(json.dumps(common, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
            "semantic_completeness": "REQUIRED_FIELDS_PRESENT_WITH_EXPLICIT_UNKNOWNS_NOT_INDEPENDENTLY_COMPLETE",
            "runtime_arm_parity": "NOT_EXECUTED_OR_QUALIFIED",
            "limitations": ["Finite reviewed predicates and docstring relation grammar are not exhaustive semantic discovery.",
                            "Declared implementation intent/dependency is source-owned evidence, not accepted J2 coverage or verified behavior.",
                            "Project contract to Product component is a candidate category interpretation needing prospective independent review.",
                            "Local witness bundles do not establish necessary/minimum task closure; normative dependencies and conflicts remain open.",
                            "Explicit unknown carrier values preserve missing facts; field completeness is not semantic qualification.",
                            "No task wording, selected twelve, reference answers, build/held-out draw, historical gold adjudication or arm execution."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--source-ref", default=SOURCE_REF)
    args = parser.parse_args()
    print(json.dumps(build_assessment(args.repository, args.source_ref), indent=2))


if __name__ == "__main__":
    main()
