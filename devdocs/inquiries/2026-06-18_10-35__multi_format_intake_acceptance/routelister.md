# Route Map — multi-format intake acceptance

## User Input

territory: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-18_10-35__multi_format_intake_acceptance/` (7 inquiry artifacts).

goal: enumerate the onward route-field this inquiry opens. Committed: per-format 4×2 matrix; acceptance-vs-priority distinction; hybrid auto-detect + warn-and-degrade + UI recommendation routing; quality-tier flag extending Category 7; `refines:` prior intake-preprocessing-operations finding.

---

## Map Header

- **Identities enumerated:** 17
- **High-priority count:** 4 (R1-R3 MUSTs + R4 refinements-bundle)
- **Mode:** root / project-space (breadth)
- **Entry point:** fresh

## Route Index

| # | Direction | grain | kind | engagement-type | Priority |
|---|---|---|---|---|---|
| R1 | Quality-tier + format fields added to Cat 7 schema (composes with prior MUST 4) | project-space | teleological | DEVELOP | HIGH |
| R2 | Magic-bytes lookup table for source-format detection | project-space | teleological | DEVELOP | HIGH |
| R3 | Mac app UI "EPUB recommended" message text | project-space | teleological | DEVELOP | HIGH |
| R4 | Cross-cutting critique refinements integration (6 edits at CONCLUDE) | project-space | epistemic | REFINE | HIGH |
| R5 | Runtime complex-content auto-detection | project-space | teleological | INVESTIGATE-FRONTIER | MED |
| R6 | Plain-text structural recovery | project-space | epistemic | INVESTIGATE-FRONTIER | MED |
| R7 | Word reader engineering (cross-reference prior R11 of preprocessing-operations finding) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R8 | Magic-bytes lookup table maintenance (ongoing) | project-space | teleological | DEVELOP | LOW |
| R9 | Quality-tier downgrade for EPUB-from-PDF (composes with prior R19) | project-space | teleological | DEVELOP | MED |
| R10 | UI guidance effectiveness measurement | project-space | epistemic | TEST | MED |
| R11 | Additional format acceptance (RTF / FB2 / ODT / MOBI / AZW3 / KFX) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R12 | Format conversion utilities in Mac app (e.g., PDF-to-EPUB helper) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R13 | Calibration-corpus-aware UI guidance (composes with prior R8 Cat 8 API) | project-space | teleological | DEVELOP | LOW |
| R14 | Streaming intake for large source files | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R15 | Multi-file / multi-volume input (cross-reference prior R20 multi-volume) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R16 | URL input (user pastes a URL to web-sourced content) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R17 | Mac app drag-and-drop UX specifics | project-space | teleological | DEVELOP | MED |

---

## Per-Route Records

### R1 — Quality-tier + format fields added to Cat 7 schema

```
Direction:        quality-tier + format fields added to Category 7 informational-flag schema
Goal:             extend the prior finding's MUST 4 schema with the new format-fidelity fields
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         add `quality_tier` ∈ {high, medium, low, minimal} and `format` ∈ {epub, pdf, md, txt}
                  as top-level fields in the sidecar JSON schema and as <meta> blocks in HTML5 <head>;
                  document the field semantics for downstream consumers
WHY:              the per-format matrix (P3) requires a runtime signal of format-fidelity;
                  the prior's Category 7 schema is the natural composition target
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "Top-level in sidecar JSON; not inside the `flags` array" (bc per-source attribute, not flag-event)
  · "Composes with prior MUST 4; same inquiry could cover both" (bc minimal duplication)
Depth-link:       none
```

### R2 — Magic-bytes lookup table for source-format detection

```
Direction:        magic-bytes lookup table + detection algorithm for 4 input formats
Goal:             ship a deterministic format-detection mechanism for the v0.2 routing
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         document magic-byte signatures: EPUB (PK\x03\x04 ZIP header + mimetype entry
                  `application/epub+zip`); PDF (%PDF- header); md (no magic byte; heuristic);
                  txt (text/plain; encoding-detection per Category 6 plain-text path);
                  implement detection via python-magic + extension-first hybrid logic
WHY:              the hybrid auto-detect routing (P4) depends on reliable format detection;
                  python-magic is the standard libmagic wrapper for Python
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "Extension first; magic-bytes as verification" (bc innovation P4)
  · "Ambiguous md/txt case defaults to txt (lower tier; safer)" (bc lean-to-conservative)
