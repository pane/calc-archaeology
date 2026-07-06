# ROM Annotation Conventions

This document defines rules for ROM disassembly and annotation work.
It implements `docs/fundamental-principles.md`.

## Purpose

ROM annotations are research records, not free-form commentary. They must make
the status of each claim visible.

## Routine Header Template

```asm
;------------------------------------------------------------------------------
; Routine:
; Address:
; Proposed name:
;
; Purpose:
;
; Claim type:
; Evidence:
; Confidence:
; References:
; Open questions:
;------------------------------------------------------------------------------
```

## Instruction Comment Template

```asm
; OBSERVATION
; <Directly observed behavior or decoded operation.>
;
; Evidence:
; <Existing evidence ID or source reference>
;
; Confidence:
; C5
```

## Inference Template

```asm
; INFERENCE
; <Reasoned interpretation.>
;
; Evidence:
; <Existing evidence ID, experiment ID, or source reference>
;
; Confidence:
; C2-C4
```

## Hypothesis Template

```asm
; HYPOTHESIS
; <Plausible but unconfirmed explanation.>
;
; Rationale:
; <Why this hypothesis is being considered.>
;
; Evidence:
; <Existing evidence ID if available, otherwise "none yet">
;
; Confidence:
; C1-C3
;
; Validation:
; <Experiment, trace, or source needed to test it.>
```

## Naming

Symbol names should be descriptive but conservative.

Use prefixes when confidence is low:

- `known_` only for established behavior
- `likely_` for C3 inferences
- `hyp_` for C1-C2 hypotheses
- `unk_` for unknown routines, fields, or addresses

Do not rename a published symbol casually. If a symbol changes meaning, record
the reason in the related map or annotation note.

## Cross-References

ROM comments may reference:

- evidence IDs
- experiment IDs
- architecture IDs
- trace files
- source records

References must point to real records. Placeholder references are forbidden.

## Commentary

Avoid narrative comments that hide uncertainty. Prefer short labeled blocks.
When a comment is speculative, label it as HYPOTHESIS or ASSUMPTION.
