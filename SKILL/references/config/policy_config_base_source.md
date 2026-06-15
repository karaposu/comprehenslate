# Comprehenslate Policy Layer — LLM Calibration Context

This document is the prompt context the translator-AI reads to interpret Policy-class instances from `schemas.py`. Each Policy-class section makes the **full spectrum** of `Literal[N]` values visible so a single chosen value (e.g. `HonorificsPolicy.policy = "translate-meaning"`) calibrates against its neighbors. Per-value definitions distinguish each value from the ones immediately adjacent on the preserve↔replace spectrum, with concrete Said Nursi anchors and cross-cultural examples wherever applicable.

**Companion to `config_base_source.md`.** That document calibrates the 8 axes of `TranslationConfig` (TC) — the user's broad strategy choices. This document calibrates the **Policy layer** — per-edge-case `Literal[N]` enums for recurring authorial value judgments. `PipelineConfig` (PC) — runtime engine knobs — is calibrated separately at integration time.

The 7 Policy classes adopted in `schemas.py`:

| # | Policy class | Edge case it governs | Values | Default |
|---|---|---|---|---|
| 1 | NonMainLangPartsPolicy | Non-main language quotes, mentions, references inside the source text | 5 | `preserve-original-and-add-translation-as-a-note` |
| 2 | SourceApparatusPolicy | Author's pre-existing apparatus (marginalia, glosses, hashiye) | 4 | `translate-as-footnote` |
| 3 | VoiceMarkingPolicy | Transitions between author voice and cited / student voices | 5 | `as-in-original` |
| 4 | ArchaicRegisterPolicy | Archaic source-language **register** (old vocabulary, syntax, idiom feel) | 4 | `hybrid-by-register-domain` |
| 5 | HonorificsPolicy | Theological honorifics that follow names | 5 | `transliterate-with-original` |
| 6 | FormulaicOpeningPolicy | Formulaic openings (invocations, basmala, dedicatory formulae) | 4 | `preserve-original-with-translation` |
| 7 | EmbeddedPoetryPolicy | Embedded poetry, distinct from prose embedded language | 4 | `preserve-original-with-prose-gloss` |

Four candidate policies are catalogued in this document but **not yet adopted** in `schemas.py` (see §Candidate Policies below): `TransliterationStandardPolicy`, `PriorTranslationStancePolicy`, `AnachronismHandlingPolicy`, `CitationReferenceFormatPolicy`.

---

## Cross-cutting principles

### FP2 — *"Don't declare what the LLM can infer."*

A schema field belongs in `schemas.py` only when the LLM cannot derive its value from the source text plus the rest of the configuration. The Policy layer specifically holds the **user's value judgments** about recurring authorial edge-cases. The LLM detects the phenomenon (an embedded ayah; a Mevlana couplet; a hashiye; an honorific); the user decides handling (preserve / replace / annotate / use famous rendering). FP2 is the membership test for Policy classes.

### Four filters per Policy class

Each adopted Policy class passes all four filters:

1. **Structural shape** — single-field `BaseModel` with a `Literal[N]` enum.
2. **Language-agnosticism** — enum literals never name a specific language, tradition, or corpus.
3. **Authorial edge-case category** — the phenomenon is something the author did (not translator-side, publication-side, or reader-side).
4. **LLM-can't-infer** — the handling decision is a human value judgment, not an inference.

### Co-application

**Policy classes co-apply per text span.** A Bismillah is BOTH a formulaic opening (governed by `FormulaicOpeningPolicy`) AND a non-main-language phrase (governed by `NonMainLangPartsPolicy`); both policies' values apply to their respective concerns without conflict. A Mevlana couplet is BOTH embedded poetry (governed by `EmbeddedPoetryPolicy`) AND a non-main-language phrase (governed by `NonMainLangPartsPolicy`); same independent co-application. The Policy classes do not compete; each governs its own concern.

### Preserve↔Replace spectrum (general pattern)

Most Policy classes lie on a spectrum from highest-preservation to highest-domestication / lowest-preservation:

- **Preserve-original baseline** — the source is preserved as-is, with whatever minimum additional context the value adds.
- **Preserve-with-translator-help** — the source is preserved alongside translator-provided assistance (gloss, note, footnote).
- **Replace-with-translation** — the source is replaced by the translator's rendering; the original may or may not be retained in apparatus.
- **Replace-with-established-rendering** — the source is replaced by an existing famous/canonical rendering rather than a new translation.
- **Drop** — the phenomenon is omitted entirely (the most aggressive end).

The default for most Policy classes lies in the **preserve-with-translator-help** region — faithful to source while remaining accessible.

### Cross-axis interaction with TC

The Policy layer composes with `TranslationConfig`:

