from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN_COMMIT = "b693ca84722149e91e5a6e67b5d2b292491097ac"
PLAN_PATH = "experiments/r8c_assurance_probe_v01/p_s_power_study_plan.json"
PLAN_SHA256 = "a0894f9fcfa49311571de80fc6a91afdc19a5eb48d9104fd142591089d59f8d7"
HARNESS_PATHS = [
    "experiments/r8c_assurance_probe_v01/README.md",
    "experiments/r8c_assurance_probe_v01/p_s_stochastic_power.py",
]


class ProbeFailure(RuntimeError):
    pass


def git_bytes(*args: str) -> bytes:
    cp = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=False)
    if cp.returncode:
        raise ProbeFailure(
            "git failed: " + " ".join(args) + "\n" + cp.stderr.decode("utf-8", errors="replace")
        )
    return cp.stdout


def blob(commit: str, path: str) -> bytes:
    return git_bytes("show", f"{commit}:{path}")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def harness_binding(commit: str) -> dict[str, object]:
    return {
        "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
        "commit": commit,
        "files": {path: sha256(blob(commit, path)) for path in HARNESS_PATHS},
    }


def load_plan() -> dict[str, object]:
    raw = blob(PLAN_COMMIT, PLAN_PATH)
    if sha256(raw) != PLAN_SHA256:
        raise ProbeFailure("frozen P-S plan Git-blob SHA-256 mismatch")
    plan = json.loads(raw)
    if plan.get("status") != "FROZEN_BEFORE_POWER_CALCULATION":
        raise ProbeFailure("P-S plan was not frozen before calculation")
    source_commit = str(plan["source_commit"])
    for binding in plan["source_bindings"]:
        source = blob(source_commit, str(binding["path"]))
        if sha256(source) != binding["git_blob_content_sha256"]:
            raise ProbeFailure(f"source binding drift: {binding['path']}")
    return plan


def sample_variance(values: list[float]) -> float:
    if len(values) < 2:
        raise ProbeFailure("sample variance requires at least two values")
    return statistics.variance(values)


def observed_variance(plan: dict[str, object]) -> dict[str, object]:
    clusters = plan["observed_design"]["independent_item_clusters"]
    if len(clusters) < 2:
        raise ProbeFailure("P-S requires at least two independent item clusters")

    cluster_rows: list[dict[str, object]] = []
    pooled_ss = 0.0
    pooled_df = 0
    raw_pairs: list[float] = []
    repeat_counts: set[int] = set()
    for cluster in clusters:
        values = [float(x) for x in cluster["repeated_paired_differences"]]
        if len(values) < 2:
            raise ProbeFailure(f"{cluster['item_id']} lacks repeated paired observations")
        variance = sample_variance(values)
        mean = statistics.mean(values)
        pooled_ss += (len(values) - 1) * variance
        pooled_df += len(values) - 1
        raw_pairs.extend(values)
        repeat_counts.add(len(values))
        cluster_rows.append(
            {
                "item_id": cluster["item_id"],
                "n_repeats": len(values),
                "paired_mean": mean,
                "paired_sample_variance": variance,
                "paired_sample_sd": math.sqrt(variance),
            }
        )

    if pooled_df <= 0:
        raise ProbeFailure("no within-item degrees of freedom")
    sigma2 = pooled_ss / pooled_df
    if not math.isfinite(sigma2) or sigma2 <= 0:
        raise ProbeFailure("within-item paired stochastic variance is not finite and positive")
    sigma = math.sqrt(sigma2)
    item_means = [float(row["paired_mean"]) for row in cluster_rows]
    grand_item_mean = statistics.mean(item_means)
    between_item_mean_variance = sample_variance(item_means)

    tau_mom: float | None = None
    if len(repeat_counts) == 1:
        repeats = next(iter(repeat_counts))
        tau_mom = max(0.0, between_item_mean_variance - sigma2 / repeats)

    naive_raw_variance = sample_variance(raw_pairs)
    naive_se = math.sqrt(naive_raw_variance / len(raw_pairs))
    conservative_tau = 2.0 * sigma
    current_j = len(cluster_rows)
    if len(repeat_counts) != 1:
        raise ProbeFailure("current negative control expects balanced repeated items")
    current_r = next(iter(repeat_counts))
    cluster_sensitive_se = math.sqrt(
        (conservative_tau**2 + sigma2 / current_r) / current_j
    )

    return {
        "independent_item_count": len(cluster_rows),
        "paired_repeat_count": len(raw_pairs),
        "item_rows": cluster_rows,
        "grand_mean_of_item_effects": grand_item_mean,
        "pooled_within_item_variance_sigma2": sigma2,
        "pooled_within_item_sd_sigma": sigma,
        "between_item_sample_variance_of_item_means": between_item_mean_variance,
        "method_of_moments_tau2_truncated": tau_mom,
        "tau_estimation_warning": "J=2 is insufficient for a reliable population heterogeneity estimate; tau_hat is descriptive only.",
        "pseudo_independence": {
            "naive_n": len(raw_pairs),
            "naive_raw_pair_sample_variance": naive_raw_variance,
            "naive_standard_error": naive_se,
            "cluster_sensitive_tau_over_sigma": 2.0,
            "cluster_sensitive_standard_error_current_design": cluster_sensitive_se,
            "cluster_sensitive_exceeds_naive": cluster_sensitive_se > naive_se,
            "naive_allowed_for_recommendation": False,
        },
    }


