from __future__ import annotations

import json
from pathlib import Path

from tools.project_knowledge.adapters.schema import SchemaValidator
from tools.project_knowledge.authority import resolve_authority
from tools.project_knowledge.declaration import BEGIN, END, parse_markdown
from tools.project_knowledge.model import (
    AuthorityClass,
    AuthorityEvidence,
    AuthorityQuery,
    AuthorityStatus,
    GovernedSource,
    Profile,
    RawDeclaration,
    Relation,
    Scope,
    SemanticId,
    SnapshotMode,
    SubstrateError,
)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixture.json"
RESULT = HERE / "result.json"
VALIDATOR = SchemaValidator()
LOCAL = SnapshotMode.WORKTREE_SNAPSHOT

def source(sid: str | None, *, path: str, scope=None, relations=()):
    data = {
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "T3_REGISTRY_PROBE",
        "authority_class": "canonical",
    }
    if sid is not None:
        data["semantic_id"] = sid
    if scope is not None:
        data["scope"] = scope
    if relations:
        data["relations"] = [
            {
                "mode": mode,
                "target": target,
                **({"scope": rel_scope} if rel_scope is not None else {}),
            }
            for mode, target, rel_scope in relations
        ]
    raw = RawDeclaration(data)
    diagnostics = VALIDATOR.validate(raw)
    assert not diagnostics, diagnostics
    return GovernedSource(
        path,
        Profile.SEMANTIC_SOURCE,
        AuthorityClass.CANONICAL,
        data["kind"],
        raw,
        LOCAL,
        SemanticId(sid) if sid else None,
        Scope(scope) if scope is not None else None,
        tuple(
            Relation(mode, SemanticId(target), Scope(rel_scope) if rel_scope is not None else None)
            for mode, target, rel_scope in relations
        ),
        None,
        None,
    )

def evidence(sources):
    return [AuthorityEvidence(s.carrier_path, True, "FRESH", None) for s in sources]

def resolve(sources, facets):
    query = AuthorityQuery("govern", "decision", Scope(facets), "consequential")
    return resolve_authority(query, sources, snapshot_mode=LOCAL, evidence=evidence(sources))

def resolve_required(sources, semantic_id: str):
    query = AuthorityQuery(
        "govern",
        "registry-item",
        Scope({}),
        "consequential",
        required_authorities=(SemanticId(semantic_id),),
    )
    return resolve_authority(query, sources, snapshot_mode=LOCAL, evidence=evidence(sources))

def option_a(fixture):
    base = source("D-011", path="docs/decisions/d_011.md")
    successors = [
        source(
            item["id"],
            path=f"docs/decisions/{item['id'].lower().replace('-', '_')}.md",
            scope={"decision_domain": item["scope"]},
            relations=[("REPLACE", "D-011", {"decision_domain": item["scope"]})],
        )
        for item in fixture["d011"]["successors"]
    ]
    sources = [base, *successors]
    rows = []
    for item in fixture["d011"]["successors"]:
        result = resolve(sources, {"decision_domain": item["scope"]})
        rows.append({
            "scope": item["scope"],
            "status": result.status.value,
            "governing_ids": sorted(
                s.semantic_id.value for s in result.receipt.governing_sources
                if s.semantic_id is not None
            ) if result.receipt else [],
        })
    residual = resolve(sources, {"decision_domain": fixture["d011"]["residual_scope"]})
    residual_ids = sorted(
        s.semantic_id.value for s in residual.receipt.governing_sources
        if s.semantic_id is not None
    ) if residual.receipt else []
    ab032 = source(
        fixture["ab032"]["proposed_identity"],
        path="docs/architecture_backlog/ab_032_git_branch_lifecycle_policy.md",
    )
    ab032_required = resolve_required([ab032], fixture["ab032"]["proposed_identity"])
    ab032_ids = sorted(
        s.semantic_id.value for s in ab032_required.receipt.governing_sources
        if s.semantic_id is not None
    ) if ab032_required.receipt else []

    return {
        "all_scoped_successors_resolve": all(
            row["status"] == "RESOLVED" and row["governing_ids"] == [item["id"]]
            for row, item in zip(rows, fixture["d011"]["successors"])
        ),
        "residual_base_resolves": residual.status == AuthorityStatus.RESOLVED and residual_ids == ["D-011"],
        "ab032_first_class_required_identity_resolves": (
            ab032_required.status == AuthorityStatus.RESOLVED
            and ab032_ids == [fixture["ab032"]["proposed_identity"]]
        ),
        "rows": rows,
        "residual": {
            "status": residual.status.value,
            "governing_ids": residual_ids,
        },
        "ab032_required_identity": {
            "status": ab032_required.status.value,
            "governing_ids": ab032_ids,
        },
    }

