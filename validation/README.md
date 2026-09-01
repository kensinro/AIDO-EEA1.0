# Locked Validation Evidence

This directory records the bounded EEA 1.0 Validation MVP locked on 2026-08-14.

T3 measures natural held-out cross-operator reproducibility. T6-R1 measures controlled five-state discrimination after opaque reblinding. T8-R1 measures **controlled evidence responsiveness** under masking, restoration/addition, and one directly incompatible evidence condition while claim wording is held fixed.

The LLM systems acted as blinded validation operators in fresh sessions. They are not part of the EEA 1.0 entitlement kernel, and model/provider separation must not be interpreted as personnel or institutional independence.

Permanent boundaries:
- T3 is not a natural five-state operating-characteristic estimate.
- T6-R1 controlled performance is not natural-domain accuracy.
- T8-R1 produced 27/27 expected supportive-state restorations and 0/30 false `CONTRADICTED` calls under masking.
- The direct-incompatible-evidence observation is `CONTRADICTED` in 3/3 operator evaluations from **one base scenario × three operators**. It is not three independent contradiction scenarios and is not a general contradiction-detection operating characteristic.
- Residual QUALIFIED↔NOT ENTITLED and smaller NOT ENTITLED↔ABSTAIN boundaries remain limitations.

Historical locked JSON may contain the field name `independent_base_scenarios`. That field records the count of distinct base scenarios (=1); it must not be interpreted as evidence of statistical, personnel, institutional, or scenario-level independence. See `REPORTING_CORRECTION_2026-09-01.md`.
