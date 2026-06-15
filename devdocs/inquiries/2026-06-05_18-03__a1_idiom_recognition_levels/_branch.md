# Branch: a1_idiom_recognition_levels

## Question

The three prior inquiries in this chain have settled:
1. **`translation_config_axes`** — A1 Reader Level is a composite-axis with 5 sub-fields, of which **idiom-recognition** is the 3rd. Prior framing: "ability to read figurative expressions figuratively (not literally). A high-recognition reader sees 'kick the bucket' and understands 'die'; a low-recognition reader takes it literally or freezes on the unfamiliar phrase."
2. **`a1_vocabulary_breadth_levels`** — sub-field 1; 5 levels with 4-component template (reader-profile + frequency-tier + register-tier + substitution-test).
3. **`a1_syntactic_processing_capacity_levels`** — sub-field 2; 5 levels with an ADAPTED 4-component template (structural-complexity tier replacing frequency-tier; register/genre-tier reframed; restructuring-test replacing substitution-test).

This inquiry takes the **same step for idiom-recognition** — the sub-field that captures whether figurative expressions land figuratively (`kick the bucket` → "die") or get taken literally / freeze the reader.

Constraints inherited from the chain:
1. 5 ordinal levels, same labels (`very_basic | daily | conversational | advanced | native`) for default-propagation from A1 headline.
2. Receptive-only — recognition not production; "recognizes the figurative meaning when encountered," not "uses idioms in writing."
3. Language-agnostic at concept level — every language has idioms with frequency gradients and register variation; English examples are illustrative.
4. Conservative-bias-for-reader-axes = LOWER default (assume less idiom recognition; user dials UP).
5. 4-component template ADAPTED if needed — for idioms, the template may be closer to vocabulary-breadth's (since idioms have frequency distributions and register tiers like vocabulary does, unlike syntax) but the substitution-test analogue is different: for idioms, the translator's runtime action is HANDLING (paraphrase / familiar equivalent / inline gloss / footnote / literal-with-explanation).
6. Scope discipline: **idiom-recognition ONLY.** The 2 remaining A1 sub-fields (inference-capacity, cultural-reference-recognition) are out of scope.

State the question: **For the idiom-recognition sub-field of A1 Reader Level, what should the 5 ordinal levels be — what concept does each level capture (which kinds of idioms the reader recognizes figuratively rather than literally), what logic distinguishes each level from its neighbors, and what concrete idiom examples make each level operationally identifiable — defined language-agnostically at the concept level (English idiom examples allowed for illustration), and using a 4-component definition template adapted as needed from the vocabulary-breadth template?**

