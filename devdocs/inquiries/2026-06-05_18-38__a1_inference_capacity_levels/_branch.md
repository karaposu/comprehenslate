# Branch: a1_inference_capacity_levels

## Question

The four prior inquiries in this chain have settled:
1. **`translation_config_axes`** — A1 Reader Level is a composite-axis with 5 sub-fields, of which **inference-capacity** is the 4th. Prior framing: "ability to fill in implicit information from context: ellipses, gaps, 'what the author means without saying it,' compressed or elliptical prose. A high-capacity reader follows compressed argument (e.g., a Said Nursi passage that telescopes a five-step logical chain into one sentence); a low-capacity reader needs the chain made explicit step by step."
2. **`a1_vocabulary_breadth_levels`** — sub-field 1; original 4-component template.
3. **`a1_syntactic_processing_capacity_levels`** — sub-field 2; HEAVY template adaptation (structural-complexity tier + restructuring-test).
4. **`a1_idiom_recognition_levels`** — sub-field 3; LIGHT template adaptation (only substitution-test → idiom-handling test).

This inquiry takes the **same step for inference-capacity** — the sub-field that captures how much implicit / compressed / elliptical content the reader can fill in cognitively.

Constraints inherited from the chain:
1. 5 ordinal levels, same labels (`very_basic | daily | conversational | advanced | native`).
2. Receptive only — fills implicit gaps when encountered, doesn't write compressed argument.
3. Language-agnostic at concept level.
4. Conservative-bias-for-reader-axes = LOWER default.
5. Scope = inference-capacity ONLY (other A1 sub-fields out of scope; cross-sub-field interactions documented but not specified).
6. Template adaptation — likely MEDIUM (between idiom's LIGHT and syntax's HEAVY). Frequency-tier doesn't directly apply (inferences don't have Zipfian frequency); the dimension is COGNITIVE LOAD (compression depth; ellipsis tolerance; pragmatic inference distance; anaphora resolution distance). Register-tier partly applies but more directly through GENRES (news = low inference demand; academic = high; poetry/literary = highest). The substitution-test analogue becomes **gap-filling test** with named runtime actions: EXPLICATE (make implicit step explicit) / BRIDGE-CONNECTIVES (add logical connectives) / RESOLVE-ANAPHORA (make pronoun references explicit) / UNPACK-COMPRESSION (expand telescoped argument into steps) / KEEP-AS-IS.

State the question: **For the inference-capacity sub-field of A1 Reader Level, what should the 5 ordinal levels be — what concept does each level capture (how much implicit content the reader fills in: compression depth, ellipsis tolerance, pragmatic inference, anaphora resolution, discourse coherence), what logic distinguishes each level from its neighbors, and what concrete examples of inferentially-dense vs explicit text make each level operationally identifiable — defined language-agnostically at the concept level, with a 4-component definition template adapted as needed from the vocabulary-breadth template (frequency-tier → inference-load tier; substitution-test → gap-filling test)?**

Multiple observation targets:
- **OT1.** The 5 level NAMES (same labels per same-labels-for-default-propagation; validate that the labels carry sensible inference-capacity semantics).
- **OT2.** The CONCEPT each level captures (one sentence per level: how much implicit content the reader fills in).
- **OT3.** The distinguishing LOGIC between adjacent levels (what makes very_basic ≠ daily? what makes advanced ≠ native? — likely along COMPRESSION-DEPTH and ELLIPSIS-TOLERANCE dimensions).
- **OT4.** Concrete EXAMPLES at each level — pairs of inferentially-dense text (high-inference-capacity required) vs explicit text (low-inference-capacity sufficient). The user's seed anchor (Said Nursi telescoping a 5-step argument) sits at advanced.
- **OT5.** The 4-component template ADAPTATION for inference (what stays the same as vocabulary-breadth's; what adapts; particularly: how does the gap-filling-test with named actions work).
- **OT6.** Language-agnosticism check per level.
- **OT7.** The A1↔A2 boundary for inference-capacity (general educated inference vs domain-specialist inference patterns: legal reasoning conventions; mathematical proof inference; medical clinical reasoning; specialist-domain implicit-meaning conventions).
- **OT8.** Cross-sub-field interaction with the other A1 sub-fields (especially syntactic-processing-capacity — they're related but distinct: parsing dense subordination vs filling implicit steps; and with cultural-reference-recognition for allusion inference).

The user's seed framing additionally specifies the kinds of phenomena: "ellipses, gaps, 'what the author means without saying it,' compressed or elliptical prose ... a Said Nursi passage that telescopes a five-step logical chain into one sentence."

## Goal

- **Criterion.** Five mutually distinct, ordinally meaningful, spectrum-covering levels for inference-capacity — each operationalizable as a translator-AI prompt instruction (so the AI knows which gaps to fill explicitly, which to leave implicit), each with explicit distinguishing logic, each language-agnostic at concept level. The 4-component template adapts MEDIUM-heaviness from vocabulary-breadth's.
- **Use case.** The user will commit these as the `inference_capacity: Literal[...]` enum values; the per-level prose becomes part of the translator-AI's prompt context; the boundaries guide the AI in deciding gap-filling per level.
- **Desired outcome.** A stable, named, defined set of 5 inference-capacity levels with adapted-component definition + distinguishing logic + 3–5 concrete textual examples per level; ready for the user to commit to the schema and move to the last remaining A1 sub-field (cultural-reference-recognition).
- **What would fail.**
  - Levels defined only by example without explicit distinguishing logic.
  - Levels that overlap.
  - Levels that aren't ordinal (mixing categorical inference-types alongside ordinal capacity).
  - Level CONCEPTS that presuppose English-specific inference patterns.
  - Conflating inference-capacity with syntactic-processing-capacity (parsing dense syntax vs filling implicit steps — both interact but are distinct).
  - Conflating inference-capacity with cultural-reference-recognition (allusion inference combines both but is the cultural-ref sub-field's territory).
  - Conflating inference-capacity with vocabulary-breadth (knowing words ≠ inferring implicit meaning).
  - Addressing other A1 sub-fields when the user said inference-capacity only.
  - Mixing receptive and productive framing.
  - Failure to address the A1↔A2 boundary for inference (specialist-domain inference patterns).
  - Failure to adapt the substitution-test analogue.

## Source Input

```text
now do it for  inference-capacity
```

## Scope Check

Question covers goal: YES.

The Question targets the 5 levels of inference-capacity with names, concepts, distinguishing logic, examples, adapted template, A1↔A2 boundary, and cross-sub-field interactions. The Goal asks for those plus operationalizability and scope discipline.

**Specific-vs-pattern check.** User said "now do it for inference-capacity" — apply the same shape as prior siblings to this specific sub-field. Scope is the broader pattern of inference-capacity (compression / ellipsis / pragmatic / anaphora dimensions), not a single anchor case.

**Decoupling from other sub-fields:** explicit. Vocabulary-breadth (done), syntactic-processing-capacity (done), idiom-recognition (done), cultural-reference-recognition (next) are out of scope. The cross-sub-field interaction with syntactic-processing-capacity (parsing vs inference) and cultural-reference-recognition (allusion inference) are in scope only for boundary clarification.

**Decoupling from prior findings' commitments:** structural commitments inherited and treated as settled. Inherited Commitments Re-test in the finding.

**Template-adaptation in scope.** Likely MEDIUM heaviness: frequency-tier doesn't apply to inferences (inferences don't have Zipfian frequency); replace with inference-load tier (multiple sub-measures). Register-tier reframes as register/genre-tier (inference demand varies by genre). Substitution-test replaced by gap-filling test with named runtime actions.
