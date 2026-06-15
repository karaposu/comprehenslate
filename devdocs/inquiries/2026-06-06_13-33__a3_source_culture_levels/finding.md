---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md
---
# Finding: A3 — Source Culture (the 5 Levels)

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` (the root architectural finding that established the 4-layer / 4-family / 8-axis configuration framework for Comprehenslate; specified A3 — Source Culture as a plain-ordinal axis in the Reader family but deferred level-value finalization).

**Revision trigger:** The user directed: "now lets do it for A3 Source Culture in [root path]." Unlike A2 (where the user explicitly directed 5 levels), the cardinality for A3 was NOT pre-specified by the user. The root finding proposed 3 levels (`outsider / familiar / source-native`); this inquiry decided cardinality on substantive grounds — settling on 5 levels.

**What's preserved:**
- A3's identity as a plain-ordinal axis (NOT a composite-axis like A1 Reader Level).
- A3's concept (per root): the reader's IDENTITY-BASED proximity to the source's cultural milieu.
- A3's scope (per root): controls how many cultural references need explanation; transliteration choices for proper names; cultural-context flagging.
- A3's boundaries (per root): explicitly distinct from A1's cultural-reference-recognition sub-field (A1 = competence-based; A3 = identity-based) and from A2 Domain Expertise (A2 = specialist knowledge in a domain).
- Receptive-only commitment inherited from A1+A2 chain.
- Conservative-bias-LOWER default inherited from root + A1+A2 chain.
- Language-agnostic at concept level inherited from root.
- DOMESTICATE-disfavored project policy inherited from `a1_cultural_reference_recognition_levels/finding.md` and extended to A3.

**What's changed:**
- **A3 cardinality refined from 3 to 5 levels** on substantive grounds (not by default-to-pattern-consistency). The substantive argument: the diaspora gradient (1st-generation immigrant / 1.5-generation / 2nd-generation / heritage-only / outsider) produces OPERATIONALLY DIFFERENT translator-AI handling decisions at each step. Collapsing to 3 levels forces a single handling rule across operationally-distinct reader types. The diaspora-studies literature (especially Avtar Brah's work on diasporic identification) supports the 5-step empirical ordering. Schema ergonomics also favor 5 (parallels the Reader family's pattern: A1 sub-fields × 5; A2 × 5).
- **Labels are identity-meaningful** rather than capacity-graded. The 5 levels are `outsider | acquainted | familiar | heritage | source-native`. These map to diaspora-studies categories + religious-insider sociology categories (born / converted / heritage trichotomy expanded to 5).

**What's new:**
- **Composite-with-primary-axis identity dimension.** The headline dimension is **lived cultural-fluency** — a composite of residential markers (where the reader lives/has lived), linguistic markers (native vs learned source language), practice markers (actively practices source-culture customs), and religious/ideological markers (for religious-text sources). Sub-dimensions are context-dependently weighted: religious-text sources weight religious identity more; secular sources weight residential/linguistic more.
- **Single-source-culture default for the domain-scope question** (parallel to A2's single-domain default). A3 specifies proximity to the source TEXT's primary culture. The source's culture is implicit at runtime via Layer 3 SOURCE-DESCRIPTION. Multi-source-culture readers (insider for Turkish-Islamic + outsider for Greek classical simultaneously) are deferred to a future audience-level inquiry.
- **10 translator-AI handling actions in 4 categories.** Proper-noun handling (TRANSLITERATE-FULLY / TRANSLITERATE-WITH-GLOSS / TARGET-LANGUAGE-EQUIVALENT); cultural-context handling (ASSUME-SHARED-CULTURAL-KNOWLEDGE / FLAG-CULTURAL-CONTEXT / BRIDGE-CULTURAL-DISTANCE); honorific handling (KEEP-HONORIFICS-SOURCE / ANGLICIZE-HONORIFICS — disfavored); strategic stance (PRESERVE-CULTURAL-SPECIFICITY / DOMESTICATE-CULTURAL-FRAME — disfavored).
- **DOMESTICATE policy extended from A1 to A3.** DOMESTICATE-CULTURAL-FRAME + ANGLICIZE-HONORIFICS are DISFAVORED per the project's translation-register-fidelity commitment (user memory) + Venuti's foreignization ethics — the same anchors that justified the policy in `a1_cultural_reference_recognition_levels/finding.md`. PRESERVE-CULTURAL-SPECIFICITY + FLAG-CULTURAL-CONTEXT + TRANSLITERATE-WITH-GLOSS are preferred at low A3 levels as foreignization-preserving alternatives.
- **Layered-source-culture handling note.** The Said Nursi corpus has a LAYERED source culture (Muslim + Turkish + Naqshbandi-Khalidi-Sufi nested). A3 captures proximity to the PRIMARY (most-specific) layer — the innermost layer. The translator-AI handles within-layer variation at runtime by examining whether a specific reference invokes the outer Muslim-broad layer or the inner Naqshbandi-specific layer; a high-A3 reader (proximity to inner layer) knows the outer layer too; an outer-layer-only reader needs FLAG-CONTEXT for inner-layer references but the configuration tracks the primary proximity.
- **Edge-case mapping for diaspora / convert / long-resident readers.** Adult convert + decades residence → `familiar`; spouse + 20+ years residence + no conversion → `familiar`; long-term scholar-resident → `familiar`; recent convert without residence → `acquainted`; returnee from diaspora → `heritage` or `source-native` per lived years; 1.5-generation → `heritage` (conservative-bias); 2nd-generation → `heritage`; 3rd-generation+ → `heritage` (diluted); 1st-generation immigrant → `source-native` (primary identity still source).
- **Translator-AI runtime determination mechanism explicit** (parallels A2). The reader-level configuration specifies the reader's identity; the AI determines a specific reference's cultural-layer-membership, transliteration-choice context, and shared-knowledge-assumption at runtime from training. Configuration tells the AI the reader; AI's knowledge tells it per reference; the handling action is a deterministic function.
- **Self-identification = configuration trust mechanism.** A3 is identity-based; the user self-reports the A3 value. The AI takes it at face value. (This is true of all reader-level configurations; A3 isn't special.)
- **Reader-family closure marker.** This finding CLOSES the Reader family — the 3 axes (A1 Reader Level, A2 Domain Expertise, A3 Source Culture) are now fully specified. The schema is ready for commit on the Reader family. Next inquiries target the Purpose family (A4), the Strategy family (A5 Source Fidelity / A6 Form Preservation / A7 Scaffolding), and the Depth family (A8 Analysis Depth).

**Migration:** No migration needed — this is the first A3 axis specification. When the user commits the schema: `source_culture: Literal["outsider", "acquainted", "familiar", "heritage", "source-native"]`.

---

## Question

For A3 — Source Culture (the third axis in the Reader family per the root architectural finding), what should the level cardinality be (3 per root proposal vs 5 per the A1+A2 pattern, on substantive grounds), what should each level's name and concept be, what logic distinguishes each level from its neighbors, what concrete examples spread across multiple source cultures (Turkish-Ottoman-Islamic / Hebrew biblical / Greek classical / Hindu Sanskrit / Chinese Confucian / etc.) make each level operationally identifiable — AND resolving the A3↔A1 boundary (identity vs competence), the A3↔A2 boundary (cultural identity vs domain expertise), the identity-dimension decision (what specifically is being measured: birth / lived years / language / religion / heritage / combination), the domain-scope question (single source culture vs profile), and the diaspora/convert/long-resident edge cases?

---

## Finding Summary

- **5 ordinal levels with identity-meaningful labels.** `outsider | acquainted | familiar | heritage | source-native`. The cardinality was decided on substantive grounds (not by default-consistency-with-A2): the diaspora gradient (1st-generation immigrant / 1.5-generation / 2nd-generation / heritage-only / outsider) produces operationally-different translator-AI handling decisions at each step. Collapsing to 3 levels forces a single rule across operationally-distinct readers.

- **Primary dimension is LIVED CULTURAL-FLUENCY (composite-with-primary-axis).** A composite of residential markers (where the reader lives/has lived), linguistic markers (native vs learned source language), practice markers (actively practices source-culture customs), and religious/ideological markers (for religious-text sources). The sub-dimensions are not separate axes (A3 is plain-ordinal) but they aggregate into a single headline dimension with context-dependent weighting: religious-text sources weight religious identity more; secular sources weight residential/linguistic markers more.

- **Plain-ordinal pattern (no sub-fields).** A3 is NOT a composite-axis like A1 Reader Level. The user sets ONE A3 value; there are no propagating sub-fields.

- **Level is TARGET-READER-RELATIVE.** The A3 value captures the reader's identity-based proximity to the source TEXT's primary culture. The source's culture is detected at runtime via Layer 3 SOURCE-DESCRIPTION, not configured by the user.

- **Single-source-culture default** (parallel to A2's single-domain default). A3 specifies proximity to the source TEXT's culture. Each translation job has one source text with one primary culture (Said Nursi = Turkish-Ottoman-Naqshbandi-Khalidi-Islamic; the Bible = Hebrew biblical or NT Hellenistic; Greek tragedy = ancient Greek). Multi-source-culture readers (insider for Turkish-Islamic + outsider for Greek classical simultaneously) deferred to future audience-level inquiry.

- **Layered-source-culture handling note.** A3 captures proximity to the PRIMARY (most-specific) cultural layer. For Said Nursi the primary is Naqshbandi-Khalidi-Sufi-Islamic-Turkish (innermost). The AI handles within-layer variation at runtime: outer-layer references at high A3 → ASSUME-SHARED-KNOWLEDGE; outer-layer-only reader (Muslim but not Naqshbandi-Khalidi) handled by configuration capturing only outer-layer proximity (high-end `familiar` rather than `source-native`).

- **10 handling actions in 4 categories.** Proper-noun (3): TRANSLITERATE-FULLY / TRANSLITERATE-WITH-GLOSS / TARGET-LANGUAGE-EQUIVALENT. Cultural-context (3): ASSUME-SHARED-CULTURAL-KNOWLEDGE / FLAG-CULTURAL-CONTEXT / BRIDGE-CULTURAL-DISTANCE. Honorific (2): KEEP-HONORIFICS-SOURCE / ANGLICIZE-HONORIFICS (disfavored). Strategic (2): PRESERVE-CULTURAL-SPECIFICITY / DOMESTICATE-CULTURAL-FRAME (disfavored).

- **DOMESTICATE-CULTURAL-FRAME + ANGLICIZE-HONORIFICS DISFAVORED** per A1 policy extension. Anchored to the user's translation-register-fidelity memory + Venuti's foreignization ethics (the same anchors that justify the A1 cultural-reference-recognition policy). Preference order: PRESERVE-CULTURAL-SPECIFICITY > KEEP-HONORIFICS-SOURCE > TRANSLITERATE-WITH-GLOSS > FLAG-CULTURAL-CONTEXT > BRIDGE-CULTURAL-DISTANCE > [TARGET-LANGUAGE-EQUIVALENT / DOMESTICATE / ANGLICIZE] as last resorts.

- **4-component template MEDIUM-adapted** from A1+A2 template: reader profile + cultural-proximity-tier + cultural-context-tier + cultural-handling-test.

- **A3↔A1 boundary: identity vs competence.** A1 cultural-reference-recognition is competence-based (does the reader know the references?). A3 is identity-based (does the reader come from inside the culture?). Four-corners independence (per root finding): well-read insider; poorly-read insider; well-read outsider (Western academic Islamicist); uninitiated outsider — all real configurations.

- **A3↔A2 boundary: cultural identity vs domain expertise.** A2 captures depth of specialist knowledge in the source's DOMAIN (Islamic theology, biblical scholarship, etc.). A3 captures identity-based proximity to source's CULTURE (broader than domain). Four-corners independence: Western Islamicist (A3=outsider + A2=expert); born-Muslim with no formal study (A3=source-native + A2=lay); Muslim Islamic-studies professor (A3=source-native + A2=expert); typical Western non-Muslim (A3=outsider + A2=lay) — all real.

- **A3↔A4 Purpose: distinct concepts.** A4 = WHY (use-case); A3 = WHO (identity). A specialist source-native may read for casual purpose; a curious outsider may read for scholarly purpose.

- **A3↔A5 Source Fidelity: reader-side vs translation-strategy-side.** A3 is reader-side; A5 is translation-strategy-side (the translator's foreignization vs domestication stance). They interact (low A3 reader tends to suit foreignized translation if user wants source-cultural encounter; high A3 reader doesn't need foreignization) but they are distinct.

- **Self-identification = configuration trust mechanism.** The user self-reports the A3 value. The AI takes it at face value. The configuration is the user's responsibility; the AI cannot reliably infer reader identity from text-side signals.

- **Translator-AI runtime determination mechanism explicit.** Reader-level configuration specifies the reader's identity; AI determines reference's cultural-layer-membership and shared-knowledge-assumption at runtime from its training. Handling action = deterministic function of (A3 level, reference's cultural-layer, source markings, action policy).

- **Conservative-bias-LOWER default.** AI assumes OUTSIDER when in doubt → more FLAG-CULTURAL-CONTEXT, TRANSLITERATE-WITH-GLOSS, BRIDGE-CULTURAL-DISTANCE. Safer ethically (avoids assuming-shared-knowledge that's not there).

- **Reader-family closure.** This finding CLOSES the 3-axis Reader family (A1 Reader Level, A2 Domain Expertise, A3 Source Culture). The user can commit the Reader-family schema. Next inquiries target Purpose family (A4); Strategy family (A5, A6, A7); Depth family (A8).

---

## Finding

The root architectural inquiry established Comprehenslate's translation-configuration framework with 4 layers, 4 families, 8 axes. The Reader family has 3 axes: A1 Reader Level (5 sub-fields × 5 levels each, completed in the A1 chain); A2 Domain Expertise (5 levels `lay | aware | educated | trained | expert`, completed in `a2_domain_expertise_levels/finding.md`); and A3 Source Culture — this finding.

The root finding proposed 3 levels for A3 (`outsider / familiar / source-native`) but deferred level-value finalization. The user's directive for this inquiry was open on cardinality (unlike A2, where they explicitly said "should be 5 levels"). This inquiry decided cardinality on substantive grounds and settled on 5 levels.

### 1. The Framework

#### 1.1 Why 5 levels (not 3)

The root finding's 3 proposed levels (`outsider / familiar / source-native`) capture an identity-trichotomy that has some appeal — identity feels discrete in everyday language. But the operational reality of translator-AI handling decisions cuts finer.

The diaspora gradient is empirically real and produces operationally-different translator-AI handling decisions at each step. Consider the spectrum from a typical Western non-Muslim reading a Said Nursi translation to a born-and-raised Naqshbandi-Khalidi-Sufi reader:

- **Outsider (no cultural ties; identity firmly target).** A typical Western non-Muslim reader. AI assumes the reader needs explicit cultural context, transliteration with gloss, and bridge-cultural-distance for source-cultural assumptions.
- **Acquainted (some exposure; identity-shift without immersion).** A Western reader with general "world religions" exposure; a convert without residence; a non-conversational student of source language. AI can transliterate-with-gloss, flag-cultural-context briefly, but still cannot assume shared cultural knowledge.
- **Familiar (sustained immersion; cultural-fluency without inherited identity).** A long-resident Western convert; a 30-year scholar-resident; a non-converting spouse with 20+ years residence. AI can use KEEP-HONORIFICS-SOURCE, TRANSLITERATE-WITH-GLOSS for less-central references, FLAG-CULTURAL-CONTEXT minimally.
- **Heritage (identity inherited but diluted).** A 2nd-generation Turkish-American not actively practicing; a 1.5-generation reader; heritage-but-not-actively-practicing. AI can ASSUME-SHARED-KNOWLEDGE for major cultural anchors but may FLAG-CONTEXT for inner-layer references (e.g., Naqshbandi-Khalidi-specific terminology vs general Islamic terminology).
- **Source-native (born and raised in source culture; primary identity source).** A born-and-raised Turkish-Muslim from a Naqshbandi-Khalidi-leaning community. AI uses ASSUME-SHARED-CULTURAL-KNOWLEDGE; KEEP-HONORIFICS-SOURCE; PRESERVE-CULTURAL-SPECIFICITY throughout.

These 5 reader types have operationally-distinct AI handling decisions. A 3-level scheme would force the AI to use a single rule across operationally-different readers (e.g., grouping "familiar" with "heritage" with "first-generation immigrant" all as one `familiar` level). 5 levels match the empirical ordering documented in diaspora studies (especially Avtar Brah's work on diasporic identification) and religious-insider sociology (Lewis Rambo on conversion trajectories; Sherman Jackson on Blackamerican Islam).

Schema ergonomics also favor 5: the Reader family's pattern is 5 (A1 sub-fields × 5; A2 × 5). Consistency aids the schema's overall ergonomics.

#### 1.2 The 5 levels and the cultural-proximity tier ladder

The 5 ordinal labels are `outsider | acquainted | familiar | heritage | source-native`. They are identity-meaningful, not capacity-graded — the labels reflect the reader's identity-based proximity to the source culture, not their reading capability (which is A1's territory) or domain expertise (A2's).

Each label maps to a cultural-proximity tier:

- `outsider` ↔ "no cultural ties; identity firmly in target culture"
- `acquainted` ↔ "some exposure; cultural-tourist or identity-shift-without-immersion"
- `familiar` ↔ "sustained immersion; cultural-fluency without inherited identity"
- `heritage` ↔ "identity inherited but diluted; bicultural with target-primary"
- `source-native` ↔ "born and raised in source culture; primary identity source"

The "heritage" placement note: a heritage reader has MORE proximity than `familiar` (their identity is inherited not chosen — they grew up with cultural exposure, even if practice has lapsed) but LESS than `source-native` (heritage is diluted; not full immersion-since-birth). This empirical ordering comes from diaspora studies.

#### 1.3 The composite-with-primary-axis identity dimension

A3's primary dimension is **lived cultural-fluency** — a composite of several sub-markers that aggregate together:

- **Residential markers:** where the reader lives now; where they have lived; for how long.
- **Linguistic markers:** native vs learned source language; current fluency.
- **Practice markers:** actively practices source-culture customs (religious observance for religious-text sources; cultural traditions for secular sources).
- **Religious/ideological markers:** religious identity for religious-text sources; ideological identity for political-canon sources.
- **Heritage markers:** descended from source culture; family network in source culture.

These sub-markers are NOT separate axes (A3 is plain-ordinal — one user-set value). They aggregate into a single headline dimension (lived cultural-fluency) with context-dependent weighting:

- **For religious-text sources** (Said Nursi corpus; the Bible; the Quran): religious identity weights more. A born Catholic reading the Bible has higher A3 proximity than a non-religious Westerner with the same residential profile.
- **For secular sources** (Greek classical; Chinese Confucian; modern Russian literature): residential and linguistic markers weight more. A scholar-resident of Greece has higher A3 proximity to Greek classical than a non-resident scholar with the same domain expertise.
- **For layered sources** (Said Nursi has Muslim + Turkish + Naqshbandi-Khalidi-Sufi nested): the primary layer is the most-specific. The AI handles within-layer references at runtime.

The composite-with-primary-axis approach avoids two failure modes: a single-dimension approach is too vague to operationalize; a multiple-axis approach (separate axes for each sub-marker) multiplies configuration burden without operational benefit.

#### 1.4 Plain-ordinal pattern (no sub-fields)

A3 is plain-ordinal. The user sets ONE A3 value; there are no propagating sub-fields. This contrasts with A1 Reader Level (composite-axis with 5 sub-fields).

#### 1.5 Reader-relative; single-source-culture default

The A3 value captures the reader's identity-based proximity to the source TEXT's primary culture. The source's culture is detected at runtime via Layer 3 SOURCE-DESCRIPTION (the AI auto-detects it from the source text), not configured by the user.

Each translation job has one source text with one primary culture. Multi-source-culture readers (insider for Turkish-Islamic + outsider for Greek classical) are real but are deferred to a future audience-level inquiry. The natural future schema would be `audience.source_culture_proximity: list[(source_culture, level)]` at the audience level.

#### 1.6 Layered-source-culture handling note

The Said Nursi corpus's source culture is LAYERED: Muslim (broad) + Turkish (mid) + Naqshbandi-Khalidi-Sufi (specific, innermost). A reader can be insider for the outer Muslim layer + outsider for the inner Naqshbandi-Khalidi layer.

A3 captures proximity to the PRIMARY (most-specific) cultural layer. For Said Nursi, the primary is Naqshbandi-Khalidi-Sufi-Islamic-Turkish. The translator-AI handles within-layer variation at runtime:

- A `source-native` reader (inner-layer proximity) catches inner-layer references silently; the AI ASSUME-SHARED-KNOWLEDGE.
- A `familiar` reader (outer-Muslim-layer proximity but not inner) needs brief FLAG-CONTEXT for inner-layer references like specific Naqshbandi-Khalidi-Sufi terminology; the AI handles this at runtime by examining each reference's cultural-layer-membership.

This is similar to A2's handling of subfield expertise within a domain (an Ash'ari specialist reading a Mu'tazila-focused text knows kalam vocabulary but not Mu'tazila-internal positions). The configuration captures the primary proximity; the AI handles within-layer variation at runtime.

#### 1.7 10 handling actions in 4 categories

The translator-AI's runtime action vocabulary for A3 is structured into 4 categories with 10 total actions:

**Proper-noun handling (3 actions):**

| Action | Operation | Use when |
|---|---|---|
| **TRANSLITERATE-FULLY** | Keep source-language proper names in original script or Latin transliteration ("Allah" / "yeshua" / "Üstad") | High A3; reader recognizes source-language forms |
| **TRANSLITERATE-WITH-GLOSS** | Transliteration + brief target-language gloss ("Allah (God)") | Mid A3; reader catches the source form with help |
| **TARGET-LANGUAGE-EQUIVALENT** | Use target-language version ("Jesus" not "Yeshua"; "God" not "Allah") | Low A3 last resort; project policy disfavors |

**Cultural-context handling (3 actions):**

| Action | Operation | Use when |
|---|---|---|
| **ASSUME-SHARED-CULTURAL-KNOWLEDGE** | Don't flag cultural assumptions; reader has them | High A3; reader has source-cultural background |
| **FLAG-CULTURAL-CONTEXT** | Briefly explain cultural background assumed by source | Mid A3; reader benefits from light cultural framing |
| **BRIDGE-CULTURAL-DISTANCE** | Extensive explanation of source culture's assumptions and worldview | Low A3; reader is far from source culture |

**Honorific handling (2 actions):**

| Action | Operation | Use when |
|---|---|---|
| **KEEP-HONORIFICS-SOURCE** | Preserve source honorifics (Hazret-i Üstad; Imam-i Azam; Sahabe) | High A3; reader recognizes honorific tradition |
| **ANGLICIZE-HONORIFICS** | Translate honorifics (Master So-and-so; the Imam; the Companions) | Low A3 last resort; project policy disfavors |

**Strategic stance (2 actions):**

| Action | Operation | Use when |
|---|---|---|
| **PRESERVE-CULTURAL-SPECIFICITY** | Keep source-cultural elements foreign-feeling for reader to encounter | Across all levels; foreignization stance per project policy |
| **DOMESTICATE-CULTURAL-FRAME** | Substitute target-cultural framework | Last resort; project policy disfavors |

#### 1.8 Project-specific action policy: DOMESTICATE-CULTURAL-FRAME + ANGLICIZE-HONORIFICS disfavored

The DOMESTICATE-disfavored policy extends from `a1_cultural_reference_recognition_levels/finding.md` (the A1 cultural-reference-recognition sub-field) to A3. The same anchors apply:

**Anchor 1: User's translation-register-fidelity memory.** The user's persistent memory commits to preserving source-cultural character ("don't pull plain source registers up into ornate/archaic English" — implies preserving source character, not just sentence-level register).

**Anchor 2: Lawrence Venuti's foreignization ethics.** *The Translator's Invisibility* (1995) argues that domesticating translation makes the translator invisible and erases the foreignness that gives the source its specificity. For the project's primary corpus (Said Nursi) and most other source cultures the project handles, foreignization is the ethical default.

The policy translates to a preference order:

```
PRESERVE-CULTURAL-SPECIFICITY  >  KEEP-HONORIFICS-SOURCE  >  TRANSLITERATE-WITH-GLOSS  >  FLAG-CULTURAL-CONTEXT  >  BRIDGE-CULTURAL-DISTANCE  >  [TARGET-LANGUAGE-EQUIVALENT / DOMESTICATE-CULTURAL-FRAME / ANGLICIZE-HONORIFICS] (last resorts)
```

The foreignization-preserving alternatives (FLAG-CULTURAL-CONTEXT + TRANSLITERATE-WITH-GLOSS) handle outsider readers without DOMESTICATING — the reader encounters cultural specificity with light support, not erasure.

#### 1.9 Self-identification = configuration trust mechanism

A3 is identity-based. The user self-reports the A3 value. The AI takes it at face value. The configuration is the user's responsibility; the AI cannot reliably infer reader cultural identity from text-side signals (unlike A2 domain expertise, where some signals may exist — like the reader using specialist vocabulary in feedback).

This is true of all reader-level configurations; A3 isn't special. But A3's identity-based dimension makes the trust mechanism more salient.

#### 1.10 Translator-AI runtime determination

The configurable inputs (A3 level, A1 sub-field levels, A2 level, etc.) are constants for a translation pass. The translator-AI determines runtime properties from its training:

- Whether a specific reference invokes the outer cultural layer or an inner layer (for layered sources).
- Which transliteration convention applies to a specific proper name (standard Arabic transliteration; Turkish modern spelling; Ottoman script).
- Whether an honorific has an Anglicized equivalent that conventionally appears in translation literature.

The action selection is then a deterministic function: `action = cultural_handling_test(A3_level, reference_cultural_layer, transliteration_context, source_markings, action_policy)`.

#### 1.11 Conservative-bias-LOWER default

When the user's configuration is silent or ambiguous, the AI assumes OUTSIDER → more FLAG-CULTURAL-CONTEXT, TRANSLITERATE-WITH-GLOSS, BRIDGE-CULTURAL-DISTANCE. This is safer ethically (avoids assuming-shared-knowledge that's not there); it errs toward over-glossing rather than under-glossing.

### 2. The 5 Per-Level Definitions

Each level has the 4 components (reader profile + cultural-proximity-tier + cultural-context-tier + cultural-handling-test) plus cross-cultural examples plus explicit distinguishing logic at the boundary with the adjacent level.

#### 2.1 `outsider`

**Reader profile.** No cultural ties to the source culture. Identity firmly anchored in the target culture. Has not lived in the source culture; doesn't speak the source language natively; doesn't practice source-culture customs; no familial or religious heritage from the source culture.

**Cultural-proximity-tier.** No identity-based proximity; treats the source culture as fully foreign. May have some cultural-general competence (A1 cultural-reference-recognition territory) but does not have lived cultural-fluency.

**Cultural-context-tier.** Handles only target-cultural register; needs explicit framing for source-cultural assumptions. Religious-sermon register, cultural-celebration register, source-language-native register all sit beyond reliable comprehension.

**Cultural-handling-test.** Proper-noun: TRANSLITERATE-WITH-GLOSS for source-language proper names; AVOID TARGET-LANGUAGE-EQUIVALENT (per project policy DOMESTICATE-disfavored). Cultural-context: BRIDGE-CULTURAL-DISTANCE for source-cultural assumptions. Honorific: KEEP-HONORIFICS-SOURCE with first-use gloss. Strategic: PRESERVE-CULTURAL-SPECIFICITY (foreignization-preserving over DOMESTICATE-CULTURAL-FRAME).

**Examples spread across source cultures:**
- *Turkish-Ottoman-Naqshbandi-Khalidi-Islamic (Said Nursi corpus):* Typical Western non-Muslim reader. Doesn't know "Hazret-i Üstad" carries an honorific weight; doesn't know "Bediuzzaman" means "wonder of the age"; doesn't recognize Naqshbandi-Khalidi-Sufi tradition. AI: TRANSLITERATE-WITH-GLOSS "Üstad (Master)"; FLAG-CULTURAL-CONTEXT for Sufi-spiritual-practice references; BRIDGE-CULTURAL-DISTANCE for Islamic-theological assumptions.
- *Hebrew biblical:* Secular Western non-Jewish reader. Recognizes "Moses" and "David" via cultural exposure but doesn't know Second Temple Judaism's covenant theology or Hellenistic Jewish cultural specifics. AI: BRIDGE-CULTURAL-DISTANCE for covenant theology assumptions.
- *Quranic:* Western non-Muslim reader. Doesn't know "Bismillah" carries opening-prayer weight; doesn't recognize "Sırat" as the bridge over hellfire. AI: TRANSLITERATE-WITH-GLOSS; BRIDGE-CULTURAL-DISTANCE.
- *Hindu Sanskrit:* Western reader with no Hindu background. Doesn't know "Rama" vs "Krishna" cultural significance; doesn't recognize "Atman" beyond a vague "soul" gloss. AI: TRANSLITERATE-WITH-GLOSS; FLAG-CULTURAL-CONTEXT.
- *Chinese Confucian:* Western reader. Doesn't recognize "junzi" as the exemplary-person concept; doesn't know "li" carries ritual-propriety weight. AI: PARAPHRASE or TRANSLITERATE-WITH-GLOSS.

#### 2.2 `acquainted`

**Reader profile.** Some exposure to the source culture but no immersion; identity-shift without sustained immersion. May be a cultural-tourist (visited the source country briefly); a convert without residence; a non-conversational student of the source language; a general-knowledge enthusiast.

**Cultural-proximity-tier.** Cultural-tourist exposure. Catches major cultural anchors when explicitly framed; misses deeper cultural assumptions.

**Cultural-context-tier.** Handles popular-introduction register; major-cultural-anchor references with brief framing. Specialist-cultural register and source-language-native register sit beyond reliable comprehension.

**Cultural-handling-test.** Proper-noun: TRANSLITERATE-WITH-GLOSS first use, then bare transliteration. Cultural-context: FLAG-CULTURAL-CONTEXT briefly for cultural assumptions. Honorific: KEEP-HONORIFICS-SOURCE with first-use gloss. Strategic: PRESERVE-CULTURAL-SPECIFICITY.

**Examples spread across source cultures:**
- *Said Nursi corpus:* Western reader with general "world religions" exposure or a recent convert without residence. Recognizes "Allah" as standard Arabic for God; knows what "5 pillars" are; doesn't reliably know "Naqshbandi-Khalidi". AI: TRANSLITERATE-WITH-GLOSS "Hazret-i Üstad (the venerated Master)"; FLAG-CULTURAL-CONTEXT for Naqshbandi-Khalidi-specific references.
- *Hebrew biblical:* Westerner who took a religion-survey course. Recognizes major figures (Moses, David, Paul) and basic narratives (Eden, Exodus). AI: FLAG-CULTURAL-CONTEXT for Documentary Hypothesis-style scholarly assumptions; TRANSLITERATE-WITH-GLOSS for less-common Hebrew terms.
- *Quranic:* Westerner with general Islam-aware background. Recognizes Bismillah, Surah, basic prayers. AI: TRANSLITERATE-WITH-GLOSS for Quranic-specific terms; FLAG-CULTURAL-CONTEXT for Islamic-theological frames.
- *Hindu Sanskrit:* Westerner with yoga-/meditation-cultural exposure. Recognizes "karma," "dharma" loosely. AI: FLAG-CULTURAL-CONTEXT for deeper Vedic concepts.
- *Greek classical (secular):* Westerner with general classical-history exposure. Recognizes major figures (Socrates, Caesar) and major events (Battle of Marathon). AI: FLAG-CULTURAL-CONTEXT for less-major historical references.

**Distinguishing logic from `outsider`:** The `acquainted` reader has SOME EXPOSURE (cultural-tourist, religion-survey course, popular-book reading) — they catch major cultural anchors when explicitly framed. The `outsider` reader has NONE — they need everything bridged. The translator-AI can use brief FLAG-CULTURAL-CONTEXT at `acquainted` where it would need BRIDGE-CULTURAL-DISTANCE at `outsider`.

#### 2.3 `familiar`

**Reader profile.** Sustained immersion in the source culture without inherited identity. May be: a Western convert who has lived in a Muslim community for years; a long-resident Westerner in a Muslim-majority country (10+ years); a 30-year scholar-resident (Western Islamicist in Cairo); a non-converting spouse with 20+ years residence; a converted-Catholic-priest with decades of Hebrew biblical study and residence in Jerusalem.

**Cultural-proximity-tier.** Lived cultural-fluency without inherited identity. Catches most cultural references silently; understands cultural assumptions through immersion; recognizes source-language honorifics in their proper register. Doesn't have the inherited identity of a heritage or source-native reader.

**Cultural-context-tier.** Handles general-cultural register + major-religious-text register + popular-cultural-celebration register. Approaches scholar-canonical register and source-language-native subtle register at the edges.

**Cultural-handling-test.** Proper-noun: TRANSLITERATE-FULLY for major source-language terms (the reader recognizes "Allah", "Üstad", "isnād" without gloss); TRANSLITERATE-WITH-GLOSS only for less-central references. Cultural-context: ASSUME-SHARED-CULTURAL-KNOWLEDGE for major cultural anchors; FLAG-CULTURAL-CONTEXT for inner-layer references at layered sources. Honorific: KEEP-HONORIFICS-SOURCE without gloss for major honorifics. Strategic: PRESERVE-CULTURAL-SPECIFICITY.

**Examples spread across source cultures:**
- *Said Nursi corpus:* A Western convert who has lived in a Naqshbandi-Khalidi community for 15 years. Knows "Hazret-i Üstad" carries honorific weight; recognizes major Sufi figures (Mevlana, Abdulkadir-i Geylani). AI: TRANSLITERATE-FULLY for established terms; FLAG-CULTURAL-CONTEXT only for the most specialist Naqshbandi-Khalidi-internal references.
- *Hebrew biblical:* A long-term Christian-clergy reader with biblical-Hebrew study and Jerusalem residence. AI: TRANSLITERATE-FULLY for Hebrew terms in established transliteration; KEEP-HONORIFICS-SOURCE.
- *Quranic:* A 20-year scholar-resident in a Muslim country. AI: TRANSLITERATE-FULLY for major Quranic terms; ASSUME-SHARED-CULTURAL-KNOWLEDGE for major Islamic-theological frames.
- *Hindu Sanskrit:* A Westerner who has been a Hindu practitioner for 25 years and lived in India for 10. AI: TRANSLITERATE-FULLY for major Sanskrit terms; KEEP-HONORIFICS-SOURCE.
- *Greek classical:* A classics professor who has spent sabbaticals in Greece. AI: TRANSLITERATE-FULLY for Greek terms in established transliteration; ASSUME-SHARED-CULTURAL-KNOWLEDGE for major cultural assumptions.

**Distinguishing logic from `acquainted`:** The `familiar` reader has SUSTAINED IMMERSION (years of residence, decades of practice, or both). They have lived cultural-fluency: they catch most cultural references silently; they understand cultural assumptions through having lived them; they don't need brief FLAG-CULTURAL-CONTEXT for major cultural anchors. The `acquainted` reader has SOME EXPOSURE but not immersion. The translator-AI can ASSUME-SHARED-CULTURAL-KNOWLEDGE at `familiar` where it would need to FLAG-CULTURAL-CONTEXT at `acquainted`.

#### 2.4 `heritage`

**Reader profile.** Identity inherited but diluted. Typically: 2nd-generation or later diaspora; raised in a mixed household (one parent from source culture); heritage but not actively practicing; born of source-culture family but raised outside the source country. Has bicultural identity with target-primary; carries source-cultural traces and cultural-anchor knowledge but with some dilution.

**Cultural-proximity-tier.** Inherited cultural-fluency, partially diluted. Catches major cultural anchors via inheritance; may miss some specialist or inner-layer cultural assumptions. Has the inherited identity that distinguishes from `familiar` but lacks the full immersion of `source-native`.

**Cultural-context-tier.** Handles general-cultural + major-religious-text + popular-cultural-celebration register through inheritance. May have gaps at scholar-canonical or inner-layer register.

**Cultural-handling-test.** Proper-noun: TRANSLITERATE-FULLY for major heritage-known terms; TRANSLITERATE-WITH-GLOSS for less-central or inner-layer references. Cultural-context: ASSUME-SHARED-CULTURAL-KNOWLEDGE for major cultural anchors; FLAG-CULTURAL-CONTEXT for inner-layer or specialist references. Honorific: KEEP-HONORIFICS-SOURCE. Strategic: PRESERVE-CULTURAL-SPECIFICITY.

**Examples spread across source cultures:**
- *Said Nursi corpus:* A 2nd-generation Turkish-American whose parents emigrated from a Turkish-Muslim community but who was raised in the U.S. without active Naqshbandi-Khalidi practice. Knows "Allah", "Quran", basic Islamic vocabulary through inheritance; may not reliably catch Naqshbandi-Khalidi-specific terminology. AI: TRANSLITERATE-FULLY for general Islamic terms; FLAG-CULTURAL-CONTEXT for Naqshbandi-Khalidi-specific.
- *Hebrew biblical:* A 3rd-generation Jewish-American without active religious observance but cultural-Jewish identity. AI: ASSUME-SHARED-CULTURAL-KNOWLEDGE for major Jewish-cultural anchors; FLAG-CULTURAL-CONTEXT for specialist scholarship.
- *Quranic:* A 2nd-generation Muslim-American without active mosque attendance but cultural-Muslim identity. AI: ASSUME-SHARED-CULTURAL-KNOWLEDGE for major Quranic-cultural anchors; FLAG-CULTURAL-CONTEXT for specialist theology.
- *Hindu Sanskrit:* A 3rd-generation Indian-American without active religious observance but cultural-Hindu identity. AI: ASSUME-SHARED-CULTURAL-KNOWLEDGE for major figures (Rama, Krishna); FLAG-CULTURAL-CONTEXT for Vedic specialist terms.
- *Chinese Confucian:* A 2nd-generation Chinese-American whose family has Confucian cultural background but who was raised mostly in U.S. cultural context. AI: ASSUME-SHARED-CULTURAL-KNOWLEDGE for major figures; FLAG-CULTURAL-CONTEXT for specialist Confucian-cultural references.

**Distinguishing logic from `familiar`:** The `heritage` reader has INHERITED identity (raised by source-culture family; descended from source culture; bicultural identity carried from childhood). The `familiar` reader has ACQUIRED proximity (convert; long-resident; scholar-immersed) without inherited identity. Heritage gives the reader cultural-anchor knowledge through upbringing (even if practice has lapsed); familiar gives the reader lived cultural-fluency through immersion. Both can ASSUME-SHARED-CULTURAL-KNOWLEDGE for major anchors; the heritage reader has more reliable major-anchor inheritance; the familiar reader has more current-practice immersion. They sit at similar operational positions for most handling decisions but the distinction matters for inner-layer references (heritage reader has inherited general but not specialized; familiar reader has immersion-acquired which may include specialist).

#### 2.5 `source-native`

**Reader profile.** Born and raised in the source culture; primary identity source. Includes 1st-generation immigrants who emigrated as adults (primary identity still source despite current residence elsewhere). For religious-text sources, includes born-and-raised practitioners with active practice.

**Cultural-proximity-tier.** Full lived cultural-fluency with source-primary identity. Catches all cultural references silently; understands all cultural assumptions through having lived them since birth; recognizes source-language honorifics in their full register.

**Cultural-context-tier.** Handles all source-cultural registers including specialist-cultural register, inner-layer register, source-language-native subtle register.

**Cultural-handling-test.** Proper-noun: TRANSLITERATE-FULLY across the board; the reader recognizes source-language forms in original script or transliteration. Cultural-context: ASSUME-SHARED-CULTURAL-KNOWLEDGE for everything. Honorific: KEEP-HONORIFICS-SOURCE. Strategic: PRESERVE-CULTURAL-SPECIFICITY at maximum (the reader doesn't need foreignization-preserving alternatives — they ARE the cultural context).

**Examples spread across source cultures:**
- *Said Nursi corpus:* A born-and-raised Turkish-Muslim from a Naqshbandi-Khalidi-leaning community in Turkey. AI: TRANSLITERATE-FULLY for everything; ASSUME-SHARED-CULTURAL-KNOWLEDGE for all cultural assumptions including Naqshbandi-Khalidi-specific tradition.
- *Hebrew biblical:* A born-and-raised observant Jew from an Orthodox community with strong biblical-Hebrew literacy. AI: TRANSLITERATE-FULLY; ASSUME-SHARED-CULTURAL-KNOWLEDGE.
- *Quranic:* A born-and-raised Muslim from a country with strong Quranic-recitation tradition (Egypt, Morocco, Indonesia). AI: TRANSLITERATE-FULLY; ASSUME-SHARED-CULTURAL-KNOWLEDGE for full Quranic-cultural context.
- *Hindu Sanskrit:* A born-and-raised Hindu from India with active practice. AI: TRANSLITERATE-FULLY; ASSUME-SHARED-CULTURAL-KNOWLEDGE.
- *Chinese Confucian:* A born-and-raised Chinese reader from a Confucian-tradition-respecting family with classical-Chinese literacy. AI: TRANSLITERATE-FULLY; ASSUME-SHARED-CULTURAL-KNOWLEDGE.

**Distinguishing logic from `heritage`:** The `source-native` reader has BORN-AND-RAISED primary identity. The `heritage` reader has INHERITED but DILUTED identity (raised in mixed household; lost language; lapsed practice). The source-native catches inner-layer references silently; the heritage reader may need brief FLAG-CONTEXT for inner-layer specialist references. The source-native ASSUMES all source-cultural context; the heritage reader has the general-anchor inheritance but may need light support for specialized assumptions.

### 3. Cross-Axis Boundaries

#### 3.1 A3 ↔ A1 cultural-reference-recognition (identity vs competence)

**Criterion.** A1's cultural-reference-recognition sub-field is COMPETENCE-based: does the reader know the references? A3 is IDENTITY-based: does the reader come from inside the culture?

**Four-corners independence demonstration** (per root finding):

- *Well-read insider:* A born Muslim Islamic-studies professor who studied Said Nursi formally. A1 high (catches all references) + A3 source-native.
- *Poorly-read insider:* A born Muslim who has not studied Islamic theology formally and has lapsed practice. A1 lower (may miss less-common references) + A3 source-native or heritage.
- *Well-read outsider:* A Western academic Islamicist who has studied Islamic-cultural references through scholarship without living in a Muslim community. A1 high (recognizes references through study) + A3 outsider or acquainted.
- *Uninitiated outsider:* A typical Western non-Muslim reader. A1 low + A3 outsider.

All four corners are real. The translator-AI applies BOTH axes per encountered item: A1 decides whether the reader recognizes a specific cultural reference (and at what tier); A3 decides whether the reader has the LIVED cultural context that gives the reference its native weight. A well-read outsider catches "Üstad" as a reference (A1 fires) but may not have the lived-identity associations the source-native has (A3 fires).

#### 3.2 A3 ↔ A2 Domain Expertise (cultural identity vs domain expertise)

**Criterion.** A2 captures depth of specialist knowledge in the source's DOMAIN (Islamic theology, biblical scholarship, etc.). A3 captures identity-based proximity to source's CULTURE (broader than domain). They are distinct.

**Four-corners independence:**

- *High A2 + low A3:* A Western academic Islamicist who has spent a career studying Islamic theology but has never lived in a Muslim-majority country and is not Muslim. A2=expert + A3=outsider or acquainted.
- *Low A2 + high A3:* A born Muslim with no formal Islamic-studies education. A2=lay + A3=source-native.
- *High A2 + high A3:* A born Muslim Islamic-studies professor. A2=expert + A3=source-native.
- *Low A2 + low A3:* A typical Western non-Muslim reader. A2=lay + A3=outsider.

All four corners are real. The translator-AI's handling decisions differ across these four: A2=expert + A3=outsider can use technical-vocabulary freely (A2 fires for specialist-vocabulary handling) but may need cultural-context flagging for source-cultural assumptions the reader doesn't have lived experience with (A3 fires for cultural-context handling).

#### 3.3 A3 ↔ A4 Purpose

**Criterion.** A4 Purpose answers "WHY is the reader reading?" (scholarly study / devotional reading / casual reading / language learning / performance). A3 answers "WHO is the reader?" (cultural-identity).

**Interaction.** A4 and A3 interact at runtime: a devotional reading by a source-native reader (`source-native` + `devotional`) handles differently from a casual reading by an outsider (`outsider` + `casual`). But they are distinct concepts: a specialist source-native may read for casual purpose (relaxation); a curious outsider may read for scholarly purpose (research).

#### 3.4 A3 ↔ A5 Source Fidelity

**Criterion.** A3 is reader-side (the reader's cultural identity). A5 is translation-strategy-side (the translator's foreignization-vs-domestication stance).

**Interaction.** A3 and A5 interact: low A3 reader (outsider) tends to suit foreignized translation IF the user wants the reader to encounter source-cultural specificity (the foreignization Venuti advocates); high A3 reader (source-native) doesn't need foreignization to encounter source culture (they ARE the culture). But they are distinct: A3 captures the reader; A5 captures the strategy. A user could set A3=outsider + A5=heavily-foreignized to give an outsider reader full source-cultural encounter, OR A3=outsider + A5=balanced for a more accessible translation.

### 4. Action Policy (DOMESTICATE-CULTURAL-FRAME + ANGLICIZE-HONORIFICS disfavored)

The action policy from `a1_cultural_reference_recognition_levels/finding.md` extends to A3.

**Anchor 1: User's translation-register-fidelity memory.** "Translation register fidelity — don't pull plain source registers up into ornate/archaic English; preserve register alternation as Tier 1/2 structure." The principle is about register but its broader commitment is preservation of source-cultural character.

**Anchor 2: Lawrence Venuti's foreignization ethics.** Domesticating translation makes the translator invisible and erases the foreignness that gives the source its specificity.

**Policy:**

- **DOMESTICATE-CULTURAL-FRAME** is structurally retained as a last resort but project policy DISFAVORS. It substitutes a target-cultural framework for the source's (e.g., replacing "Allah" with "God" throughout; replacing "Üstad" with "Master"). At low A3 levels the AI might naturally lean this way; project policy disfavors and prefers foreignization-preserving alternatives.
- **ANGLICIZE-HONORIFICS** is similarly DISFAVORED. The source's honorific tradition carries cultural weight (Hazret-i Üstad signals deep respect; "the Master" loses this); the project preserves the source honorific.
- **PRESERVE-CULTURAL-SPECIFICITY** is the preferred strategic stance at all levels. The source's cultural specificity is the encounter the reader is meant to have.

**Preference order:**

```
PRESERVE-CULTURAL-SPECIFICITY > KEEP-HONORIFICS-SOURCE > TRANSLITERATE-WITH-GLOSS > FLAG-CULTURAL-CONTEXT > BRIDGE-CULTURAL-DISTANCE > [TARGET-LANGUAGE-EQUIVALENT / DOMESTICATE-CULTURAL-FRAME / ANGLICIZE-HONORIFICS] (last resorts)
```

The foreignization-preserving actions (KEEP-HONORIFICS-SOURCE + TRANSLITERATE-WITH-GLOSS + FLAG-CULTURAL-CONTEXT) handle outsider readers without DOMESTICATING. The reader encounters cultural specificity with light support; they are not handed a domesticated version that erases the source culture.

### 5. Edge-Case Mapping

The diaspora gradient and convert / long-resident edge cases map to the 5 levels via lived-cultural-fluency:

| Reader type | A3 level | Reasoning |
|---|---|---|
| Adult convert + decades residence | `familiar` | Strong commitment + immersion but no birth/heritage marker |
| Spouse + 20+ years residence + no conversion | `familiar` | Community immersion without identity-shift |
| Long-term scholar-resident (30 years) | `familiar` | Scholar immersion; lacks practice/devotional identity |
| Recent convert without residence | `acquainted` | Identity-shift without immersion |
| Returnee from diaspora | `heritage` or `source-native` (per lived years) | Conservative-bias places returnee at `heritage` unless they have substantial lived years in source culture |
| 1.5-generation diaspora (came as children) | `heritage` | Bicultural with target-primary; conservative-bias |
| 2nd-generation diaspora | `heritage` | Inherited but diluted; bicultural target-primary |
| 3rd-generation+ | `heritage` (diluted further) | Heritage marker still present but diluted; may approach `acquainted` if heritage is very distant |
| 1st-generation immigrant (emigrated as adult) | `source-native` | Primary identity still source; immigration didn't shift cultural identity |
| Heritage-but-no-practice reader | `heritage` | Inherited identity even without active practice |

**Said Nursi audience spectrum mapping** (the project's primary corpus):

- Western secular reader: `outsider` (default)
- Western reader with general "world religions" exposure: `acquainted`
- Western convert without residence: `acquainted`
- Western convert + 15-year residence in Muslim community: `familiar`
- 30-year scholar-resident in Turkey: `familiar`
- 2nd-generation Turkish-American without active Naqshbandi-Khalidi practice: `heritage`
- 1.5-generation Turkish reader who emigrated as child: `heritage` (conservative-bias)
- 1st-generation Turkish immigrant: `source-native`
- Born-and-raised Turkish-Muslim from Naqshbandi-Khalidi-leaning community: `source-native`

### 6. Reader Family Closure

This finding CLOSES the Reader family — the 3 axes are now fully specified across all their levels:

1. **A1 Reader Level** — composite-axis with 5 sub-fields, each at 5 levels. Specified across the A1 chain ending with `a1_cultural_reference_recognition_levels/finding.md`.
2. **A2 Domain Expertise** — plain-ordinal axis with 5 levels (`lay | aware | educated | trained | expert`). Specified in `a2_domain_expertise_levels/finding.md`.
3. **A3 Source Culture** — plain-ordinal axis with 5 levels (`outsider | acquainted | familiar | heritage | source-native`). Specified here.

**What's now spec'd.** The Reader-family schema is ready for commit:

```python
class A1ReaderLevel:  # composite-axis
    vocabulary_breadth: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    syntactic_processing_capacity: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    idiom_recognition: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    inference_capacity: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    cultural_reference_recognition: Literal["very_basic", "daily", "conversational", "advanced", "native"]

