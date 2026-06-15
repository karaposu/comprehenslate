# Branch: Chunk Types vs Mechanisms

## Source Input

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

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** I1
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**Item I1** — literal-statement: *"I think these are bad. Paragraph yes this is good. Sentence yes this is good. Passage. Chapter. Subchapter. These are fundemanral ones I guess. LLM detected. Fixed budget etc doesnt make snese. Bc they are how to determine the chunk, but we are talking about what kind of chunks exist. Lets dive deep into this updated logic"*

The user identifies a category conflation in the chunking finding's `chunking_strategy` enum: some literals (paragraph, sentence) name TYPES of chunks (categorical units that exist in the source); others (LLM-detected, fixed-budget-with-snap) name MECHANISMS for finding chunks (how to determine boundaries). These are two orthogonal axes merged into one field. The user requests a deep-dive into the updated logic.

**MQ1 verdict-axis identified-ambiguities:**
- `refactor-chunking-strategy-into-two-axes`
- `enumerate-chunk-types-only` (delete mechanisms)
- `enumerate-mechanisms-separately`
- `kill-the-bad-literals` (remove without replacing)
- `redesign-strategy-as-2D` (combinatorial)
- `learn-and-extract-pattern` (apply LOOP_DIAGNOSE MC2 as validation)

**MQ3 intent-axis identified-ambiguities:**
- `produce-revised-chunking_strategy-enum-of-types-only`
- `produce-separate-mechanism-axis`
- `produce-the-2-axis-schema-shape`
- `apply-MC2-comparative-pattern-test-as-validation`
- `validate-the-clean-separation-with-Nursi-examples-and-cross-domain-cases`
- `update-the-config_base_source.md-and-chunking-finding-text`

**MQA — surface (irreducible overlap content).** TWO-AXIS-RECOGNITION: the user has identified two axes merged in one field but the downstream pipeline must preserve openness on (1) the full type-enum, (2) the mechanism-enum content, (3) whether mechanism is user-visible or internal, (4) how the new design interacts with the existing `SourceDescriptor.source_chunking_units` (which already separates `ChunkingUnit.name` from `ChunkingUnit.detector` — informative comparative evidence that the type/mechanism split is already implicit in the existing substrate). The remaining literals from the current 8-enum (harmony-tier-aware, passage-typology-aware, hybrid) are not explicitly addressed by the user; by their own logic these are mechanisms; the pipeline tests whether they all migrate to the mechanism axis or have special status.

## Goal

**Deconstruct tuple:**
- **deliverable:** /aMVLwr-style finding with revised chunking schema (type-vs-mechanism separation), per-axis enum content, cross-axis interaction, updated chunking-finding text.
- **kinds:** enum-revision + schema-shape-decision (1 field vs 2 fields vs hierarchy vs internal-mechanism) + cross-axis interaction + SourceDescriptor-integration + maintenance-impact.
- **bounds:** scoped to the `chunking_strategy` enum redesign per user's explicit signal; informed by chunking finding + edge-cases finding + LOOP_DIAGNOSE inquiry + existing 8-axis TC. NOT redesigning split-placement; NOT touching A1-A8.

**MultiDepth WHY-axis identified-purpose-motivation-ambiguities:**
- `clean-the-conceptual-mess`
- `extract-the-LOOP_DIAGNOSE-pattern`
- `framework-completeness-check`
- `practical-application-now`
- `understand-fundamental-categories`
- `validate-intuition-and-see-where-it-leads`

**MQ2 context-need identified-ambiguities:**
- **verdict sub-axis:** `[chunking finding's current 8-literal enum / LOOP_DIAGNOSE MC2 (Comparative-Pattern Test perspective) — directly relevant; this case validates it / existing 8-axis TC as comparative evidence / SourceDescriptor.source_chunking_units with its name/detector split — existing substrate that already separates type from mechanism]`
- **kinds sub-axis:** `[2-axis explicit schema vs type-only with hidden mechanism vs hierarchical types vs SD-integration / impact on the chunking finding's recommended hybrid default (a mechanism, not a type)]`
- **stance sub-axis:** `[mechanism user-visible vs internal-only / fully replace enum vs revise inline / how to handle the implicit-by-logic exclusions (harmony-tier-aware, passage-typology-aware, hybrid)]`

