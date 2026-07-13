# Period-correct analysis constraints

## Core principle

Vintage calculator chips are often custom control/data-path systems rather than small modern general-purpose CPUs. Similar names do not guarantee similar mechanisms.

## Questions to answer before interpretation

1. What is the physical data path: bit-serial, digit-serial, word-parallel, or mixed?
2. What constitutes an addressable unit: bit, digit, word, instruction, field, or ROM page?
3. Which state is physically stored, and which state recirculates or is reconstructed each cycle?
4. Is control firmware, microcode, a PLA/state machine, hardwired logic, or a combination?
5. How are keyboard scanning, display scanning, timing, and arithmetic coupled?
6. Are apparent calls, branches, stacks, and registers documented structures or analyst conveniences?
7. Does a trace show instruction semantics, micro-operations, bus phases, or only external effects?
8. Which behavior belongs to the calculator system rather than one chip in isolation?

## Common misleading translations

| Modern-looking term | Required caution |
|---|---|
| RAM | May be serial registers, shift storage, or a few addressable words |
| Register | May be a recirculating digit field or analyst-defined slice |
| Program counter | May be a sequencer with page/bank behavior unlike a linear PC |
| Stack | May be a fixed-depth return mechanism or calculator operand stack |
| Function | May cross multiple ROM regions or depend on persistent machine state |
| Interrupt | May instead be phase-driven polling, key scanning, or hardwired sequencing |
| Floating point | May be BCD fields with device-specific normalization and guard digits |
| Cycle | May mean oscillator phase, digit time, word time, instruction time, or display frame |

## Writing rule

Prefer the hardware's own terminology. When introducing an analogy, use:

> ANALOGY: This resembles ___ only in ___. It differs in ___, which remains relevant because ___.

Never silently normalize historical architecture into a modern CPU narrative.