Depth-link:       none
```

### R3 — Mac app UI "EPUB recommended" message text

```
Direction:        Mac app UI message text for the "EPUB recommended for complex content" notice
Goal:             ship the user-facing notice text + display logic
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         draft message text; specify display conditions (when user is about to ingest
                  a non-EPUB source for a complex-content corpus); specify dismissal behavior
                  (user can continue without changing source; notice does not block)
WHY:              the routing mechanism (P4) commits this as the user-facing guidance surface;
                  without ship-ready message text, the UI commitment is incomplete
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "Soft notice; not modal; user can dismiss / continue" (bc honor-user-agency)
  · "Display BEFORE intake runs (not after)" (bc the guidance is to influence format choice)
Depth-link:       none
```

### R4 — Cross-cutting critique refinements integration (HIGH-priority pre-CONCLUDE work)

```
Direction:        integrate critique's 6 cross-cutting refinements at CONCLUDE composition
Goal:             the finding's text reflects critique-surfaced wording + completeness sharpening
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         apply per critique.md verdicts:
                  (a) P2 — cite the prior's DEFERRED 1 verbatim (not paraphrase)
                  (b) P3 — promote Word row to ACCEPTED-at-MINIMUM + DEFERRED-priority (consistent with txt/md)
                  (c) P4 — specify format-extension-mismatch flag downstream consequence
                  (d) P6 — Decision 5 verdict: PRESERVED (not STRENGTHENED — prior already strengthened)
                  (e) P7 — rewrite the "update prior DEFERRED 1" MUST: this finding supersedes in practice; no editing of prior
                  (f) P8 — add 4 frontier items: streaming intake; multi-file / multi-volume (cross-reference prior R20); URL input; Mac app drag-and-drop UX
WHY:              critique surfaced 6 refinement targets; CONCLUDE composes finding.md and is the moment to apply;
                  without integration the finding's text doesn't reflect critique honesty
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "All are wording / completeness; no architectural change" (bc bounded work)
  · "Apply during CONCLUDE composition, before finding.md is committed" (bc workflow-anchored)
Depth-link:       none
```

### R5 — Runtime complex-content auto-detection

```
Direction:        runtime complex-content auto-detection at intake-time
Goal:             intake-time detection of complex content; intelligent EPUB recommendation
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         design heuristics or model for runtime detection (multi-alphabet via Unicode-range scan;
                  apparatus via footnote-anchor scan; structural depth via heading-count); evaluate
                  against calibration corpus; integrate with UI recommendation if reliable
WHY:              v0.2 deferred this; future versions may need it if UI guidance proves ineffective
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "Revival: empirical evidence shows users miss UI guidance" (bc demand-driven)
Depth-link:       none
```

### R6 — Plain-text structural recovery

```
Direction:        plain-text structural recovery from blank-line patterns + numbered-section markers
Goal:             lift the txt quality-tier from `minimal` to `low` for sources with detectable structure
grain:            project-space
kind:             epistemic
engagement-type:  INVESTIGATE-FRONTIER
Movement:         heuristic detection of section-start patterns in plain text (blank-line clusters;
                  numbered headings; centered single-line text); promote to structural hierarchy where
                  detected; if reliable for Risale-i Nur calibration corpus, ship as v0.x enhancement
WHY:              plain-text Risale-i Nur sources (copy-paste from sites) are realistic input;
                  structural recovery would improve translate-quality
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "Revival: users frequently hand plain-text Risale-i Nur sources" (bc empirical gate)
Depth-link:       none
```

### R7 — Word reader engineering (cross-reference prior R11)

```
Direction:        Word (.docx) reader engineering for high-quality intake
Goal:             when source-mix expands to include Word sources, build high-quality Word reader
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         design Pandoc-docx-reader composition with intake Category 6 (style-mapping;
                  run-merge; Track Changes handling; embedded comments handling)
WHY:              the prior finding's DEFERRED 1 (now refined in this finding to scope only to Word)
                  preserves this as DEFERRED; revival triggered by source-mix expansion
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "Cross-reference: prior intake-preprocessing-operations finding's R11 covers this identity" (bc avoid duplication)
  · "Revival: project source-mix expands to include Word" (bc per prior + this finding)
Depth-link:       none
```

### R8 — Magic-bytes lookup table maintenance (ongoing)

```
Direction:        magic-bytes lookup table maintenance across format additions
Goal:             keep the lookup table current as new formats are added
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         when a new format is added (e.g., RTF, FB2), extend the lookup table with its
                  magic-byte signature; update the routing code
