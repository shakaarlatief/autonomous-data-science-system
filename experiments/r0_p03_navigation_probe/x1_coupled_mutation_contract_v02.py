"""Unscored X1 coupled-mutation experiment with a real D2 semantic evaluator.

F09/F10 are alternative states of the same D2 REPLACE source scenario, not
sequential owner-accepted J1 events. All carrier/metadata records here are
explicitly authored experimental analogues. This program probes the boundary
between common semantic currentness and optional navigation declarations.

It is NOT the future GOVERNED_LEDGER_KERNEL_V02 implementation, a production
J1/J2 authority mechanism, or a formal Research 513 B0-B4 comparison.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from experiments.ao10_hybrid_d2_lineage_v01.evaluator_chatgpt_a import evaluate_fixture
from experiments.r0_p03_navigation_probe.x1_navigation_extension_boundary_v01 import (
    rank_experiment,
)

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "experiments/ao10_hybrid_d2_lineage_v01/reviewer_fixtures.json"
RESULT = Path(__file__).with_name("x1_coupled_mutation_contract_result_v02.json")
EXPERIMENT_OWNER = "EXPERIMENT_AUTHOR_NOT_AUTHENTICATED_OWNER"
MODEL = "synthetic-vector-interface-v1"

# Each declaration is colocated with the simulated source-owner carrier and
# explicitly bound to its exact content revision. Physical paths are locator
# hints only; stable carrier IDs and revision digests own all references.
CARRIERS = {
    "carrier:decision": {
        "owner": "simulated:project-governance",
        "path": "synthetic/decision.md",
        "body": "The experimental predecessor effect P1 is governed here.",
    },
    "carrier:code": {
        "owner": "simulated:implementation",
        "path": "synthetic/authority.py",
        "body": "The experimental source component c1 realizes predecessor P1.",
    },
    "carrier:tests": {
        "owner": "simulated:verification",
        "path": "synthetic/test_authority.py",
        "body": "The predecessor P1 has tested component c2.",
    },
    "carrier:continuity": {
        "owner": "simulated:project-knowledge",
        "path": "synthetic/continuity.md",
        "body": "Effect P1 is superseded by S1 through a REPLACE event.",
    },
}
SUBJECTS = {
    "subject:governance": "governing effect and predecessor decision",
    "subject:implementation": "realizer code implementation",
}
CONCERNS = {
    "concern:recovery": "crosscutting recovery and evidence freshness",
}
VECTORS = {
    "carrier:decision": [1.0, 0.0, 0.0],
    "carrier:code": [0.7, 0.3, 0.0],
    "carrier:tests": [0.0, 1.0, 0.0],
    "carrier:continuity": [0.5, 0.0, 0.5],
}
# The role/status here is from a synthetic authoring contract, not proof of
# current ADS owner acceptance or qualified natural-owner J2 declarations.
DECLARED_NAVIGATION = {
    "carrier:decision": {
        "subjects": ["subject:governance"], "concerns": ["concern:recovery"],
        "about_effects": ["P1"],
    },
    "carrier:code": {
        "subjects": ["subject:implementation"], "concerns": ["concern:recovery"],
        "about_effects": ["P1"],
    },
    "carrier:tests": {
        "subjects": ["subject:implementation"], "concerns": [],
        "about_effects": ["P1"],
    },
    "carrier:continuity": {
        "subjects": ["subject:governance"], "concerns": ["concern:recovery"],
        "about_effects": ["P1"],
    },
}


def digest(value: Any) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf8")
    ).hexdigest()


def source_digest(record: dict[str, str]) -> str:
    """Digest authored content, not a carrier's mutable path."""
    return sha256(record["body"].encode("utf8")).hexdigest()


def scenario_pair() -> tuple[dict, dict]:
    """Use existing adjudicated development-replay inputs, without rewriting them."""
    all_cases = json.loads(SOURCE.read_text("utf8"))["fixtures"]
    by_id = {case["fixture_id"]: case for case in all_cases}
    fresh, stale = (
        by_id["F09_REPLACE_VALID_REALIZATION_CARRY"],
        by_id["F10_REPLACE_STALE_CARRY_FACTS"],
    )
    if fresh["relation_type"] != "REPLACE" or stale["relation_type"] != "REPLACE":
        raise ValueError("Real D2 source no longer has the expected REPLACE cases")
    a, b = deepcopy(fresh), deepcopy(stale)
    # These cases are the same source scenario with only the evaluator-relevant
    # freshness fact changed; no generated fixture is substituted for an original.
    a.pop("fixture_id")
    b.pop("fixture_id")
    if sorted(k for k in a if a[k] != b[k]) != ["source_realization_facts_fresh"]:
        raise ValueError("F09/F10 are no longer an exact freshness counterfactual pair")
    return fresh, stale


