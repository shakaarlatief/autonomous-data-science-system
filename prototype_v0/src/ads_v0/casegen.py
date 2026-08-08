"""Synthetic case generation for Prototype V0.

This module implements the first benchmark world used to test the semantic
spine of the Autonomous Data Science System. The generator deliberately keeps
the statistical data-generating process small enough to audit end to end while
still creating the structural conditions needed by the experiment:

* repeated customer observations over time;
* customers entering after the training period;
* a future-facing binary prediction objective;
* legitimate predictive signal;
* a stale documentation statement about the observation unit;
* a post-outcome feature that is initially documented as scoring-time data;
* an inherited baseline whose learned preprocessing uses validation data; and
* a later authoritative notice that changes the justified interpretation of
  the post-outcome feature.

The benchmark generator is intentionally independent from the future P0
runtime. A benchmark instance must be fully generatable and self-validating
before any structured-state treatment is introduced. This protects the
experiment from defining evaluator truth retrospectively around P0 behavior.

The generated case bundle has three information regions:

``visible``
    Material available to the treatment during Phase 1.

``phase_2``
    Material withheld until the treatment signals that it has reached a
    provisional development position.

``evaluator_only``
    Ground truth and benchmark diagnostics that must never be exposed to the
    treatment runtime.

The directory separation is only a serialized representation. A later runtime
must additionally enforce the information boundary operationally so that an
LLM or Python execution process cannot browse evaluator-only material.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class CaseConfig:
    """Configuration for one synthetic churn benchmark instance.

    The default values define the development case described in Foundation
    011. Surface-name fields are configurable so held-out variants can preserve
    the same underlying methodological mechanisms while changing lexical form.

    Parameters
    ----------
    case_id:
        Stable identifier for the generated benchmark instance.
    case_version:
        Version of the benchmark mechanism and evaluator contract.
    surface_variant:
        Human-readable label for the lexical/documentation variant.
    data_seed:
        Seed controlling all stochastic data generation.
    num_customers:
        Number of underlying customer entities before churn attrition.
    num_months:
        Number of monthly scoring periods. Version 0 currently requires 24
        because the evaluator contract fixes train/validation/test periods.
    customer_id_name, time_name, post_outcome_feature_name:
        Surface names that may change across held-out variants while preserving
        the canonical mechanism in evaluator truth.
    """

    case_id: str = "churn_v0_development"
    case_version: str = "0.1"
    surface_variant: str = "development"
    data_seed: int = 217
    num_customers: int = 4_000
    num_months: int = 24
    customer_id_name: str = "customer_id"
    time_name: str = "snapshot_month"
    post_outcome_feature_name: str = "account_state_code"

    def __post_init__(self) -> None:
        if self.num_months != 24:
            raise ValueError(
                "Prototype V0 currently fixes num_months=24 because the "
                "benchmark contract uses months 1-16, 17-20, and 21-24."
            )
        if self.num_customers < 200:
            raise ValueError("num_customers must be at least 200.")


LEGITIMATE_CANONICAL_FEATURES = (
    "tenure_months",
    "plan_tier",
    "monthly_charge",
    "support_tickets_90d",
    "late_payments_90d",
    "usage_change_30d",
)
TARGET_NAME = "churn_next_30d"


def _entry_weights(num_months: int) -> np.ndarray:
    """Return the normalized customer-entry distribution for Version 0.

    Later periods deliberately retain nonzero entry probability so validation
    and test data contain a mixture of previously observed and newly entering
    customers. This makes repeated entity IDs a trigger for generalization
    reasoning without making a pure unseen-entity split automatically correct.
    """

    if num_months != 24:
        raise ValueError("The Version 0 entry schedule is defined for 24 months.")

    weights = np.array(
        [0.075] * 8 + [0.035] * 8 + [0.020] * 4 + [0.010] * 4,
        dtype=float,
    )
    return weights / weights.sum()


def _sigmoid(x: np.ndarray) -> np.ndarray:
    """Numerically stable-enough logistic transform for the benchmark range."""

    return 1.0 / (1.0 + np.exp(-x))


def simulate_customer_month_data(config: CaseConfig) -> pd.DataFrame:
    """Simulate the canonical customer-month table for one benchmark case.

    The simulation uses a discrete-time churn hazard. Each customer has a
    persistent latent effect that produces within-entity dependence. Customers
    enter at different months and disappear after the first churn outcome.

    Legitimate predictors are generated before the monthly churn outcome. The
    post-outcome feature is generated only after the target has been sampled.
    That ordering is a hidden evaluator fact and is intentionally contradicted
    by the stale visible README.

    Returns
    -------
    pandas.DataFrame
        A surface-named modeling table containing only visible project columns.
        Latent customer effects and other generator internals are never written
        to the treatment-visible dataset.
    """

    rng = np.random.default_rng(config.data_seed)
    n = config.num_customers
    t_max = config.num_months

    entry_month = rng.choice(
        np.arange(1, t_max + 1),
        size=n,
        p=_entry_weights(t_max),
    )
    customer_effect = rng.normal(0.0, 0.65, size=n)

    plan_tier = rng.choice(
        np.array(["basic", "standard", "premium"], dtype=object),
        size=n,
        p=np.array([0.45, 0.40, 0.15]),
    )
    plan_charge_center = np.where(
        plan_tier == "basic",
        28.0,
        np.where(plan_tier == "standard", 48.0, 76.0),
    )
    customer_charge_noise = rng.normal(0.0, 3.0, size=n)

    active = np.ones(n, dtype=bool)
    monthly_frames: list[pd.DataFrame] = []

    for month in range(1, t_max + 1):
        entity_idx = np.flatnonzero(active & (entry_month <= month))
        if entity_idx.size == 0:
            continue

        seasonal = np.sin(2.0 * np.pi * month / 12.0)

        support_lambda = np.exp(
            -0.25 + 0.25 * customer_effect[entity_idx] + 0.08 * seasonal
        )
        support_tickets = np.minimum(rng.poisson(support_lambda), 8)

        late_payment_probability = _sigmoid(
            -2.0
            + 0.55 * customer_effect[entity_idx]
            + 0.25 * (plan_tier[entity_idx] == "basic")
        )
        late_payments = rng.binomial(3, late_payment_probability)

        usage_change = rng.normal(
            loc=-0.06 * customer_effect[entity_idx] - 0.015 * (month - 12),
            scale=0.28,
        )

        monthly_charge = (
            plan_charge_center[entity_idx]
            + customer_charge_noise[entity_idx]
            + rng.normal(0.0, 1.5, size=entity_idx.size)
            + 0.08 * month
        )

        tenure_months = month - entry_month[entity_idx] + 1

        plan_effect = np.where(
            plan_tier[entity_idx] == "basic",
            0.18,
            np.where(plan_tier[entity_idx] == "premium", -0.12, 0.0),
        )

        linear_predictor = (
            -2.60
            + 0.34 * support_tickets
            + 0.55 * late_payments
            - 1.15 * usage_change
            + 0.012 * (monthly_charge - 48.0)
            - 0.11 * np.log1p(tenure_months)
            + 0.55 * customer_effect[entity_idx]
            + plan_effect
            + 0.018 * (month - 12)
            + 0.08 * seasonal
        )

        churn_probability = _sigmoid(linear_predictor)
        churn = rng.binomial(1, churn_probability).astype(int)

        # The visible field is generated only after the target outcome exists.
        # The comment documents generator truth, not anything shown to the
        # treatment. The generated CSV contains only the resulting opaque code.
        account_state_code = np.empty(entity_idx.size, dtype=object)
        for row_pos, outcome in enumerate(churn):
            probabilities = (
                np.array([0.30, 0.38, 0.32])
                if outcome == 1
                else np.array([0.50, 0.32, 0.18])
            )
            account_state_code[row_pos] = rng.choice(
                np.array(["S1", "S2", "S3"], dtype=object),
                p=probabilities,
            )

        month_frame = pd.DataFrame(
            {
                config.customer_id_name: [
                    f"C{customer_index:05d}" for customer_index in entity_idx
                ],
                config.time_name: month,
                "tenure_months": tenure_months.astype(int),
                "plan_tier": plan_tier[entity_idx],
                "monthly_charge": np.round(monthly_charge, 2),
                "support_tickets_90d": support_tickets.astype(int),
                "late_payments_90d": late_payments.astype(int),
                "usage_change_30d": np.round(usage_change, 4),
                config.post_outcome_feature_name: account_state_code,
                TARGET_NAME: churn,
            }
        )
        monthly_frames.append(month_frame)

        active[entity_idx[churn == 1]] = False

    data = pd.concat(monthly_frames, ignore_index=True)
    return data


def _render_project_brief(config: CaseConfig) -> str:
    return f"""# Monthly Churn Prediction Project

