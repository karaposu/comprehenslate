# Branch: a1_syntactic_processing_capacity_levels

## Question

The two prior inquiries in this chain have settled:
1. **`translation_config_axes`** — A1 Reader Level is a composite-axis with 5 sub-fields (vocabulary-breadth, **syntactic-processing-capacity**, idiom-recognition, inference-capacity, cultural-reference-recognition); the 5 sub-fields share the same 5 labels for clean default-propagation from A1 headline.
2. **`a1_vocabulary_breadth_levels`** — vocabulary-breadth's 5 ordinal levels are `very_basic | daily | conversational | advanced | native`, each with a 4-component definition (reader-profile + frequency-tier band + register-tier inclusion + substitution-test sketch), plus adjacent-level boundary pairs, an A1↔A2 boundary clarification, and a suggested migration mapping.

This inquiry takes the **same step for syntactic-processing-capacity** — the sub-field that captures "how dense a sentence structure the reader can parse without losing the thread (long nested clauses, multi-clause subordination, etc.)" per the prior translation_config_axes finding.

Constraints inherited from the chain:
1. 5 ordinal levels, same labels (`very_basic | daily | conversational | advanced | native`) for default-propagation.
2. Receptive-only — recognition not production; "can parse / can follow when encountered," not "can construct."
3. Language-agnostic at concept level — every language has syntactic complexity gradients; the level CONCEPTS must hold for English, Russian, Japanese, Arabic, etc.; English examples are illustrative.
4. Conservative-bias-for-reader-axes = LOWER default (assume less processing capacity; user dials UP).
5. Adapted 4-component template — the vocabulary-breadth template used (reader-profile + frequency-tier + register-tier + substitution-test). For syntax, some components need adaptation: **frequency-tier** is not the right concept for syntactic structures (sentences don't have a Zipfian frequency the way words do); **register-tier** partly applies (academic register has denser syntax than casual register, but the syntactic dimension is its own axis). The substitution-test logic adapts as a **restructuring-test** (split / shorten / un-embed clauses).
6. Scope discipline: **syntactic-processing-capacity ONLY.** The other 3 remaining A1 sub-fields and the already-defined vocabulary-breadth are out of scope.

State the question: **For the syntactic-processing-capacity sub-field of A1 Reader Level, what should the 5 ordinal levels be — what concept does each level capture, what logic distinguishes each level from its neighbors, and what concrete example sentence structures make each level operationally identifiable — defined language-agnostically at the concept level (with English example sentences allowed for illustration), and using a 4-component definition template adapted from the vocabulary-breadth template?**

Multiple observation targets, listed separately per the transcription-audit:
- **OT1.** The 5 level NAMES (same as vocabulary-breadth labels per same-labels-for-default-propagation; validate that the labels carry sensible syntactic semantics).
- **OT2.** The CONCEPT each level captures (one sentence per level: what kind of reader can parse what kind of sentence structures?).
- **OT3.** The distinguishing LOGIC between adjacent levels (what makes "very_basic" syntax not "daily" syntax? what makes "conversational" syntax not "advanced" syntax? — the structural-complexity principle that draws each boundary).
- **OT4.** Concrete EXAMPLE SENTENCES at each level (English example sentences as illustration; the level CONCEPTS must remain target-language-independent).
- **OT5.** Adapted 4-component template for SYNTAX (what replaces frequency-tier? what does register-tier mean here? what is the substitution-test analogue for syntactic restructuring?).
- **OT6.** Language-agnosticism check per level (the level CONCEPT works for any target language; specific syntactic patterns may differ per language but the complexity gradient is universal).

The user's seed framing additionally specifies the kinds of structures relevant: "long nested clauses, multi-clause subordination, etc." — these are observation targets within the LOGIC component (distinguishing logics should reference clause-nesting depth, subordination chain length, working-memory load, sentences that hold multiple ideas in suspension before resolving).

## Goal

- **Criterion.** Five mutually distinct, ordinally meaningful, spectrum-covering levels for syntactic-processing-capacity — each operationalizable as a prompt instruction for the translator-AI, each with explicit distinguishing logic (not example-based vibe), each language-agnostic at the concept level. The 4-component template adapts from the vocabulary-breadth template; components that don't fit syntax are replaced with analogues that do.
- **Use case.** The user will commit these as the `syntactic_processing_capacity: Literal[...]` enum values in the pydantic schema; the per-level prose descriptions will become part of the translator-AI's prompt context; the boundaries between levels will guide the AI in deciding how dense a sentence structure to use at each level (split long sentences? unembed clauses? avoid multi-clause subordination?).
- **Desired outcome.** A stable, named, defined set of 5 syntactic-processing-capacity levels with adapted-component definition + distinguishing logic + 1–3 concrete example sentences per level; ready for the user to commit to the schema and move to the next sub-field.
- **What would fail.**
  - Levels defined only by example without explicit distinguishing logic (vibe-based, not principle-based).
  - Levels that overlap such that two adjacent levels could describe the same reader's parsing capacity.
  - Levels that aren't ordinal (mixing a categorical distinction like "narrative-style vs argumentative-style syntax" alongside ordinal complexity).
  - Level CONCEPTS that presuppose English-specific syntactic phenomena (e.g., "head-final" vs "head-initial" as the defining axis would fail — Japanese is head-final and that's a typology, not a complexity gradient).
  - Conflating syntactic-processing-capacity with vocabulary-breadth (sentence complexity ≠ word recognition; both can vary independently — a reader can know all the words but lose the thread on a deeply-nested clause structure).
  - Conflating syntactic-processing-capacity with inference-capacity (which is its own A1 sub-field about filling compressed argument gaps — distinct from parsing the syntactic structure of stated content).
  - Conflating with cultural-reference-recognition or idiom-recognition.
  - Addressing the other 3 remaining A1 sub-fields (idiom-recognition, inference-capacity, cultural-reference-recognition) when the user explicitly said syntactic-processing-capacity only.
  - Mixing receptive and productive framing (the field is about PARSING when encountered, not constructing).
  - Using English-Latinate-style register cues as the defining syntactic-complexity signal (a sentence can be syntactically dense without using Latinate vocabulary; this is the failure mode of conflating syntax with vocabulary-breadth).
  - Failure to adapt the 4-component template — blindly copying vocabulary-breadth's "frequency-tier" component when frequency-tier doesn't apply to syntactic structures.

## Source Input

```text
now can we do the same for syntactic-processing-capacity — how dense a sentence structure the reader can parse without losing the thread (long nested clauses, multi-clause subordination, etc.). ?
```

## Scope Check

Question covers goal: YES.

The Question targets the 5 levels of syntactic-processing-capacity with names, concepts, distinguishing logic, examples, and the adapted 4-component template. The Goal asks for those same five things plus operationalizability, language-agnosticism, scope discipline, and the adaptation of the vocabulary-breadth template for syntax.

**Specific-vs-pattern check.** The user explicitly scoped to "syntactic-processing-capacity" only ("now can we do the same for syntactic-processing-capacity"). The "do the same" phrasing refers to applying the same shape/pattern as the vocabulary-breadth inquiry. The inquiry addresses the SPECIFIC sub-field, not the broader pattern of "how to apply the vocabulary-breadth template to any sub-field" (that pattern is implicit; future inquiries for idiom-recognition / inference-capacity / cultural-reference-recognition will apply the same shape with their own adaptations).

**Decoupling from other sub-fields:** explicit. Vocabulary-breadth (done), idiom-recognition (next), inference-capacity (next-next), cultural-reference-recognition (last) are out of scope for THIS inquiry.

**Decoupling from prior findings' commitments:** the structural commitments (composite-axis pattern, receptive-only, language-agnostic at concept, same-labels-across-A1-sub-fields, conservative-bias-for-reader-axes-LOWER-default, A1↔A2 boundary, 4-layer architecture) are INHERITED and treated as settled. This inquiry does not re-open those; the finding will include an `## Inherited Commitments Re-test` section per CONCLUDE's policy when refining a prior finding.

**Template-adaptation in scope.** Unlike the vocabulary-breadth inquiry which could directly use frequency-tier as a primary component, this inquiry must adapt the template — frequency-tier becomes something like "structural-complexity tier" or "working-memory load tier"; the substitution-test becomes a "restructuring-test" (split / unembed / linearize). The adaptation is in scope and decomposition / innovation will produce the adapted components.
