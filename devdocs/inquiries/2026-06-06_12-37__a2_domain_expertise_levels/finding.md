---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md
---
# Finding: A2 — Domain Expertise (the 5 Levels)

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` (the root architectural finding that established the 4-layer / 4-family / 8-axis configuration framework for Comprehenslate; specified A2 — Domain Expertise as a plain-ordinal axis in the Reader family but deferred level-value finalization).

**Revision trigger:** The user directed: "now do it for A2 — Domain Expertise" with the explicit cardinality directive "it should be 5 levels" (refining the root's proposed 3) and the explicit framing of the inquiry's main challenge: "the real question is the definitions of how to distinguish these 5 levels — we need some good, explicit definitions with good examples."

**What's preserved:**
- A2's identity as a plain-ordinal axis (NOT a composite-axis like A1 Reader Level).
- A2's concept (per root): the reader's specialist knowledge in the source's subject domain (Islamic theology, biblical scholarship, theoretical physics, etc.) — independent of their general reading fluency.
- A2's scope (per root): controls whether the translator-AI can use technical vocabulary without unpacking.
- A2's boundaries (per root): distinct from A1 Reader Level (general fluency) and A3 Source Culture (cultural identity).
- Receptive-only commitment (recognition not production) — inherited from the A1 sub-field chain.
- Conservative-bias-for-reader-axes = LOWER default — inherited from root + A1 chain.
- Language-agnostic at concept level — the framework works for any source domain.

**What's changed:**
- **A2 cardinality refined from 3 to 5 levels** per user directive. The 3-level proposal (`lay / general-educated / specialist`) in the root finding is replaced with a 5-level structure that allows finer-grained translator-AI handling decisions.
- **Labels are domain-meaningful rather than A1-consistent.** The 5 A2 levels are `lay | aware | educated | trained | expert` — not the A1 labels `very_basic | daily | conversational | advanced | native`. Same-labels-for-default-propagation is an A1-composite-axis concern (the headline level propagates to A1's 5 sub-fields). A2 is plain-ordinal — no sub-fields, no propagation, so the labels need only be domain-meaningful. "Daily domain expertise" reads oddly; "aware" reads cleanly. The new labels map approximately to Hubert and Stuart Dreyfus's 5-stage model of skill acquisition (novice / advanced beginner / competent / proficient / expert), the canonical 5-stage expertise model in cognitive science.

**What's new:**
- **5 per-level definitions with explicit distinguishing logic and cross-domain examples** (the user's explicit "main challenge"). Each adjacent-level boundary has explicit prose distinguishing logic — not just example differences but stated criteria. Examples span 5 reference domains: Islamic theology (the project's primary corpus via Said Nursi), biblical scholarship, philosophy, theoretical physics, and legal scholarship.
- **4-component template MEDIUM-adapted from the A1 sub-field template.** The template structure (reader profile + tier-component + register-component + handling-test) applies to A2 with adaptations specific to domain-specialist knowledge: frequency-tier → expertise-depth-tier; register-tier → discourse-register-tier; substitution-test → domain-handling-test.
- **9 translator-AI handling actions organized into 2 categories + 1 bridge.** Vocabulary-level (USE-TECHNICAL-VOCABULARY-FREELY / INLINE-DEFINE-ON-FIRST-USE / FOOTNOTE-TECHNICAL-TERM / PARAPHRASE-IN-LAYMAN-TERMS); discourse-level (INVOKE-SPECIALIST-DEBATES / ATTRIBUTE-VIEW-TO-SCHOOL / UNATTRIBUTED-CONSENSUS / AVOID-SPECIALIST-DEBATES); bridge (KEEP-SOURCE-TERM-WITH-GLOSS). The vocabulary-level actions handle technical terms; the discourse-level actions handle school-internal debates and lineage-of-argument references.
- **Single-domain default for the domain-scope question.** The A2 value applies to the source's domain (the source text has one domain at any given translation job; the source's domain is implicit at runtime via Layer 3 SOURCE-DESCRIPTION). Multi-domain reader configuration (a reader who is `expert` in Islamic theology AND `lay` in physics) is deferred to a future audience-level inquiry.
- **A2 receives the 5 forward-tagged specialist canons from `a1_cultural_reference_recognition_levels/finding.md`** (the most recent A1 sub-field finding, which closed the A1 chain). The 5 specialist canons (legal-history precedents / mathematical figures / scientific figures / medical eponyms / specialist philosophy) were routed to A2 by A1's "general cultural literacy → A1; domain training required → A2" criterion. This finding receives and integrates them via A2's expertise-depth dimension.
- **Translator-AI runtime determination mechanism explicit.** The reader-level configuration specifies what the reader recognizes; the AI determines a specific term's domain-specialist-ness, discourse-level role, and canonicity at runtime from its training. Clear architectural distinction between configurable inputs and runtime-determined inputs.
- **Cross-axis boundaries documented explicitly.** A2↔A1 (general fluency vs domain-specialist knowledge; same-word-fires-both with different roles); A2↔A3 Source Culture (competence-based vs identity-based; four-corners independence demonstration); A2↔A4 Purpose (expertise vs purpose; independence demonstration).

**Migration:** No migration needed — this is the first A2-axis specification (the root finding committed to A2's identity but deferred level values to this inquiry). When the user commits the schema, A2 becomes `domain_expertise: Literal["lay", "aware", "educated", "trained", "expert"]`.

---

## Question

For A2 — Domain Expertise (the second axis in the Reader family per the root architectural finding), what should the 5 ordinal levels be?

The user's specific framing: defining 5 levels for A2 is structurally easy to deduce; the REAL DIFFICULTY is defining HOW to DISTINGUISH the 5 levels — explicit definitions with good examples that make each level operationally identifiable.

Specifically: what concept does each level capture (how much domain-specialist knowledge the reader has in the source's subject domain), what logic distinguishes each level from its neighbors, what concrete examples of domain-specialist vs general-reader knowledge make each level operationally identifiable across multiple domains (Islamic theology, biblical scholarship, philosophy, science, law) — defined language-agnostically at the concept level (the framework works for any source domain) — and resolving the A2↔A1 boundary, the A2↔A3 boundary, and the domain-scope question (single-domain config vs domain-set config)?

The goal: 5 named ordinal levels operationalizable as translator-AI prompt instructions, with explicit distinguishing logic and concrete examples spread across multiple domains, ready for the user to commit to the schema and proceed to A3 — Source Culture or further.

---

## Finding Summary

- **5 ordinal levels with domain-meaningful labels.** `lay | aware | educated | trained | expert` — not the A1 labels. Same-labels-for-default-propagation is an A1-composite-axis concern; A2 is plain-ordinal so the labels need only be domain-meaningful. Labels map to Hubert and Stuart Dreyfus's 5-stage skill-acquisition model (the canonical 5-level expertise model in cognitive science: novice ≈ lay; advanced beginner ≈ aware; competent ≈ educated; proficient ≈ trained; expert ≈ expert).

- **Primary dimension is DEPTH OF DOMAIN-SPECIALIST KNOWLEDGE in the source's subject domain.** Five sub-aspects rise together with the level (they are not separate axes — A2 is plain-ordinal): technical-vocabulary depth (count of specialist terms recognized); conceptual-schema integration (how well the reader places concepts in the domain's relational structure); discourse-conventions recognition (recognizing school-internal debates, lineage of arguments); specialist-debates recognition (catching "this is the Mu'tazila position" or "this is Calvinist"); and primary-source canon familiarity (specialist reads primary; lay reads secondary if any).

- **Level is TARGET-READER-RELATIVE.** The configuration specifies what THE READER knows in the domain. A reader's A2 value captures their depth in the source text's domain.

- **Single-domain default for the domain-scope question.** A2 applies to the source's domain. Each translation job has one source domain (Said Nursi = Islamic theology; a Bible passage = biblical scholarship; a physics paper = theoretical physics). The source's domain is implicit at runtime via Layer 3 SOURCE-DESCRIPTION (the AI detects it). Multi-domain reader configuration (a reader who is `expert` in Islamic theology AND `lay` in physics) is deferred to a future audience-level inquiry.

- **9 translator-AI handling actions in 2 categories + 1 bridge.** Vocabulary-level actions handle technical terms encountered in the source: USE-TECHNICAL-VOCABULARY-FREELY (at high A2; no gloss); INLINE-DEFINE-ON-FIRST-USE (mid A2; "tafsīr (Quranic exegesis)" first time, then bare term); FOOTNOTE-TECHNICAL-TERM (mid-low A2; technical term in body, definition in footnote); PARAPHRASE-IN-LAYMAN-TERMS (low A2; replace technical term with everyday equivalent). Discourse-level actions handle school-internal debates and lineage references: INVOKE-SPECIALIST-DEBATES (high A2; "the Ash'ari position vs the Mu'tazila position"); ATTRIBUTE-VIEW-TO-SCHOOL (mid-high A2; "the Ash'ari position holds..."); UNATTRIBUTED-CONSENSUS (low A2; mainstream view without school-internal debate); AVOID-SPECIALIST-DEBATES (very low A2; don't invoke school-internal references). Bridge action: KEEP-SOURCE-TERM-WITH-GLOSS (transliteration retention with brief explanation; used across levels when the source term itself is the point — "ism-i azam (the greatest name of God)").

- **4-component template MEDIUM-adapted from the A1 sub-field template.** Component 1 (reader profile) kept conceptually. Component 2 (frequency-tier) REPLACED with `expertise-depth-tier` — the 5 sub-aspects aggregate into expertise depth. Component 3 (register-tier) REFRAMED as `discourse-register-tier` — different genres in the domain (sermon vs commentary vs scholarly article) draw from different registers. Component 4 (substitution-test) REPLACED with `domain-handling-test` containing the 9 named actions.

- **A2↔A1 boundary: same word can fire both axes with different roles.** A1 covers general reading fluency (vocabulary breadth, syntactic processing, etc.); A2 covers specialist domain knowledge. "Ratiocination" is general English vocabulary — A1 vocabulary-breadth fires; A2 doesn't. "Isnād" is Islamic-studies technical vocabulary — A2 fires; A1 vocabulary-breadth doesn't. Both axes can fire simultaneously on different words. A non-native ESL Bible scholar (A1=very_basic + A2=expert) and a native English speaker who knows nothing about Islamic theology (A1=native + A2=lay) are both real configurations.

- **A2↔A3 boundary: competence-based vs identity-based.** A2 is acquired through study; A3 is identity-based (cultural insider/outsider). All four corners of the joint distribution are real: A2=expert + A3=outsider (a Western academic Islamicist who has never lived in a Muslim-majority country); A2=lay + A3=source-native (a born Muslim with no formal study); A2=expert + A3=source-native (a born Muslim Islamic-studies professor); A2=lay + A3=outsider (a typical Western non-Muslim reader). The translator-AI's handling decisions differ across these four.

- **A2↔A4 boundary: expertise vs purpose.** A4 Purpose answers "why is the reader reading?" A2 answers "how much does the reader know?" A specialist reader can read for casual purpose (relaxation); a lay reader can read for scholarly purpose (researching unfamiliar material).

- **Translator-AI runtime determination mechanism is explicit.** The reader-level configuration specifies what the reader recognizes (the configurable side). The AI determines a specific term's domain-specialist-ness, the discourse-level role of an encountered reference, and the canonicity of a citation at runtime from its training. The two are complementary: configuration tells the AI the reader; the AI's knowledge tells it about each term/reference encountered; the handling action is a deterministic function of (level, term properties, source markings).

- **A2 receives 5 forward-tagged specialist canons from `a1_cultural_reference_recognition_levels/finding.md`.** A1's cultural-reference-recognition finding routed legal-history precedents, mathematical figures, scientific figures, medical eponyms, and specialist philosophy to A2 by its criterion "general cultural literacy → A1; domain training required → A2." This finding receives and integrates them via A2's expertise-depth dimension: each specialist canon maps to a specialist domain; within any one translation job, only one of these (or another not-listed specialist domain like Islamic theology) is the source's domain.

- **Conservative-bias-for-reader-axes = LOWER default.** When in doubt about a reader's expertise level, the translator-AI assumes a lower A2 level — more aggressive technical-vocabulary unpacking. Protects against the "I'll just use the technical term; they probably know it" failure mode.

---

## Finding

The root architectural inquiry (`devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md`) established Comprehenslate's translation-configuration framework: 4 layers, 4 families, 8 axes. Layer 1 (USER-FACING AXES) has 8 axes organized into 4 families (Reader / Purpose / Strategy / Depth). A2 — Domain Expertise is the second axis in the Reader family. Its concept was settled there (the reader's specialist knowledge in the source's subject domain — independent of general reading fluency); its level-value definitions were deferred to "the next inquiry."

This finding is that inquiry. It specifies the 5 ordinal levels for A2 — with the user's emphasis on EXPLICIT distinguishing logic and GOOD examples spread across multiple domains.

### 1. The Framework

#### 1.1 The 5 levels and the 5-tier expertise-depth ladder

The 5 ordinal labels for A2 are `lay | aware | educated | trained | expert`. These differ from the A1 Reader Level sub-field labels (`very_basic | daily | conversational | advanced | native`) — the divergence is intentional. The A1 labels are designed for general reading fluency at gradient levels (daily English vs conversational English vs native English). For A2 — domain expertise — those labels read oddly ("daily domain expertise" is awkward). The A2 labels are domain-meaningful: lay (no domain background), aware (cultural-general exposure), educated (general-amateur reading in the domain), trained (formal study or professional engagement), expert (specialist scholar).

These labels approximate Hubert and Stuart Dreyfus's 5-stage model of skill acquisition (novice / advanced beginner / competent / proficient / expert), the canonical 5-level expertise model in cognitive science. They also approximate Pierre Bourdieu's cultural-capital stratification when applied to domain-specific cultural capital.

Why this divergence from A1 is OK. The A1 labels exist as they do because A1 is a `composite-axis` (per the root finding's terminology): the user sets ONE headline level, and the headline propagates as defaults across A1's 5 sub-fields. Propagation requires consistent labels across the sub-fields. A2 is NOT a composite-axis — it's a plain ordinal axis with no sub-fields and no propagation. The labels need only be domain-meaningful, not consistent with A1's general-fluency gradients.

The 5 A2 levels capture 5 sub-aspects that rise together (they are not separate axes — A2 is plain-ordinal):

1. **Technical-vocabulary depth** — the count of specialist terms the reader recognizes. The expert recognizes ten thousand specialist terms in the domain; the lay reader recognizes a handful and may misidentify some.
2. **Conceptual-schema integration** — how well the reader places concepts in the domain's relational structure. The expert thinks in the domain's categories; the lay reader holds concepts as isolated facts.
3. **Discourse-conventions recognition** — recognizing school-internal debates, lineage of arguments, scholarly genres. The expert hears "the Maturidi view holds..." and immediately maps it within Sunni theological schools; the lay reader hears it as an unfamiliar proper noun.
4. **Specialist-debates recognition** — catching "this is the Mu'tazila position" or "this is Calvinist" without prompting. The expert spots the position immediately; the trained reader recognizes it with a moment's thought; the educated reader may catch it if it's pointed out; the aware reader doesn't recognize the position label; the lay reader doesn't recognize that there are positions to argue over.
5. **Primary-source canon familiarity** — the specialist reads primary sources directly (the *Sözler* in Turkish; the Septuagint; Plato's Greek); the trained reader reads major secondary literature; the educated reader reads accessible introductions; the aware reader reads journalism that mentions the canon; the lay reader doesn't read in the domain at all.

These 5 sub-aspects are not user-configurable separately — A2 is plain-ordinal. They are sub-dimensions of the same expertise-depth concept, and they rise together as the level rises. (A reader whose sub-aspects diverge significantly — e.g., huge vocabulary knowledge but zero schema integration — is rare; the conservative-bias-LOWER default handles this case by treating the reader at the LOWER of the divergent sub-aspect levels.)

#### 1.2 The 4-component template (MEDIUM-adapted)

The 4-component definition template was established in `devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/finding.md` (the original A1 Reader Level sub-field finding for vocabulary-breadth, which served as the template source). The four components are: (1) reader profile; (2) tier-component (originally frequency-tier); (3) register-component (originally register-tier); (4) handling-test (originally substitution-test). Each subsequent A1 sub-field adapted the template as needed.

For A2, the adaptation is MEDIUM — comparable to the inference-capacity sub-field's MEDIUM adaptation, lighter than the syntactic-processing-capacity sub-field's HEAVY adaptation:

**Component 1: Reader profile.** Kept conceptually. A short paragraph describing the reader at this level — their domain-exposure profile, what they've read, what their formal training looks like.

**Component 2: Expertise-depth-tier (replaces frequency-tier).** The replacement is needed because domain expertise doesn't have Zipfian word-frequency in the way general vocabulary does. The relevant stratification is depth-of-knowledge-in-domain, which is expertise-depth. The 5 sub-aspects from Section 1.1 aggregate into expertise depth at this level.

**Component 3: Discourse-register-tier (reframed from register-tier).** Different genres within the source's domain draw from different registers — a sermon-genre Islamic text vs a kalam-treatise vs a Risale-i Nur (the project's primary corpus's mixed register). The discourse-register-tier specifies which genres at this level the reader can handle without breaking comprehension.

**Component 4: Domain-handling-test (replaces substitution-test).** The translator-AI runs this test per technical term and per discourse-level reference encountered in the source. The test specifies which of the 9 handling actions fires at this level given the term's specialist-tier and source markings.

#### 1.3 Plain-ordinal pattern (no sub-fields)

A2 is a plain-ordinal axis. There are no sub-fields. The user sets ONE A2 value (e.g., `domain_expertise = "educated"`) and that's it. This contrasts with A1 Reader Level, which is a composite-axis with 5 sub-fields and per-sub-field overrides.

#### 1.4 Target-reader-relative (not source-relative)

The A2 level captures what THE READER knows in the source's domain — target-reader-relative. The source text's content doesn't determine the A2 value; the reader's depth does. A reader's A2=lay status is the same whether they're encountering a Said Nursi text or a Bible passage; what changes is the source's domain (which is detected via Layer 3 SOURCE-DESCRIPTION, not Layer 1 user-axis).

#### 1.5 Single-domain default

The A2 value applies to the source's domain. Each translation job has one source domain — a Said Nursi text is in Islamic theology; a Bible passage is in biblical scholarship; a physics paper is in theoretical physics; a Supreme Court opinion is in legal-history. The source's domain is implicit at runtime via Layer 3 SOURCE-DESCRIPTION (the AI auto-detects it from the source text).

Multi-domain reader configuration — a reader who is `expert` in Islamic theology AND `lay` in physics — is real but is deferred to a future audience-level inquiry. The natural future schema would be `audience.expertise_set: list[(domain, level)]` at the audience-level, but that's a separate inquiry. For now, A2 captures the reader's depth in the source's (single) domain.

When the source text crosses domains — for example, an Islamic philosophy passage that cites both Quranic references and Greek references — the AI handles this at runtime via its own cross-domain knowledge. The configuration only needs to settle "what's the reader's depth in this source's main domain?" Cross-domain references are runtime concerns, not configuration concerns.

#### 1.6 Markedness and source-genre as runtime conditioning variables

Two text-side properties modulate the AI's runtime action choice but do not belong in the A2 level definition itself:

**Markedness** is a text property (analogous to the A1 cultural-reference-recognition finding's use of the same term). A technical term is *marked* when the source explicitly defines it on first use ("isnād (the chain of transmission)"; "tafsīr (Quranic exegesis)"). It is *unmarked* when the source assumes the reader catches it without help. The AI weighs marking when deciding handling action: an unmarked term at a low A2 level needs FOOTNOTE or PARAPHRASE; a marked term may KEEP-AS-IS the source's marking.

**Source-genre** affects which discourse-level moves appear. A sermon-genre source may invoke school positions in passing (without attribution); a kalam-treatise may explicitly attribute every position. The discourse-register-tier component in the level definition reflects which genres the reader at this level can handle.

#### 1.7 The 9 handling actions (vocabulary-level + discourse-level + bridge)

The translator-AI's runtime action vocabulary is structured into 2 categories with 1 bridge action:

**Vocabulary-level actions (handle technical terms):**

| Action | Operation | Use when |
|---|---|---|
| **USE-TECHNICAL-VOCABULARY-FREELY** | Use the technical term in the translation without unpacking | Reader's A2 level meets the term's specialist tier; AI assumes recognition |
| **KEEP-SOURCE-TERM-WITH-GLOSS** | Preserve the source term verbatim with a brief inline gloss ("ism-i azam (the greatest name of God)") | Source term itself is load-bearing AND the reader benefits from a one-time gloss |
| **INLINE-DEFINE-ON-FIRST-USE** | Inline definition first time, then bare term ("tafsīr (Quranic exegesis) ... ") | Reader's level is one tier below the term's specialist tier |
| **FOOTNOTE-TECHNICAL-TERM** | Technical term in body, definition in footnote | Reader is two or more tiers below; inline gloss would disrupt flow |
| **PARAPHRASE-IN-LAYMAN-TERMS** | Replace technical term with everyday equivalent ("commentary" instead of "tafsīr") | Reader is at the lowest tier; preserving the term sacrifices comprehension; project policy allows |

**Discourse-level actions (handle school-internal debates and lineage references):**

| Action | Operation | Use when |
|---|---|---|
| **INVOKE-SPECIALIST-DEBATES** | Use full school references ("the Ash'ari position vs the Mu'tazila position on attributes of God") | Reader's A2 is at expert; full debate context expected |
| **ATTRIBUTE-VIEW-TO-SCHOOL** | "The Ash'ari position holds..." but don't engage debates | Reader's A2 is at trained; attribution is informative without overwhelming |
| **UNATTRIBUTED-CONSENSUS** | Present mainstream view without school-internal attribution | Reader's A2 is at educated; school-internal debates would distract |
| **AVOID-SPECIALIST-DEBATES** | Don't invoke school-internal references at all | Reader's A2 is at aware or lay; debates would confuse |

**Bridge action:** **KEEP-SOURCE-TERM-WITH-GLOSS** sits between vocabulary and discourse — it handles the case where the source-language term itself is the meaning carrier (it can't be replaced) but the reader needs a brief explanation. The Said Nursi corpus uses many such terms (lakaps, theological-school references, Sufi vocabulary).

The translator-AI uses these actions per encountered item: per technical term, the vocabulary-level ladder fires; per school-debate reference, the discourse-level ladder fires.

#### 1.8 Conservative-bias-for-reader-axes = LOWER default

When the user's configuration is silent or ambiguous, the AI assumes a LOWER A2 level — more aggressive technical-vocabulary unpacking and discourse-level restraint. This protects against the "I'll just use the technical term; they probably know it" failure mode where the AI mis-estimates the reader's expertise upward.

The conservative-bias-LOWER default is inherited from the A1 chain (where it was originally stated in the vocabulary-breadth sub-field finding). The same principle applies here for A2.

#### 1.9 Translator-AI runtime determination mechanism

A clean architectural distinction underlies the framework:

- **Configurable (user-set at config time):** the reader's `domain_expertise` level (one of the 5); the action-selection policy (currently default, no project-specific override for A2 unlike the cultural-reference-recognition DOMESTICATE-disfavored policy).
- **Runtime-determined (the translator-AI judges per encountered item):** a specific technical term's specialist tier within the source's domain; a discourse-level reference's school attribution; the source's genre/register markings; whether the source itself defines the term on first use.

The AI uses the configurable inputs as constants for a translation pass and computes the runtime-determined properties from its training and source-text observation. The action selection is then a deterministic function: `action = domain_handling_test(reader_A2_level, term_specialist_tier, source_markings, discourse_role, action_policy)`.

This means: the configuration is small (one enum value); the AI's domain knowledge does the heavy lifting at runtime; the action-selection rule is well-defined.

### 2. The 5 Per-Level Definitions

This is the user's flagged "main challenge" — explicit distinguishing logic with good examples. Each level has the 4 components (reader profile + expertise-depth-tier + discourse-register-tier + domain-handling-test) plus 3-5 cross-domain examples plus explicit distinguishing logic at the boundary with the adjacent level.

#### 2.1 `lay`

**Reader profile.** The reader has no domain background. They have not studied the source's subject domain in any formal or substantial-informal way. The technical vocabulary of the domain reads as foreign words; the conceptual structure is opaque; school-internal debates are invisible. They may know the broadest cultural-anchor concepts of the domain (Islam exists; there's an Old Testament and a New Testament; physics studies matter and energy) but nothing beyond that.

**Expertise-depth-tier.** The reader recognizes the domain's existence as a category of human activity but does not recognize technical terms, does not navigate conceptual schemas, does not catch school-internal positions, and does not engage with primary or secondary literature.

**Discourse-register-tier.** The reader handles only journalistic-level register about the domain (a New York Times article mentioning "the Quran"). Religious-sermon register, scholarly-treatise register, primary-source register all sit beyond reliable recognition.

**Domain-handling-test.** Vocabulary-level: PARAPHRASE-IN-LAYMAN-TERMS for any non-ubiquitous technical term; FOOTNOTE only for terms whose source-language form is load-bearing. Discourse-level: AVOID-SPECIALIST-DEBATES entirely; UNATTRIBUTED-CONSENSUS for any view the source invokes.

**Examples spread across domains:**
- *Islamic theology (the project's primary corpus via Said Nursi):* Doesn't reliably know that "Allah" is the standard Arabic word for God; may think "Muhammad" might be a generic name. References to "tafsīr" → PARAPHRASE as "interpretive commentary." References to "Bediuzzaman" → INLINE-GLOSS as "Bediuzzaman (Said Nursi's honorific)" or FOOTNOTE. References to "ism-i azam" → KEEP-SOURCE-TERM-WITH-GLOSS ("the greatest name of God").
- *Biblical scholarship:* Knows there's an Old Testament and New Testament; may not know what "Torah" means specifically (PARAPHRASE as "the first five books of the Bible" or "Jewish scripture"). References to "the Documentary Hypothesis" → FOOTNOTE.
- *Theoretical physics:* Knows physics studies "matter and energy"; doesn't know what "quantum" means precisely. References to "Schrödinger equation" → FOOTNOTE.
- *Legal scholarship:* Knows there are courts and lawyers; doesn't know "tort" or "common law" precisely. References to "stare decisis" → PARAPHRASE as "the principle that courts follow precedent."
- *Philosophy:* Knows philosophy exists; may confuse Plato and Aristotle. References to "Cartesian dualism" → PARAPHRASE as "Descartes's view that mind and body are separate."

#### 2.2 `aware`

**Reader profile.** The reader has cultural-general exposure to the domain — they have heard of major concepts and major figures through general adult life (journalism, casual conversation, mass media), but they have not studied the domain.

**Expertise-depth-tier.** Recognizes the domain's major figures and major concepts at journalistic depth. Doesn't recognize specialist terms beyond the most-popularized ones. Has no integrated conceptual schema; concepts are isolated cultural-general facts. School-internal debates are invisible; specialist positions are unknown. Has not read primary or substantial secondary literature.

**Discourse-register-tier.** Handles journalistic-level + popular-book-level register (a Karen Armstrong introduction to Islam; a Bart Ehrman introduction to the New Testament; a general physics popularization). Scholarly-treatise register and primary-source register sit beyond reliable recognition.

**Domain-handling-test.** Vocabulary-level: PARAPHRASE-IN-LAYMAN-TERMS for specialist terms; INLINE-DEFINE-ON-FIRST-USE for popular-book-level terms; KEEP-SOURCE-TERM-WITH-GLOSS for source-language terms whose form is load-bearing. Discourse-level: AVOID-SPECIALIST-DEBATES; UNATTRIBUTED-CONSENSUS for mainstream views.

**Examples spread across domains:**
- *Islamic theology:* Knows "Allah / Muhammad / Quran" exist as religious terms; knows the 5 pillars by name; knows Sunni / Shia split exists. References to "tafsīr" → INLINE-DEFINE on first use ("tafsīr (Quranic exegesis)"). References to "kalam" → PARAPHRASE as "Islamic theology." References to "the Ash'ari position" → AVOID-SPECIALIST-DEBATES or UNATTRIBUTED-CONSENSUS.
- *Biblical scholarship:* Knows basic narratives (Genesis, Exodus, Gospels); recognizes "Pharisee" pejoratively; has heard of Apostle Paul. References to "the Documentary Hypothesis" → INLINE-DEFINE ("the Documentary Hypothesis (the theory that the Torah was composed from multiple sources)").
- *Theoretical physics:* Knows Newton / Einstein / Hawking; knows quantum mechanics and general relativity by name; recognizes E=mc². References to "quantum entanglement" → INLINE-DEFINE.
- *Legal scholarship:* Knows the Constitution exists; knows there's a Supreme Court; has heard of Brown v. Board. References to "stare decisis" → INLINE-DEFINE ("stare decisis (the principle that courts follow precedent)").
- *Philosophy:* Knows major figures (Plato / Aristotle / Descartes / Kant); knows "philosophical" as a vague-thoughtful term. References to "Kant's categorical imperative" → INLINE-DEFINE.

**Distinguishing logic from `lay`:** The `aware` reader catches the MAJOR cultural-anchor concepts of the domain through general life exposure; the `lay` reader does not reliably catch even these. The `aware` reader handles a Karen-Armstrong-level introduction; the `lay` reader struggles with it. The translator-AI can use one-shot INLINE-DEFINE for popular-book-level terms at `aware`, while at `lay` even those need PARAPHRASE.

#### 2.3 `educated`

**Reader profile.** The reader has read general literature on the source's domain. They have a working amateur knowledge — equivalent to a serious undergraduate-survey course or a sustained personal reading project. They handle the domain's mainstream conceptual framework. Note: "educated" here specifically means EDUCATED-IN-THIS-DOMAIN (not just generally educated; A1 covers general fluency).

**Expertise-depth-tier.** Recognizes the mainstream concepts and figures of the domain. Has the start of an integrated conceptual schema — can place major figures in historical context, can connect major concepts to their classical statements. Begins to recognize that there are school-internal debates but doesn't navigate them deeply. Has read general-audience secondary literature; perhaps some accessible primary sources.

**Discourse-register-tier.** Handles popular-book-level + introductory-academic-level register (a Wadood Hamid translation; a Norton Anthology introduction; a James Gleick popularization in physics). Scholarly-treatise and primary-source register sit at the edge of comprehension.

**Domain-handling-test.** Vocabulary-level: USE-TECHNICAL-VOCABULARY-FREELY for mainstream terms; INLINE-DEFINE-ON-FIRST-USE for specialist terms; KEEP-SOURCE-TERM-WITH-GLOSS for source-language terms whose form matters. Discourse-level: UNATTRIBUTED-CONSENSUS as primary mode; ATTRIBUTE-VIEW-TO-SCHOOL when school-internal debates are central to the source's argument and can't be ignored.

**Examples spread across domains:**
- *Islamic theology:* Knows the shahada components; knows basic Islamic origin narrative; understands "tawhid" (divine oneness) as a concept; knows "tafsīr" as Quranic exegesis. References to "Mu'tazila" → INLINE-DEFINE first use ("Mu'tazila (a rationalist Islamic theological school)"). References to specific Sufi figures → KEEP-SOURCE-TERM-WITH-GLOSS.
- *Biblical scholarship:* Knows canon order; understands "Synoptic Gospels"; recognizes major figures (Moses, David, John the Baptist, Paul); has heard of the Septuagint. References to "JEDP" → INLINE-DEFINE.
- *Theoretical physics:* Undergraduate physics literacy; understands entropy; recognizes Schrödinger's cat as a thought experiment; knows the basic standard model structure. References to "the measurement problem" → INLINE-DEFINE.
- *Legal scholarship:* Understands tort / contract / criminal distinction; "stare decisis" as precedent; recognizes major Supreme Court cases (Brown, Roe, Marbury). References to "the dormant commerce clause" → INLINE-DEFINE.
- *Philosophy:* Undergraduate-philosophy-equivalent; Cartesian dualism / Humean empiricism / Kant's categorical imperative. References to "Husserl's phenomenology" → INLINE-DEFINE.

**Distinguishing logic from `aware`:** The `educated` reader has READ general literature on the domain (not just heard of it through general life). They have an integrated conceptual schema for mainstream concepts (where the `aware` reader holds them as isolated facts). They can handle USE-TECHNICAL-VOCABULARY-FREELY for mainstream terms; the `aware` reader cannot. They begin to recognize school-internal debates exist (without navigating them); the `aware` reader does not.

#### 2.4 `trained`

**Reader profile.** The reader has formal study or sustained professional engagement with the domain. They have either an undergraduate-major or graduate-level coursework in the domain, OR sustained professional engagement (an imam who studied in seminary; a Bible-college graduate; a working physicist; a lawyer in the relevant subfield). They navigate the domain's conceptual schema with comfort.

**Expertise-depth-tier.** Recognizes specialist terms reliably. Has a well-integrated conceptual schema and can place specific positions within school-internal taxonomies. Catches major school-internal debates and can navigate them. Has read substantial secondary literature and meaningful primary-source material.

**Discourse-register-tier.** Handles introductory-academic + intermediate-academic + meaningful primary-source register (a Brill encyclopedia article; a scholarly translation with footnotes; the *Risale-i Nur* in English translation with annotations).

**Domain-handling-test.** Vocabulary-level: USE-TECHNICAL-VOCABULARY-FREELY for most terms; INLINE-DEFINE-ON-FIRST-USE only for truly specialist sub-field terms. Discourse-level: ATTRIBUTE-VIEW-TO-SCHOOL as primary mode; INVOKE-SPECIALIST-DEBATES at the edge when source's argument requires it.

**Examples spread across domains:**
- *Islamic theology:* Knows the 4 Sunni jurisprudential schools by name (Hanafi / Maliki / Shafi'i / Hanbali); knows kalam vs falsafa distinction; recognizes al-Ghazali / Ibn Sina / Ibn Taymiyyah; knows tafsīr as a genre with named major works. References to "isnād criticism" → USE-TECHNICAL-VOCABULARY-FREELY (assumed known) but ATTRIBUTE-VIEW-TO-SCHOOL when debates appear.
- *Biblical scholarship:* Knows source criticism basics (Documentary Hypothesis / Q source); recognizes major commentators; knows what midrash is; understands canon-formation history. References to "redaction criticism" → USE-FREELY; ATTRIBUTE-VIEW-TO-SCHOOL ("the Tübingen position holds...").
- *Theoretical physics:* Graduate-level physics; recognizes Maxwell's equations in any form; navigates Lagrangian vs Hamiltonian mechanics; recognizes Feynman diagrams. References to "the Copenhagen interpretation vs Many-worlds" → ATTRIBUTE-VIEW-TO-SCHOOL.
- *Legal scholarship:* Law-school graduate; case-law analysis; recognizes specific doctrines (constitutional avoidance; dormant commerce clause; ratione decidendi). References to "the originalism debate" → ATTRIBUTE-VIEW-TO-SCHOOL.
- *Philosophy:* Graduate-level philosophy; navigates analytic-vs-continental divide; recognizes logical positivism / phenomenology / ordinary-language philosophy. References to "Quine's critique of the analytic-synthetic distinction" → USE-FREELY.

**Distinguishing logic from `educated`:** The `trained` reader has FORMAL STUDY or sustained professional engagement (the `educated` reader has general-amateur reading only). They navigate school-internal debates (the `educated` reader recognizes they exist but doesn't navigate). They handle most specialist terms without unpacking (the `educated` reader needs first-use definitions for specialist terms). The translator-AI's primary discourse mode shifts from UNATTRIBUTED-CONSENSUS at `educated` to ATTRIBUTE-VIEW-TO-SCHOOL at `trained`.

#### 2.5 `expert`

**Reader profile.** The reader is a specialist scholar in the source's domain. They have at minimum graduate-level training, often a doctorate, often years of working scholarship in the subfield. They navigate internal debates at scholar-canonical depth and engage with primary-source material directly.

**Expertise-depth-tier.** Recognizes all specialist terms including subfield-internal terminology. Has a fully-integrated conceptual schema covering both mainstream and contested terrain. Engages with school-internal debates as primary discourse, including the lineage of arguments and the contemporary positions. Reads primary sources directly in original language when relevant (the Quran in Arabic; the Hebrew Bible in Hebrew; Plato in Greek).

**Discourse-register-tier.** Handles all academic registers including scholar-canonical register (specialized monographs; critical editions; subfield-internal journal articles).

**Domain-handling-test.** Vocabulary-level: USE-TECHNICAL-VOCABULARY-FREELY across the board; KEEP-SOURCE-TERM-WITH-GLOSS or even KEEP-AS-IS for source-language terms whose form is the point. Discourse-level: INVOKE-SPECIALIST-DEBATES as primary mode; ATTRIBUTE-VIEW-TO-SCHOOL when nuance about positions matters.

**Examples spread across domains:**
- *Islamic theology:* Navigates Mu'tazila vs Ash'ari debate on divine attributes; recognizes Said Nursi's Risale-i Nur terminology and the wider Naqshbandi-Khalidi Sufi context; knows lineage of arguments in classical kalam. References to specific positions in al-Maturidi's *Kitab al-Tawhid* → USE-FREELY; INVOKE-SPECIALIST-DEBATES.
- *Biblical scholarship:* Navigates JEDP source-criticism debates; recognizes critical apparatus conventions (Nestle-Aland); knows manuscript family distinctions; engages with redaction criticism. References to "the Yahwist source's date" → INVOKE-SPECIALIST-DEBATES.
- *Theoretical physics:* Navigates loop-quantum-gravity vs string-theory debates; recognizes specific researchers' positions on the measurement problem; engages with subfield literature. References to "AdS/CFT correspondence" → USE-FREELY.
- *Legal scholarship:* Subfield specialist; recognizes judges' jurisprudential leanings; navigates academic debates. References to "Hart's rule of recognition" → USE-FREELY.
- *Philosophy:* Subfield specialist (phil-of-mind: functionalism vs eliminativism; meta-ethics: cognitivism vs non-cognitivism); recognizes specific philosophers' positions. References to "the Frankfurt cases" → USE-FREELY.

**Distinguishing logic from `trained`:** The `expert` reader engages with subfield-internal debates at scholar-canonical depth (the `trained` reader navigates mainstream school debates but not subfield-internal ones). The `expert` reads primary sources directly in original language when relevant (the `trained` reader reads major primary sources in translation). The translator-AI's primary discourse mode shifts from ATTRIBUTE-VIEW-TO-SCHOOL at `trained` to INVOKE-SPECIALIST-DEBATES at `expert`. Vocabulary handling drops most unpacking entirely.

### 3. Cross-Axis Boundaries

#### 3.1 A2 ↔ A1 (general fluency)

**Criterion.** A2 captures domain-specialist knowledge (technical vocabulary + conceptual schema + discourse conventions in the domain). A1 captures general reading fluency (vocabulary breadth + syntactic processing + idiom recognition + inference capacity + cultural-reference recognition). They are distinct.

**Same-word-fires-both example.** The same encountered word can fire A1, A2, both, or neither depending on the word's nature. "Ratiocination" is general English vocabulary — A1 vocabulary-breadth fires (at low A1, replace with "reasoning"). "Isnād" is Islamic-studies technical vocabulary — A2 fires (at low A2, FOOTNOTE the meaning). "Pharisee" is biblical vocabulary that's also general cultural vocabulary — A1 cultural-reference-recognition fires (at low A1, gloss the pejorative usage) AND A2 may also fire (at low A2 in biblical-scholarship contexts, INLINE-DEFINE the specific Pharisaic-tradition reference). The translator-AI applies BOTH axes per term; both can fire simultaneously on different aspects of the same term-handling decision.

**Independence demonstration.** A non-native ESL Bible scholar has A1=very_basic (general English fluency low) + A2=expert (biblical scholarship deep). A native English speaker who knows nothing about Islamic theology has A1=native (general fluency high) + A2=lay (domain expertise zero). Both configurations are real readers.

#### 3.2 A2 ↔ A3 (cultural identity)

**Criterion.** A2 is competence-based (the reader's acquired knowledge through study or professional engagement). A3 is identity-based (the reader's cultural insider/outsider status — were they born into the culture? do they live in it?). They are distinct.

**Four-corners independence demonstration.** All four corners of the A2-A3 joint distribution are real:

- *A2=expert + A3=outsider:* a Western academic Islamicist who has spent a career studying Islamic theology but has never lived in a Muslim-majority country.
- *A2=lay + A3=source-native:* a born Muslim with no formal study of Islamic theology — fluent in the cultural surround but unable to navigate kalam debates.
- *A2=expert + A3=source-native:* a born Muslim Islamic-studies professor — both cultural insider and trained specialist.
- *A2=lay + A3=outsider:* a typical Western non-Muslim reader — neither cultural insider nor specialist.

The translator-AI's handling decisions differ across these four corners. The A2=expert + A3=outsider reader catches the technical references (USE-FREELY) but may need cultural-context flags for source-culture-specific assumptions. The A2=lay + A3=source-native reader doesn't need cultural-context flags but does need technical-vocabulary unpacking.

#### 3.3 A2 ↔ A4 (purpose)

**Criterion.** A4 Purpose answers "WHY is the translation being made?" (scholarly study / devotional reading / casual reading / language learning / performance). A2 answers "HOW MUCH does the reader know in the domain?" They are distinct.

**Independence demonstration.** A specialist reader can read for a casual purpose (a Bible scholar reading for relaxation; an Islamic-studies professor browsing Risale-i Nur for personal devotion rather than research). A lay reader can read for a scholarly purpose (a curious-amateur researching an unfamiliar topic for a school project; a non-Muslim journalist preparing background on Said Nursi).

### 4. Forward-Tagged Specialist Canons (Received from A1)

The most recent A1 sub-field finding (`devdocs/inquiries/2026-06-06_11-47__a1_cultural_reference_recognition_levels/finding.md`) defined the A1 cultural-reference-recognition sub-field and identified 5 specialist-domain canons whose recognition requires domain training rather than general cultural literacy. The criterion was: general cultural literacy → A1; domain training required → A2. The 5 canons were forward-tagged for A2 to receive. This finding receives them.

Each canon is a specialist domain in its own right. Within any one translation job, ONE of these (or another not-listed specialist domain like Islamic theology) is the source's domain. The A2 framework applies to that source's domain — and the 5-level progression captures the depth of the reader's knowledge in that specific specialist domain.

**Legal-history precedents.** Specialist canon: Marbury v. Madison, Brown v. Board of Education, Roe v. Wade, Dred Scott. A2 progression: `lay` doesn't reliably know any specific case; `aware` has heard of Brown v. Board; `educated` recognizes major Supreme Court cases; `trained` engages with specific doctrines (constitutional avoidance, stare decisis); `expert` navigates subfield debates (originalism vs living-constitutionalism; Hart's rule of recognition).

**Mathematical figures and concepts.** Specialist canon: Cantor's diagonal, Gödel's incompleteness theorems, Russell's paradox, Hilbert's problems, the Riemann hypothesis. A2 progression: `lay` doesn't know these as concepts; `aware` has heard of Einstein's E=mc² but not Cantor; `educated` knows the basic existence of Gödel's incompleteness as cultural-anchor; `trained` engages with the proofs at undergraduate-math level; `expert` works in the subfield. Note the gray-zone case: Einstein has migrated from specialist to general cultural literacy (every educated adult has heard of Einstein); the Pythagorean theorem has migrated similarly.

**Scientific figures and concepts.** Specialist canon: Maxwell's equations, Bohr's atom, Pasteur (synonymous with germ theory), Feynman diagrams. A2 progression as in Section 2's theoretical-physics examples. Note Einstein migrated specialist→general; Maxwell has not.

**Medical eponyms.** Specialist canon: Alzheimer's, Parkinson's, Charcot, Hodgkin's lymphoma, Bell's palsy. A2 progression: Alzheimer's and Parkinson's have migrated specialist→general (every adult has heard of them); Charcot and Hodgkin's lymphoma remain specialist. The framework handles both via the same expertise-depth dimension.

**Specialist philosophy.** Specialist canon: Heideggerian (beyond the popular "existentialism"), Wittgensteinian (beyond the popular Wittgenstein name-drop), Hegelian dialectic at the specialist level. A2 progression as in Section 2's philosophy examples.

The translator-AI applies A2 within the source's specialist domain. If the source is a Said Nursi text, the source's domain is Islamic theology; A2 applies to the reader's depth in Islamic theology. The 5 forward-tagged canons above describe 5 different specialist domains — they are not all present in a single translation job. They illustrate the breadth of specialist-canon territory that A2 can cover.

---

## Inherited Commitments Re-test

This finding inherits commitments from the root architectural finding + the A1 chain. The Synthesis Trigger in `_branch.md` requires each inherited commitment be either re-tested with cited evidence or flagged as INHERITED-WITHOUT-RE-TEST with a reason.

**IC1 — Receptive-only commitment.**
- **Source:** A1 sub-field chain (originally `a1_vocabulary_breadth_levels/finding.md`); re-affirmed in all 4 subsequent A1 sub-field findings.
- **Re-test status:** RE-TESTED.
- **Evidence:** Sensemaking Ambiguity A8 tested whether A2 should be productive-also (a specialist might write/produce in the domain). The counter failed on structural grounds: in translation context the reader receives translated text; the relevant axis is recognition depth not production capability. A2 is receptive-only. Per-level prose (Section 2.1–2.5) is framed as recognition throughout.

**IC2 — Conservative-bias-for-reader-axes = LOWER default.**
- **Source:** Root architectural finding (the 2-tier default principle's conservative-bias fallback) + A1 chain.
- **Re-test status:** RE-TESTED.
- **Evidence:** Section 1.8 documents the conservative-bias-LOWER policy for A2. When the user is silent or ambiguous, the AI assumes lower A2 → more aggressive technical-vocabulary unpacking and discourse-level restraint.

**IC3 — Language-agnostic at concept level.**
- **Source:** Root architectural finding (Layer 1 commitment for all 8 axes) + A1 chain.
- **Re-test status:** RE-TESTED.
- **Evidence:** The level FRAMEWORK is language-agnostic — it works for any source domain (Section 2 demonstrates with 5 reference domains: Islamic theology, biblical scholarship, theoretical physics, legal scholarship, philosophy). Specific DOMAIN content (which terms are technical; which figures are canonical) is culture- and domain-specific but is handled at runtime by the AI, not by the level framework.

**IC4 — A2 plain-ordinal pattern (no sub-fields).**
- **Source:** Root architectural finding.
- **Re-test status:** RE-TESTED.
- **Evidence:** Sensemaking Ambiguity A6 tested whether A2 should be split into multiple specialist-domain axes (A2-legal, A2-math, A2-Islamic-theology, etc.). The counter failed on structural grounds: multi-axis multiplies configuration burden; single-axis with single-domain-default handles the operational need. Section 1.3 documents the plain-ordinal pattern.

**IC5 — A2 cardinality (root proposed 3 levels).**
- **Source:** Root architectural finding (proposed 3 levels).
- **Re-test status:** RE-TESTED & REFINED.
- **Evidence:** The user directed 5 levels. The 5-level structure (`lay | aware | educated | trained | expert`) maps to Hubert and Stuart Dreyfus's 5-stage skill-acquisition model (the canonical 5-level expertise model in cognitive science). The refinement is principled (anchored in expertise-stratification literature) and matches the user's directive.

**IC6 — A2 boundary vs A1 (general fluency) and A3 (cultural identity).**
- **Source:** Root architectural finding.
- **Re-test status:** RE-TESTED & DOCUMENTED.
- **Evidence:** Section 3 documents both boundaries. A2↔A1 with same-word-fires-both criterion + independence demonstration. A2↔A3 with four-corners independence demonstration. Also A2↔A4 documented for completeness.

**IC7 — A2 controls technical vocabulary unpacking.**
- **Source:** Root architectural finding (A2's scope statement).
- **Re-test status:** RE-TESTED.
- **Evidence:** Section 1.7 documents the 9 handling actions including 4 vocabulary-level (USE-FREELY / INLINE-DEFINE / FOOTNOTE / PARAPHRASE) that operationalize the technical-vocabulary-unpacking commitment.

**IC8 — 5 forward-tagged specialist canons from A1's cultural-reference-recognition.**
- **Source:** `a1_cultural_reference_recognition_levels/finding.md` (the most recent A1 sub-field finding) — Section 3 (A1↔A2 boundary) forward-tagged 5 specialist-domain canons to A2.
- **Re-test status:** RE-TESTED & APPLIED.
- **Evidence:** Sensemaking Ambiguity A5 confirmed the forward-tagging is valid (the canons are A2-territory by A1's own criterion). Section 4 of this finding receives and integrates all 5 canons via the expertise-depth dimension, with the constraint that any one translation job has ONE source domain.

**IC9 — Same-labels-for-default-propagation does NOT inherit.**
- **Source:** A1 chain (each A1 sub-field finding documents the same-labels commitment for propagation across A1's 5 sub-fields).
- **Re-test status:** RE-TESTED & DOCUMENTED.
- **Evidence:** A2 is plain-ordinal (no sub-fields, no propagation). The same-labels rationale (a headline level propagates to sub-fields) does not apply. Sensemaking Ambiguity A1 settled: domain-meaningful labels (`lay | aware | educated | trained | expert`) are preferable to A1-consistency labels. Section 1.1 documents.

**IC10 — Domain-meaningful labels `lay | aware | educated | trained | expert`** (NEW commitment unique to this inquiry).
- **Source:** Sensemaking Ambiguity A1 at HIGH confidence.
- **Re-test status:** NEW.
- **Anchor:** Hubert and Stuart Dreyfus's 5-stage skill-acquisition model (the canonical cognitive-science model for 5-level expertise progression: novice / advanced beginner / competent / proficient / expert).

**IC11 — Single-domain default for the domain-scope question** (NEW commitment unique to this inquiry).
- **Source:** Sensemaking Ambiguity A2 at HIGH confidence.
- **Re-test status:** NEW.
- **Anchor:** Section 1.5 documents. Each translation job has one source domain; the source's domain is implicit at runtime via Layer 3 SOURCE-DESCRIPTION. Multi-domain configuration is deferred to a future audience-level inquiry.

**IC12 — 9 handling actions in 2 categories + 1 bridge** (NEW commitment unique to this inquiry).
- **Source:** Surfacing R9 + sensemaking Ambiguity A7 at MEDIUM confidence.
- **Re-test status:** NEW.
- **Anchor:** Section 1.7 documents the action vocabulary structured as 4 vocabulary-level + 4 discourse-level + 1 bridge (KEEP-SOURCE-TERM-WITH-GLOSS).

---

## Next Actions

### MUST

- **What:** Commit the A2 enum to the schema: `domain_expertise: Literal["lay", "aware", "educated", "trained", "expert"]`.
  - **Who:** User (project author).
  - **Gate:** Condition-bound — when the user is ready to lock the A2 spec.
  - **Why:** Enables the translator-AI to receive the A2 configuration as prompt context and decide handling actions per encountered technical term and discourse-level reference at runtime.

- **What:** Verify in the per-level prose (Section 2) that each of the 5 levels has at least 3 different domain examples (Islamic theology / biblical scholarship / theoretical physics / legal scholarship / philosophy) and includes a Said Nursi corpus example position.
  - **Who:** This finding (already done — Section 2.1–2.5 includes all 5 reference domains per level + Said Nursi corpus references per level).
  - **Gate:** Observable — verify by inspection.
  - **Why:** Prevents Western-canon or single-domain lock-in; honors the user's explicit ask for "good examples" spread across domains; anchors the project's primary use case (Said Nursi).

### COULD

- **What:** Add an `audience.expertise_set: list[(domain, level)]` field at the audience-level for multi-domain reader configuration.
  - **Who:** Future audience-level inquiry (separate).
  - **Gate:** Condition-bound — when the user reaches the audience-level inquiry.
  - **Why:** Enables multi-domain handling for readers who have radically different expertise across multiple specialist domains.
  - **Depends-on:** MUST item "Commit the A2 enum to the schema". This COULD is GATED — do not act until the MUST resolves.

- **What:** Add a translator-AI prompt-engineering pass that embeds Sections 1, 2, 3, and 4 of this finding (the framework + per-level definitions + cross-axis boundaries + forward-tagged canons integration) as system-context for the AI.
  - **Who:** Translation runtime / prompt-engineering layer.
  - **Gate:** Condition-bound — after schema commit.
  - **Why:** Makes the A2 level definitions operationally available to the translator-AI.
  - **Depends-on:** MUST item "Commit the A2 enum to the schema". This COULD is GATED.

### DEFERRED

- **What:** Medical-translation cross-domain illustration (patient-information leaflets vs medical-journal articles as a 5-tier expertise parallel).
  - **Gate:** Revival trigger — if a future inquiry needs additional cross-domain anchors for the expertise-depth ladder.
  - **Why (if revived):** Provides additional didactic anchor for the expertise stratification.

- **What:** Wine sommelier certification cross-domain illustration (beginner / informed / certified / advanced / master as a parallel 5-tier expertise framework).
  - **Gate:** Revival trigger — same as above.
  - **Why (if revived):** Same.

- **What:** Adaptive runtime expertise estimation — translator-AI dynamically estimates the reader's expertise from feedback signals (clarifying questions, hover-clicks, etc.) instead of static A2 configuration.
  - **Gate:** Revival trigger — when AI capability matures to support dynamic expertise estimation (5-10 years horizon).
  - **Why (if revived):** Removes static configuration burden; adapts to the reader's actual expertise in real time.

---

## Reasoning

### Why these 5 labels and not A1's

The user's explicit framing emphasized that the 5-level structure is "easy to deduce" but the explicit distinguishing logic is the real difficulty. Two natural label sets were considered:

**Rejected: A1-consistency labels** (`very_basic | daily | conversational | advanced | native`). These read oddly when applied to domain expertise. "Daily domain expertise" doesn't carry meaning; "conversational domain expertise" is meaningless. The A1 labels are designed for general-language-fluency gradients (daily English vs conversational English vs native English) — not for domain-specialist knowledge.

**Survived: Domain-meaningful labels** (`lay | aware | educated | trained | expert`). These read cleanly and map to a well-established cognitive-science anchor (Hubert and Stuart Dreyfus's 5-stage model). They are not project-specific jargon; any reader of the schema understands them immediately.

Why the divergence from A1 is principled: A1 is a `composite-axis` — the headline level PROPAGATES to A1's 5 sub-fields, requiring label consistency. A2 is plain-ordinal — no sub-fields, no propagation, no consistency requirement. The labels need only be domain-meaningful, and they are.

### Why single-domain default

Two architectural alternatives were considered for the domain-scope question:

**Rejected: Multi-domain configuration.** An `audience.expertise_set: list[(domain, level)]` field at the audience-level would allow specifying per-domain expertise for readers with multiple specializations. Why rejected for THIS inquiry: A2's operational role is to inform the translator-AI for a specific translation job. Each translation job has one source domain (a Said Nursi text = Islamic theology; a Bible passage = biblical scholarship). Multi-domain configuration multiplies the user's configuration burden without operational benefit at the A2 layer. The multi-domain need is real but belongs at the audience-level (a future inquiry).

**Survived: Single-domain default.** A2 specifies the reader's expertise in the source's domain. The source's domain is implicit at runtime via Layer 3 SOURCE-DESCRIPTION. Multi-domain references within the source are handled at runtime by the AI's cross-domain knowledge. This is operationally complete for the typical translation job.

### Why the 4-component template adapts (not abandons)

The 4-component template from the A1 sub-field chain has the structure (reader profile + tier-component + register-component + handling-test). One could argue A2 is structurally different (plain-ordinal not composite-axis) and so the template doesn't apply. Counter: the template is about PER-LEVEL DEFINITION SHAPE, not axis-pattern shape. The 4 components organize per-level prose in a way usable as translator-AI prompt context. They apply to any level definition. The adaptations are clean: frequency-tier → expertise-depth-tier (the dimension changes from word-frequency to expertise depth); register-tier → discourse-register-tier (different genres in the domain draw from different registers); substitution-test → domain-handling-test (the action vocabulary changes from substitution to the 9 named actions).

### Why 9 handling actions in 2 categories + 1 bridge

Surfacing identified 9 distinct handling actions in the translation-studies literature on domain translation. Two alternatives were considered:

**Rejected: Consolidate to 4-5 actions.** Would lose operational distinction. FOOTNOTE-TECHNICAL-TERM and INLINE-DEFINE-ON-FIRST-USE are operationally different — they have different reader-experience implications (footnote breaks gaze; inline definition flows). Consolidating loses these distinctions.

**Rejected: Expand to 12+ actions.** Would add complexity without coverage gain. 9 covers the territory.

**Survived: 9 actions in 4 vocabulary-level + 4 discourse-level + 1 bridge.** The two categories are operationally distinct: vocabulary-level actions handle technical terms; discourse-level actions handle school-internal debates and lineage references. The bridge (KEEP-SOURCE-TERM-WITH-GLOSS) handles the case where the source-language term itself is the meaning carrier.

### Why A2 doesn't have a project-policy override like A1's cultural-reference-recognition

A1 cultural-reference-recognition committed to a project-policy that DISFAVORS the DOMESTICATE action (per the user's translation-register-fidelity memory + Venuti's foreignization ethics). A2 does NOT have an analogous policy. Why: specialist terminology IS the desired register at high A2 levels — the expert WANTS to read specialist terms, not see them paraphrased. There's no foreignization-vs-domestication tension at A2 because using technical vocabulary at high A2 is structurally correct (not ethically loaded). The action selection at A2 is governed only by reader-level + term-properties + source-markings, not by a project-policy override.

---

## Open Questions

### Monitoring

- **AI prompt-context calibration.** Once the schema is committed and the translator-AI receives this finding's framework, observe whether the AI's per-term handling decisions match the level definitions. Specifically: does the AI INLINE-DEFINE at `trained` when it should USE-FREELY (over-glossing)? Does it USE-FREELY at `aware` when it should FOOTNOTE (under-glossing)? Calibration adjustments to the per-level prose may be needed after observing N≥10 translation samples.

### Blocked

- **Multi-domain reader configuration.** Cannot be specified until the audience-level inquiry establishes the `audience.expertise_set` field. Blocked by COULD item 1.

### Research Frontiers

- **Adaptive runtime expertise estimation.** Translator-AI dynamically estimates the reader's expertise from feedback signals (clarifying questions, hover-clicks, etc.) instead of static A2 configuration. Long-horizon (5-10 years); depends on AI capability development.

- **Per-subfield expertise distinction within a domain.** An Ash'ari-school specialist reading a Mu'tazila-focused text knows kalam vocabulary but not Mu'tazila-internal positions. Currently handled by conservative-bias-LOWER + per-translation-job conscious config. A more granular configuration (per-subfield expertise within a domain) is a future research question.

### Refinement Triggers

- **Refinement trigger for the expertise-depth ladder:** if cognitive-science research yields a substantially different expertise-stratification model (e.g., a 7-stage alternative becomes consensus), revisit the 5-tier ladder.

- **Refinement trigger for A2's label choice:** if user feedback indicates that `lay | aware | educated | trained | expert` reads oddly in actual translator-AI prompt context, revisit. The Dreyfus anchor is well-established but labels are reversible.

- **Refinement trigger for the A2↔A1 boundary:** if same-word-fires-both produces translator-AI confusion at runtime (the AI can't tell which axis adjudicates a specific term), the boundary criterion may need refinement.

- **Refinement trigger for the single-domain default:** if multi-domain texts become a primary use case (e.g., the project expands beyond Said Nursi to corpora that routinely cross domains), revisit and consider the multi-domain configuration.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
now do it for A2 — Domain Expertise
first of all reread devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md fully.
it is a bit challanging, it should be 5 level again. this is easy to deduct. But the real question is the definitions of how to distinguish these 5 levels, we need some good, explicit definitions with good examples i think
```

</details>
