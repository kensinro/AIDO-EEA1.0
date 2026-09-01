# AIDO-EEA Python Reference V0.2.0

**Release date:** 2026-08-14  
**Status:** Public validation-locked reference release

V0.2.0 is an append-only successor to V0.1.0 and corresponds to the Human-Gate-locked bounded Validation MVP.

## Included validation evidence

- T3 natural held-out reproducibility: 70/90 pooled exact Gold agreement (77.8%).
- T6-R1 controlled five-state discrimination: 87/90 (96.7%), macro-F1 0.967, Fleiss' κ=0.917.
- T8-R1 controlled evidence responsiveness: 87/90 (96.7%), 90.0% complete transition paths, 27/27 supportive-state recovery, and 0/30 false `CONTRADICTED` calls under masking.
- Direct-incompatible evidence: `CONTRADICTED` in 3/3 operator evaluations from **one base scenario**; this is not a general contradiction-detection operating characteristic.

## Scope boundary

EEA remains human-governed and LLM-independent at the entitlement-kernel level. The LLM systems used in the Validation MVP served only as blinded operators of frozen decision rules. Autonomous semantic adjudication, universal operating characteristics, human inter-rater reliability, and article-type invariance are not established by this release.

## Public-artifact boundary

The repository is publicly accessible for inspection and reproducibility review. Public access does not by itself grant unrestricted reuse rights; consult the repository license notice for the current permissions status.