def z_values(alpha: float, power: float) -> tuple[float, float, float]:
    normal = statistics.NormalDist()
    z_alpha = normal.inv_cdf(1.0 - alpha / 2.0)
    z_power = normal.inv_cdf(power)
    return z_alpha, z_power, (z_alpha + z_power) ** 2


def required_items(
    sigma2: float,
    sigma: float,
    tau_over_sigma: float,
    repeats: int,
    delta: float,
    factor: float,
) -> dict[str, object]:
    tau = tau_over_sigma * sigma
    per_item_mean_variance = tau**2 + sigma2 / repeats
    raw_required = factor * per_item_mean_variance / (delta**2)
    j = max(2, math.ceil(raw_required))
    return {
        "mde": delta,
        "repeats_per_item": repeats,
        "tau_over_sigma": tau_over_sigma,
        "tau": tau,
        "per_item_mean_variance": per_item_mean_variance,
        "raw_required_items": raw_required,
        "required_independent_items": j,
        "total_candidate_baseline_treatment_executions": 2 * j * repeats,
    }


def power_table(plan: dict[str, object], observed: dict[str, object]) -> dict[str, object]:
    contract = plan["analysis_contract"]
    alpha = float(contract["alpha"])
    power = float(contract["target_power"])
    z_alpha, z_power, factor = z_values(alpha, power)
    sigma2 = float(observed["pooled_within_item_variance_sigma2"])
    sigma = float(observed["pooled_within_item_sd_sigma"])
    rows: list[dict[str, object]] = []
    for mde_row in contract["mde_grid"]:
        delta = float(mde_row["delta"])
        for repeats in contract["repeat_grid"]:
            for tau_ratio in contract["between_item_sensitivity"]["tau_over_sigma_grid"]:
                row = required_items(
                    sigma2,
                    sigma,
                    float(tau_ratio),
                    int(repeats),
                    delta,
                    factor,
                )
                row["mde_role"] = mde_row["role"]
                rows.append(row)

    return {
        "alpha": alpha,
        "target_power": power,
        "z_two_sided_alpha": z_alpha,
        "z_power": z_power,
        "squared_quantile_sum": factor,
        "rows": rows,
    }


def feasibility(plan: dict[str, object], table: dict[str, object]) -> dict[str, object]:
    candidates = [
        row
        for row in table["rows"]
        if abs(float(row["mde"]) - 0.10) < 1e-12
        and abs(float(row["tau_over_sigma"]) - 2.0) < 1e-12
        and int(row["repeats_per_item"]) in {2, 3, 5}
    ]
    candidates.sort(
        key=lambda row: (
            int(row["total_candidate_baseline_treatment_executions"]),
            int(row["required_independent_items"]),
        )
    )
    if not candidates:
        raise ProbeFailure("conservative feasibility candidates missing")
    best = candidates[0]
    within_bound = int(best["total_candidate_baseline_treatment_executions"]) <= 200
    return {
        "conservative_condition": {
            "mde": 0.10,
            "tau_over_sigma": 2.0,
            "allowed_repeats": [2, 3, 5],
            "max_total_treatment_executions": 200,
        },
        "best_candidate": best,
        "within_frozen_feasibility_bound": within_bound,
        "all_conservative_candidates": candidates,
    }


