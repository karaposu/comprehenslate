# Innovation — user_research_persona_validation

## User Input

[abbreviated — see _branch.md + sensemaking.md SV6 + decomposition.md for full context]

Production-task: generate content for 8 pieces (P1 Methodology / P2 Plan / P3 Personas / P4 Matrix / P5 Verdicts / P6 Recommendations / P7 Re-test / P8 Open Questions). Meta-decision pieces: P1, P5, P7. CRITICAL: substrate-anchoring is mandatory; synthesis disclaimer on every output.

---

## Seed + Methodology-Mode Consideration

### Inherited mode
**Standard default** (4G+3F balanced; elaborate SV6 model). Substrate-anchoring + bias-balance discipline are the central constraints.

### Alternative mode
**Contrarian-rethink** — would treat the SV6 hybrid as a candidate to invalidate (e.g., commit to pure simulation or pure plan).

### Decision
**Default — Standard default.** Sensemaking already adjudicated the hybrid via 6 ambiguity collapses at HIGH confidence; reopening it would discard validated work.

---

## Meta-Decision-Piece Classification

| Piece | Properties firing | Classification |
|---|---|---|
| P1 — Methodology & Disclaimers | (b) framing-semantic + (c) lesson-vocabulary (substrate-anchoring rule; bias-balance; synthesis disclaimer; anti-pattern guards) | **META-DECISION** |
| P2 — Research Plan | content-production within P1 frame | content-production |
| P3 — 5 Persona Profiles | content-production within P1 frame (substrate-anchored generation) | content-production |
| P4 — 50-cell Matrix | content-production within P1+P3 frame | content-production |
| P5 — 6 Re-test Verdicts | (a) relationship-label commitment (CONFIRMED/REFINED/QUESTIONED propagates to prior Mac-app finding) | **META-DECISION** |
| P6 — Design Recommendations | content-production within P5 frame | content-production |
| P7 — Inherited Re-test admin | (a) relationship-label commitment (Inherited propagation per CONCLUDE) | **META-DECISION** |
| P8 — Open Questions | content-production residuals | content-production |

P1, P5, P7 require piece-level Inversion-candidates.

---

## P1 — Methodology & Disclaimers

### Principal Candidate (PC1)

#### Synthesis Disclaimer (verbatim template — apply to every synthetic output)

> ⚠ **Synthesis Notice.** This output is AI-generated from project substrate (`SKILL/references/core/translation_principals.md`, `advanced_principles.md`, `notes.md`, `harmony_layer.md`; the `comprehenslate_mac_app_design/finding.md`; the schemas + calibration docs). It is a **best-effort first-pass** representing what a real theological translator in this archetype *might* think or need. It is **NOT empirical user research**. Treat as a design-validation preview only. Validate with real translator interviews (per Research Plan, §2) before treating any conclusion as definitive design action.

#### Substrate-anchoring rule

Every persona pain-point + every walkthrough cell + every verdict must cite ≥1 substrate source:
- `references/core/translation_principals.md` (principles)
- `references/core/advanced_principles.md` (escalation chains; deeper principles)
- `references/core/harmony_layer.md` (Tier 1-4 patterns)
- `references/core/notes.md` (Nursi-specific observations)
- `comprehenslate_mac_app_design/finding.md` (the design under validation)
- `policy_config_base_source.md` / `config_base_source.md` (TC + Policy semantics)

If a pain-point or reaction cannot be tied to substrate, **flag it explicitly** as *"extrapolated beyond substrate; lower confidence."* This is the **anti-hallucination rule**.

#### Bias-balance discipline

- Each persona must have **both supporting AND critical** reactions across the 10 decisions.
- No persona uniformly approves or uniformly critiques.
- Each per-decision aggregate must include voices on multiple sides where reasonable.

#### Anti-pattern guards (the 5 risks from Sensemaking)

| # | Risk | Guard |
|---|---|---|
| 1 | Confirmation bias | Bias-balance discipline + dedicated anti-confirmation persona (P5 academic critic) |
| 2 | Over-claim from synthesis | Synthesis Disclaimer on every output |
| 3 | Pain-point invention | Substrate-anchoring rule |
| 4 | Persona homogeneity | Variant-spread (5 personas across distinct territory facets) |
| 5 | Solution bias ("would you use X?") | Problem-framed walkthrough cells ("what need does this address for this persona?") |