def semantic_projection(fixture: dict) -> dict:
    """Projection of an actually executed D2 evaluator result, not a new J3."""
    result = evaluate_fixture(fixture)
    if not result["relation_valid"]:
        raise ValueError("D2 relation invalid: " + repr(result["reason_codes"]))
    return {
        "source_case": fixture["fixture_id"],
        "fixture_digest": digest(fixture),
        "relation_type": fixture["relation_type"],
        "current_effect_ids": list(result["current_effect_ids"]),
        "successor_initialization": deepcopy(result["successor_initialization"]),
        "review_required": result["review_required"],
        "reason_codes": list(result["reason_codes"]),
        "source_facts_current": fixture["source_realization_facts_current"],
        "source_facts_fresh": fixture["source_realization_facts_fresh"],
    }


def predecessor_projection(fixture: dict) -> dict:
    """Pre-REPLACE effect status declared by the same D2 scenario's predecessor."""
    return {
        "source_case": fixture["fixture_id"] + ":PREDECESSOR",
        "fixture_digest": digest(fixture),
        "relation_type": "PREDECESSOR_SOURCE_FACT_NOT_EXECUTED_LINEAGE",
        "current_effect_ids": sorted(
            row["effect_id"] for row in fixture["predecessors"] if row["status"] == "ACTIVE"
        ),
        "successor_initialization": [],
        "review_required": False,
        "reason_codes": [],
        "source_facts_current": fixture["source_realization_facts_current"],
        "source_facts_fresh": fixture["source_realization_facts_fresh"],
    }


def author_declarations(carriers: dict = CARRIERS) -> dict:
    """Construct four deliberately simulated, source-revision-bound declarations."""
    return {
        cid: {
            "carrier_id": cid,
            "declared_owner": carrier["owner"],
            "source_digest": source_digest(carrier),
            "authorship_class": EXPERIMENT_OWNER,
            **deepcopy(DECLARED_NAVIGATION[cid]),
        }
        for cid, carrier in carriers.items() if cid in DECLARED_NAVIGATION
    }


def check_declarations(carriers: dict, declarations: dict) -> None:
    """Fail closed on stale or foreign-owner data before optional indexing."""
    if set(declarations) != set(carriers):
        raise ValueError("All experimental source declarations must be explicit")
    for cid, carrier in carriers.items():
        row = declarations[cid]
        if set(row) != {
            "carrier_id", "declared_owner", "source_digest", "authorship_class",
            "subjects", "concerns", "about_effects",
        }:
            raise ValueError("Unknown or governing field in navigation metadata")
        if row["carrier_id"] != cid or row["declared_owner"] != carrier["owner"]:
            raise ValueError("Carrier identity or simulated source owner mismatch")
        if row["source_digest"] != source_digest(carrier):
            raise ValueError("STALE_SOURCE_DECLARATION")
        if row["authorship_class"] != EXPERIMENT_OWNER:
            raise ValueError("Attempt to promote experimental declaration to J1/J2")
        if not set(row["subjects"]) <= set(SUBJECTS):
            raise ValueError("Ungoverned new subject: governance hook required")
        if not set(row["concerns"]) <= set(CONCERNS):
            raise ValueError("Ungoverned new concern: governance hook required")
        if not all(isinstance(e, str) for e in row["about_effects"]):
            raise ValueError("Malformed source-owned editorial effect link")


def navigation_statuses(
    semantic: dict, declarations: dict,
) -> dict:
    """A real semantic currentness transition controls editorial link status."""
    current = set(semantic["current_effect_ids"])
    return {
        cid: {
            "effect_links": {
                effect: ("CURRENT_EXPERIMENT_EFFECT" if effect in current else "REVIEW_REQUIRED")
                for effect in row["about_effects"]
            },
            "source_fact_status": (
                "SOURCE_FACT_STALE" if not semantic["source_facts_fresh"]
                else "SOURCE_FACT_CURRENT"
            ),
        }
        for cid, row in declarations.items()
    }


def provider_manifest(carriers: dict, model: str = MODEL) -> dict:
    """Represent a disposable dense-index build bound to model and source bytes."""
    return {
        "model": model,
        "carrier_digests": {cid: source_digest(c) for cid, c in sorted(carriers.items())},
    }


