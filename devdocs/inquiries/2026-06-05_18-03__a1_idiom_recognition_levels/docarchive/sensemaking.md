# Sensemaking — a1_idiom_recognition_levels

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_18-03__a1_idiom_recognition_levels/_branch.md` (with surfacing output at `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_18-03__a1_idiom_recognition_levels/surfacing.md`)

---

## SV1 — Baseline Understanding

The inquiry asks to define 5 ordinal levels for idiom-recognition, parallel to vocabulary-breadth (sub-field 1) and syntactic-processing-capacity (sub-field 2). Same labels (`very_basic | daily | conversational | advanced | native`) carry over. My initial impression: the template adaptation should be LIGHTER than for syntax — idioms have frequency distributions (like words; unlike sentences) AND register tiers (like both); the substitution-test analogue becomes idiom-handling-test with named runtime actions. Key challenges: (a) how heavily to adapt; (b) the cross-sub-field boundary with cultural-reference-recognition for dual-membership cases like "Achilles' heel"; (c) the A1↔A2 boundary for domain-specialist idioms (legal / financial / sports).

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1.** 5 ordinal levels with same labels.
- **C2.** Receptive only — recognizes the FIGURATIVE meaning when encountered, not produces idioms.
- **C3.** Language-agnostic at concept level.
- **C4.** Scope = idiom-recognition only.
- **C5.** Mutually distinct ordinal levels.
- **C6.** 4-component template adapted as needed.
- **C7.** Conservative-bias for reader-axes = LOWER default.
- **C8.** Distinct from the other 4 A1 sub-fields (vocabulary-breadth, syntactic-processing-capacity, inference-capacity, cultural-reference-recognition).

### Key Insights

- **KI1.** Idioms have **frequency distributions** (some idioms are far more common than others; corpus-based frequency lists exist — Oxford Dictionary of English Idioms; COCA idiom queries) AND **register stratification** (casual / colloquial / journalistic / literary / archaic / biblical). Both vocabulary-breadth's frequency-tier and register-tier concepts apply DIRECTLY to idioms with light prefix-renaming. The template adaptation is LIGHTER than for syntactic-processing-capacity (which had to replace frequency-tier entirely because sentences don't have Zipfian frequency).

- **KI2.** The substitution-test becomes **idiom-handling test** with named runtime actions drawn from Newmark / Baker translation-of-idioms research:
  - **PARAPHRASE** — replace the idiom with its literal meaning (`kick the bucket` → "die")
  - **FAMILIAR-EQUIVALENT** — replace with a target-language idiom of similar meaning (English `raining cats and dogs` → Russian `льёт как из ведра` / French `il pleut des cordes`)
  - **INLINE-GLOSS** — keep the idiom + brief inline explanation (`kick the bucket — i.e., die`)
  - **FOOTNOTE** — keep the idiom + footnote it
  - Plus secondary: LITERAL-WITH-EXPLANATION; OMIT-IF-DECORATIVE.

- **KI3.** **Compositionality** (transparent idioms like "see the light" — partly inferable from the parts — vs opaque idioms like "kick the bucket" — meaning unrelated to parts) is a real cognitive variable. BUT transparent idioms cluster at lower levels (a `daily` reader recognizes "see the light" partly via the metaphor); opaque idioms cluster at higher levels. Compositionality correlates with level placement; absorbing it into per-level prose is cleaner than adding a 5th template component.

- **KI4.** **A1↔A2 boundary for idioms.** General idioms (everyday → literary → archaic) → A1. Domain-specialist idioms requiring field training (legal "with all deliberate speed"; financial "below the line"; sports "in the home stretch" when sport-specific; medical specialist idioms) → A2. Borderline: domain-derived idioms now in general use ("moving the goalposts" sports → general) → A1.advanced or A1.native, not A2.

- **KI5.** **Cross-sub-field boundary with cultural-reference-recognition.** Dual-membership cases (`Achilles' heel`, `Crossing the Rubicon`, `Pyrrhic victory`, `Trojan horse`) are simultaneously idioms (figurative meaning) AND cultural references (Greek myth / Roman history). RESOLUTION: handled per sub-field INDEPENDENTLY. The idiom-recognition sub-field measures "does the reader recognize `Achilles' heel` as meaning 'vulnerability point'?" The cultural-reference-recognition sub-field measures "does the reader recognize the Greek-myth source?" A reader can know one but not the other. Both sub-fields tag dual-membership cases at appropriate levels.

- **KI6.** **Proverbs** (sentence-length idiomatic expressions like "a stitch in time saves nine") are part of the idiom-recognition spectrum, concentrated at advanced/native levels. Include in the spec with note.

- **KI7.** **Phrasal verbs** that are idiomatic (`give in` = surrender; `carry on` = continue; `look up` = search; `make out` = perceive / kiss / fare) are part of the gradient. High-frequency idiomatic phrasal verbs sit at daily/conversational; less-common at advanced. Include.

- **KI8.** **Dead metaphors** (`understand` = "stand under"; `comprehend` = "grasp"; `consider` = "with stars") are NOT idiom-recognition territory — readers process them as literal. Exclude from the spec.

- **KI9.** **Universal vs language-specific idioms.** Most surface idioms are language-specific (English `raining cats and dogs`; Russian `льёт как из ведра`; French `il pleut des cordes`). Some conceptual metaphors are universal (water-fluidity = emotion-overflow). The CONCEPT (frequency × register gradient) is universal; specific idioms are per-language.

- **KI10.** The user's earlier "backpacker won't understand idioms" framing (from `my_notes.md`) locates the `daily` reader as still mostly idiom-blind for opaque idioms. Resolution: `very_basic` = essentially zero recognition; `daily` = recognizes only the most common transparent idioms (top ~30 like "piece of cake"); `conversational` = where common opaque idioms enter (user's anchor `kick the bucket` sits here).

### Structural Points

- **SP1.** **Adapted 4-component template** (LIGHTLY adapted from vocabulary-breadth's):
  1. Reader profile + anchor demographics + idiom-genre anchor (kept unchanged in shape)
  2. **Idiom-frequency tier** (lightly prefixed from frequency-tier) — top-N idioms the reader recognizes; English-illustrative
  3. **Idiom-register tier** (lightly prefixed from register-tier) — inclusions and exclusions across casual / colloquial / journalistic / literary / archaic / biblical
  4. **Idiom-handling test sketch** (replaces substitution-test) — named runtime actions: PARAPHRASE / FAMILIAR-EQUIVALENT / INLINE-GLOSS / FOOTNOTE; strength-graded per level

- **SP2.** Adaptation is LIGHTER than syntactic-processing-capacity's. Only the substitution-test analogue needs genuine replacement; frequency-tier and register-tier apply with light prefix-renaming.

- **SP3.** **Strength-graded idiom-handling per level:**
  - very_basic: aggressive PARAPHRASE for ALL idioms (literal render of any figurative source)
  - daily: PARAPHRASE most; FAMILIAR-EQUIVALENT for top-30 transparent
  - conversational: PARAPHRASE only rare/literary; FAMILIAR-EQUIVALENT for common opaque (user's "kick the bucket"); KEEP common transparent
  - advanced: KEEP most idioms; PARAPHRASE/GLOSS only archaic / Biblical; FAMILIAR-EQUIVALENT for borderline
  - native: KEEP all general idioms including archaic + Biblical + Shakespeare-derived; only A2 specialist domain idioms get glossed or footnoted

- **SP4.** **A1↔A2 boundary test for idioms** (parallel to vocabulary's and syntax's): "does recognizing this idiom's figurative meaning require subject-domain training, or only broad general exposure?" Subject-domain training → A2. General reading → A1.

- **SP5.** **Cross-sub-field boundary with cultural-reference-recognition:** dual-membership cases handled per sub-field independently. Each sub-field's level measures its own dimension; both can fire for the same expression.

- **SP6.** **Compositionality is correlated with level placement, not a separate axis.** Transparent idioms cluster at daily-conversational; opaque cluster at conversational-and-above; archaic-literary cluster at native. Absorbed into per-level prose.

- **SP7.** **Per-sub-field independence with the other A1 sub-fields.** Vocabulary-breadth, syntactic-processing-capacity, idiom-recognition, inference-capacity, cultural-reference-recognition are formally orthogonal. Empirical correlation is high in typical readers (most users at A1=conversational are conversational on all sub-fields), but edge cases exist (a backpacker can have daily vocabulary but be totally idiom-blind even for transparent idioms).

### Foundational Principles

- **FP1.** Receptive only.
- **FP2.** Language-agnostic at concept level.
- **FP3.** Ordinal.
- **FP4.** A1 excludes domain-specialist idioms (those are A2).
- **FP5.** Conservative-bias for reader-axes = LOWER default.
- **FP6.** Template adaptation is principled — components that fit are kept (with light prefix-renaming); components that don't fit are replaced. Don't replace what doesn't need replacing.
- **FP7.** Dual-membership cases (idiom + cultural-reference) handled per sub-field independently.

### Meaning-Nodes

- **MN1.** IDIOM-RECOGNITION LEVEL = tier specifying which idioms the reader recognizes figuratively when encountered.
- **MN2.** IDIOM-FREQUENCY TIER = Zipfian-like band of idioms ranked by usage frequency.
- **MN3.** IDIOM-REGISTER TIER = sociolinguistic register of idioms.
- **MN4.** TRANSPARENCY vs OPACITY = Nunberg compositionality distinction; absorbed into per-level placement.
- **MN5.** IDIOM-HANDLING TEST = runtime translator action analogue to substitution-test.
- **MN6.** PARAPHRASE / FAMILIAR-EQUIVALENT / INLINE-GLOSS / FOOTNOTE = the 4 primary handling actions; strength-graded per level.
- **MN7.** A1↔A2 BOUNDARY FOR IDIOMS = general idioms vs domain-specialist idioms.
- **MN8.** DUAL-MEMBERSHIP CASES = expressions that are both idioms and cultural references; handled per sub-field independently.

### Meta-Inspection after SV2 (H4, H5)

- **H4 — concept names.** `idiom-frequency tier` + `idiom-register tier` + `idiom-handling test` are loop-coined with light prefix-renaming from vocabulary-breadth's components. The 4 primary action names (PARAPHRASE / FAMILIAR-EQUIVALENT / INLINE-GLOSS / FOOTNOTE) are standard translation-of-idioms vocabulary (Newmark, Baker). User-language alignment: HIGH.
- **H5 — motivating examples.** User's anchor (`kick the bucket`) sits at conversational. Surfacing produced 5 example collections covering all 5 levels. Innovation must enumerate per-level concrete idiom examples (5–10 per level) + boundary pairs (4) + A1↔A2 specialist examples + cross-sub-field dual-membership examples.

### SV2 — Anchor-Informed Understanding

The 5 levels for idiom-recognition use a LIGHTLY-ADAPTED 4-component template: frequency-tier and register-tier kept (with `idiom-` prefix); substitution-test replaced by idiom-handling test with 4 named primary actions (PARAPHRASE / FAMILIAR-EQUIVALENT / INLINE-GLOSS / FOOTNOTE). Strength-graded handling per level. Compositionality (transparent vs opaque) absorbed into per-level prose. A1↔A2 boundary distinguishes general idioms (A1) from domain-specialist idioms requiring field training (A2). Cross-sub-field boundary with cultural-reference-recognition handled per-sub-field independently (dual-membership cases tagged at appropriate levels in both sub-fields). Proverbs at advanced/native; idiomatic phrasal verbs distributed across daily/conversational; dead metaphors excluded.

---

## Phase 2 — Perspective Checking

### Technical / Logical

Each level → Literal value. The translator-AI consumes prose + concrete idiom examples to make runtime decisions (PARAPHRASE / FAMILIAR-EQUIVALENT / INLINE-GLOSS / FOOTNOTE). LLMs have rich idiom knowledge; corpus-frequency lists provide backing if needed.

**T-A1.** 2–3 sentence prose per level.
**T-A2.** LLM-judged at runtime initially; corpus-frequency backing possible.
**T-A3.** Concrete English idiom examples anchor LLM judgment.

### Human / User

User-evocative reader-profile names (same labels). Concrete examples ("kick the bucket"; "give up the ghost"; "piece of cake") help user identify their reader.

**H-A1.** User-facing prose uses reader-profile names + idiom-genre anchors + concrete idiom examples.
**H-A2.** Per-level prose should help user identify their reader by reading the examples.

### Strategic / Long-term

Across target languages, idiom-frequency and idiom-register concepts hold; specific idioms differ per-language.

**S-A1.** Concept stable; per-language idiom lists are downstream (per-language inquiry).
**S-A2.** Translation strategies (PARAPHRASE / FAMILIAR-EQUIVALENT) require per-language target-idiom repertoires; deferred.

### Risk / Failure

Bad definitions would:
- Conflate idioms with vocabulary (an idiom uses words; the figurative recognition is separate)
- Miss the cultural-ref overlap (Achilles' heel must be addressable in both sub-fields)
- Include domain-specialist as A1.native (legal/financial/sports specialist are A2)
- Exclude proverbs or phrasal verbs without rationale
- Include dead metaphors (which readers don't process as figurative)
- Use English-Greek-mythology-derived idioms as defining axis (fails language-agnosticism)
- Mix receptive and productive framing

**R-A1.** Distinguish idiom-recognition from vocabulary-breadth (separate cognitive dimensions).
**R-A2.** Cross-sub-field dual-membership cases handled in both sub-fields independently.
**R-A3.** A1↔A2 boundary explicit with subject-domain-training test.
**R-A4.** Receptive-only enforced.
**R-A5.** Examples can be English-illustrative; concepts language-agnostic.

### Resource / Feasibility

LLMs judge idiom recognition reliably. Corpus-frequency lists provide backing. PARAPHRASE / FAMILIAR-EQUIVALENT runtime actions implementable via LLM prompt context.

**F-A1.** Anchor idiom examples ground LLM judgment.
**F-A2.** Per-target-language idiom repertoires for FAMILIAR-EQUIVALENT action — future inquiry.

### Ethical / Systemic

Native-level anchor idioms include Biblical / Shakespeare-derived expressions ("give up the ghost"; "method in his madness"). These are English-language-specific. The CONCEPT (literary-extreme idiomatic recognition in target-language tradition) translates; per-language anchors differ.

**E-A1.** Native-level genre anchors are English-language-specific; CONCEPT translates.

### Definitional / Internal Consistency

- Receptive-only honored throughout.
- Distinct from vocabulary-breadth (independent cognitive dimensions).
- Distinct from cultural-reference-recognition (dual-membership handled per sub-field).
- A1↔A2 boundary for idioms with subject-domain-training test.

**C-A1.** All level prose uses recognition verbs.
**C-A2.** Examples are general idioms (not domain-specialist).
**C-A3.** Distinguishing principles reference idiom-frequency, idiom-register, compositionality.

### Definitional / Frame-exit Completeness

Gating fires (inquiry inherits 4-component template from vocabulary-breadth + the adaptation pattern from syntactic-processing-capacity).

**1. Existence Enumeration.** "TEMPLATE" refers to: vocabulary-breadth's original 4-component template; syntactic-processing-capacity's heavily-adapted version; the meta-pattern of "adapt where needed, preserve where it fits." LAYER: USER-FACING SPEC.

**2. Role Assessment.** Each component decision:
- Reader-profile: kept (universal pattern across all 5 A1 sub-fields).
- Frequency-tier: KEPT with prefix-renaming (`idiom-frequency tier`) — idioms have frequency distributions; the concept applies directly.
- Register-tier: KEPT with prefix-renaming (`idiom-register tier`) — idioms span registers like vocabulary does.
- Substitution-test: REPLACED with idiom-handling test — runtime action differs (idiom-handling is multi-action: PARAPHRASE / FAMILIAR-EQUIVALENT / INLINE-GLOSS / FOOTNOTE).

**3. Verdict Rigor.** Clean-boundary "frequency-tier fits idioms" — counter: "idiom-frequency at the granularity of individual idioms might be too sparse." Test: idiom dictionaries provide empirical frequency data (Oxford Dictionary of English Idioms; CALD; corpus-based studies). The tier is operationalizable. PASS.

**4. Residual / Coverage Justification.** Compositionality dimension — does it need its own component? Test: compositionality correlates with frequency-and-register placement (transparent → daily; opaque → conversational+; archaic-literary → native). Absorbing into per-level prose is cleaner. NOT a 5th component.

### Phase / Calibration-State

Conservative-bias for idiom-recognition (reader-facing axis) = LOWER default level (assume reader recognizes fewer idioms; user dials UP). Per-language idiom-frequency lists are calibration-dependent.

**P-A1.** LOWER default for idiom-recognition.
**P-A2.** Level CONCEPTS stable; per-language operationalization downstream.

### Meta-Inspection after SV3 (H1, H2, H3, H7)

- **H1.** 5 candidate names align with A1 headline; pairwise distinct: very_basic = no idioms; daily = top-30 transparent; conversational = common opaque (kick the bucket); advanced = literary academic (cast aspersions); native = archaic/Biblical (give up the ghost). No collapse.
- **H2.** Frame scope = idiom-recognition; cross-sub-field boundary clarification + A1↔A2 in scope.
- **H3.** User's framing ("recognize figurative phrases figuratively") biases toward frequency-and-register dimensions — appropriate.
- **H7.** Defaults calibration-dependent; concepts not.

### SV3 — Multi-Perspective Understanding

1. **LIGHTLY-ADAPTED 4-component template:** reader-profile + idiom-frequency tier + idiom-register tier + idiom-handling test sketch.
2. **Strength-graded handling actions per level.**
3. **A1↔A2 boundary for idioms** with subject-domain-training test.
4. **Cross-sub-field boundary** with cultural-reference-recognition handled independently.
5. **Compositionality absorbed** into per-level prose (not 5th component).
6. **Proverbs** at advanced/native; **idiomatic phrasal verbs** at daily/conversational; **dead metaphors** excluded.
7. **Migration mapping** parallel to vocabulary-breadth's.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — Template adaptation extent (heavy or light)?

**Counter:** Heavily adapt the template parallel to syntactic-processing-capacity's adaptation — "idiom-complexity tier" replacing frequency-tier for parallel naming.

**Why fails:** Idioms HAVE Zipfian frequency distributions (unlike sentences). The frequency-tier concept applies DIRECTLY. Renaming to "complexity-tier" obscures the operational basis (corpus frequency). The lighter adaptation (prefix-rename frequency-tier → idiom-frequency tier; same for register-tier; replace only substitution-test) is more principled because each component is replaced WHERE NEEDED, not uniformly.

**Confidence:** HIGH.

**Resolution:** LIGHTLY-ADAPTED template — only the substitution-test analogue gets genuine replacement.

---

### Ambiguity 2 — Compositionality as 5th component?

**Counter:** Add compositionality (transparent vs opaque) as a 5th component for explicit grading.

**Why fails:** Compositionality correlates strongly with frequency-and-register placement. Transparent idioms ("see the light"; "piece of cake") cluster at daily. Opaque idioms ("kick the bucket"; "spill the beans") at conversational. Literary-archaic ("give up the ghost") at native. Absorbing into per-level prose preserves the dimension without over-engineering.

**Confidence:** HIGH.

**Resolution:** Absorb into per-level prose; not 5th component.

---

### Ambiguity 3 — Idiom↔cultural-reference boundary for dual-membership cases

**Counter:** Dual-membership cases (Achilles' heel, Pyrrhic victory, Crossing the Rubicon, Trojan horse) tagged as ONE sub-field only to avoid double-counting.

**Why fails:** A reader can recognize the IDIOMATIC meaning ("Achilles' heel = vulnerability point") WITHOUT recognizing the CULTURAL source (Achilles from Greek myth), OR vice versa. Tagging only as one sub-field loses information. The composite-axis pattern's strength is that sub-fields measure independent cognitive dimensions; collapsing them obscures the orthogonality.

**Confidence:** HIGH.

**Resolution:** Dual-membership cases handled per sub-field INDEPENDENTLY. The idiom-recognition spec tags them at appropriate levels; the cultural-reference-recognition spec will tag them at its own appropriate levels (likely different levels since cultural knowledge is acquired differently from idiomatic recognition).

---

### Ambiguity 4 — A1↔A2 boundary for idioms

**Counter:** All idioms are A1 (since they're "general language"); only vocabulary and syntax have A2 boundaries.

**Why fails:** Domain-specialist idioms genuinely require field training to recognize the figurative meaning:
- Legal: "with all deliberate speed" (≠ "quickly"; means "as soon as practicable"); "color of law"; "boilerplate"
- Financial: "below the line" (accounting); "in the red" (now general); "haircut" (financial loss); "moving the needle"
- Sports (when domain-specific): "in the home stretch"; "tagging up"; "Hail Mary pass"
- Medical: specialist idioms in medical communication

A reader without domain training would NOT recognize these. Borderline: sports/military idioms that have entered general use ("moving the goalposts"; "in the trenches"; "level playing field") are A1.advanced or A1.native, NOT A2.

**Confidence:** HIGH.

**Resolution:** A1↔A2 boundary for idioms with subject-domain-training test, parallel to vocabulary's and syntax's.

---

### Ambiguity 5 — Proverbs and idiomatic phrasal verbs

**Counter:** Proverbs are sentence-length and culturally-anchored; exclude. Phrasal verbs are vocabulary, not idioms; exclude.

**Why partially fails:**
- **Proverbs** ("a stitch in time saves nine"; "the early bird catches the worm"; "look before you leap"): sentence-length idiomatic expressions; the figurative recognition required is the same as for shorter idioms. Concentrated at advanced/native. INCLUDE with note that proverbs are a sub-category.
- **Idiomatic phrasal verbs** ("give in" = surrender; "carry on" = continue; "look up" = search; "make out" = perceive / kiss / fare; "give up" = surrender): many are IDIOMATIC (meaning not derivable from parts) and high-frequency. They straddle vocabulary and idiom-recognition. Common idiomatic phrasal verbs at daily/conversational; less common at advanced.

**Confidence:** HIGH.

**Resolution:** Proverbs at advanced/native (with note); idiomatic phrasal verbs distributed across daily/conversational/advanced; dead metaphors excluded.

---

### Ambiguity 6 — Universal vs language-specific idioms

**Counter:** Conceptual metaphor theory (Lakoff) shows some metaphors are universal; the spec should distinguish.

**Why partially holds:** Universal conceptual metaphors exist (water = emotion; container = self). But MOST surface idioms are language-specific (English `raining cats and dogs`; Russian `льёт как из ведра`; French `il pleut des cordes`). The CONCEPT of the idiom-recognition gradient (frequency × register) is universal; specific idioms are per-language.

**Confidence:** HIGH.

**Resolution:** Language-agnostic at concept level; specific idiom examples are English-illustrative; per-language idiom lists are the per-language inquiry.

---

### Ambiguity 7 — Migration mapping

**Counter:** Specify different mapping than vocabulary-breadth's.

**Why fails:** Per same-labels-for-default-propagation commitment, the migration mapping is parallel — same target labels:
- `late_learner_simple → daily`
- `late_learner → conversational`
- `native → native`
- New positions: `very_basic` (below; for zero-idiom-recognition); `advanced` (between; for literary academic).

**Confidence:** HIGH.

**Resolution:** Parallel to prior siblings.

---

### Ambiguity 8 — Conservative-bias default direction

**Counter:** HIGHER default to be safe (assume reader knows idioms).

**Why fails:** For reader-facing axes (inherited principle), conservative-bias = assume LESS reader competence. Default to LOWER level (assume reader recognizes fewer idioms; the translator paraphrases more; user dials UP if reader is more advanced).

**Confidence:** HIGH.

**Resolution:** LOWER default for idiom-recognition.

---

### Load-bearing concept test

1. **LIGHTLY-ADAPTED template** — concept valid; renaming with `idiom-` prefix preserves operational meaning.
2. **A1↔A2 boundary for idioms** — HIGH confidence; concrete examples (legal, financial, sports).
3. **Dual-membership independent handling** — HIGH confidence; preserves cross-sub-field orthogonality.
4. **Compositionality absorbed** — HIGH confidence; not a 5th component.
5. **Strength-graded idiom-handling** — HIGH confidence; per-level intensity differences.

### Specific-vs-pattern recognition cue

User's anchor example: `kick the bucket` (conversational). Innovation must produce concrete English idiom examples for all 5 levels + boundary pairs + A1↔A2 specialist list + dual-membership case list.

### SV4 — Clarified Understanding

The 5 idiom-recognition levels:

- **very_basic** — essentially zero idiom recognition; treats all figurative phrases literally. Runtime: aggressive PARAPHRASE.
- **daily** — recognizes only the top ~30 universally-transparent idioms ("piece of cake"; "easy as 1-2-3"; "rain or shine"). Runtime: PARAPHRASE most; FAMILIAR-EQUIVALENT for top-30.
- **conversational** — recognizes top ~200–500 common idioms including opaque ones (user's anchor `kick the bucket`; "spill the beans"; "hit the nail on the head"; "let the cat out of the bag"). Runtime: FAMILIAR-EQUIVALENT for common; PARAPHRASE only rare.
- **advanced** — recognizes ~1000–2000 idioms including academic / literary / less-common ("cast aspersions"; "tilt at windmills"; "throw down the gauntlet"; "Pyrrhic victory"). Runtime: KEEP most; PARAPHRASE/GLOSS only archaic / Biblical.
- **native** — recognizes all general idioms including archaic / Biblical / Shakespeare-derived ("give up the ghost"; "the patience of Job"; "by the skin of my teeth"; "method in his madness"; "the slings and arrows of outrageous fortune"). Runtime: KEEP all general; only A2 specialist domain idioms get glossed or footnoted.

The adapted 4-component template: reader-profile + idiom-frequency tier + idiom-register tier + idiom-handling test sketch. Compositionality absorbed into per-level prose. A1↔A2 boundary for idioms with subject-domain-training test. Cross-sub-field dual-membership handled independently. Same labels propagate; conservative-bias = LOWER default; receptive-only; language-agnostic at concept.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Variables fixed

- 5 ordinal levels with same labels.
- LIGHTLY-ADAPTED 4-component template (3 components renamed with `idiom-` prefix; substitution-test replaced).
- 4 primary idiom-handling actions: PARAPHRASE / FAMILIAR-EQUIVALENT / INLINE-GLOSS / FOOTNOTE.
- 2 secondary actions: LITERAL-WITH-EXPLANATION / OMIT-IF-DECORATIVE.
- Strength-graded handling per level (aggressive at very_basic; none at native general).
- Compositionality absorbed into per-level prose.
- A1↔A2 boundary for idioms (general → A1; domain-specialist → A2).
- Cross-sub-field with cultural-reference-recognition handled per-sub-field independently.
- Proverbs at advanced/native; idiomatic phrasal verbs distributed; dead metaphors excluded.
- Receptive only; language-agnostic at concept; conservative-bias = LOWER default.
- Migration mapping parallel to prior siblings.

### Options eliminated

- Heavy template adaptation (idioms have frequency + register; lighter adaptation appropriate).
- 5th component for compositionality (over-engineering).
- Dual-membership cases tagged only once (information loss).
- All-idioms-are-A1 (specialist domain idioms genuinely require field training).
- Excluding proverbs / phrasal verbs (they fit the spectrum).
- Including dead metaphors (no longer processed figuratively).
- HIGHER default for reader-axes (inherited principle).

### Paths remaining viable

- Concrete per-level English idiom examples (5–10 per level).
- Boundary-pair examples at each adjacent transition.
- A1↔A2 specialist-domain idiom list with reasoning.
- Cross-sub-field dual-membership case list.
- Migration mapping rationale.

### SV5 — Constrained Understanding

5 levels with lightly-adapted 4-component template, strength-graded handling, explicit A1↔A2 + cross-sub-field boundaries, compositionality absorbed. Ready for innovation to produce concrete examples.

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Did perspectives keep destabilizing? Phase 2 produced REFINEMENTS (lighter template adaptation; compositionality absorbed; dual-membership independent handling). Phase 3 ambiguity collapses converged consistently. No "patch and re-patch."

**Accommodation trigger does NOT fire.**

### Meta-Inspection final check (H6 model fit)

The lightly-adapted 4-component template + strength-graded handling + A1↔A2 + cross-sub-field boundaries + compositionality-absorbed fits all 8 constraints + 10 surfacing frontier flags + inherited commitments.

### SV6 — Stabilized Model

The 5 idiom-recognition levels use a **LIGHTLY-ADAPTED 4-component template** (3 components prefix-renamed from vocabulary-breadth's; substitution-test replaced by idiom-handling test):

1. **Reader profile** (with anchor demographics + idiom-genre anchor)
2. **Idiom-frequency tier** (English-illustrative — top-N idioms recognized)
3. **Idiom-register tier** (inclusions + exclusions across casual / colloquial / journalistic / literary / archaic / biblical)
4. **Idiom-handling test sketch** (which actions the translator applies; strength-graded)

```
LEVEL 1 — very_basic
  Reader profile: young child / brand-new L2 learner
  Idiom-frequency tier (English-illustrative): essentially 0 idioms recognized;
                                                 treats all figurative phrases literally
  Idiom-register tier: NONE (recognizes no idiomatic register)
  Idiom-handling: AGGRESSIVE PARAPHRASE — all idioms rendered literally
                  (`kick the bucket` → "die"; `piece of cake` → "very easy")

