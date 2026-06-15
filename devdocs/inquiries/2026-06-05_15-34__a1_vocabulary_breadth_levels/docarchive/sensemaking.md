# Sensemaking — a1_vocabulary_breadth_levels

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/_branch.md` (with surfacing output at `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/surfacing.md`)

---

## SV1 — Baseline Understanding

The inquiry asks to define 5 levels for the **vocabulary-breadth** sub-field of A1 Reader Level. The user's seed naming is `very_basic | daily | conversational | advanced | native`. My initial impression: these 5 names are intuitive reader-profile labels; the task is to give each one a concept + distinguishing logic + examples. The challenges will be (a) finding ONE primary logic that grounds the 5 levels (frequency-tier vs reader-profile vs substitution-test vs register-tier all surfaced as candidates), (b) handling the daily↔conversational boundary (they sound close), (c) deciding where specialist/technical vocabulary lives (A1.native vs A2 Domain Expertise), and (d) ensuring language-agnosticism without losing operational specificity.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1.** 5 ordinal levels covering the full spectrum (from prior finding's A1 cardinality).
- **C2.** Language-agnostic at concept level — every language has frequency/register tiers; specific thresholds are per-language.
- **C3.** RECEPTIVE vocabulary only — recognition not production (prior finding's A1 commitment).
- **C4.** Scope = vocabulary-breadth ONLY — not the other 4 A1 sub-fields, not other axes.
- **C5.** Each level must be operationalizable as a translator-AI prompt instruction.
- **C6.** Mutually distinct levels (each describes meaningfully different readers).
- **C7.** Ordinal — low-to-high monotonic; no categorical mixing.
- **C8.** Respect prior commitment to composite-axis pattern — these levels are sub-field defaults that propagate from A1 headline.
- **C9.** Existing AUDIENCE_LEVEL knob is 3-level (`native | late_learner | late_learner_simple`); soft constraint that the new 5-level should be migration-mappable from it.
- **C10.** Respect register-preservation policy (memory feedback H1) — the POLICY layer interacts with vocabulary level at runtime, but level definitions themselves don't encode policy.

### Key Insights

- **KI1.** ACTFL has exactly **5 levels** (Novice / Intermediate / Advanced / Superior / Distinguished). This is a structural anchor — the international 5-level standard matches the inquiry's cardinality. CEFR has 6 (A1–C2); ILR has 6 (0–5). The 5-level commitment isn't arbitrary.
- **KI2.** Zipf's law applies to every natural language — high-frequency words form a small set; frequency drops along a power law. This is the universal language-agnostic basis for "vocabulary breadth" levels.
- **KI3.** Receptive vs productive asymmetry (~2–3x): a "conversational" reader RECOGNIZES more words than they CAN USE. The levels are about recognition only (per C3).
- **KI4.** Multiple distinguishing logics surfaced (frequency-tier, reader-profile, substitution-test, register-tier, coverage-based). The right approach is LAYERED — one primary operational basis + reader-profile naming + substitution-test runtime. The substitution-test is what the translator-AI does at runtime; the frequency-tier/register-tier is the conceptual basis; the reader-profile is the human-facing label.
- **KI5.** The daily↔conversational boundary is real but subtle. Daily = vocabulary used to FUNCTION (buy groceries, transit, work). Conversational = vocabulary used in INFORMED INFORMAL CONVERSATION between educated adults. They differ in REGISTER (functional vs educated-informal) and EDUCATION level, not in raw word count.
- **KI6.** Specialist/technical vocabulary like `myocardial infarction` is a borderline case: is it A1.native (broad vocabulary) or A2 Domain Expertise (specialist medical training)? The boundary rule: if knowing the word requires SUBJECT-DOMAIN TRAINING, it's A2; if it requires only BROAD GENERAL READING, it's A1. `Myocardial infarction` requires medical training → A2. `Ratiocination` is general high vocabulary → A1.advanced or A1.native.
- **KI7.** Archaic vocabulary (`anon`, `verily`, `thee`) is general-language not specialist; it belongs at A1.native. A native reader recognizes archaic forms even without specialist training.
- **KI8.** The level CONCEPT can be defined as a coverage tier — e.g., "very_basic = top-N most frequent words; native = all general vocabulary including archaic/literary." This is language-agnostic; the N varies per language.
- **KI9.** Default-propagation in the composite-axis pattern: when user sets A1=conversational, vocabulary_breadth defaults to conversational. For clean default-propagation, the vocabulary_breadth labels must MATCH the A1 headline labels. The 5 labels should be the SAME across all A1 sub-fields (label semantics are sub-field-specific, but the strings match).
- **KI10.** English has a distinctive Latinate/Germanic register split (`purchase` vs `buy`) that maps cleanly to the conversational→advanced boundary. Other languages have analogous dynamics (Russian Slavic/Church-Slavonic; Japanese yamato/Sino-Japanese; Arabic MSA/Classical). The CONCEPT (register-tier inclusion) is universal; the SPECIFIC mechanism differs per language.

### Structural Points

- **SP1.** The 5 levels can be operationalized via the **substitution-test**: at level L, the translator REPLACES words above L with simpler equivalents at or below L. This is the runtime mechanism.
- **SP2.** Each level's definition has 4 components: **name + frequency-tier band + register-tier inclusion + substitution-test sketch**.
- **SP3.** Frequency-band and register-tier ARE CORRELATED but not identical — `purchase` and `buy` are roughly equally frequent in modern English but differ in register. The substitution test handles register difference even when frequencies are similar.
- **SP4.** Level definitions need ENGLISH examples for illustration but the level CONCEPTS must be specified language-agnostically.
- **SP5.** The A1↔A2 boundary: A1 = general-language vocabulary breadth (everyday → archaic → literary; in general usage). A2 = subject-domain knowledge (medicine, law, theology, mathematics). Test: "does the word require domain training, or only broad reading?"
- **SP6.** The existing AUDIENCE_LEVEL (3-level) maps to a SUBSET of the new 5-level. Suggested mapping: `late_learner_simple → daily`; `late_learner → conversational`; `native → native`. The new levels EXTEND the spectrum: `very_basic` below the old's lowest; `advanced` between the old's middle and top.

### Foundational Principles

- **FP1.** Levels are about RECEPTIVE vocabulary — operationalized via "would the reader pause / look up / freeze at this word?"
- **FP2.** Levels are LANGUAGE-AGNOSTIC at concept. The concept "frequency-tier" exists in every language; specific words differ per language.
- **FP3.** Levels are ORDINAL — each level subsumes lower levels (a native reader knows daily vocabulary; a daily reader doesn't know advanced). Monotonic.
- **FP4.** Vocabulary-breadth EXCLUDES specialist domain vocabulary that requires A2 Domain Expertise. A1 measures GENERAL vocabulary.
- **FP5.** Conservative-bias for reader-facing axes = assume LOWER reader competence (default to lower levels; user dials UP). Important for default-derivation: for vocabulary_breadth, the conservative-bias fallback is a low-to-mid level (daily or conversational), NOT a high level.

### Meaning-Nodes

- **MN1.** VOCABULARY-BREADTH LEVEL = a tier specifying how broad a reader's passive recognition vocabulary is.
- **MN2.** FREQUENCY BAND = a Zipfian tier of words ordered by usage frequency (universal across languages; specific words language-specific).
- **MN3.** REGISTER TIER = a sociolinguistic register (everyday / colloquial / journalistic / literary / archaic / technical-general).
- **MN4.** SUBSTITUTION-TEST LOGIC = the runtime rule: at level L, the translator replaces words above L with equivalents at or below L.
- **MN5.** READER PROFILE = a typical reader the level represents (small child / functional adult / educated adult / native).
- **MN6.** A1↔A2 BOUNDARY = A1 measures general vocabulary at all registers; specialist subject-domain vocabulary is A2; the test is "requires subject-domain training" vs "requires only broad reading."

### Meta-Inspection after SV2 (H4 concept names, H5 motivating examples)

- **H4 — concept names.** "frequency-tier" + "register-tier" are linguistics standard. "reader-profile" is intuitive. "substitution-test" is loop-coined but operationally clear. The 5 level names `very_basic | daily | conversational | advanced | native` are the user's seed; user-language alignment is HIGH. No new vocabulary-coining risks.
- **H5 — motivating examples.** The user's example pair (ratiocination/ostensibly vs reasoning/apparently) illustrates ONE boundary (roughly advanced↔daily or advanced↔conversational). The OTHER three boundaries (very_basic↔daily, daily↔conversational, advanced↔native) need their own example pairs. Specific-vs-pattern check: the user's pair is illustrative of one boundary; innovation must enumerate examples for ALL boundaries.

### SV2 — Anchor-Informed Understanding

The 5 levels for vocabulary-breadth are ordinal, receptive-only, language-agnostic at concept, and operationalizable via the substitution-test. The user's seed naming aligns with the framework. The primary distinguishing logic should be LAYERED: frequency-tier (the Zipfian universal basis) + register-tier (literary/archaic/specialist) + reader-profile (the human-facing label) + substitution-test (runtime translator action). Each level has 4 components.

The A1↔A2 boundary needs to be made explicit: A1 covers general vocabulary at all registers (including archaic); A2 covers subject-domain specialist vocabulary requiring training.

The 5 labels propagate from the A1 headline (composite-axis pattern); same labels across all A1 sub-fields, with sub-field-specific semantics.

The existing AUDIENCE_LEVEL (3-level) maps to a subset of the new 5-level; migration guidance belongs in the finding but doesn't affect level definitions.

---

## Phase 2 — Perspective Checking

### Technical / Logical perspective

Each level becomes a `Literal` value in the pydantic enum. The translator-AI consumes the level via its prose description in the prompt context. The substitution-test logic implies a per-word level mapping; initially this is LLM-judged (the LLM has language knowledge), later potentially frequency-list-backed.

**New anchors:**
- **T-A1.** Each level needs a 2–3 sentence prose description suitable for the translator-AI's prompt context.
- **T-A2.** Substitution-test implies per-word level judgment; LLM-judged is the initial path.
- **T-A3.** Per-language frequency-list backing is a future addition; doesn't affect this inquiry's level definitions.

### Human / User perspective

A user specifying `vocabulary_breadth = "conversational"` should have a clear mental model of "I'm translating for a reader who can carry an informed conversation but doesn't know academic vocabulary." The level names should evoke this immediately. The user's seed names DO evoke reader profiles; CEFR-style abstract labels (A1, A2, B1...) don't.

**New anchors:**
- **H-A1.** User-facing level names should be evocative reader-profile names, not abstract framework labels.
- **H-A2.** Level descriptions should help the user identify their target reader by reading (i.e., a description should let the user say "yes, that's my reader" or "no, mine is more like the next level").

### Strategic / Long-term perspective

As Comprehenslate adds target languages, the level CONCEPTS must hold. Frequency-tier and register-tier exist universally. Level NAMES might need translation per UI language; CONCEPTS stay. As LLM translators become more capable, the substitution-test may shift from word-by-word substitution to selective lexical choice throughout — but the LEVEL DEFINITIONS shouldn't depend on a specific runtime mechanism.

**New anchors:**
- **S-A1.** Level definitions must be stable across target-language additions.
- **S-A2.** Level NAMES might need translation per UI language; CONCEPTS are universal.
- **S-A3.** Runtime operationalization will evolve; level DEFINITIONS should not depend on a specific runtime mechanism.

### Risk / Failure perspective

Worst-case bad level definitions:
- Levels that overlap (daily and conversational describing the same reader)
- Levels not operationalizable (LLM can't judge "is this word at this level?")
- Levels that conflate A1 with A2 (advanced level includes domain-specialist vocabulary)
- Levels that presuppose English (Latinate/Germanic register as defining axis)
- Levels with confused defaults
- Definitions slipping into productive vocabulary (violating C3)

**New anchors:**
- **R-A1.** Each adjacent-level pair needs a clean distinguishing principle (not a vibe).
- **R-A2.** Definitions must be operationalizable: LLM must consistently judge "is this word at this level?"
- **R-A3.** A1↔A2 boundary must be explicit in level definitions.
- **R-A4.** Examples can be English (for illustration); concept must operationalize for other languages.
- **R-A5.** Receptive-only constraint must be strictly maintained throughout level prose.

### Resource / Feasibility perspective

Can the LLM consistently judge level membership? GPT-4-class LLMs have rich vocabulary knowledge but may inconsistently judge edge cases. Definitions should include ANCHOR EXAMPLES (words clearly at this level + words clearly above) to ground LLM judgment.

**New anchors:**
- **F-A1.** Level definitions need anchor examples (positive: words clearly AT this level; negative: words clearly ABOVE this level).
- **F-A2.** Initial implementation = LLM-judged via prose + examples; future = frequency-list backing.

### Ethical / Systemic perspective

Level names should not be culturally biased. "Backpacker level" (from user's framing) might evoke Western stereotypes; "daily" is culturally neutral. The "native" level should mean "vocabulary-breadth equivalent to an educated native speaker" — NOT "the reader IS a native speaker" (a non-native scholarly reader can be at vocabulary_breadth=native if their receptive vocabulary is broad).

**New anchors:**
- **E-A1.** Level NAMES should be reader-profile-based, not identity-based.
- **E-A2.** "native" level means "vocabulary-breadth equivalent to an educated native speaker"; non-native readers can reach this level through extensive reading.

### Definitional / Internal Consistency perspective

- **C-A1.** Prior finding committed to vocabulary-breadth as RECEPTIVE (recognition not production). Level definitions must be phrased in recognition terms. Any level definition that says "uses this vocabulary" (productive) instead of "recognizes this vocabulary" (receptive) violates.
- **C-A2.** Default-propagation in composite-axis pattern: when A1 headline = conversational, vocabulary_breadth defaults to conversational. For clean propagation, the labels must MATCH between A1 headline and vocabulary_breadth. Same 5 labels.
- **C-A3.** Per the prior finding's POLICY layer, register-preservation is always-on. At low vocabulary levels, register-preservation may force a tradeoff: the source has high-register vocabulary but the target reader doesn't recognize high-register vocabulary in the target language. This is a runtime conflict (frontier from prior finding, deferred). Level definitions can flag the interaction but don't resolve it.

### Definitional / Frame-exit Completeness perspective

Gating fires: inquiry inherits "vocabulary-breadth" from prior finding; uses it across 5 distinct values within this inquiry's committed structures.

**1. Existence Enumeration.** What does "VOCABULARY-BREADTH LEVEL" refer to project-wide?
- Within this inquiry: 5 ordinal levels for vocabulary-breadth specifically.
- In prior finding: a sub-field of A1, propagating from A1 headline.
- In `.env.example`: indirectly via AUDIENCE_LEVEL (3 levels).
- The TYPE of "level" in the project: levels appear across multiple axes (DEPTH_PROFILE has 4; AUDIENCE_LEVEL has 3; prospectively A1–A8 each have 3–5). Each axis's levels are separate namespaces; label collisions don't conflict if the namespace is clear (vocabulary_breadth.conversational is different from analysis_depth.scholarly).
- AGENT axis: levels are USER-set (with A1 headline propagating defaults to sub-fields).

**2. Role Assessment.**
- A1 HEADLINE LEVEL is out of this inquiry's frame but the labels SHOULD match for clean default-propagation. **Verdict: re-locate.** The vocabulary_breadth 5 labels must equal the A1 headline 5 labels.
- Other A1 sub-fields (idiom-recognition, syntactic-processing-capacity, inference-capacity, cultural-reference-recognition) are out of scope but each will need its OWN level definitions. The labels CAN match (same `very_basic | daily | conversational | advanced | native`) for default-propagation simplicity, with each sub-field carrying its own SEMANTICS for each label. **Verdict: re-locate; future inquiries will define their own semantics.**
- A2 Domain Expertise is out of scope but its BOUNDARY with A1 must be explicitly drawn here. **Verdict: re-locate boundary acknowledgement into the level definitions.**

**3. Verdict Rigor.** Clean-boundary "specialist vocabulary is A2 not A1" — strongest counter: "a native English reader knows `myocardial infarction` casually." Test: does the average native English reader recognize `myocardial infarction` instantly? No — they recognize "heart attack" and might infer "infarction" is medical. Specialist vocabulary genuinely requires domain training. The boundary holds — HIGH confidence.

**4. Residual / Coverage Justification.** Frame-exit concerns the named categories missed? The relationship between vocabulary-breadth levels and the runtime SUBSTITUTION action when no equivalent exists at the target level — this is a runtime conflict (frontier D1 from prior inquiry; deferred). Acknowledged; not in this inquiry's scope.

### Phase / Calibration-State perspective

Does the inquiry involve rules dependent on calibration the project has?

Yes — DEFAULTS for vocabulary-breadth are calibration-dependent. The prior finding's 2-tier default principle (Purpose-driven → conservative-bias fallback) means vocabulary_breadth's default depends on Purpose and conservative-bias.

Conservative-bias for vocabulary-breadth specifically: for READER-FACING axes, conservative-bias = ASSUME LOWER READER COMPETENCE (default to LOWER levels; user dials UP if they have a more advanced reader). This protects against over-estimating readers and producing unreadable translations.

**P-A1.** Conservative-bias for reader-facing axes = LOWER default level. For vocabulary_breadth, the conservative-bias fallback is `daily` or `conversational`, not `advanced` or `native`. The exact default value is the next inquiry; the PRINCIPLE INTERPRETATION is settled here.

### Meta-Inspection after SV3 (H1, H2, H3, H7)

- **H1 — candidate set convergence.** Test the 5 candidate level names: do any collapse? Daily↔conversational is the closest pair. Test by reader profile: "daily" = functional adult; "conversational" = educated adult who has informed conversation. Distinct. Test by substitution: at "daily" replace `endeavor`→`try`; at "conversational" keep `endeavor`. Distinct. The 5 levels are non-collapsing.

- **H2 — frame scope** (already done via Frame-exit Completeness): scope = vocabulary-breadth-specific; A1 headline-label alignment confirmed; A1↔A2 boundary explicit.

- **H3 — question framing pre-bias.** User's seed names bias toward reader-profile logic. Is this right? Yes — reader-profile is user-natural. Frequency-tier numbers (top-500, top-5000) are developer-natural but bad UX. The bias is appropriate.

- **H7 — phase / calibration state**: defaults are calibration-dependent (P-A1 noted); level definitions are not.

### SV3 — Multi-Perspective Understanding

After perspective checking, the model gains:

1. **Layered logic confirmed.** Per-level definition has 4 components: name + frequency-tier + register-tier + substitution-test sketch. Each component is independently verifiable.

2. **Same labels across A1 sub-fields.** The 5 labels `very_basic | daily | conversational | advanced | native` apply to ALL A1 sub-fields (each carrying its own semantics for those labels) — for clean default-propagation from A1 headline.

3. **A1↔A2 boundary made explicit.** A1 = general vocabulary at all registers (including archaic); A2 = subject-domain specialist vocabulary. The test is "requires subject-domain training" vs "requires only broad reading."

4. **Conservative-bias for reader-facing axes** = LOWER default level. This interpretation matters for the defaults inquiry.

5. **Concrete 5-level shape emerging** with reader profiles, frequency-tier bands (English-illustrative), register-tier inclusion, and substitution-test sketches.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — Primary distinguishing logic

**Strongest counter-interpretation:** Pick ONE primary logic (frequency-tier OR reader-profile OR substitution-test) and define the levels strictly by it. Mixed logic creates confusion.

**Why the counter fails (structural grounds):** Frequency-tier alone misses register (the word `whereas` is high-frequency but high-register). Reader-profile alone is operationally vague. Substitution-test alone is runtime mechanism, not concept. The LAYERED approach (frequency-tier basis + register-tier modifier + reader-profile name + substitution-test runtime) gives each level a coherent multi-dimensional definition the LLM can use for consistent judgment. Each component captures a different facet; none is redundant.

**Confidence:** HIGH.

**Resolution:** Use LAYERED logic with 4 components per level.

**Fixed:** Each level has 4 components: name + frequency-tier band + register-tier inclusion + substitution-test sketch.

**No longer allowed:** Defining levels with only ONE logic dimension.

---

### Ambiguity 2 — Are daily and conversational distinct enough?

**Strongest counter-interpretation:** Collapse to 4 levels (`very_basic | daily | advanced | native`). Daily already covers "everyday vocabulary"; conversational is just "slightly more."

**Why the counter fails (structural grounds):** Daily and conversational differ in REGISTER and EDUCATION level, not just word count:
- Daily = FUNCTIONAL everyday (buy / sell / walk / work / eat / sleep) — backpacker / new immigrant / functional second-language adult
- Conversational = EDUCATED-ADULT INFORMAL (purchase / decide / consider / approximate) — average newspaper reader

Substitution-test distinguishes them clearly: at daily, replace `endeavor`→`try`; at conversational, keep `endeavor`. The two reader profiles are distinct: a backpacker functioning in a foreign country vs an educated adult at a dinner party.

**Confidence:** HIGH.

**Resolution:** Keep daily and conversational as separate levels.

**Fixed:** 5 levels (not 4); daily↔conversational boundary defined as "functional vs educated-informal register."

---

### Ambiguity 3 — Where do specialist/technical terms live?

**Strongest counter-interpretation:** A native-level reader knows `myocardial infarction` because they have broad vocabulary; this is A1.native.

**Why the counter fails (structural grounds):** A native English reader without medical training does NOT recognize `myocardial infarction` instantly — they recognize "heart attack" and might guess medical-from-morphology. Specialist vocabulary requires SUBJECT-DOMAIN TRAINING. The boundary: A1 = general vocabulary (everyday → archaic → literary); A2 = subject-domain (medical, legal, theological-specialist). Test: "requires domain training" → A2; "requires broad reading" → A1.

Edge cases:
- `eschatology` = A2 (theology specialist) for most; A1.native for very-broadly-read; treat as A2-default.
- `transubstantiation` = A2 (Catholic theology specialist).
- `ratiocination` = A1.advanced or A1.native (general Latinate; no domain training needed).
- `anon` (archaic) = A1.native (archaic general).

**Confidence:** HIGH.

**Resolution:** A1 covers GENERAL vocabulary at all registers (including archaic). A2 covers SUBJECT-DOMAIN specialist. Test: "requires subject-domain training to know."

**Fixed:** A1↔A2 boundary explicit; vocabulary-breadth example sets must use GENERAL words only.

---

### Ambiguity 4 — Level names: user's seed vs abstract labels?

**Strongest counter-interpretation:** Abstract labels (L1–L5 or A1–C2) avoid mental-model bias from evocative names.

**Why the counter mostly fails:** The user explicitly said the seed names are good ("very_basic | daily | conversational | advanced | native" is "a good field"). User-evocative names are user-natural; abstract labels require translation overhead.

A possible refinement: use BOTH — user-facing name = reader-profile; pydantic enum key = snake_case version of name; internal index L1–L5 for migration logic if needed. But this is implementation detail (pydantic layer, future inquiry).

**Confidence:** HIGH.

**Resolution:** Adopt user's seed names. 5 labels = `very_basic | daily | conversational | advanced | native`.

**Fixed:** Level NAMES committed.

---

### Ambiguity 5 — Migration mapping from existing AUDIENCE_LEVEL?

**Strongest counter-interpretation:** Don't commit a mapping here; let the next inquiry handle it.

**Why the counter mostly holds, but partially fails:** Mapping is a migration concern that doesn't affect level CONCEPTS. But the user will want to understand the relationship. Documenting the SUGGESTED mapping in the finding (without making it a strict requirement) is appropriate.

**Confidence:** MEDIUM.

**Resolution:** Document the suggested migration mapping in the finding's Next Actions: `late_learner_simple → daily`; `late_learner → conversational`; `native → native`. New positions: `very_basic` (extends low end below `late_learner_simple`); `advanced` (between `late_learner`/conversational and native).

**Fixed:** Suggested mapping documented; not a strict requirement.

---

### Ambiguity 6 — Language-agnosticism stress test

**Strongest counter-interpretation:** English has distinctive Latinate/Germanic register (`purchase`/`buy`) defining conversational→advanced. Other languages don't have this dynamic identically.

**Why the counter fails:** Every language has analogous register-tier dynamics:
- Russian: native Slavic vs Church Slavonic vs technical-borrowed
- Japanese: yamato vs Sino-Japanese vs katakana-borrowed
- Arabic: MSA vs Classical vs regional dialects vs scholarly

The CONCEPT (register-tier inclusion at higher levels; Zipfian frequency) is universal. The MECHANISM (which words are higher-register) is language-specific. The 5-level structure (basic core / functional / educated-informal / educated-formal / native-all-registers) translates to any language with appropriate register substitutions.

**Confidence:** HIGH.

**Resolution:** Level concepts are language-agnostic. English examples are illustrative. Per-language frequency thresholds and register lexicons belong in the next inquiry.

**Fixed:** Language-agnosticism constraint satisfied at concept level.

---

### Ambiguity 7 — Conservative-bias default direction

**Strongest counter-interpretation:** Conservative-bias = "preserve more" → higher vocabulary-breadth default (preserves richer source vocabulary in translation).

**Why the counter fails:** For READER-FACING axes (A1, A2, A3), conservative-bias means assume LESS reader competence (default to LOWER level; user dials UP). This protects against over-estimating readers and producing unreadable output. For TRANSLATION-STRATEGIC axes (A5, A6, A7), conservative-bias means preserve more (default to HIGHER preservation; user dials DOWN). The two cases differ.

**Confidence:** HIGH.

**Resolution:** Conservative-bias for reader-facing axes (including vocabulary_breadth) = LOWER default level. Specific default value (`daily` vs `conversational`) is the next inquiry; the PRINCIPLE interpretation is settled here.

**Fixed:** Conservative-bias-for-reader-axes principle.

---

### Ambiguity 8 — Receptive-only enforcement

**Strongest counter-interpretation:** Level definitions can use either receptive or productive framing; readers know what they mean either way.

**Why the counter fails:** Prior finding's A1 explicitly committed to RECEPTIVE vocabulary. Productive framing means "what the reader CAN SAY"; receptive means "what the reader UNDERSTANDS when encountered." For TRANSLATION, only reception matters (the reader is consuming the translation, not producing). The asymmetry is ~2-3x: a "conversational" reader RECOGNIZES more words than they could PRODUCE. Mixing the framings introduces vagueness in level definitions.

**Confidence:** HIGH.

**Resolution:** All level prose must use RECOGNITION terms. No "uses" / "speaks" / "writes" / "produces" verbs; only "recognizes" / "understands when encountered" / "doesn't pause at."

**Fixed:** Receptive-only constraint enforced.

---

### Load-bearing concept test (per refinement note)

Load-bearing concepts:
1. **LAYERED 4-component definition** — concept valid; component names acceptable.
2. **A1↔A2 boundary** (general vs subject-domain) — HIGH confidence, real structural distinction.
3. **Same labels across A1 sub-fields** — for default-propagation; semantics per-sub-field.
4. **Conservative-bias for reader-facing axes = lower default** — principle clarified.

### Specific-vs-pattern recognition cue

The user's example pair illustrates ONE boundary. The other three boundaries (very_basic↔daily, daily↔conversational, advanced↔native) need their own example pairs surfaced. Innovation should enumerate.

### SV4 — Clarified Understanding

The 5 vocabulary-breadth levels are:

- **very_basic** — top ~500–1000 most frequent words (core + function vocabulary); young child or brand-new learner; translator replaces almost everything above this band with descriptive paraphrase.
- **daily** — top ~2000–3000 most frequent words (functional everyday vocabulary); backpacker / functional adult second-language speaker; translator replaces Latinate / academic / literary with everyday equivalents.
- **conversational** — top ~5000–7000 words including common Latinate; average educated adult; reads newspapers comfortably; translator avoids dense academic, archaic, dialectal, specialist.
- **advanced** — top ~10000–20000 words including academic and literary; university-educated reader / skilled non-native; translator avoids only archaic, dialectal, specialist-rare.
- **native** — full general vocabulary including archaic, dialectal, rare-but-general; educated native speaker; translator avoids ONLY A2 specialist domain vocabulary.

Each level has 4 components (name + frequency-tier + register-tier + substitution-test sketch). All prose is in recognition terms. English examples are illustrative; concepts are language-agnostic.

Vocabulary-breadth EXCLUDES A2 specialist domain vocabulary. The A1↔A2 boundary test: "requires subject-domain training" vs "requires only broad general reading."

The 5 labels match the A1 headline labels for clean default-propagation across sub-fields.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Variables now fixed

- **5 ordinal levels** matching prior finding's A1 cardinality.
- **Level names:** `very_basic | daily | conversational | advanced | native`.
- **Per-level definition has 4 components:** name + frequency-tier band + register-tier inclusion + substitution-test sketch.
- **A1 covers GENERAL vocabulary; A2 covers SUBJECT-DOMAIN vocabulary** with the "requires subject-domain training" test.
- **Receptive only** — definitions phrased in recognition terms.
- **Language-agnostic at concept** — concepts use Zipfian frequency and register-tier; English examples illustrative.
- **Same labels across A1 sub-fields** for default-propagation; semantics sub-field-specific.
- **Migration mapping from existing AUDIENCE_LEVEL** documented in finding (not in level definitions).
- **Conservative-bias for reader-facing axes = LOWER default level** (principle, not specific default value).

### Options eliminated

- Frequency-bands-only as definition logic.
- Substitution-test alone as definition (it's runtime mechanism, not concept).
- Daily↔conversational collapse.
- A1.native including specialist domain vocabulary like `myocardial infarction` (that's A2).
- Abstract labels (L1–L5 or A1–C2) as primary names.
- Different labels per A1 sub-field.
- Productive-vocabulary semantics in definitions.
- Conservative-bias = HIGHER default level for reader-facing axes.

### Paths remaining viable

- Concrete per-level definitions with 4 components, written language-agnostically with English examples.
- Example pairs (positive and negative) for each level.
- Boundary-pair examples at each adjacent-level boundary.
- Documentation of A1↔A2 boundary with edge-case classification.
- Suggested migration mapping from existing AUDIENCE_LEVEL.

### SV5 — Constrained Understanding

**5 levels with reader-profile names (`very_basic | daily | conversational | advanced | native`), each defined by 4 components (name + frequency-tier + register-tier + substitution-test sketch), with adjacent-level example pairs, all phrased in language-agnostic concept terms with English examples for illustration, and the A1↔A2 boundary explicitly drawn.**

Remaining work:
- Innovation: concrete prose definitions + examples per level + boundary pairs (in scope).
- Critique: verify levels are mutually distinct, ordinal, operationalizable, language-agnostic.
- Future inquiry: per-language frequency thresholds.
- Future inquiry: runtime substitution mechanism.
- Future inquiry: specific conservative-bias default value.
- Future inquiry: the other 4 A1 sub-fields.

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Did new perspectives keep destabilizing the model?
- Phase 2 perspectives produced anchors that REFINED the model (4-component definition, A1↔A2 boundary, conservative-bias-for-reader-axes principle, language-agnosticism at concept level). They did NOT force major revisions.
- Phase 3 ambiguity collapses converged consistently.
- No "patch and re-patch" pattern.

**Accommodation trigger does NOT fire.**

### Meta-Inspection final check (H6 model fit)

The 5-level structure with 4-component definitions fits all 10 constraints + 8 surfacing frontier flags + the user's seed naming + the prior finding's inherited commitments. Revision pattern was REFINEMENT, not PATCHING.

### SV6 — Stabilized Model

The 5 vocabulary-breadth levels are:

```
LEVEL 1 — very_basic
  Reader profile: young child / brand-new second-language learner
  Frequency tier (English-illustrative): top ~500–1000 most frequent words
                                          (function words + most-common content)
  Register tier: only the most everyday core vocabulary;
                 no Latinate, no abstract, no specialist, no literary
  Substitution-test sketch: translator replaces almost everything above the
                            core band with simpler descriptive equivalents
                            or paraphrase