def build_projection(
    arm: str, semantic: dict, carriers: dict, declarations: dict,
    *, model_manifest: dict | None = None,
) -> dict:
    """Produce derived navigation surface bound to D2 truth and exact inputs.

    Unlike the prior passive adapter pilot, the indexed status is computed by
    inspecting effect IDs and J2 freshness obtained from D2 evaluation.
    """
    if arm not in {"B0", "B1", "B2", "B3", "B4"}:
        raise ValueError("Unknown comparator")
    check_declarations(carriers, declarations)
    if model_manifest is None:
        model_manifest = provider_manifest(carriers)
    if arm == "B4" and model_manifest != provider_manifest(carriers):
        raise ValueError("STALE_VECTOR_MODEL_OR_SOURCE_INDEX")
    by_carrier = navigation_statuses(semantic, declarations)
    if not semantic["source_facts_fresh"] and any(
        init["mode"] == "CARRY_FACTS_FOR_REVALIDATION"
        for init in semantic["successor_initialization"]
    ):
        raise ValueError("STALE_J2_WAS_INCORRECTLY_CARRIED")
    body = {
        "classification": "DERIVED_EXPERIMENT_ONLY_NOT_AUTHORITY",
        "arm": arm,
        "semantic_digest": digest(semantic),
        "source_manifest_digest": digest({
            cid: source_digest(record) for cid, record in sorted(carriers.items())
        }),
        "authority_current_effects_read_only": semantic["current_effect_ids"],
        "review_required_from_d2": semantic["review_required"],
        "j2_successor_initialization_from_d2": semantic["successor_initialization"],
        "source_links": by_carrier if arm == "B2" else {},
    }
    if arm in {"B1", "B3"}:
        body["metadata_memberships"] = {
            cid: declarations[cid]["subjects" if arm == "B1" else "concerns"]
            for cid in sorted(declarations)
        }
    if arm == "B4":
        body["model_manifest_digest"] = digest(model_manifest)
    # Use previous executed prototype rankers, but rankings are never governing.
    corpus = {cid: {"text": carrier["body"], "path": carrier["path"]}
              for cid, carrier in carriers.items()}
    if arm == "B0":
        ranked = rank_experiment("B0", {}, corpus)
    elif arm in {"B1", "B3"}:
        vocab = SUBJECTS if arm == "B1" else CONCERNS
        field = "subjects" if arm == "B1" else "concerns"
        metadata = {
            "definitions": vocab,
            "assignments": {
                cid: row[field] for cid, row in declarations.items() if row[field]
            },
        }
        # Directly reused ranking implementation with different input contract.
        from experiments.r0_p03_navigation_probe.route_b_distinct_b1_b2_b3_navigation_comparison_v01 import (
            ranked_annotation_channel, two_channel_rrf,
        )
        base = rank_experiment("B0", {}, corpus)
        rank = ranked_annotation_channel(
            "authority evidence",
            {cid: {"tags": tags} for cid, tags in metadata["assignments"].items()},
            vocab, "tags",
        )
        ranked = two_channel_rrf(base, rank)
    elif arm == "B2":
        from experiments.r0_p03_navigation_probe.route_b_distinct_b1_b2_b3_navigation_comparison_v01 import (
            editorial_link_rank,
        )
        base = rank_experiment("B0", {}, corpus)
        edges = [
            {"source_path": cid, "target_path": "carrier:decision", "source_line": 1}
            for cid, row in declarations.items()
            if cid != "carrier:decision" and "P1" in row["about_effects"]
        ]
        ranked, _ = editorial_link_rank(base, edges, set(corpus))
    else:
        from experiments.r0_p03_navigation_probe.route_b_b4_local_lsa_embedding_comparison_v01 import (
            dense_rank,
        )
        ordered = sorted(VECTORS)
        ranked, _ = dense_rank(
            ordered, [VECTORS[cid] for cid in ordered], [1.0, 0.0, 0.0]
        )
    body["diagnostic_ranked_carrier_ids"] = ranked
    body["derived_digest"] = digest(body)
    return body


def verify_publication(projection: dict, semantic: dict, carriers: dict) -> bool:
    """A cached orientation must expose staleness after semantic/source updates."""
    if projection["semantic_digest"] != digest(semantic):
        raise ValueError("STALE_SEMANTIC_PUBLICATION")
    expected = digest({cid: source_digest(c) for cid, c in sorted(carriers.items())})
    if projection["source_manifest_digest"] != expected:
        raise ValueError("STALE_SOURCE_PUBLICATION")
    if projection["derived_digest"] != digest({
        k: v for k, v in projection.items() if k != "derived_digest"
    }):
        raise ValueError("TAMPERED_DERIVED_PUBLICATION")
    return True


def try_bad(operation) -> bool:
    try:
        operation()
    except ValueError:
        return True
    raise AssertionError("Invalid source/semantic operation was not rejected")


