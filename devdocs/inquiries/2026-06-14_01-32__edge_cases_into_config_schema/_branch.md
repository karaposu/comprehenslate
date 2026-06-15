# Branch: edge_cases_into_config_schema

## Source Input

The user's raw request, preserved verbatim. Also lives in `articulate_simple.md`'s `## User Input` section; both copies are authoritative for transcription audit.

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

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** I1
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**Item I1** — literal-statement: *"How should the 14 edge-case candidates from `translation_config_edge_cases.md` change the current 8-field `TranslationConfig` (as fields)?"*

**MQ1 verdict-axis identified-ambiguities (what kinds of asks the statement carries):**
- `concrete-schema-decision` — definitive ADD-NOW / DEFER / REJECT triage per field.
- `architectural-routing` — for each of the 14, which schema is its home (TranslationConfig / SourceDescriptor / UseContext / PipelineConfig / internal / deferred).
- `field-shape-specification` — for fields that land on TranslationConfig, what the Literal[...] enum looks like.
- `deferred-vs-now-decision` — which fields are MUST-now (load-bearing for current Nursi work), COULD-defer, DEFERRED.
- `prioritized-incremental-update` — staged migration sequence (Phase 1 / Phase 2 / Phase 3).
- `defense-of-status-quo` — explicit argument for KEEPING the 8 fields and NOT adding any of the 14.

**MQ3 intent-axis (WHAT) identified-ambiguities (what action-endpoints are plausible):**
- `decide-which-edge-cases-to-add` — produce a triage.
- `route-each-edge-case-to-its-schema-home` — produce a routing table per field.
- `update-the-pydantic-class` — produce concrete Python code.
- `plan-the-migration-sequence` — staged migration plan.
- `verify-no-conflicts-with-existing-axes` — check against A1-A8 + chunking commitments.
- `unblock-current-translation-work` — identify which fields would unblock the in-flight 4_mesele translation.

**MQA — reconcile (joint-axis content).** MQ1's `architectural-routing` + MQ2's stance sub-axis + MQ3's `route-each-edge-case-to-its-schema-home` converge on a **SCHEMA-SCOPE-OF-DELIVERABLE** axis. **Literal reading** commits each edge-case to TranslationConfig (ADD) or NOT (omit). **Architectural reading** (informed by the just-completed chunking finding's split-placement decision) routes each edge-case to its appropriate schema home across multiple schemas. The literal answer is a strict subset of the architectural one. The downstream pipeline should produce the architectural reading and explicitly extract the literal subset.

## Goal

**Deconstruct tuple:**
- **deliverable:** /aMVLwr finding compiled from 7 discipline artifacts. Central output: per-field routing table (14 rows × decision columns) + resulting updated schema(s) + migration sequence.
- **kinds:** routing-decision (per-field schema-home) + field-shape-spec (Literal[...] enums where applicable) + migration-sequence (staged plan) + cross-axis-conflict-check (verify against A1-A8 + chunking) + anti-bloat-defense (justify omissions and deferrals).
- **bounds:** scoped to the 14 edge-case candidates + existing 8-axis TranslationConfig + the chunking finding's split-placement architectural commitment. NOT generic schema-design literature; NOT extending beyond the 14 candidates.