def option_b():
    first = {
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "DECISION",
        "authority_class": "canonical",
        "semantic_id": "D-011",
    }
    second = {
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "DECISION",
        "authority_class": "canonical",
        "semantic_id": "D-028",
    }
    text = (
        "# Aggregate registry\n\n"
        + BEGIN + "\n" + json.dumps(first) + "\n" + END + "\n\n"
        + "## second\n\n"
        + BEGIN + "\n" + json.dumps(second) + "\n" + END + "\n"
    ).encode("utf-8")
    try:
        parse_markdown(text)
    except SubstrateError as exc:
        return {"accepted_by_current_parser": False, "error_code": exc.code}
    return {"accepted_by_current_parser": True, "error_code": None}

def option_c(fixture):
    base = source(None, path="docs/DECISIONS.md")
    item = fixture["d011"]["successors"][0]
    successor = source(
        item["id"],
        path="docs/decisions/d_028.md",
        scope={"decision_domain": item["scope"]},
        relations=[("REPLACE", "D-011", {"decision_domain": item["scope"]})],
    )
    relation_result = resolve([base, successor], {"decision_domain": item["scope"]})

    ab032_anchor_only = source(None, path=fixture["ab032"]["legacy_carrier"])
    ab032_required = resolve_required(
        [ab032_anchor_only],
        fixture["ab032"]["proposed_identity"],
    )
    return {
        "status": relation_result.status.value,
        "diagnostic_codes": sorted(d.code for d in relation_result.diagnostics),
        "typed_relation_target_resolves": relation_result.status == AuthorityStatus.RESOLVED,
        "ab032_required_identity_status": ab032_required.status.value,
        "ab032_anchor_only_satisfies_required_identity": (
            ab032_required.status == AuthorityStatus.RESOLVED
        ),
        "ab032_required_identity_diagnostics": sorted(
            d.code for d in ab032_required.diagnostics
        ),
    }

def main():
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    a = option_a(fixture)
    b = option_b()
    c = option_c(fixture)

    result = {
        "schema_version": 1,
        "experiment": "W5-T3",
        "authority_class": "research_output",
        "source_boundary": fixture["source_boundary"],
        "option_a_selective_per_item": a,
        "option_b_multiple_declarations_one_carrier": b,
        "option_c_anchor_only": c,
        "qualitative_comparison": {
            "A": {
                "implementation_blast_radius": "LOW: native one-carrier/one-declaration/source-ID model",
                "reference_integrity": "HIGH: typed relations target stable semantic IDs",
                "move_rename_behavior": "SUPPORTED by existing identity-transition machinery when needed",
                "migration_cost": "SELECTIVE: only items that justify first-class identity need new carriers",
            },
            "B": {
                "implementation_blast_radius": "HIGH: parser cardinality, discovery, carrier/source revision and downstream path-key assumptions must change",
                "reference_integrity": "POSSIBLE but requires section-level declaration/source semantics absent from V1",
                "move_rename_behavior": "MORE COMPLEX: one carrier can move multiple independently identified units",
                "migration_cost": "LOWER file-count churn but HIGHER substrate/schema/runtime change",
            },
            "C": {
                "implementation_blast_radius": "NONE",
                "reference_integrity": "LOW for first-class items: typed relation targets cannot resolve anchor-only identity",
                "move_rename_behavior": "PATH/ANCHOR COUPLED unless another identity layer is invented",
                "migration_cost": "LOW initially but leaves the motivating first-class-identity problem unsolved",
            },
        },
        "mechanical_verdict": {
            "A_native_semantics_pass": (
                a["all_scoped_successors_resolve"]
                and a["residual_base_resolves"]
                and a["ab032_first_class_required_identity_resolves"]
            ),
            "B_requires_substrate_change": not b["accepted_by_current_parser"],
            "C_fails_typed_relation_target": not c["typed_relation_target_resolves"],
            "C_fails_required_item_identity": (
                not c["ab032_anchor_only_satisfies_required_identity"]
            ),
        },
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["mechanical_verdict"], indent=2))

if __name__ == "__main__":
    main()
