"""Read-only executed C_arm diagnostic AFTER fixed primary arm/version freeze.

This script creates and rechecks one immutable non-scored evidence receipt.
It reads NO hidden reference or scored task, and will not repair or retune
post-freeze subject memberships, editorial links, concern vocabulary,
BM25 coefficients, context-pack budgets, or prospective neural B4 omission.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess

from experiments.r0_p03_navigation_probe import (
    w1_primary_c_arm_v01 as arms,
    w1_freeze_v01 as w1,
)

HERE = Path(__file__).resolve().parent
FREEZE_FILE = HERE / "w1_c_arm_primary_freeze_contract_v01.json"
FREEZE_COMMIT = "f43390ab267810502d7538e212cd30f4fee18aaf"
FREEZE_SHA256 = "31e77378218e60780cdbad2dfec98293ac71f3fbeb58206066dff268ea5d845a"
OUTPUT = HERE / "w1_c_arm_exposed_mechanism_execution_receipt_v01.json"
ARMS = ("B0","B1","B2","B3")

# Deliberately exposed engineering signal probes. These are NOT prospective
# primary needs or legacy scenarios, MUST NOT be given to independent primary
# originators, and have no label/quality truth. No result from them may tune
# frozen arm construction or future Research 513 hard thresholds.
EXPOSED_MECHANISM_PROBES = (
    "project knowledge reconstruction",
    "decision authority currentness",
    "runtime persistence evidence",
    "cockpit visual language",
    "source evidence integrity",
    "developer tooling migration",
    "model collaboration review",
    "knowledge preservation continuity",
)


def _git(*args: str) -> bytes:
    return subprocess.check_output(
        ["git",*args],cwd=w1.ROOT
    )


def verify_freeze() -> dict:
    original=_git("show",f"{FREEZE_COMMIT}:{FREEZE_FILE.relative_to(w1.ROOT).as_posix()}")
    if sha256(original).hexdigest()!=FREEZE_SHA256:
        raise ValueError("W1_C_ARM_FROZEN_CONTRACT_DIGEST_FAILURE")
    work=FREEZE_FILE.read_bytes()
    if work.replace(b"\r\n",b"\n")!=original:
        raise ValueError("W1_C_ARM_FROZEN_CONTRACT_WORKTREE_CHANGED")
    if subprocess.run(
        ["git","merge-base","--is-ancestor",FREEZE_COMMIT,"HEAD"],
        cwd=w1.ROOT,capture_output=True,
    ).returncode:
        raise ValueError("W1_C_ARM_FREEZE_NOT_ANCESTOR")
    frozen=json.loads(original.decode("utf8"))
    if (
        frozen["classification"]!=
            "C_ARM_W1_PRIMARY_B0_B3_SOURCE_AND_IMPL_FREEZE_BEFORE_INDEPENDENT_PRIMARY_TASKS"
        or frozen["freeze_source_implementation_commit"]!=
            "b987b1837f38479c3ccd34410de4ef52ab4c1edd"
        or frozen["b4_omitted_prospectively_at_fixture_freeze"] is not True
        or frozen["post_freeze_task_construction"]!=
            "NO_INDEPENDENT_TASKS_OR_GOLD_EXIST_AT_FREEZE"
        or frozen["excluded_formal_operations"]["heldout_draw"] is not False
    ):
        raise ValueError("W1_C_ARM_NOT_PROSPECTIVE_FROZEN_PRIMARY")
    for entry in frozen["w1_primary_arm_implementation_git_objects"].values():
        path=entry["path"]
        pre=_git("show",f'{entry["git_source_commit"]}:{path}')
        blob_id=_git("rev-parse",f'{entry["git_source_commit"]}:{path}').decode().strip()
        if sha256(pre).hexdigest()!=entry["sha256"] or blob_id!=entry["git_blob_oid"]:
            raise ValueError("W1_C_ARM_ORIGINAL_FROZEN_FILE_PROVENANCE_DRIFT")
        if Path(w1.ROOT/path).read_bytes().replace(b"\r\n",b"\n")!=pre:
            raise ValueError("W1_C_ARM_LIVE_IMPLEMENTATION_CHANGED_FROM_FREEZE")
    return frozen


def diagnostic() -> dict:
    frozen=verify_freeze()
    contract,metadata,catalog,implementations=arms.make_frozen()
    if arms.canonical(contract)!=arms.canonical(frozen["treatment_specification"]):
        raise ValueError("W1_C_ARM_RUNTIME_CONTRACT_DIFFERS_FROM_FREEZE")
    queries=[]
    for query in EXPOSED_MECHANISM_PROBES:
        out={name:implementation.context_pack(query,limit=6)
             for name,implementation in implementations.items()}
        if any(value["source_git_ref"]!=w1.PIN
               or value["evidence_not_independent_gold"] is not True
               or value["derived_index_or_ranking_confers_authority"] is not False
               or value["excerpts_total_characters"]>16800
               or len(value["source_candidates"])!=6
               for value in out.values()):
            raise ValueError("W1_C_ARM_CONTEXT_BUDGET_OR_PROVENANCE_VIOLATION")
        ranked={name:[x["source_path"] for x in value["source_candidates"]]
                for name,value in out.items()}
        queries.append({
            "query_exposed_non_scored":query,
            "candidate_order_by_arm":ranked,
            "same_candidate_order_as_b0":{
                name:paths==ranked["B0"] for name,paths in ranked.items()
            },
            "context_exact_line_evidence_sha256_by_arm":{
                name:sha256(arms.canonical(value)).hexdigest()
                for name,value in out.items()
            },
            "source_context_characters_by_arm":{
                name:value["excerpts_total_characters"]
                for name,value in out.items()
            },
            "not_relevance_or_quality_scored":True,
        })
    changed={
        name:sum(not q["same_candidate_order_as_b0"][name] for q in queries)
        for name in ARMS
    }
    b1=implementations["B1"]
    b2=implementations["B2"]
    b3=implementations["B3"]
    hierarchy={
        "subject_parent_browse_count":len(b1.browse_subject("project-development")["sources"]),
        "controlled_subject_count":len(catalog["subjects"]),
        "source_to_governing_editorial_links":len(metadata["b2_additional_editorial_links"]),
        "example_editorial_browse_count":len(b2.browse_links("tools/project_knowledge/identity.py")),
        "example_concern_browse_count":len(b3.browse_concern("source-evidence-integrity")),
    }
    return {
        "schema_version":1,
        "classification":"W1_FROZEN_PRIMARY_B0_B3_REAL_EXECUTION_EXPOSED_UNSCORED",
        "frozen_c_arm_commit":FREEZE_COMMIT,
        "frozen_contract_sha256":FREEZE_SHA256,
        "original_source_git_ref":w1.PIN,
        "source_count":60,
        "total_original_git_source_bytes":contract["common_original_source_bytes"],
        "bm25_passages":contract["common_bm25_passage_count"],
        "common_core_digest":contract["common_source_semantic_digest"],
        "context_cap":contract["equalized_context_budget"],
        "exposed_probe_count":len(EXPOSED_MECHANISM_PROBES),
        "exposed_diagnostic_order_by_arm":queries,
        "orders_different_from_b0_not_quality_score":changed,
        "mechanism_browse_smoke_counts":hierarchy,
        "per_arm_method_operation_counts":{
            name:dict(sorted(implementation.operation_counts.items()))
            for name,implementation in implementations.items()
        },
        "per_arm_curated_metadata_costs_not_performance_scores":
            contract["costs_not_quality_scores"],
        "neural_b4":"PROSPECTIVELY_OMITTED_AT_PRIMARY_C_ARM_FREEZE",
        "legacy_65_source_arm_work":"NOT_STARTED_BEFORE_INDEPENDENT_NEUTRAL_NINE",
        "independent_primary_task_authorship":"NOT_STARTED",
        "heldout_paths":"NOT_DRAWN",
        "protected_reference":"NONE",
        "research513_primary_or_legacy_pass_counts":"NONE",
        "research673_m6_formal_attempt_used":False,
        "physical_architecture_selection":False,
        "production_authority_changed":False,
        "fairness_limits":[
            "Eight exposed mechanism probes are not independent needs or correctness scores and must not enter fresh origination or reference packets.",
            "No post-freeze membership/link/concern/parameter tuning is permitted from this execution.",
            "B0-B3 share full original 60 source W1 contents and exact experimental S1 semantics but rank candidates through distinct metadata-only additions.",
            "Authored navigation metadata is a coordinator-curated source-adjacent overlay, not natural-owner J2, blind gold, or source-verified authority.",
            "B4 omission is scoped to present equalized environment feasibility, not embedding-performance evidence.",
            "Closed context packs are bounded and cannot guarantee all future independent needs are answerable.",
        ],
    }


def main() -> None:
    result=diagnostic()
    raw=arms.canonical(result)
    if OUTPUT.exists():
        if OUTPUT.read_bytes()!=raw:
            raise ValueError("W1_C_ARM_CREATE_ONLY_EXECUTION_RECEIPT_CHANGED")
    else:
        OUTPUT.write_bytes(raw)
    print(json.dumps({
        "classification":result["classification"],
        "frozen_c_arm_commit":result["frozen_c_arm_commit"],
        "source_count":result["source_count"],
        "probes":result["exposed_probe_count"],
        "changed_order_from_b0_not_score":result["orders_different_from_b0_not_quality_score"],
        "receipt_sha256":sha256(raw).hexdigest(),
        "m6_consumed":result["research673_m6_formal_attempt_used"],
    },sort_keys=True))


if __name__=="__main__":
    main()
