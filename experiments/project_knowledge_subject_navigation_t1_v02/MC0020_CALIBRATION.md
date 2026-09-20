# W5 T1 V0.2 MC-0020 Blind Placement Calibration

**Reviewer subset:** 24 artifacts
**Authority:** Non-authoritative research output.

## V0.2 agreement

```text
exact full subject sets          16 / 24 (66.7%)
preferred-route agreement        22 / 24 (91.7%)
mean subject-set Jaccard         0.852
median subject-set Jaccard       1.000
micro membership precision       0.818
micro membership recall          0.923
micro membership F1              0.867
ChatGPT memberships              39
Claude memberships               44
```

## Change from V0.1

```text
exact-set fraction               29.2% -> 66.7% (+37.5%)
mean Jaccard                     0.642 -> 0.852 (+0.210)
micro membership F1              0.753 -> 0.867 (+0.115)
preferred-route agreement        91.7% -> 91.7%
absolute membership count gap    13 -> 5
```

V0.2 materially improves multi-membership agreement while preserving the already-strong preferred-route signal. Remaining disagreement is concentrated in broad cross-cutting carriers and a small number of boundary cases rather than distributed across the vocabulary.
