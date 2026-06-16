# Decomposition — a1_vocabulary_breadth_levels

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/_branch.md` (with prior outputs: `surfacing.md` and `sensemaking.md` in the same folder)

---

## The Whole Being Decomposed

The vocabulary-breadth 5-level spec as sensemaking SV6 stabilized it: 5 levels named `very_basic | daily | conversational | advanced | native`, each with a 4-component definition (reader-profile + frequency-tier band + register-tier inclusion + substitution-test sketch), with adjacent-level boundary pairs and an explicit A1↔A2 (general vs subject-domain) boundary, all phrased language-agnostically (English examples illustrative only), receptive-only, with same-labels-for-default-propagation across A1 sub-fields and a suggested migration mapping from the existing 3-level `AUDIENCE_LEVEL` knob.

The job of decomposition: partition this conceptual whole into pieces that can each be specified independently with explicit interfaces and reassemble into the inquiry's deliverable.

---

## Step 1 — Perceive Coupling Topology

### Elements

| # | Element |
|---|---|
| E1–E5 | The 5 level specs (very_basic, daily, conversational, advanced, native) — each comprising name + reader-profile + frequency-tier + register-tier + substitution-test sketch |
| E6 | The 4-component definition pattern (template that all 5 levels instantiate) |
| E7 | Adjacent-level boundary pairs (4 boundaries: L1↔L2, L2↔L3, L3↔L4, L4↔L5) |
| E8a | Per-level positive examples (words AT each level) |
| E8b | Per-level negative examples (words ABOVE each level) |
| E8c | Boundary-pair examples (word pairs at each adjacent-level transition) |
| E9 | A1↔A2 boundary clarification (general vs subject-domain; subject-domain-training test) |
| E10 | A1↔A2 borderline-words table (edge cases: eschatology, transubstantiation, myocardial infarction, ratiocination, ostensibly, verily, anon, etc.) |
| E11 | Anchor demographics per level (real, recognizable reader types) |
| E12 | Migration mapping from existing AUDIENCE_LEVEL (3 levels → subset of 5 new) |
| E13 | Conservative-bias-for-reader-axes principle (informs future default selection; not the actual default) |
| E14 | Receptive-only constraint (applies to all level prose) |
| E15 | Language-agnostic concept-statement (applies per-level and cross-cutting) |
| E16 | Same-labels-across-A1-sub-fields note (default-propagation discipline) |
| E17 | Substitution-test runtime CONCEPT (not implementation) |
| E18 | Scope boundary (this inquiry vs future inquiries) |

### Coupling map (pairwise)

| Pair | Strength | Notes |
|---|---|---|
| E1–E5 ↔ E6 4-component template | STRONG | Each level instantiates the template |
| E1 ↔ E2 (adjacent levels) | MODERATE | Defined relative via the L1↔L2 boundary |
| E2 ↔ E3, E3 ↔ E4, E4 ↔ E5 | MODERATE | Same adjacency dynamic |
| E1 ↔ E3 (non-adjacent) | WEAK | Only transitively related |
| E1–E5 ↔ E7 boundary pairs | STRONG | Each boundary spans two adjacent levels |
| E1–E5 ↔ E8a/E8b per-level examples | STRONG | Examples belong to specific levels |
| E7 ↔ E8c boundary-pair examples | STRONG | Boundary pairs illustrate transitions |
| E4 + E5 ↔ E9 A1↔A2 boundary | MODERATE | The boundary mainly affects L4 (advanced) and L5 (native) substitution-test sketches |
| E9 ↔ E10 borderline-words table | STRONG | Table operationalizes the boundary |
| E1–E5 ↔ E11 anchor demographics | STRONG | Demographics are part of each level's reader-profile component |
| E12 migration ↔ E1–E5 names | MODERATE | Mapping references specific levels |
| E13 conservative-bias principle ↔ E1–E5 | WEAK | Principle is meta; specific defaults deferred |
| E14 receptive-only ↔ all level prose | STRONG | Constraint applies universally |
| E15 language-agnostic ↔ E1–E5 | STRONG | Each level carries the claim |
| E16 same-labels ↔ E1–E5 names | STRONG | Label commitment is the names |
| E17 substitution-test concept ↔ E1–E5 sketches | STRONG | Sketches reference the concept |
| E18 scope ↔ all | WEAK | Meta-information |

### Clusters

- **Cluster 1 — Per-Level Specs.** E1–E5 + their per-level examples (E8a, E8b) + reader-profile demographics (E11) + 4-component template instantiation. High internal coupling.
- **Cluster 2 — Adjacent-Level Boundaries.** E7 (4 boundary distinctions) + E8c (boundary-pair examples).
- **Cluster 3 — A1↔A2 Boundary.** E9 + E10 borderline-words table. Conceptually distinct from adjacent-level boundaries.
- **Cluster 4 — Migration & Scope Framing.** E12 (migration mapping) + E13 (conservative-bias principle reference) + E18 (scope boundary).
- **Cluster 5 — Cross-Cutting Notes.** E14 (receptive-only) + E15 (language-agnostic) + E16 (same-labels) + E17 (substitution-test concept). These constraints apply to ALL level definitions.
- **Cluster 6 — Template.** E6 alone — the 4-component definition pattern.

### Valleys

| Boundary | Strength | Notes |
|---|---|---|
| Cluster 1 (Per-level) ↔ Cluster 2 (Adjacent boundaries) | MODERATE | Boundaries reference level specs; specs don't reference boundaries |
| Cluster 1 ↔ Cluster 3 (A1↔A2) | LOW-MODERATE | A1↔A2 affects L4 + L5 substitution-test sketches |
| Cluster 1 ↔ Cluster 5 (Cross-cutting) | LOW | Cross-cutting applies universally; specs honor it without reference |
| Cluster 1 ↔ Cluster 6 (Template) | STRONG | Each spec instantiates the template — handled by dependency order (template before specs) |
| Cluster 2 ↔ Cluster 3 | LOW | Different boundary concepts |
| Cluster 4 ↔ All | LOW | Migration and scope are meta-level |

---

## Step 2 — Detect Boundaries (Top-Down)

| # | Boundary | Coupling across | Rationale |
|---|---|---|---|
| **B1** | Per-level specs ↔ Adjacent-level boundaries | MODERATE | Each level specifiable individually; boundaries are about TRANSITIONS |
| **B2** | Per-level specs ↔ A1↔A2 boundary | LOW | A1↔A2 is a separate conceptual boundary; affects L4/L5 specifically |
| **B3** | Level definitions ↔ Migration mapping | LOW | Mapping is meta-information |
| **B4** | Level definitions ↔ Cross-cutting notes | LOW | Cross-cutting notes apply universally; per-level specs honor them |
| **B5** | Between individual levels (E1↔E2↔...↔E5) | LOW | Each level spec is independent given the template + cross-cutting constraints |
| **B6** | Template ↔ Spec instances | STRONG-but-sequential | Template defined first; specs instantiate |

### Initial partition

| Piece | Cluster | Description |
|---|---|---|
| **P1** | Cluster 5 | Cross-cutting framing constraints (receptive-only, language-agnostic, same-labels, substitution-test concept) |
| **P2** | Cluster 6 | The 4-component definition template (the structure each level uses) |
| **P3** | Cluster 1 | The 5 individual level specs. Sub-decomposes into P3.1–P3.5 |
| **P4** | Cluster 2 | Adjacent-level boundary pairs. Sub-decomposes into P4.1–P4.4 |
| **P5** | Cluster 3 | A1↔A2 boundary clarification + borderline-words table |
| **P6** | Cluster 4 | Migration mapping from existing AUDIENCE_LEVEL |
| **P7** | Cluster 4 | Scope boundary (deliverable vs deferred) |

---

## Step 3 — Validate Boundaries (Bottom-Up Check)

### Atoms

- 5 level NAMES
- 5 reader-profile sentences (one per level)
- 5 frequency-tier band statements (English-illustrative)
- 5 register-tier inclusion lists
- 5 substitution-test sketches
- 4 adjacent-level boundary principles + 4 boundary-pair example sets
- A1↔A2 boundary test phrase
- ~10 A1↔A2 borderline-word classifications
- Migration mapping (5 entries: 3 existing + 2 new positions)
- Receptive-only reminder (1 atom)
- Language-agnostic claim (1 atom + per-level instances)
- Same-labels-for-default-propagation note (1 atom)
- Substitution-test runtime concept (1 atom)
- Scope boundary table (deliverables + deferrals)
- Conservative-bias principle reference (1 atom)
- 4-component template structure (1 atom)
- Per-level positive examples (~5-7 per level × 5 levels)
- Per-level negative examples (~3-5 per level × 5 levels)
- Anchor demographics (1 per level × 5 levels)

### Atom-to-cluster mapping

- Per-level atoms (name, profile, tier, register, substitution, positive examples, negative examples, demographics) → P3 (per-level specs) ✓
- Boundary distinctions + boundary-pair examples → P4 ✓
- A1↔A2 boundary + borderline-words table → P5 ✓
- Migration mapping → P6 ✓
- Cross-cutting atoms → P1 ✓
- 4-component template → P2 ✓
- Scope boundary table + conservative-bias reference → P7 ✓

All atoms map cleanly. No atoms stranded.

### Confidence verdict

| Boundary | Top-down | Bottom-up | Confidence |
|---|---|---|---|
| B1 per-level ↔ adjacent boundaries | ✓ | ✓ | HIGH |
| B2 per-level ↔ A1↔A2 | ✓ | ✓ | HIGH |
| B3 levels ↔ migration | ✓ | ✓ | HIGH |
| B4 levels ↔ cross-cutting | ✓ | ✓ | HIGH |
| B5 between individual levels | ✓ | ✓ | HIGH |
| B6 template ↔ specs | ✓ | ✓ (sequential) | HIGH |

All boundaries confident. Proceed.

---

## Step 4 — Express as Question Tree

### Top-level question (the whole)

**What are the 5 vocabulary-breadth levels — their names, 4-component definitions, examples, adjacent-level boundaries, A1↔A2 boundary clarification, and migration mapping from existing AUDIENCE_LEVEL — specified such that each level is operationalizable as a translator-AI prompt instruction, the spec is internally consistent, and all level concepts are language-agnostic?**

### Question tree

#### **P1 — Cross-cutting framing constraints**

**Question:** What constraints apply to ALL level definitions in this spec, and what cross-cutting notes set the universal context?

**Verification criteria:**
- [ ] **Receptive-only constraint** stated: all level prose phrased in recognition terms ("recognizes," "understands when encountered," "does not pause at"); no productive verbs ("uses," "speaks," "writes").
- [ ] **Language-agnosticism claim** stated: level CONCEPTS are universal (frequency-tier, register-tier exist in every language); English examples are illustrative, not definitional.
- [ ] **Same-labels-for-default-propagation note** stated: vocabulary_breadth's 5 labels equal A1 headline's 5 labels for clean default-propagation; each A1 sub-field carries its own semantics for those labels.
- [ ] **Substitution-test runtime CONCEPT** defined: at level L, the translator-AI replaces words above L with equivalents at or below L. Runtime IMPLEMENTATION (LLM-judged vs frequency-list-backed) is explicitly deferred.
- [ ] **Conservative-bias-for-reader-axes principle** referenced: for reader-facing axes, conservative-bias means LOWER default (assume less reader competence). Specific default value is deferred to a future defaults inquiry.

---

#### **P2 — The 4-component definition template**

**Question:** What is the standard 4-component template each level uses, and what prose shape does each component take?

**Verification criteria:**
- [ ] Template's 4 components named: (1) reader-profile + name; (2) frequency-tier band; (3) register-tier inclusion; (4) substitution-test sketch.
- [ ] **Component 1 (Reader profile + name)** format: "**[level_name]** — Reader profile: [demographic description]" (one sentence describing the typical reader at this level).
- [ ] **Component 2 (Frequency-tier band)** format: "Frequency tier (English-illustrative): top ~N words [optional: known generally as X]." The "English-illustrative" annotation makes language-specificity explicit.
- [ ] **Component 3 (Register-tier inclusion)** format: "Register tier: [included registers]; excludes [excluded registers]." Both inclusions and exclusions explicit.
- [ ] **Component 4 (Substitution-test sketch)** format: "Substitution-test sketch: translator [actions at this level: which kinds of words are replaced, with what kind of equivalents]." This is the runtime guidance for the AI.
- [ ] Template specifies that each level instance includes (a) the 4 components, (b) 5–7 positive examples (words AT this level), (c) 3–5 negative examples (words ABOVE this level).
- [ ] Template specifies that example words must be GENERAL VOCABULARY (no subject-domain specialist words, per the A1↔A2 boundary).

---

#### **P3 — The 5 individual level specs**

**Question:** For each of the 5 levels, what is the complete spec instantiating the P2 template?

**P3 sub-decomposes into 5 sibling pieces (P3.1–P3.5); each instantiates the P2 template:**

##### **P3.1 — `very_basic` level spec**

**Verification:**
- [ ] **Reader profile:** young child / brand-new second-language learner.
- [ ] **Frequency tier (English):** top ~500–1000 most frequent words (function words + most-common content words).
- [ ] **Register tier:** only everyday core vocabulary; **excludes** Latinate, abstract, academic, literary, archaic, specialist.
- [ ] **Substitution-test sketch:** translator replaces almost everything above the core band with descriptive paraphrase or simpler equivalents; favors short concrete words.
- [ ] **Positive examples:** 5–7 words clearly at this level (e.g., go, have, work, food, water, house, person).
- [ ] **Negative examples:** 3–5 words clearly ABOVE this level (e.g., consider, decide, approximate, ratiocination).
- [ ] **Anchor demographic:** small child reading early-reader books / brand-new ESL learner in first weeks.
- [ ] Cross-cutting constraints (P1) honored: receptive-only phrasing; English-as-illustrative annotation.

##### **P3.2 — `daily` level spec**

**Verification:**
- [ ] **Reader profile:** functional adult in daily life (backpacker / new immigrant / functional second-language speaker).
- [ ] **Frequency tier (English):** top ~2000–3000 most frequent words.
- [ ] **Register tier:** everyday concrete + simple abstract; **excludes** Latinate, academic, literary, specialist, archaic.
- [ ] **Substitution-test sketch:** translator replaces Latinate ("purchase" → "buy"), academic ("endeavor" → "try"), literary, and archaic vocabulary with everyday equivalents.
- [ ] **Positive examples:** 5–7 words at this level (e.g., decide, remember, carry, simple, important, problem, difficult).
- [ ] **Negative examples:** 3–5 words ABOVE this level (e.g., purchase, endeavor, consider, ostensibly, ratiocination).
- [ ] **Anchor demographic:** backpacker carrying out daily transactions in a foreign country / new immigrant functioning in their second language.
- [ ] Cross-cutting constraints honored.

##### **P3.3 — `conversational` level spec**

**Verification:**
- [ ] **Reader profile:** average educated adult who can carry an informed informal conversation; reads newspapers comfortably.
- [ ] **Frequency tier (English):** top ~5000–7000 words including common Latinate.
- [ ] **Register tier:** everyday + conversational-educated + journalistic; **includes** common Latinate (purchase, endeavor, consider, approximate); **excludes** dense academic, literary-archaic, dialectal, specialist.
- [ ] **Substitution-test sketch:** translator avoids dense academic, archaic, dialectal, and specialist vocabulary; keeps common Latinate without substitution.
- [ ] **Positive examples:** 5–7 words at this level (e.g., purchase, endeavor, consider, approximate, apparently, generally, decision).
- [ ] **Negative examples:** 3–5 words ABOVE this level (e.g., ostensibly, ratiocination, verily, ameliorate).
- [ ] **Anchor demographic:** average newspaper-reading adult / casual reader of mainstream non-fiction.
- [ ] Cross-cutting constraints honored.

##### **P3.4 — `advanced` level spec**

**Verification:**
- [ ] **Reader profile:** university-educated reader / skilled non-native who reads widely / educated professional.
- [ ] **Frequency tier (English):** top ~10000–20000 words including academic and literary.
- [ ] **Register tier:** everyday + conversational + journalistic + academic + general literary; **excludes** archaic, dialectal, specialist-rare general.
- [ ] **Substitution-test sketch:** translator avoids ONLY archaic ("verily," "anon"), dialectal, and specialist-rare general vocabulary; keeps academic and literary register.
- [ ] **Positive examples:** 5–7 words at this level (e.g., ratiocination, ostensibly, ameliorate, contingent, putative, ineffable).
- [ ] **Negative examples:** 3–5 words ABOVE this level (e.g., verily, anon, whilom). NOT subject-domain specialist (those belong to the A1↔A2 boundary, addressed in P5, not as negative examples here).
- [ ] **Anchor demographic:** university-educated professional reader / skilled non-native reader of literary fiction.
- [ ] Cross-reference to **P5 A1↔A2 boundary**: at this level, the translator MAY use technical vocabulary if it's general-educated (e.g., `hypothesis`, `epistemic`) but NOT subject-domain specialist (e.g., `myocardial infarction`, `habeas corpus`).
- [ ] Cross-cutting constraints honored.

##### **P3.5 — `native` level spec**

**Verification:**
- [ ] **Reader profile:** educated native speaker who reads broadly across registers.
- [ ] **Frequency tier (English):** full general vocabulary (no upper bound on rarity within the general lexicon).
- [ ] **Register tier:** ALL general registers including archaic, dialectal, literary-rare. **Includes** archaic ("verily," "anon," "whilom"), dialectal, literary-archaic.
- [ ] **Substitution-test sketch:** translator avoids ONLY A2 specialist domain vocabulary (medical, legal, theological-specialist); keeps all general vocabulary including archaic and dialectal.
- [ ] **Positive examples:** 5–7 words at this level (e.g., verily, anon, thee, whilom, gainsay, withal, perchance).
- [ ] **Negative examples:** 3–5 words ABOVE this level — specifically A2 SPECIALIST vocabulary (e.g., myocardial infarction, habeas corpus, transubstantiation, kenosis, ontogenesis).
- [ ] **Anchor demographic:** educated native speaker who reads literary fiction and historical / archaic texts comfortably.
- [ ] **Explicit note:** archaic and literary belong here at A1.native, NOT in A2. The A2 boundary is the subject-domain-training test (P5).
- [ ] Cross-reference to **P5 A1↔A2 boundary**: this level's spec depends on the A1↔A2 boundary to delineate what's NOT included (subject-domain specialist).
- [ ] Cross-cutting constraints honored.

---

#### **P4 — Adjacent-level boundary pairs**

**Question:** At each of the 4 adjacent-level transitions, what is the distinguishing principle and what are the concrete word-pair examples illustrating the transition?

**P4 sub-decomposes into 4 sibling pieces (P4.1–P4.4):**

##### **P4.1 — `very_basic` ↔ `daily` boundary**

**Verification:**
- [ ] **Principle:** shift from CORE/FUNCTION vocabulary (universally needed for basic communication) to FUNCTIONAL EVERYDAY content vocabulary (used by an adult to navigate daily life).
- [ ] **3–5 boundary pairs** (low-side `very_basic` ↔ high-side `daily`):
  - `go` ↔ `decide`
  - `food` ↔ `meal`
  - `work` ↔ `job`
  - `house` ↔ `apartment`
  - `tell` ↔ `explain`
- [ ] Logic noted: the high-side word is recognizable to a functional adult but NOT to a brand-new learner.

##### **P4.2 — `daily` ↔ `conversational` boundary**

**Verification:**
- [ ] **Principle:** shift from FUNCTIONAL EVERYDAY register to EDUCATED-INFORMAL register (common Latinate vocabulary enters).
- [ ] **3–5 boundary pairs** (low-side `daily` ↔ high-side `conversational`):
  - `buy` ↔ `purchase`
  - `try` ↔ `endeavor`
  - `think about` ↔ `consider`
  - `about` ↔ `approximately`
  - `clearly` ↔ `apparently`
- [ ] Logic noted: the high-side word is recognizable to a newspaper-reading adult but NOT to a backpacker-level functional speaker.

##### **P4.3 — `conversational` ↔ `advanced` boundary**

**Verification:**
- [ ] **Principle:** shift from CONVERSATIONAL-EDUCATED register to WRITTEN-EDUCATED register (academic and literary vocabulary enters).
- [ ] **3–5 boundary pairs** (low-side `conversational` ↔ high-side `advanced`):
  - `apparently` ↔ `ostensibly`
  - `reasoning` ↔ `ratiocination`
  - `improve` ↔ `ameliorate`
  - `depending on` ↔ `contingent on`
  - `supposed` ↔ `putative`
- [ ] Logic noted: the high-side word is recognizable to a university-educated reader but NOT to a typical newspaper reader.

##### **P4.4 — `advanced` ↔ `native` boundary**

**Verification:**
- [ ] **Principle:** shift from MODERN EDUCATED vocabulary to ALL GENERAL vocabulary including archaic, dialectal, and rare-but-general.
- [ ] **3–5 boundary pairs** (low-side `advanced` ↔ high-side `native`):
  - `truly` ↔ `verily`
  - `soon` ↔ `anon`
  - `you` (archaic singular) ↔ `thee`
  - `formerly` ↔ `whilom`
  - `also` ↔ `withal`
- [ ] Logic noted: the high-side word is archaic / dialectal / literary-rare general; a skilled non-native or modern educated reader may not recognize it, but an educated native reading literary or historical texts does.

---

#### **P5 — A1↔A2 boundary clarification + borderline-words table**

**Question:** How is the A1 (general vocabulary breadth) vs A2 (subject-domain specialist vocabulary) boundary drawn, and how are common edge cases classified?

**Verification criteria:**
- [ ] **Boundary test stated:** "Does recognizing this word require subject-domain training, or only broad general reading?" Subject-domain training → A2. Broad reading → A1.
- [ ] **Borderline-words table** with explicit classifications:
  | Word | Classification | Reasoning |
  |---|---|---|
  | `ratiocination` | A1.advanced (or A1.native) | General Latinate; no domain training needed |
  | `ostensibly` | A1.advanced | General Latinate; common in educated writing |
  | `ameliorate` | A1.advanced | General Latinate; appears in literary and academic writing |
  | `verily` | A1.native | Archaic general; appears in literary / historical texts |
  | `anon` | A1.native | Archaic general |
  | `whilom` | A1.native | Archaic literary |
  | `eschatology` | A2 (theology specialist) — A1.native for unusually broad readers | Mostly requires theology training; borderline |
  | `transubstantiation` | A2 (Catholic theology specialist) | Requires Catholic-theology training |
  | `myocardial infarction` | A2 (medical specialist) | Requires medical training |
  | `habeas corpus` | A2 (legal specialist) | Requires legal training |
  | `kenosis` | A2 (Christian theology specialist) | Requires theology training |
  | `ontogenesis` | A2 (biology specialist) | Requires biology training |
- [ ] **Explicit note:** A1.native EXCLUDES subject-domain specialist vocabulary. Archaic, dialectal, literary-rare belong AT A1.native; specialist domain belongs AT A2.

---

#### **P6 — Migration mapping from existing AUDIENCE_LEVEL**

**Question:** How do the existing 3 levels in `.env.example`'s `AUDIENCE_LEVEL` knob map to the new 5 levels?

**Verification criteria:**
- [ ] **Mapping table:**
  | Existing (`AUDIENCE_LEVEL`) | New (vocabulary_breadth) |
  |---|---|
  | `late_learner_simple` | `daily` |
  | `late_learner` | `conversational` |
  | `native` | `native` |
- [ ] **New positions noted:**
  - `very_basic` — extends BELOW `late_learner_simple` (for child / brand-new-learner readers not previously addressable)
  - `advanced` — fills the gap BETWEEN `late_learner` and `native` (for university-educated / skilled-non-native readers)
- [ ] **Status:** SUGGESTED mapping. The actual migration is a separate inquiry; this mapping is documentation, not enforcement.
- [ ] **Note:** the existing `AUDIENCE_LEVEL` knob may continue to exist for backwards compatibility; the new `vocabulary_breadth` axis may take precedence when both are set.

---

#### **P7 — Scope boundaries: deliverable vs deferred**

**Question:** What does this inquiry produce vs what is deferred to which subsequent inquiry?

**Verification criteria:**
- [ ] **In scope (deliverable):**
  - 5 level names (`very_basic | daily | conversational | advanced | native`)
  - Per-level 4-component specs (P3.1–P3.5)
  - Per-level positive + negative examples
  - 4 adjacent-level boundary pairs with principles (P4.1–P4.4)
  - A1↔A2 boundary test + borderline-words table (P5)
  - Suggested migration mapping (P6)
  - Cross-cutting framing constraints documentation (P1)
  - 4-component template (P2)
- [ ] **Deferred items + target inquiry:**
  - **Per-language frequency thresholds** (what counts as "top ~5000 words" in Russian, Japanese, Arabic) → future per-language inquiry
  - **Specific conservative-bias default value** for vocabulary_breadth (which of the 5 levels is the conservative-bias default? `daily` or `conversational`?) → future defaults inquiry
  - **Other 4 A1 sub-fields** (syntactic-processing-capacity, idiom-recognition, inference-capacity, cultural-reference-recognition) → each has its own follow-up inquiry
  - **Runtime substitution implementation** (LLM-judged vs frequency-list-backed) → future runtime inquiry
  - **Pydantic dataclass shape** including `vocabulary_breadth: Literal[...]` field → structural-layer inquiry
  - **Default-derivation mechanism** for vocabulary_breadth given A1 headline + Purpose value → future defaults inquiry
  - **Existing AUDIENCE_LEVEL knob's actual migration** (when do we deprecate it, do we keep both, etc.) → migration inquiry
- [ ] Each deferred item has one-line rationale referencing why it's deferred (the inquiry's explicit scope from `_branch.md` Constraint C4 or prior finding's scope).

---

## Step 5 — Map Interfaces

### Interface inventory

| Source → Target | Direction | What flows |
|---|---|---|
| P1 → P2 | one-way | Cross-cutting constraints (receptive-only, language-agnostic, same-labels) the template must honor |
| P1 → P3 (all sub-pieces) | one-way | Constraints all per-level specs honor |
| P1 → P4 | one-way | Constraints boundary pairs honor (boundary-pair examples are also receptive-only) |
| P1 → P5 | one-way | A1↔A2 boundary must use the substitution-test concept reference from P1 |
| P2 → P3.1–P3.5 | one-way (strong) | The 4-component template defines the SHAPE each per-level spec follows |
| P3.1–P3.5 → P4.1–P4.4 | one-way | Each boundary pair (e.g., P4.1) references its bracketing levels (P3.1 + P3.2) by name |
| P3.4 + P3.5 → P5 | one-way | A1↔A2 boundary's negative examples appear in P5's table; P3.4 and P3.5 substitution-test sketches reference P5's boundary test |
| P5 → P3.4, P3.5 | feedback | P5's borderline-words table informs the per-level negative examples |
| P3.1–P3.5 → P6 | one-way | Migration mapping references new level names |
| All → P7 | one-way | P7 enumerates the deliverables produced by the prior pieces |

### Assumptions-not-data check

| Piece | Assumption made about... | Captured? |
|---|---|---|
| P2 (template) | …P1's cross-cutting constraints are well-defined before the template specifies its components | YES — explicit P1 → P2 dependency |
| P3.X (each level) | …P2's template is fully specified before per-level instantiation | YES — explicit P2 → P3 dependency |
| P3.X | …the cross-cutting receptive-only constraint applies; verifiable by reading the level's prose | YES — verification criterion explicit |
| P4.X (each boundary) | …both bracketing levels (P3.X, P3.X+1) are spec'd before boundary-pair examples can be written | YES — explicit P3 → P4 dependency |
| P3.4, P3.5 | …P5's A1↔A2 boundary is settled enough to cross-reference in their substitution-test sketches | PARTIAL — P5 and P3.4/3.5 have a CIRCULAR-looking dependency; resolved at the build level (see Step 6) |
| P5 | …level names from P3.1–P3.5 are committed before borderline-words table can reference them | YES — explicit P3 → P5 dependency |
| P5 (borderline-words classification) | …subject-domain training is a recognizable category distinct from broad reading | YES — captured in the boundary test phrasing |
| P6 | …existing `AUDIENCE_LEVEL` knob exists in `.env.example` with the 3 values; verifiable from file | YES — verifiable |
| P7 | …all prior pieces have produced their outputs by the time P7 synthesizes | YES — explicit synthesis ordering |

### Circular-dependency check

P3.4/3.5 ↔ P5 has a soft circular look: per-level specs reference A1↔A2 boundary; A1↔A2 boundary table references level names. Resolved at build level:
1. P5's BOUNDARY TEST phrasing (the "subject-domain training" test) is independent of any specific level — can be defined first.
2. P3.4 and P3.5 substitution-test sketches reference the BOUNDARY TEST (independent), not the borderline-words table.
3. P5's BORDERLINE-WORDS TABLE references level names (from P3.4 / P3.5), so the table is built AFTER the levels.

So P5 sub-decomposes:
- **P5a** — boundary test (independent; can come early)
- **P5b** — borderline-words table (depends on P3.4 + P3.5 names)

Net dependency: P5a before P3.4/P3.5; P5b after P3.4/P3.5.

No actual circular dependencies.

---

## Step 6 — Order by Dependency

### Dependency DAG

```
Stage 1: P1 (cross-cutting constraints)
         P5a (A1↔A2 boundary test phrasing)
         [both can run in parallel; both are standalone]
                          │
                          ▼
