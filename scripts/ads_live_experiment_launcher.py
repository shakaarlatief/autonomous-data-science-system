"""Governed GitHub Actions launcher for explicitly authorized ADS live experiments.

This module implements the control-plane contract frozen in Specification 018.  Its
purpose is deliberately narrower than a general workflow runner.  A GitHub issue may
select an existing repository-owned launch authorization by ``launch_id`` and prove
knowledge of that authorization's confirmation token, but the issue cannot define the
workflow file, Git ref, source commit, CI evidence, model configuration, prompt, secret,
or any other executable input.

The security model is based on three separations:

1. Human/agent transport is separated from authorization.  Creating the issue is only
   the transport event.  The repository registry remains the authority for what may be
   launched.
2. Launch authorization is separated from provider credentials.  This script requires
   only a repository ``GITHUB_TOKEN`` with Actions/Issues permissions and must never be
   given a provider API key.
3. Launcher validation is separated from target-workflow validation.  The launcher
   verifies the frozen source head and exact CI evidence before dispatch, while the
   target workflow must independently verify ``github.sha`` and the frozen confirmation
   before any provider call.

The pure validation functions are intentionally independent from HTTP transport so that
all fail-closed behavior can be exercised provider-free in unit tests.
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


REGISTRY_SCHEMA_VERSION = 1
LAUNCH_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{2,79}$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
CONFIRMATION_RE = re.compile(r"^[A-Z0-9_]{8,120}$")
WORKFLOW_FILE_RE = re.compile(r"^[A-Za-z0-9._-]+\.ya?ml$")
REF_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{0,199}$")
OWNER_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")

_ALLOWED_AUTH_KEYS = {
    "launch_id",
    "enabled",
    "owner_login",
    "workflow_file",
    "ref",
    "expected_source_sha",
    "confirmation",
    "required_ci_runs",
}
_ALLOWED_CI_KEYS = {"run_id", "workflow_name"}


class LaunchRejected(RuntimeError):
    """A bounded, user-auditable rejection that must prevent workflow dispatch."""

    def __init__(self, code: str, detail: str) -> None:
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


class GitHubApiError(RuntimeError):
    """Transport-level GitHub API failure with the HTTP status retained when known."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status


@dataclass(frozen=True)
class RequiredCiRun:
    """Exact Actions run that must be green for the frozen source head."""

    run_id: int
    workflow_name: str


@dataclass(frozen=True)
class LaunchAuthorization:
    """Repository-owned immutable launch configuration for one bounded authorization."""

    launch_id: str
    enabled: bool
    owner_login: str
    workflow_file: str
    ref: str
    expected_source_sha: str
    confirmation: str
    required_ci_runs: tuple[RequiredCiRun, ...]


@dataclass(frozen=True)
class LaunchRegistry:
    """Validated registry whose launch IDs are unique and safe to resolve by key."""

    authorizations: tuple[LaunchAuthorization, ...]

    def by_id(self, launch_id: str) -> LaunchAuthorization:
        for authorization in self.authorizations:
            if authorization.launch_id == launch_id:
                return authorization
        raise LaunchRejected("UNKNOWN_LAUNCH_ID", "launch identifier is not registered")


@dataclass(frozen=True)
class IssueRequest:
    """The only two semantic values the issue transport is allowed to provide."""

    issue_number: int
    launch_id: str
    confirmation: str


@dataclass(frozen=True)
class DispatchRequest:
    """Exact registry-derived workflow-dispatch request."""

    workflow_file: str
    ref: str
    inputs: Mapping[str, str]


