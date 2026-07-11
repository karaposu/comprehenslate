# Concept Index — intake preprocessing operations

> Persistent identity-set + invocation log. Routelisting writes this file itself on every run.
> Within-concept only (no inter-concept dependency edges; no process/control-flow state).

## Identity Set

| ID | Identity | First-seen | Last-touched | Own-depth pointer | Depth-signal |
|---|---|---|---|---|---|
| R1 | Per-category operation specs (MUST 1) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R2 | Hierarchy-inference algorithm for flat-h1 sources (MUST 2) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R3 | Format-specific Pandoc invocation patterns (MUST 3) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R4 | Category 7 flag-exposure mechanism (MUST 4) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R5 | Test-case fixture corpus (MUST 5) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R6 | Mac app PipelineConfig html-output integration (MUST 6) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R7 | Pandoc version pin for v0.2 reproducibility (MUST 7) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R8 | Category 8 extensions API design (COULD 1) | 2026-06-17 | 2026-06-17 | — | uncertain-individuation (DEVELOP vs INVESTIGATE-FRONTIER) |
| R9 | Hierarchy-inference for additional corpora (COULD 2) | 2026-06-17 | 2026-06-17 | — | frontier; gated on R8 + DEFERRED 2 |
| R10 | Quality-floor sub-category boundary refinements (COULD 3) | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R11 | Word + plain-text format support (DEFERRED 1) | 2026-06-17 | 2026-06-17 | — | frontier; demand-driven |
| R12 | Cross-corpus validation (DEFERRED 2) | 2026-06-17 | 2026-06-17 | — | frontier; gated on R5 stability |
| R13 | Classification work (DEFERRED 3) | 2026-06-17 | 2026-06-17 | — | frontier; conditional revival |
| R14 | Per-corpus configuration UI in Mac app (DEFERRED 4) | 2026-06-17 | 2026-06-17 | — | frontier; gated on R8 + R9 |
| R15 | Cross-cutting critique refinements integration (8 edits at CONCLUDE) | 2026-06-17 | 2026-06-17 | — | bundled identity; merged at finding-compose grain |
| R16 | Scope-line edge case adjudication | 2026-06-17 | 2026-06-17 | — | demand-driven (new gray-zone op surfaces) |
| R17 | Sentence segmentation Turkish quality | 2026-06-17 | 2026-06-17 | — | empirical gate |
| R18 | Hyphenation-repair false-positives mitigation | 2026-06-17 | 2026-06-17 | — | empirical gate; mitigation paths sketched |
| R19 | EPUB-from-PDF detection heuristics | 2026-06-17 | 2026-06-17 | — | breadth-only |
| R20 | Multi-volume document handling | 2026-06-17 | 2026-06-17 | — | frontier; demand-driven |
| R21 | Intake-output versioning | 2026-06-17 | 2026-06-17 | — | frontier; demand-driven |
| R22 | CI for v0.2 reproducibility | 2026-06-17 | 2026-06-17 | — | breadth-only; composes with R5+R7+R1 |
| R23 | Calibration of empirical thresholds | 2026-06-17 | 2026-06-17 | — | breadth-only; engineering-pull |

## Individuation history

- Fresh entry point; 23 identities individuated in one breadth run.
- Per lean-to-split principle: R7 (Pandoc version pin) kept separate from R22 (CI for reproducibility) — different concepts (version selection vs infrastructure).
- Per lean-to-split principle: R10 (quality-floor boundary refinements) kept separate from R23 (calibration of empirical thresholds) — R10 is which-ops-where; R23 is what-threshold-values.
- Per lean-to-split principle: R1 (per-category specs) kept as ONE merged identity at breadth grain (not split into 8 sub-routes); the depth-resolution split into 8 sub-inquiries is a depth-run consideration.
- Per lean-to-split principle: R15 (cross-cutting refinements) kept as ONE bundled identity at the finding-compose-time grain — 8 distinct refinements at distinct pieces, but they all happen at one moment (CONCLUDE) with the same engagement-type (REFINE).
- R8 (Category 8 extensions API design) flagged uncertain at engagement-type axis (DEVELOP vs INVESTIGATE-FRONTIER); chose DEVELOP because the API shape (opt-in plugin; per-corpus configuration) is concrete enough; the choice is reviewable.

## Invocation log

| Date | Mode | Entry | Identities-Δ | Convergence | Verdict |
|---|---|---|---|---|---|
| 2026-06-17 | root / project-space (breadth) | fresh | +23 | converged | PROCEED |
