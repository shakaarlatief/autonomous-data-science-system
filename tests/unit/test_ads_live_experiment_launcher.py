from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from scripts.ads_live_experiment_launcher import (
    GitHubApiError,
    LaunchAuthorization,
    LaunchRejected,
    RequiredCiRun,
    build_dispatch_request,
    load_registry,
    parse_issue_request,
    run_launcher,
    validate_authorization,
    validate_ci_runs,
    validate_duplicate_state,
    validate_registry_data,
    validate_source_head,
)


REPOSITORY = "shakaarlatief/autonomous-data-science-system"
OWNER = "shakaarlatief"
SOURCE_SHA = "a" * 40
CI_RUN_ID = 123456789
CI_WORKFLOW_NAME = "V1 autonomous live experiment launcher CI"
LAUNCH_ID = "spec018-probe-001"
CONFIRMATION = "RUN_SPEC018_PROBE_001"
WORKFLOW_FILE = "v1-live-launcher-probe.yml"
REF = "v1-autonomous-live-experiment-launcher"


def authorization(*, enabled: bool = True) -> LaunchAuthorization:
    return LaunchAuthorization(
        launch_id=LAUNCH_ID,
        enabled=enabled,
        owner_login=OWNER,
        workflow_file=WORKFLOW_FILE,
        ref=REF,
        expected_source_sha=SOURCE_SHA,
        confirmation=CONFIRMATION,
        required_ci_runs=(RequiredCiRun(run_id=CI_RUN_ID, workflow_name=CI_WORKFLOW_NAME),),
    )


def registry_data(**authorization_overrides: Any) -> dict[str, Any]:
    raw = {
        "launch_id": LAUNCH_ID,
        "enabled": True,
        "owner_login": OWNER,
        "workflow_file": WORKFLOW_FILE,
        "ref": REF,
        "expected_source_sha": SOURCE_SHA,
        "confirmation": CONFIRMATION,
        "required_ci_runs": [{"run_id": CI_RUN_ID, "workflow_name": CI_WORKFLOW_NAME}],
    }
    raw.update(authorization_overrides)
    return {"schema_version": 1, "authorizations": [raw]}


def issue_event(
    *,
    actor: str = OWNER,
    sender: str = OWNER,
    issue_author: str = OWNER,
    repository_owner: str = OWNER,
    title: str = f"[ADS LIVE] {LAUNCH_ID}",
    body: str = f"authorization: {CONFIRMATION}",
) -> tuple[dict[str, Any], str]:
    event = {
        "action": "opened",
        "sender": {"login": sender},
        "issue": {
            "number": 42,
            "title": title,
            "body": body,
            "user": {"login": issue_author},
        },
        "repository": {
            "full_name": REPOSITORY,
            "owner": {"login": repository_owner},
        },
    }
    return event, actor


class FakeClient:
    """Small deterministic GitHub API double used to test fail-closed transport logic."""

    def __init__(self) -> None:
        self.gets: dict[str, Any] = {}
        self.posts: list[tuple[str, dict[str, Any], set[int]]] = []

    def get_json(self, path: str) -> dict[str, Any]:
        if path not in self.gets:
            raise AssertionError(f"unexpected GET {path}")
        value = self.gets[path]
        if isinstance(value, BaseException):
            raise value
        if value is None:
            raise GitHubApiError("not found", status=404)
        return value

    def get_json_optional(self, path: str) -> dict[str, Any] | None:
        if path not in self.gets:
            raise AssertionError(f"unexpected optional GET {path}")
        value = self.gets[path]
        if isinstance(value, BaseException):
            raise value
        return value

    def post_json(self, path: str, payload: dict[str, Any], *, expected_statuses: set[int]) -> dict[str, Any]:
        self.posts.append((path, payload, expected_statuses))
        return {}


def configured_client(*, duplicate_runs: list[dict[str, Any]] | None = None) -> FakeClient:
    client = FakeClient()
    client.gets[f"/repos/{REPOSITORY}/git/ref/heads/{REF}"] = {
        "object": {"type": "commit", "sha": SOURCE_SHA}
    }
    client.gets[f"/repos/{REPOSITORY}/git/ref/tags/{REF}"] = None
    client.gets[f"/repos/{REPOSITORY}/actions/runs/{CI_RUN_ID}"] = {
        "repository": {"full_name": REPOSITORY},
        "name": CI_WORKFLOW_NAME,
        "head_sha": SOURCE_SHA,
        "status": "completed",
        "conclusion": "success",
    }
    client.gets[
        f"/repos/{REPOSITORY}/actions/workflows/{WORKFLOW_FILE}/runs?event=workflow_dispatch&per_page=100"
    ] = {"workflow_runs": duplicate_runs or []}
    return client


