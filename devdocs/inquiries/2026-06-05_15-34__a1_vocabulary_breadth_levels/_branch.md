# Branch: a1_vocabulary_breadth_levels

## Question

The user has accepted the prior `translation_config_axes` inquiry's specification of A1 Reader Level as a composite-axis with 5 sub-fields: vocabulary-breadth, syntactic-processing-capacity, idiom-recognition, inference-capacity, cultural-reference-recognition. The previous finding committed to ~5 headline levels for A1 but left the actual level values + per-level meanings undefined (deferred per Constraint C7 to a follow-up inquiry).

This inquiry is the **first step of that follow-up**: it defines the level values for ONE sub-field only — **vocabulary-breadth** — with logic and examples that make each level distinguishable.

Constraints inherited from the prior finding:
1. 5 ordinal levels covering the full spectrum (the user's sketch named them `very_basic | daily | conversational | advanced | native` as a starting set).
2. Language-agnostic at the CONCEPT level — every human language has high-frequency vs low-frequency vocabulary; the concept of "vocabulary-breadth" is universal; level CONCEPTS must work for English, Russian, Japanese, Arabic, etc. English examples are allowed for illustration but cannot encode level CONCEPTS as English-specific frequency thresholds.
3. Sub-field of A1 (a composite-axis), not a standalone axis. The 5 levels propagate as sub-field defaults from A1's headline level; per-sub-field override semantics already settled in the prior finding.
4. Scope discipline: **vocabulary-breadth ONLY.** The other 4 sub-fields (syntactic-processing-capacity, idiom-recognition, inference-capacity, cultural-reference-recognition) are out of scope for this inquiry; they will be handled in their own follow-ups.

State the question: **For the vocabulary-breadth sub-field of A1 Reader Level, what should the 5 ordinal levels be — what concept does each level capture, what logic distinguishes each level from its neighbors, and what concrete examples make each level operationally identifiable — defined language-agnostically at the concept level (with English examples allowed for illustration)?**

The question has multiple observation targets, listed separately to preserve transcription fidelity:
- **OT1.** The 5 level NAMES (validated or refined from the sketch `very_basic | daily | conversational | advanced | native`).
- **OT2.** The CONCEPT each level captures (one sentence per level: what kind of reader is at this level?).
- **OT3.** The distinguishing LOGIC between adjacent levels (what makes "very_basic" not "daily"? what makes "conversational" not "advanced"? — the principle that draws the boundary).
- **OT4.** Concrete EXAMPLES that illustrate each level operationally (English examples allowed; the level CONCEPT must remain target-language-independent).
- **OT5.** A language-agnosticism CHECK per level (the level CONCEPT works whether the target language is English, Russian, Japanese, etc.; only the threshold examples differ per language).

## Goal

- **Criterion.** Five mutually distinct, ordinally meaningful, spectrum-covering levels — each operationalizable as a prompt instruction for the translator-AI, each with explicit distinguishing logic (not just example-based vibe), and each language-agnostic at the concept level.
- **Use case.** The user will commit these as the `vocabulary_breadth: Literal[...]` enum values in the pydantic schema; the per-level prose descriptions will become part of the translator-AI's prompt context; the boundaries between levels will guide the AI in deciding what vocabulary to use at each level.
- **Desired outcome.** A stable, named, defined set of 5 vocabulary-breadth levels with definition + distinguishing logic + 1–3 concrete examples per level; the user can immediately commit to the schema and move to the next sub-field.
- **What would fail.**
  - Levels defined only by example without explicit distinguishing logic (vibe-based, not principle-based).
  - Levels that overlap such that two adjacent levels could describe the same reader (failed ordinal distinctness).
  - Levels that aren't ordinal (mixing in a categorical level like "technical-specialist" alongside ordinal ones).
  - Level CONCEPTS that presuppose English-specific frequency lists / corpora as their definition (failed language-agnosticism — fine to give English examples; not fine to define a level as "level 4 of New General Service List").
  - Addressing the other 4 sub-fields of A1 (syntactic-processing-capacity, idiom-recognition, inference-capacity, cultural-reference-recognition) when the user explicitly said vocabulary-breadth only (scope creep).
  - Conflating vocabulary RECOGNITION with PRODUCTION — the prior finding's A1 explicitly said the field is about passive recognition, not active vocabulary use. A level definition that talks about what the reader CAN SAY rather than what the reader CAN UNDERSTAND fails.

## Source Input

```text
okay for A1 — Reader Level
Concept. The reader's overall ability to receive the translation. This is the broadest reader-facing axis.

User question it answers. "How fluent is the reader of this translation?"

Pattern. composite-axis — a headline level that the user sets, plus optional sub-field overrides. Sub-fields:

vocabulary-breadth — how many words the reader recognizes (passive vocabulary). High-breadth readers recognize technical or archaic words; low-breadth readers need everyday vocabulary.
syntactic-processing-capacity — how dense a sentence structure the reader can parse without losing the thread (long nested clauses, multi-clause subordination, etc.).
idiom-recognition — whether figurative expressions like "kick the bucket" land figuratively or get taken literally / freeze the reader.
inference-capacity — how much the reader can fill in compressed or elliptical argument (a passage that telescopes a five-step logical chain into one sentence; a passage where the verb is deliberately deleted; etc.).
cultural-reference-recognition — whether allusions and named entities land without explanation. This is competence-based, distinct from A3 Source Culture (which is identity-based — see below).
Why one axis with sub-fields, not 5 separate axes. The 5 sub-fields are empirically correlated in typical readers — a non-native ESL professor with high vocabulary but low idiom recognition is real but rare; the joint distribution is heavily clustered. If you split into 5 separate axes, every typical user must reason about 5 fields just to describe one reader (concept-load exceeds the ergonomic bound stated in the problem). If you collapse into one ordinal scale, the rare cases can't be expressed. The composite-axis pattern preserves both: the user sets ONE headline level; sub-field defaults derive from the headline; per-sub-field overrides are available for the cases where the joint correlation breaks.

Cardinality (proposed). 5 headline levels.

Scope. Controls the reader's overall comprehension profile.

Boundary. Does NOT control domain expertise (that's A2), source-culture proximity (that's A3), or how much explanatory help the translation provides (that's A7 Scaffolding).

Language-agnostic at concept level. Every human language has high-frequency vs low-frequency vocabulary; every language has idioms; every language has syntactic complexity gradients. The CONCEPT is universal. The level thresholds (what specifically counts as "very basic" vs "advanced" in a given language) are language-specific and belong in the next inquiry.


lets dive deep into 5 levels starting from very basic to advanced.. and also logic and example of how to distinguish them but only for vocabulary-breadth field, not about others
```

## Scope Check

Question covers goal: YES.

The Question targets vocabulary-breadth's 5 levels with names, concepts, distinguishing logic, examples, and language-agnosticism. The Goal asks for those same five things plus operationalizability and scope discipline. The Question's 5 observation targets (OT1–OT5) map directly to the Goal's criteria.

**Specific-vs-pattern check.** The user has SPECIFICALLY scoped to vocabulary-breadth (one sub-field of one axis). They are explicit: "but only for vocabulary-breadth field, not about others." The inquiry addresses the SPECIFIC sub-field, not the broader pattern of "how to define level values for any composite-axis sub-field." A future inquiry may abstract the pattern from this one; this inquiry's scope is concrete.

**Decoupling from other sub-fields and other axes:** explicit. The 4 other A1 sub-fields are out of scope; A2–A8 axes are out of scope; pydantic shape is out of scope; the per-Purpose default mappings are out of scope.

**Decoupling from prior finding's commitments:** the prior finding's A1 axis identity (composite-axis with 5 sub-fields, recognition not production, language-agnostic at concept level, ordinal pattern) is INHERITED and treated as settled. This inquiry does not re-open those.
