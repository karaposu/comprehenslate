# Branch: translation_config_axes

## Question

The user is designing the configuration framework for Comprehenslate, an AI translation system that produces configurable translations. Before deciding the LEVEL VALUES within each configuration axis (the "up to 5 levels" — e.g., `vocabulary_lvl = "very_basic" | "daily" | "conversational" | "advanced" | "native"`), the prior question is: **what AXES (dimensions / paradigms) should the configuration be built on?**

The question must be answered such that:
1. The axes are designed from scratch (the user's sketched 5 axes — RCL, feature activation, Source-Fidelity Stance, Domain Expertise, Source-Culture Proximity — are suggestions to interrogate, not a definitive baseline).
2. The axes are **language-agnostic** — the same axis set must work whether the target language is English, Russian, Japanese, or any other; nothing in the axis definitions may presuppose target-language properties.
3. Each axis must be a candidate for "up to 5 selectable levels" covering the whole spectrum (so the axis must be ordinal-or-categorical in a way that 3–5 distinct levels can plausibly partition it).
4. Each axis must have a **sensible default** so a typical audience-spec overrides only 1–2 axes from defaults; the rest stays default (the env-style config principle).
5. The axes must be **independent / orthogonal** — each axis controls something the others do not; no double-counting; no axis whose values are derivable from another axis's values.
6. **Coverage check**: every reasonable user-side configuration need (who is reading; for what purpose; how close to the source; what scaffolding they need) must be expressible as a combination of values across the axis set, without leftover unrepresented needs.
7. **Derivative-properties exclusion**: text-side properties of the OUTPUT (output vocabulary altitude, output syntactic complexity, output idiom literalness, output footnote density, output rhythm) are NOT axes — they emerge from `{source content + axes + translator policy}`. The axes must control inputs/configurations, not output features directly. The output features are derivative.

State the question as: **What is the correct set of axes (dimensions) that the Comprehenslate translation configuration framework should be built on — such that each axis is language-agnostic, supports 3–5 selectable levels covering its full spectrum, has a sensible default, is independent of the other axes, and the full axis set covers every reasonable user-side configuration need without including any axis whose values would actually be derivative of source content + other axes?**

## Goal

A good answer is:

- **Criterion** — Precision (each axis is clearly individuated; the boundary between any two axes is articulable), independence-checked (every pair tested for orthogonality), coverage-checked (the user-side need-space is enumerated and each need is mapped to one axis), language-agnostic (no axis presupposes target-language properties), default-bearing (each axis has a sensible default justified by typical use), and decomposition-aware (where an axis decomposes into sub-fields, the sub-fields are named — but the AXIS itself, not the sub-fields, is the configuration unit).
- **Use case** — The user will (a) freeze this axis set as the architecture of the configuration framework, (b) later define the 3–5 level values within each axis, (c) later still translate the axes + levels into pydantic dataclasses, (d) use the axes to interpret translation-rendering rules in `harmony_layer.md`, `translation_principals.md`, and `advanced_principles.md`, (e) extend the existing `.env.example` knobs (AUDIENCE_LEVEL, DEPTH_PROFILE, POETIC_MODE, QUOTED_CONTENT, HARMONY_ENABLED) into a coherent typed configuration matching the agreed axes.
- **Desired outcome** — A stable, named, defined set of N axes (where 3 ≤ N ≤ 7) with each axis's definition, scope, default, and independence-rationale stated; the user can then move directly to defining level values within each axis.
- **What would fail** —
  - An axis list that just renames the user's sketched 5 axes without interrogating whether they are the right axes (no value added).
  - An axis list that includes derivative output-properties (e.g., "output vocabulary altitude") as separate axes (architectural error per Constraint 7).
  - An axis list where two axes overlap such that adjusting one ALWAYS implies adjusting the other (failed orthogonality).
  - An axis list that presupposes English as the target language (failed language-agnosticism).
  - An axis list that includes 10+ axes the user must specify on every translation (violates the "default-driven, override 1–2" principle).
  - An axis list that defines levels prematurely (the user explicitly said: focus on axes for now, not level values).
  - An axis list that omits a user-side need-dimension that does have configuration impact (incomplete coverage).

## Source Input

The user's raw request, preserved verbatim:

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

## Scope Check

Question covers goal: YES.

The question targets the AXIS SET — what dimensions the configuration framework should be built on — and the goal asks for that same axis set (named, defined, defaulted, independence-checked). The question's seven explicit constraints (from-scratch design, language-agnostic, ordinal/categorical for 3–5 levels, sensible defaults, orthogonal, full user-side coverage, derivative-exclusion) match the goal's "criterion" clause point-for-point.

**Specific-vs-pattern check:** The user has sketched 5 specific axes (RCL, feature activation, Source-Fidelity Stance, Domain Expertise, Source-Culture Proximity) BUT explicitly says "these are my notes and they are not definitive or final. I would like you to think from scratch." So this inquiry addresses the **broader pattern** (what should the axis set be), with the sketched 5 as inputs to interrogate rather than a fixed answer to validate. The inquiry may end up confirming, merging, splitting, removing, or adding axes relative to the sketch.

**Decoupling-from-levels check:** The user is explicit that this inquiry stops at the axis layer. Level values inside each axis (the `vocabulary_lvl = "very_basic" | "daily" | "conversational" | "advanced" | "native"` example) are OUT OF SCOPE for this inquiry; they are the next inquiry. The deliverable is N axes with definitions and defaults, NOT N axes each with its 5 enumerated level values.

**Pydantic-translation decoupling:** Translation of axes into pydantic dataclasses is also OUT OF SCOPE for this inquiry. The deliverable is conceptual axes; later inquiries handle level enumeration and code-shape.

## Layer Commitment

This is a from-scratch redefinition of a framework artifact (the configuration axis set). Trigger fires: the user said "think from scratch and better define these axises."

**Primary layer: meaning.**

The question is about what concept each axis CAPTURES — what dimension of user/translation reality each axis represents, why it is one axis and not two, why it is a separate axis from the others. This is the meaning layer: what the axis IS as a cognitive operation in the configuration framework.

**Out of scope for THIS run:**
- **Structural** — what the pydantic dataclass / config schema LOOKS LIKE. The user explicitly defers this: "later on when they configurations are better defined, we can make a pydantic dataclasses from them later." A separate inquiry handles structural shape after meaning is settled.
- **Process** — what STEPS the system runs when applying axis values to a translation (the pipeline from `{source, axes}` to rendered output). This presupposes meaning is settled; a separate inquiry handles process.

The order is meaning → structural → process: until we know WHAT the axes are conceptually, we cannot decide the schema fields or the application procedure.
