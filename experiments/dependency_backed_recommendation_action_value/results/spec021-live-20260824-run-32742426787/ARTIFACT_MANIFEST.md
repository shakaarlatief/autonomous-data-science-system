# Specification 021 Replacement Live Artifact Manifest

**Purpose:** durable contained-file verification metadata generated after the raw GitHub Actions artifact was preserved. This manifest was not part of the original artifact and does not alter any preserved experiment file.

```text
Specification             021
launch issue              60
launcher run              32742406506
target workflow run       32742426787
target workflow job       97479810225
source head               575a3264ea39a10e35d769f9c54a2d1a13c28c08
source ref                v1-spec021-dependency-backed-recommendation-value-replacement-live-source
artifact ID               9525947445
artifact name             v1-dependency-backed-recommendation-action-575a3264ea39a10e35d769f9c54a2d1a13c28c08-1
artifact SHA-256          05724335763fdbeb7eecb456f9662a95dd8d25579d82d360d29d306755648fa8
raw preservation commit   5930a3c52f9580febb56f8e80d3d6eaf8d2cac66
```

## Exact contained files

| File | Bytes | SHA-256 |
|---|---:|---|
| `RESULT.md` | 240 | `d923078488b1e1ea194ea05aed8f419efcd4753a9cc5043c0b739013e7126bb4` |
| `dependency_backed_recommendation_action.sqlite3` | 307200 | `042b359b2702fd7a38a43310190eb580f2b6fe86131cd3f825a8b6439f7d3b53` |
| `judge_attempts.jsonl` | 24962 | `99894051f2985b8c084c8ea830c7d0eb074a97b5e1c0fe964bbf490fb151d073` |
| `judge_plan.json` | 2846 | `b7b90735c202d74f848bf30543a092b041f98efb7a7cf9fe2467986dcd664751` |
| `reasoner_attempts.jsonl` | 141350 | `976799abd6cf1fa1e612c8b399ff55bd739e93d92b35ac7cb4a4913499208d87` |
| `reasoning_plan.json` | 5126 | `b56a260c88363f572f49a42c8bb06122f449d33e5edf1840258f87f73e6d6a42` |
| `result.json` | 6355 | `3645a180de005edc859e8e76fcaf910b33f00ec4d13f617df160f1050316347a` |
| `system_provenance_plan.json` | 23837 | `53c23156d238a36b5bcd665a1b21ff4116f5da058907f0a4a5bb93df41aa829f` |

The outer ZIP digest is GitHub's artifact digest. The contained-file hashes above were computed from the downloaded artifact bytes after the preservation boundary and provide durable verification even if GitHub later repackages the outer archive.