class GitHubApiClient:
    """Minimal JSON GitHub REST client used by the issue-event launcher workflow.

    The client deliberately exposes only GET and POST JSON operations needed by the
    launcher.  It does not execute shell commands and it never logs the bearer token.
    """

    def __init__(self, *, token: str, api_url: str = "https://api.github.com") -> None:
        if not token:
            raise LaunchRejected("MISSING_GITHUB_TOKEN", "launcher token is unavailable")
        self._token = token
        self._api_url = api_url.rstrip("/")

    def get_json(self, path: str) -> Mapping[str, Any]:
        return self._request_json("GET", path, None, expected_statuses={200})

    def get_json_optional(self, path: str) -> Mapping[str, Any] | None:
        try:
            return self.get_json(path)
        except GitHubApiError as exc:
            if exc.status == 404:
                return None
            raise

    def post_json(
        self,
        path: str,
        payload: Mapping[str, Any],
        *,
        expected_statuses: set[int],
    ) -> Mapping[str, Any]:
        return self._request_json("POST", path, payload, expected_statuses=expected_statuses)

    def _request_json(
        self,
        method: str,
        path: str,
        payload: Mapping[str, Any] | None,
        *,
        expected_statuses: set[int],
    ) -> Mapping[str, Any]:
        body = None if payload is None else json.dumps(payload).encode("utf-8")
        request = Request(
            f"{self._api_url}{path}",
            data=body,
            method=method,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self._token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "Content-Type": "application/json",
            },
        )
        try:
            with urlopen(request, timeout=30) as response:  # noqa: S310 - fixed GitHub API base
                status = int(response.status)
                raw = response.read()
        except HTTPError as exc:
            raise GitHubApiError(
                f"GitHub API returned HTTP {exc.code} for {method} {path}",
                status=int(exc.code),
            ) from exc
        except URLError as exc:
            raise GitHubApiError(f"GitHub API transport error for {method} {path}") from exc

        if status not in expected_statuses:
            raise GitHubApiError(
                f"GitHub API returned unexpected HTTP {status} for {method} {path}",
                status=status,
            )
        if not raw:
            return {}
        parsed = json.loads(raw.decode("utf-8"))
        if not isinstance(parsed, Mapping):
            raise GitHubApiError(f"GitHub API returned non-object JSON for {method} {path}")
        return parsed


def load_registry(path: str | Path) -> LaunchRegistry:
    """Load and fully validate the repository-controlled authorization registry."""

    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise LaunchRejected("INVALID_REGISTRY", "registry cannot be read as JSON") from exc
    return validate_registry_data(data)


