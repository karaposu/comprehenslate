# Comprehenslate Translation Config — LLM Calibration Context

This document is the prompt context the translator-AI reads to interpret a `TranslationConfig` from `translation_config.py`. Each axis section makes the **full spectrum** visible so a single chosen value (e.g. `reader_level=daily`) calibrates against its five neighbors. Per-level definitions distinguish each level from the ones immediately above and below it, with concrete cross-cultural examples wherever applicable.

The 8 axes:

| # | Axis | Family | Cardinality | Pattern |
|---|---|---|---|---|
| A1 | reader_level | Reader | 5 levels × 5 sub-fields | composite (headline + sub-field overrides) |
| A2 | domain_expertise | Reader | 5 levels | plain ordinal |
| A3 | source_culture | Reader | 5 levels | plain ordinal |
| A4 | purpose | Purpose | 5 categories | categorical (drives defaults) |
| A5 | source_fidelity | Strategy | 4 levels | asymmetric (no `heavily-domesticated`) |
| A6 | form_preservation | Strategy | 5 levels | plain ordinal (ties to `harmony_layer.md`) |
| A7 | scaffolding | Strategy | 5 levels | plain ordinal (budget) |
| A8 | analysis_depth | Depth | 5 levels | plain ordinal (with explicit `none`) |

**Project policy: DOMESTICATE is disfavored.** Across A1's cultural-reference-recognition, A3's strategic stance, and A5's range, the translator-AI prefers foreignization-preserving alternatives (KEEP-AS-IS, INLINE-GLOSS, EXPLICATE-FUNCTION, TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT) over substitution into target-cultural equivalents. The asymmetric A5 range (no `heavily-domesticated` level) embeds this structurally.

**Receptive-only commitment for Reader-family axes.** A1, A2, A3 describe what the reader RECOGNIZES when encountered, not what the reader produces. The translator-AI's level decisions are about reception, not production.

**Conservative-bias-for-reader-axes = LOWER default level.** For A1, A2, A3, when in doubt assume LESS reader competence — defaulting to a lower level produces a more accessible translation; the user dials UP if the actual reader is more advanced. (The opposite direction holds for strategy-side axes A5/A6/A7 where conservative-bias = preserve more.)

---

## A1 — reader_level

**Concept.** The reader's overall ability to receive the translation. A1 is a *composite* axis: one headline value drives 5 sub-fields, each of which can be independently overridden when a reader's profile is uneven. The 5 sub-fields capture orthogonal-in-principle but typically-correlated abilities.

**Same enum for all 5 sub-fields:** `very_basic | daily | conversational | advanced | native`.

**The 5 sub-fields:**

- `vocabulary_breadth` — passive recognition of words
- `syntactic_processing_capacity` — parsing of complex sentence structure
- `idiom_recognition` — figurative reading of fixed phrases
- `inference_capacity` — filling in compressed / elliptical / implicit content
- `cultural_reference_recognition` — catching allusions, named figures, canonical references

For a typical reader the 5 sub-fields cluster at the same level — that's why a single `headline` value propagates. The override exists for rare-but-real cases (a non-native ESL professor: advanced vocabulary, very_basic idiom; a young heritage reader: native cultural-reference-recognition, daily vocabulary).

**Substitution-test runtime concept.** At level L, the translator-AI replaces words/structures/idioms/inferences/references above L with equivalents at or below L. The CONCEPT is captured per-level in each sub-field's handling-test sketch. The IMPLEMENTATION (LLM judgment vs frequency-list vs parser-based metric) is downstream.

**A1↔A2 boundaries are SEPARATE PER SUB-FIELD.** Each A1 sub-field carries its own A1↔A2 boundary. A sentence with general syntax but specialist medical vocabulary is A1 syntax + A2 vocabulary. The boundaries don't need to align.

### A1.a — vocabulary_breadth

How many words the reader passively recognizes.

**Frequency-tier illustrative thresholds (English; concept universal):**

| Level | Reader profile | Frequency band | CEFR |
|---|---|---|---|
| `very_basic` | Young child age 4–6 reading early-reader books, or brand-new L2 learner in first weeks | top ~500–1000 most-frequent words | ≈ A1 |
| `daily` | Functional adult — backpacker, new immigrant, L2 learner after a few months in-country | top ~2000–3000 most-frequent words | ≈ A2–B1 |
| `conversational` | Average educated newspaper-reading adult; carries informed informal conversation | top ~5000–7000 words including common Latinate | ≈ B1–B2 |
| `advanced` | University-educated reader; skilled non-native who reads widely; educated professional | top ~10000–20000 words including academic + general literary | ≈ B2–C1 |
| `native` | Educated native who reads broadly across literary registers including historical and archaic | full general vocabulary (no upper rarity bound within general lexicon) | ≈ C2+ |

**Per-level full prose:**

#### `very_basic` — function words + everyday core only

Reader: a young child age 4–6 reading early-reader books, or a brand-new second-language learner in their first weeks. Recognizes only the most everyday core vocabulary of the target language: function words, basic verbs, and the most common concrete nouns. Does not recognize Latinate, abstract, academic, literary, archaic, or specialist vocabulary.

Register tier: only everyday core. Excludes Latinate, abstract, academic, literary, archaic, and specialist.

Substitution-test: the translator replaces almost everything above the core band with descriptive paraphrase or simpler equivalents. `consider` becomes `think about`; `decision` becomes `what to do`; `purchase` becomes `buy`.

Positive examples (words AT this level): `the`, `is`, `has`, `do`, `of`, `go`, `eat`, `work`, `house`, `food`, `water`, `person`.

Negative examples (words ABOVE this level): `consider`, `decision`, `approximate`, `apparently`, `ratiocination`.

#### `daily` — functional everyday content vocabulary

Reader: a functional adult in daily life — a backpacker carrying out transactions in a foreign country, a new immigrant functioning in their second language, an L2 learner who has been in-country a few months. Recognizes vocabulary in simple signs, instructions, and casual conversation; does not recognize Latinate, academic, literary, archaic, or specialist register.

Register tier: everyday concrete + simple abstract. Excludes Latinate (`purchase`, `endeavor`, `consider`), academic, literary, archaic, and specialist.

Substitution-test: the translator replaces Latinate alternatives with Germanic everyday equivalents. `purchase` → `buy`; `endeavor` → `try`; `ostensibly` → `seemingly` / `it looks like`; `consider` → `think about`.

Positive examples: `decide`, `remember`, `carry`, `important`, `problem`, `simple`, `difficult`, `understand`, `area`.

Negative examples: `purchase`, `endeavor`, `consider`, `ostensibly`, `ratiocination`.

#### `conversational` — educated-informal register; common Latinate enters

Reader: an average educated adult who carries informed informal conversation and reads newspapers and mainstream non-fiction comfortably. Recognizes common Latinate vocabulary in educated speech (`purchase`, `consider`, `endeavor`, `approximately`) but does not read dense academic prose or literary-archaic vocabulary.

Register tier: everyday + conversational-educated + journalistic. Includes common Latinate. Excludes dense academic (`ratiocination`, `ostensibly`), literary-archaic (`verily`, `anon`), dialectal, and specialist.

Substitution-test: the translator keeps common Latinate without substitution but avoids dense academic, archaic, dialectal, and specialist vocabulary. `ratiocination` → `reasoning`; `ostensibly` → `apparently`; `verily` → `truly`.

Positive examples: `purchase`, `endeavor` (high-end of conversational; appears in newspaper register), `consider`, `approximately`, `apparently`, `generally`, `decision`, `essential`, `establish`.

Negative examples: `ostensibly`, `ratiocination`, `ameliorate`, `verily`, `whilom`.

#### `advanced` — written-educated register; academic + literary enter

Reader: a university-educated reader, a skilled non-native who reads widely across academic and literary genres, or an educated professional. Recognizes academic vocabulary (`ratiocination`, `epistemic`, `contingent`) and general literary vocabulary (`ineffable`, `putative`, `ostensibly`). Does not necessarily recognize archaic forms (`verily`, `anon`, `whilom`), dialectal vocabulary, or subject-domain specialist vocabulary (`myocardial infarction`, `habeas corpus`) — these are A2 territory.

Register tier: everyday + conversational + journalistic + academic + general literary. Excludes archaic, dialectal, and specialist-rare general.

Substitution-test: the translator avoids only archaic (`verily` → `truly`, `anon` → `soon`), dialectal, and specialist-rare general vocabulary. Academic and literary register is kept.

Positive examples: `ratiocination`, `ostensibly`, `ameliorate`, `contingent`, `putative`, `ineffable`, `epistemic`, `prescient`, `recondite`.

Negative examples (above advanced): `verily`, `anon`, `whilom` (these are native). Also (A2 specialist, here to clarify the boundary): `myocardial infarction`, `transubstantiation`.

#### `native` — all general registers including archaic + dialectal + literary-rare

Reader: an educated native who reads broadly across genres including literary fiction, historical texts, and rare literary registers. Recognizes archaic vocabulary (`verily`, `anon`, `whilom`, `thee`, `withal`), dialectal forms encountered in fiction, and literary-rare general vocabulary. Does NOT necessarily recognize subject-domain specialist vocabulary requiring field training (`myocardial infarction`, `habeas corpus`, `transubstantiation`) — these are A2 territory.

Register tier: all general registers including archaic, dialectal, literary-rare.

Substitution-test: the translator avoids ONLY A2 specialist domain vocabulary. All general vocabulary including archaic and dialectal is kept — `verily` stays as `verily`; `anon` stays as `anon`.

Positive examples: `verily`, `anon`, `thee`, `whilom`, `gainsay`, `withal`, `perchance`, `forsooth`, `wherefore`.

Negative examples (A2 specialist domain): `myocardial infarction` (medical), `habeas corpus` (legal), `transubstantiation` (Catholic theology), `kenosis` (Christian theology), `ontogenesis` (biology).

**Adjacent-level boundaries (vocabulary_breadth):**

| Boundary | Distinguishing principle | Word-pair examples |
|---|---|---|
| `very_basic` ↔ `daily` | Core/function → functional everyday content | `go ↔ decide` / `food ↔ meal` / `work ↔ job` / `house ↔ apartment` / `tell ↔ explain` |
| `daily` ↔ `conversational` | Germanic everyday → common Latinate | `buy ↔ purchase` / `try ↔ endeavor` / `think about ↔ consider` / `about ↔ approximately` / `clearly ↔ apparently` |
| `conversational` ↔ `advanced` | Conversational-educated → written-academic + literary | `apparently ↔ ostensibly` / `reasoning ↔ ratiocination` / `improve ↔ ameliorate` / `depending on ↔ contingent on` / `supposed ↔ putative` |
| `advanced` ↔ `native` | Modern educated → archaic + dialectal + literary-rare | `truly ↔ verily` / `soon ↔ anon` / `you ↔ thee` (archaic 2nd-person singular object) / `formerly ↔ whilom` / `also ↔ withal` |

**A1↔A2 boundary for vocabulary_breadth — the borderline-words table.**

The test: "Does recognizing this word require subject-domain training, or only broad general reading?" Subject-domain training → A2. Broad reading → A1.

| Word | Classification | Reasoning |
|---|---|---|
| `ratiocination` | A1.advanced | General Latinate from rhetoric/logic; no domain training; appears in literary writing |
| `ostensibly` | A1.advanced | General Latinate; common in educated writing |
| `ameliorate` | A1.advanced | General Latinate; literary and policy-discussion vocabulary |
| `contingent` | A1.advanced | General academic; cross-disciplinary |
| `epistemic` | A1.advanced (borderline) | Appears in non-specialist philosophy + general "epistemic humility" usage |
| `verily`, `anon`, `whilom` | A1.native | Archaic general; KJV / Shakespeare / historical-fiction territory |
| `thee`, `thou`, `thy` | A1.native | Archaic pronouns |
| `gainsay`, `withal`, `perchance`, `forsooth` | A1.native | Archaic literary general |
| `eschatology` | A2 theology (A1.native borderline) | Mostly theology specialist; well-read general readers may know it |
| `transubstantiation` | A2 Catholic theology | Requires Catholic-theology training |
| `myocardial infarction` | A2 medical | General readers know "heart attack" |
| `habeas corpus` | A2 legal | Requires legal training |
| `kenosis` | A2 Christian theology | Requires theology training |
| `phenomenology` | A2 philosophy specialist | Requires philosophy training |
| `epistemology` | A2 philosophy (A1.native borderline) | Less specialist than phenomenology |
| `entropy` | A1.advanced/native (commonsense use); A2 physics (technical-precise) | Borderline by context |
| `mitosis` | A2 biology | Requires biology training |
| `isotope` | A2 chemistry | Requires science training |

Borderline-default rule: when genuinely borderline, prefer A2-default (treat as requiring domain knowledge); the translator-AI will gloss or footnote unless the user explicitly set A2=specialist for the matching domain.

---

### A1.b — syntactic_processing_capacity

How dense a sentence the reader can parse without losing the thread.

**Structural-complexity tier has 5 sub-measures per level** (jointly characterizing parsing difficulty):

1. **Sentence-length range** (English-illustrative): "≤N words/sentence"
2. **Embedding depth max**
3. **Suspension load max** — number of ideas held in working memory before the main verb resolves
4. **Word-order canonicality** — canonical SVO only / + common marked / + academic-literary marked / + archaic-literary inverted
5. **Center-embedding max** — relevant at top two levels; 0 implicit below

**Restructuring-test primary actions** (strength-graded across levels): **SPLIT** (break long sentence into shorter), **UNEMBED** (pull embedded clause into its own sentence), **LINEARIZE** (convert center-embedding to left/right-branching), **ADD-CONNECTIVES** (replace implicit logical connections with explicit "because"/"however"). Secondary: **REDUCE-NOMINALIZATIONS**, **REPLACE-PARENTHETICALS**, **RESOLVE-GARDEN-PATHS**.

#### `very_basic` — SVO simple only

Reader: a young child age 4–6, or a brand-new L2 learner. Parses only SVO simple sentences; loses the thread on any coordination beyond minimal, any subordination, any marked word order.

Genre anchor: Dr. Seuss / Eric Carle / picture-book prose / children's signs / early-reader instructional text.

Structural-complexity tier: sentence-length ≤6 words; embedding depth 0; suspension load 0; word-order canonical SVO only; center-embedding 0.

Restructuring: AGGRESSIVE. Translator SPLITS any compound sentence, UNEMBEDS any embedded clause, LINEARIZES any non-canonical order, ADDS-CONNECTIVES to make all logic explicit, REDUCES-NOMINALIZATIONS.

Positive examples: "The cat sat." "The dog ran." "The man was tired." "The boy ate the apple." "The girl saw the bird."

Negative examples (above this level): "The cat sat on the mat and looked around." (coordination — daily); "The man who came home was tired." (1 relative — daily); "Even though I was hungry, I went to bed." (subordination — daily/conversational).

#### `daily` — coordination + 1 simple embedded clause

Reader: a functional adult in daily life. Parses coordinated sentences and simple relative clauses; loses the thread on multi-clause subordination, dense nominalization, marked word orders.

Genre anchor: practical instruction manuals / simple news headlines / casual conversational prose / everyday signs and notices.

Structural-complexity tier: sentence-length ≤15 words; embedding depth ≤1; suspension load ≤1; canonical SVO with minimal marked orders; center-embedding 0.

Restructuring: MODERATE. Translator SPLITS sentences longer than 15 words, ADDS-CONNECTIVES, UNEMBEDS multi-level embeddings, REDUCES-NOMINALIZATIONS.

Positive examples:
- "The cat sat on the mat, and the dog ran outside."
- "The man who came home was tired."
- "I went home because I was hungry."
- "She bought a book that her friend recommended."
- "When it rained, we stayed inside."

Negative examples (above daily): "When the cat sat down, the dog ran outside because it heard a noise that frightened it." (multi-clause subordinate linear — conversational); "The argument, despite being couched in dense subordination, succeeds." (advanced).

#### `conversational` — multi-clause linear subordination

Reader: an average educated newspaper-reading adult. Parses multi-clause subordinate sentences that proceed LINEARLY — subordinate clauses appear AFTER the main clause or as left-branching, not significantly suspending the main verb. Loses the thread on nested subordination, deep parentheticals, suspended-thread structures, center-embedding.

Genre anchor: mainstream journalism / popular non-fiction / well-written conversational prose / weekly magazine articles.

Structural-complexity tier: sentence-length ≤25 words; embedding depth ≤2 (subordinate clauses with simple embedded relatives); suspension load ≤2 (subordinate mostly AFTER main verb; short suspension acceptable); canonical + common marked orders (topicalization, common inversions); center-embedding 0.

Restructuring: LIGHT. Translator SPLITS only sentences longer than 25 words that contain dense embedding; avoids constructions with suspension greater than 2 clauses; keeps linear subordination and simple relative clauses without restructuring.

Positive examples:
- "When the cat sat down, the dog ran outside because it heard a noise that frightened it."
- "The man, who had just come home from a long day, was tired but content."
- "Even though the weather was cold, we decided to walk to the store after considering whether to drive instead."
- "The book that she bought from the shop where her brother works was exactly what she had been looking for."

Negative examples (above conversational): "The argument, despite being couched in the kind of dense subordination that requires the reader to hold three clauses in working memory before encountering the main verb, succeeds." (advanced); "Whilst it cannot be denied that the man, who, having decided..., set forth at dawn..." (native).

#### `advanced` — nested subordination + parentheticals + 3-clause suspension

Reader: a university-educated reader; a skilled non-native who reads widely; an educated professional. Parses nested subordination, parentheticals, and **up to 3-clause suspension before the main verb resolves**. Tolerates 1 center-embedding. Loses the thread on 2-deep center-embedding, 4+ clause suspension, archaic literary inversion, dialectal syntax, and subject-domain specialist syntactic conventions.

Genre anchor: academic articles / contemporary literary fiction / well-written essays / dense argumentative prose / New Yorker-style longform.

Structural-complexity tier: sentence-length ~25–40 words (no strict upper bound; complexity is the constraint); embedding depth ≤3 (nested subordination, parentheticals); suspension load ≤3 (the canonical anchor: "The argument, despite being couched in the kind of dense subordination that requires the reader to hold three clauses in working memory before encountering the main verb, succeeds."); marked orders common in academic and literary register; center-embedding ≤1.

Restructuring: MINIMAL. Translator avoids only center-embedding 2-deep or more; avoids suspension exceeding 3 clauses; keeps nested subordination, parentheticals, marked academic/literary word orders.

Positive examples:
- (The anchor sentence.) "The argument, despite being couched in the kind of dense subordination that requires the reader to hold three clauses in working memory before encountering the main verb, succeeds."
- "The cat's decision to sit, prompted by an exhaustion that had built throughout the day, was met with relief by the dog who had been waiting outside."
- "What the researchers found, contrary to what conventional wisdom would predict, was that the intervention worked best when applied gradually rather than all at once."
- "His insistence that the procedure, though admittedly novel, would yield results comparable to those of established methods proved, in the end, to be vindicated."

Negative examples (above advanced):
- A1.native: "Whilst it cannot be denied that the man, who, having decided that he ought, despite his misgivings, to attempt the journey, set forth at dawn..." (Henry-James-style; native)
- A2 legal: "Provided that the party of the first part, hereinafter referred to as the Lessor, shall..."
- A2 mathematical: "For all ε > 0, there exists δ > 0 such that |f(x) − L| < ε whenever 0 < |x − c| < δ."

#### `native` — 2-deep center-embedding + 4+ clause suspension + archaic word orders

Reader: an educated native reading broadly across literary registers including historical, archaic, and extreme-literary prose. Parses 2-deep center-embedding, 4+ clause suspension, archaic word orders (KJV-Pauline inverted constituent order), Faulkner stream-of-consciousness, late-Victorian deeply-nested literary prose. Does NOT necessarily parse subject-domain specialist syntactic conventions (legal cross-reference; mathematical formal-statement; medical-research nominalization-heavy passive) — those are A2.

Genre anchor: Henry James / Henry Adams / Faulkner / KJV-Pauline / late-Victorian literary prose / 18th-century English / archaic and literary-extreme prose.

