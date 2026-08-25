from __future__ import annotations

from pathlib import Path


WORKFLOW = Path(".github/workflows/v1-methodological-navigation-coverage-live.yml")


def test_spec022_live_workflow_is_explicit_exact_source_and_secret_gated() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "workflow_dispatch:" in text
    assert "spec022-methodological-navigation-coverage-001" in text
    assert "RUN_SPEC_022_FROZEN" in text
    assert "expected_source_sha" in text
    assert "ref: ${{ inputs.expected_source_sha }}" in text
    assert "OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}" in text
    assert "OPENAI_API_KEY: ''" in text
    assert "openai-agents==0.19.4" in text
    assert "fastembed==0.8.0" in text
    assert "experiments.methodological_navigation_coverage.live_runner" in text
    assert "actions/upload-artifact@v4" in text
    assert "schedule:" not in text
    assert "pull_request:" not in text
    assert "push:" not in text


def test_spec022_live_workflow_preflight_precedes_live_execution() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    preflight = text.index("Validate live-capable implementation without provider calls")
    versions = text.index("Verify exact live dependency versions before execution")
    execute = text.index("Execute frozen Specification 022 live diagnostic")
    upload = text.index("Upload complete frozen result bundle")
    assert preflight < versions < execute < upload