WHY:              format addition is a recurring concern; treating it as ongoing engineering work
                  rather than a one-shot inquiry reflects reality
Priority:         LOW     Confidence: HIGH
Guidance Mode:    compact
  · "Composes with R11 (new format acceptance) — each new format triggers this maintenance" (bc joint demand)
Depth-link:       none
```

### R9 — Quality-tier downgrade for EPUB-from-PDF

```
Direction:        quality-tier downgrade logic for EPUB-from-PDF cases (composes with prior R19)
Goal:             when EPUB-from-PDF is detected (per prior R19 heuristics), downgrade quality-tier
                  from `high` to `medium`
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         integrate EPUB-from-PDF detection signals from prior R19 with this finding's
                  quality-tier flag; emit `medium` instead of `high` for detected EPUB-from-PDF
                  sources; document the downgrade rule
WHY:              the per-format matrix's EPUB=high assumes well-formed EPUB; the EPUB-from-PDF
                  edge case violates the assumption; the downgrade preserves the matrix's honesty
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "GATED on prior R19 — EPUB-from-PDF detection must resolve first" (bc this finding consumes that signal)
Depth-link:       none
```

### R10 — UI guidance effectiveness measurement

```
Direction:        measure whether users heed the Mac app "EPUB recommended" UI notice
Goal:             empirical validation of the UI guidance approach
grain:            project-space
kind:             epistemic
engagement-type:  TEST
Movement:         when v0.2 ships, observe user behavior around the EPUB-recommendation notice;
                  measure how often users continue with non-EPUB sources after seeing the notice;
                  measure translation-quality outcomes for those cases
WHY:              the no-runtime-detection commitment rests on the UI guidance being effective;
                  empirical validation determines whether to revive R5 (runtime detection)
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "Composes with R5 — if effectiveness is low, R5 fires" (bc complementary)
Depth-link:       none
```

### R11 — Additional format acceptance (RTF / FB2 / ODT / MOBI / AZW3 / KFX)

```
Direction:        accept additional input formats beyond the v0.2 four
Goal:             extend format acceptance to other formats as use cases arise
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         for each candidate format (RTF, FB2, ODT, MOBI, AZW3, KFX), evaluate Pandoc reader
                  availability + use-case demand + quality-tier assignment; ship acceptance when
                  use-case justifies engineering effort
WHY:              the acceptance-vs-priority architecture extends cleanly to new formats;
                  most are low priority until a specific use case names them
Priority:         LOW     Confidence: HIGH
Guidance Mode:    compact
  · "Demand-driven: each format awaits a specific user case" (bc revival trigger)
  · "Pandoc reads ODT and RTF natively" (bc lower acceptance cost for those two)
Depth-link:       none
```

### R12 — Format conversion utilities in Mac app

```
Direction:        format conversion utilities built into Mac app (e.g., "convert PDF to EPUB first")
Goal:             provide user-facing format-improvement tools in the Mac app
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         evaluate whether built-in format conversion (PDF → EPUB; txt → md;
                  Word → md) would improve user outcomes; if so, design Mac app UI for the conversion
WHY:              users handling low-fidelity sources might benefit from conversion-then-intake
                  workflow; would compose with quality-tier signal
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "Revival: empirical evidence users want conversion built into the app" (bc UX signal)
Depth-link:       none
```

### R13 — Calibration-corpus-aware UI guidance

```
Direction:        calibration-corpus-aware UI guidance (composes with prior R8 Cat 8 API)
Goal:             tailor the EPUB-recommendation notice to the corpus the user has identified
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         when corpus context is named (e.g., --corpus risale-i-nur), customize the UI
                  recommendation; for known-complex corpora make the notice more emphatic;
                  for known-simple corpora suppress
WHY:              currently the UI recommendation is generic; corpus-awareness improves UX
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "GATED on prior R8 (Category 8 extensions API)" (bc corpus context comes from Cat 8)
Depth-link:       none
```

### R14 — Streaming intake for large source files

```
Direction:        streaming intake for large source files
Goal:             handle very large source files (100+ MB) without exceeding in-memory limits
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         design streaming-read + chunked-processing architecture for large source files;
                  evaluate which intake categories can be streamed (Category 1 normalization;
                  Category 2 sentence segmentation) vs which need whole-document context
                  (Category 5 structural detection)