LEVEL 2 — daily
  Reader profile: functional adult in daily life (backpacker / new immigrant /
                  functional second-language speaker)
  Frequency tier (English-illustrative): top ~2000–3000 most frequent words
  Register tier: everyday concrete + simple abstract;
                 excludes Latinate, academic, literary, specialist, archaic
  Substitution-test sketch: translator replaces Latinate ("purchase"→"buy"),
                            academic ("endeavor"→"try"), and literary
                            vocabulary with everyday equivalents

LEVEL 3 — conversational
  Reader profile: average educated adult who can carry an informed informal
                  conversation; reads newspapers comfortably
  Frequency tier (English-illustrative): top ~5000–7000 words including common
                                          Latinate
  Register tier: everyday + conversational-educated + journalistic;
                 includes common Latinate (purchase, endeavor, consider,
                 approximate);
                 excludes dense academic, literary-archaic, specialist, dialectal
  Substitution-test sketch: translator avoids dense academic, archaic, dialectal,
                            specialist; keeps common Latinate

LEVEL 4 — advanced
  Reader profile: university-educated reader / skilled non-native who reads
                  widely / educated professional
  Frequency tier (English-illustrative): top ~10000–20000 words including
                                          academic and literary
  Register tier: everyday + conversational + journalistic + academic +
                 general literary;
                 excludes archaic, dialectal, specialist-rare general
  Substitution-test sketch: translator avoids only archaic ("verily", "anon"),
                            dialectal, and specialist-rare general vocabulary;
                            keeps academic and literary

