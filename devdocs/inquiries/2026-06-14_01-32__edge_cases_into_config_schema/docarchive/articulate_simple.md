# Articulate-Simple — Edge-Cases into Config Schema

## User Input

```text
14 edge-case fields written to devdocs/innovation/translation_config_edge_cases.md. Quick map:

  Multi-lingual / multi-layer source — (1) embedded_source_languages (your Arabic-in-Turkish example), (2) split source_language from
  source_culture (an A3-conflation fix), (3) source_edition (which printing/manuscript).

  Voice / authority / textual layer — (4) voice_disambiguation (Nursi's own writing vs. citations vs. hashiye vs. lahika), (5)
  relay_translation (source→intermediate→target chains), (6) source_apparatus_handling (Nursi's hashiye preservation).

  Passage heterogeneity — (7) passage_typology (different passages, different configs in one chapter), (8) quranic_citation_special_status
  (Quranic citation ≠ Persian-couplet embedding).

  Reader mode-of-use — (9) consumption_mode (silent / aloud / dersane / recitation / memorization), (10) reading_session_pattern
  (single-pass vs. progressive-daily vs. reference vs. study-circle).

  Translation-process / output — (11) prior_translation_relationship (honor / extend / diverge from Vahide / Akarsu etc.), (12)
  output_finality (ship-ready vs. editor-draft vs. teaching-draft).

  Source-time — (13) source_temporal_register (Ottoman archaism: preserve / modernize / hybrid).

  Surface — (14) script_direction_handling (RTL Arabic embedded in LTR English target).

how these should change our current config

class TranslationConfig(BaseModel):
      reader_level:      Literal["very_basic", "daily", "conversational", "advanced", "native"]         = "conversational"
      domain_expertise:  Literal["lay", "aware", "educated", "trained", "expert"]                       = "aware"
      source_culture:    Literal["outsider", "acquainted", "familiar", "heritage", "source-native"]     = "acquainted"
      purpose:           Literal["scholarly", "devotional", "casual", "language-learning", "performance"] = "casual"
      source_fidelity:   Literal["foreignized-max", "foreignized", "balanced", "lightly-domesticated"]  = "balanced"
      form_preservation: Literal["off", "minimal", "light", "standard", "maximum"]                      = "standard"
      scaffolding:       Literal["off", "minimal", "standard", "rich", "scholarly"]                     = "minimal"
      analysis_depth:    Literal["none", "surface", "standard", "deep", "scholarly"]                    = "none"

fields?
```

---

## Itemize

- **count:** 1
- **items:**
  - `I1` — "How should the 14 edge-case candidates from translation_config_edge_cases.md change the current 8-field TranslationConfig (as fields)?"

**Reasoning.** The statement quotes the 14 edge-cases as input + the current 8-field schema as input + asks "how these should change our current config fields?" One work item: produce the schema-modification answer. The 14 edge-cases are *content the answer must process*, not 14 independent work items.

---

## Item I1 — Articulation

**Item text.** "How should the 14 edge-case candidates from translation_config_edge_cases.md change the current 8-field TranslationConfig (as fields)?"

### Stage 2 — Meta-questions + MQA

**MQ1 (verdict-axis).** *What is the user asking for?*