**Mechanism trace:** Combination (4 rules + 5 guards into a methodology) + Absence Recognition (the explicit synthesis-can't-replace-real-interviews stance is unusual in tool-design contexts) + Inversion (PI1 below) + Constraint Manipulation (ADD substrate-anchoring + bias-balance as design-time constraints on synthesis).

### Piece-level Inversion Candidate (PI1)

**Assumption:** "synthesis-with-disclaimer + substrate-anchoring + bias-balance is the right methodology."

**Alternative:** "Don't disclaim — present synthesis as if empirical to maximize design-action confidence; lean into the persuasion."

**5-test on PI1:**
- Novelty: low (treats synthesis as data)
- Scrutiny survival: **WEAK** — violates honesty (FP1); risks user using syntheses as real research findings
- Verdict: **REJECTED.**

**PC1 5-test:** Novelty HIGH (rigorous synthesis methodology not standard); Scrutiny STRONG; Fertility HIGH (enables all downstream pieces); Actionability HIGH; Mechanism independence (Combination + Absence Recognition + Constraint Manipulation + Inversion-as-rejection). **ACTIONABLE.**

---

## P2 — Research Plan

### Principal Candidate (PC2)

#### Interview script (semi-structured; ~60-90 min per session)

| Block | Time | Questions |
|---|---|---|
| **1. Background** | 5 min | Tell me about your translation work. Which corpora? Target languages? How often / how long sessions? |
| **2. Current tools** | 10 min | What do you use today? Walk me through a typical session. What works well? What's missing? |
| **3. Pain points** | 10 min | What's the most frustrating part of your current process? Show me a specific example. |
| **4. Magic-wand question** | 5 min | If you could change one thing about your current process, what? |
| **5. Mac-app design probe** | 15 min | Show the 5-layer architecture + key UI surfaces (TC editor; Policy editor; live reading; harmony viz; lineage view; multi-translation collation). Observe + record reactions. |
| **6. Feature priority** | 10 min | Rank these 10 features by importance. Which would you use weekly? Which never? |
| **7. Differentiator validation** | 10 min | Specifically: would harmony viz / lineage / multi-translation collation help your work? When? Walk me through a use case. |
| **8. Pricing / monetization** | 5 min | What would you pay? Subscription / one-time / free / open-source preferences? Team-license interest? |
| **9. Edge cases** | 5 min | Have you encountered [specific theological-text phenomenon: voice-marking; archaic register; embedded language; idiom mismatch; cultural reference]? How did you handle it? |
| **10. Reprise magic-wand** | 5 min | Given what you've seen, change one thing about the Mac-app design? |

#### Recruitment criteria

Per-persona-type screening (interviewer asks these; recruits the participant if criteria match):

| Persona | Screening criteria |
|---|---|
| **P1 Nur Talebesi-tradition** | Currently translating Risale-i Nur (or similar Nursi-corpus)? ≥1 year? Familiar with Vahide / Akarsu? |
| **P2 Quran-translation editor** | Currently editing or producing a Quran translation? Familiar with Yusuf Ali / Sahih / Asad / Pickthall / Khalidi traditions? |
| **P3 Mevlana / Rumi translator** | Currently translating Persian Sufi poetry (Mevlana / Hafez / Saadi / Attar)? |
| **P4 Talmud / rabbinic translator** | Currently translating Talmudic or rabbinic-commentary texts? Hebrew-Aramaic source? |
| **P5 Academic translation-studies scholar** | PhD or PhD-track in translation studies / comparative religion / Islamic studies? Familiar with CAT tools or theological-translation literature? |

Plus general criteria: actively working translator (not just researcher); willing 60-90 min interview; consent for recording + anonymized quotes.

#### Sample size guidance

~5 participants per persona-type (qualitative-research saturation point); total ~20-25 participants. Stop earlier if successive interviews produce no new insights.

#### Recruitment channels

- Academic networks (translation-studies departments; Islamic-studies programs; Hebrew Union College; Bar-Ilan; Najran University)
- Translator associations (ATA — American Translators Association; AAR — American Academy of Religion; FIT — International Federation of Translators)
- Theological publisher contacts (Risale-i Nur Tahsiye Vakfı; Fons Vitae; Continuum; Oxford USA; Brill)
- LinkedIn searches with screening
- Specialized forums (Sefaria community; Quranist forums; Risale-i Nur reader networks)

#### Compensation guidance

- Academic respondents: $50-100 honorarium
- Professional translators: pay equivalent to 1-hour consulting rate (likely $100-300)
- Gift card / Amazon credit as alternative

#### Ethics / IRB

- Academic research → follow institutional IRB consent forms
- Non-academic → basic consent template (recorded with consent; anonymized quotes; right to withdraw at any time)

#### Analysis framework

1. **Transcribe** (Otter.ai or equivalent; manual cleanup for accuracy)
2. **Affinity mapping** — cluster insights from quotes across all interviews
3. **Persona-pattern extraction** — synthesize real personas from clusters; compare against synthetic personas in §3
4. **Jobs-to-be-done analysis** — extract core jobs translators "hire" the tool for
5. **Pain-point ranking** — frequency × severity across interviews
6. **Feature-priority synthesis** — quantifiable feature ranking
7. **Design-impact mapping** — translate insights into specific Mac-app design changes (keep / refine / drop)

#### Expected deliverables from real-research execution

- Anonymized interview transcripts
- Real persona profiles (compare to synthetic in §3)
- Pain-point ranking with frequency + severity
- Feature-priority synthesis
- Design-impact memo updating the Mac-app finding's verdicts

**Mechanism trace:** Combination (10 question blocks + 5 recruitment criteria + analysis framework) + Domain Transfer (qualitative-research convention from UX research + academic social science).

**5-test PC2:** ACTIONABLE.

---

## P3 — Five Synthetic Persona Profiles

### Principal Candidate (PC3)

> ⚠ **Synthesis Notice applies to every persona below.** See §P1 for full disclaimer.

---

### Persona P1 — Mehmet Sözcü — Nur Talebesi-tradition scholar

- **Role:** Independent translator + adjunct lecturer at İlahiyat Fakültesi
- **Demographics:** Mid-40s; based in Istanbul; PhD in Islamic Studies focused on Said Nursi's metaphysics
- **Experience:** 12 years translating Risale-i Nur volumes into English; 5 published volumes via Risale-i Nur Tahsiye Vakfı
- **Workflow:** Reads source mesele-by-mesele; cross-references with Vahide + Akarsu translations; takes paper notes on theological terminology decisions; uses MS Word + Google Drive
- **Goals:** Produce translations faithful to Nursi's harmony layer (nazm preservation); maintain Vahide-Akarsu terminology consistency where they're correct; depart explicitly where they're not; make accessible to English-speaking Nur Talebesi reader
- **Pain Points (substrate-anchored):**
  1. *Terminology consistency across volumes is hard with Word alone* — `translation_principals.md` (rhetoric carries meaning; need consistent rendering)
  2. *Vahide-Akarsu reference cross-checking is manual; can't see all three side-by-side easily* — supports multi-translation collation (Mac-app §3 D4)
  3. *Hashiye handling is tedious; current tools don't separate them from main text* — supports `SourceApparatusPolicy`
  4. *Belagat (rhetorical-structure) decisions are intuitive but lineage/audit is lost between drafts* — supports per-chunk lineage view (Mac-app §3 D5)
- **Current Tools:** MS Word; Google Drive; printed Vahide + Akarsu volumes; Concordance app
- **Representative Quote:** *"My biggest worry is that I'm rendering one of Nursi's key terms — say, hakikat-i mutlaka — differently from Vahide without realizing it. I want to see three columns side-by-side before I commit a translation choice."*
- **Substrate Anchor:** `translation_principals.md` (rhetoric; ihlas); `notes.md` (Nursi's micro-to-macro mirroring); Mac-app finding §3 (multi-translation collation; lineage view)

---

### Persona P2 — Dr. Salma Karim — Quran-translation editor

- **Role:** Senior Editor at a small academic-imprint publishing Quran translations
- **Demographics:** Late 30s; UK-based; PhD in Arabic + Islamic Studies (Edinburgh)
- **Experience:** 8 years as editor; oversaw 3 new translations + 2 revisions; deeply familiar with Yusuf Ali / Sahih / Asad / Pickthall / Khalidi / Saheeh International
- **Workflow:** Works in parallel with a primary translator (typically a senior scholar); editor's job is consistency-checking + variant-tradition citation + apparatus; uses custom Word template + concordance database
- **Goals:** Ensure every key ayah aligns with or explicitly departs from established translations; maintain "infamous translation" availability for famous citations; edit for consistency across 6000+ ayah translation
- **Pain Points (substrate-anchored):**
  1. *Variant-comparison workflow fragmented across 5 print volumes + spreadsheet* — directly supports multi-translation collation (Mac-app §3 D4); validates `PriorTranslationStancePolicy`
  2. *Establishing whether a chosen rendering "follows" or "departs from" tradition is judgment-heavy and undocumented* — supports per-chunk lineage view (D5)
  3. *Quranic citations within secondary literature need consistent rendering; current workflow allows mixed sources without audit trail* — supports `NonMainLangPartsPolicy "replace-original-with-infamous-translation"`
  4. *BYO API key model assumes editor sets up + manages OpenAI billing — small academic teams might prefer managed service* — POTENTIAL CRITIQUE of D2
- **Current Tools:** MS Word; custom variant-comparison spreadsheet; Quran.com; offline 5 print volumes
- **Representative Quote:** *"For famous ayat, I want to honor the established translations — Yusuf Ali, Sahih, sometimes Asad — but I need to see the choice explicitly and audit it. Right now if my translator picks one, I trust their judgment but I can't verify it later."*
- **Substrate Anchor:** `policy_config_base_source.md` (NonMainLangPartsPolicy `replace-original-with-infamous-translation` value; PriorTranslationStancePolicy); Mac-app finding §3 (multi-translation collation; per-chunk lineage); Mac-app finding §5 (BYO API key — potential mismatch)

---

### Persona P3 — Aliyah Tanaka — Mevlana / Rumi translator

- **Role:** Independent literary translator + part-time Persian instructor
- **Demographics:** Mid-30s; based in San Francisco; MFA in Literary Translation (Iowa); Persian + Turkish reading fluency
- **Experience:** 6 years translating Persian Sufi poetry (Mevlana, Hafez, Attar); 1 published book + 8 journal pieces
- **Workflow:** Translates couplets in batches; reads aloud frequently to test meter; keeps private glossary of personal renderings; resists Coleman Barks-style "free renderings" but respects the poetic-register tradeoff
- **Goals:** Render Persian couplets in English verse OR prose-with-meter-notes per edition target; preserve nazm where possible (`advanced_principles.md`); maintain rendering consistency across a book's worth of couplets
- **Pain Points (substrate-anchored):**
  1. *Verse vs prose decision is judgment-heavy; current tools don't help frame the choice* — supports `EmbeddedPoetryPolicy` (verse / prose / facing-original-with-meter-notes options)
  2. *Reading aloud is essential but offline; tool can't help with meter analysis* — supports reading-aloud TTS (Mac-app v2)
  3. *Persian source-language fluency varies by reader; single-config doesn't fit both audiences* — supports two-level provider config + per-project TC
  4. *Coleman Barks-style renderings popular but lose meaning; I want to defend my faithful renderings explicitly* — supports per-chunk lineage view (D5)
  5. *Bismillah and other formulaic invocations need consistent handling across volumes* — supports `FormulaicOpeningPolicy`
- **Current Tools:** Word; Persian-English dictionaries; recorded readings; offline private glossary
- **Representative Quote:** *"When I translate a Rumi couplet, I'm making twenty decisions in five seconds — meter, register, phonetic echo, target convention, Barks-tradition reference. Right now those decisions vanish; I can't audit them or be consistent over 200 couplets."*
- **Substrate Anchor:** `policy_config_base_source.md` (EmbeddedPoetryPolicy; FormulaicOpeningPolicy); `harmony_layer.md` (Tier 1-2 nazm preservation); Mac-app finding §3 (per-chunk lineage view)

---

### Persona P4 — Avraham Goldfeld — Talmud translator

- **Role:** Senior scholar at a yeshiva + Talmud translation project
- **Demographics:** Late 50s; based in Jerusalem; trained in classical rabbinic tradition + Hebrew University; multi-decade career
- **Experience:** 25+ years translating Talmudic tractates into English; published 4 tractates with apparatus
- **Workflow:** Works one daf (folio) at a time; manages text + Rashi + Tosafot + later commentaries simultaneously; produces translation + multi-column apparatus
- **Goals:** Render Talmudic text faithful to Hebrew-Aramaic source; preserve marginal commentary structure (Rashi inner column; Tosafot outer column); make accessible to English-reading yeshiva students
- **Pain Points (substrate-anchored):**
  1. *Multi-channel apparatus rendering is extremely manual; current tools don't preserve source-channel structure* — supports `SourceApparatusPolicy.preserve-as-source-channel`
  2. *Multiple commentary voices (Rashi, Tosafot, Ramban, Maharsha) need consistent voice-marking* — supports `VoiceMarkingPolicy`
  3. *Aramaic + Hebrew embedded in single text needs different handling per context* — supports `NonMainLangPartsPolicy` cross-tradition
  4. *Honorifics (z"l, zt"l, etc.) need consistent rendering* — supports `HonorificsPolicy` (cross-tradition validation)
  5. *Mac-only is a constraint — Talmud-scholar workflow often involves Windows or Linux server access* — POTENTIAL CRITIQUE of Mac-platform commitment
- **Current Tools:** Bar-Ilan Responsa database; Sefaria; MS Word; custom multi-column LaTeX template for print
- **Representative Quote:** *"Talmud isn't a single voice — it's a meeting of Rashi, Tosafot, the Gemara itself, sometimes Ramban or Ran. If your tool can preserve the original page structure, that's already a step beyond Word. If it can handle voice attribution automatically, that's transformative."*
- **Substrate Anchor:** `policy_config_base_source.md` (SourceApparatusPolicy + VoiceMarkingPolicy + HonorificsPolicy + NonMainLangPartsPolicy); Mac-app finding §3 (Quality layer); Mac-app finding §1 (Mac platform — potential mismatch)

---

### Persona P5 — Prof. Elena Ricci — Academic translation-studies scholar (critic-leaning)

- **Role:** Associate Professor of Translation Studies; comparative-religion focus
- **Demographics:** Late 40s; based in Rome; PhD in Translation Studies (Bologna)
- **Experience:** Researches CAT-tool adoption among theological translators; 12 papers + 2 books; consultant for translation-tool startups
- **Workflow:** Doesn't actively translate in production; uses tools as research case-studies; tests tools with grad students; writes critical reviews
- **Goals:** Evaluate Comprehenslate as a research case study in theory-driven translation tools; identify gaps between tool design and real translator workflow; pressure-test claims
- **Pain Points (substrate-anchored):**
  1. *Tool descriptions over-promise; harmony viz might be marketing-speak unless backed by real LLM behavior* — CRITIQUE of D3 + D5 (need LLM-mechanism documentation)
  2. *5-layer architecture sounds clean but doesn't map to academic-translator workflow* — CRITIQUE of architecture (implicit D1)
  3. *BYO API key model is a niche-tech-savvy assumption; alienates many academic translators* — STRONG CRITIQUE of D2
  4. *3-tier triage assumes essential vs differentiating; but for academic critics, "deferrable" (e.g., TM) might be exactly what makes the tool research-defensible* — CRITIQUE of D7
  5. *"Innovative heavy" framing is fine but who validates principle-derived features have research backing?* — CRITIQUE of D3
  6. *Local LLM at v1 is great in principle; in practice Ollama performance varies wildly + setup is hard* — REFINE on D8
- **Current Tools:** SDL Trados Studio (research); CafeTran; OmegaT; ATA newsletters; GitHub for community tools
- **Representative Quote:** *"Show me where the harmony-layer preservation claim is operationalized in the LLM, not just visualized in the UI. If I can't see the LLM-level guarantee, the visualization is empty calories."*
- **Substrate Anchor:** `harmony_layer.md` (non-negotiable claim being scrutinized); Mac-app finding §1 (architecture); Mac-app finding §5 (BYO API key + multi-provider + 3-tier triage); `translation_principals.md` (principles being tested)

---

**Mechanism trace (PC3):** Combination (per-persona × per-substrate-source) + Absence Recognition (P5 academic critic = deliberately-absent confirmation-bias) + Domain Transfer (persona-design conventions from UX research) + Substrate-anchoring (anti-hallucination rule from P1).

**5-test PC3:** ACTIONABLE (each persona substrate-anchored; variant-spread verified; bias-balance built in via P5).

---

## P4 — 50-cell Pressure-Test Walkthrough Matrix

### Principal Candidate (PC4)

> ⚠ **Synthesis Notice applies to every cell.** See §P1.

#### D1 — Project-as-data-model (`.compldoc` bundle)

| Persona | Reaction | Gloss + Design Implication |
|---|---|---|
| **P1 Mehmet** | + supportive | Already thinks mesele-by-mesele; `.compldoc` fits mental model. → **KEEP** |
| **P2 Salma** | + supportive with caveat | Bundle-per-translation matches editor workflow. But: multi-translator collab? → **REFINE: clarify single-user constraint** |
| **P3 Aliyah** | + supportive | A book of 200 couplets = one project. Native Mac docs familiar. → **KEEP** |
| **P4 Avraham** | + supportive with caveat | Project = tractate makes sense. Will bundle handle 4-5 commentary layers? → **REFINE: multi-channel apparatus bundle structure** |
| **P5 Elena** | neutral | Document-based-app is conventional; nothing innovative. → **KEEP (don't claim differentiator)** |

**Aggregate:** 4 supportive + 1 neutral → **CONFIRMED** (minor refinement on multi-channel apparatus).

#### D2 — BYO API key + Keychain

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | – critical | Not technical. API key setup feels like a barrier. → **QUESTIONED** |
| **P2 Salma** | – critical | Small editor team; managing 5 keys = nightmare. → **QUESTIONED** |
| **P3 Aliyah** | neutral | Tech-comfortable but friends won't adopt. → **REFINE** |
| **P4 Avraham** | – critical | Yeshiva tech is conservative. Where's managed option? → **QUESTIONED** |
| **P5 Elena** | – very critical | BYO API key alienates 60% of academic theological translators. → **QUESTIONED** |

**Aggregate:** 4 critical + 1 refined → **QUESTIONED**. Strong signal. Consider hybrid: BYO for advanced; managed-paid for non-technical; or team-license model.

#### D3 — 10 principle-derived features

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + supportive | Harmony viz + lineage + collation + idiom/cultural inboxes = all valuable. → **KEEP** |
| **P2 Salma** | + supportive | Lineage = killer feature; collation = essential. → **KEEP** |
| **P3 Aliyah** | mixed | Lineage + alternative-renderings great; rhetorical-device detection uncertain. → **REFINE: validate LLM-level guarantee** |
| **P4 Avraham** | + supportive with caveat | Voice marking + apparatus essential. Idiom inbox less relevant for Aramaic. → **REFINE: per-corpus relevance** |
| **P5 Elena** | – critical | Are these researched or claimed? Show LLM mechanism. → **REFINE: document mechanisms** |

**Aggregate:** 3 supportive + 2 refined → **REFINED**. Refinement: document LLM-level mechanisms; per-corpus relevance toggle.

#### D4 — Multi-translation collation

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + very supportive | "What I need most. Vahide / Akarsu / mine side-by-side." → **KEEP** |
| **P2 Salma** | + very supportive | Essential. Want 5-column, not just 3. → **REFINE: support N-column** |
| **P3 Aliyah** | + supportive | Nicholson / Barks / Lewis for Rumi = transformative. → **KEEP** |
| **P4 Avraham** | + supportive | Soncino / Steinsaltz / ArtScroll for Talmud. → **KEEP** |
| **P5 Elena** | + supportive | Genuinely useful and well-grounded. → **KEEP** |

**Aggregate:** 5/5 supportive → **CONFIRMED**. Minor refinement: support 4+ column collation.

#### D5 — Per-chunk lineage view (ethical-provenance)

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + supportive | Audit trail for every decision. → **KEEP** |
| **P2 Salma** | + very supportive | "MUST have for editor compliance. Killer feature." → **KEEP** |
| **P3 Aliyah** | + supportive | Documents my 20-decisions-per-couplet. → **KEEP** |
| **P4 Avraham** | + supportive | Helps document Rashi-aligned vs Tosafot-aligned tradeoffs. → **KEEP** |
| **P5 Elena** | – skeptical | Lineage only as good as LLM self-report. Validate against ground truth. → **REFINE: clarify epistemic status** |

**Aggregate:** 4 supportive + 1 refined → **CONFIRMED** with epistemic-status refinement.

#### D6 — Glossary / terminology consistency

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + critical priority | "Terminology drift = my #1 nightmare. Mandatory." → **KEEP** |
| **P2 Salma** | + critical priority | "Editor work IS terminology consistency." → **KEEP** |
| **P3 Aliyah** | + supportive | Private term glossary across 200 couplets. → **KEEP** |
| **P4 Avraham** | + critical priority | Talmud terms must be consistent across tractates. → **KEEP** |
| **P5 Elena** | + supportive | Standard CAT-tool feature; well-established. → **KEEP** |

**Aggregate:** 5/5 strongly supportive → **CONFIRMED**. Note: consider elevating to "critical foundational" tier.

#### D7 — 3-tier triage + MVP scope

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | mixed | v1 enough if collation + glossary in. Lineage = wait. → **REFINE** |
| **P2 Salma** | – critical | "Lineage view essential. v2 = I won't use v1." → **QUESTIONED: lineage should be v1** |
| **P3 Aliyah** | mixed | EmbeddedPoetryPolicy needs v1 or I can't use it. → **REFINE** |
| **P4 Avraham** | mixed | VoiceMarkingPolicy + SourceApparatusPolicy = v1 essential, not v2. → **REFINE** |
| **P5 Elena** | – critical | Researchers need TM. v3+ = academic users skip v1. → **REFINE: TM earlier** |

**Aggregate:** mixed/critical from ≥3 → **REFINED**. Specifically: re-evaluate v1 essential tier — move lineage view, some Quality-layer Policies, TM earlier.

#### D8 — Multi-provider with local LLM at v1

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + supportive | Local LLM = privacy for theological work. → **KEEP** |
| **P2 Salma** | mixed | Local good in principle; setup is the issue. Editor-grade quality unclear. → **REFINE: quality verification** |
| **P3 Aliyah** | + supportive | Local for offline travel. → **KEEP** |
| **P4 Avraham** | + supportive | Yeshiva-friendly (no cloud). Ollama perf unproven for Talmud-scale. → **REFINE** |
| **P5 Elena** | mixed | Local great-on-paper; Ollama / LM Studio perf varies. Realistic expectations needed. → **REFINE** |

**Aggregate:** supportive but ≥3 quality concerns → **REFINED**. Set realistic local-LLM-quality expectations; document model recommendations.

#### D9 — Pause/resume + chunked persistence

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + supportive | Mesele-a-day for months. Essential. → **KEEP** |
| **P2 Salma** | + supportive | Quran takes a year+. → **KEEP** |
| **P3 Aliyah** | + supportive | 200 couplets over 6 months. → **KEEP** |
| **P4 Avraham** | + supportive | Tractate work is years. → **KEEP** |
| **P5 Elena** | + supportive | Well-established long-form pattern. → **KEEP** |

**Aggregate:** 5/5 → **CONFIRMED**. Universal support.

#### D10 — Monetization preferences

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | one-time preference | "Subscription = no. One-time = yes. Or donation." → **CHOOSE one-time/donation** |
| **P2 Salma** | team-license preference | "$200-500 for editor-grade. Team-license for 5 editors better." → **REFINE: team-license** |
| **P3 Aliyah** | open-source preference | "Open-source ideal. Else low one-time." → **CHOOSE open-source/low one-time** |
| **P4 Avraham** | one-time preference | "Yeshiva budgets prefer one-time over subscriptions." → **CHOOSE one-time** |
| **P5 Elena** | open-source-for-research preference | "Academic uses OSS. If commercial, paid license w/ academic-discount." → **REFINE: academic discount** |

**Aggregate:** strong preference for one-time + open-source + academic-discount; against subscription. → **REFINED with clear monetization signal**.

**Mechanism trace:** Combination (5 personas × 10 decisions per-cell synthesis) + Lens Shifting (per-persona lens applied to each design decision) + Substrate-anchoring (cells cite substrate where applicable).

**5-test PC4:** ACTIONABLE.

---

## P5 — Per-Commitment Re-test Verdicts

### Principal Candidate (PC5)

| # | Commitment | Verdict | Evidence |
|---|---|---|---|
| 1 | 5-layer architecture | **RE-TESTED — confirmed (implicit)** | Personas don't think in architecture, but workflows map to layers cleanly; no strong objection across 50 cells |
| 2 | Project-as-data-model | **RE-TESTED — confirmed with minor refinement** | D1: 4/5 supportive; P4 caveat on layered-apparatus bundle support |
| 3 | 3-tier triage + MVP scope | **found INVALID at v1 scope** | D7: ≥3 personas need currently-differentiating items at v1 (lineage; Quality-layer Policies; TM) |
| 4 | 10 principle-derived features | **confirmed but frame revised** | D3 + D4 + D5: features supported but P5 demands LLM-mechanism documentation; D4 + D5 universally valued |
| 5 | BYO API key + multi-provider with local at v1 | **found INVALID (BYO)** + **REFINED (local LLM)** | D2: ≥3 critical concerns about BYO; D8: local-LLM quality concerns from ≥3 |
| 6 | Pause/resume + chunked persistence | **RE-TESTED — confirmed** | D9: 5/5 supportive |

### Piece-level Inversion Candidate (PI5)

**Assumption:** verdicts propagate via CONFIRMED / REFINED / QUESTIONED to prior Mac-app finding (relationship-label commitment).

**Alternative:** "All commitments CONFIRMED; don't QUESTION anything (rubber-stamp the prior)."

**5-test:** WEAK — violates matrix evidence; over-confirms; misses real-signal that BYO API key + 3-tier triage need revisiting. **REJECTED.**

**5-test PC5:** ACTIONABLE.

---

## P6 — Synthesis-Based Design Recommendations

### Principal Candidate (PC6)

> ⚠ **Synthesis Caveat (mandatory):** These recommendations are derived from AI-synthesized personas. Validate against real translator interviews (per Research Plan §2) before committing to design changes.

| # | Decision | Recommendation | Priority |
|---|---|---|---|
| D1 | Project-as-data-model | KEEP — document multi-channel apparatus support for Talmud-style corpora | LOW |
| D2 | BYO API key + Keychain | **REVISIT** — consider hybrid: BYO for advanced + managed-paid for non-technical; or team-license model | **HIGH** |
| D3 | 10 principle-derived features | REFINE — document LLM-level mechanisms (especially harmony preservation); per-corpus relevance toggle | MED |
| D4 | Multi-translation collation | KEEP — confirmed universal value; support 4+ column collation | LOW |
| D5 | Per-chunk lineage view | KEEP — clarify epistemic status (LLM-self-report vs ground truth) | LOW |
| D6 | Glossary / terminology consistency | KEEP — strongly confirmed; consider tier elevation ("critical foundational") | LOW |
| D7 | 3-tier triage + MVP scope | **REVISIT** — re-evaluate v1 essential tier (move lineage; some Quality-layer Policies; TM) | **HIGH** |
| D8 | Multi-provider with local LLM at v1 | REFINE — set realistic local-LLM expectations; document model recommendations; test on Mac M-series hardware | MED |
| D9 | Pause/resume + chunked persistence | KEEP — strongly confirmed | LOW |
| D10 | Monetization preferences | DECIDE — strong signal toward one-time + open-source + academic-discount; against subscription. Team license for editor-shop users | MED |

**Mechanism trace:** Combination + Lens Shifting (per-decision viewed through aggregate-persona reaction).

**5-test PC6:** ACTIONABLE.

---

## P7 — Inherited Commitments Re-test (admin section per CONCLUDE)

### Principal Candidate (PC7)

| Commitment | Source | Status | Evidence |
|---|---|---|---|
| 5-layer architecture | Mac-app finding | **RE-TESTED — confirmed (implicit)** | Workflows map; no strong objection |
| Project-as-data-model | Mac-app finding | **RE-TESTED — confirmed** | D1: 4/5 supportive |
| 3-tier triage + MVP scope | Mac-app finding | **RE-TESTED — found INVALID at v1 scope** | D7: ≥3 personas need re-tiering |
| 10 principle-derived features | Mac-app finding | **RE-TESTED — confirmed with frame revision** | D3-D5: supported with LLM-mechanism documentation refinement |
| BYO API key + multi-provider with local at v1 | Mac-app finding | **RE-TESTED — BYO found INVALID; local LLM REFINED** | D2: ≥3 critical; D8: realistic-expectations refinement needed |
| Pause/resume + chunked persistence | Mac-app finding | **RE-TESTED — confirmed** | D9: 5/5 |
| Translation principles' comprehensation identity | SKILL/references/core/ | **INHERITED-WITHOUT-RE-TEST** | Substrate used; not re-tested |
| Harmony layer Tier 1-2 non-negotiable | SKILL/references/core/ | **INHERITED-WITHOUT-RE-TEST** | Substrate; P5 raised LLM-mechanism validation but didn't refute principle |
| Anti-bloat principle | Session-recurring | **INHERITED-WITHOUT-RE-TEST** | Per-tier re-evaluation may refine application |
| FP2 "don't declare what LLM can infer" | `schemas_rationale_and_policy_list` finding | **INHERITED-WITHOUT-RE-TEST** | Not directly tested |
| schemas.py 3-layer architecture | SKILL/references/config/ | **INHERITED-WITHOUT-RE-TEST** | Underlying substrate |
| SKILL.md 5-step workflow | SKILL/SKILL.md | **INHERITED-WITHOUT-RE-TEST** | Underlying substrate |

### Piece-level Inversion Candidate (PI7)

**Assumption:** Re-test verdicts propagate per CONCLUDE protocol (relationship-label commitment).

**Alternative:** Skip propagation; treat as informational only.

**5-test:** WEAK — violates CONCLUDE protocol; loses corrective reach back into Mac-app finding. **REJECTED.**

**5-test PC7:** ACTIONABLE.

---

## P8 — Open Questions

### Principal Candidate (PC8)

#### Monitoring
- **Substrate calibration** — refresh personas when `references/core/` or Mac-app finding evolves
- **Provider landscape** — Apple Intelligence as future provider may shift the BYO key calculus

#### Blocked
None.

#### Research Frontiers
- **Secondary stakeholders** — editors who hire translators; publishers commissioning translations. Not direct users but influence adoption.
- **Cross-corpus persona expansion** — Hindu / Sanskrit; Buddhist; Christian patristic personas would test cross-corpus design portability.
- **Translation Memory (TM) need-validation** — P5 raised TM as research-essential; not currently in synthesis; needs targeted validation.

#### Refinement Triggers
- **Real-interview execution.** Trigger: when v1 build commitment is imminent. Validate this synthesis with 20-30 real translators per the Research Plan in §2.
- **Mac-platform commitment.** Trigger: when v2 cross-platform plans solidify. P4 (Talmud translator) + P5 (academic) raised mismatches; mobile/iPad + Windows might be needed.
- **BYO API key model.** Trigger: as v1 ships; observe adoption metrics; if non-technical-user friction is real, ship managed-paid option in v2.
- **3-tier triage re-evaluation.** Trigger: before v1 freeze. Move lineage view, some Quality-layer Policies, and possibly TM to earlier tiers.

**Mechanism trace:** Absence Recognition (gaps the synthesis didn't cover) + Extrapolation (substrate evolution; provider landscape).

**5-test PC8:** ACTIONABLE.

---

## Inherited Frame Audit (between Phase 2 and Phase 3)

### Seed-level central assumption
"The SV6 hybrid deliverable is the right substrate to populate."

### Step (iii) Challenge scan
- **PI1** (P1 Inversion) challenges P1's methodology — REJECTED structurally.
- **P3 + P4 matrix** challenges BYO API key + 3-tier triage AT THE VALIDATION LEVEL — these aren't seed challenges; they're validation findings the synthesis genuinely surfaces. The seed survives challenge but PRODUCES challenges to upstream Mac-app commitments — which is exactly the inquiry's purpose.
- **PI5 + PI7** challenge the relationship-label commitments — REJECTED.

### Step (iv) Firing condition
Audit **does NOT fire** — all assumptions challenged via piece-level Inversion or via matrix validation. The matrix's challenges to Mac-app commitments are the inquiry's intended output, not seed-level destabilization.

---

## Phase 3 — Assembly Check

### Survivors combined
PC1 (methodology) + PC2 (research plan) + PC3 (5 personas) + PC4 (50-cell matrix) + PC5 (6 verdicts) + PC6 (recommendations) + PC7 (Re-test admin) + PC8 (open questions) — 8 principal candidates, all ACTIONABLE.

### Emergent
The matrix output IS the emergent insight. Two specific findings emerge that weren't predictable from any single piece:

**AE1 — BYO API key is the single largest mis-commitment in the Mac-app design.** ≥3 personas (P1, P2, P4) plus P5 critic raise it as a critical concern. The signal is strong enough that v1 plans should incorporate a managed-paid option.

**AE2 — The 3-tier triage's v1 essential vs v2 differentiating split needs re-evaluation.** Multiple personas (P2, P4, P5) name currently-differentiating features (lineage view; Quality-layer Policies; TM) as v1-essential for their workflows.

Both emergents are CONFIRMED via matrix evidence; they constitute the inquiry's central design feedback.

### Axis coverage check
Content axis (PC1-PC6) + Intervention-shape axis (PC5 + PC7 commit relationship-label propagation) + Scope axis (PC8 Open Questions) + Direction axis (PC5 verdicts move INVALID-direction where matrix demands). Multi-axis variance verified.

### Shared-input detection
Multiple pieces consume substrate (`references/core/` + Mac-app finding). Spurious convergence risk? Each piece transforms the substrate distinctly (P3 = personas; P4 = matrix cells; P5 = verdicts). Convergence on AE1 + AE2 emerges from matrix evidence, not from substrate-tautology.

---

## Telemetry

### Standard
- **Generators applied:** 4/4 (Combination throughout; Absence Recognition at P1 + P3 + P8; Domain Transfer at P2; Extrapolation at P8)
- **Framers applied:** 3/3 (Lens Shifting at P4; Constraint Manipulation ADD at P1 anti-pattern guards; Inversion at P1/P5/P7)
- **Convergence:** YES — 3+ mechanisms per PC
- **Survivors tested:** 8 PCs + 3 PIs + 2 AEs = 13 tested
- **Failure modes:** NONE

### Production-task additional telemetry

| Piece | Mechanism log | Classification | Inversion compliance |
|---|---|---|---|
| P1 | [Combination, AbsenceRec, ConstraintManip-ADD, Inversion] | META-DECISION | satisfied (PI1 tested) |
| P2 | [Combination, DomainTransfer] | content-production | n/a |
| P3 | [Combination, AbsenceRec, DomainTransfer, Substrate-anchor] | content-production | n/a |
| P4 | [Combination, LensShifting, Substrate-anchor] | content-production | n/a |
| P5 | [Combination, Lens Shifting, Inversion] | META-DECISION | satisfied (PI5 tested) |
| P6 | [Combination, LensShifting] | content-production | n/a |
| P7 | [Combination, Inversion] | META-DECISION | satisfied (PI7 tested) |
| P8 | [AbsenceRec, Extrapolation] | content-production | n/a |

### Verdict

**PROCEED.** Full coverage; convergence on every PC; all 3 meta-decision pieces' Inversion compliance satisfied; 2 emergents surfaced (AE1 BYO key mis-commitment; AE2 3-tier triage re-evaluation); no failure modes.