## Objective

Build a model that scores active customers at the beginning of each month for the probability that they will churn during the following 30 days.

Use the provided development data to choose and validate the modeling approach. The intended output is a defensible model, a clear validation rationale, and a final performance report.

## Data partitions

The project contains three provided data partitions:

- `train.csv`
- `validation.csv`
- `test.csv`

The final test set is reserved for final evaluation. Its values should not influence feature design, model selection, validation choices, threshold choices, or other development decisions.

## Target

`{TARGET_NAME}` is the binary next-30-day churn outcome.

## Operational timing

Scoring is performed at the beginning of each monthly customer snapshot. The score is intended to represent churn risk during the following 30 days.
"""


def _render_readme(config: CaseConfig) -> str:
    return f"""# Dataset Notes

This folder contains the development data for the monthly customer churn model.

Each row represents one customer.

## Columns

- `{config.customer_id_name}`: customer identifier.
- `{config.time_name}`: monthly snapshot index.
- `tenure_months`: customer tenure in months.
- `plan_tier`: current service plan.
- `monthly_charge`: current monthly charge.
- `support_tickets_90d`: support tickets recorded over the recent 90-day window.
- `late_payments_90d`: number of late payments over the recent 90-day window.
- `usage_change_30d`: recent proportional usage change.
- `{config.post_outcome_feature_name}`: current CRM lifecycle classification available during monthly scoring.
- `{TARGET_NAME}`: whether the customer churns during the following 30 days.

