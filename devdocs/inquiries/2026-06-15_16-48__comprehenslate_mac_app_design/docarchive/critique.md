# Critique — comprehenslate_mac_app_design

## User Input

```text
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/_branch.md

Upstream outputs: articulate_simple.md + surfacing.md + sensemaking.md + decomposition.md + innovation.md. Evaluate Innovation's 10 PCs + 2 AEs (Comprehenslate-Mac branding; user-visible triage).

Adversarial focus areas:
- 5-layer architecture soundness (P1/PC1) — hidden coupling? missing layers? Quality as 2 layers?
- 7 principle-derived features (P7/PC7) — right 7? missing UI-mappable? intrinsic-only included?
- MVP roadmap (P8/PC8) — v1 realistic for 3-6mo single-dev? wrong-tier items?
- FP2 conformance — any candidate asking for LLM-inferable facts?
- Anti-bloat conformance — too many features?
- Mac-platform native-ness — genuine macOS patterns or web-app patterns?
```

---

## Phase 0 — Dimension Construction

### Extracted from sensemaking SV6

Load-bearing principles + constraints:
- FP1-FP7 from PC1 (local-first; BYO credentials; native Mac; Tier 1-2 non-negotiable; schemas canonical; workflow canonical; don't-declare-LLM-inferable).
- C1-C10 from sensemaking.
- The "innovative heavy" user framing → differentiator-load-bearing-ness matters.
- Anti-bloat principle is recurring across the session.
- User-stated adversarial focus areas (above) drive several problem-specific dimensions.

### Dimensions

| # | Dimension | Weight | Source | Success criteria |
|---|---|---|---|---|
| D1 | **Architectural soundness** (5-layer is structurally motivated; no hidden coupling; no missing layers) | CRITICAL | SV6; user-stated focus | Substance-level: each surfaced feature places cleanly in one layer; layer-vs-layer coupling is through explicit interfaces (Project bundle structure; schemas) |
| D2 | **Principle-mapping correctness** (the 7 are UI-mappable; nothing intrinsic-only included; no UI-mappable principle missed) | CRITICAL | SV6 Ambiguity 3; user-stated focus | Substance-level: per-principle UI-mappability check; audit of remaining principles in `references/core/` for missed UI-mappable ones |
| D3 | **MVP feasibility** (v1 scope realistic for stated effort) | HIGH | SV6 resource perspective; user-stated focus | Aggregate dev-effort estimate per essential-tier item; compare to 3-6mo single-dev target |
| D4 | **FP2 conformance** | CRITICAL | SV6 FP7; user-stated focus; session-verbatim | External-anchor (user quotes "translation happens regardless of source language via LLMs"): no candidate field asks for LLM-inferable facts |
| D5 | **Anti-bloat conformance** | HIGH | Recurring user preference; user-stated focus | Per-tier item-count justification; load-bearing-ness check per essential item |
| D6 | **Mac-platform native-ness** | HIGH | C2 not-webapp; user-stated focus | External-anchor (Apple HIG): per-UI-pattern check; document-based-app + Keychain + menu bar + native controls; no web-stack patterns disguised as Mac |
| D7 | **Differentiator-load-bearing-ness** | HIGH | "innovative heavy" user framing | Per differentiating-tier item: does it surface Comprehenslate's substrate (harmony / translation principles) or is it generic LLM-app polish? |
| D8 | **Tier classification correctness** | HIGH | SV6 SP5 | Each item in essential/differentiating/deferrable tested against the triage criterion (MVP-critical / unique-to-Comprehenslate / nice-to-have) |
| D9 | **User-pushback fidelity** | HIGH | _branch.md MQ4 NOT-list + user-named features | External-anchor (session): every user-named feature appears in the design; no user-named exclusion (signup/login/webapp) is violated |
| D10 | **Data-model commitment** (Project-as-unit is right vs alternatives) | HIGH | SV6 KI2; Frame-premise test | Substance: does Project carry all the bundled content correctly? Are there features that would belong on a workspace-unit or task-unit instead? |
| D11 | Correctness | HIGH | Default | Solves the design ask (architectural + feature inventory + cross-cutting + roadmap) |
| D12 | Coherence | HIGH | Default | Composes with existing Comprehenslate substrate without break |
| D13 | **Frame-Premise: 5-layer architecture itself** | HIGH | Frame-premise refinement | What-if-wrong probe (against 3-layer and 7-layer alternatives — already done in Sensemaking Frame-exit; re-tested here) |
| D14 | **Frame-Premise: Project-as-data-model itself** | HIGH | Frame-premise refinement | What-if-wrong probe (against workspace-unit and task-unit alternatives) |

### Dimension validation

Cross-reference against sensemaking's perspectives:
- Technical → D1 + D6 + D11
- Human → D9
- Strategic → D7 + D8
- Risk → D3 + D4
- Resource → D3 + D5
- Ethical → D7 (ethical-provenance via lineage)
- Definitional Internal Consistency → D1 + D4
- Definitional Frame-exit → D13 + D14
- Phase/Calibration-State → implicit in D3 (LLM landscape calibration)

All upstream perspectives covered. **Dimension Blindness check: NOT FIRED.**

### Frame-premise test

Load-bearing premises:
1. 5-layer architecture is right (D13 probes).
2. Project-as-data-model is right (D14 probes).
3. 7 selectively-mapped principle features are the right cluster (D2 probes).
4. 3-tier triage is the right phasing (D8 probes).

### External-anchor dimension requirement

External anchors:
- User verbatim quotes ("project selection logic", "pause/continue", "support local llm models openai and antropic models at once", "save as pdf or md", "reading screen", "no signup or login", "not a webapp") → D9
- `schemas.py` + `SKILL.md` (project artifacts) → D1
- `references/core/` files (principle source) → D2
- Apple HIG conventions → D6
- User's session-wide anti-bloat preference → D5

D4, D6, D9 fire external-anchor sub-axis.

---

## Phase 1 — Fitness Landscape

- **Viable region:** candidates passing all CRITICAL (D1, D2, D4) and HIGH dimensions with at most 1 minor caveat.
- **Dead region:** candidates failing D1 (architectural mismatch); D2 (principle-mapping wrong); D4 (FP2 violation — asking for LLM-inferable fact).
- **Boundary region:** candidates passing CRITICAL but with caveats on HIGH (anti-bloat partial; MVP estimate optimistic; missing principle-derived feature).
- **Unexplored region:** AE-emergent space (branding, user-visible triage) — already DEFERRED at Innovation.

---

## Phase 2 — Adversarial Evaluation

### PC1 — Architectural commitments (5-layer + Project + 3-tier + FPs + cross-cutting)

**Prosecution:**

- **D1 + D13 (architectural soundness + frame-premise):** Is "Quality" actually two layers — operational quality (terminology, glossary, issue inbox) vs principle-derived viz (harmony, lineage, collation)? Test their lifecycle: operational quality is COMPUTED DURING translation; principle-derived viz is RENDERED ON DEMAND. Two different lifecycles. Counter-counter: they share UI surface (same tab); share data dependencies (consume per-chunk state); share user audience. Splitting them would fragment UX. **Conclusion:** they're SUB-MODULES of one Quality layer with mixed-lifecycle internals — normal in software architecture. Quality stays as one layer. **D1 PASSES.**
- **D1 (hidden coupling check):** Project shell (P2) ↔ Execution engine (P4) — both depend on .compldoc bundle structure. Made explicit by P1's commitment. NO HIDDEN COUPLING. Configuration (P3) ↔ Execution (P4) — config values feed Execution; schemas are the interface. Made explicit. NO HIDDEN COUPLING.
- **D4 (FP2 conformance):** PC1 is principles + architecture; no field-level user-input asking. **D4 PASSES.**
- **D5 (anti-bloat — 7 FPs):** Is FP3-FP7 inflating? Per-FP load-bearing test: remove FP3 (native Mac) → design becomes web-app-like (BAD); remove FP4 (Tier 1-2) → harmony toggle-able (BAD); remove FP5 (schemas canonical) → schemas rewritable (BAD); remove FP6 (workflow canonical) → workflow bypassable (BAD); remove FP7 (don't-declare-LLM-inferable) → user asked for source language (BAD). All 7 FPs are load-bearing. NOT BLOAT.
- **D6 (Mac-platform native-ness):** PC1 commits document-based-app + Keychain + menu bar + system notifications + Spotlight + share extension. All native macOS patterns. **D6 PASSES.**

**Defense:** 5-layer architecture is structurally motivated (clusters from surfacing's 155 items map cleanly); multiple Sensemaking perspectives confirmed; Frame-exit Completeness tested 3-layer and 7-layer counters; cross-cutting concerns naturally separate from layers.

**Collision:** Defense holds against all prosecution lines.

**Verdict: SURVIVE.** No caveats.

---

### PC2 — Project shell features

**Prosecution:**

- **D4 FP2 conformance:** "source-language (LLM-inferred per FP7 + user override)" — explicitly FP2-conformant (LLM infers; user override is value-judgment override). PASSES.
- **D5 anti-bloat:** essential 7 + differentiating 4 + deferrable 4 = 15. Comparison: Pages / Final Cut Pro project lifecycle is similar count. NOT BLOAT.
- **D9 user-pushback fidelity:** "project selection logic" → project list ✓; "save translation process" → per-chunk persistence in bundle ✓; "pause/continue" correctly homed in P4 not P2.
- **D6 Mac-platform native-ness:** document-based-app pattern + Finder integration + Quick Look extension. Native.

**Defense:** matches user requests; project templates per corpora are differentiating per "innovative heavy" framing.

**Verdict: SURVIVE.** No caveats.

---

### PC3 — Configuration surface features

**Prosecution:**

- **D4 FP2 conformance:** TC axes are user value judgments; Policy values are user value judgments; PC knobs are engineering choices. **No LLM-inferable facts asked.** PASSES.
- **D5 anti-bloat:** essential 5 + differentiating 6 + deferrable 4 = 15. Per-policy preview is high implementation cost — is it really differentiating tier (load-bearing) or deferrable (nice-to-have)? Counter: per-policy preview is the TEACHING surface for users who don't know what each Policy value does. Without it, the Policy editor becomes inscrutable. Load-bearing for first-time users. Stays differentiating.
- **D8 tier classification:** "inline calibration text" — could it be essential? Segmented controls carry SOME meaning via label; inline text is upgrade not essential. Stays differentiating. OK.
- **D6 Mac-platform native-ness:** segmented controls, sliders, dropdowns, disclosure triangles — native macOS. PASSES.

**Defense:** directly wraps `schemas.py` (FP5); cross-references calibration docs; teaches users the substrate.

**Verdict: SURVIVE.** No caveats.

---

### PC4 — Execution engine features

**Prosecution:**

- **D3 MVP feasibility:** essential tier has 10 items including multi-provider abstraction + per-chunk persistence + crash recovery + background continuation. Engineering effort estimate: ~10 weeks of focused work for the Execution layer alone in 3-6mo window. Adding other layers' essential tiers makes 3-6mo TIGHT. **CAVEAT: 3-6mo is optimistic for an inexperienced dev; 3-9mo more realistic range.**
- **D5 anti-bloat:** 10 essential items are different facets of the same persistence primitive (pause/resume + cancel + crash recovery + retry) plus orthogonal concerns (multi-provider + rate-limit). Each is a distinct user-facing affordance. NOT BLOAT.
- **D4 FP2 conformance:** PC4 doesn't ask the user for LLM-inferable facts. PASSES.
- **D9 user-pushback fidelity:** "pause/continue" ✓; "save progress per chunk" ✓; "support local llm models openai and antropic models at once" → essential has 2 providers (Anthropic + OpenAI); local LLM in differentiating tier. **This is a TENSION with user-pushback fidelity** — user said "at once," implying all 3 v1. The roadmap defers local to v2. See PC8 for the cross-cutting REFINE.

**Defense:** covers all runtime behaviors; provider abstraction enables multi-provider; smart cache + cost prediction are high-utility for long books.

**Verdict: SURVIVE with CAVEAT.** Constructive output: MVP estimate should be widened (PC8 addresses this); local LLM should move from differentiating tier (v2) to essential tier (v1) per user-pushback fidelity (PC8 addresses this too).

---

### PC5 — Reading & output features

**Prosecution:**

- **D8 tier classification:** "Search across source + target" placed in differentiating — could it be essential? Users expect search in any reading app. Counter: basic reading is sufficient for v1; search is a power-user upgrade. Defensible at differentiating tier.
- **D6 Mac-platform native-ness:** NSSplitView / SwiftUI split + AVSpeechSynthesizer + native PDF rendering. All native.
- **D9 user-pushback fidelity:** "save as pdf or md" ✓ (essential); "reading screen" ✓ (essential live reading view).
- **D5 anti-bloat:** 5 + 6 + 8 = 19. Deferrable has 8 export formats — does this bloat the catalog? Counter: each export format is a discrete user need; deferred items are catalog entries not v1 commitments. NOT BLOAT.

**Defense:** live reading + side-by-side are user-facing; analysis-depth overlay couples with TC.A8 differentiator.

**Verdict: SURVIVE.** No caveats.

---

### PC6 — Quality & translation-craft features

**Prosecution:**

- **D2 principle-mapping correctness:** PC6 differentiating tier includes the 7 principle-derived cluster (cross-references PC7). See PC7 evaluation.
- **D7 differentiator-load-bearing-ness:** the 9 differentiating items all surface Comprehenslate's substrate (harmony layer; translation principles; embedded-language; honorifics; glossary). Each is unique-to-Comprehenslate vs generic LLM apps. PASSES.
- **D5 anti-bloat:** essential 3 + differentiating 9 + deferrable 7 = 19. Differentiating is large — but this IS the innovative-heavy surface the user explicitly asked for. NOT BLOAT per the user's own framing.

**Defense:** cohesive set; each differentiating feature has clear UX role.

**Verdict: SURVIVE.** No caveats.

---

### PC7 — 7 translation-principle-derived differentiating features (CENTRAL ADVERSARIAL FOCUS)

**Prosecution (D2 — principle-mapping correctness; substance-axis):**

For each of the 7, test UI-mappability:

| # | Feature | UI-mappable? |
|---|---|---|
| 1 | Harmony-layer visualization | ✓ (user views Tier 1-4 markers; audits preservation) |
| 2 | Multi-translation collation | ✓ (user picks among priors) |
| 3 | Per-chunk lineage view | ✓ (user audits which TC/Policy values produced output) |
| 4 | Per-chunk analysis-depth explanation overlay | ✓ (user toggles "explain"; per TC.A8) |
| 5 | Passage bookmarks (fihrist) | ✓ (user marks passages; indexed view) |
| 6 | Idiom-alert inbox | ✓ (user reviews idioms; picks renderings) |
| 7 | Cultural-reference inbox | ✓ (user reviews allusions; picks renderings) |

All 7 PASS UI-mappability. None is intrinsic-only smuggled in.

**Audit: what UI-mappable principles did Innovation MISS?** Walk through `references/core/`:

- **Multi-meaning preservation per-chunk** (not just per-translator). The principle: *"all meanings derived from a text are valid... choosing a meaning is up to the user."* Innovation covered multi-translator collation (#2) but NOT per-chunk alternative-renderings. **MISSING UI-mappable feature.**
- **Rhetorical device detection (belagat).** The principle: *"rhetoric is a fundamental carrier of meaning."* Detect chiasmus / antimetabole / alliteration per chunk; flag for translator awareness. Currently only partially covered by harmony Tier-3. **MISSING UI-mappable feature.**
- **Escalation chain detection.** From `advanced_principles.md`: small-cycle-proves-large-cycle argumentation; the escalation pattern is non-negotiable but specific examples can adapt. Detect escalation chains; flag to translator. **MISSING UI-mappable feature.**
- **Self-illuminating passage flagging.** Innovation marked as INTRINSIC (LLM detects; user doesn't toggle). But the FLAGGING is itself UI-mappable — show user "this passage is self-illuminating; no external context added." **MISSING UI-mappable feature** (Sensemaking under-classified).
- **Grammatical-anomaly-as-deliberate alerts.** From `notes.md`: grammar violations in carefully composed text are usually deliberate. Detect anomalies; flag user. **POTENTIALLY MISSING.**
- **Meaningful omission flagging.** From `translation_principals.md`: omission carries meaning. Detect ellipses LLM treats as load-bearing; flag user. **POTENTIALLY MISSING.**

The 7 features are CORE but the set is INCOMPLETE. 3-4 additional UI-mappable principles surfaced.

Severity check (purpose-fitness): if the missing features were left out, would PC7 still do what it's supposed to (cover Comprehenslate's principle-derived UI surface)? It would do PART of it — but the "innovative heavy" mandate strongly implies completeness on this dimension. The omission is substantive but not architecture-breaking.

**Defense:** the 7 listed features are the SHAPE-FIT BEST; they're the most-immediately-UI-mappable and have the clearest user-decision surface. Adding more is incremental extension, not structural rewrite.

**Collision:** the 7 are CORRECT but the catalog is INCOMPLETE. This is REFINE territory, not KILL.

**Verdict: REFINE.** Constructive output: expand from 7 to ~10 principle-derived features. Specifically add:

- **#8 Alternative-renderings per chunk** (multi-meaning at chunk level; principle: *"all meanings derived from a text are valid... choosing a meaning is up to the user"*; layer-home: Quality; UX: each chunk shows 1-3 LLM-identified valid renderings; user picks).
- **#9 Rhetorical-device detection** (belagat-specific; principle: *"rhetoric is a fundamental carrier of meaning"*; layer-home: Quality; UX: per-chunk rhetorical-device markers; click → see device type and what's preserved/lost).
- **#10 Escalation-chain detection** (principle: *small-cycle-proves-large-cycle*; layer-home: Quality; UX: chain markers across chunks; "this passage uses escalation; pattern and final claim non-negotiable; small examples can adapt").

Optionally add (lower priority):
- **#11 Self-illuminating passage flagging** (re-classify from intrinsic to UI-mappable; layer-home: Reading; UX: "this passage is self-illuminating; no context required").
- **#12 Grammatical-anomaly-as-deliberate alerts** (principle: grammar violations are intentional in careful texts; layer-home: Quality; UX: flag detected anomalies with confidence score).
- **#13 Meaningful-omission flagging** (principle: omission carries meaning; layer-home: Quality; UX: flag ellipses LLM treats as load-bearing).

---

### PC8 — MVP roadmap

**Prosecution:**

- **D3 MVP feasibility:** Aggregate v1 effort estimate: P1 (~2 weeks design work) + P2 essential (~3 weeks) + P3 essential (~4 weeks) + P4 essential (~10 weeks for Execution including multi-provider) + P5 essential (~3 weeks) + P6 essential (~2 weeks) + cross-cutting baseline (~3 weeks) = ~27 weeks ≈ 6 months. Tight for experienced single dev; 9-12 months realistic for less experienced. **The 3-6mo claim is optimistic.**
- **D8 + D9 (tier classification + user-pushback fidelity):** Local LLM placed in v2 (differentiating). User explicitly said *"it shoudl ssupport local llm models openai and antropic models at once."* "At once" strongly implies CONCURRENT v1 support. Pushing local to v2 violates user-pushback fidelity. **D9 PROSECUTION SUCCEEDS.** Move local LLM to v1.
- **D8 cross-check:** is harmony Tier 1-2 flagging really v2? Per FP4, the PRESERVATION is non-negotiable (intrinsic LLM behavior in v1). The FLAGGING is the UI surface (v2 is fine for the visualization layer). Distinction holds. OK.

**Defense:** roadmap provides concrete commitment moments; aligns with development phases; respects anti-bloat by tiering.

**Collision:** two prosecution lines hit — (a) MVP estimate optimistic; (b) local LLM mis-tiered per user-fidelity.

**Verdict: REFINE.** Constructive output:
- (a) Widen v1 estimate to **3-9 months single-developer** (3-6mo for experienced; 9mo for less experienced).
- (b) Move **local LLM auto-discovery** from v2 (differentiating tier of P4) to **v1 essential** per user-pushback fidelity ("at once" implies concurrent v1 support of Anthropic + OpenAI + local).

---

### PC9 — Inherited Commitments Re-test

**Prosecution:**

- **Honesty check:** 5 CONFIRMED + 1 CONFIRMED-with-frame-revised. Is this rubber-stamping?
- Substance test: would the design work without each commitment?
  - Remove "3-layer schema architecture" → no config surface to design. BREAKS.
  - Remove "5-step workflow" → no UX flow spine. BREAKS.
  - Remove "Tier 1-2 non-negotiable" → harmony preservation becomes user-toggleable; contradicts user's intent. BREAKS.
  - Remove "comprehensation identity" → translation-principle features lose anchor. BREAKS.
  - Remove "anti-bloat" → catalog inflates without filter. BREAKS.
  - Remove "FP2" → user asked LLM-inferable facts. BREAKS.
- All 6 commitments are load-bearing for the design.
- The frame revision on "comprehensation identity" is structurally honest (selective principle-mapping splits UI-mappable from intrinsic).

**Defense:** each commitment cites structural evidence; verdicts honest.

**Verdict: SURVIVE.** No caveats.

---

### PC10 — Open Questions

**Prosecution:**

- **Completeness check:** are there missing open questions?
  - Update-aware migration (when `schemas.py` changes, prompt user to migrate config) — Surfacing identified but not in PC10. **MINOR GAP.**
  - LLM cost-curve evolution — partially in Monitoring.
- **D9 user-pushback fidelity:** monetization out-of-scope ✓; mobile/iPad future ✓ (user didn't ask); localization ✓.

**Defense:** standard finding-template open-questions structure; revival triggers per item.

**Verdict: SURVIVE with minor CAVEAT.** Constructive output: add **Update-aware migration** to Refinement Triggers (when `schemas.py` evolves, prompt user to migrate stored config; trigger: schemas.py schema change between v1 and v1.x).

---

### AE1 — "Comprehenslate Mac" branding (positioning)

**Prosecution:** is branding load-bearing for architectural design? Innovation correctly deferred — branding is downstream of distribution decisions. The Mac app design is architecture-complete without commitments to brand name or positioning.

**Verdict: DEFERRED (sustained from Innovation).** No constructive output beyond revival trigger.

---

### AE2 — User-visible triage as roadmap teaching surface

**Prosecution:** is exposing "deferrable" features to users wise marketing? Showing what users don't have can feel anti-marketing.

**Defense:** for power users who want roadmap visibility, a public roadmap page builds trust.

**Verdict: DEFERRED (sustained from Innovation).** Revival trigger: user demand for roadmap visibility.

---

## Phase 3 — Verdict Summary + Constructive Output

| Candidate | Verdict | Constructive Output |
|---|---|---|
| **PC1** Architectural commitments | SURVIVE | None |
| **PC2** Project shell features | SURVIVE | None |
| **PC3** Config surface features | SURVIVE | None |
| **PC4** Execution engine features | SURVIVE-with-CAVEAT | Local LLM should move from differentiating to essential tier (cross-resolved in PC8 REFINE) |
| **PC5** Reading & output features | SURVIVE | None |
| **PC6** Quality & translation-craft features | SURVIVE | None |
| **PC7** 7 principle-derived features | **REFINE** | Expand from 7 to ~10. ADD: (#8) alternative-renderings per chunk; (#9) rhetorical-device detection; (#10) escalation-chain detection. OPTIONALLY ADD: (#11) self-illuminating passage flagging; (#12) grammatical-anomaly alerts; (#13) meaningful-omission flagging. |
| **PC8** MVP roadmap | **REFINE** | (a) Widen v1 estimate to 3-9 months single-developer. (b) Move local LLM auto-discovery from v2 to v1 essential per user-pushback fidelity ("at once" implies concurrent v1 support). |
| **PC9** Inherited Re-test | SURVIVE | None |
| **PC10** Open Questions | SURVIVE-with-CAVEAT | Add Update-aware migration to Refinement Triggers |
| **AE1** Comprehenslate-Mac branding | DEFERRED (sustained) | None |
| **AE2** User-visible triage | DEFERRED (sustained) | None |

**Distribution:** 8 SURVIVE (2 with minor CAVEAT) + 2 REFINE (PC7 expand; PC8 widen+retier) + 2 DEFERRED. Zero KILLs.

### User-stated-concern resolution

1. **5-layer architecture soundness (PC1):** prosecuted via D1 (Quality-as-2-layers test; hidden coupling test) + D13 (3-layer / 7-layer counters re-tested). **VERDICT: 5 layers structurally sound; Quality is one cohesive layer with mixed-lifecycle internals; no hidden coupling.**
2. **7 principle-derived features (PC7):** prosecuted via D2 substance-axis audit of `references/core/` principles. **VERDICT: the 7 are CORRECT but the set is INCOMPLETE; 3-6 additional UI-mappable principles surfaced; PC7 expanded to ~10 (constructive output above).**
3. **MVP roadmap (PC8):** prosecuted via D3 effort estimate + D9 user-pushback fidelity. **VERDICT: 3-6mo is optimistic; widen to 3-9mo; local LLM should be v1 not v2 per user's "at once" framing.**
4. **FP2 conformance (D4):** every candidate passes; no candidate asks for LLM-inferable facts.
5. **Anti-bloat conformance (D5):** the catalogs are large but each tier respects the user's framing (innovative-heavy in differentiating; MVP-discipline in essential). Deferrable entries are catalog-not-commitment. NOT BLOAT.
6. **Mac-platform native-ness (D6):** all UI patterns (document-based-app; menu bar; Keychain; segmented controls; SwiftUI; AVSpeechSynthesizer; NSSplitView; system notifications; Spotlight; share extension) are native macOS. No web-stack patterns.

---

## Phase 3.5 — Assembly Check

Combining SURVIVE + REFINE survivors: the design holds together coherently. The two REFINEs (PC7 expansion to ~10 features; PC8 widening + local-LLM-retier) are content-adjustments not structural rewrites. The 5-layer architecture, Project-as-data-model, 3-tier triage, and cross-cutting concerns are unchanged.

No new assembly emergent at Critique stage. AE1 and AE2 remain DEFERRED.

---

## Phase 4 — Coverage + Convergence Assessment

### Coverage map

- **Per-candidate:** 14 dimensions × 10 PCs + 2 AEs = full adversarial coverage.
- **Per-solution-space:** clean SURVIVE cluster (6 candidates) + REFINE boundary (2) + DEFERRED unexplored (2 emergents).

### Convergence

- At least one SURVIVE with no critical-dimension caveat: YES — PC1, PC2, PC3, PC5, PC6, PC9 are clean SURVIVE.
- Landscape stability: YES — single iteration produced stable positioning.
- Unexplored: monetization model + branding + user-visible triage are Open-Questions / Deferred (intentional).
- Accumulator: iteration 1; convergence reached.

### Mechanism-Independence Quarantine check

Do surviving candidates have external-anchor evidence?

- PC1: schemas.py + SKILL.md (empirical artifacts) ✓
- PC2: schemas.py + user verbatim ("project selection logic") ✓
- PC3: schemas.py + config_base_source.md + policy_config_base_source.md ✓
- PC4: user verbatim ("pause/continue"; "support local llm models openai and antropic models") ✓
- PC5: user verbatim ("save as pdf or md"; "reading screen") ✓
- PC6: references/core/ + harmony_layer.md ✓
- PC7: references/core/ principle texts ✓
- PC8: same anchors as PC4/PC5
- PC9: 6 prior commitments anchored in artifacts ✓
- PC10: prior inquiry findings + session context ✓

**Quarantine NOT triggered.** All surviving candidates cite external anchors.

### Failure mode scan

| Mode | Status | Notes |
|---|---|---|
| #1 Wrong Dimensions | NOT FIRED | Dimensions extracted from sensemaking + user-stated focus areas |
| #2 Rubber-Stamping | NOT FIRED | 2 REFINEs + 2 CAVEATs across 10 PCs — genuine prosecution worked |
| #3 Nitpicking | NOT FIRED | No KILLs; refinements address load-bearing concerns (principle-set completeness; user-pushback fidelity on local LLM) |
| #4 Dimension Blindness | NOT FIRED | Cross-reference against sensemaking perspectives verified |
| #5 False Convergence | NOT FIRED | Multiple clean SURVIVEs; landscape stable; REFINEs are content-adjustments not structural |
| #6 Evaluation Drift | N/A | Single iteration |
| #7 Self-Reference Collapse | NOT FIRED | Subject is the Mac app design, not critique itself |
| #8 Axis Absence | NOT FIRED | User-stated focus areas explicitly dimensional (D1, D2, D3, D4, D5, D6) |
| #9 External-Grounding Absence | NOT FIRED | All survivors cite external anchors |

### Signal

**TERMINATE.** Coverage sufficient; convergence reached; refinements applied at finding-write-time:
- PC7 → expand from 7 to ~10 principle-derived features
- PC8 → widen v1 estimate to 3-9mo; move local LLM to v1 essential
- PC4 → CAVEAT cross-resolved in PC8
- PC10 → add Update-aware migration to Refinement Triggers

No iteration needed.

---

## Convergence Telemetry

- **Dimension coverage:** 14 dimensions; 6 default + 8 problem-specific (D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D13, D14 are problem-specific or frame-premise).
- **Adversarial strength:** STRONG — user-stated focus areas generated explicit dimensions; substance-axis prosecution on D2 surfaced principle-set gap; external-anchor sub-axis fired at D2, D4, D6, D9.
- **Landscape stability:** STABLE.
- **Clean SURVIVE exists:** YES (6 clean SURVIVEs; 2 SURVIVE-with-minor-CAVEAT; 2 REFINE; 2 DEFERRED).
- **Failure modes observed:** NONE.
- **Overall: PROCEED.**
