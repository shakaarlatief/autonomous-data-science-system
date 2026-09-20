# MC-0020 Resolution: W5 T1 V0.2 Blind Calibration Closed

**Thread:** MC-0020
**Date resolved:** 2026-09-20
**Status:** RESOLVED / T1 ACCEPTED
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Task owner:** ChatGPT / `chatgpt-27`
**Independent reviewer:** Claude Opus / fresh conversation
**Reviewer-fixture target:** `f4308cc74b6d44640f399b6e9c102473382232df`
**Source-corpus boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Authority:** Collaboration evidence only. Research 217 records the formal T1 design acceptance.

## Result

V0.2 materially improved blind multi-membership reproducibility while preserving the strong preferred-route signal:

```text
exact subject-set agreement   7/24 -> 16/24
mean Jaccard                  0.642 -> 0.852
micro membership F1          0.753 -> 0.867
preferred-route agreement     22/24 -> 22/24
```

Claude explicitly found the V0.2 include/exclude clauses, secondary-membership rule and `admissibility-authority` addition materially useful.

Remaining ambiguity is localized to broad cross-cutting carriers and bounded wording/scope issues rather than a failure of the controlled-subject architecture.

## Close

```text
MC0020=RESOLVED
T1=ACCEPTED
NEXT=FINAL_W5_INFORMATION_ARCHITECTURE_RECONCILIATION
```
