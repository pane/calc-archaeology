# Holmes Workspace Policy

Holmes is isolated from the magazine project. It uses only the calculator
research workspaces and the dedicated Honcho workspace `calc-archaeology`.

## Workspace roles

| Workspace | Role | External status |
|---|---|---|
| `calc-archaeology` | Canonical reviewed research and Git history | GitHub-capable after Pane review |
| `calc-archaeology-vault` | Private source archive and sensitive ROM storage | Internal only |
| `calc-archaeology-lab` | Reproducible experiments and controlled derivatives | Internal until reviewed |
| Honcho `calc-archaeology` | Durable summaries, questions, terminology, decisions | Context only; never canonical |

## Movement rules

1. Preserve received source files in the vault with provenance.
2. Create an evidence record before treating a source as support for a claim.
3. Use the laboratory for extraction, traces, emulator runs, and temporary
   derivatives.
4. Move only reviewed, non-sensitive, non-reconstructive results into the
   canonical repository.
5. Require Pane's explicit approval before commits, pushes, GitHub mutations,
   publication, or external transfer of sensitive/reconstructive material.
6. Never move magazine context, editorial memory, or Redaktor artifacts into
   calculator workspaces.

## Authority

Files and Git are authoritative for evidence, experiments, conclusions, and
approval state. Honcho may remember concise context but cannot promote a claim,
reserve an identifier, or approve publication.
