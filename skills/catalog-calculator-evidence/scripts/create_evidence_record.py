#!/usr/bin/env python3
"""Create a real evidence record and register its stable ID."""

from __future__ import annotations

import argparse
import fcntl
import os
import re
import tempfile
from datetime import date
from pathlib import Path

ID_RE = re.compile(r"EV-(\d{4,})")


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def next_id(register: str, records_dir: Path) -> str:
    used = {int(match) for match in ID_RE.findall(register)}
    for path in records_dir.glob("EV-*.md"):
        match = ID_RE.search(path.name)
        if match:
            used.add(int(match.group(1)))
    number = max(used, default=0) + 1
    return f"EV-{number:04d}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--rights", required=True)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()

    repo = args.repo.resolve()
    register_path = repo / "evidence" / "evidence-register.md"
    records_dir = repo / "evidence" / "records"
    lock_path = repo / "evidence" / ".evidence.lock"
    if not register_path.is_file() or not (repo / "docs" / "fundamental-principles.md").is_file():
        parser.error("--repo must point to the calc-archaeology repository root")

    records_dir.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+", encoding="utf-8") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        register = register_path.read_text(encoding="utf-8")
        evidence_id = next_id(register, records_dir)
        record_path = records_dir / f"{evidence_id}.md"
        record = f"""# Evidence Record: {evidence_id}

## Title

{args.title}

## Evidence Type

{args.type}

## Source

- origin: {args.source}
- author: UNKNOWN
- date: UNKNOWN
- retrieval date: {date.today().isoformat()}
- URL or local path: {args.source}
- license or publication status: {args.rights}

## Raw Observation

UNKNOWN — inspect and describe only what the source directly shows.

## Interpretation

None recorded.

## Confidence

C1 pending inspection.

## Related Records

None.

## Open Questions

- What claims can this source directly support?

## Notes

Record created; human/agent cataloging review required.
"""
        atomic_write(record_path, record)
        row = f"| {evidence_id} | {args.title} | {args.type} | {args.source} | intake | Rights: {args.rights} |\n"
        if not register.endswith("\n"):
            register += "\n"
        atomic_write(register_path, register + row)
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)

    print(f"{evidence_id}\t{record_path.relative_to(repo)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