WHY:              v0.2 assumes in-memory processing; large source files may exceed limits
Priority:         LOW     Confidence: LOW
Guidance Mode:    compact
  · "Revival: a source file exceeds in-memory limits" (bc empirical gate)
Depth-link:       none
```

### R15 — Multi-file / multi-volume input (cross-reference prior R20)

```
Direction:        multi-file / multi-volume input handling
Goal:             handle multi-volume works (e.g., Risale-i Nur Külliyat as 5+ EPUBs)
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         design how multi-volume composition works; cross-volume references; single
                  canonical for the whole collection vs per-volume canonicals
WHY:              the prior intake-preprocessing-operations finding's R20 covers this same identity
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "Cross-reference: prior R20 covers this identity" (bc avoid duplication; same demand-driven trigger)
Depth-link:       none
```

### R16 — URL input

```
Direction:        URL input (user provides a URL rather than a local file)
Goal:             accept web-sourced content via URL
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         design URL fetching + format detection from URL + content negotiation;
                  decide which URL sources are supported (direct file downloads; Substack
                  exports; GitHub README raw views)
WHY:              users may have web-sourced content (Substack articles; GitHub README;
                  online editions of classical texts)
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "Revival: project source-mix includes web-sourced content" (bc demand-driven)
Depth-link:       none
```

### R17 — Mac app drag-and-drop UX specifics

```
Direction:        Mac app drag-and-drop UX for intake source acceptance
Goal:             concrete UX design for how user provides source files to intake
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         specify drag-and-drop behavior; file-picker behavior; URL-input UI; multi-file
                  selection; UI feedback during intake processing; error display for unsupported
                  formats; quality-tier display
WHY:              the Mac app's UI layer needs concrete specification for the v0.2 intake workflow;
                  currently the UI surface is named but not specified
Priority:         MED     Confidence: HIGH
Guidance Mode:    compact
  · "Composes with R3 (UI message text) + R6 (Mac app integration from prior finding)" (bc UI-layer composition)
Depth-link:       none
```

---

## Excluded

| Candidate | Reason |
|---|---|
| "Edit the prior finding's DEFERRED 1 wording" | excluded — findings are immutable historical record; refining produces a new finding whose content supersedes in practice (per critique R-P7) |
| "Re-litigate the user's `all 3 vs 4` typo" | excluded — handled in P3 via explicit acknowledgment; not a route |
| "Re-open the canonical format choice (HTML5)" | excluded — settled in the post-repair canonical format finding; not in this inquiry's scope |
| "Per-format engineering inquiries (8 per-category specs from prior R1)" | excluded — covered by prior finding's R1; not duplicated here |
| "Translate-stage prompt design for low-quality-tier sources" | excluded — translate-stage scope, not intake |
| "Publishing-stage CSS for displaying source-quality-tier in published EPUB" | excluded — publishing-stage scope, not intake |

---

## Telemetry

| Field | Value |
|---|---|
| Mode | root / project-space (breadth) |
| Entry point | fresh |
| Identities enumerated | 17 |
| Routes — teleological | 13 |
| Routes — epistemic | 4 |
| High-priority count | 4 (R1-R3 MUSTs + R4 refinements-bundle) |
| Cross-references to prior inquiry | 3 (R7 ↔ prior R11; R9 ↔ prior R19; R15 ↔ prior R20) |
| Individuations made | 17 splits; 1 merge (runtime complex-content detection as COULD and frontier merged into single R5; ditto for plain-text recovery R6 and Word engineering R7) |
| Uncertain individuations flagged | 0 |
| Stale entries flagged | 0 (fresh entry point) |
| Convergence status | converged |
| Frontier flags emitted | 0 |
| LAYER 1 modes scanned | Over-merge: no (R7 vs prior R11 cross-referenced not merged; R9 vs prior R19 same). Under-coverage: no (MUST + COULD + DEFERRED + critique refinements + frontier items all covered). Wrong-grain: no. Goal-loss: no. Type-misassignment: no. Index-drift: NA (fresh). |
| LAYER 2 modes scanned | Selection-creep: no. Process-coupling: no. Description-collapse: no. Manifestation-dump: no. |
| Self-assessment verdict | **PROCEED** |

---

## Self-Assessment

**PROCEED.** Territory swept at identity resolution; 17 concept-identities individuated. 3 routes cross-reference the prior inquiry's routes (R11, R19, R20) rather than duplicating. No LAYER 1 or LAYER 2 failure modes. Output ready for the routelog / consumer step.
