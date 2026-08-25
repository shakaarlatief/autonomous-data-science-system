# Source Intake Snapshot 001: VU Amsterdam Machine Learning Chat Batch

**Date:** 2026-08-25  
**Status:** Pre-substrate diagnostic intake snapshot; not an accepted Source Registry export  
**Scope:** Exact-byte fingerprints of the first course-sized source batch supplied during Design Session 06  
**Authority:** Historical/intake evidence only. The original source bytes remain outside Git. These records do not establish methodological authority, final course membership, redistribution rights, or accepted ADS source identities.  
**Design session:** 06  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 06 - Methodological Knowledge Universe Construction

## 1. User-supplied context

The user identified this batch as material from the Machine Learning course taught at Vrije Universiteit Amsterdam and supplied the public course page:

```text
https://mlvu.github.io/
```

The user explicitly noted uncertainty about whether the files named `Lecture9-*` belonged to the course; those files were simply present in the user's Machine Learning folder.

This snapshot intentionally preserves that uncertainty rather than resolving it by assumption.

---

## 2. Purpose

This snapshot exists because the source-substrate discussion began after these files had already been uploaded into ChatGPT.

Before a governed ADS Source Registry / SourceArtifactStore exists, the project can still preserve a non-authoritative diagnostic record of the exact bytes that were observed in this intake session.

This gives the future first-corpus ingestion test a comparison target without making ChatGPT Library the canonical source store.

---

## 3. Exact-byte fingerprints observed in the current intake batch

SHA-256 was computed over the exact uploaded file bytes available during this development session.

| Observed filename | Bytes | SHA-256 |
|---|---:|---|
| `00.Preliminaries.annotated.pdf` | 40,775,434 | `101b8fa2f38dbfbf014cdb420843e2606f9b8dfdbe8646a1eb44fe08df81dc00` |
| `11.Introduction.annotated(1).pdf` | 58,443,253 | `c428482f40cd6f70e76a7bdb7e3322d6371d41ce47e1298c50ae1081fcf05062` |
| `12.LinearModels1.annotated(1).pdf` | 11,611,714 | `5ea103271a06bfb4a7cd60994026641438007e23ef7d82eeb8ac83ac6ba414d5` |
| `21.Methodology1.annotated(1).pdf` | 32,162,504 | `f193bd0ded530129ce12f7b524785262733e3901e81280cfb57ceab9e49736ea` |
| `22.Methodology2.annotated(1).pdf` | 12,797,065 | `c095b78dcdb5d006112f0e16ee22a89883a0df92dbc09e018c015164b2d82c58` |
| `31.ProbabilisticModels1.annotated(1).pdf` | 6,954,298 | `c16a8f5aa92db5af2d82d44f90cb14fcc1c5a46d1deb5575d6472b7c6e2c6da0` |
| `32.LinearModels2.annotated(1).pdf` | 8,715,014 | `9b4bb8efa6f1adfc27f1cacbfc7b77e1c4335d1629962235f64121ad2768f3e9` |
| `41.DeepLearning1.annotated(1).pdf` | 30,148,932 | `477db561cd7e9befe6fc0f9ce27caba9c49e037de4ab55d097f30f61d502b1a1` |
| `51.Deep Learning2.annotated(1).pdf` | 78,874,939 | `3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110` |
| `52.Trees.annotated(1).pdf` | 4,435,890 | `6a489b8bb451183fa9f204718d02495fc63d6d1edcf3767df93fc4f01ce50ad1` |
| `61.SequentialModels.annotated(1).pdf` | 11,142,975 | `e5223a47a8c043a30822fbee8d27659d3f3035387fab3f5b31bfb05bc23b002a` |
| `62.Matrices.annotated(1).pdf` | 19,822,400 | `413762ed6ad9f4d028f979e3e9eb2ca8d2a217a82e280f64a348ac3a71fb7762` |
| `71.Reinforcement Learning.annotated(1).pdf` | 34,862,777 | `29bdf5ef38322197a7bb71874c5972885f4b45a784f6199d9374de0e92588356` |
| `72.Review.annotated(1).pdf` | 17,080,579 | `09ab5728dc2fb3bc828840ac542317b41edf4927307019c6bd3ffdc93bc2e11b` |
| `Transformers.annotated(1).pdf` | 40,254,527 | `9d7f5e60d5af2f059da8ab1edc0ea8488dc51499bfa680961d2c1a2cfe3c1ebf` |
| `book-v1.2.0-cropped.pdf` | 33,385,812 | `597d9bbf3115e565af9e61263d83f8778098259d274a0933c28eeedfb5a38342` |
| `Lecture9-GANs.pdf` | 539,761 | `331961622a2f6588c48a34ecddc6a3d052ffe8fcfba333f233d5f27b2da5565d` |
| `Lecture9-Medical-Example2.pdf` | 762,628 | `fcad76b95b2a7732de7a211070134ddce03c635850603bd3798c14347185508d` |
| `Lecture9-Medical-Problem.pdf` | 627,927 | `14d1380126bda2beef12dee2c8e76293300f04d9c5e2c9a77ba7949be63d6c46` |
| `unraveling-pca.pdf` | 46,684,862 | `d7fb21184810126a92835d3ab42bbedaf3e51cf0fb5a4ba912c25e9e9a6eafb4` |

