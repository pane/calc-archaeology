# Research Methodology

This document implements `docs/fundamental-principles.md`.

## Purpose

This repository documents research related to classic electronic calculators,
including firmware, ROM analysis, hardware behavior, emulator development,
execution traces, and algorithm reconstruction.

The repository combines:

- historical preservation
- reverse engineering
- experimental observation
- comparative analysis
- AI-assisted interpretation

The primary goal is to preserve evidence and document reasoning transparently.

## Core Principles

### 1. Evidence First

Primary artifacts always take precedence over interpretation.

Examples:

- ROM dumps
- oscilloscope captures
- emulator traces
- calculator photographs
- official documentation
- verified disassemblies

### 2. Separation of Evidence and Interpretation

Observed facts and inferred conclusions should be documented separately.
Interpretations may evolve as new evidence becomes available.

### 3. Preservation of Uncertainty

Uncertainty is documented explicitly. Research findings are assigned confidence
levels to distinguish directly observed behavior from inferred or speculative
claims.

## Evidence Hierarchy

Evidence is ranked conservatively. A lower-level source may still be useful,
but it must not be presented as stronger than it is.

- Level A: ROM bytes, raw dumps, or other direct digital artifacts
- Level B: reproducible emulator traces
- Level C: hardware measurements or physical observations
- Level D: manufacturer documentation
- Level E: patents
- Level F: published research or contemporary third-party material
- Level G: reasoned inference from documented evidence
- Level H: hypothesis or AI-assisted interpretation

## Confidence Levels

- C5: Confirmed by direct primary evidence or reproducible experiment
- C4: Strong support from multiple independent sources
- C3: Reasonable inference from available evidence
- C2: Weak or incomplete inference
- C1: Speculative working hypothesis

When uncertain, use the lower confidence level.

## Claim Labels

Use explicit labels where ambiguity is possible:

- OBSERVATION: directly observed source or behavior
- INFERENCE: reasoned interpretation from evidence
- HYPOTHESIS: plausible but unconfirmed explanation
- ASSUMPTION: temporary working premise
- UNKNOWN: unresolved behavior or missing information
- CONFLICT: evidence sources disagree

## AI-Assisted Analysis Policy

AI-generated material may contain:

- incorrect assumptions
- fabricated relationships
- incomplete reasoning
- invalid conclusions

Unless independently supported by cataloged evidence, AI-assisted analysis
should be treated as provisional. AI-generated claims should normally start as
C1 or C2.

Primary evidence always takes precedence over AI interpretation.

## Source Attribution

External materials should preserve:

- original author
- original URL
- retrieval date
- copyright status when known

Referenced materials remain property of their respective authors.

Do not invent or reserve evidence IDs before the corresponding evidence record
exists.

## Experimental Observations

Hardware observations should document:

- calculator model
- hardware revision if known
- measurement method
- instrumentation used
- replication status

Single-device observations are acceptable when labeled clearly.

## Experimental Workflow

1. Record the raw observation or source.
2. Assign or link a real evidence ID.
3. Classify the evidence level.
4. Separate observation from interpretation.
5. Assign conservative confidence.
6. Document reproduction status.
7. Link related architecture, ROM, or trace notes only after records exist.

## Repository Philosophy

This repository functions both as:

- a preservation archive
- an active research workspace

Not all content represents final conclusions. Transparency is preferred over
false certainty.
