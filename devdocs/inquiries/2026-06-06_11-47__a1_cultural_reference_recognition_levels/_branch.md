# Branch: a1_cultural_reference_recognition_levels

## Question

The four prior inquiries in this chain have settled:
1. **`translation_config_axes`** — A1 Reader Level is a composite-axis with 5 sub-fields, of which **cultural-reference-recognition** is the 5th and last. Prior framing: "knowledge of cultural anchors, allusions, mythological/biblical/literary references, historical events used metonymically. A reader with low recognition needs 'crossing the Rubicon' / 'Achilles' heel' / 'Said Nursi's Sözler' to be inline-glossed or footnoted; a reader with high recognition catches them silently."
2. **`a1_vocabulary_breadth_levels`** — sub-field 1; original 4-component template.
3. **`a1_syntactic_processing_capacity_levels`** — sub-field 2; HEAVY template adaptation (structural-complexity tier + restructuring-test).
4. **`a1_idiom_recognition_levels`** — sub-field 3; LIGHT template adaptation (substitution-test → idiom-handling test); 12-entry dual-membership table forward-tagged for THIS inquiry.
5. **`a1_inference_capacity_levels`** — sub-field 4; MEDIUM template adaptation (inference-load tier + gap-filling test); 8-entry allusion-inference dual-membership table forward-tagged for THIS inquiry.

This inquiry takes the **same step for cultural-reference-recognition** — the sub-field that captures how many cultural anchors the reader catches silently and how many need to be made explicit. This is the FINAL sub-field of A1; after this, the A1 Reader Level composite-axis is fully specified across all 5 sub-fields.