Stage 2: P2 (4-component template)
         [depends on P1]
                          │
                          ▼
Stage 3: P3.1, P3.2, P3.3, P3.4, P3.5 (5 per-level specs, parallel)
         [each depends on P1 + P2; P3.4 and P3.5 also depend on P5a]
                          │
                          ▼
Stage 4: P4.1, P4.2, P4.3, P4.4 (4 boundary specs, parallel)
         [each depends on bracketing P3 pieces]
         P5b (borderline-words table)
         [depends on P3.1–P3.5 names]
         P6 (migration mapping)
         [depends on P3.1–P3.5 names]
                          │
                          ▼
Stage 5: P7 (scope synthesis)
         [depends on all prior]
```

### Ordering summary

| Stage | Pieces (parallel within stage) | Dependencies |
|---|---|---|
| **Stage 1** | P1, P5a | None |
| **Stage 2** | P2 | P1 |
| **Stage 3** | P3.1, P3.2, P3.3, P3.4, P3.5 | P1 + P2 (+ P5a for P3.4, P3.5) |
| **Stage 4** | P4.1, P4.2, P4.3, P4.4, P5b, P6 | Stage 3 outputs |
| **Stage 5** | P7 | All prior |

No circular dependencies.

---

## Step 7 — Self-Evaluate

### Minimum 3 dimensions

#### Independence — PASS

- **P1**: Standalone; no other pieces required. ✓
- **P5a (A1↔A2 boundary test)**: Standalone; the test phrasing is independent of specific levels. ✓
- **P2**: Depends only on P1; otherwise self-contained. ✓
- **P3.1–P3.5**: Each per-level spec specifiable independently given P1 + P2 (+ P5a for L4, L5). No inter-level dependencies (the boundary pairs in P4 handle those). ✓
- **P4.1–P4.4**: Each boundary pair specifiable independently given its bracketing levels. No inter-boundary dependencies. ✓
- **P5b**: Specifiable independently given P3 outputs. ✓
- **P6**: Specifiable independently given P3 names + existing `.env.example`. ✓
- **P7**: Synthesis piece; requires all prior. Within its stage, self-contained. ✓

All pieces independently workable in dependency order. **PASS.**

#### Completeness — PASS

Coverage of sensemaking SV6's commitments:

| Commitment | Piece |
|---|---|
| 5 levels with reader-profile names | P3.1–P3.5 ✓ |
| 4-component definition pattern | P2 ✓ |
| A1↔A2 boundary (general vs subject-domain) | P5 (P5a + P5b) ✓ |
| Same labels propagate from A1 headline | P1 ✓ |
| Conservative-bias for reader-axes = LOWER default | P1 (reference) + P7 (deferred specific value) ✓ |
| Receptive-only constraint | P1 + per-level verification in P3 ✓ |
| Language-agnostic at concept | P1 + per-level statements in P3 ✓ |
| Migration mapping suggested | P6 ✓ |

Coverage of sensemaking's 6 frontier flags handed to decomposition:

| Flag | Piece |
|---|---|
| D1 per-level prose structure | P2 template + P3 instances ✓ |
| D2 positive + negative examples | P3.X verification criteria (5–7 positive + 3–5 negative per level) ✓ |
| D3 anchor demographics | P3.X reader-profile component ✓ |
| D4 boundary-pair examples | P4.1–P4.4 ✓ |
| D5 A1↔A2 borderline-words table | P5b ✓ |
| D6 4-component organization in spec | P2 ✓ |

All commitments and flags covered. **PASS.**

#### Determination-mechanism check (per refinement note)

Load-bearing concepts in the Q-tree whose use depends on a RUNTIME determination?

| Concept | Determination type | Runtime mechanism needed? |
|---|---|---|
| Level identity | Design-time (commit at this inquiry) | NO |
| 4-component template | Design-time (P2) | NO |
| A1↔A2 boundary test | Design-time (P5a phrasing) | NO — but its runtime APPLICATION (does WORD X require subject-domain training?) is partly judgment-based; this is the substitution-test runtime CONCEPT, deferred via P7 |
| Frequency-tier band | Design-time (P3.X spec) for the English-illustrative band; per-language thresholds DEFERRED via P7 | Per-language thresholds need a runtime determination; explicitly deferred |
| Register-tier inclusion | Design-time enumeration (P3.X spec) | NO |
| Substitution-test sketch | Design-time CONCEPT (P1 + P3.X); runtime implementation DEFERRED via P7 | Runtime: LLM-judged vs frequency-list-backed; explicitly deferred |
| Borderline-words classifications | Design-time table (P5b); runtime extension (new borderline words encountered later) needs the same boundary test | NO — the boundary test handles novel cases via the same test |

Load-bearing concepts requiring RUNTIME determination IN THIS INQUIRY'S SCOPE: none. Runtime determinations are explicitly DEFERRED via P7 to future inquiries. The deferral itself is the determination-mechanism. **PASS.**

#### Reassembly — PASS

Given:
- P1 answered: cross-cutting constraints stated
- P2 answered: 4-component template defined
- P3.1–P3.5 answered: each level fully spec'd with the 4 components + examples + demographics
- P4.1–P4.4 answered: each adjacent-level boundary with principle + word-pair examples
- P5a answered: A1↔A2 boundary test phrased
- P5b answered: borderline-words table populated
- P6 answered: migration mapping documented
- P7 answered: deliverables + deferred enumerated

Reconstructs the inquiry's deliverable: "5 vocabulary-breadth levels, named, defined with 4 components per level, with examples and boundaries, A1↔A2 boundary explicit, migration mapping documented, all cross-cutting constraints honored." **PASS.**

### Optional 4 additional dimensions

**Tractability — PASS.** Each piece is one focused pass. Largest pieces are P3.X individual level specs (each ~½ page) and P5b borderline-words table (~½ page).

**Interface clarity — PASS.** 10 explicit interfaces; assumptions-not-data check found one soft circular (P3.4/3.5 ↔ P5) resolved by sub-decomposing P5 into P5a + P5b.

**Balance — PASS.** P3 cluster has 5 sub-pieces; P4 has 4 sub-pieces. Each sub-piece ~equal complexity. No piece is 80% of total work.

**Confidence — PASS.** Top-down + bottom-up agree on all 6 boundaries (Step 3 confidence).

---

## Failure Modes Cross-Check

- **Premature Decomposition** — No: sensemaking stabilized at SV6 before decomposition started.
- **Wrong Boundaries** — No: bottom-up validation confirmed.
- **Hidden Coupling** — Checked at Step 5; P3.4/3.5 ↔ P5 soft circular surfaced and resolved by sub-decomposing P5.
- **Missing Pieces** — Completeness check passed all SV6 commitments + 6 sensemaking frontier flags.
- **Over-Decomposition** — 7 main pieces + 5 P3 sub-pieces + 4 P4 sub-pieces + P5 split into P5a/P5b = 18 total. Reflects the inquiry's structure; no piece is trivial.
- **Ignoring Dependencies** — Step 6 ordering DAG explicit; 5-stage parallel-able structure.
- **Imbalanced Decomposition** — P3 is the biggest cluster but sub-decomposes evenly.

---

## Final Deliverable

### Coupling Map (Step 1)

6 clusters (Per-Level Specs / Adjacent-Level Boundaries / A1↔A2 Boundary / Migration & Scope / Cross-Cutting / Template), 6 boundaries (B1–B6).

### Question Tree (Step 4)

```
TOP — What are the 5 vocabulary-breadth levels (names, definitions, examples, boundaries, migration)?
├── P1 — Cross-cutting framing constraints (receptive-only, language-agnostic, same-labels, substitution-test concept, conservative-bias reference)
├── P2 — The 4-component definition template
├── P3 — The 5 individual level specs
│       ├── P3.1 — very_basic (small child / brand-new learner)
│       ├── P3.2 — daily (functional adult, backpacker)
│       ├── P3.3 — conversational (educated newspaper-reader)
│       ├── P3.4 — advanced (university-educated; cross-ref P5)
│       └── P3.5 — native (educated native; cross-ref P5)
├── P4 — Adjacent-level boundary pairs
│       ├── P4.1 — very_basic ↔ daily (core/function → functional everyday)
│       ├── P4.2 — daily ↔ conversational (functional everyday → educated-informal/Latinate)
│       ├── P4.3 — conversational ↔ advanced (conversational → written-educated/academic-literary)
│       └── P4.4 — advanced ↔ native (modern educated → all general incl. archaic)
├── P5 — A1↔A2 boundary clarification
│       ├── P5a — boundary test ("requires subject-domain training")
│       └── P5b — borderline-words classification table
├── P6 — Migration mapping from existing AUDIENCE_LEVEL
└── P7 — Scope boundaries (deliverable + deferred)
```

### Interface Map (Step 5)

10 explicit interfaces documented; assumptions-not-data check passed (one soft circular resolved by P5 sub-decomposition).

### Dependency Order (Step 6)

5 stages:
1. P1, P5a (parallel; standalone)
2. P2 (depends on P1)
3. P3.1–P3.5 (parallel; depend on P1 + P2 + P5a)
4. P4.1–P4.4 + P5b + P6 (parallel; depend on Stage 3)
5. P7 (synthesis)

### Self-Evaluation (Step 7)

| Dimension | Verdict |
|---|---|
| Independence | PASS |
| Completeness | PASS |
| Reassembly | PASS |
| Determination-mechanism | PASS (deferred items address future runtime questions) |
| Tractability | PASS |
| Interface clarity | PASS (one soft circular resolved) |
| Balance | PASS |
| Confidence | PASS |

All 8 dimensions PASS. Decomposition stable. Ready for Innovation.

---

## Frontier handed to Innovation

Innovation generates concrete candidates for these design points:

1. **Per-level prose CONCRETE wording.** For each of P3.1–P3.5, generate 2–3 candidate prose drafts of the 4 components (the actual sentences the spec will use). Critique selects the best per level.

2. **Per-level POSITIVE example sets.** For each level, generate 5–7 candidate English example words at this level. Critique validates (does each word genuinely fit the level?).

3. **Per-level NEGATIVE example sets.** For each level, generate 3–5 candidate English example words ABOVE this level. Critique validates.

4. **Adjacent-level BOUNDARY-PAIR example sets.** For each of P4.1–P4.4, generate 3–5 candidate word pairs illustrating the transition. Critique validates.

5. **A1↔A2 BORDERLINE-WORDS table candidates.** For P5b, generate a comprehensive set of borderline words spanning multiple subject domains (medicine, law, theology, science, philosophy, archaic-literary) with proposed classifications. Critique validates and may refine.

6. **MIGRATION mapping rationale.** Per P6, generate 1–2 sentences of rationale per mapping entry (why `late_learner_simple → daily`, etc.). Critique validates.

7. **ANCHOR DEMOGRAPHIC alternatives.** For each level's reader profile, generate 2–3 alternative anchor demographics (different real-world reader types representing the level). Critique selects the most evocative + universally recognizable.

These are content-generation points where Innovation operates within the structural commitments settled at sensemaking SV6 + this decomposition.