Structural-complexity tier: sentence-length unlimited; embedding depth unlimited within general syntactic conventions; suspension load 4+ allowed; word-order includes archaic, dialectal, KJV-Pauline inverted, Faulkner stream-of-consciousness; center-embedding ≤2 (Henry James / Henry Adams anchor; 3-deep breaks even for natives).

Restructuring: NONE for general syntax. Translator preserves all general structures. ONLY A2 specialist-domain syntactic conventions are substituted, footnoted, or paraphrased.

Positive examples:
- Henry-James-style (2-deep center-embedding; 4+ clause suspension): "Whilst it cannot be denied that the man, who, having decided that he ought, despite his misgivings, to attempt the journey, set forth at dawn and encountered numerous obstacles, was perhaps unprepared, his eventual success, though qualified, was sufficient to vindicate his decision."
- KJV-Pauline archaic inversion: "Through Him to whom be glory, the work was done."
- Left-branching archaic with parenthetical participial: "What the man did, having done what he could, was return."

Negative examples (A2 specialist syntax only):
- Legal: "Provided that the party of the first part..."
- Mathematical: "For all ε > 0..."
- Medical-research: "Administration of the intervention (n = 142, mean age 54.3 ± 8.2 years) resulted in..."

**Adjacent-level boundaries (syntactic_processing_capacity):**

| Boundary | Distinguishing principle | Sentence-pair examples |
|---|---|---|
| `very_basic` ↔ `daily` | SVO-only simple → coordination + 1 simple relative | "The cat sat. The dog ran." ↔ "The cat sat on the mat, and the dog ran outside." / "The man was tired." ↔ "The man who came home was tired." |
| `daily` ↔ `conversational` | Simple coordination + 1 relative → multi-clause subordinate linear (embedding ≤2) | "I went home because I was hungry." ↔ "When the cat sat down, the dog ran outside because it heard a noise that frightened it." |
| `conversational` ↔ `advanced` | Linear multi-clause → nested + parentheticals + 3-clause suspension | "When the cat sat down, the dog ran outside because it heard a noise." ↔ (canonical anchor) "The argument, despite being couched in the kind of dense subordination that requires the reader to hold three clauses in working memory before encountering the main verb, succeeds." |
| `advanced` ↔ `native` | 3-clause suspension + 1-deep → 4+ clause suspension + 2-deep center-embedding + archaic inversion | (Advanced 3-clause suspension; 1-deep) "The argument, despite being couched in dense subordination, succeeds." ↔ (Native 4+ clause suspension; 2-deep) "Whilst it cannot be denied that the man, who, having decided that he ought, despite his misgivings, to attempt the journey, set forth at dawn and encountered numerous obstacles, was perhaps unprepared, his eventual success, though qualified, was sufficient to vindicate his decision." / Modern educated: "Through whom glory is due, the work was finished." ↔ KJV-Pauline native: "Through Him to whom be glory, the work was done." |

**A1↔A2 boundary for syntactic_processing_capacity — specialist-syntax list.**

The test: "Does parsing this sentence's STRUCTURE require subject-domain training, or only broad general reading?"

| Domain | Example | Why A2 |
|---|---|---|
| Legal | "Provided that the party of the first part, hereinafter referred to as the Lessor, shall, upon receipt of the consideration described in Section 3 herein, transfer to the party of the second part, hereinafter the Lessee, all rights, title, and interest in the property described in Schedule A hereto attached and made a part hereof." | Requires legal training to track "first part / second part" parallel structure and "hereinabove / herein / hereto" cross-reference conventions |
| Legal | "It is hereby ordered, adjudged, and decreed that the defendant, having been duly served with process and having failed to answer within the time prescribed by law, is found in default." | Documentary parataxis with formal triplet |
| Mathematical | "For all ε > 0, there exists δ > 0 such that \|f(x) − L\| < ε whenever 0 < \|x − c\| < δ." | Quantifier-conditional formal-statement structure (∀-∃-such-that); alternating quantifier scopes |
| Mathematical | "Let X be a topological space. A subset A of X is said to be open if, for every x in A, there exists an open neighborhood U of x such that U is contained in A." | Definition syntax with embedded quantifier-conditional |
| Medical-research | "Administration of the intervention (n = 142, mean age 54.3 ± 8.2 years) resulted in statistically significant (p < 0.01) improvement in primary endpoint measures, although secondary outcomes (Table 2) demonstrated heterogeneity across cohort subgroups." | Nominalization-heavy passive with parenthetical reference notation |
| Medical-research | "It was observed that, in the cohort under study, those subjects who, having received the standard treatment for a period of no less than six months, were subsequently exposed to the experimental intervention exhibited a statistically significant (p < 0.05) reduction in symptom severity." | Passive nominalization with nested subordinate clauses and parenthetical statistical notation |

---

### A1.c — idiom_recognition

Whether figurative expressions land figuratively or freeze the reader.

**Lightly-adapted template:** idiom-frequency tier + idiom-register tier + idiom-handling test.

**Primary handling actions:** **PARAPHRASE** (replace idiom with literal meaning: `kick the bucket` → "die"); **FAMILIAR-EQUIVALENT** (replace with target-language idiom of similar meaning: English `raining cats and dogs` → Russian `льёт как из ведра` / French `il pleut des cordes`); **INLINE-GLOSS** (keep idiom + brief inline explanation: `kick the bucket — i.e., die`); **FOOTNOTE** (keep idiom + footnote). Secondary: **LITERAL-WITH-EXPLANATION**, **OMIT-IF-DECORATIVE**.

Compositionality (transparent vs opaque) absorbed into level placement: transparent idioms cluster at daily-conversational; opaque idioms at conversational-and-above; archaic-literary at native.

Proverbs at advanced/native; idiomatic phrasal verbs distributed by frequency; dead metaphors (`comprehend` = "stand under") excluded — readers no longer process them figuratively.

#### `very_basic` — zero idiom recognition

Reader: young child age 4–6 or brand-new L2 learner. Recognizes essentially zero idioms; treats all figurative expressions literally.

Idiom-frequency tier: 0 idioms recognized. Idiom-register tier: NONE.

Idiom-handling: AGGRESSIVE PARAPHRASE — all idioms rendered literally. `kick the bucket` → "die"; `piece of cake` → "very easy"; `out of the blue` → "suddenly".

#### `daily` — top ~30 universally-transparent idioms

Reader: functional adult — backpacker / new immigrant / functional L2 speaker after a few months in-country. Recognizes the top ~30 universally-transparent idioms; treats most figurative expressions literally.

Idiom-frequency tier: top ~30 universally-transparent. Idiom-register tier: casual + most-common conversational. Excludes literary, archaic, biblical, dialectal, specialist.

Idiom-handling: PARAPHRASE most; FAMILIAR-EQUIVALENT for the top-30 transparent.

Positive examples (top-30 transparent): "piece of cake"; "easy as 1-2-3"; "rain or shine"; "out of the blue"; "break the ice"; "under the weather"; "once in a blue moon"; "make ends meet".

Negative examples (above daily): "kick the bucket" (conversational); "cast aspersions" (advanced); "give up the ghost" (native).

#### `conversational` — top ~200–500 common idioms including opaque

Reader: average educated newspaper-reading adult. Recognizes top ~200–500 common idioms including opaque ones — the canonical anchor `kick the bucket` sits here.

Idiom-frequency tier: top ~200–500 including opaque. Idiom-register tier: casual + conversational-educated + journalistic. Excludes literary-rare, archaic, biblical, dialectal, A2 specialist.

Idiom-handling: FAMILIAR-EQUIVALENT for common opaque; KEEP common transparent; PARAPHRASE only rare or literary-archaic.

Positive examples:
- "kick the bucket" (canonical anchor)
- "spill the beans"
- "hit the nail on the head"
- "let the cat out of the bag"
- "burn the midnight oil"
- "bite the bullet"
- "the ball is in your court"
- "go the extra mile"
- "by the book"
- "in hot water"

Negative examples (above conversational): "cast aspersions" (advanced); "tilt at windmills" (advanced); "give up the ghost" (native).

#### `advanced` — top ~1000–2000 idioms including academic + literary

Reader: university-educated reader; skilled non-native who reads widely; educated professional. Recognizes top ~1000–2000 idioms including academic, literary, less-common. Does not necessarily recognize archaic / Biblical / Shakespeare-derived (native), nor subject-domain specialist (A2).

Idiom-frequency tier: top ~1000–2000 including academic + literary. Idiom-register tier: + academic + general literary. Excludes archaic, Biblical-Shakespeare-rare, dialectal, A2 specialist.

Idiom-handling: KEEP most idioms; PARAPHRASE / GLOSS only archaic / Biblical; FAMILIAR-EQUIVALENT for borderline.

Positive examples:
- "cast aspersions"
- "tilt at windmills" (literary; Don Quixote)
- "throw down the gauntlet"
- "rise to the occasion"
- "Pyrrhic victory" *(dual-membership with cultural-reference-recognition)*
- "play one's cards close to the chest"
- "lay an egg" (theater meaning)
- "Achilles' heel" *(dual-membership)*
- "Catch-22" *(dual-membership)*

Negative examples (above advanced): A1.native archaic Biblical ("give up the ghost"; "the patience of Job"; "by the skin of my teeth"); A2 specialist ("with all deliberate speed" — legal; "below the line" — financial).

#### `native` — all general idioms including archaic + Biblical + Shakespeare-derived

Reader: educated native reading broadly across literary registers. Recognizes all general idioms including archaic, Biblical, Shakespeare-derived. Does NOT necessarily recognize subject-domain specialist idioms (A2).

Idiom-frequency tier: all general including archaic and literary-rare. Idiom-register tier: ALL general including archaic, biblical, Shakespeare-derived. Excludes ONLY A2 specialist.

Idiom-handling: KEEP all general idioms including archaic. Only A2 specialist gets glossed or footnoted.

Positive examples:
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

Negative examples (A2 specialist only): legal — "with all deliberate speed", "color of law", "boilerplate"; financial — "below the line", "on the books", "haircut" (financial); sports-specialist — "Hail Mary pass"; medical specialist idioms.

**Adjacent-level boundaries (idiom_recognition):**

| Boundary | Distinguishing principle | Idiom-pair examples |
|---|---|---|
| `very_basic` ↔ `daily` | Zero recognition → top ~30 transparent | "very easy" ↔ "piece of cake" / "very rarely" ↔ "once in a blue moon" / "suddenly" ↔ "out of the blue" |
| `daily` ↔ `conversational` | Transparent only → common opaque (canonical anchor `kick the bucket`) | "very easy" (still daily) ↔ `kick the bucket` (opaque; conversational) / "told a secret" ↔ "spilled the beans" / "found the answer exactly" ↔ "hit the nail on the head" |
| `conversational` ↔ `advanced` | Common opaque → less-common literary / academic | "criticized harshly" ↔ "cast aspersions" / "attempted impossibly" ↔ "tilted at windmills" / "challenged formally" ↔ "threw down the gauntlet" / "did poorly" (theater) ↔ "laid an egg" |
| `advanced` ↔ `native` | Modern academic-literary → archaic / Biblical / Shakespeare-derived | "died" ↔ "gave up the ghost" / "showed great patience" ↔ "had the patience of Job" / "barely succeeded" ↔ "by the skin of my teeth" / "wasted effort on ungrateful audience" ↔ "cast pearls before swine" |

**A1↔A2 boundary for idiom_recognition — specialist-domain idiom list.**

The test: "Does recognizing this idiom's figurative meaning require subject-domain training, or only broad general exposure?"

| Domain | Example | Why A2 |
|---|---|---|
| Legal | "with all deliberate speed" | Means "as soon as practicable" (not "quickly"); requires legal-training awareness of the technical sense |
| Legal | "color of law" | Legal-specific term for appearance of legal authority |
| Legal | "boilerplate" | Legal/contracts specialist |
| Legal | "with prejudice" / "without prejudice" | Legal-specialist meaning |
| Financial | "below the line" | Accounting term |
| Financial | "haircut" (financial) | Loss on debt restructuring |
| Financial | "moving the needle" | Business strategy specialist (entering general use) |
| Sports-specialist | "Hail Mary pass" | American football specialist |
| Sports-specialist | "tagging up" | Baseball specialist |
| Medical | Medical specialist idioms | Require medical training |

Borderline domain-derived now in general use (A1.advanced, NOT A2): "moving the goalposts" (sports → general); "in the trenches" (military → general); "level playing field" (sports → general); "in the home stretch" (sports → general); "in the red" (financial → general for "losing money").

**Cross-sub-field dual-membership cases (with cultural_reference_recognition).** Twelve expressions are simultaneously idioms (fixed figurative meaning) AND cultural references (source in myth / history / literature). Tagged here at idiom-recognition level; cultural_reference_recognition (A1.e) independently tags them.

| Expression | Idiom-recognition level | Source |
|---|---|---|
| Achilles' heel | conversational/advanced | Greek myth (Iliad) |
| Pyrrhic victory | advanced | Pyrrhus of Epirus |
| Crossing the Rubicon | native | Julius Caesar 49 BCE |
| Trojan horse | conversational/advanced | Greek myth + modern computing |
| Catch-22 | conversational/advanced | Joseph Heller novel (1961) |
| Big Brother | conversational/advanced | Orwell 1984 (1949) |
| Cassandra | advanced | Greek myth |
| Pandora's box | conversational/advanced | Greek myth (Hesiod) |
| Sword of Damocles | advanced/native | Greek/Roman story |
| Sisyphean | advanced | Greek myth |
| Lazarus | advanced | Bible (Gospel of John) |
| Methuselah | advanced | Bible (Genesis) |

A reader can know the IDIOMATIC meaning ("Achilles' heel = vulnerability point") WITHOUT knowing the CULTURAL source (Achilles from Greek myth), or vice versa. Each sub-field tags independently.

---

### A1.d — inference_capacity

Filling in implicit information from context (ellipses, gaps, compressed argument, anaphora, presuppositions, bridging inferences).

**Medium-adapted template:** inference-load tier (umbrella with 6 sub-measures) + register/genre-tier + gap-filling test.

**Inference-load tier — 6 sub-measures per level:**
1. **Compression-depth** — max telescoped steps the reader can fill
2. **Ellipsis-tolerance** — VP-ellipsis / gapping / sluicing / implicit subjects
3. **Anaphora-distance** — within-sentence / cross-paragraph / section-level
4. **Pragmatic-inference** — Gricean implicature recognition
5. **Presupposition-recognition** — what the text assumes the reader knows
6. **Bridging-inference** — Clark-Haviland causal/temporal implicit-link filling

**Primary gap-filling actions:** **EXPLICATE** (make implicit step explicit); **BRIDGE-CONNECTIVES** (add explicit logical connectives); **RESOLVE-ANAPHORA** (make pronoun references explicit); **UNPACK-COMPRESSION** (expand telescoped chain into separate steps); **ADD-BRIDGING-INFERENCES** (make implicit causal/temporal connections explicit); **KEEP-AS-IS** (preserve compression for high-capacity readers). Secondary: **ADD-PRESUPPOSITION-CONTEXT**.

**Orthogonal to syntactic_processing_capacity.** Parsing dense nested syntax (working-memory load on STRUCTURE) is operationally distinct from filling implicit logical steps (working-memory load on INFERENCE). Four divergence scenarios:
- *Advanced syntax + daily inference* (rare): word-by-word parser of Henry James who doesn't follow compressed argument.
- *Daily syntax + advanced inference* (more common): proverb/aphorism reader handling "Haste makes waste" (simple SVO syntax) with implicit causal chain (advanced inference). Cultural traditions of aphoristic wisdom (Confucian Analects; Sufi sayings; Talmudic sayings) develop this profile.
- *Both advanced*: typical educated literary reader.
- *Both very_basic*: child / brand-new L2.

#### `very_basic` — zero implicit content recognition

Reader: young child or brand-new L2 learner. Recognizes essentially zero implicit content; treats every text as the literal sequence of stated propositions.

Inference-load tier: compression-depth 0; ellipsis-tolerance 0; anaphora-distance ≤1 sentence; pragmatic-inference literal-only; presupposition-recognition minimal; bridging-inference 0.

Gap-filling: AGGRESSIVE all 6 primary actions. Every implicit step EXPLICATED.

Positive example (explicit-step prose): "John went to the restaurant. John saw the waiter. The waiter was rude. Because the waiter was rude, John was unhappy."

Negative example (above very_basic): Clark-Haviland 1-step ("John went to the restaurant. The waiter was rude." — implicit "John saw the waiter").

#### `daily` — 1-step Clark-Haviland bridging

Reader: functional adult. Handles 1-step Clark-Haviland bridging; simple anaphora.

Inference-load tier: compression-depth ≤1 step; ellipsis-tolerance minimal (canonical only); anaphora-distance ≤2 sentences; pragmatic-inference obvious Gricean; presupposition-recognition common cultural; bridging-inference 1-step Clark-Haviland.

Gap-filling: MODERATE. BRIDGE-CONNECTIVES between most sentences; ADD-BRIDGING-INFERENCES for unstated causal links; RESOLVE-ANAPHORA when antecedent is more than 1–2 sentences away.

Positive examples (Clark-Haviland 1-step):
- "John went to the restaurant. The waiter was rude." (reader infers "John saw the waiter")
- "She bought a cake. The candles were beautiful." (reader infers "the cake had candles")
- "He went home because he was hungry. There was nothing in the fridge."

Negative examples (above daily): news-style 2-step ("The bill passed the Senate yesterday. Critics decried it as rushed."); academic compression; Said Nursi 5-step.

#### `conversational` — 2-step news-style implicit causal

Reader: average newspaper-reading educated adult. Handles 2-step news-style implicit causal; cross-paragraph anaphora.

Inference-load tier: compression-depth ≤2 steps; ellipsis-tolerance VP-ellipsis + gapping + simple sluicing; anaphora-distance cross-paragraph; pragmatic-inference standard Gricean; presupposition-recognition educated-general; bridging-inference 2-step news-style.

Gap-filling: LIGHT. UNPACK-COMPRESSION only for academic-rare 3+ step chains.

Positive examples:
- "The Senate bill passed yesterday. Critics decried it as rushed." (implicit political-process bridging)
- "The team rallied late but fell short. Their coach offered no excuses."
- "Markets rose despite the report. Analysts attributed the resilience to forward guidance."

Negative examples (above conversational): Said Nursi 5-step; Henry-James suspended inference; A2 specialist.

#### `advanced` — 3-step compression + suspended-thread

Reader: university-educated reader. Handles 3-step compressed argument; the canonical Said Nursi 5-step telescoping sits at the upper bound here, requiring UNPACK-COMPRESSION effort.

Inference-load tier: compression-depth ≤3 steps (Said Nursi 5-step approaches upper bound); ellipsis-tolerance academic + literary; anaphora-distance long (multi-paragraph; section-level); pragmatic-inference literary-academic implicature; presupposition-recognition academic-general + literary-canonical (Shakespeare; mythology); bridging-inference 3-step + suspended-thread.

Gap-filling: MINIMAL. UNPACK-COMPRESSION for Said Nursi-style 5-step (with effort); KEEP-AS-IS most others; ADD-PRESUPPOSITION-CONTEXT for A2 specialist.

Positive examples:
- **Said Nursi 5-step istilzam (canonical anchor):** "Rahman (the Merciful) implies Rezzak (the Provider), which presupposes Rızk (sustenance), which requires Beka (continuity), which entails Vücud (existence), which necessitates İlim, İrade, Kudret (knowledge, will, power), which presuppose Hayat (life)." — 7 attributes unpacked from one word via logical-necessity chain.
- **Henry-James suspended:** "Whether what one called success would, in this case, prove sufficient — the kind of sufficiency, that is, that one had learnt to expect — remained, as ever, a question whose answer, though tacitly approached, was not, in fact, given."
- **Academic compressed argument:** "The intervention's failure — itself a contested verdict — speaks less to the design than to the unmeasured confounders that, despite extensive controls, remained available to alternative explanations."
- "He met his Waterloo" *(dual-membership)*
- "Their Trojan horse strategy" *(dual-membership)*

Negative examples (above advanced): full Said Nursi 7-step routine (native); Faulkner stream-of-consciousness (native); Quranic compressed argument (native); A2 specialist (legal "absent any showing"; mathematical "WLOG"; medical differential diagnosis).

#### `native` — 5+ step compression routinely + literary-extreme

