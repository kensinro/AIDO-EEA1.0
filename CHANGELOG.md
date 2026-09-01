# Changelog

## 0.2.0 — 2026-08-14

Public validation-locked reference release.

### Added / locked

- Canonical five-state entitlement reporting: `ENTITLED`, `QUALIFIED`, `ABSTAIN`, `NOT ENTITLED`, `CONTRADICTED`.
- Explicit `Rmin` / `Rfull` contract logic and escalation boundary.
- Provenance, dependency, contradiction, abstention, and inference-ceiling governance.
- Deterministic validation scoring and regression-testable release behavior.
- Locked T3 / T6-R1 / T8-R1 validation artifacts and bounded reporting.
- Machine-readable schemas and example claim objects.

### Validation boundary

- T3: 70/90 pooled exact Gold agreement (77.8%).
- T6-R1: 87/90 (96.7%), macro-F1 0.967, Fleiss' κ=0.917.
- T8-R1: 87/90 (96.7%), 27/27 supportive-state recovery, 0/30 false `CONTRADICTED` calls under masking.
- Direct incompatible evidence was tested in one base scenario evaluated by three operators (3/3), not three independent scenarios.

### Nonclaims

This release does not establish universal operating characteristics, human inter-rater reliability, autonomous semantic adjudication, article-type invariance, or production readiness as a general-purpose scientific audit instrument.

### Metadata hygiene

Repository citation, release-status, and archival metadata have been reconciled with the public v0.2.0 release. Public access and software reuse rights remain distinct; see the repository license notice.
