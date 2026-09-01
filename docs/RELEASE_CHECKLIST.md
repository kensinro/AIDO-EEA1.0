# GitHub / archival release checklist

## Public v0.2.0 status

The GitHub v0.2.0 release is public and the validation-locked scientific boundary is frozen. This checklist separates completed public-release actions from archival items that still require explicit confirmation.

### Confirmed in the current repository

- [x] `VERSION` is 0.2.0.
- [x] GitHub release tag `v0.2.0` exists.
- [x] Apache License 2.0 was explicitly authorized for the public reference implementation on 2026-09-01.
- [x] Canonical Apache-2.0 terms are present in `LICENSE`.
- [x] `README.md`, `pyproject.toml`, `CITATION.cff`, `MANIFEST.in`, and `.zenodo.json` carry aligned Apache-2.0 metadata.
- [x] `CITATION.cff` contains the public repository and release URLs.
- [x] Current `main`-branch `.zenodo.json` is configured for open access under Apache-2.0 for any future authorized deposition.
- [x] Existing test report records `17 passed` for the validation-locked package.
- [x] Validation results and nonclaims are recorded in README/release notes.
- [x] Post-release metadata/reporting corrections are documented append-only without moving the v0.2.0 tag.

### Human / archival confirmation still required

- [ ] Confirm ORCID if it is to be included in public citation metadata.
- [ ] Independently verify the archived Zenodo record and exact DOI against the manuscript before submission.
- [ ] If a DOI is verified, add the exact DOI/badge without changing the locked scientific results.
- [ ] If the post-release metadata/license corrections must be preserved as a separately archived software release, create a separately authorized metadata-hygiene successor release rather than silently moving the existing v0.2.0 tag.

## Scientific release boundary

Do not describe EEA 1.0 as a validated general-purpose scientific audit instrument, autonomous semantic adjudicator, or system with known universal operating characteristics unless new evidence is formally admitted. Preserve T3/T6-R1/T8-R1 denominators and the one-base-scenario × three-operator contradiction boundary exactly.