- **A4 `purpose`** typically influences sensible defaults (a `scholarly` purpose pushes Policy defaults toward higher preservation; a `casual` purpose pushes toward translator-helped accessibility; a `language-learning` purpose pushes toward explicit-marking variants).
- **A5 `source_fidelity`** modulates: `foreignized` / `foreignized-max` push Policy values toward the preserve end; `lightly-domesticated` permits the replace end with caveats.
- **A6 `form_preservation`** is mostly orthogonal — Policy values govern handling decisions, not structural form.
- **A7 `scaffolding`** affects apparatus-heavy values (`scholarly-apparatus-marking`, `translate-as-footnote`, `facing-original-with-meter-notes`): when `A7 = off / minimal`, these become heavier than the apparatus budget allows.

---

## 1. NonMainLangPartsPolicy — non-main language quotes, mentions, references

**Concept.** How to handle quotes, mentions, and references that appear in a language other than the main target language. The canonical first Policy class.

**Edge case.** The source text contains content in a language other than its main language: Said Nursi's 1920s-30s Turkish prose embeds Arabic ayahs from the Quran, Persian Mevlana couplets, transliterated Sufi formulae. Sub-edge: one chapter can have canon language A while another has canon language B; a single chapter can carry two canon languages.

**Values:** `preserve-original | preserve-original-and-add-translation-as-a-note | replace-original-with-translation | replace-original-with-translation-add-original-as-a-note | replace-original-with-infamous-translation`

**Default:** `preserve-original-and-add-translation-as-a-note` — preserve fidelity to the embedded original while ensuring the meaning transmits to readers without source-tradition fluency.

#### `preserve-original`

**Strategic stance.** Keep the non-main-language content verbatim with no translation or note. Maximum source-fidelity; assumes reader recognizes (or accepts not understanding) the embedded language.

**Said Nursi anchor.** Nursi's Arabic-script Quranic citations preserved unchanged in the English edition — the reader encounters the Arabic glyphs as Nursi placed them, with no English rendering.

**Cross-cultural example.** Quran-edition that preserves the Arabic ayah without translation, assuming reader recitation/recognition; in-tradition Hebrew prayer books that preserve Hebrew without English translation alongside.

**Suits.** Editions for source-culture-fluent readers; in-tradition devotional or scholarly editions where the embedded language IS the meaning.

#### `preserve-original-and-add-translation-as-a-note`

**Strategic stance.** Preserve the non-main-language original verbatim AND provide translation as a note (footnote, endnote, or inline note). The default — combines maximum source-fidelity with accessibility.

**Said Nursi anchor.** Nursi's Arabic-script ayah preserved with an English translation as a footnote: *"بَلَىٰ مَن أَسْلَمَ وَجْهَهُ لِلَّهِ وَهُوَ مُحْسِنٌ — Yes, whoever submits their whole self to Allah and is a doer of good [Sura 2:112]"*

**Cross-cultural example.** Norton Critical Editions of biblical texts with Hebrew/Greek preserved and English in apparatus; M.A.S. Abdel Haleem's Quran translation with Arabic facing-page and English translation.

**Suits.** Most general-purpose translations; scholarly and devotional editions alike.

#### `replace-original-with-translation`

**Strategic stance.** Replace the non-main-language content with a target-language translation in the main text; the original is dropped from the main path. Accessibility-first.

**Said Nursi anchor.** Nursi's Arabic ayah rendered only in English in main text: *"Yes, whoever submits their whole self to Allah and is a doer of good"* — the Arabic glyphs are not shown.

**Cross-cultural example.** Trade-paperback editions targeting non-specialist readers; popular Bible translations where Greek/Hebrew is not retained.

**Suits.** Casual reading editions; mass-market accessibility-focused translations.

#### `replace-original-with-translation-add-original-as-a-note`

**Strategic stance.** Translation in main text; original preserved in a note. Inverse of `preserve-original-and-add-translation-as-a-note` — translation foregrounded, original archived for scholarly check.

**Said Nursi anchor.** English ayah in main text; Arabic original in footnote with sura:ayah citation.

**Cross-cultural example.** Penguin Classics editions of biblical / Quranic texts where translation reads as primary and source-original is footnoted for verification.

**Suits.** Reader-friendly editions that still respect source-original for scholarly check; teaching editions.

#### `replace-original-with-infamous-translation`

**Strategic stance.** Use the **accepted famous translation** of the source rather than producing a new translation. "Infamous" here means "well-known / canonical," not pejorative — the established rendering the audience would recognize.

**Said Nursi anchor.** A Quranic ayah rendered using Yusuf Ali's, Sahih International's, or Asad's existing English translation — recognizable to a reader who knows the Quran in English. Or, for a Nursi-specific phrase, using Şükran Vahide's established English rendering.

**Cross-cultural example.** KJV English for Bible quotations in English-language scholarly works; Robert Alter for Hebrew Bible quotations where his rendering is canonical; Coleman Barks for Rumi where his rendering is canonical.

**Suits.** Editions where the embedded text has an established public-recognition rendering and the translator wants to honor that rather than introduce a new one.

