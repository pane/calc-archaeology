# Fundamental Principles

This document defines the non-negotiable rules governing repository content.
All documentation, annotations, metadata, tools, and AI-assisted contributions
must comply with these principles.

## 1. Evidence Traceability

Every technical statement must be traceable to one of:

- primary evidence
- a documented experiment
- an explicitly labeled hypothesis

Unsupported assertions do not belong in the repository.

## 2. No Placeholder Citations

Evidence IDs, experiment IDs, citations, and cross-references must refer to real
records that exist in the repository or to clearly identified external sources.

Do not add placeholder evidence such as `EV-0001` unless the corresponding
record already exists.

## 3. Separation of Claim Types

Do not mix observations, interpretations, and hypotheses as if they had the same
status.

Use explicit labels when needed:

- OBSERVATION
- INFERENCE
- HYPOTHESIS
- ASSUMPTION
- UNKNOWN
- CONFLICT

## 4. Conservative Confidence

When uncertain, assign lower confidence. It is better to later promote a
hypothesis than to publish an unsupported conclusion as fact.

Confidence levels:

- C5: Confirmed by direct primary evidence or reproducible experiment
- C4: Strong support from multiple independent sources
- C3: Reasonable inference from available evidence
- C2: Weak or incomplete inference
- C1: Speculative working hypothesis

AI-generated analysis starts as C1 or C2 unless independently supported by
cataloged evidence.

## 5. Evidence Supremacy

Primary evidence takes precedence over interpretation.

If ROM bytes, hardware measurements, or reproducible traces contradict prior
notes, the prior interpretation must be revised or marked as conflicted.

## 6. Explicit Hypotheses

Hypotheses must include:

- rationale
- confidence level
- supporting evidence if any
- open questions or validation path

Hypotheses must never be presented as confirmed findings.

## 7. Stable Identifiers

Evidence IDs, experiment IDs, architecture IDs, ROM labels, and symbolic names
must be stable once published.

Do not reuse an identifier for a different meaning.

## 8. Source Boundaries

Raw private, copyrighted, or license-unclear source material must not be
committed unless its publication status is understood and explicitly approved.

Derived summaries may be committed when they preserve attribution and avoid
copying restricted source material.

## 9. Revision Integrity

Research conclusions may change. Changes must preserve traceability:

- record what changed
- identify the new evidence or reasoning
- avoid silent overwrites of disputed conclusions

## 10. Enforcement

If a reader cannot trace a technical claim back to evidence, experiment, or a
labeled hypothesis, the claim should be removed, rewritten, or marked as
unsupported.

## 11. Period-Correct Architecture

Vintage calculator systems must be interpreted from their documented physical
organization, timing, instruction sequencing, and historical terminology.
Modern concepts such as flat byte-addressable memory, conventional stacks,
interrupts, pipelines, caches, or IEEE floating point must not be assumed.
Modern terminology may be used only as an explicitly limited analogy or when
evidence establishes a real equivalent.

## 12. Sensitive ROM Handling

ROM images and reconstructive ROM-derived artifacts are sensitive internal
documents by default. Store raw ROM material only in the private vault, never
in Git, Honcho, public issues, or external services. Repository records may
contain non-reconstructive metadata and analysis. Publication or external
transfer of reconstructive ROM content requires documented rights review and
Pane's explicit approval.