def run() -> dict:
    fresh_case, stale_case = scenario_pair()
    before = predecessor_projection(fresh_case)
    after_fresh = semantic_projection(fresh_case)
    after_stale = semantic_projection(stale_case)
    if after_fresh["current_effect_ids"] != ["S1"] or after_stale["current_effect_ids"] != ["S1"]:
        raise AssertionError("Expected exact D2 current effect IDs changed")
    if after_fresh["successor_initialization"][0]["mode"] != "CARRY_FACTS_FOR_REVALIDATION":
        raise AssertionError("Expected D2 valid-carry result changed")
    if after_stale["successor_initialization"][0]["mode"] != "OPEN_RESET":
        raise AssertionError("Expected D2 stale-carry result changed")
    if not after_stale["review_required"]:
        raise AssertionError("A stale D2 carry did not require review")
    authored = author_declarations()
    observations = {}
    for arm in ("B0", "B1", "B2", "B3", "B4"):
        pre = build_projection(arm, before, CARRIERS, authored)
        good = build_projection(arm, after_fresh, CARRIERS, authored)
        stale = build_projection(arm, after_stale, CARRIERS, authored)
        assert verify_publication(pre, before, CARRIERS)
        assert verify_publication(good, after_fresh, CARRIERS)
        assert verify_publication(stale, after_stale, CARRIERS)
        if good["semantic_digest"] == stale["semantic_digest"]:
            raise AssertionError("Navigation failed to recognize actual J2 semantic mutation")
        if good["j2_successor_initialization_from_d2"] == stale["j2_successor_initialization_from_d2"]:
            raise AssertionError("Navigator masked a change to actual D2 realization status")
        if arm == "B2":
            assert pre["source_links"]["carrier:code"]["effect_links"]["P1"] == "CURRENT_EXPERIMENT_EFFECT"
            assert good["source_links"]["carrier:code"]["effect_links"]["P1"] == "REVIEW_REQUIRED"
        observations[arm] = {
            "replay_semantic_changes_visible": True,
            "pre_and_post_currentness_distinguished": pre["authority_current_effects_read_only"] != good["authority_current_effects_read_only"],
            "fresh_vs_stale_j2_distinguished": good["j2_successor_initialization_from_d2"] != stale["j2_successor_initialization_from_d2"],
            "stale_publication_rejected": try_bad(
                lambda: verify_publication(good, after_stale, CARRIERS)
            ),
            "disposable_rebuild_stable": good == build_projection(arm, after_fresh, CARRIERS, authored),
            "diagnostic_carrier_ids": good["diagnostic_ranked_carrier_ids"],
        }
    relocated = deepcopy(CARRIERS)
    relocated["carrier:code"]["path"] = "synthetic/moved/authority.py"
    relocation = build_projection("B1", after_fresh, relocated, authored)
    old = build_projection("B1", after_fresh, CARRIERS, authored)
    if old["source_manifest_digest"] != relocation["source_manifest_digest"]:
        raise AssertionError("Path relocation changed semantic source identity")
    modified = deepcopy(CARRIERS)
    modified["carrier:code"]["body"] += "\nAdditional implementation evidence."
    revised = author_declarations(modified)
    # Accepted experimental source revisions must be re-authored; no automatic
    # source-ownership migration is inferred from the physical location.
    negative = {
        "stale_source_owner_declaration": try_bad(
            lambda: build_projection("B1", after_fresh, modified, authored)),
        "foreign_claimed_source_owner": try_bad(
            lambda: build_projection("B2", after_fresh, CARRIERS, {
                **authored,
                "carrier:code": {
                    **authored["carrier:code"], "declared_owner": "simulated:unrelated-owner"
                },
            })),
        "invented_navigation_authority": try_bad(
            lambda: build_projection("B2", after_fresh, CARRIERS, {
                **authored,
                "carrier:code": {**authored["carrier:code"], "accepted_j1": "FORGED"},
            })),
        "ungoverned_new_subject": try_bad(
            lambda: build_projection("B1", after_fresh, CARRIERS, {
                **authored,
                "carrier:code": {**authored["carrier:code"],
                                 "subjects": ["subject:unapproved-new"]},
            })),
        "ungoverned_new_concern": try_bad(
            lambda: build_projection("B3", after_fresh, CARRIERS, {
                **authored,
                "carrier:code": {**authored["carrier:code"],
                                 "concerns": ["concern:unapproved-new"]},
            })),
        "obsolete_model_revision": try_bad(
            lambda: build_projection("B4", after_fresh, CARRIERS, authored,
                                     model_manifest=provider_manifest(CARRIERS, "old-model"))),
        "stale_model_source_revision": try_bad(
            lambda: build_projection("B4", after_fresh, modified, revised,
                                     model_manifest=provider_manifest(CARRIERS))),
        "tampered_published_orientation": try_bad(
            lambda: verify_publication(
                {**old, "authority_current_effects_read_only": ["P1"]},
                after_fresh, CARRIERS)),
        "old_cache_after_source_rewrite": try_bad(
            lambda: verify_publication(old, after_fresh, modified)),
    }
    # When the simulated source owner produces an exact new declaration and the
    # derived dense index is rebuilt, the new source revision is usable again.
    rebuilt_model = build_projection(
        "B4", after_fresh, modified, revised,
        model_manifest=provider_manifest(modified),
    )
    if not verify_publication(rebuilt_model, after_fresh, modified):
        raise AssertionError("Rebuilt revised B4 projection is unavailable")
    # No possible kernel/J1 alteration is inferred from this experiment-only
    # source-authoring or cache-publication contract.
    classifications = {
        "B0": {
            "classification": "INCONCLUSIVE",
            "evidence": "Common D2 projection and publication stale check exercised; no actual V02 orientation publication or lexical service",
            "candidate_r1_hook": "versioned connector-readable orientation freshness and source-head bound publication",
        },
        "B1": {
            "classification": "REQUIRES_R1_HOOK_CANDIDATE",
            "evidence": "Simulated source owner and declared subject validation; unknown subject blocked",
            "candidate_r1_hook": "source-owned facet declaration schema and governed vocabulary admission/evolution",
        },
        "B2": {
            "classification": "REQUIRES_R1_HOOK_CANDIDATE",
            "evidence": "Actual D2 effect successor makes old P1 editorial links REVIEW_REQUIRED, without auto-rebind",
            "candidate_r1_hook": "typed editorial relation provenance and lineage-triggered review/rebinding",
        },
        "B3": {
            "classification": "REQUIRES_R1_HOOK_CANDIDATE",
            "evidence": "Concern declarations are source revision bound and unknown concern blocked",
            "candidate_r1_hook": "distinct crosscutting concern vocabulary ownership and evolution",
        },
        "B4": {
            "classification": "REQUIRES_R1_HOOK_CANDIDATE",
            "evidence": "Model/source index provenance invalidates stale publication, and explicit rebuild restores it",
            "candidate_r1_hook": "pluggable model/version/source-index provenance, safety and update/rebuild contract",
        },
    }
    return {
        "status": "COUPLED_D2_MUTATION_EVIDENCE_X1_FULL_INCONCLUSIVE",
        "source": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
        "d2_case_ids": [fresh_case["fixture_id"], stale_case["fixture_id"]],
        "d2_fresh_mode": after_fresh["successor_initialization"][0]["mode"],
        "d2_stale_mode": after_stale["successor_initialization"][0]["mode"],
        "d2_stale_review_required": after_stale["review_required"],
        "scenario_kind": "ALTERNATIVE_FRESH_VS_STALE_D2_REPLAY_NOT_REAL_HISTORY",
        "common_projection_hashes": {
            "predecessor": digest(before), "valid_carry": digest(after_fresh),
            "stale_carry": digest(after_stale),
        },
        "per_arm": observations,
        "negative_controls_rejected": negative,
        "source_revision_rebuilt_usable": True,
        "arm_interface_classifications": classifications,
        "verified_production_j1_or_j2": False,
        "v02_kernel_implemented": False,
        "research_513_formal_score": None,
        "physical_target_selected": False,
        "missing_contracts": [
            "Actual V02 governing admission and versioned effect/evidence projection",
            "Natural-owner J2 RELATIONAL declaration and revocation/coverage ownership",
            "Actual source-owned navigation governance and owner authorization",
            "Shared V03 identity and fragment/reference contract across real carriers",
            "Connector-readable derived orientation publication and freshness SLA",
            "Real B4 model feasibility and embeddings; Research 217 navigational sufficiency",
        ],
    }


def main() -> None:
    result = run()
    raw = json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if RESULT.exists():
        if RESULT.read_text("utf8") != raw:
            raise RuntimeError("Existing receipt differs, refusing rewrite")
    else:
        with RESULT.open("x", encoding="utf8", newline="\n") as output:
            output.write(raw)
    print(json.dumps({
        "status": result["status"],
        "negative_controls_rejected": len(result["negative_controls_rejected"]),
        "arms": list(result["per_arm"]),
        "d2_fresh_mode": result["d2_fresh_mode"],
        "d2_stale_mode": result["d2_stale_mode"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
