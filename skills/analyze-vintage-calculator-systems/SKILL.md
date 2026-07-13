---
name: analyze-vintage-calculator-systems
description: "Analyze vintage calculator processors, ROMs, hardware, traces, instruction sets, and firmware using period-correct architectural constraints. Use for calculator reverse engineering, disassembly, emulator interpretation, ROM research, hardware/firmware claims, or comparisons that risk importing unsupported modern CPU concepts; enforce sensitive internal handling of ROM images."
---

# Analyze vintage calculator systems

Analyze each machine on its documented physical and historical terms. Never use a modern processor model as an unstated default.

## Establish the actual machine model

Before interpreting code or behavior, identify what evidence supports:

- word width, digit/bit seriality, and number representation;
- instruction encoding and sequencing;
- ROM organization, addressing, banking, and dispatch;
- registers, latches, flags, stacks, and working storage;
- timing phases, recirculation, and shared buses;
- display, keyboard, peripheral, and custom-chip coupling;
- microcode, firmware, state-machine, or hardwired-control boundaries.

If any item is unknown, label it `UNKNOWN`. Do not fill gaps with conventions from modern microprocessors.

## Block modern-CPU projection

Do not assume the presence or meaning of:

- byte-addressable flat memory;
- conventional RAM, stack, program counter, call/return, or interrupts;
- orthogonal registers or instruction sets;
- modern ALU flags, pipelines, caches, operating systems, or processes;
- source-level functions corresponding cleanly to ROM address ranges;
- fixed-cycle instruction timing independent of serial datapaths or display phases;
- modern numeric formats such as IEEE 754.

Use modern vocabulary only when primary documentation defines an equivalent or when clearly marked as an analogy. State where the analogy fails.

Read [references/period-correct-analysis.md](references/period-correct-analysis.md) before architecture or ROM interpretation. Follow the repository's `docs/fundamental-principles.md` and `docs/research-methodology.md`.

## Handle ROMs as sensitive internal documents

Treat every ROM image, dump, extracted byte/word stream, derived reconstruction capable of reproducing the image, and unverified firmware archive as sensitive by default.

1. Store raw ROM material only under `/home/tron/calc-archaeology-vault/private-rom/` with restrictive local permissions.
2. Never place raw ROMs in Git worktrees, issues, chat transcripts, public artifacts, temporary web uploads, or Honcho memory.
3. Put only non-reconstructive metadata in `calc-archaeology`: cryptographic hash, size, provenance summary, acquisition date, rights status, and internal vault locator.
4. Do not quote or publish substantial ROM sequences. Use minimal excerpts only after Pane explicitly approves the purpose and rights basis.
5. Perform derived work in `calc-archaeology-lab` using controlled copies; delete unnecessary temporary copies after recording reproducible metadata.
6. Treat publication rights as `UNKNOWN` until documented. Sensitivity is not removed merely because a ROM can be found online.
7. Require Pane's explicit approval before moving any ROM-derived reconstructive artifact into GitHub or another external system.

Read [references/rom-handling.md](references/rom-handling.md) before touching ROM data.

## Produce disciplined conclusions

For every material claim, report:

- claim label: OBSERVATION, INFERENCE, HYPOTHESIS, ASSUMPTION, UNKNOWN, or CONFLICT;
- confidence C1–C5;
- exact supporting evidence or experiment record;
- period-correct interpretation;
- modern analogy, only if useful and explicitly limited;
- falsification or validation path for non-observational claims.

AI-derived architectural interpretations begin at C1 or C2 until supported independently.
