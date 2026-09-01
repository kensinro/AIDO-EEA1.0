# Validation reporting correction — 2026-09-01

This append-only note corrects **reporting terminology only**. It does not modify any frozen validation prediction, Gold state, numerator, denominator, score, or Human-Gate scientific interpretation.

## T8-R1 direct-incompatible-evidence denominator

The canonical reporting form is:

> One directly incompatible base scenario was evaluated by three blinded model operators; all three returned `CONTRADICTED` (3/3 operator evaluations).

Therefore:

- `3/3` = one base scenario × three operators;
- it is **not** three independent contradiction scenarios;
- it is **not** a general contradiction-detection sensitivity estimate;
- provider/model separation is **not** personnel or institutional independence.

Historical locked JSON contains the field name `independent_base_scenarios: 1`. This is retained as immutable historical output. For interpretation, the field should be read only as **number of distinct base scenarios = 1**; the word `independent` carries no statistical, personnel, institutional, or scenario-replication claim.

## T8-R1 terminology

Preferred manuscript-facing terminology is **controlled evidence responsiveness**, not generic “evidence sensitivity” or “contradiction sensitivity.” The locked numerical results remain:

- pooled exact accuracy: 87/90 (96.7%);
- complete transition-path accuracy: 90.0%;
- supportive-evidence restoration: 27/27;
- false `CONTRADICTED` calls under masking: 0/30;
- directly incompatible evidence: `CONTRADICTED` in 3/3 operator evaluations from one base scenario.

## Governance

This correction is append-only and preserves the validation lock. Any future release should carry this reporting boundary forward rather than rewriting the historical locked artifacts.
