---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-05_17-05__a1_syntactic_processing_capacity_levels/finding.md
---
# Finding: a1_idiom_recognition_levels

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-05_17-05__a1_syntactic_processing_capacity_levels/finding.md` (the immediately-prior sibling — sub-field 2 of A1; itself refines `a1_vocabulary_breadth_levels` which refines `translation_config_axes`).

**Revision trigger:** Continuation — applying the same shape to the next A1 sub-field. The user explicitly asked: "now lets do the same for idiom-recognition."

**What's preserved:**
- A1 Reader Level as composite-axis with 5 sub-fields (root architectural commitment)
- Sub-fields 1 (vocabulary-breadth) and 2 (syntactic-processing-capacity) with their complete specs
- 4-layer framework architecture
- 8-axis structure in 4 families
- Receptive-only commitment for A1 (recognition not production)
- Language-agnosticism at concept level
- Composite-axis pattern's default-propagation mechanism
- Same labels (`very_basic | daily | conversational | advanced | native`) across A1 sub-fields
- A1↔A2 boundary as a SEPARATE per-sub-field test (vocabulary's A1↔A2 vs syntax's A1↔A2 vs idiom's A1↔A2 are all separate)
- POLICY layer commitments
- Conservative-bias-for-reader-axes = LOWER default

**What's changed:** No structural commitment of prior findings altered. This finding ADDS specification at the sub-field level for idiom-recognition, ADAPTING the template LIGHTLY (less than syntax's adaptation; idioms have frequency + register distributions like vocabulary does).

**What's new:**
- 5 named ordinal levels for idiom-recognition (same labels as A1 headline)
- A **LIGHTLY-ADAPTED 4-component template**: reader-profile + **idiom-frequency tier** (prefix-renamed from frequency-tier) + **idiom-register tier** (prefix-renamed from register-tier) + **idiom-handling test sketch** (replaces substitution-test with 4 named primary actions: PARAPHRASE / FAMILIAR-EQUIVALENT / INLINE-GLOSS / FOOTNOTE; plus 2 secondary: LITERAL-WITH-EXPLANATION / OMIT-IF-DECORATIVE)
- Strength-graded idiom-handling per level (aggressive PARAPHRASE at very_basic; none at native for general idioms; only A2 specialist gets glossed)
- Per-level positive + negative English idiom examples
- 4 adjacent-level boundary specs with idiom-pair examples
- A1↔A2 boundary clarification for IDIOMS with specialist-domain list (legal / financial / sports / medical)
- **Cross-sub-field dual-membership case list (NEW)** — 12 expressions that are simultaneously idioms AND cultural references (Achilles' heel, Pyrrhic victory, Crossing the Rubicon, Trojan horse, Catch-22, Big Brother, Cassandra, Pandora's box, Sword of Damocles, Sisyphean, Lazarus, Methuselah) handled per sub-field INDEPENDENTLY
- Suggested migration mapping parallel to prior siblings
- Template-adaptation rationale (why LIGHTER than syntactic-processing-capacity's)
- Compositionality (transparent vs opaque idioms) absorbed into per-level prose, not made a 5th component
- Proverbs at advanced/native; idiomatic phrasal verbs distributed; dead metaphors excluded

**Migration:** No production system has yet implemented `idiom_recognition` as a typed field. This finding produces the design for future pydantic / schema work. The existing 3-level `AUDIENCE_LEVEL` knob continues alongside; suggested mapping parallel to siblings.

## Question

**Context.** The three prior inquiries in this chain established A1 Reader Level as a composite-axis with 5 sub-fields. Sub-fields 1 (vocabulary-breadth) and 2 (syntactic-processing-capacity) have been spec'd. This inquiry specifies **sub-field 3: idiom-recognition** — which the root finding defined as: "ability to read figurative expressions figuratively (not literally). A high-recognition reader sees 'kick the bucket' and understands 'die'; a low-recognition reader takes it literally or freezes on the unfamiliar phrase."

**The question.** For the idiom-recognition sub-field of A1 Reader Level, what should the 5 ordinal levels be — what concept does each level capture (which kinds of idioms the reader recognizes figuratively rather than literally), what logic distinguishes each level from its neighbors, and what concrete idiom examples make each level operationally identifiable — defined language-agnostically at the concept level (English idiom examples allowed for illustration), and using a 4-component template adapted as needed from the vocabulary-breadth template?

**Goal.** Produce 5 mutually-distinct, ordinally-meaningful, spectrum-covering levels — each operationalizable as a translator-AI prompt instruction (so the AI knows which idioms to KEEP, which to PARAPHRASE, which to GLOSS), each with explicit distinguishing logic along idiom-frequency × register dimensions, each language-agnostic at the concept level.

**Scope.** Idiom-recognition ONLY. The 2 remaining A1 sub-fields (inference-capacity, cultural-reference-recognition) will be handled in their own follow-up inquiries.

## Finding Summary

- **The 5 level names match A1 headline labels:** `very_basic | daily | conversational | advanced | native`. Same labels across all A1 sub-fields for clean default-propagation; semantics are sub-field-specific (vocabulary's `conversational` = newspaper-vocabulary; syntax's = newspaper-syntax; idiom's = recognizes top ~200–500 common idioms including the user's anchor `kick the bucket`).

- **Each level has a LIGHTLY-ADAPTED 4-component definition.** Two prior templates exist: vocabulary-breadth's (reader-profile + frequency-tier + register-tier + substitution-test) and syntactic-processing-capacity's heavy adaptation (structural-complexity tier replacing frequency-tier; register/genre-tier reframed; restructuring-test replacing substitution-test). For idiom-recognition, the adaptation is **LIGHTER than syntax's** because idioms have frequency distributions and register tiers like vocabulary does. Only the substitution-test analogue needs genuine replacement. The adapted components: reader-profile (kept) + **idiom-frequency tier** (light prefix-rename from frequency-tier) + **idiom-register tier** (light prefix-rename) + **idiom-handling test sketch** (replaces substitution-test).

- **The idiom-handling test sketch names the runtime translator actions** (drawn from Newmark / Baker translation-of-idioms research). Primary actions: **PARAPHRASE** (replace idiom with its literal meaning: `kick the bucket` → "die"); **FAMILIAR-EQUIVALENT** (replace with a target-language idiom of similar meaning: English `raining cats and dogs` → Russian `льёт как из ведра` / French `il pleut des cordes`); **INLINE-GLOSS** (keep idiom + brief inline explanation: `kick the bucket — i.e., die`); **FOOTNOTE** (keep idiom + footnote). Secondary: **LITERAL-WITH-EXPLANATION** (translate literally + add explanation); **OMIT-IF-DECORATIVE** (rarely appropriate). Actions are STRENGTH-GRADED per level.

- **`very_basic` — essentially zero idiom recognition.** Treats all figurative phrases literally. Reader: young child or brand-new L2 learner. Runtime: aggressive PARAPHRASE for ALL idioms.

- **`daily` — recognizes top ~30 universally-transparent idioms.** "Piece of cake"; "easy as 1-2-3"; "rain or shine"; "out of the blue"; "break the ice"; "under the weather"; "once in a blue moon"; "make ends meet". Reader: functional adult (backpacker / new immigrant). Runtime: PARAPHRASE most; FAMILIAR-EQUIVALENT for the top-30 transparent.

- **`conversational` — recognizes top ~200–500 common idioms including opaque ones.** The user's anchor `kick the bucket` sits here. Also "spill the beans"; "hit the nail on the head"; "let the cat out of the bag"; "burn the midnight oil"; "bite the bullet"; "the ball is in your court"; "go the extra mile"; "by the book"; "in hot water". Reader: average newspaper-reading educated adult. Runtime: FAMILIAR-EQUIVALENT for common opaque; KEEP common transparent; PARAPHRASE rare/literary-archaic.

- **`advanced` — recognizes top ~1000–2000 idioms including academic / literary / less-common.** "Cast aspersions"; "tilt at windmills"; "throw down the gauntlet"; "rise to the occasion"; "Pyrrhic victory" (dual-membership); "play one's cards close to the chest"; "lay an egg" (theater meaning); "Achilles' heel" (dual-membership); "Catch-22" (dual-membership). Reader: university-educated / skilled non-native who reads widely. Runtime: KEEP most idioms; PARAPHRASE / GLOSS only archaic / Biblical; FAMILIAR-EQUIVALENT for borderline.

- **`native` — recognizes all general idioms including archaic / Biblical / Shakespeare-derived.** "Give up the ghost"; "the patience of Job"; "by the skin of my teeth"; "a thorn in my side"; "cast pearls before swine"; "method in his madness"; "more in sorrow than in anger"; "the slings and arrows of outrageous fortune"; "Crossing the Rubicon" (dual); "Trojan horse" (dual). Does NOT necessarily recognize subject-domain specialist idioms (legal / financial / sports / medical specialist) — those are A2. Reader: educated native reading broadly across literary registers. Runtime: KEEP all general idioms; only A2 specialist domain idioms get glossed or footnoted.

- **The A1↔A2 boundary for idioms is explicit:** A1 covers all GENERAL idioms across general registers including archaic and Biblical. A2 covers DOMAIN-SPECIALIST idioms requiring field training — legal ("with all deliberate speed"; "color of law"; "boilerplate"); financial ("below the line"; "haircut"); sports-specialist ("Hail Mary pass"; "tagging up"); medical specialist idioms. Borderline domain-derived idioms now in general use ("moving the goalposts"; "in the trenches"; "level playing field") are A1.advanced, NOT A2. The boundary test parallels vocabulary's and syntax's: "does recognizing this idiom's figurative meaning require subject-domain training, or only broad general exposure?"

- **The A1↔A2 boundaries for the three A1 sub-fields are SEPARATE.** A reader can have A1 idiom-recognition (recognizes general idioms) + A2 vocabulary in some domain (knows medical terms) + A1 syntactic-processing-capacity (parses general syntax). Each sub-field's A1↔A2 boundary is independent.

- **Cross-sub-field dual-membership cases handled per sub-field INDEPENDENTLY** (NEW for this inquiry). Twelve expressions are simultaneously idioms (figurative meaning) AND cultural references (source in myth / history / literature): Achilles' heel, Pyrrhic victory, Crossing the Rubicon, Trojan horse, Catch-22, Big Brother, Cassandra, Pandora's box, Sword of Damocles, Sisyphean, Lazarus, Methuselah. RESOLUTION: each sub-field tags them at its own appropriate level. A reader can know the IDIOMATIC meaning ("Achilles' heel = vulnerability point") WITHOUT knowing the CULTURAL source (Achilles from Greek myth), or vice versa. The dual-membership table in this finding gives idiom-recognition tags; the forward-looking cultural-reference-recognition column is a recommendation for the future cultural-reference-recognition sub-field inquiry — NOT a commitment of this finding.

- **Compositionality (transparent vs opaque)** is absorbed into per-level prose, not a 5th template component. Transparent idioms ("see the light"; "piece of cake") cluster at daily-conversational; opaque idioms ("kick the bucket"; "spill the beans") at conversational-and-above; archaic-literary ("give up the ghost"; "method in his madness") at native. The compositionality dimension correlates with frequency-and-register placement; no separate axis needed.

- **Proverbs, phrasal verbs, dead metaphors.** Proverbs ("a stitch in time saves nine"; "the early bird catches the worm") are sentence-length idiomatic expressions; concentrated at advanced/native. Idiomatic phrasal verbs ("give in" = surrender; "carry on" = continue; "look up" = search; "make out") are distributed across daily/conversational/advanced based on frequency. Dead metaphors ("understand" = "stand under"; "comprehend") are excluded — readers no longer process them as figurative.

- **Conservative-bias for reader-facing axes = LOWER default level.** For idiom-recognition specifically, the conservative default is at a LOWER level (assume reader recognizes fewer idioms; user dials UP if reader is more advanced). Specific default value is deferred to the defaults inquiry.

- **Migration from existing `AUDIENCE_LEVEL` is suggested**, parallel to prior siblings: `late_learner_simple → daily`; `late_learner → conversational`; `native → native`. New positions: `very_basic` (below; for zero idiom recognition) and `advanced` (between; for literary academic idiom recognition).

- **What's deferred to future inquiries.** Per-language idiom lists (English `kick the bucket` ↔ Russian `сыграть в ящик` ↔ French `casser sa pipe`); target-language idiom repertoires for the FAMILIAR-EQUIVALENT runtime action; specific conservative-bias default; remaining 2 A1 sub-fields (inference-capacity, cultural-reference-recognition — the latter will independently tag the dual-membership cases from this finding); runtime idiom-handling implementation; pydantic dataclass shape; default-derivation from A4 Purpose + A1 headline.

## Finding

### How to read this finding

The body presents:
1. **Cross-cutting framing constraints** applying to all 5 levels
2. **The LIGHTLY-ADAPTED 4-component template** with rationale
3. **Each of the 5 levels** in its own subsection
4. **The 4 adjacent-level boundary specs** with idiom-pair examples
5. **The A1↔A2 boundary for idioms** with the specialist-domain list
6. **The cross-sub-field dual-membership case list** (NEW)
7. **The suggested migration mapping**

### Cross-cutting framing constraints

- **Receptive only.** Every level specifies what the reader RECOGNIZES FIGURATIVELY when encountered, not what the reader PRODUCES.
- **Language-agnostic at concept level.** Idiom-frequency and idiom-register are universal concepts; specific idioms are per-language. English examples illustrate; per-language inquiries will produce per-language idiom lists.
- **Same 5 labels across all A1 sub-fields** for clean default-propagation; semantics sub-field-specific.
- **Idiom-handling test runtime concept.** At level L, the translator applies the appropriate handling action (PARAPHRASE / FAMILIAR-EQUIVALENT / INLINE-GLOSS / FOOTNOTE; secondary LITERAL-WITH-EXPLANATION / OMIT-IF-DECORATIVE) based on the idiom's frequency and register vs the reader's level. Runtime implementation deferred.
- **Conservative-bias for reader-facing axes = LOWER default.**
- **Handling notes:** proverbs included at advanced/native; idiomatic phrasal verbs distributed by frequency; dead metaphors excluded.
- **Cross-sub-field handling:** dual-membership cases (Achilles' heel, etc.) handled per sub-field independently.

### The LIGHTLY-ADAPTED 4-component template

The template adapts from vocabulary-breadth's. Two components are kept with light prefix-rename; one is genuinely replaced. The adaptation is **LIGHTER than syntactic-processing-capacity's** because idioms behave like vocabulary in their frequency-and-register distributions.

**1. Reader profile (kept).** Same shape as vocabulary-breadth and syntactic-processing-capacity: one-sentence description + anchor demographics + idiom-genre anchor.

**2. Idiom-frequency tier (LIGHT PREFIX-RENAME from frequency-tier).** *Why the adaptation is light:* idioms have Zipfian-like frequency distributions (idiom dictionaries provide empirical frequency data; some idioms appear far more often than others). The frequency-tier concept applies directly; only a prefix-rename is needed to scope it to idioms.

**3. Idiom-register tier (LIGHT PREFIX-RENAME from register-tier).** *Why light:* idioms span casual → colloquial → journalistic → literary → archaic → biblical registers, like vocabulary does. Same concept; light prefix-rename.

**4. Idiom-handling test sketch (GENUINE REPLACEMENT of substitution-test).** *Why genuine replacement:* for vocabulary, the runtime action is single-word LEXICAL SUBSTITUTION (`purchase → buy`). For idioms, the runtime action is multi-action HANDLING with 4 named primary actions drawn from Newmark / Baker translation-of-idioms research:

- **PARAPHRASE** — replace idiom with literal meaning
- **FAMILIAR-EQUIVALENT** — replace with target-language idiom of similar meaning
- **INLINE-GLOSS** — keep idiom + brief inline explanation
- **FOOTNOTE** — keep idiom + footnote

Plus 2 secondary actions:
- **LITERAL-WITH-EXPLANATION** — translate literally + add explanation
- **OMIT-IF-DECORATIVE** — skip if idiom is purely decorative and meaning conveyed elsewhere (rarely appropriate)

Actions are STRENGTH-GRADED per level: aggressive PARAPHRASE at very_basic; none at native for general idioms.

**Why the adaptation is LIGHTER than syntactic-processing-capacity's:** Syntax had to replace frequency-tier entirely because sentences don't follow Zipfian distributions. Register-tier also needed reframing. For idioms, both apply directly. Only the substitution-test analogue needs genuine replacement. **The principle: adapt where needed; preserve where it fits.**

### Level 1 — `very_basic`

**Reader profile.** A young child age 4–6 reading early-reader books, or a brand-new second-language learner in first weeks. Recognizes essentially zero idioms; treats all figurative expressions literally.

Anchor demographic alternatives: child age 4–6 reading literal-only prose; absolute beginner L2 learner; L2 learner first 1–2 weeks of immersion.

**Idiom-genre anchor.** Early-reader books without idioms; literal-only prose.

**Idiom-frequency tier (English-illustrative).** 0 idioms recognized.

**Idiom-register tier.** NONE — recognizes no idiomatic register.

**Idiom-handling test sketch.** AGGRESSIVE PARAPHRASE — all idioms rendered literally. `kick the bucket` → "die"; `piece of cake` → "very easy"; `out of the blue` → "suddenly."

**Positive examples.** None (recognizes 0 idioms).

**Negative examples** (above this level): "piece of cake" (daily); "kick the bucket" (conversational); any idiom.

### Level 2 — `daily`

**Reader profile.** A functional adult in daily life — backpacker, new immigrant, functional L2 speaker who has been in-country a few months. Recognizes the top ~30 universally-transparent idioms; treats most figurative expressions literally.

Anchor demographic alternatives: new immigrant functioning in L2; casual L2 learner; backpacker carrying out daily transactions.

**Idiom-genre anchor.** Practical guides with high-frequency transparent idioms only; simple news headlines.

**Idiom-frequency tier (English-illustrative).** Top ~30 universally-transparent idioms.

**Idiom-register tier.** Casual + most-common conversational. Excludes literary, archaic, biblical, dialectal, specialist.

**Idiom-handling test sketch.** PARAPHRASE most idioms; FAMILIAR-EQUIVALENT for the top-30 transparent idioms the reader recognizes.

**Positive examples** (top-30 transparent + few high-frequency opaque):
- "piece of cake"
- "easy as 1-2-3"
- "rain or shine"
- "out of the blue"
- "break the ice"
- "under the weather"
- "once in a blue moon"
- "make ends meet"

**Negative examples** (above daily): "kick the bucket" (conversational); "cast aspersions" (advanced); "give up the ghost" (native).

### Level 3 — `conversational`

**Reader profile.** An average educated newspaper-reading adult who carries informed informal conversation. Recognizes top ~200–500 common idioms including opaque ones — the user's anchor `kick the bucket` sits here.

Anchor demographic alternatives: high-school-educated adult with workplace literacy; competent L2 reader at upper-intermediate (CEFR B1–B2 idiom range); casual reader of mainstream non-fiction.

**Idiom-genre anchor.** Mainstream journalism; popular non-fiction; well-written conversational prose.

**Idiom-frequency tier (English-illustrative).** Top ~200–500 common idioms including opaque.

**Idiom-register tier.** Casual + conversational-educated + journalistic. Excludes literary-rare, archaic, biblical, dialectal, A2 specialist.

**Idiom-handling test sketch.** FAMILIAR-EQUIVALENT for common opaque idioms; KEEP common transparent; PARAPHRASE only rare or literary-archaic.

**Positive examples:**
- "kick the bucket" (user's anchor)
- "spill the beans"
- "hit the nail on the head"
- "let the cat out of the bag"
- "burn the midnight oil"
- "bite the bullet"
- "the ball is in your court"
- "go the extra mile"
- "by the book"
- "in hot water"

**Negative examples** (above conversational): "cast aspersions" (advanced); "tilt at windmills" (advanced); "give up the ghost" (native).

### Level 4 — `advanced`

**Reader profile.** A university-educated reader, a skilled non-native who reads widely, or an educated professional. Recognizes top ~1000–2000 idioms including academic / literary / less-common. Does not necessarily recognize archaic / Biblical / Shakespeare-derived idioms (those are native), nor subject-domain specialist idioms (those are A2).

Anchor demographic alternatives: university-educated professional; humanities graduate student; skilled non-native reader of literary fiction; well-read amateur literary critic.

**Idiom-genre anchor.** Academic articles; contemporary literary fiction; well-written essays; dense argumentative prose.

**Idiom-frequency tier (English-illustrative).** Top ~1000–2000 idioms including academic and literary.

**Idiom-register tier.** Casual + conversational + journalistic + academic + general literary. Excludes archaic, Biblical-Shakespeare-rare, dialectal, A2 specialist.

**Idiom-handling test sketch.** KEEP most idioms; PARAPHRASE / GLOSS only archaic / Biblical; FAMILIAR-EQUIVALENT for borderline.

**Positive examples:**
- "cast aspersions"
- "tilt at windmills"
- "throw down the gauntlet"
- "rise to the occasion"
- "Pyrrhic victory" *(dual-membership — see cross-sub-field section)*
- "play one's cards close to the chest"
- "lay an egg" (theater meaning)
- "Achilles' heel" *(dual-membership)*
- "Catch-22" *(dual-membership)*

**Negative examples** (above advanced):
- A1.native archaic Biblical: "give up the ghost"; "the patience of Job"; "by the skin of my teeth"
- A2 specialist: "with all deliberate speed" (legal); "below the line" (financial)

### Level 5 — `native`

**Reader profile.** An educated native speaker who reads broadly across literary registers including historical, archaic, and extreme-literary. Recognizes all general idioms including archaic / Biblical / Shakespeare-derived. Does NOT necessarily recognize subject-domain specialist idioms requiring field training — those are A2.

Anchor demographic alternatives: literature scholar / English-major academic; broadly-read native who enjoys archaic / Biblical-language texts (readers of Tolkien, the King James Bible, Shakespeare, Henry James).

**Idiom-genre anchor.** Henry James / Faulkner / KJV-Pauline / Shakespeare / late-Victorian literary prose with archaic-Biblical idioms.

**Idiom-frequency tier (English-illustrative).** All general idioms including archaic and literary-rare.

**Idiom-register tier.** ALL general registers including archaic, biblical, Shakespeare-derived. Excludes ONLY A2 specialist-domain idioms.

**Idiom-handling test sketch.** KEEP all general idioms including archaic. Only A2 specialist domain idioms get glossed or footnoted per the A1↔A2 boundary section.

**Positive examples:**
- "give up the ghost" (KJV-derived)
- "the patience of Job" (Bible)
- "by the skin of my teeth" (Job)
- "a thorn in my side" (NT)
- "cast pearls before swine" (Sermon on the Mount)
- "method in his madness" (Hamlet)
- "more in sorrow than in anger" (Hamlet)
- "the slings and arrows of outrageous fortune" (Hamlet)
- "Crossing the Rubicon" *(dual-membership)*
- "Trojan horse" *(dual-membership)*

**Negative examples (A2 specialist only):**
- Legal: "with all deliberate speed"; "color of law"; "boilerplate"
- Financial: "below the line"; "on the books"; "haircut" (financial)
- Sports-specialist: "Hail Mary pass"
- Medical specialist idioms

### Adjacent-level boundary specs

#### Boundary 1 — `very_basic` ↔ `daily`

**Distinguishing principle.** Shift from zero idiom recognition to the top ~30 universally-transparent idioms.

**Idiom pairs** (low-side literal rendering ↔ high-side recognized idiom):
- "very easy" ↔ "piece of cake"
- "very rarely" ↔ "once in a blue moon"
- "suddenly" ↔ "out of the blue"

#### Boundary 2 — `daily` ↔ `conversational`

**Distinguishing principle.** Shift from universally-transparent only to COMMON OPAQUE idioms entering (the user's anchor `kick the bucket` is the high-side anchor).

**Idiom pairs:**
- "very easy" (still daily-recognized) ↔ `kick the bucket` (conversational — opaque, requires recognition)
- "told a secret" ↔ "spilled the beans"
- "found the answer exactly" ↔ "hit the nail on the head"

#### Boundary 3 — `conversational` ↔ `advanced`

**Distinguishing principle.** Shift from common opaque to LESS COMMON LITERARY / ACADEMIC idioms.

**Idiom pairs:**
- "criticized harshly" ↔ "cast aspersions"
- "attempted impossibly" ↔ "tilted at windmills" (literary; Don Quixote)
- "challenged formally" ↔ "threw down the gauntlet"
- "did poorly" (theater) ↔ "laid an egg"

#### Boundary 4 — `advanced` ↔ `native`

**Distinguishing principle.** Shift from modern academic-literary to ARCHAIC / BIBLICAL / SHAKESPEARE-derived.

**Idiom pairs:**
- "died" ↔ "gave up the ghost"
- "showed great patience" ↔ "had the patience of Job"
- "barely succeeded" ↔ "by the skin of my teeth"
- "wasted effort on ungrateful audience" ↔ "cast pearls before swine"

### A1↔A2 boundary clarification for idioms

**The boundary test.** "Does recognizing this idiom's figurative meaning require subject-domain training, or only broad general exposure?" Subject-domain training → A2. Broad reading → A1.

**Important note.** A1 covers all GENERAL idiom registers including archaic, biblical, Shakespeare-derived. Archaic/biblical idioms like `give up the ghost` belong at A1.native — broad literary-reading experience is enough. A2 covers DOMAIN-SPECIALIST idioms requiring field training.

**Specialist-domain idiom list:**

| Domain | Example | Why A2 |
|---|---|---|
| **Legal** | "with all deliberate speed" | Means "as soon as practicable" (not "quickly"); requires legal-training awareness of the technical sense |
| **Legal** | "color of law" | Legal-specific term for appearance of legal authority; requires legal training |
| **Legal** | "boilerplate" | Legal/contracts specialist; requires legal training to know it refers to standard contract language |
| **Legal** | "with prejudice" / "without prejudice" | Legal-specialist meaning |
| **Financial** | "below the line" | Accounting term; requires financial training |
| **Financial** | "haircut" (financial) | Means loss on debt restructuring; requires financial training |
| **Financial** | "moving the needle" | Business strategy specialist (though entering general use) |
| **Sports-specialist** | "Hail Mary pass" | American football specialist |
| **Sports-specialist** | "tagging up" | Baseball specialist |
| **Medical** | Medical specialist idioms | Require medical training |

**Borderline domain-derived-now-general idioms (A1, NOT A2):**
- "moving the goalposts" (sports → general) — A1.advanced
- "in the trenches" (military → general) — A1.advanced
- "level playing field" (sports → general) — A1.advanced
- "in the home stretch" (sports → general) — A1.advanced
- "in the red" (financial → general for "losing money") — A1.advanced

**Cross-sub-field independence.** The A1↔A2 boundaries for vocabulary-breadth, syntactic-processing-capacity, and idiom-recognition are SEPARATE. A reader can have A1 idiom-recognition + A2 vocabulary in some domain.

### Cross-sub-field dual-membership case list

Some expressions are SIMULTANEOUSLY idioms (figurative meaning) AND cultural references (source in myth / history / literature). They are tagged HERE at their idiom-recognition level; the cultural-reference-recognition sub-field (future inquiry) will INDEPENDENTLY tag their cultural-reference level.

| Expression | Idiom-recognition level (THIS finding's commitment) | Cultural-reference level (forward-looking; NOT committed here) | Source |
|---|---|---|---|
| Achilles' heel | conversational/advanced | advanced *(suggested)* | Greek myth (Iliad) |
| Pyrrhic victory | advanced | advanced *(suggested)* | Pyrrhus of Epirus |
| Crossing the Rubicon | native | native *(suggested)* | Julius Caesar 49 BCE |
| Trojan horse | conversational/advanced | advanced *(suggested)* | Greek myth + modern computing |
| Catch-22 | conversational/advanced | advanced *(suggested)* | Joseph Heller novel (1961) |
| Big Brother | conversational/advanced | advanced *(suggested)* | Orwell 1984 (1949) |
| Cassandra | advanced | native *(suggested)* | Greek myth |
| Pandora's box | conversational/advanced | advanced *(suggested)* | Greek myth (Hesiod) |
| Sword of Damocles | advanced/native | advanced *(suggested)* | Greek/Roman story |
| Sisyphean | advanced | native *(suggested)* | Greek myth |
| Lazarus | advanced | native *(suggested)* | Bible (Gospel of John) |
| Methuselah | advanced | native *(suggested)* | Bible (Genesis) |

**Important annotations:**

1. **The "Cultural-reference level" column is FORWARD-LOOKING and NOT committed by this finding.** The future cultural-reference-recognition sub-field inquiry will set those values authoritatively; what appears here is documentation / recommendation.

2. **A reader can know one without the other.** Someone may use "Achilles' heel" to mean "vulnerability" without knowing Achilles from Greek mythology; conversely, someone deeply read in Greek myth may not know "Pyrrhic victory" is in current idiomatic use.

3. **Both sub-fields measure independent dimensions** — they're not collapsed; they're not double-counted; they're orthogonal axes that happen to address overlapping vocabulary territory.

### Migration mapping from existing `AUDIENCE_LEVEL`

| Existing | New (idiom-recognition) | Rationale |
|---|---|---|
| `late_learner_simple` | `daily` | Existing label captures readers needing simpler language; matches `daily` idiom-recognition (top-30 transparent only). |
| `late_learner` | `conversational` | Late-learner adults handle common opaque idioms (the user's anchor `kick the bucket`). |
| `native` | `native` | Identity mapping. |

**New positions:**
- `very_basic` extends BELOW for child / brand-new-L2 readers who recognize NO idioms.
- `advanced` fills middle for university-educated readers handling literary academic idioms.

This mapping is SUGGESTED. The actual migration belongs in a separate inquiry.

## Inherited Commitments Re-test

This finding refines `a1_syntactic_processing_capacity_levels` (sibling), which refines `a1_vocabulary_breadth_levels`, which refines `translation_config_axes`. The N ≥ 3 inherited commitments are listed and re-tested.

- **Commitment:** A1 Reader Level is composite-axis with 5 sub-fields.
  - **Source:** `translation_config_axes/finding.md`
  - **Re-test status:** RE-TESTED
  - **Evidence:** This finding instantiates the 3rd of the 5 sub-fields (idiom-recognition). The composite-axis pattern is honored.

- **Commitment:** A1 measures RECEPTIVE capacity (recognition not production).
  - **Source:** `translation_config_axes/finding.md`
  - **Re-test status:** RE-TESTED
  - **Evidence:** Every level's prose phrased in recognition verbs ("recognizes the figurative meaning when encountered"; "treats figurative phrases literally"; "does not recognize"). No productive verbs. Critique D2 scan verified.

- **Commitment:** A1 is language-agnostic at concept level.
  - **Source:** `translation_config_axes/finding.md`
  - **Re-test status:** RE-TESTED
  - **Evidence:** Each level annotates "Idiom-frequency tier (English-illustrative)." The CONCEPTS (idiom-frequency tier; idiom-register tier; compositionality gradient) are universal across human languages. Specific idioms are per-language (deferred to per-language inquiry).

- **Commitment:** Same labels across A1 sub-fields for default-propagation.
  - **Source:** `a1_vocabulary_breadth_levels/finding.md`
  - **Re-test status:** RE-TESTED
  - **Evidence:** This finding adopts the same 5 labels. Semantics differ per sub-field (vocabulary's `conversational` = newspaper-vocabulary; syntax's = newspaper-syntax; idiom's = user's `kick the bucket` + top ~200–500 idioms).

- **Commitment:** Conservative-bias for reader-facing axes = LOWER default.
  - **Source:** `a1_vocabulary_breadth_levels/finding.md`
  - **Re-test status:** RE-TESTED
  - **Evidence:** Applied to idiom-recognition (LOWER default = assume reader recognizes fewer idioms; user dials UP). Specific default value deferred.

- **Commitment:** A1↔A2 boundary as separate per-sub-field test.
  - **Source:** `a1_syntactic_processing_capacity_levels/finding.md` (sibling — established that A1↔A2 boundaries for syntax and vocabulary are SEPARATE)
  - **Re-test status:** RE-TESTED with EXTENSION
  - **Evidence:** Applied to idioms with the same test phrasing ("requires subject-domain training to recognize the figurative meaning"). EXTENSION: now there are 3 separate A1↔A2 boundaries (vocabulary's, syntax's, idiom's). A reader's domain-specialist boundary placement may differ across sub-fields. Sensemaking Ambiguity 4 verified.

- **Commitment:** Template adaptation is principled (replace where it doesn't fit; preserve where it does).
  - **Source:** `a1_syntactic_processing_capacity_levels/finding.md`
  - **Re-test status:** RE-TESTED with REINFORCEMENT
  - **Evidence:** Syntax's adaptation was HEAVY (frequency-tier replaced entirely; register-tier reframed). Idiom's adaptation is LIGHTER — both frequency-tier and register-tier apply with light prefix-rename; only substitution-test is genuinely replaced. The principle "adapt where needed; preserve where it fits" is reinforced by this lighter adaptation; the syntax inquiry showed the same principle producing heavier adaptation when warranted.

- **Commitment:** 4-layer framework architecture.
  - **Source:** `translation_config_axes/finding.md`
  - **Re-test status:** INHERITED-WITHOUT-RE-TEST
  - **Reason:** Out of scope for sub-field-level inquiry.

- **Commitment:** POLICY layer items (register-alternation preservation; etc.).
  - **Source:** `translation_config_axes/finding.md`
  - **Re-test status:** INHERITED-WITHOUT-RE-TEST
  - **Reason:** Out of scope. Acknowledged interaction: register-preservation policy interacts with idiom-handling at runtime (preserving high-register idioms like `give up the ghost` at the native level matches the policy; paraphrasing them at lower levels is itself a register-shift that the policy tolerates because the reader can't recognize the source register).

## Next Actions

### MUST

- **What:** Define the 5 level values + per-level 4-component specs for each of the remaining 2 A1 sub-fields (inference-capacity, cultural-reference-recognition). Each sub-field may require its own template adaptation. **The cultural-reference-recognition inquiry will INDEPENDENTLY tag the 12 dual-membership cases from this finding's cross-sub-field list.**
  - **Who:** the next 2 follow-up inquiries (cultural-reference-recognition is particularly important next since it will close the dual-membership loop).
  - **Gate:** condition-bound — before A1 Reader Level can be fully instantiated.
  - **Why:** A1 Reader Level requires all 5 sub-fields specified.

### COULD

- **What:** Define per-language idiom lists per level (English `kick the bucket` ↔ Russian `сыграть в ящик` ↔ French `casser sa pipe`; English `raining cats and dogs` ↔ Russian `льёт как из ведра`; etc.). Required for the FAMILIAR-EQUIVALENT runtime action.
  - **Who:** per-language inquiry.
  - **Gate:** when Comprehenslate adds the target language.
  - **Why:** the FAMILIAR-EQUIVALENT action requires per-target-language idiom repertoires.
  - **Depends-on:** MUST item "Define the remaining 2 A1 sub-fields" — best to spec all sub-fields for English first.

- **What:** Specific conservative-bias default value for idiom_recognition (`daily` or `conversational`?).
  - **Who:** the defaults inquiry.
  - **Gate:** condition-bound.

- **What:** Define Purpose-driven default-derivation for idiom-recognition.
  - **Who:** the defaults inquiry.

### DEFERRED

- **What:** Runtime idiom-handling implementation (LLM-judged vs frequency-list-backed; FAMILIAR-EQUIVALENT requires per-language idiom maps).
  - **Gate:** revival when level enums committed.
  - **Why (if revived):** initial LLM-judged via prose + examples; later frequency-list backing.

- **What:** Translate the 5 levels into pydantic `idiom_recognition: Literal[...]` field nested inside A1's composite-axis.
  - **Gate:** revival when structural-layer inquiry begins.

- **What:** Migration from `AUDIENCE_LEVEL` to the new `idiom_recognition` alongside other A1 sub-fields.
  - **Gate:** revival when production systems wire up the new axis.

## Reasoning

### What survived

The Final Recommended Assembly (Assembly E2 from critique) survives all 12 evaluation dimensions: Correctness (CRITICAL), Receptive-only discipline (CRITICAL), Language-agnostic at concept (CRITICAL), Mutually-distinct ordinal levels (CRITICAL), A1↔A2 boundary respect for idioms (CRITICAL), Sensemaking SV6 consistency (HIGH), Operationalizability (HIGH), Example correctness (CRITICAL), Template-adaptation coherence (HIGH; LIGHTER than syntax — justified), **Cross-sub-field boundary handling (HIGH; NEW dimension for this inquiry)**, Project-value-fit (MEDIUM), Scope-discipline (MEDIUM).

One minor clarification was incorporated: the cross-sub-field dual-membership table's "Cultural-reference level" column is explicitly annotated as FORWARD-LOOKING and NOT committed by this finding.

### Significant alternatives rejected

- **Heavy template adaptation paralleling syntax's** (renaming frequency-tier to "idiom-complexity tier" etc.). Rejected at sensemaking Ambiguity 1: idioms have Zipfian frequency distributions (unlike sentences); frequency-tier applies directly with light prefix-rename. Heavy adaptation would obscure the operational basis. Principle: adapt where needed; preserve where it fits.

- **Adding compositionality (transparent vs opaque) as a 5th template component.** Rejected at sensemaking Ambiguity 2: compositionality correlates strongly with frequency-and-register placement (transparent → daily; opaque → conversational+; archaic-literary → native). Absorbing into per-level prose is cleaner.

- **Collapsing dual-membership cases (Achilles' heel) to a single sub-field.** Rejected at sensemaking Ambiguity 3: a reader can know the idiomatic meaning without the cultural source (or vice versa). The composite-axis pattern's strength is independent measurement of orthogonal dimensions; collapsing obscures the orthogonality. Dual-membership handled per sub-field INDEPENDENTLY.

- **Treating all idioms as A1 (no A1↔A2 boundary for idioms).** Rejected at sensemaking Ambiguity 4: domain-specialist idioms (legal "with all deliberate speed"; financial "below the line"; sports "Hail Mary pass"; medical specialist) genuinely require field training to recognize the figurative meaning.

- **Excluding proverbs and phrasal verbs.** Rejected at sensemaking Ambiguity 5: proverbs are sentence-length idiomatic expressions (concentrated at advanced/native); idiomatic phrasal verbs are high-frequency idiom material (distributed across daily/conversational/advanced).

- **Including dead metaphors.** Rejected: readers no longer process them figuratively.

- **Productive-vocabulary framing.** Rejected at inherited commitment from chain: A1 is RECEPTIVE only.

- **HIGHER default for reader-axes.** Rejected: inherited principle is LOWER default for reader-facing axes.

### Why the template adaptation is lighter than syntax's

Syntactic-processing-capacity's adaptation was HEAVY: frequency-tier had to be replaced entirely (sentences don't follow Zipfian distributions); register-tier needed reframing (syntactic register has its own dynamics); substitution-test needed replacement (the runtime action for syntax is structural restructuring, not lexical substitution).

For idiom-recognition: idioms DO have Zipfian-like frequency distributions (corpus-based studies; idiom dictionaries provide empirical frequency data). Idioms span sociolinguistic registers (casual / colloquial / journalistic / literary / archaic / biblical) like vocabulary does. Both vocabulary-breadth components apply directly with light prefix-rename. Only the substitution-test analogue needs genuine replacement because the runtime action for idioms is multi-action HANDLING (4 named primary actions), not single-word substitution.

The principle: **adapt where needed; preserve where it fits.** Idioms are closer to vocabulary than syntax in their cognitive structure; the template adaptation reflects that.

## Open Questions

### Refinement Triggers

- **Per-level positive-idiom anchor refinement.** If the translator-AI mis-judges an anchor idiom's level consistently (e.g., the LLM places `Achilles' heel` at conversational when the spec tagged conversational/advanced), revisit. Trigger: observable — 5+ runtime divergences.

- **Cross-sub-field dual-membership table extension.** As more dual-membership cases emerge (e.g., new political coinages like "October surprise"), additions warranted. Trigger: observable.

- **5-level cardinality re-evaluation.** If real-user feedback clusters at 2–3 levels, collapse may be warranted. Trigger: condition-bound — after first 30 configurations.

### Research Frontiers

- **Per-language idiom equivalence mapping.** The FAMILIAR-EQUIVALENT runtime action requires per-language idiom maps. Per-language inquiries will need to produce these.

- **Idiom-frequency × register × compositionality 3D model.** This finding absorbs compositionality into per-level prose. A future inquiry might extract it as a separate dimension if usage feedback shows the conflation creates ambiguity.

### Monitoring

- **AUDIENCE_LEVEL usage statistics.** Migration mapping assumes existing labels are used as semantically intended.

### Blocked

- **Default value selection** — defaults inquiry covers all 8 axes jointly.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
now lets do the same for idiom-recognition
```

</details>