Reader: educated native reading broadly across literary registers including classical-rare, archaic, and literary-extreme. Handles 5+ step compression routinely (full Said Nursi istilzam without effort); literary ellipsis (poetic compression); cross-paragraph compressed argument; classical-Arabic / Quranic-style maximum compression.

Inference-load tier: compression-depth 5+ routine; ellipsis-tolerance poetic + literary-extreme; anaphora-distance unlimited within general literary; pragmatic-inference full literary-rhetorical incl. archaic; presupposition-recognition literary-canonical + archaic + Biblical + classical; bridging-inference 5+ step + non-linear (associative, thematic, symbolic).

Gap-filling: NONE for general inference. KEEP-AS-IS for all general. Only A2 specialist gets ADD-PRESUPPOSITION-CONTEXT.

Positive examples:
- Full Said Nursi 7-step istilzam routine (parsed without effort)
- Faulkner stream-of-consciousness (implicit threading across paragraphs)
- Quranic-style compressed argument (classical-Arabic; maximum compression)
- KJV-Pauline: "Through Him to whom be glory, the work was done — yea, the work which, ordained before the foundations were laid, awaited only the appointed hour."
- "Crossing the Rubicon" *(dual-membership)*
- "Sisyphean labor" *(dual-membership)*

Negative examples (A2 specialist only):
- Legal: "Absent any showing that the defendant acted with malice, the doctrine of qualified immunity attaches."
- Mathematical: "WLOG (without loss of generality), let x ∈ ℝ. By induction..."
- Medical: differential diagnosis chains
- Scientific: data-to-claim conventional inference

**Adjacent-level boundaries (inference_capacity):**

| Boundary | Distinguishing principle | Text-pair example |
|---|---|---|
| `very_basic` ↔ `daily` | Explicit-everything → Clark-Haviland 1-step | explicit-all ("John went to the restaurant. John saw the waiter. The waiter was rude.") ↔ Clark-Haviland 1-step ("John went to the restaurant. The waiter was rude.") |
| `daily` ↔ `conversational` | 1-step bridging → news-style 2-step + cross-paragraph anaphora | "John went to the restaurant because he was hungry. The waiter was rude." ↔ "The bill passed the Senate yesterday. Critics decried it as rushed." |
| `conversational` ↔ `advanced` | News-style 2-step → 3-step + suspended-thread; Said Nursi 5-step approaches upper bound | "The Senate bill faces opposition for being rushed." ↔ Said Nursi 5-step istilzam (UNPACK-COMPRESSION with effort) |
| `advanced` ↔ `native` | 3-step + Said Nursi-approaching → 5+ step routine + literary-extreme + Quranic | Said Nursi 5-step condensed (advanced — UNPACK with effort) ↔ full Said Nursi 7-step istilzam routine + Faulkner stream-of-consciousness + Quranic compression (native — no effort) |

**A1↔A2 boundary for inference_capacity — specialist-domain inference list.**

The test: "Does parsing this argument's IMPLICIT STRUCTURE require subject-domain training, or only broad general reading?"

**Legal** (require legal training):
- "Absent any showing that the defendant acted with malice, the doctrine of qualified immunity attaches."
- "By operation of law, the precedent set in [case] compels..."
- "It is well-settled that, in the absence of statutory authority..."

**Mathematical** (require mathematical training):
- "WLOG (without loss of generality), let x ∈ ℝ. By induction..."
- "Trivially, it follows that f is continuous on the closed interval."
- "By the principle of mathematical induction, the result extends to all n ∈ ℕ."

**Medical** (require medical training):
- Differential diagnosis chains
- "Suggestive of a paraneoplastic syndrome; further workup indicated."
- Clinical-reasoning conventions

**Scientific** (require scientific training):
- "Results suggest..." — data-to-claim
- "Consistent with the hypothesis that..." — statistical-presupposition
- "By the principle of..." — domain-axiom implicit-invocation

Borderline (A1, NOT A2): humanities-general inference chains; literary-criticism inference; academic-philosophy inference.

**Cross-sub-field dual-membership cases (with cultural_reference_recognition).** Allusion-inference cases requiring BOTH cultural-ref recognition AND inferring current-context relevance:

| Expression | Inference-capacity level | Source |
|---|---|---|
| "He met his Waterloo" | advanced | Napoleon 1815 |
| "She was their Joan of Arc" | advanced | French history |
| "Crossing the Rubicon" | native | Caesar 49 BCE |
| "Their Trojan horse strategy" | advanced | Iliad/Aeneid + modern |
| "He played the Cassandra role" | advanced | Greek myth |
| "Sisyphean labor" | advanced | Greek myth |
| "Pyrrhic victory" (argument context) | advanced | Pyrrhus |
| "He came back like Lazarus" | advanced | Bible Gospel of John |

Several overlap with idiom_recognition's dual-membership table (Trojan horse, Pyrrhic victory, Crossing the Rubicon, Catch-22). A reader at advanced inference-capacity but daily idiom-recognition can recognize the allusion-inference but not the fixed-idiom status — rare but real.


---

### A1.e — cultural_reference_recognition

Whether allusions, named figures, and canonical references land without explanation. **Maps to a 5-tier canonicity ladder** drawn from cultural-literacy research (Hirsch *Cultural Literacy*; Bourdieu cultural-capital strata).