def validate_registry_data(data: Any) -> LaunchRegistry:
    """Validate registry structure and reject every ambiguous executable field.

    Strict key sets are intentional.  A typo or newly introduced field should not be
    silently ignored because ignored configuration can create a false impression that a
    safety property is active when the launcher does not enforce it.
    """

    if not isinstance(data, Mapping):
        raise LaunchRejected("INVALID_REGISTRY", "registry root must be an object")
    if set(data) != {"schema_version", "authorizations"}:
        raise LaunchRejected("INVALID_REGISTRY", "registry root contains unexpected keys")
    if data.get("schema_version") != REGISTRY_SCHEMA_VERSION:
        raise LaunchRejected("INVALID_REGISTRY", "unsupported registry schema version")

    raw_authorizations = data.get("authorizations")
    if not isinstance(raw_authorizations, list):
        raise LaunchRejected("INVALID_REGISTRY", "authorizations must be a list")

    authorizations: list[LaunchAuthorization] = []
    seen_launch_ids: set[str] = set()
    for raw in raw_authorizations:
        if not isinstance(raw, Mapping) or set(raw) != _ALLOWED_AUTH_KEYS:
            raise LaunchRejected("INVALID_REGISTRY", "authorization contains invalid keys")

        launch_id = raw.get("launch_id")
        enabled = raw.get("enabled")
        owner_login = raw.get("owner_login")
        workflow_file = raw.get("workflow_file")
        ref = raw.get("ref")
        expected_source_sha = raw.get("expected_source_sha")
        confirmation = raw.get("confirmation")
        required_ci_runs = raw.get("required_ci_runs")

        if not isinstance(launch_id, str) or not LAUNCH_ID_RE.fullmatch(launch_id):
            raise LaunchRejected("INVALID_REGISTRY", "invalid launch_id")
        if launch_id in seen_launch_ids:
            raise LaunchRejected("INVALID_REGISTRY", "duplicate launch_id")
        seen_launch_ids.add(launch_id)
        if not isinstance(enabled, bool):
            raise LaunchRejected("INVALID_REGISTRY", "enabled must be boolean")
        if not isinstance(owner_login, str) or not OWNER_RE.fullmatch(owner_login):
            raise LaunchRejected("INVALID_REGISTRY", "invalid owner_login")
        if not isinstance(workflow_file, str) or not WORKFLOW_FILE_RE.fullmatch(workflow_file):
            raise LaunchRejected("INVALID_REGISTRY", "workflow_file must be a safe basename")
        if "/" in workflow_file or "\\" in workflow_file:
            raise LaunchRejected("INVALID_REGISTRY", "workflow_file path separators are forbidden")
        if not isinstance(ref, str) or not REF_RE.fullmatch(ref) or ".." in ref:
            raise LaunchRejected("INVALID_REGISTRY", "invalid Git ref")
        if not isinstance(expected_source_sha, str) or not SHA_RE.fullmatch(expected_source_sha):
            raise LaunchRejected("INVALID_REGISTRY", "expected_source_sha must be lowercase 40-hex")
        if not isinstance(confirmation, str) or not CONFIRMATION_RE.fullmatch(confirmation):
            raise LaunchRejected("INVALID_REGISTRY", "invalid confirmation token")
        if not isinstance(required_ci_runs, list):
            raise LaunchRejected("INVALID_REGISTRY", "required_ci_runs must be a list")
        if enabled and not required_ci_runs:
            raise LaunchRejected("INVALID_REGISTRY", "enabled authorization requires CI evidence")

        ci_requirements: list[RequiredCiRun] = []
        seen_run_ids: set[int] = set()
        for raw_ci in required_ci_runs:
            if not isinstance(raw_ci, Mapping) or set(raw_ci) != _ALLOWED_CI_KEYS:
                raise LaunchRejected("INVALID_REGISTRY", "CI requirement contains invalid keys")
            run_id = raw_ci.get("run_id")
            workflow_name = raw_ci.get("workflow_name")
            if isinstance(run_id, bool) or not isinstance(run_id, int) or run_id <= 0:
                raise LaunchRejected("INVALID_REGISTRY", "CI run_id must be a positive integer")
            if run_id in seen_run_ids:
                raise LaunchRejected("INVALID_REGISTRY", "duplicate CI run_id")
            seen_run_ids.add(run_id)
            if not isinstance(workflow_name, str) or not workflow_name.strip():
                raise LaunchRejected("INVALID_REGISTRY", "CI workflow_name must be non-empty")
            ci_requirements.append(RequiredCiRun(run_id=run_id, workflow_name=workflow_name))

        authorizations.append(
            LaunchAuthorization(
                launch_id=launch_id,
                enabled=enabled,
                owner_login=owner_login,
                workflow_file=workflow_file,
                ref=ref,
                expected_source_sha=expected_source_sha,
                confirmation=confirmation,
                required_ci_runs=tuple(ci_requirements),
            )
        )

    return LaunchRegistry(authorizations=tuple(authorizations))


def parse_issue_request(event: Mapping[str, Any]) -> IssueRequest:
    """Parse only the exact title/body grammar allowed to select a registry entry."""

    if event.get("action") != "opened":
        raise LaunchRejected("INVALID_EVENT", "only newly opened issues may request launch")
    issue = event.get("issue")
    if not isinstance(issue, Mapping):
        raise LaunchRejected("INVALID_EVENT", "issue payload is missing")

    issue_number = issue.get("number")
    title = issue.get("title")
    body = issue.get("body")
    if isinstance(issue_number, bool) or not isinstance(issue_number, int) or issue_number <= 0:
        raise LaunchRejected("INVALID_EVENT", "issue number is invalid")
    if not isinstance(title, str) or not title.startswith("[ADS LIVE] "):
        raise LaunchRejected("INVALID_REQUEST", "title does not match ADS LIVE grammar")

    launch_id = title.removeprefix("[ADS LIVE] ")
    if not LAUNCH_ID_RE.fullmatch(launch_id):
        raise LaunchRejected("INVALID_REQUEST", "launch identifier is malformed")
    if not isinstance(body, str):
        raise LaunchRejected("INVALID_REQUEST", "issue body is missing")

    stripped = body.strip(" \t\r\n")
    prefix = "authorization: "
    if not stripped.startswith(prefix):
        raise LaunchRejected("INVALID_REQUEST", "authorization line is missing")
    confirmation = stripped.removeprefix(prefix)
    if "\n" in confirmation or "\r" in confirmation or not CONFIRMATION_RE.fullmatch(confirmation):
        raise LaunchRejected("INVALID_REQUEST", "issue body contains unsupported content")
    if stripped != f"authorization: {confirmation}":
        raise LaunchRejected("INVALID_REQUEST", "issue body contains unsupported content")

    return IssueRequest(issue_number=issue_number, launch_id=launch_id, confirmation=confirmation)


