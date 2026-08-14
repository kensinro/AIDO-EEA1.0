# AIDO-EEA Python Reference Implementation

**Version:** 0.2.0  
**Status:** Validation-locked reference implementation / pre-public-release candidate  
**Scope:** EEA 1.0 human-governed, LLM-independent entitlement kernel  
**Not included:** autonomous semantic adjudication, full validated M1–M8 automation, journal workflow, or scientific-writing automation.

## Overview

This repository provides a small, auditable Python reference implementation for the core governed objects of the **Evidence Entitlement Audit (EEA)** framework.

The implementation is intentionally conservative. It focuses on:

- canonical claim objects;
- claim-specific minimum and full evidence contracts;
- provenance and dependency objects;
- clause-level contract evaluation;
- five-state entitlement reporting:
  - `ENTITLED`
  - `QUALIFIED`
  - `ABSTAIN`
  - `NOT_ENTITLED`
  - `CONTRADICTED`
- decision traces;
- human disposition;
- deterministic JSON/CLI workflows;
- regression-testable release behavior.

The package does **not** claim that all scientific semantics can be resolved automatically. Human adjudication remains load-bearing.

## EEA 1.0 / EEA 2.0 boundary

EEA 1.0 is represented here as a human-governed, LLM-independent kernel.

A semantic adapter may, in a future EEA 2.0 implementation, propose:

- claim candidates;
- atomic decompositions;
- claim types;
- evidence candidates;
- source-role labels;
- ambiguity flags;
- multilingual normalization.

Such adapter outputs are **provisional** and may not change evidence contracts or issue final entitlement states without governed review.

## Installation

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

python -m pip install -U pip
pip install -e .
```

For testing:

```bash
pip install -e ".[dev]"
pytest -q
```

## Quick example

```bash
aido-eea audit examples/example_claim.json
```

or:

```bash
python -m aido_eea.cli audit examples/example_claim.json
```

## Canonical decision logic

The reference evaluator follows the bounded logic below:

1. If direct incompatible evidence is present → `CONTRADICTED`.
2. If the claim is structurally non-adjudicable because critical evidence is unavailable → `ABSTAIN`.
3. If the strongest audited formulation satisfies the full contract → `ENTITLED`.
4. If the minimum contract is satisfied but the full contract is incomplete → `QUALIFIED`.
5. Otherwise → `NOT_ENTITLED`.

These states are **not an ordinal quality score**.

## Repository structure

```text
src/aido_eea/
    models.py            governed data models
    contracts.py         contract evaluation
    decision.py          five-state adjudication
    provenance.py        provenance/dependency helpers
    validators.py        bounded deterministic validators
    io.py                JSON load/save
    cli.py               command-line interface
    semantic_adapter.py  EEA 2.0 interface only; no autonomous adjudication
tests/
examples/
schemas/
docs/
```

## Release philosophy

This repository is intended to support:

- transparent GitHub development;
- archived Zenodo releases;
- fixed version identifiers;
- reproducible examples;
- machine-readable ledgers;
- regression testing.

It should not be described as a validated general-purpose scientific audit instrument until external operating characteristics are established.

## Citation

See `CITATION.cff`.

## License

A public software license has intentionally **not** been selected in this draft package.  
Before public GitHub/Zenodo release, replace `LICENSE_PENDING.md` with the license chosen by the author and update `pyproject.toml`, `CITATION.cff`, and `.zenodo.json` accordingly.


## Validation-locked V0.2.0 evidence boundary

V0.2.0 incorporates the Human-Gate-locked bounded Validation MVP without making the EEA 1.0 kernel LLM-dependent.

- T3 natural held-out reproducibility: 70/90 pooled exact Gold agreement (77.8%).
- T6-R1 controlled five-state discrimination: 87/90 (96.7%), macro-F1 0.967, Fleiss' κ 0.917 after opaque reblinding.
- T8-R1 evidence sensitivity: 87/90 (96.7%), 90.0% complete transition paths, 27/27 supportive-state recovery, 0/30 false contradiction under masking.

The direct-incompatible-evidence result is 3/3 from one independent base scenario evaluated by three operators and must not be generalized broadly.

## Rfull / escalation boundary

`Rfull(c)` is the full contract for the current frozen claim formulation. Evidence required only for a hypothetical stronger claim `c+` must not be inserted into `Rfull(c)` and used to downgrade `c`; stronger wording requires a separate M6 escalation contract.

## Canonical state serialization

Public JSON output uses: `ENTITLED`, `QUALIFIED`, `ABSTAIN`, `NOT ENTITLED`, `CONTRADICTED`. The Python enum member remains `ClaimState.NOT_ENTITLED`; validation helpers accept legacy `NOT_ENTITLED` serialization.