domain_expertise: Literal["lay", "aware", "educated", "trained", "expert"]
source_culture: Literal["outsider", "acquainted", "familiar", "heritage", "source-native"]
```

**What's next.** The remaining axes per the root 8-axis architecture:

- **A4 Purpose** (Purpose family) — categorical axis with ~5 categorical levels (scholarly / devotional / casual / language-learning / performance).
- **A5 Source Fidelity** (Strategy family) — plain-ordinal, 3 levels per root proposal (foreignization ↔ domestication).
- **A6 Form Preservation** (Strategy family) — plain-ordinal, 5 levels per root proposal (ties to harmony-layer Tier 1–4).
- **A7 Scaffolding** (Strategy family) — plain-ordinal, 5 levels per root proposal.
- **A8 Analysis Depth** (Depth family) — plain-ordinal, 4 levels per root proposal (surface / standard / deep / scholarly).

**What's still open per A3 specifically:**

- **Audience-level multi-source-culture configuration.** Some readers have radically different A3 proximities to different source cultures simultaneously. The natural future schema: `audience.source_culture_proximity: list[(source_culture, level)]`. Future inquiry.
- **Layered-source-culture full operational spec.** This finding's primary-culture-with-runtime-layer-detection note covers the conceptual handling but a full operational spec (how the AI detects layer-membership; how it adjusts handling per layer) is a runtime implementation concern.
- **Time-shift identity refresh.** Cultural identity shifts over time (recent conversion; recent emigration; second-generation children growing up). Configuration is a snapshot at config time; refresh-cadence is an audience-level concern.

---

## Inherited Commitments Re-test

This finding inherits commitments from 3 prior outputs: the root architectural finding, the A2 Domain Expertise inquiry, and the A1 cultural-reference-recognition sub-field finding (the A1 chain's final sub-field, which directly intersects with A3 conceptually).

**IC1 — Receptive-only commitment.**
- **Source:** A1 chain + A2 inquiry.
- **Re-test status:** RE-TESTED.
- **Evidence:** Sensemaking Ambiguity A7 confirmed: A3 is identity-based; the reader's identity is what they bring, not what they produce. Per-level prose (Sections 2.1–2.5) framed as recognition throughout.

**IC2 — Conservative-bias-LOWER default.**
- **Source:** root + A1+A2 chain.
- **Re-test status:** RE-TESTED.
- **Evidence:** Section 1.11. When the user's configuration is silent, the AI assumes OUTSIDER → more FLAG-CULTURAL-CONTEXT, TRANSLITERATE-WITH-GLOSS.

**IC3 — Language-agnostic at concept level.**
- **Source:** root + A1+A2 chain.
- **Re-test status:** RE-TESTED & REFINED.
- **Evidence:** The level FRAMEWORK is language-agnostic (5 cultural-proximity tiers work for any source culture). The IDENTITY CONTENT is culture-specific (a Hindu Sanskrit source culture has different identity markers than a Turkish-Ottoman-Islamic source culture). Caveat preserved.

**IC4 — A3 plain-ordinal pattern.**
- **Source:** root architectural finding.
- **Re-test status:** RE-TESTED.
- **Evidence:** Section 1.4. A3 is plain-ordinal; no sub-fields; no propagation.

**IC5 — A3 cardinality (root proposed 3).**
- **Source:** root architectural finding.
- **Re-test status:** RE-TESTED & REFINED to 5.
- **Evidence:** Section 1.1 documents the substantive argument: the diaspora gradient produces operationally-different translator-AI handling decisions at each step; collapsing to 3 forces a single rule across operationally-distinct readers. Anchored to Brah's diaspora studies + Reader-family schema-ergonomic consistency.

**IC6 — A3↔A1 + A3↔A2 boundaries.**
- **Source:** root + A1 cultural-reference-recognition + A2.
- **Re-test status:** RE-TESTED & DOCUMENTED.
- **Evidence:** Section 3 documents both boundaries with four-corners independence demonstrations (Section 3.1 for A3↔A1; Section 3.2 for A3↔A2). Also Section 3.3 (A3↔A4) and 3.4 (A3↔A5) for completeness.

**IC7 — A3 scope (cultural references + transliterations + cultural-context flagging).**
- **Source:** root architectural finding.
- **Re-test status:** RE-TESTED.
- **Evidence:** Section 1.7's 10 handling actions in 4 categories operationalize the scope.

**IC8 — 4-component template adapts as needed.**
- **Source:** A1+A2 chain.
- **Re-test status:** RE-TESTED & APPLIED (MEDIUM).
- **Evidence:** Section 1.2. Adaptation parallels A2's MEDIUM: reader profile + cultural-proximity-tier + cultural-context-tier + cultural-handling-test.

**IC9 — DOMESTICATE-disfavored project policy.**
- **Source:** `a1_cultural_reference_recognition_levels/finding.md`.
- **Re-test status:** RE-TESTED & EXTENDED to A3.
- **Evidence:** Section 4 documents the policy extension. DOMESTICATE-CULTURAL-FRAME + ANGLICIZE-HONORIFICS disfavored per the same anchors (user's translation-register-fidelity memory + Venuti foreignization). PRESERVE-CULTURAL-SPECIFICITY preferred.

**IC10 — Translator-AI runtime determination mechanism.**
- **Source:** A2 inquiry.
- **Re-test status:** RE-TESTED.
- **Evidence:** Section 1.10 documents. Handles layered-source-culture cases at runtime by examining reference's cultural-layer-membership.

**IC11 — Single-domain default analog (from A2).**
- **Source:** `a2_domain_expertise_levels/finding.md`.
- **Re-test status:** RE-TESTED & APPLIED as single-source-culture default.
- **Evidence:** Section 1.5 documents. Parallel reasoning to A2: source has one primary culture per translation job; the source's culture implicit at runtime; multi-source-culture deferred to audience-level.

**IC12 — Identity-meaningful labels `outsider | acquainted | familiar | heritage | source-native`** (NEW).
- **Source:** Sensemaking Ambiguity A8 + A1 + Brah diaspora studies anchor.
- **Re-test status:** NEW.
- **Anchor:** Diaspora studies (Brah's diasporic identification gradient) + religious-insider sociology (Rambo on conversion; Sherman Jackson on Blackamerican Islam) + Stuart Hall on cultural identity.

**IC13 — Composite-with-primary-axis identity dimension** (NEW).
- **Source:** Sensemaking Ambiguity A2.
- **Re-test status:** NEW.
- **Anchor:** Section 1.3. Headline dimension = lived cultural-fluency; sub-markers (residential, linguistic, practice, religious, heritage) aggregate with context-dependent weighting.

**IC14 — 10 handling actions in 4 categories** (NEW).
- **Source:** Surfacing R9 + sensemaking Ambiguity A6.
- **Re-test status:** NEW.
- **Anchor:** Section 1.7. 4 categories (proper-noun / cultural-context / honorific / strategic) with 10 total actions.

**IC15 — Layered-source-culture handling (primary-culture + runtime-layer-detection)** (NEW).
- **Source:** Sensemaking Ambiguity A4.
- **Re-test status:** NEW.
- **Anchor:** Section 1.6. A3 captures primary (innermost) layer proximity; AI handles within-layer variation at runtime.

---

## Next Actions

### MUST

- **What:** Commit the A3 enum to the schema: `source_culture: Literal["outsider", "acquainted", "familiar", "heritage", "source-native"]`.
  - **Who:** User.
  - **Gate:** Condition-bound — when ready to lock the A3 spec.
  - **Why:** Enables the translator-AI to receive the A3 configuration as prompt context.

- **What:** Verify the per-level prose (Section 2) includes ≥3 different source-culture examples per level and the Said Nursi corpus position at each level.
  - **Who:** This finding (already done — Section 2.1–2.5 includes Turkish-Ottoman-Islamic + Hebrew biblical + Quranic + Hindu Sanskrit + Chinese Confucian + Greek classical examples at each level + Said Nursi position).
  - **Gate:** Observable.
  - **Why:** Per critique CC-B refinement note; prevents source-culture lock-in; honors the user's pattern across A2.

### COULD

- **What:** Add an `audience.source_culture_proximity: list[(source_culture, level)]` field at the audience level for multi-source-culture readers.
  - **Who:** Future audience-level inquiry.
  - **Gate:** Condition-bound — when the user reaches the audience-level inquiry.
  - **Why:** Enables multi-source-culture configuration for readers with radically different proximities across source cultures.
  - **Depends-on:** MUST item "Commit the A3 enum". GATED.

- **What:** Add a translator-AI prompt-engineering pass that embeds Sections 1, 2, 3, 4, 5 of this finding as system-context.
  - **Who:** Translation runtime / prompt-engineering layer.
  - **Gate:** After schema commit.
  - **Why:** Makes the A3 level definitions operationally available to the AI.
  - **Depends-on:** MUST item. GATED.

### DEFERRED

- **What:** Etic/emic anthropology cross-domain illustration (full-etic / informed-etic / etic-with-immersion / emic-claim / full-emic).
  - **Gate:** Revival — if future inquiries need additional cross-domain anchors.
  - **Why (if revived):** Provides additional didactic anchor.

- **What:** Adaptive runtime cultural-identity estimation — translator-AI dynamically estimates reader cultural identity from feedback signals.
  - **Gate:** Revival — when AI capability matures (5-10 years).
  - **Why (if revived):** Removes static configuration burden; adapts to reader's actual identity-related cues over time.

---

## Reasoning

### Why 5 levels (and not 3 per root proposal)

The user did NOT pre-specify cardinality for A3 (unlike A2 where they directed 5). This inquiry decided on substantive grounds.

**Rejected: 3-level interpretation** (`outsider / familiar / source-native` per root). Identity feels naturally discrete (you're either born into a culture or not), suggesting a clean trichotomy. But the operational reality of translator-AI handling decisions cuts finer.

**Survived: 5-level interpretation.** The diaspora gradient (1st-generation immigrant, 1.5-generation, 2nd-generation, heritage-only, outsider) produces OPERATIONALLY DIFFERENT translator-AI handling decisions at each step. A 1st-gen immigrant (born in source, emigrated as adult) handles references at parity with a never-emigrated source-native; the AI can TRANSLITERATE-FULLY without gloss. A 2nd-gen reader may need brief TRANSLITERATE-WITH-GLOSS for less-central references. A heritage-only reader needs more FLAG-CONTEXT. These are not artificial distinctions — they're empirically grounded in diaspora studies (Avtar Brah on diasporic identification gradients) and religious-insider sociology (Sherman Jackson on Blackamerican Islam).

Schema ergonomic consistency also favors 5 (Reader family pattern is 5 per axis).

### Why composite-with-primary-axis (and not single dimension OR separate axes)

**Rejected: Single dimension "cultural-proximity".** Too vague to operationalize. "Cultural-proximity" alone doesn't say what marker matters: birth? Lived years? Language? Religion? Heritage?

**Rejected: Multiple separate dimensions** (linguistic identity + religious identity + residential identity as separate axes). Multiplies configuration burden. Most readers don't have radically divergent sub-dimensions; a Turkish-Muslim raised in Turkey is high on residential, linguistic, religious simultaneously.

**Survived: Composite-with-primary-axis.** Headline dimension = lived cultural-fluency (composite of residential + linguistic + practice + religious + heritage markers). Sub-dimensions modify the headline for context-specific cases: religious-text sources weight religious identity more; secular sources weight residential/linguistic more; layered sources (Said Nursi) need both inner-layer and outer-layer awareness via runtime layer detection.

### Why DOMESTICATE-CULTURAL-FRAME disfavored (extending A1 policy)

The A1 cultural-reference-recognition finding committed to a project-policy that DISFAVORS DOMESTICATE per the user's translation-register-fidelity memory + Venuti's foreignization ethics. Two natural alternatives were considered:

**Rejected: DOMESTICATE-at-parity.** Treat DOMESTICATE-CULTURAL-FRAME as a normal handling action at low A3 levels (replacing "Allah" with "God" for outsider readers). Why killed: project's broader commitment is foreignization-preserving. DOMESTICATE at low A3 erases source-cultural specificity precisely where the reader most needs to encounter it (to learn about the source culture). Conflicts with Venuti.

**Rejected: DOMESTICATE-banned-entirely.** Remove DOMESTICATE-CULTURAL-FRAME from the action vocabulary. Why killed: structural completeness — there are edge cases where DOMESTICATE is genuinely the only viable option (very_basic reader + opaque reference + no foreignization-preserving alternative works without burdening the text).

**Survived: DOMESTICATE-disfavored.** Keep DOMESTICATE-CULTURAL-FRAME and ANGLICIZE-HONORIFICS in the action vocabulary as LAST RESORTS; project policy explicitly disfavors. Foreignization-preserving alternatives (FLAG-CULTURAL-CONTEXT + TRANSLITERATE-WITH-GLOSS + PRESERVE-CULTURAL-SPECIFICITY) handle outsider readers at low A3.

### Why single-source-culture default

Parallel reasoning to A2's single-domain default. A3 is for a SPECIFIC translation job; the source text has ONE primary culture. Multi-source-culture configuration adds complexity without operational benefit at the A3 layer. Cross-source-culture references within a source text are handled at runtime by the AI's cross-cultural knowledge.

### Why labels diverge from A1 and A2

A1 labels are general-fluency-graded (`very_basic | daily | conversational | advanced | native`). A2 labels are expertise-graded (`lay | aware | educated | trained | expert`). A3 needs identity-meaningful labels — labels that capture identity-based proximity, not capacity or knowledge depth.

The survived label set (`outsider | acquainted | familiar | heritage | source-native`) maps to diaspora-studies and religious-insider categories. Same-labels-for-default-propagation is an A1-composite-axis concern; A2 and A3 are both plain-ordinal so their labels can be domain-appropriate.

---

## Open Questions

### Monitoring

- **AI prompt-context calibration.** Observe whether the AI's per-reference handling decisions match the level definitions at runtime. Over-glossing vs under-glossing patterns may signal calibration adjustment needs.

### Blocked

- **Multi-source-culture configuration.** Cannot be specified until the audience-level inquiry establishes the `audience.source_culture_proximity` field. Blocked by COULD item 1.

- **Purpose family inquiry (A4).** A4 Purpose is the next axis; doesn't depend on A3 but is logically next.

### Research Frontiers

- **Adaptive runtime cultural-identity estimation.** Translator-AI dynamically estimates reader cultural identity from feedback signals (clarifying questions; hover-clicks; engagement patterns). Long-horizon; depends on AI capability development.

- **Per-cultural-layer expertise distinction within a layered source culture.** Currently handled by primary-culture-with-runtime-layer-detection. A more granular per-layer configuration is a future research question.

### Refinement Triggers

- **Refinement trigger for cardinality.** If user feedback indicates the 5-level granularity is unused (users cluster at 3 levels), revisit. Diaspora-studies anchoring is well-established but operational empirical evidence may differ.

- **Refinement trigger for labels.** If user feedback indicates the labels read oddly in actual prompt context, revisit. The diaspora-studies anchor is well-established but labels are reversible.

- **Refinement trigger for A3↔A1 boundary.** If same-word-fires-both produces translator-AI confusion at runtime, the boundary criterion may need refinement.

- **Refinement trigger for the DOMESTICATE-disfavored policy.** If the project expands beyond corpora where foreignization is appropriate (e.g., children's literature, where domestication may be appropriate), the policy may need per-corpus override.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
now lets do it for A3 Source Culture in devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md
```

</details>