**MultiDepth WHY-axis identified-purpose-motivation-ambiguities (what motivations a good answer might serve):**
- `preparing-for-implementation` — about to update `translation_config.py`; needs to know what to write.
- `framework-completeness` — chunking just settled; this is the natural next step in the schema cascade.
- `scope-anxiety` — worried that adding 14 fields would bloat TranslationConfig past usability; wants principled triage.
- `architectural-consistency` — wants the schema to settle into a stable shape before further work.
- `unblock-current-work` — the in-flight 4_mesele translation has Arabic ayahs (edge-case #1); the question implicitly asks which fields would help RIGHT NOW.
- `synthesis-completeness` — closing the loop on the edge-case innovation; converting candidates to settled decisions.
- `learning-from-prior-pattern` — checking whether the chunking finding's split-placement pattern applies uniformly to the 14.

**MQ2 context-need axis identified-ambiguities (what context downstream consumers need that isn't in the raw input):**
- **verdict sub-axis:** `[the edge-cases innovation output with Assembly check Group α/β/γ already proposed / the just-completed chunking deep-dive finding which committed split-placement and ALREADY routed #1 → ChunkingUnit.is_atomic and #6 → ChunkingUnit.attached_to / the existing 8-axis config_base_source.md spec / the user's anti-bloat constraint / the in-flight 4_mesele translation]`
- **kinds sub-axis:** `[literal-reading (fields-on-TranslationConfig only) / architectural-reading (per-field schema-home across multiple schemas) / hybrid-reading (TC changes explicit; non-TC changes noted)]`
- **stance sub-axis:** `[committed to single-schema extension vs open to split-placement / complete-now vs phased / anti-bloat-limit vs comprehensiveness]`

**MQ4 boundary-axis identified-ambiguities (negative spec; what would explicitly fail):** explicit-empty. No statement-level exclusions.

## Considered Articulations

**Item I1** — variant-set from Rephrase:

1. **Strict literal reading — TranslationConfig-only triage.** For each of the 14, ADD to TranslationConfig as Literal[...] / REJECT. Output: updated TranslationConfig with N additional fields. Honors the literal "fields?" phrasing.

2. **Architectural-routing per the chunking pattern.** For each of the 14, route to its schema home (TranslationConfig / SourceDescriptor / UseContext / PipelineConfig / internal / deferred). Output: per-field routing table + updated schemas. Honors split-placement precedent.

3. **Edge-case-innovation-Assembly-grouping-driven.** The Assembly check already grouped: Group α (SourceDescriptor: #1, #2, #3, #4, #6, #8, #13) / Group β (passage-overrides on strategy: #7) / Group γ (UseContext: #9, #10, #12). Adopt directly; ratify or refine per-field. Output: schemas per Assembly + ratifying finding.

4. **Implementation-readiness brief.** Produce concrete Python code: updated TranslationConfig + sketches of SourceDescriptor + UseContext + PipelineConfig with field signatures + defaults + Literal enums. Output: code-level decision the user can paste.

5. **Triage-and-sequence (phased plan).** Phase 1 = load-bearing for current Nursi work (likely #1 for ayahs); Phase 2 = composes with existing axes (e.g., #2 A3-split, #6 hashiye, #7 passage_typology); Phase 3 = deferred until use-case emerges. Output: phased migration plan with explicit gates.

6. **Anti-bloat-first triage.** Filter the 14 against anti-bloat; keep only unambiguously load-bearing; defer or reject the rest. Output: minimal-addition update (likely 2-4 fields) + 10-12 deferred with revival triggers.

## Scope Check

**Question covers goal:** YES — with the SCHEMA-SCOPE-OF-DELIVERABLE openness (literal vs architectural reading) preserved by MQA's reconcile.

**IN-scope (from Deconstruct bounds):** the 14 edge-case candidates; the existing 8-axis TranslationConfig; the chunking finding's split-placement architectural commitment; cross-axis conflict checks against A1-A8 and chunking; anti-bloat triage.

**OUT-of-scope:** generic schema-design literature; extending beyond the 14 candidates to new edge-cases; re-opening the chunking finding's split-placement decision (it's a settled prior the synthesis inherits).

**Specific-vs-pattern check:** The question names "the 14 edge-cases" specifically. The inquiry addresses THESE 14 SPECIFICALLY — not the broader pattern of all possible TranslationConfig extensions. The question is scoped to a specific set of candidates with specific names.

## Synthesis Trigger

This inquiry consumes two prior inquiry outputs as inputs and rolls them up into a settled per-field routing + updated schema:

- `devdocs/innovation/translation_config_edge_cases.md` — commits to 14 edge-case candidates with their motivating context (Said Nursi corpus phenomena like embedded Arabic ayahs, hashiye, passage typology variance), each as a proposed pydantic field. The Assembly check at the end of that innovation pass proposed Group α / β / γ as the architectural-routing direction.

- `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` — commits to a three-operation chunking category, split placement across `SourceDescriptor` + `PipelineConfig` + `TranslationConfig`, ALREADY routes edge-case #1 (`embedded_source_languages`) into `ChunkingUnit.is_atomic` and edge-case #6 (`source_apparatus_handling`) into `ChunkingUnit.attached_to`, and treats edge-case #7 (`passage_typology`) as orthogonal sister-concept to chunking. Inherits Group α/β/γ pattern direction from the edge-cases innovation.

Each prior carries commitments this inquiry will inherit. CONCLUDE will require the finding to include an `## Inherited Commitments Re-test` section that names each commitment and either re-tests it with cited evidence or explicitly flags it as inherited-without-re-test with a reason. The pipeline's Sensemaking + Critique phases must actually do the re-testing of:

- The 14 edge-case candidates (each proposed as a field by the innovation; this inquiry decides ADD-NOW / DEFER / REJECT per field).
- The Group α/β/γ Assembly direction (does it ratify, refine, or supersede?).
- The chunking finding's split-placement decision (does it extend uniformly to the 14, or do some edge-cases break the pattern?).
- The chunking finding's specific routing of #1 + #6 into ChunkingUnit fields (this inquiry inherits without re-test if confirmed, or re-tests if any conflict surfaces).
- The chunking finding's #7-as-orthogonal-sister-concept disposition (this inquiry inherits or refines).