Constraints inherited from the chain:
1. 5 ordinal levels, same labels (`very_basic | daily | conversational | advanced | native`).
2. Receptive only — recognizes references when encountered; doesn't produce them.
3. Language-agnostic at concept level — but cultural-canon CHOICE is unavoidably culture-bound (Greek myth vs Confucian classics vs Quranic anchors vs Hindu epics differ; the LEVEL framework must accommodate any target-culture canon, not lock English/Western references).
4. Conservative-bias-for-reader-axes = LOWER default.
5. Scope = cultural-reference-recognition ONLY (other A1 sub-fields out of scope; cross-sub-field dual-membership documented).
6. Template adaptation in scope — likely MEDIUM-to-LIGHT (cultural references behave LIKE ITEMS, similar to vocabulary and idioms; frequency-tier conceptually applies via canonicity tiers, but the dimension isn't Zipfian word-frequency — it's CANONICITY in a target audience's cultural literacy). The substitution-test analogue becomes **cultural-reference-handling test** with named runtime actions: INLINE-GLOSS / FOOTNOTE / DOMESTICATE (replace with target-culture analogue) / KEEP-AS-IS / EXPLICATE-FUNCTION (paraphrase what the reference is *doing*, e.g., "his decisive irreversible commitment" instead of "crossing the Rubicon").
7. **MUST INTEGRATE forward-tagged dual-membership lists from prior siblings:**
   - From `a1_idiom_recognition_levels`: 12-entry list (Achilles' heel, Pyrrhic victory, Crossing the Rubicon, Trojan horse, Catch-22, Big Brother, Cassandra, Pandora's box, Sword of Damocles, Sisyphean, Lazarus, Methuselah)
   - From `a1_inference_capacity_levels`: 8-entry list (He met his Waterloo, Joan of Arc, Crossing the Rubicon, Trojan horse, Cassandra, Sisyphean, Pyrrhic victory, Lazarus)
   - Each entry must be INDEPENDENTLY tagged from cultural-reference-recognition's frame (its place in the cultural canonicity tier; what handling action fires per level).

State the question: **For the cultural-reference-recognition sub-field of A1 Reader Level, what should the 5 ordinal levels be — what concept does each level capture (how many cultural anchors / allusions / mythological-biblical-literary-historical references the reader catches silently vs needs explicated), what logic distinguishes each level from its neighbors, and what concrete examples of culturally-loaded vs culturally-neutral text make each level operationally identifiable — defined language-agnostically at the concept level (despite cultural-canon choice being unavoidably culture-bound), with a 4-component definition template adapted as needed from the vocabulary-breadth template (frequency-tier → canonicity-tier; substitution-test → cultural-reference-handling test), AND independently re-tagging the forward-tagged dual-membership cases from `a1_idiom_recognition_levels` (12 entries) and `a1_inference_capacity_levels` (8 entries) from this sub-field's frame?**

Multiple observation targets:
- **OT1.** The 5 level NAMES (same labels per same-labels-for-default-propagation; validate that the labels carry sensible cultural-reference-recognition semantics).
- **OT2.** The CONCEPT each level captures (one sentence per level: how many cultural anchors the reader catches silently).
- **OT3.** The distinguishing LOGIC between adjacent levels (likely along CANONICITY DEPTH: ubiquitous-canon / educated-mainstream / literary-educated / specialist-canon / scholar-canon).
- **OT4.** Concrete EXAMPLES at each level — pairs of culturally-loaded vs culturally-neutral text. Cross-cultural illustration MUST appear (Greek + Biblical + Confucian + Quranic + Hindu/Sanskrit + literary-secular) to keep canon-choice culture-bound but level-framework language-agnostic.
- **OT5.** The 4-component template ADAPTATION for cultural-reference (what stays; what adapts: canonicity-tier replaces frequency-tier; cultural-reference-handling test with 5 named primary actions).
- **OT6.** Language-agnosticism check per level — the level FRAMEWORK is language-agnostic; per-reader CANON membership is culture-specific. Make this distinction explicit.
- **OT7.** The A1↔A2 boundary for cultural-reference-recognition (general cultural-canonical knowledge vs domain-specialist references: legal-history precedents, mathematical-naming conventions like Cantor/Gödel/Erdős, scientific-canonical figures like Maxwell/Bohr, medical-eponymic references like Charcot/Alzheimer).
- **OT8.** Cross-sub-field DUAL-MEMBERSHIP integration with both `a1_idiom_recognition_levels` (12-entry list) and `a1_inference_capacity_levels` (8-entry list) — each entry independently tagged from cultural-reference's frame.
- **OT9.** Completion of the A1 Reader Level composite-axis — this inquiry CLOSES the chain. Document the chain's closure (all 5 sub-fields now specified; ready for the schema commitment + the A1 vs A2 split inquiry).

The user's seed framing additionally specifies: cultural anchors include "Greek/Roman mythology, Biblical references, literary canonical figures (Hamlet, Don Quixote, Faust), historical events used metonymically (Waterloo, the Rubicon, Pearl Harbor), allusive proper nouns (a Cassandra, a Sisyphean task, a Trojan horse), genre-fixed references (Big Brother, Catch-22 from Orwell/Heller), and project-specific Said Nursi references (Sözler, Risale-i Nur, named lakaps)."

## Goal

- **Criterion.** Five mutually distinct, ordinally meaningful, spectrum-covering levels for cultural-reference-recognition — each operationalizable as a translator-AI prompt instruction (so the AI knows which references to gloss/footnote/domesticate/keep), each with explicit distinguishing logic, each language-agnostic at concept level. The 4-component template adapts MEDIUM-to-LIGHT heaviness from vocabulary-breadth's. The forward-tagged dual-membership cases from idiom-recognition and inference-capacity are independently re-tagged.
- **Use case.** The user will commit these as the `cultural_reference_recognition: Literal[...]` enum values; the per-level prose becomes part of the translator-AI's prompt context; the boundaries guide the AI in deciding cultural-reference handling per level.
- **Desired outcome.** A stable, named, defined set of 5 cultural-reference-recognition levels with adapted-component definition + distinguishing logic + 3–5 concrete textual examples per level (across multiple cultural canons); plus the 20-entry independent re-tagging of forward-flagged dual-membership cases. Ready for the user to commit to the schema and proceed to the A1 vs A2 split inquiry (the next conceptual step after A1 is fully specified).
- **What would fail.**
  - Levels defined only by example without explicit distinguishing logic.
  - Levels that overlap.
  - Levels that aren't ordinal (mixing categorical canon-types alongside ordinal recognition-depth).
  - Level CONCEPTS that lock to Greek/Roman/Biblical canon as definitional (cultural-canon must be configurable; level framework is language-agnostic).
  - Failure to make the canon-choice-is-culture-bound vs level-framework-is-language-agnostic distinction explicit.
  - Conflating cultural-reference-recognition with vocabulary-breadth (knowing the proper noun ≠ recognizing its allusive function).
  - Conflating cultural-reference-recognition with idiom-recognition (some overlap — the 12-entry list — but allusion ≠ idiom; idioms can be culturally-neutral, allusions point at a specific cultural anchor).
  - Conflating cultural-reference-recognition with inference-capacity (allusion-inference overlap — the 8-entry list — but recognizing the reference ≠ inferring what it means in context; one is identification, the other is compression-unpacking).
  - Addressing other A1 sub-fields when the user said cultural-reference-recognition only.
  - Mixing receptive and productive framing.
  - Failure to address the A1↔A2 boundary for cultural-references (domain-specialist canons).
  - Failure to adapt the substitution-test analogue.
  - Failure to independently re-tag the forward-flagged dual-membership cases from prior siblings.
  - Failure to acknowledge A1-composite closure (this is the chain's final sub-field; the document should mark the closure cleanly).

## Source Input

```text
now do it for  cultural-reference-recognition
```

## Scope Check

Question covers goal: YES.

The Question targets the 5 levels of cultural-reference-recognition with names, concepts, distinguishing logic, examples (cross-cultural), adapted template, A1↔A2 boundary, cross-sub-field dual-membership re-tagging, and explicit chain-closure marking. The Goal asks for those plus operationalizability and scope discipline.

**Specific-vs-pattern check.** User said "now do it for cultural-reference-recognition" — apply the same shape as prior siblings to this specific sub-field. Scope is the broader pattern of cultural-reference-recognition (canonicity tiers, recognition depth across cultural canons), not a single anchor case. The 20 forward-tagged dual-membership cases ARE specific examples and must be re-tagged independently.

**Decoupling from other sub-fields:** explicit. Vocabulary-breadth (done), syntactic-processing-capacity (done), idiom-recognition (done), inference-capacity (done) are out of scope, EXCEPT for the dual-membership integration which is explicitly in scope per Sub-field 3 and Sub-field 4's forward-tagging commitments.

**Decoupling from prior findings' commitments:** structural commitments inherited and treated as settled. Inherited Commitments Re-test in the finding will be REQUIRED (this inquiry consumes prior outputs — see Synthesis Trigger).

**Template-adaptation in scope.** Likely MEDIUM-to-LIGHT heaviness: cultural references are ITEMS (like vocabulary words, like idioms) but with a different dimension — canonicity-in-target-culture rather than Zipfian word-frequency or idiomaticity. Adapt frequency-tier → canonicity-tier (5 tiers: ubiquitous / educated-mainstream / literary-educated / specialist-canonical / scholar-canonical). Register-tier reframes as register/canon-tier (the cultural canon the text references). Substitution-test replaced by cultural-reference-handling test with named runtime actions: INLINE-GLOSS / FOOTNOTE / DOMESTICATE / KEEP-AS-IS / EXPLICATE-FUNCTION.

**Chain-closure flag in scope.** This is sub-field 5 of 5. The finding must mark the closure of the A1 Reader Level composite-axis. The next conceptual step (A1 vs A2 split inquiry, then audience-fidelity and other axes) is the user's call to start.

## Synthesis Trigger

This inquiry consolidates / synthesizes commitments from FOUR prior inquiry outputs:

- `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — root architectural finding: A1 Reader Level is a composite-axis with 5 sub-fields including cultural-reference-recognition; 4-layer / 4-family / 8-axis architecture; conservative-bias-for-reader-axes principle.
- `devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/finding.md` — sub-field 1: original 4-component template (reader-profile + frequency-tier + register-tier + substitution-test); same-labels-for-default-propagation; A1↔A2 split.
- `devdocs/inquiries/2026-06-05_17-05__a1_syntactic_processing_capacity_levels/finding.md` — sub-field 2: HEAVY adaptation (structural-complexity tier + restructuring-test); receptive-only commitment; cross-sub-field independence with vocab.
- `devdocs/inquiries/2026-06-05_18-03__a1_idiom_recognition_levels/finding.md` — sub-field 3: LIGHT adaptation (idiom-handling test with 4 named actions); strength-graded handling; 12-entry cross-sub-field dual-membership list FORWARD-TAGGED for this inquiry.
- `devdocs/inquiries/2026-06-05_18-38__a1_inference_capacity_levels/finding.md` — sub-field 4: MEDIUM adaptation (inference-load tier with 6 sub-measures + gap-filling test with 6 actions); orthogonality with syntactic-processing-capacity made explicit; 8-entry allusion-inference dual-membership list FORWARD-TAGGED for this inquiry.

Inherited commitments to re-test (non-exhaustive; finding's `## Inherited Commitments Re-test` will enumerate fully):
- Same-labels-for-default-propagation (`very_basic | daily | conversational | advanced | native`).
- Conservative-bias-for-reader-axes = LOWER default.
- Receptive-only commitment.
- Language-agnostic at concept level (with the cultural-canon-choice caveat made explicit here).
- 4-component template adapts as needed.
- A1↔A2 boundary defined per sub-field.
- Cross-sub-field dual-membership handled INDEPENDENTLY per sub-field (re-tag the 12 idiom-flagged + 8 inference-flagged entries here).
- Orthogonality with siblings (specifically: cultural-reference-recognition vs idiom-recognition vs inference-capacity vs vocabulary-breadth — explicit boundary).
- A1 composite-axis closure marker (this inquiry closes the 5-sub-field chain).

The discipline work (Sensemaking and Critique especially) will actually re-test these commitments, not merely record the inheritance.
