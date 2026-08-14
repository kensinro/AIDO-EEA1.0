# GitHub / Zenodo release checklist

Before public release:

- [ ] Select and insert software license.
- [ ] Update `pyproject.toml` license metadata.
- [ ] Update `CITATION.cff`.
- [ ] Update `.zenodo.json`.
- [ ] Confirm author name and ORCID.
- [ ] Confirm repository URL.
- [ ] Create GitHub release tag matching `VERSION`.
- [ ] Run `pytest -q`.
- [ ] Run example CLI.
- [ ] Record SHA256 for the release archive.
- [ ] Upload release archive to Zenodo.
- [ ] Add Zenodo DOI badge after DOI assignment.
- [ ] Do not claim full-system validation unless supported by locked external evidence.