LEVEL 2 — daily
  Reader profile: functional adult in daily life (backpacker / new immigrant)
  Idiom-frequency tier (English-illustrative): top ~30 universally-transparent idioms;
                                                 includes near-literal idioms ("piece of cake",
                                                 "easy as 1-2-3", "rain or shine", "out of the blue")
                                                 + a handful of high-frequency opaque idioms
                                                 ("break the ice", "under the weather")
  Idiom-register tier: casual + most-common conversational; excludes literary, archaic, biblical
  Idiom-handling: PARAPHRASE most idioms; FAMILIAR-EQUIVALENT for the top-30 transparent

LEVEL 3 — conversational
  Reader profile: average educated newspaper-reading adult
  Idiom-frequency tier (English-illustrative): top ~200–500 common idioms incl. opaque
                                                 (user's anchor `kick the bucket` sits here;
                                                 also "spill the beans", "hit the nail on the head",
                                                 "let the cat out of the bag", "burn the midnight oil",
                                                 "bite the bullet", "the ball is in your court")
  Idiom-register tier: casual + conversational-educated + journalistic;
                       excludes literary-rare, archaic, biblical, dialectal, specialist
  Idiom-handling: FAMILIAR-EQUIVALENT for common opaque; KEEP common transparent;
                  PARAPHRASE only rare or literary-archaic