# Registry contract


def test_empty_repository_registry_is_valid(tmp_path: Path) -> None:
    path = tmp_path / "registry.json"
    path.write_text(json.dumps({"schema_version": 1, "authorizations": []}), encoding="utf-8")
    assert load_registry(path).authorizations == ()


def test_valid_enabled_registry_is_accepted() -> None:
    registry = validate_registry_data(registry_data())
    assert registry.by_id(LAUNCH_ID).expected_source_sha == SOURCE_SHA


def test_wrong_schema_version_rejected() -> None:
    data = registry_data()
    data["schema_version"] = 2
    with pytest.raises(LaunchRejected, match="INVALID_REGISTRY"):
        validate_registry_data(data)


def test_duplicate_launch_id_rejected() -> None:
    data = registry_data()
    data["authorizations"].append(dict(data["authorizations"][0]))
    with pytest.raises(LaunchRejected, match="duplicate launch_id"):
        validate_registry_data(data)


def test_malformed_sha_rejected() -> None:
    with pytest.raises(LaunchRejected, match="expected_source_sha"):
        validate_registry_data(registry_data(expected_source_sha="ABC"))


def test_workflow_path_traversal_rejected() -> None:
    with pytest.raises(LaunchRejected, match="workflow_file"):
        validate_registry_data(registry_data(workflow_file="../evil.yml"))


def test_shell_like_ref_rejected() -> None:
    with pytest.raises(LaunchRejected, match="Git ref"):
        validate_registry_data(registry_data(ref="main;echo-pwned"))


def test_malformed_confirmation_rejected() -> None:
    with pytest.raises(LaunchRejected, match="confirmation"):
        validate_registry_data(registry_data(confirmation="run me"))


def test_enabled_authorization_requires_ci_evidence() -> None:
    with pytest.raises(LaunchRejected, match="requires CI evidence"):
        validate_registry_data(registry_data(required_ci_runs=[]))


def test_unknown_registry_key_rejected() -> None:
    data = registry_data()
    data["authorizations"][0]["command"] = "rm -rf /"
    with pytest.raises(LaunchRejected, match="invalid keys"):
        validate_registry_data(data)


# Issue grammar and actor authorization


def test_exact_issue_request_is_parsed() -> None:
    event, _ = issue_event()
    request = parse_issue_request(event)
    assert request.issue_number == 42
    assert request.launch_id == LAUNCH_ID
    assert request.confirmation == CONFIRMATION


def test_wrong_title_prefix_rejected() -> None:
    event, _ = issue_event(title=f"run {LAUNCH_ID}")
    with pytest.raises(LaunchRejected, match="INVALID_REQUEST"):
        parse_issue_request(event)


def test_additional_issue_body_content_rejected() -> None:
    event, _ = issue_event(body=f"authorization: {CONFIRMATION}\nref: main")
    with pytest.raises(LaunchRejected, match="unsupported content"):
        parse_issue_request(event)


def test_issue_supplied_fake_workflow_sha_and_command_rejected() -> None:
    event, _ = issue_event(
        body=(
            f"authorization: {CONFIRMATION}\n"
            "workflow: evil.yml\nref: attacker\nsha: deadbeef\ncommand: echo pwned"
        )
    )
    with pytest.raises(LaunchRejected, match="unsupported content"):
        parse_issue_request(event)


def test_unknown_launch_id_rejected_by_registry() -> None:
    registry = validate_registry_data(registry_data())
    with pytest.raises(LaunchRejected, match="UNKNOWN_LAUNCH_ID"):
        registry.by_id("unknown-launch")


def _validate_identity_case(**event_overrides: str) -> None:
    event, actor = issue_event(**event_overrides)
    request = parse_issue_request(event)
    validate_authorization(
        event=event,
        actor=actor,
        repository=REPOSITORY,
        request=request,
        authorization=authorization(),
    )


def test_owner_identity_is_accepted() -> None:
    _validate_identity_case()


