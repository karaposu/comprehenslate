# Articulate-Simple — Chunk Types vs Mechanisms

## User Input

```text
I think these are bad 

Paragraph yes  this is good
Sentence yes this is good
Passage
Chapter
Subchapter


These are fundemanral ones i guess

Llm detected 
Fixed budget etc doesnt make snese

Bc they are how to determine the chunk, but we are talking about what kind of chunks exist

Lets dive deep into this updated logic
```

---

## Itemize

- **count:** 1
- **items:**
  - `I1` — "The current `chunking_strategy` enum mixes two conceptual axes — TYPES of chunks (sentence, paragraph, passage, subchapter, chapter) and MECHANISMS for finding chunks (LLM-detected, fixed-budget-with-snap, ...). Dive deep into this updated logic to revise the schema."

**Reasoning.** The statement has multiple facets (judgment of current enum; approval of types; rejection of mechanisms; diagnosis of the conflation; action request) but they form ONE work item: revise the chunking schema based on the type-vs-mechanism distinction.

---

## Item I1 — Articulation

### Stage 2 — Meta-questions + MQA

**MQ1 (verdict-axis).** *What is the user asking for?*

Identified-ambiguities-list:
- `refactor-chunking-strategy-into-two-axes` — split the single enum into chunk-type + chunking-mechanism
- `enumerate-chunk-types-only` — focus on TYPE axis only; produce a clean enum of fundamental chunk units
- `enumerate-mechanisms-separately` — define mechanism axis with the user-rejected literals + harmony-aware variants
- `kill-the-bad-literals` — remove LLM-detected / fixed-budget-with-snap entirely (treat them as implementation)
- `redesign-strategy-as-2D` — combinatorial (type × mechanism) config space
- `learn-and-extract-pattern` — apply the LOOP_DIAGNOSE just-proposed MC2 (Comparative-Pattern Test) to this case as validation

**MQ2 (context-need axis).** *What context does the response need?*

Identified-ambiguities-list:
- **verdict sub-axis:** `[the chunking finding's current 8-literal enum (source-structural-unit / paragraph / sentence / harmony-tier-aware / passage-typology-aware / LLM-detected / fixed-budget-with-snap / hybrid) / the LOOP_DIAGNOSE inquiry's MC2 (Comparative-Pattern Test perspective) — directly relevant; this case validates it / the 8-axis TranslationConfig as comparative evidence (none of A1-A8 mix type-vs-mechanism axes within one field) / SourceDescriptor.source_chunking_units which already declares corpus-specific types with detectors (those detectors ARE mechanisms — separation already implicit there)]`
- **kinds sub-axis:** `[2-axis explicit schema (type field + mechanism field) vs type-only with hidden mechanism vs hierarchical types (nesting-level enum) / does the new design touch SourceDescriptor.source_chunking_units which already separates declaration (types via ChunkingUnit.name) from detector (mechanism via ChunkingUnit.detector)? / corpus-agnostic types (sentence/paragraph) vs corpus-specific (mesele/ayah/sloka) integration]`
- **stance sub-axis:** `[mechanism is user-visible vs internal-only / chunking-strategy enum is fully replaced vs revised inline / impact on the chunking finding's recommended hybrid default (which is a mechanism, not a type)]`

**MQ3 (intent-axis, WHAT).** *What is the user trying to accomplish?*

Identified-ambiguities-list:
- `produce-revised-chunking_strategy-enum-of-types-only`
- `produce-separate-mechanism-axis`
- `produce-the-2-axis-schema-shape`
- `apply-MC2-comparative-pattern-test-as-validation-of-the-LOOP_DIAGNOSE-maintenance-candidate`
- `validate-the-clean-separation-with-Nursi-examples-and-cross-domain-cases`
- `update-the-config_base_source.md-and-chunking-finding-text`

**MQ4 (boundary-axis).** *What is the user explicitly excluding?*

The user explicitly excludes:
- `LLM-detected — not a chunk-type` (verbatim: "LLM detected ... doesn't make sense ... they are how to determine the chunk")
- `fixed-budget — not a chunk-type` (verbatim: "Fixed budget etc doesn't make sense")

