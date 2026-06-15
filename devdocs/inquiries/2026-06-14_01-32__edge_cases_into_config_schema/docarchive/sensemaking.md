# Sensemaking — Edge-Cases into Config Schema

## User Input

Input file: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/_branch.md`
Upstream: `articulate_simple.md` + `surfacing.md` in same folder. Synthesis priors: edge-cases innovation + chunking finding.

---

## SV1 — Baseline

The user wants to know how 14 edge-case candidates should change the current 8-field TranslationConfig. They just settled chunking with split-placement architecture. They have anti-bloat preferences. In-flight Nursi 4_mesele translation likely needs at least #1 (Arabic ayahs).

---

## Phase 1 — Cognitive Anchor Extraction

**Constraints:**
- **C1** — Anti-bloat: user has consistently pushed back against schema/spec sprawl (280-line config rewrite cut; config_base_source.md bloat cut; chunking finding kept TC additions to ONE field).
- **C2** — Split-placement precedent: chunking finding established schema ownership matches data ownership.
- **C3** — Pre-routing inheritance: #1 → `ChunkingUnit.is_atomic`, #6 → `ChunkingUnit.attached_to`, #7 → orthogonal sister-concept. SETTLED.
- **C4** — In-flight 4_mesele has Arabic ayahs + hashiye + de-facto mesele chunking → #1, #6 directly relevant NOW.
- **C5** — 8-axis schema + 5 always-on Layer-2 policies must compose; no conflicts.
- **C6** — SourceDescriptor + PipelineConfig don't yet exist as implemented schemas (paper commitments from chunking finding).

**Key Insights:**
- **K1** — Architectural reading (multi-schema routing) is the right reading; literal reading (TC-only triage) is its strict subset (per articulate_simple MQA).
- **K2** — #1 and #6 are ALREADY ROUTED — no decision; inherit.
- **K3** — #2 is REFINE-existing-axis case, not add-new-field. Different decision shape.
- **K4** — #7 ALREADY DISPOSED — orthogonal sister-concept; `passage-typology-aware` strategy literal IS the composition.
- **K5** — Group γ (UseContext) needs ratification; if rejected, #9/#10/#12 go DEFER.
- **K6** — Anti-bloat suggests MOST of 14 should NOT land on TC. Likely 0-2 TC additions; rest distributed or deferred.
- **K7** — PRIORITY filter = what does 4_mesele need NOW (Phase 1).

**Structural Points:**
- **S1** — 7-category routing taxonomy: TranslationConfig / SourceDescriptor / UseContext / PipelineConfig / REFINE-existing-axis / Internal / DEFERRED.
- **S2** — Per-field decision shape: which category does each field land in?
- **S3** — Pre-routed cases (#1, #6, #7) reduce decision count from 14 to 11.
- **S4** — Group α/β/γ Assembly proposed groupings; this inquiry ratifies or refines per field.
- **S5** — Inherited-commitment re-test architecture (RE-TESTED-OK / RE-TESTED-REVISED / INHERITED-WITHOUT-RE-TEST per commitment).

**Foundational Principles:**
- **P1** — Anti-bloat: minimize TranslationConfig surface.
- **P2** — Schema ownership matches data ownership (inherited from chunking finding).
- **P3** — Don't break the chunking finding's split-placement decision (load-bearing prior).
- **P4** — Phase additions: Phase 1 = unblock current work; Phase 2 = composes with existing; Phase 3 = DEFER.

**Meaning-Nodes:**
- **M1 — per-field routing decision** (central operation)
- **M2 — schema home** (TC / SD / UC / PC / REFINE / Internal / DEFER)
- **M3 — decision shape** (ADD-NOW / REFINE / DEFER / REJECT / ALREADY-ROUTED)
- **M4 — load-bearing-for-current-work** (Phase 1 filter)
- **M5 — Group α/β/γ groupings**
- **M6 — pre-routing inheritance** from chunking finding

### SV2 — Anchor-informed understanding

The synthesis problem: given 14 candidates, 7 routing categories, and 3 already-routed cases, produce a per-field decision table that triages by use-case priority + composes with anti-bloat + ratifies-or-refines Group α/β/γ + inherits the chunking finding's pre-routing.

**Meta-Inspection (H4 + H5):**
- **H4 concept names:** "ALREADY-ROUTED-BY-PRIOR" / "REFINE-existing-axis" / "schema home" — structurally grounded distinctions, not loop coinages.
- **H5 motivating examples:** 14 specific fields + 4_mesele specific use case. Per scope check, inquiry IS scoped specifically; not a broader-pattern question.

---

## Phase 2 — Perspective Checking

**Technical / Logical.** Pydantic Literal[] can be deeply nested but user-facing config benefits from flat fields. SourceDescriptor doesn't exist as implemented schema yet (per C6).
→ **A1** — Schema additions to SourceDescriptor are PAPER COMMITMENTS until SourceDescriptor inquiry runs.

**Human / User.** User just settled chunking; their pattern is ONE structural decision per inquiry, not bulk. User's "fields?" phrasing emphasizes FIELD-shape — they want concrete, not architectural. But the chunking precedent shows they ACCEPT split-placement.
→ **A2** — User wants a CONCRETE per-field decision TABLE; not an essay.

**Strategic / Long-term.** TC additions are EXPENSIVE (high maintenance, compose with all existing axes). Other schemas are cheaper.
→ **A3** — TC additions are the EXPENSIVE choice; SourceDescriptor / DEFER are cheaper.

**Risk / Failure.** Adding-and-wrong → migration headache. Deferring-and-needed → easy add-later.
→ **A4** — Asymmetric-failure direction: DEFER under uncertainty; ADD-NOW only when load-bearing.

**Resource / Feasibility.** 14 fields × 2 priors = lots of re-testing.
→ **A5** — Use a decision table format — one row per field, columns for pre-routing-inheritance / Assembly-group / chunking-finding-disposition / cross-axis / 4_mesele-load-bearing / final-decision.

**Definitional / Internal Consistency.** Does architectural reading CONTRADICT user's "fields?" question? No — it PRODUCES the literal answer as a column. The chunking finding's decision framework (P2 schema ownership) is the inherited decision rule.
→ **A6** — The decision framework from the chunking finding IS the inherited decision rule for routing.

**Definitional / Frame-exit Completeness.** Gating predicate test:
- (i) Inherited terms? YES — "schema home" used across 7 distinct categories; "edge-case field" across 14 distinct values; "Group" across α/β/γ.
- Gating FIRES.

Four meta-categories:
1. **Existence Enumeration.** What does "edge-case" refer to project-wide? Could it span beyond 14? Yes — future ones will emerge. But scoped to THESE 14 per scope check. Other-than-14 OUT of scope.
2. **Role Assessment.** Edge-cases beyond 14 → future work; no role.
3. **Verdict Rigor.** "These 14 only" counter-argument: future edge-cases (e.g., translator-attribution) may be related. Why counter fails: inquiry bounds explicitly scope to 14; future cases come in via separate inquiries. HIGH confidence.
4. **Residual.** Frame-exit concern not captured: **the "schema home" framing is 1D**, but the routing is actually **2D**:
   - (a) routing OUTCOME (schema-add / refine-existing-axis / internal / defer)
   - (b) schema HOME (only meaningful when outcome = ADD)
   - REFINE-existing-axis (only #2) and DEFER aren't schemas — they're outcomes. Conflating produces a confused column.
→ **A7** — Routing decision is 2D (outcome × schema-home); not 1D. Refines S1.

**Phase / Calibration-State.** Project is at FRAMEWORK-CLOSURE-stage-PLUS — 8 axes settled; chunking just settled; edge-cases proposed. Phase implies: additions JUSTIFIED, not bulk.
→ **A8** — Project phase signals INCREMENTAL ADDITION; not bulk reorganization.

### SV3 — Multi-perspective understanding

Material shifts:
1. Decision is 2D (outcome × schema-home), not 1D.
2. Most fields will NOT land on TC per anti-bloat + schema-ownership.
3. Pre-routing inheritance reduces decision count from 14 to 11.
4. Phase 1 = what unblocks 4_mesele NOW = ratify pre-routed cases.
5. Group γ (UseContext) needs explicit ratification; rejection means #9/#10/#12 → DEFER.

**Meta-Inspection (H1 + H3):**
- **H1 candidate set:** #1 and #8 are conceptually adjacent (Quranic citation is a kind of embedded language). Consider #8 collapsing into #1 + a policy field. Flag for Ambiguity 7.
- **H3 question framing:** "fields?" presupposes additions. Status-quo-defense variant (KEEP 8, ADD 0) is a real alternative deserving consideration.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: Literal vs architectural reading

**Counter:** Strict literal — answer only "which of 14 should be TC fields?"; ignore other schema homes.

**Why counter fails (structural):** The chunking finding established split-placement. Answering "which to TC" requires answering "which to NOT-TC" — the question is ill-posed without multi-schema routing.

**Confidence:** HIGH.

**Resolution:** Architectural answer (per-field × per-outcome × per-schema-home). Extract literal subset (TC-only column) explicitly. One deliverable serves both readings.

### Ambiguity 2: 2D vs 1D decision shape

**Counter:** Single "schema home" column per field.

**Why counter fails:** REFINE-existing-axis (only #2) and DEFER aren't schema-homes — they're outcomes. Conflating produces confused column with mixed types.

**Confidence:** HIGH.

**Resolution:** 2D per field — outcome ∈ {ADD-now / REFINE-existing-axis / DEFER / REJECT / ALREADY-ROUTED} × schema-home (only meaningful when outcome = ADD-now).

### Ambiguity 3: Group γ (UseContext) ratification

**Counter:** UseContext doesn't exist as implemented schema; introducing a third NEW schema (SourceDescriptor + PipelineConfig + UseContext) all from edge-case work is anti-bloat-tense. DEFER Group γ; members → DEFER individually.

**Why counter has merit:** Three new schemas in one push violates user's incremental-addition pattern (one structural decision per inquiry).

**Confidence:** MED.

**Resolution:** DEFER Group γ as schema commitment. #9 / #10 / #12 → individual DEFER with revival trigger = "when a downstream consumer (renderer, UI, validator) actually distinguishes these modes." UseContext is research-frontier schema, not committed now.

### Ambiguity 4: #2 source_language vs source_culture (A3 modification)

**Counter:** Keep A3 as is; add `source_language_fluency` as new field BESIDE A3 (not split A3).

**Why counter has merit:** Splitting A3 is BREAKING change to settled axis (config_base_source.md prose assumes A3 as is). Adding beside is non-breaking.

**Confidence:** MED-HIGH for "add beside" over "split."

**Resolution:** ADD-now to SourceDescriptor — `source_language_fluency: dict[language_code, fluency_level]` as a NEW SourceDescriptor field (NOT a TC field; NOT an A3 modification). A3 keeps existing meaning. Future inquiry may re-examine A3 if conflation produces concrete problems.

### Ambiguity 5: #4 voice_disambiguation placement

**Counter:** Voice disambiguation is SOURCE PROPERTY (Group α SourceDescriptor) vs USER STRATEGY (TranslationConfig rendering choice).

**Both readings valid.** Group α Assembly put it in SourceDescriptor. But enum (off / implicit-typographic / explicit-attribution / scholarly-apparatus) is RENDERING strategy — sounds like TC.

**Why DEFER wins:** Chunking finding's ChunkingUnit may already cover voice via `attached_to` (hashiye attached_to author). Most concrete voice case (#6 hashiye) is already routed. The lahika / extended-citation case isn't load-bearing for 4_mesele NOW.

**Confidence:** MED.

**Resolution:** DEFER #4 — revival trigger = "when a real translation case needs explicit voice-rendering distinct from hashiye attachment (lahika or extended-citation case)." Pre-routing via #6's ChunkingUnit.attached_to covers Nursi+hashiye currently.

### Ambiguity 6: #11 and #14 — innovation unassigned

**Counter:** Both must be assigned to schema homes NOW.

**Why counter doesn't kill:** Neither is load-bearing for current Nursi work. Anti-bloat + asymmetric-failure favor DEFER.

**Resolution:** DEFER both.
- #11 revival = "when a third translation iteration needs to position vs prior translators (Vahide / Akarsu)."
- #14 revival = "when output rendering reaches apparatus-edition stage with bidirectional RTL Arabic display."

### Ambiguity 7: #8 as sub-case of #1 or peer

**Counter:** #8 is a sub-case of #1 — Quranic citation IS embedded source language with special policy.

**Counter partly right:** Structurally yes; policy-wise different (established translation tradition; numbering convention; sura:ayah attribution format).

**Resolution:** #1 stays parent (already routed via `ChunkingUnit.is_atomic` + `EmbeddedLanguagePolicy` list). #8 becomes a POLICY value within #1's `EmbeddedLanguagePolicy` — `quranic_citation_policy: Literal[...]` is one entry. NOT a separate top-level field. ADD-now to SourceDescriptor as property of the embedded-language declaration for Quranic ayahs specifically.

### SV4 — Clarified understanding

**Clear:**
- Decision is 2D (outcome × schema-home).
- Pre-routed cases (#1, #6, #7) INHERIT with RE-TESTED-OK status.
- Most fields DEFER per anti-bloat + asymmetric-failure.
- Few SourceDescriptor additions where source-property mapping clear.
- TranslationConfig: 0 new fields beyond chunking_strategy.
- Group γ UseContext deferred as schema.

**No longer viable:**
- Bulk addition of all 14 to TranslationConfig.
- UseContext commitment now.
- A3 destructive split.
- #8 as peer to #1.

---

## Phase 4 — Degrees-of-Freedom Reduction

**Variables fixed:**
- 7 routing-outcome categories (ADD-to-TC / ADD-to-SD / ADD-to-UC / ADD-to-PC / REFINE-existing-axis / DEFER / ALREADY-ROUTED).
- Per-field decision shape: each lands in exactly one outcome.
- Anti-bloat principle: DEFER over ADD-now unless load-bearing.

**Options eliminated:**
- Bulk TC addition.
- UseContext schema commitment.
- A3 destructive split.
- #8 as separate top-level field.

**Viable paths (from articulate_simple's 6 considered articulations):**
- Variant 1 (literal): morphed into "TC-only column" of architectural table — 0 additions.
- Variant 2 (architectural): SURVIVES as deliverable shape.
- Variant 3 (Assembly-driven): SURVIVES with Group γ deferred + some Group α members deferred.
- Variant 4 (implementation-readiness): SURVIVES as code output for Phase 1.
- Variant 5 (phased plan): SURVIVES as migration sequence wrapper.
- Variant 6 (anti-bloat-first): SURVIVES as dominant filter.

### SV5 — Constrained understanding

The per-field decision table is the deliverable's core. Net: 0 new TC fields; 4 SourceDescriptor additions (Phase 2); 3 ALREADY-ROUTED (Phase 1 ratify); 7 DEFER (Phase 3 with revival triggers).

| # | Field | Outcome | Schema home | Phase |
|---|---|---|---|---|
| 1 | embedded_source_languages | ALREADY-ROUTED | SourceDescriptor.ChunkingUnit.is_atomic | Phase 1 |
| 2 | source_language_fluency | ADD-now | SourceDescriptor.source_language_fluency | Phase 2 |
| 3 | source_edition | ADD-now (light) | SourceDescriptor.source_edition | Phase 2 |
| 4 | voice_disambiguation | DEFER | — | Phase 3 |
| 5 | relay_translation | DEFER | — | Phase 3 |
| 6 | source_apparatus_handling | ALREADY-ROUTED | SourceDescriptor.ChunkingUnit.attached_to | Phase 1 |
| 7 | passage_typology | ALREADY-DISPOSED (orthogonal) | TranslationConfig.chunking_strategy literal | Phase 1 |
| 8 | quranic_citation_special_status | ADD-now (as policy in #1) | SourceDescriptor.EmbeddedLanguagePolicy | Phase 2 |
| 9 | consumption_mode | DEFER | — | Phase 3 |
| 10 | reading_session_pattern | DEFER | — | Phase 3 |
| 11 | prior_translation_relationship | DEFER | — | Phase 3 |
| 12 | output_finality | DEFER | — | Phase 3 |
| 13 | source_temporal_register | ADD-now (light) | SourceDescriptor.source_temporal_register | Phase 2 |
| 14 | script_direction_handling | DEFER | — | Phase 3 |

**Phase 1 (Phase-1-now-needs):** ratify #1, #6, #7 inheritance. TC = 0 changes beyond chunking_strategy. SourceDescriptor: Nursi-instance declaration per chunking finding.

**Phase 2 (composes-with-existing):** SourceDescriptor adds: #2, #3, #13, plus #8 as policy within #1.

**Phase 3 (deferred):** #4, #5, #9, #10, #11, #12, #14 with revival triggers.

**Net change to TranslationConfig: 0 new fields.** All additions land on SourceDescriptor.

---

## Phase 5 — Conceptual Stabilization

**Accommodation trigger check:**
- Technical: confirmed paper-commitment caveat (A1).
- Human: confirmed concrete-table preference (A2).
- Strategic: confirmed TC-expensive vs others-cheaper (A3).
- Risk: produced DEFER-under-uncertainty direction (A4).
- Resource: produced table-format anchor (A5).
- Definitional/Internal: confirmed framework-inheritance (A6).
- Frame-exit Completeness: produced 2D-decision refinement (A7) — material shift, strengthened.
- Phase/Calibration: produced incremental-addition framing (A8).

Shifts CONVERGED on coherent model. Accommodation trigger does NOT fire.

### SV6 — Stabilized model

**The 14 edge-case candidates resolve into: 3 ALREADY-ROUTED-by-chunking-finding (ratify), 4 ADD-now-to-SourceDescriptor (Phase 2), and 7 DEFER-with-revival-triggers (Phase 3). TranslationConfig gains 0 new fields beyond the chunking finding's `chunking_strategy`. The decision is structurally driven by the chunking finding's split-placement precedent + anti-bloat + asymmetric-failure (DEFER under uncertainty).**

### SV6 vs SV1 delta

SV1 took the question at surface: "decide ADD/REJECT for 14 fields on TranslationConfig."

SV6 reframes: (a) deliverable is 2D per-field routing not 1D add/reject; (b) most fields don't land on TC per split-placement + anti-bloat; (c) 3 cases already settled and inherit from chunking finding; (d) most additions go to SourceDescriptor not TC; (e) Phase 1 / Phase 2 / Phase 3 sequencing honors current use-case priority. **TC gains 0 new fields.** Major structural shift.

---

## Telemetry

- **Perspective saturation:** 8 perspectives applied (Technical / Human / Strategic / Risk / Resource / Definitional-Internal / Definitional-Frame-exit / Phase-Calibration). Material shifts at Frame-exit Completeness; convergence by SV4.
- **Ambiguity resolution ratio:** 7 identified, 7 resolved (3 HIGH + 4 MED-HIGH/MED). 100%.
- **SV delta:** substantial. SV1 → SV6 reframes from literal-TC-triage to 2D-architectural-routing-with-0-TC-additions.
- **Anchor diversity:** 8 A-anchors + 6 constraints + 7 key insights + 7 structural points + 4 principles + 6 meaning-nodes. No single dominant.

### Failure-mode check

- **Status Quo Bias:** chunking finding's split-placement is preserved because schema-ownership argument is structurally sound, not because it's the recent prior. Not triggered.
- **Premature Stabilization:** SV2 → SV3 added 2D-decision refinement; SV3 → SV4 narrowed. Not premature.
- **Anchor Dominance:** many anchors; no single decisive.
- **Perspective Blindness:** 8 perspectives including uncomfortable ones (Frame-exit produced the 2D refinement; Phase/Calibration produced incremental framing). Not triggered.
- **Clean Resolution Trap:** each ambiguity has stated counter + structural why-counter-fails.
- **Self-Reference Blindness:** subject is Comprehenslate schema, not sensemaking itself.

### Verdict

**PROCEED to Decomposition.**

The per-field decision table is the deliverable's core. Decomposition should partition: (a) the table-construction work, (b) the ALREADY-ROUTED ratification (Phase 1), (c) the SourceDescriptor additions (Phase 2), (d) the DEFER revival-trigger specification (Phase 3), (e) the cross-axis-conflict check, (f) the migration sequence wrapper, (g) the inherited-commitment re-test architecture.