Observed batch count:

```text
20 files
```

---

## 4. Immediate duplicate evidence

Fourteen of the current `(1)`-suffixed lecture uploads could be compared with same-named earlier uploads already present in the development environment.

Every compared pair was byte-identical despite the changed filename:

```text
11.Introduction
12.LinearModels1
21.Methodology1
22.Methodology2
31.ProbabilisticModels1
32.LinearModels2
41.DeepLearning1
51.Deep Learning2
52.Trees
61.SequentialModels
62.Matrices
71.Reinforcement Learning
72.Review
Transformers
```

For every pair:

```text
SHA-256(previous upload) == SHA-256(current (1) upload)
```

This is direct real-corpus evidence for Foundation 021's rule:

```text
filename != artifact identity
```

and for exact content-addressed duplicate detection.

No conclusion is drawn here about whether other files are semantic duplicates or alternate versions.

---

## 5. Important variant example

The files:

```text
book-v1.2.0-cropped.pdf
unraveling-pca.pdf
```

both appear to represent Peter Bloem's *Unraveling Principal Component Analysis* material, but their exact-byte hashes differ.

Therefore the future source subsystem must not infer:

```text
same apparent work/title -> same SourceArtifact
```

They are distinct exact artifacts until the Source Registry records a reviewed logical relationship such as alternate format/version/variant.

---

## 6. Association uncertainty preserved

The following files must not be silently classified as confirmed members of the VU Machine Learning course solely because they were found in the user's Machine Learning folder:

```text
Lecture9-GANs.pdf
Lecture9-Medical-Example2.pdf
Lecture9-Medical-Problem.pdf
```

The user's explicit statement is that Lecture 9 membership is uncertain.

Likewise, book/paper material may later be classified as required reading, supplementary material, separately relevant material, or merely colocated source material after source review.

---

## 7. Non-authority boundary

This file is not:

```text
a Source Registry export
a source-vault backup
a claim that ChatGPT retains the canonical bytes
a redistribution authorization
a final course syllabus
a methodological authority decision
a knowledge-ingestion result
```

It is a durable bridge between the pre-substrate chat intake and the future governed first-corpus ingestion.

---

## 8. Future acceptance use

When Specification 023 is implemented, the VU Machine Learning first-corpus exercise should compare the locally ingested original files against this diagnostic snapshot where the corresponding files are available.

Expected outcomes may include:

```text
MATCH
    local original bytes equal the chat-observed artifact

DIFFERENT_ARTIFACT
    local original differs and should be preserved separately

MISSING_LOCAL_SOURCE
    chat-observed artifact is not available in the chosen local intake folder

ADDITIONAL_LOCAL_SOURCE
    local course folder contains material not included in this first chat batch
```

None of these outcomes should be silently normalized away.