The "etc" is load-bearing — by the user's own logic the other mechanism-shaped literals (`harmony-tier-aware`, `passage-typology-aware`, `hybrid`) are also implicit exclusions from the type axis. Per Edge 2 asymmetric-failure direction (route ambiguous exclusions to BOTH MQ3 and MQ4), these implicit-by-logic exclusions are noted here but the explicit MQ4 list contains only the user's named ones.

**Identified-ambiguities-list:**
- `LLM-detected — NOT-a-chunk-type` (explicit)
- `fixed-budget-with-snap — NOT-a-chunk-type` (explicit; via "etc")

**MQA — surface (irreducible overlap content).**

The user explicitly names paragraph + sentence + passage + chapter + subchapter as "fundamental" TYPES. They explicitly reject LLM-detected + fixed-budget as MECHANISMS (named via "etc"). The remaining literals (harmony-tier-aware, passage-typology-aware, hybrid) from the current 8-literal enum are not addressed; by the user's own logic they are mechanisms but the user didn't name them explicitly.

The joint axis is **TWO-AXIS-RECOGNITION** — the user has identified that two different conceptual axes were merged. The downstream pipeline must preserve openness on:
1. The full type-enum (user-named + corpus-specific candidates like mesele/ayah/sloka from SourceDescriptor)
2. The mechanism-enum (user-rejected literals + harmony-tier-aware + LLM-based variants + hybrid)
3. Whether mechanism is user-visible or internal
4. How the new design interacts with SourceDescriptor.source_chunking_units (which already separates types from detectors in its existing shape — `ChunkingUnit.name` + `ChunkingUnit.detector`)

This MQA surface should NOT collapse to "the answer is 2-axis schema" or "the answer is type-only" — both are viable per the considered articulations; the pipeline adjudicates.

### Stage 3 — Deconstruct + MultiDepth

**Deconstruct.** Tuple = (deliverable, kinds, bounds):
- **deliverable:** /aMVLwr-style finding with revised chunking schema (type-vs-mechanism separation), per-axis enum, cross-axis interaction, updated chunking-finding text.
- **kinds:** `[enum-revision (chunk-type enum + mechanism enum or merged-with-rationale) + schema-shape-decision (1 field vs 2 fields vs hierarchy vs internal-mechanism) + cross-axis interaction (some types might constrain which mechanisms apply; some mechanisms might constrain producible types) + SourceDescriptor-integration (the existing ChunkingUnit.name/detector split is informative comparative evidence) + maintenance-impact (chunking finding update; LOOP_DIAGNOSE MC2 validation)]`
- **bounds:** scoped to the chunking_strategy enum redesign per user's signal; informed by chunking finding + edge-cases finding + LOOP_DIAGNOSE inquiry + existing 8-axis TC. NOT redesigning split-placement; NOT touching A1-A8.

**Late-split check:** single deliverable with multi-kind structure; keep-together correct. NO late-split.

**MultiDepth.**

- **literal-statement:** *(verbatim from User Input above — preserved without contamination, including typos "fundemanral" / "Llm" / "snese")*

- **identified-purpose-motivation-ambiguities (WHY-axis):**
  - `clean-the-conceptual-mess` — recognizing the conflation as a category error; wants conceptual cleanness
  - `extract-the-LOOP_DIAGNOSE-pattern` — having just diagnosed facts-vs-strategies conflation, recognizing type-vs-mechanism as the same pattern shape; wants to apply the learning
  - `framework-completeness-check` — testing whether the chunking finding survives detailed scrutiny; LOOP_DIAGNOSE said chunking "survived intact" but the user found a new issue
  - `practical-application-now` — needs a workable schema for `translation_config.py`
  - `understand-fundamental-categories` — "fundamental ones I guess" — wants to settle what the basic chunk types actually are
  - `validate-intuition-and-see-where-it-leads` — reasoning aloud ("I guess" hedge); wants confirmation the type-vs-mechanism distinction holds + downstream consequences

