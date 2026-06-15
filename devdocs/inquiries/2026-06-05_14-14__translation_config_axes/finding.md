---
status: active
model: claude-opus-4-7[1m]
effort: max
---
# Finding: translation_config_axes

## Question

**Context.** Comprehenslate is an AI-assisted translation system in early design at `/Users/ns/Desktop/projects/comprehenslate`. The project corpus argues that high-quality translation must preserve multiple meanings, word order as meaning, and rhetorical structure — see `notes.md`, `translation_principals.md`, and `harmony_layer.md` for the principles, plus the sample English rendering of Said Nursi's 5th Word in `mytrasnlations/5th_word/eng.md`. The system needs to be **configurable**: the same source text should be translatable differently for different readers and different purposes. Existing configuration knobs in `.env.example` (AUDIENCE_LEVEL, DEPTH_PROFILE, POETIC_MODE, etc.) mix multiple concerns and are not yet a coherent typed configuration.

**The question.** What is the correct set of **axes** (configuration dimensions) for the Comprehenslate translation-configuration framework? Each axis must be language-agnostic at the concept level (so the same axis set works whether the target language is English, Russian, Japanese, or anything else); each must support 3–5 selectable levels covering its full spectrum; each must have a sensible default so a typical user only overrides 1–2 axes from defaults; the axes must be orthogonal (changing one does not force changing another); the full axis set must cover the user-side need-space without leaving gaps; and the axis set must **exclude** derivative output-properties such as "output vocabulary altitude" — those emerge from `{source content + axes + always-on policy}`, not from a separate user-facing axis.

**Goal.** Settle the AXIS SET (their identity, their meaning, what each captures) so that subsequent inquiries can define level values within each axis, then translate the resulting structure into pydantic dataclasses. The deliverable is "the right axes," not "the right level values" — level values are deferred to the next inquiry.

## Finding Summary

- **The framework has 4 layers; only Layer 1 is in this inquiry's scope.** Layer 1 = USER-FACING AXES (the user's configuration). Layer 2 = POLICY (always-on rules grounded in project values; out of scope, adjacent). Layer 3 = SOURCE-DESCRIPTION (auto-detected source properties with optional user override; out of scope, adjacent). Layer 4 = SYSTEM-FLAGS (pipeline knobs like chunking and parallel mode; out of scope, far).

- **Layer 1 has 8 axes organized into 4 families.** The families (Reader / Purpose / Strategy / Depth) are navigational labels for documentation, not configuration units; the configuration unit is the axis.