def validate_authorization(
    *,
    event: Mapping[str, Any],
    actor: str,
    repository: str,
    request: IssueRequest,
    authorization: LaunchAuthorization,
) -> None:
    """Validate owner identity, repository identity, enablement, and confirmation."""

    if not authorization.enabled:
        raise LaunchRejected("AUTHORIZATION_DISABLED", "launch authorization is disabled")
    if request.confirmation != authorization.confirmation:
        raise LaunchRejected("CONFIRMATION_MISMATCH", "confirmation token does not match registry")

    repository_payload = event.get("repository")
    sender = event.get("sender")
    issue = event.get("issue")
    if not isinstance(repository_payload, Mapping) or not isinstance(sender, Mapping) or not isinstance(issue, Mapping):
        raise LaunchRejected("INVALID_EVENT", "identity payload is incomplete")
    issue_user = issue.get("user")
    repo_owner = repository_payload.get("owner")
    if not isinstance(issue_user, Mapping) or not isinstance(repo_owner, Mapping):
        raise LaunchRejected("INVALID_EVENT", "owner identity payload is incomplete")

    observed_repository = repository_payload.get("full_name")
    identities = {
        "github.actor": actor,
        "sender": sender.get("login"),
        "issue_author": issue_user.get("login"),
        "repository_owner": repo_owner.get("login"),
    }
    if observed_repository != repository:
        raise LaunchRejected("REPOSITORY_MISMATCH", "event repository does not match runtime repository")
    for label, value in identities.items():
        if value != authorization.owner_login:
            raise LaunchRejected("OWNER_MISMATCH", f"{label} is not the authorized owner")


def resolve_source_sha(
    client: Any,
    *,
    repository: str,
    ref: str,
) -> str:
    """Resolve a branch or lightweight/annotated tag to exactly one commit SHA."""

    encoded_ref = quote(ref, safe="")
    head = client.get_json_optional(f"/repos/{repository}/git/ref/heads/{encoded_ref}")
    tag = client.get_json_optional(f"/repos/{repository}/git/ref/tags/{encoded_ref}")
    if head is not None and tag is not None:
        raise LaunchRejected("AMBIGUOUS_REF", "ref resolves as both branch and tag")
    resolved = head if head is not None else tag
    if resolved is None:
        raise LaunchRejected("SOURCE_REF_MISSING", "authorized ref cannot be resolved")

    obj = resolved.get("object")
    if not isinstance(obj, Mapping):
        raise LaunchRejected("SOURCE_REF_INVALID", "resolved ref has no object")
    object_type = obj.get("type")
    object_sha = obj.get("sha")
    if not isinstance(object_sha, str) or not SHA_RE.fullmatch(object_sha):
        raise LaunchRejected("SOURCE_REF_INVALID", "resolved ref SHA is invalid")
    if object_type == "commit":
        return object_sha
    if object_type != "tag":
        raise LaunchRejected("SOURCE_REF_INVALID", "resolved ref does not target a commit")

    # Dereference annotated tags with a bounded depth.  Deep or cyclic tag chains are
    # rejected rather than interpreted recursively without limit.
    seen: set[str] = set()
    current_sha = object_sha
    for _ in range(5):
        if current_sha in seen:
            raise LaunchRejected("SOURCE_REF_INVALID", "annotated tag cycle detected")
        seen.add(current_sha)
        tag_object = client.get_json(f"/repos/{repository}/git/tags/{current_sha}")
        target = tag_object.get("object")
        if not isinstance(target, Mapping):
            raise LaunchRejected("SOURCE_REF_INVALID", "annotated tag target is invalid")
        target_type = target.get("type")
        target_sha = target.get("sha")
        if not isinstance(target_sha, str) or not SHA_RE.fullmatch(target_sha):
            raise LaunchRejected("SOURCE_REF_INVALID", "annotated tag target SHA is invalid")
        if target_type == "commit":
            return target_sha
        if target_type != "tag":
            raise LaunchRejected("SOURCE_REF_INVALID", "annotated tag does not target a commit")
        current_sha = target_sha
    raise LaunchRejected("SOURCE_REF_INVALID", "annotated tag chain exceeds bounded depth")


