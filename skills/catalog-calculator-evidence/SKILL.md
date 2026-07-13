---
name: catalog-calculator-evidence
description: "Catalog calculator manuals, patents, photographs, hardware observations, ROM metadata, traces, chat-derived notes, and research documents into real evidence records with stable IDs, provenance, rights status, claim boundaries, and conservative confidence. Use during source intake, before citing material, when adding evidence to calc-archaeology, or when reconciling duplicates and conflicting sources."
---

# Catalog calculator evidence

Create traceable evidence without turning interpretation into observation.

## Inspect before registering

1. Locate the original source in the vault or approved external location.
2. Determine source type, origin, author, date, retrieval date, locator, and rights/publication status.
3. Check the evidence register and hashes/metadata for duplicates.
4. Decide whether the source may be represented publicly, only summarized, or must remain internal.
5. For ROM material, first load `analyze-vintage-calculator-systems` and follow its sensitive-ROM rules.

Read [references/cataloging-policy.md](references/cataloging-policy.md) for classification and duplicate handling.

## Create a real record

Use `scripts/create_evidence_record.py` from the repository root. It creates the record before registering its stable ID, preventing placeholder reservations.

```bash
python3 skills/catalog-calculator-evidence/scripts/create_evidence_record.py \
  --title "TI-59 service manual, scan" \
  --type "manufacturer documentation" \
  --source "internal vault locator or approved URL" \
  --rights "UNKNOWN — internal research copy"
```

Then edit the new record:

- write only what the source directly shows under Raw Observation;
- place interpretation in its own labeled section;
- start AI-assisted interpretation at C1 or C2;
- link only records that already exist;
- add open questions and conflicts;
- do not copy substantial copyrighted text or ROM data.

## Verify

Confirm:

- the ID exists both in `evidence/evidence-register.md` and as a record file;
- source and rights fields are not blank;
- internal sensitive locators reveal no unnecessary personal/system details;
- every technical claim is traceable to the source or clearly labeled;
- no ROM bytes or reconstructive derivatives entered Git;
- `git diff` contains only intended metadata/analysis.

Do not commit, push, create GitHub issues, or publish without Pane's approval.