@pytest.mark.parametrize(
    ("field", "kwargs"),
    [
        ("actor", {"actor": "attacker"}),
        ("sender", {"sender": "attacker"}),
        ("issue author", {"issue_author": "attacker"}),
        ("repository owner", {"repository_owner": "attacker"}),
    ],
)
def test_non_owner_identity_rejected(field: str, kwargs: dict[str, str]) -> None:
    del field
    with pytest.raises(LaunchRejected, match="OWNER_MISMATCH"):
        _validate_identity_case(**kwargs)


def test_wrong_confirmation_rejected() -> None:
    event, actor = issue_event(body="authorization: RUN_SPEC018_PROBE_999")
    request = parse_issue_request(event)
    with pytest.raises(LaunchRejected, match="CONFIRMATION_MISMATCH"):
        validate_authorization(
            event=event,
            actor=actor,
            repository=REPOSITORY,
            request=request,
            authorization=authorization(),
        )


def test_repository_mismatch_rejected() -> None:
    event, actor = issue_event()
    request = parse_issue_request(event)
    with pytest.raises(LaunchRejected, match="REPOSITORY_MISMATCH"):
        validate_authorization(
            event=event,
            actor=actor,
            repository="other/repository",
            request=request,
            authorization=authorization(),
        )


# Source and CI evidence


def test_exact_branch_sha_is_accepted() -> None:
    validate_source_head(configured_client(), repository=REPOSITORY, authorization=authorization())


def test_moved_branch_rejected() -> None:
    client = configured_client()
    client.gets[f"/repos/{REPOSITORY}/git/ref/heads/{REF}"] = {
        "object": {"type": "commit", "sha": "b" * 40}
    }
    with pytest.raises(LaunchRejected, match="SOURCE_SHA_MISMATCH"):
        validate_source_head(client, repository=REPOSITORY, authorization=authorization())


def _ci_client(**run_overrides: Any) -> FakeClient:
    client = configured_client()
    run = dict(client.gets[f"/repos/{REPOSITORY}/actions/runs/{CI_RUN_ID}"])
    run.update(run_overrides)
    client.gets[f"/repos/{REPOSITORY}/actions/runs/{CI_RUN_ID}"] = run
    return client


def test_ci_wrong_sha_rejected() -> None:
    with pytest.raises(LaunchRejected, match="CI_SHA_MISMATCH"):
        validate_ci_runs(
            _ci_client(head_sha="b" * 40), repository=REPOSITORY, authorization=authorization()
        )


def test_ci_wrong_workflow_name_rejected() -> None:
    with pytest.raises(LaunchRejected, match="CI_WORKFLOW_MISMATCH"):
        validate_ci_runs(
            _ci_client(name="Different workflow"), repository=REPOSITORY, authorization=authorization()
        )


def test_ci_not_completed_rejected() -> None:
    with pytest.raises(LaunchRejected, match="CI_NOT_COMPLETED"):
        validate_ci_runs(
            _ci_client(status="in_progress", conclusion=None),
            repository=REPOSITORY,
            authorization=authorization(),
        )


def test_ci_failure_rejected() -> None:
    with pytest.raises(LaunchRejected, match="CI_NOT_GREEN"):
        validate_ci_runs(
            _ci_client(conclusion="failure"), repository=REPOSITORY, authorization=authorization()
        )


def test_ci_api_error_rejected_fail_closed() -> None:
    client = configured_client()
    client.gets[f"/repos/{REPOSITORY}/actions/runs/{CI_RUN_ID}"] = GitHubApiError(
        "missing", status=404
    )
    with pytest.raises(LaunchRejected, match="CI_EVIDENCE_UNAVAILABLE"):
        validate_ci_runs(client, repository=REPOSITORY, authorization=authorization())


# Duplicate launch checks


def test_no_prior_dispatch_is_accepted() -> None:
    validate_duplicate_state(configured_client(), repository=REPOSITORY, authorization=authorization())


@pytest.mark.parametrize("status", ["queued", "in_progress", "completed"])
def test_same_sha_prior_dispatch_rejected(status: str) -> None:
    client = configured_client(duplicate_runs=[{"head_sha": SOURCE_SHA, "status": status}])
    with pytest.raises(LaunchRejected, match="DUPLICATE_LAUNCH"):
        validate_duplicate_state(client, repository=REPOSITORY, authorization=authorization())


def test_unrelated_sha_prior_dispatch_is_ignored() -> None:
    client = configured_client(duplicate_runs=[{"head_sha": "b" * 40, "status": "completed"}])
    validate_duplicate_state(client, repository=REPOSITORY, authorization=authorization())


