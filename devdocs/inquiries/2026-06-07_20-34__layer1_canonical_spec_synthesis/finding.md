---
status: active
version: v1.0
model: claude-opus-4-7[1m]
effort: max
refines:
  - devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md
  - devdocs/inquiries/2026-06-06_11-47__a1_cultural_reference_recognition_levels/finding.md
  - devdocs/inquiries/2026-06-06_12-37__a2_domain_expertise_levels/finding.md
  - devdocs/inquiries/2026-06-06_13-33__a3_source_culture_levels/finding.md
  - devdocs/inquiries/2026-06-06_14-05__a4_purpose_categories/finding.md
  - devdocs/inquiries/2026-06-06_14-38__a5_source_fidelity_levels/finding.md
  - devdocs/inquiries/2026-06-06_14-59__a6_form_preservation_levels/finding.md
  - devdocs/inquiries/2026-06-07_19-07__a7_scaffolding_levels/finding.md
  - devdocs/inquiries/2026-06-07_19-51__a8_analysis_depth_levels/finding.md
---
# Finding: Comprehenslate Layer 1 Canonical Spec — v1.0

## Question

**From `_branch.md`.** Comprehenslate is an AI-assisted translation system. The 8-axis Layer 1 (USER-FACING AXES) framework is now fully specified across 9 prior findings: the root architectural finding established the 4-layer / 4-family / 8-axis structure; 8 axis-level findings (A1 cultural-reference-recognition closing the A1 composite-axis chain through A8 analysis-depth closing the framework) specified each axis. The A8 finding closed the framework at 8/8 axes complete and marked framework-synthesis as a Next Actions COULD item — the synthesis being this inquiry's purpose.

This synthesis produces the SINGLE CANONICAL LAYER 1 SPEC at v1.0 consolidating all 8 axes into one authoritative reference document. Self-contained dense (per user choice): full per-level prose reproduced; cross-axis interaction tables produced; per-purpose × per-axis default matrix synthesized; special patterns compendium documented; receptive-only applicability compendium consolidated; carry-forward refinement notes resolved into bundled maintenance items; policy interaction map produced; framework completion declared; versioning anchored; downstream-unblock list specified; inherited commitments re-tested at synthesis level.

**Goal.** Serve as: (a) single-source-of-truth Layer 1 reference; (b) input to pydantic dataclass commit; (c) input to translator-AI prompt assembly with all 8 axes + 5 always-on policies; (d) versioning anchor (v1.0) for future framework changes; (e) reference for Layer 1A UX preset catalog design.

## Finding Summary

- **Comprehenslate Layer 1 = 8 user-facing axes in 4 families.** Reader family: A1 Reader Level (composite-axis with 5 sub-fields), A2 Domain Expertise, A3 Source Culture. Purpose family: A4 Purpose. Strategy family: A5 Source Fidelity, A6 Form Preservation, A7 Scaffolding. Depth family: A8 Analysis Depth. FRAMEWORK CLOSED at 8/8 axes.

- **Layer 1 sits within a 4-layer architecture.** Layer 1 = user-facing axes (this canonical spec's scope). Layer 2 = always-on POLICY (5 policies enumerated; operational specs deferred to separate inquiries). Layer 3 = SOURCE-DESCRIPTION (auto-detected source properties; schema deferred). Layer 4 = SYSTEM-FLAGS (pipeline-internal knobs; out of Layer-1 scope).

- **9 architectural patterns documented in Patterns Compendium.** composite-axis (A1); categorical (A4); asymmetric ordinal (A5 — no `heavily-domesticated` level; policy embedded structurally); explicit-zero level (A6 `off`, A7 `off`, A8 `none`); dual-tier default (A8 unique); content-type-by-level table (A8); action-permission table (A7); harmony report apparatus channel (A6 Levels 3+); multi-meaning three-layer treatment (policy invariant + A7 render + A8 analysis).

- **Per-axis full prose** preserved (self-contained dense): each axis has concept + user-question + pattern + cardinality + level enum + per-level definitions (4-component template) + cross-axis boundaries + default chain + receptive-only applicability + handling action vocabulary.

- **4 cross-axis matrices produced**: (a) 40-cell per-purpose × per-axis default matrix with refinement notes applied inline (canonical spec internally consistent); (b) 28-pair cross-axis orthogonality verification matrix with 4 relation types (orthogonal / gated / orthogonal-with-modulation / drives-default); (c) 3-channel apparatus separation table (text-surface owned by A7; harmony-report owned by A6; separate-sections owned by A8); (d) action-vocabulary 4-role map (own actions / modulates / produces / drives-default).

- **5 × 8 = 40-cell policy interaction map** — for each of 5 always-on policies (multi-meaning preservation; register-alternation preservation; polysemy-via-local-construction; nazm preservation; no-smoothing) across 8 axes, the cell labels the policy-axis interaction (invariant / activation gate at level X / renders preserved senses per axis level / analyzes preserved senses at high level / drives policy emphasis / modulates / not applicable).

- **Receptive-only applicability compendium**: APPLIES to A1 (5 sub-fields), A2, A3 (Reader-family axes); NOT APPLICABLE to A4, A5, A6, A7, A8 (translator-strategy axes — user-configuration, not reader-property).

- **Default-derivation chains**: A1/A2/A3 use conservative-bias-LOWER per axis; A4 defaults to `casual` when silent; A5/A6/A7 chain through A4 matrix; A8 is dual-tier (A4 chain when A4 set; conservative-bias `standard` when A4 silent — A8 unique among translator-strategy axes).

- **Pydantic dataclass structure HINT** provided in pydantic-like syntax (not actual code; implementation specifics — validators, base-class, serializers — deferred to downstream schema-commit inquiry).

- **Said Nursi corpus per-axis mapping** included as concrete operational anchor; canonical spec stays language-agnostic at concept level + corpus-illustrated at example level.

- **Carry-forward maintenance bundle**: TWO Next Actions MUST items consolidate accumulated refinement notes — (1) A4 finding maintenance pass with 4-5 refinements (A5/A6/A7/A8 label alignments); (2) `.env.example` DEPTH_PROFILE refinement (add `none` at position 1).

- **Downstream-unblock list**: schema commit (MUST after this finding); Layer 1A UX preset catalog (COULD; future UX inquiry); 5 Layer 2 POLICY operational specs (COULD; per-policy inquiries); Layer 3 SOURCE-DESCRIPTION schema (COULD); UX-layer runtime conflict surface (COULD); per-target-language refinements (DEFERRED).

- **23 inherited commitments re-tested** at synthesis level across all 9 priors; no silent inheritance.

- **Versioned v1.0** with inline Changelog; increment rules documented for future revisions.

## Finding

### 1. Framework Overview

#### 1.1 The 4-layer architecture

Comprehenslate's configuration framework has 4 layers:

- **Layer 1 — USER-FACING AXES.** The user's configuration knobs per translation job. 8 axes organized into 4 families. **This canonical spec's scope.**
- **Layer 2 — POLICY.** 5 always-on rules grounded in project values. The user does NOT configure these (opt-out would contradict project identity). Operational specs deferred to separate POLICY-layer inquiries.
- **Layer 3 — SOURCE-DESCRIPTION.** Auto-detected source-text properties (genre, era, register profile, source culture, source language) with optional user override. Schema deferred to separate SOURCE-DESCRIPTION inquiry.
- **Layer 4 — SYSTEM-FLAGS.** Pipeline-internal knobs (chunking strategy, parallel mode, output format, indexing). Not translation-content choices. Out of this canonical spec's scope.

#### 1.2 The 4-family organization

Layer 1's 8 axes are organized into 4 families. **Families are navigational labels for documentation, not configuration units.** The configuration unit is the axis. A user picks an axis-value, not a family.

| Family | Axes | About |
|---|---|---|
| Reader | A1 Reader Level, A2 Domain Expertise, A3 Source Culture | properties of the intended reader |
| Purpose | A4 Purpose | what the translation is for |
| Strategy | A5 Source Fidelity, A6 Form Preservation, A7 Scaffolding | how the translator handles source-target distance |
| Depth | A8 Analysis Depth | how much interpretive material the system surfaces |

#### 1.3 The 8 axes (inventory)

- **A1 — Reader Level** (composite-axis with 5 sub-fields; each sub-field at 5 levels)
- **A2 — Domain Expertise** (plain-ordinal; 5 levels)
- **A3 — Source Culture** (plain-ordinal; 5 levels)
- **A4 — Purpose** (categorical; 5 categories)
- **A5 — Source Fidelity** (plain-ordinal asymmetric; 4 levels with policy embedded structurally)
- **A6 — Form Preservation** (plain-ordinal; 5 levels tied to `harmony_layer.md` Tier 1-4)
- **A7 — Scaffolding** (plain-ordinal; 5 levels)
- **A8 — Analysis Depth** (plain-ordinal; 5 levels with explicit `none`)

#### 1.4 Framework closure status

- **FRAMEWORK CLOSED at 8/8 axes specified.** Reader 3/3 + Purpose 1/1 + Strategy 3/3 + Depth 1/1 = 8 axes complete.
- **5 always-on policies enumerated** in Layer 2 (operational specs deferred).
- **What's next** (after this canonical spec): schema commit (pydantic dataclass); Layer 1A UX preset catalog; Layer 2 policy operational specs; Layer 3 SOURCE-DESCRIPTION schema; UX-layer runtime conflict surface.

### 2. Patterns Compendium

The framework uses 9 architectural patterns that emerged across the per-axis findings. Naming these patterns enables future axes (or framework extensions) to reference them.

#### 2.1 composite-axis pattern (A1)

When an axis bundles multiple sub-dimensions that are empirically correlated in typical users (joint distribution is clustered) AND genuinely orthogonal in principle (individual override matters for edge cases), use the composite-axis pattern: one HEADLINE level the user sets + per-sub-field defaults derived from the headline + optional per-sub-field overrides.

A1 Reader Level is the canonical instance. The 5 sub-fields (vocabulary-breadth, syntactic-processing-capacity, idiom-recognition, inference-capacity, cultural-reference-recognition) share the same labels (`very_basic | daily | conversational | advanced | native`) so a single user-level configuration propagates across all 5 sub-fields unless explicitly overridden.

#### 2.2 categorical pattern (A4)

When axis values are qualitatively distinct uses rather than points on an intensity scale, use a categorical (non-ordinal) pattern. A4 Purpose is the canonical instance — 5 categories (`scholarly | devotional | casual | language-learning | performance`) that don't lie on a single intensity scale.

Three independent tests confirm categorical: semantic (the user-question "what is this translation FOR?" asks for a category not a degree); lexical ("more scholarly than devotional" doesn't make sense); orthogonality (a scholar can want a CASUAL-feel translation; a casual reader can want DEEP analysis — purposes don't lie on a single scale).

#### 2.3 asymmetric ordinal pattern (A5)

When a cross-cutting policy constrains the user-configurable range of an ordinal axis, use an asymmetric ordinal with the policy embedded structurally. A5 Source Fidelity is the canonical instance — 4 levels `foreignized-max | foreignized | balanced | lightly-domesticated` with NO `heavily-domesticated` level. The DOMESTICATE-disfavored cross-cutting policy is structurally embedded by the absence of `heavily-domesticated` — the user cannot silently opt out by choosing that level because it doesn't exist as a user-facing option. Per-corpus policy override (for atypical corpora like children's adaptations) is deferred to a future audience-level inquiry.

