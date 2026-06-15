---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/finding.md
---
# Finding: a1_syntactic_processing_capacity_levels

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/finding.md` (the sibling sub-field finding, which itself refines `2026-06-05_14-14__translation_config_axes/finding.md` — the root architectural finding).

**Revision trigger:** Continuation — applying the same shape developed for vocabulary-breadth to the next A1 sub-field. The user explicitly asked: "now can we do the same for syntactic-processing-capacity."

**What's preserved:**
- A1 Reader Level as composite-axis with 5 sub-fields (the root architectural commitment)
- vocabulary-breadth as A1 sub-field #1 with its complete spec (the prior sibling finding)
- The 4-layer framework architecture (4 layers: USER-FACING AXES / POLICY / SOURCE-DESCRIPTION / SYSTEM-FLAGS)
- The 8-axis structure in 4 families
- Receptive-only commitment for A1 (recognition not production)
- Language-agnosticism at concept level
- Composite-axis pattern's default-propagation mechanism
- Same labels (`very_basic | daily | conversational | advanced | native`) across A1 sub-fields
- A1↔A2 boundary as a per-sub-field test (vocabulary's A1↔A2 vs syntax's A1↔A2 are SEPARATE)
- POLICY layer commitments

**What's changed:** No structural commitment of the prior findings is altered. This finding ADDS specification at the sub-field level for syntactic-processing-capacity, ADAPTING the vocabulary-breadth 4-component template for syntax.

**What's new:**
- 5 named ordinal levels for syntactic-processing-capacity (same labels as A1 headline)
- An **ADAPTED 4-component template**: reader-profile + **structural-complexity tier** (replacing vocabulary's frequency-tier) + **register/genre-tier** (reframed from register-tier) + **restructuring-test sketch** (replacing substitution-test)
- The structural-complexity tier with 5 sub-measures: sentence-length range / embedding-depth max / suspension-load max / word-order canonicality / center-embedding max
- Restructuring-test action names: SPLIT / UNEMBED / LINEARIZE / ADD-CONNECTIVES (primary); REDUCE-NOMINALIZATIONS / REPLACE-PARENTHETICALS / RESOLVE-GARDEN-PATHS (secondary)
- Per-level positive + negative English example sentences (verified by structural analysis)
- 4 adjacent-level boundary specs with sentence pairs — the user's seed sentence anchors conversational↔advanced
- A1↔A2 boundary clarification for SYNTAX with specialist-domain example list (legal / mathematical / medical-research)
- Suggested migration mapping parallel to vocabulary-breadth's (same labels per same-labels-for-default-propagation)
- Template-adaptation rationale (3 paragraphs explaining the 3 adapted components)

**Migration:** No production system has yet implemented `syntactic_processing_capacity` as a typed field. This finding produces the design that future pydantic / schema work will instantiate. The existing 3-level `AUDIENCE_LEVEL` knob can continue alongside; the suggested mapping is parallel to vocabulary-breadth's (`late_learner_simple → daily`; `late_learner → conversational`; `native → native`).

## Question

**Context.** The translation_config_axes inquiry established A1 Reader Level as a composite-axis with 5 sub-fields. The vocabulary_breadth_levels inquiry specified the first sub-field (vocabulary-breadth) with a 4-component template (reader-profile + frequency-tier + register-tier + substitution-test). This inquiry is the next step: specify the second sub-field — **syntactic-processing-capacity** — which the prior finding defined as "how dense a sentence structure the reader can parse without losing the thread (long nested clauses, multi-clause subordination, etc.)."

**The question.** For the syntactic-processing-capacity sub-field of A1 Reader Level, what should the 5 ordinal levels be — what concept does each level capture, what logic distinguishes each level from its neighbors, and what concrete example sentence structures make each level operationally identifiable — defined language-agnostically at the concept level (English example sentences allowed for illustration), and using a 4-component definition template adapted from the vocabulary-breadth template (since some components — particularly frequency-tier — don't directly apply to syntax)?

**Goal.** Produce 5 mutually-distinct, ordinally-meaningful, spectrum-covering levels for syntactic-processing-capacity — each operationalizable as a prompt instruction for the translator-AI, each with explicit distinguishing logic referencing clause-nesting / subordination-chain length / working-memory load, each language-agnostic at the concept level. The 4-component template adapts from vocabulary-breadth's, with components that don't fit syntax replaced by analogues.

**Scope.** Syntactic-processing-capacity ONLY. The other 3 remaining A1 sub-fields (idiom-recognition, inference-capacity, cultural-reference-recognition) will be handled in their own follow-up inquiries with the same shape.

## Finding Summary

- **The 5 level names match the A1 headline labels:** `very_basic | daily | conversational | advanced | native`. Same labels across all A1 sub-fields for clean default-propagation; semantics are sub-field-specific (vocabulary-breadth's `conversational` means newspaper-level vocabulary recognition; syntactic-processing-capacity's `conversational` means newspaper-level sentence-structure parsing).

- **Each level has an ADAPTED 4-component definition.** The vocabulary-breadth template had: reader-profile + frequency-tier + register-tier + substitution-test sketch. The syntactic-processing-capacity template ADAPTS to: reader-profile (kept) + **structural-complexity tier** (REPLACES frequency-tier; sentences don't have Zipfian frequency the way words do) + **register/genre-tier** (REFRAMED from register-tier; genres at similar complexity differ in syntactic profile) + **restructuring-test sketch** (REPLACES substitution-test; the runtime translator action for syntax is structural rearrangement, not lexical substitution).

- **The structural-complexity tier has 5 sub-measures**, presented as a labeled list per level: (1) sentence-length range (English-illustrative); (2) embedding-depth max; (3) suspension-load max — the number of ideas held in working memory before the main verb resolves; (4) word-order canonicality (canonical SVO vs marked); (5) center-embedding max (relevant at the top two levels). These five sub-measures jointly characterize a sentence's parsing difficulty.

- **The restructuring-test sketch names the runtime translator actions.** Primary actions: **SPLIT** (break long sentence into shorter), **UNEMBED** (pull embedded clause into its own sentence), **LINEARIZE** (convert center-embedding to left/right-branching), **ADD-CONNECTIVES** (replace implicit logical connections with explicit "because" / "however"). Secondary actions: REDUCE-NOMINALIZATIONS, REPLACE-PARENTHETICALS, RESOLVE-GARDEN-PATHS. Actions are STRENGTH-GRADED across levels: aggressive at very_basic; none at native (for general syntax).

- **`very_basic` — young child / brand-new L2 learner.** Parses only SVO simple sentences (≤6 words English-illustrative); no embedding, no suspension, canonical word order only. Translator splits any compound sentence, unembeds any embedded clause. CEFR ≈ A1.

- **`daily` — functional adult in daily life.** Parses coordinated sentences and simple relative clauses (≤15 words English-illustrative); embedding depth ≤1; suspension ≤1; canonical SVO with minimal marked orders. Translator replaces multi-clause subordination, dense nominalization, marked word orders. CEFR ≈ A2–B1.

- **`conversational` — average newspaper-reading educated adult.** Parses multi-clause subordinate sentences that proceed LINEARLY (subordinate clauses don't suspend the main verb) (≤25 words English-illustrative); embedding depth ≤2; suspension ≤2; common marked orders accepted; no center-embedding. Translator avoids dense academic, archaic, dialectal, specialist. CEFR ≈ B1–B2.

- **`advanced` — university-educated reader / skilled non-native who reads widely.** Parses nested subordination, parentheticals, and **up to 3-clause suspension before the main verb resolves** (the user's seed sentence is the anchor here: "The argument, despite being couched in the kind of dense subordination that requires the reader to hold three clauses in working memory before encountering the main verb, succeeds."). Sentence length ~25–40 words; embedding depth ≤3; up to 1 center-embedding; academic and literary marked word orders accepted. Translator avoids only 2-deep center-embedding, archaic word orders, and 4+ clause suspension. CEFR ≈ B2–C1.

- **`native` — educated native reading broadly across literary registers.** Parses all general syntactic structures including **2-deep center-embedding** (Henry James / Henry Adams style), 4+ clause suspension, archaic word orders (KJV-Pauline inverted constituent order; "Through Him to whom be glory, the work was done."), Faulkner stream-of-consciousness, late-Victorian deeply-nested literary prose. Sentence length unlimited. Does NOT necessarily parse subject-domain specialist syntactic conventions (legal compound with cross-references; mathematical quantifier-conditional formal statements; medical-research nominalization-heavy passive) — those are A2 Domain Expertise territory, NOT A1.native. CEFR ≈ C2+.

- **The A1↔A2 boundary for SYNTAX is explicit:** A1 covers all GENERAL syntactic structures across general registers (everyday → journalistic → academic-general → literary → archaic-literary). A2 Domain Expertise covers SUBJECT-DOMAIN syntactic conventions that require domain training to parse — legal cross-reference syntax ("Provided that the party of the first part, hereinabove referred to as..."); mathematical formal-statement syntax ("For all ε > 0, there exists δ > 0 such that..."); medical-research nominalization-heavy passive with statistical parenthetical notation. The boundary test parallels vocabulary's: "Does parsing this sentence's STRUCTURE require subject-domain training, or only broad general reading?" A 20-entry specialist-syntax example list in the body covers all three domains.

- **The A1↔A2 boundaries for syntax and vocabulary are SEPARATE.** A sentence with general syntactic structure but specialist vocabulary (e.g., a clear sentence about `myocardial infarction`) is A1 syntax + A2 vocabulary. Each sub-field carries its own A1↔A2 boundary; they don't need to align.

- **Conservative-bias for reader-facing axes = LOWER default level.** Same principle as vocabulary-breadth: for syntactic-processing-capacity, default to a LOWER level (assume less parsing capacity; user dials UP when the actual reader handles denser syntax). Specific default value is deferred to the defaults inquiry.

- **Migration from existing `AUDIENCE_LEVEL` is suggested**, parallel to vocabulary-breadth's: `late_learner_simple → daily`; `late_learner → conversational`; `native → native`. New positions: `very_basic` (below `late_learner_simple` for children / brand-new L2 learners parsing only SVO simple sentences); `advanced` (between `late_learner` and `native` for university-educated readers who handle 3-clause suspension but not 2-deep center-embedding).

- **What's deferred to future inquiries.** Per-language structural-complexity thresholds (Russian / Japanese / Arabic have different complexity dynamics — head-final SOV in Japanese; flexible word order in Russian; VSO canonical with marked SVO in Arabic). Specific conservative-bias default value for syntactic_processing_capacity. The 3 remaining A1 sub-fields (idiom-recognition, inference-capacity, cultural-reference-recognition). Runtime restructuring implementation (LLM-judged vs parser-backed). Pydantic dataclass shape including the `syntactic_processing_capacity: Literal[...]` field. Default-derivation from A4 Purpose + A1 headline.

## Finding

### How to read this finding

The body presents:

1. **Cross-cutting framing constraints** that apply to all 5 levels.
2. **The ADAPTED 4-component template** with rationale for each adaptation.
3. **Each of the 5 levels** in its own subsection, with the structural-complexity tier presented in TABULAR format for clarity.
4. **The 4 adjacent-level boundary specs** with sentence-pair examples (the user's seed sentence at conversational↔advanced).
5. **The A1↔A2 boundary for syntax** with the test and a 3-domain specialist-syntax example list.
6. **The suggested migration mapping** from `AUDIENCE_LEVEL`.

### Cross-cutting framing constraints

- **Receptive only.** Every level description specifies what the reader PARSES / FOLLOWS / RECOGNIZES when encountered, not what the reader CAN CONSTRUCT. Phrases like "uses this structure" / "writes at this complexity" never appear.

- **Language-agnostic at the concept level.** Every level's CONCEPT (gradient from simple to complex; cognitive complexity via length / depth / suspension / word-order / center-embedding) is universal. English example sentences and thresholds are ILLUSTRATIVE. SOV languages (Japanese) have left-branching dynamics; flexible-word-order languages (Russian) have different marked-vs-canonical distinctions; the CONCEPT translates, the specifics are per-language (next inquiry).

- **Same 5 labels across all A1 sub-fields.** A1 is a composite-axis with 5 sub-fields. When the user sets A1=`conversational`, syntactic-processing-capacity defaults to `conversational` (and vocabulary-breadth defaults to `conversational`, etc.). For clean default-propagation, all 5 A1 sub-fields use the same 5 label strings. The label SEMANTICS differ per sub-field.

- **Restructuring-test runtime concept.** At level L, the translator-AI restructures sentences above L's complexity threshold using SPLIT / UNEMBED / LINEARIZE / ADD-CONNECTIVES (primary) and secondary actions. Runtime IMPLEMENTATION (LLM-judged vs parser-based metric) is deferred.

- **Conservative-bias for reader-facing axes** = LOWER default level. Specific default value deferred.

### The ADAPTED 4-component template

The template adapts from vocabulary-breadth's. Three components are renamed/replaced; the reasoning is principled, not arbitrary.

**1. Reader profile (kept).** Same shape as vocabulary-breadth: a one-sentence description of the typical reader + anchor demographics + genre anchor.

**2. Structural-complexity tier (REPLACES frequency-tier).**

*Why the adaptation:* Vocabulary uses frequency-tier because words have a Zipfian frequency distribution that strongly correlates with recognition difficulty (rare words are harder). For syntax, frequency and difficulty correlate WEAKLY — a long coordinated sentence is COMMON and EASY; a double center-embedding is RARE and HARD. The right dimension for syntactic-processing-capacity is COGNITIVE COMPLEXITY, not corpus frequency.

The structural-complexity tier is an umbrella for 5 sub-measures, presented per level as a labeled list:
- Sentence-length range (English-illustrative): "≤N words/sentence"
- Embedding depth max
- Suspension load max — the number of ideas held in working memory before the main verb resolves
- Word-order canonicality — canonical SVO only / canonical + common marked / + academic-literary marked / + archaic-literary inverted
- Center-embedding max — applies at L4 (≤1) and L5 (≤2); 0 implicit at L1–L3

**3. Register/genre-tier (REFRAMED from register-tier).**

*Why the adaptation:* Register and syntactic complexity correlate (academic register is hypotactic and dense), but GENRES at similar complexity differ in SYNTACTIC PROFILE — academic prose uses nominalization-heavy passive; literary fiction at the same complexity uses parentheticals and suspension. The reframed "register/genre-tier" captures both the sociolinguistic register AND the writing-genre, helping the user identify their target reader through a concrete genre (Dr. Seuss, newspaper, Henry James) rather than an abstract register label.

**4. Restructuring-test sketch (REPLACES substitution-test).**

*Why the adaptation:* Vocabulary's runtime translator action is lexical SUBSTITUTION (`purchase → buy`). Syntax's runtime translator action is structural RESTRUCTURING. The parallel naming (substitution-test ↔ restructuring-test) preserves template symmetry while reflecting genuinely different runtime actions.

Named primary actions:
- **SPLIT** — break a long sentence into shorter ones
- **UNEMBED** — pull an embedded clause into its own sentence
- **LINEARIZE** — convert center-embedding into left/right-branching
- **ADD-CONNECTIVES** — replace implicit logical connections with explicit "because" / "however" / "therefore"

Secondary actions:
- **REDUCE-NOMINALIZATIONS** — convert "the destruction of X" to "X was destroyed"
- **REPLACE-PARENTHETICALS** — move asides into separate main clauses
- **RESOLVE-GARDEN-PATHS** — add disambiguating cues for sentences that prime the wrong parse

Actions are STRENGTH-GRADED across the 5 levels: aggressive at very_basic; minimal at advanced; none at native (for general syntax).

### Level 1 — `very_basic`

**Reader profile.** A young child age 4–6 reading early-reader books, or a brand-new second-language learner in first weeks of immersion — someone who parses only SVO simple sentences with no embedding. Loses the thread on any coordination beyond minimal, any subordination, any marked word order.

Anchor demographic alternatives: child age 4–6 learning to read in L1; absolute-beginner L2 learner; L2 learner in first 1–2 weeks of immersion.

**Genre anchor.** Dr. Seuss / Eric Carle / picture-book prose / children's signs / early-reader instructional text.

**Structural-complexity tier:**
- Sentence-length (English-illustrative): ≤6 words/sentence
- Embedding depth: 0
- Suspension load: 0
- Word-order canonicality: canonical SVO only
- Center-embedding: N/A (0)

**Register/genre-tier.** Only children's signs + early-reader prose. Excludes coordination beyond minimal, subordination, nominalization, marked word orders.

**Restructuring-test sketch.** AGGRESSIVE. The translator SPLITS any compound sentence into separate sentences, UNEMBEDS any embedded clause, LINEARIZES any non-canonical word order, ADDS-CONNECTIVES to make all logic explicit, REDUCES-NOMINALIZATIONS.

**Positive examples** (sentences AT this level): "The cat sat." "The dog ran." "The man was tired." "The boy ate the apple." "The girl saw the bird."

**Negative examples** (sentences ABOVE this level): "The cat sat on the mat and looked around." (coordination — daily); "The man who came home was tired." (1 relative — daily); "Even though I was hungry, I went to bed." (subordination — daily / conversational).

### Level 2 — `daily`

**Reader profile.** A functional adult in daily life — a backpacker carrying out transactions in a foreign country, a new immigrant functioning in their second language, an L2 learner after a few months of in-country immersion. Parses coordinated sentences and simple relative clauses; loses the thread on multi-clause subordination, dense nominalization, marked word orders.

Anchor demographic alternatives: new immigrant functioning in L2; backpacker carrying out daily transactions; functional L2 learner after a few months in-country.

**Genre anchor.** Practical instruction manuals / simple news headlines / casual conversational prose / everyday signs and notices.

**Structural-complexity tier:**
- Sentence-length (English-illustrative): ≤15 words/sentence
- Embedding depth: ≤1 (one simple embedded clause max)
- Suspension load: ≤1 (short embedded element delaying main verb)
- Word-order canonicality: canonical SVO; minimal marked orders
- Center-embedding: 0

**Register/genre-tier.** Practical guides + simple news headlines + casual instructional + simple narrative. Excludes multi-clause subordination, parentheticals, marked word orders, dense nominalization, specialist.

**Restructuring-test sketch.** MODERATE. The translator SPLITS sentences longer than 15 words, ADDS-CONNECTIVES (replace implicit logic with explicit "because" / "however"), UNEMBEDS multi-level embeddings, REDUCES-NOMINALIZATIONS.

**Positive examples:**
- "The cat sat on the mat, and the dog ran outside."
- "The man who came home was tired."
- "I went home because I was hungry."
- "She bought a book that her friend recommended."
- "When it rained, we stayed inside."

**Negative examples** (above daily): "When the cat sat down, the dog ran outside because it heard a noise that frightened it." (multi-clause subordinate linear — conversational); "The argument, despite being couched in dense subordination, succeeds." (advanced).

### Level 3 — `conversational`

**Reader profile.** An average educated newspaper-reading adult who carries informed informal conversation. Parses multi-clause subordinate sentences that proceed LINEARLY (subordinate clauses don't suspend the main verb significantly; they appear AFTER the main clause or as left-branching). Loses the thread on nested subordination, deep parentheticals, suspended-thread structures, center-embedding.

Anchor demographic alternatives: high-school-educated adult with workplace literacy; competent second-language reader at upper-intermediate (CEFR B1–B2 syntax); casual reader of mainstream non-fiction.

**Genre anchor.** Mainstream journalism / popular non-fiction / well-written conversational prose / weekly magazine articles.

**Structural-complexity tier:**
- Sentence-length (English-illustrative): ≤25 words/sentence
- Embedding depth: ≤2 (subordinate clauses with simple embedded relatives)
- Suspension load: ≤2 (subordinate mostly AFTER main verb; short suspension acceptable)
- Word-order canonicality: canonical + common marked orders (topicalization, common inversions)
- Center-embedding: 0

**Register/genre-tier.** Mainstream journalism + popular non-fiction + well-written conversational prose. Excludes nested suspension, center-embedding, archaic word orders, dense parentheticals, specialist.

**Restructuring-test sketch.** LIGHT. The translator SPLITS only sentences longer than 25 words that contain dense embedding; avoids constructions with suspension greater than 2 clauses; keeps linear subordination and simple relative clauses without restructuring.

**Positive examples:**
- "When the cat sat down, the dog ran outside because it heard a noise that frightened it."
- "The man, who had just come home from a long day, was tired but content."
- "Even though the weather was cold, we decided to walk to the store after considering whether to drive instead."
- "The book that she bought from the shop where her brother works was exactly what she had been looking for."

**Negative examples** (above conversational): "The argument, despite being couched in the kind of dense subordination that requires the reader to hold three clauses in working memory before encountering the main verb, succeeds." (advanced — user's seed); "Whilst it cannot be denied that the man, who, having decided..., set forth at dawn..." (native).

### Level 4 — `advanced`

**Reader profile.** A university-educated reader, a skilled non-native who reads widely across academic and literary genres, or an educated professional. Parses nested subordination, parentheticals, and **up to 3-clause suspension before the main verb resolves**. Tolerates 1 center-embedding. Loses the thread on 2-deep center-embedding, 4+ clause suspension, archaic literary inversion, dialectal syntax, and subject-domain specialist syntactic conventions.

Anchor demographic alternatives: university-educated professional; humanities graduate student; skilled non-native reader of literary fiction; well-read amateur literary critic.

**Genre anchor.** Academic articles / contemporary literary fiction / well-written essays / dense argumentative prose / New Yorker-style longform.

**Structural-complexity tier:**
- Sentence-length (English-illustrative): ~25–40 words/sentence (no strict upper bound; complexity is the constraint)
- Embedding depth: ≤3 (nested subordination, parentheticals)
- Suspension load: ≤3 — the user's seed sentence is the anchor (3 clauses held before main verb resolves)
- Word-order canonicality: includes marked orders common in academic and literary register
- Center-embedding: ≤1 (one center-embedded relative clause)

**Register/genre-tier.** Academic articles + contemporary literary fiction + well-written essays + dense argumentative. Excludes 2-deep center-embedding, archaic word orders, 4+ clause suspension, specialist-domain syntactic conventions.

**Restructuring-test sketch.** MINIMAL. The translator avoids only center-embedding 2-deep or more; avoids suspension exceeding 3 clauses; keeps nested subordination, parentheticals, and marked academic / literary word orders without restructuring. May use technical vocabulary structures if they are general-educated (e.g., nominalized abstractions in philosophy) but NOT subject-domain specialist (see the A1↔A2 boundary section).

**Positive examples:**
- **(User's seed.)** "The argument, despite being couched in the kind of dense subordination that requires the reader to hold three clauses in working memory before encountering the main verb, succeeds."
- "The cat's decision to sit, prompted by an exhaustion that had built throughout the day, was met with relief by the dog who had been waiting outside."
- "What the researchers found, contrary to what conventional wisdom would predict, was that the intervention worked best when applied gradually rather than all at once."
- "His insistence that the procedure, though admittedly novel, would yield results comparable to those of established methods proved, in the end, to be vindicated."

**Negative examples** (above advanced):
- A1.native (2-deep center-embedding or 4+ clause suspension): "Whilst it cannot be denied that the man, who, having decided that he ought, despite his misgivings, to attempt the journey, set forth at dawn..." (Henry-James-style; native).
- A2 specialist legal: "Provided that the party of the first part, hereinafter referred to as the Lessor, shall..." (legal; A2).
- A2 specialist mathematical: "For all ε > 0, there exists δ > 0 such that |f(x) − L| < ε whenever 0 < |x − c| < δ." (mathematical; A2).

### Level 5 — `native`

**Reader profile.** An educated native speaker who reads broadly across literary registers including historical, archaic, and extreme-literary prose. Parses 2-deep center-embedding, 4+ clause suspension, archaic word orders (KJV-Pauline inverted constituent order), Faulkner stream-of-consciousness, late-Victorian deeply-nested literary prose. Does NOT necessarily parse subject-domain specialist syntactic conventions requiring field training (legal cross-reference structures; mathematical formal-statement syntax; medical-research nominalization-heavy passive with statistical notation) — those are A2 territory, NOT A1.

Anchor demographic alternatives: literature scholar / English-major academic; broadly-read native who enjoys archaic-syntax fiction (readers of Tolkien, the King James Bible, Shakespeare, Henry James); readers of late-Victorian and 18th-century English (Edward Gibbon-style).

**Genre anchor.** Henry James / Henry Adams / Faulkner / KJV-Pauline / late-Victorian literary prose / 18th-century English / archaic and literary-extreme prose.

**Structural-complexity tier:**
- Sentence-length (English-illustrative): unlimited
- Embedding depth: unlimited within general syntactic conventions
- Suspension load: 4+ allowed
- Word-order canonicality: includes archaic, dialectal, KJV-Pauline inverted, Faulkner stream-of-consciousness
- Center-embedding: ≤2 (Henry James / Henry Adams literary anchor; 3-deep breaks even for natives)

**Register/genre-tier.** Literary-extreme prose + archaic-literary + dense Victorian + KJV-Pauline + Faulkner stream-of-consciousness. Excludes ONLY A2 specialist-domain syntactic conventions (legal, mathematical, medical-research).

**Restructuring-test sketch.** NONE for general syntax. The translator preserves all general structures including 2-deep center-embedding, archaic word orders, 4+ clause suspension. ONLY A2 specialist-domain syntactic conventions are substituted, footnoted, or paraphrased — see the A1↔A2 boundary section.

**Positive examples:**
- Henry-James-style (2-deep center-embedding; 4+ clause suspension): "Whilst it cannot be denied that the man, who, having decided that he ought, despite his misgivings, to attempt the journey, set forth at dawn and encountered numerous obstacles, was perhaps unprepared, his eventual success, though qualified, was sufficient to vindicate his decision."
- KJV-Pauline archaic inversion: "Through Him to whom be glory, the work was done."
- Left-branching archaic with parenthetical participial: "What the man did, having done what he could, was return."

**Negative examples (A2 specialist syntax only):** "Provided that the party of the first part..." (legal); "For all ε > 0..." (mathematical); "Administration of the intervention (n = 142, mean age 54.3 ± 8.2 years) resulted in..." (medical-research).

### Adjacent-level boundary specs

#### Boundary 1 — `very_basic` ↔ `daily`

**Distinguishing principle.** Shift from SVO-only simple sentences (no embedding) to coordinated sentences and simple relative clauses (≤1 embedded clause).

**Sentence pairs** (low-side `very_basic` ↔ high-side `daily`):
- "The cat sat. The dog ran." ↔ "The cat sat on the mat, and the dog ran outside."
- "The man was tired." ↔ "The man who came home was tired."
- "I went home. I was hungry." ↔ "I went home because I was hungry."
- "The girl saw the bird." ↔ "The girl saw the bird that flew over the house."

#### Boundary 2 — `daily` ↔ `conversational`

**Distinguishing principle.** Shift from simple coordination + 1 simple relative to MULTI-CLAUSE SUBORDINATION proceeding linearly (subordinate clauses don't suspend main verb; embedding depth up to 2).

**Sentence pairs:**
- "I went home because I was hungry." ↔ "When the cat sat down, the dog ran outside because it heard a noise that frightened it."
- "The man who came home was tired." ↔ "The man, who had just come home from a long day, was tired but content."
- "We stayed inside because it rained." ↔ "Even though the weather was cold, we decided to walk to the store after considering whether to drive instead."

#### Boundary 3 — `conversational` ↔ `advanced`

**Distinguishing principle.** Shift from linear multi-clause subordination to NESTED SUBORDINATION + PARENTHETICALS + 3-CLAUSE SUSPENSION before the main verb resolves. The user's seed sentence is the high-side anchor.

**Sentence pairs:**
- "When the cat sat down, the dog ran outside because it heard a noise." ↔ "The cat's decision to sit, prompted by an exhaustion that had built throughout the day, was met with relief by the dog who had been waiting outside."
- "The argument succeeded after careful preparation." ↔ **(User's seed)** "The argument, despite being couched in the kind of dense subordination that requires the reader to hold three clauses in working memory before encountering the main verb, succeeds."

#### Boundary 4 — `advanced` ↔ `native`

**Distinguishing principle.** Shift from 1-deep embedding + 3-clause suspension to ALL GENERAL syntactic structures including 2-deep center-embedding, 4+ clause suspension, archaic word orders (KJV-Pauline inversion), Faulkner stream-of-consciousness.

**Sentence pairs:**
- Advanced (3-clause suspension; 1-deep): "The argument, despite being couched in dense subordination, succeeds."
- Native (4+ clause suspension; 2-deep center-embedding): "Whilst it cannot be denied that the man, who, having decided that he ought, despite his misgivings, to attempt the journey, set forth at dawn and encountered numerous obstacles, was perhaps unprepared, his eventual success, though qualified, was sufficient to vindicate his decision."
- Modern educated: "Through whom glory is due, the work was finished." ↔ KJV-Pauline native: "Through Him to whom be glory, the work was done."

### A1↔A2 boundary clarification for syntax

**The boundary test.** "Does parsing this sentence's STRUCTURE require subject-domain training, or only broad general reading?" Subject-domain training → A2. Broad reading → A1.

**Important note.** A1 covers all GENERAL syntactic structures across general registers including literary-extreme and archaic. Henry-James-style 2-deep center-embedding belongs at A1.native — broad literary-reading experience is enough. A2 covers SUBJECT-DOMAIN syntactic conventions requiring specific field training.

**Specialist-syntax example list:**

| Domain | Example | Why A2 |
|---|---|---|
| **Legal** | "Provided that the party of the first part, hereinafter referred to as the Lessor, shall, upon receipt of the consideration described in Section 3 herein, transfer to the party of the second part, hereinafter the Lessee, all rights, title, and interest in the property described in Schedule A hereto attached and made a part hereof." | Requires legal training to track "first part / second part" parallel structure and "hereinabove / herein / hereto" cross-reference conventions |
| **Legal** | "It is hereby ordered, adjudged, and decreed that the defendant, having been duly served with process and having failed to answer within the time prescribed by law, is found in default." | Documentary parataxis with formal triplet; A2 legal training required for the documentary register |
| **Mathematical** | "For all ε > 0, there exists δ > 0 such that \|f(x) − L\| < ε whenever 0 < \|x − c\| < δ." | Quantifier-conditional formal-statement structure (∀-∃-such-that); A2 mathematical training required for alternating quantifier scopes |
| **Mathematical** | "Let X be a topological space. A subset A of X is said to be open if, for every x in A, there exists an open neighborhood U of x such that U is contained in A." | Definition syntax with embedded quantifier-conditional; A2 mathematical training required |
| **Medical-research** | "Administration of the intervention (n = 142, mean age 54.3 ± 8.2 years) resulted in statistically significant (p < 0.01) improvement in primary endpoint measures, although secondary outcomes (Table 2) demonstrated heterogeneity across cohort subgroups." | Nominalization-heavy passive with parenthetical reference notation; A2 medical-research training required |
| **Medical-research** | "It was observed that, in the cohort under study, those subjects who, having received the standard treatment for a period of no less than six months, were subsequently exposed to the experimental intervention exhibited a statistically significant (p < 0.05) reduction in symptom severity." | Passive nominalization with nested subordinate clauses and parenthetical statistical notation; A2 training required |

**Cross-sub-field interaction note.** A sentence with GENERAL syntactic structure but SPECIALIST VOCABULARY (e.g., "The patient had a myocardial infarction.") is A1 syntax + A2 vocabulary. The A1↔A2 boundaries for syntax and vocabulary are SEPARATE — each sub-field carries its own boundary, and they don't need to align.

### Migration mapping from existing `AUDIENCE_LEVEL`

The existing `.env.example` knob `AUDIENCE_LEVEL` has 3 values (`native | late_learner | late_learner_simple`). The suggested mapping for syntactic-processing-capacity is parallel to vocabulary-breadth's mapping by design (same-labels-for-default-propagation):

| Existing | New (syntactic-processing-capacity) | Rationale |
|---|---|---|
| `late_learner_simple` | `daily` | Existing label captures readers needing simpler structures than ordinary late-learner level. Matches `daily` — functional adult handling simple coordination + ≤1 embedded clause but not multi-clause subordinate or Latinate academic patterns. |
| `late_learner` | `conversational` | Matches multi-clause subordinate linear syntax of educated newspaper-reading adults. `late_learner` is at upper-intermediate L2 reading; this matches the `conversational` syntactic-processing-capacity zone. |
| `native` | `native` | Direct identity mapping. Both refer to educated natives handling literary-extreme syntactic structures including 2-deep center-embedding. |

**New positions introduced:**
- `very_basic` extends BELOW `late_learner_simple` for children and brand-new L2 learners parsing only SVO simple sentences. The existing 3-level scheme could not address this profile.
- `advanced` fills the gap BETWEEN `late_learner` and `native` for university-educated readers and skilled non-natives who handle 3-clause suspension and 1-deep center-embedding but not 2-deep center-embedding or archaic literary inversion.

This mapping is SUGGESTED. The actual migration belongs in a separate inquiry.

## Inherited Commitments Re-test

This finding refines the prior `a1_vocabulary_breadth_levels` finding (the sibling sub-field), which itself refines `translation_config_axes`. Per CONCLUDE's synthesis re-test enforcement, the N ≥ 3 inherited commitments are listed and re-tested.

- **Commitment:** A1 Reader Level is a composite-axis with 5 sub-fields.
  - **Source:** `translation_config_axes/finding.md` — A1 Reader Level definition
  - **Re-test status:** RE-TESTED
  - **Evidence:** This finding instantiates the 2nd of the 5 sub-fields (syntactic-processing-capacity) parallel to vocabulary-breadth (the 1st). The composite-axis pattern is honored.

- **Commitment:** A1 measures RECEPTIVE capacity (recognition / parsing not production).
  - **Source:** `translation_config_axes/finding.md` — A1 receptive-only constraint
  - **Re-test status:** RE-TESTED
  - **Evidence:** Every level's prose phrased in reception verbs (parses / follows / does not lose the thread / does not parse). Verified by critique D2 scan.

- **Commitment:** A1 axis identity is language-agnostic at the concept level.
  - **Source:** `translation_config_axes/finding.md` — language-agnosticism statement
  - **Re-test status:** RE-TESTED
  - **Evidence:** Each level's structural-complexity tier annotates sentence-length as "English-illustrative." The CONCEPTS (gradient from simple to complex; working-memory load from embedding; canonical vs marked word order) are universal. Sensemaking SV6 Ambiguity 7 verified holds for non-SVO target languages (Japanese head-final; Russian flexible word order).

- **Commitment:** Same labels (`very_basic | daily | conversational | advanced | native`) across A1 sub-fields for clean default-propagation.
  - **Source:** `a1_vocabulary_breadth_levels/finding.md` — same-labels commitment
  - **Re-test status:** RE-TESTED
  - **Evidence:** This finding adopts the same 5 labels for syntactic-processing-capacity. Semantics differ per sub-field (vocabulary's `conversational` = newspaper-vocabulary; syntax's `conversational` = newspaper-syntax) but label strings match.

- **Commitment:** Conservative-bias for reader-facing axes = LOWER default level.
  - **Source:** `a1_vocabulary_breadth_levels/finding.md` — conservative-bias-for-reader-axes principle
  - **Re-test status:** RE-TESTED
  - **Evidence:** Applied to syntactic-processing-capacity (LOWER default = assume less parsing capacity; user dials UP). Specific default value deferred to defaults inquiry.

- **Commitment:** A1↔A2 boundary distinguishes general capacity from subject-domain-training-required capacity.
  - **Source:** `a1_vocabulary_breadth_levels/finding.md` — A1↔A2 boundary for vocabulary
  - **Re-test status:** RE-TESTED with EXTENSION
  - **Evidence:** Applied to syntax with the same test phrasing ("requires subject-domain training to parse"). EXTENSION: A1↔A2 boundaries for syntax and vocabulary are SEPARATE — sensemaking Ambiguity 6 confirmed that a sentence with general syntactic structure but specialist vocabulary (e.g., a clear sentence about `myocardial infarction`) is A1 syntax + A2 vocabulary.

- **Commitment:** The 4-component vocabulary-breadth template (reader-profile + frequency-tier + register-tier + substitution-test).
  - **Source:** `a1_vocabulary_breadth_levels/finding.md` — 4-component template
  - **Re-test status:** RE-TESTED with PRINCIPLED ADAPTATION
  - **Evidence:** Frequency-tier doesn't fit syntax (sentences don't have Zipfian frequency); replaced with structural-complexity tier (5 sub-measures). Register-tier reframed as register/genre-tier. Substitution-test renamed as restructuring-test with named primary actions. Sensemaking Ambiguities 1, 2, 3 verified each adaptation is principled. Critique D9 (Template-adaptation coherence) confirmed.

- **Commitment:** 4-layer framework architecture (USER-FACING AXES / POLICY / SOURCE-DESCRIPTION / SYSTEM-FLAGS).
  - **Source:** `translation_config_axes/finding.md` — 4-layer architecture
  - **Re-test status:** INHERITED-WITHOUT-RE-TEST
  - **Reason:** Out of scope for sub-field-level inquiry. The architecture is structural; this inquiry operates inside Layer 1 USER-FACING AXES.

- **Commitment:** POLICY layer items (register-alternation preservation, etc.) are always-on.
  - **Source:** `translation_config_axes/finding.md` — Layer 2 POLICY
  - **Re-test status:** INHERITED-WITHOUT-RE-TEST
  - **Reason:** Out of scope. Acknowledged interaction: register-preservation policy may interact with syntactic-processing-capacity at runtime (if source has high-register dense syntax and target reader is at conversational level, the policy and the axis may give conflicting signals; runtime conflict resolution deferred per the prior root finding).

## Next Actions

### MUST

- **What:** Define the 5 level values + per-level 4-component specs for each of the remaining 3 A1 sub-fields (idiom-recognition, inference-capacity, cultural-reference-recognition). Each sub-field may require its own template adaptation (idiom-recognition may use a "frequency-tier of idioms" component; inference-capacity may use a "compression-depth tier"; cultural-reference-recognition may use a "reference-density tier").
  - **Who:** the next 3 follow-up inquiries.
  - **Gate:** condition-bound — before A1 Reader Level can be fully instantiated as a typed composite-axis. Each sub-field follow-up applies the same shape as this and the vocabulary-breadth inquiry.
  - **Why:** without all 5 sub-fields' level specs, A1 Reader Level cannot be fully operationalized — the composite-axis pattern requires all sub-fields to share the same 5 labels with their own semantics.

### COULD

- **What:** Define per-language structural-complexity thresholds for syntactic-processing-capacity. English-illustrative thresholds (≤6 / ≤15 / ≤25 / ~25–40 / unlimited words/sentence; embedding depth 0 / 1 / 2 / 3 / unlimited; suspension load 0 / 1 / 2 / 3 / 4+; center-embedding 0 / 0 / 0 / 1 / 2) need per-language equivalents. SOV languages (Japanese head-final) have different embedding dynamics; flexible-word-order languages (Russian) have different marked-vs-canonical distinctions; the CONCEPT (gradient) translates, the specifics are per-language.
  - **Who:** a per-language inquiry.
  - **Gate:** condition-bound — when Comprehenslate adds the target language.
  - **Why:** runtime restructuring decisions depend on per-language thresholds.
  - **Depends-on:** MUST item "Define the 5 level values for the remaining 3 A1 sub-fields." Per-language inquiries are best run AFTER all A1 sub-fields are specified for English.

- **What:** Define the specific conservative-bias default value for syntactic_processing_capacity (`daily` or `conversational`?).
  - **Who:** the defaults inquiry.
  - **Gate:** condition-bound.
  - **Why:** the principle (LOWER default) is settled; the specific level is calibration-dependent.

- **What:** Define the Purpose-driven default-derivation for syntactic-processing-capacity (which A4 Purpose value pulls toward which syntactic-processing level by default).
  - **Who:** the defaults inquiry.
  - **Gate:** condition-bound.
  - **Why:** the 2-tier default principle requires Purpose-driven mapping.

### DEFERRED

- **What:** Implement the runtime restructuring mechanism (LLM-judged vs parser-backed metrics).
  - **Gate:** revival when level enums committed to pydantic and translator-AI runtime begins consuming them.
  - **Why (if revived):** initial implementation can be LLM-judged using per-level prose + example sentences as anchor context; later parser-based metrics (Yngve depth, dependency length) can supplement.

- **What:** Translate the 5 levels into the pydantic dataclass `syntactic_processing_capacity: Literal[...]` field nested inside A1's composite-axis.
  - **Gate:** revival when structural-layer inquiry begins.
  - **Why (if revived):** structural-layer artifact.

- **What:** Implement the migration from existing `AUDIENCE_LEVEL` to the new `syntactic_processing_capacity` (alongside `vocabulary_breadth` and other A1 sub-fields).
  - **Gate:** revival when production systems wire up the new axis.
  - **Why (if revived):** migration cutover plan is operational.

## Reasoning

### What survived

The Final Recommended Assembly (Assembly E2 from critique) survives all 11 evaluation dimensions: Correctness (CRITICAL), Receptive-only discipline (CRITICAL), Language-agnostic at concept (CRITICAL), Mutually-distinct ordinal levels (CRITICAL), A1↔A2 boundary respect for syntax (CRITICAL), Sensemaking SV6 consistency (HIGH), Operationalizability (HIGH), Example correctness (CRITICAL), **Template-adaptation coherence (HIGH; NEW project-specific risk axis for this inquiry)**, Project-value-fit (MEDIUM), Scope-discipline (MEDIUM).

One minor format refinement note was incorporated: the structural-complexity tier inside each level's spec is presented as a labeled list of sub-measures (not running prose) for both human-readability and LLM-anchor-extraction clarity.

### Significant alternatives rejected

- **Blindly copying vocabulary-breadth's 4-component template** (keeping frequency-tier, register-tier, substitution-test names). Rejected at sensemaking Ambiguities 1, 2, 3: sentences don't have Zipfian frequency (frequency-tier inappropriate); register and syntactic complexity correlate but aren't identical (register-tier needs reframing); the runtime action for syntax is restructuring, not substitution. Each component was REPLACED or REFRAMED with rationale.

- **Skipping the restructuring-test analogue.** Rejected at sensemaking Ambiguity 3: the substitution-test was load-bearing in vocabulary-breadth as the RUNTIME ACTION CONCEPT. For syntax, naming the actions explicitly (SPLIT / UNEMBED / LINEARIZE / ADD-CONNECTIVES) preserves template symmetry and gives the translator-AI clear runtime guidance.

- **Collapsing daily and conversational into one level.** Rejected at sensemaking: daily = simple coordination + 1 simple relative (≤15 words); conversational = multi-clause subordinate linear (≤25 words, embedding ≤2). Distinct reader profiles (backpacker functioning in daily life vs newspaper-reading educated adult) and distinct restructuring actions.

- **Placing center-embedding 2-deep at conversational↔advanced.** Rejected at sensemaking Ambiguity 4: psycholinguistic research and literary practice (Henry James, Henry Adams use 2-deep routinely) support placing 2-deep at advanced↔native. Advanced readers tolerate 1-deep; native readers tolerate 2-deep; 3-deep breaks for all.

- **Treating literary-extreme syntax (Henry James, KJV) as A2.** Rejected at sensemaking Ambiguity 6: Henry-James-style sentences require only broad literary-reading EXPERIENCE, not subject-domain TRAINING. They belong at A1.native. A2 covers subject-domain-training-required structures (legal cross-reference; mathematical formal-statement; medical-research nominalization-heavy passive).

- **Productive-vocabulary framing in level definitions.** Rejected at sensemaking Ambiguity 8 (inherited from prior chain): the A1 commitment is RECEPTIVE only. All prose uses "parses" / "follows" / "recognizes when encountered."

- **Sentence-length alone as the defining axis.** Rejected at sensemaking Ambiguity 1: a long coordinated sentence is COMMON and EASY; a short densely-embedded sentence is RARE and HARD. The structural-complexity tier umbrella captures multiple sub-measures (length + depth + suspension + word-order + center-embedding).

- **Different labels per A1 sub-field.** Rejected (inherited from prior chain): the composite-axis pattern requires the same 5 labels across sub-fields for clean default-propagation. Same strings; sub-field-specific semantics.

- **Conservative-bias = HIGHER default for reader-facing axes.** Rejected (inherited): for reader-facing axes, conservative-bias means assume LESS reader competence; default to LOWER level; user dials UP.

### Why the template adaptation was principled, not arbitrary

The vocabulary-breadth template was designed for word-level recognition. For sentence-level parsing, three of the four components don't translate directly:

**Frequency-tier doesn't apply.** Sentences don't follow Zipfian frequency distributions the way words do. While SOME structures appear more frequently than others in corpora, frequency and parsing-difficulty correlate WEAKLY at the sentence level (a long coordinated sentence is common and easy; a center-embedding is rare and hard). The right dimension is COGNITIVE COMPLEXITY, captured by the structural-complexity tier's 5 sub-measures.

**Register-tier needs reframing.** Register correlates with syntactic complexity (academic register is more hypotactic) but isn't identical — different genres at similar complexity use different syntactic profiles. The reframed register/genre-tier captures both register and writing-genre, helping the user identify their target reader concretely.

**Substitution-test is a vocabulary-runtime concept.** Lexical substitution (`purchase → buy`) is appropriate for vocabulary-breadth. For syntactic-processing-capacity, the runtime translator action is STRUCTURAL RESTRUCTURING (SPLIT, UNEMBED, LINEARIZE, ADD-CONNECTIVES). The parallel naming (substitution-test ↔ restructuring-test) preserves template symmetry while reflecting the genuinely different runtime actions.

The adaptation pattern (replace components that don't fit; rename to reflect actual semantics; preserve template symmetry where possible) provides a template-adaptation template for the next 3 sub-field inquiries (idiom-recognition / inference-capacity / cultural-reference-recognition), each of which may need its own adaptations.

## Open Questions

### Refinement Triggers

- **Per-level positive-sentence anchor refinement.** If the translator-AI runtime LLM consistently mis-judges a specific anchor sentence's level, the anchor should be revisited. Trigger: observable — when 5+ runtime LLM judgments diverge from spec classification for the same sentence.

- **5-level cardinality re-evaluation.** If real-user feedback shows users cluster at 2–3 of the 5 levels for syntactic-processing-capacity, cardinality may collapse. Trigger: condition-bound — after first 30 real configurations.

- **A1↔A2 boundary for syntax extension.** As the translator-AI encounters borderline syntactic patterns not in the specialist-syntax table (e.g., technical-writing style in software documentation; academic-philosophy syntactic conventions), additions warranted.

### Research Frontiers

- **Per-language register-tier dynamics for syntax.** English Latinate/Germanic register split affects vocabulary primarily; for syntax, the relevant analogue is academic-vs-conversational register. Other languages have different dynamics — Japanese has yamato vs Sino-Japanese vs katakana-borrowed registers with distinct syntactic profiles; Arabic has MSA vs Classical vs colloquial; Russian has Slavic vs Church-Slavonic. A future per-language inquiry maps each language's register-tier syntactic dynamics.

- **Productive vs receptive parsing capacity divergence.** Some non-native readers parse complex syntax better than they produce it; others parse simple syntax fluently but produce complex syntax with effort. The current spec assumes the standard receptive ≥ productive asymmetry. Edge cases observed in second-language acquisition research; not actionable now.

### Monitoring

- **Existing AUDIENCE_LEVEL usage.** The suggested migration mapping presupposes existing labels are used as semantically intended. If usage telemetry shows different interpretations, the mapping needs revision. Trigger: observable — when migration inquiry begins.

### Blocked

- **Default value selection.** Specific conservative-bias default value for syntactic_processing_capacity (`daily` or `conversational`) cannot be answered without the defaults inquiry running (which covers all 8 axes' defaults jointly).

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
now can we do the same for syntactic-processing-capacity — how dense a sentence structure the reader can parse without losing the thread (long nested clauses, multi-clause subordination, etc.). ?
```

</details>