### Stage 4 — Rephrase (considered articulations)

Composition sources:
1. Deconstruct deliverable-shape: revised schema with type-axis cleanly separated from mechanism-axis; cross-axis interactions; finding-text update.
2. Aggregated identified-ambiguities: MQ1 + MQ2 + MQ3 + MultiDepth WHY-axis.
3. MQ4 NOT-list: LLM-detected + fixed-budget excluded from chunk-type axis.
4. Substrate: warm — chunking finding's 8-literal enum; LOOP_DIAGNOSE's MC2; existing 8-axis TC; SourceDescriptor.source_chunking_units with its existing name/detector split.

**Considered articulations:**

1. **Type-axis-only redesign (delete mechanism literals).** Produce a clean chunk-type enum (sentence / paragraph / passage / subchapter / chapter / corpus-specific via SourceDescriptor). DELETE mechanism literals entirely. Treat HOW to find chunks as internal AI-pipeline detail. Output: simpler 1-axis enum on TC; mechanism implicit.

2. **Two-axis schema (type + mechanism, both user-visible).** Make BOTH explicit: `chunking_type: Literal[...]` (sentence/paragraph/passage/subchapter/chapter) + `chunking_mechanism: Literal["structural", "llm-detected", "harmony-aware", "fixed-budget-with-snap", "hybrid"]`. User picks both. Cross-axis interactions documented. Output: 2 fields on TC.

3. **Type-axis user-visible + mechanism hidden.** Expose chunk-type as user-config; treat mechanism as internal (AI picks cheapest mechanism that produces the requested type with Tier-1 preservation). Output: 1 field on TC; mechanism is implementation choice.

4. **Hierarchical types (nesting-level structure).** Recognize that chapter > subchapter > passage > paragraph > sentence forms a strict nesting hierarchy. Single field naming the granularity level: `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]`. Output: 1 field; enum is a granularity ladder.

5. **Type-axis with corpus-specific extension via SourceDescriptor.** TC chunk-type enum includes canonical types (sentence/paragraph/passage/...); corpus-specific types (mesele/ayah/sloka) declared per-corpus via SourceDescriptor.source_chunking_units; TC enum's `source-structural-unit` resolves to the corpus's top-level declared unit. Output: clean separation TC-canonical-types vs SD-corpus-types; existing SD `ChunkingUnit.detector` field absorbs the mechanism question per unit.

6. **Apply LOOP_DIAGNOSE MC2 directly as validation.** Frame the inquiry as the FIRST USE of the Comparative-Pattern Test perspective (the maintenance candidate just proposed by LOOP_DIAGNOSE). Run the test: A1-A8 don't conflate axes; current chunking_strategy DOES; the test catches the conflation; refactor follows. Output: meta-validation of MC2 + refactored schema; this inquiry becomes evidence for MC2's branch-test promotion.

**Composition-bound check:**
- All 6 preserve deliverable shape (revised schema + finding-text update). ✓
- All 6 span identified ambiguities. ✓
- All 6 respect MQ4 NOT-list (LLM-detected + fixed-budget not in type axis). ✓
- All 6 stay within warm substrate. ✓

---

## LAYER 1 Self-Check (single LIGHT pass)

| Mode | Fire? |
|---|---|
| 1 — Premature Itemize split | NO |
| 2 — Late-detected multi-item | NO |
| 3 — MQ extension violates bounded-extensibility | NO |
| 4 — Per-operation firing missed | NO |
| 5 — MQ2 missing preparation content | NO (verdict + kinds + stance all present) |
| 6 — MQ2 missing kinds/stance | NO |
| 7 — 2-shape violation | NO |
| 8 — AMBIGUITY-NATURE conflation | NO (MQ3 has action-endpoints; MultiDepth has motivation chains) |
| 9 — Considered-articulations drift | NO |

Zero fires. Friction: LOW (substrate rich; conflation pattern is clear; LOOP_DIAGNOSE precedent provides analytic frame).

---

## Self-Assessment Verdict

**HIGH-PROCEED**
