---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-05_18-38__a1_inference_capacity_levels/finding.md
---
# Finding: A1 Reader Level — Cultural-Reference-Recognition Sub-Field (the 5 Levels)

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-05_18-38__a1_inference_capacity_levels/finding.md` (the inquiry that specified the 5 levels for inference-capacity, the 4th of 5 sub-fields of A1 Reader Level)

**Revision trigger:** This inquiry takes the same shape — define the 5 ordinal levels — for the FIFTH and FINAL sub-field of A1 Reader Level. The user's directive "now do it for cultural-reference-recognition" continues the chain.

**What's preserved:**
- Same 5 ordinal labels (`very_basic | daily | conversational | advanced | native`) per the same-labels-for-default-propagation principle established in `a1_vocabulary_breadth_levels` (the first sub-field's finding; original 4-component template source).
- Conservative-bias-for-reader-axes (LOWER default — the translator-AI assumes lower recognition unless explicitly configured higher).
- Receptive-only commitment (the reader recognizes references when encountered; does not produce them).
- Per-sub-field A1↔A2 boundary handling (each sub-field defines its own boundary between general reader-level concerns and domain-specialist concerns).
- Cross-sub-field dual-membership handled INDEPENDENTLY per sub-field (each sub-field re-tags overlap cases from its own frame).
- 4-component template adapts as needed per sub-field (the recurring pattern across all 5 sub-fields).

**What's changed:**
- **Template adaptation tagged MEDIUM-to-LIGHT.** This sits between the LIGHT adaptation in `a1_idiom_recognition_levels` (idiom-recognition, the 3rd sub-field; only the substitution-test was renamed there) and the HEAVY adaptation in `a1_syntactic_processing_capacity_levels` (syntactic-processing-capacity, the 2nd sub-field; structural-complexity tier + restructuring-test). Specifically: the `frequency-tier` component is REPLACED with a `canonicity-tier` (a more substantial change than idiom's reuse of frequency for idiom-density, but less invasive than syntax's full structural-complexity tier); the `register-tier` is REFRAMED as `register/canon-tier` (genre-conditioned canon); the `substitution-test` is REPLACED with a `cultural-reference-handling test` with 5 named primary actions.
- **Markedness and transparency are explicitly placed on the TEXT/REFERENCE side**, orthogonal to the reader-level. This is a new commitment unique to this inquiry — the prior siblings did not need to make this text-side-vs-reader-side distinction explicit because their dimensions (word frequency, sentence complexity, idiomaticity, inference compression) are more straightforwardly reader-property-derivable.
- **Action policy is project-specific and DISFAVORS the DOMESTICATE action**, anchored to the user's persistent memory commitment about translation register fidelity ("don't pull plain source registers up into ornate/archaic English") and Lawrence Venuti's foreignization ethics. Prior siblings did not have an analogous cross-cutting policy because their handling actions (vocabulary substitution, syntactic restructuring, idiom paraphrase, gap-filling) are less ethically loaded than cultural domestication.

**What's new:**
- **Reader-relative canon commitment.** The level captures what THE READER recognizes (target-reader-relative); not what the source text references. This is explicitly distinguished from a hypothetical source-canon-density (which would be a TEXT property, not a reader property).
- **Canon-choice as a separate audience-level configuration concern** (out of scope here). The level framework operates over a presumed-target canon; the choice of canon (Greek/Roman vs Biblical vs Confucian vs Quranic vs Hindu/Sanskrit vs Persian vs the project's Said Nursi corpus) belongs at the audience level, not at the per-reader cultural-reference-recognition sub-field.
- **Cross-sub-field dual-membership table for cultural-reference-recognition.** The 20 entries forward-flagged by `a1_idiom_recognition_levels` (12 entries) and `a1_inference_capacity_levels` (8 entries; 6 overlap with the idiom list) are re-tagged INDEPENDENTLY here from cultural-reference's frame — assigning each entry a cultural-ref canonicity tier and a per-level handling action.
- **A1 Composite-Axis Chain Closure marker.** This inquiry CLOSES the 5-sub-field chain that constitutes A1 Reader Level. After this finding, the A1 composite-axis is fully specified across all 5 sub-fields and is ready for schema commitment.
- **Triple-overlap union rule.** When a single reference fires multiple sub-fields simultaneously (the canonical case: "Crossing the Rubicon" fires idiom-recognition + cultural-reference-recognition + inference-capacity), the translator-AI applies the UNION of the per-sub-field handling rules (or the most-explicating action), determined per-sub-field-level on the reader's per-sub-field configuration. This rule is needed to prevent indeterminacy and is added per Critique's refinement note on CC-E (the sibling-orthogonality piece).

**Migration:** No migration needed — this is a new sub-field specification. When the user commits the A1 schema, this sub-field's enum becomes `cultural_reference_recognition: Literal["very_basic", "daily", "conversational", "advanced", "native"]` parallel to the other 4 sub-fields' enums.

---

## Question

For the cultural-reference-recognition sub-field of A1 Reader Level — the FIFTH and FINAL sub-field — what should the 5 ordinal levels be?

Specifically: what concept does each level capture (how many cultural anchors / allusions / mythological-biblical-literary-historical references the reader catches silently versus needs explicated), what logic distinguishes each level from its neighbors, and what concrete examples make each level operationally identifiable — defined language-agnostically at the concept level (despite cultural-canon choice being unavoidably culture-bound), with a 4-component definition template adapted from the vocabulary-breadth template — AND independently re-tagging the 20 forward-flagged dual-membership cases from `a1_idiom_recognition_levels` (12 entries) and `a1_inference_capacity_levels` (8 entries)?

The goal: five mutually distinct, ordinally meaningful, spectrum-covering levels operationalizable as translator-AI prompt instructions (so the AI knows which references to gloss/footnote/keep/explicate-function/domesticate); each with explicit distinguishing logic; each language-agnostic at level-framework concept; with the 20-entry dual-membership re-tagging table integrated; closing the A1 5-sub-field chain.

---

## Finding Summary

- **5 ordinal levels with the same labels as prior siblings.** `very_basic | daily | conversational | advanced | native` — applied to cultural-reference-recognition. Same-labels-for-default-propagation across all 5 A1 sub-fields makes a single user-level configuration possible (the user sets `reader_level = daily` once, and "daily" propagates across vocabulary, syntax, idiom, inference, and cultural-reference unless any sub-field is explicitly overridden).

- **Primary dimension is CANONICITY DEPTH within a presumed-target cultural canon.** A reference is canonical when it belongs to the shared knowledge a member of the target audience's culture is expected to recognize. Canonicity stratifies: some references are ubiquitous (everyone catches), others are educated-mainstream (high-school-educated catches), others literary-educated (humanities-degree catches), specialist-canonical (domain-specialist catches), or scholar-canonical (canon-scholars catch). The 5-tier stratification comes from cultural-literacy research (E.D. Hirsch's *Cultural Literacy* + Pierre Bourdieu's cultural-capital strata) and maps 1-to-1 to the 5 reader levels.

- **Level is TARGET-READER-RELATIVE, not source-text-relative.** The configuration specifies what THE READER recognizes. A Western-secular reader is `very_basic` for the Quranic canon regardless of whether they're reading Said Nursi (whose source canon is Islamic-Sufi). The translator-AI uses this to decide handling actions; the source text's canon-density is a runtime observation the AI makes from the text itself, not part of the reader-level configuration.

- **Canon-choice is OUT OF SCOPE here.** It belongs at the audience level — an `audience.canon_set: list[str]` field would specify which canons the reader's recognition operates over (e.g., `["greek_roman", "biblical", "literary_western", "said_nursi_corpus"]`). The level framework here works ON a presumed-target canon; multi-canon audiences would need per-canon reader-level configuration (a future inquiry concern).

- **Markedness and transparency are TEXT/REFERENCE properties, not level dimensions.** A reference is MARKED when the source signposts it ("as the Greeks said...") and UNMARKED when not. A reference is TRANSPARENT when it functions metaphorically without source-knowledge (the "Trojan horse" works as a metaphor for "deceptive gift" even if the reader doesn't know the *Iliad*), and OPAQUE when it doesn't ("Catch-22" means nothing without Joseph Heller). These two properties modulate the translator-AI's runtime handling-action choice — but they are properties of the text and the reference, not of the reader, so they are not part of the reader-level definition.

- **5 primary handling actions, structurally at parity (Newmark / Aixelá translation-procedure taxonomy):** INLINE-GLOSS (append brief explanation inside the translation), FOOTNOTE (externalize the explanation), DOMESTICATE (replace with target-culture analogue), KEEP-AS-IS (preserve and trust reader recognition), EXPLICATE-FUNCTION (paraphrase what the reference is *doing* without naming it — e.g., "his decisive irreversible commitment" instead of "his crossing of the Rubicon").

- **Project-specific policy DISFAVORS DOMESTICATE; EXPLICATE-FUNCTION is the foreignization-preserving alternative.** Anchored to the user's persistent memory about translation register fidelity ("don't pull plain source registers up into ornate/archaic English" — implies preserving source-cultural character) and Venuti's foreignization ethics. The action preference order is: KEEP-AS-IS → INLINE-GLOSS → EXPLICATE-FUNCTION → FOOTNOTE → DOMESTICATE (last resort). DOMESTICATE remains in the taxonomy for structural completeness but is reserved for the edge case of `very_basic` + opaque + unmarked + EXPLICATE-FUNCTION-would-burden-the-text.

- **4-component template adapts MEDIUM-to-LIGHT from the vocabulary-breadth template.** Component 1 (reader profile) is kept verbatim. Component 2 (frequency-tier) is REPLACED with canonicity-tier. Component 3 (register-tier) is REFRAMED as register/canon-tier (different genres invoke different canons; a sermon draws from religious canon, a newspaper from current-events canon, a literary novel from literary canon). Component 4 (substitution-test) is REPLACED with a cultural-reference-handling test that runs the 5 named primary actions.

- **A1↔A2 boundary criterion.** General cultural-canonical knowledge stays in A1 (cultural-reference-recognition is a reader-level concern). Domain-specialist canons move to A2 (Domain Expertise — a separate sub-field family in the configuration architecture). Five specialist-domain canons illustrate the boundary: legal-history precedents (Marbury v. Madison; Roe v. Wade), mathematical figures (Cantor's diagonal; Gödel; Erdős; Russell's paradox), scientific figures (Maxwell; Bohr; Pasteur; Feynman), medical eponyms (Alzheimer; Parkinson; Charcot; Hodgkin), and specialist philosophy (Heideggerian; Wittgensteinian beyond the popular-cultural "Wittgenstein"). Gray-zone cases are acknowledged: Einstein has migrated from specialist to general; Pythagorean theorem similarly; Marx's canonicity tier varies by political-canon.

- **Translator-AI runtime determination mechanism is explicit.** The reader-level configuration specifies what the READER recognizes. The AI determines a specific reference's canonicity tier, transparency, and markedness AT RUNTIME from its training. The two are complementary: configuration tells the AI the reader; the AI's knowledge tells it about each reference encountered; the action rule resolves the cross-product.

- **20-entry dual-membership table re-tags forward-flagged cases independently from cultural-reference's frame.** 12 entries forward-flagged by `a1_idiom_recognition_levels`, 8 entries forward-flagged by `a1_inference_capacity_levels` (with 6 entries appearing in both lists → deduplicated to 14 unique entries + 6 dual-origin entries). Most cluster around the educated-mainstream canonicity tier; a few are ubiquitous (Trojan horse, Big Brother) or literary-educated (Joan of Arc).

- **A1 Composite-Axis Chain Closure.** This finding CLOSES the 5-sub-field chain that constitutes A1 Reader Level. The 5 sub-fields are: vocabulary-breadth, syntactic-processing-capacity, idiom-recognition, inference-capacity, and cultural-reference-recognition. Each is now specified with 5 ordinal levels and an adapted 4-component template. The user can now commit the A1 schema and proceed to the next conceptual step (the A1↔A2 split inquiry — what goes into A1 as reader concerns vs A2 as domain-expertise concerns).

- **Triple-overlap union rule** for references that fire multiple sub-fields simultaneously: the translator-AI applies the union of per-sub-field handling rules, with the most-explicating action winning when actions conflict.

---

## Finding

The 5 prior inquiries in this chain established A1 Reader Level as a composite-axis with 5 sub-fields, of which cultural-reference-recognition is the 5th and final. The translation-configuration framework being built ("Comprehenslate" — the user's AI-assisted translation project at this repository) needs each sub-field specified with 5 ordinal levels because the configuration is what the translator-AI receives as prompt context to decide, at runtime, how to handle each cultural reference it encounters in the source text. Without these per-level definitions, the AI either over-glosses (insulting a fluent reader) or under-glosses (losing a less-fluent reader). The 5 levels are the resolution between those two failure modes.

### 1. The Framework

#### 1.1 The 5 levels and the 5-tier canonicity ladder

The 5 ordinal labels are the same across all 5 A1 sub-fields: `very_basic | daily | conversational | advanced | native`. This is by design — same-labels-for-default-propagation, established in `a1_vocabulary_breadth_levels` (the first sub-field's finding). A single user-level configuration ("daily") propagates across all 5 sub-fields unless any is explicitly overridden.

For cultural-reference-recognition specifically, the 5 levels map 1-to-1 to a 5-tier canonicity ladder drawn from cultural-literacy research (primarily Hirsch's *Cultural Literacy*, 1987, with Bourdieu's cultural-capital stratification supporting the layered tier model). The ladder runs from ubiquitous (known to virtually any member of the target audience's culture) to scholar-canonical (known only to specialists in the relevant canon):

| Reader level | Canonicity tier recognized | Tier description |
|---|---|---|
| `very_basic` | ubiquitous-canon (unreliably) | The reader recognizes only the most widely-shared cultural anchors, and even those with gaps. They have heard "Garden of Eden" and "Trojan horse" but may not connect them to specific canonical sources. |
| `daily` | ubiquitous + first slice of educated-mainstream | The reader catches ubiquitous references reliably and begins to recognize educated-mainstream references in well-known contexts (a "David and Goliath" matchup; a "Big Brother is watching" reference). |
| `conversational` | ubiquitous + educated-mainstream (complete) | The reader catches the canonical set a high-school-educated member of the target culture would know — including most Greek/Roman myth-references in metonymic use ("Pyrrhic victory"; "Sword of Damocles"); standard Biblical references; canonical Shakespeare; canonical 20th-century literary references (Catch-22; Big Brother). |
| `advanced` | ubiquitous + educated-mainstream + literary-educated | The reader has a humanities-undergraduate-equivalent knowledge of the target canon. Catches mid-tier literary references (Dante's Beatrice; Madame Bovary; Jean Valjean), specialized Biblical references (Methuselah's longevity; Job's patience), and Roman political references (Caesar's wife; the Augustan age). |
| `native` | all 5 tiers (incl. specialist + scholar-canonical) | The reader catches references at the depth a specialist in the target canon would. Includes specialist literary references (Joyce's *Ulysses*; Bartleby), specialist canonical-figure references, and scholar-canonical references that only appear in canon-internal discussion. |

The "and only unreliably" qualifier at `very_basic` is intentional. The conservative-bias-for-reader-axes principle (established in the root architectural inquiry, `translation_config_axes`) says: when in doubt, the translator-AI assumes a LOWER reader recognition. At `very_basic`, the AI assumes that even ubiquitous references may be missed.

#### 1.2 The 4-component template (MEDIUM-to-LIGHT adapted)

The 4-component definition template was established in `a1_vocabulary_breadth_levels` (the original template-source inquiry). The four components are: (1) reader profile; (2) frequency-tier; (3) register-tier; (4) a substitution-test that the translator-AI runs to decide how to handle the encountered item. For each sub-field after vocabulary-breadth, the template ADAPTS as needed.

For cultural-reference-recognition, the adaptation is MEDIUM-to-LIGHT — meaning more invasive than the LIGHT adaptation in `a1_idiom_recognition_levels` (where only the substitution-test was renamed to idiom-handling-test) but less invasive than the HEAVY adaptation in `a1_syntactic_processing_capacity_levels` (where the frequency-tier was replaced with a structural-complexity tier with subcomponents and the substitution-test was replaced with a restructuring-test).

The 4 components for cultural-reference-recognition:

**Component 1: Reader profile.** Kept verbatim from vocabulary-breadth — a short paragraph naming the reader's age-range, education level, and cultural-canon exposure expectations. Same for every sub-field.

**Component 2: Canonicity-tier (replaces frequency-tier).** A specification of which canonicity tiers (ubiquitous / educated-mainstream / literary-educated / specialist-canonical / scholar-canonical) the reader at this level reliably recognizes. The replacement is needed because cultural references don't have Zipfian word-frequency in the way vocabulary does; the relevant stratification is recognition-depth-within-canon, which is canonicity.

**Component 3: Register/canon-tier (reframed from register-tier).** Different genres invoke different canons: a religious sermon draws from theological canon; a newspaper from current-events canon; a literary novel from literary canon; a scientific paper from scientific-canon (which sits more in A2's Domain Expertise territory). This component specifies which genre/canon combinations the reader at this level can handle without breaking comprehension.

**Component 4: Cultural-reference-handling test (replaces substitution-test).** The translator-AI runs this test per cultural reference encountered. The test names 5 primary actions: INLINE-GLOSS, FOOTNOTE, DOMESTICATE, KEEP-AS-IS, EXPLICATE-FUNCTION. The test specifies which action fires at this level given the reference's canonicity tier, transparency, and markedness.

#### 1.3 Reader-relative canon (not source-relative)

The level captures what THE READER recognizes — the configuration is a property of the reader, not of the source text. This matters because the source text and the target reader can have different canons. A canonical project case: Said Nursi's *Risale-i Nur* (the user's primary translation corpus) is written in a register saturated with Islamic-Sufi canonical references (prophets named in the Quran; Companions of the Prophet; medieval Sufi figures like Mevlana and Geylani; theological-school references like Maturidi and Ashari). The SOURCE canon is high-density-Islamic. The TARGET reader is often Western-secular, for whom this canon is `very_basic`. The same Nursi paragraph translated for a Turkish-Muslim audience would have the canon at `native`.

The level configuration captures the latter — what the reader brings — and the translator-AI cross-references this with what it observes in the source text to decide handling actions.

#### 1.4 Canon-choice is out of scope (separate audience-level config)

The level framework operates over a PRESUMED-TARGET canon. The CHOICE of canon — which canon the reader's recognition operates over — is a separate concern, belonging at the audience level. A reasonable schema design would have an `audience.canon_set: list[str]` field at the audience level, specifying which canons the reader recognizes. For multi-canon audiences (e.g., a reader equally fluent in Western and Islamic canon), the configuration would need per-canon reader-level values; that's a future inquiry concern, not addressed here.

The reason for splitting these concerns is structural: canonicity-depth and canon-choice are ORTHOGONAL axes. A reader can be `native` for Greek-Biblical canon and SIMULTANEOUSLY `very_basic` for Quranic canon. Treating them as one axis would force a single value per reader that loses the multi-canon literacy information.

#### 1.5 Markedness and transparency: text/reference properties, not level dimensions

Two reference-side properties modulate the translator-AI's runtime action choice but do not belong in the reader-level definition itself:

**Markedness** is a TEXT property. A reference is *marked* when the source explicitly signposts it ("as the ancient Greeks would say..."; "in the famous phrase of Marx..."). It is *unmarked* when the source assumes the reader catches the reference without help. Markedness affects which handling action fires (a marked reference at `very_basic` can KEEP the marker and INLINE-GLOSS the content; an unmarked reference at `very_basic` likely needs FOOTNOTE or EXPLICATE-FUNCTION). But markedness is not a reader-recognition-depth dimension — it's a text-side feature observable by the AI from the source.

**Transparency** is a REFERENCE property. A reference is *transparent* when it functions metaphorically without requiring the reader to identify its source (the "Trojan horse" works as a metaphor for "deceptive gift" even when the reader doesn't know the *Iliad*). It is *opaque* when it doesn't (Catch-22 is dead-meaningless without Joseph Heller's novel). Transparency affects whether KEEP-AS-IS is viable at low recognition (transparent references can; opaque references can't). But transparency is a property of the reference itself, not the reader.

Placing markedness and transparency on the text/reference side is a NEW commitment unique to this sub-field. The prior siblings did not need to make this distinction explicit because their reader-property dimensions (word frequency, sentence complexity, idiomaticity, inference-compression-depth) are more straightforwardly reader-derivable. Cultural references uniquely require disentangling reader-side recognition from text-side markedness and reference-side transparency.

#### 1.6 The 5 primary handling actions

The translator-AI's runtime action vocabulary is structurally at parity with the established translation-studies taxonomy (Peter Newmark's *A Textbook of Translation* + Javier Franco Aixelá's "Culture-Specific Items in Translation"):

| Action | Operation | Use when |
|---|---|---|
| **KEEP-AS-IS** | Preserve the reference verbatim; trust reader recognition | Reader's level meets the reference's canonicity tier; reference is transparent OR is marked enough to carry itself |
| **INLINE-GLOSS** | Append a brief explanation inside the translation ("the Sword of Damocles — an ever-present threat") | Reader's level is one tier below the reference's canonicity; reference is short and the gloss won't disrupt flow |
| **EXPLICATE-FUNCTION** | Paraphrase what the reference is *doing* without naming it ("his decisive irreversible commitment" instead of "his crossing of the Rubicon") | Reader is multiple tiers below; reference is opaque or culturally specific; foreignization-preservation matters |
| **FOOTNOTE** | Externalize the explanation to a note | Reference requires substantial unpacking; inline gloss would be too long; reader benefits from reference attribution |
| **DOMESTICATE** | Replace with a target-culture analogue | Last resort: very_basic + opaque + unmarked + EXPLICATE-FUNCTION would burden the text too much |

The translator-AI uses the action ladder per-reference at runtime, conditioned on the reader's configured level + the reference's canonicity tier (from AI's training) + the reference's transparency (from AI's training) + the reference's markedness (observable from the source text).

#### 1.7 Project-specific action policy: DOMESTICATE is disfavored

The above table places DOMESTICATE structurally at parity with the other 4 actions (because the underlying taxonomy treats them at parity). But this project's policy DISFAVORS DOMESTICATE in favor of EXPLICATE-FUNCTION at all levels.

The anchor for this policy has two parts:

**Anchor 1: User's persistent memory on translation register fidelity.** The user has explicitly stored the principle "don't pull plain source registers up into ornate/archaic English; C1 ≠ vocabulary display; preserve register alternation as Tier 1/2 structure" (see the `feedback_translation_register` memory file). The principle is about register, but its underlying commitment is preservation of source-cultural character — which extends to cultural-reference preservation when possible.

**Anchor 2: Lawrence Venuti's foreignization ethics** (*The Translator's Invisibility*, 1995). Venuti's argument: domesticating translation makes the translator invisible and erases the foreignness that gives the source its specificity; foreignization preserves the encounter with the source culture. For a translation project whose primary corpus is Said Nursi (a corpus where the Islamic-Sufi cultural specificity is load-bearing), foreignization is the ethical default.

The policy translates to a preference order:

```
KEEP-AS-IS  >  INLINE-GLOSS  >  EXPLICATE-FUNCTION  >  FOOTNOTE  >  DOMESTICATE (last resort)
```

EXPLICATE-FUNCTION is the foreignization-preserving alternative to DOMESTICATE at lower reader levels. Instead of replacing "the Sword of Damocles" with a target-culture analogue (DOMESTICATE), it paraphrases the function ("the ever-present threat hanging over him") which preserves Western-classical cultural specificity in the surrounding prose while making the immediate meaning accessible.

DOMESTICATE remains in the action vocabulary because it is the structurally correct last resort for the edge case of `very_basic` reader + opaque reference + unmarked + EXPLICATE-FUNCTION would burden the text excessively. It is NOT available at higher reader levels.

#### 1.8 Translator-AI runtime determination mechanism

A clean architectural distinction underlies the framework:

- **Configurable (specified by the user at config time):** the reader's `cultural_reference_recognition` level (one of the 5); the audience's canon-set (the canons the reader recognizes over); the project's action policy (DOMESTICATE-disfavored by default).
- **Runtime-determined (the translator-AI judges per encountered reference):** the specific reference's canonicity tier (which of the 5 tiers it sits in for the configured canon); the reference's transparency (does the metaphor work without source-knowledge?); the reference's markedness (does the source signpost it?).

The translator-AI uses the configurable inputs as constants for a translation pass and computes the runtime-determined properties per reference from its training. The action selection is then a deterministic function: `action = handling_test(reader_level, reference_canonicity, reference_transparency, reference_markedness, action_policy)`.

The prompt context for the translator-AI is the per-level prose in Section 2 plus this framework section.

### 2. The 5 Per-Level Definitions

Each level definition has the 4 components: reader profile, canonicity-tier (replaces frequency-tier), register/canon-tier (reframed), and cultural-reference-handling test (replaces substitution-test). Examples span multiple cultural canons (per Critique's CC-B refinement: ensure at least one non-Western canon example at each level).

#### 2.1 `very_basic`

**Reader profile.** The reader has minimal exposure to canonical cultural literacy. They have heard the most ubiquitous references but cannot reliably trace them to canonical sources. They are typically reading at a comprehension threshold; cultural references that aren't supported by inline explanation are likely to be missed.

**Canonicity-tier.** Recognizes ubiquitous-canon ONLY, and even those unreliably. Examples of ubiquitous references the reader might catch: "Garden of Eden" (Western-Biblical); "the Quran" (Islamic); "Buddha" (Buddhist); "Trojan horse" (Greek, transparent — the metaphor works even if the *Iliad* is unknown). References at higher tiers — Pyrrhic victory, Cassandra, Bovarysme, Faustian bargain — are not reliably caught.

**Register/canon-tier.** The reader handles current-events and everyday-conversational canon. Religious-sermon-canon, scientific-canon, and literary-canon all sit beyond the reader's reliable recognition. Cross-cultural specificity (Greek-vs-Quranic-vs-Confucian) is not navigated; the reader's recognition is effectively monocultural in their own background.

**Cultural-reference-handling test.** The AI assumes the reader will miss any non-ubiquitous reference. The action ladder fires aggressively: INLINE-GLOSS for short ubiquitous-canon references the reader might still miss; FOOTNOTE or EXPLICATE-FUNCTION for educated-mainstream and higher tiers; KEEP-AS-IS only when the reference is BOTH ubiquitous AND transparent (the "Trojan horse" can be kept as a metaphor; a "Pyrrhic victory" cannot). DOMESTICATE is the last resort for opaque-unmarked-educated references where EXPLICATE-FUNCTION would burden the text.

**Examples spread across canons:**
- *Greek/Roman*: "Trojan horse" → KEEP-AS-IS (transparent); "Pyrrhic victory" → EXPLICATE-FUNCTION ("a costly win that wasn't worth winning"); "Cassandra" → FOOTNOTE or INLINE-GLOSS.
- *Biblical*: "Garden of Eden" → KEEP-AS-IS; "David and Goliath" → KEEP-AS-IS (transparent); "Methuselah" → INLINE-GLOSS ("a very old man, like Methuselah").
- *Said Nursi corpus (non-Western)*: "Bediuzzaman" (Said Nursi's lakap) → FOOTNOTE; "Sözler" → INLINE-GLOSS or "The Words (Sözler)"; "İsm-i azam" → EXPLICATE-FUNCTION ("the greatest name of God").
- *Quranic*: "Prophet Musa" → INLINE-GLOSS ("Prophet Moses (Musa)"); references to *isra'* (the Night Journey) → FOOTNOTE.
- *Confucian (non-Western)*: "junzi" → EXPLICATE-FUNCTION ("the morally exemplary person"); "Confucius said" → KEEP-AS-IS (the name carries).

#### 2.2 `daily`

**Reader profile.** The reader has working cultural literacy at the level of an attentive consumer of mass media and general adult conversation. They catch ubiquitous references reliably and pick up some educated-mainstream references when context is supportive. The user's notes on a "backpacker-level conversational knowledge" reader approximately match this level.

**Canonicity-tier.** Reliably catches ubiquitous-canon; catches the first slice of educated-mainstream (the part that appears regularly in journalism and pop culture: Catch-22, Big Brother, David-and-Goliath as metaphor, Kafkaesque as adjective). Misses the deeper educated-mainstream that requires literary-historical exposure (Bovarysme, Goethe's Faust beyond "Faustian bargain", Roman political references like "Caesar's wife").

**Register/canon-tier.** Handles journalistic and current-events canon at the educated-mainstream tier. Catches well-known religious references at the ubiquitous tier (Good Samaritan; David and Goliath; Eden). Cross-cultural specificity begins to navigate (the reader can distinguish a Quranic reference from a Greek reference, even if not deeply understanding either).

**Cultural-reference-handling test.** KEEP-AS-IS for ubiquitous-canon (both transparent and opaque, since the reader catches them) and for the first slice of educated-mainstream (Big Brother; Catch-22; Kafkaesque). INLINE-GLOSS for deeper educated-mainstream (Pyrrhic victory; Sword of Damocles; Faustian bargain). EXPLICATE-FUNCTION for literary-educated and above. FOOTNOTE for specialist-canonical and scholar-canonical references the reader encounters but cannot place.

**Examples spread across canons:**
- *Greek/Roman*: "Pyrrhic victory" → INLINE-GLOSS or KEEP-AS-IS depending on transparency in context; "Crossing the Rubicon" → KEEP-AS-IS if marked + transparent; "Achilles' heel" → KEEP-AS-IS.
- *Biblical*: "Methuselah" → KEEP-AS-IS; "Job's patience" → KEEP-AS-IS or INLINE-GLOSS; "Lazarus" → KEEP-AS-IS for metaphoric ("Lazarus rising").
- *20th-c. literary*: "Big Brother" → KEEP-AS-IS; "Catch-22" → KEEP-AS-IS; "Kafkaesque" → KEEP-AS-IS.
- *Said Nursi corpus (non-Western)*: "Sözler" → INLINE-GLOSS as title; "Bediuzzaman" → FOOTNOTE explaining the lakap; "İsm-i azam" → INLINE-GLOSS.
- *Historical*: "Waterloo" → KEEP-AS-IS for "met his Waterloo" (the metaphor is sufficient); "Watergate" → KEEP-AS-IS.

#### 2.3 `conversational`

**Reader profile.** The reader has cultural literacy at the level of a college-educated adult who reads widely in journalism, mainstream literature, and general non-fiction. They handle the canonical references a high-school education + general adult reading would equip them for.

**Canonicity-tier.** Reliably catches the full educated-mainstream tier in addition to ubiquitous-canon. Misses literary-educated references that require humanities-undergraduate exposure (Dante's Beatrice; Madame Bovary; Jean Valjean as specifically Hugo's character vs as generic ex-convict; the Augustan Age).

**Register/canon-tier.** Handles educated-mainstream across genres: journalistic + religious-sermon at the canonical level + popular-literary canon (Shakespeare's most famous; Dickens's most famous). Cross-cultural specificity is reliably navigated for the dominant cultural canon of the reader's background, partial for adjacent canons.

**Cultural-reference-handling test.** KEEP-AS-IS for ubiquitous + educated-mainstream. INLINE-GLOSS for literary-educated when the reference is clearly invoked but the reader may not place it (mentioning "Karenin" in a context that needs Anna Karenina specifically). EXPLICATE-FUNCTION rarely needed; FOOTNOTE for the occasional specialist-canonical reference the reader cannot place.

**Examples spread across canons:**
- *Greek/Roman*: "Sword of Damocles" → KEEP-AS-IS; "Pyrrhic victory" → KEEP-AS-IS; "Sisyphean task" → KEEP-AS-IS.
- *Biblical*: "Methuselah" → KEEP-AS-IS; "the Lazarus moment" → KEEP-AS-IS; "thirty pieces of silver" → KEEP-AS-IS.
- *Literary canonical*: "Faustian bargain" → KEEP-AS-IS; "Hamlet's dilemma" → KEEP-AS-IS; "quixotic" → KEEP-AS-IS.
- *Said Nursi corpus (non-Western)*: "Bediuzzaman" → KEEP-AS-IS with one-time gloss in chapter introduction; "Risale-i Nur" → KEEP-AS-IS as established title; references to Mevlana → INLINE-GLOSS ("Mevlana (Rumi)") if the Persian-poetry canonicity isn't reliable for the reader.
- *Hindu/Sanskrit (non-Western)*: a reference to "Arjuna's dilemma" → INLINE-GLOSS for Western-conversational; reference to Krishna's role → KEEP-AS-IS with INLINE-GLOSS if needed.

#### 2.4 `advanced`

**Reader profile.** The reader has humanities-undergraduate-equivalent cultural literacy. They have read canonical Western literature broadly and have working familiarity with the major non-Western canons through coursework or sustained reading. They catch literary-educated references and approach specialist-canonical references with comfort.

**Canonicity-tier.** Reliably catches ubiquitous + educated-mainstream + literary-educated. Specialist-canonical references appear but the reader may need brief support (mention of a Habakkuk-prophet reference may need INLINE-GLOSS).

**Register/canon-tier.** Handles literary canon broadly; reliably navigates cross-canon references (recognizes a Quranic reference in a text using both Quranic and Greek canon; tells Hindu from Buddhist from Confucian). Religious-sermon, philosophical, and literary registers all handled at the literary-educated tier.

**Cultural-reference-handling test.** KEEP-AS-IS as the default for ubiquitous + educated-mainstream + literary-educated. INLINE-GLOSS only when a specialist-canonical reference is invoked that may exceed the reader's tier. EXPLICATE-FUNCTION rarely needed; FOOTNOTE for true scholar-canonical references.

**Examples spread across canons:**
- *Greek/Roman*: "Procrustean bed" → KEEP-AS-IS; "Promethean fire" → KEEP-AS-IS; references to Niobe → KEEP-AS-IS.
- *Biblical*: "Habakkuk" → KEEP-AS-IS or INLINE-GLOSS; "Melchizedek" → KEEP-AS-IS for advanced reader.
- *Literary canonical*: "Bovarysme" → KEEP-AS-IS; "Karamazov-esque guilt" → KEEP-AS-IS; "Jean Valjean" as specifically Hugo's character → KEEP-AS-IS.
- *Said Nursi corpus (non-Western)*: references to Mevlana, Abdulkadir-i Geylani → KEEP-AS-IS; references to the specific theological-school history (Maturidi vs Ashari) → INLINE-GLOSS.
- *Persian/Quranic (non-Western)*: Rumi quotations → KEEP-AS-IS; references to Hafez → KEEP-AS-IS; references to *isra'* and *miraj* → KEEP-AS-IS.

#### 2.5 `native`

**Reader profile.** The reader has specialist cultural literacy in the relevant canon — at the depth of a humanities scholar, theological scholar, classical-studies expert, or specialist in the source culture. They catch references at scholar-canonical depth.

**Canonicity-tier.** Reliably catches all 5 tiers including specialist-canonical and scholar-canonical. References to lesser figures (Erysichthon, Phaedra, Iphigenia from Greek; Onan, Melchizedek from Biblical; specific Sufi figures from Islamic mystical tradition) are caught silently.

**Register/canon-tier.** Native-level canon-handling across all genres. Religious-sermon canon at scholar depth; literary canon at scholar depth; philosophical canon at scholar depth.

**Cultural-reference-handling test.** KEEP-AS-IS for everything. The translator-AI's role at this level is preservation; no glossing, footnoting, or explication. The reader catches the references silently and the translation reads as in the source.

**Examples spread across canons:**
- *Greek/Roman*: "Erysichthon" → KEEP-AS-IS; "Niobe's tears" → KEEP-AS-IS; "Tantalus" → KEEP-AS-IS.
- *Biblical*: "Habakkuk" → KEEP-AS-IS; "Melchizedek" → KEEP-AS-IS; "Onan" → KEEP-AS-IS.
- *Literary canonical*: Joyce's Bloomsday → KEEP-AS-IS; Bartleby → KEEP-AS-IS; specific Tolstoy characters → KEEP-AS-IS.
- *Said Nursi corpus (non-Western, for a Nursi-specialist reader)*: all Risale-i Nur internal references including lesser-known prophets in Quranic accounts, theological-school positions, all Sufi figures → KEEP-AS-IS.
- *Specialist Islamic theology (non-Western)*: Maturidi vs Ashari vs Mutazila → KEEP-AS-IS; al-Razi vs al-Ghazali → KEEP-AS-IS.

#### 2.6 Distinguishing logic between adjacent levels

The boundaries are anchored in the canonicity-tier ladder:

- **`very_basic` → `daily`:** "ubiquitous-only (unreliably)" vs "ubiquitous (reliably) + first slice of educated-mainstream". The very_basic reader catches ubiquitous references when explicitly supported; the daily reader catches them reliably and starts picking up well-known educated-mainstream references from journalism and pop culture.
- **`daily` → `conversational`:** "first slice of educated-mainstream" vs "full educated-mainstream". The daily reader has spotty coverage of educated-mainstream (gets Big Brother and Kafkaesque but may miss Pyrrhic victory or Sword of Damocles); the conversational reader has complete coverage of educated-mainstream.
- **`conversational` → `advanced`:** "+ literary-educated tier". The advanced reader adds humanities-undergraduate-equivalent coverage of literary canon (Dante's Beatrice; Bovarysme; mid-tier Russian literary canon).
- **`advanced` → `native`:** "+ specialist-canonical + scholar-canonical". The native reader has scholar-depth coverage of the canon; catches the lesser figures, the specialist theological positions, the canon-internal cross-references.

### 3. The A1↔A2 Boundary

A1 (Reader Level) covers GENERAL cultural literacy across the recognized canon. A2 (Domain Expertise — a separate sub-field family in the configuration architecture) covers DOMAIN-specialist canon-knowledge requiring focused training.

**Criterion:** a reference belongs in A1 if a member of the relevant target culture with general education could plausibly recognize it (within the canon they recognize). A reference belongs in A2 if recognition requires DOMAIN training beyond general cultural literacy.

**Five specialist-domain canons illustrate the A2 territory:**

1. **Legal-history precedents.** Marbury v. Madison, Brown v. Board of Education, Roe v. Wade, Dred Scott — recognized by legal-trained readers. Not part of general cultural literacy.

2. **Mathematical figures and concepts.** Cantor's diagonal, Gödel's theorems, Russell's paradox, Hilbert's problems, the Riemann hypothesis. A specialist canon. Note the exception: the Pythagorean theorem has migrated from specialist to general (most adults learn it in school) — a gray-zone case.

3. **Scientific figures and concepts.** Maxwell's equations, Bohr's atom, Pasteur (synonymous with germ theory), Feynman diagrams. Specialist canon — with the notable exception that Einstein has migrated from specialist to general (Einstein = generic-genius reference for most adults).

4. **Medical eponyms.** Alzheimer's, Parkinson's, Charcot, Hodgkin's lymphoma, Bell's palsy. Some medical eponyms (Alzheimer's, Parkinson's) have migrated to general usage; others (Charcot, Hodgkin) remain specialist.

5. **Specialist philosophy.** Heideggerian (beyond the popular "existentialism"), Wittgensteinian (beyond the popular "Wittgenstein" name-drop), Hegelian dialectic at the specialist level. Note: Marx's canonicity tier varies by political-canon; for some readers Marx is general, for others specialist.

**Gray-zone cases are acknowledged.** Einstein moved specialist → general. Pythagorean theorem similarly. The framework assumes a SNAPSHOT at config time; gray-zone cases need periodic re-classification as cultural-canon migration occurs. The mechanism for refresh-cadence is an audience-level concern (out of scope here).

### 4. Cross-Sub-Field Dual-Membership Table

The 20 entries forward-flagged by prior sibling findings are re-tagged INDEPENDENTLY here from cultural-reference-recognition's frame. The 12 entries from `a1_idiom_recognition_levels` and the 8 entries from `a1_inference_capacity_levels` overlap on 6 entries (Crossing the Rubicon, Trojan horse, Cassandra, Sisyphean, Pyrrhic victory, Lazarus), leaving 14 unique entries.

Each entry receives: a cultural-ref canonicity tier; a per-reader-level handling action; and a dual-membership origin tag (idiom-only / inference-only / both).

| # | Entry | Origin | Canonicity tier | very_basic | daily | conversational | advanced | native |
|---|---|---|---|---|---|---|---|---|
| 1 | Achilles' heel | idiom | educated-mainstream | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 2 | Pyrrhic victory | both | educated-mainstream | EXPLICATE-FUNCTION | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 3 | Crossing the Rubicon | both | educated-mainstream | EXPLICATE-FUNCTION | KEEP-AS-IS (if marked) | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 4 | Trojan horse | both | ubiquitous | KEEP-AS-IS (transparent) | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 5 | Catch-22 | idiom | educated-mainstream | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 6 | Big Brother | idiom | ubiquitous (in modern usage) | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 7 | Cassandra | both | educated-mainstream | FOOTNOTE or EXPLICATE-FUNCTION | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 8 | Pandora's box | idiom | ubiquitous | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 9 | Sword of Damocles | idiom | educated-mainstream | EXPLICATE-FUNCTION | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 10 | Sisyphean | both | educated-mainstream | EXPLICATE-FUNCTION | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 11 | Lazarus | both | educated-mainstream (Biblical) | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 12 | Methuselah | idiom | educated-mainstream (Biblical) | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 13 | He met his Waterloo | inference | educated-mainstream | EXPLICATE-FUNCTION ("his decisive defeat") | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| 14 | Joan of Arc | inference | educated-mainstream-to-literary-educated | INLINE-GLOSS or FOOTNOTE | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |

Six entries (Crossing the Rubicon, Trojan horse, Cassandra, Sisyphean, Pyrrhic victory, Lazarus) appear in both prior siblings' forward-flag lists. Their dual-membership origin reflects that they fire in idiom-recognition (as idiomatic phrases), inference-capacity (as compressed allusion-inferences), AND cultural-reference-recognition (as canonical cultural references) — triple-overlap cases. The translator-AI's handling for these uses the triple-overlap union rule described in Section 5.

### 5. Cross-Sub-Field Orthogonality

The cultural-reference-recognition sub-field is distinct from but interacts with each of the other 4 A1 sub-fields. The distinctions matter so the translator-AI doesn't double-count or miss handling decisions.

**vs. vocabulary-breadth.** Knowing the proper noun is not the same as recognizing its allusive function. A reader who knows the name "Cassandra" (it appears in their vocabulary) still may not catch "she's a Cassandra" as a metaphor for the unheeded-prophet pattern. Vocabulary-breadth handles word-knowledge; cultural-reference-recognition handles allusive-function recognition.

**vs. syntactic-processing-capacity.** Near-orthogonal. Cultural references don't significantly affect sentence-parsing; sentence-parsing capacity doesn't determine whether the reader catches a reference. They interact only weakly when a sentence's syntactic density obscures whether a reference is even being made (a marked-but-syntactically-buried reference may be missed for syntax reasons).

**vs. idiom-recognition.** Significant overlap (the 12 forward-flagged entries from idiom-recognition's finding). The distinction: idioms can be culturally-neutral (skin in the game, the elephant in the room, raining cats and dogs — no specific cultural anchor); cultural references point at a specific cultural source (Greek myth, Bible, historical event, named work). The overlap cases — Achilles' heel, Pyrrhic victory, Crossing the Rubicon, Trojan horse, etc. — are BOTH idioms AND cultural references; they fire both sub-fields.

**vs. inference-capacity.** Allusion-inference overlap (the 8 forward-flagged entries from inference-capacity's finding). The distinction: recognizing the reference is identification (the reader catches that "Waterloo" is being invoked); inferring its meaning in context is compression-unpacking (the reader works out that "his Waterloo" means "his decisive defeat"). These are sequenced operations — identification first, inference second — but the sub-fields capture different reader capabilities.

**Triple-overlap cases.** Six entries fire all three sub-fields (idiom-recognition + inference-capacity + cultural-reference-recognition): Crossing the Rubicon, Trojan horse, Cassandra, Sisyphean, Pyrrhic victory, Lazarus. For these, the triple-overlap union rule applies.

**Triple-overlap union rule.** When a reference fires multiple sub-fields, the translator-AI applies the union of the per-sub-field handling rules — meaning, when the per-sub-field actions conflict, the more-explicating action wins. Example: at `daily` reader level, a Crossing the Rubicon reference might be KEEP-AS-IS by cultural-ref's rule (it's educated-mainstream in canonicity and the daily reader is at the canonicity tier) but INLINE-GLOSS by inference-capacity's rule (the compression-depth is non-trivial and the daily inference-capacity reader benefits from explicit "decisive irreversible commitment"). The union rule selects INLINE-GLOSS because it is more explicating. This prevents indeterminacy when sub-field rules disagree.

### 6. A1 Composite-Axis Chain Closure

This finding CLOSES the chain of 5 sub-field specifications that constitute A1 Reader Level. The complete chain:

1. **Vocabulary-breadth** (sub-field 1; specified in `devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/finding.md`) — the original 4-component template; word-frequency / register / substitution-test.
2. **Syntactic-processing-capacity** (sub-field 2; specified in `devdocs/inquiries/2026-06-05_17-05__a1_syntactic_processing_capacity_levels/finding.md`) — HEAVY adaptation; structural-complexity tier + restructuring-test.
3. **Idiom-recognition** (sub-field 3; specified in `devdocs/inquiries/2026-06-05_18-03__a1_idiom_recognition_levels/finding.md`) — LIGHT adaptation; substitution-test → idiom-handling test with 4 named primary actions.
4. **Inference-capacity** (sub-field 4; specified in `devdocs/inquiries/2026-06-05_18-38__a1_inference_capacity_levels/finding.md`) — MEDIUM adaptation; inference-load tier with 6 sub-measures + gap-filling test with 6 named primary actions.
5. **Cultural-reference-recognition** (sub-field 5; this finding) — MEDIUM-to-LIGHT adaptation; canonicity-tier + cultural-reference-handling test with 5 named primary actions.

**What's now specified.** A1 Reader Level is fully defined across all 5 sub-fields. Each has 5 ordinal levels with same labels (`very_basic | daily | conversational | advanced | native`). Each has a 4-component template adapted to its dimension. Each has a per-sub-field A1↔A2 boundary. The user can commit the A1 schema:

```python
class A1ReaderLevel:
    vocabulary_breadth: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    syntactic_processing_capacity: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    idiom_recognition: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    inference_capacity: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    cultural_reference_recognition: Literal["very_basic", "daily", "conversational", "advanced", "native"]