LEVEL 4 — advanced
  Reader profile: university-educated reader / skilled non-native who reads widely
  Idiom-frequency tier (English-illustrative): top ~1000–2000 idioms incl. literary/academic
                                                 ("cast aspersions", "tilt at windmills",
                                                 "throw down the gauntlet", "rise to the occasion",
                                                 "Pyrrhic victory", "play one's cards close to the chest",
                                                 "lay an egg" [theater])
  Idiom-register tier: casual + conversational + journalistic + academic + general literary;
                       excludes archaic, biblical-Shakespeare-rare, dialectal, A2 specialist
  Idiom-handling: KEEP most idioms; PARAPHRASE / GLOSS only archaic or biblical;
                  FAMILIAR-EQUIVALENT for borderline

LEVEL 5 — native
  Reader profile: educated native reading broadly across literary registers
  Idiom-frequency tier (English-illustrative): all general idioms incl. archaic and
                                                 literary-rare ("give up the ghost",
                                                 "the patience of Job", "by the skin of my teeth",
                                                 "a thorn in my side", "cast pearls before swine",
                                                 "method in his madness",
                                                 "more in sorrow than in anger",
                                                 "the slings and arrows of outrageous fortune")
  Idiom-register tier: ALL general registers incl. archaic, biblical, Shakespeare-derived;
                       excludes ONLY A2 specialist domain idioms
  Idiom-handling: KEEP all general idioms including archaic; only A2 specialist domain idioms
                  get glossed or footnoted (per the A1↔A2 boundary section)
