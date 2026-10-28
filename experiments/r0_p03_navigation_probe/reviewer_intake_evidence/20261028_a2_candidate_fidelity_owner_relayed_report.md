# Source-free file and representation fidelity test

**Provenance:** Owner-relayed text of the separate prospective reviewer session's response, transcribed from the current conversation and normalized into readable Markdown. This is **not** an original-byte export of the Temporary Chat response, nor independently audited tool-call telemetry. The source message remains authoritative for exact wording; cosmetic chat rendering artifacts (empty table wrappers and “Copy” labels) are omitted here.

**Required outcome:** verified

**Reported outcome:** `TEXT_AND_PNG_BYTES_AND_RENDER_VERIFIED`

All three supplied attachments were reported readable end-to-end as raw files in the candidate sandbox. Their byte counts and SHA-256 hashes were reportedly calculated directly from those bytes. The text fixture was decoded and its line endings inspected. The PNG was decoded, checked at pixel level, and visually rendered.

**Candidate's qualification:** These results verify the received attachment representations, not byte-for-byte identity with the sender's pre-upload files. No independent pre-upload digest was supplied or consulted by the candidate session.

## 1. Source-by-source receipt inventory

| Attachment | Reported receipt and inspection | Raw bytes | Pre-upload identity |
| --- | --- | ---: | --- |
| `S1_A2_CANDIDATE_FIDELITY_PROBE_V01.md` | Complete raw file read; text decoded | 5,392 | `NOT_VERIFIED` by candidate |
| `a2_source_free_fidelity_unicode_crlf.txt` | Complete raw file read; encoding and line endings inspected | 193 | `NOT_VERIFIED` by candidate |
| `a2_source_free_fidelity_pattern.png` | Complete raw file read; PNG decoded, checked and rendered | 291 | `NOT_VERIFIED` by candidate |

No missing, unreadable or truncated attachment was observed in the received raw files. The chat interface also displayed text and image representations, but those previews were reportedly not used for byte counts or hashes.

## 2. Reported raw-byte SHA-256

Candidate states Python `hashlib.sha256` was called on complete bytes obtained with `Path.read_bytes()`:

| Attachment | Bytes | SHA-256 reported by candidate |
| --- | ---: | --- |
| Brief | 5,392 | `c00df15f79b1b734a40efa34b5fe14aed536fdedafb4acba49a77114974e384c` |
| Text | 193 | `8af9f2f5ea35071e1e8db50e0f467188a63b0a2ad390e5a3eba3853b109603fb` |
| PNG | 291 | `fb598054eef1c3200b13967887f225d41acfd88059c6a335f9cb4655fa3cb05f` |

The candidate claimed all hashes were calculated rather than copied from a manifest or preview.

## 3. Text integrity

| Property | Brief | Text fixture |
| --- | --- | --- |
| Strict UTF-8 decoding | Success | Success |
| UTF-8 BOM | Absent | Absent |
| CRLF sequences | 0 | 5 |
| Standalone LF | 50 | 0 |
| Standalone CR | 0 | 0 |
| Ends in newline | Yes | No |
| Tab characters | 0 | 1 |
| Non-ASCII characters | None | Present |

The text fixture reportedly contained six logical lines including an intentionally blank line, preserved one tab and multilingual characters (accented Latin, Greek Δ, Chinese 雪 and Arabic), and preserved raw CRLF sequences.

Strict decoding was acknowledged as evidence of *received* valid UTF-8 rather than independent proof of the intended pre-upload encoding.

## 4. PNG representation fidelity

The candidate reported original PNG visual inspection from the attachment, **48 × 32** pixels, PNG format, RGB mode, four RGB colors, successful Pillow decoding/verification, and ancillary PNG text metadata.

Visual interpretation: geometric pattern, red region on left, blue on right, green central element and pale diagonal detail.

Independent pixel enumeration reported:

| RGB color | Pixel count |
| --- | ---: |
| Red `(219, 61, 47)` | 651 |
| Blue `(45, 96, 207)` | 641 |
| Green `(42, 178, 86)` | 212 |
| Pale `(248, 234, 202)` | 32 |
| **Total** | **1,536** |

Reported PNG chunks: `IHDR`, `tEXt`, `IDAT`, `IEND`, valid CRCs and no trailing bytes. `Comment` metadata: `S1 A2 source-free integrity probe`.

The candidate correctly distinguished the displayed image from evidence of raw bytes and did not claim to have verified upload transformation against a supplied original.

## 5. Tools and completeness reported by candidate

The session reported invoking Python `pathlib`, `hashlib`, standard-library byte and PNG chunk checks, Pillow image decoding and pixel sampling, and a container image-viewing tool for visual inspection. It reported no web requests, connected-app access, repository searches, other conversations, historical records or expected-value manifest access.

All requested received-file properties were reported observed. Missing pre-upload authoritative digest was the key acknowledged limitation, not an observed missing or unreadable candidate file.

## 6. Capability and scientific boundaries

The result **does not** demonstrate actual reviewer/challenger identity independence, owner-only report custody, OS or provider access denial, complete support for all historical modalities, or future task-author exclusion. No real-source adjudication, restricted output, source admission or role appointment was claimed.

**Final candidate outcome:** `TEXT_AND_PNG_BYTES_AND_RENDER_VERIFIED` at the scope of source-free text/PNG intake, hashing, decoding and rendering, **not independent certification of upload identity or real reviewer qualification**.

```text
A2_TEST=REAL_CANDIDATE_SESSION_SOURCE_FREE_FILE_AND_RENDER_FIDELITY
HISTORICAL_SOURCES_DELIVERED=ZERO
REAL_REVIEWER_ROLE=PENDING
REAL_CHALLENGER_ROLE=PENDING
RESTRICTED_REPORT_ROUTE=NOT_TESTED_IN_THIS_PROBE
AUTHOR_VIEW_DENIAL=NOT_TESTED_IN_THIS_PROBE
GOLD=NONE
SCORING=NOT_STARTED
```
