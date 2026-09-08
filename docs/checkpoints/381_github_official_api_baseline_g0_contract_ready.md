# Checkpoint 381: GitHub Official API Baseline, G0 Contract Ready

**Date:** 2026-09-08
**Status:** PASS / OFFICIAL GITHUB PLATFORM BASELINE FROZEN / G0 IMPLEMENTATION READY
**Checkpoint class:** RESEARCH EVIDENCE + IMPLEMENTATION-READINESS BOUNDARY
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Freeze the current official GitHub authentication/API baseline after Checkpoint 380 and open implementation of the G0 protected user-auth/token/REST-GraphQL kernel.
**Authority:** Validation 138 owns the platform-evidence result; `docs/research/GITHUB_API_AUTH_AND_CONTRACT_BASELINE.md` owns the detailed current source-backed contract.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Selected authentication design is confirmed

Current GitHub documentation supports the GitHub App user-access-token + device-flow architecture. User-directed actions are bounded by both app and user permissions/access, and installation-aware repository scope is directly enumerable with the user token.

Device-flow access/refresh token handling does not require a client secret. Current default expiring user-token lifecycle is eight hours plus a six-month refresh token.

## 2. First REST transport target is frozen

For github.com the initial REST transport will explicitly pin `2026-03-10`, use the standard GitHub JSON Accept header, send a fixed valid User-Agent, and attach the server-owned user access token as Bearer authorization.

Enterprise Server remains a separate future qualification because supported API-version sets differ.

## 3. First request gaps are closed

Official GitHub docs close the platform-level `create_tree` nested entry contract and the create-PR head/base requirements that the native host projection could not express structurally.

Same-path Contents write serialization is also independently confirmed by GitHub documentation.

## 4. Implementation can start without native-wrapper wire cloning

Checkpoint 380 already established that hidden native `any` output schemas do not block the independent G0 kernel. Checkpoint 381 now supplies the platform authority needed to implement that kernel professionally.

The next work is local-runtime G0 implementation and focused regression qualification. No live GitHub App credential or production GitHub mutation is required for the first candidate.

```text
CHECKPOINT381=GITHUB_OFFICIAL_API_BASELINE_FROZEN
G0_CONTRACT=READY
AUTH=GITHUB_APP_USER_ACCESS_TOKEN_DEVICE_FLOW
REST_GITHUB_COM_VERSION=2026-03-10
PROTECTED_TOKEN_STORE=LOCAL_DESIGN_NEXT
LIVE_GITHUB_CREDENTIALS=NOT_REQUIRED_FOR_FIRST_CANDIDATE
ACTION_PUBLICATION=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=IMPLEMENT_G0_AUTH_TOKEN_AND_TRANSPORT_KERNEL
```