#### 2.4 explicit-zero level pattern (A6, A7, A8)

Every ordinal Strategy / Depth axis has an explicit-zero level for the "no feature" case (A6 `off`, A7 `off`, A8 `none`). The pattern preserves operational distinction between "zero feature" and "minimal feature" cases. Without it, A4 matrix performance default `surface` (for A8) and casual default `surface` would produce identical output despite operationally different intents (performance wants ZERO apparatus; casual wants minimal-nonzero apparatus).

#### 2.5 dual-tier default pattern (A8)

When an axis's A4 chain default is operationally sparse at cold-start (e.g., A8's A4 chain casual default `surface` is near-empty), use a dual-tier default: A4 chain when A4 is set; conservative-bias fallback when A4 is also silent. A8 is the canonical instance — A4 set + A8 silent → A4 matrix value; A4 silent + A8 silent → A8 = `standard` (conservative-bias-fallback midpoint).

This is the only multi-tier default chain among the translator-strategy axes (A5/A6/A7 use single-tier A4 chain; A8 needs dual-tier because A4's casual default for A8 is uniquely sparse).

#### 2.6 content-type-by-level table pattern (A8)

When an axis produces content directly (not gating or modulating other axes' actions), use a content-type-by-level table as its operational substance. A8 Analysis Depth is the canonical instance — 12 content-types × 5 levels = 60-cell table. The structural distinction: A7 has an action-permission table (gates A1/A3 actions); A8 has a content-type-by-level table (produces 12 content-types directly).

#### 2.7 action-permission table pattern (A7)

When an axis's role is to gate other axes' action vocabularies via a budget mechanism, use an action-permission table. A7 Scaffolding is the canonical instance — the scaffolding budget gates A1 cultural-reference-recognition's INLINE-GLOSS/FOOTNOTE actions and A3 source-culture's TRANSLITERATE-WITH-GLOSS/FLAG-CULTURAL-CONTEXT/BRIDGE-CULTURAL-DISTANCE actions. At A7=off, all budget-consuming actions are BLOCKED.

#### 2.8 harmony report apparatus channel pattern (A6 Levels 3+)

When an axis produces meta-analytic commentary distinct from text-surface scaffolding AND distinct from separate-sections analysis, use a harmony report apparatus channel. A6 Form Preservation is the canonical instance — at A6 Levels 3+ (`light`, `standard`, `maximum`), the AI produces a harmony report documenting which `harmony_layer.md` tiers were preserved and what was sacrificed at the harmony level. The harmony report lives in its own apparatus channel distinct from A7's text-surface (footnotes/glosses on reading page) and A8's separate-sections (introduction/endnotes/appendix). At A8 deep+ and A6 Levels 3+, cross-references between channels are added.

#### 2.9 multi-meaning three-layer treatment (Policy + A7 + A8)

When an always-on policy preserves a property AND a user-facing axis controls HOW the property appears AND another user-facing axis controls HOW the property is analyzed in apparatus, use a three-layer treatment. Multi-meaning preservation is the canonical instance:

- **Policy invariant** (Layer 2): the polysemy policy preserves both senses when the local construction permits multiple simultaneously-valid readings.
- **A7 controls HOW rendered in translation** (Layer 1, text-surface): footnote / parenthetical / inline-paired / apparatus-edition render per A7 level + EXPLICATE-FUNCTION fallback at A7=off.
- **A8 controls HOW analyzed in separate sections at high A8 levels** (Layer 1, separate-sections): exegetical-history paragraph at A8=`deep`; full exegetical-history apparatus at A8=`scholarly`.

### 3. Per-Axis Sections

This section reproduces full operationalizable per-level prose for each axis. Each axis subsection includes: Concept + User-question + Pattern + Cardinality + Level enum + Per-level prose + Cross-axis boundaries + Default chain + Receptive-only applicability + Handling action vocabulary + Said Nursi corpus mapping.

#### 3.1 A1 — Reader Level (composite-axis with 5 sub-fields)

**Concept.** The reader's overall ability to receive the translation. The broadest reader-facing axis.

**User question.** "How fluent is the reader of this translation?"

**Pattern.** composite-axis. Headline level + 5 sub-fields with same-labels-for-default-propagation + optional per-sub-field overrides.

**Cardinality.** 5 headline levels; each of 5 sub-fields also at 5 levels (same labels).

**Level enum.** `very_basic | daily | conversational | advanced | native`

**Sub-fields.**

1. **vocabulary-breadth** — passive vocabulary recognition depth.
2. **syntactic-processing-capacity** — ability to parse complex sentence structures.
3. **idiom-recognition** — figurative-expression recognition.
4. **inference-capacity** — ability to fill in implicit information / compressed argument.
5. **cultural-reference-recognition** — ability to recognize cultural allusions and named entities within a presumed-target canon.

**Per-level prose (cultural-reference-recognition sub-field — the canonical level definitions).** Each level uses the 4-component MEDIUM-to-LIGHT adapted template: reader profile + canonicity-tier + register/canon-tier + cultural-reference-handling test.

- **`very_basic`** — recognizes ubiquitous-canon ONLY, unreliably. AI: aggressive INLINE-GLOSS for ubiquitous references; EXPLICATE-FUNCTION for educated-mainstream; FOOTNOTE for higher tiers; KEEP-AS-IS only for transparent + ubiquitous; DOMESTICATE as last resort.
- **`daily`** — ubiquitous (reliably) + first slice of educated-mainstream (Big Brother, Catch-22, Kafkaesque). AI: KEEP-AS-IS for ubiquitous + journalistic educated-mainstream; INLINE-GLOSS for deeper educated-mainstream (Pyrrhic victory, Sword of Damocles); EXPLICATE-FUNCTION for literary-educated and above.
- **`conversational`** — full educated-mainstream (high-school-educated canonical set). AI: KEEP-AS-IS for ubiquitous + educated-mainstream; INLINE-GLOSS for literary-educated when invoked but not placeable.
- **`advanced`** — + literary-educated (humanities-undergraduate-equivalent). AI: KEEP-AS-IS as default through literary-educated; INLINE-GLOSS only for specialist-canonical exceeding tier; FOOTNOTE for true scholar-canonical.
- **`native`** — all 5 tiers including specialist + scholar-canonical. AI: KEEP-AS-IS for everything; the reader catches references silently.

**Cross-axis boundaries.** A1↔A2: general fluency vs domain-specialist knowledge; same word can fire both (e.g., `ratiocination` fires A1 vocabulary-breadth; `isnād` fires A2 technical-vocabulary). Four-corners independence: non-native ESL Bible scholar (A1=very_basic + A2=expert); native English with no Islamic-theology (A1=native + A2=lay). A1↔A3: competence-based (A1's cultural-reference-recognition) vs identity-based (A3); four-corners independence (well-read insider; poorly-read insider; well-read outsider; uninitiated outsider).

**Default chain.** Conservative-bias-LOWER per sub-field; headline propagates to sub-field defaults; overrides supersede.

**Receptive-only.** APPLIES (reader RECOGNIZES content; doesn't produce).

**Handling action vocabulary.** Per sub-field. cultural-reference-recognition: 5 actions (KEEP-AS-IS / INLINE-GLOSS / EXPLICATE-FUNCTION / FOOTNOTE / DOMESTICATE — last resort per project DOMESTICATE-disfavored policy). Other sub-fields have own action vocabularies per per-axis findings.

**Triple-overlap union rule.** When a reference fires multiple sub-fields, AI applies the union of per-sub-field handling rules; more-explicating action wins.

**Said Nursi corpus mapping.** Typically `daily` or `conversational` cultural-reference-recognition for general curious Western reader; `very_basic` for non-Quran-familiar outsider; `native` for born-Muslim with formal Risale-i Nur study.

#### 3.2 A2 — Domain Expertise (plain-ordinal)

**Concept.** The reader's specialist knowledge in the source's subject domain (Islamic theology, biblical scholarship, theoretical physics, etc.) — independent of general reading fluency.

**User question.** "How much does the reader already know about the subject matter?"

**Pattern.** Plain-ordinal (no sub-fields).

**Cardinality.** 5 levels (root proposed 3; user directed 5; anchored in Dreyfus 5-stage skill-acquisition model).

**Level enum.** `lay | aware | educated | trained | expert`

**Per-level prose.** Each level uses the 4-component MEDIUM-adapted template: reader profile + expertise-depth-tier + discourse-register-tier + domain-handling-test.

- **`lay`** — no domain background. Recognizes domain's existence only. AI vocabulary-level: PARAPHRASE-IN-LAYMAN-TERMS for any non-ubiquitous technical term. AI discourse-level: AVOID-SPECIALIST-DEBATES; UNATTRIBUTED-CONSENSUS for mainstream views.
- **`aware`** — cultural-general exposure (mass-media + popular books). Catches major figures + major concepts at journalistic depth. AI: PARAPHRASE for specialist terms; INLINE-DEFINE-ON-FIRST-USE for popular-book-level; KEEP-SOURCE-TERM-WITH-GLOSS for source-language terms; AVOID-SPECIALIST-DEBATES.
- **`educated`** — general-amateur reading; undergraduate-survey-equivalent. AI: USE-TECHNICAL-VOCABULARY-FREELY for mainstream terms; INLINE-DEFINE-ON-FIRST-USE for specialist terms; UNATTRIBUTED-CONSENSUS as primary mode; ATTRIBUTE-VIEW-TO-SCHOOL when essential.
- **`trained`** — formal study or sustained professional engagement (graduate-level coursework; working professional in field). AI: USE-FREELY for most terms; INLINE-DEFINE only for truly specialist sub-field terms; ATTRIBUTE-VIEW-TO-SCHOOL as primary mode; INVOKE-SPECIALIST-DEBATES at edges.
- **`expert`** — specialist scholar (graduate-doctorate-equivalent). AI: USE-FREELY across the board; KEEP-SOURCE-TERM-WITH-GLOSS or KEEP-AS-IS for source-language load-bearing terms; INVOKE-SPECIALIST-DEBATES as primary mode.

**Cross-axis boundaries.** A2↔A1 (same-word-fires-both); A2↔A3 (competence-based vs identity-based; four-corners); A2↔A4 (expertise vs purpose; specialist can read for casual purpose).

**Default chain.** Conservative-bias-LOWER; default `lay`.

**Receptive-only.** APPLIES.

**Handling action vocabulary.** 9 actions in 2 categories + 1 bridge:
- *Vocabulary-level (4):* USE-TECHNICAL-VOCABULARY-FREELY / INLINE-DEFINE-ON-FIRST-USE / FOOTNOTE-TECHNICAL-TERM / PARAPHRASE-IN-LAYMAN-TERMS.
- *Discourse-level (4):* INVOKE-SPECIALIST-DEBATES / ATTRIBUTE-VIEW-TO-SCHOOL / UNATTRIBUTED-CONSENSUS / AVOID-SPECIALIST-DEBATES.
- *Bridge (1):* KEEP-SOURCE-TERM-WITH-GLOSS.

**Single-domain default.** A2 applies to source's domain (one domain per translation job; source's domain implicit via Layer 3 SOURCE-DESCRIPTION). Multi-domain reader configuration deferred to future audience-level inquiry.

**Said Nursi corpus mapping.** Typically `aware` or `educated` for general curious reader; `lay` for non-Muslim non-religious-studies reader; `expert` for Islamic-studies professor; `trained` for working imam / Islamic-studies graduate student.

#### 3.3 A3 — Source Culture (plain-ordinal)

**Concept.** The reader's IDENTITY-BASED proximity to the source's cultural milieu.

**User question.** "Does this reader come from inside the source's culture, or from outside?"

**Pattern.** Plain-ordinal (no sub-fields).

**Cardinality.** 5 levels (root proposed 3; refined to 5 on substantive grounds — diaspora gradient produces operationally-different AI handling at each step; anchored in Brah diaspora studies + Rambo/Jackson religious-insider sociology).

**Level enum.** `outsider | acquainted | familiar | heritage | source-native`

**Composite-with-primary-axis identity dimension.** Lived cultural-fluency aggregates residential + linguistic + practice + religious/ideological + heritage markers. For religious-text sources (Said Nursi corpus; Bible; Quran) religious identity weights more; for secular sources residential/linguistic weights more.

**Per-level prose.** Each level uses the 4-component MEDIUM-adapted template: reader profile + cultural-proximity-tier + cultural-context-tier + cultural-handling-test.

- **`outsider`** — no cultural ties; identity firmly target. AI proper-noun: TRANSLITERATE-WITH-GLOSS for source-language proper names. AI cultural-context: BRIDGE-CULTURAL-DISTANCE for source-cultural assumptions. AI honorific: KEEP-HONORIFICS-SOURCE with first-use gloss. AI strategic: PRESERVE-CULTURAL-SPECIFICITY (foreignization-preserving).
- **`acquainted`** — some exposure (cultural-tourist; religion-survey course; popular-book reading); identity-shift without immersion. AI: TRANSLITERATE-WITH-GLOSS first use then bare; FLAG-CULTURAL-CONTEXT briefly; KEEP-HONORIFICS-SOURCE with first-use gloss.
- **`familiar`** — sustained immersion without inherited identity (long-term convert; 30-year scholar-resident; non-converting spouse with 20+ years residence). AI: TRANSLITERATE-FULLY for major source-language terms; ASSUME-SHARED-KNOWLEDGE for major cultural anchors; FLAG-CONTEXT for inner-layer references; KEEP-HONORIFICS-SOURCE without gloss for major honorifics.
- **`heritage`** — identity inherited but diluted (2nd-generation diaspora; bicultural target-primary; raised in mixed household). AI: TRANSLITERATE-FULLY for major heritage-known; TRANSLITERATE-WITH-GLOSS for inner-layer; ASSUME-SHARED-KNOWLEDGE for major; FLAG-CONTEXT for specialist inner-layer.
- **`source-native`** — born and raised in source culture; primary identity source (includes 1st-generation immigrants who emigrated as adults; primary identity still source). AI: TRANSLITERATE-FULLY everything; ASSUME-SHARED-CULTURAL-KNOWLEDGE; KEEP-HONORIFICS-SOURCE; PRESERVE-CULTURAL-SPECIFICITY at maximum.

**Cross-axis boundaries.** A3↔A1 (identity vs competence; four-corners); A3↔A2 (cultural identity vs domain expertise; four-corners); A3↔A4 (WHO vs WHY); A3↔A5 (reader-side vs translation-strategy-side).

**Default chain.** Conservative-bias-LOWER (assumes OUTSIDER); default `outsider`.

**Receptive-only.** APPLIES.

**Handling action vocabulary.** 10 actions in 4 categories:
- *Proper-noun (3):* TRANSLITERATE-FULLY / TRANSLITERATE-WITH-GLOSS / TARGET-LANGUAGE-EQUIVALENT.
- *Cultural-context (3):* ASSUME-SHARED-CULTURAL-KNOWLEDGE / FLAG-CULTURAL-CONTEXT / BRIDGE-CULTURAL-DISTANCE.
- *Honorific (2):* KEEP-HONORIFICS-SOURCE / ANGLICIZE-HONORIFICS (DISFAVORED per project policy).
- *Strategic (2):* PRESERVE-CULTURAL-SPECIFICITY / DOMESTICATE-CULTURAL-FRAME (DISFAVORED per project policy).

**Layered-source-culture note.** Said Nursi corpus's source culture is layered (Muslim broad + Turkish mid + Naqshbandi-Khalidi-Sufi innermost). A3 captures proximity to the PRIMARY (innermost) layer; AI handles within-layer variation at runtime.

**Said Nursi corpus mapping.** Typically `outsider` for general Western reader; `acquainted` for Western with general world-religions exposure; `familiar` for long-term Western convert + residence; `heritage` for 2nd-generation Turkish-American without active practice; `source-native` for born-and-raised Turkish-Muslim from Naqshbandi-Khalidi-leaning community.

#### 3.4 A4 — Purpose (categorical)

**Concept.** What the translation is FOR — the use-case.

**User question.** "Why is this translation being made? What will the reader do with it?"

**Pattern.** Categorical (the only categorical axis in the framework). Levels are qualitatively distinct use-cases; not points on an intensity scale.

**Cardinality.** 5 categories.

**Level enum.** `scholarly | devotional | casual | language-learning | performance`

**Special role.** **A4 drives DEFAULTS for the other 7 axes** via the per-purpose × per-axis matrix (Section 4.1).

**Per-category prose.** Each category uses the NEW 4-component categorical template: use-case profile + strategic implications + per-axis default mappings + DOMESTICATE-policy emphasis.

- **`scholarly`** — reader STUDIES the translation (analyzes structure, cites passages, prepares academic work). Source-fidelity paramount; footnoting expected. DOMESTICATE-policy emphasis: HIGH foreignization. Per-axis defaults: A1 advanced; A2 educated; A5 foreignized; A6 standard; A7 rich; A8 deep.
- **`devotional`** — reader READS for spiritual practice (meditates, memorizes, recites, reflects). Liturgical form sacred. DOMESTICATE-policy emphasis: MAXIMUM foreignization. Per-axis defaults: A1 conversational; A2 aware-to-educated; A3 source-native/heritage; A5 foreignized-max; A6 standard; A7 standard; A8 standard.
- **`casual`** — reader READS for general comprehension (curiosity, light reading, getting the gist). Balance source-fidelity with accessibility. DOMESTICATE-policy emphasis: BALANCED (foreignization-preserving alternatives over DOMESTICATE). Per-axis defaults: A1 daily; A2 lay-to-aware; A3 outsider-to-acquainted; A5 balanced; A6 light; A7 rich; A8 surface.
- **`language-learning`** — reader LEARNS the source language through the translation. Maximum transparency to source structure. DOMESTICATE-policy emphasis: HIGH foreignization. Per-axis defaults: A1 conversational; A2 lay; A3 outsider; A5 foreignized; A6 standard; A7 scholarly; A8 scholarly.
- **`performance`** — reader DELIVERS the translation orally (recitation, theatrical, sermon). Maximum cadence preservation. DOMESTICATE-policy emphasis: BALANCED. Per-axis defaults: A1 conversational; A5 balanced; A6 maximum; A7 minimal; A8 surface (or `none` for pure oral).

**Cross-axis boundaries.** A4↔A2 (WHY vs HOW MUCH KNOWN); A4↔A3 (WHY vs WHO); A4↔A8 (A4 sets DEFAULT for A8 but doesn't subsume; scholar can want low A8; casual can want high A8).

**Single-purpose default + override path.** A4 is single-valued. Real multi-purpose cases (scholarly + devotional academic-spiritual-formation) handled by manual per-axis override (scholar sets A4=devotional + overrides A8=deep). Multi-purpose configuration as list deferred to future inquiry.

**Default-when-A4-silent.** `casual` (categorical equivalent of conservative-bias-LOWER).

**Receptive-only.** NOT APPLICABLE (A4 is user-configuration choice; not reader-property).

**Handling action vocabulary.** None of own; drives defaults for other axes via matrix.

**Said Nursi corpus mapping.** All 5 purposes are valid Nursi use cases; project's primary corpus accommodates all 5.

#### 3.5 A5 — Source Fidelity (asymmetric ordinal)

**Concept.** The translator's strategic stance on the foreignization↔domestication spectrum (Venuti framework). Controls lexical/idiomatic SURFACE choices.

**User question.** "Should the translation sound like a translation, or read as if originally written in the target language?"

**Pattern.** Plain-ordinal but ASYMMETRIC (policy embedded structurally; no `heavily-domesticated` level).

**Cardinality.** 4 levels (root proposed 3 symmetric; refined to 4 asymmetric on substantive grounds — policy constraint + A4-matrix-implied granularity + user-need spectrum).

**Level enum.** `foreignized-max | foreignized | balanced | lightly-domesticated`

**Why no `heavily-domesticated`.** DOMESTICATE-disfavored cross-cutting policy from A1 chain + A3 + A4 is structurally embedded by the absence of `heavily-domesticated` — the user cannot silently opt out by choosing that level. Per-corpus policy override (for atypical corpora) deferred to future audience-level inquiry.

**Per-level prose.** Each level uses the NEW translator-strategy 4-component template: strategic stance + per-stance handling-action bias + foreignization-preservation emphasis + cross-axis interaction.

- **`foreignized-max`** — Maximum source-fidelity. Preserve everything source-cultural. A1: KEEP-AS-IS prioritized; EXPLICATE-FUNCTION for opaque load-bearing. A3: TRANSLITERATE-FULLY; KEEP-HONORIFICS-SOURCE; PRESERVE-CULTURAL-SPECIFICITY max. A4 match: `devotional` (matrix).
- **`foreignized`** — Strong source-fidelity with light support. A1: INLINE-GLOSS for moderate-difficulty; EXPLICATE-FUNCTION for opaque-with-explanation. A3: TRANSLITERATE-FULLY for established; KEEP-HONORIFICS-SOURCE; FLAG-CULTURAL-CONTEXT briefly. A4 match: `scholarly` and `language-learning` (matrix).
- **`balanced`** — Balance source-fidelity with accessibility. A1: INLINE-GLOSS primary; EXPLICATE-FUNCTION for compressed-meaning. A3: TRANSLITERATE-WITH-GLOSS primary; FLAG-CULTURAL-CONTEXT; KEEP-HONORIFICS-SOURCE for established. A4 match: `casual` and `performance` (matrix).
- **`lightly-domesticated`** — Light target-naturalization where source-cultural specificity isn't load-bearing. A1: INLINE-GLOSS still preferred for load-bearing; DOMESTICATE permissible in narrow cases. A3: TARGET-LANGUAGE-EQUIVALENT permissible in narrow cases. A4 match: no purpose defaults here (user override).

**Cross-axis boundaries.** A5↔A6 orthogonal (lexical surface vs structural form; four-corners); A5↔A1 (strategy vs per-reference tactics — A5 modulates which A1 actions fire).

**A5 has NO own actions.** A5 is a STRATEGIC STANCE that MODULATES which A1 and A3 actions fire (sets preference order over the existing vocabularies). A5 → A1 action modulation table + A5 → A3 action modulation table per per-axis finding.

**Default chain.** Via A4 matrix. A4 silent → casual → A5 = `balanced`.

**Receptive-only.** NOT APPLICABLE.

**Said Nursi corpus mapping.** Typically `foreignized` for scholarly + language-learning Nursi; `foreignized-max` for devotional liturgical use; `balanced` for casual + performance.

#### 3.6 A6 — Form Preservation (plain-ordinal; tied to harmony_layer)

**Concept.** The strength of structural preservation — rhythm, parallelism, ring composition, word order as meaning carrier (nazm). Ties to `harmony_layer.md` Tier 1-4 system.

**User question.** "Should structural elements like rhythm and parallelism survive the crossing into the target language?"

**Pattern.** Plain-ordinal. Direct tie to harmony_layer.md (49 entries; 3-Pass Meaning Lock → Harmony Map → Target Reconstruction methodology).

**Cardinality.** 5 levels.

**Level enum.** `off | minimal | light | standard | maximum`

**Per-level tier-coverage** (the operational substance):

| A6 Level | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Nazm Policy |
|---|---|---|---|---|---|
| `off` | — | — | — | — | OFF |
| `minimal` | ✓ | — | — | — | OFF |
| `light` | ✓ | ✓ | — | — | **ACTIVE — activation gate** |
| `standard` | ✓ | ✓ | ✓ (per PRESERVE-WHEN) | — | ACTIVE |
| `maximum` | ✓ | ✓ | ✓ (per PRESERVE-WHEN) | ✓ (where target permits) | ACTIVE |

**Activation gate at Level 3 `light`.** When A6 ≥ `light`, the always-on nazm-as-meaning policy ACTIVATES and the full 3-Pass methodology fires.

**Tier 3 conditional logic INVARIANT across Levels 4-5.** harmony_layer.md's PRESERVE-WHEN/SACRIFICE-WHEN clauses are the system's adjudication mechanism. Level 5 ADDS Tier 4 ON TOP of Tier 3 conditional handling; doesn't override.

**Tier 4 language-feasibility caveat at Level 5.** Attempt where target permits; harmony report acknowledges sacrifices when target language structurally cannot support feature (e.g., Semitic root echo to non-Semitic target).

**Per-level prose.** Each level uses the A6-adapted 4-component template: strategic stance + tier-coverage + nazm-policy-activation marker + cross-axis interaction.

- **`off`** — no harmony work; Pass 1 (Meaning Lock) only. Semantic-fidelity output. Said Nursi: rare utility/draft use.
- **`minimal`** — Tier 1 (Non-Negotiable) preservation only. Cause-effect chains, hidden syllogisms, conditional chains preserved. Said Nursi: istilzam chain preservation when no other harmony work performed.
- **`light`** — Tier 1 + Tier 2. Full 3-Pass methodology fires; nazm policy ACTIVE. A4 default for `casual`.
- **`standard`** — Tier 1 + Tier 2 + Tier 3 conditional. AI examines source at runtime per Tier 3 entry's PRESERVE-WHEN/SACRIFICE-WHEN clauses. A4 default for `scholarly`/`devotional`/`language-learning`.
- **`maximum`** — All 4 tiers. Tier 3 respecting conditional; Tier 4 attempted where target permits. A4 default for `performance` (rhythm = meaning).

**A6 produces HARMONY REPORT at Levels 3+.** Separate apparatus channel from text-surface (A7) and separate-sections (A8). Documents which tiers were preserved + what was sacrificed at the harmony level.

**Cross-axis boundaries.** A6↔A5 orthogonal (lexical surface vs structural form; four-corners); A6↔A7 orthogonal (harmony-report channel vs text-surface channel); A6↔A8 orthogonal with cross-references at A8 deep+.

**Default chain.** Via A4 matrix. A4 silent → casual → A6 = `light` (activation gate; project defaults to nazm-policy-active).

**Receptive-only.** NOT APPLICABLE.

**Said Nursi corpus mapping.** Typically `standard` (Tier 1+2+3 conditional) for scholarly/devotional Nursi; `maximum` for performance/recitation; `light` for casual.

#### 3.7 A7 — Scaffolding (plain-ordinal)

**Concept.** How much explanatory material accompanies the translation at the text surface — footnotes, parenthetical glosses, transliterations, brief in-line explanations.

**User question.** "How much help does the reader need at the surface of the translation?"

**Pattern.** Plain-ordinal. Subsumes feature-activation bundle MINUS harmony (which became A6).

**Cardinality.** 5 levels.

**Level enum.** `off | minimal | standard | rich | scholarly`

**TWO special characteristics:** (1) A7 is the **scaffolding budget** that gates A1/A3 budget-consuming actions; (2) A7 controls **multi-meaning render** when polysemy policy fires.

**Per-level prose.** Each level uses the A7-adapted 4-component template: scaffolding stance + per-level budget + A1/A3 action permission + cross-axis interaction.

- **`off`** — No text-surface scaffolding. Clean target-language prose only. STRICTLY BLOCKS: INLINE-GLOSS / FOOTNOTE / TRANSLITERATE-WITH-GLOSS / FLAG-CULTURAL-CONTEXT / BRIDGE-CULTURAL-DISTANCE. Available: budget-FREE actions (KEEP-AS-IS / EXPLICATE-FUNCTION / DOMESTICATE-disfavored / TRANSLITERATE-FULLY / etc.). Multi-meaning render: EXPLICATE-FUNCTION fallback (paraphrase combining senses; preserves polysemy POLICY without scaffolding). A4 default: `performance` (oral recitation).
- **`minimal`** — Sparse text-surface scaffolding for hardest references. 0-1 footnotes/page. INLINE-GLOSS sparingly (1-2/page for hardest); FOOTNOTE rare; TRANSLITERATE-WITH-GLOSS first-use only. Multi-meaning render: PRIMARY + MINIMAL FOOTNOTE noting other senses. A4 default: none (edge cases).
- **`standard`** — Moderate text-surface scaffolding. 1-3 footnotes/page; routine inline glosses; routine cultural-context flags. Multi-meaning render: INLINE PARENTHETICAL PAIRED. A4 default: `devotional`.
- **`rich`** — Extensive text-surface scaffolding (Norton-Critical-style). 3-6 footnotes/page; extensive inline glosses; appendix-light. Multi-meaning render: INLINE PAIRED WITHOUT BRACKETS or FULL FOOTNOTE PAIRED. A4 default: `scholarly` AND `casual` (matrix). Also chain default when A7 silent.
- **`scholarly`** — Full text-surface scaffolding apparatus. 6+ footnotes/page; full apparatus + introduction + glossary + endnotes. Multi-meaning render: APPARATUS-EDITION RENDER. A4 default: `language-learning`.

**Runtime conflict resolution.** When A7 too low for required A1/A3 actions: (1) STRICT budget enforcement; (2) FALLBACK to budget-FREE actions; (3) FLAG in harmony report at A6 Levels 3+.

**Multi-meaning render rules table** (per level):
| A7 Level | Render mechanism |
|---|---|
| `off` | EXPLICATE-FUNCTION fallback (6th case) |
| `minimal` | PRIMARY + MINIMAL FOOTNOTE |
| `standard` | INLINE PARENTHETICAL PAIRED |
| `rich` | INLINE PAIRED WITHOUT BRACKETS or FULL FOOTNOTE PAIRED |
| `scholarly` | APPARATUS-EDITION RENDER |

**Cross-axis boundaries.** A7↔A6 orthogonal (text-surface vs harmony-report channels); A7↔A8 orthogonal (3-framing rule + LOCATION default tiebreaker — see Section 3.8); A7↔A1, A7↔A3 GATED (scaffolding budget gates budget-consuming actions).

**Default chain.** Via A4 matrix. A4 silent → casual → A7 = `rich`.

**Receptive-only.** NOT APPLICABLE.

**Said Nursi corpus mapping.** Typically `rich` for casual + scholarly Nursi; `scholarly` for full apparatus edition; `standard` for devotional; `minimal` for performance.

#### 3.8 A8 — Analysis Depth (plain-ordinal)

**Concept.** How much interpretive material the system surfaces ALONGSIDE the translation in separate analysis sections — distinct from A7's text-surface scaffolding.

**User question.** "How much interpretive commentary should accompany the translation?"

**Pattern.** Plain-ordinal. Inherits DEPTH_PROFILE labels from `.env.example` with refinement (add `none` at position 1).

**Cardinality.** 5 levels (root proposed 4; refined to 5 — added `none` parallel to A6/A7=off).

**Level enum.** `none | surface | standard | deep | scholarly`

**Content-type-by-level table** (the operational substance; 12 content-types × 5 levels = 60 cells):

| Content-type | `none` | `surface` | `standard` | `deep` | `scholarly` |
|---|---|---|---|---|---|
| Introduction | — | publisher's note | brief | scholarly | comprehensive |
| Glossary | — | major terms only | major terms | extensive | exhaustive |
| Etymology | — | — | — | major terms | every key term |
| Rhetorical analysis | — | — | — | per major passage | per passage |
| Cross-references | — | — | major passages | extensive | exhaustive |
| Exegetical history | — | — | brief footnote | paragraph per major concept | full commentary tradition |
| Lexical-history | — | — | — | major terms | every key term |
| Target-language-equivalent analysis | — | — | — | major choices | every choice |
| Theological commentary | — | — | — | major concepts | extensive |
| Historical-critical context | — | — | — | per major passage | full |
| Philological apparatus | — | — | — | — | full |
| Cross-tradition references | — | — | — | — | full |

**Per-level prose.** Each level uses the A8-adapted 4-component template: analysis stance + per-level depth + content-type-by-level reference + cross-axis interaction.

- **`none`** — No separate-sections apparatus at all. Pure translation only. A4 default for `performance` (oral recitation) and casual configurations with A7=off.
- **`surface`** — Minimal apparatus. 0-2 content-types fire minimally (intro + glossary). A4 default for `casual` (and performance variant).
- **`standard`** — Moderate apparatus. 2-4 content-types fire routinely (brief intro + glossary + cross-references + brief exegetical-history). A4 default for `devotional`.
- **`deep`** — Extensive apparatus (Norton-Critical-style analysis chapter). 4-10 content-types fire. A4 default for `scholarly`.
- **`scholarly`** — Full critical apparatus edition. All 12 content-types fire. A4 default for `language-learning` (refined from A4 `deep+scholarly` ambiguous).

**A7↔A8 boundary spec (3 framings + LOCATION default tiebreaker).** The most consequential cross-axis boundary in the framework:

1. **By LOCATION:** A7 in-page (footnotes/glosses on reading page); A8 separate-sections (front matter / endnotes / appendix / sidebars).
2. **By SCOPE:** A7 per-reference; A8 per-passage / per-corpus.
3. **By AUDIENCE-INTERACTION:** A7 inline interruption; A8 deferred study session.

LOCATION is the default tiebreaker at disagreement edge cases.

**Harmony-report-location.** A6 harmony report stays in A6 channel standalone regardless of A8 level. At A8 = `deep` or `scholarly`, cross-references between channels are added (harmony report cites A8 sections; A8 sections cite harmony report).

**Multi-meaning analysis at A8.** Distinct from A7 render. A8 produces exegetical-history at high levels (paragraph at `deep`; full apparatus at `scholarly`). Three-layer treatment: policy invariant + A7 render + A8 analysis.

**Cross-axis boundaries.** A8↔A5 orthogonal (A5 stance modulates A8 content emphasis); A8↔A6 orthogonal (separate channels); A8↔A7 (3-framing rule).

**Default chain.** DUAL-TIER. A4 set + A8 silent → A4 matrix value. A4 silent + A8 silent → A8 = `standard` (conservative-bias-fallback midpoint; A8 unique among translator-strategy axes — A4 chain casual default `surface` is operationally near-empty; conservative-bias defends cold-start).

**Receptive-only.** NOT APPLICABLE.

**Said Nursi corpus mapping.** Typically `deep` for scholarly Nursi (Norton-Critical-style); `scholarly` for language-learning full apparatus; `standard` for devotional; `surface` for casual; `none` for performance oral recitation.

### 4. Cross-Axis Interaction Matrices

#### 4.1 Per-Purpose × Per-Axis Default Matrix (40 cells)

Refinement notes applied inline (canonical spec internally consistent at v1.0). The matrix supplies DEFAULTS; user can override any cell.

| Purpose | A1 (headline) | A2 | A3 | A5 | A6 | A7 | A8 |
|---|---|---|---|---|---|---|---|
| **scholarly** | advanced | educated | any (often outsider-with-study) | foreignized | standard | rich | deep |
| **devotional** | conversational | aware-to-educated | source-native / heritage | foreignized-max | standard | standard | standard |
| **casual** | daily | lay-to-aware | outsider-to-acquainted | balanced | light | rich | surface |
| **language-learning** | conversational | lay | outsider | foreignized | standard | scholarly | scholarly |
| **performance** | conversational | any | any | balanced | maximum | minimal | surface (or `none`) |

**Refinement notes applied:**
- A5 column language-learning: A4 finding's `balanced-to-foreignized` → `foreignized` (A5 4-level structure).
- A6 column: A4 finding's "moderate" → `light`; "high" → `standard`; "MAXIMUM" → `maximum`.
- A7 column: A4 finding's "moderate" → `standard`; "MAX rich" → `scholarly`; "rich (help unfamiliar)" → `rich`.
- A8 column: A4 finding's `deep+scholarly` (language-learning) → `scholarly`.

A4 finding maintenance pass (Section 11 carry-forward) propagates these refinements back to A4 finding for source-of-truth alignment.

#### 4.2 Cross-Axis Orthogonality Verification Matrix (28 pairs)

4 relation types:
- **orthogonal** — fully independent; no interaction at runtime.
- **gated** — one axis structurally constrains another's action vocabulary.
- **orthogonal-with-modulation** — one axis affects another's action selection but axes remain independent.
- **drives-default** — A4 supplies defaults for other axes via matrix.

| Pair | Relation | Rationale |
|---|---|---|
| A1↔A2 | orthogonal | general fluency vs domain-specialist knowledge |
| A1↔A3 | orthogonal | competence vs identity; four-corners |
| A1↔A4 | orthogonal | reader vs purpose |
| A1↔A5 | orthogonal-with-modulation | A5 modulates which A1 actions fire |
| A1↔A6 | orthogonal | reader-fluency vs structural-form |
| A1↔A7 | gated | A7 budget gates A1 cultural-reference-recognition's INLINE-GLOSS/FOOTNOTE/DOMESTICATE |
| A1↔A8 | orthogonal | A8 in separate channel; A1 reader-side informs content style |
| A2↔A3 | orthogonal | competence vs identity; four-corners |
| A2↔A4 | orthogonal | expertise vs purpose |
| A2↔A5 | orthogonal-with-modulation | A5 modulates A2 action density |
| A2↔A6 | orthogonal | expertise vs form |
| A2↔A7 | orthogonal-with-modulation | A7 budget affects A2 specialist-debate FOOTNOTE density |
| A2↔A8 | orthogonal | A8 content style adapts to A2 reader |
| A3↔A4 | orthogonal | identity vs purpose |
| A3↔A5 | orthogonal-with-modulation | A5 modulates which A3 actions fire |
| A3↔A6 | orthogonal | cultural identity vs structural form |
| A3↔A7 | gated | A7 budget gates A3 cultural-handling actions |
| A3↔A8 | orthogonal | A8 content style adapts to A3 reader |
| A4↔A5 | drives-default | A4 matrix supplies A5 default |
| A4↔A6 | drives-default | A4 matrix supplies A6 default |
| A4↔A7 | drives-default | A4 matrix supplies A7 default |
| A4↔A8 | drives-default | A4 matrix supplies A8 default |
| A5↔A6 | orthogonal | lexical surface vs structural form; four-corners |
| A5↔A7 | orthogonal-with-modulation | A5 affects budget-FREE foreignization-preserving fallbacks at A7=off |
| A5↔A8 | orthogonal | A5 modulates A8 content emphasis (foreignized→etymology; lightly-domesticated→target-language-equivalent justification) |
| A6↔A7 | orthogonal | harmony-report channel vs text-surface channel |
| A6↔A8 | orthogonal | harmony-report channel vs separate-sections channel; cross-references at A8 deep+ |
| A7↔A8 | orthogonal | text-surface vs separate-sections; LOCATION+SCOPE+AUDIENCE-INTERACTION 3-framing rule |

#### 4.3 3-Channel Apparatus Separation Table

| Channel | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 |
|---|---|---|---|---|---|---|---|---|
| **Text-surface** (in-page footnotes/glosses) | produces (via A7 budget) | produces (via A7 budget) | produces (via A7 budget) | drives defaults | modulates selection | does not contribute | **OWNS** | does not contribute |
| **Harmony report** (meta-analytic; A6 Levels 3+) | does not contribute | does not contribute | does not contribute | drives defaults | does not contribute | **OWNS** | flags conflicts | cross-references at deep+ |
| **Separate-sections** (front matter / endnotes / appendix) | reader-side informs content style | reader-side informs content style | reader-side informs content style | drives defaults | content emphasis modulator | cross-references at deep+ | does not contribute | **OWNS** |

**Reading:** A7 OWNS text-surface; A6 OWNS harmony-report (at Levels 3+); A8 OWNS separate-sections. Other axes contribute (produce / modulate / drive defaults / cross-reference at high level).

#### 4.4 Action-Vocabulary Map

| Axis | Action role | Vocabulary |
|---|---|---|
| A1 | OWN ACTIONS per sub-field | 5 sub-fields with own actions; cultural-reference-recognition has 5 actions (KEEP-AS-IS / INLINE-GLOSS / EXPLICATE-FUNCTION / FOOTNOTE / DOMESTICATE) |
| A2 | OWN ACTIONS | 9 actions in 2 categories + 1 bridge (USE-FREELY / INLINE-DEFINE / FOOTNOTE-TECHNICAL / PARAPHRASE; INVOKE-DEBATES / ATTRIBUTE-VIEW / UNATTRIBUTED-CONSENSUS / AVOID-DEBATES; bridge KEEP-SOURCE-TERM-WITH-GLOSS) |
| A3 | OWN ACTIONS | 10 actions in 4 categories (proper-noun 3; cultural-context 3; honorific 2; strategic 2) |
| A4 | DRIVES DEFAULTS | No own actions; per-purpose × per-axis matrix supplies defaults for other axes |
| A5 | MODULATES (no own actions) | Sets preference order over A1 + A3 action vocabularies |
| A6 | METHODOLOGY (no per-reference actions) | 3-Pass methodology (Meaning Lock → Harmony Map → Target Reconstruction) + per-tier preservation rules |
| A7 | GATES + MODULATES (no own per-reference actions) | Scaffolding budget gates A1/A3 budget-consuming actions + 5 multi-meaning render rules |
| A8 | PRODUCES CONTENT | 12 content-types (Intro / Glossary / Etymology / Rhetorical / Cross-references / Exegetical history / Lexical-history / Target-language-equivalent / Theological / Historical-critical / Philological / Cross-tradition) |

A8 is the only axis with a **content-production** role. A1/A2/A3 have **own actions**. A4 **drives defaults**. A5/A6/A7 are **modulators / methodology / gates**.

### 5. Policy Interaction Map (5 × 8 = 40 cells)

5 always-on policies (Layer 2; operational specs deferred):

1. **Multi-meaning preservation** — when source word's local construction permits multiple simultaneously-valid senses, preserve both.
2. **Register-alternation preservation** — don't lift a plain source register into ornate English; don't push elevated into casual; preserve register alternation as Tier 1/2 structure.
3. **Polysemy-via-local-construction** — local grammatical construction (case marking, agreement, plausibility) selects intended sense; not surrounding metaphor's momentum.
4. **Nazm preservation** — when A6 ≥ `light`, word order / parallelism / ring composition / structural elements treated as meaning-carriers and preserved.
5. **No-smoothing** — translating away awkward/uncomfortable nuance to make output "cleaner" is corruption; smoothing introduces worse error than awkwardness.

Policy × axis interaction:

| Policy | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 |
|---|---|---|---|---|---|---|---|---|
| Multi-meaning preservation | informs cultural-ref handling | informs technical-term ambiguity | informs cultural-religious ambiguity | drives render emphasis (devotional max) | modulates render bias | not applicable | **RENDERS preserved senses** per A7 level (5 mechanisms + EXPLICATE-FUNCTION fallback at off) | **ANALYZES preserved senses** at deep+ (exegetical history) |
| Register-alternation preservation | feeds A6 Tier 1 register-rotation | not applicable | informs cultural-register specificity | drives form emphasis | modulates lexical register | **INVARIANT at A6 Levels 3+; Tier 1/2 entry** | not applicable | not applicable |
| Polysemy-via-local-construction | informs sense selection | not applicable | informs cultural-religious sense | not applicable | not applicable | not applicable | not applicable | not applicable |
| Nazm preservation | not applicable | not applicable | informs source-cultural prosody | drives form emphasis | not applicable | **ACTIVATION GATE at Level 3 `light`; INVARIANT at Levels 3+** | not applicable | not applicable |
| No-smoothing | INVARIANT | INVARIANT | INVARIANT | INVARIANT | INVARIANT | INVARIANT | INVARIANT | INVARIANT |

**Load-bearing cells:**
- Multi-meaning × A7 (renders) and × A8 (analyzes) — three-layer treatment.
- Register-alternation × A6 (Tier 1/2 structure).
- Nazm × A6 (activation gate).
- No-smoothing × all (invariant; lesser-evil principle from `translation_principals.md`).

### 6. Receptive-only Applicability Compendium

| Axis | Receptive-only | Rationale |
|---|---|---|
| A1 | APPLIES | Reader RECOGNIZES content (vocabulary / syntactic complexity / idioms / inferences / cultural references); doesn't produce |
| A2 | APPLIES | Reader RECOGNIZES technical vocabulary + discourse-level references; doesn't produce |
| A3 | APPLIES | Reader's cultural identity determines what they bring; receptive |
| A4 | NOT APPLICABLE | A4 = user-configuration choice; not reader-property |
| A5 | NOT APPLICABLE | A5 = translator-strategy stance; not reader-property |
| A6 | NOT APPLICABLE | A6 = translator-strategy / methodology; not reader-property |
| A7 | NOT APPLICABLE | A7 = translator-strategy / scaffolding-budget; not reader-property |
| A8 | NOT APPLICABLE | A8 = translator-strategy / analysis-depth; not reader-property |

**Pattern.** Reader-family axes (A1/A2/A3) inherit receptive-only mode. Translator-strategy axes (A4-A8) are user-configuration; receptive-only DOES NOT APPLY. Future productive cases (e.g., language-learning back-translation where reader writes target → source) deferred to future inquiry.

### 7. Default-Derivation Chains

Per-axis default mechanism:

| Axis | Default mechanism | Default value when silent |
|---|---|---|
| A1 (5 sub-fields) | Conservative-bias-LOWER per sub-field; headline propagates | per-sub-field LOWER |
| A2 | Conservative-bias-LOWER | `lay` |
| A3 | Conservative-bias-LOWER (assumes OUTSIDER) | `outsider` |
| A4 | Categorical default | `casual` |
| A5 | A4 chain (matrix) | A4 silent → casual → `balanced` |
| A6 | A4 chain (matrix) | A4 silent → casual → `light` (activation gate) |
| A7 | A4 chain (matrix) | A4 silent → casual → `rich` |
| A8 | **DUAL-TIER** (A8 unique) | A4 set → matrix; A4 silent → conservative-bias `standard` |

**A8's dual-tier is unique** among translator-strategy axes. A8's A4 chain casual default `surface` is operationally near-empty (would under-defend cold-start); conservative-bias `standard` defends. A5/A6/A7's A4 chain casual defaults are operationally substantive; no need for fallback.

### 8. Pydantic Dataclass Structure HINT

This is pydantic-like syntax for structural clarity. NOT actual code. Implementation specifics (validators, base-class, serializers) deferred to downstream schema-commit inquiry.

```python
# Hint, not implementation
class A1ReaderLevel:  # composite-axis
    headline: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    vocabulary_breadth: Literal["very_basic", "daily", "conversational", "advanced", "native"] | None  # None = inherit headline
    syntactic_processing_capacity: Literal["very_basic", "daily", "conversational", "advanced", "native"] | None
    idiom_recognition: Literal["very_basic", "daily", "conversational", "advanced", "native"] | None
    inference_capacity: Literal["very_basic", "daily", "conversational", "advanced", "native"] | None
    cultural_reference_recognition: Literal["very_basic", "daily", "conversational", "advanced", "native"] | None

class Layer1Config:
    reader_level: A1ReaderLevel  # composite
    domain_expertise: Literal["lay", "aware", "educated", "trained", "expert"]
    source_culture: Literal["outsider", "acquainted", "familiar", "heritage", "source-native"]
    purpose: Literal["scholarly", "devotional", "casual", "language-learning", "performance"]
    source_fidelity: Literal["foreignized-max", "foreignized", "balanced", "lightly-domesticated"]  # 4 asymmetric
    form_preservation: Literal["off", "minimal", "light", "standard", "maximum"]
    scaffolding: Literal["off", "minimal", "standard", "rich", "scholarly"]
    analysis_depth: Literal["none", "surface", "standard", "deep", "scholarly"]  # `none` at position 1
```

**Notes on receptive-only mode.** Reader-family axes (A1/A2/A3) currently default to receptive-only mode (reader RECEIVES translation; doesn't produce). Productive case (e.g., language-learning back-translation) is deferred — when supported, an optional `mode: Literal["receptive", "productive"]` field would be added at the Reader-family axes only; A4-A8 stay receptive-only-NOT-APPLICABLE.

### 9. Said Nursi Corpus Illustrative Mapping

For each axis, the Said Nursi corpus level the AI commonly uses (the project's primary anchor):

| Axis | Common Nursi mapping |
|---|---|
| A1 headline | `daily` (general curious Western reader) → `conversational` (engaged reader) → `native` (born-Muslim Risale-i Nur scholar) |
| A1 cultural-reference-recognition | `very_basic` for outsider Western non-Muslim; `daily` for general; `advanced` for Islamic-studies engaged; `native` for born-Muslim scholar |
| A2 | `aware` for curious general; `educated` for general religion-survey background; `trained` for working imam / Islamic-studies graduate; `expert` for Islamic-studies professor |
| A3 | `outsider` for Western secular; `acquainted` for Western world-religions exposure; `familiar` for Western convert + residence; `heritage` for 2nd-generation Turkish-American without active practice; `source-native` for born-and-raised Turkish-Muslim from Naqshbandi-Khalidi community |
| A4 | All 5 purposes are valid Nursi use cases (scholarly academic; devotional spiritual practice; casual curious reader; language-learning Turkish learner; performance recitation) |
| A5 | `foreignized` for scholarly + language-learning; `foreignized-max` for devotional liturgical; `balanced` for casual + performance |
| A6 | `standard` (Tier 1+2+3 conditional) for scholarly/devotional/language-learning; `maximum` for performance/recitation; `light` for casual |
| A7 | `rich` for casual + scholarly + chain-default; `scholarly` for full apparatus edition; `standard` for devotional; `minimal` for performance |
| A8 | `deep` for scholarly Norton-Critical-style; `scholarly` for language-learning full apparatus; `standard` for devotional; `surface` for casual; `none` for performance pure oral |

**Source-culture layering note.** Said Nursi corpus has layered source culture (Muslim broad + Turkish mid + Naqshbandi-Khalidi-Sufi innermost). A3 captures proximity to PRIMARY (innermost) layer; AI handles within-layer variation at runtime by examining whether a specific reference invokes the outer Muslim-broad layer or the inner Naqshbandi-Khalidi layer.

### 10. Versioning + Inline Changelog

**Current version: v1.0** (first canonical synthesis after A8 framework closure at 8/8 axes).

**Status:** active.

**Refines:** all 9 priors named in frontmatter.

**Version-increment rules:**
- **Patch (v1.0.1):** typo fixes; clarifications without semantic change.
- **Minor (v1.1):** refinement-notes propagation to per-axis findings; additional pattern documented in compendium; matrix cell updates that don't change defaults' semantic intent; new sub-field added to A1 (would propagate to A1 schema).
- **Major (v2.0):** axis-level revision (cardinality / labels / per-level definitions); new axis added (would expand 8 to 9+); fundamental restructure (e.g., 5-layer architecture if Layer 1A presets are integrated).

**Refinement triggers** (when does canonical spec re-version?):
- Any per-axis finding receives maintenance update.
- A4 finding maintenance bundle propagates (Section 11 carry-forward).
- `.env.example` DEPTH_PROFILE refinement propagates (Section 11).
- New cross-axis pattern emerges that warrants Patterns Compendium entry.
- New default matrix entries (e.g., if A4 categories expand).
- Layer 2 / Layer 3 inquiries reveal interaction with Layer 1 that affects canonical spec.

**Inline Changelog:**

- **v1.0 (2026-06-07):** Initial canonical synthesis after A8 framework closure at 8/8 axes. Consolidates 9 priors: root architectural finding + A1-A8 axis-level findings. Produces: 14-section canonical spec; 9-pattern compendium; 40-cell per-purpose × per-axis default matrix with refinement notes applied inline; 28-pair cross-axis orthogonality verification matrix with 4 relation types; 3-channel apparatus separation table; action-vocabulary 4-role map; 5 × 8 = 40-cell policy interaction map; receptive-only APPLIES + NOT APPLICABLE compendium; default-derivation chains; pydantic dataclass structure HINT; Said Nursi corpus illustrative mapping; 23-IC re-test.

### 11. Carry-Forward Maintenance Bundle (Next Actions MUST)

#### MUST item 1 — A4 finding maintenance pass

**What.** Propagate 4 refinement notes to `devdocs/inquiries/2026-06-06_14-05__a4_purpose_categories/finding.md` matrix:

- **A5 column language-learning:** A4's `balanced-to-foreignized` → `foreignized` (per A5 finding's refinement note; A5's 4-level structure has no in-between).
- **A6 column:** A4's "moderate" → `light`; "high" → `standard`; "MAXIMUM" → `maximum` (per A6 finding's refinement note).
- **A7 column:** A4's "moderate" → `standard`; "MAX rich" → `scholarly`; "rich (help unfamiliar)" → `rich` (per A7 finding's refinement note).
- **A8 column:** A4's language-learning `deep+scholarly` → `scholarly` (per A8 finding's refinement note; resolves ambiguity).

**Who.** A4 finding maintainer.

**Gate.** Time-bound: at next A4 finding maintenance opportunity (bundled refinements should ride a single pass).

**Why.** Aligns A4 finding's matrix with downstream axis labels; canonical spec at v1.0 is source-of-truth; A4 finding gets brought into alignment.

#### MUST item 2 — `.env.example` DEPTH_PROFILE refinement

**What.** Update `.env.example` `DEPTH_PROFILE` to accept `none` at position 1 of the accepted values (or document historical default as `surface` for legacy compatibility while exposing `none` as the explicit-zero case).

**Who.** `.env.example` maintainer.

**Gate.** Time-bound: at next `.env.example` maintenance pass.

**Why.** Aligns operational env knob with Layer 1 axis specification (A8's 5-level structure with explicit `none`).

### 12. Downstream-Unblock List

#### MUST (after this canonical spec)

- **Schema commit.** Translate canonical spec's pydantic structure HINT (Section 8) into actual pydantic dataclass code with validators, base-class choices, serializers. Becomes the runtime schema for translator-AI configuration.

- **Translator-AI prompt assembly.** Build the AI prompt context from canonical spec — per-axis prose + cross-axis matrices + policy interaction map + receptive-only compendium + default-derivation chains. Becomes the operational input to translator-AI runtime.

#### COULD

- **Layer 1A UX preset catalog.** Named scenarios (`casual-english-reader`, `scholarly-english-reader`, `language-learning-reader`, `devotional-source-native-reader`, etc.) each with all 8 axis values pre-populated, sitting above Layer 1B (the 8 axes). User picks a preset as primary UI; the 8 axes are power-user override interface. Future UX / presets inquiry.

- **Layer 2 POLICY operational specs.** For each of 5 always-on policies, specify operational behavior at translator-runtime level (what each policy ENFORCES). Likely 5 separate inquiries or one bundled.

- **Layer 3 SOURCE-DESCRIPTION schema.** Define what source properties the system auto-detects (genre, era, register profile, source culture, source language) and user-override fields. Future SOURCE-DESCRIPTION inquiry.

- **UX-layer runtime conflict surface.** Config-time warning surface for incompatible axis combinations (e.g., A7=scholarly + A8=scholarly may produce overlapping apparatus; A7=off + A5=foreignized may produce uncomfortable text). Future UX inquiry.

#### DEFERRED

- **Per-target-language refinements.** Tier 4 feasibility matrix (A6); per-target-language scaffolding feasibility (A7); per-target-language analysis-content feasibility (A8). Revival trigger: when Comprehenslate adds second target language beyond English.

- **Multi-source-culture / multi-domain audience configuration.** `audience.source_culture_proximity: list[(source_culture, level)]` for A3; `audience.expertise_set: list[(domain, level)]` for A2. Revival trigger: when audience-level inquiry runs.

- **Per-corpus DOMESTICATE-policy override.** `audience.policy_override: dict[policy_name, override_value]` for atypical corpora (children's adaptations; popular mass-market editions where heavy domestication is the genre standard). Revival trigger: when project expands beyond foreignization-preferring corpora.

- **Adaptive runtime configuration.** AI-runtime inference of axis values from feedback signals (clarifying questions; hover-clicks; back-translations). Long-horizon research frontier; depends on AI capability development.

- **Multi-purpose configuration.** `purpose: list[Literal[...]]` with weights for genuine multi-purpose use cases (scholarly + devotional academic-spiritual-formation). Revival trigger: when multi-purpose cases become primary use cases.

## Inherited Commitments Re-test

The `_branch.md` declared a Synthesis Trigger naming 9 prior outputs. Re-test of each inherited commitment at synthesis level:

| # | Commitment | Source | Re-test status |
|---|---|---|---|
| IC1 | 4-layer architecture (Layer 1 USER-FACING / Layer 2 POLICY / Layer 3 SOURCE-DESCRIPTION / Layer 4 SYSTEM-FLAGS) | root | RE-TESTED OK — Section 1.1 |
| IC2 | 8 axes in 4 families | root | RE-TESTED OK — Sections 1.2, 1.3 |
| IC3 | composite-axis pattern | root + A1 | RE-TESTED & DOCUMENTED in Patterns Compendium (Section 2.1) |
| IC4 | 5 always-on policies | root | RE-TESTED OK — Section 5 Policy Interaction Map covers all 5 |
| IC5 | 2-tier default principle | root | RE-TESTED & EXTENDED — A8 introduces dual-tier variant (Section 2.5 + 7) |
| IC6 | A1 5 sub-fields | A1 | RE-TESTED OK — Section 3.1 |
| IC7 | A1 same-labels-for-default-propagation | A1 | RE-TESTED OK — Section 3.1 |
| IC8 | DOMESTICATE-disfavored cross-cutting policy | A1 + A3 + A4 + A5 | RE-TESTED OK — preserved in Patterns Compendium (Section 2.3) + per-axis sections (Sections 3.1, 3.3, 3.4, 3.5) |
| IC9 | A2 5 levels `lay | aware | educated | trained | expert` | A2 | RE-TESTED OK — Section 3.2 |
| IC10 | A2 9 actions in 2 categories + 1 bridge | A2 | RE-TESTED OK — Section 3.2 |
| IC11 | A3 5 levels `outsider | acquainted | familiar | heritage | source-native` | A3 | RE-TESTED OK — Section 3.3 |
| IC12 | A3 10 actions in 4 categories | A3 | RE-TESTED OK — Section 3.3 |
| IC13 | A4 5 categorical | A4 | RE-TESTED OK — Section 3.4 |
| IC14 | A4 per-purpose × per-axis default matrix | A4 | RE-TESTED & CONSOLIDATED — Section 4.1 with refinement notes applied inline |
| IC15 | A4 defaults-driver special role | A4 | RE-TESTED OK — Section 3.4 + Section 4.1 |
| IC16 | A5 4 asymmetric levels + policy-embedded structure | A5 | RE-TESTED OK — Section 3.5 + Patterns Compendium 2.3 |
| IC17 | NEW translator-strategy 4-component template | A5 | RE-TESTED OK — adapted across A5/A6/A7/A8 sections |
| IC18 | A5 has NO own actions; modulates A1+A3 | A5 | RE-TESTED OK — Section 3.5 + Action-Vocabulary Map (Section 4.4) |
| IC19 | A6 5 levels tied to harmony_layer Tier 1-4 | A6 | RE-TESTED OK — Section 3.6 |
| IC20 | A6 produces harmony report at Levels 3+ | A6 | RE-TESTED OK — Section 3.6 + Apparatus Channel Separation Table (Section 4.3) |
| IC21 | A6 activation gate at `light` | A6 | RE-TESTED OK — Section 3.6 + Policy Interaction Map (Section 5) |
| IC22 | A7 5 levels with action-permission table | A7 | RE-TESTED OK — Section 3.7 + Patterns Compendium 2.7 |
| IC23 | A7 5 multi-meaning render rules + EXPLICATE-FUNCTION fallback | A7 | RE-TESTED OK — Section 3.7 + Policy Interaction Map (Section 5) |
| IC24 | A8 5 levels with `none` (revised from root's 4) | A8 | RE-TESTED OK — Section 3.8 |
| IC25 | A8 content-type-by-level table | A8 | RE-TESTED OK — Section 3.8 + Patterns Compendium 2.6 |
| IC26 | A8 A7↔A8 3-framing rule | A8 | RE-TESTED OK — Section 3.8 + Orthogonality Matrix (Section 4.2) |
| IC27 | A8 dual-tier default | A8 | RE-TESTED OK — Section 7 Default-Derivation Chains + Patterns Compendium 2.5 |
| IC28 | A8 harmony-report-location (standalone + cross-references at deep+) | A8 | RE-TESTED OK — Section 3.8 + Apparatus Channel Separation Table (Section 4.3) |
| IC29 | A8 multi-meaning analysis (three-layer treatment) | A8 | RE-TESTED OK — Patterns Compendium 2.9 + Policy Interaction Map (Section 5) |
| IC30 | FRAMEWORK CLOSURE marker (8/8) | A8 | RE-TESTED & EMBODIED — canonical spec IS the closure |
| IC31 | Receptive-only APPLIES (A1-A3) + NOT APPLICABLE (A4-A8) | A4 + A5 + A6 + A7 + A8 | RE-TESTED & CONSOLIDATED in Receptive-only Compendium (Section 6) |
| IC32 | Per-axis A4 refinement notes (carry-forward) | A5 + A6 + A7 + A8 | RE-TESTED & RESOLVED — refinement notes applied inline in Section 4.1; propagation bundled in Section 11 |

32 inherited commitments re-tested. No silent inheritance. All ICs either RE-TESTED OK, RE-TESTED & DOCUMENTED, RE-TESTED & CONSOLIDATED, RE-TESTED & EXTENDED, RE-TESTED & RESOLVED, or RE-TESTED & EMBODIED.

## Open Questions

### Monitoring

- Observable after schema commit: does the pydantic structure HINT translate cleanly into actual code, or do validator/serializer specifics surface gaps the canonical spec doesn't address?
- Observable after first translations: do default-derivation chains produce reasonable cold-start configurations across A4 purposes?
- Observable after per-purpose × per-axis matrix usage: do any cells consistently over- or under-shoot (need calibration shift toward typical-use bias as feedback accumulates)?
- Observable after Layer 2 policy operational specs run: do they surface gaps in the policy interaction map's "not applicable" cells?

### Blocked

- Schema commit blocked by canonical spec v1.0 (this finding); unblocks immediately after this finding.
- Layer 1A UX preset catalog blocked by schema commit.
- Multi-source-culture / multi-domain audience configuration blocked by audience-level inquiry.

### Research Frontiers

- AI-runtime adaptive configuration (long-horizon).
- Per-target-language refinements (depends on second target language addition).
- Per-corpus policy override (depends on project expansion beyond foreignization-preferring corpora).

### Refinement Triggers

- If per-axis maintenance pass surfaces inconsistencies the canonical spec didn't anticipate, revise canonical spec at v1.1.
- If a future axis-level inquiry revises cardinality / labels / per-level definitions, revise canonical spec at v2.0.
- If new architectural patterns emerge (e.g., a future axis introduces a pattern not in the 9-pattern compendium), add to Patterns Compendium at v1.1.
- If Layer 1A presets are designed and the architecture revises to 5 layers, revise canonical spec at v2.0.
- If 30+ real translation configurations show default-derivation chains consistently over- or under-shoot, calibrate toward typical-use bias.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
now lets synthesize all 8 axes into canonical Layer 1 spec
```

</details>
