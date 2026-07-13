# Sensitive ROM handling

## Classification

Classify raw and reconstructive ROM material as `SENSITIVE-ROM` by default. Rights status is a separate field and defaults to `UNKNOWN`.

## Storage zones

| Zone | ROM policy |
|---|---|
| `calc-archaeology-vault/private-rom/` | Raw internal storage; restrictive permissions |
| `calc-archaeology-lab/` | Temporary controlled analysis and experiments |
| `calc-archaeology/` | Metadata, non-reconstructive analysis, approved minimal excerpts |
| Honcho | Summaries and locators only; never ROM bytes |
| GitHub/external services | No raw or reconstructive ROM content without explicit approval |

## Metadata record

For an internally stored ROM, record without exposing content:

- internal identifier;
- calculator/model and hardware revision if known;
- byte or word length;
- SHA-256 hash;
- acquisition source and date;
- dump method if known;
- rights/publication status;
- internal vault-relative locator;
- related evidence record;
- known conflicts or duplicate hashes.

Do not place credentials, personal source identities, or an absolute sensitive path in public metadata when that would expose a person or system.

## Derived artifacts

Treat the following as reconstructive unless shown otherwise:

- complete disassembly or word listing;
- lossless encoded or transformed dump;
- exhaustive opcode/address table containing original words;
- patch/delta paired with an obtainable base image;
- emulator resource embedding the complete ROM;
- OCR/transcription of a full printed ROM listing.

Architecture notes, control-flow summaries, hashes, statistics, symbolic maps without original words, and small approved excerpts may be non-reconstructive, but still require evidence and rights review.
