# Branch: schemas_rationale_and_policy_list

## Source Input

```text
explain why /Users/ns/Desktop/projects/comprehenslate/schemas.py makes a lot more sense. and also what other scenarios , policies like NonMainLangPartsPolicy exists? give me list of them
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/articulate_simple.md`
- **Itemize count:** 2
- **Per-item identifiers:** Item 1 (schemas.py rationale explanation); Item 2 (NonMainLangPartsPolicy-like policy list)
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

### Item 1 — schemas.py rationale explanation

**Literal statement:** *explain why /Users/ns/Desktop/projects/comprehenslate/schemas.py makes a lot more sense*

**Kinds of ask the statement carries (MQ1 verdict-axis ambiguities):**
- *compared-against-what* — measured against the four-schema design proposed earlier in session (TC + SD + EmbeddedLanguageProfile + PC), or against the original chunking finding's split-placement architecture, or against the 8-literal `chunking_strategy` enum proposal, or against an implicit baseline
- *type-of-rationale* — architectural (fewer schemas / cleaner separation) vs domain-fit (matches Nursi translation reality) vs anti-bloat (simpler) vs LLM-capability (the LLM doesn't need source-language declarations) vs honest-categorization (each remaining class carries genuinely distinct kinds of facts)
- *depth-of-explanation* — short paragraph vs full essay vs annotated-code walkthrough vs comparison table

**Action-endpoints the statement could be targeting (MQ3 intent-axis ambiguities):**
- achieve-design-clarity (write the rationale down for future use)
- validate-the-simplification (get an independent read confirming the schema collapse was sound)
- surface-residual-structural-issues (find anything the simplification did not resolve)

### Item 2 — NonMainLangPartsPolicy-like policy list

**Literal statement:** *what other scenarios, policies like NonMainLangPartsPolicy exists? give me list of them*

**Kinds of ask the statement carries (MQ1 verdict-axis ambiguities):**
- *like-in-what-way* — structurally-like (same Literal[] enum shape governing a recurring authorial edge-case), domain-like (same kind of multi-language source-text situation), functionally-like (same kind of translator decision point: preserve / replace / annotate)
- *scope-of-scenarios* — Nursi-corpus-specific (hashiye, mesele, ayah handling) vs general-theological-translation (citation policy across traditions) vs broad translation-of-non-fiction (footnotes, sigla, marginalia)
- *granularity* — policy-level fields (Literal[] enums sized like NonMainLangPartsPolicy's 5 values) vs broader edge-case categories vs both at different levels

**Action-endpoints the statement could be targeting (MQ3 intent-axis ambiguities):**
- build-out-the-policy-layer (add more policy classes alongside NonMainLangPartsPolicy in `schemas.py`)
- pressure-test-the-pattern (see whether other scenarios fit the policy-enum shape)
- catalog-for-later-decision (just list now; route later or not at all)

## Goal

### Item 1 — schemas.py rationale explanation

**Deliverable shape (Deconstruct):** explanation (prose argument); kinds = rationale text + contrastive structure (this-vs-that across schema versions) + code-anchored where useful; bounds = `schemas.py` (3 classes) plus the prior-design history accessible via session substrate.

**Motivation-chain ambiguities (MultiDepth WHY-axis):**
- document-for-future-self (paper trail to prevent regression on the simplification)
- build-confidence (the user wants to feel certain the simplification was right before moving forward)
- articulate-the-principle (extract the design principle so it can be applied to Item 2)
- prepare-for-collaborator-or-audience (write it once so it can be shared)

**Context-need (MQ2):**
- *verdict:* `schemas.py` contents (TC + NonMainLangPartsPolicy + PC) required; prior 4-schema proposals from this session required for comparison; chunking finding's split-placement principle useful as trajectory the simplification corrects
- *kinds:* file's actual class contents; recent conversation's reasoning chain (TC frozen; SD dropped because LLMs don't need source-lang declared; EmbeddedLanguage replaced by NonMainLangPartsPolicy with language-agnostic policy values); Comprehenslate project's purpose (Nursi corpus translation)
- *stance:* explanatory (teach the rationale dispassionately) vs validating (confirm the user's choice was good) vs critical (pressure-test even though framed as "makes more sense")

**Explicit exclusions (MQ4 NOT-list):**
- the framing "makes a lot more sense" implies the user has decided this design is good — re-opening whether SD or EmbeddedLanguage *should* be re-added is implicitly out of scope
- recommending re-adding the just-dropped classes would conflict with the user's framing

### Item 2 — NonMainLangPartsPolicy-like policy list

**Deliverable shape (Deconstruct):** list (enumeration); kinds = named scenarios + brief description per item + optional sketch policy enum per scenario; bounds = scenarios in Comprehenslate / theological-translation / multi-language-source-text territory; excludes unrelated translation edge-cases unless they share structural shape.

**Motivation-chain ambiguities (MultiDepth WHY-axis):**
- complete-the-policy-set (build out what the user senses must exist beyond NonMainLangPartsPolicy)
- validate-the-pattern (test whether the enum-of-strategies shape generalizes)
- pre-bloat-prevention (catalog now to deliberately decide what to commit vs defer)
- educational-self-survey (a map of the edge-case territory)

**Context-need (MQ2):**
- *verdict:* NonMainLangPartsPolicy's exact shape needed as the template; prior 14-edge-case innovation pass useful (most deferred but the phenomena are real); 8-axis TC + 3 PC fields needed to know what's already covered
- *kinds:* corpus-specific phenomena (hashiye marginalia, register-alternation, ayah-atomicity); general theological-translation phenomena (Quranic citation tradition, biblical apparatus, transliteration); cross-corpus patterns (footnote/endnote conventions, scriptural reference notation)
- *stance:* loose brainstorm vs filtered-by-real-need vs ranked-by-priority

**Explicit exclusions (MQ4 NOT-list):**
- re-adding SourceDescriptor or a separate EmbeddedLanguage class (the user just dropped both)
- modifying TranslationConfig (frozen per the prior turn)
- pure runtime-engine concerns (those belong on PipelineConfig, not on a new policy class)

## Considered Articulations

### Item 1 — schemas.py rationale explanation
1. Explain the architectural reasoning for collapsing the four-schema design (TC / SD / EmbeddedLanguageProfile / PC) into the three-class `schemas.py` — what principle made SD and EmbeddedLanguage unnecessary?
2. Write a contrastive walkthrough of `schemas.py` vs the prior proposals showing what each correction caught and why the resulting structure is more honest about LLM capabilities and corpus reality.
3. Articulate the design principle behind `schemas.py` — what makes this a load-bearing improvement over earlier versions — in a way that generalizes to the other policies enumerated in Item 2.
4. Validate the `schemas.py` simplification by stating its rationale, and flag any residual structural concerns the simplification did not resolve.

### Item 2 — NonMainLangPartsPolicy-like policy list
1. List the recurring translation-edge-case scenarios in the Nursi / theological-translation territory that fit the same shape as NonMainLangPartsPolicy — a recurring authorial-edge-case whose handling is governed by a small Literal[] enum of strategies.
2. Catalog policy-shaped fields beyond NonMainLangPartsPolicy that the `schemas.py` architecture would naturally absorb as additional sibling classes.
3. Enumerate translation phenomena (citations, marginalia, register-shifts, transliteration, etc.) that need a policy-style enum and would compose with NonMainLangPartsPolicy in the same schema layer.
4. Survey the edge-case territory and identify which ones structurally match the policy-enum pattern vs which need a different shape — pressure-testing the pattern's reach.

## Scope Check

**Item 1:** Question covers goal. The MQ1/MQ3 ambiguity space is bracketed by the Deconstruct bounds (`schemas.py` + session substrate). The MQ4 NOT-list (don't re-open SD/EmbeddedLanguage drops) keeps the scope honest. Goal includes both motivation surfacing (WHY-axis: document / validate / extract-principle / prepare-for-audience) and rationale shape (architectural / domain / anti-bloat / LLM-capability / honest-categorization) — the question covers both.

**Item 2:** Question covers goal. The Deconstruct bounds (theological-translation territory) match the user's NonMainLangPartsPolicy template anchor. The MQ4 NOT-list (no SD / no EmbeddedLanguage / no TC modification / no PC-runtime concerns) keeps the list within the policy-class layer.

**Specific-vs-pattern check:**
- Item 1's *NonMainLangPartsPolicy* mention is a *specific class* but the rationale being asked about is the *broader principle* — the inquiry addresses the BROADER PATTERN (why this kind of design works), with NonMainLangPartsPolicy as the concrete anchor.
- Item 2's *"policies like NonMainLangPartsPolicy"* is explicitly pattern-shaped (using NonMainLangPartsPolicy as the template for "like"). The inquiry addresses the BROADER PATTERN — what other scenarios fit this shape.

Question covers goal across both items.

## Synthesis Trigger

This inquiry synthesizes context from prior outputs:

- `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md` — the most recent finding that committed to the 4-schema architecture (TC with chunking_granularity / SD with canonical_level / PC with chunking_mechanism_override) — the user has now simplified past this finding's TC modification and SD shape. The finding's commitments around chunking_granularity placement, SD.canonical_level, and the corpus-mappings table are inherited by reference and need re-test in light of the simplification.
- `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` — the original chunking finding that established the split-placement principle (schema ownership matches data ownership) and the 3-schema (SD + PC + TC) architecture. The principle is preserved in spirit (clean separation by data ownership) but the conclusion (3 schemas of specific shape) has shifted.
- `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md` — the edge-cases inquiry that produced the 14-candidate list and the proposed `EmbeddedLanguagePolicy` shape. Item 2 of this inquiry draws on those 14 candidates as the source territory for the policy-list catalog.
- `/Users/ns/Desktop/projects/comprehenslate/schemas.py` — the current authoritative schema (3 classes: TC + NonMainLangPartsPolicy + PC) the rationale-explanation in Item 1 must explain.

CONCLUDE will require an `## Inherited Commitments Re-test` section testing each inherited commitment (especially: split-placement / TC delta = 0 / SD as a schema / chunking_granularity placement / EmbeddedLanguagePolicy shape) with evidence cited or explicit flag.