def validate_source_head(client: Any, *, repository: str, authorization: LaunchAuthorization) -> None:
    """Require the live ref to resolve to the exact frozen source commit."""

    observed_sha = resolve_source_sha(client, repository=repository, ref=authorization.ref)
    if observed_sha != authorization.expected_source_sha:
        raise LaunchRejected("SOURCE_SHA_MISMATCH", "authorized ref moved from frozen source SHA")


def validate_ci_runs(client: Any, *, repository: str, authorization: LaunchAuthorization) -> None:
    """Verify every exact preregistered CI run against the frozen source commit."""

    for requirement in authorization.required_ci_runs:
        try:
            run = client.get_json(f"/repos/{repository}/actions/runs/{requirement.run_id}")
        except Exception as exc:
            if isinstance(exc, LaunchRejected):
                raise
            raise LaunchRejected("CI_EVIDENCE_UNAVAILABLE", "required CI run cannot be verified") from exc

        observed_repo = run.get("repository")
        observed_repo_name = observed_repo.get("full_name") if isinstance(observed_repo, Mapping) else None
        if observed_repo_name != repository:
            raise LaunchRejected("CI_REPOSITORY_MISMATCH", "required CI run belongs to another repository")
        if run.get("name") != requirement.workflow_name:
            raise LaunchRejected("CI_WORKFLOW_MISMATCH", "required CI workflow name does not match")
        if run.get("head_sha") != authorization.expected_source_sha:
            raise LaunchRejected("CI_SHA_MISMATCH", "required CI run is not for frozen source SHA")
        if run.get("status") != "completed":
            raise LaunchRejected("CI_NOT_COMPLETED", "required CI run is not completed")
        if run.get("conclusion") != "success":
            raise LaunchRejected("CI_NOT_GREEN", "required CI run did not conclude success")


def validate_duplicate_state(client: Any, *, repository: str, authorization: LaunchAuthorization) -> None:
    """Reject any prior workflow-dispatch run for the same workflow and source SHA."""

    workflow = quote(authorization.workflow_file, safe="")
    try:
        response = client.get_json(
            f"/repos/{repository}/actions/workflows/{workflow}/runs?event=workflow_dispatch&per_page=100"
        )
    except Exception as exc:
        if isinstance(exc, LaunchRejected):
            raise
        raise LaunchRejected("DUPLICATE_STATE_UNAVAILABLE", "prior launch state cannot be verified") from exc

    runs = response.get("workflow_runs")
    if not isinstance(runs, list):
        raise LaunchRejected("DUPLICATE_STATE_UNAVAILABLE", "workflow run listing is malformed")
    for run in runs:
        if not isinstance(run, Mapping):
            raise LaunchRejected("DUPLICATE_STATE_UNAVAILABLE", "workflow run listing is malformed")
        if run.get("head_sha") == authorization.expected_source_sha:
            raise LaunchRejected("DUPLICATE_LAUNCH", "target workflow already ran for frozen source SHA")


def build_dispatch_request(authorization: LaunchAuthorization) -> DispatchRequest:
    """Construct the only workflow-dispatch payload permitted by Specification 018."""

    return DispatchRequest(
        workflow_file=authorization.workflow_file,
        ref=authorization.ref,
        inputs={
            "launch_id": authorization.launch_id,
            "expected_source_sha": authorization.expected_source_sha,
            "confirmation": authorization.confirmation,
        },
    )


