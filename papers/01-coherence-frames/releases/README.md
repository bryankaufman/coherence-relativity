# Paper 1 Release Architecture
This directory is the release layer for `papers/01-coherence-frames/`.

## What happened to the prior management architecture
The original management split Paper 1 into three layers:
- working manuscript files at the paper root (`main.tex`, `main.pdf`, review notes, checklists)
- release snapshots in `releases/`
- submission materials in `submission/`

That structure was introduced when the paper was reorganized into `releases/`, `submission/`, and `session-logs/`, but later revisions continued landing directly in the working manuscript and root-level management documents. The result was:
- the working manuscript became newer than the release snapshots
- review and submission documents retained older version assumptions
- `releases/` preserved flat PDF snapshots (`main_v2.pdf`, `main_v3.pdf`) without a per-version manifest
- Zenodo references drifted between concept DOI and version-specific DOI usage

## Current policy
Starting with v4, each Paper 1 release gets its own directory under `releases/`.

The release directory is the source of truth for:
- release PDF artifact
- source bundle used for archival upload
- DOI policy and Zenodo notes
- release checklist and provenance

## Legacy snapshots
- `main_v2.pdf`
- `main_v3.pdf`

These legacy files are retained as flat historical snapshots from the pre-directory release scheme.

## Current release
- `v4/RELEASE_MANIFEST.md`
