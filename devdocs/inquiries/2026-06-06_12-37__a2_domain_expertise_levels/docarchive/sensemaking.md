# Sensemaking — a2_domain_expertise_levels

## User Input
`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-06_12-37__a2_domain_expertise_levels/_branch.md` (with surfacing output at `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-06_12-37__a2_domain_expertise_levels/surfacing.md`)

---

## SV1 — Baseline Understanding

Define 5 ordinal levels for A2 — Domain Expertise (the 2nd axis in the Reader family per root architectural finding). User directive: 5 levels (refining root's proposed 3). Plain-ordinal axis, NOT composite-axis like A1. The real challenge per user: explicit distinguishing logic and good cross-domain examples. Resolve A2↔A1, A2↔A3, A2↔A4 boundaries; settle label choice (5 candidate sets); settle domain-scope (single vs set); decide template adaptation.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints
- **C1** 5 ordinal levels (user directive — refines root's proposed 3).
- **C2** Plain-ordinal pattern, NOT composite-axis (per root finding).
- **C3** Receptive-only (recognition; inherited from A1 chain).
- **C4** Conservative-bias-for-reader-axes = LOWER default (inherited).
- **C5** Language-agnostic at concept level (the framework works for any source domain).
- **C6** Distinct from A1 (general fluency), A3 (cultural identity), A4 (purpose) — boundaries explicit.
- **C7** Operationalizable as translator-AI prompt context.
- **C8** Examples MUST span multiple domains (not lock to one).
- **C9** Same-labels-for-default-propagation does NOT inherit (A2 has no sub-fields; the rationale doesn't apply).

### Key Insights

- **KI1** A2's dimension is DEPTH OF DOMAIN-SPECIALIST KNOWLEDGE in the source's subject domain — not general reading capacity. 5 sub-aspects (per surfacing R8) cluster as a single ordinal rise: technical-vocabulary depth + conceptual-schema integration + discourse-conventions recognition + specialist-debates recognition + primary-source-canon familiarity. These are NOT separate axes (A2 is plain-ordinal); they all rise together.
- **KI2** Dreyfus & Dreyfus 5-stage expertise (novice / advanced beginner / competent / proficient / expert) is the canonical 5-stage cognitive-science model and maps naturally onto A2's 5 levels.
- **KI3** Polanyi's tacit knowledge distinction is load-bearing: at lower A2 levels the reader has only explicit knowledge; at higher levels they have tacit-and-explicit. The translator-AI can use specialist-tacit shorthand at high A2 levels (specialists "know what is meant" by abbreviated phrasing).
- **KI4** The same word fires both A1 and A2 in different roles: "ratiocination" → A1 vocabulary (general English); "isnād" → A2 Islamic-studies vocabulary (specialist domain). The translator-AI uses BOTH axis values per term: A1 decides whether the GENERAL-VOCABULARY substitution fires (replace "ratiocination" with "reasoning"); A2 decides whether the DOMAIN-VOCABULARY unpacking fires (FOOTNOTE "isnād" or INLINE-DEFINE "isnād").
- **KI5** A2 is RECEPTIVE-ONLY like A1 — the reader RECOGNIZES specialist terms; doesn't produce them. The translator-AI's job is to gauge what the reader CAN FOLLOW.
- **KI6** DOMAIN-SCOPE — for any given translation job, the source text is in ONE domain (a Said Nursi text = Islamic theology; a Bible passage = biblical scholarship; a physics paper = theoretical physics). The A2 value applies to that single source domain. Cross-domain references within the source (Islamic philosophy drawing on Greek references) are handled at runtime via the AI's cross-domain knowledge, not via the configuration. SINGLE-DOMAIN DEFAULT settles frontier flag F2.
- **KI7** LABEL CHOICE — domain-meaningful labels serve operational clarity better than A1-consistency labels. A1's `daily` / `conversational` don't carry domain-meaning ("daily domain expertise" reads oddly). Better: `lay | aware | educated | trained | expert` — standard in expertise-stratification literature; maps to Dreyfus 5-stage (novice ≈ lay, advanced beginner ≈ aware, competent ≈ educated, proficient ≈ trained, expert ≈ expert); cross-domain semantics intact. Frontier flag F1 resolves toward this set.
- **KI8** TEMPLATE ADAPTATION — the 4-component A1 sub-field template adapts MEDIUM-heaviness:
  - Component 1 (reader profile) — kept conceptually.
  - Component 2 (frequency-tier) → REPLACED with `expertise-depth-tier` (5 dimensions cluster as one ordinal rise).
  - Component 3 (register-tier) → REFRAMED as `discourse-register-tier` (school-internal debates appear at higher levels; lay discourse at lower).
  - Component 4 (substitution-test) → REPLACED with `domain-handling-test` containing 9 named actions in 2 categories + 1 bridge.
- **KI9** LEVEL 3 CONFLATION RISK (F5) — the user's original sketch used "general-educated" as A2's middle level. Risk: confusion with A1's "advanced" general-fluency reader. RESOLUTION: A2's "educated" level explicitly means EDUCATED-IN-THIS-SPECIFIC-DOMAIN (e.g., has read general material on the domain: Karen Armstrong's *Islam*; Bart Ehrman's intro to NT; an undergraduate philosophy survey). Distinct from A1's general fluency. Explicit framing in each level definition + explicit A2↔A1 boundary section.
- **KI10** FORWARD-TAGGED SPECIALIST CANONS from A1 (F9) — A1's cultural-reference-recognition forward-tagged 5 specialist-domain canons (legal precedents / mathematical figures / scientific figures / medical eponyms / specialist philosophy) to A2. This inquiry RECEIVES them: they are valid A2-territory items. A2's framework handles them via the same expertise-depth dimension. Each specialist canon maps to a specialist domain; A2's 5 levels apply within each.
- **KI11** A2's level applies WITHIN the source's domain. The translator-AI knows the source's domain from the source text itself (runtime observation; Layer 3 SOURCE-DESCRIPTION concern). Configuration just specifies "what level the reader is at" for that domain. The reader doesn't pick a domain; the source's domain is implicit.
- **KI12** CONSERVATIVE-BIAS at A2 → AI assumes lower expertise. For technical vocabulary, AI defaults to INLINE-DEFINE-ON-FIRST-USE or PARAPHRASE-IN-LAYMAN-TERMS until explicitly configured higher. Protects against "I'll just use the technical term; they probably know it" failure mode.
- **KI13** A2's specialist HANDLING ACTIONS differ from A1's: A1 sub-fields involve vocabulary substitution, syntactic restructuring, idiom paraphrase, gap-filling, cultural-reference gloss. A2 involves technical-vocabulary unpacking AND discourse-level moves (school references, debate references). The DISCOURSE-LEVEL dimension is what makes A2 distinctive.
- **KI14** SAID NURSI ANCHOR — the project's primary corpus. For an English target reader:
  - A2=lay (generic Western reader; needs all Islamic terms unpacked)
  - A2=aware (Western reader with general "world religions" exposure; recognizes Quran/Prophet Muhammad/5 pillars)
  - A2=educated (read Karen Armstrong's *Islam* or similar; understands tawhid as concept)
  - A2=trained (formal university Islamic-studies background; recognizes kalam/fiqh/tafsīr distinctions; knows 4 Sunni schools)
  - A2=expert (Nursi scholar OR Islamic-studies professor; navigates Mu'tazila/Ash'ari debates; recognizes Risale-i Nur internal terminology + Naqshbandi-Khalidi Sufi context)
- **KI15** AVOID OVER-ANCHORING TO ISLAMIC THEOLOGY — the framework MUST be domain-agnostic. Each level needs cross-domain examples (biblical / philosophy / science / law) to demonstrate the level concept travels.

### Structural Points
- **SP1** 5 levels named `lay | aware | educated | trained | expert` (working choice; tested in Ambiguity A1).
- **SP2** A2 has 5 stratification dimensions that rise together (not separate sub-fields; A2 is plain-ordinal): technical-vocabulary depth + conceptual schema + discourse conventions + specialist-debates recognition + primary-source-canon familiarity.
- **SP3** 4-component template adapts: reader-profile + expertise-depth-tier + discourse-register-tier + domain-handling-test.
- **SP4** 9 named handling actions in 2 sub-categories + 1 bridge:
  - **Vocabulary-level (4):** USE-TECHNICAL-VOCABULARY-FREELY / INLINE-DEFINE-ON-FIRST-USE / FOOTNOTE-TECHNICAL-TERM / PARAPHRASE-IN-LAYMAN-TERMS
  - **Discourse-level (4):** INVOKE-SPECIALIST-DEBATES / ATTRIBUTE-VIEW-TO-SCHOOL / UNATTRIBUTED-CONSENSUS / AVOID-SPECIALIST-DEBATES
  - **Bridge (1):** KEEP-SOURCE-TERM-WITH-GLOSS (transliteration retention)
- **SP5** Single-domain default for domain-scope (A2 = reader's expertise IN THE SOURCE'S DOMAIN; the source's domain is implicit at runtime).
- **SP6** A2↔A1 boundary: same-word-can-fire-both with domain-specific (A2) vs general (A1) distinction.
- **SP7** A2↔A3 boundary: competence-based (A2) vs identity-based (A3); four-corners independence.
- **SP8** A2↔A4 boundary: A4 = why (purpose); A2 = how much known (expertise).
- **SP9** Forward-tagged 5 specialist canons from A1 (legal / math / science / medical / specialist-philosophy) are A2-territory; framework handles via expertise-depth dimension.

### Foundational Principles
- **FP1** Receptive-only (inherited from A1 chain).
- **FP2** Conservative-bias-for-reader-axes = LOWER default.
- **FP3** Language-agnostic at concept level (works for any source domain).
- **FP4** Domain-meaningful labels preferred over A1-consistency labels (labels open since A2 is not composite-axis).
- **FP5** Single-domain-per-config (source's domain is implicit at runtime).
- **FP6** Plain-ordinal pattern (no sub-fields, no propagation).
- **FP7** Operationalizable as translator-AI prompt context.

### Meaning-Nodes
- **MN1** Domain expertise — central concept; depth of specialist knowledge in the source's subject domain.
- **MN2** Technical vocabulary — primary sub-dimension that rises with expertise.
- **MN3** Discourse conventions — recognizing school-internal debates, lineage of arguments.
- **MN4** Conceptual schema — how well-integrated the reader's knowledge structure is.
- **MN5** Translator-AI handling — runtime decision the AI makes per technical term + per discourse-level reference.

### Meta-Inspection after SV2 (hooks H4, H5)
- **H4 (concept names):**
  - "expertise-depth-tier" → STRUCTURAL (real dimension grounded in Dreyfus + Polanyi + schema theory).
  - "domain-handling-test" → user-language aligned (parallels sibling test names from A1 chain).
  - `lay | aware | educated | trained | expert` → STRUCTURAL labels grounded in expertise-stratification literature (Dreyfus 5-stage approximate mapping).
- **H5 (motivating examples):** 25 example clusters (5 domains × 5 levels) are SAMPLES of a wider pattern (domain expertise across any specialist domain). Examples are illustrative, not THE WHOLE problem.

### SV2 — Anchor-Informed Understanding

After anchor extraction:
- A2 is a plain-ordinal axis with 5 levels capturing depth of domain-specialist knowledge.
- 5 stratification dimensions rise together (vocabulary depth + conceptual schema + discourse conventions + specialist debates + primary-source canon familiarity).
- Working label set: `lay | aware | educated | trained | expert` (anchored to expertise-stratification literature).
- 4-component template adapts MEDIUM-heaviness (reader profile + expertise-depth-tier + discourse-register-tier + domain-handling-test).
- 9 handling actions structured as 4 vocabulary-level + 4 discourse-level + 1 bridge.
- Single-domain default for domain-scope.
- A2↔A1 / A2↔A3 / A2↔A4 boundaries clear.
- Forward-tagged specialist canons from A1 are A2-territory.

---

## Phase 2 — Perspective Checking

### Technical / Logical
- **T1** 5 levels ordinally distinct.
- **T2** Each level definition needs operational predicate (what distinguishes level N from level N+1).
- **T3** Handling actions form ordered ladders:
  - Vocabulary: USE-FREELY > KEEP-WITH-GLOSS > INLINE-DEFINE > FOOTNOTE > PARAPHRASE
  - Discourse: INVOKE-DEBATES > ATTRIBUTE-TO-SCHOOL > UNATTRIBUTED-CONSENSUS > AVOID-DEBATES
- **T4** Domain-scope unambiguous: source's domain at config time is the relevant scope.

### Human / User
- **U1** User is translator; cares about AI making right handling choices at runtime.
- **U2** User's corpus is Said Nursi → English. Typical target reader Western, A2 ranging from lay (no Islamic background) to expert (Nursi scholar).
- **U3** User explicitly flagged the inquiry's main challenge as "explicit definitions distinguishing the 5 levels with good examples" — the finding should NOT lean on examples alone; distinguishing logic must be explicit text.
- **U4** Examples must span multiple domains so the framework's domain-agnosticism is visible to the user.

### Strategic / Long-term
- **S1** A2 is one of 8 axes; this inquiry settles A2; the next is A3 Source Culture or further.
- **S2** A2 once committed feeds the schema: `domain_expertise: Literal["lay", "aware", "educated", "trained", "expert"]`.
- **S3** Label choice should age well; `lay | aware | educated | trained | expert` is timeless and standard in expertise literature; not project-specific jargon.

### Risk / Failure
- **R1** Risk: levels defined by example only, no distinguishing logic. CORRECTIVE: explicit per-level distinguishing predicates (user flagged).
- **R2** Risk: examples lock to Islamic theology. CORRECTIVE: cross-domain examples per level (5 domains × 5 levels).
- **R3** Risk: level 3 "educated" conflated with A1's "advanced" general fluency. CORRECTIVE: explicit "educated-IN-THIS-DOMAIN" framing; explicit A2↔A1 boundary.
- **R4** Risk: A2's handling actions conflated with A1's. CORRECTIVE: A2's actions are domain-vocabulary + discourse-level; A1's are general-vocabulary substitution + syntactic restructuring; explicit separation.
- **R5** Risk: multi-domain texts not handled. CORRECTIVE: single-domain-default; multi-domain handled at runtime via AI's domain-detection.
- **R6** Risk: receptive-only commitment lost. CORRECTIVE: explicit framing inherited.
- **R7** Risk: conservative-bias-default lost. CORRECTIVE: explicit LOWER-default.

### Resource / Feasibility
- **Re1** Operationalizable as AI prompt context: feasible.
- **Re2** Cross-domain examples: feasible (5 × 5 surfaced).
- **Re3** 4-component template: adapts cleanly from A1.

### Definitional / Internal Consistency
- Interpretation does not contradict A1 chain or root architectural finding.
- A2 plain-ordinal vs A1 composite-axis: different structural patterns but consistent within the root framework.
- Receptive-only and conservative-bias both inherited consistently.

### Definitional / Frame-exit Completeness (GATING CHECK fires)

Gating predicate:
- (i) Inherited terms from prior findings: YES (receptive-only, conservative-bias, language-agnostic, A2↔A1↔A3 boundaries, 5 forward-tagged specialist canons from A1).
- (ii) Used across ≥2 distinct values/levels: YES (5 levels with distinct propositions per level; A2↔A1, A2↔A3, A2↔A4 across multiple cross-axis pairs).
- **Gating FIRES.** Apply 4 meta-categories:

1. **Existence Enumeration.** What does "domain expertise" refer to project-wide?
   - TYPE axis: technical vocabulary; conceptual schema; discourse conventions; specialist debates; primary-source canon familiarity.
   - LAYER axis: appears in source text (technical vocabulary in source) AND in reader's expected knowledge (reader's expertise level).
   - PHASE axis: not relevant.
   - AGENT axis: reader-side property (A2 is reader-relative).
   - TIME axis: expertise accumulates over time but configuration is a snapshot at config time.
   - STRUCTURAL ROLE axis: domain expertise enables technical-vocabulary recognition without unpacking.
   - **IN-SCOPE:** reader's domain expertise depth in the source's subject domain.
   - **OUT-OF-SCOPE:** source's domain identity (Layer 3 SOURCE-DESCRIPTION concern; auto-detected); cross-domain expertise variation (multi-domain handled by runtime AI domain-detection); user's expertise change over time (snapshot assumption).

2. **Role Assessment.** Out-of-scope referents:
   - Source's domain identity → Layer 3 SOURCE-DESCRIPTION; not A2. Operation coherent without it being in A2 (AI auto-detects source's domain).
   - Cross-domain expertise variation → handled at runtime; not A2 config. KEEP OUT.

3. **Verdict Rigor.** "Single-domain-default" verdict tested:
   - Strongest counter: maybe A2 SHOULD capture multi-domain expertise (a reader fluent in Islamic theology AND Greek philosophy is real).
   - Why counter fails: A2's role is to inform the translator-AI about the reader's expertise FOR THE SOURCE TEXT. The source has ONE domain. Multi-domain configuration would add complexity (per-domain values) without operational benefit (AI only needs "what does reader know about THIS text's domain?"). Cross-references handled at runtime.
   - HOLDS at HIGH confidence.

4. **Residual / Coverage Justification.** Other frame-exit concerns:
   - Source crosses domains and AI can't unambiguously identify "the source's domain"? → Layer 3 concern.
   - Reader's expertise differs between technical vocabulary and discourse conventions? → 5 dimensions rise together per surfacing R8; integrated rise. Edge cases conservative-bias.
   - Recursion terminates.

### Phase / Calibration-State
- Does rule depend on calibration project state has? NO. 5 levels are concept-level; translator-AI handling-action selection is deterministic given (A2 level, source's technical vocabulary, discourse moves observed).
- Early-stage default: conservative bias LOWER (per FP2).

### Ethical / Systemic
- Treating readers as MORE knowledgeable than they are = condescension-by-absence (jargon used; reader excluded).
- Treating readers as LESS knowledgeable = condescension-by-overgloss (over-explained; reader patronized).
- Framework with conservative-bias-LOWER default leans toward over-glossing — safer ethically but potentially patronizing at higher A2 levels. Trade-off acceptable given project early stage; user can dial up.

### Meta-Inspection after SV3 (hooks H1, H2, H3, H7)
- **H1 (candidate set):** 5 levels — convergence with user directive.
- **H2 (frame scope):** Frame-exit handled.
- **H3 (question framing):** explicit.
- **H7 (phase/calibration):** no calibration dependency.

### SV3 — Multi-Perspective Understanding

Confirms:
- 5 ordinal levels for A2 plain-ordinal axis.
- Labels `lay | aware | educated | trained | expert` (working hypothesis to be settled in Ambiguity A1).
- 4-component template adapts MEDIUM (reader profile + expertise-depth-tier + discourse-register-tier + domain-handling-test).
- 9 handling actions in 2 categories + 1 bridge.
- Single-domain default.
- Cross-domain examples (5 domains × 5 levels).
- A2↔A1 / A2↔A3 / A2↔A4 boundaries explicit.
- Receptive-only + conservative-bias inherited.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity A1: Label choice
Which 5 labels?

**Strongest counter-interpretation:** Use `very_basic | daily | conversational | advanced | native` to match A1 for naming consistency.

**Why counter fails (structural grounds):** A1's labels are designed for general reading fluency (daily/conversational are everyday-language gradients). "Daily" and "conversational" don't carry domain-meaning; "daily domain expertise" reads oddly. Domain-meaningful labels operationalize cleanly with cross-domain semantics. Same-labels-for-default-propagation applies to A1 because A1 is composite-axis (propagation across 5 sub-fields needed). A2 has no sub-fields; labels need only be domain-meaningful. Cost of label divergence is mild; cost of label awkwardness is significant ("daily domain expertise" wrong).

**Confidence:** HIGH
**Resolution:** Labels = `lay | aware | educated | trained | expert`. Anchored to expertise-stratification literature (Dreyfus 5-stage approximate mapping).
**What is fixed:** the label set.
**What is no longer allowed:** A1-label forcing.
**What depends:** schema enum values.

### Ambiguity A2: Domain-scope (single vs set)
Does A2 specify expertise in one domain or multiple?

**Strongest counter-interpretation:** Multi-domain — a reader can be specialist in Islamic theology AND lay in physics simultaneously.

**Why counter fails (structural grounds):** A2's operational role is to inform the AI for a SPECIFIC translation job. The source text has ONE domain (a Nursi text = Islamic theology). A2 value applies to THAT domain. Multi-domain configuration adds complexity (per-domain values) without operational benefit (AI only needs "what does the reader know about THIS text's domain?"). Cross-domain references within source handled at runtime via AI's multi-domain knowledge.

**Confidence:** HIGH
**Resolution:** Single-domain default. A2 = reader's expertise in the source's domain.
**What is fixed:** single-domain interpretation.
**What is no longer allowed:** multi-domain configuration at A2.
**What depends:** AI prompt context phrasing.

### Ambiguity A3: Template adaptation
Does the 4-component A1 template apply to A2?

**Strongest counter-interpretation:** A2 is plain-ordinal not composite-axis; different structural pattern; the A1 template doesn't apply.

**Why counter fails (structural grounds):** The 4-component template (reader profile + tier-component + register-component + handling-test) is about PER-LEVEL definition shape, not axis-pattern shape (composite vs plain). The 4 components organize per-level prose in a way that's usable as translator-AI prompt context. They apply to ANY level definition.

**Confidence:** HIGH
**Resolution:** 4-component template applies with MEDIUM adaptations. Reader profile kept; frequency-tier → expertise-depth-tier (5-dimension aggregate); register-tier → discourse-register-tier; substitution-test → domain-handling-test with 9 named actions.
**What is fixed:** template inherited; adaptations specified.
**What is no longer allowed:** abandoning the template entirely.
**What depends:** per-level prose structure.

### Ambiguity A4: Level 3 ("educated") conflation risk with A1's "general-educated"
Does A2's "educated" level conflict with A1's general fluency framing?

**Strongest counter-interpretation:** Maybe yes — calling level 3 "educated" overlaps with A1's "advanced" general fluency framing.

**Why counter fails (structural grounds):** A2's "educated" specifically means EDUCATED-IN-THIS-DOMAIN. A reader at A2=educated has read general material on the source's domain (Karen Armstrong's *Islam* for Islamic theology; Bart Ehrman intro for biblical scholarship; undergraduate philosophy survey). They have SOME domain literacy but no formal training. A1=advanced means general English reading fluency at humanities-undergraduate level; A2=educated means domain-specific literacy at educated-amateur level. DIFFERENT axes capturing DIFFERENT properties. Boundary clarity preserved by EXPLICIT framing in each level definition.

**Confidence:** HIGH
**Resolution:** Explicit "educated-IN-THIS-SPECIFIC-DOMAIN" framing for level 3; explicit A2↔A1 boundary statement; level definitions contrast with A1's general fluency.
**What is fixed:** framing.
**What is no longer allowed:** ambiguous "educated" without domain-scope marker.
**What depends:** per-level prose carries explicit framing.

### Ambiguity A5: Forward-tagged specialist canons from A1
How does A2 handle the 5 forward-tagged specialist canons (legal precedents / mathematical figures / scientific figures / medical eponyms / specialist philosophy)?

**Strongest counter-interpretation:** Maybe these don't fit A2 — they're cultural-reference items, not domain-expertise items.

**Why counter fails (structural grounds):** A1's cultural-reference-recognition explicitly routed these to A2 because recognition requires domain training (the criterion was "general cultural literacy → A1; domain training required → A2"). The 5 canons are A2-territory by A1's own framework. A2 handles them via expertise-depth dimension: lay = doesn't know any; aware = has heard of "Brown v. Board"; educated = recognizes major Supreme Court cases; trained = recognizes specific doctrines; expert = navigates subfield debates.

**Confidence:** HIGH
**Resolution:** A2 receives forward-tagged specialist canons; each maps to A2's expertise-depth dimension within its specialist domain. In any given translation job only one specialist domain is the source's domain.
**What is fixed:** A2 handles forward-tagged canons via expertise-depth.
**What is no longer allowed:** ignoring the forward-tagging.
**What depends:** the cross-domain examples in level definitions include these specialist canons.

### Ambiguity A6: Single A2 axis vs multiple specialist-domain axes
Should A2 be ONE axis or MULTIPLE (one per specialist domain)?

**Strongest counter-interpretation:** Multiple axes — captures cross-domain expertise variation.

**Why counter fails (structural grounds):** Root architectural finding committed to A2 as ONE axis. Multiple axes would multiply configuration burden (a reader might have N specialist-domain expertise levels to set) and would mostly be unused (typical user only cares about source's domain). Single-domain-default handles this: A2 is ONE axis whose VALUE applies to the source's domain at runtime.

**Confidence:** HIGH
**Resolution:** A2 remains ONE axis (per root); single-domain-default for scope; source's domain is implicit at runtime.
**What is fixed:** single-axis architecture.
**What is no longer allowed:** multi-axis specialist-domain decomposition.

### Ambiguity A7: Handling action vocabulary count
Are 9 handling actions (4 vocabulary + 4 discourse + 1 bridge) the right number?

**Strongest counter-interpretation:** Maybe simpler (4 or 5) or richer (12+).

**Why counter fails (structural grounds):** Surfacing identified 9 distinct actions in the literature. Consolidating loses operational distinction (FOOTNOTE vs INLINE-DEFINE are operationally different). Expanding adds complexity without coverage gain. 9 is the natural count.

**Confidence:** MEDIUM (action count somewhat negotiable; categorization into vocabulary + discourse is structural).
**Resolution:** 9 handling actions structured as 4 vocabulary-level + 4 discourse-level + 1 bridge. Translator-AI uses appropriate action conditioned on (A2 level, term type, source's marking).
**What is fixed:** 9-action vocabulary.
**What depends:** per-level prose specifies which actions fire at which level.

### Ambiguity A8: Receptive-only inheritance
Does A2 inherit receptive-only from A1?

**Strongest counter-interpretation:** Maybe A2 should be productive-also (a specialist might write/produce in the domain).

**Why counter fails (structural grounds):** In TRANSLATION context, the reader is receiving translated text. The relevant question is what the reader CAN RECOGNIZE/FOLLOW, not what they can produce. A specialist reader's production capability is irrelevant to translation-AI handling decisions.

**Confidence:** HIGH
**Resolution:** A2 is RECEPTIVE-ONLY. Reader recognizes specialist vocabulary and discourse-level moves; doesn't have to produce them.
**What is fixed:** receptive-only.
**What is no longer allowed:** productive interpretation.
**What depends:** per-level prose framed as recognition.

### Meta-Inspection (Load-bearing concept test + Specific-vs-pattern recognition cue)
- "Expertise-depth-tier" — tested in A3.
- "Domain-handling-test" — user-language aligned; 9 actions categorized.
- "Single-domain-default" — tested in A2.
- "Domain-meaningful labels" — tested in A1.
- Specific-vs-pattern: 25 example clusters (5 × 5) are SPECIFIC EXAMPLES; broader pattern is "domain expertise across any specialist domain." Examples are concrete instantiations of the general framework.

### SV4 — Clarified Understanding

After ambiguity collapse:
- 5 levels labeled `lay | aware | educated | trained | expert`.
- Plain-ordinal axis with 5 stratification dimensions rising together.
- Single-domain default (source's domain implicit at runtime).
- 4-component template adapts MEDIUM heaviness.
- 9 handling actions in 2 categories + 1 bridge.
- Forward-tagged 5 specialist canons from A1 received and handled.
- Receptive-only inherited.
- Conservative-bias LOWER inherited.
- A2↔A1 / A2↔A3 / A2↔A4 boundaries explicit.
- Cross-domain examples required at every level.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Variables now fixed
- **VF1** 5 levels with labels `lay | aware | educated | trained | expert`.
- **VF2** Plain-ordinal pattern; no sub-fields.
- **VF3** Single-domain default.
- **VF4** 4-component template MEDIUM-adapted.
- **VF5** 9 handling actions in 2 categories + 1 bridge.
- **VF6** Receptive-only.
- **VF7** Conservative-bias LOWER default.
- **VF8** A2↔A1 / A2↔A3 / A2↔A4 boundaries documented.
- **VF9** Forward-tagged 5 specialist canons from A1 received and integrated.

### Options eliminated
- **OE1** A1-label-set forcing here.
- **OE2** Multi-domain configuration at A2.
- **OE3** Multi-axis specialist-domain decomposition.
- **OE4** Productive interpretation.
- **OE5** Abandoning the 4-component template.
- **OE6** Ambiguous "educated" without domain-scope marker.

### Viable paths remaining
- **VP1** Per-level prose with 4 components for each of 5 levels.
- **VP2** Cross-domain examples per level (Islamic theology + biblical + philosophy + science + law) — at least 3 per level.
- **VP3** A2↔A1 / A2↔A3 / A2↔A4 boundary sections.
- **VP4** Forward-tagged 5 specialist canons integration in level definitions.
- **VP5** Conservative-bias handling commitment statement.
- **VP6** Distinguishing-logic statements between adjacent levels (the user's explicit ask).

### SV5 — Constrained Understanding

Solution space organized:
1. 5 conceptual definitions (one per level) with 4 components each.
2. Distinguishing logic between adjacent levels — 4 boundaries.
3. Cross-domain examples — 5 domains × 5 levels = 25 example clusters.
4. A2↔A1 / A2↔A3 / A2↔A4 boundary statements.
5. Forward-tagged 5 specialist canons integration.
6. Handling action vocabulary (9 actions, 2 categories + 1 bridge).
7. Single-domain-default commitment statement.
8. Conservative-bias handling commitment statement.

---

## Phase 5 — Conceptual Stabilization

**A2 — Domain Expertise** = 5 ordinal levels (`lay | aware | educated | trained | expert`) of the reader's specialist knowledge in the source text's subject domain. Plain-ordinal axis (no sub-fields). 5 dimensions rise together with the level (technical-vocabulary depth + conceptual schema + discourse conventions + specialist debates recognition + primary-source canon familiarity). 4-component template MEDIUM-adapted (reader profile + expertise-depth-tier + discourse-register-tier + domain-handling-test). 9 handling actions structured as 4 vocabulary-level + 4 discourse-level + 1 bridge. Single-domain default (A2 applies to source's domain; source's domain implicit at runtime). Receptive-only. Conservative-bias LOWER default. Forward-tagged 5 specialist canons from A1 received and handled. Examples span 5 reference domains.

### Meta-Inspection (Accommodation trigger check)
Did any perspective force model patching? **NO** — perspectives ENRICHED the model. 8 ambiguities settled cleanly at HIGH (7) / MEDIUM (1) confidence. Not premature stabilization on either axis.

### SV6 — Stabilized Model

**A2 — Domain Expertise stabilized model:**
- 5 levels: `lay | aware | educated | trained | expert`
- Plain-ordinal; 5 dimensions rise together
- 4-component template MEDIUM-adapted: reader profile + expertise-depth-tier + discourse-register-tier + domain-handling-test
- 9 handling actions: vocabulary-level (USE-FREELY / INLINE-DEFINE / FOOTNOTE / PARAPHRASE) + discourse-level (INVOKE-DEBATES / ATTRIBUTE-TO-SCHOOL / UNATTRIBUTED-CONSENSUS / AVOID-DEBATES) + bridge (KEEP-SOURCE-TERM-WITH-GLOSS)
- Single-domain default; source's domain implicit at runtime
- Receptive-only; conservative-bias LOWER
- Forward-tagged 5 specialist canons from A1 received
- Cross-domain examples (5 × 5 = 25)
- A2↔A1, A2↔A3, A2↔A4 boundaries explicit

**Difference from SV1:** SV1 was task restatement. SV6 commits to specific structural decisions: (1) labels `lay | aware | educated | trained | expert` settled; (2) single-domain default settled; (3) 4-component template adapts MEDIUM; (4) 9 handling actions in 2 categories + 1 bridge; (5) A2 receives forward-tagged specialist canons from A1; (6) receptive-only + conservative-bias inherited; (7) explicit "educated-IN-THIS-DOMAIN" framing prevents A1 conflation; (8) explicit distinguishing logic between adjacent levels required (user's explicit ask honored).

---

## Saturation Indicators

- **Perspective saturation:** 8 perspectives applied; last few produced refinements not new types. APPROACHING SATURATION.
- **Ambiguity resolution ratio:** 8/8 ambiguities resolved at HIGH (7) or MEDIUM (1) confidence; 0 OPEN. Ratio = 1.0.
- **SV delta:** SV1 → SV6 major delta; SV6 commits to 8+ specific structural decisions.
- **Anchor diversity:** Constraints (9), Key Insights (15), Structural Points (9), Foundational Principles (7), Meaning-Nodes (5) across 8 perspectives. DIVERSE.

**Saturation: HIGH. PROCEED to Decomposition.**

## Inherited Commitments Re-tested

| # | Inherited commitment | Source | Re-test verdict |
|---|---|---|---|
| IC1 | Receptive-only | A1 chain | RE-TESTED OK — Ambiguity A8 settled at HIGH; A2 receptive-only confirmed |
| IC2 | Conservative-bias-LOWER default | root + A1 chain | RE-TESTED OK — explicit in level definitions; AI assumes lower expertise → more aggressive technical-vocab unpacking |
| IC3 | Language-agnostic at concept level | root | RE-TESTED OK — framework works for any source domain; 5 reference domains demonstrate |
| IC4 | A2 plain-ordinal pattern (no sub-fields) | root | RE-TESTED OK — Ambiguity A6 settled at HIGH |
| IC5 | A2 cardinality (root proposed 3) | root | RE-TESTED & REFINED — user-directed to 5; Dreyfus 5-stage anchors |
| IC6 | A2 boundary vs A1 (general fluency) and A3 (cultural identity) | root | RE-TESTED & DOCUMENTED — Ambiguity A4 settled; four-corners independence demonstrated |
| IC7 | A2 controls technical vocabulary unpacking | root | RE-TESTED OK — 9 handling actions specified |
| IC8 | 5 forward-tagged specialist canons from A1's cultural-reference-recognition | a1_cultural_reference_recognition_levels | RE-TESTED & APPLIED — A2 receives all 5 via expertise-depth dimension; Ambiguity A5 |
| IC9 | Same-labels-for-default-propagation does NOT inherit | A1 chain | RE-TESTED & DOCUMENTED — A2 not composite-axis; labels chosen domain-meaningful instead |
| IC10 | Domain-meaningful labels `lay | aware | educated | trained | expert` | NEW — this inquiry | NEW commitment; anchored to Dreyfus + expertise-stratification literature |
| IC11 | Single-domain default | NEW — this inquiry | NEW commitment; source's domain implicit at runtime |
| IC12 | 9 handling actions (4 vocabulary + 4 discourse + 1 bridge) | NEW — this inquiry | NEW commitment; structured action ladder |

## Frontier Flags for Decomposition / Critique

- **FF1** Cross-domain example balance — each level should have at least 3 different domain examples (parallel to A1 cultural-reference-recognition's CC-B refinement note).
- **FF2** Forward-tagged 5 specialist canons integration — table or per-level inclusion?
- **FF3** How does A2 interact with A4 Purpose at runtime? Out of scope for this inquiry but noted.
- **FF4** Multi-domain texts (text crossing multiple specialist domains) — runtime concern; AI handles via its own knowledge; not a configuration concern.
- **FF5** Time-shift expertise drift (specialist may forget; amateur may study more) — snapshot assumption; refresh at config time.
