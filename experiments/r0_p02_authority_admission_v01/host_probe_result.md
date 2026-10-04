# R0-P02 live-host transport result

**Status:** LIVE-HOST LEG EXECUTED / RAW RESULT PRESERVED
**Protocol:** R0-P02-V01
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Frozen coordination head:** `15428acfc9a8ca8ac0cfa3ce9c05e4110f922dec`
**Runtime surface:** Codexless Runtime Bridge GitHub connector
**Production credentials used:** no

## Temporary refs

Both temporary branches were created from the frozen coordination head:

```text
r0-p02-host-v01-base  15428acfc9a8ca8ac0cfa3ce9c05e4110f922dec
r0-p02-host-v01-work  15428acfc9a8ca8ac0cfa3ce9c05e4110f922dec
```

## Work-branch payload

Exactly one file was added on the work branch:

```text
experiments/r0_p02_authority_admission_v01/host_probe_payload.json
```

Work commit:

```text
44ade93f30cd6fc2eb0c8e08ec9028a22dacdfc6
```

Git blob SHA:

```text
3fbf6af8e6b116c787786c064d0ff3c2f3ba70c4
```

Exact UTF-8 payload SHA-256:

```text
b4f5561dd0e129658ad28ee9178e264118198a8eeef269300f1971a84fbc00f5
```

Detached synthetic proof verification before host transport:

```text
PROOF_VALID=True
profile=TEST_HMAC_SHA256_NOT_PRODUCTION
signer_id=OWNER-TEST-1
```

## Pull request and squash transformation

Pull request:

```text
#86
head r0-p02-host-v01-work
base r0-p02-host-v01-base
changed files 1
head SHA 44ade93f30cd6fc2eb0c8e08ec9028a22dacdfc6
base SHA 15428acfc9a8ca8ac0cfa3ce9c05e4110f922dec
```

The PR was squash-merged through Runtime Bridge.

Squash result commit:

```text
4bd7d3971f09683613c4374d14ed98fc69e2c462
```

The work commit identity and squash result commit identity are different.

## Post-squash payload verification

The merged payload on `r0-p02-host-v01-base` had:

```text
Git blob SHA
3fbf6af8e6b116c787786c064d0ff3c2f3ba70c4

UTF-8 payload SHA-256
b4f5561dd0e129658ad28ee9178e264118198a8eeef269300f1971a84fbc00f5

DETACHED_PROOF_VALID=True
PROFILE_OK=True
SIGNER_OK=True
```

Therefore the payload bytes and detached test proof survived the host commit transformation exactly.

## Coordination-branch preservation

After the squash merge, the coordination branch remained:

```text
v1-source-vault-bootstrap-resume
15428acfc9a8ca8ac0cfa3ce9c05e4110f922dec
```

The host leg did not modify the coordination branch.

## Cleanup

Both temporary refs were deleted using expected-head guards.

Post-cleanup branch searches returned zero matches for:

```text
r0-p02-host-v01-base
r0-p02-host-v01-work
```

The merged PR remains ordinary host history; it is not a semantic authority surface.

This artifact preserves observed host-leg evidence only. Full R0-P02 classification is owned by the subsequent research reconciliation.