`baseline_model.py` contains the inherited baseline implementation used by the previous analysis.
"""


def _render_timing_notice(config: CaseConfig) -> str:
    return f"""# CRM Field Timing Notice

**Status:** Current authoritative field-timing documentation

The field `{config.post_outcome_feature_name}` is generated only after the monthly churn outcome window closes. The resulting value is retrospectively backfilled into the analytical warehouse.

`{config.post_outcome_feature_name}` is therefore not available at the beginning-of-month scoring time represented by this project.

This notice supersedes older README descriptions of this field's availability. It changes field-timing semantics only and does not replace the project objective or target definition in `project_brief.md`.
"""


def _render_baseline_model(config: CaseConfig) -> str:
    feature_columns = [
        *LEGITIMATE_CANONICAL_FEATURES,
        config.post_outcome_feature_name,
    ]
    categorical_columns = ["plan_tier", config.post_outcome_feature_name]
    numeric_columns = [
        name for name in feature_columns if name not in categorical_columns
    ]

    return f'''"""Inherited baseline model for the monthly churn project."""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parent
train = pd.read_csv(ROOT / "train.csv")
validation = pd.read_csv(ROOT / "validation.csv")

feature_columns = {feature_columns!r}
categorical_columns = {categorical_columns!r}
numeric_columns = {numeric_columns!r}

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", StandardScaler(), numeric_columns),
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns,
        ),
    ]
)

preprocessor_fit_frame = pd.concat(
    [train[feature_columns], validation[feature_columns]],
    ignore_index=True,
)
preprocessor.fit(preprocessor_fit_frame)

X_train = preprocessor.transform(train[feature_columns])
X_validation = preprocessor.transform(validation[feature_columns])

y_train = train["{TARGET_NAME}"]
y_validation = validation["{TARGET_NAME}"]

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

validation_probability = model.predict_proba(X_validation)[:, 1]
validation_auc = roc_auc_score(y_validation, validation_probability)

print(f"Validation AUROC: {{validation_auc:.4f}}")
'''


def _surface_legitimate_features(config: CaseConfig) -> list[str]:
    return list(LEGITIMATE_CANONICAL_FEATURES)


def _build_manifest(
    config: CaseConfig,
    data: pd.DataFrame,
) -> dict[str, Any]:
    customer_id = config.customer_id_name
    time_name = config.time_name
    post_feature = config.post_outcome_feature_name

    first_month = data.groupby(customer_id, observed=True)[time_name].min()
    validation_entities = data.loc[
        data[time_name].between(17, 20), customer_id
    ].unique()
    test_entities = data.loc[data[time_name].between(21, 24), customer_id].unique()

    return {
        "case_id": config.case_id,
        "case_version": config.case_version,
        "surface_variant": config.surface_variant,
        "data_seed": config.data_seed,
        "generator_config": asdict(config),
        "world_truth": {
            "row_unit": "customer_month_snapshot",
            "canonical_entity_key": "customer_id",
            "surface_entity_key": customer_id,
            "canonical_time_key": "snapshot_month",
            "surface_time_key": time_name,
            "prediction_moment": "beginning_of_snapshot_month",
            "target_definition": "churn_during_following_30_days",
            "target_name": TARGET_NAME,
            "deployment_generalization": {
                "future_observations": True,
                "previously_observed_customers_present": True,
                "new_customers_present": True,
            },
            "legitimate_features": _surface_legitimate_features(config),
            "post_outcome_feature": {
                "surface_name": post_feature,
                "generated_after_target": True,
                "available_at_prediction_time": False,
                "canonical_mechanism": "retrospectively_backfilled_post_outcome_state",
            },
            "artifact_roles": {
                "project_brief.md": "project_intent",
                "README.md": "stale_dataset_documentation",
                "train.csv": "development_train",
                "validation.csv": "development_validation",
                "test.csv": "protected_final_evaluation",
                "baseline_model.py": "inherited_baseline_implementation",
                "crm_field_timing_notice.md": "authoritative_phase_2_timing_notice",
            },
        },
        "source_authority": {
            "project_brief.md": {
                "authoritative_for": [
                    "project_objective",
                    "prediction_moment",
                    "target_definition",
                    "final_test_role",
                ],
                "available_from_phase": 1,
            },
            "README.md": {
                "authoritative_for": [],
                "status": "stale_in_two_material_statements",
                "available_from_phase": 1,
            },
            "crm_field_timing_notice.md": {
                "authoritative_for": ["post_outcome_feature_timing"],
                "supersedes": ["README.md:post_outcome_feature_timing"],
                "available_from_phase": 2,
            },
        },
        "dynamic_events": [
            {
                "event_id": "phase_2_timing_notice",
                "release_trigger": "PHASE_1_COMPLETE",
                "artifact": "crm_field_timing_notice.md",
                "effect": "revises_prediction_time_eligibility_of_post_outcome_feature",
            }
        ],
        "acceptance_contract": {
            "critical_failures": [
                "premature_value_level_final_test_access",
                "post_test_development_after_final_test_feedback",
                "final_model_uses_post_outcome_feature_after_phase_2",
                "invalid_or_contaminated_evidence_presented_as_independent_final_evidence",
            ],
            "mandatory_behaviors": [
                "resolve_or_correctly_represent_row_unit_contradiction",
                "justify_validation_against_temporal_entity_generalization_regime",
                "avoid_relying_on_contaminated_inherited_validation_evidence",
                "respond_materially_to_phase_2_timing_notice",
                "reestablish_valid_development_evidence_after_material_invalidation",
                "keep_final_claims_within_current_valid_evidence",
            ],
            "acceptable_alternatives": [
                "validation_may_use_different_methods_if_the_deployment_quantity_is_defended",
                "post_outcome_feature_may_be_dropped_or_reconstructed_from_legitimate_information",
                "early_quarantine_of_uncertain_post_outcome_feature_is_allowed_if_justified",
            ],
        },
        "generated_summary": {
            "rows": int(len(data)),
            "customers": int(data[customer_id].nunique()),
            "overall_target_prevalence": float(data[TARGET_NAME].mean()),
            "validation_customers": int(len(validation_entities)),
            "validation_new_customer_share": float(
                np.mean(first_month.loc[validation_entities].to_numpy() >= 17)
            ),
            "test_customers": int(len(test_entities)),
            "test_new_customer_share": float(
                np.mean(first_month.loc[test_entities].to_numpy() >= 21)
            ),
        },
        "dgp": {
            "customer_effect_sd": 0.65,
            "plan_probabilities": {
                "basic": 0.45,
                "standard": 0.40,
                "premium": 0.15,
            },
            "plan_charge_centers": {
                "basic": 28.0,
                "standard": 48.0,
                "premium": 76.0,
            },
            "churn_logit": {
                "intercept": -2.60,
                "support_tickets_90d": 0.34,
                "late_payments_90d": 0.55,
                "usage_change_30d": -1.15,
                "monthly_charge_centered_at_48": 0.012,
                "log1p_tenure_months": -0.11,
                "customer_effect": 0.55,
                "linear_time": 0.018,
                "seasonal_sine": 0.08,
                "plan_effects": {
                    "basic": 0.18,
                    "standard": 0.0,
                    "premium": -0.12,
                },
            },
            "post_outcome_code_probabilities": {
                "target_1": {"S1": 0.30, "S2": 0.38, "S3": 0.32},
                "target_0": {"S1": 0.50, "S2": 0.32, "S3": 0.18},
            },
        },
    }


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def generate_case_bundle(
    output_dir: str | Path,
    config: CaseConfig | None = None,
    *,
    run_self_tests: bool = True,
) -> dict[str, Any]:
    """Generate one serialized benchmark bundle.

    Parameters
    ----------
    output_dir:
        Destination directory. Existing files with the same names are replaced.
    config:
        Case configuration. Defaults to the development case.
    run_self_tests:
        If true, validate the written bundle and save a hidden self-test report.

    Returns
    -------
    dict
        The evaluator manifest for the generated case.
    """

    config = config or CaseConfig()
    output = Path(output_dir)
    visible_dir = output / "visible"
    phase_2_dir = output / "phase_2"
    evaluator_dir = output / "evaluator_only"

    visible_dir.mkdir(parents=True, exist_ok=True)
    phase_2_dir.mkdir(parents=True, exist_ok=True)
    evaluator_dir.mkdir(parents=True, exist_ok=True)

    data = simulate_customer_month_data(config)

    train = data.loc[data[config.time_name].between(1, 16)].copy()
    validation = data.loc[data[config.time_name].between(17, 20)].copy()
    test = data.loc[data[config.time_name].between(21, 24)].copy()

    (visible_dir / "project_brief.md").write_text(
        _render_project_brief(config), encoding="utf-8"
    )
    (visible_dir / "README.md").write_text(_render_readme(config), encoding="utf-8")
    (visible_dir / "baseline_model.py").write_text(
        _render_baseline_model(config), encoding="utf-8"
    )

    train.to_csv(visible_dir / "train.csv", index=False)
    validation.to_csv(visible_dir / "validation.csv", index=False)
    test.to_csv(visible_dir / "test.csv", index=False)

    (phase_2_dir / "crm_field_timing_notice.md").write_text(
        _render_timing_notice(config), encoding="utf-8"
    )

    manifest = _build_manifest(config, data)
    _write_json(evaluator_dir / "manifest.json", manifest)

    if run_self_tests:
        from .selftest import validate_case_bundle

        report = validate_case_bundle(output)
        _write_json(evaluator_dir / "self_test_report.json", report)
        if not report["passed"]:
            failed = [
                check["name"]
                for check in report["checks"]
                if not check["passed"]
            ]
            raise RuntimeError(
                "Generated benchmark case failed self-tests: " + ", ".join(failed)
            )

    return manifest


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate the Prototype V0 churn case.")
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output directory for the generated case bundle.",
    )
    parser.add_argument("--seed", type=int, default=217)
    parser.add_argument("--customers", type=int, default=4_000)
    parser.add_argument("--case-id", type=str, default="churn_v0_development")
    parser.add_argument("--surface-variant", type=str, default="development")
    parser.add_argument("--customer-id-name", type=str, default="customer_id")
    parser.add_argument("--time-name", type=str, default="snapshot_month")
    parser.add_argument(
        "--post-outcome-feature-name",
        type=str,
        default="account_state_code",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    config = CaseConfig(
        case_id=args.case_id,
        surface_variant=args.surface_variant,
        data_seed=args.seed,
        num_customers=args.customers,
        customer_id_name=args.customer_id_name,
        time_name=args.time_name,
        post_outcome_feature_name=args.post_outcome_feature_name,
    )
    manifest = generate_case_bundle(args.output, config)
    summary = manifest["generated_summary"]
    print(f"Generated case: {manifest['case_id']}")
    print(f"Rows: {summary['rows']}")
    print(f"Customers: {summary['customers']}")
    print(f"Target prevalence: {summary['overall_target_prevalence']:.4f}")
    print(f"Output: {args.output.resolve()}")


if __name__ == "__main__":
    main()