LEVEL 5 — native
  Reader profile: educated native speaker who reads broadly across registers
  Frequency tier (English-illustrative): full general vocabulary
                                          (no upper bound on rarity)
  Register tier: all general registers including archaic, dialectal,
                 literary-rare
  Substitution-test sketch: translator avoids ONLY A2 specialist domain
                            vocabulary (medical, legal, theological-specialist);
                            keeps all general vocabulary including archaic
```

**Key clarifications:**
- VOCABULARY-BREADTH (A1) covers general vocabulary across all registers (including archaic).
- SUBJECT-DOMAIN VOCABULARY (A2) covers terms requiring field training.
- Boundary test: "requires subject-domain training to recognize" → A2; "requires only broad general reading" → A1.
- All level concepts are language-agnostic; English examples illustrative.
- Same labels propagate from A1 headline; sub-field-specific semantics.

### How SV6 differs from SV1

SV1 said: "5 levels for vocabulary-breadth; user's seed names are intuitive; need concept + logic + examples per level."

SV6 commits to:
- **Concrete 5-level structure** with names = user's seed.
- **4-component definition pattern** per level (name + frequency-tier + register-tier + substitution-test).
- **Explicit A1↔A2 boundary** (general vs subject-domain; subject-domain-training test).
- **Same labels across A1 sub-fields** for default-propagation.
- **Conservative-bias-for-reader-axes principle** noted (LOWER default).
- **Receptive-only constraint** strictly maintained.
- **Migration mapping from existing AUDIENCE_LEVEL** suggested.
- **All 8 surfacing frontier flags resolved** or explicitly handed off.

### Frontier flags handed to Decomposition

- **D1.** Per-level prose structure — sentence count, paragraph organization, formatting conventions.
- **D2.** Should example sets include both positive (at-level) and negative (above-level) examples?
- **D3.** Should each level include an "anchor reader profile" that's a real, recognizable demographic?
- **D4.** Should boundary-pair examples (at each adjacent-level transition) be explicit deliverables?
- **D5.** Should the spec include an A1↔A2 borderline-words table (with explicit classification for edge cases like `eschatology`, `transubstantiation`)?
- **D6.** How are the 4 components per level organized in the final spec (e.g., sub-headings, table layout, or running prose)?

### Saturation indicators

- **Perspective saturation:** Phase / Calibration-State perspective (conservative-bias for reader-axes) produced NEW anchor type. Earlier perspectives produced new types (Technical → 4-component schema; Strategic → language-stability; Risk → boundary tests). No premature saturation.
- **Ambiguity resolution ratio:** 8/8 ambiguities resolved.
- **SV delta:** SV6 differs structurally from SV1 in 4-component pattern, explicit A1↔A2 boundary, conservative-bias interpretation, same-labels-across-sub-fields default propagation, and migration mapping suggestion. Substantial shift.
- **Anchor diversity:** anchors from all 5 types (10 constraints; 10 key insights; 6 structural points; 5 principles; 6 meaning-nodes) and from 8 perspectives. Diverse.

All four indicators show sufficiency. Model is stable; ready for decomposition.