def evaluate(harness_commit: str) -> dict[str, object]:
    plan = load_plan()
    observed = observed_variance(plan)
    table = power_table(plan, observed)
    feasible = feasibility(plan, table)

    finite_table = all(
        math.isfinite(float(row["raw_required_items"]))
        and int(row["required_independent_items"]) >= 2
        for row in table["rows"]
    )
    cluster_rule_honored = (
        observed["independent_item_count"] == plan["observed_design"]["independent_item_count"]
        and observed["paired_repeat_count"] == plan["observed_design"]["paired_run_count"]
        and observed["independent_item_count"] < observed["paired_repeat_count"]
    )
    negative_control_pass = bool(
        observed["pseudo_independence"]["cluster_sensitive_exceeds_naive"]
        and not observed["pseudo_independence"]["naive_allowed_for_recommendation"]
    )
    public_private_required = bool(
        plan["public_private_release_contract"]["required_for_decision_grade_blocking"]
        and plan["public_private_release_contract"]["split_unit"] == "INDEPENDENT_ITEM"
    )
    current_evidence_observe_only = observed["independent_item_count"] == 2

    criteria = {
        "positive_within_item_variance_estimated": float(observed["pooled_within_item_variance_sigma2"]) > 0.0,
        "independent_items_distinguished_from_repeated_runs": cluster_rule_honored,
        "finite_item_counts_for_all_preregistered_scenarios": finite_table,
        "conservative_mde_010_campaign_within_200_treatment_executions": bool(feasible["within_frozen_feasibility_bound"]),
        "pseudo_independence_negative_control_passes": negative_control_pass,
        "item_clustered_paired_campaign_model_preserved": "item-clustered" in plan["analysis_contract"]["future_campaign_primary_analysis"],
        "public_private_item_level_split_required_for_blocking": public_private_required,
        "current_two_item_evidence_not_promoted_to_decision_grade_generalization": current_evidence_observe_only,
    }
    result = "PASS" if all(criteria.values()) else "INCONCLUSIVE"

    return {
        "probe": "P-S",
        "protocol": "Research 277",
        "candidate": "WARRANT-F V0.2",
        "result": result,
        "plan_binding": {
            "commit": PLAN_COMMIT,
            "path": PLAN_PATH,
            "git_blob_content_sha256": PLAN_SHA256,
        },
        "harness_binding": harness_binding(harness_commit),
        "observed_evidence": observed,
        "power_planning": table,
        "feasibility": feasible,
        "campaign_contract": {
            "paired_candidate_baseline_by_item": True,
            "item_clustered_when_repeated": True,
            "one_decisive_metric": plan["observed_design"]["primary_metric"],
            "public_private_split_unit": plan["public_private_release_contract"]["split_unit"],
            "all_repeats_of_item_same_partition": True,
            "no_retry_to_green": True,
            "current_evidence_status_for_decision_grade_block": "OBSERVE_ONLY",
        },
        "criteria": criteria,
        "interpretation": {
            "future_decision_grade_campaign_is_designable": result == "PASS",
            "current_prototype_v0_is_decision_grade_generalization_evidence": False,
            "between_item_heterogeneity_identified_by_current_evidence": False,
            "target_architecture_amendment_required": False if result == "PASS" else None,
            "physical_migration_authorized": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--harness-commit", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = evaluate(args.harness_commit)
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "probe": payload["probe"],
                "result": payload["result"],
                "sigma2": payload["observed_evidence"]["pooled_within_item_variance_sigma2"],
                "sigma": payload["observed_evidence"]["pooled_within_item_sd_sigma"],
                "best_conservative_campaign": payload["feasibility"]["best_candidate"],
                "criteria_passed": sum(payload["criteria"].values()),
                "criteria_total": len(payload["criteria"]),
            },
            indent=2,
        )
    )
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