def dispatch_authorization(
    client: Any,
    *,
    repository: str,
    dispatch: DispatchRequest,
) -> None:
    """POST the validated workflow-dispatch request using registry-derived values only."""

    workflow = quote(dispatch.workflow_file, safe="")
    client.post_json(
        f"/repos/{repository}/actions/workflows/{workflow}/dispatches",
        {"ref": dispatch.ref, "inputs": dict(dispatch.inputs)},
        expected_statuses={204},
    )


def comment_issue(client: Any, *, repository: str, issue_number: int, body: str) -> None:
    """Write a bounded audit comment to the triggering issue."""

    client.post_json(
        f"/repos/{repository}/issues/{issue_number}/comments",
        {"body": body},
        expected_statuses={201},
    )


def _safe_issue_number(event: Mapping[str, Any]) -> int | None:
    issue = event.get("issue")
    if not isinstance(issue, Mapping):
        return None
    value = issue.get("number")
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        return None
    return value


def run_launcher(
    *,
    event: Mapping[str, Any],
    registry: LaunchRegistry,
    client: Any,
    repository: str,
    actor: str,
    launcher_run_id: str,
) -> DispatchRequest:
    """Validate one issue event and dispatch exactly one authorized workflow."""

    request = parse_issue_request(event)
    authorization = registry.by_id(request.launch_id)
    validate_authorization(
        event=event,
        actor=actor,
        repository=repository,
        request=request,
        authorization=authorization,
    )
    validate_source_head(client, repository=repository, authorization=authorization)
    validate_ci_runs(client, repository=repository, authorization=authorization)
    validate_duplicate_state(client, repository=repository, authorization=authorization)
    dispatch = build_dispatch_request(authorization)
    dispatch_authorization(client, repository=repository, dispatch=dispatch)
    comment_issue(
        client,
        repository=repository,
        issue_number=request.issue_number,
        body=(
            "ADS live launch accepted. "
            f"launch_id=`{authorization.launch_id}`; "
            f"source=`{authorization.expected_source_sha}`; "
            f"launcher_run=`{launcher_run_id}`."
        ),
    )
    return dispatch


def main() -> int:
    """GitHub Actions entry point using only trusted environment/runtime paths."""

    event_path = os.environ.get("GITHUB_EVENT_PATH", "")
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    actor = os.environ.get("GITHUB_ACTOR", "")
    token = os.environ.get("GITHUB_TOKEN", "")
    launcher_run_id = os.environ.get("GITHUB_RUN_ID", "unknown")
    api_url = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    registry_path = os.environ.get("ADS_LIVE_REGISTRY", ".github/ads_live_experiments.json")

    if not event_path or not repository or not actor:
        print("Launcher rejected: INVALID_RUNTIME_CONTEXT", file=sys.stderr)
        return 2

    try:
        event_data = json.loads(Path(event_path).read_text(encoding="utf-8"))
        if not isinstance(event_data, Mapping):
            raise LaunchRejected("INVALID_EVENT", "event payload must be an object")
        registry = load_registry(registry_path)
        client = GitHubApiClient(token=token, api_url=api_url)
        dispatch = run_launcher(
            event=event_data,
            registry=registry,
            client=client,
            repository=repository,
            actor=actor,
            launcher_run_id=launcher_run_id,
        )
    except (json.JSONDecodeError, OSError) as exc:
        print("Launcher rejected: INVALID_EVENT", file=sys.stderr)
        return 2
    except LaunchRejected as exc:
        print(f"Launcher rejected: {exc.code}", file=sys.stderr)
        issue_number = None
        try:
            if "event_data" in locals() and isinstance(event_data, Mapping):
                issue_number = _safe_issue_number(event_data)
            if issue_number is not None and "client" in locals():
                comment_issue(
                    client,
                    repository=repository,
                    issue_number=issue_number,
                    body=f"ADS live launch rejected: `{exc.code}`.",
                )
        except Exception:
            print("Launcher rejection comment could not be written", file=sys.stderr)
        return 2
    except GitHubApiError:
        print("Launcher rejected: GITHUB_API_ERROR", file=sys.stderr)
        return 2

    print(
        "Launcher dispatched "
        f"workflow={dispatch.workflow_file} ref={dispatch.ref} source={dispatch.inputs['expected_source_sha']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