Multiple observation targets:
- **OT1.** The 5 level NAMES (same labels per same-labels-for-default-propagation; validate that the labels carry sensible idiom-recognition semantics).
- **OT2.** The CONCEPT each level captures (one sentence per level: what kinds of idioms does the reader recognize figuratively?).
- **OT3.** The distinguishing LOGIC between adjacent levels (what makes `very_basic` idiom-recognition different from `daily`? what makes `advanced` different from `native`? — the principle that draws each boundary, likely along idiom-FREQUENCY and idiom-REGISTER dimensions).
- **OT4.** Concrete EXAMPLE IDIOMS at each level (English idiom examples by frequency band: universally-known idioms like "piece of cake"; common conversational idioms like "kick the bucket"; literary/archaic idioms like "give up the ghost"; etc.).
- **OT5.** The 4-component template ADAPTATION for idioms (what stays the same as vocabulary-breadth's, what adapts; particularly: how does the substitution-test analogue work — is it a "paraphrase-test" / "idiom-handling test" with named actions PARAPHRASE / FAMILIAR-EQUIVALENT / INLINE-GLOSS / FOOTNOTE?).
- **OT6.** Language-agnosticism check per level (the level CONCEPT works for any target language; specific idioms differ per language but the frequency-and-register gradient is universal).
- **OT7.** The A1↔A2 boundary for idioms (general idioms vs domain-specialist idioms — e.g., financial "below the line"; legal "with all deliberate speed"; sports "in the home stretch"; medical jargon idioms).
- **OT8.** Cross-sub-field interaction with cultural-reference-recognition (some idioms are cultural references like "crossing the Rubicon," "Achilles' heel"; sensemaking should clarify the boundary between A1.idiom-recognition and A1.cultural-reference-recognition).

The user's prior framing (carried from `translation_config_axes`) additionally specifies the kinds of phenomena: "ability to read figurative expressions figuratively (not literally). A high-recognition reader sees 'kick the bucket' and understands 'die'; a low-recognition reader takes it literally or freezes on the unfamiliar phrase."

## Goal

- **Criterion.** Five mutually distinct, ordinally meaningful, spectrum-covering levels for idiom-recognition — each operationalizable as a prompt instruction for the translator-AI (so the AI knows which idioms to KEEP, which to PARAPHRASE, which to GLOSS), each with explicit distinguishing logic, each language-agnostic at concept level. The 4-component template adapts from vocabulary-breadth's; components are kept where they fit and replaced where they don't.
- **Use case.** The user will commit these as the `idiom_recognition: Literal[...]` enum values in the pydantic schema; the per-level prose will become part of the translator-AI's prompt context; the boundaries will guide the AI in deciding idiom-handling per level.
- **Desired outcome.** A stable, named, defined set of 5 idiom-recognition levels with adapted-component definition + distinguishing logic + 5–10 concrete English idiom examples per level; ready for the user to commit to the schema and move to the next sub-field.
- **What would fail.**
  - Levels defined only by example without explicit distinguishing logic.
  - Levels that overlap (two adjacent levels could describe the same reader's idiom recognition).
  - Levels that aren't ordinal (mixing categorical idiom-source distinction like "biblical idioms" vs "sports idioms" alongside ordinal complexity).
  - Level CONCEPTS that presuppose English-specific idioms as the defining axis (Greek-mythology-derived English idioms aren't universal; the CONCEPT — idiom-frequency × register — is universal).
  - Conflating idiom-recognition with vocabulary-breadth (an idiom can be all daily-vocabulary words combined non-literally, like "kick the bucket"; recognizing the figurative meaning is a separate cognitive capacity).
  - Conflating idiom-recognition with cultural-reference-recognition (the boundary needs explicit handling — some expressions sit at both, like "Achilles' heel").
  - Conflating idiom-recognition with syntactic-processing-capacity (idioms have their own syntactic patterns but the figurative recognition is a separate dimension).
  - Addressing the 2 remaining A1 sub-fields (inference-capacity, cultural-reference-recognition) when the user explicitly said idiom-recognition only.
  - Mixing receptive and productive framing.
  - Failure to address the A1↔A2 boundary for idioms.
  - Failure to adapt the substitution-test analogue (the translator's runtime action for idioms is HANDLING — paraphrase, familiar-equivalent, gloss, footnote — not lexical substitution).

## Source Input

```text
now lets do the same for idiom-recognition
```

## Scope Check

Question covers goal: YES.

The Question targets the 5 levels of idiom-recognition with names, concepts, distinguishing logic, idiom examples, and the adapted 4-component template (including the A1↔A2 boundary and cross-sub-field interactions). The Goal asks for those plus operationalizability, language-agnosticism, scope discipline.

**Specific-vs-pattern check.** The user said "now lets do the same for idiom-recognition" — the "do the same" phrasing refers to applying the same shape/pattern as the prior two sibling inquiries (vocabulary-breadth, syntactic-processing-capacity). The inquiry addresses the SPECIFIC sub-field (idiom-recognition), not a meta-pattern abstraction.

**Decoupling from other sub-fields:** explicit. Vocabulary-breadth (done), syntactic-processing-capacity (done), inference-capacity (next), cultural-reference-recognition (last) are out of scope. The cross-sub-field interaction between idiom-recognition and cultural-reference-recognition is in scope to clarify the BOUNDARY between them (not to spec cultural-reference-recognition itself).

**Decoupling from prior findings' commitments:** structural commitments (composite-axis pattern, receptive-only, language-agnostic at concept, same-labels-across-A1-sub-fields, conservative-bias-for-reader-axes-LOWER-default, A1↔A2 boundary as separate per-sub-field test, 4-layer architecture) are INHERITED and treated as settled. The finding will include `## Inherited Commitments Re-test` per CONCLUDE's policy when refining a prior finding.

**Template-adaptation in scope.** Idioms have frequency distributions and register tiers similar to vocabulary (unlike syntactic structures, which don't have Zipfian frequency). So the frequency-tier and register-tier components from vocabulary-breadth's template may apply directly OR with light reframing as `idiom-frequency tier` and `idiom-register tier`. The substitution-test almost certainly needs replacement — the runtime action for idioms is HANDLING (paraphrase / familiar-equivalent / inline-gloss / footnote / literal-with-explanation), not lexical substitution.
