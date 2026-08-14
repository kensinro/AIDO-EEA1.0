# Architecture

## EEA 1.0

The package implements governed data objects and deterministic adjudication over explicit contract states.

It does not autonomously extract scientific meaning from manuscripts.

### M1–M8 mapping

| Module | Framework role | Reference implementation status |
|---|---|---|
| M1 | claim decomposition | data structure / external human or adapter input |
| M2 | claim typing | data structure / external human or adapter input |
| M3 | evidence-contract definition | implemented as explicit contract objects |
| M4 | provenance & traceability | provenance object helpers |
| M5 | statistical/model contract | bounded deterministic validators + clause states |
| M6 | dependency & escalation | dependency fields; final semantic determination remains human-governed |
| M7 | contradiction & abstention | implemented as explicit governed triggers |
| M8 | entitlement & reporting | deterministic five-state adjudicator |

The implementation intentionally distinguishes **framework semantics** from **automation coverage**.


## Validation-locked decision boundaries

- Current-claim Rfull is distinct from hypothetical escalation evidence.
- QUALIFIED requires Rmin satisfied and current-claim Rfull incomplete.
- Missing decisive evidence is not contradiction.
- CONTRADICTED requires direct incompatible evidence.
- ABSTAIN requires explicit non-adjudicability.
- NOT ENTITLED records failure of the current minimum evidence/inference contract without direct incompatibility.

`validation.py` provides deterministic scoring only; it does not perform semantic extraction or scientific truth assessment.
