# Post-release metadata corrections — 2026-09-01

This append-only note documents **metadata, reporting, and licensing corrections made on the `main` branch after the frozen GitHub `v0.2.0` release**. The existing `v0.2.0` tag is intentionally preserved and has not been moved or rewritten.

## Why this note exists

The original v0.2.0 release snapshot contained several pre-public-release placeholders and one terminology issue that no longer matched the public repository or the bounded manuscript interpretation. Correcting those items on `main` improves public traceability without silently changing the frozen release bytes.

## Corrections on `main`

- README status changed from pre-public candidate wording to **public validation-locked reference release**.
- `CITATION.cff` now contains the actual public repository and v0.2.0 release URLs instead of a placeholder.
- On 2026-09-01, the Human Gate explicitly authorized **Apache License 2.0** for the public AIDO-EEA reference implementation.
- Canonical Apache-2.0 terms are now provided in `LICENSE`; the temporary `LICENSE_NOTICE.md` no-license notice is retired.
- `README.md`, `pyproject.toml`, `CITATION.cff`, `MANIFEST.in`, and `.zenodo.json` are aligned to Apache-2.0.
- The current `main`-branch `.zenodo.json` is configured for open access under Apache-2.0 for any future authorized deposition. It does not move or rewrite the existing v0.2.0 tag and does not assert an unverified DOI.
- `docs/RELEASE_CHECKLIST.md` now separates confirmed release/licensing actions from archival items still requiring confirmation.
- `RELEASE_MANIFEST_SHA256.json` remains identified as the **frozen v0.2.0 release snapshot manifest**, not a live-main manifest.
- T8 manuscript-facing terminology was normalized to **controlled evidence responsiveness**.
- The direct-incompatible-evidence result is explicitly bounded to **one base scenario × three operators (3/3 operator evaluations)**. Historical wording that used `independent_base_scenarios` is not interpreted as statistical, personnel, institutional, or scenario-replication independence; see `validation/REPORTING_CORRECTION_2026-09-01.md`.

## Scientific invariance

These corrections do **not** alter:

- source validation matrices;
- Gold states;
- predictions;
- T3/T6-R1/T8-R1 numerators or denominators;
- locked metrics;
- five-state decision logic;
- claim ceilings;
- Human-Gate scientific interpretation.

No new experiment or validation claim is created by these corrections.

## Version governance

If these metadata and licensing corrections need to be preserved as a separately archived software release, that should be done through a separately authorized successor version rather than by moving or rewriting the existing `v0.2.0` tag.
