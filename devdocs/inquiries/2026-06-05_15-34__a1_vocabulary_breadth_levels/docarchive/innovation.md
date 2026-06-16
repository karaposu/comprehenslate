# Innovation — a1_vocabulary_breadth_levels

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/_branch.md` (with prior outputs: `surfacing.md`, `sensemaking.md`, `decomposition.md` in the same folder)

---

## Phase 1 — Seed

### Methodology-Mode Consideration

**Inherited mode** (from seed framing): **Standard default** (balanced 4G + 3F).

The seed framing is the decomposition's "Frontier handed to Innovation" — 7 content-generation points within a structural frame already settled at sensemaking SV6. Innovation operates in Production-task mode (generating text per piece). Each generation point is **content-production** (not meta-decision) per the Meta-Decision-Piece Criterion: no relationship-label, framing-semantic, lesson-vocabulary, evaluation-criterion, or intervention-shape commitment is being newly introduced. The Piece-Level Inversion Rule does not fire for content-production pieces.

**Alternative mode considered:** **Generator-weighted exploration.**

**What follows under the alternative:** Generator-weighted (4 Generators dominant; Framers light) would yield more candidate example words per level/boundary. The risk: less Framer-level edge-case testing ("would this example FAIL at this level under some plausible condition?").

**Decision:** **Standard default.** The 7 content-generation points need both Generators (to enumerate concrete words) and Framers (to test against the receptive-only constraint, language-agnosticism, and the LLM-readability lens).

### Seeds (one per content-generation point from decomposition)

| # | Seed |
|---|---|
| S1 | Per-level prose wording for each of 5 levels (P3.1–P3.5) |
| S2 | Per-level positive example sets (5–7 English words per level) |
| S3 | Per-level negative example sets (3–5 English words above each level) |
| S4 | Adjacent-level boundary-pair examples (4 boundaries; 3–5 pairs each) |
| S5 | A1↔A2 borderline-words table content (P5b) |
| S6 | Migration mapping rationale (P6; 3 entries) |
| S7 | Anchor demographic alternatives (P3.X reader profiles; 2–3 per level) |

---

## Phase 2 — Generate

### Generator 1: Combination

**Generic.** Combine reader-profile name + frequency-tier band + register-tier inclusion + substitution-test sketch for each level — the 4-component template instantiated into concrete prose.

**Focused.** Combine English register-tier markers (Latinate vs Germanic) with specific word selection. At conversational: words common in newspapers AND in educated speech (`purchase`, `endeavor`, `consider`, `approximately`). At advanced: words common in academic writing but rare in conversation (`ratiocination`, `ostensibly`, `contingent`, `putative`).

**Contrarian.** Combine the substitution-test logic with translation-pair enumeration — for each adjacent-level boundary, what's the PAIR of words that swap during translation? `purchase` (conversational) ↔ `buy` (daily); `endeavor` ↔ `try`; `ratiocination` ↔ `reasoning`. These pairs become CC-D below.

### Generator 2: Absence Recognition

**Patch-level (missing examples).** Sensemaking's only worked example is the user's `ratiocination/ostensibly vs reasoning/apparently` pair. Missing: ~25-35 positive examples (5 levels × 5–7 each) + ~15-20 negative examples + ~12-20 boundary pairs. These need explicit enumeration.

**Patch-level (missing borderline cases).** The spec's A1↔A2 borderline-words table is structurally committed but content-empty. Generate ~15-20 borderline words across domains: medicine (myocardial infarction, hematuria, parenchyma), law (habeas corpus, mens rea, estoppel), theology (transubstantiation, eschatology, kenosis), philosophy (epistemology, phenomenology, hermeneutics), science (entropy, mitosis, isotope).

**Redesign-level (from-scratch translation context).** If the spec were designed from scratch today for a TRANSLATION SYSTEM (rather than a language-teaching framework), it would want per-level WORD-PAIR SUBSTITUTION CANDIDATES that the translator-AI uses at runtime. The spec currently has substitution-test SKETCHES (general guidance) but no per-word substitution pairs. The pairs are partly captured in CC-D boundary pairs — direction of translation = "at level L, replace high-side with low-side." This is implicit in the design.

**Bidirectional (present-in-different-form).** The project ALREADY has the `.env.example` AUDIENCE_LEVEL knob with 3 levels (`native | late_learner | late_learner_simple`). These are partial-form vocabulary level labels. The new 5-level structure articulates what was implicit; the existing knob is the predecessor.

### Generator 3: Domain Transfer

**Native-domain source — CEFR vocabulary mapping.** Common European Framework of Reference vocabulary sizes (receptive):
- A1 ~500–700 words
- A2 ~1000–1500 words
- B1 ~2000–2500 words
- B2 ~4000 words
- C1 ~8000 words
- C2 ~16000+ words

Map to the inquiry's 5 levels:
- `very_basic` ≈ CEFR A1 (~500–1000 words)
- `daily` ≈ CEFR A2–B1 boundary (~2000–3000)
- `conversational` ≈ CEFR B1–B2 (~3500–7000)
- `advanced` ≈ CEFR B2–C1 (~8000–20000)
- `native` ≈ CEFR C2+ (full general vocabulary)

**Native-domain source — ACTFL proficiency descriptors.** ACTFL has exactly 5 levels (Novice / Intermediate / Advanced / Superior / Distinguished). The vocabulary descriptors align:
- `very_basic` ≈ ACTFL Novice ("limited memorized vocabulary")
- `daily` ≈ ACTFL Intermediate ("concrete everyday vocabulary for survival situations")
- `conversational` ≈ ACTFL Advanced ("vocabulary for narrative and description across topics")
- `advanced` ≈ ACTFL Superior ("precise vocabulary including abstract")
- `native` ≈ ACTFL Distinguished ("sophisticated vocabulary across genres including archaic")

**Deliberately-different source — Graded readers (Penguin / Oxford Bookworms).** 6 stages with headword limits:
- Stage 1 ~300 headwords ≈ `very_basic`
- Stage 2–3 ~600–1000 ≈ `daily`
- Stage 4 ~1400 ≈ borderline `daily`/`conversational`
- Stage 5 ~1800 ≈ `conversational`
- Stage 6 ~2500 + unabridged ≈ `advanced`
- Unabridged literature ≈ `native`

**Deliberately-different source — Reading level metrics (Lexile / grade levels).** Gives anchor demographics:
- `very_basic` ≈ K–1 grade reader / brand-new ESL learner
- `daily` ≈ grade 3–5 reader / functional ESL adult
- `conversational` ≈ grade 8–10 reader / average newspaper reader
- `advanced` ≈ grade 12+ reader / university-educated
- `native` ≈ educated native who reads literary fiction comfortably

### Generator 4: Extrapolation

**Generic (1-year horizon).** When Comprehenslate adds Russian / Japanese / Arabic, the level CONCEPTS hold; examples need per-language equivalents. The English examples produced now become canonical English-illustrative references that future per-language inquiries cite when defining their own examples.

**Focused (5-year horizon).** LLM judgment of "is this word at level X?" will become more reliable. The spec's anchor examples become training-context examples for the LLM. Implication: ensure examples are CANONICAL and CLEAR (uncontroversial belongings at their level), not edge cases the LLM might mis-judge. The A1↔A2 borderline-words table (CC-E) explicitly handles edge cases separately.

**Contrarian (10-year horizon).** LLM-direct lexical choice may replace explicit level-tagging — the LLM consumes the prose description and chooses appropriate vocabulary without consulting a per-word level lookup. The spec becomes documentation rather than runtime guidance. Doesn't change the inquiry's content.

### Framer 1: Lens Shifting

**Generic — non-native English reader lens.** Some "obviously native-level" words (`anon`, `whilom`, `gainsay`) are unfamiliar even to high-A1 non-native readers. This makes them GOOD native-level positive examples — they reliably distinguish native readers from advanced.

**Focused — developer-reading-the-pydantic-schema lens.** Examples must work as `Literal` values: no spaces, no special characters in label keys. The labels `very_basic | daily | conversational | advanced | native` work (snake_case-compatible). PASS.

**Contrarian — LLM-agent-reading-the-prose lens.** The LLM needs CLEAR anchor examples to ground judgment. Edge cases like `eschatology` should be marked explicitly as A1↔A2 borderline (could go either way), not buried in either category. The borderline-words table (CC-E) handles this.

### Framer 2: Constraint Manipulation

**ADD constraint — "Every very_basic example must include FUNCTION words AND CONTENT words separately."** At very_basic, function words (the, is, has, of, do) and content words (food, water, house, person) both belong; the distinction sharpens the level. Apply to CC-B P3.1.

**ADD constraint — "Every adjacent boundary-pair must include AT LEAST ONE Latinate↔Germanic example."** This catches the English register-shift signature. P4.2 (daily↔conversational) and P4.3 (conversational↔advanced) both satisfy: P4.2 = `buy↔purchase`, `try↔endeavor`; P4.3 = `apparently↔ostensibly`, `reasoning↔ratiocination`.

**REMOVE constraint — "Examples must be commonly used in 21st-century English."** When removed, archaic words like `verily`, `anon`, `whilom`, `wherefore` become native-level positive examples (not negative). This is what sensemaking already committed to (A1.native includes archaic).

**REMOVE constraint — "Examples must be English."** When removed, per-language equivalents become possible — but that's the next inquiry. This inquiry's examples STAY English-illustrative.

### Framer 3: Inversion

**Level 1 (component-level).** "Words at this level are EASY" → "Words at this level are EXACTLY the words the translator would HESITATE to use above this level." Substitution-test inversion: the EXAMPLES at each level are the boundary cases for the level ABOVE.

**Level 2 (system-level).** "Examples are concrete words" → "Examples are SUBSTITUTION CHOICES" — what gets swapped for what. This shifts the example representation from single words to word-pairs, generating the boundary-pair examples (CC-D).

**Level 3 (root-cause-level).** "The spec lists EXAMPLES" → "The spec lists FORMS OF JUDGMENT" — at each level, what KIND of words does the translator avoid? At `daily`: avoid Latinate. At `conversational`: avoid academic-rare. At `advanced`: avoid archaic. At `native`: avoid specialist-domain. This generalized substitution-test logic is captured in each level's Component 4 (substitution-test sketch).

**Multi-axis existence-axis.** "5 levels" → "Could the count be 3?" Tested at the prior inquiry (sensemaking SV6 committed 5 levels); no re-test needed here.

---

## Inherited Frame Audit

### Seed-level central assumption

**"The 5 levels are correct and need content (examples + prose) to instantiate."** Inherited from sensemaking SV6 + the user's input.

### Challenge scan

Does any candidate explicitly challenge this assumption? The structural commitments were tested at the prior inquiry's innovation stage (5-axis vs 4-axis collapse) and at this inquiry's sensemaking stage (8 ambiguities resolved). Re-litigating here would be redundant.

The inquiry's content-generation seeds are downstream of the structural commitments. No piece in this inquiry introduces a new meta-decision; each piece instantiates a frame committed elsewhere. **Audit DOES NOT FIRE at seed level.**

### Piece-level commitments

| Piece | Meta-decision property fires? | Verdict |
|---|---|---|
| P1 cross-cutting constraints | No new commitments; references prior-finding constraints | Content-production |
| P2 4-component template | Structural commitment from decomposition; instantiated here | Content-production (template structure was meta-decision at decomposition stage, not here) |
| P3.1–P3.5 per-level specs | Instantiations of P2; content-production | Content-production |
| P4.1–P4.4 boundary pairs | Content-production | Content-production |
| P5a A1↔A2 boundary test | Already settled at sensemaking | Content-production |
| P5b borderline-words table | Content-production | Content-production |
| P6 migration mapping | Content-production | Content-production |
| P7 scope | Settled at decomposition | Not relevant for innovation |

No piece fires any of the 5 meta-decision-piece properties. **Audit DOES NOT FIRE at piece level.**

Piece-Level Inversion Rule and Intervention-Shape-Axis Inversion are not triggered.

---

## Phase 3 — Test

The content generation produces 7 candidate clusters. Each cluster is run through the 5-test cycle.

### Cluster CC-A — Per-level prose drafts (5 drafts)

The drafts instantiate the P2 4-component template per the cross-cutting constraints from P1. Below is the proposed prose for each level; critique selects or refines.

**P3.1 — `very_basic`**
> Reader profile: a young child reading early-reader books, or a brand-new second-language learner in their first weeks — someone who recognizes only the most everyday core vocabulary of the target language: function words, basic verbs, and the most common concrete nouns. Does not recognize Latinate, abstract, academic, literary, archaic, or specialist vocabulary.
>
> Frequency tier (English-illustrative): top ~500–1000 most frequent words. Roughly CEFR A1.
>
> Register tier: only everyday core. Excludes Latinate, abstract, academic, literary, archaic, and specialist registers.
>
> Substitution-test sketch: the translator replaces almost everything above the core band with descriptive paraphrase or simpler equivalents. `consider` becomes `think about`; `decision` becomes `what to do`; `purchase` becomes `buy`.

**P3.2 — `daily`**
> Reader profile: a functional adult in daily life — a backpacker carrying out transactions in a foreign country, a new immigrant functioning in their second language, an L2 learner who has been in-country a few months. Recognizes everyday concrete and simple abstract vocabulary; does not recognize Latinate, academic, literary, archaic, or specialist register.
>
> Frequency tier (English-illustrative): top ~2000–3000 most frequent words. Roughly CEFR A2–B1.
>
> Register tier: everyday concrete + simple abstract. Excludes Latinate (`purchase`, `endeavor`, `consider`), academic, literary, archaic, specialist.
>
> Substitution-test sketch: the translator replaces Latinate alternatives with Germanic everyday equivalents. `purchase` becomes `buy`; `endeavor` becomes `try`; `ostensibly` becomes `seemingly` or `it looks like`; `consider` becomes `think about`.

**P3.3 — `conversational`**
> Reader profile: an average educated adult who carries informed informal conversation and reads newspapers and mainstream non-fiction comfortably. Recognizes common Latinate vocabulary in educated speech (`purchase`, `consider`, `endeavor`, `approximately`) but does not read dense academic prose or literary-archaic vocabulary.
>
> Frequency tier (English-illustrative): top ~5000–7000 words including common Latinate. Roughly CEFR B1–B2.
>
> Register tier: everyday + conversational-educated + journalistic. Includes common Latinate. Excludes dense academic (`ratiocination`, `ostensibly`), literary-archaic (`verily`, `anon`), dialectal, and specialist.
>
> Substitution-test sketch: the translator keeps common Latinate without substitution but avoids dense academic, archaic, dialectal, and specialist vocabulary. `ratiocination` becomes `reasoning`; `ostensibly` becomes `apparently`; `verily` becomes `truly`.

**P3.4 — `advanced`**
> Reader profile: a university-educated reader, a skilled non-native who reads widely across academic and literary genres, or an educated professional. Recognizes academic vocabulary (`ratiocination`, `epistemic`, `contingent`) and general literary vocabulary (`ineffable`, `putative`, `ostensibly`). Does not necessarily recognize archaic forms (`verily`, `anon`, `whilom`), dialectal vocabulary, or subject-domain specialist vocabulary (`myocardial infarction`, `habeas corpus` — these are A2 territory).
>
> Frequency tier (English-illustrative): top ~10000–20000 words including academic and literary. Roughly CEFR B2–C1.
>
> Register tier: everyday + conversational + journalistic + academic + general literary. Excludes archaic, dialectal, and specialist-rare general.
>
> Substitution-test sketch: the translator avoids only archaic (`verily` → `truly`, `anon` → `soon`), dialectal, and specialist-rare general vocabulary. Academic and literary register is kept. The translator may use technical vocabulary if it is general-educated (`hypothesis`, `epistemic`) but not subject-domain specialist (see the A1↔A2 boundary section).

**P3.5 — `native`**
> Reader profile: an educated native speaker who reads broadly across genres including literary fiction, historical texts, and rare literary registers. Recognizes archaic vocabulary (`verily`, `anon`, `whilom`, `thee`, `withal`), dialectal forms encountered in fiction, and literary-rare general vocabulary. Does NOT necessarily recognize subject-domain specialist vocabulary requiring field training (`myocardial infarction`, `habeas corpus`, `transubstantiation` — these are A2 territory).
>
> Frequency tier (English-illustrative): full general vocabulary (no upper bound on rarity within the general lexicon). Roughly CEFR C2+.
>
> Register tier: ALL general registers including archaic, dialectal, literary-rare.
>
> Substitution-test sketch: the translator avoids ONLY A2 specialist domain vocabulary (medical, legal, theological-specialist). All general vocabulary including archaic and dialectal is kept — `verily` stays as `verily`; `anon` stays as `anon`. The A1↔A2 boundary (see that section) determines when to substitute or footnote specialist vocabulary.

**5-test verdicts on CC-A:**
| Test | Verdict | Reasoning |
|---|---|---|
| Novelty | PASS (moderate) | Instantiations of the template; not radical novelty but newly written for this spec |
| Scrutiny survival | PASS | All drafts use recognition verbs (`recognizes`, `understands`, `does not recognize`); no productive verbs slip in. Honors P1 receptive-only constraint |
| Fertility | PASS | Ready for direct insertion into the finding |
| Actionability | PASS | Each draft is immediately usable |
| Mechanism independence | PASS | Generated via Combination (reader-profile + frequency-band + register-tier + substitution-test) + Domain Transfer (CEFR + ACTFL grounding) + Inversion (substitution-test as forms-of-judgment). 3 independent mechanisms converge per draft |

**Disposition: ACTIONABLE.**

---

### Cluster CC-B — Per-level POSITIVE example sets

**P3.1 — `very_basic` positive examples:**
- Function words: `the`, `is`, `has`, `do`, `of`
- Content words: `go`, `eat`, `work`, `house`, `food`, `water`, `person`

**P3.2 — `daily` positive examples:**
- `decide`, `remember`, `carry`, `important`, `problem`, `simple`, `difficult`, `understand`, `area`

**P3.3 — `conversational` positive examples:**
- `purchase`, `endeavor`, `consider`, `approximately`, `apparently`, `generally`, `decision`, `essential`, `establish`

**P3.4 — `advanced` positive examples:**
- `ratiocination`, `ostensibly`, `ameliorate`, `contingent`, `putative`, `ineffable`, `epistemic`, `hermetic`, `prescient`

**P3.5 — `native` positive examples:**
- `verily`, `anon`, `thee`, `whilom`, `gainsay`, `withal`, `perchance`, `forsooth`, `wherefore`

**5-test verdicts on CC-B:**
| Test | Verdict |
|---|---|
| Novelty | PASS (moderate) — concrete enumeration |
| Scrutiny survival | PASS — each example genuinely fits its level (verified via frequency-band check + register-tier check) |
| Fertility | PASS — anchor examples for both LLM judgment and user understanding |
| Actionability | PASS |
| Mechanism independence | PASS — drawn from Combination (level × example) + Domain Transfer (CEFR ranges + ACTFL descriptors + graded readers). 3 mechanisms |

**Disposition: ACTIONABLE.**

---

### Cluster CC-C — Per-level NEGATIVE example sets

Words ABOVE each level (the translator AVOIDS these at the named level):

**P3.1 — `very_basic` negatives:** `consider`, `decision`, `approximate`, `apparently`, `ratiocination`.

**P3.2 — `daily` negatives:** `purchase`, `endeavor`, `consider`, `ostensibly`, `ratiocination`.

**P3.3 — `conversational` negatives:** `ostensibly`, `ratiocination`, `ameliorate`, `verily`, `whilom`.

**P3.4 — `advanced` negatives:**
- A1.native vocabulary (above advanced): `verily`, `anon`, `whilom`
- A2 specialist (to clarify A1↔A2 boundary at this level): `myocardial infarction`, `transubstantiation`

**P3.5 — `native` negatives** (A2 specialist domain vocabulary):
- `myocardial infarction` (medical)
- `habeas corpus` (legal)
- `transubstantiation` (Catholic theology)
- `kenosis` (Christian theology)
- `ontogenesis` (biology)

**5-test verdicts on CC-C:**
| Test | Verdict |
|---|---|
| Novelty | PASS (low-moderate) |
| Scrutiny survival | PASS — each negative is genuinely above its named level |
| Fertility | PASS — pairs with positives to bracket each level |
| Actionability | PASS |
| Mechanism independence | PASS |

**Disposition: ACTIONABLE.**

---

### Cluster CC-D — Boundary-pair examples

**P4.1 — `very_basic` ↔ `daily`** (core/function → functional everyday content):
- `go` ↔ `decide`
- `food` ↔ `meal`
- `work` ↔ `job`
- `house` ↔ `apartment`
- `tell` ↔ `explain`

**P4.2 — `daily` ↔ `conversational`** (functional everyday → educated-informal / Latinate enters):
- `buy` ↔ `purchase`
- `try` ↔ `endeavor`
- `think about` ↔ `consider`
- `about` ↔ `approximately`
- `clearly` ↔ `apparently`

**P4.3 — `conversational` ↔ `advanced`** (conversational-educated → written-educated / academic):
- `apparently` ↔ `ostensibly`
- `reasoning` ↔ `ratiocination`
- `improve` ↔ `ameliorate`
- `depending on` ↔ `contingent on`
- `supposed` ↔ `putative`

**P4.4 — `advanced` ↔ `native`** (modern educated → all-general including archaic / dialectal):
- `truly` ↔ `verily`
- `soon` ↔ `anon`
- `you` (singular) ↔ `thee`
- `formerly` ↔ `whilom`
- `also` ↔ `withal`

**5-test verdicts on CC-D:**
| Test | Verdict |
|---|---|
| Novelty | PASS (moderate) — each pair illustrates the named transition concretely |
| Scrutiny survival | PASS — each pair is a real translation choice the translator makes at the named boundary |
| Fertility | PASS — anchor examples for boundary judgment |
| Actionability | PASS |
| Mechanism independence | PASS — generated via Combination + Inversion (substitution-test) + Domain Transfer (English register theory) |

**Disposition: ACTIONABLE.**

---

### Cluster CC-E — A1↔A2 borderline-words table

| Word | Classification | Reasoning |
|---|---|---|
| `ratiocination` | A1.advanced | General Latinate from rhetoric/logic; no domain training; appears in literary writing |
| `ostensibly` | A1.advanced | General Latinate; common in educated writing |
| `ameliorate` | A1.advanced | General Latinate; literary and policy-discussion vocabulary |
| `contingent` | A1.advanced | General academic; cross-disciplinary; appears in everyday educated speech |
| `epistemic` | A1.advanced | Borderline; appears in non-specialist philosophy writing and general "epistemic humility"-type usage |
| `verily` | A1.native | Archaic general; King James Bible-era English; recognized by literary-fiction readers |
| `anon` | A1.native | Archaic general |
| `whilom` | A1.native | Archaic literary; recognized by historical-fiction readers |
| `thee` / `thou` / `thy` | A1.native | Archaic pronouns; Shakespeare, KJV |
| `gainsay` / `withal` / `perchance` | A1.native | Archaic literary general |
| `eschatology` | A2 (theology specialist) — A1.native for unusually broad readers | Borderline; mostly theology specialist; well-read general readers may know it |
| `transubstantiation` | A2 Catholic theology specialist | Requires Catholic-theology training |
| `myocardial infarction` | A2 medical specialist | Requires medical training; general readers know "heart attack" |
| `habeas corpus` | A2 legal specialist | Requires legal training |
| `kenosis` | A2 Christian theology specialist | Requires theology training |
| `phenomenology` | A2 philosophy specialist | Requires philosophy training |
| `epistemology` | A2 philosophy specialist (or A1.native for broad readers) | Borderline; less specialist than phenomenology; appears in non-philosophy contexts |
| `entropy` | A1.advanced/native (commonsense) — A2 physics for technical-precise sense | Borderline; commonly-known concept in non-technical use |
| `mitosis` | A2 biology specialist | Requires biology training |
| `isotope` | A2 chemistry specialist | Requires science training |

**Note on borderline cases.** Words like `eschatology`, `epistemology`, `entropy` sit at the A1.native / A2 boundary. The classification depends on context: in a Catholic-theology text, `eschatology` is A2 (requires the surrounding domain); in a broadly-read general text, A1.native readers recognize it. The recommendation: when classification is genuinely borderline, prefer A2-default (treat as requiring domain knowledge) to be conservative.

**5-test verdicts on CC-E:**
| Test | Verdict |
|---|---|
| Novelty | PASS — concrete enumeration with reasoning per entry |
| Scrutiny survival | PASS — borderline cases explicitly flagged; A2-default rule stated |
| Fertility | PASS — extends to novel cases via the subject-domain-training test |
| Actionability | PASS — table is directly usable in the spec |
| Mechanism independence | PASS — generated via Absence Recognition (patch-level enumeration) + Domain Transfer (multiple specialist fields) |

**Disposition: ACTIONABLE.**

---

### Cluster CC-F — Migration mapping rationale

- **`late_learner_simple → daily`.** The existing label `late_learner_simple` suggests a reader who needs simplification beyond ordinary late-learner level. This best matches `daily` — a functional adult who can handle daily life vocabulary but not Latinate, academic, or literary register. The match is the closest semantic neighbor among the new 5 levels.

- **`late_learner → conversational`.** The existing label `late_learner` suggests a second-language adult who is still building fluency but is past survival level. This matches `conversational` — an educated adult who handles informed conversation including common Latinate vocabulary. The cleanest of the three mappings.

- **`native → native`.** Direct identity mapping. Both labels refer to readers with educated native-speaker vocabulary breadth.

**New positions introduced by the 5-level scheme:**
- `very_basic` extends BELOW `late_learner_simple` to cover children and brand-new learners (a reader profile the existing 3-level scheme could not address).
- `advanced` fills the gap BETWEEN `late_learner` (`→ conversational`) and `native` to cover university-educated readers and skilled non-natives who handle academic and literary register but not necessarily archaic (a reader profile the existing scheme conflated with `native`).

**5-test verdicts on CC-F:**
| Test | Verdict |
|---|---|
| Novelty | PASS (low) — fills in rationale |
| Scrutiny survival | PASS — rationale is plausible per label; new-position rationale explains the spectrum extension |
| Fertility | PASS — enables future migration work |
| Actionability | PASS |
| Mechanism independence | PASS — primarily Combination (existing labels × new labels × semantic matching) |

**Disposition: ACTIONABLE.**

---

### Cluster CC-G — Anchor demographic alternatives

**P3.1 — `very_basic`**
- Primary: a small child reading early-reader books / a brand-new ESL learner in their first weeks
- Alt 1: a child age 4–6 learning to read in L1 / an absolute-beginner L2 learner
- Alt 2: an L2 learner in their first 1–2 weeks of immersion

**P3.2 — `daily`**
- Primary: a backpacker carrying out daily transactions in a foreign country
- Alt 1: a new immigrant functioning in their second language
- Alt 2: a casual L2 learner who has been in-country a few months

**P3.3 — `conversational`**
- Primary: an average newspaper-reading adult / casual reader of mainstream non-fiction
- Alt 1: a high-school-educated adult with workplace literacy
- Alt 2: a competent second-language reader at upper-intermediate level (CEFR B1–B2)

**P3.4 — `advanced`**
- Primary: a university-educated professional reader
- Alt 1: a skilled non-native reader of literary fiction
- Alt 2: a humanities graduate student / well-read amateur literary critic

**P3.5 — `native`**
- Primary: an educated native speaker who reads literary fiction and historical texts comfortably
- Alt 1: a literature scholar / English-major academic
- Alt 2: a broadly-read native speaker who enjoys archaic-language fiction (readers of Tolkien, the King James Bible, Shakespeare)

**5-test verdicts on CC-G:**
| Test | Verdict |
|---|---|
| Novelty | PASS (low-moderate) |
| Scrutiny survival | PASS with one refinement note — the previous draft Alt 2 at very_basic was "person with severe reading-difficulty," which conflates vocabulary-breadth with reading-difficulty (different axes); replaced with "L2 learner in first 1–2 weeks of immersion" |
| Fertility | PASS — helps users identify their reader |
| Actionability | PASS |
| Mechanism independence | PASS — Combination (level × real demographic) |

**Disposition: ACTIONABLE.**

---

### Axis coverage check

The candidate set varies along:
- **Level axis** (5 levels: very_basic / daily / conversational / advanced / native)
- **Boundary axis** (4 adjacent-level boundaries + A1↔A2 boundary)
- **Word-type axis** (function vs content; Germanic vs Latinate; archaic vs modern; specialist vs general)
- **Reader-demographic axis** (multiple per level)
- **Domain axis** (medicine / law / theology / philosophy / science / archaic-literary in the A1↔A2 table)

Good axis coverage. **PASS.**

### Per-row mechanism-trace

Each piece with content-generation needs has at least one mechanism applied:
- P1 cross-cutting → not new content this inquiry (inherited from prior + decomposition)
- P2 template → addressed via Domain Transfer (CEFR/ACTFL template patterns) + Combination
- P3.1–P3.5 prose → addressed via Combination + Domain Transfer + Inversion (CC-A above)
- P3.1–P3.5 positive examples → Combination + Domain Transfer (CC-B above)
- P3.1–P3.5 negative examples → Combination + Domain Transfer (CC-C above)
- P3.1–P3.5 demographics → Combination + Domain Transfer (CC-G above)
- P4.1–P4.4 boundary pairs → Combination + Inversion + Domain Transfer (CC-D above)
- P5b borderline-words table → Absence Recognition + Domain Transfer (CC-E above)
- P6 migration rationale → Combination (CC-F above)
- P7 scope → settled at decomposition; not innovation territory

All content-generation pieces traced. **PASS.**

### Mechanism Independence — Shared-input detection

Convergences identified:
- **Per-level positive examples** reach the same answer via CEFR ranges + ACTFL descriptors + graded readers + register theory. These are RELATED but INDEPENDENT vocabulary frameworks (CEFR is European receptive; ACTFL is American spoken-fluency; graded readers are pedagogical). The convergence is INDEPENDENT.
- **Boundary pairs** reach the same answer via Combination (concrete enumeration) + Inversion (substitution-test logic) + Domain Transfer (English register theory). Three independent grounds. INDEPENDENT.
- **A1↔A2 borderline cases** reach the same answer via Absence Recognition (what edge cases need classification) + Domain Transfer (multiple specialist fields with internal classification logic). Two independent grounds. INDEPENDENT.

No spurious convergence detected. **PASS.**

---

## Assembly Check

### Emergent assembly E1 — The COMPLETE LEVEL SPEC

Combining CC-A prose + CC-B positives + CC-C negatives + CC-G demographics for each level produces a complete per-level spec entry. Tested against the inquiry's purpose: yes, this assembly is the deliverable for each of P3.1–P3.5.

**Disposition: ACTIONABLE.** This is what the finding presents per level.

### Emergent assembly E2 — The COMPLETE VOCABULARY-BREADTH SPEC

Combining E1 (× 5 levels) + CC-D (× 4 boundaries) + CC-E table + CC-F migration rationale + P1 cross-cutting + P2 template produces the complete spec deliverable.

**Disposition: ACTIONABLE.** This is the finding's content.

No emergent candidates beyond piece-assembly. The content directly fills the structural frame committed at sensemaking + decomposition.

---

## Mechanism Coverage Telemetry

- **Generators applied:** 4/4 (Combination, Absence Recognition, Domain Transfer, Extrapolation)
- **Framers applied:** 3/3 (Lens Shifting, Constraint Manipulation, Inversion)
- **Total candidate clusters produced:** 7 (CC-A through CC-G), each with multiple sub-items
- **Convergence:** YES — at least 3 mechanisms converge on per-level positive examples and on boundary pairs
- **Survivors tested:** 7/7
- **Inherited Frame Audit:** PASSED (seed-level and piece-level commitments inherited from sensemaking SV6 and decomposition; no new meta-decisions introduced)
- **Failure modes observed:** None
  - NOT Premature Evaluation
  - NOT Single-Mechanism Trap (4G + 3F applied)
  - NOT Early Frame Lock (multiple mechanisms applied per cluster)
  - NOT Innovation Without Grounding (every cluster 5-test cycled)
  - NOT Mechanism Exhaustion
  - NOT Survival Bias (one minor refinement noted at CC-G very_basic Alt 2)
- **Per-piece Inversion compliance** (Production-task mode telemetry): N/A — no meta-decision pieces fired the rule

**Overall: PROCEED.**

---

## Handoff to Critique

Critique should adjudicate:

1. **Per-level prose drafts (CC-A).** For each of P3.1–P3.5, verify the prose honors receptive-only + language-agnostic + same-labels + substitution-test concept constraints. Approve or refine.

2. **Per-level positive examples (CC-B).** For each of P3.1–P3.5, verify each English example genuinely sits at the named level. Reject any false-positives (words actually above/below).

3. **Per-level negative examples (CC-C).** For each of P3.1–P3.5, verify each English example is genuinely above the named level.

4. **Boundary pairs (CC-D).** For each of P4.1–P4.4, verify each pair genuinely illustrates the transition with the low-side at the lower level and the high-side at the higher.

5. **A1↔A2 borderline-words table (CC-E).** Verify each entry's classification with reasoning. Flag any controversial classifications for user review.

6. **Migration mapping rationale (CC-F).** Verify rationale is plausible for each of the 3 mapping entries.

7. **Anchor demographics (CC-G).** Verify each alternative is operationalizable and culturally neutral. The previous draft's "severe reading-difficulty" demographic was refined; check the replacement.

8. **The Assembly (E2).** Test the full assembled spec against the inquiry's purpose: does it answer "what should the 5 levels for vocabulary-breadth be, with logic and examples"? YES expected.
