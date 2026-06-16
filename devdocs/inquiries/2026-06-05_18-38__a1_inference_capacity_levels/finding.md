---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-05_18-03__a1_idiom_recognition_levels/finding.md
---
# Finding: a1_inference_capacity_levels

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-05_18-03__a1_idiom_recognition_levels/finding.md` (immediately-prior sibling — sub-field 3; itself refines `a1_syntactic_processing_capacity_levels` → `a1_vocabulary_breadth_levels` → `translation_config_axes`).

**Revision trigger:** Continuation — sub-field 4 of A1. User asked: "now do it for inference-capacity."

**What's preserved:** A1 Reader Level as composite-axis with 5 sub-fields; sub-fields 1 (vocabulary), 2 (syntax), 3 (idiom) complete specs; 4-layer architecture; receptive-only; language-agnosticism; composite-axis default-propagation; same labels; A1↔A2 SEPARATE per sub-field; conservative-bias = LOWER for reader-axes; cross-sub-field dual-membership pattern (from idiom-recognition).

**What's changed:** No structural commitment altered. ADDS sub-field 4 specification.

**What's new:**
- 5 ordinal levels for inference-capacity (same labels)
- **MEDIUM-adapted 4-component template** (between idiom's LIGHT and syntax's HEAVY) — reader-profile + **inference-load tier** (umbrella with 6 sub-measures) + **register/genre-tier** + **gap-filling test sketch** with 6 primary actions (EXPLICATE / BRIDGE-CONNECTIVES / RESOLVE-ANAPHORA / UNPACK-COMPRESSION / ADD-BRIDGING-INFERENCES / KEEP-AS-IS) + 1 secondary (ADD-PRESUPPOSITION-CONTEXT)
- Strength-graded gap-filling per level
- Per-level text examples (Clark-Haviland general bridging + Henry James literary suspended inference + Said Nursi project-relevant istilzam chains at L4/L5)
- 4 adjacent-level boundary text pairs
- A1↔A2 boundary for inference with 4-domain specialist list (legal precedent / mathematical WLOG / medical clinical / scientific data-to-claim)
- **Cross-sub-field dual-membership case list** with cultural-reference-recognition (8 allusion-inference cases; parallel to idiom-recognition's pattern)
- **ORTHOGONALITY with syntactic-processing-capacity** made EXPLICIT (NEW) — inference-capacity and syntactic-processing-capacity are INDEPENDENT cognitive dimensions; the finding includes 4 concrete divergence scenarios documenting that a reader can have advanced syntax + daily inference, daily syntax + advanced inference, or matched levels
- Suggested migration mapping parallel to siblings
- Template-adaptation rationale (MEDIUM-heaviness comparison to LIGHT/HEAVY siblings)

## Question

**Context.** Sub-fields 1–3 of A1 are spec'd. This inquiry specifies **sub-field 4: inference-capacity** — "ability to fill in implicit information from context: ellipses, gaps, 'what the author means without saying it,' compressed or elliptical prose. A high-capacity reader follows compressed argument (e.g., a Said Nursi passage that telescopes a five-step logical chain into one sentence); a low-capacity reader needs the chain made explicit step by step."

**The question.** For inference-capacity, what should the 5 ordinal levels be — how much implicit content the reader fills in (compression depth, ellipsis tolerance, anaphora resolution, pragmatic inference, presupposition recognition, bridging inference), what distinguishes adjacent levels, what concrete textual examples illustrate each level, with a 4-component template adapted as needed?

**Goal.** Produce 5 mutually-distinct, ordinally-meaningful, spectrum-covering levels — each operationalizable as translator-AI prompt instruction (which implicit steps to fill explicitly), each with explicit distinguishing logic, each language-agnostic at concept.

**Scope.** Inference-capacity ONLY. The 1 remaining A1 sub-field (cultural-reference-recognition) will be the last.

## Finding Summary

- **5 level names match A1 headline labels.** Same labels across all A1 sub-fields for default-propagation; sub-field-specific semantics.

- **MEDIUM-adapted 4-component template** — between idiom's LIGHT (only substitution-test replaced) and syntax's HEAVY (full architectural restructure). Three components substantively adapted: frequency-tier → **inference-load tier** (umbrella with 6 sub-measures); register-tier → **register/genre-tier**; substitution-test → **gap-filling test** (6 primary actions). Reader-profile kept. Underlying tier+handling pattern preserved.

- **Inference-load tier has 6 sub-measures** (jointly characterizing inference cognitive load):
  1. **Compression-depth** — max telescoped steps the reader can fill (the user's seed measure: Said Nursi 5-step at advanced; native handles 5+ routinely)
  2. **Ellipsis-tolerance** — VP-ellipsis / gapping / sluicing / implicit subjects
  3. **Anaphora-distance** — within-sentence / cross-paragraph / section-level
  4. **Pragmatic-inference** — Gricean implicature recognition
  5. **Presupposition-recognition** — what the text assumes the reader knows
  6. **Bridging-inference** — Clark-Haviland causal/temporal implicit-link filling

- **6 primary gap-filling actions** (strength-graded per level):
  - **EXPLICATE** — make implicit step explicit
  - **BRIDGE-CONNECTIVES** — add explicit logical connectives
  - **RESOLVE-ANAPHORA** — make pronoun references explicit
  - **UNPACK-COMPRESSION** — expand telescoped multi-step chain into steps
  - **ADD-BRIDGING-INFERENCES** — make implicit causal/temporal connections explicit
  - **KEEP-AS-IS** — preserve compression for high-capacity readers

  Secondary: **ADD-PRESUPPOSITION-CONTEXT** (provide background the source presupposes).

- **`very_basic`** — recognizes essentially zero implicit content; needs every step explicit. Runtime: AGGRESSIVE all 6 primary actions.

- **`daily`** — handles 1-step Clark-Haviland bridging ("John went to the restaurant. The waiter was rude." reader infers "John saw the waiter"). Runtime: MODERATE — explicit connectives between most sentences.

- **`conversational`** — handles 2-step news-style implicit causal ("The bill passed the Senate yesterday. Critics decried it as rushed." reader infers political-process + critique-vs-passage link). Runtime: LIGHT — UNPACK-COMPRESSION for academic-rare 3+ step chains.

- **`advanced`** — handles 3-step compressed argument + suspended-thread (the user's seed: **Said Nursi 5-step telescoping** "Rahman → Rezzak → Rızk → Beka → Vücud → İlim/İrade/Kudret → Hayat" approaches the upper bound here, requiring UNPACK-COMPRESSION effort); Henry-James-style suspended inference. Runtime: MINIMAL — UNPACK for Said Nursi-style; KEEP-AS-IS most others.

- **`native`** — handles 5+ step compression routinely (full Said Nursi 7-step istilzam without effort); literary-extreme ellipsis (Faulkner stream-of-consciousness); cross-paragraph compressed argument; classical-Arabic / Quranic-style maximum compression. Runtime: NONE for general inference; only A2 specialist gets ADD-PRESUPPOSITION-CONTEXT.

- **A1↔A2 boundary for inference** explicit: A1 covers all GENERAL educated inference including literary-extreme (Said Nursi; Henry James; Quranic). A2 covers DOMAIN-SPECIALIST inference patterns:
  - **Legal:** precedent reasoning chains; "absent any showing that..." presupposition patterns
  - **Mathematical:** "WLOG" universal-generalization; "by induction"; "trivially follows"
  - **Medical:** differential diagnosis chains; clinical-reasoning conventions
  - **Scientific:** data-to-claim inference conventions ("results suggest")

- **Cross-sub-field dual-membership with cultural-reference-recognition** (parallel to idiom-recognition's pattern, but distinct in dimension). Allusion-inference cases require BOTH cultural-ref recognition AND inferring current-context relevance. 8 cases tagged here (Waterloo; Joan of Arc; Rubicon; Trojan horse; Cassandra; Sisyphean; Pyrrhic victory; Lazarus). Forward-looking cultural-reference-recognition column is recommendation only; the future cultural-ref sub-field inquiry will commit those tags authoritatively.

- **ORTHOGONALITY with syntactic-processing-capacity** explicit (NEW, central commitment of this finding). Inference-capacity and syntactic-processing-capacity measure INDEPENDENT cognitive dimensions:
  - **Advanced syntax + daily inference (rare but real):** word-by-word parser of Henry James who doesn't follow the argument
  - **Daily syntax + advanced inference (more common):** proverb/aphorism reader handling "Haste makes waste" (simple SVO syntax) with implicit causal chain (advanced inference)
  - **Both advanced:** typical educated literary reader
  - **Both very_basic:** child / brand-new L2

  The composite-axis pattern's sub-field-override mechanism handles cross-sub-field divergence cleanly. The orthogonality is documented to prevent users from assuming inference = syntax-capacity by default.

- **Conservative-bias = LOWER default** for inference_capacity.

- **Suggested migration mapping** parallel to siblings.

- **What's deferred.** Per-language inference-load thresholds (Japanese/Arabic high-context vs English news low-context per-language thresholds); specific conservative-bias default; **the last remaining A1 sub-field — cultural-reference-recognition** (which will independently tag the dual-membership cases from this finding's P6 + idiom-recognition's dual-membership table); runtime gap-filling implementation; pydantic dataclass shape.

## Finding

### How to read this finding

Body presents:
1. Cross-cutting framing constraints
2. MEDIUM-adapted 4-component template with rationale
3. Each of 5 levels
4. 4 adjacent-level boundary specs with text-pair examples
5. A1↔A2 boundary for inference
6. Cross-sub-field dual-membership case list
7. **Orthogonality with syntactic-processing-capacity** (NEW; central section)
8. Migration mapping

### Cross-cutting framing constraints

- **Receptive only.** "Fills implicit gaps when encountered."
- **Language-agnostic at concept.** Hall's high-context vs low-context distinction holds universally; specific thresholds per-language.
- **Same 5 labels across A1 sub-fields.**
- **Gap-filling test runtime concept** with 6 primary + 1 secondary actions.
- **Conservative-bias = LOWER default.**
- **ORTHOGONALITY with syntactic-processing-capacity** — explicit cross-reference to that section.
- **Cross-sub-field dual-membership** — explicit cross-reference.

### The MEDIUM-adapted 4-component template

Three components substantively adapted; reader-profile kept.

**1. Reader profile (kept).** Same shape.

**2. Inference-load tier (REPLACES frequency-tier).** *Why:* inferences are PROCESSES (not items like vocabulary or idioms); cognitive load is the right axis, not corpus frequency.

Umbrella with 6 sub-measures: compression-depth + ellipsis-tolerance + anaphora-distance + pragmatic-inference + presupposition-recognition + bridging-inference.

**3. Register/genre-tier (REFRAMED from register-tier).** *Why:* inference demand varies by genre. News = low; academic = high; poetry/literary = highest.

**4. Gap-filling test sketch (REPLACES substitution-test).** *Why:* runtime action is multi-action HANDLING (not single-word substitution; not lexical replacement; not structural restructuring).

Primary actions:
- **EXPLICATE** — make implicit step explicit
- **BRIDGE-CONNECTIVES** — add explicit logical connectives
- **RESOLVE-ANAPHORA** — make pronoun references explicit
- **UNPACK-COMPRESSION** — expand telescoped chain into separate steps
- **ADD-BRIDGING-INFERENCES** — make implicit causal/temporal connections explicit
- **KEEP-AS-IS** — preserve compression

Secondary: **ADD-PRESUPPOSITION-CONTEXT**.

Strength-graded per level: aggressive at very_basic; none at native for general inference.

**Why MEDIUM and not LIGHT:** three components adapted (vs idiom's one). Frequency-tier doesn't apply to processes.

**Why MEDIUM and not HEAVY:** the architectural pattern parallels syntactic-processing-capacity (inference-load tier ↔ structural-complexity tier; gap-filling actions ↔ restructuring actions). Pattern preserved with component-content adapted.

The principle remains: **adapt where needed; preserve where it fits.** Inferences are PROCESSES — closer to syntax (also process-based) than to vocabulary/idioms (item-based).

### Level 1 — `very_basic`

**Reader profile.** Young child age 4–6 reading early-reader books, or brand-new L2 in first weeks. Recognizes essentially zero implicit content; treats every text as the literal sequence of stated propositions.

Anchor demographics: child age 4–6; absolute-beginner L2 learner.

**Genre anchor.** Early-reader explicit-step prose; children's signs.

**Inference-load tier:**
- Compression-depth: 0
- Ellipsis-tolerance: 0
- Anaphora-distance: ≤1 sentence
- Pragmatic-inference: literal-only
- Presupposition-recognition: minimal
- Bridging-inference: 0

**Register/genre-tier.** Children's signs / early-reader instructional with all steps explicit.

**Gap-filling test sketch.** AGGRESSIVE all 6 primary actions. Every implicit step EXPLICATED; every logical connection BRIDGE-CONNECTIVES added; every pronoun RESOLVE-ANAPHORA; every compression UNPACK-COMPRESSION; every causal/temporal link ADD-BRIDGING-INFERENCES; every presupposition ADD-PRESUPPOSITION-CONTEXT.

**Positive examples** (explicit-step prose):
- "John went to the restaurant. John saw the waiter. The waiter was rude. Because the waiter was rude, John was unhappy."

**Negative examples** (above very_basic): Clark-Haviland 1-step ("John went to the restaurant. The waiter was rude." — implicit "John saw the waiter").

### Level 2 — `daily`

**Reader profile.** Functional adult in daily life (backpacker / new immigrant / functional L2). Handles 1-step Clark-Haviland bridging; simple anaphora.

Anchor demographics: backpacker; new immigrant; L2 learner after a few months immersion.

**Genre anchor.** Practical guides; simple news with explicit connectives.

**Inference-load tier:**
- Compression-depth: ≤1 step
- Ellipsis-tolerance: minimal (canonical ellipsis only)
- Anaphora-distance: ≤2 sentences
- Pragmatic-inference: obvious Gricean
- Presupposition-recognition: common cultural
- Bridging-inference: 1-step Clark-Haviland

**Register/genre-tier.** Practical guides + simple news with explicit connectives. Excludes multi-step compression, academic-rare, dense literary.

**Gap-filling test sketch.** MODERATE. BRIDGE-CONNECTIVES between most sentences; ADD-BRIDGING-INFERENCES for unstated causal links; RESOLVE-ANAPHORA when antecedent is more than 1–2 sentences away.

**Positive examples** (Clark-Haviland 1-step):
- "John went to the restaurant. The waiter was rude." (reader infers "John saw the waiter")
- "She bought a cake. The candles were beautiful." (reader infers "the cake had candles")
- "He went home because he was hungry. There was nothing in the fridge."

**Negative examples** (above daily): news-style 2-step ("The bill passed the Senate yesterday. Critics decried it as rushed."); academic compression; Said Nursi 5-step.

### Level 3 — `conversational`

**Reader profile.** Average newspaper-reading educated adult. Handles 2-step news-style implicit causal; cross-paragraph anaphora.

Anchor demographics: high-school-educated adult; competent L2 reader at CEFR B1–B2 inference range; casual reader of mainstream non-fiction.

**Genre anchor.** Mainstream journalism + popular non-fiction.

**Inference-load tier:**
- Compression-depth: ≤2 steps
- Ellipsis-tolerance: VP-ellipsis, gapping, simple sluicing
- Anaphora-distance: cross-paragraph
- Pragmatic-inference: standard Gricean
- Presupposition-recognition: educated-general
- Bridging-inference: 2-step news-style

**Register/genre-tier.** Mainstream journalism + popular non-fiction + well-written conversational prose. Excludes academic-compressed, literary-suspended, A2 specialist.

**Gap-filling test sketch.** LIGHT. UNPACK-COMPRESSION only for academic-rare 3+ step chains; news-style implicit connectives acceptable.

**Positive examples:**
- "The Senate bill passed yesterday. Critics decried it as rushed." (implicit political-process bridging)
- "The team rallied late but fell short. Their coach offered no excuses."
- "Markets rose despite the report. Analysts attributed the resilience to forward guidance."

**Negative examples** (above conversational): Said Nursi 5-step; Henry-James suspended inference; A2 specialist (legal precedent).

### Level 4 — `advanced`

**Reader profile.** University-educated reader, skilled non-native who reads widely, or educated professional. Handles 3-step compressed argument; the user's seed anchor — **Said Nursi 5-step telescoping** — sits at the upper bound here, requiring UNPACK-COMPRESSION effort.

Anchor demographics: university-educated professional; humanities graduate student; skilled non-native reader of literary fiction.

**Genre anchor.** Academic articles + contemporary literary fiction + Said Nursi-style compressed argument + Henry-James-style suspended inference.

**Inference-load tier:**
- Compression-depth: ≤3 steps (Said Nursi 5-step approaches upper bound)
- Ellipsis-tolerance: academic + literary ellipsis
- Anaphora-distance: long (multi-paragraph; section-level)
- Pragmatic-inference: literary-academic implicature
- Presupposition-recognition: academic-general + literary-canonical (Shakespeare; mythology)
- Bridging-inference: 3-step + suspended-thread

**Register/genre-tier.** Academic + contemporary literary + dense argumentative. Excludes 5+-step routine, archaic-Biblical poetic compression, A2 specialist.

**Gap-filling test sketch.** MINIMAL. UNPACK-COMPRESSION for Said Nursi-style 5-step (with effort); KEEP-AS-IS most others; ADD-PRESUPPOSITION-CONTEXT for A2 specialist.

**Positive examples:**
- **Said Nursi 5-step (user's seed):** "Rahman (the Merciful) implies Rezzak (the Provider), which presupposes Rızk (sustenance), which requires Beka (continuity), which entails Vücud (existence), which necessitates İlim, İrade, Kudret (knowledge, will, power), which presuppose Hayat (life)." — 7 attributes unpacked from one word via logical-necessity chain.
- **Henry-James suspended:** "Whether what one called success would, in this case, prove sufficient — the kind of sufficiency, that is, that one had learnt to expect — remained, as ever, a question whose answer, though tacitly approached, was not, in fact, given."
- **Academic compressed argument:** "The intervention's failure — itself a contested verdict — speaks less to the design than to the unmeasured confounders that, despite extensive controls, remained available to alternative explanations."
- **"He met his Waterloo"** *(dual-membership)*
- **"Their Trojan horse strategy"** *(dual-membership)*

**Negative examples** (above advanced):
- A1.native: full Said Nursi 7-step routine; Faulkner stream-of-consciousness; Quranic compressed argument
- A2 specialist: legal "absent any showing"; mathematical "WLOG"; medical differential diagnosis

### Level 5 — `native`

**Reader profile.** Educated native reading broadly across literary registers including classical-rare, archaic, and literary-extreme. Handles 5+ step compression routinely (full Said Nursi istilzam without effort); literary ellipsis (poetic compression); cross-paragraph compressed argument.

Anchor demographics: literature scholar; broadly-read native of Henry James / Faulkner / KJV-Pauline / Tolkien / Shakespeare.

**Genre anchor.** Said Nursi istilzam routine + Henry James + Faulkner stream-of-consciousness + classical-Arabic / Quranic compressed argument + KJV-Pauline.

**Inference-load tier:**
- Compression-depth: 5+ routine
- Ellipsis-tolerance: poetic + literary-extreme
- Anaphora-distance: unlimited within general literary
- Pragmatic-inference: full literary-rhetorical incl. archaic
- Presupposition-recognition: literary-canonical + archaic + Biblical + classical
- Bridging-inference: 5+ step + non-linear (associative, thematic, symbolic)

**Register/genre-tier.** ALL general literary registers incl. Quranic / classical-Arabic / KJV-Pauline / Henry James / Faulkner / Said Nursi. Excludes ONLY A2 specialist domain inference.

**Gap-filling test sketch.** NONE for general inference. KEEP-AS-IS for all general. Only A2 specialist-domain inference patterns get ADD-PRESUPPOSITION-CONTEXT.

**Positive examples:**
- **Full Said Nursi 7-step istilzam routine** (parsed without effort)
- **Faulkner stream-of-consciousness** (implicit threading across paragraphs)
- **Quranic-style compressed argument** (classical-Arabic; maximum compression)
- **KJV-Pauline:** "Through Him to whom be glory, the work was done — yea, the work which, ordained before the foundations were laid, awaited only the appointed hour."
- **"Crossing the Rubicon"** *(dual-membership)*
- **"Sisyphean labor"** *(dual-membership)*

**Negative examples (A2 specialist only):**
- Legal: "Absent any showing that the defendant acted with malice, the doctrine of qualified immunity attaches."
- Mathematical: "WLOG (without loss of generality), let x ∈ ℝ. By induction..."
- Medical: differential diagnosis chains
- Scientific: data-to-claim conventional inference

### Adjacent-level boundary specs

#### Boundary 1 — `very_basic` ↔ `daily`

**Principle.** From explicit-everything to 1-step Clark-Haviland bridging.

**Text pair:** explicit-all ("John went to the restaurant. John saw the waiter. The waiter was rude.") ↔ Clark-Haviland 1-step ("John went to the restaurant. The waiter was rude.")

#### Boundary 2 — `daily` ↔ `conversational`

**Principle.** From Clark-Haviland 1-step to news-style 2-step + cross-paragraph anaphora.

**Text pair:** "John went to the restaurant because he was hungry. The waiter was rude." (daily) ↔ "The bill passed the Senate yesterday. Critics decried it as rushed." (conversational; implicit political-process + critique-vs-passage)

#### Boundary 3 — `conversational` ↔ `advanced`

**Principle.** From news-style 2-step to 3-step + suspended-thread compressed argument. **Said Nursi 5-step approaches upper bound here.**

**Text pair:** "The Senate bill faces opposition for being rushed." (conversational) ↔ Said Nursi 5-step istilzam condensed into single sentence (advanced; UNPACK-COMPRESSION with effort).

#### Boundary 4 — `advanced` ↔ `native`

**Principle.** From 3-step + Said Nursi-approaching to 5+ step routine + literary-extreme ellipsis + Quranic-style compression.

**Text pair:** Said Nursi 5-step condensed (advanced — readers UNPACK with effort) ↔ full Said Nursi 7-step istilzam routine + Faulkner stream-of-consciousness + Quranic compression (native — no effort).

### A1↔A2 boundary clarification for inference

**Test:** "Does parsing this argument's IMPLICIT STRUCTURE require subject-domain training, or only broad general reading?"

**Specialist-domain inference list:**

**Legal** (require legal training):
- "Absent any showing that the defendant acted with malice, the doctrine of qualified immunity attaches."
- "By operation of law, the precedent set in [case] compels..."
- "It is well-settled that, in the absence of statutory authority..."

**Mathematical** (require mathematical training):
- "WLOG (without loss of generality), let x ∈ ℝ. By induction..."
- "Trivially, it follows that f is continuous on the closed interval."
- "By the principle of mathematical induction, the result extends to all n ∈ ℕ."

**Medical** (require medical training):
- Differential diagnosis chains
- "Suggestive of a paraneoplastic syndrome; further workup indicated."
- Clinical-reasoning conventions

**Scientific** (require scientific training):
- "Results suggest..." — data-to-claim
- "Consistent with the hypothesis that..." — statistical-presupposition
- "By the principle of..." — domain-axiom implicit-invocation

**Borderline (A1, NOT A2):** humanities-general inference chains; literary-criticism inference; academic-philosophy inference — these are general educated reading, not domain-specialist training.

### Cross-sub-field dual-membership case list

These expressions require BOTH inferring current-argument relevance AND recognizing the cultural reference. Tagged here at inference-capacity level; the cultural-reference-recognition future inquiry will independently tag them.

| Expression | Inference-capacity level (THIS commitment) | Cultural-reference level (forward-looking; future inquiry) | Source |
|---|---|---|---|
| "He met his Waterloo" | advanced | advanced *(suggested)* | Napoleon 1815 |
| "She was their Joan of Arc" | advanced | advanced *(suggested)* | French history |
| "Crossing the Rubicon" | native | native *(suggested)* | Caesar 49 BCE |
| "Their Trojan horse strategy" | advanced | advanced *(suggested)* | Iliad/Aeneid + modern |
| "He played the Cassandra role" | advanced | native *(suggested)* | Greek myth |
| "Sisyphean labor" | advanced | native *(suggested)* | Greek myth |
| "Pyrrhic victory" (argument context) | advanced | advanced *(suggested)* | Pyrrhus |
| "He came back like Lazarus" | advanced | native *(suggested)* | Bible Gospel of John |

**Important annotations:**
1. **Forward-looking column is NOT committed** by this finding. Future cultural-reference-recognition inquiry will set those values.
2. **Cross-list overlap with idiom-recognition's dual-membership table.** "Trojan horse"; "Pyrrhic victory"; "Crossing the Rubicon"; "Catch-22" appear in BOTH lists. These expressions are simultaneously idioms (fixed expressions with figurative meaning) AND allusion-inference cases (require inferring current-argument relevance). A reader at advanced inference-capacity but daily idiom-recognition can recognize the allusion-inference but not the fixed-idiom status — rare but real.
3. **Both sub-fields measure independent dimensions** that happen to address overlapping vocabulary territory.

### Orthogonality with syntactic-processing-capacity

This is the **central NEW commitment of this finding** — explicit documentation that inference-capacity is INDEPENDENT of syntactic-processing-capacity. Parsing dense nested syntax (working-memory load on STRUCTURE) is operationally distinct from filling implicit logical steps (working-memory load on INFERENCE).

**4 concrete divergence scenarios:**

#### Example 1 — Advanced syntax + daily inference (rare but real)

**Profile.** A careful word-by-word parser of Henry James who can hold 3 clauses in suspension and resolve the nested-relative-clause structure, but doesn't follow the argument when it's compressed.

**Text scenario.** A long Henry-James-style sentence with 3-clause suspension AND an explicit-stepped argument → reader handles parsing (advanced syntax) but if the argument were compressed (Said Nursi 5-step), reader fails (daily inference).

**Composite-axis configuration.** A1 headline = `conversational`; `syntactic_processing_capacity` override = `advanced`; `inference_capacity` override = `daily`.

#### Example 2 — Daily syntax + advanced inference (more common)

**Profile.** Aphorism / proverb reader.

**Text scenario.** "Haste makes waste." (simple SVO — daily syntax) requires inferring causal chain "haste → reduced attention → errors → wasted effort" (advanced inference). Or: "All that glitters is not gold." (simple SVO — daily syntax) requires inferring meta-rhetorical "appearances can deceive" (advanced inference). Cultural traditions of aphoristic wisdom (Confucian Analects; Sufi sayings; Talmudic sayings) develop this profile.

**Composite-axis configuration.** A1 headline = `conversational`; `syntactic_processing_capacity` override = `daily`; `inference_capacity` override = `advanced`.

#### Example 3 — Both at advanced (typical educated literary reader)

**Profile.** University-educated reader of dense literary fiction.

**Text scenario.** Literary-extreme prose (Henry James + Said Nursi-style) demanding BOTH suspended parsing AND compressed inference.

**Composite-axis configuration.** A1 headline = `advanced` (default propagates both).

#### Example 4 — Both at very_basic (early reader)

**Profile.** Child or brand-new L2 learner.

**Text scenario.** Explicit-SVO + explicit-causal-links.

**Composite-axis configuration.** A1 headline = `very_basic` (default propagates both).

**Implication for composite-axis configuration:** the sub-field-override mechanism handles cross-sub-field divergence cleanly. The orthogonality is documented to prevent users from assuming `inference_capacity` = `syntactic_processing_capacity` by default; for the rare-but-real profiles (Examples 1 and 2), the override mechanism enables accurate configuration.

**Why this orthogonality matters operationally:** the translator-AI's gap-filling decisions (UNPACK-COMPRESSION; ADD-BRIDGING-INFERENCES) depend on inference-capacity; its restructuring decisions (SPLIT; UNEMBED; LINEARIZE) depend on syntactic-processing-capacity. Conflating them produces wrong translator behavior in the rare-but-real cases.

### Migration mapping from existing `AUDIENCE_LEVEL`

| Existing | New (inference-capacity) | Rationale |
|---|---|---|
| `late_learner_simple` | `daily` | Existing label captures readers needing simpler implicit-content; matches `daily` (1-step Clark-Haviland bridging only). |
| `late_learner` | `conversational` | Late-learner adults handle news-style 2-step bridging. |
| `native` | `native` | Identity mapping. |

**New positions:**
- `very_basic` extends below for child / brand-new-L2 readers needing every step explicit.
- `advanced` fills middle for university-educated readers handling Said Nursi 5-step compressed argument.

## Inherited Commitments Re-test

This finding refines `a1_idiom_recognition_levels` (sibling) which refines syntactic-processing-capacity which refines vocabulary-breadth which refines translation_config_axes.

- **Commitment:** A1 Reader Level composite-axis with 5 sub-fields.
  - **Source:** `translation_config_axes/finding.md`
  - **Re-test status:** RE-TESTED
  - **Evidence:** This finding instantiates the 4th sub-field.

- **Commitment:** A1 measures RECEPTIVE capacity.
  - **Re-test status:** RE-TESTED
  - **Evidence:** All level prose uses recognition verbs ("fills implicit gaps when encountered"; "treats every text as the literal sequence"; "does not recognize"). Verified by critique D2.

- **Commitment:** Language-agnostic at concept.
  - **Re-test status:** RE-TESTED
  - **Evidence:** Inference-load tier's 6 sub-measures are universal cognitive operations; per-language thresholds deferred. Hall high-context vs low-context applies.

- **Commitment:** Same labels across A1 sub-fields.
  - **Re-test status:** RE-TESTED
  - **Evidence:** This finding adopts same 5 labels; semantics sub-field-specific.

- **Commitment:** Conservative-bias for reader-axes = LOWER.
  - **Re-test status:** RE-TESTED
  - **Evidence:** Applied to inference_capacity.

- **Commitment:** A1↔A2 boundary as SEPARATE per-sub-field.
  - **Re-test status:** RE-TESTED with EXTENSION
  - **Evidence:** Now 4 separate A1↔A2 boundaries (vocabulary, syntax, idiom, inference). Specialist-domain inference patterns identified (legal/mathematical/medical/scientific).

- **Commitment:** Template adaptation principled.
  - **Re-test status:** RE-TESTED with REINFORCEMENT
  - **Evidence:** Syntax was HEAVY; idiom was LIGHT; inference is MEDIUM. The principle "adapt where needed; preserve where it fits" continues to produce calibrated adaptations.

- **Commitment:** Cross-sub-field dual-membership handled per sub-field independently.
  - **Source:** `a1_idiom_recognition_levels/finding.md`
  - **Re-test status:** RE-TESTED with EXTENSION
  - **Evidence:** Applied to inference-capacity's dual-membership with cultural-reference-recognition (allusion-inference cases). EXTENSION: cross-list overlap with idiom-recognition's table explicitly acknowledged.

- **Commitment:** 4-layer framework architecture.
  - **Re-test status:** INHERITED-WITHOUT-RE-TEST
  - **Reason:** Out of scope.

- **Commitment:** POLICY layer items always-on.
  - **Re-test status:** INHERITED-WITHOUT-RE-TEST
  - **Reason:** Out of scope. Acknowledged interaction: register-preservation policy interacts with inference-capacity (academic register has high inference demand; preserving it requires keeping compression at high levels).

## Next Actions

### MUST

- **What:** Define 5 level values + 4-component specs for the LAST remaining A1 sub-field: cultural-reference-recognition. The cultural-reference-recognition inquiry will INDEPENDENTLY tag the dual-membership cases from BOTH idiom-recognition's table AND this inquiry's allusion-inference table.
  - **Who:** the next follow-up inquiry.
  - **Gate:** before A1 Reader Level can be fully instantiated.
  - **Why:** A1 requires all 5 sub-fields specified.

### COULD

- **What:** Define per-language inference-load thresholds (Japanese / Arabic high-context vs English news low-context).
  - **Who:** per-language inquiry.
  - **Gate:** when Comprehenslate adds the target language.

- **What:** Specific conservative-bias default value for `inference_capacity`.
  - **Who:** defaults inquiry.

- **What:** Define Purpose-driven default-derivation.
  - **Who:** defaults inquiry.

### DEFERRED

- **What:** Runtime gap-filling implementation (LLM-judged vs structured inference-graph backed).
  - **Gate:** when level enums committed.

- **What:** Translate to pydantic `inference_capacity: Literal[...]` field.
  - **Gate:** structural-layer inquiry.

- **What:** Migration from `AUDIENCE_LEVEL`.
  - **Gate:** when production systems wire up the new axis.

## Reasoning

### What survived

Final Recommended Assembly (E2 from critique) survives all 13 dimensions including NEW **D13 (Orthogonality-with-syntax coherence)**.

### Significant alternatives rejected

- **HEAVY adaptation paralleling syntax** (over-restructures; the tier+handling pattern is preserved naturally).
- **LIGHT adaptation paralleling idiom** (under-restructures; three components genuinely need adaptation).
- **Splitting inference-load tier into 4–6 separate components** (over-engineers; sub-measures are correlated; one umbrella matches the syntactic-processing-capacity model).
- **Collapsing gap-filling actions to 2–3** (loses operational distinctions across the 6 sub-measures).
- **Collapsing inference-capacity with syntactic-processing-capacity** (orthogonality verified by edge-case profiles — Examples 1 and 2 in the body).
- **All-inference-is-A1** (specialist-domain patterns require domain training).
- **Said Nursi as defining anchor** (over-narrows; triangulate with Clark-Haviland and Henry James).
- **Productive framing** (receptive only per inherited principle).

### Why the template adaptation is MEDIUM (not LIGHT, not HEAVY)

Three siblings provide adaptation precedents:
- **Idiom-recognition (LIGHT):** only substitution-test replaced; frequency-tier and register-tier light prefix-rename. Idioms behave like vocabulary in frequency+register distributions.
- **Syntactic-processing-capacity (HEAVY):** frequency-tier replaced entirely; register-tier fundamentally reframed; substitution-test replaced. Sentences don't follow Zipfian distributions; syntactic register has its own dynamics.
- **Inference-capacity (MEDIUM):** three components substantively adapted (frequency-tier → inference-load tier; register-tier → register/genre-tier; substitution-test → gap-filling test). Underlying tier+handling pattern preserved (parallels syntactic-processing-capacity's structure).

The principle "adapt where needed; preserve where it fits" continues to produce calibrated adaptations.

### Why orthogonality with syntactic-processing-capacity is documented explicitly

Inference-capacity and syntactic-processing-capacity could appear collapsible — both are about cognitive load on working memory. But the loads are on DIFFERENT TARGETS:
- Syntactic-processing-capacity: parsing STRUCTURE (does the reader hold 3 clauses in suspension?)
- Inference-capacity: filling INFERENCE (does the reader fill 3 missing causal steps?)

These are independent operations. The 4 concrete divergence scenarios (advanced syntax + daily inference; daily syntax + advanced inference; both advanced; both very_basic) document the independence with real reader profiles. Documenting the orthogonality prevents users from assuming `inference_capacity` = `syntactic_processing_capacity` by default, which would produce wrong translator behavior in the rare-but-real cases.

## Open Questions

### Refinement Triggers

- **Per-level anchor refinement.** If translator-AI mis-judges an anchor text consistently, revisit.
- **Cross-sub-field dual-membership extension** (especially after cultural-reference-recognition inquiry completes).
- **Said Nursi 5-step vs 7-step boundary refinement.** The advanced/native boundary uses "5-step approaches upper bound at advanced; 7-step routine at native." If empirical user feedback shows the 5/7 boundary is too granular, simplify.

### Research Frontiers

- **Per-language inference-load thresholds.** Japanese / Arabic high-context default-inference-demand higher than English news; per-language inquiry will produce thresholds.

- **Inference vs syntax independence empirical study.** The 4 divergence scenarios are theoretically justified; future empirical user studies could verify (and possibly refine) the independence claim.

### Monitoring

- **AUDIENCE_LEVEL usage statistics.** Migration mapping assumes existing labels used as semantically intended.

### Blocked

- **Default value selection** — defaults inquiry covers all 8 axes jointly.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
now do it for  inference-capacity
```

</details>