**Important distinction from A3.** A1.e is **competence-based** (does the reader KNOW the references?). A3 is **identity-based** (does the reader COME FROM inside the source's culture?). All four corners of the joint distribution are real:

|  | A1.e high (well-read) | A1.e low (uninitiated) |
|---|---|---|
| **A3 source-native** | Born Muslim Islamic-studies professor | Born Muslim with no formal study |
| **A3 outsider** | Western academic Islamicist | Typical Western non-Muslim reader |

**Reader-relative canon (not source-relative).** The level captures what THE READER recognizes. A Western-secular reader is `very_basic` for the Quranic canon regardless of whether they're reading Said Nursi (whose source canon is Islamic-Sufi).

**Canon-choice is OUT OF SCOPE** here. It belongs at the audience-configuration layer — an `audience.canon_set: list[str]` field would specify which canons the reader's recognition operates over (`["greek_roman", "biblical", "literary_western", "said_nursi_corpus"]`). This sub-field operates on a presumed-target canon.

**Markedness and transparency are TEXT/REFERENCE properties, not level dimensions.** Markedness = whether source signposts the reference ("as the Greeks said..."). Transparency = whether reference functions metaphorically without source-knowledge (the "Trojan horse" works as a metaphor for "deceptive gift" even without knowing the *Iliad*; "Catch-22" doesn't without Heller). These modulate the translator-AI's runtime action choice but aren't reader-level dimensions.

**5 handling actions (preference order; DOMESTICATE last-resort per project policy):**

1. **KEEP-AS-IS** — preserve the reference; trust reader recognition.
2. **INLINE-GLOSS** — brief in-translation explanation: "the Sword of Damocles — an ever-present threat".
3. **EXPLICATE-FUNCTION** — paraphrase what the reference is *doing* without naming it: "his decisive irreversible commitment" instead of "his crossing of the Rubicon". The foreignization-preserving alternative to DOMESTICATE.
4. **FOOTNOTE** — externalize the explanation.
5. **DOMESTICATE** — replace with target-culture analogue. DISFAVORED; reserved for `very_basic` + opaque + unmarked + EXPLICATE-FUNCTION would burden the text.

Preference order at any level: `KEEP-AS-IS > INLINE-GLOSS > EXPLICATE-FUNCTION > FOOTNOTE > DOMESTICATE (last resort)`.

#### `very_basic` — ubiquitous-canon ONLY, unreliably

Reader: minimal canonical exposure. Has heard the most ubiquitous references but cannot reliably trace them to canonical sources. Has heard "Garden of Eden" and "Trojan horse" but may not connect them to specific canonical sources. References at higher tiers — Pyrrhic victory, Cassandra, Bovarysme, Faustian bargain — are not reliably caught.

Canonicity tier: ubiquitous-canon only, unreliably (catches the most-ubiquitous like "Garden of Eden" / "Trojan horse" only when supported by inline framing).

Register/canon-tier: handles current-events and everyday-conversational canon. Religious-sermon-canon, scientific-canon, literary-canon all beyond reliable recognition.

Cultural-reference handling: assumes reader will miss any non-ubiquitous reference. INLINE-GLOSS for short ubiquitous references reader might still miss; FOOTNOTE or EXPLICATE-FUNCTION for educated-mainstream and higher; KEEP-AS-IS only when reference is BOTH ubiquitous AND transparent ("Trojan horse" as a metaphor can be kept; "Pyrrhic victory" cannot). DOMESTICATE as last resort for opaque-unmarked-educated where EXPLICATE-FUNCTION would burden.

Cross-cultural examples across canons:
- *Greek/Roman*: "Trojan horse" → KEEP-AS-IS (transparent); "Pyrrhic victory" → EXPLICATE-FUNCTION ("a costly win that wasn't worth winning"); "Cassandra" → FOOTNOTE or INLINE-GLOSS.
- *Biblical*: "Garden of Eden" → KEEP-AS-IS; "David and Goliath" → KEEP-AS-IS (transparent); "Methuselah" → INLINE-GLOSS ("a very old man, like Methuselah").
- *Said Nursi corpus*: "Bediuzzaman" (Said Nursi's honorific) → FOOTNOTE; "Sözler" → INLINE-GLOSS or "The Words (Sözler)"; "İsm-i azam" → EXPLICATE-FUNCTION ("the greatest name of God").
- *Quranic*: "Prophet Musa" → INLINE-GLOSS ("Prophet Moses (Musa)"); references to *isra'* (the Night Journey) → FOOTNOTE.
- *Confucian*: "junzi" → EXPLICATE-FUNCTION ("the morally exemplary person"); "Confucius said" → KEEP-AS-IS (the name carries).
- *Hindu/Sanskrit*: nothing reliable; INLINE-GLOSS or FOOTNOTE everything.

#### `daily` — ubiquitous (reliably) + first slice of educated-mainstream

Reader: working cultural literacy at the level of an attentive consumer of mass media and general adult conversation. Catches ubiquitous references reliably; picks up some educated-mainstream references when context is supportive. Misses the deeper educated-mainstream that requires literary-historical exposure (Bovarysme, Goethe's Faust beyond "Faustian bargain", Roman political references like "Caesar's wife").

Canonicity tier: ubiquitous (reliably) + first slice of educated-mainstream (Big Brother, Catch-22, Kafkaesque as adjective, David-and-Goliath as metaphor).

Register/canon-tier: journalistic + current-events at the educated-mainstream tier. Catches well-known religious references at the ubiquitous tier (Good Samaritan; David and Goliath; Eden). Cross-cultural specificity begins to navigate.

Cultural-reference handling: KEEP-AS-IS for ubiquitous-canon (both transparent and opaque) and first slice of educated-mainstream (Big Brother; Catch-22; Kafkaesque). INLINE-GLOSS for deeper educated-mainstream (Pyrrhic victory; Sword of Damocles; Faustian bargain). EXPLICATE-FUNCTION for literary-educated and above. FOOTNOTE for specialist-canonical and scholar-canonical the reader encounters but cannot place.

Cross-cultural examples:
- *Greek/Roman*: "Pyrrhic victory" → INLINE-GLOSS or KEEP-AS-IS depending on transparency in context; "Crossing the Rubicon" → KEEP-AS-IS if marked + transparent; "Achilles' heel" → KEEP-AS-IS.
- *Biblical*: "Methuselah" → KEEP-AS-IS; "Job's patience" → KEEP-AS-IS or INLINE-GLOSS; "Lazarus" → KEEP-AS-IS for metaphoric ("Lazarus rising").
- *20th-c. literary*: "Big Brother" → KEEP-AS-IS; "Catch-22" → KEEP-AS-IS; "Kafkaesque" → KEEP-AS-IS.
- *Said Nursi corpus*: "Sözler" → INLINE-GLOSS as title; "Bediuzzaman" → FOOTNOTE explaining the lakap; "İsm-i azam" → INLINE-GLOSS.
- *Historical*: "Waterloo" → KEEP-AS-IS for "met his Waterloo"; "Watergate" → KEEP-AS-IS.

#### `conversational` — ubiquitous + educated-mainstream (complete)

Reader: cultural literacy at the level of a college-educated adult who reads widely in journalism, mainstream literature, and general non-fiction. Catches the canonical set a high-school-educated member of the target culture would know — including most Greek/Roman myth-references in metonymic use ("Pyrrhic victory"; "Sword of Damocles"); standard Biblical references; canonical Shakespeare; canonical 20th-century literary references (Catch-22; Big Brother).

Canonicity tier: ubiquitous + educated-mainstream (complete). Misses literary-educated references requiring humanities-undergraduate exposure (Dante's Beatrice; Madame Bovary; Jean Valjean as specifically Hugo's character; Augustan Age).

Register/canon-tier: educated-mainstream across genres: journalistic + religious-sermon at the canonical level + popular-literary canon (Shakespeare's most famous; Dickens's most famous). Cross-cultural specificity reliably navigated for dominant cultural canon of reader's background, partial for adjacent canons.

Cultural-reference handling: KEEP-AS-IS for ubiquitous + educated-mainstream. INLINE-GLOSS for literary-educated when reference is clearly invoked but reader may not place it (mentioning "Karenin" in a context that needs Anna Karenina specifically). EXPLICATE-FUNCTION rarely needed; FOOTNOTE for the occasional specialist-canonical reference the reader cannot place.

Cross-cultural examples:
- *Greek/Roman*: "Sword of Damocles" → KEEP-AS-IS; "Pyrrhic victory" → KEEP-AS-IS; "Sisyphean task" → KEEP-AS-IS.
- *Biblical*: "Methuselah" → KEEP-AS-IS; "the Lazarus moment" → KEEP-AS-IS; "thirty pieces of silver" → KEEP-AS-IS.
- *Literary canonical*: "Faustian bargain" → KEEP-AS-IS; "Hamlet's dilemma" → KEEP-AS-IS; "quixotic" → KEEP-AS-IS.
- *Said Nursi corpus*: "Bediuzzaman" → KEEP-AS-IS with one-time gloss in chapter introduction; "Risale-i Nur" → KEEP-AS-IS as established title; references to Mevlana → INLINE-GLOSS ("Mevlana (Rumi)") if the Persian-poetry canonicity isn't reliable for the reader.
- *Hindu/Sanskrit*: reference to "Arjuna's dilemma" → INLINE-GLOSS for Western-conversational; reference to Krishna's role → KEEP-AS-IS with INLINE-GLOSS if needed.

#### `advanced` — + literary-educated tier (humanities-undergraduate)

Reader: humanities-undergraduate-equivalent cultural literacy. Has read canonical Western literature broadly; has working familiarity with major non-Western canons through coursework or sustained reading. Catches literary-educated references; approaches specialist-canonical references with comfort.

Canonicity tier: + literary-educated. Specialist-canonical references appear but reader may need brief support (mention of a Habakkuk-prophet reference may need INLINE-GLOSS).

Register/canon-tier: literary canon broadly; reliably navigates cross-canon references (recognizes a Quranic reference in a text using both Quranic and Greek canon; tells Hindu from Buddhist from Confucian). Religious-sermon, philosophical, literary registers all handled at the literary-educated tier.

Cultural-reference handling: KEEP-AS-IS as default for ubiquitous + educated-mainstream + literary-educated. INLINE-GLOSS only when a specialist-canonical reference is invoked that may exceed the reader's tier. EXPLICATE-FUNCTION rarely needed; FOOTNOTE for true scholar-canonical.

Cross-cultural examples:
- *Greek/Roman*: "Procrustean bed" → KEEP-AS-IS; "Promethean fire" → KEEP-AS-IS; references to Niobe → KEEP-AS-IS.
- *Biblical*: "Habakkuk" → KEEP-AS-IS or INLINE-GLOSS; "Melchizedek" → KEEP-AS-IS for advanced reader.
- *Literary canonical*: "Bovarysme" → KEEP-AS-IS; "Karamazov-esque guilt" → KEEP-AS-IS; "Jean Valjean" as specifically Hugo's character → KEEP-AS-IS.
- *Said Nursi corpus*: references to Mevlana, Abdulkadir-i Geylani → KEEP-AS-IS; references to specific theological-school history (Maturidi vs Ashari) → INLINE-GLOSS.
- *Persian/Quranic*: Rumi quotations → KEEP-AS-IS; references to Hafez → KEEP-AS-IS; references to *isra'* and *miraj* → KEEP-AS-IS.

#### `native` — all 5 tiers including specialist + scholar-canonical

Reader: specialist cultural literacy in the relevant canon — humanities scholar, theological scholar, classical-studies expert, or specialist in the source culture. Catches references at scholar-canonical depth.

Canonicity tier: all 5 tiers including specialist-canonical and scholar-canonical. References to lesser figures (Erysichthon, Phaedra, Iphigenia from Greek; Onan, Melchizedek from Biblical; specific Sufi figures from Islamic mystical tradition) caught silently.

Register/canon-tier: native-level canon-handling across all genres. Religious-sermon canon at scholar depth; literary canon at scholar depth; philosophical canon at scholar depth.

Cultural-reference handling: KEEP-AS-IS for everything. Translator-AI's role at this level is preservation; no glossing, footnoting, or explication. Reader catches the references silently and the translation reads as in the source.

Cross-cultural examples:
- *Greek/Roman*: "Erysichthon" → KEEP-AS-IS; "Niobe's tears" → KEEP-AS-IS; "Tantalus" → KEEP-AS-IS.
- *Biblical*: "Habakkuk" → KEEP-AS-IS; "Melchizedek" → KEEP-AS-IS; "Onan" → KEEP-AS-IS.
- *Literary canonical*: Joyce's Bloomsday → KEEP-AS-IS; Bartleby → KEEP-AS-IS; specific Tolstoy characters → KEEP-AS-IS.
- *Said Nursi corpus (Nursi-specialist reader)*: all Risale-i Nur internal references including lesser-known prophets in Quranic accounts, theological-school positions, all Sufi figures → KEEP-AS-IS.
- *Specialist Islamic theology*: Maturidi vs Ashari vs Mutazila → KEEP-AS-IS; al-Razi vs al-Ghazali → KEEP-AS-IS.

**Adjacent-level boundaries (cultural_reference_recognition):**

- `very_basic` → `daily`: from "ubiquitous-only, unreliably" to "ubiquitous (reliably) + first slice of educated-mainstream". The `daily` reader catches ubiquitous references reliably and starts picking up well-known educated-mainstream references from journalism and pop culture.
- `daily` → `conversational`: from "first slice of educated-mainstream" to "full educated-mainstream". The `daily` reader has spotty coverage (gets Big Brother and Kafkaesque but may miss Pyrrhic victory or Sword of Damocles); the `conversational` reader has complete coverage.
- `conversational` → `advanced`: "+ literary-educated tier" — adds humanities-undergraduate-equivalent coverage (Dante's Beatrice; Bovarysme; mid-tier Russian literary canon).
- `advanced` → `native`: "+ specialist-canonical + scholar-canonical" — scholar-depth coverage; catches the lesser figures, specialist theological positions, canon-internal cross-references.

**A1↔A2 boundary for cultural_reference_recognition — the specialist-canon test.**

The test: "Does recognizing this reference require subject-domain training, or only broad general reading within the recognized canon?"

A1 covers GENERAL cultural-canonical knowledge across the recognized canon. A2 covers DOMAIN-specialist canon-knowledge requiring focused training. Five specialist-domain canons illustrate A2 territory:

1. **Legal-history precedents.** Marbury v. Madison, Brown v. Board of Education, Roe v. Wade, Dred Scott — recognized by legal-trained readers.
2. **Mathematical figures and concepts.** Cantor's diagonal, Gödel's theorems, Russell's paradox, Hilbert's problems, the Riemann hypothesis. Gray-zone: Pythagorean theorem has migrated specialist → general.
3. **Scientific figures and concepts.** Maxwell's equations, Bohr's atom, Pasteur (germ theory), Feynman diagrams. Gray-zone: Einstein has migrated specialist → general.
4. **Medical eponyms.** Alzheimer's, Parkinson's (migrated to general usage); Charcot, Hodgkin's lymphoma, Bell's palsy (remain specialist).
5. **Specialist philosophy.** Heideggerian (beyond popular "existentialism"), Wittgensteinian (beyond popular name-drop), Hegelian dialectic at the specialist level. Gray-zone: Marx's canonicity tier varies by political-canon.

Gray-zone cases acknowledged. Einstein moved specialist → general. Pythagorean theorem similarly. The framework assumes a SNAPSHOT at config time; gray-zone cases need periodic re-classification.

**Triple-overlap union rule.** When a reference fires multiple A1 sub-fields simultaneously (Crossing the Rubicon fires idiom-recognition + inference-capacity + cultural-reference-recognition), the translator-AI applies the UNION of per-sub-field handling rules; the more-explicating action wins. Example: at `daily` reader level, "Crossing the Rubicon" might be KEEP-AS-IS by cultural-ref's rule (educated-mainstream canonicity tier; daily catches it) but INLINE-GLOSS by inference-capacity's rule (compression-depth is non-trivial). Union selects INLINE-GLOSS.

**Cross-sub-field dual-membership table (cultural_reference_recognition column).** Independent classification of the 14 dual-membership entries forward-flagged by idiom-recognition and inference-capacity:

| Entry | Canonicity tier | very_basic | daily | conversational | advanced | native |
|---|---|---|---|---|---|---|
| Achilles' heel | educated-mainstream | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Pyrrhic victory | educated-mainstream | EXPLICATE-FUNCTION | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Crossing the Rubicon | educated-mainstream | EXPLICATE-FUNCTION | KEEP-AS-IS (if marked) | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Trojan horse | ubiquitous (transparent) | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Catch-22 | educated-mainstream | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Big Brother | ubiquitous (modern usage) | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Cassandra | educated-mainstream | FOOTNOTE or EXPLICATE-FUNCTION | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Pandora's box | ubiquitous | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Sword of Damocles | educated-mainstream | EXPLICATE-FUNCTION | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Sisyphean | educated-mainstream | EXPLICATE-FUNCTION | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Lazarus | educated-mainstream (Biblical) | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Methuselah | educated-mainstream (Biblical) | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| He met his Waterloo | educated-mainstream | EXPLICATE-FUNCTION ("his decisive defeat") | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |
| Joan of Arc | educated-mainstream-to-literary-educated | INLINE-GLOSS or FOOTNOTE | INLINE-GLOSS | KEEP-AS-IS | KEEP-AS-IS | KEEP-AS-IS |


---

## A2 — domain_expertise

**Concept.** The reader's specialist knowledge IN the source's subject domain (Islamic theology for Said Nursi; biblical scholarship for Bible passages; theoretical physics for a physics paper; legal scholarship for case law). **Independent of A1's general fluency.** A non-native ESL Bible scholar can be A1=very_basic + A2=expert; a native-English reader with no Islamic background can be A1=native + A2=lay. Both are real.

**Plain ordinal. Single value applies to the source's single domain (auto-detected at runtime; multi-domain audience configuration deferred).**

**Levels:** `lay | aware | educated | trained | expert`

Anchored to Hubert and Stuart Dreyfus's 5-stage skill-acquisition model (novice / advanced-beginner / competent / proficient / expert). Why these labels diverge from A1's: A1 is composite-axis with same-labels-for-propagation; A2 is plain-ordinal, no propagation, labels need only be domain-meaningful. "Daily domain expertise" reads oddly; "aware" reads cleanly.

**A2's 5 sub-aspects rise together (not separate axes):**

1. **Technical-vocabulary depth** — count of specialist terms recognized.
2. **Conceptual-schema integration** — how well the reader places concepts in the domain's relational structure.
3. **Discourse-conventions recognition** — recognizing school-internal debates, lineage of arguments, scholarly genres.
4. **Specialist-debates recognition** — catching "this is the Mu'tazila position" or "this is Calvinist" without prompting.
5. **Primary-source canon familiarity** — specialist reads primary; lay reads secondary if any.

**9 handling actions in 2 categories + 1 bridge:**

*Vocabulary-level (technical terms):*
- **USE-TECHNICAL-VOCABULARY-FREELY** — at `expert`/`trained`; use the technical term without unpacking.
- **INLINE-DEFINE-ON-FIRST-USE** — "tafsīr (Quranic exegesis)" first time, bare term after. At `educated`/`trained` for sub-specialist terms.
- **FOOTNOTE-TECHNICAL-TERM** — technical term in body, definition in footnote. At `aware`/`educated` for terms needing substantial unpacking.
- **PARAPHRASE-IN-LAYMAN-TERMS** — replace technical term with everyday equivalent ("commentary" instead of "tafsīr"). At `lay`.

*Discourse-level (school-internal debates):*
- **INVOKE-SPECIALIST-DEBATES** — "the Ash'ari position vs the Mu'tazila position on attributes of God". At `expert`.
- **ATTRIBUTE-VIEW-TO-SCHOOL** — "the Ash'ari position holds…" without engaging debates. At `trained`.
- **UNATTRIBUTED-CONSENSUS** — present mainstream view without school-internal attribution. At `educated`.
- **AVOID-SPECIALIST-DEBATES** — don't invoke school-internal references at all. At `aware`/`lay`.

*Bridge:*
- **KEEP-SOURCE-TERM-WITH-GLOSS** — "ism-i azam (the greatest name of God)". Used across levels for source-language terms whose form is load-bearing.

**Conservative-bias = LOWER default.** Protects against the "I'll just use the technical term; they probably know it" failure.

#### `lay`

Reader: no domain background. Has not studied the source's subject domain in any formal or substantial-informal way. The technical vocabulary reads as foreign words; the conceptual structure is opaque; school-internal debates are invisible. May know the broadest cultural-anchor concepts (Islam exists; there's an Old Testament and a New Testament; physics studies matter and energy) but nothing beyond.

Expertise-depth tier: recognizes the domain's existence as a category of human activity but does not recognize technical terms, does not navigate conceptual schemas, does not catch school-internal positions, does not engage with primary or secondary literature.

Discourse-register tier: only journalistic-level register about the domain (a New York Times article mentioning "the Quran"). Religious-sermon, scholarly-treatise, primary-source register all beyond reliable recognition.

Domain-handling: PARAPHRASE-IN-LAYMAN-TERMS for any non-ubiquitous technical term; FOOTNOTE only for terms whose source-language form is load-bearing. AVOID-SPECIALIST-DEBATES entirely; UNATTRIBUTED-CONSENSUS for any view the source invokes.

Examples across domains:
- *Islamic theology (Said Nursi)*: doesn't reliably know "Allah" is the standard Arabic word for God; may think "Muhammad" might be a generic name. References to "tafsīr" → PARAPHRASE as "interpretive commentary." References to "Bediuzzaman" → INLINE-GLOSS as "Bediuzzaman (Said Nursi's honorific)" or FOOTNOTE. References to "ism-i azam" → KEEP-SOURCE-TERM-WITH-GLOSS ("the greatest name of God").
- *Biblical scholarship*: knows there's an Old Testament and New Testament; may not know what "Torah" means specifically (PARAPHRASE as "the first five books of the Bible"). References to "the Documentary Hypothesis" → FOOTNOTE.
- *Theoretical physics*: knows physics studies "matter and energy"; doesn't know what "quantum" means precisely. References to "Schrödinger equation" → FOOTNOTE.
- *Legal scholarship*: knows there are courts and lawyers; doesn't know "tort" or "common law" precisely. References to "stare decisis" → PARAPHRASE as "the principle that courts follow precedent."
- *Philosophy*: knows philosophy exists; may confuse Plato and Aristotle. References to "Cartesian dualism" → PARAPHRASE as "Descartes's view that mind and body are separate."

#### `aware`

Reader: cultural-general exposure to the domain through general adult life (journalism, casual conversation, mass media). Has not studied the domain.

Expertise-depth tier: recognizes major figures and concepts at journalistic depth. Doesn't recognize specialist terms beyond the most-popularized. Has no integrated conceptual schema; concepts are isolated cultural-general facts. School-internal debates are invisible. Has not read primary or substantial secondary literature.

Discourse-register tier: journalistic + popular-book level (Karen Armstrong introduction to Islam; Bart Ehrman introduction to NT; James Gleick popular physics). Scholarly-treatise and primary-source register beyond reliable recognition.

Domain-handling: PARAPHRASE-IN-LAYMAN-TERMS for specialist terms; INLINE-DEFINE-ON-FIRST-USE for popular-book-level terms; KEEP-SOURCE-TERM-WITH-GLOSS for source-language load-bearing terms. AVOID-SPECIALIST-DEBATES; UNATTRIBUTED-CONSENSUS for mainstream views.

Examples across domains:
- *Islamic theology*: knows "Allah / Muhammad / Quran" exist as religious terms; knows 5 pillars by name; knows Sunni / Shia split exists. References to "tafsīr" → INLINE-DEFINE on first use ("tafsīr (Quranic exegesis)"). References to "kalam" → PARAPHRASE as "Islamic theology." References to "the Ash'ari position" → AVOID-SPECIALIST-DEBATES or UNATTRIBUTED-CONSENSUS.
- *Biblical scholarship*: knows basic narratives (Genesis, Exodus, Gospels); recognizes "Pharisee" pejoratively; has heard of Apostle Paul. References to "the Documentary Hypothesis" → INLINE-DEFINE.
- *Theoretical physics*: knows Newton / Einstein / Hawking; knows quantum mechanics and general relativity by name; recognizes E=mc². References to "quantum entanglement" → INLINE-DEFINE.
- *Legal scholarship*: knows the Constitution exists; knows there's a Supreme Court; has heard of Brown v. Board. References to "stare decisis" → INLINE-DEFINE.
- *Philosophy*: knows major figures (Plato / Aristotle / Descartes / Kant); knows "philosophical" as a vague-thoughtful term. References to "Kant's categorical imperative" → INLINE-DEFINE.

#### `educated`

Reader: has read general literature on the source's domain. Working amateur knowledge — undergraduate-survey-equivalent or sustained personal reading project. Handles the domain's mainstream conceptual framework. "Educated" here specifically means EDUCATED-IN-THIS-DOMAIN (not just generally educated; A1 covers general fluency).

Expertise-depth tier: recognizes mainstream concepts and figures. Has the start of an integrated conceptual schema. Begins to recognize that school-internal debates exist but doesn't navigate them deeply. Has read general-audience secondary literature; perhaps some accessible primary sources.

Discourse-register tier: popular-book + introductory-academic level (Wadood Hamid translation; Norton Anthology introduction; James Gleick popularization). Scholarly-treatise and primary-source register at the edge.

Domain-handling: USE-TECHNICAL-VOCABULARY-FREELY for mainstream terms; INLINE-DEFINE-ON-FIRST-USE for specialist terms; KEEP-SOURCE-TERM-WITH-GLOSS for source-language terms whose form matters. UNATTRIBUTED-CONSENSUS as primary mode; ATTRIBUTE-VIEW-TO-SCHOOL when school-internal debates are central.

Examples:
- *Islamic theology*: knows the shahada components; understands "tawhid" (divine oneness); knows "tafsīr" as Quranic exegesis. References to "Mu'tazila" → INLINE-DEFINE first use ("Mu'tazila (a rationalist Islamic theological school)"). References to specific Sufi figures → KEEP-SOURCE-TERM-WITH-GLOSS.
- *Biblical scholarship*: knows canon order; understands "Synoptic Gospels"; recognizes major figures (Moses, David, John the Baptist, Paul); has heard of the Septuagint. References to "JEDP" → INLINE-DEFINE.
- *Theoretical physics*: undergraduate physics literacy; understands entropy; recognizes Schrödinger's cat as thought experiment; knows basic standard model structure. References to "the measurement problem" → INLINE-DEFINE.
- *Legal scholarship*: understands tort / contract / criminal distinction; "stare decisis" as precedent; recognizes major Supreme Court cases (Brown, Roe, Marbury). References to "the dormant commerce clause" → INLINE-DEFINE.
- *Philosophy*: undergraduate-philosophy-equivalent; Cartesian dualism / Humean empiricism / Kant's categorical imperative. References to "Husserl's phenomenology" → INLINE-DEFINE.

#### `trained`

Reader: formal study or sustained professional engagement. Undergraduate-major or graduate-level coursework in the domain, OR sustained professional engagement (an imam who studied in seminary; a Bible-college graduate; a working physicist; a lawyer in the relevant subfield). Navigates the domain's conceptual schema with comfort.

Expertise-depth tier: recognizes specialist terms reliably. Has a well-integrated conceptual schema; places specific positions within school-internal taxonomies. Catches major school-internal debates and can navigate them. Has read substantial secondary literature and meaningful primary-source material.

Discourse-register tier: introductory-academic + intermediate-academic + meaningful primary-source (Brill encyclopedia article; scholarly translation with footnotes; the *Risale-i Nur* in English translation with annotations).

Domain-handling: USE-TECHNICAL-VOCABULARY-FREELY for most terms; INLINE-DEFINE-ON-FIRST-USE only for truly specialist sub-field terms. ATTRIBUTE-VIEW-TO-SCHOOL as primary mode; INVOKE-SPECIALIST-DEBATES at the edge when source's argument requires it.

Examples:
- *Islamic theology*: knows the 4 Sunni jurisprudential schools by name (Hanafi / Maliki / Shafi'i / Hanbali); knows kalam vs falsafa distinction; recognizes al-Ghazali / Ibn Sina / Ibn Taymiyyah; knows tafsīr as a genre with named major works. References to "isnād criticism" → USE-FREELY but ATTRIBUTE-VIEW-TO-SCHOOL when debates appear.
- *Biblical scholarship*: knows source criticism basics (Documentary Hypothesis / Q source); recognizes major commentators; knows what midrash is; understands canon-formation history. References to "redaction criticism" → USE-FREELY; ATTRIBUTE-VIEW-TO-SCHOOL ("the Tübingen position holds...").
- *Theoretical physics*: graduate-level physics; recognizes Maxwell's equations in any form; navigates Lagrangian vs Hamiltonian mechanics; recognizes Feynman diagrams. References to "Copenhagen interpretation vs Many-worlds" → ATTRIBUTE-VIEW-TO-SCHOOL.
- *Legal scholarship*: law-school graduate; case-law analysis; recognizes specific doctrines (constitutional avoidance; dormant commerce clause; ratione decidendi). References to "the originalism debate" → ATTRIBUTE-VIEW-TO-SCHOOL.
- *Philosophy*: graduate-level; navigates analytic-vs-continental divide; recognizes logical positivism / phenomenology / ordinary-language philosophy. References to "Quine's critique of the analytic-synthetic distinction" → USE-FREELY.

#### `expert`

Reader: specialist scholar. At minimum graduate-level training, often a doctorate, often years of working scholarship in the subfield. Navigates internal debates at scholar-canonical depth; engages with primary-source material directly.

Expertise-depth tier: recognizes all specialist terms including subfield-internal terminology. Has a fully-integrated conceptual schema covering both mainstream and contested terrain. Engages with school-internal debates as primary discourse, including the lineage of arguments and contemporary positions. Reads primary sources directly in original language when relevant (the Quran in Arabic; the Hebrew Bible in Hebrew; Plato in Greek).

Discourse-register tier: handles all academic registers including scholar-canonical (specialized monographs; critical editions; subfield-internal journal articles).

Domain-handling: USE-TECHNICAL-VOCABULARY-FREELY across the board; KEEP-SOURCE-TERM-WITH-GLOSS or KEEP-AS-IS for source-language terms whose form is the point. INVOKE-SPECIALIST-DEBATES as primary mode; ATTRIBUTE-VIEW-TO-SCHOOL when nuance about positions matters.

Examples:
- *Islamic theology*: navigates Mu'tazila vs Ash'ari debate on divine attributes; recognizes Said Nursi's Risale-i Nur terminology and the wider Naqshbandi-Khalidi Sufi context; knows lineage of arguments in classical kalam. References to specific positions in al-Maturidi's *Kitab al-Tawhid* → USE-FREELY; INVOKE-SPECIALIST-DEBATES.
- *Biblical scholarship*: navigates JEDP source-criticism debates; recognizes critical apparatus conventions (Nestle-Aland); knows manuscript family distinctions; engages with redaction criticism. References to "the Yahwist source's date" → INVOKE-SPECIALIST-DEBATES.
- *Theoretical physics*: navigates loop-quantum-gravity vs string-theory debates; recognizes specific researchers' positions on the measurement problem; engages with subfield literature. References to "AdS/CFT correspondence" → USE-FREELY.
- *Legal scholarship*: subfield specialist; recognizes judges' jurisprudential leanings; navigates academic debates. References to "Hart's rule of recognition" → USE-FREELY.
- *Philosophy*: subfield specialist (phil-of-mind: functionalism vs eliminativism; meta-ethics: cognitivism vs non-cognitivism); recognizes specific philosophers' positions. References to "the Frankfurt cases" → USE-FREELY.

**Adjacent-level boundaries (domain_expertise):**

- *lay → aware*: `aware` catches the MAJOR cultural-anchor concepts of the domain through general life exposure; `lay` does not reliably catch even these. `aware` handles a Karen-Armstrong-level introduction; `lay` struggles with it. Translator-AI can use one-shot INLINE-DEFINE for popular-book-level terms at `aware`; at `lay` even those need PARAPHRASE.
- *aware → educated*: `educated` has READ general literature on the domain (not just heard of it through general life). Has an integrated conceptual schema for mainstream concepts (where `aware` holds them as isolated facts). Can handle USE-TECHNICAL-VOCABULARY-FREELY for mainstream terms; `aware` cannot. Begins to recognize school-internal debates exist (without navigating them); `aware` does not.
- *educated → trained*: `trained` has FORMAL STUDY or sustained professional engagement; `educated` has general-amateur reading only. Navigates school-internal debates; `educated` recognizes they exist but doesn't navigate. Handles most specialist terms without unpacking; `educated` needs first-use definitions for specialist terms. Primary discourse mode shifts from UNATTRIBUTED-CONSENSUS at `educated` to ATTRIBUTE-VIEW-TO-SCHOOL at `trained`.
- *trained → expert*: `expert` engages with subfield-internal debates at scholar-canonical depth; `trained` navigates mainstream school debates but not subfield-internal ones. `expert` reads primary sources directly in original language when relevant; `trained` reads major primary sources in translation. Primary discourse mode shifts from ATTRIBUTE-VIEW-TO-SCHOOL at `trained` to INVOKE-SPECIALIST-DEBATES at `expert`. Vocabulary handling drops most unpacking entirely.

---

## A3 — source_culture

**Concept.** The reader's **identity-based** proximity to the source's cultural milieu — distinct from A1.e's competence-based cultural-reference-recognition. **Four-corners independence is real:**

|  | A1.e / A2 high (well-read) | A1.e / A2 low (uninitiated) |
|---|---|---|
| **A3 source-native** | Born Muslim Islamic-studies professor | Born Muslim with no formal study |
| **A3 outsider** | Western academic Islamicist | Typical Western secular reader |

**Plain ordinal. Single value applies to source TEXT's primary culture.**

**Levels:** `outsider | acquainted | familiar | heritage | source-native`

Anchored in diaspora studies (Avtar Brah) + religious-insider sociology (Lewis Rambo on conversion trajectories; Sherman Jackson on Blackamerican Islam / heritage identity).

**Composite-with-primary-axis identity dimension.** Lived cultural-fluency aggregates:
- **Residential markers** — where reader lives / has lived; for how long.
- **Linguistic markers** — native vs learned source language; current fluency.
- **Practice markers** — actively practices source-culture customs (religious observance for religious-text sources; cultural traditions for secular sources).
- **Religious/ideological markers** — religious identity for religious-text sources; ideological identity for political-canon sources.
- **Heritage markers** — descended from source culture; family network in source culture.

Context-dependent weighting:
- *Religious-text sources* (Said Nursi corpus; Bible; Quran): religious identity weights more. A born Catholic reading the Bible has higher A3 proximity than a non-religious Westerner with the same residential profile.
- *Secular sources* (Greek classical; Chinese Confucian; modern Russian literature): residential and linguistic markers weight more. A scholar-resident of Greece has higher A3 proximity to Greek classical than a non-resident scholar with the same domain expertise.
- *Layered sources* (Said Nursi has Muslim + Turkish + Naqshbandi-Khalidi-Sufi nested): the primary layer is the most-specific. The AI handles within-layer references at runtime.

**Layered-source-culture handling.** A3 captures proximity to the PRIMARY (most-specific) cultural layer. For Said Nursi the primary is Naqshbandi-Khalidi-Sufi-Islamic-Turkish (innermost). The translator-AI handles within-layer variation at runtime — a `source-native` reader (inner-layer proximity) catches inner-layer references silently; a `familiar` reader (outer-Muslim-layer proximity but not inner) needs brief FLAG-CULTURAL-CONTEXT for inner-layer references like specific Naqshbandi-Khalidi-Sufi terminology.

**Self-identification = configuration trust mechanism.** A3 is identity-based; the user self-reports the A3 value. The AI takes it at face value. The configuration is the user's responsibility; the AI cannot reliably infer reader cultural identity from text-side signals (unlike A2 where some signals may exist).

**10 handling actions in 4 categories (preference order; DOMESTICATE-CULTURAL-FRAME + ANGLICIZE-HONORIFICS DISFAVORED per project policy):**

*Proper-noun handling (3):*
- **TRANSLITERATE-FULLY** — "Allah", "Üstad", "Bediuzzaman" verbatim. At `familiar`/`heritage`/`source-native`.
- **TRANSLITERATE-WITH-GLOSS** — "Allah (God)" first use. At `acquainted`/early-`familiar`.
- **TARGET-LANGUAGE-EQUIVALENT** — "Jesus" instead of "Yeshua"; "God" not "Allah". At `outsider` last-resort; DISFAVORED per project policy.

*Cultural-context handling (3):*
- **ASSUME-SHARED-CULTURAL-KNOWLEDGE** — at `heritage`/`source-native`.
- **FLAG-CULTURAL-CONTEXT** — brief framing of source-cultural assumptions. At `acquainted`/`familiar`/`heritage` for inner-layer.
- **BRIDGE-CULTURAL-DISTANCE** — extensive explanation of source-culture worldview. At `outsider`.

*Honorific handling (2):*
- **KEEP-HONORIFICS-SOURCE** — "Hazret-i Üstad", "Imam-i Azam", "Sahabe". Preferred across levels.
- **ANGLICIZE-HONORIFICS** — "Master So-and-so", "the Imam", "the Companions". DISFAVORED per project policy.

*Strategic stance (2):*
- **PRESERVE-CULTURAL-SPECIFICITY** — preferred across levels.
- **DOMESTICATE-CULTURAL-FRAME** — substitute target-cultural framework. DISFAVORED.

Preference order: `PRESERVE-CULTURAL-SPECIFICITY > KEEP-HONORIFICS-SOURCE > TRANSLITERATE-WITH-GLOSS > FLAG-CULTURAL-CONTEXT > BRIDGE-CULTURAL-DISTANCE > [TARGET-LANGUAGE-EQUIVALENT / DOMESTICATE-CULTURAL-FRAME / ANGLICIZE-HONORIFICS] (last resorts)`.

**Conservative-bias = LOWER default (assumes OUTSIDER).** Safer ethically — avoids assuming-shared-knowledge that's not there; errs toward over-glossing rather than under-glossing.

#### `outsider`

Reader: no cultural ties to the source culture. Identity firmly anchored in target culture. Has not lived in source culture; doesn't speak source language natively; doesn't practice source-culture customs; no familial or religious heritage from source culture.

Cultural-proximity tier: no identity-based proximity; treats source culture as fully foreign. May have some cultural-general competence (A1.e territory) but does not have lived cultural-fluency.

Cultural-context tier: handles only target-cultural register; needs explicit framing for source-cultural assumptions. Religious-sermon register, cultural-celebration register, source-language-native register all beyond reliable comprehension.

Cultural-handling: TRANSLITERATE-WITH-GLOSS for source-language proper names; AVOID TARGET-LANGUAGE-EQUIVALENT (per project policy). BRIDGE-CULTURAL-DISTANCE for source-cultural assumptions. KEEP-HONORIFICS-SOURCE with first-use gloss. PRESERVE-CULTURAL-SPECIFICITY (foreignization-preserving over DOMESTICATE-CULTURAL-FRAME).

Examples spread across source cultures:
- *Turkish-Ottoman-Naqshbandi-Khalidi-Islamic (Said Nursi)*: typical Western non-Muslim. Doesn't know "Hazret-i Üstad" carries an honorific weight; doesn't know "Bediuzzaman" means "wonder of the age"; doesn't recognize Naqshbandi-Khalidi-Sufi tradition. AI: TRANSLITERATE-WITH-GLOSS "Üstad (Master)"; FLAG-CULTURAL-CONTEXT for Sufi-spiritual-practice references; BRIDGE-CULTURAL-DISTANCE for Islamic-theological assumptions.
- *Hebrew biblical*: secular Western non-Jewish reader. Recognizes "Moses" and "David" via cultural exposure but doesn't know Second Temple Judaism's covenant theology or Hellenistic Jewish cultural specifics. AI: BRIDGE-CULTURAL-DISTANCE for covenant theology assumptions.
- *Quranic*: Western non-Muslim reader. Doesn't know "Bismillah" carries opening-prayer weight; doesn't recognize "Sırat" as the bridge over hellfire. AI: TRANSLITERATE-WITH-GLOSS; BRIDGE-CULTURAL-DISTANCE.
- *Hindu Sanskrit*: Western reader with no Hindu background. Doesn't know "Rama" vs "Krishna" cultural significance; doesn't recognize "Atman" beyond a vague "soul" gloss. AI: TRANSLITERATE-WITH-GLOSS; FLAG-CULTURAL-CONTEXT.
- *Chinese Confucian*: Western reader. Doesn't recognize "junzi" as the exemplary-person concept; doesn't know "li" carries ritual-propriety weight. AI: PARAPHRASE or TRANSLITERATE-WITH-GLOSS.

#### `acquainted`

Reader: some exposure to the source culture but no immersion; identity-shift without sustained immersion. May be a cultural-tourist (visited the source country briefly); a convert without residence; a non-conversational student of the source language; a general-knowledge enthusiast.

Cultural-proximity tier: cultural-tourist exposure. Catches major cultural anchors when explicitly framed; misses deeper cultural assumptions.

Cultural-context tier: handles popular-introduction register; major-cultural-anchor references with brief framing. Specialist-cultural register and source-language-native register beyond reliable comprehension.

Cultural-handling: TRANSLITERATE-WITH-GLOSS first use, then bare transliteration. FLAG-CULTURAL-CONTEXT briefly for cultural assumptions. KEEP-HONORIFICS-SOURCE with first-use gloss. PRESERVE-CULTURAL-SPECIFICITY.

Examples:
- *Said Nursi corpus*: Western reader with general "world religions" exposure or a recent convert without residence. Recognizes "Allah" as standard Arabic for God; knows what "5 pillars" are; doesn't reliably know "Naqshbandi-Khalidi". AI: TRANSLITERATE-WITH-GLOSS "Hazret-i Üstad (the venerated Master)"; FLAG-CULTURAL-CONTEXT for Naqshbandi-Khalidi-specific references.
- *Hebrew biblical*: Westerner who took a religion-survey course. Recognizes major figures (Moses, David, Paul) and basic narratives (Eden, Exodus). AI: FLAG-CULTURAL-CONTEXT for Documentary Hypothesis-style scholarly assumptions; TRANSLITERATE-WITH-GLOSS for less-common Hebrew terms.
- *Quranic*: Westerner with general Islam-aware background. Recognizes Bismillah, Surah, basic prayers. AI: TRANSLITERATE-WITH-GLOSS for Quranic-specific terms; FLAG-CULTURAL-CONTEXT for Islamic-theological frames.
- *Hindu Sanskrit*: Westerner with yoga-/meditation-cultural exposure. Recognizes "karma," "dharma" loosely. AI: FLAG-CULTURAL-CONTEXT for deeper Vedic concepts.
- *Greek classical (secular)*: Westerner with general classical-history exposure. Recognizes major figures (Socrates, Caesar) and major events (Battle of Marathon). AI: FLAG-CULTURAL-CONTEXT for less-major historical references.

Boundary distinguishing from `outsider`: the `acquainted` reader has SOME EXPOSURE (cultural-tourist, religion-survey course, popular-book reading) — they catch major cultural anchors when explicitly framed. The `outsider` reader has NONE — they need everything bridged. The translator-AI can use brief FLAG-CULTURAL-CONTEXT at `acquainted` where it would need BRIDGE-CULTURAL-DISTANCE at `outsider`.

#### `familiar`

Reader: sustained immersion in the source culture without inherited identity. May be a Western convert who has lived in a Muslim community for years; a long-resident Westerner in a Muslim-majority country (10+ years); a 30-year scholar-resident (Western Islamicist in Cairo); a non-converting spouse with 20+ years residence; a converted-Catholic-priest with decades of Hebrew biblical study and residence in Jerusalem.

Cultural-proximity tier: lived cultural-fluency without inherited identity. Catches most cultural references silently; understands cultural assumptions through immersion; recognizes source-language honorifics in their proper register. Doesn't have the inherited identity of a heritage or source-native reader.

Cultural-context tier: handles general-cultural register + major-religious-text register + popular-cultural-celebration register. Approaches scholar-canonical register and source-language-native subtle register at the edges.

Cultural-handling: TRANSLITERATE-FULLY for major source-language terms (the reader recognizes "Allah", "Üstad", "isnād" without gloss); TRANSLITERATE-WITH-GLOSS only for less-central references. ASSUME-SHARED-CULTURAL-KNOWLEDGE for major cultural anchors; FLAG-CULTURAL-CONTEXT for inner-layer references at layered sources. KEEP-HONORIFICS-SOURCE without gloss for major honorifics. PRESERVE-CULTURAL-SPECIFICITY.

Examples:
- *Said Nursi corpus*: a Western convert who has lived in a Naqshbandi-Khalidi community for 15 years. Knows "Hazret-i Üstad" carries honorific weight; recognizes major Sufi figures (Mevlana, Abdulkadir-i Geylani). AI: TRANSLITERATE-FULLY for established terms; FLAG-CULTURAL-CONTEXT only for the most specialist Naqshbandi-Khalidi-internal references.
- *Hebrew biblical*: a long-term Christian-clergy reader with biblical-Hebrew study and Jerusalem residence. AI: TRANSLITERATE-FULLY for Hebrew terms in established transliteration; KEEP-HONORIFICS-SOURCE.
- *Quranic*: a 20-year scholar-resident in a Muslim country. AI: TRANSLITERATE-FULLY for major Quranic terms; ASSUME-SHARED-CULTURAL-KNOWLEDGE for major Islamic-theological frames.
- *Hindu Sanskrit*: a Westerner who has been a Hindu practitioner for 25 years and lived in India for 10. AI: TRANSLITERATE-FULLY for major Sanskrit terms; KEEP-HONORIFICS-SOURCE.
- *Greek classical*: a classics professor who has spent sabbaticals in Greece. AI: TRANSLITERATE-FULLY for Greek terms in established transliteration; ASSUME-SHARED-CULTURAL-KNOWLEDGE for major cultural assumptions.

Boundary distinguishing from `acquainted`: the `familiar` reader has SUSTAINED IMMERSION (years of residence, decades of practice, or both). Has lived cultural-fluency: catches most cultural references silently; understands cultural assumptions through having lived them; doesn't need brief FLAG-CULTURAL-CONTEXT for major cultural anchors. The translator-AI can ASSUME-SHARED-CULTURAL-KNOWLEDGE at `familiar` where it would need FLAG-CULTURAL-CONTEXT at `acquainted`.

#### `heritage`

Reader: identity inherited but diluted. Typically: 2nd-generation or later diaspora; raised in a mixed household (one parent from source culture); heritage but not actively practicing; born of source-culture family but raised outside the source country. Has bicultural identity with target-primary; carries source-cultural traces and cultural-anchor knowledge but with some dilution.

Cultural-proximity tier: inherited cultural-fluency, partially diluted. Catches major cultural anchors via inheritance; may miss some specialist or inner-layer cultural assumptions. Has the inherited identity that distinguishes from `familiar` but lacks the full immersion of `source-native`.

Cultural-context tier: handles general-cultural + major-religious-text + popular-cultural-celebration register through inheritance. May have gaps at scholar-canonical or inner-layer register.

Cultural-handling: TRANSLITERATE-FULLY for major heritage-known terms; TRANSLITERATE-WITH-GLOSS for less-central or inner-layer references. ASSUME-SHARED-CULTURAL-KNOWLEDGE for major cultural anchors; FLAG-CULTURAL-CONTEXT for inner-layer or specialist references. KEEP-HONORIFICS-SOURCE. PRESERVE-CULTURAL-SPECIFICITY.

Examples:
- *Said Nursi corpus*: a 2nd-generation Turkish-American whose parents emigrated from a Turkish-Muslim community but who was raised in the U.S. without active Naqshbandi-Khalidi practice. Knows "Allah", "Quran", basic Islamic vocabulary through inheritance; may not reliably catch Naqshbandi-Khalidi-specific terminology. AI: TRANSLITERATE-FULLY for general Islamic terms; FLAG-CULTURAL-CONTEXT for Naqshbandi-Khalidi-specific.
- *Hebrew biblical*: a 3rd-generation Jewish-American without active religious observance but cultural-Jewish identity. AI: ASSUME-SHARED-CULTURAL-KNOWLEDGE for major Jewish-cultural anchors; FLAG-CULTURAL-CONTEXT for specialist scholarship.
- *Quranic*: a 2nd-generation Muslim-American without active mosque attendance but cultural-Muslim identity. AI: ASSUME-SHARED-CULTURAL-KNOWLEDGE for major Quranic-cultural anchors; FLAG-CULTURAL-CONTEXT for specialist theology.
- *Hindu Sanskrit*: a 3rd-generation Indian-American without active religious observance but cultural-Hindu identity. AI: ASSUME-SHARED-CULTURAL-KNOWLEDGE for major figures (Rama, Krishna); FLAG-CULTURAL-CONTEXT for Vedic specialist terms.
- *Chinese Confucian*: a 2nd-generation Chinese-American whose family has Confucian cultural background but who was raised mostly in U.S. cultural context. AI: ASSUME-SHARED-CULTURAL-KNOWLEDGE for major figures; FLAG-CULTURAL-CONTEXT for specialist Confucian-cultural references.

Boundary distinguishing from `familiar`: the `heritage` reader has INHERITED identity (raised by source-culture family; descended from source culture; bicultural identity carried from childhood). The `familiar` reader has ACQUIRED proximity (convert; long-resident; scholar-immersed) without inherited identity. Heritage gives cultural-anchor knowledge through upbringing (even if practice has lapsed); familiar gives lived cultural-fluency through immersion. Both can ASSUME-SHARED-CULTURAL-KNOWLEDGE for major anchors; the heritage reader has more reliable major-anchor inheritance; the familiar reader has more current-practice immersion. The distinction matters for inner-layer references — heritage reader has inherited general but not specialized; familiar reader has immersion-acquired which may include specialist.

#### `source-native`

Reader: born and raised in the source culture; primary identity source. Includes 1st-generation immigrants who emigrated as adults (primary identity still source despite current residence elsewhere). For religious-text sources, includes born-and-raised practitioners with active practice.

Cultural-proximity tier: full lived cultural-fluency with source-primary identity. Catches all cultural references silently; understands all cultural assumptions through having lived them since birth; recognizes source-language honorifics in their full register.

Cultural-context tier: handles all source-cultural registers including specialist-cultural register, inner-layer register, source-language-native subtle register.

Cultural-handling: TRANSLITERATE-FULLY across the board; the reader recognizes source-language forms in original script or transliteration. ASSUME-SHARED-CULTURAL-KNOWLEDGE for everything. KEEP-HONORIFICS-SOURCE. PRESERVE-CULTURAL-SPECIFICITY at maximum (the reader doesn't need foreignization-preserving alternatives — they ARE the cultural context).

Examples:
- *Said Nursi corpus*: a born-and-raised Turkish-Muslim from a Naqshbandi-Khalidi-leaning community in Turkey. AI: TRANSLITERATE-FULLY for everything; ASSUME-SHARED-CULTURAL-KNOWLEDGE for all cultural assumptions including Naqshbandi-Khalidi-specific tradition.
- *Hebrew biblical*: a born-and-raised observant Jew from an Orthodox community with strong biblical-Hebrew literacy. AI: TRANSLITERATE-FULLY; ASSUME-SHARED-CULTURAL-KNOWLEDGE.
- *Quranic*: a born-and-raised Muslim from a country with strong Quranic-recitation tradition (Egypt, Morocco, Indonesia). AI: TRANSLITERATE-FULLY; ASSUME-SHARED-CULTURAL-KNOWLEDGE for full Quranic-cultural context.
- *Hindu Sanskrit*: a born-and-raised Hindu from India with active practice. AI: TRANSLITERATE-FULLY; ASSUME-SHARED-CULTURAL-KNOWLEDGE.
- *Chinese Confucian*: a born-and-raised Chinese reader from a Confucian-tradition-respecting family with classical-Chinese literacy. AI: TRANSLITERATE-FULLY; ASSUME-SHARED-CULTURAL-KNOWLEDGE.

Boundary distinguishing from `heritage`: the `source-native` reader has BORN-AND-RAISED primary identity. The `heritage` reader has INHERITED but DILUTED identity (raised in mixed household; lost language; lapsed practice). The source-native catches inner-layer references silently; the heritage reader may need brief FLAG-CONTEXT for inner-layer specialist references. The source-native ASSUMES all source-cultural context; the heritage reader has the general-anchor inheritance but may need light support for specialized assumptions.

**Edge-case mapping (diaspora gradient / convert / long-resident):**

| Reader type | A3 level | Reasoning |
|---|---|---|
| Adult convert + decades residence | `familiar` | Strong commitment + immersion but no birth/heritage marker |
| Spouse + 20+ years residence + no conversion | `familiar` | Community immersion without identity-shift |
| Long-term scholar-resident (30 years) | `familiar` | Scholar immersion; lacks practice/devotional identity |
| Recent convert without residence | `acquainted` | Identity-shift without immersion |
| Returnee from diaspora | `heritage` or `source-native` per lived years | Conservative-bias places returnee at `heritage` unless substantial lived years in source culture |
| 1.5-generation (came as children) | `heritage` | Bicultural with target-primary; conservative-bias |
| 2nd-generation diaspora | `heritage` | Inherited but diluted; bicultural target-primary |
| 3rd-generation+ | `heritage` (diluted further) | Heritage marker still present but diluted; may approach `acquainted` if heritage is very distant |
| 1st-generation immigrant (emigrated as adult) | `source-native` | Primary identity still source; immigration didn't shift cultural identity |
| Heritage-but-no-practice reader | `heritage` | Inherited identity even without active practice |

**Said Nursi audience spectrum mapping (project's primary corpus):**

- Western secular reader → `outsider` (default)
- Western reader with general "world religions" exposure → `acquainted`
- Western convert without residence → `acquainted`
- Western convert + 15-year residence in Muslim community → `familiar`
- 30-year scholar-resident in Turkey → `familiar`
- 2nd-generation Turkish-American without active Naqshbandi-Khalidi practice → `heritage`
- 1.5-generation Turkish reader who emigrated as child → `heritage` (conservative-bias)
- 1st-generation Turkish immigrant → `source-native`
- Born-and-raised Turkish-Muslim from Naqshbandi-Khalidi-leaning community → `source-native`


---

## A4 — purpose

**Concept.** What the translation is FOR — the use-case. **Categorical** (qualitatively distinct uses; not points on an intensity scale).

Three independent tests confirm categorical:
- *Semantic*: the user-question "what is this translation FOR?" asks a category, not a degree.
- *Lexical*: "more scholarly than devotional" doesn't make sense.
- *Orthogonality*: a scholar might want a CASUAL-feel translation for an easy read; a casual reader might want DEEP analysis to understand a stuck passage. Purposes don't lie on one scale.

**Default-when-A4-silent = `casual`.** Categorical equivalent of conservative-bias-LOWER: lowest assumption about reader effort; broadest reader spectrum; the casual-purpose defaults for other axes produce the safest fallback.

#### `scholarly`

**Use-case profile.** The reader STUDIES the translation — analyzes structure, traces arguments, cites passages, compares versions, prepares academic work. The translation serves research and analysis. The reader engages the text with notes, marginalia, cross-references.

**Strategic implications.** Source-fidelity is paramount; preserve as much source structure as possible (rhythm, parallelism, word order, multi-meaning, source-language honorifics). Footnoting is expected. Cultural specificity is preserved. Analysis depth defaults to `deep`/`scholarly`.

**Per-axis default mappings:** A1 advanced; A2 educated; A3 any (often outsider-with-study); A5 foreignized; A6 standard; A7 rich; A8 deep.

**Said Nursi anchor.** A scholar researching Said Nursi's place in Naqshbandi-Khalidi Sufi theology; a graduate student writing on Nursi's epistemology.

**Cross-cultural illustration.** A graduate student writing on the Documentary Hypothesis (Hebrew biblical scholarly); an academic studying Husserl's phenomenology (philosophy scholarly); a Norton Critical Edition of Plato.

#### `devotional`

**Use-case profile.** The reader READS for spiritual practice — meditates on passages, memorizes, recites, reflects. The translation serves religious / spiritual formation. The reader returns to favorite passages; daily reading habit; communal study (dersane for Nursi).

**Strategic implications.** Liturgical form is sacred — preserve source rhythm, honorifics, transliteration. Avoid distractions (over-glossing, heavy footnoting at-text). The reader is engaging spiritually, not analytically. Cultural specificity is preserved maximally.

**Per-axis default mappings:** A1 conversational; A2 aware-to-educated; A3 source-native / heritage; A5 foreignized-max; A6 standard; A7 standard; A8 standard.

**Said Nursi anchor.** A Risale-i Nur reader doing daily spiritual reading; a dersane study circle.

**Cross-cultural illustration.** A daily prayer reading from the Quran in translation; a Christian using the Bible for lectio divina; a Hindu reading the Gita for meditation.

#### `casual`

**Use-case profile.** The reader READS for general comprehension — curiosity, light reading, getting the gist. The translation serves general literary engagement. The reader doesn't return to passages obsessively; reads once or twice; isn't preparing analysis or spiritual practice.

**Strategic implications.** Balance source-fidelity with accessibility. Help the reader where they need it (rich scaffolding); don't overwhelm with footnotes. Cultural references get foreignization-preserving glosses (FLAG-CULTURAL-CONTEXT + TRANSLITERATE-WITH-GLOSS) rather than DOMESTICATE. Analysis depth is surface.

**Per-axis default mappings:** A1 daily; A2 lay-to-aware; A3 outsider-to-acquainted; A5 balanced; A6 light; A7 rich; A8 surface.

**Said Nursi anchor.** A general curious reader exploring Risale-i Nur; a non-Muslim with interest in Islamic theology; a convert reading for general orientation.

**Cross-cultural illustration.** A Penguin Classics reader of Plato; a general reader of a literary novel in translation; a curious reader of an introductory Quran translation.

#### `language-learning`

**Use-case profile.** The reader LEARNS the source language through the translation — reads to acquire vocabulary, syntax, idiomatic patterns. The translation serves pedagogical clarity. The reader may have an interlinear or parallel-text version; consults the source alongside; back-translates; notes syntactic patterns.

**Strategic implications.** Maximum transparency to source structure. Preserve source word-order, parallelism, structural patterns even at cost of target-language naturalness. Rich scaffolding (vocabulary glosses, grammatical notes, parallel-source alignment). Source-fidelity for pedagogical value.

**Per-axis default mappings:** A1 conversational (matched to learner); A2 lay; A3 outsider; A5 foreignized; A6 standard; A7 scholarly; A8 scholarly.

**Said Nursi anchor.** A Turkish learner using Nursi as reading material; an advanced student of Ottoman Turkish; an Arabic-students reading Nursi's Quran-citations.

**Cross-cultural illustration.** A Latin student reading Cicero with parallel text; a Greek student reading Plato with vocabulary glosses; a Sanskrit student reading the Gita with grammar notes.

#### `performance`

**Use-case profile.** The reader DELIVERS the translation orally — recitation, reading aloud, theatrical performance, sermon delivery. The translation serves oral / aural reception. The reader's audience receives the text through hearing.

**Strategic implications.** Maximum cadence preservation. Form is meaning per the project's harmony_layer commitment (Tier 1-4 system). Rhythm, parallelism, and other structural elements that create oral effect are preserved. Footnotes are off — they break delivery. Clean text for oral flow.

**Per-axis default mappings:** A1 conversational; A2 any; A3 any; A5 balanced; A6 maximum; A7 minimal; A8 surface (or `none` for pure oral).

**Said Nursi anchor.** Nursi recitation passages (some are designed for oral delivery); a sermon-translation drawing on Nursi.

**Cross-cultural illustration.** Quran recitation in translation (some translations are designed for recitation); a Greek tragedy in staged English; an opera surtitle translation; a poetry slam translation.

---

## A5 — source_fidelity

**Concept.** Translator's strategic stance on the foreignization↔domestication spectrum (Lawrence Venuti's framework). Controls **lexical / idiomatic surface** choices. **Distinct from A6 Form Preservation** (which controls structural form — rhythm, parallelism, word-order as meaning).

**Asymmetric 4-level range. No `heavily-domesticated`** — the DOMESTICATE-disfavored cross-cutting policy is embedded structurally (the absence of `heavily-domesticated` makes the policy load-bearing).

**Levels:** `foreignized-max | foreignized | balanced | lightly-domesticated`

**A5 has NO own implementation actions.** A5 is a STRATEGIC STANCE that MODULATES which A1 cultural-reference-recognition handling actions and A3 source-culture handling actions fire per encountered translation choice. A5's level determines the PREFERENCE ORDER over A1's 5 actions and A3's 10 actions.

**Default-when-A5-silent CHAINS THROUGH A4 matrix.** When A4 is set, A4 supplies A5 default per purpose. When A4 is silent → A4 defaults to `casual` → casual's A5 = `balanced`. Final A5 default = `balanced`.

#### `foreignized-max`

**Strategic stance.** Maximum source-fidelity. Preserve everything source-cultural: transliterations, honorifics, cultural references, source-language phrases. The reader encounters the source culture in its specificity. Domestication is structurally absent at this level.

**Per-stance handling-action bias.** A1: KEEP-AS-IS prioritized for transparent references; EXPLICATE-FUNCTION for opaque-but-load-bearing; FOOTNOTE for context. INLINE-GLOSS minimal; DOMESTICATE never. A3: TRANSLITERATE-FULLY; KEEP-HONORIFICS-SOURCE; PRESERVE-CULTURAL-SPECIFICITY at maximum; ASSUME-SHARED-CULTURAL-KNOWLEDGE when reader is source-native. TARGET-LANGUAGE-EQUIVALENT / DOMESTICATE-CULTURAL-FRAME / ANGLICIZE-HONORIFICS strictly avoided.

**Cross-axis interaction.** A4 default match: `devotional`. A6 orthogonality: typically pairs with high A6 (preserve nazm + structural form) but doesn't require it — a `foreignized-max` lexical stance can coexist with low A6 form preservation (rare but possible — preserve foreign vocabulary while flattening rhythm).

**Said Nursi anchor.** Risale-i Nur devotional reading for source-culture-fluent reader (A3=source-native). All Sufi honorifics + theological terms preserved; Sufi practice references untranslated; reader brings the cultural fluency.

**Cross-cultural example.** Quran recitation translation; SBL Greek NT scholar-edition; Tanakh Jewish Publication Society edition.

#### `foreignized`

**Strategic stance.** Strong source-fidelity. Preserve source-cultural specificity but provide light support (inline glosses, brief footnotes) where reader needs it. The reader does encounter the source culture but with translator help at the edges.

**Per-stance handling-action bias.** A1: INLINE-GLOSS for moderate-difficulty references; EXPLICATE-FUNCTION for opaque-with-explanation-needed; KEEP-AS-IS where reader can catch it. FOOTNOTE for scholarly context. DOMESTICATE explicitly avoided. A3: TRANSLITERATE-FULLY for established terms; TRANSLITERATE-WITH-GLOSS for less-established; KEEP-HONORIFICS-SOURCE; PRESERVE-CULTURAL-SPECIFICITY; FLAG-CULTURAL-CONTEXT briefly where reader benefits.

**Cross-axis interaction.** A4 default match: `scholarly` and `language-learning`. A6 orthogonality: typically pairs with high A6 for scholarly use but independent.

**Said Nursi anchor.** Academic Islamic-studies edition of Risale-i Nur with footnotes. Nursi-specific terminology kept; Sufi context briefly explained where reader benefits.

**Cross-cultural example.** Norton Critical Edition of Plato; NRSV biblical edition; M.A.S. Abdel Haleem Quran translation with light apparatus.

#### `balanced`

**Strategic stance.** Balance source-fidelity with accessibility. Where source-cultural specificity is load-bearing, preserve with explication. Where not, accept brief foreignization-preserving alternatives (INLINE-GLOSS / EXPLICATE-FUNCTION) for reader comfort. The reader engages source culture in approachable form.

**Per-stance handling-action bias.** A1: INLINE-GLOSS as primary mode; EXPLICATE-FUNCTION for compressed-meaning references; FOOTNOTE selectively for added context. KEEP-AS-IS for transparent + culturally-ubiquitous references. DOMESTICATE still avoided (foreignization-preserving alternatives preferred). A3: TRANSLITERATE-WITH-GLOSS as primary; FLAG-CULTURAL-CONTEXT where reader needs framing; KEEP-HONORIFICS-SOURCE for established source honorifics; BRIDGE-CULTURAL-DISTANCE for broader cultural assumptions.

**Cross-axis interaction.** A4 default match: `casual` and `performance`. A6 orthogonality: typically pairs with moderate A6 form but independent — performance pairs `balanced` A5 with MAXIMUM A6 (cadence preservation).

**Said Nursi anchor.** Penguin-Classics-style edition for general curious reader. Nursi terms glossed in-line on first use; Sufi assumptions briefly framed; reader can follow.

**Cross-cultural example.** Penguin Classics edition of Plato; NIV biblical edition; Penguin Quran (e.g., Tarif Khalidi translation).

#### `lightly-domesticated`

**Strategic stance.** Light target-naturalization where source-cultural specificity isn't load-bearing. Source-language honorifics may be selectively anglicized; cultural references may be selectively replaced with target-culture equivalents. The reader engages a more accessible text but with preserved cultural-specificity at load-bearing points.

**Per-stance handling-action bias.** A1: INLINE-GLOSS still preferred for load-bearing references; DOMESTICATE permissible in narrow cases (non-load-bearing cultural references where target-natural reads better and source-otherness doesn't serve the reader). PARAPHRASE-IN-LAYMAN-TERMS becomes more permissible. A3: TARGET-LANGUAGE-EQUIVALENT permissible for proper-noun handling in narrow cases (less common Sufi figures; less-recognized historical figures); ANGLICIZE-HONORIFICS selectively permissible. PRESERVE-CULTURAL-SPECIFICITY still expected for load-bearing points; DOMESTICATE-CULTURAL-FRAME still disfavored but permissible at this level when the cultural frame isn't pedagogically central.

**Cross-axis interaction.** A4 default match: no purpose defaults to `lightly-domesticated` in the matrix (the closest is `casual` defaulting to `balanced`). User would set A5 = `lightly-domesticated` as a per-axis override when more accessibility is wanted than `balanced` provides.

**Said Nursi anchor.** A popular paperback edition of Risale-i Nur for the broadest possible general audience — convert exploring Islam casually; non-Muslim curious reader. Less central Sufi honorifics may be anglicized; cultural assumptions more heavily explicated; load-bearing terms (Allah, Quran, key theological concepts) preserved with light gloss.

**Cross-cultural example.** A trade-paperback edition of a classical text for mass-market reading; popular Penguin "Gateway" series introductory editions.

**A5 → A1 cultural-reference-recognition action modulation table:**

| A5 Level | Preferred Actions (in order) | Avoided |
|---|---|---|
| `foreignized-max` | KEEP-AS-IS → EXPLICATE-FUNCTION → FOOTNOTE | INLINE-GLOSS minimal; DOMESTICATE never |
| `foreignized` | INLINE-GLOSS → EXPLICATE-FUNCTION → KEEP-AS-IS → FOOTNOTE | DOMESTICATE avoided |
| `balanced` | INLINE-GLOSS → EXPLICATE-FUNCTION → FOOTNOTE → KEEP-AS-IS | DOMESTICATE still avoided (project policy) |
| `lightly-domesticated` | INLINE-GLOSS → EXPLICATE-FUNCTION → PARAPHRASE-IN-LAYMAN-TERMS → FOOTNOTE → DOMESTICATE (permissible in narrow cases) | — |

**A5 → A3 source-culture action modulation table:**

| A5 Level | Proper-Noun | Cultural-Context | Honorific | Strategic |
|---|---|---|---|---|
| `foreignized-max` | TRANSLITERATE-FULLY | ASSUME-SHARED-CULTURAL-KNOWLEDGE | KEEP-HONORIFICS-SOURCE | PRESERVE-CULTURAL-SPECIFICITY (max) |
| `foreignized` | TRANSLITERATE-FULLY / WITH-GLOSS | FLAG-CULTURAL-CONTEXT briefly | KEEP-HONORIFICS-SOURCE | PRESERVE-CULTURAL-SPECIFICITY |
| `balanced` | TRANSLITERATE-WITH-GLOSS | FLAG-CULTURAL-CONTEXT / BRIDGE-CULTURAL-DISTANCE | KEEP-HONORIFICS-SOURCE | PRESERVE-CULTURAL-SPECIFICITY |
| `lightly-domesticated` | TRANSLITERATE-WITH-GLOSS / TARGET-LANGUAGE-EQUIVALENT (narrow cases) | BRIDGE-CULTURAL-DISTANCE | KEEP-HONORIFICS-SOURCE / ANGLICIZE-HONORIFICS (selective) | PRESERVE-CULTURAL-SPECIFICITY at load-bearing points; DOMESTICATE-CULTURAL-FRAME selectively permissible |

The pattern across both tables: DOMESTICATE / TARGET-LANGUAGE-EQUIVALENT / ANGLICIZE-HONORIFICS become PERMISSIBLE only at `lightly-domesticated` and even there are selective (not default). The project policy carries through all levels via the absence of `heavily-domesticated` as a level.


---

## A6 — form_preservation

**Concept.** Translator-AI's stance on structural form preservation — rhythm, parallelism, word-order, ring composition, chiasmus, cause-effect chains. **Distinct from A5 source_fidelity** (lexical/idiomatic surface). A6 controls FORM-AS-MEANING per the project's `harmony_layer.md` Tier 1-4 system.

**5 ordinal levels:** `off | minimal | light | standard | maximum`. Plain-ordinal. Maps to `harmony_layer.md`'s 4 natural tier strata + an "off" floor.

**Activation gate at Level 3 `light` for nazm-as-meaning policy.** Below the gate (`off`, `minimal`): partial 3-Pass methodology. At or above the gate (`light`, `standard`, `maximum`): full 3-Pass methodology fires (Meaning Lock → Harmony Map → Target Reconstruction) and the nazm-as-meaning policy is active.

**Tier 3 conditional logic INVARIANT across Levels 4-5.** `harmony_layer.md`'s PRESERVE-WHEN/SACRIFICE-WHEN clauses are the SYSTEM's own adjudication mechanism; they are NOT a user-configurable property. A6 Level 5 doesn't override Tier 3 conditional — it adds Tier 4 ON TOP.

**Tier 4 language-feasibility caveat at Level 5.** Tier 4 entries are language-specific. Level 5 attempts where target language permits; harmony report acknowledges sacrifices when target structurally cannot support feature (e.g., Semitic root echo to non-Semitic target).

**Per-level tier-coverage table:**

| A6 Level | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Nazm Policy |
|---|---|---|---|---|---|
| `off` | — | — | — | — | OFF |
| `minimal` | ✓ | — | — | — | OFF |
| `light` | ✓ | ✓ | — | — | **ACTIVE (activation gate)** |
| `standard` | ✓ | ✓ | ✓ (per PRESERVE-WHEN) | — | ACTIVE |
| `maximum` | ✓ | ✓ | ✓ (per PRESERVE-WHEN) | ✓ (where target permits) | ACTIVE |

**Tier 1 (13 entries — Non-Negotiable; meaning IS carried by harmony):** cause-effect chains; conditional chains; hidden syllogisms; semantic escalation/de-escalation; convergence (havuz); ellipsis patterns; emotional arc; tense consistency; person-voice threading + iltifat; antonym pairing; etc.

**Tier 2 (12 entries — High Priority; strongly supports comprehension):** grammatical parallelism; ring composition; chiastic structure; pronoun chains; clause-length patterning; evidence-claim rhythm; concession-rebuttal; thematic bracketing; etc.

**Tier 3 (13 entries — Context-Dependent):** register consistency; synonym chaining; isotopy; callback/forward-reference; performative continuity; parallel panel structure; merismus; particle threading; etc. — each entry has its own PRESERVE-WHEN / SACRIFICE-WHEN clauses adjudicated at runtime.

**Tier 4 (11 entries — Low Priority, language-specific):** phonetic echo; internal rhyme/assonance; root echo; phonetic weight; maqta' harmony; etc.

**Default-when-A6-silent = `light` via A4 chain.** A4 silent → `casual` → A6 `light`. The project defaults to nazm-policy-ACTIVE. The threshold matters: defaulting to the activation gate reflects the project's commitment to form-as-meaning as baseline.

#### `off`

**Strategic stance.** No harmony work. Translator-AI runs Pass 1 (Meaning Lock) only. Output is semantic-fidelity-only; no structural preservation; no harmony report.

**Tier-coverage.** None.

**Nazm-policy marker.** OFF.

**Cross-axis interaction.** No A4 purpose defaults to `off` — this level requires explicit user override. A5 orthogonal (any value).

**Said Nursi anchor.** Internal AI utility pass; semantic extraction for indexing; rough draft for editorial review.

#### `minimal`

**Strategic stance.** Preserve Tier 1 (Non-Negotiable; meaning-as-harmony) only. The AI preserves cause-effect chains, hidden syllogisms, conditional chains, semantic escalation/de-escalation, convergence (havuz), ellipsis patterns, emotional arc, tense consistency, person-voice threading + iltifat, antonym pairing — because LOSING THEM CHANGES MEANING. Tier 2+3+4 sacrificed.

**Tier-coverage.** Tier 1 only.

**Nazm-policy marker.** OFF (Tier 1 preserved as meaning-bearing structures, but full nazm policy not yet active).

**Cross-axis interaction.** No A4 purpose defaults to `minimal` — explicit user override (e.g., utility translation that needs argument-structure preservation without aesthetic harmony).

**Said Nursi anchor.** Said Nursi's istilzam chain "Rahman → Rezzak → Rızk → Beka → Vücud → İlim/İrade/Kudret → Hayat" — Tier 1 preservation is critical for the argument structure even when no other harmony work is performed. The cause-effect chain itself carries the theology; sacrifice it and the argument vanishes.

#### `light` (ACTIVATION GATE)

**Strategic stance.** Preserve Tier 1 + Tier 2. Full 3-Pass methodology fires (Meaning Lock → Harmony Map → Target Reconstruction). Tier 1 entries (meaning-as-harmony) AND Tier 2 entries (high-priority comprehension scaffolds: grammatical parallelism, ring composition, chiastic structure, pronoun chains, clause-length patterning, evidence-claim rhythm, concession-rebuttal, thematic bracketing) are preserved. Tier 3 + Tier 4 sacrificed.

**Tier-coverage.** Tier 1 + Tier 2.

**Nazm-policy marker.** **ACTIVE — activation gate threshold.**

**Cross-axis interaction.** A4 purpose default match: `casual` (per A4 matrix's "moderate"). A4 silent → `light` via chain.

**Said Nursi anchor.** Casual edition of Risale-i Nur for general curious reader. The text's parallelism, ring composition, and chiastic structures are preserved (Tier 2); the meaning-bearing istilzam chains, emotional arcs, and tense shifts are preserved (Tier 1); the register-alternation conditionality (Tier 3) and phonetic echoes (Tier 4) are sacrificed.

#### `standard`

**Strategic stance.** Preserve Tier 1 + Tier 2 + Tier 3 with conditional clauses respected. Translator-AI examines source at runtime per Tier 3 entry and determines whether PRESERVE-WHEN or SACRIFICE-WHEN clause fires. Tier 4 sacrificed.

**Tier-coverage.** Tier 1 + Tier 2 + Tier 3 conditional.

**Nazm-policy marker.** ACTIVE.

**Cross-axis interaction.** A4 purpose defaults: `scholarly`, `devotional`, `language-learning` (per A4 matrix's "high").

**Said Nursi anchor.** Scholarly/devotional edition of Risale-i Nur. Register alternation (Tier 3 PRESERVE-WHEN: "source uses register alternation as a structural device" — fires for Nursi per the user's stored register-fidelity memory). Synonym chaining (Tier 3 PRESERVE-WHEN: deliberate theological emphasis on divine names — Nursi's repeated names of God in chains) — preserved. Callback and forward-reference (Tier 3 PRESERVE-WHEN: source's long-range echoes carry argument) — preserved. Sentence-length rhythm (Tier 3 PRESERVE-WHEN: source's tempo carries meaning) — preserved when Nursi's tempo is meaning-bearing.

#### `maximum`

**Strategic stance.** Preserve all 4 tiers. Tier 1 + Tier 2 + Tier 3 conditional + Tier 4 where target language permits. The AI attempts maximum form preservation including phonetic echo, rhyme, cadence matching where target language structurally supports it; acknowledges sacrifices in the harmony report when target language cannot (e.g., Semitic root echo to non-Semitic target).

**Tier-coverage.** All 4 tiers (Tier 3 respecting conditional; Tier 4 attempted where feasible).

**Nazm-policy marker.** ACTIVE (maximum emphasis).

**Cross-axis interaction.** A4 purpose default: `performance` (per A4 matrix's "MAXIMUM"). Rhythm = meaning per harmony_layer commitment. A5 orthogonal — `maximum` form can coexist with any A5 stance: `foreignized-max` + `maximum` = scholarly devotional Quran-recitation; `lightly-domesticated` + `maximum` = poetic translation that mirrors source rhythm in target's natural poetic vocabulary.

**Said Nursi anchor.** Performance/recitation edition of Risale-i Nur. Phonetic harmony attempted where Turkish-English target permits; cadence matched where possible; maqta' harmony explored; root echo acknowledged as "source-language-specific, no equivalent" in harmony report where the source's Arabic/Turkish root play cannot transfer.

**Tier 3 runtime determination example.** For each Tier 3 entry at A6 `standard`+, the AI examines the source:

1. AI examines source for register-consistency Tier 3 entry.
2. AI checks PRESERVE-WHEN clause: "source uses register alternation as a structural device."
3. AI checks SACRIFICE-WHEN clause: "source is register-uniform and target language requires register adjustment for naturalness."
4. AI determines which clause fires for the specific source passage.
5. AI applies preserve-or-sacrifice decision accordingly.

This runtime determination is INVARIANT across A6 Levels 4 and 5. The Tier 3 conditional logic is harmony_layer's structural rule, not a user-configurable property.

**Tier 4 language-feasibility at Level 5 details:**
- Phonetic echo: attempted where target language has its own sonic possibilities.
- Internal rhyme and assonance: attempted; sacrificed when target phonology doesn't support source's pattern.
- Root echo: Semitic-specific. For non-Semitic targets (English, Turkish, etc.), acknowledged as "source-language-specific, no equivalent" in the harmony report.
- Rhythmic cadence: attempted where target syllable structure permits.
- Maqta' harmony: source-language-specific; acknowledged in harmony report.

The harmony report is the documentation channel where the translator-AI flags Tier 4 sacrifices that target-language structure made unavoidable.

**A5↔A6 four-corners independence:**
- `foreignized-max` A5 + `off` A6: rare — preserve foreign vocabulary while flattening rhythm (utility translation).
- `foreignized-max` A5 + `maximum` A6: common scholarly devotional (preserve both vocabulary and form).
- `lightly-domesticated` A5 + `off` A6: common casual mass-market (anglicize vocabulary, flatten rhythm).
- `lightly-domesticated` A5 + `maximum` A6: poetic translations that domesticate vocabulary but mirror rhythm.


---

## A7 — scaffolding

**Concept.** How much explanatory material accompanies the translation at the TEXT SURFACE — footnotes, parenthetical glosses, transliterations, brief in-line explanations. A7 has two distinguishing roles beyond simple level-setting:

1. **Scaffolding budget** that determines which A1 cultural-reference-recognition actions and A3 source-culture handling actions can fire (some actions like INLINE-GLOSS and FOOTNOTE consume budget; others like KEEP-AS-IS and EXPLICATE-FUNCTION don't).
2. **Render-control surface** for the always-on multi-meaning preservation policy when polysemy fires (the user controls HOW preserved senses appear; the policy controls WHETHER).

**5 ordinal levels:** `off | minimal | standard | rich | scholarly`. Plain-ordinal. Maps to edition-tradition exemplars at each level.

**Default-when-A7-silent = `rich` via A4 chain.** A7 silent → A4 silent → A4 = `casual` → A4 matrix's "casual A7 = rich (help unfamiliar)" → A7 = `rich`. Intentionally HIGHER than A6's default `light` — reflects the project's accessibility commitment for outsider/uninitiated readers.

**Per-level budget = qualitative + per-page operational guidance.** Qualitative threshold gives prompt-clear stance; per-page operational guidance gives the AI a sanity-check unit. **Per-page numbers are NOT hard caps** — some passages legitimately need more; AI uses them as orientation thresholds, not enforcement gates.

#### `off`

**Scaffolding stance.** No text-surface scaffolding. The translation reads as plain target-language prose. No footnotes, no inline glosses, no transliterations with parenthetical paraphrase, no flagged cultural-context markers.

**Budget.** Zero footnotes per page; zero inline glosses; zero apparatus. Qualitative: clean text only.

**Action permission.** STRICTLY BLOCKED: INLINE-GLOSS, FOOTNOTE, TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT, BRIDGE-CULTURAL-DISTANCE. Available: all budget-FREE actions (KEEP-AS-IS, EXPLICATE-FUNCTION, DOMESTICATE-disfavored-but-available, TRANSLITERATE-FULLY, ASSUME-SHARED-CULTURAL-KNOWLEDGE, PRESERVE-CULTURAL-SPECIFICITY, TARGET-LANGUAGE-EQUIVALENT, KEEP-HONORIFICS-SOURCE, ANGLICIZE-HONORIFICS, DOMESTICATE-CULTURAL-FRAME).

**Multi-meaning render rule.** EXPLICATE-FUNCTION FALLBACK — when the polysemy policy fires, the AI paraphrases combining senses into the body (e.g., "the day of judgment, of religion, of true reckoning"). No scaffolding; the polysemy POLICY (preservation) is invariant; the RENDER falls back to the only mechanism A7=off permits.

**Why STRICT.** Permitting "minimal scaffolding for essential cases" at A7=off would make A7=off operationally indistinguishable from A7=minimal and would defeat the budget semantics. Strict blocking forces fallback to budget-FREE actions.

**Cross-axis note.** A4 default for `performance` (oral recitation; clean text). A5/A6 orthogonal. A7=off + foreignization-preferring A5 forces budget-FREE foreignization-preserving alternatives (EXPLICATE-FUNCTION over INLINE-GLOSS); harmony report at A6 Levels 3+ flags the trade-off.

**Said Nursi anchor.** An oral-recitation passage of Risale-i Nur for live audience delivery — clean text only, no apparatus.

**Edition-tradition exemplar.** A utility translation; oral interpretation; road sign; UN-style summary translation.

#### `minimal`

**Scaffolding stance.** Sparse text-surface scaffolding for the HARDEST references only. Pop-translation general-audience paperback with rare footnotes and first-use-only transliteration glosses.

**Budget.** 0-1 footnotes per page (orientation, not cap); sparse inline glosses; first-use transliteration only ("Bediuzzaman (wonder of the age)" once, then "Bediuzzaman").

**Action permission.** ALLOWED SPARINGLY (1-2 per page for hardest): INLINE-GLOSS. RARE: FOOTNOTE. FIRST-USE-ONLY: TRANSLITERATE-WITH-GLOSS. SPARINGLY: FLAG-CULTURAL-CONTEXT. BLOCKED: BRIDGE-CULTURAL-DISTANCE.

**Multi-meaning render rule.** PRIMARY + MINIMAL FOOTNOTE NOTING OTHER SENSES — primary sense in body; brief footnote like "also: judgment / religion / truth". One footnote per polysemous-passage maximum.

**Cross-axis note.** No A4 purpose defaults here in the matrix (reserved for edge cases). A5 typically foreignized or balanced. A6 typically off or minimal.

**Said Nursi anchor.** A pop-translation general-audience Risale-i Nur paperback — sparse footnotes only for the hardest Sufi/kalam terms; first-use transliteration gloss.

**Edition-tradition exemplar.** Penguin Classics paperback; NIV pew Bible (no study apparatus).

#### `standard`

**Scaffolding stance.** Moderate text-surface scaffolding suitable for a standard scholarly edition. Inline glosses for technical terms on first use; moderate footnotes for context; routine transliteration with gloss; routine cultural-context flagging.

**Budget.** 1-3 footnotes per page (orientation); moderate inline glosses; transliteration with parenthetical paraphrase routine; cultural-context flags routine; bridge-cultural-distance moderate.

**Action permission.** MODERATE (3-5 per page): INLINE-GLOSS. FOR CONTEXT: FOOTNOTE. ROUTINE: TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT. MODERATE: BRIDGE-CULTURAL-DISTANCE.

**Multi-meaning render rule.** INLINE PARENTHETICAL PAIRED — `din [judgment / religion]` or `judgment (also religion / truth)`. Used for high-load polysemous passages where both senses matter for the reading.

**Cross-axis note.** A4 default for `devotional` (A4 matrix's "moderate"). A5 typically balanced. A6 typically light to standard. Orthogonal to A6's harmony report channel.

**Said Nursi anchor.** A standard scholarly Risale-i Nur edition — moderate footnotes; inline glosses for Sufi/kalam terms on first use; inline parenthetical for major polysemous concepts.

**Edition-tradition exemplar.** NIV Study Bible; Loeb Classical Library bilingual edition with apparatus on facing page.

#### `rich`

**Scaffolding stance.** Extensive text-surface scaffolding suitable for a Norton-Critical-style edition or a scholarly-but-readable casual edition. Inline glosses routine and extensive; footnotes extensive; transliteration with full paraphrase routine; cultural-context flagging routine; bridge-cultural-distance extensive.

**Budget.** 3-6 footnotes per page (orientation); extensive inline glosses; appendix-light material; full inline parentheticals for polysemy.

**Action permission.** ROUTINE + EXTENSIVE: INLINE-GLOSS. EXTENSIVE: FOOTNOTE. ROUTINE: TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT. EXTENSIVE: BRIDGE-CULTURAL-DISTANCE.

**Multi-meaning render rule.** INLINE PAIRED WITHOUT BRACKETS (where syntactically possible — "the day of judgment, of religion, of truth") OR FULL FOOTNOTE PAIRED (when inline pairing is awkward — full footnote explaining all senses with brief exegesis).

**Cross-axis note.** A4 default for `scholarly` AND `casual` (A4 matrix's "rich (help unfamiliar)" for casual — also chain default when A7 is silent). A5 anywhere from foreignized to lightly-domesticated. A6 anywhere from minimal to standard.

**Said Nursi anchor.** A Norton-Critical-style Risale-i Nur edition — extensive footnotes per page, inline glosses, light appendix material, inline parentheticals for polysemy.

**Edition-tradition exemplar.** Norton Critical Edition; Oxford World's Classics with critical introduction and notes.

#### `scholarly`

**Scaffolding stance.** Full text-surface scaffolding apparatus suitable for a critical apparatus edition. All scaffolding-consuming actions fire freely; full apparatus channels engaged (introduction + glossary + endnotes + appendix + critical apparatus + exegetical history).

**Budget.** 6+ footnotes per page (orientation); full inline glosses; appendix; introduction; glossary; endnotes; critical apparatus; exegetical-history notes for major polysemous terms.

**Action permission.** ALL ACTIONS FREE: INLINE-GLOSS, FOOTNOTE, TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT, BRIDGE-CULTURAL-DISTANCE.

**Multi-meaning render rule.** APPARATUS-EDITION RENDER — body + full footnote + scholarly apparatus citing exegetical/linguistic literature on the polysemy + glossary entry. Each polysemous concept receives a glossary entry; each major polysemous passage receives an exegetical-history footnote tracing the sense-tradition.

**Cross-axis note.** A4 default for `language-learning` (A4 matrix's "MAX rich"). A5 typically foreignized. A6 typically standard to maximum.

**Said Nursi anchor.** A full scholarly apparatus Risale-i Nur edition — extensive footnotes, endnotes, scholarly introduction, glossary of Sufi/kalam terms, appendix, critical apparatus, exegetical history for major polysemous concepts like `din`, `nur`, `iman`.

**Edition-tradition exemplar.** SBL Greek NT critical apparatus edition; Robert Alter scholarly Hebrew Bible translation with apparatus; Brill critical edition.

**A1/A3 action permission table per level.**

Budget-consuming actions (gated by A7 level):

| Action | `off` | `minimal` | `standard` | `rich` | `scholarly` |
|---|---|---|---|---|---|
| A1 INLINE-GLOSS | BLOCKED | sparingly (1-2/page for hardest) | moderate (3-5/page) | routine + extensive | free |
| A1 FOOTNOTE | BLOCKED | rare | for context | extensive | free + full apparatus |
| A3 TRANSLITERATE-WITH-GLOSS | BLOCKED (use TRANSLITERATE-FULLY) | first-use only | routine | routine | free |
| A3 FLAG-CULTURAL-CONTEXT | BLOCKED | sparingly | routine | routine | free |
| A3 BRIDGE-CULTURAL-DISTANCE | BLOCKED | BLOCKED | moderate | extensive | free |

Budget-FREE actions (available at every A7 level, subject to A5 policy bias):
- A1: KEEP-AS-IS, EXPLICATE-FUNCTION, DOMESTICATE (project policy DOMESTICATE-disfavored), ASSUME-SHARED-CULTURAL-KNOWLEDGE.
- A3: KEEP-HONORIFICS-SOURCE, PRESERVE-CULTURAL-SPECIFICITY, TARGET-LANGUAGE-EQUIVALENT, ANGLICIZE-HONORIFICS, DOMESTICATE-CULTURAL-FRAME, TRANSLITERATE-FULLY (without gloss).

**Multi-meaning render rules per level (consolidated):**

| A7 Level | Render mechanism |
|---|---|
| `off` | EXPLICATE-FUNCTION fallback — preserve polysemy via paraphrase combining senses into body; no scaffolding |
| `minimal` | PRIMARY + MINIMAL FOOTNOTE noting other senses |
| `standard` | INLINE PARENTHETICAL PAIRED (`din [judgment / religion]` or `judgment (also religion / truth)`) |
| `rich` | INLINE PAIRED WITHOUT BRACKETS (where syntactically possible) OR FULL FOOTNOTE PAIRED |
| `scholarly` | APPARATUS-EDITION RENDER (body + footnote + scholarly apparatus citing exegetical/linguistic literature + glossary entry) |

The polysemy policy preserves WHETHER (invariant); A7 controls HOW (5 render mechanisms + A7=off fallback).

**Runtime conflict resolution.** When A7 is too low to accommodate the A1/A3 actions a low-A1 reader-level + foreignization-preferring A5 would demand:

1. **STRICT budget enforcement.** A7 BLOCKS budget-consuming actions per the action permission table.
2. **FALLBACK to budget-FREE actions.** EXPLICATE-FUNCTION, KEEP-AS-IS, ASSUME-SHARED-CULTURAL-KNOWLEDGE, PRESERVE-CULTURAL-SPECIFICITY. The AI selects per A5 stance.
3. **FLAG in harmony report at A6 Levels 3+.** Records that source-cultural specificity was preserved via paraphrase or budget-FREE action rather than via scaffolding.

**Worked example (A7=off + A1=very_basic + A5=foreignized):** AI wants INLINE-GLOSS for unfamiliar references but A7=off blocks. AI falls back to EXPLICATE-FUNCTION (paraphrases the cultural reference into the body). Harmony report at A6 Level 3+ flags: "source-cultural specificity preserved via paraphrase rather than gloss (A7=off budget constraint)."

---

## A8 — analysis_depth

**Concept.** How much interpretive material the system surfaces ALONGSIDE the translation in SEPARATE ANALYSIS SECTIONS — etymology notes, rhetorical analysis, cross-references, exegetical history, lexical-philological apparatus. **Distinct from A7's text-surface scaffolding** which lives on the reading page. A8 lives in the separate-sections apparatus channel (front matter, endnotes, appendix, sidebars, dedicated analysis chapters).

**5 ordinal levels:** `none | surface | standard | deep | scholarly`. Plain-ordinal.

**Default-when-A8-silent = `standard` via DUAL-TIER resolution** (unique among Strategy/Depth axes):
- **Tier 1 (A4 chain):** A8 silent + A4 explicitly set → A4 matrix's per-purpose A8 value.
- **Tier 2 (conservative-bias fallback):** A8 silent + A4 silent → A8 = `standard`.

Dual-tier is necessary because A8's A4 matrix casual default `surface` is operationally near-empty; chained-silent through casual default would produce sparse output at framework-cold-start. Conservative-bias `standard` defends the cold-start case while still allowing A4-driven defaults when A4 is set.

#### `none`

**Analysis stance.** No separate-sections apparatus at all. The translation reads as pure target-language prose with no front matter, no endnotes, no appendix, no analysis sections. Just the translation.

**Depth.** Zero content-types fire. Qualitative: pure translation only.

**Operational substance.**
- Content-type-by-level table: ALL 12 content-types BLOCKED.
- A7↔A8 boundary irrelevant at A8=none (no A8 channel content to position).
- Harmony-report-location: A6 harmony report remains in A6 channel regardless.
- Multi-meaning analysis: NONE (polysemy policy preserves senses via A7's render mechanism only; no A8 exegetical-history analysis produced).

**Cross-axis note.** A4 default for `performance` (oral recitation; zero apparatus) and in some configurations for `casual` (when paired with A7=off for utility translation). A5/A6/A7 orthogonal. **A7=off + A8=none = maximally-clean pure-translation configuration** (oral recitation use case).

**Said Nursi anchor.** An oral recitation passage of Risale-i Nur delivered live; pure translation only, no apparatus.

**Edition-tradition exemplar.** A utility translation (road sign / quick UN-style summary / oral interpretation) with no apparatus.

#### `surface`

**Analysis stance.** Minimal separate-sections apparatus. Brief publisher's note or minimal glossary for the most-needed terms; no analysis chapters, no extensive front matter.

**Depth.** 0-2 content-types fire minimally (introduction + glossary for most-needed terms only).

**Operational substance.**
- Content-type-by-level table: Introduction (publisher's note) + Glossary (major terms only) ACTIVE BRIEFLY; all other 10 content-types BLOCKED.
- A7↔A8 boundary: A7 carries scaffolding in-page; A8 surface keeps separate-sections minimal.
- Harmony-report-location: A6 harmony report standalone in A6 channel (no cross-references at A8=surface).
- Multi-meaning analysis: NONE — the brief glossary may note polysemy without full analysis.

**Cross-axis note.** A4 default for `casual` (per A4 matrix) and `performance` (when slight context needed). A5 typically domesticated or balanced. A6 typically off or minimal.

**Said Nursi anchor.** Pop-translation Risale-i Nur paperback; brief publisher's note; 2-page glossary of the most-needed Sufi/kalam terms only.

**Edition-tradition exemplar.** Penguin Classics paperback (no analysis chapter; minimal front matter).

#### `standard`

**Analysis stance.** Moderate separate-sections apparatus. Brief scholarly introduction; glossary of major terms; cross-references to other passages; brief exegetical-history footnotes on key concepts.

**Depth.** 2-4 content-types fire routinely (Introduction + Glossary + Cross-references + brief Exegetical-history).

**Operational substance.**
- Content-type-by-level table: Introduction (brief) + Glossary (major terms) + Cross-references (major passages) + Exegetical history (brief footnote on key polysemy) ACTIVE; other 8 content-types BLOCKED.
- A7↔A8 boundary: A7 in-page; A8 separate-sections (LOCATION rule).
- Harmony-report-location: A6 standalone (no cross-references at A8=standard).
- Multi-meaning analysis: brief lexical note in glossary on key polysemy (e.g., glossary entry for `din` noting "judgment / religion / truth"). No full exegetical paragraph.

**Cross-axis note.** A4 default for `devotional` (per A4 matrix). A5 typically balanced. A6 typically light to standard.

**Said Nursi anchor.** Standard scholarly Risale-i Nur edition; brief introduction; glossary of major Sufi/kalam terms; cross-references to other Words/Letters; brief footnotes on key polysemous concepts (`din`, `nur`, `iman`).

**Edition-tradition exemplar.** Oxford World's Classics with brief introduction + select notes; Loeb Classical Library with introduction.

#### `deep`

**Analysis stance.** Extensive separate-sections apparatus suitable for a Norton-Critical-style edition. Scholarly introduction; analysis chapter per major passage; extensive cross-references; exegetical-history paragraphs for key concepts; rhetorical analysis of structural elements; target-language-equivalent justification; theological commentary; historical-critical context.

**Depth.** 4-10 content-types fire per major passage; full apparatus channels open EXCEPT philological apparatus and cross-tradition references.

**Operational substance.**
- Content-type-by-level table: Introduction (scholarly) + Glossary (extensive) + Etymology (major terms) + Rhetorical analysis (per major passage) + Cross-references (extensive) + Exegetical history (paragraph per major polysemous concept) + Lexical-history (major terms) + Target-language-equivalent analysis (major translation choices) + Theological commentary (major concepts) + Historical-critical context (per major passage) ACTIVE EXTENSIVELY; Philological apparatus + Cross-tradition references BLOCKED.
- A7↔A8 boundary: in-page (A7) vs separate-sections (A8); LOCATION default tiebreaker.
- Harmony-report-location: A6 channel standalone with cross-references to A8 analysis chapters (and A8 sections cite harmony report).
- Multi-meaning analysis: exegetical-history paragraph per major polysemous concept in dedicated analysis section.

**Cross-axis note.** A4 default for `scholarly` (per A4 matrix). A5 typically foreignized or balanced. A6 typically standard to maximum.

**Said Nursi anchor.** Norton-Critical-style Risale-i Nur edition; scholarly introduction; analysis chapter per major Word/Letter; extensive cross-references; exegetical-history paragraphs for key concepts (`din`, `nur`, `iman`, `nefs`); rhetorical analysis of nazm; target-language-equivalent justification for major translation choices; theological commentary; historical-critical context.

**Edition-tradition exemplar.** Norton Critical Edition (translation + extensive analysis chapter + criticism collection).

#### `scholarly`

**Analysis stance.** Full critical apparatus edition. All 12 content-types fire as relevant. Comprehensive introduction; exhaustive glossary; etymology of every key term; rhetorical analysis per passage; full exegetical history; lexical-history; target-language-equivalent analysis; theological commentary; historical-critical context; philological apparatus; cross-tradition references.

**Depth.** All 12 content-types fire; full apparatus.

**Operational substance.**
- Content-type-by-level table: ALL 12 content-types ACTIVE with full apparatus density.
- A7↔A8 boundary: maximum-apparatus configuration in both channels at A7=scholarly + A8=scholarly.
- Harmony-report-location: A6 channel standalone with cross-references to A8 analysis sections (and A8 sections cite harmony report).
- Multi-meaning analysis: full exegetical-history apparatus per polysemous concept (commentary tradition + lexical-philological argument + cross-tradition references).

**Cross-axis note.** A4 default for `language-learning` (per A4 matrix; refinement resolves prior `deep+scholarly` ambiguity to `scholarly`). A5 typically foreignized. A6 typically standard to maximum.

**Said Nursi anchor.** Full critical apparatus Risale-i Nur edition; comprehensive introduction (Said Nursi's life, intellectual context, Risale-i Nur project history); exhaustive glossary; etymology of every key term; rhetorical analysis per passage; exhaustive cross-references; full exegetical history per polysemous concept; lexical-history of target-language equivalents; full target-language-equivalent analysis; extensive theological commentary; full historical-critical apparatus; philological apparatus (manuscript variants if available); cross-tradition references (other Sufi/kalam authors).

**Edition-tradition exemplar.** SBL Greek NT critical apparatus edition; Robert Alter scholarly Hebrew Bible translation with apparatus; Brill critical edition; Cambridge Companion + Critical Edition.

**Content-type-by-level table** (12 content-types × 5 levels):

| Content-type | `none` | `surface` | `standard` | `deep` | `scholarly` |
|---|---|---|---|---|---|
| Introduction (front matter) | — | publisher's note | brief | scholarly | comprehensive |
| Glossary entries | — | major terms only | major terms | extensive | exhaustive |
| Etymology notes | — | — | — | major terms | every key term |
| Rhetorical analysis (nazm structure) | — | — | — | per major passage | per passage |
| Cross-references (intra-corpus) | — | — | major passages | extensive | exhaustive |
| Exegetical history (polysemy senses) | — | — | brief footnote | paragraph per major concept | full commentary tradition |
| Lexical-history (target-equiv drift) | — | — | — | major terms | every key term |
| Target-language-equivalent analysis | — | — | — | major translation choices | every translation choice |
| Theological/conceptual commentary | — | — | — | major concepts | extensive |
| Historical-critical context | — | — | — | per major passage | full |
| Philological apparatus | — | — | — | — | full |
| Cross-tradition references | — | — | — | — | full |

Content-type distinctions:
- **Etymology** = source-language word origins (Arabic-root analysis for Said Nursi).
- **Lexical-history** = target-language equivalent's semantic drift (how "religion" came to mean what it means in English; relevant when translating `din`).
- **Target-language-equivalent analysis** = WHY this English word was chosen over alternatives (translator's justification).
- **Exegetical history** = sense-tradition of polysemous concepts across commentary tradition (how the senses of `din` developed).

**A7↔A8 boundary spec — 3 complementary framings (LOCATION is default tiebreaker):**

**Framing 1 — by LOCATION.**
- **A7 = in-page apparatus** — footnotes, glosses, transliterations with parenthetical paraphrase, brief in-line cultural-context flags. Lives on the reading page next to the source text.
- **A8 = separate-sections apparatus** — front matter (introduction, glossary), endnotes, appendix, sidebars, dedicated analysis chapters. Lives in distinct sections of the published edition.

**Framing 2 — by SCOPE.**
- **A7 = per-reference scaffolding** — addresses a specific word or phrase at a specific point in the text.
- **A8 = per-passage / per-corpus analysis** — addresses a full passage, a thematic concept across passages, or the source corpus as a whole.

**Framing 3 — by AUDIENCE-INTERACTION.**
- **A7 = inline interruption** — reader looks down to footnote/gloss, then back up to continue reading same passage.
- **A8 = deferred study session** — reader reads the translation first, then turns to separate analysis sections after completing the translation reading.

**LOCATION default tiebreaker.** When the three framings disagree (e.g., a long footnote that scopes per-passage but lives in-page), use LOCATION: if it lives on the reading page, it's A7; if it lives in a separate section, it's A8.

**Operational test for AI.** "Does this belong on the reading page next to the source word (A7) or in a separate analysis section after the translation (A8)?"

Worked examples:
- Footnote citing a single word's cultural meaning → A7.
- Multi-paragraph analysis of the passage's rhetorical structure → A8.
- Brief inline gloss of `nefs` → A7.
- Full essay on the development of the `nefs` concept across Sufi tradition → A8.
- Glossary entry for `din` noting "judgment / religion / truth" → A8 (lives in glossary section).
- Inline parenthetical `din [judgment / religion]` → A7 (lives on reading page next to source word).

**All 4×5 = 20 A7×A8 combinations valid.** Notable patterns:
- A7=off + A8=none: maximally-clean pure-translation (oral recitation).
- A7=off + A8=scholarly: clean translation + heavy analysis section (Robert Alter Hebrew Bible).
- A7=scholarly + A8=surface: extensive in-page apparatus + clean post-translation (language-learning parallel-text).
- A7=scholarly + A8=scholarly: maximum-apparatus in both channels.

**Harmony-report-location rule.** A6 harmony report stays in the A6 channel STANDALONE regardless of A8 level. At A8 = `deep` or `scholarly`, cross-references between channels are added (harmony report cites A8 analysis chapters; A8 sections cite harmony report). This preserves A6 finding's apparatus-channel commitment AND preserves A6↔A8 orthogonality AND enables reader navigation.

**Multi-meaning three-layer treatment.**
- **Policy invariant (WHETHER preserved):** policy preserves both senses regardless of axis settings.
- **A7 controls HOW rendered in translation** at text surface — footnote / parenthetical / inline-paired / apparatus-edition render per A7 level.
- **A8 controls HOW analyzed in separate sections at high A8 levels** — exegetical-history of the sense-tradition; commentary tradition; lexical-philological argument.

A7 and A8 are complementary, not redundant: A7 makes the polysemy visible in the translation; A8 (at high levels) explains the sense-tradition in analysis.


---

## A4 default matrix (per-purpose × per-axis defaults)

A4 drives DEFAULTS for the other 7 axes via this matrix. When A4 is set and an axis is silent, the system uses the matrix's per-purpose default. Refinement notes from A6/A7/A8 findings are applied inline (precise labels matched to each axis's enum).

| A4 Purpose | A1 reader_level | A2 domain_expertise | A3 source_culture | A5 source_fidelity | A6 form_preservation | A7 scaffolding | A8 analysis_depth |
|---|---|---|---|---|---|---|---|
| `scholarly` | `advanced` | `educated` | any (often outsider-with-study) | `foreignized` | `standard` | `rich` | `deep` |
| `devotional` | `conversational` | `aware`-to-`educated` | `source-native` / `heritage` | `foreignized-max` | `standard` | `standard` | `standard` |
| `casual` | `daily` | `lay`-to-`aware` | `outsider`-to-`acquainted` | `balanced` | `light` | `rich` | `surface` |
| `language-learning` | `conversational` (matched to learner) | `lay` | `outsider` | `foreignized` | `standard` | `scholarly` | `scholarly` |
| `performance` | `conversational` | any | any | `balanced` | `maximum` | `minimal` (or `off` for pure oral) | `surface` (or `none` for pure oral) |

**Default-when-A4-silent = `casual`.** Categorical equivalent of conservative-bias-LOWER. When A4 is silent, all 7 other-axis defaults chain through casual: A1=`daily`, A2=`aware`, A3=`acquainted`, A5=`balanced`, A6=`light`, A7=`rich`, A8=`standard` (via dual-tier: A4 silent → conservative-bias-fallback `standard`, not casual's `surface`).

---

## 5 always-on Layer 2 policies

These policies are INVARIANT across all axis configurations. They fire whenever their triggering condition is met, regardless of any single axis setting. The user does not opt out at the framework level; only the RENDER (per axis) varies.

### 1. Multi-meaning preservation

**Policy.** When a source word is polysemous AND the local construction (genitive, plausibility, syntactic frame) permits multiple senses simultaneously, preserve ALL senses in the translation. The policy preserves WHETHER (senses are retained); A7 controls HOW (render mechanism per A7 level); A8 controls analysis depth (exegetical-history per A8 level).

**Why.** Source-side polysemy carries theological / argumentative load (e.g., Quranic `din` simultaneously meaning judgment / religion / truth in the local construction; Said Nursi's layered Sufi/Naqshbandi/Islamic vocabulary). Selecting a single sense in target collapses the source's intended layered reading.

**Three-layer treatment.** Policy (WHETHER) + A7 render (HOW in translation) + A8 analysis (HOW in apparatus).

**Render fallback at A7=off.** When A7=off blocks all scaffolding-render mechanisms, EXPLICATE-FUNCTION (a budget-FREE A1 action) provides preservation by paraphrasing rather than bracketing — both senses fit into the body text as plain prose. Policy invariant satisfied; render forced budget-FREE.

### 2. Register-alternation preservation

**Policy.** When the source uses register alternation as a structural device (mixing plain and elevated registers as a Tier 1/2 structure), preserve the register alternation in the target. Do not flatten source's plain register into elaborate target prose; do not flatten source's elevated register into casual target prose. The register alternation is meaning-bearing structure, not vocabulary display.

**Why.** Said Nursi's register alternations between plain Turkish, elaborated Sufi Turkish, and Quranic Arabic citations are structural (the alternation marks shifts between exposition, mystical state, and scripture). Flattening produces ornate uniformity that collapses the structural signal. This is also recorded as the user's stored register-fidelity memory: don't pull plain source registers up into ornate/archaic English; C1 ≠ vocabulary display; preserve register alternation as Tier 1/2 structure.

**Operational scope.** Tier 1 (Non-Negotiable) for register-alternation as structural device; Tier 3 conditional (per harmony_layer Tier 3 PRESERVE-WHEN clause) when source is register-uniform.

### 3. Polysemy disambiguation via local construction

**Policy.** When a source word is polysemous, the LOCAL CONSTRUCTION (genitive, plausibility, syntactic frame) picks the intended sense — NOT the surrounding metaphor's momentum. Do not let the larger metaphorical theme override the local construction's sense-selection signal.

**Why.** A surrounding legal-courtroom metaphor doesn't override that `mukabil` in genitive construction with `İman` means "in exchange for" / "put up as stake"; nor does a surrounding light-darkness metaphor override that `din` in a specific local genitive picks "judgment" not "religion." The local construction is the disambiguation evidence; the surrounding momentum can mislead.

**This is also recorded as the user's stored word-sense disambiguation memory.** Polysemy resolution = local-construction-first, surrounding-momentum-second.

**Distinction from Policy 1.** Policy 1 fires when local construction permits MULTIPLE senses (preserve all). Policy 3 fires when local construction picks a SINGLE sense (don't let momentum override). They are complementary, not overlapping.

### 4. Nazm preservation

**Policy.** Form is meaning. Structural form (rhythm, parallelism, word-order, ring composition, chiasmus, cause-effect chains, hidden syllogisms) carries semantic weight per the project's harmony_layer Tier 1-4 system. At A6 ≥ `light`, the nazm-as-meaning policy is ACTIVE: full 3-Pass methodology (Meaning Lock → Harmony Map → Target Reconstruction) fires; structural form is preserved per the per-level tier-coverage map.

**Why.** Said Nursi's istilzam chains, Quranic ring composition, Sufi parallelism — these are not surface ornament; they are how meaning is carried. Loss of form is loss of meaning.

**Activation gate.** A6 Level 3 `light` per A6 commitment. Below the gate: partial 3-Pass methodology. At or above the gate: full methodology.

**Sacrifices documented in harmony report.** At A6 ≥ `light`, the translator-AI produces a harmony report (A6 apparatus channel) documenting what was preserved and what was sacrificed at the harmony level. Sacrifices include Tier 4 language-feasibility issues (Semitic root echo to non-Semitic target) and Tier 3 SACRIFICE-WHEN-clause-fired cases.

### 5. No-smoothing

**Policy.** Do not smooth source's awkwardness into target's natural prose when the awkwardness is meaning-bearing. Source's intentional disruption (delayed resolution, abrupt shift, surprising word-order, deliberate ellipsis) carries semantic load; smoothing collapses it. Prefer slight target-language awkwardness over loss of source's intentional structure.

**Why.** Translator-AI's natural target-language fluency bias produces over-smoothed translations that lose source's signal. The no-smoothing policy is the counter-bias.

**Operational examples.** Said Nursi's elliptical Sufi formulations should not be expanded into explicit explanatory prose; Nursi's abrupt iltifat (person-shift) should not be smoothed into consistent third-person; Quranic delayed-revelation structures should not be smoothed into linear exposition.

**Bidirectional complement.** A future 6th policy (target-side accidental polysemy / direction-flip leakage) is the BIDIRECTIONAL DUAL of no-smoothing: no-smoothing prevents UNDER-translation via source-smoothing; the new policy prevents OVER-translation via target wording opening senses source doesn't admit. The 6th policy is being incrementally added per diagnostic inquiry findings.

---

## Notes on prompt context (how the AI uses this document at translation time)

**This document is AI prompt context, not a synthesis-process artifact.** It is loaded into the translator-AI's system prompt to give the AI calibrated understanding of each TranslationConfig field value.

**Spectrum calibration.** When the user sets a single config value (e.g., `reader_level = "daily"`), the AI sees not just the chosen value but the full enum (`very_basic | daily | conversational | advanced | native`) and per-level definitions. This lets the AI calibrate "daily" against its neighbors — daily means MORE than very_basic but LESS than conversational; the AI's behavior is anchored by the full spectrum, not floating on a single label.

**Per-axis order of consultation.**
1. A1 / A2 / A3 (Reader family) — read at every reference (cultural reference recognition, domain term, source-culture proper-noun / honorific / cultural context).
2. A4 (Purpose) — read once per translation to set strategic defaults for axes left silent.
3. A5 (Source Fidelity) — read at every translation choice to modulate which A1/A3 actions to PREFER.
4. A6 (Form Preservation) — read at every passage to determine which harmony_layer tiers to preserve; controls 3-Pass methodology activation.
5. A7 (Scaffolding) — read at every reference to determine which A1/A3 budget-consuming actions can fire; controls multi-meaning render in translation.
6. A8 (Analysis Depth) — read at major-passage level to determine which content-types fire in separate-sections apparatus; controls multi-meaning analysis in apparatus.

**Cross-axis cascade (when axes left silent).**
- A8 silent → A4 chain (A4 explicitly set → A4 matrix); or conservative-bias fallback `standard` when A4 also silent.
- A7 silent → A4 chain → `rich`.
- A6 silent → A4 chain → `light`.
- A5 silent → A4 chain → `balanced`.
- A4 silent → `casual`.
- A1 / A2 / A3 silent → defaults (`conversational` / `aware` / `acquainted`) — conservative-bias-LOWER.

**Receptive-only commitment for A1/A2/A3 (Reader family).** The reader's receptive capacity is what drives handling actions — what the reader can recognize / understand / engage with — not productive capacity. A1=`daily` means a reader who reads at daily-conversational level; the AI calibrates handling actions to that receptive threshold.

**Receptive-only NOT APPLICABLE to A4/A5/A6/A7/A8.** These are translator-strategy axes; not reader properties.

**DOMESTICATE-disfavored cross-cutting policy.** INVARIANT across all axes and levels. Foreignization-preserving alternatives (INLINE-GLOSS, EXPLICATE-FUNCTION, FLAG-CULTURAL-CONTEXT, TRANSLITERATE-WITH-GLOSS, PRESERVE-CULTURAL-SPECIFICITY) are preferred over DOMESTICATE. DOMESTICATE is last-resort, even at `lightly-domesticated` A5 (where it is selectively PERMITTED in narrow cases, not preferred).

**A5 has NO own implementation actions.** A5 is a strategic stance that MODULATES which A1 / A3 actions to PREFER. The PREFERENCE ORDER varies by A5 level; the action set is fixed.

**A7 is the scaffolding BUDGET that GATES A1/A3 budget-consuming actions.** Even if A5 prefers INLINE-GLOSS, A7=off blocks it; AI must fall back to budget-FREE alternatives (EXPLICATE-FUNCTION, KEEP-AS-IS).

**Runtime conflict resolution (A7 strict budget enforcement).** When A7 blocks a preferred A1/A3 action: (1) strict block; (2) fallback to budget-FREE; (3) flag in harmony report at A6 ≥ `light`. Deterministic; runtime; does not change axis semantics.

**Apparatus channel separation (A6 vs A7 vs A8).**
- A6 harmony report = meta-analytic (translator's commentary on form-preservation work).
- A7 in-page scaffolding = reader-facing in-page (footnotes / glosses on reading page).
- A8 separate-sections = reader-facing post-translation (introduction / glossary / analysis chapters / appendix).

Three distinct apparatus channels; cross-references at high A8 (deep / scholarly) for reader navigation; otherwise standalone.

**A4 drives the per-purpose × per-axis default matrix.** When the user picks A4 only and leaves other axes silent, the matrix supplies defaults per-purpose. This is the primary user UX — pick a purpose, let the matrix calibrate the rest. Per-axis override is always available for the user who wants explicit control.