```

### Key clarifications

- A1 covers all GENERAL idiom registers including archaic, biblical, Shakespeare-derived.
- A2 covers DOMAIN-SPECIALIST idioms requiring field training (legal, financial, sports-specialist, medical-specialist).
- A1↔A2 boundary test: "does recognizing this idiom's figurative meaning require subject-domain training, or only broad general exposure?"
- Dual-membership cases (Achilles' heel, Pyrrhic victory, Crossing the Rubicon) handled per sub-field independently.
- Compositionality (transparent vs opaque) absorbed into per-level prose, correlating naturally with frequency and register.
- Proverbs at advanced/native; idiomatic phrasal verbs distributed; dead metaphors excluded.

### How SV6 differs from SV1

SV1: "5 levels for idiom-recognition; user's labels carry over; need template adaptation, distinguishing logic, examples."

SV6 commits to:
- **LIGHTLY-ADAPTED template** (3 components prefix-renamed; only substitution-test replaced) — lighter than syntactic-processing-capacity's adaptation because idioms have frequency + register like vocabulary does.
- **4 named primary handling actions** + 2 secondary, strength-graded per level.
- **Compositionality absorbed** into per-level prose (not 5th component).
- **A1↔A2 boundary for idioms** explicit with concrete legal / financial / sports examples.
- **Cross-sub-field dual-membership cases** handled independently.
- **Proverbs at advanced/native; phrasal verbs distributed; dead metaphors excluded.**
- **Conservative-bias for reader-axes** (LOWER default) re-applied.
- **All 10 surfacing frontier flags** resolved or handed off.

### Frontier flags to Decomposition

- **D1.** Per-level prose structure (idiom-frequency tier may benefit from tabular presentation or running prose with examples inline).
- **D2.** Per-level positive + negative example idioms.
- **D3.** 4 adjacent-level boundary-pair examples.
- **D4.** A1↔A2 specialist-domain idiom list (legal / financial / sports-specialist / medical).
- **D5.** Cross-sub-field dual-membership case list with handling.
- **D6.** Per-level reader-profile anchor demographics + idiom-genre anchors.
- **D7.** Migration mapping rationale.
- **D8.** Template-adaptation rationale (why lighter than syntax).

### Saturation indicators

- Perspective saturation: Phase / Calibration-State produced new anchor (LOWER default); Frame-exit Completeness produced template-adaptation refinement. No premature saturation.
- Ambiguity resolution ratio: 8/8 resolved HIGH confidence.
- SV delta: SV6 differs from SV1 in adapted-template decisions + handling-action specification + A1↔A2 + cross-sub-field handling + compositionality absorption.
- Anchor diversity: anchors from all 5 types.

All four indicators show sufficiency. Ready for decomposition.
