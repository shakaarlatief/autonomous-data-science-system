"""Unscored X1 navigation-extension boundary pilot.

Use D1 and D2 development replay evaluators and the actual Route-B ranking
primitives. The synthetic carriers and metadata in this file are NOT accepted
J1, qualified J2, future V02 kernel code, or formal R0-P03 comparator arms.
A local interface pass cannot establish target-architecture lock-in freedom.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path

from experiments.ao10_hybrid_d1_replay_v01.evaluator_chatgpt_a import evaluate as d1_evaluate
from experiments.ao10_hybrid_d2_lineage_v01.evaluator_chatgpt_a import evaluate_fixture as d2_evaluate
from experiments.r0_p03_navigation_probe.route_b_distinct_b1_b2_b3_navigation_comparison_v01 import (
    editorial_link_rank, ranked_annotation_channel, two_channel_rrf,
)
from experiments.r0_p03_navigation_probe.route_b_b4_local_lsa_embedding_comparison_v01 import dense_rank

ROOT = Path(__file__).resolve().parents[2]
RESULT = Path(__file__).with_name("x1_navigation_extension_boundary_result_v01.json")
CARRIERS = {
    "carrier:decision": {"path": "synthetic/docs/decision.md", "text": "governing authority and accepted effects"},
    "carrier:code": {"path": "synthetic/code/authority.py", "text": "implementation of authority effect"},
    "carrier:test": {"path": "synthetic/tests/test_authority.py", "text": "verification evidence for authority"},
    "carrier:continuity": {"path": "synthetic/docs/continuity.md", "text": "lineage and continuity of governing effects"},
}
EFFECT_ID = "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT"
ARMS = {
    "B0": {},
    "B1": {
        "definitions": {"subject:authority": "authority governing accepted effects", "subject:evidence": "verification and tests"},
        "assignments": {"carrier:decision": ["subject:authority"], "carrier:code": ["subject:authority"], "carrier:test": ["subject:evidence"]},
    },
    "B2": {"links": [{"source_id": "carrier:code", "target_id": "carrier:decision",
                      "effect_id": EFFECT_ID, "source_line": 1, "evidence": "EXPERIMENTAL_EDITORIAL_ONLY"}]},
    "B3": {
        "definitions": {"concern:assurance": "crosscutting assurance, tests and evidence"},
        "assignments": {"carrier:decision": ["concern:assurance"], "carrier:test": ["concern:assurance"]},
    },
    "B4": {"vectors": {"carrier:decision": [1.0, 0.0, 0.0], "carrier:code": [0.6, 0.4, 0.0],
                       "carrier:test": [0.0, 1.0, 0.0], "carrier:continuity": [0.5, 0.0, 0.5]}},
}
SCHEMAS = {
    "B0": set(), "B1": {"definitions", "assignments"}, "B2": {"links"},
    "B3": {"definitions", "assignments"}, "B4": {"vectors"},
}
LINK_FIELDS = {"source_id", "target_id", "effect_id", "source_line", "evidence"}


def digest(value):
    return sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf8")).hexdigest()


def load_development_replays():
    """Development fixtures, never production current-authority declarations."""
    d1 = ROOT / "experiments/ao10_hybrid_d1_replay_v01"
    d2 = ROOT / "experiments/ao10_hybrid_d2_lineage_v01"
    j1 = json.loads((d1 / "accepted_j1.json").read_text("utf8"))
    facts = json.loads((d1 / "source_facts.json").read_text("utf8"))
    cases = json.loads((d2 / "reviewer_fixtures.json").read_text("utf8"))["fixtures"]
    if len(j1["effects"]) != 4 or len(cases) != 14:
        raise ValueError("D1/D2 historical fixture count unexpectedly changed")
    return j1, facts, cases


def validate(arm, metadata, carriers, effects):
    """Reject undeclared metadata and any proposed acceptance/authority injection."""
    if arm not in SCHEMAS or not isinstance(metadata, dict) or set(metadata) != SCHEMAS[arm]:
        raise ValueError("Navigation extension schema mismatch")
    ids = set(carriers)
    if any(not key.startswith("carrier:") for key in ids):
        raise ValueError("Carrier identity cannot be a physical path")
    if arm in {"B1", "B3"}:
        if set(metadata["assignments"]) - ids:
            raise ValueError("Assigned carrier does not have stable identity")
        for tags in metadata["assignments"].values():
            if not isinstance(tags, list) or not set(tags) <= set(metadata["definitions"]):
                raise ValueError("Unrecognized metadata vocabulary")
    if arm == "B2":
        for link in metadata["links"]:
            if set(link) != LINK_FIELDS:
                raise ValueError("Link would change the allowed metadata schema")
            if link["source_id"] not in ids or link["target_id"] not in ids:
                raise ValueError("Link must use carrier identity")
            if link["effect_id"] not in effects:
                raise ValueError("Link would refer to an unrecognized effect")
            if link["evidence"] != "EXPERIMENTAL_EDITORIAL_ONLY":
                raise ValueError("Editorial link cannot become governing authority")
    if arm == "B4":
        if set(metadata["vectors"]) - ids:
            raise ValueError("Vectors cannot use physical path identity")
        if any(not isinstance(v, list) or len(v) != 3 or not all(
            isinstance(x, (int, float)) and -1e6 < x < 1e6 for x in v
        ) for v in metadata["vectors"].values()):
            raise ValueError("Incorrect experimental vector shape")


def derived_index(arm, metadata, carriers, effects):
    validate(arm, metadata, carriers, effects)
    return {
        "authority": "DERIVED_NON_GOVERNING_EXPERIMENT",
        "arm": arm,
        "ids": sorted(carriers),
        "data": deepcopy(metadata),
    }

def rank_experiment(arm, metadata, carriers, question="authority evidence"):
    """Exercise real Route-B ranking primitives over *synthetic stable IDs*.

    This exercises code reuse, not response quality; query and inputs are
    coordinator-authored, not independently selected reference questions.
    """
    ids = sorted(carriers)
    words = question.lower().split()
    lexical = sorted(ids, key=lambda c: (
        -sum(w in carriers[c]["text"].lower() for w in words), c,
    ))
    if arm == "B0":
        return lexical
    if arm in {"B1", "B3"}:
        annotated = {c: {"tags": tags} for c, tags in metadata["assignments"].items()}
        ranked = ranked_annotation_channel(
            question, annotated, metadata["definitions"], "tags",
        )
        return two_channel_rrf(lexical, ranked)
    if arm == "B2":
        # Original Route-B function calls the ID fields source_path/target_path;
        # supplying actual paths here would violate the stable identity design.
        edges = [
            {"source_path": e["source_id"], "target_path": e["target_id"],
             "source_line": e["source_line"]}
            for e in metadata["links"]
        ]
        ranked, _ = editorial_link_rank(lexical, edges, set(ids))
        return ranked
    vectors = metadata["vectors"]
    ordered = [c for c in ids if c in vectors]
    ranked, _ = dense_rank(
        ordered, [vectors[c] for c in ordered], [1.0, 0.0, 0.0],
    )
    return two_channel_rrf(lexical, ranked)


def evidence_status_after_lineage(links, current_effect_ids):
    """Lineage never silently rebinds an editorial reference to a new J1 ID."""
    return "REVIEW_REQUIRED" if any(
        edge["effect_id"] not in current_effect_ids for edge in links
    ) else "CURRENT_TARGET"


def negative_controls(effects):
    """Ensure the pilot guard actually rejects adversarial invalid input."""
    bad = {
        "authority_field_injection": ("B1", {
            **ARMS["B1"], "accepted_j1": {"forged": True},
        }),
        "path_as_identity": ("B1", {
            **ARMS["B1"], "assignments": {
                **ARMS["B1"]["assignments"],
                "synthetic/docs/decision.md": ["subject:authority"],
            },
        }),
        "invented_effect": ("B2", {"links": [{
            **ARMS["B2"]["links"][0], "effect_id": "FAKE-EFFECT",
        }]}),
        "authority_class_promotion": ("B2", {"links": [{
            **ARMS["B2"]["links"][0], "evidence": "ACCEPTED_GOVERNING",
        }]}),
        "vector_path_as_identity": ("B4", {"vectors": {
            **ARMS["B4"]["vectors"],
            "synthetic/docs/decision.md": [1.0, 0.0, 0.0],
        }}),
    }
    rejected = []
    for label, (arm, metadata) in bad.items():
        try:
            derived_index(arm, metadata, CARRIERS, effects)
        except ValueError:
            rejected.append(label)
        else:
            raise AssertionError("Invalid plugin accepted: " + label)
    return rejected


def run():
    """Run one finite interface experiment; never emit a formal P03 score."""
    j1, facts, cases = load_development_replays()
    j1_copy, facts_copy = deepcopy(j1), deepcopy(facts)
    j3 = d1_evaluate(j1, facts)
    d2_out = [d2_evaluate(c) for c in cases]
    effects = {e["accepted_effect_id"] for e in j1["effects"]}
    observations = {}
    for arm, data in ARMS.items():
        index = derived_index(arm, data, CARRIERS, effects)
        before = digest(index)
        del index
        after = digest(derived_index(arm, data, CARRIERS, effects))
        moved = deepcopy(CARRIERS)
        moved["carrier:decision"]["path"] = "synthetic/moved/decision.md"
        moved_view = derived_index(arm, data, moved, effects)
        assert moved_view["data"] == data
        ranked = rank_experiment(arm, data, CARRIERS)
        assert set(ranked) <= set(CARRIERS)
        observations[arm] = {
            "rebuild_digest_preserved": before == after,
            "metadata_survives_path_rename": moved_view["data"] == data,
            "ranking_ids": ranked,
            "metadata_digest": digest(data),
        }
    # The D2 fixture gives an actual development-replay successor boundary.
    replace = next(c for c in cases if c["fixture_id"] == "F08_REPLACE_DEFAULT_OPEN_RESET")
    replace_out = d2_evaluate(replace)
    old = replace["predecessors"][0]["effect_id"]
    status = evidence_status_after_lineage(
        [{"effect_id": old}], set(replace_out["current_effect_ids"]),
    )
    if not replace_out["relation_valid"] or status != "REVIEW_REQUIRED":
        raise AssertionError("Obsolete effect reference was silently accepted")
    added = deepcopy(CARRIERS)
    for i in range(10):
        added[f"carrier:growth:{i:02d}"] = {
            "path": f"synthetic/growth/{i:02d}.md",
            "text": "synthetic growth and no new governing authority",
        }
    churn = sum(
        derived_index(arm, data, added, effects)["data"] != data
        for arm, data in ARMS.items()
    )
    if churn:
        raise AssertionError("Synthetic growth changed existing authored metadata")
    if j1 != j1_copy or facts != facts_copy:
        raise AssertionError("Original accepted/replay facts mutated")
    if d1_evaluate(j1, facts) != j3:
        raise AssertionError("D1 J3 semantic output changed")
    if [d2_evaluate(c) for c in cases] != d2_out:
        raise AssertionError("D2 lineage semantic output changed")
    return {
        "status": "LIMITED_UNSCORED_INTERFACE_PILOT_NOT_X1_PASS",
        "d1_effect_count": len(j1["effects"]),
        "d1_j3_digest": digest(j3),
        "d2_case_count": len(cases),
        "d2_digest": digest(d2_out),
        "mechanical_negative_controls_rejected": negative_controls(effects),
        "d2_replace_obsolete_link": status,
        "synthetic_growth_carriers_added": 10,
        "authored_metadata_rewritten_count": churn,
        "d1_d2_results_unchanged": True,
        "arms": observations,
        "limitations": [
            "No implemented GOVERNED_LEDGER_KERNEL_V02 kernel or R1 extension contract",
            "D1 accepted effects are development replay, not current production authority",
            "D1 and D2 are distinct replay scenarios, not one integrated lineage world",
            "Four synthetic carriers are not source-owned production relationships",
            "B4 synthetic vectors are not neural embedding quality or model feasibility",
            "B1/B3 governed vocabulary admission and owner burden are not tested",
            "Index rebuild and growth are synthetic, not production maintenance F1",
            "Rank outputs are diagnostics, not original Research 513 answer scores",
        ],
        "research_513_formal_outcome": None,
        "physical_target_selected": False,
    }


def main():
    result = run()
    body = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if RESULT.exists():
        if RESULT.read_text("utf8") != body:
            raise RuntimeError("Frozen first-run receipt mismatch; refusing overwrite")
    else:
        with RESULT.open("x", encoding="utf8", newline="\n") as f:
            f.write(body)
    print(body)


if __name__ == "__main__":
    main()
