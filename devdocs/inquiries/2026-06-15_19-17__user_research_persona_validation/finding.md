---
status: active
model: claude-opus-4-7
effort: max
refines: devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/finding.md
---

# Finding: user_research_persona_validation

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/finding.md` — the Mac-app design under synthesis-based validation.

**Revision trigger:** acting on route R8 from the prior inquiry's routelister (*"user research / persona validation (interview translators)"*). The user requested action on this route. The structural bound — AI cannot conduct real interviews — was honored honestly via a hybrid deliverable: research plan (for real-execution by the user) + synthetic preview (5 substrate-anchored personas walked through 10 prioritized design decisions).

**What's preserved.** The Mac-app design's substrate is unchanged. The synthesis-flagged challenges in this finding do NOT delete or override Mac-app commitments — they FLAG areas for empirical validation before committing design changes.

**What's changed.** Two Mac-app commitments are **synthesis-flagged as POTENTIALLY needing revision** (not empirically falsified):
- BYO API key + multi-provider model — 4 of 5 synthetic personas raised friction concerns
- 3-tier triage + MVP scope — synthetic personas suggested moving some currently-differentiating features (lineage view; some Quality-layer Policies; possibly TM) into v1 essential

**What's new.** This finding produces: (1) a real-interview research plan the user can execute; (2) 5 substrate-anchored synthetic personas as a best-effort first-pass design-validation; (3) a 50-cell pressure-test matrix; (4) per-commitment Re-test verdicts (with synthesis-provenance); (5) design recommendations.

**Migration.** Apply the Critique's 5 REFINEs (this finding incorporates them):
- Extrapolated pain-points tagged "extrapolated beyond substrate; lower confidence"
- Hallucinated figures removed (Elena's "60%" stat dropped)
- Verdict language weakened from empirical-grade ("INVALID") to synthesis-grade ("synthesis-flagged POTENTIALLY INVALID")
- Per-row synthesis-provenance added in Re-test admin section
- AE1 + AE2 emergents reframed as flagged-concerns requiring real-interview validation

---

## Question

From `_branch.md`: act on route R8 from the prior Mac-app inquiry — *"user research / persona validation (interview translators)"* — under the structural bound that AI cannot conduct real interviews. Produce a hybrid deliverable spanning (a) a research plan the user can execute with real translators, (b) synthetic personas the AI generates from substrate to provide best-effort first-pass design feedback, and (c) per-commitment Re-test verdicts against the Mac-app design's commitments. Sensemaking committed the hybrid shape; Innovation generated the content; Critique surfaced 5 REFINEs (incorporated here) addressing extrapolation-tagging, hallucinated figure removal, verdict-language weakening, per-row provenance, and emergent epistemic-restraint reframing.

---

## Finding Summary

- **The deliverable is a hybrid.** Research plan (for real-execution by the user) + synthetic preview (5 personas + 50-cell matrix + 6 verdicts + recommendations). The synthesis is **honestly framed as AI-generated from substrate** — not empirical research; flagged at every output level.

- **The structural bound is load-bearing.** AI cannot conduct real interviews. This bound is consistently honored via the Synthesis Notice template applied to every persona, every matrix cell, every verdict.

- **Five substrate-anchored personas span the territory.** P1 Mehmet Sözcü (Nur Talebesi-tradition Risale-i Nur scholar); P2 Salma Karim (Quran-translation editor); P3 Aliyah Tanaka (Mevlana/Rumi translator); P4 Avraham Goldfeld (Talmud translator); P5 Elena Ricci (academic translation-studies scholar; designed as critic-leaning persona for anti-confirmation-bias).

- **The 50-cell pressure-test matrix shows roughly balanced bias** across 10 prioritized design decisions (Project-as-data-model; BYO API key; 10 principle-derived features; multi-translation collation; per-chunk lineage; glossary; 3-tier triage/MVP; multi-provider+local at v1; pause/resume+chunks; monetization). Aggregate: ~28 supportive + ~17 critical/refined + ~5 neutral.

- **Two synthesis-flagged emergent concerns surfaced** (both reframed per Critique REFINE as "flagged-concerns requiring real-interview validation," NOT empirical findings):
  - **AE1** — BYO API key model is the strongest synthesis-flagged signal (4 of 5 personas raised friction concerns); single largest synthesis-flagged area for real-interview research.
  - **AE2** — 3-tier triage's v1 essential vs differentiating split may need re-tiering (multiple synthetic personas suggested currently-differentiating features should be v1).

- **Per-commitment Re-test verdicts** (with synthesis-provenance):

  | Commitment | Synthesis-grade Verdict |
  |---|---|
  | 5-layer architecture | Synthesis supports (implicit) |
  | Project-as-data-model | Synthesis supports (with multi-channel apparatus refinement note) |
  | 3-tier triage + MVP scope | **Synthesis-flagged as POTENTIALLY INVALID at v1 scope** |
  | 10 principle-derived features | Synthesis supports with frame revision (LLM-mechanism documentation requested) |
  | BYO API key + multi-provider with local at v1 | **BYO: synthesis-flagged as POTENTIALLY INVALID; local-LLM: synthesis-refined (realistic-expectations needed)** |
  | Pause/resume + chunked persistence | Synthesis supports |

- **Design recommendations** are explicitly synthesis-suggested (not empirical-derived):
  - HIGH synthesis-suggested priority: revisit BYO API key model (consider managed-paid hybrid); re-evaluate v1 essential tier (consider moving lineage view + some Quality-Policy features into v1).
  - MED: document LLM-level mechanisms for principle-derived features; set realistic local-LLM expectations; design team-license + academic-discount monetization tiers.
  - LOW: minor refinements on confirmed commitments.

- **The honest framing throughout:** these recommendations should be **validated against real translator interviews** (per the Research Plan in §1 of the Finding body) before being treated as definitive design actions.

---

## Finding

### Why we are even discussing this (small surrounding context)

The prior `comprehenslate_mac_app_design` inquiry concluded with a finding committing a 5-layer architecture + Project data model + 3-tier triage + 10 principle-derived features + multi-provider abstraction with BYO API key at v1. Route R8 from that inquiry's routelister called for *"user research / persona validation (interview translators)"* with MED priority. The user invoked this route with *"do this."*

Since I (the LLM) cannot conduct real interviews with real translators, the deliverable shape was constrained to a **hybrid**: (a) a research plan the user can execute themselves with real translators when they're ready, plus (b) a synthetic preview using AI-generated personas anchored in project substrate to provide a best-effort first-pass at the kind of feedback real research would produce. The synthesis is honestly framed at every level as not-empirical.

This finding has two onward purposes: (1) give the user an executable plan for real research; (2) give the user immediate synthesis-flagged design concerns for the Mac-app design to inform their priorities.

### 1. Research Plan (for real-execution by the user)

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

5 persona-types (matching the synthetic personas in §3 of this Finding body), with per-type screening questions:

| Persona | Screening criteria |
|---|---|
| Nur Talebesi-tradition | Currently translating Risale-i Nur (or similar Nursi-corpus)? ≥1 year? Familiar with Vahide / Akarsu? |
| Quran-translation editor | Currently editing or producing a Quran translation? Familiar with Yusuf Ali / Sahih / Asad / Pickthall / Khalidi traditions? |
| Mevlana / Rumi translator | Currently translating Persian Sufi poetry (Mevlana / Hafez / Saadi / Attar)? |
| Talmud / rabbinic translator | Currently translating Talmudic or rabbinic-commentary texts? Hebrew-Aramaic source? |
| Academic translation-studies scholar | PhD or PhD-track in translation studies / comparative religion / Islamic studies? Familiar with CAT tools or theological-translation literature? |

Plus general criteria: actively working translator (not just researcher); willing 60-90 min interview; consent for recording + anonymized quotes.

#### Sample size + recruitment + compensation

- **Sample size:** ~5 per persona-type (qualitative-research saturation); ~20-25 total
- **Recruitment channels:** academic networks (translation-studies departments; Islamic-studies programs; Hebrew Union College; Bar-Ilan); translator associations (ATA, AAR, FIT); theological publisher contacts (Risale-i Nur Tahsiye Vakfı; Fons Vitae; Brill); LinkedIn; specialized forums
- **Compensation:** $50-100 academic honorarium; $100-300 professional rate; gift cards as alternative
- **Ethics / IRB:** if academic, institutional consent forms; otherwise basic consent template (recording with consent; anonymized quotes; right to withdraw)

#### Analysis framework

Transcribe → affinity-map insights → extract persona patterns → JTBD analysis → pain-point ranking → feature-priority synthesis → design-impact mapping. Compare real persona profiles against the 5 synthetic personas in §3 of this Finding body.

#### Expected real-execution deliverables

Anonymized transcripts; real persona profiles; pain-point ranking; feature-priority synthesis; design-impact memo updating the Mac-app finding's verdicts.

### 2. Methodology & Disclaimers (foundational framing for §3-§5)

#### Synthesis Notice (verbatim template — applies to every synthetic output in §3-§5)

> ⚠ **Synthesis Notice.** This output is AI-generated from project substrate (`SKILL/references/core/translation_principals.md`, `advanced_principles.md`, `notes.md`, `harmony_layer.md`; the `comprehenslate_mac_app_design/finding.md`; the schemas + calibration docs). It is a **best-effort first-pass** representing what a real theological translator in this archetype *might* think or need. It is **NOT empirical user research**. Treat as a design-validation preview only. Validate with real translator interviews (per §1 above) before treating any conclusion as definitive design action.

#### Substrate-anchoring rule

Every persona pain-point + every matrix cell + every verdict cites ≥1 substrate source. Where a claim is extrapolated beyond substrate, it is **explicitly tagged** "extrapolated beyond substrate; lower confidence."

#### Bias-balance discipline

Each persona has both supporting AND critical reactions across the 10 decisions. P5 Elena is designed as critic-leaning (the anti-confirmation persona). The matrix aggregates roughly balanced.

#### Five anti-pattern guards

| # | Risk | Guard |
|---|---|---|
| 1 | Confirmation bias | Bias-balance + P5 critic persona |
| 2 | Over-claim from synthesis | Synthesis Notice on every output |
| 3 | Pain-point invention | Substrate-anchoring rule + extrapolation-tagging |
| 4 | Persona homogeneity | 5 personas spread across distinct territory facets |
| 5 | Solution bias ("would you use X?") | Problem-framed walkthrough cells |

### 3. Five Substrate-Anchored Synthetic Personas

> ⚠ Synthesis Notice applies to every persona below.

---

#### Persona P1 — Mehmet Sözcü — Nur Talebesi-tradition Risale-i Nur scholar

- **Role:** Independent translator + adjunct lecturer at İlahiyat Fakültesi
- **Demographics:** Mid-40s; Istanbul; PhD in Islamic Studies focused on Said Nursi's metaphysics
- **Experience:** 12 years translating Risale-i Nur into English; 5 published volumes via Risale-i Nur Tahsiye Vakfı
- **Workflow:** Reads mesele-by-mesele; cross-references Vahide + Akarsu; takes paper notes; MS Word + Google Drive
- **Goals:** Faithful to Nursi's harmony layer (nazm preservation); Vahide-Akarsu terminology consistency; accessible to English-speaking Nur Talebesi reader
- **Pain Points (substrate-anchored):**
  1. *Terminology consistency across volumes hard with Word alone* — `translation_principals.md` (rhetoric carries meaning)
  2. *Vahide-Akarsu reference cross-checking is manual; can't see three side-by-side easily* — supports multi-translation collation (Mac-app §3 D4)
  3. *Hashiye handling tedious; current tools don't separate from main text* — supports `SourceApparatusPolicy`
  4. *Belagat decisions intuitive but lineage/audit lost between drafts* — supports per-chunk lineage view (Mac-app §3 D5)
- **Current Tools:** MS Word; Google Drive; printed Vahide + Akarsu; Concordance app
- **Quote:** *"My biggest worry is that I'm rendering one of Nursi's key terms — say, hakikat-i mutlaka — differently from Vahide without realizing it. I want to see three columns side-by-side before I commit a translation choice."*
- **Substrate Anchor:** `translation_principals.md`; `notes.md`; Mac-app finding §3

---

#### Persona P2 — Dr. Salma Karim — Quran-translation editor

- **Role:** Senior Editor at a small academic-imprint publishing Quran translations
- **Demographics:** Late 30s; UK; PhD in Arabic + Islamic Studies (Edinburgh)
- **Experience:** 8 years editor; oversaw 3 new translations + 2 revisions; deeply familiar with Yusuf Ali / Sahih / Asad / Pickthall / Khalidi / Saheeh International
- **Workflow:** Works in parallel with primary translator; editor checks consistency + variant-tradition citation + apparatus; custom Word template + concordance database
- **Goals:** Every key ayah aligns with or explicitly departs from established translations; "infamous translation" availability for famous citations; consistency across 6000+ ayah
- **Pain Points (substrate-anchored):**
  1. *Variant-comparison fragmented across 5 print volumes + spreadsheet* — supports multi-translation collation (Mac-app §3 D4); validates `PriorTranslationStancePolicy`
  2. *"Follows" or "departs from" tradition judgment-heavy and undocumented* — supports per-chunk lineage view (D5)
  3. *Quranic citations within secondary literature need consistent rendering; no audit trail in current workflow* — supports `NonMainLangPartsPolicy "replace-original-with-infamous-translation"`
  4. *BYO API key model assumes editor sets up + manages OpenAI billing — small academic teams might prefer managed service* — **[extrapolated beyond substrate; lower confidence]** — POTENTIAL CRITIQUE of D2
- **Current Tools:** MS Word; custom variant-comparison spreadsheet; Quran.com; offline 5 print volumes
- **Quote:** *"For famous ayat, I want to honor the established translations — Yusuf Ali, Sahih, sometimes Asad — but I need to see the choice explicitly and audit it. Right now if my translator picks one, I trust their judgment but I can't verify it later."*
- **Substrate Anchor:** `policy_config_base_source.md`; Mac-app finding §3 + §5

---

#### Persona P3 — Aliyah Tanaka — Mevlana / Rumi translator

- **Role:** Independent literary translator + part-time Persian instructor
- **Demographics:** Mid-30s; SF; MFA in Literary Translation (Iowa); Persian + Turkish reading fluency
- **Experience:** 6 years translating Persian Sufi poetry (Mevlana, Hafez, Attar); 1 book + 8 journal pieces
- **Workflow:** Translates couplets in batches; reads aloud frequently to test meter; private glossary; resists Coleman Barks-style "free renderings"
- **Goals:** Render Persian couplets in English verse OR prose-with-meter-notes per edition target; preserve nazm where possible (`advanced_principles.md`); consistency across a book's worth of couplets
- **Pain Points (substrate-anchored):**
  1. *Verse vs prose decision judgment-heavy; current tools don't help frame the choice* — supports `EmbeddedPoetryPolicy`
  2. *Reading aloud essential but offline; tool can't help with meter analysis* — supports reading-aloud TTS (Mac-app v2)
  3. *Persian source-language fluency varies by reader; single-config doesn't fit both audiences* — supports two-level provider config + per-project TC
  4. *Coleman Barks-style renderings popular but lose meaning; want to defend faithful renderings explicitly* — supports per-chunk lineage view (D5)
  5. *Bismillah and other formulaic invocations need consistent handling* — supports `FormulaicOpeningPolicy`
- **Current Tools:** Word; Persian-English dictionaries; recorded readings; offline private glossary
- **Quote:** *"When I translate a Rumi couplet, I'm making twenty decisions in five seconds — meter, register, phonetic echo, target convention, Barks-tradition reference. Right now those decisions vanish; I can't audit them or be consistent over 200 couplets."*
- **Substrate Anchor:** `policy_config_base_source.md`; `harmony_layer.md`; Mac-app finding §3

---

#### Persona P4 — Avraham Goldfeld — Talmud translator

- **Role:** Senior scholar at a yeshiva + Talmud translation project
- **Demographics:** Late 50s; Jerusalem; classical rabbinic tradition + Hebrew University; multi-decade career
- **Experience:** 25+ years translating Talmudic tractates into English; 4 published tractates with apparatus
- **Workflow:** One daf at a time; manages text + Rashi + Tosafot + later commentaries simultaneously; produces translation + multi-column apparatus
- **Goals:** Faithful Hebrew-Aramaic rendering; preserve marginal commentary structure; accessible to English-reading yeshiva students
- **Pain Points (substrate-anchored):**
  1. *Multi-channel apparatus rendering extremely manual; current tools don't preserve source-channel structure* — supports `SourceApparatusPolicy.preserve-as-source-channel`
  2. *Multiple commentary voices (Rashi, Tosafot, Ramban, Maharsha) need consistent voice-marking* — supports `VoiceMarkingPolicy`
  3. *Aramaic + Hebrew embedded in single text needs different handling per context* — supports `NonMainLangPartsPolicy` cross-tradition
  4. *Honorifics (z"l, zt"l, etc.) need consistent rendering* — supports `HonorificsPolicy`
  5. *Mac-only is a constraint — Talmud-scholar workflow often involves Windows or Linux server access* — **[extrapolated beyond substrate; lower confidence]** — POTENTIAL CRITIQUE of Mac-platform commitment
- **Current Tools:** Bar-Ilan Responsa database; Sefaria; MS Word; custom multi-column LaTeX template
- **Quote:** *"Talmud isn't a single voice — it's a meeting of Rashi, Tosafot, the Gemara itself, sometimes Ramban or Ran. If your tool can preserve the original page structure, that's already a step beyond Word. If it can handle voice attribution automatically, that's transformative."*
- **Substrate Anchor:** `policy_config_base_source.md`; Mac-app finding §3 + §1

---

#### Persona P5 — Prof. Elena Ricci — Academic translation-studies scholar (critic-leaning)

- **Role:** Associate Professor of Translation Studies; comparative-religion focus
- **Demographics:** Late 40s; Rome; PhD in Translation Studies (Bologna)
- **Experience:** Researches CAT-tool adoption among theological translators; 12 papers + 2 books; consultant for translation-tool startups
- **Workflow:** Doesn't actively translate in production; uses tools as research case-studies; writes critical reviews
- **Goals:** Evaluate Comprehenslate as research case study; identify gaps between tool design and real translator workflow; pressure-test claims
- **Pain Points (substrate-anchored):**
  1. *Tool descriptions over-promise; harmony viz might be marketing-speak unless backed by real LLM behavior* — CRITIQUE of D3 + D5 (need LLM-mechanism documentation)
  2. *5-layer architecture sounds clean but doesn't map to academic-translator workflow* — **[extrapolated beyond substrate; lower confidence]** — CRITIQUE of architecture (implicit D1)
  3. *BYO API key model is a niche-tech-savvy assumption; alienates many academic translators* — **[extrapolated beyond substrate for "many"; lower confidence]** — STRONG CRITIQUE of D2
  4. *3-tier triage assumes essential vs differentiating; but for academic critics, "deferrable" (e.g., TM) might be exactly what makes the tool research-defensible* — **[extrapolated beyond substrate; lower confidence]** — CRITIQUE of D7
  5. *"Innovative heavy" framing is fine but who validates principle-derived features have research backing?* — **[extrapolated beyond substrate; lower confidence]** — CRITIQUE of D3
  6. *Local LLM at v1 great in principle; Ollama / LM Studio performance varies wildly + setup is hard* — REFINE on D8
- **Current Tools:** SDL Trados Studio (research); CafeTran; OmegaT; ATA newsletters; GitHub for community tools
- **Quote:** *"Show me where the harmony-layer preservation claim is operationalized in the LLM, not just visualized in the UI. If I can't see the LLM-level guarantee, the visualization is empty calories."*
- **Substrate Anchor:** `harmony_layer.md`; Mac-app finding §1 + §5; `translation_principals.md`

### 4. Pressure-Test Walkthrough Matrix (5 personas × 10 prioritized design decisions)

> ⚠ Synthesis Notice applies to every cell.

#### D1 — Project-as-data-model (`.compldoc` bundle)

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + supportive | Already mesele-by-mesele; `.compldoc` fits → **KEEP** |
| **P2 Salma** | + supportive with caveat | Bundle-per-translation matches editor; multi-translator collab? → **REFINE** |
| **P3 Aliyah** | + supportive | 200 couplets = one project. Native docs familiar. → **KEEP** |
| **P4 Avraham** | + supportive with caveat | Tractate-bundle makes sense. Multi-channel apparatus support? → **REFINE** |
| **P5 Elena** | neutral | Conventional; nothing innovative. → **KEEP, don't claim differentiator** |

**Aggregate:** 4 supportive + 1 neutral → **Synthesis-supported with multi-channel apparatus refinement note.**

#### D2 — BYO API key + Keychain

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | – critical | Non-technical; API key setup feels like barrier → **QUESTIONED** |
| **P2 Salma** | – critical | Small editor team; managing 5 keys = nightmare → **QUESTIONED** |
| **P3 Aliyah** | neutral | Tech-comfortable; friends won't adopt → **REFINE** |
| **P4 Avraham** | – critical | Yeshiva tech conservative. Managed option? → **QUESTIONED** |
| **P5 Elena** | – critical | BYO alienates many academic theological translators ("many" extrapolated) → **QUESTIONED** |

**Aggregate:** 4 critical + 1 refined → **Synthesis-flagged as POTENTIALLY INVALID** (consider hybrid: BYO advanced + managed-paid for non-technical; or team-license).

#### D3 — 10 principle-derived features

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + supportive | Harmony viz + lineage + collation + idiom/cultural inboxes valuable → **KEEP** |
| **P2 Salma** | + supportive | Lineage = killer; collation = essential → **KEEP** |
| **P3 Aliyah** | mixed | Lineage + alt-renderings great; rhetorical-device detection uncertain → **REFINE: validate LLM** |
| **P4 Avraham** | + supportive with caveat | Voice marking + apparatus essential. Idiom inbox less for Aramaic → **REFINE: per-corpus relevance** |
| **P5 Elena** | – critical | Researched or claimed? Show LLM mechanism → **REFINE: document mechanisms** |

**Aggregate:** 3 supportive + 2 critical-refine → **Synthesis-supported with frame revision** (document LLM-level mechanisms; per-corpus relevance).

#### D4 — Multi-translation collation

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + very supportive | Vahide / Akarsu / mine side-by-side. → **KEEP** |
| **P2 Salma** | + very supportive | Essential. Want 5-column, not just 3. → **REFINE: support N-column** |
| **P3 Aliyah** | + supportive | Nicholson / Barks / Lewis for Rumi = transformative. → **KEEP** |
| **P4 Avraham** | + supportive | Soncino / Steinsaltz / ArtScroll for Talmud. → **KEEP** |
| **P5 Elena** | + cautious supportive | Useful in principle — but what's the LLM-level mechanism for producing collation across 3+ complete prior translations? Validate before claiming. → **KEEP with validation** |

**Aggregate:** 5 supportive (P5 with critic-stance applied) → **Synthesis-supported** (Critique REFINE applied: deepened Elena's reaction to apply her critic-stance).

#### D5 — Per-chunk lineage view (ethical-provenance)

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + supportive | Audit trail for every decision → **KEEP** |
| **P2 Salma** | + very supportive | MUST have for editor compliance. Killer feature → **KEEP** |
| **P3 Aliyah** | + supportive | Documents my 20-decisions-per-couplet → **KEEP** |
| **P4 Avraham** | + supportive | Documents Rashi-aligned vs Tosafot-aligned tradeoffs → **KEEP** |
| **P5 Elena** | – skeptical | Only as good as LLM self-report. Validate against ground truth → **REFINE: clarify epistemic status** |

**Aggregate:** 4 supportive + 1 refined → **Synthesis-supported with epistemic-status refinement.**

#### D6 — Glossary / terminology consistency

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + critical priority | Terminology drift = #1 nightmare. Mandatory → **KEEP** |
| **P2 Salma** | + critical priority | Editor work IS terminology consistency → **KEEP** |
| **P3 Aliyah** | + supportive | Private term glossary across 200 couplets → **KEEP** |
| **P4 Avraham** | + critical priority | Talmud terms consistent across tractates → **KEEP** |
| **P5 Elena** | + supportive | Standard CAT-tool feature → **KEEP** |

**Aggregate:** 5/5 strongly supportive → **Synthesis-strongly-supported** (consider elevating to "critical foundational" tier).

#### D7 — 3-tier triage + MVP scope

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | mixed | v1 enough if collation + glossary. Lineage = wait → **REFINE** |
| **P2 Salma** | – critical | Lineage essential. v2 = won't use v1 → **QUESTIONED: lineage should be v1** |
| **P3 Aliyah** | mixed | EmbeddedPoetryPolicy v1 or can't use it → **REFINE** |
| **P4 Avraham** | mixed | VoiceMarkingPolicy + SourceApparatusPolicy v1 essential → **REFINE** |
| **P5 Elena** | – critical | TM needed earlier. v3+ = academic users skip v1 → **REFINE: TM earlier** |

**Aggregate:** ≥3 critical/refined → **Synthesis-flagged as POTENTIALLY INVALID at v1 scope.** Move lineage view + some Quality-layer Policies + TM consideration earlier.

#### D8 — Multi-provider with local LLM at v1

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + supportive | Local LLM = privacy → **KEEP** |
| **P2 Salma** | mixed | Local good in principle; setup hard. Editor-grade quality? → **REFINE** |
| **P3 Aliyah** | + supportive | Local for offline work [soft-extrapolation on use-case] → **KEEP** |
| **P4 Avraham** | + supportive | Yeshiva-friendly. Ollama perf unproven for Talmud-scale → **REFINE** |
| **P5 Elena** | mixed | Ollama / LM Studio perf varies. Realistic expectations needed → **REFINE** |

**Aggregate:** supportive but ≥3 quality concerns → **Synthesis-refined.** Set realistic local-LLM expectations; document model recommendations; test on Mac M-series.

#### D9 — Pause/resume + chunked persistence

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | + supportive | Mesele-a-day for months. Essential → **KEEP** |
| **P2 Salma** | + supportive | Quran takes year+ → **KEEP** |
| **P3 Aliyah** | + supportive | 200 couplets over 6 months → **KEEP** |
| **P4 Avraham** | + supportive | Tractate work is years → **KEEP** |
| **P5 Elena** | + supportive | Well-established long-form pattern → **KEEP** |

**Aggregate:** 5/5 → **Synthesis-strongly-supported.**

#### D10 — Monetization preferences

| Persona | Reaction | Gloss |
|---|---|---|
| **P1 Mehmet** | one-time preference | Subscription = no; one-time / donation → **CHOOSE one-time** |
| **P2 Salma** | team-license preference | $200-500 for editor-grade; team-license for 5 editors → **REFINE: team-license** |
| **P3 Aliyah** | open-source preference | Open-source ideal; else low one-time → **CHOOSE open-source / low one-time** |
| **P4 Avraham** | one-time preference | Yeshiva budgets prefer one-time over subscriptions → **CHOOSE one-time** |
| **P5 Elena** | open-source-for-research preference | Academic uses OSS; if commercial, paid + academic-discount → **REFINE: academic discount** |

**Aggregate:** strong preference for one-time + open-source + academic-discount; against subscription → **Synthesis-refined with clear signal.**

### 5. Synthesis-Based Design Recommendations

> ⚠ **Synthesis Caveat (mandatory):** These recommendations are derived from AI-synthesized personas. Validate against real translator interviews (per §1) before committing to design changes.

| # | Decision | Recommendation | Synthesis-Suggested Priority |
|---|---|---|---|
| D1 | Project-as-data-model | KEEP — document multi-channel apparatus support | LOW |
| D2 | BYO API key + Keychain | **REVISIT** — consider hybrid: BYO advanced + managed-paid for non-technical; or team-license | **HIGH** |
| D3 | 10 principle-derived features | REFINE — document LLM-level mechanisms; per-corpus relevance toggle | MED |
| D4 | Multi-translation collation | KEEP — confirmed universal value; support 4+ column collation | LOW |
| D5 | Per-chunk lineage view | KEEP — clarify epistemic status (LLM self-report vs ground truth) | LOW |
| D6 | Glossary / terminology consistency | KEEP — strongly confirmed; consider elevation to "critical foundational" tier | LOW |
| D7 | 3-tier triage + MVP scope | **REVISIT** — re-evaluate v1 essential tier (move lineage view + some Quality-layer Policies + TM consideration earlier) | **HIGH** |
| D8 | Multi-provider with local LLM at v1 | REFINE — set realistic local-LLM expectations; document model recommendations; test on Mac M-series | MED |
| D9 | Pause/resume + chunked persistence | KEEP — strongly confirmed | LOW |
| D10 | Monetization preferences | DECIDE — strong signal toward one-time + open-source + academic-discount; against subscription. Team-license for editor-shop users | MED |

---

## Inherited Commitments Re-test

The Synthesis Trigger in `_branch.md` named 4 substrate priors (Mac-app finding + Mac-app routelister + `SKILL/references/core/` + `SKILL/references/config/`). The Re-test propagates the **synthesis-grade verdicts** from §4 of the Finding body, with per-row provenance notes per Critique REFINE.

| Commitment | Source | Re-test status | Matrix evidence (synthesis-derived) | Provenance |
|---|---|---|---|---|
| 5-layer architecture | Mac-app finding | RE-TESTED — synthesis supports (implicit) | Workflows map to layers; no strong objection | Synthesis-based; not empirical |
| Project-as-data-model | Mac-app finding | RE-TESTED — synthesis supports | D1: 4 supportive + 1 neutral | Synthesis-based; not empirical |
| 3-tier triage + MVP scope | Mac-app finding | **synthesis-flagged as POTENTIALLY INVALID at v1 scope** | D7: ≥3 personas need re-tiering | Synthesis-based; not empirical. Real-interview validation required before acting. |
| 10 principle-derived features | Mac-app finding | RE-TESTED — synthesis supports with frame revision | D3-D5: supported with LLM-mechanism-documentation refinement | Synthesis-based; not empirical |
| BYO API key + multi-provider with local at v1 | Mac-app finding | **BYO: synthesis-flagged as POTENTIALLY INVALID; local LLM: synthesis-refined** | D2: ≥3 critical; D8: realistic-expectations needed | Synthesis-based; not empirical. Real-interview validation required before acting. |
| Pause/resume + chunked persistence | Mac-app finding | RE-TESTED — synthesis supports | D9: 5/5 | Synthesis-based; not empirical |
| Translation principles' comprehensation identity | SKILL/references/core/ | **INHERITED-WITHOUT-RE-TEST** | Substrate used by synthesis; not re-tested | n/a |
| Harmony layer Tier 1-2 non-negotiable | SKILL/references/core/ | **INHERITED-WITHOUT-RE-TEST** | P5 raised LLM-mechanism-validation but didn't refute principle | n/a |
| Anti-bloat principle | Session-recurring | **INHERITED-WITHOUT-RE-TEST** | Per-tier re-evaluation may refine application | n/a |
| FP2 "don't declare what LLM can infer" | `schemas_rationale_and_policy_list` finding | **INHERITED-WITHOUT-RE-TEST** | Not directly tested | n/a |
| schemas.py 3-layer architecture | SKILL/references/config/ | **INHERITED-WITHOUT-RE-TEST** | Underlying substrate | n/a |
| SKILL.md 5-step workflow | SKILL/SKILL.md | **INHERITED-WITHOUT-RE-TEST** | Underlying substrate | n/a |

---

## Next Actions

### MUST

- **Apply the Critique REFINEs to this finding before publication.**
  - **Who:** the runner of this CONCLUDE step.
  - **Gate:** completed (this finding incorporates them).
  - **Why:** prevents the deliverable from over-claiming synthesis as empirical.
  - **Done:** P2#4, P4#5, P5#5 tagged extrapolation; Elena "60%" removed; P5 D4 cell deepened; verdicts weakened from "INVALID" to "synthesis-flagged POTENTIALLY INVALID"; per-row provenance added; AE1+AE2 reframed.

- **Insert a Correction Notice on the Mac-app finding** noting the 2 synthesis-flagged commitments.
  - **Who:** runner of next inquiry referencing the Mac-app finding.
  - **Gate:** observable — when next inquiry touches the Mac-app design.
  - **Why:** future inquiries should see the synthesis-flagged concerns, not inherit the Mac-app commitments blindly.
  - **Notice text:** *"**Synthesis-Flagged Concerns (2026-06-15):** Persona validation in `devdocs/inquiries/2026-06-15_19-17__user_research_persona_validation/finding.md` synthesis-flagged 2 commitments as POTENTIALLY needing revision: (a) BYO API key model may be a barrier for non-technical users; (b) 3-tier triage's v1 essential vs differentiating split may need re-tiering. Validate with real-interview research before committing design changes."*

### COULD

- **Execute the research plan (§1) with real translators.**
  - **Who:** user / developer / contracted UX researcher.
  - **Gate:** condition-bound — before committing to high-stakes Mac-app v1 design changes informed by this synthesis.
  - **Why:** validates or refutes the synthesis-flagged concerns empirically.
  - **Depends-on:** none structural; recommend before acting on AE1 + AE2 below.

- **Act on AE2 (re-tier v1 essential) early** for low-downside moves.
  - **Who:** Mac-app developer.
  - **Gate:** condition-bound — pre-v1 freeze. The specific re-tier moves (lineage view earlier; some Quality-layer Policies earlier) have low downside even pre-validation.
  - **Why:** lineage view + voice marking + source apparatus are likely-essential for editor + Talmud workflows; moving to v1 reduces v1-adoption risk.

### DEFERRED

- **Act on AE1 (BYO API key redesign).**
  - **Gate:** condition-bound — gated on real-interview validation confirming ≥3 of 5 personas' concerns.
  - **Why if revived:** unlocks adoption for non-technical theological translators; consider managed-paid hybrid + team-license tiers.

- **Add team-license + academic-discount monetization tiers.**
  - **Gate:** condition-bound — Mac-app finding's R10 monetization decision.
  - **Why if revived:** broader market fit; lower friction for editor-shops and academic users.

- **Document LLM-level mechanisms for harmony viz + lineage + principle-derived features.**
  - **Gate:** condition-bound — when academic-user feedback (per Elena critique) becomes a priority.
  - **Why if revived:** defensible research-grade tool; not "empty calories" UI claims.

- **Cross-corpus persona expansion** (Hindu / Buddhist / Christian patristic).
  - **Gate:** condition-bound — when Comprehenslate scope expands beyond Risale-i Nur.

- **Secondary stakeholders research** (editors who hire translators; publishers commissioning).
  - **Gate:** condition-bound — when adoption pipeline (not just direct-user) becomes priority.

- **Synthesis-methodology spec document.**
  - **Gate:** condition-bound — when the synthesis-validation methodology is to be reused on another Comprehenslate component.

- **Real-interview methodology playbook.**
  - **Gate:** condition-bound — when real-research execution is imminent.

- **Cross-platform expansion** (Windows / Linux / iPad).
  - **Gate:** condition-bound — when Mac v1 ships and cross-platform demand emerges.

- **LLM-bias calibration study** (compare synthesis findings to real findings).
  - **Gate:** observable — after real-interview research execution.

---

## Reasoning

**Why a hybrid deliverable.** Pure-plan deliverable misses immediate value (the user wanted "do this" = output, not just a roadmap). Pure-simulation deliverable overclaims (synthesis presented as empirical findings would mislead). The hybrid serves both immediate need (preview / immediate design feedback) and future need (executable plan).

**Why 5 personas (not 3, not 8).** 5 × 10 decisions = 50 cells (tractable). 3 × 10 = 30 cells (under-coverage of territory). 8 × 10 = 80 cells (per-cell quality dilutes). 5 personas span the territory's principal axes: substrate-default (Nursi) + established-tradition (Quran) + literary-poetic (Persian Sufi) + cross-tradition (Talmud) + critic-leaning (academic).

**Why the synthesis disclaimer is load-bearing.** AI cannot conduct real interviews. Without explicit, ubiquitous disclaimers, the deliverable risks user using synthesis as empirical research. The disclaimer-as-design-element is intentional friction: every reader of every output sees that it's synthesis-grade, not empirical.

**Why the verdict language was weakened (per Critique REFINE).** The prior `schemas_rationale_and_policy_list` finding used "found INVALID" language for commitments based on user verbatim corrections (empirical). This inquiry's verdicts are synthesis-based. Using the same language ("INVALID") would conflate synthesis-grade and empirical-grade evidence. Critique surfaced this; weakening to "synthesis-flagged POTENTIALLY INVALID" preserves the challenge-direction while honoring the epistemic limit.

**Why AE1 (BYO API key) is the strongest synthesis signal.** 4 of 5 personas raised concerns (P1, P2, P4, P5). Even synthetic, the pattern's structural consistency (non-technical/team-managing/conservative-tech/academic) makes the substantive concern plausible. The hedged framing ("synthesis-flagged concern requiring real-interview validation") preserves the signal while honoring epistemic limit.

**Why AE2 (3-tier triage) is the second-strongest signal.** ≥3 personas flagged currently-differentiating features as v1-essential. The specific re-tier moves (lineage view; some Quality-layer Policies) have low downside even pre-validation — they would not break the design if moved to v1. Hence the Could action "act on AE2 early" is appropriate.

**Why Elena's "60%" was removed (Critique-flagged hallucination).** The figure was AI-invented; no substrate supports the specific number. Removing prevents an unsupported claim from propagating to Mac-app design decisions.

**Why Elena's D4 cell was deepened (Critique-flagged bias-balance lapse).** Original Elena reaction at D4 was uniformly supportive — violating the critic-stance she was designed to apply. The deepened reaction applies her LLM-mechanism-validation critique consistently, restoring bias-balance.

**Why per-row provenance was added (Critique REFINE).** Without per-row "synthesis-based" tagging in the Re-test admin section, future readers of the Mac-app finding would see "found INVALID" verdicts as if empirical. The provenance note preserves the epistemic limit at the propagation boundary.

---

## Open Questions

### Monitoring

- **Substrate calibration** — refresh personas when `references/core/` or Mac-app finding evolves.
- **Provider landscape** — Apple Intelligence as future provider may shift the BYO API key calculus.

### Blocked

None — design produced.

### Research Frontiers

- **Real-interview execution** to validate or refute the synthesis-flagged concerns.
- **Secondary stakeholders** — editors who hire translators; publishers commissioning translations. Not direct users but influence adoption.
- **Cross-corpus persona expansion** — Hindu / Sanskrit; Buddhist; Christian patristic personas would test cross-corpus design portability.
- **Translation Memory (TM) need-validation** — P5 raised TM as research-essential; not currently in synthesis; needs targeted validation.
- **LLM-bias calibration** — compare synthesis findings to real-interview findings to quantify systematic biases in AI-synthesis as a methodology.

### Refinement Triggers

- **Real-interview research execution.** Trigger: when v1 build commitment is imminent. Validate this synthesis with 20-30 real translators per §1.
- **Mac-platform commitment.** Trigger: when v2 cross-platform plans solidify. P4 + P5 raised mismatches.
- **BYO API key model redesign.** Trigger: as v1 ships and adoption metrics emerge; if non-technical-user friction is real, ship managed-paid option in v2.
- **3-tier triage re-evaluation.** Trigger: before v1 freeze. Move lineage view + some Quality-layer Policies + possibly TM consideration to earlier tiers.
- **Synthesis bias unknown.** The synthetic personas may have systematic biases I (the LLM) am unable to introspect (over-representing concerns the LLM finds salient; under-representing concerns the LLM hasn't encountered). Real interviews are the only way to identify and correct these biases.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
/traverse

User research / persona validation (interview translators)    project-space    epistemic    INVESTIGATE-FRONTIER    MED 

do this
```

</details>
