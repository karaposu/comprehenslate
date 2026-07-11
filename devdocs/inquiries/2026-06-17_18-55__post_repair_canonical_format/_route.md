# Concept Index — post-repair canonical format

> Persistent identity-set + invocation log. Routelisting writes this file itself on every run.
> Within-concept only (no inter-concept dependency edges; no process/control-flow state).

## Identity Set

| ID | Identity | First-seen | Last-touched | Own-depth pointer | Depth-signal |
|---|---|---|---|---|---|
| R1 | HTML5 schema / validation profile (MUST 1) | 2026-06-17 | 2026-06-17 | — (not drilled) | breadth-only |
| R2 | Per-policy class-attribute conventions (MUST 2) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R3 | Per-element provenance encoding pattern (MUST 3) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R4 | HTML5 → EPUB 3 packaging pipeline (COULD 1) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R5 | HTML5-to-markdown round-trip-stable subset (COULD 2) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R6 | Risale-i Nur sample prototype (COULD 3) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R7 | Parser-determinism axis caveat (P2 + P3 refinement) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R8 | Polyglot wording precision (P4 refinement) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R9 | Dual-persistent clarification (P7 refinement) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R10 | TEI architectural-lever wording (P7 refinement) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R11 | JSON-AST bias-balance acknowledgment (P7 refinement) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R12 | TEI as future archival output format | 2026-06-17 | 2026-06-17 | — | frontier; revival-trigger-gated |
| R13 | Pandoc version pinning policy | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R14 | HTML5 Living Standard version stability snapshot | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R15 | Cross-corpus format-architecture validation | 2026-06-17 | 2026-06-17 | — | frontier; scaling-gated |
| R16 | Archival / historical preservation as 5th temporal layer | 2026-06-17 | 2026-06-17 | — | frontier; project-maturity-gated |
| R17 | In-memory representation choice (HTML5 DOM vs Pandoc AST) | 2026-06-17 | 2026-06-17 | — | uncertain-individuation flagged |
| R18 | Per-translation-output format expansion (PDF / reveal.js / LaTeX) | 2026-06-17 | 2026-06-17 | — | frontier; expansion-gated |
| R19 | Intake pipeline producing HTML5 canonical | 2026-06-17 | 2026-06-17 | — | broad-scope; subsumes engineering work |
| R20 | The 7 detector designs operating on HTML5 DOM | 2026-06-17 | 2026-06-17 | — | 7 sister inquiries implied |
| R21 | EPUB CSS template for Arabic typography | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R22 | Mac app PipelineConfig.swift html-output integration | 2026-06-17 | 2026-06-17 | — | breadth-only |

## Individuation history

- Fresh entry point; 22 identities individuated in one breadth run.
- R23 (OCR-to-HTML5 reconstruction sub-pipeline) initially split but re-merged into R19 (intake pipeline) — OCR is one pass of the multi-pass orchestration; not a separate onward concept-identity.
- R17 (in-memory representation choice) flagged uncertain at the engagement-type axis (PURSUE-SEED vs DIAGNOSE); chose PURSUE-SEED because the concept was surfaced in P10 of innovation but not yet taken up; the choice is reviewable.
- The 5 critique refinements (R7-R11) kept as 5 separate identities per lean-to-split — each is a distinct wording change at a distinct piece (P2/P3, P4, P7, P7, P7); over-merging would collapse them into one "critique-edits" identity and lose the distinct semantic surfaces.
- The 7 detector designs (R20) kept as one identity at this grain — at depth, R20 splits into 7 sister inquiries (one per Policy class); breadth keeps it as one to preserve compactness.

## Invocation log

| Date | Mode | Entry | Identities-Δ | Convergence | Verdict |
|---|---|---|---|---|---|
| 2026-06-17 | root / project-space (breadth) | fresh | +22 | converged | PROCEED |