```

A single user-level configuration (`reader_level = "daily"`) propagates across all 5 sub-fields as a default; any sub-field can be explicitly overridden.

**What's next.** The next conceptual step is the A1↔A2 split inquiry — determining what belongs in A1 (Reader Level) as established here vs A2 (Domain Expertise) as a separate sub-field family. The root architectural inquiry (`devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md`) committed to the 4-layer / 4-family / 8-axis architecture; A1 is now fully specified and A2's specification is the next inquiry's territory.

**What's still open** (specific to cultural-reference-recognition):

- **Audience-level canon-set configuration.** The schema needs an `audience.canon_set: list[str]` field for the reader's recognized canons. Future inquiry.
- **Multi-canon handling.** When the audience recognizes multiple canons at different levels (e.g., `native` Greek-Biblical but `very_basic` Quranic), per-canon reader-level configuration is needed. Future inquiry — depends on audience-level canon-set being specified first.
- **Genre-canon mapping.** Different genres (sermon, news, literary, scientific) invoke different canons; a genre-aware translator-AI may need explicit genre-to-canon mappings. Future inquiry, lower priority.
- **Time-shift canon membership.** Canon membership migrates over time (Einstein moved specialist → general; Sarajevo's reference-tier depends on generation). The framework assumes a snapshot at config time; refresh-cadence is an audience-level concern. Future inquiry.

---

## Inherited Commitments Re-test

This finding inherits commitments from 5 prior inquiries (4 sibling sub-field findings + the root architectural finding). The Synthesis Trigger in `_branch.md` requires each inherited commitment be either re-tested with cited evidence OR flagged as INHERITED-WITHOUT-RE-TEST with a reason.

**IC1 — Same-labels-for-default-propagation** (`very_basic | daily | conversational | advanced | native`).
- **Source:** `a1_vocabulary_breadth_levels/finding.md` — the original 4-component template source — and all subsequent sub-field findings.
- **Re-test status:** RE-TESTED.
- **Evidence:** the labels apply meaningfully to canonicity-recognition (ubiquitous → all tiers); the canonicity-tier ladder maps 1-to-1 to the 5 reader levels (Section 1.1). Same-labels enables single-user-level-config propagation across all 5 sub-fields (Section 6).

**IC2 — Conservative-bias-for-reader-axes = LOWER default.**
- **Source:** `translation_config_axes/finding.md` (root architectural finding) and all 4 sibling sub-field findings.
- **Re-test status:** RE-TESTED.
- **Evidence:** At `very_basic`, the framework explicitly assumes the reader catches ubiquitous-canon only UNRELIABLY (Section 2.1). The conservative bias yields more aggressive glossing at lower levels — safer for translator-AI's default behavior.

**IC3 — Receptive-only commitment.**
- **Source:** Established in `a1_vocabulary_breadth_levels/finding.md`; reaffirmed in all subsequent sibling findings.
- **Re-test status:** RE-TESTED.
- **Evidence:** Each per-level prose (Sections 2.1–2.5) is framed as recognition (the reader CATCHES references) not production. The translator-AI's handling actions all operate on what the AI does with references the source provides; the reader is never asked to generate references.

**IC4 — Language-agnostic at concept level.**
- **Source:** `translation_config_axes/finding.md` and all sibling findings.
- **Re-test status:** RE-TESTED AND REFINED.
- **Evidence:** the level FRAMEWORK (canonicity-tier ladder; 4-component template; handling-test) is language-agnostic — it does not presuppose any particular language's lexicon or grammar. The CANON CHOICE itself is unavoidably culture-bound (a Greek/Roman canon is not Confucian, is not Quranic, is not Said Nursi corpus). The explicit caveat — framework language-agnostic, canon-choice culture-bound — is the refinement made at this sub-field (Sections 1.3, 1.4).

**IC5 — 4-component template adapts as needed.**
- **Source:** `a1_vocabulary_breadth_levels/finding.md` (template-source) and all subsequent sibling findings (each adapts to its sub-field's dimension).
- **Re-test status:** RE-TESTED AND APPLIED.
- **Evidence:** the adaptation here is MEDIUM-to-LIGHT (Section 1.2): frequency-tier → canonicity-tier (medium change); register-tier → register/canon-tier (light reframe); substitution-test → cultural-reference-handling test with 5 primary actions (medium change). The label MEDIUM-to-LIGHT positions this sub-field between idiom-recognition's LIGHT adaptation and syntactic-processing-capacity's HEAVY adaptation.

**IC6 — A1↔A2 boundary defined per sub-field.**
- **Source:** `a1_vocabulary_breadth_levels/finding.md` and all subsequent sibling findings.
- **Re-test status:** RE-TESTED AND APPLIED.
- **Evidence:** Section 3 defines the cultural-reference-specific A1↔A2 boundary: general cultural literacy (A1) vs domain-specialist canon training (A2); 5 specialist-domain canons (legal precedents, mathematical figures, scientific figures, medical eponyms, specialist philosophy); gray-zone case acknowledgments (Einstein, Pythagorean, Marx).

**IC7 — Cross-sub-field dual-membership handled INDEPENDENTLY per sub-field.**
- **Source:** `a1_idiom_recognition_levels/finding.md` (introduced the 12-entry forward-tagged list) and `a1_inference_capacity_levels/finding.md` (introduced the 8-entry list).
- **Re-test status:** RE-TESTED AND APPLIED.
- **Evidence:** Section 4 re-tags all 20 forward-flagged entries from cultural-reference's frame independently — assigning each a cultural-ref canonicity tier and a per-level handling action. The re-tagging does not cascade from the prior siblings' tagging; it uses cultural-reference's own frame (Hirsch tier conventions).

**IC8 — Orthogonality with siblings — explicit boundary.**
- **Source:** `a1_idiom_recognition_levels/finding.md` and `a1_inference_capacity_levels/finding.md`.
- **Re-test status:** RE-TESTED AND DOCUMENTED.
- **Evidence:** Section 5 enumerates the 4 cross-sub-field boundaries (vs vocabulary-breadth, vs syntactic-processing-capacity, vs idiom-recognition, vs inference-capacity) with criteria distinguishing each. Triple-overlap union rule added to prevent AI indeterminacy.

**IC9 — A1 composite-axis chain closure marker** (NEW commitment unique to this inquiry).
- **Source:** No prior; introduced here.
- **Re-test status:** NEW.
- **Anchor:** Section 6 explicitly marks the closure of the 5-sub-field chain; all 5 sub-fields are now specified. The schema is ready for commitment. The next conceptual step is the A1↔A2 split inquiry.

**IC10 — DOMESTICATE-disfavored per project policy** (NEW commitment unique to this inquiry).
- **Source:** Anchored to user's persistent memory (`feedback_translation_register`) and Lawrence Venuti's foreignization ethics.
- **Re-test status:** NEW.
- **Anchor:** Section 1.7 documents the DOMESTICATE-disfavored policy with the action preference order (KEEP-AS-IS → INLINE-GLOSS → EXPLICATE-FUNCTION → FOOTNOTE → DOMESTICATE last-resort); EXPLICATE-FUNCTION presented as the foreignization-preserving alternative.

**IC11 — Markedness / transparency as text/reference properties orthogonal to level** (NEW commitment unique to this inquiry).
- **Source:** Sensemaking ambiguities A3 (markedness) and A4 (transparency) at HIGH confidence.
- **Re-test status:** NEW.
- **Anchor:** Section 1.5 places markedness on the text side and transparency on the reference side, both orthogonal to reader-level. They modulate runtime action choice but are not level dimensions.

---

## Next Actions

### MUST

- **What:** Commit the A1 schema with all 5 sub-fields' enums (the `class A1ReaderLevel` snippet in Section 6).
  - **Who:** User (project author).
  - **Gate:** Condition-bound — when the user is ready to lock the A1 spec.
  - **Why:** Enables the translator-AI to receive the reader-level configuration as prompt context and decide handling actions per reference at runtime. Without commitment, the spec stays as documentation.

- **What:** Add to each level's per-level prose at least one non-Western canon example explicitly, ensuring no level relies solely on Greek/Biblical/Western-literary examples.
  - **Who:** This finding (already done — Section 2 examples at each level include non-Western canons: Said Nursi corpus, Quranic, Confucian, Hindu/Sanskrit, Persian).
  - **Gate:** Observable — verify by inspection that every level (`very_basic / daily / conversational / advanced / native`) lists at least one non-Western canon example.
  - **Why:** Prevents Greek/Biblical canon lock-in; supports the language-agnostic-at-framework / culture-bound-at-canon-choice commitment.

### COULD

- **What:** Add an `audience.canon_set: list[str]` field to the audience-level configuration to specify which canons the reader recognizes.
  - **Who:** Audience-level configuration inquiry (separate, future).
  - **Gate:** Condition-bound — when the user reaches the audience-level configuration inquiry (after the A1↔A2 split inquiry).
  - **Why:** Enables multi-canon handling and per-canon reader-level configuration; supports project expansion to additional source corpora beyond Said Nursi.
  - **Depends-on:** MUST item "Commit the A1 schema with all 5 sub-fields' enums". This COULD is GATED — do not act until the MUST resolves, since the audience-level field depends on the reader-level schema being settled first.

- **What:** Add a translator-AI prompt-engineering pass that embeds Sections 1, 2, 3, and 5 of this finding (the framework + per-level definitions + A1↔A2 boundary + sibling orthogonality) as system-context for the AI.
  - **Who:** Translation runtime / prompt-engineering layer (downstream of schema commitment).
  - **Gate:** Condition-bound — after the schema is committed.
  - **Why:** Makes the level definitions operationally available to the translator-AI.
  - **Depends-on:** MUST item "Commit the A1 schema with all 5 sub-fields' enums". This COULD is GATED — do not act until the MUST resolves.

### DEFERRED

- **What:** Performance-practice cross-domain illustration (music's "ubiquitous / specialist / scholar repertoire" stratification as a teaching analogy for the canonicity-tier ladder).
  - **Gate:** Revival trigger — if a future inquiry surfaces a need for additional cross-domain anchors for the tier ladder (beyond Hirsch + Bourdieu); or if the translator-AI prompt-engineering pass benefits from analogical scaffolding.
  - **Why (if revived):** Provides an additional didactic anchor for the canonicity stratification; useful for explaining the framework to users new to translation studies.

- **What:** Multi-canon reader-level configuration (per-canon level values for audiences fluent in multiple canons).
  - **Gate:** Revival trigger — when the user encounters a translation project where the target audience has materially different canonicity levels across multiple canons (e.g., a reader equally fluent in Western and Islamic canons), forcing single-value-per-reader to be insufficient.
  - **Why (if revived):** Closes the multi-canon gap not addressed at the A1 layer.

- **What:** Time-shift canon-membership refresh cadence (mechanism for periodic re-classification as references migrate between specialist and general canon — e.g., Einstein's migration from specialist to general).
  - **Gate:** Revival trigger — when canon-migration produces user-observable translator-AI mistakes (the AI glosses a reference that has migrated to general usage, or vice versa).
  - **Why (if revived):** Prevents the snapshot-at-config-time assumption from producing stale handling decisions over the lifecycle of a translation project.

---

## Reasoning

### Why these 5 levels and this framework

The 5-level structure with `very_basic | daily | conversational | advanced | native` labels is inherited from the prior 4 sibling findings. The labels carry sensible cultural-reference-recognition semantics: each level corresponds to a recognizable depth of cultural literacy a target-audience reader might have. Same-labels-for-default-propagation enables the user to set a single `reader_level` value once and have it apply across all 5 A1 sub-fields by default.

The 5 canonicity tiers come from cultural-literacy research. Hirsch's *Cultural Literacy* (1987) is the canonical argument that shared cultural knowledge is a precondition for textual comprehension; Hirsch's appendix list of ~5000 terms — methodologically contested but useful as anchor — illustrates the ubiquitous-to-educated-mainstream tiers. Bourdieu's *Distinction* (1979) provides the sociological frame for canon-stratification: who has access to which canon depth shapes who recognizes which references. The 5-tier ladder (ubiquitous / educated-mainstream / literary-educated / specialist-canonical / scholar-canonical) is a natural stratification supported by both anchors.

The 4-component template is the recurring pattern across all 5 A1 sub-fields. The MEDIUM-to-LIGHT adaptation here is justified by the fact that cultural references are ITEMS (like vocabulary words, like idioms) — the LIGHT-adaptation pattern — but the relevant dimension is canonicity-within-canon rather than Zipfian word-frequency, requiring more substantive component-2 replacement than the LIGHT case.

### Why DOMESTICATE-disfavored as project policy

Three considered alternatives, with two killed and one survived:

**Killed Alternative 1: DOMESTICATE-at-parity.** This would treat DOMESTICATE as a standard handling action at every level, with the translator-AI choosing it freely when appropriate for the reader's level. Why killed: the user's persistent memory on translation register fidelity ("don't pull plain source registers up into ornate/archaic English") implies preserving source-cultural character; Venuti's foreignization ethics provide the wider anchor; the project's primary corpus (Said Nursi) is one where Islamic-Sufi cultural specificity is load-bearing. DOMESTICATE-at-parity would routinely erase that specificity.

**Killed Alternative 2: DOMESTICATE-banned-entirely.** This would remove DOMESTICATE from the action taxonomy. Why killed: structurally, DOMESTICATE is part of the established translation-studies taxonomy (Newmark; Aixelá); banning it removes a legitimate last-resort tool. Some references at `very_basic` reader level are genuinely too opaque + too unmarked + too burdensome-to-EXPLICATE-FUNCTION to handle any other way. Banning the action loses the escape valve.

**Survived: DOMESTICATE-disfavored.** Keep DOMESTICATE in the action taxonomy for structural completeness; specify a project policy that makes it the last resort. EXPLICATE-FUNCTION is the foreignization-preserving alternative at lower reader levels. This preserves both the structural taxonomy and the project's foreignization commitment.

### Why reader-relative (not source-relative)

Sensemaking's ambiguity A2 explicitly tested this. The strongest counter-interpretation was: level should be source-canon-relative (captures how much of the source's reference set the reader catches). The counter fails on structural grounds: the reader's recognition is a property of the reader, not the source. A Western-secular reader's recognition of Quranic references is `very_basic` REGARDLESS of whether they're reading Said Nursi or reading a Western text that happens to mention a Quranic reference. The level captures what the reader brings; source-relative would conflate this with source-canon-density, which is a TEXT property the AI observes from the text itself.

### Why canon-choice is out of scope here

Sensemaking's ambiguity A1 explicitly tested this. The strongest counter-interpretation was: bundle canon-choice into the level. The counter fails: a Western-secular reader can be `native` for Greek-Biblical canon AND SIMULTANEOUSLY `very_basic` for Quranic canon. Treating canon-choice and canonicity-depth as one axis forces a single value per reader that loses the multi-canon literacy information. Keeping canon-choice separate (at the audience level) and canonicity-depth at the reader-level preserves both axes orthogonally.

### Why markedness and transparency are NOT level dimensions

Sensemaking's ambiguities A3 (markedness) and A4 (transparency) tested this. Both are TEXT/REFERENCE properties: markedness is whether the source signposts the reference (a text-side property); transparency is whether the reference functions metaphorically without source-knowledge (a reference-side property intrinsic to the reference itself). The reader-level captures recognition-depth; markedness and transparency are runtime conditioning variables for action selection but they don't characterize the reader.

### Why this finding closes the A1 chain

The root architectural inquiry (`translation_config_axes`) committed to A1 Reader Level as a composite-axis with 5 sub-fields. Each of the 4 prior siblings specified one sub-field. This finding specifies the 5th. There is no further A1 sub-field to specify; the architecture is complete. The next conceptual step is the A1↔A2 split inquiry — what belongs in A1 vs A2 — which is a separate architectural inquiry, not a continuation of this chain.

---

## Open Questions

### Monitoring

- **AI prompt-context calibration.** Once the schema is committed and the translator-AI receives this finding's framework as prompt context, observe whether the AI's per-reference handling decisions match the level definitions. Specifically: does the AI INLINE-GLOSS at `daily` when it should KEEP-AS-IS (over-glossing)? Does it KEEP-AS-IS at `very_basic` when it should EXPLICATE-FUNCTION (under-glossing)? Calibration adjustments to the per-level prose may be needed after observing N≥10 translation samples.

### Blocked

- **Multi-canon reader configuration.** Cannot be specified until the audience-level configuration inquiry establishes the `audience.canon_set` field. Blocked by COULD item 1 in Next Actions.

- **A1↔A2 split inquiry.** Cannot proceed until A1 is fully specified (this finding completes that) AND a separate inquiry decides which other reader/configuration concerns belong in A1 vs A2. Blocked by MUST item 1 (schema commitment), unblocks the next architectural step.

### Research Frontiers

- **Genre-conditioned canon mapping.** A truly genre-aware translator-AI would have explicit mappings from genre (sermon / newspaper / literary fiction / scientific paper) to canon-set. Currently handled implicitly via the register/canon-tier component; explicit mapping requires further investigation.

- **Time-shift canon refresh cadence.** Canon membership migrates (Einstein, Pythagorean theorem) but the mechanism for periodic re-classification is not specified. Future research.

### Refinement Triggers

- **Refinement trigger for the canonicity-tier ladder:** if cultural-literacy research yields a substantially different tier structure (e.g., a 3-tier or 7-tier alternative becomes consensus), revisit the 5-tier ladder and the 1-to-1 mapping to reader levels.

- **Refinement trigger for DOMESTICATE-disfavored:** if the project expands beyond Said Nursi to corpora where foreignization-by-default is inappropriate (e.g., children's literature, where domestication may be ethically and pedagogically correct), the DOMESTICATE-disfavored policy may need a per-corpus override.

- **Refinement trigger for the A1↔A2 boundary:** if the A1↔A2 split inquiry finds that some specialist-domain canons (e.g., specialist philosophy) belong in A1 after all — perhaps because the relevant reader audience is humanities-PhD-educated for whom these are general — revisit the boundary.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
now do it for  cultural-reference-recognition
```

</details>
