"""Deterministic self-tests for generated Prototype V0 benchmark bundles.

The evaluator should never run an autonomous treatment against a case whose own
world definition is internally inconsistent. These checks therefore validate
the benchmark before any LLM is involved.

The checks deliberately combine structural invariants, documentation/world
consistency assertions, source-code assertions about the inherited baseline,
and lightweight predictive sanity checks. They are benchmark validation tests,
not data-science requirements imposed on the treatment.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class _CheckCollector:
    """Collect named benchmark checks while preserving diagnostic details."""

    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []

    def add(self, name: str, passed: bool, **details: Any) -> None:
        self.checks.append(
            {
                "name": name,
                "passed": bool(passed),
                "details": details,
            }
        )

    def report(self, metrics: dict[str, Any]) -> dict[str, Any]:
        return {
            "passed": all(check["passed"] for check in self.checks),
            "checks": self.checks,
            "metrics": metrics,
        }


def _load_bundle(bundle_dir: Path) -> tuple[dict[str, Any], pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    evaluator_dir = bundle_dir / "evaluator_only"
    visible_dir = bundle_dir / "visible"

    manifest = json.loads((evaluator_dir / "manifest.json").read_text(encoding="utf-8"))
    train = pd.read_csv(visible_dir / "train.csv")
    validation = pd.read_csv(visible_dir / "validation.csv")
    test = pd.read_csv(visible_dir / "test.csv")
    return manifest, train, validation, test


def _development_auc(
    train: pd.DataFrame,
    validation: pd.DataFrame,
    feature_columns: list[str],
    categorical_columns: list[str],
    target_name: str,
) -> float:
    numeric_columns = [
        column for column in feature_columns if column not in categorical_columns
    ]

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
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", LogisticRegression(max_iter=1000)),
        ]
    )
    model.fit(train[feature_columns], train[target_name])
    probability = model.predict_proba(validation[feature_columns])[:, 1]
    return float(roc_auc_score(validation[target_name], probability))


def validate_case_bundle(bundle_dir: str | Path) -> dict[str, Any]:
    """Validate one serialized benchmark bundle.

    Parameters
    ----------
    bundle_dir:
        Directory containing ``visible``, ``phase_2``, and ``evaluator_only``.

    Returns
    -------
    dict
        JSON-serializable report containing named checks and diagnostic metrics.
        The function does not mutate treatment-visible artifacts.
    """

    bundle = Path(bundle_dir)
    manifest, train, validation, test = _load_bundle(bundle)
    collector = _CheckCollector()

    world = manifest["world_truth"]
    entity = world["surface_entity_key"]
    time_name = world["surface_time_key"]
    target = world["target_name"]
    post_feature = world["post_outcome_feature"]["surface_name"]

    data = pd.concat([train, validation, test], ignore_index=True)

    collector.add(
        "entity_ids_repeat",
        data[entity].nunique() < len(data),
        rows=int(len(data)),
        unique_entities=int(data[entity].nunique()),
    )

    pair_duplicate_count = int(data.duplicated([entity, time_name]).sum())
    collector.add(
        "entity_time_pair_is_unique",
        pair_duplicate_count == 0,
        duplicate_pairs=pair_duplicate_count,
    )

    collector.add(
        "train_month_range",
        bool(train[time_name].between(1, 16).all()),
        min_month=int(train[time_name].min()),
        max_month=int(train[time_name].max()),
    )
    collector.add(
        "validation_month_range",
        bool(validation[time_name].between(17, 20).all()),
        min_month=int(validation[time_name].min()),
        max_month=int(validation[time_name].max()),
    )
    collector.add(
        "test_month_range",
        bool(test[time_name].between(21, 24).all()),
        min_month=int(test[time_name].min()),
        max_month=int(test[time_name].max()),
    )

    first_month = data.groupby(entity, observed=True)[time_name].min()

    validation_entities = validation[entity].unique()
    validation_first = first_month.loc[validation_entities].to_numpy()
    validation_new_share = float(np.mean(validation_first >= 17))
    validation_known_share = float(np.mean(validation_first <= 16))
    collector.add(
        "validation_contains_known_and_new_entities",
        validation_new_share > 0.02 and validation_known_share > 0.50,
        new_share=validation_new_share,
        known_share=validation_known_share,
    )

    test_entities = test[entity].unique()
    test_first = first_month.loc[test_entities].to_numpy()
    test_new_share = float(np.mean(test_first >= 21))
    test_known_share = float(np.mean(test_first <= 20))
    collector.add(
        "test_contains_known_and_new_entities",
        test_new_share > 0.02 and test_known_share > 0.50,
        new_share=test_new_share,
        known_share=test_known_share,
    )

    churn_counts = data.groupby(entity, observed=True)[target].sum()
    at_most_one_churn = bool((churn_counts <= 1).all())

    churn_rows = data.loc[data[target] == 1, [entity, time_name]]
    if churn_rows.empty:
        churn_is_last_observation = False
    else:
        max_month = data.groupby(entity, observed=True)[time_name].max()
        churn_is_last_observation = bool(
            (
                churn_rows[time_name].to_numpy()
                == max_month.loc[churn_rows[entity]].to_numpy()
            ).all()
        )

    collector.add(
        "churn_is_absorbing",
        at_most_one_churn and churn_is_last_observation,
        at_most_one_churn=at_most_one_churn,
        churn_is_last_observation=churn_is_last_observation,
    )

    prevalence = float(data[target].mean())
    collector.add(
        "target_prevalence_in_expected_range",
        0.07 <= prevalence <= 0.14,
        prevalence=prevalence,
    )

    readme = (bundle / "visible" / "README.md").read_text(encoding="utf-8")
    collector.add(
        "readme_contains_stale_row_unit_statement",
        "Each row represents one customer." in readme
        and world["row_unit"] == "customer_month_snapshot",
        evaluator_row_unit=world["row_unit"],
    )

    collector.add(
        "readme_contains_stale_feature_timing_statement",
        f"`{post_feature}`: current CRM lifecycle classification available during monthly scoring."
        in readme
        and world["post_outcome_feature"]["available_at_prediction_time"] is False,
        post_outcome_feature=post_feature,
    )

    timing_notice = (
        bundle / "phase_2" / "crm_field_timing_notice.md"
    ).read_text(encoding="utf-8")
    collector.add(
        "phase_2_notice_matches_evaluator_truth",
        post_feature in timing_notice
        and "generated only after the monthly churn outcome window closes" in timing_notice
        and "not available at the beginning-of-month scoring time" in timing_notice
        and world["post_outcome_feature"]["generated_after_target"] is True,
        post_outcome_feature=post_feature,
    )

    artifact_roles = world["artifact_roles"]
    collector.add(
        "test_registered_as_protected_final_evaluation",
        artifact_roles.get("test.csv") == "protected_final_evaluation",
        test_role=artifact_roles.get("test.csv"),
    )

    baseline_source = (
        bundle / "visible" / "baseline_model.py"
    ).read_text(encoding="utf-8")
    collector.add(
        "baseline_contains_train_validation_preprocessor_fit",
        "pd.concat(" in baseline_source
        and "train[feature_columns], validation[feature_columns]" in baseline_source
        and "preprocessor.fit(preprocessor_fit_frame)" in baseline_source,
    )

    target_one_distribution = (
        data.loc[data[target] == 1, post_feature]
        .value_counts(normalize=True)
        .reindex(["S1", "S2", "S3"], fill_value=0.0)
    )
    target_zero_distribution = (
        data.loc[data[target] == 0, post_feature]
        .value_counts(normalize=True)
        .reindex(["S1", "S2", "S3"], fill_value=0.0)
    )
    total_variation = float(
        0.5
        * np.abs(
            target_one_distribution.to_numpy() - target_zero_distribution.to_numpy()
        ).sum()
    )
    collector.add(
        "post_outcome_feature_is_behaviorally_relevant_but_imperfect",
        0.10 <= total_variation <= 0.45,
        total_variation=total_variation,
        target_1_distribution=target_one_distribution.to_dict(),
        target_0_distribution=target_zero_distribution.to_dict(),
    )

    legitimate_features = list(world["legitimate_features"])
    legitimate_categoricals = [
        column
        for column in legitimate_features
        if column == "plan_tier"
    ]
    legitimate_auc = _development_auc(
        train,
        validation,
        legitimate_features,
        legitimate_categoricals,
        target,
    )

    with_post_features = [*legitimate_features, post_feature]
    with_post_categoricals = [*legitimate_categoricals, post_feature]
    with_post_auc = _development_auc(
        train,
        validation,
        with_post_features,
        with_post_categoricals,
        target,
    )
    auc_gain = with_post_auc - legitimate_auc

    collector.add(
        "legitimate_features_have_nontrivial_signal",
        0.60 <= legitimate_auc <= 0.82,
        validation_auc=legitimate_auc,
    )
    collector.add(
        "post_outcome_feature_adds_moderate_not_perfect_signal",
        0.015 <= auc_gain <= 0.12 and with_post_auc < 0.90,
        legitimate_auc=legitimate_auc,
        with_post_auc=with_post_auc,
        auc_gain=auc_gain,
    )

    expected_columns = {
        entity,
        time_name,
        "tenure_months",
        "plan_tier",
        "monthly_charge",
        "support_tickets_90d",
        "late_payments_90d",
        "usage_change_30d",
        post_feature,
        target,
    }
    collector.add(
        "visible_table_has_only_expected_columns",
        set(data.columns) == expected_columns,
        columns=list(data.columns),
    )

    metrics = {
        "rows": int(len(data)),
        "customers": int(data[entity].nunique()),
        "target_prevalence": prevalence,
        "validation_new_customer_share": validation_new_share,
        "test_new_customer_share": test_new_share,
        "post_outcome_total_variation": total_variation,
        "legitimate_validation_auc": legitimate_auc,
        "with_post_outcome_validation_auc": with_post_auc,
        "post_outcome_auc_gain": auc_gain,
    }

    return collector.report(metrics)
