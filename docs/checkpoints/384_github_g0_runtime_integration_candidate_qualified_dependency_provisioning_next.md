# Checkpoint 384: GitHub G0 Runtime Integration Candidate Qualified, Dependency Provisioning Next

**Date:** 2026-09-08
**Status:** PASS / G0 MAIN-RUNTIME SOURCE INTEGRATION QUALIFIED / LIVE RELEASE BLOCKED ON DEPENDENCY PACKAGING
**Checkpoint class:** PRIVATE IMPLEMENTATION + DEPLOYMENT-BOUNDARY QUALIFICATION
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve the first main-runtime G0 source integration candidate and localize the only newly discovered live-release blocker to native dependency provisioning.
**Authority:** Validation 141 owns the integration result; private local-runtime commit `6ce0da8818a455731acc10ba231ef9f52c0c8206` owns the candidate bytes.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. G0 is composed into a runtime candidate

The private candidate now wires the qualified GitHub G0 kernel into public-preview runtime construction without changing the MCP server factory or public tool allowlist.

The kernel remains dormant unless GitHub App configuration is present and internal services are actually requested. Ordinary startup imports no keyring package, reads no credential and makes no GitHub request.

## 2. Candidate result

```text
private head            6ce0da8818a455731acc10ba231ef9f52c0c8206
source syntax           9 / 9 PASS
integration regression  4 / 4 PASS
secret scanner          0 matches
private integrity       RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
```

No public `github.*` action exists yet.

## 3. Live publication is deliberately blocked

The existing Runtime Release v1 contract can replace/add only files under `src`, `test`, `scripts`, and `config`. It cannot provision root package manifests or `node_modules` and does not own an npm dependency transaction.

The Windows-qualified keyring package was temporary staging and has been removed. Publishing G0 source without solving dependency provisioning would therefore create a latent configured-runtime failure.

## 4. Next boundary

The next work is a bounded package-provisioning extension to the Runtime Release architecture, not a live GitHub login and not public action registration. The extension must preserve deterministic package identity, integrity, rollback and no arbitrary caller-selected installation authority.

```text
CHECKPOINT384=G0_RUNTIME_INTEGRATION_CANDIDATE_QUALIFIED
G0_SOURCE_INTEGRATION=READY
G0_DEPENDENCY_PROVISIONING=BLOCKED
PUBLIC_GITHUB_SURFACE=0_ACTIONS
LIVE_GITHUB_AUTH=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=BOUNDED_RUNTIME_DEPENDENCY_PROVISIONING_DESIGN
```