def test_malformed_duplicate_listing_rejected() -> None:
    client = configured_client()
    path = f"/repos/{REPOSITORY}/actions/workflows/{WORKFLOW_FILE}/runs?event=workflow_dispatch&per_page=100"
    client.gets[path] = {"workflow_runs": "not-a-list"}
    with pytest.raises(LaunchRejected, match="DUPLICATE_STATE_UNAVAILABLE"):
        validate_duplicate_state(client, repository=REPOSITORY, authorization=authorization())


def test_duplicate_lookup_api_error_rejected() -> None:
    client = configured_client()
    path = f"/repos/{REPOSITORY}/actions/workflows/{WORKFLOW_FILE}/runs?event=workflow_dispatch&per_page=100"
    client.gets[path] = GitHubApiError("boom", status=500)
    with pytest.raises(LaunchRejected, match="DUPLICATE_STATE_UNAVAILABLE"):
        validate_duplicate_state(client, repository=REPOSITORY, authorization=authorization())


# Dispatch construction and full orchestration


def test_dispatch_contains_only_registry_derived_fields() -> None:
    dispatch = build_dispatch_request(authorization())
    assert dispatch.workflow_file == WORKFLOW_FILE
    assert dispatch.ref == REF
    assert dispatch.inputs == {
        "launch_id": LAUNCH_ID,
        "expected_source_sha": SOURCE_SHA,
        "confirmation": CONFIRMATION,
    }


def test_successful_launcher_dispatches_exact_workflow_and_comments() -> None:
    event, actor = issue_event()
    registry = validate_registry_data(registry_data())
    client = configured_client()

    dispatch = run_launcher(
        event=event,
        registry=registry,
        client=client,
        repository=REPOSITORY,
        actor=actor,
        launcher_run_id="999",
    )

    assert dispatch.workflow_file == WORKFLOW_FILE
    assert client.posts[0] == (
        f"/repos/{REPOSITORY}/actions/workflows/{WORKFLOW_FILE}/dispatches",
        {
            "ref": REF,
            "inputs": {
                "launch_id": LAUNCH_ID,
                "expected_source_sha": SOURCE_SHA,
                "confirmation": CONFIRMATION,
            },
        },
        {204},
    )
    assert client.posts[1][0] == f"/repos/{REPOSITORY}/issues/42/comments"
    assert "ADS live launch accepted" in client.posts[1][1]["body"]


def test_untrusted_issue_fields_never_propagate_to_dispatch() -> None:
    event, actor = issue_event()
    event["issue"]["labels"] = [{"name": "workflow=evil.yml"}]
    event["issue"]["assignee"] = {"login": "attacker"}
    event["issue"]["milestone"] = {"title": "ref=main"}
    registry = validate_registry_data(registry_data())
    client = configured_client()

    dispatch = run_launcher(
        event=event,
        registry=registry,
        client=client,
        repository=REPOSITORY,
        actor=actor,
        launcher_run_id="1000",
    )

    serialized = json.dumps(
        {"workflow": dispatch.workflow_file, "ref": dispatch.ref, "inputs": dispatch.inputs},
        sort_keys=True,
    )
    assert "evil.yml" not in serialized
    assert "attacker" not in serialized


# Static workflow boundaries


def test_launcher_workflow_has_exact_bounded_permissions_and_no_provider_secret() -> None:
    text = Path(".github/workflows/v1-autonomous-live-experiment-launcher.yml").read_text(
        encoding="utf-8"
    )
    assert "permissions:\n  actions: write\n  contents: read\n  issues: write\n" in text
    assert "OPENAI_API_KEY" not in text
    assert "eval " not in text
    assert "github.event.issue.body" not in text
    assert "python scripts/ads_live_experiment_launcher.py" in text


def test_probe_workflow_is_provider_free_read_only_and_exactly_scoped() -> None:
    text = Path(".github/workflows/v1-live-launcher-probe.yml").read_text(encoding="utf-8")
    assert "workflow_dispatch:" in text
    assert "permissions:\n  contents: read\n" in text
    assert "OPENAI_API_KEY" not in text
    assert "actions: write" not in text
    assert "contents: write" not in text
    assert "spec018-probe-001" in text
    assert "RUN_SPEC018_PROBE_001" in text
    assert "OBSERVED_SOURCE_SHA" in text
