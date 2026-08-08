from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pandas as pd

from ads_v0.casegen import CaseConfig, generate_case_bundle, simulate_customer_month_data
from ads_v0.selftest import validate_case_bundle


def test_simulation_is_deterministic_for_same_seed() -> None:
    config = CaseConfig(data_seed=91, num_customers=500)

    first = simulate_customer_month_data(config)
    second = simulate_customer_month_data(config)

    pd.testing.assert_frame_equal(first, second)


def test_development_case_generates_and_passes_self_tests(tmp_path: Path) -> None:
    output = tmp_path / "development_case"
    manifest = generate_case_bundle(output, CaseConfig())

    assert (output / "visible" / "project_brief.md").exists()
    assert (output / "visible" / "README.md").exists()
    assert (output / "visible" / "train.csv").exists()
    assert (output / "visible" / "validation.csv").exists()
    assert (output / "visible" / "test.csv").exists()
    assert (output / "visible" / "baseline_model.py").exists()
    assert (output / "phase_2" / "crm_field_timing_notice.md").exists()
    assert (output / "evaluator_only" / "manifest.json").exists()
    assert (output / "evaluator_only" / "self_test_report.json").exists()

    assert manifest["world_truth"]["row_unit"] == "customer_month_snapshot"
    assert (
        manifest["world_truth"]["artifact_roles"]["test.csv"]
        == "protected_final_evaluation"
    )

    report = validate_case_bundle(output)
    assert report["passed"], report


def test_generated_inherited_baseline_is_executable(tmp_path: Path) -> None:
    """The intentionally contaminated baseline must still be valid runnable code.

    The benchmark is supposed to test whether a treatment recognizes the
    baseline's information-boundary problem. A syntax error, missing file, or
    broken estimator would introduce an unrelated implementation failure and
    make that behavioral test ambiguous.
    """

    output = tmp_path / "baseline_execution_case"
    generate_case_bundle(
        output,
        CaseConfig(data_seed=311, num_customers=1_000),
        run_self_tests=False,
    )

    completed = subprocess.run(
        [sys.executable, "baseline_model.py"],
        cwd=output / "visible",
        check=True,
        capture_output=True,
        text=True,
        timeout=60,
    )

    match = re.search(r"Validation AUROC:\s*([0-9.]+)", completed.stdout)
    assert match is not None, completed.stdout

    validation_auc = float(match.group(1))
    assert 0.0 <= validation_auc <= 1.0


def test_surface_variant_names_propagate_through_visible_and_hidden_artifacts(
    tmp_path: Path,
) -> None:
    output = tmp_path / "surface_variant"
    config = CaseConfig(
        case_id="churn_v0_surface_test",
        surface_variant="surface_test",
        data_seed=122,
        customer_id_name="member_key",
        time_name="scoring_period",
        post_outcome_feature_name="lifecycle_flag",
    )

    generate_case_bundle(output, config)

    train = pd.read_csv(output / "visible" / "train.csv")
    readme = (output / "visible" / "README.md").read_text(encoding="utf-8")
    notice = (
        output / "phase_2" / "crm_field_timing_notice.md"
    ).read_text(encoding="utf-8")
    manifest = json.loads(
        (output / "evaluator_only" / "manifest.json").read_text(encoding="utf-8")
    )

    assert "member_key" in train.columns
    assert "scoring_period" in train.columns
    assert "lifecycle_flag" in train.columns
    assert "lifecycle_flag" in readme
    assert "lifecycle_flag" in notice
    assert manifest["world_truth"]["surface_entity_key"] == "member_key"
    assert manifest["world_truth"]["surface_time_key"] == "scoring_period"
    assert (
        manifest["world_truth"]["post_outcome_feature"]["surface_name"]
        == "lifecycle_flag"
    )

    report = validate_case_bundle(output)
    assert report["passed"], report
