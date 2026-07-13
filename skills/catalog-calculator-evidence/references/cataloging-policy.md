# Evidence cataloging policy

## Evidence versus source

An evidence record documents what one source directly supports. A large document may justify multiple later claims, but do not multiply IDs merely for convenience. Create a new ID for a distinct artifact, version, hardware observation, trace, or materially different source.

## Duplicate handling

- Same hash and provenance: use the existing record and add the alternate locator privately if useful.
- Same content, different scan: relate the scans and document quality/provenance differences.
- Different revision: create separate records.
- Conflicting sources: preserve both and mark `CONFLICT`; do not silently choose.
- Composite archive: catalog the archive and its important components only when individual provenance can be preserved.

## Public metadata

Safe candidates include title, type, author, date, retrieval date, rights status, hash, size, and non-sensitive provenance summary. Do not expose private source identities, credentials, absolute sensitive paths, ROM content, or copyrighted bulk text.

## Confidence

Confidence describes support for a stated claim, not prestige of a document. A manufacturer manual may be primary evidence of what the manufacturer documented while still being incomplete or wrong about observed hardware behavior.