---

## 2. SourceApparatusPolicy — author's pre-existing apparatus

**Concept.** How to handle the source's pre-existing apparatus — marginal annotations, glosses, hashiye that the author included alongside the main text.

**Edge case.** Said Nursi's *hashiye* (author's own marginal annotations); Talmud's marginal commentary tradition; critical-edition apparatus criticus. Distinct from translator-added apparatus (which lives in TC.A7 scaffolding); this is about apparatus the AUTHOR placed.

**Values:** `drop | translate-inline-bracketed | translate-as-footnote | preserve-as-source-channel`

**Default:** `translate-as-footnote` — preserves the author's annotation layer as a distinct channel without interrupting the main text flow.

#### `drop`

**Strategic stance.** Discard the author's marginalia entirely.

**Said Nursi anchor.** A casual paperback edition of Risale-i Nur omits the hashiye and presents only Nursi's main text.

**Cross-cultural example.** Trade-paperback editions of classical texts that strip critical apparatus; popular Penguin editions of biblical books without footnotes.

**Suits.** Mass-market accessibility-first editions; readers for whom the marginalia would create cognitive overhead without proportional gain.

#### `translate-inline-bracketed`

**Strategic stance.** Render marginalia inline in the target with bracket markers.

**Said Nursi anchor.** Hashiye inserted into the translation flow as bracketed asides: *"...[Hashiye: this point applies also to the situation of the believer in adversity]..."*

**Cross-cultural example.** Penguin Classics with translator-inserted bracketed glosses; some Quran translations that bracket explanatory expansions inside the verse.

**Suits.** Editions where the marginalia is short, contextually-relevant, and adds value without breaking reading flow.

#### `translate-as-footnote`

**Strategic stance.** Render marginalia as target-language footnotes. The default.

**Said Nursi anchor.** The hashiye become numbered footnotes in the English edition, preserving the author's voice as a distinct annotation layer without interrupting the main text.

**Cross-cultural example.** Norton Critical Edition style; scholarly editions of biblical commentaries; M.A.S. Abdel Haleem's Quran translation with footnoted explanations.

**Suits.** Most general-purpose editions; scholarly and devotional editions; preserves the author/marginalia distinction visibly.

#### `preserve-as-source-channel`

**Strategic stance.** Preserve marginalia as a structurally distinct channel — sidebar, parallel column, distinct font — mirroring the source's physical layout.

**Said Nursi anchor.** The hashiye appear in a sidebar or smaller font running parallel to Nursi's main text, mirroring the source manuscript's layout.

**Cross-cultural example.** Talmud Bavli editions where main text and commentaries occupy distinct columns; sacred-text editions with patristic commentary in parallel apparatus; medieval manuscript facsimile editions.

**Suits.** Scholarly editions; manuscript-tradition-conscious editions; readers expected to engage the marginalia as a parallel reading channel rather than as footnoted secondary content.

---

## 3. VoiceMarkingPolicy — voice transitions

**Concept.** How to mark transitions between the author's voice and cited authorities, student-voice additions, or other source-internal voice changes.

**Edge case.** Said Nursi's prose interleaves his own voice with Quran citations, hadith, kalam authors, and lahika (student letters). A reader needs (or doesn't need) to know "who is speaking" at any moment. Cross-corpus: rabbinic source-stacks with named attribution chains; Christian patristic citation traditions; Sanskrit commentary traditions citing earlier scholars.

**Values:** `off | as-in-original | implicit-typographic | explicit-attribution-inline | scholarly-apparatus-marking`

**Default:** `as-in-original` — mirror the source's own voice-marking conventions (script changes, indentation, typography) in the target.

**Spectrum.** The first four values lie on a spectrum from least to most visible marking (`off` → `as-in-original` → `implicit-typographic` → `explicit-attribution-inline`); `scholarly-apparatus-marking` is the maximum end with full apparatus.

#### `off`

**Strategic stance.** No marking at all. Author voice and citations blend into one flat narrative surface.

**Said Nursi anchor.** The English translation flows continuously without typographic, attributional, or apparatus marking — a reader encounters Quran citations, hadith, and Nursi's own prose at the same surface level.

**Cross-cultural example.** Vernacular translations targeting narrative flow where voice attribution would feel academic; popular religious paraphrases.

**Suits.** Devotional reading where voice-distinction is not the reading purpose; mass-market accessibility.

#### `as-in-original`

**Strategic stance.** Preserve the source's own voice-marking conventions in the target. The default. This is the source-preserving baseline that aligns with the other Policy classes' default-preserve patterns.

**Said Nursi anchor.** Nursi uses Arabic script for ayahs and Latin script for his Turkish prose; the English target mirrors this visual contrast (Arabic-script ayahs preserved; hashiye indented as Nursi indented them).