Identified-ambiguities-list:
- `concrete-schema-decision` — a definitive ADD-NOW / DEFER / REJECT triage per field
- `architectural-routing` — for each of the 14, which schema is its home (TranslationConfig / SourceDescriptor / UseContext / PipelineConfig / internal / deferred)
- `field-shape-specification` — for each field that DOES land on TranslationConfig, what its Literal[...] enum looks like
- `deferred-vs-now-decision` — which fields are MUST-now (load-bearing for current Nursi work), which COULD-defer, which DEFERRED-out-of-scope
- `prioritized-incremental-update` — staged migration sequence (Phase 1 / Phase 2 / Phase 3)
- `defense-of-status-quo` — explicit argument for KEEPING the 8 fields and NOT adding any of the 14 (rejection of the question's premise)

**MQ2 (context-need axis).** *What context does the response need that isn't in the statement?*

Identified-ambiguities-list:
- **verdict sub-axis:** `[the edge-cases innovation output (with Assembly check Group α/β/γ — source-descriptor / passage-overrides / use-context — already proposed) / the just-completed chunking deep-dive finding (which committed split-placement architecture: SourceDescriptor + PipelineConfig + TranslationConfig.chunking_strategy; ALREADY routed edge-case #1 → ChunkingUnit.is_atomic and #6 → ChunkingUnit.attached_to) / the existing 8-axis config_base_source.md spec / the user's anti-bloat constraint as session-level filter / the in-flight 4_mesele translation (which fields would unblock it?)]`
- **kinds sub-axis:** `[the question reads "fields" — literally pydantic fields on TranslationConfig. BUT the just-completed chunking finding established that "field on TranslationConfig" is NOT the only option (split-placement was the chosen architecture). So the question spans: literal-reading (which 14 → TranslationConfig fields, which not?) / architectural-reading (per-field schema-home assignment across all schemas) / hybrid-reading (TranslationConfig changes named explicitly; non-TC changes noted as related architectural decisions)]`
- **stance sub-axis:** `[is the user committed to single-schema extension (their literal phrasing), or open to the split-placement precedent from chunking? / is the user asking for complete-now or phased? / should the answer honor anti-bloat (limit additions to load-bearing) or comprehensiveness (route all 14)?]`

**MQ3 (intent-axis, WHAT).** *What is the user trying to accomplish?*

Identified-ambiguities-list:
- `decide-which-edge-cases-to-add` — triage: ADD-NOW / DEFER / REJECT per field
- `route-each-edge-case-to-its-schema-home` — routing table mapping each of the 14 to a target schema
- `update-the-pydantic-class` — produce concrete Python code showing the new TranslationConfig (and sketches of other schemas if needed)
- `plan-the-migration-sequence` — staged plan: what changes first, what depends on what
- `verify-no-conflicts-with-existing-axes` — check each edge-case for conflicts with A1-A8 + chunking work
- `unblock-current-translation-work` — identify which fields would directly help the in-flight 4_mesele translation

**MQ4 (boundary-axis).** *What is the user explicitly excluding?*

**explicit-empty.**

No exclusion language in the statement. Substrate-level implicit constraints (anti-bloat; the chunking finding's split-placement commitment; mesele-level baseline) are warm-context, not statement-level exclusions; per Edge 2 asymmetric-failure direction, do not synthesize them into MQ4.

**MQA — reconcile (joint-axis content).**

MQ1's `architectural-routing`, MQ2's stance sub-axis, and MQ3's `route-each-edge-case-to-its-schema-home` converge on a **SCHEMA-SCOPE-OF-DELIVERABLE** axis: at what architectural level does the answer land?

- **Literal reading** of the user's question (`fields?`): the answer commits each edge-case to either TranslationConfig (ADD as Literal[...]) or NOT (omit/defer). The deliverable's schema-scope is TranslationConfig-only.
- **Architectural reading** (informed by the just-completed chunking finding's split-placement decision): the answer routes each edge-case to its appropriate schema home (TranslationConfig / SourceDescriptor / UseContext / PipelineConfig / internal / deferred). The deliverable's schema-scope is multi-schema.

The literal answer is a strict subset of the architectural answer — "which of these 14 should be TranslationConfig fields" is one column of the broader routing table. The downstream pipeline should produce the architectural reading and explicitly extract the literal subset; this preserves the user's "fields" framing while honoring the chunking-precedent's split-placement commitment.

### Stage 3 — Deconstruct + MultiDepth

**Deconstruct.** Tuple = (deliverable, kinds, bounds):
- **deliverable:** a /aMVLwr finding compiled from 7 discipline artifacts. The finding's central output is a per-field routing table (14 rows × decision columns) + the resulting updated schema(s) + migration sequence.
- **kinds:** `[routing-decision (per-field schema-home) + field-shape-spec (Literal[...] enums where applicable) + migration-sequence (staged plan with phases) + cross-axis-conflict-check (verify against A1-A8 and chunking) + anti-bloat-defense (justify omissions and deferrals)]`
- **bounds:** scoped to the 14 edge-case candidates + the existing 8-axis TranslationConfig + the chunking finding's split-placement architectural commitment. NOT generic schema-design literature; NOT extending beyond the 14 candidates to new edge-cases.

**Late-split check:** single deliverable with multi-kind internal structure; keep-together correct. NO late-split.

**MultiDepth.**

- **literal-statement:** *(verbatim from User Input — the 14-item map + 8-field schema + "fields?" closer, preserved without contamination)*

- **identified-purpose-motivation-ambiguities (WHY-axis):**
  - `preparing-for-implementation` — about to update translation_config.py; needs to know what to write
  - `framework-completeness` — just settled chunking; this is the natural next step to close out the schema cascade
  - `scope-anxiety` — worried the 14 edge-cases would bloat TranslationConfig past usability; wants principled triage
  - `architectural-consistency` — wants the schema to settle into a stable shape before further work
  - `unblock-current-work` — the in-flight 4_mesele translation likely needs at least #1 (embedded Arabic ayahs); the question implicitly asks which fields would actually help RIGHT NOW
  - `synthesis-completeness` — closing the loop on the edge-case innovation pass; converting candidates to settled decisions
  - `learning-from-prior-pattern` — the chunking finding modeled split-placement; user may be checking whether the same pattern applies uniformly to the 14 edge-cases

### Stage 4 — Rephrase (considered articulations)

Composition sources read:
- Deconstruct deliverable-shape: per-field routing table + updated schema(s) + migration sequence; multi-kind; scoped to 14 + existing 8 + chunking finding architecture.
- Aggregated identified-ambiguities: MQ1 + MQ2 + MQ3 + MultiDepth WHY.
- MQ4 NOT-list: explicit-empty.
- Substrate: warm — Comprehenslate; 8-axis TranslationConfig; edge-cases innovation (with Group α/β/γ Assembly); chunking finding's split-placement (with ChunkingUnit fields already routing #1 + #6); Nursi corpus; anti-bloat preference.

**Considered articulations:**

1. **Strict literal reading — TranslationConfig-only triage.** For each of the 14, decide: ADD to TranslationConfig as a Literal[...] field / REJECT (don't add). Output: an updated TranslationConfig with N additional fields. Honors the user's literal "fields?" phrasing; ignores split-placement precedent.

2. **Architectural-routing per the chunking pattern.** For each of the 14, route to its schema home (TranslationConfig / SourceDescriptor / UseContext / PipelineConfig / internal / deferred). Output: a per-field routing table + updated schemas for each affected home. Honors the chunking finding's split-placement architectural precedent; produces a broader answer than the literal question asks.

3. **Edge-case-innovation-Assembly-grouping-driven.** The edge-case innovation's Assembly check already grouped the 14 into Group α (SourceDescriptor: #1, #2, #3, #4, #6, #8, #13) / Group β (passage-overrides on strategy: #7) / Group γ (UseContext: #9, #10, #12) — with #5, #11, #14 unassigned in that assembly. Adopt that grouping directly; ratify or refine per-field. Output: schemas per the Assembly check + a finding that ratifies/refines the Assembly decision.

4. **Implementation-readiness brief.** Produce concrete Python code: updated TranslationConfig + sketches of SourceDescriptor + UseContext + PipelineConfig with field signatures + defaults + Literal enums where applicable. Output: a code-level decision the user can paste into translation_config.py and start using.

5. **Triage-and-sequence (phased plan).** Stage the additions: Phase 1 = load-bearing for current Nursi work (likely #1 for ayahs in 4_mesele); Phase 2 = composes with existing axes (e.g., #2 A3-split, #6 hashiye, #7 passage_typology); Phase 3 = deferred until use-case emerges. Output: a phased migration plan with explicit revival gates.

6. **Anti-bloat-first triage.** Filter the 14 against the user's anti-bloat constraint: keep only fields unambiguously load-bearing; defer or reject everything else. Output: a minimal-addition update (likely 2-4 fields added; 10-12 deferred with explicit revival triggers).

Composition-bound check per variant:
- Preserve deliverable shape (per-field routing + updated schema(s) + migration sequence): ✓ all six.
- Span an identified ambiguity dimension: ✓ each maps to at least one MQ-identified ambiguity (1→MQ1 literal-reading; 2→MQ1 architectural-routing; 3→MQ2 verdict sub-axis Assembly-prior; 4→MQ3 update-pydantic-class; 5→MQ3 plan-migration-sequence + WHY unblock-current-work; 6→MQ2 stance sub-axis anti-bloat).
- Exclude MQ4 NOT-list vocab: ✓ trivially (explicit-empty).
- Stay within substrate: ✓ all six anchored in Comprehenslate + edge-cases + chunking finding.

---

## LAYER 1 Self-Check (single LIGHT pass)

| Mode | Signature | Fire? |
|---|---|---|
| 1 — Premature Itemize split | per-item bundles can't be emitted cleanly without cross-item interpretation | NO — count = 1; coherent |
| 2 — Late-detected multi-item case | Deconstruct tuple shows multi-tuple internal structure | NO — single-deliverable multi-kind; keep-together correct |
| 3 — MQ extension violates bounded-extensibility | emergent fifth-axis content | NO — only MQ1-MQ4 fired |
| 4 — Per-operation firing missed | missing field where one is required | NO — all operations emitted |
| 5 — MQ2 missing preparation content | absence of verdict / kinds / stance | NO — all three sub-axes present |
| 6 — MQ2 missing kinds-axis or stance-axis | ambiguities present but specific axis absent | NO — both present |
| 7 — 2-shape violation | commitment-shaped content at a 2-shape position | NO — all MQs identified-ambiguities-list or explicit-empty; MultiDepth same |
| 8 — AMBIGUITY-NATURE conflation | WHY content at MQ3 or WHAT content at MultiDepth | NO — MQ3 action-endpoints (decide/route/update/plan/verify/unblock); MultiDepth motivation chains (preparing/completeness/scope-anxiety/consistency/unblock/synthesis/learning) |
| 9 — Considered-articulations drift | composition-bound violation | NO — all 6 variants pass all 4 bounds |

**Zero fires.** Friction: LOW (substrate rich; question structurally clear after warm-context unpacking).

---

## Self-Assessment Verdict

**HIGH-PROCEED**
