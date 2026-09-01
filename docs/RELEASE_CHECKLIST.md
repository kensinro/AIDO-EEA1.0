# GitHub / archival release checklist

## Public v0.2.0 status

The GitHub v0.2.0 release is public and the validation-locked scientific boundary is frozen. This checklist now separates completed public-release actions from metadata items that still require explicit confirmation.

### Confirmed in the current repository

- [x] `VERSION` is 0.2.0.
- [x] GitHub release tag `v0.2.0` exists.
- [x] `CITATION.cff` contains the public repository and release URLs.
- [x] `.zenodo.json` is aligned with the public validation-locked release description.
- [x] Existing test report records `17 passed` for the validation-locked package.
- [x] Validation results and nonclaims are recorded in README/release notes.
- [x] Public-release wording distinguishes repository availability from reuse rights.

### Human / archival confirmation still required

- [ ] Select a reusable software license if broader reuse rights are intended; otherwise retain the explicit no-general-license notice.
- [ ] Add license metadata to `pyproject.toml`, `CITATION.cff`, and archival metadata only after the license decision is authorized.
- [ ] Confirm ORCID if it is to be included in public citation metadata.
- [ ] Independently verify the archived Zenodo record and exact DOI against the manuscript before submission.
- [ ] If a DOI is verified, add the exact DOI/badge without changing the locked scientific results.
- [ ] If post-release metadata corrections must be preserved as a versioned archive, create a separately authorized metadata-hygiene successor release rather than silently moving the existing v0.2.0 tag.

## Scientific release boundary

Do not describe EEA 1.0 as a validated general-purpose scientific audit instrument, autonomous semantic adjudicator, or system with known universal operating characteristics unless new evidence is formally admitted. Preserve T3/T6-R1/T8-R1 denominators and the one-base-scenario × three-operator contradiction boundary exactly.