**MQ4 boundary-axis identified-ambiguities (explicit exclusions only):**
- `LLM-detected — NOT-a-chunk-type` (explicit)
- `fixed-budget-with-snap — NOT-a-chunk-type` (explicit, via "etc")

## Considered Articulations

**Item I1** — variant-set from Rephrase:

1. **Type-axis-only redesign.** Clean chunk-type enum (sentence / paragraph / passage / subchapter / chapter / corpus-specific via SD). Delete mechanism literals entirely. Mechanism becomes internal AI-pipeline detail.

2. **Two-axis schema (type + mechanism, both user-visible).** `chunking_type` field + `chunking_mechanism` field on TC. Cross-axis interactions documented.

3. **Type-axis user-visible + mechanism hidden.** Chunk-type on TC; AI picks mechanism internally based on Tier-1 preservation + cost.

4. **Hierarchical types (granularity ladder).** `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]`. Strict nesting hierarchy.

5. **Type-axis with corpus-specific extension via SourceDescriptor.** Canonical types on TC; corpus-types declared per-corpus via SD's existing ChunkingUnit; SD's existing name/detector split provides the type/mechanism separation per declared unit.

6. **Apply LOOP_DIAGNOSE MC2 directly as validation.** Frame this inquiry as MC2's first use; the comparative-pattern test catches the conflation; refactor follows; this inquiry becomes evidence for MC2 promotion.

## Scope Check

**Question covers goal:** YES — with TWO-AXIS-RECOGNITION openness preserved via MQA-surface.

**IN-scope:** `chunking_strategy` enum redesign; type-vs-mechanism separation; cross-axis interaction with SD's ChunkingUnit; chunking finding text update; LOOP_DIAGNOSE MC2 validation.

**OUT-of-scope:** redesigning split-placement; touching A1-A8; redesigning SD or PipelineConfig structure; addressing fields not within the chunking enum.

**Specific-vs-pattern check:** The user names specific literals (paragraph/sentence/passage/chapter/subchapter approved; LLM-detected/fixed-budget rejected). The inquiry addresses BOTH the specific literals AND the broader pattern (type-vs-mechanism conflation as a category error). The motivating WHY-axis (`extract-the-LOOP_DIAGNOSE-pattern`) confirms pattern-level treatment is wanted.

## Synthesis Trigger

This inquiry refines the chunking finding (`devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`). Per the Synthesis Trigger requirement, the resulting finding will include an `## Inherited Commitments Re-test` section.

Priors and their carried commitments:
- `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` — chunking_strategy 8-literal enum (under direct revision); split-placement architecture (preserved); A4-driven defaults (revised per new enum shape); hybrid as operational default (revised — hybrid is a mechanism not a type; new home needed); 3 hard constraints (preserved); asymmetric-failure direction (preserved). The 8-literal enum is the central commitment being revised.
- `devdocs/inquiries/2026-06-14_02-29__loop_diagnose__sd_vs_tc_misrouting/finding.md` — MC2 (Comparative-Pattern Test perspective) is the maintenance candidate this inquiry validates. The chunking finding "survived intact" claim from LOOP_DIAGNOSE is now CHALLENGED — the user found a new conflation issue in chunking_strategy. LOOP_DIAGNOSE's verdict may need revision.

## Relationships

- REFINES: `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/` (the chunking_strategy enum)
- VALIDATES: `devdocs/inquiries/2026-06-14_02-29__loop_diagnose__sd_vs_tc_misrouting/` MC2 (Comparative-Pattern Test perspective) — this inquiry IS the branch-test
- CHALLENGES: LOOP_DIAGNOSE's "chunking survived intact" claim — chunking finding has a type-vs-mechanism conflation that survived its own critique
- RELATED: `/Users/ns/Desktop/projects/comprehenslate/config_base_source.md` (chunking_strategy section needs update)
- RELATED: `/Users/ns/Desktop/projects/comprehenslate/translation_config.py` (schema baseline)
