# `_route.md` — concept-map index for canonical intake format deep dive

This file is the persistent within-concept concept-map for this inquiry's onward route-field. Routelisting owns it; no process/control-flow state is recorded here. Loaded on every routelist run; updated load-modify-save.

---

## Invocation log

| Run timestamp (UTC) | Mode | Entry | Identities | Notes |
|---|---|---|---|---|
| 2026-06-17_18-21 | project-space (breadth) | fresh | 12 (R1-R12) | initial routelist on the inquiry's onward route-field; concludes the canonical-format deep-dive |

---

## Identity registry

Each entry: `{ identity → { own-depth pointer, depth-signal, individuation history, first-seen, last-touched } }`.

| Identity | own-depth | depth-signal | Individuation history | First-seen | Last-touched |
|---|---|---|---|---|---|
| R1: JSON-AST canonical schema design | none | — | created fresh; load-bearing for R3, R4, R6 | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R2: Round-trip-stable Pandoc-md subset definition | none | depends on R4 prototype edge cases | created fresh | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R3: EPUB 3 generation pipeline design | none | depends on R1 + R4 | created fresh; kept split from R4 (R3 = design; R4 = integration) | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R4: End-to-end AST → EPUB prototype on Risale-i Nur sample | none | gates R8 (cross-corpus validation) + R2 edge-case discovery | created fresh; PURSUE-SEED type (integration test seed) | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R5: Apply the 4 REFINE-direction adjustments at finding.md construction | none | one-shot; resolved at CONCLUDE | created fresh from critique REFINE-direction signals | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R6: Re-spec the seven policy-perception detectors for AST node types | none | tightly couples to R1 (schema apparatus shape) | created fresh; kept split from R5 (R5 = this inquiry's finding edits; R6 = prior finding's detector specs) | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R7: Pandoc cross-version stability validation | none | resolvable inside R1 | created fresh from critique REFINE-direction; TEST type | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R8: Cross-corpus format-architecture validation | none | gated by R4 | created fresh; TEST type | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R9: TEI as future archival output | none | conditional on scholarly archival need OR R8 surfacing TEI requirement | created fresh; INVESTIGATE-FRONTIER type | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R10: Custom format revisit | none | conditional on AST + md + EPUB insufficiency | created fresh; INVESTIGATE-FRONTIER type with named triggers | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R11: Archival / historical preservation as fifth temporal layer | none | conditional on archival need emergence | created fresh; REFRAME type | 2026-06-17_18-21 | 2026-06-17_18-21 |
| R12: Pandoc version pinning operational policy | none | small task; resolvable in project engineering README | created fresh; REFINE type | 2026-06-17_18-21 | 2026-06-17_18-21 |

---

## Within-concept depth notes

(None — no identity has been drilled to depth-run yet.)

---

## Individuation principles applied

- **R3 / R4 split** (kept separate): R3 is the EPUB pipeline design inquiry; R4 is the integration prototype that tests the whole architecture (intake + schema + EPUB). Different goal-roles.
- **R5 / R6 split** (kept separate): R5 is editing THIS inquiry's finding.md per critique's REFINE adjustments; R6 is refining the PRIOR finding's detector specs. Different artifacts targeted.
- **R7 / R12 merge?** considered: R7 is TEST (empirical cross-version drift); R12 is REFINE (operational policy). Kept split — different engagement-types.
- **R8 (cross-corpus) / R11 (archival layer) split**: kept separate. R8 tests whether the three-format works for other corpora; R11 considers ADDING a fifth layer for archival. Different goal-roles.

---

## Coupling notes (for downstream consumers — not adjudicating priorities)

- R1 is the architectural-keystone — R3, R6 directly depend; R2 and R4 indirectly depend.
- R4 is the empirical-keystone — R2 (subset definition) and R8 (cross-corpus) both depend on R4 surfacing issues + baseline.
- R5 is the publish-keystone — must apply at CONCLUDE to make the finding correct.
- R9, R10, R11 are conditional-future routes with named triggers; they do not gate anything in the current commit.
