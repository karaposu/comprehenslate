# `_route.md` — concept-map index for document intake handling concepts

This file is the persistent within-concept concept-map for this inquiry's onward route-field. Routelisting owns it; no process/control-flow state is recorded here. Loaded on every routelist run; updated load-modify-save.

---

## Invocation log

| Run timestamp (UTC) | Mode | Entry | Identities | Notes |
|---|---|---|---|---|
| 2026-06-17_14-14 | project-space (breadth) | fresh | 24 (R1-R24) | initial routelist on the inquiry's onward route-field |

---

## Identity registry

Each entry: `{ identity → { own-depth pointer, depth-signal, individuation history, first-seen, last-touched } }`. Depth-signal is a compact within-concept marker if the identity has been drilled (concept-space run); fresh identities carry no depth-signal yet.

| Identity | own-depth | depth-signal | Individuation history | First-seen | Last-touched |
|---|---|---|---|---|---|
| R1: `IntakeDoc` pydantic schema | none | — | created fresh 2026-06-17_14-14; load-bearing for many other identities | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R2: NonMainLangPartsPolicy perception detector | none | — | created fresh; split from R3-R8 per lean-to-split (distinct signals per policy) | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R3: SourceApparatusPolicy perception detector | none | coupled to R9 (PDF layout analysis) | created fresh; split from R2/R4-R8 | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R4: VoiceMarkingPolicy perception detector | none | — | created fresh; split from R2/R3/R5-R8 | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R5: ArchaicRegisterPolicy perception detector | none | language-resource-dependent | created fresh; split from R2-R4/R6-R8 | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R6: HonorificsPolicy perception detector | none | — | created fresh; split from R2-R5/R7-R8 | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R7: FormulaicOpeningPolicy perception detector | none | — | created fresh; split from R2-R6/R8 | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R8: EmbeddedPoetryPolicy perception detector | none | coupled to R9 (PDF typography loss) | created fresh; split from R2-R7 | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R9: OCR sub-pipeline design | none | coupled to R3 + R8 (layout analysis is shared dependency) | created fresh; merged A3 + layout-analysis sub-concept (both serve the same goal-role of preparing PDF for Pandoc) | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R10: Pandoc invocation per format | none | — | created fresh | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R11: Multi-file project intake mechanics | none | deferred until R14 prototype | created fresh | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R12: Intake-quality-metrics + gates | none | coupled to R1 (schema details inform metric definition) | created fresh; merged D2 + D3 + D4 (all serve quality-measurement goal-role) | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R13: Paratext handling override mechanism | none | — | created fresh | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R14: End-to-end Pandoc → IntakeDoc prototype on Risale-i Nur PDF | none | gates R22 (TEST) + R11 (multi-file) + R15 (Mac-app re-entry) | created fresh; PURSUE-SEED type because it's the integration test seed surfaced as "Next Action 3" in P9 | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R15: Mac-app intake UI re-entry (F4) | none | deferred until R14 + intake build | created fresh; INVESTIGATE-FRONTIER type because it's flagged-but-deferred | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R16: Standard intake pipeline-stage engineering (C3-C9) | none | depends on R1 + R10 + R18 (A7) | created fresh; consolidates 7 ENGINEER-tagged pipeline-stage manifestations into one identity (same goal-role) | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R17: Structure-engineering items (B3 / B11 / B12) | none | could merge with R16 in depth run (left split — distinct structural targets) | created fresh; consolidates 3 small structure-layer manifestations; uncertain-individuation noted | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R18: Format-engineering items (A5 / A7) | none | A7 is critical path for R16 | created fresh; consolidates 2 format-layer engineering manifestations | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R19: Decision 1 less-portable concern refinement | none | applies at finding.md construction | created fresh from critique REFINE-direction signal | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R20: Decision 2 typography-meaning concern refinement | none | applies at finding.md construction | created fresh from critique REFINE-direction signal | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R21: B5 PDF-marginalia format-dependent caveat | none | applies at finding.md construction | created fresh from critique REFINE-direction signal; coupled to R3 (the detector) and R9 (the layout-analysis dependency) | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R22: Pandoc + 7-policy split empirical validation | none | gated by R14 (needs prototype runnable first) | created fresh; TEST type because the inquiry's commitments need empirical verification | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R23: `IntakeDoc` schema versioning + idempotency + partial-intake (open questions) | none | resolvable inside R1 | created fresh; merged 3 open questions from P9 (all relate to schema-design refinement) | 2026-06-17_14-14 | 2026-06-17_14-14 |
| R24: Calibration corpus expansion beyond Risale-i Nur | none | gated by R14 + R22 | created fresh; CONSOLIDATE type because the move is cross-corpus aggregation; long-horizon | 2026-06-17_14-14 | 2026-06-17_14-14 |

---

## Within-concept depth notes

(None — no identity has been drilled to depth-run yet. This section accumulates depth-signals as concept-space runs occur. Each entry would record the identity's within-concept manifestation field [README, implementation, prior version, etc.] and any divergence flagged as a high-value epistemic route at that depth.)

---

## Individuation principles applied

For audit trail when future runs re-individuate:

- **R2-R8 split** (per asymmetric-failure lean-to-split): each of the 7 policy-perception detectors carries distinct signals + per-language resource needs; merging would hide per-detector design choices.
- **R12 merge of D2 + D3 + D4**: all serve the same goal-role (quality-measurement framing → metric design → gate threshold). Merging is safe — the three are manifestations of "intake quality measurement" at different abstraction levels.
- **R16 merge of C3-C9**: all serve the same goal-role (move document through standard pipeline stages). Merging keeps the breadth map compact while individual stage engineering is tractable as one cohesive task.
- **R17 / R18 split** (kept split with uncertainty noted): structure-engineering items (B3/B11/B12) and format-engineering items (A5/A7) have distinct structural targets but small surface; could be re-individuated in a depth run.
- **R23 merge of 3 open questions**: schema versioning + idempotency + partial-intake all refine the IntakeDoc design; merging them as one DIAGNOSE route signals they resolve at R1 design time.

These notes are the audit trail; perception governs in future runs — re-confirmation against the territory may shift individuation.