**Cross-cultural example.** Tanakh translations that preserve the source's typographic distinction between narrative and poetry sections; red-letter Bibles that mark Jesus's speech as the source typeset it.

**Suits.** Faithful editions where the source's own marking system carries meaning; devotional + scholarly editions alike.

#### `implicit-typographic`

**Strategic stance.** Translator applies typographic conventions to mark voice transitions (italics for citations, indented blocks for marginalia, distinct fonts for embedded language).

**Said Nursi anchor.** Quranic citations rendered in italic; hashiye indented and set in smaller type; Persian Mevlana couplets in a serif italic distinct from main type — typographic conventions chosen by the translator regardless of how Nursi marked them.

**Cross-cultural example.** Standard scholarly editions of cross-tradition theological texts; academic biblical commentaries; Oxford World's Classics.

**Suits.** Editions where source-original typography would not be reproducible in English (script-change visual contrast doesn't transfer); standardized scholarly typography preferred.

#### `explicit-attribution-inline`

**Strategic stance.** Translator inserts explicit "as X says" attributions at voice transitions.

**Said Nursi anchor.** *"As the Quran says in Sūrah 36:53..."* precedes each ayah; *"Said Nursi here notes in the margin..."* precedes each hashiye.

**Cross-cultural example.** Critical editions with named-source inline attribution; teaching editions where every source-shift is explicitly tagged for the reader.

**Suits.** Teaching editions; language-learning editions; readers who benefit from explicit voice-tracking.

#### `scholarly-apparatus-marking`

**Strategic stance.** Full apparatus with footnotes, sidebar attributions, source-marker sigla. Maximum voice-marking.

**Said Nursi anchor.** Every voice transition produces an apparatus criticus entry; the reader sees footnoted citation references, sigla for hashiye-vs-main-text, and bibliographic anchors for each cited authority.

**Cross-cultural example.** Norton Critical Editions; SBL Greek New Testament critical editions; Loeb Classical Library scholarly apparatus.

**Suits.** Scholarly editions; critical editions; comparative-literature editions where voice-attribution is part of the study.

---

## 4. ArchaicRegisterPolicy — archaic source-language register

**Concept.** How to render archaic source language in the target translation. About archaic *language* (old vocabulary, syntax, idiom feel) — distinct from archaic *referents* (institutions / offices / scientific frameworks that no longer exist), which would be handled by `AnachronismHandlingPolicy` (a candidate policy).

**Edge case.** An author wrote in a register that has aged. Their vocabulary, syntax, and idioms were contemporary at authorship but feel old to current readers. Nursi wrote in 1920s-30s Turkish that carries significant Ottoman-Turkish residue, especially in theological vocabulary (*iman*, *takvim*, *marifet*); Early Modern English in Shakespeare-era source; Classical Arabic in modern theological writing.

**Carries `source_temporal_register` field** re-homed from the dropped `SourceDescriptor` (per the corrective inquiry).

**Values:** `preserve-archaic-throughout | modernize-fully | hybrid-by-register-domain | mark-archaisms-explicitly`

**Default:** `hybrid-by-register-domain` — preserve archaic feel where it carries semantic weight; modernize where archaic English would be needlessly ornate.

#### `preserve-archaic-throughout`

**Strategic stance.** Keep the archaic register fully in the target throughout.

**Said Nursi anchor.** Nursi's Ottoman-Turkish theological prose rendered in archaic English throughout: *"Verily, behold the believer who upon the path of certainty doth walk, who unto the divine names with assurance turneth..."*

**Cross-cultural example.** KJV Bible style for Hebrew/Aramaic source; Hakluyt Society editions of historical travel writing preserving period diction; Loeb's older English translations of Greek philosophy.

**Suits.** Scholarly editions; historicizing translations where the period feel is part of the meaning; pastiche-aware editions.

#### `modernize-fully`

**Strategic stance.** Render everything in contemporary target language.

**Said Nursi anchor.** The same passage in fully modern English: *"Truly, look at how the believer walks the path of certainty, turning with assurance to the divine names..."*

**Cross-cultural example.** The Message paraphrase of the Bible; modern colloquial editions of Plato (Robin Waterfield translations); contemporary popular Sufi-poetry renderings (Coleman Barks-style Rumi).

**Suits.** Accessibility-first translations for general readers. Carries some no-smoothing-policy risk (smoothing of archaic forms violates faithful-rendering preservation).

#### `hybrid-by-register-domain`

**Strategic stance.** Preserve archaic feel where it carries semantic weight; modernize where archaic English would be needlessly ornate. The default.

**Said Nursi anchor.** Theological vocabulary (*iman*, *takvim*, *marifet*) keeps its weight in transliteration or archaic-register equivalent; Nursi's narrative analogies render in modern English without "thee/thou." Result: *"The believer (sahib-i iman) walks with certainty along the path, turning to the divine names with the assurance that comes from knowing them."*

**Cross-cultural example.** Penguin Classics of Plato — philosophical terminology preserved (eudaimonia, logos); narrative prose modernized. NRSV Bible style. Norton Critical editions that preserve period theological vocabulary while modernizing narrative.

**Suits.** The most general case — composes positively with the Layer-2 register-alternation preservation policy.

#### `mark-archaisms-explicitly`

**Strategic stance.** Use modern target language throughout but mark places where the source was archaic.

**Said Nursi anchor.** Modern English throughout; Ottoman-Turkish theological vocabulary appears in italic + footnote: *"the believer's *iman*¹..."* with footnote glossing the term and noting its archaic-but-precise sense.

**Cross-cultural example.** Language-learning editions; ALA-LC scholarly editions where archaisms are explicitly typographically marked; pedagogical critical editions for students.

**Suits.** Language-learning purposes; study-editions where the reader is expected to engage the archaism as data, not as register-feel.

---

## 5. HonorificsPolicy — theological honorifics

**Concept.** How to render theological honorifics that follow names — the Islamic *SAW / AS / RA / PBUH* family, the Jewish *ZT"L / RA / OBM* family, Hindu *śrī* before names, and analogous conventions across other traditions.

**Edge case.** Theological texts routinely follow proper names with honorifics that carry devotional and religious weight. The translator decides how to render these: as source-script glyphs, as transliterated abbreviations, as fully translated meanings, as conventional English abbreviations, or dropped.

**Values:** `preserve-original-script | transliterate-with-original | translate-meaning | abbreviate-translated | drop`

**Default:** `transliterate-with-original` — preserves the honorific's specificity while providing Latin-script accessibility.

#### `preserve-original-script`

**Strategic stance.** Keep the honorific in its original script.

**Said Nursi anchor.** *"Resul-i Ekrem ﷺ buyurmuştur"* preserved with the Arabic ﷺ glyph after the Prophet's name; *"Hazret-i Ali (kerremallâhu vechehû)"* preserves the parenthesized Arabic honorific.

**Cross-cultural example.** Hebrew Bible editions preserving ז״ל / זצ״ל after rabbinic names; Sanskrit editions preserving devanagari śrī before names; East-Asian Buddhist editions preserving 仏 (bul/butsu) glyphs.

**Suits.** Editions for source-culture-fluent readers; in-tradition devotional texts; manuscript-faithful editions.

#### `transliterate-with-original`

**Strategic stance.** Transliterate the honorific in Latin script alongside the original. The default.

**Said Nursi anchor.** *"The Prophet (sallallāhu ʿalayhi wa-sallam ﷺ)"* rendered with both Romanized transliteration and the original glyph.

**Cross-cultural example.** Encyclopedia of Islam style; scholarly Hindu studies editions that pair devanagari with transliterated honorifics; SBL biblical editions that show Hebrew + transliteration for proper-noun honorifics.

**Suits.** Scholarly editions; bilingual study editions; readers comfortable with both scripts.

#### `translate-meaning`

**Strategic stance.** Render the honorific's meaning fully in the target language.

**Said Nursi anchor.** *"The Prophet, peace and blessings be upon him"* — the full English meaning rendered after each Prophet reference.

**Cross-cultural example.** Most popular Islamic-history books for general audiences; Tarif Khalidi Quran translation style; popular Hindu texts that translate *śrī* as "blessed" or "revered."

**Suits.** General-reader editions; introductory non-academic texts; translations targeting readers without source-tradition fluency.

#### `abbreviate-translated`

**Strategic stance.** Use the established target-language abbreviation.

**Said Nursi anchor.** *"The Prophet (PBUH)"* — using the conventional English abbreviation.

**Cross-cultural example.** Mass-market Islamic-studies books; Western journalism on Islam; popular interfaith dialogue publications.

**Suits.** Texts where compactness matters and readers recognize the abbreviation; popular religious-studies books.

#### `drop`

**Strategic stance.** Omit the honorific entirely.

**Said Nursi anchor.** *"The Prophet said..."* — no honorific marking. Suits academic prose where editorial style mandates omission.

**Cross-cultural example.** Academic religious-studies monographs; Encyclopedia Britannica articles; secular comparative-religion textbooks.

**Suits.** Academic neutral-voice editions; comparative-religion scholarship where preserving honorifics would imply confessional commitment.

---

## 6. FormulaicOpeningPolicy — formulaic openings

**Concept.** How to render formulaic openings (invocations, basmala, dedicatory formulae) that open major sections of theological prose.

**Edge case.** Most theological treatises and devotional texts open with a formulaic invocation — the Islamic Bismillah; the Jewish Shema; Christian invocations; Vedic mantras. The translator decides whether to preserve original, transliterate, translate, or preserve untranslated.

**Values:** `preserve-original-with-translation | transliterate-with-translation | translate-only | preserve-original-untranslated`

**Default:** `preserve-original-with-translation` — preserves liturgical weight while ensuring accessibility.

#### `preserve-original-with-translation`

**Strategic stance.** Keep the original formula plus translation. The default.

**Said Nursi anchor.** *"بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ — In the name of Allah, the Most Compassionate, the Most Merciful"* opens each major section, with both the Arabic glyph block and the English meaning.

**Cross-cultural example.** Tanakh editions that preserve Hebrew *Shema Yisrael* with English translation; Sanskrit editions preserving devanagari mantras with translation; Catholic missals preserving Latin formulae with vernacular.

**Suits.** General-purpose translations that respect liturgical/devotional weight while remaining accessible.

#### `transliterate-with-translation`

**Strategic stance.** Transliterate in Latin script + translation.

**Said Nursi anchor.** *"Bismillāhi r-raḥmāni r-raḥīm — In the name of Allah, the Most Compassionate, the Most Merciful"*

**Cross-cultural example.** Academic editions of liturgical texts; scholarly Vedic editions transliterating mantras; Reform Jewish prayer books pairing transliterated Hebrew with English.

**Suits.** Scholarly editions where source-script reproduction is impractical; readers comfortable with transliteration but without source-script.

#### `translate-only`

**Strategic stance.** Render only the meaning in target language.

**Said Nursi anchor.** *"In the name of Allah, the Most Compassionate, the Most Merciful"* — without the Arabic glyphs or transliteration.

**Cross-cultural example.** Popular English-language editions of religious texts targeting non-specialist readers; trade-paperback editions of Sufi poetry.

**Suits.** Accessibility-first translations; readers without source-tradition familiarity.

#### `preserve-original-untranslated`

**Strategic stance.** Preserve the original formula with no translation.

**Said Nursi anchor.** *"بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"* preserved as-is, untranslated, on the assumption that the reader recognizes the basmala by sight.

**Cross-cultural example.** Editions targeting religiously-fluent readers; in-tradition prayer books; Hebrew prayer-book reprints assuming Shema-recognition.

**Suits.** In-tradition devotional editions; readers for whom the formula's recognition IS the rendering.

---

## 7. EmbeddedPoetryPolicy — embedded poetry

**Concept.** How to render embedded poetry that appears within prose source text. Distinct from `NonMainLangPartsPolicy` because poetry's rendering decision (verse vs prose vs facing-original) differs structurally from prose-quote handling.

**Edge case.** Said Nursi embeds Persian Mevlana couplets within his Turkish prose; biblical commentaries embed psalm verses within prose; Hindu prose-commentaries embed Sanskrit ślokas. The verse-vs-prose decision is the additional axis poetry adds.

**Values:** `preserve-original-with-prose-gloss | translate-as-verse | translate-as-prose | facing-original-with-meter-notes`

**Default:** `preserve-original-with-prose-gloss` — preserves poetic identity while ensuring meaning transmits.

#### `preserve-original-with-prose-gloss`

**Strategic stance.** Preserve the original poetry; follow with a prose gloss in the target. The default.

**Said Nursi anchor.** A Mevlana couplet preserved in Persian script, followed by an English prose paragraph explaining its meaning and how Nursi uses it: *"بشنو از نی چون حکایت می‌کند / از جدایی‌ها شکایت می‌کند — Listen to the reed as it tells its tale, complaining of separations. Nursi here invokes Mevlana's opening to anchor his point that..."*

**Cross-cultural example.** Loeb Classical Library editions where Greek verse appears with English prose translation on the facing page; scholarly editions of Hebrew poetry in biblical commentaries; academic editions of Sanskrit ślokas with prose gloss.

**Suits.** Most faithful default — preserves poetic identity while ensuring meaning transmits.

#### `translate-as-verse`

**Strategic stance.** Render the embedded poetry as poetry in the target.

**Said Nursi anchor.** Mevlana couplets rendered in English rhymed verse (or English free verse approximating the couplet structure): *"Listen as the reed laments / its tale of distance and lament."*

**Cross-cultural example.** Coleman Barks's Rumi translations; Robert Alter's poetic translations of the Hebrew Bible; A.K. Ramanujan's poetic translations of South Indian devotional verse.

**Suits.** Editions targeting readers for whom verse-form recognition is part of the experience; literary translations.

#### `translate-as-prose`

**Strategic stance.** Render embedded poetry as prose in the target.

**Said Nursi anchor.** A Mevlana couplet rendered as a paragraph of English prose, integrating into Nursi's surrounding text without verse markup: *"Listen to the reed as it tells of separations and complains."*

**Cross-cultural example.** Penguin Classics editions that prose-translate verse for accessibility; trade-paperback translations of Iranian classical poetry; popular-edition Bible Psalms in prose paragraphs.

**Suits.** Accessibility-first translations; reader unfamiliar with verse conventions; texts where the verse is illustrative not load-bearing.

#### `facing-original-with-meter-notes`

**Strategic stance.** Preserve original verse with target verse on facing page, with metrical notes.

**Said Nursi anchor.** A bilingual edition with the Persian couplet on the verso and an English verse equivalent on the recto, plus a footnote on the original meter (*"hazaj-i muthamman maḥdhūf"*) and how the English approximates it.

**Cross-cultural example.** Loeb Classical Library; bilingual editions of Pushkin; scholarly editions of Hafez; Penguin parallel-text editions of Dante.

**Suits.** Scholarly editions; readers studying the poetic form itself; comparative-literature editions.

---

## Candidate Policies (catalogued, not yet adopted)

These four Policy classes were evaluated in the corrective inquiry and assessed as **moderate-fit** — each passes the four filters with one specific caveat. They are catalogued here so that future adoption decisions have calibration context already prepared; adoption requires an explicit decision per class.

### A. TransliterationStandardPolicy

**Concept.** Which transliteration convention to use when rendering source script in target script.

**Values:** `scholarly-standard | popular-standard | phonetic | diacritic-stripped`

**Default:** `scholarly-standard`

**Caveat.** Transliteration is partly translator-side (a render convention) rather than purely authorial. Filter 3 (authorial-edge-case category) is partial.

- **`scholarly-standard`** — full diacritics per academic convention (ALA-LC, DIN-31635, IAST). *Nursi:* "Bedīʿuzzamān Saʿīd Nūrsī"; full Arabic diacritics. *Cross-cultural:* Encyclopedia of Islam; IAST-compliant Sanskrit.
- **`popular-standard`** — established public-facing transliteration without full diacritics. *Nursi:* "Bediuzzaman Said Nursi"; "Quran"; "iman". *Cross-cultural:* trade-paperback editions; popular Islamic books.
- **`phonetic`** — simplified-to-target-language phonetics for readability. *Nursi:* "Bediyuzzaman Said Noorsee". *Cross-cultural:* children's introductions to world religions.
- **`diacritic-stripped`** — like scholarly but without diacritics; suits constrained typography. *Nursi:* "Bediuzzaman Said Nursi" without ī / ʿ. *Cross-cultural:* web editions; ASCII-only databases.

### B. PriorTranslationStancePolicy

**Concept.** Stance toward established prior translations of the same corpus.

**Values:** `independent | honor-terminology | extend-with-revisions | explicit-divergence-noted | collate-and-cite`

**Default:** `independent`

**Caveat.** A `list[PriorRef]` companion structure (which translations are being honored / extended) would live separately, not on this Policy class — the class carries only the *stance* choice. Filter 1 (structural shape) is near-miss because companion data is needed.

- **`independent`** — translate from scratch; treat priors as background reference only. *Nursi:* new translation that does not consult Vahide / Akarsu during drafting. *Cross-cultural:* Robert Alter's Hebrew Bible.
- **`honor-terminology`** — preserve key terminology choices from accepted priors. *Nursi:* preserves Vahide's English of Nursi's key terms (*haqiqat* → "reality"). *Cross-cultural:* NIV's deference to KJV terminology where possible.
- **`extend-with-revisions`** — build on a prior translation, revising where new scholarship demands. *Nursi:* revised edition of Vahide updating where subsequent scholarship has shifted readings. *Cross-cultural:* NRSV's relationship to RSV.
- **`explicit-divergence-noted`** — independently translate but explicitly flag divergence from priors. *Nursi:* footnotes each significant divergence from Vahide / Akarsu. *Cross-cultural:* Robert Alter's footnoted KJV / RSV divergences.
- **`collate-and-cite`** — present multiple prior renderings alongside the new translation. *Nursi:* critical edition presenting Vahide, Akarsu, and new translator side-by-side. *Cross-cultural:* variorum Shakespeare editions.

### C. AnachronismHandlingPolicy

**Concept.** How to handle references to institutions, offices, scientific frameworks, currency, or administrative units that **were current at authorship but no longer exist or no longer mean what they meant**. About archaic *referents*, not archaic *language* (which is `ArchaicRegisterPolicy`'s territory).

**Values:** `preserve-with-footnote | inline-gloss | modernize-equivalent | drop-and-replace-current`

**Default:** `inline-gloss`

**Caveat.** Overlaps with `ArchaicRegisterPolicy` at the boundary — when does archaic language become anachronistic reference? Filter caveat: the boundary needs care.

Nursi-specific anachronism examples: **Şeyhülislam** (Ottoman state's highest Islamic religious authority, abolished 1924); **Darü'l-Hikmet'il-İslamiye** (Ottoman House of Islamic Wisdom where Nursi taught, dissolved with the caliphate); specific Ottoman vilayet names; **altın lira** (gold-backed Ottoman currency); specific Eastern Front WWI engagements.

- **`preserve-with-footnote`** — keep the anachronism in the target; footnote it. *Nursi:* "Şeyhülislam" preserved + footnote on the abolished office. *Cross-cultural:* Penguin Classics of Renaissance texts preserving "Privy Council" with footnote.
- **`inline-gloss`** — preserve with brief in-text gloss. *Nursi:* "...the Şeyhülislam (the Ottoman state's highest Islamic religious authority, an office since abolished)...". *Cross-cultural:* trade-paperback historical novels inline-glossing period offices.
- **`modernize-equivalent`** — substitute a current-equivalent term. *Nursi:* "Şeyhülislam" rendered as "the Grand Mufti." Risk: loses state-administrative dimension. *Cross-cultural:* "centurion" → "captain."
- **`drop-and-replace-current`** — drop and replace with current-day equivalent. *Nursi:* "Darü'l-Hikmet'il-İslamiye" → "a contemporary Islamic scholarly institution." *Cross-cultural:* The Message's biblical political references.

### D. CitationReferenceFormatPolicy

**Concept.** How to render cross-reference notation (sura:ayah; book:chapter:verse; canto:line).

**Values:** `preserve-source-format | standardize-canonical | both-with-cross-reference | footnoted-only`

**Default:** `preserve-source-format`

**Caveat.** Use-case is narrow (only matters for corpora with formal citation conventions). Filter check passes but adoption is gated on whether the project's corpora carry enough formal citation to warrant the field.

- **`preserve-source-format`** — keep the source's own citation format. *Nursi:* "Yâsîn sûresi, 53. âyet" renders as "Yāsīn Surah, 53rd verse." *Cross-cultural:* Talmud's folio:line; Sanskrit's canto:śloka.
- **`standardize-canonical`** — convert to standardized format. *Nursi:* Quranic citations rendered "Quran 36:53." *Cross-cultural:* SBL biblical citation format.
- **`both-with-cross-reference`** — provide both. *Nursi:* "Yâsîn 53 (Quran 36:53)." *Cross-cultural:* bilingual scholarly editions.
- **`footnoted-only`** — citations as footnote references rather than inline. *Nursi:* superscript footnote numbers; citation in footnotes. *Cross-cultural:* academic monographs.

---

## Deferred Policies (catalogued with revival triggers)

These were considered and intentionally deferred — out of shape, out of scope, or not load-bearing for current work. Each has an explicit revival trigger.

| Candidate | Reason deferred | Revival trigger |
|---|---|---|
| **ScriptDirectionPolicy** | Rendering surface (bidi RTL embedded in LTR), not authorial | When output rendering reaches the bidirectional-display stage |
| **PassageTypologyPolicy** | Typology label per chunk, not handling strategy | If a per-chunk typology mechanism is committed |
| **ConsumptionModePolicy / ReadingSessionPolicy** | Reader-side, not authorial | When reader-side context becomes load-bearing beyond TC.A4 purpose |
| **OutputFinalityPolicy** | Pipeline-side / output-status, not authorial | When the downstream pipeline distinguishes finality levels (draft / final / teaching) |
| **RelayTranslationPolicy** | Carries `list[LanguageHop]` chain structure that breaks pure single-field shape | When a relay-translation use case becomes active (current scope is direct Turkish→English) |

---

## Notes on prompt context (how the AI uses this document at translation time)

**1. Policy classes are independent of each other.** Each Policy instance can be set independently; the AI applies them per text span where each policy's edge case fires. Co-application is the norm, not the exception (a Bismillah is both a formulaic opening AND non-main-language content).

**2. Default values represent the "balanced preservation" choice.** When a Policy is not explicitly set, the AI uses the default, which generally lies in the preserve-with-translator-help region (preserves source while ensuring accessibility).

**3. TC composes with Policy.** Read this document alongside `config_base_source.md`. The TC choices (especially A4 purpose, A5 source_fidelity, A7 scaffolding) shape sensible Policy defaults and constrain which Policy values compose well at translation time. A `scholarly` purpose with `foreignized-max` fidelity will push most Policy values toward preservation; a `casual` purpose with `lightly-domesticated` fidelity will push toward translator-helped accessibility.

**4. The LLM-inferable test gates schema membership.** When a candidate field appears that might warrant a new Policy class, apply FP2: ask whether the LLM can derive the value from source text + existing config. If yes → no schema field needed (LLM handles at runtime). If no → the field carries a user value judgment and may warrant a new Policy class (subject to the four filters).

**5. Language-agnosticism is a design constraint.** Policy enum literals do not name specific languages, traditions, or corpora — the same value names work for Arabic, Hebrew, Sanskrit, Latin, Greek alike. Corpus-specificity lives in the user's per-job Policy instance, not in the schema values themselves.

**6. The Policy layer is the third schema-kind alongside TC and PC.** TC carries user strategy axes (continuous-axis enums). Policy classes carry per-edge-case enums for authorial value judgments. PC carries engine knobs. The three layers don't overlap; each Policy class addresses ONE recurring authorial edge-case the LLM cannot autonomously decide.
