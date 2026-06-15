---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md
---
# Finding: a1_vocabulary_breadth_levels

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md`

**Revision trigger:** Continuation — the prior finding's MUST action #1 said "Define the level values (the enum strings + per-level prose descriptions) for each of the 8 axes." This inquiry takes the first step of that MUST by defining the 5 ordinal levels for A1 Reader Level's **vocabulary-breadth** sub-field.

**What's preserved:**
- A1 Reader Level identity as a composite-axis with 5 sub-fields
- vocabulary-breadth as one of those 5 sub-fields with the prior finding's definition ("how many words the reader recognizes; passive vocabulary")
- The 4-layer framework architecture
- The 8-axis structure in 4 families
- The receptive-only commitment for A1 (recognition not production)
- Language-agnosticism at the concept level
- The composite-axis pattern's default-propagation mechanism
- All POLICY-layer commitments

**What's changed:** Nothing in the prior finding's structural commitments is altered. This finding ADDS specification at the sub-field-level enum-values layer that the prior finding deferred.

**What's new:**
- 5 named ordinal levels for vocabulary-breadth: `very_basic | daily | conversational | advanced | native`
- A per-level **4-component definition template** (reader-profile + frequency-tier band + register-tier inclusion + substitution-test sketch)
- Per-level positive + negative anchor examples (English-illustrative)
- 4 adjacent-level boundary specs with distinguishing principles and word-pair examples
- An explicit **A1↔A2 boundary clarification** (general vocabulary vs subject-domain specialist) with a 20-entry borderline-words table
- A **suggested migration mapping** from the existing `AUDIENCE_LEVEL` knob in `.env.example`
- A **conservative-bias-for-reader-axes principle clarification**: for reader-facing axes, conservative-bias means LOWER default (assume less reader competence; user dials UP)

**Migration:** No production system has yet implemented `vocabulary_breadth` as a typed field. This finding produces the design that future pydantic / schema work will instantiate. The existing 3-level `AUDIENCE_LEVEL` knob can continue to operate alongside; the suggested mapping (`late_learner_simple → daily`; `late_learner → conversational`; `native → native`) provides a clean translation when the new axis is wired up.

## Question

**Context.** The prior `translation_config_axes` inquiry (path above) defined A1 Reader Level as a **composite-axis** — one user-facing axis whose headline level the user sets, with 5 sub-fields (vocabulary-breadth, syntactic-processing-capacity, idiom-recognition, inference-capacity, cultural-reference-recognition) each optionally overridable. The prior finding committed to ~5 headline levels for A1 but deferred the actual level VALUES + per-level meanings to a follow-up inquiry. This inquiry is that follow-up, scoped to **one sub-field only**: vocabulary-breadth.

**The question.** For the vocabulary-breadth sub-field of A1 Reader Level, what should the 5 ordinal levels be — what concept does each level capture, what logic distinguishes each level from its neighbors, and what concrete examples make each level operationally identifiable — defined language-agnostically at the concept level (with English examples allowed for illustration)?

**Goal.** Produce 5 mutually-distinct, ordinally-meaningful, spectrum-covering levels — each operationalizable as a prompt instruction for the translator-AI, each with explicit distinguishing logic, each language-agnostic at the concept level. The user will commit the levels as the `vocabulary_breadth: Literal[...]` enum values in the pydantic schema (next-step work), pass the per-level prose to the translator-AI's prompt context, and use the boundary information at runtime to decide vocabulary substitution choices.

**Scope.** Vocabulary-breadth ONLY. The other 4 A1 sub-fields (syntactic-processing-capacity, idiom-recognition, inference-capacity, cultural-reference-recognition) will be handled in their own follow-up inquiries with the same shape.

## Finding Summary

- **The 5 level names match the user's seed:** `very_basic | daily | conversational | advanced | native`. These are reader-profile labels (user-evocative, not abstract framework labels like CEFR's A1–C2). The same 5 labels apply across all A1 sub-fields for clean default-propagation from the A1 headline level (each sub-field carries its own semantics for those labels).

- **Each level has a 4-component definition.** Component 1 = reader-profile name with anchor demographics. Component 2 = frequency-tier band (English-illustrative; concept is universal). Component 3 = register-tier inclusion (which sociolinguistic registers — everyday / journalistic / academic / literary / archaic — the level includes, with explicit exclusions). Component 4 = substitution-test sketch (the runtime action: what kind of words the translator avoids at this level, with concrete example substitutions like `purchase` → `buy`).

- **`very_basic` — small child or brand-new second-language learner.** Recognizes only the core ~500–1000 most-frequent words (function words + everyday concrete nouns and verbs). Translator replaces almost everything outside this band with descriptive paraphrase. CEFR ≈ A1.

- **`daily` — functional adult in daily life.** A backpacker, a new immigrant, an L2 learner who has been in-country a few months. Recognizes ~2000–3000 most-frequent words including everyday concrete and simple abstract; does not recognize Latinate ("purchase"), academic ("endeavor"), literary, archaic, or specialist vocabulary. CEFR ≈ A2–B1.

- **`conversational` — average educated newspaper-reader.** Carries informed informal conversation comfortably. Recognizes ~5000–7000 words including common Latinate (`purchase`, `endeavor`, `consider`, `approximately`); does not handle dense academic, literary-archaic, or specialist registers. CEFR ≈ B1–B2.

- **`advanced` — university-educated reader / skilled non-native who reads widely.** Recognizes ~10000–20000 words including academic (`ratiocination`, `epistemic`, `contingent`) and general literary (`ineffable`, `putative`, `ostensibly`). Does not necessarily recognize archaic forms (`verily`, `anon`, `whilom`), dialectal vocabulary, or subject-domain specialist (`myocardial infarction`, `habeas corpus`). CEFR ≈ B2–C1.

- **`native` — educated native speaker who reads broadly across registers.** Recognizes the full general vocabulary including archaic (`verily`, `anon`, `whilom`, `thee`, `withal`), dialectal forms in fiction, and literary-rare general words. Does NOT recognize subject-domain specialist vocabulary requiring field training — those belong to A2 Domain Expertise, not A1 vocabulary-breadth. CEFR ≈ C2+.

- **The A1↔A2 boundary is explicit:** A1 vocabulary-breadth covers GENERAL vocabulary at all registers (including archaic and literary). A2 Domain Expertise covers SUBJECT-DOMAIN specialist vocabulary (medical, legal, theological-specialist, scientific-specialist). The boundary test: "does recognizing this word require subject-domain training, or only broad general reading?" `ratiocination` is A1 (Latinate but general — appears in literary writing). `myocardial infarction` is A2 (requires medical training). A 20-entry borderline-words table in the body classifies edge cases like `eschatology` (A2 theology / A1.native for broad readers), `entropy` (A1.advanced for commonsense / A2 physics for technical), and `epistemology` (A2 philosophy / A1.native borderline).

- **Boundary pairs make adjacent-level transitions concrete.** For each of the 4 adjacent boundaries, 5 word-pair examples illustrate the shift: `go ↔ decide` (very_basic ↔ daily, core/function → functional-everyday); `buy ↔ purchase` (daily ↔ conversational, Germanic-everyday → Latinate-educated); `apparently ↔ ostensibly` (conversational ↔ advanced, conversational-educated → written-academic); `truly ↔ verily` (advanced ↔ native, modern-educated → archaic).

- **Conservative-bias for reader-facing axes = LOWER default level.** For axes describing the reader (A1, A2, A3), conservative-bias means assume LESS reader competence — default to a LOWER level (so the translation is more accessible); the user dials UP if the actual reader is more advanced. This is the opposite of conservative-bias for strategy-side axes (A5, A6, A7) where conservative-bias = preserve more. The specific default value for vocabulary-breadth (`daily` vs `conversational`) is deferred to the defaults inquiry.

- **Migration from the existing 3-level `AUDIENCE_LEVEL` knob is suggested:** `late_learner_simple → daily`; `late_learner → conversational`; `native → native`. Two new positions extend the spectrum: `very_basic` (below `late_learner_simple`, for children / brand-new learners) and `advanced` (between `late_learner` and `native`, for university-educated / skilled non-native readers). This is a suggested mapping; the actual migration belongs in a separate inquiry.

- **What's deferred to future inquiries.** Per-language frequency-band thresholds (what counts as "top ~5000 words" in Russian, Japanese, Arabic). Specific default value for vocabulary-breadth (`daily` or `conversational` for conservative-bias). The other 4 A1 sub-fields (each needs its own inquiry, of the same shape as this one). Runtime substitution mechanism (LLM-judged vs frequency-list-backed). Pydantic dataclass shape including the `vocabulary_breadth: Literal[...]` field. Default-derivation mechanism from A4 Purpose to the A1 sub-fields.

## Finding

### How to read this finding

The inquiry's deliverable is a per-level **specification** ready to commit to the pydantic schema and to the translator-AI's prompt context. The body below presents:

1. **Cross-cutting framing constraints** that apply to all 5 levels — the receptive-only commitment, the language-agnosticism claim, the same-labels-for-default-propagation note, the substitution-test runtime concept.
2. **The 4-component definition template** that each level instantiates.
3. **Each of the 5 levels** in its own subsection.
4. **The 4 adjacent-level boundary specs** with principles and word-pair examples.
5. **The A1↔A2 boundary clarification** with the test and a borderline-words table.
6. **The suggested migration mapping** from the existing `AUDIENCE_LEVEL` knob.

### Cross-cutting framing constraints (applies to all 5 levels)

- **Receptive only.** Every level description specifies what the reader RECOGNIZES when encountered (passive vocabulary), not what the reader CAN PRODUCE (active vocabulary). The asymmetry between receptive and productive vocabulary is roughly 2–3× in typical readers (people understand more words than they actively use). For translation purposes only reception matters — the reader consumes the translation; they do not produce it. Phrases like "uses this vocabulary," "speaks at this level," or "writes at this level" never appear in the spec for that reason.

- **Language-agnostic at the concept level.** Every level's CONCEPT (frequency tier, register tier, substitution behavior) is universal — every natural language has high-frequency vs low-frequency vocabulary, every language has sociolinguistic register tiers, every language has archaic forms. The English examples in this finding are ILLUSTRATIVE — concrete anchor cases that ground the concept. The actual frequency thresholds and register lexicons for any specific target language (Russian, Japanese, Arabic) belong to a per-language inquiry.

- **Same 5 labels across all A1 sub-fields.** A1 Reader Level is a composite-axis (per the prior finding) with 5 sub-fields. When the user sets A1=`conversational`, vocabulary-breadth defaults to `conversational`. For clean default-propagation, all 5 A1 sub-fields use the same 5 label strings (`very_basic | daily | conversational | advanced | native`). The label semantics differ per sub-field — `conversational` for vocabulary-breadth means "recognizes ~5000–7000 words including common Latinate," while `conversational` for idiom-recognition (defined in a future inquiry) will mean "recognizes most common idioms in casual speech." The strings match; the meanings are sub-field-specific.

- **Substitution-test runtime concept (not implementation).** At level L, the translator-AI replaces words above L with equivalents at or below L. For example, at `daily`, the translator replaces `purchase` (Latinate-conversational) with `buy` (Germanic-daily); at `conversational`, the translator keeps `purchase` but replaces `ratiocination` (advanced-academic) with `reasoning`. The CONCEPT is captured per-level in the substitution-test sketch below. The IMPLEMENTATION (whether the translator-AI uses an LLM judgment, a frequency list, or both) is deferred to a future runtime inquiry.

- **Conservative-bias for reader-facing axes means LOWER default level.** For axes that describe the reader (A1, A2, A3), the conservative bias is to assume LESS competence — default to a lower level (so the translation is more accessible). The user can always dial UP if their actual reader is more advanced. The opposite direction holds for strategy-side axes (A5 Source Fidelity, A6 Form Preservation, A7 Scaffolding), where conservative-bias means PRESERVE MORE (default to HIGHER preservation strength). The specific conservative-bias default value for vocabulary-breadth (whether `daily` or `conversational`) belongs to the defaults inquiry.

### The 4-component definition template

Each of the 5 levels follows this 4-component shape:

1. **Reader profile (with anchor demographics).** One sentence describing the typical reader at this level. Drawn from real, recognizable demographics — a small child, a backpacker, a newspaper-reading adult, a university-educated professional, an educated native who reads literary fiction. Plus 1–2 alternative demographic anchors for users whose target reader doesn't quite match the primary.

2. **Frequency tier (English-illustrative).** The Zipfian frequency band the reader is comfortable with. Expressed as "top ~N most-frequent words" where N is illustrative for English. The CONCEPT (Zipfian frequency tier) is universal; the specific N varies per target language.

3. **Register tier (inclusion + exclusion).** Which sociolinguistic registers the level includes (everyday / colloquial / journalistic / academic / literary / archaic) and which it excludes. Both inclusion and exclusion are stated explicitly so the LLM has clear membership boundaries.

4. **Substitution-test sketch.** What the translator does at runtime: which kinds of words it avoids, with concrete example substitutions. This component is the most operationally load-bearing — it tells the translator-AI what to actually do.

### Level 1 — `very_basic`

**Reader profile.** A young child reading early-reader books, or a brand-new second-language learner in their first weeks — someone who recognizes only the most everyday core vocabulary of the target language: function words, basic verbs, and the most common concrete nouns. Does not recognize Latinate, abstract, academic, literary, archaic, or specialist vocabulary.

Anchor demographic alternatives: child age 4–6 learning to read in L1; absolute-beginner L2 learner; L2 learner in their first 1–2 weeks of immersion.

**Frequency tier (English-illustrative).** Top ~500–1000 most-frequent words. Roughly CEFR A1.

**Register tier.** Only everyday core. Excludes Latinate, abstract, academic, literary, archaic, and specialist.

**Substitution-test sketch.** The translator replaces almost everything above the core band with descriptive paraphrase or simpler equivalents. `consider` becomes `think about`; `decision` becomes `what to do`; `purchase` becomes `buy`.

**Positive examples (words AT this level).** Function: `the`, `is`, `has`, `do`, `of`. Content: `go`, `eat`, `work`, `house`, `food`, `water`, `person`.

**Negative examples (words ABOVE this level).** `consider`, `decision`, `approximate`, `apparently`, `ratiocination`.

### Level 2 — `daily`

**Reader profile.** A functional adult in daily life — a backpacker carrying out transactions in a foreign country, a new immigrant functioning in their second language, an L2 learner who has been in-country a few months. Recognizes vocabulary in simple signs, instructions, and casual conversation; does not recognize Latinate, academic, literary, archaic, or specialist register.

Anchor demographic alternatives: new immigrant functioning in their second language; casual L2 learner who has been in-country a few months.

**Frequency tier (English-illustrative).** Top ~2000–3000 most-frequent words. Roughly CEFR A2–B1.

**Register tier.** Everyday concrete + simple abstract. Excludes Latinate (`purchase`, `endeavor`, `consider`), academic, literary, archaic, and specialist.

**Substitution-test sketch.** The translator replaces Latinate alternatives with Germanic everyday equivalents. `purchase` becomes `buy`; `endeavor` becomes `try`; `ostensibly` becomes `seemingly` or `it looks like`; `consider` becomes `think about`.

**Positive examples.** `decide`, `remember`, `carry`, `important`, `problem`, `simple`, `difficult`, `understand`, `area`.

**Negative examples.** `purchase`, `endeavor`, `consider`, `ostensibly`, `ratiocination`.

### Level 3 — `conversational`

**Reader profile.** An average educated adult who carries informed informal conversation and reads newspapers and mainstream non-fiction comfortably. Recognizes common Latinate vocabulary in educated speech (`purchase`, `consider`, `endeavor`, `approximately`) but does not read dense academic prose or literary-archaic vocabulary.

Anchor demographic alternatives: a high-school-educated adult with workplace literacy; a competent second-language reader at upper-intermediate level (CEFR B1–B2).

**Frequency tier (English-illustrative).** Top ~5000–7000 words including common Latinate. Roughly CEFR B1–B2.

**Register tier.** Everyday + conversational-educated + journalistic. Includes common Latinate. Excludes dense academic (`ratiocination`, `ostensibly`), literary-archaic (`verily`, `anon`), dialectal, and specialist.

**Substitution-test sketch.** The translator keeps common Latinate without substitution but avoids dense academic, archaic, dialectal, and specialist vocabulary. `ratiocination` becomes `reasoning`; `ostensibly` becomes `apparently`; `verily` becomes `truly`.

**Positive examples.** `purchase`, `endeavor` (high-end of conversational; appears in newspaper register), `consider`, `approximately`, `apparently`, `generally`, `decision`, `essential`, `establish`.

**Negative examples.** `ostensibly`, `ratiocination`, `ameliorate`, `verily`, `whilom`.

### Level 4 — `advanced`

**Reader profile.** A university-educated reader, a skilled non-native who reads widely across academic and literary genres, or an educated professional. Recognizes academic vocabulary (`ratiocination`, `epistemic`, `contingent`) and general literary vocabulary (`ineffable`, `putative`, `ostensibly`). Does not necessarily recognize archaic forms (`verily`, `anon`, `whilom`), dialectal vocabulary, or subject-domain specialist vocabulary (`myocardial infarction`, `habeas corpus`) — these are A2 Domain Expertise territory, not A1 vocabulary-breadth.

Anchor demographic alternatives: a skilled non-native reader of literary fiction; a humanities graduate student or well-read amateur literary critic.

**Frequency tier (English-illustrative).** Top ~10000–20000 words including academic and literary. Roughly CEFR B2–C1.

**Register tier.** Everyday + conversational + journalistic + academic + general literary. Excludes archaic, dialectal, and specialist-rare general.

**Substitution-test sketch.** The translator avoids only archaic (`verily` → `truly`, `anon` → `soon`), dialectal, and specialist-rare general vocabulary. Academic and literary register is kept. The translator may use technical vocabulary if it is general-educated (`hypothesis`, `epistemic`) but not subject-domain specialist (see the A1↔A2 boundary section).

**Positive examples.** `ratiocination`, `ostensibly`, `ameliorate`, `contingent`, `putative`, `ineffable`, `epistemic`, `prescient`. (Note: `hermetic` was considered as a positive example but is context-dependent — used non-occultly it is advanced general; used in its esoteric sense it leans A2. If the user prefers a less context-dependent advanced word, `recondite` substitutes cleanly.)

**Negative examples.**
- A1.native vocabulary above advanced: `verily`, `anon`, `whilom`.
- A2 specialist (here to clarify the boundary applies at this level): `myocardial infarction`, `transubstantiation`.

### Level 5 — `native`

**Reader profile.** An educated native speaker who reads broadly across genres including literary fiction, historical texts, and rare literary registers. Recognizes archaic vocabulary (`verily`, `anon`, `whilom`, `thee`, `withal`), dialectal forms encountered in fiction, and literary-rare general vocabulary. Does NOT necessarily recognize subject-domain specialist vocabulary requiring field training (`myocardial infarction`, `habeas corpus`, `transubstantiation` — these are A2 territory, not A1).

Anchor demographic alternatives: a literature scholar or English-major academic; a broadly-read native speaker who enjoys archaic-language fiction (readers of Tolkien, the King James Bible, Shakespeare).

**Frequency tier (English-illustrative).** Full general vocabulary (no upper bound on rarity within the general lexicon). Roughly CEFR C2+.

**Register tier.** All general registers including archaic, dialectal, literary-rare.

**Substitution-test sketch.** The translator avoids ONLY A2 specialist domain vocabulary (medical, legal, theological-specialist). All general vocabulary including archaic and dialectal is kept — `verily` stays as `verily`; `anon` stays as `anon`. The A1↔A2 boundary (see that section) determines when to substitute or footnote specialist vocabulary.

**Positive examples.** `verily`, `anon`, `thee`, `whilom`, `gainsay`, `withal`, `perchance`, `forsooth`, `wherefore`.

**Negative examples (A2 specialist domain vocabulary).** `myocardial infarction` (medical), `habeas corpus` (legal), `transubstantiation` (Catholic theology), `kenosis` (Christian theology), `ontogenesis` (biology).

### Adjacent-level boundary specs

Each of the 4 boundaries between adjacent levels has a distinguishing principle and 3–5 word-pair examples.

#### Boundary 1 — `very_basic` ↔ `daily`

**Distinguishing principle.** Shift from CORE / FUNCTION vocabulary (universally needed for basic communication) to FUNCTIONAL EVERYDAY content vocabulary (used by an adult to navigate daily life).

**Word pairs** (low-side `very_basic` ↔ high-side `daily`):
- `go` ↔ `decide`
- `food` ↔ `meal`
- `work` ↔ `job`
- `house` ↔ `apartment`
- `tell` ↔ `explain`

The high-side word is recognizable to a functional adult in daily life but not to a brand-new learner.

#### Boundary 2 — `daily` ↔ `conversational`

**Distinguishing principle.** Shift from FUNCTIONAL EVERYDAY register to EDUCATED-INFORMAL register (common Latinate vocabulary enters).

**Word pairs** (low-side `daily` ↔ high-side `conversational`):
- `buy` ↔ `purchase`
- `try` ↔ `endeavor`
- `think about` ↔ `consider`
- `about` ↔ `approximately`
- `clearly` ↔ `apparently`

The high-side word is recognizable to a newspaper-reading educated adult but not to a backpacker-level functional speaker.

#### Boundary 3 — `conversational` ↔ `advanced`

**Distinguishing principle.** Shift from CONVERSATIONAL-EDUCATED register to WRITTEN-EDUCATED register (academic and literary vocabulary enters).

**Word pairs** (low-side `conversational` ↔ high-side `advanced`):
- `apparently` ↔ `ostensibly`
- `reasoning` ↔ `ratiocination`
- `improve` ↔ `ameliorate`
- `depending on` ↔ `contingent on`
- `supposed` ↔ `putative`

The high-side word is recognizable to a university-educated reader but not to a typical newspaper reader.

#### Boundary 4 — `advanced` ↔ `native`

**Distinguishing principle.** Shift from MODERN EDUCATED vocabulary to ALL GENERAL vocabulary including archaic, dialectal, and rare-but-general.

**Word pairs** (low-side `advanced` ↔ high-side `native`):
- `truly` ↔ `verily`
- `soon` ↔ `anon`
- `you` (modern 2nd-person) ↔ `thee` (archaic 2nd-person singular object form; e.g., "I love thee" for "I love you")
- `formerly` ↔ `whilom`
- `also` ↔ `withal`

The high-side word is archaic, dialectal, or literary-rare general; a skilled non-native or modern educated reader may not recognize it, but an educated native reading literary or historical texts does.

### A1↔A2 boundary clarification

**The boundary test.** "Does recognizing this word require subject-domain training, or only broad general reading?" If subject-domain training is required, the word is A2 (Domain Expertise). If broad general reading is enough, the word is A1 (vocabulary-breadth).

**Important note.** A1 covers GENERAL vocabulary at ALL registers — everyday, colloquial, journalistic, academic, general literary, AND archaic. Archaic vocabulary like `verily`, `anon`, `whilom`, `thee` belongs at A1.native (a broadly-read native speaker recognizes these from literary and historical reading). Subject-domain specialist vocabulary like `myocardial infarction`, `habeas corpus`, `transubstantiation` belongs at A2 (requires medical / legal / Catholic-theology training respectively).

**Borderline-words table.** The following 20 words illustrate edge cases:

| Word | Classification | Reasoning |
|---|---|---|
| `ratiocination` | A1.advanced | General Latinate from rhetoric/logic; no domain training; appears in literary writing |
| `ostensibly` | A1.advanced | General Latinate; common in educated writing |
| `ameliorate` | A1.advanced | General Latinate; literary and policy-discussion vocabulary |
| `contingent` | A1.advanced | General academic; cross-disciplinary |
| `epistemic` | A1.advanced | Borderline; appears in non-specialist philosophy writing and general "epistemic humility"-type usage |
| `verily` | A1.native | Archaic general; King James Bible-era English; recognized by literary-fiction readers |
| `anon` | A1.native | Archaic general |
| `whilom` | A1.native | Archaic literary; recognized by historical-fiction readers |
| `thee`, `thou`, `thy` | A1.native | Archaic pronouns; Shakespeare, KJV |
| `gainsay`, `withal`, `perchance` | A1.native | Archaic literary general |
| `eschatology` | A2 theology (A1.native for unusually broad readers) | Mostly theology specialist; well-read general readers may know it |
| `transubstantiation` | A2 Catholic theology specialist | Requires Catholic-theology training |
| `myocardial infarction` | A2 medical specialist | Requires medical training; general readers know "heart attack" |
| `habeas corpus` | A2 legal specialist | Requires legal training |
| `kenosis` | A2 Christian theology specialist | Requires theology training |
| `phenomenology` | A2 philosophy specialist | Requires philosophy training |
| `epistemology` | A2 philosophy specialist (A1.native borderline) | Less specialist than phenomenology; appears in non-philosophy contexts |
| `entropy` | A1.advanced/native (commonsense use); A2 physics (technical-precise use) | Borderline; commonly-known concept in non-technical use |
| `mitosis` | A2 biology specialist | Requires biology training |
| `isotope` | A2 chemistry specialist | Requires science training |

**Borderline-cases-default rule.** When a word's classification is genuinely borderline (could go either way depending on broader-reading exposure or context), prefer A2-default — treat as requiring domain knowledge to be conservative. The reader's domain expertise (A2 axis) is configured separately, so defaulting to A2 means the translator will gloss or footnote unless the user has explicitly set A2=specialist for the matching domain.

### Migration mapping from existing `AUDIENCE_LEVEL`

The existing `.env.example` knob `AUDIENCE_LEVEL` has 3 values (`native | late_learner | late_learner_simple`). The suggested mapping to the new 5 levels:

| Existing | New | Rationale |
|---|---|---|
| `late_learner_simple` | `daily` | The label suggests a reader needing simplification beyond ordinary late-learner level. Best matches `daily` — a functional adult who handles daily life vocabulary but not Latinate or academic register. |
| `late_learner` | `conversational` | Suggests a second-language adult still building fluency but past survival level. Matches `conversational` — an educated adult who handles informed conversation including common Latinate vocabulary. |
| `native` | `native` | Direct identity mapping. Both refer to readers with educated native-speaker vocabulary breadth. |

**New positions introduced by the 5-level scheme:**
- `very_basic` extends BELOW `late_learner_simple` — covers children and brand-new learners, a reader profile the existing 3-level scheme could not address.
- `advanced` fills the gap BETWEEN `late_learner` (which maps to `conversational`) and `native` — covers university-educated readers and skilled non-natives who handle academic and literary register but not necessarily archaic; the existing scheme conflated this with `native`.

This mapping is SUGGESTED. The actual migration (whether to deprecate `AUDIENCE_LEVEL`, whether to keep both knobs in parallel, when to flip) belongs in a separate migration inquiry.

## Inherited Commitments Re-test

This finding refines the prior `translation_config_axes` finding. The relationship is **REFINES** with N ≥ 3 inherited commitments. Per CONCLUDE's synthesis re-test enforcement, the inherited commitments are listed and re-tested.

- **Commitment:** A1 Reader Level is a composite-axis with 5 sub-fields (vocabulary-breadth, syntactic-processing-capacity, idiom-recognition, inference-capacity, cultural-reference-recognition).
  - **Source:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — Level 1 USER-FACING AXES section, A1 Reader Level
  - **Re-test status:** RE-TESTED
  - **Evidence:** This finding instantiates one of the 5 sub-fields (vocabulary-breadth) with its own 5 level values; the composite-axis pattern is honored by the same-labels-across-A1-sub-fields commitment (see Cross-cutting framing constraints).

- **Commitment:** A1 measures RECEPTIVE vocabulary (recognition not production).
  - **Source:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — A1 Reader Level → vocabulary-breadth sub-field definition
  - **Re-test status:** RE-TESTED
  - **Evidence:** Every level's prose phrasing was verified at critique to use only reception verbs (`recognizes`, `does not recognize`, `understands when encountered`). No productive verbs slipped in. The receptive-only constraint is the load-bearing axis of sensemaking SV6 Ambiguity 8.

- **Commitment:** A1 axis identity is language-agnostic at the concept level.
  - **Source:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — A1 Reader Level → language-agnostic statement
  - **Re-test status:** RE-TESTED
  - **Evidence:** Each of the 5 levels has its frequency-tier band annotated as "English-illustrative." The CONCEPTS (Zipfian frequency tier; sociolinguistic register tier; substitution-test logic) exist universally; per-language thresholds are explicitly deferred to a per-language inquiry. Sensemaking SV6 Ambiguity 6 confirmed this holds for the 5 levels specifically.

- **Commitment:** 5 ordinal headline levels for A1 (proposed cardinality from prior finding).
  - **Source:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — A1 Reader Level → Cardinality
  - **Re-test status:** RE-TESTED
  - **Evidence:** This finding produces 5 ordinal levels (`very_basic | daily | conversational | advanced | native`) for the vocabulary-breadth sub-field, aligning with A1's proposed 5 headline levels. The same labels apply across A1 sub-fields per the same-labels-for-default-propagation commitment.

- **Commitment:** Conservative-bias defaults for early calibration phase.
  - **Source:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — Default principle (2-tier)
  - **Re-test status:** RE-TESTED with REFINEMENT
  - **Evidence:** Sensemaking SV6 Ambiguity 7 refined the conservative-bias principle for READER-FACING axes specifically: conservative-bias means LOWER default level (assume less reader competence; user dials UP). This is the opposite direction from strategy-side axes where conservative-bias = preserve more. The refinement extends the prior commitment without contradicting it.

- **Commitment:** POLICY layer items (multi-meaning preservation, register-alternation preservation, etc.) are always-on and not user-axes.
  - **Source:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — Layer 2 POLICY
  - **Re-test status:** INHERITED-WITHOUT-RE-TEST
  - **Reason:** Out of scope for this inquiry. The POLICY layer's interaction with vocabulary-breadth levels is acknowledged (e.g., at low levels, register-preservation may force a tradeoff if the source has high-register vocabulary), but the policy operational specs are deferred to a separate POLICY-layer inquiry per the prior finding's COULD action.

- **Commitment:** A2 Domain Expertise is separate from A1 vocabulary-breadth.
  - **Source:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — Layer 1 USER-FACING AXES → A2 Domain Expertise
  - **Re-test status:** RE-TESTED
  - **Evidence:** This finding makes the A1↔A2 boundary explicit via the subject-domain-training test and provides a 20-entry borderline-words table. Sensemaking SV6 Ambiguity 3 confirmed the orthogonality (a Hebrew Bible scholar can have low general English fluency; a general-educated reader can have no Bible knowledge — both real configurations).

## Next Actions

### MUST

- **What:** Define the 5 level values + per-level 4-component specs for each of the remaining 4 A1 sub-fields (syntactic-processing-capacity, idiom-recognition, inference-capacity, cultural-reference-recognition).
  - **Who:** the next 4 follow-up inquiries (one per A1 sub-field, of the same shape as this one).
  - **Gate:** condition-bound — before A1 Reader Level can be fully instantiated as a typed composite-axis. Each sub-field's inquiry should produce a finding analogous to this one.
  - **Why:** without the other 4 sub-fields' level specs, A1 Reader Level cannot be fully operationalized — the composite-axis pattern requires all sub-fields to share the same 5 labels with their own semantics.

### COULD

- **What:** Define per-language frequency-tier thresholds for vocabulary-breadth. The current finding's frequency bands (top ~500–1000 for very_basic, top ~2000–3000 for daily, etc.) are English-illustrative. Russian, Japanese, Arabic, and other target languages need their own bands defined.
  - **Who:** a per-language inquiry (one per language Comprehenslate adds support for).
  - **Gate:** condition-bound — when Comprehenslate adds the relevant target language.
  - **Why:** the translator-AI's runtime decisions depend on per-language band membership; without per-language thresholds, the LLM falls back to general English-corpus intuitions which may misjudge non-English vocabulary.
  - **Depends-on:** MUST item "Define the 5 level values for the remaining 4 A1 sub-fields." Per-language inquiries are best run AFTER all A1 sub-fields are specified for English, so the cross-sub-field structure is stable.

- **What:** Define the specific conservative-bias default value for vocabulary-breadth (`daily` or `conversational`).
  - **Who:** the defaults inquiry (covering all 8 axes' defaults).
  - **Gate:** condition-bound — when the defaults inquiry runs.
  - **Why:** the prior finding committed to a 2-tier default principle (Purpose-driven → conservative-bias fallback). For vocabulary-breadth, the conservative-bias-for-reader-axes principle (clarified here) says lower default, but the specific choice between `daily` and `conversational` is calibration-dependent.

- **What:** Define the Purpose-driven default-derivation for vocabulary-breadth (which Purpose value pulls vocabulary-breadth toward which level by default).
  - **Who:** the defaults inquiry.
  - **Gate:** condition-bound — alongside the conservative-bias default.
  - **Why:** the 2-tier default principle requires Purpose-driven mapping; e.g., `Purpose=scholarly` might pull vocabulary-breadth toward `advanced` or `native` by default.

### DEFERRED

- **What:** Implement the runtime substitution mechanism (LLM-judged vs frequency-list-backed).
  - **Gate:** revival when the level enums are committed to the pydantic schema and the translator-AI runtime begins consuming them. Condition-bound.
  - **Why (if revived):** initial implementation can be LLM-judged using the per-level prose + anchor examples as prompt context; later frequency-list backing can improve consistency. The per-level positive and negative examples in this finding double as anchor examples for the LLM's training-context grounding.

- **What:** Translate the 5 levels into the pydantic dataclass `vocabulary_breadth: Literal["very_basic", "daily", "conversational", "advanced", "native"]` field nested inside A1's composite-axis structure.
  - **Gate:** revival when the structural-layer inquiry begins.
  - **Why (if revived):** structural-layer artifact. Outside this inquiry's scope per the prior finding.

- **What:** Implement the migration from existing `AUDIENCE_LEVEL` (3 values) to the new `vocabulary_breadth` (5 values).
  - **Gate:** revival when production systems wire up the new axis.
  - **Why (if revived):** the suggested mapping (`late_learner_simple → daily`; `late_learner → conversational`; `native → native`) gives the migration its starting point; the actual cutover plan is operational.

## Reasoning

### What survived

The Final Recommended Assembly (Assembly E2 from critique) survives all 10 evaluation dimensions: Correctness (CRITICAL), Receptive-only discipline (CRITICAL), Language-agnostic at concept (CRITICAL), Mutually-distinct ordinal levels (CRITICAL), A1↔A2 boundary respect (CRITICAL), Sensemaking SV6 consistency (HIGH), Operationalizability (HIGH), Example correctness (CRITICAL), Project-value-fit (MEDIUM), Scope-discipline (MEDIUM).

Three minor refinement notes were incorporated:
- P3.2 daily prose: "Reads simple signs, instructions, casual conversation" was reworded to "Recognizes vocabulary in simple signs, instructions, and casual conversation" for maximum receptive clarity.
- Borderline examples flagged: `endeavor` at conversational noted as high-end-of-conversational (defensible — appears in newspaper register); `hermetic` at advanced noted as context-dependent with `recondite` as a less context-dependent substitute if preferred.
- `you ↔ thee` boundary pair: added a brief grammatical clarification ("`thee` — archaic 2nd-person singular object form").

### Significant alternatives rejected

- **5 separate axes for the 5 A1 sub-fields** (instead of composite-axis with shared sub-field labels). Sensemaking SV6 in the prior inquiry already rejected this on ergonomic grounds. This finding inherits that rejection.

- **CEFR's 6-level scheme (A1–C2)** instead of the user's 5-level reader-profile naming. Rejected at sensemaking Ambiguity 4: CEFR labels are abstract; the user's seed names are user-evocative. Critique confirmed.

- **Collapsing daily and conversational into one level.** Rejected at sensemaking Ambiguity 2: the two levels have distinct reader profiles (backpacker / new immigrant vs newspaper-reading educated adult) and substitution behaviors (replace Latinate at daily vs keep Latinate at conversational). The boundary pair examples (`buy ↔ purchase`, `try ↔ endeavor`) made this concrete.

- **Including subject-domain specialist vocabulary at A1.native** (e.g., calling `myocardial infarction` a native-level word because broadly-read natives "might know" specialist terms). Rejected at sensemaking Ambiguity 3 with the subject-domain-training test. The borderline-words table in the body operationalizes the boundary.

- **Productive-vocabulary semantics in level definitions** (using "uses" / "speaks" / "writes" verbs alongside "recognizes" / "understands"). Rejected at sensemaking Ambiguity 8; the prior finding committed A1 to RECEPTIVE only. Innovation's drafts and critique's audit both verified the receptive-only discipline held.

- **Frequency-bands as the SOLE definition logic** (ignoring register tier). Rejected at sensemaking Ambiguity 1: frequency alone misses register (the word `whereas` is high-frequency but high-register; the word `endeavor` is mid-frequency Latinate). The 4-component definition (frequency + register + reader-profile + substitution-test) was chosen because each component captures a distinct facet.

- **Treating the conservative-bias default for vocabulary-breadth as HIGHER** (e.g., default to `advanced` to "preserve richer source vocabulary"). Rejected at sensemaking Ambiguity 7: for reader-facing axes, conservative-bias means LOWER default (assume less reader competence). The opposite direction holds for strategy-side axes.

- **CC-B `hermetic` at advanced unchanged.** Critique noted `hermetic` is context-dependent (advanced general in its non-occult sense; A2 specialist in its esoteric sense). The finding flags this and offers `recondite` as a substitute. The user can choose either.

## Open Questions

### Refinement Triggers

- **Per-level positive example refinement.** If the LLM (during translator-AI runtime) consistently mis-judges a specific example word's level, that word's positive-example entry should be revisited. Trigger: observable — when 5+ runtime LLM judgments diverge from the spec's classification for the same word.

- **Borderline words table extension.** As the translator-AI encounters borderline words not in the table, additions are warranted. Trigger: observable — when a translator-AI runtime decision flags a word as "borderline A1↔A2" without table guidance.

- **5-level cardinality re-evaluation.** If real-user feedback shows users systematically cluster at 2–3 of the 5 levels and the other 2 are unused, the cardinality may collapse. Trigger: condition-bound — after the first 30 real translation configurations log A1 vocabulary-breadth values, examine the distribution.

### Research Frontiers

- **Per-language register-tier dynamics.** English's Latinate-vs-Germanic register split is distinctive; Russian (Slavic vs Church-Slavonic vs technical-borrowed), Japanese (yamato vs Sino-Japanese vs katakana-borrowed), Arabic (MSA vs Classical vs regional dialects vs scholarly) have analogous but mechanistically different register-tier dynamics. A future per-language inquiry will need to map each language's register-tier dynamics into the same 5-level structure.

- **Productive vs receptive divergence in non-native readers.** Some non-native readers have inverted asymmetry (productive > receptive) for specific domains — they speak but don't read at the same level. The current spec assumes the standard receptive > productive asymmetry. Edge case; not actionable now.

### Monitoring

- **Existing AUDIENCE_LEVEL usage statistics.** The suggested migration mapping (`late_learner_simple → daily`; `late_learner → conversational`; `native → native`) presupposes the existing labels are being used as semantically intended. If usage telemetry on the existing knob shows the labels are being interpreted differently in production, the mapping needs revision. Trigger: observable — when the migration inquiry begins (the inquiry that does the actual cutover).

### Blocked

- **Default value selection.** The specific conservative-bias default level for vocabulary-breadth (`daily` or `conversational`) cannot be answered without the defaults inquiry running (which covers all 8 axes' defaults jointly).

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
okay for A1 — Reader Level
Concept. The reader's overall ability to receive the translation. This is the broadest reader-facing axis.

User question it answers. "How fluent is the reader of this translation?"

Pattern. composite-axis — a headline level that the user sets, plus optional sub-field overrides. Sub-fields:

vocabulary-breadth — how many words the reader recognizes (passive vocabulary). High-breadth readers recognize technical or archaic words; low-breadth readers need everyday vocabulary.
syntactic-processing-capacity — how dense a sentence structure the reader can parse without losing the thread (long nested clauses, multi-clause subordination, etc.).
idiom-recognition — whether figurative expressions like "kick the bucket" land figuratively or get taken literally / freeze the reader.
inference-capacity — how much the reader can fill in compressed or elliptical argument (a passage that telescopes a five-step logical chain into one sentence; a passage where the verb is deliberately deleted; etc.).
cultural-reference-recognition — whether allusions and named entities land without explanation. This is competence-based, distinct from A3 Source Culture (which is identity-based — see below).
Why one axis with sub-fields, not 5 separate axes. The 5 sub-fields are empirically correlated in typical readers — a non-native ESL professor with high vocabulary but low idiom recognition is real but rare; the joint distribution is heavily clustered. If you split into 5 separate axes, every typical user must reason about 5 fields just to describe one reader (concept-load exceeds the ergonomic bound stated in the problem). If you collapse into one ordinal scale, the rare cases can't be expressed. The composite-axis pattern preserves both: the user sets ONE headline level; sub-field defaults derive from the headline; per-sub-field overrides are available for the cases where the joint correlation breaks.

Cardinality (proposed). 5 headline levels.

Scope. Controls the reader's overall comprehension profile.

Boundary. Does NOT control domain expertise (that's A2), source-culture proximity (that's A3), or how much explanatory help the translation provides (that's A7 Scaffolding).

Language-agnostic at concept level. Every human language has high-frequency vs low-frequency vocabulary; every language has idioms; every language has syntactic complexity gradients. The CONCEPT is universal. The level thresholds (what specifically counts as "very basic" vs "advanced" in a given language) are language-specific and belong in the next inquiry.


lets dive deep into 5 levels starting from very basic to advanced.. and also logic and example of how to distinguish them but only for vocabulary-breadth field, not about others
```

</details>