- **Reader family — properties of the intended reader (3 axes).** A1 Reader Level (the reader's overall fluency, with optional sub-field overrides for vocabulary, syntactic-processing, idiom-recognition, inference-capacity, and cultural-reference-recognition). A2 Domain Expertise (lay / general-educated / specialist). A3 Source Culture (the reader's identity-based proximity to the source's cultural milieu — outsider / familiar / source-native).

- **Purpose family — what the translation is for (1 axis).** A4 Purpose (the use-case — scholarly, devotional, casual, language-learning, performance, etc.). Categorical, not ordinal: these are qualitatively different uses, not points on one intensity scale.

- **Strategy family — how the translator handles source-target distance (3 axes).** A5 Source Fidelity (foreignization ↔ domestication; whether the translation sounds source-like or target-natural). A6 Form Preservation (the strength of structural preservation: rhythm, parallelism, word order as meaning, etc.; ties to the Tier 1–4 system in `harmony_layer.md`). A7 Scaffolding (how much explanatory help — footnotes, parenthetical glosses, transliterations — accompanies the translation; subsumes the "feature activation" bundle in the user's original sketch).

- **Depth family — how much interpretive material to surface (1 axis).** A8 Analysis Depth (surface / standard / deep / scholarly; inherits from the existing DEPTH_PROFILE knob in `.env.example`).

- **One axis uses a special pattern: `composite-axis`.** A1 Reader Level bundles 5 sub-dimensions that are correlated in typical readers but genuinely orthogonal in principle (a non-native ESL professor can be high-vocabulary, low-idiom). The pattern: one HEADLINE level the user sets, plus optional per-sub-field overrides. The headline propagates sensible defaults to sub-fields; overrides handle the rare cases. This pattern is reusable for future axes with the same correlated-sub-dimensions structure.

- **Some translation principles do NOT become axes — they become always-on POLICY.** When a principle is unanimously prescribed by project values such that letting the user opt out would contradict the project's identity, it relocates from "user-axis" to "always-on policy." The five relocated principles are: multi-meaning preservation when grammar permits (`notes.md` polysemy principles + memory feedback on local-construction-trumps); register-alternation preservation (memory feedback "don't pull plain registers up into ornate English"); polysemy resolution via local grammatical construction (memory feedback); nazm / form-as-meaning preservation when A6 Form Preservation is at least light; and no smoothing of difficult or uncomfortable nuances. Operational specification of each policy is a separate future inquiry.

- **Defaults follow a 2-tier principle: Purpose-driven, then conservative-bias fallback.** When the user sets A4 Purpose, that value drives sensible defaults for the other axes (a scholarly Purpose pulls Analysis Depth toward "deep" by default; a casual Purpose pulls Scaffolding toward "rich" for unfamiliar readers; etc.). When Purpose-driven defaults don't apply or the user hasn't set Purpose, fall back to **conservative-bias defaults** — preserve more form, more scaffolding, more depth; the user dials DOWN. Conservative-bias is appropriate at the project's current early-calibration phase (no real-user feedback yet); the defaults shift toward typical-use bias as feedback accumulates.

- **What's deferred to future inquiries.** Level values per axis (next inquiry, before pydantic). Per-axis default values with rationale (next or next-next inquiry). Per-axis prose descriptions for the AI translator's prompt (downstream). Pydantic dataclass shape (downstream, after level values are settled). Layer 2 POLICY operational specs (separate inquiry). Layer 3 SOURCE-DESCRIPTION schema (separate inquiry). Runtime conflict resolution between axis values (downstream). Layer 1A UX preset layer above the 8 axes (a future UX inquiry — innovation surfaced this strongly but it's a different inquiry's scope). Schema-layer free-form description fallback (future schema-layer inquiry).

## Finding

### Why these 4 layers and 8 axes (the design at a glance)

When you ask "how should a translation system be configured?" the obvious first answer is "let the user pick a few dials." But picking the *right* dials turns out to be where most of the work lives. Three different kinds of dial keep showing up and they have to be told apart, because they belong at different layers of the system:

1. **Dials the user legitimately chooses.** These are USER-FACING AXES — the configuration knobs the user actually sets per translation job. Layer 1.
2. **Rules that look like dials but should never be user-choices because letting the user opt out would contradict the project's stated values.** These are POLICY — always-on rules. Layer 2.
3. **Properties of the source text the system can detect (or that the user can declare if detection is wrong).** These are SOURCE-DESCRIPTION — Layer 3.

A fourth, less interesting layer is the pipeline-internal flags (chunking strategy, parallel mode, output format). These are Layer 4 and are not translation-content choices.

This inquiry's scope is **Layer 1**. The other three layers are named here so readers can see why the axis set doesn't include some things they might expect, and so future inquiries can each address the right layer.

Within Layer 1, the 8 axes come from a careful pass over four kinds of evidence: the user's original sketched 5 axes (which become a starting point but get reshaped); the project's stated values (which decide what's POLICY vs axis); adjacent translation-theory anchors (Skopos, Venuti foreignization/domestication, Nida formal vs dynamic equivalence, House overt vs covert translation, CEFR reader-competence, Halliday register, graded readers); and the user's existing configuration knobs in `.env.example`. The user's 5 axes survive in modified form; one of them ("feature activation") turns out to be a category error and gets split into two axes; one obviously missing axis (Purpose) gets added; one existing knob (DEPTH_PROFILE) gets promoted to its own axis (Analysis Depth).

### Layer 1 — the 8 axes, individually

Each axis below is specified at the **meaning / identity level**: what concept it captures, what user-facing question it answers, what its scope is, what it doesn't control. **Level values inside each axis (the actual enum strings like `very_basic | conversational | native`) are NOT set here.** They are the next inquiry. This finding's deliverable is the axis SET, not the levels within.

---

#### A1 — Reader Level

**Concept.** The reader's overall ability to receive the translation. This is the broadest reader-facing axis.

**User question it answers.** "How fluent is the reader of this translation?"

**Pattern.** **`composite-axis`** — a headline level that the user sets, plus optional sub-field overrides. Sub-fields:

- **vocabulary-breadth** — how many words the reader recognizes (passive vocabulary). High-breadth readers recognize technical or archaic words; low-breadth readers need everyday vocabulary.
- **syntactic-processing-capacity** — how dense a sentence structure the reader can parse without losing the thread (long nested clauses, multi-clause subordination, etc.).
- **idiom-recognition** — whether figurative expressions like "kick the bucket" land figuratively or get taken literally / freeze the reader.
- **inference-capacity** — how much the reader can fill in compressed or elliptical argument (a passage that telescopes a five-step logical chain into one sentence; a passage where the verb is deliberately deleted; etc.).
- **cultural-reference-recognition** — whether allusions and named entities land without explanation. **This is competence-based**, distinct from A3 Source Culture (which is identity-based — see below).

**Why one axis with sub-fields, not 5 separate axes.** The 5 sub-fields are empirically correlated in typical readers — a non-native ESL professor with high vocabulary but low idiom recognition is real but rare; the joint distribution is heavily clustered. If you split into 5 separate axes, every typical user must reason about 5 fields just to describe one reader (concept-load exceeds the ergonomic bound stated in the problem). If you collapse into one ordinal scale, the rare cases can't be expressed. The composite-axis pattern preserves both: the user sets ONE headline level; sub-field defaults derive from the headline; per-sub-field overrides are available for the cases where the joint correlation breaks.

**Cardinality (proposed).** 5 headline levels.

**Scope.** Controls the reader's overall comprehension profile.

**Boundary.** Does NOT control domain expertise (that's A2), source-culture proximity (that's A3), or how much explanatory help the translation provides (that's A7 Scaffolding).

**Language-agnostic at concept level.** Every human language has high-frequency vs low-frequency vocabulary; every language has idioms; every language has syntactic complexity gradients. The CONCEPT is universal. The level thresholds (what specifically counts as "very basic" vs "advanced" in a given language) are language-specific and belong in the next inquiry.

---

#### A2 — Domain Expertise

**Concept.** The reader's specialist knowledge in the source's subject domain (Islamic theology, biblical scholarship, theoretical physics, etc.) — independent of their general reading fluency.

**User question it answers.** "How much does the reader already know about the subject matter?"

**Pattern.** Plain ordinal (3 levels).

**Scope.** Controls whether the translator can use technical vocabulary without unpacking.

**Boundary.** Distinct from A1 (general fluency) and A3 (cultural insider/outsider). A Hebrew Bible scholar with low general English fluency, and a general-educated reader with no Bible knowledge, are both real configurations.

---

#### A3 — Source Culture

**Concept.** The reader's IDENTITY-BASED proximity to the source's cultural milieu.

**User question it answers.** "Does this reader come from inside the source's culture, or from outside?"

**Pattern.** Plain ordinal (3 levels: outsider / familiar / source-native).

**Scope.** Controls how many cultural references need explanation, transliteration choices for proper names, etc.

**Why distinct from A1's cultural-reference-recognition sub-field.** A1's cultural-reference-recognition is COMPETENCE-based (does the reader know the references?); A3 is IDENTITY-based (does the reader live inside the source's culture?). All four corners of the joint distribution are real: well-read insider (a cultural insider who studied the literature); poorly-read insider (a cultural insider who didn't); well-read outsider (a Western academic specialist who learned the references through study); uninitiated outsider (a Western reader new to the material). The translator's decisions differ between these four — for the well-read outsider, the system can use untranslated source-language terms (they know what `nefs` means) but may still need to flag cultural CONTEXT (they lack lived intuition the source-native has).

---

#### A4 — Purpose

**Concept.** What the translation is FOR — the use-case. This is the axis Skopos theory (Vermeer / Reiss) treats as the primary determinant of translation strategy.

**User question it answers.** "Why is this translation being made? What will the reader do with it?"

**Pattern.** **Categorical** (not ordinal). Levels are qualitatively different uses — scholarly study, devotional reading, casual reading, language learning, performance / recitation, etc. — not points on a single intensity scale.

**Why categorical, not ordinal.** A casual-to-scholarly ordering looks plausible but breaks on real cases: a scholarly user might want a CASUAL-feel translation for an easy read; a casual reader might want DEEP analysis to understand a passage. Purpose categories like `devotional` and `performance` don't fit anywhere on a casual-to-scholarly scale. The 3 mechanisms that converged on "categorical" (Skopos text-typology + the orthogonality counter-example + multi-axis Inversion's existence-axis check) point at the same conclusion.

**Cardinality (proposed).** ~5 categorical levels.

**Special role.** A4's value drives DEFAULTS for other axes (a scholarly Purpose suggests higher Analysis Depth by default; a casual Purpose suggests higher Scaffolding for unfamiliar readers; etc.). The default-derivation mechanism is in scope for this finding (see "Default principle" below); the specific per-Purpose default mappings are in the next inquiry.

---

#### A5 — Source Fidelity

**Concept.** The translator's strategic stance on the foreignization ↔ domestication spectrum (Lawrence Venuti's framework). Foreignizing translations preserve source-language feel, keep transliterations, retain source rhythms even when awkward in the target; domesticating translations naturalize to target-language idiom, substitute culturally-familiar equivalents.

**User question it answers.** "Should the translation sound like a translation, or read as if originally written in the target language?"

**Pattern.** Plain ordinal (3 levels).

**Scope.** Controls lexical / idiomatic choices at the surface of the translation.

**Boundary.** Distinct from A6 Form Preservation (structural elements like rhythm, parallelism, word order as meaning). A heavily-foreignized translation can ignore form (keep foreign-sounding words but render prose-flat); a heavily-domesticated translation can preserve form (use target-language poetics that mirror source poetics). These two ARE orthogonal in real translation choices.

---

#### A6 — Form Preservation

**Concept.** The strength of structural preservation — rhythm, parallelism, ring composition, word order as meaning carrier (the project corpus's central insight: nazm / arrangement IS meaning, not decoration).

**User question it answers.** "Should structural elements like rhythm and parallelism survive the crossing into the target language?"

**Pattern.** Plain ordinal (proposed 5 levels). The level structure ties to the Tier 1–4 system in `harmony_layer.md`: at the lowest level the translation ignores harmony entirely; at the highest level it preserves all four tiers including the Tier 3 entries with PRESERVE-WHEN clauses.

**Why this is its own axis, not a derivative.** Originally tempting to say "Form Preservation = Source Fidelity + Purpose." Counter-example: a casual reader of a poetic source might want HIGH Form Preservation (they want to feel the rhythm) while wanting domesticated lexicon. A scholar might want LOW Form Preservation (just give me the semantic content, don't waste effort on form) while wanting strict lexical fidelity. The orthogonality holds.

**Cross-reference to POLICY layer.** When A6 is at "light" or higher, the always-on policy of **nazm / form-as-meaning preservation** activates. The axis level is the activation gate; the policy itself is the operational rule.

---

#### A7 — Scaffolding

**Concept.** How much explanatory material accompanies the translation at the text surface — footnotes, parenthetical glosses, transliterations, brief in-line explanations.

**User question it answers.** "How much help does the reader need at the surface of the translation?"

**Pattern.** Plain ordinal (proposed 5 levels: off / minimal / standard / rich / scholarly).

**Scope.** Subsumes the three feature toggles in the user's original sketch ("feature activation" = harmony toggle + footnote toggle + transliteration toggle). This isn't a heterogeneous bundle; it's one ordinal dial. Higher levels mean more explanatory aid.

**Multi-meaning rendering note.** When the always-on POLICY of multi-meaning preservation activates (a polysemous word allows multiple senses simultaneously per the local construction), A7's level controls how the preserved meanings RENDER: at low Scaffolding, the primary meaning appears with a minimal footnote noting other senses; at high Scaffolding, the multiple meanings appear inline or in a full footnote. The user does not control WHETHER multiple meanings are preserved (that's policy); the user controls HOW they appear.

---

#### A8 — Analysis Depth

**Concept.** How much interpretive material the system surfaces ALONGSIDE the translation — not at the surface of the translation itself, but in separate analysis sections.

**User question it answers.** "How much interpretive commentary should accompany the translation?"

**Pattern.** Plain ordinal (4 levels: surface / standard / deep / scholarly). Inherits from the existing `DEPTH_PROFILE` knob in `.env.example`.

**Scope.** Controls the existence and richness of analysis output (etymology notes, rhetorical analysis, cross-references to other passages in the source).

**Why distinct from A4 Purpose.** A scholar might want LOW Analysis Depth for a particular use (clean translation text, no commentary). A casual reader might want HIGH Analysis Depth to understand a passage they're stuck on. Purpose answers "why are you reading?"; Analysis Depth answers "how much interpretive material accompanies the translation?"

**Why distinct from A7 Scaffolding.** Scaffolding is AT THE TEXT SURFACE (footnotes, in-line glosses). Analysis Depth is in SEPARATE SECTIONS (before / after the translation, in a study-aids sidebar, etc.). A user can have rich Scaffolding with surface Analysis Depth (lots of footnotes, no separate analysis chapter) or minimal Scaffolding with scholarly Analysis Depth (clean translation followed by an analysis chapter). They are orthogonal in real reading experiences.

---

### The `composite-axis` pattern (used by A1, reusable for future axes)

When an axis bundles multiple sub-dimensions that are (i) empirically correlated in typical users such that the joint distribution is clustered AND (ii) genuinely orthogonal in principle so that individual override matters for the edge cases, use the `composite-axis` pattern:

- **Headline level.** The user sets ONE level (e.g., `Reader Level = conversational`).
- **Sub-field defaults.** Each sub-field has a default value derived from the headline (e.g., `vocabulary-breadth → conversational`, `syntactic-processing-capacity → conversational`, ...).
- **Optional overrides.** Each sub-field is independently overridable when the typical correlation breaks (e.g., `vocabulary-breadth = advanced` overrides only that sub-field while the others stay at the conversational default).

A1 Reader Level is the canonical instance. A2–A8 are plain ordinal or plain categorical and do NOT use the pattern.

The name `composite-axis` was selected from a candidate list of eleven (`envelope-with-selective-override`, `headline-with-sub-field-overrides`, `bundled-axis`, `compound-axis`, `composite-axis`, `aggregate-axis`, `parent-child-axis`, `multi-faceted-axis`, `key-signature-axis`, `tiered-headline-axis`, `nested-axis`). `composite-axis` is short, semantically clear (it's a composite of multiple sub-fields), schema-natural (composite types are a well-understood vocabulary), and domain-agnostic. The choice is low-stakes (reversible later); critique recommended it but noted that `compound-axis` and `bundled-axis` are acceptable substitutes if the user prefers a different feel.

### The 4 families

The families are **navigational labels for documentation**, not configuration units. The configuration unit is the axis. A user doesn't pick a family; they pick an axis-value. The family groupings are useful for organizing the spec, the schema documentation, and the UI's information hierarchy.

| Family | Axes | What this family is "about" |
|---|---|---|
| Reader | A1 Reader Level, A2 Domain Expertise, A3 Source Culture | properties of the intended reader |
| Purpose | A4 Purpose | what the translation is for |
| Strategy | A5 Source Fidelity, A6 Form Preservation, A7 Scaffolding | how the translator handles source-target distance |
| Depth | A8 Analysis Depth | how much interpretive material the system surfaces |

Alternative family naming schemes were considered (Halliday's Field/Tenor/Mode triad from register theory was the strongest alternative). Halliday was rejected: Field/Tenor/Mode describe properties of SOURCE TEXTS, not groupings of USER-AXES. The semantic mismatch would confuse rather than clarify.

### Layer 2 — POLICY (named here so the boundary is visible)

The POLICY layer holds always-on rules. The user does NOT configure these because letting the user opt out would contradict the project's stated values. Five principles relocate from "potential user-axis" to "always-on policy":

1. **Multi-meaning preservation when grammar permits.** When a source word's local construction allows multiple simultaneously-valid senses (the `din` case — "judgment" + "religion" / "truth" both active), the translation preserves both rather than committing to one. Grounded in `notes.md` and `translation_principals.md`'s explicit statement that "all meanings derived from a text are valid and intended, as long as they don't violate the grammatical rules and foundational principles of the language. Choosing a meaning is up to the user, not to the translation system." If "preservation" were a user-axis with a "commit-to-one" level, the user would be explicitly opting out of the project's stated value.

2. **Register-alternation preservation.** Don't lift a plain source register into ornate or archaic English (and don't push an elevated source register into casual English). Grounded in stored user feedback: "Translation register fidelity — don't pull plain source registers up into ornate/archaic English; preserve register alternation as Tier 1/2 structure." When a source alternates between plain and elevated, the alternation IS structural meaning and must survive.

3. **Polysemy resolution via local construction.** When a polysemous source word has multiple senses, the local grammatical construction (case marking, agreement, plausibility of the candidate sense given the construction) selects the intended sense — NOT the surrounding metaphor's momentum. Grounded in stored user feedback: "Translation word-sense disambiguation — when a source word is polysemous, the local construction picks the sense, not the surrounding metaphor's momentum."

4. **Nazm / form-as-meaning preservation.** When A6 Form Preservation is at "light" or higher, the policy activates: word order, parallelism, ring composition, and other structural elements are treated as meaning-carriers and preserved across the language crossing. The axis (A6) controls activation; the policy controls behavior. Grounded in the project corpus's central insight that arrangement (nazm) is meaning, not decoration.

5. **No smoothing of difficult or uncomfortable nuances.** Translating away an awkward or uncomfortable nuance to make the output "cleaner" is itself a form of corruption — the smoothing introduces a worse error than the awkwardness it removes. Grounded in `translation_principals.md`'s "lesser-evil" principle.

The OPERATIONAL specification of each policy (what each one ENFORCES at the translator-runtime level) is deferred to a separate POLICY-layer inquiry. This finding only enumerates the principles and their grounding.

### Layer 3 — SOURCE-DESCRIPTION (named here so the boundary is visible)

The SOURCE-DESCRIPTION layer holds auto-detected properties of the source text — its genre, era, register profile, source culture — with optional user override when detection is wrong. These are NOT user-axes because the mental model differs: user-axes ask "tell me about the reader / what they want"; source-description asks "here's what the source IS." Future work defines the source-description schema in its own inquiry.

### Layer 4 — SYSTEM-FLAGS (named here so the boundary is visible)

Pipeline-internal knobs: chunking strategy, parallel mode, output format, indexing. These are not translation-content axes. Several existing `.env.example` knobs (INDEXING_ENABLED, CHUNKING_STRATEGY, PARALLEL_MODE, OUTPUT_FORMAT, PRESERVE_ORIGINAL_FORMAT) live here.

### Default principle (2-tier)

Each axis must have a sensible default so the typical user only overrides 1–2 axes from defaults. The default is determined as follows:

1. **Purpose-driven default (first tier).** If the user has set A4 Purpose, that value drives sensible defaults for the other axes. The specific per-Purpose default mappings (which value of A1 the casual purpose pulls toward, which Analysis Depth the scholarly purpose pulls toward, etc.) are deferred to the next inquiry; the principle is in scope.

2. **Conservative-bias fallback (second tier).** When Purpose is not set, or when Purpose-driven defaults don't cover a specific axis, the fallback is **conservative-bias**: preserve more form, more scaffolding, more depth; the user dials DOWN when they want less. This bias is appropriate at the project's current early-calibration phase (no real-user feedback yet). As feedback accumulates and the typical-user profile becomes empirically clear, the conservative-bias fallback shifts toward typical-use bias.

Innovation surfaced a third potential tier (preset-driven defaults, from a Layer 1A UX preset catalog above the 8 axes). Critique routed that to a future UX inquiry — it's a real and valuable architectural direction but belongs in a different inquiry's scope. The 2-tier principle stated here is what's in scope for this finding.

## Next Actions

### MUST

- **What:** Define the level values (the enum strings + per-level prose descriptions) for each of the 8 axes. Each axis has a proposed cardinality in this finding (5 for A1, 3 for A2, 3 for A3, ~5 for A4, 3 for A5, 5 for A6, 5 for A7, 4 for A8) but the actual level strings are not set.
  - **Who:** the next /MVLw inquiry (or equivalent) in this project.
  - **Gate:** before any pydantic dataclass work begins. Condition-bound.
  - **Why:** without level values, the axis identity is abstract — the translator-AI cannot operationalize "A1 Reader Level = conversational" without knowing what "conversational" means in prose.

- **What:** For each level value, write a short prose description that operationalizes as a PROMPT INSTRUCTION for the translator-AI (e.g., what kind of vocabulary, what kind of syntactic complexity, what kind of idiomatic handling each level entails). Per-language thresholds where applicable.
  - **Who:** same level-definition inquiry, or its immediate successor.
  - **Gate:** before pydantic dataclass shape.
  - **Why:** the axis levels need to operationalize at runtime; abstract enum strings are insufficient.

- **What:** Per-axis default selection. With Purpose-driven defaults specified (which Purpose pulls each other axis toward which value) AND a documented conservative-bias fallback per axis.
  - **Who:** the next inquiry or the one after.
  - **Gate:** before user-facing release. Condition-bound.
  - **Why:** without defaults, the typical user must set all 8 axes; the principle "specify only what you care about" cannot be honored.

### COULD

- **What:** Specify the operational behavior of each POLICY-layer rule (what each always-on rule ENFORCES at the translator-runtime level — e.g., what "register-alternation preservation" specifically requires the translator to do or not do, with examples from the project corpus and the 5th Word translation).
  - **Who:** a separate POLICY-layer inquiry.
  - **Gate:** can run in parallel with the level-definition inquiry (the policies don't depend on level values).
  - **Why:** the POLICY layer is enumerated here but its operational specs are needed before the translator-AI can be deployed.

- **What:** Define the Layer 3 SOURCE-DESCRIPTION schema — what source properties the system auto-detects (genre, era, register profile, source culture, source language) and the user-override fields.
  - **Who:** a separate SOURCE-DESCRIPTION inquiry.
  - **Gate:** can run in parallel with the level-definition inquiry.
  - **Why:** the SOURCE-DESCRIPTION layer is named here but its schema is needed before the system can adapt translation behavior to source properties.

- **What:** Design a Layer 1A UX preset catalog — named scenarios like `casual-english-reader`, `scholarly-english-reader`, `language-learning-reader`, `devotional-source-native-reader`, etc., each with all 8 axis values pre-populated, sitting above Layer 1B (the 8 axes). The user picks a preset as primary UI; the 8 axes are the power-user override interface.
  - **Who:** a future UX / presets inquiry.
  - **Gate:** after the level-definition inquiry. Condition-bound.
  - **Why:** innovation surfaced this strongly via three independent mechanisms (Absence Recognition redesign-level + Domain Transfer from video-editing LUTs + Inversion at the user-describes-vs-user-selects level). Critique routed it out of this inquiry but confirmed its value for a separate one.
  - **Depends-on:** MUST item "Define the level values" — the preset catalog cannot be built without the level values it references. This COULD is GATED — do not act until the MUST resolves.

- **What:** Design a schema-layer escape hatch — a free-form `notes` or `description` field at the configuration root, where the user can describe special needs that don't map cleanly to axis values, consumed by the translator-AI alongside the axis values.
  - **Who:** a future schema-layer inquiry.
  - **Gate:** after the level-definition inquiry. Condition-bound.
  - **Why:** even with 8 axes covering the user-side need-space, some edge cases will surface; an escape hatch prevents the framework from becoming brittle. Innovation surfaced this and critique routed it to its own inquiry.

### DEFERRED

- **What:** Pydantic dataclass shape for the configuration framework — translating the 8 axes (with the `composite-axis` pattern for A1) into typed Python.
  - **Gate:** revival when the level-definition inquiry completes and the level enums are stable. Condition-bound.
  - **Why (if revived):** structural-layer artifact for the system. Outside this inquiry's scope per the user's explicit deferral ("we can make a pydantic dataclasses from them later").

- **What:** Runtime conflict resolution between axis values (when the user sets axis combinations that point in incompatible directions, e.g., very-basic Reader Level + heavily-foreignized Source Fidelity + Scaffolding off — what does the translator-AI do?).
  - **Gate:** revival after the level-definition inquiry. Condition-bound.
  - **Why (if revived):** runtime behavior specification.

- **What:** Default-derivation mechanism specification (the concrete per-Purpose default mappings for each of the other axes).
  - **Gate:** revival in the next inquiry where level values are defined. Condition-bound.
  - **Why (if revived):** the 2-tier default principle is in scope here, but the specific mappings depend on level values being settled first.

## Reasoning

### What was settled, and what was rejected

**The user's original sketch had 5 axes** (Reader Competence Level, Feature Activation, Source-Fidelity Stance, Domain Expertise, Source-Culture Proximity). All 5 are touched by this finding's outcome, with three substantive changes:

- **"Feature Activation" was a category error.** The user bundled three different kinds of feature into one axis: a harmony-layer activation toggle, a footnote toggle, and a transliteration toggle. Sensemaking showed these don't share a dimension. The harmony toggle is genuinely level-based (the Tier 1–4 system in `harmony_layer.md` already specifies ordinal preservation strength); that's a separate axis (A6 Form Preservation). The footnote and transliteration toggles are about scaffolding — adding explanatory aid at the text surface; together with parenthetical glosses they form an ordinal axis (A7 Scaffolding). One bundled "Feature Activation" became two clean axes.

- **Purpose was missing from the sketch.** The user's original list had no Purpose axis. Skopos theory (the canonical translation-theory anchor for purpose-driven strategy) treats purpose as the PRIMARY determinant. Surfacing the project's existing knobs (the DEPTH_PROFILE values "surface | standard | deep | scholarly" are partly purpose-coded) and the project corpus's use-case categories (scholarly, devotional, casual, language-learning, performance) made it clear Purpose needed to be its own axis. A4 Purpose was added.

- **Analysis Depth was already in `.env.example` (DEPTH_PROFILE) but wasn't in the sketch.** Promoting it to its own axis (A8) was straightforward.

**Two axes that survived the sketch unchanged.** A2 Domain Expertise and A3 Source Culture survived in essentially their sketched form. Critique tested whether A3 (Source Culture, identity-based) overlaps with A1's cultural-reference-recognition sub-field (competence-based). The four-corners test passed — all four corners of the joint distribution are real readers — so they are genuinely orthogonal and both kept.

**Two axes were renamed for clarity.** The user's "Source-Fidelity Stance" became "Source Fidelity" (the "Stance" suffix added length without semantic gain). Similar streamlining applied to other names. The streamlined names are more elegant and more LLM-friendly without losing meaning.

**Three things the user's sketch did NOT include but the project's values require became POLICY, not axes.** Multi-meaning preservation, register-alternation preservation, and polysemy resolution via local grammatical construction. These are all in the project corpus or the user's stored feedback as strong values. Letting the user "opt out" of any of them through a user-axis would contradict the project's identity. They relocate to the POLICY layer.

**The biggest architectural decision: 4 layers, not 5.** Innovation surfaced a candidate architectural upgrade — adding a Layer 1A UX preset catalog above Layer 1B (the 8 axes) — through three independent mechanisms. Critique evaluated the upgrade against the inquiry's scope. The candidate's content (presets that bundle axis-values into named scenarios for primary UX) is genuinely valuable. But adding the layer to THIS inquiry's deliverable would (a) contradict the sensemaking commitment to 4 layers, (b) creep beyond the inquiry's stated scope (axis identity at meaning level), and (c) require a preset catalog whose definition is itself a separate concern. Critique routed the preset layer to a future UX inquiry and preserved the 4-layer architecture for this inquiry.

**The biggest scope-discipline decision: 2-tier defaults, not 3-tier.** Innovation also proposed a 3-tier default principle (preset → Purpose-driven → conservative-bias). The 3-tier form depends on the preset layer existing. Since the preset layer is deferred to a future inquiry, the 3-tier principle would create cross-inquiry dependency in this finding's deliverable. Critique refined to a 2-tier principle (Purpose-driven → conservative-bias fallback) that is fully in scope and forward-compatible: when the preset layer arrives, the 2-tier expands to 3-tier without restructuring.

**Why 8 axes and not 4 or 6 or 10.** Sensemaking tested the count carefully. Below 4 axes the framework is under-expressive (too many user needs collapse into one knob). Above 8 axes the concept-load violates the user's stated ergonomic principle ("specify only what you care about"). Within the 4-to-8 range, several collapses were tested and rejected: collapsing the Reader family into one envelope axis would force every typical user to override the same sub-field every time; collapsing Form Preservation into Source Fidelity loses the orthogonality between structural and lexical fidelity; collapsing Analysis Depth into Purpose loses the orthogonality between "why are you reading" and "how much commentary accompanies the translation." 8 axes is at the upper bound of the ergonomic range — close to the limit but structurally justified.

**Why the `composite-axis` pattern only applies to A1, not other axes.** Of the 8 axes, only A1 Reader Level has multiple correlated sub-dimensions where individual override matters for the edge cases. The other 7 axes are either plain ordinal (no sub-dimensions to bundle) or plain categorical (A4 Purpose). Applying the composite pattern to axes that don't need it would be over-engineering.

### Significant alternatives rejected

- **Halliday's Field / Tenor / Mode as family names** (instead of Reader / Purpose / Strategy / Depth). Halliday's triad describes properties of SOURCE TEXTS, not groupings of USER-AXES. Semantic mismatch would confuse rather than clarify. Rejected.

- **Splitting A1 Reader Level into 5 separate axes** (one per sub-field: vocabulary, syntax, idiom, inference, cultural-reference). Total axis count rises to 12, violating the ergonomic upper bound. The empirical correlation of the 5 sub-fields in typical users means 95%+ of users would set 5 axes redundantly. Rejected in favor of the composite-axis pattern.

- **Collapsing A1 Reader Level into one ordinal scale** (like the existing `AUDIENCE_LEVEL = native | late_learner | late_learner_simple`). The rare-but-real cases (non-native ESL professor with high vocabulary, low idiom; high-cultural-knowledge outsider with average vocabulary) cannot be expressed. Rejected in favor of the composite-axis pattern.

- **"Multi-Meaning Preservation" as a user-axis with a "commit-to-one" level.** Would let the user opt out of the project's stated value. Rejected; relocated to POLICY.

- **Source-Culture Proximity merged into Reader Level's cultural-reference-recognition sub-field.** Four-corners test showed they are genuinely orthogonal (competence vs identity). Rejected; both kept.

- **Source-side properties (genre, era, source register, source culture) as user-axes.** These describe the source, not the reader or the strategy. Different mental model. Rejected; relocated to the SOURCE-DESCRIPTION layer.

- **The 5-layer architecture (adding Layer 1A presets).** Real value, wrong inquiry. Routed to a future UX inquiry.

- **The 3-tier default principle (preset → Purpose → conservative-bias).** Depends on the preset layer which is deferred. Refined to 2-tier (Purpose → conservative-bias).

- **The free-form description fallback as an escape hatch in this inquiry's schema.** Real value, wrong inquiry. Routed to a future schema-layer inquiry.

## Open Questions

### Refinement Triggers

- **A1 Reader Level cardinality may need adjustment.** Proposed 5 headline levels. If empirical user feedback shows the 5-level granularity is unused (users cluster at 2-3 levels), the cardinality may collapse. Trigger: condition-bound — after the first 30 real translation configurations are logged, examine the distribution of A1 headline-level values.

- **8 vs fewer axes.** The 8-axis count is at the ergonomic upper bound. If real-user feedback shows the system is too complex (users confuse axes or skip overrides because the concept-load is too high), collapse-via-composite-axis-extension may become the right move (e.g., collapse the Reader family into one composite Reader axis with 3 sub-fields). Trigger: condition-bound — after the first 30 user feedback reports, examine confusion-vs-axis frequency.

### Research Frontiers

- **Configuration-as-dialogue paradigm.** Innovation's Inversion at Level 3 surfaced an alternative interface where configuration is interactive dialogue between the user and the LLM rather than a static schema. The 8 axes would become internal scoring dimensions rather than user-facing fields. This is long-horizon (5–10 years) and depends on LLM capability development. Preserved as observation; not active.

### Blocked

- **Per-language level definitions for A1 Reader Level's sub-fields.** Each language has different thresholds for what counts as "advanced vocabulary" or "complex syntax." The level-definition inquiry will define these for the first target language (likely English); other languages follow as the system expands.

### Monitoring

- **The conservative-bias-defaults principle is calibration-state-dependent.** It is appropriate now (early stage, no user feedback). As feedback accumulates, the principle should shift toward typical-use bias. Trigger: observable — when 30+ real translation configurations are logged with user satisfaction signal.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
so in this project we are basically creating ai based translations.

But these translations should be configurable

both for reading levels and complex vocabulary levels, we can have up to 5 levels , define each in language agnostic way (so these levels can use used to translate to russian or any other language)

and later on when they configurations are better defined, we can make a pydantic dataclasses from them later.

so before deciding these 5 levels , lets decide what dimensions/paradigms these levels should be designed upon (vocabulary complexity, native speaker, backpacker level conversational knowledge (which means they wont understand idioms etc))

maybe one axis is

Reader Competence Level (RCL)

 which has these subfields
 vocabulary breadth ( how many words the reader recognizes (their passive vocabulary). A high-breadth reader recognizes "ratiocination" or "ostensibly"; a low-breadth reader needs "reasoning" or "apparently." Note this is RECOGNITION not PRODUCTION — the reader doesn't have to use these words, only understand them when encountered.)
 syntactic processing capacity (ability to parse complex sentence structures: nested clauses, long subordination chains, sentences that hold multiple ideas in suspension before resolving. A high-capacity reader handles dense Germanic-style syntax like "The argument, despite being couched in the kind of dense subordination that requires the reader to hold three clauses in working memory before encountering the main verb, succeeds." A low-capacity reader needs that broken into short sentences with explicit connectives.)
 idiom recognition (ability to read figurative expressions figuratively (not literally). A high-recognition reader sees "kick the bucket" and understands "die"; a low-recognition reader takes it literally or freezes on the unfamiliar phrase)
  inference capacity (ability to fill in implicit information from context: ellipses, gaps, "what the author means without saying it," compressed or elliptical prose. A high-capacity reader follows compressed argument (e.g., a Said Nursi passage that telescopes a five-step logical chain into one sentence); a low-capacity reader needs the chain made explicit step by step. )

cultural-reference recognition (ability to recognize allusions, named entities, and cultural touchstones from the source culture without explanation. A reader familiar with the source's cultural milieu hears "a Hamlet moment" or "the Quranic Fātiḥa structure" and gets the reference; an outsider needs the reference unpacked, footnoted, or substituted with a target-culture equivalent. (Note: this sub-aspect overlaps with Axis 5 Source-Culture Proximity but is distinct — proximity is identity-based, recognition is competence-based. A non-native reader can have high cultural-reference recognition through study; a native can have low recognition if poorly read.))


the second might be

something that activates certain features
 harmany layer be active or not or how strongly actiavated, , or footnotes activated or not, or preserve source-term transliterations enabled or not.


the thid might be


Source-Fidelity Stance. Translator-strategic axis on the foreignization ↔ domestication spectrum (Lawrence Venuti's framework). Three levels: heavily-foreignized (preserve source-language feel; keep transliterations; retain source rhythms even when awkward in target), balanced (the default), heavily-domesticated (naturalize to target-language idiom; substitute culturally-familiar equivalents). Independent from reader competence. Closely coupled to Purpose but conceptually distinct — a scholarly-purpose reader might want heavy domestication for ease, or might want heavy foreignization for source-faithfulness; the user picks.



Axis 4 — Domain Expertise. Reader-side, identity-adjacent. Three levels: lay (no special domain knowledge), general-educated (the default — broad competence but no specialist depth), specialist (technical expertise in the text's subject matter). Crucial for technical / scholarly translation: a Hebrew Bible scholar reading a translation needs different scaffolding than a general reader, even at the same RCL. Operationally independent from general reading fluency.


Axis 5 — Source-Culture Proximity. Reader-side, identity-adjacent. Three levels: outsider (no source-culture exposure — the default), familiar (some exposure; recognizes major references), source-native (cultural insider; allusions land without explanation). Decides how many cultural references need explanation, transliteration choices for proper names, etc.



text-side properties are derivative. Target-text vocabulary altitude, syntactic complexity, idiom literalness — these are NOT user-specified axes. They emerge from {source content + RCL + Source-Fidelity Stance}. You can't make a complex theological passage use third-grade English without losing meaning; the translator's discretionary handling of vocabulary IS a source-fidelity decision, not a separate axis. This is why the architecture has no "output vocabulary altitude" axis.


Defaults reduce specification burden. Each axis has a sensible default.  A typical audience-spec overrides only 1-2 axes from defaults; the rest stays default. Like a config file's env-style values — specify only what you care about.
so we should understand what levels should be defaults


but these are my notes and they are not definitive or final. I would like you to think from scracth and better define these axises and later on we will define  fields in these axises

for example

vocabulary_lvl= "very_basic"| "daily" | "conversational" | "advanced" | "native"

is good field for  Reader Competence Level's  vocabulary breadth

it is good becuase it can be selected. and has coverage for whole spectrum..

Again, first lets focus on axises for now.
```

</details>
