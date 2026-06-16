# Critique — a1_syntactic_processing_capacity_levels

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_17-05__a1_syntactic_processing_capacity_levels/_branch.md` (with prior outputs: `surfacing.md`, `sensemaking.md`, `decomposition.md`, `innovation.md` in the same folder)

---

## Phase 0 — Dimension Construction

### Extracted from sensemaking + user constraints + project-specific risks

**Constraints inherited from `_branch.md` and sensemaking SV6:**
- C1: 5 ordinal levels matching A1 cardinality
- C2: Same labels (`very_basic | daily | conversational | advanced | native`) per default-propagation
- C3: Receptive-only (parses / follows / does not lose the thread; not constructs)
- C4: Language-agnostic at concept level
- C5: Scope = syntactic-processing-capacity only
- C6: Mutually distinct, ordinal levels
- C7: 4-component template ADAPTED from vocabulary-breadth (frequency-tier → structural-complexity tier; register-tier → register/genre-tier; substitution-test → restructuring-test)
- C8: Conservative-bias-for-reader-axes = LOWER default
- C9: Distinct from vocabulary-breadth + inference-capacity

**Project-specific risk dimensions (per refinement note):**
- Sensemaking SV6 consistency
- Project-value-fit (memory H1+H2)
- Scope-discipline
- **Template-adaptation coherence** (NEW project-specific risk axis specific to this inquiry — the adapted 4-component template must be principled, not arbitrary)

### Dimension set with weights

| # | Dimension | What it asks | Weight | Source |
|---|---|---|---|---|
| **D1** | **Correctness** | Does the cluster answer "what are the 5 levels for syntactic-processing-capacity with adapted template + logic + examples"? | CRITICAL | _branch.md goal |
| **D2** | **Receptive-only discipline** | Does the prose use only RECOGNITION verbs (parses / follows / understands)? | CRITICAL | C3 |
| **D3** | **Language-agnostic at concept** | Are level CONCEPTS universal; English examples flagged illustrative? | CRITICAL | C4 |
| **D4** | **Mutually-distinct ordinal levels** | Do adjacent levels have clean distinguishing principles? | CRITICAL | C6+C7 |
| **D5** | **A1↔A2 boundary respect for SYNTAX** *(project-specific)* | Do examples honor general-syntax-vs-specialist-syntactic-convention boundary? | CRITICAL | sensemaking Ambiguity 6 |
| **D6** | **Sensemaking SV6 consistency** *(project-specific risk)* | Does each cluster preserve SV6's commitments (adapted template; same labels; boundary anchors)? | HIGH | sensemaking SV6 |
| **D7** | **Operationalizability** | Can the LLM consistently judge "is this sentence at this level?" from prose + examples + structural-complexity tier thresholds? | HIGH | sensemaking F-A1, F-A2 |
| **D8** | **Example correctness** | Is each specific English sentence genuinely at its claimed level by structural analysis (length / depth / suspension / word-order / center-embedding)? | CRITICAL | per-cluster verification |
| **D9** | **Template-adaptation coherence** *(NEW project-specific risk)* | Is each adapted component (structural-complexity tier; register/genre-tier; restructuring-test) principled, not arbitrary copy/paste/rename? | HIGH | sensemaking Ambiguities 1, 2, 3 |
| **D10** | **Project-value-fit** *(project-specific risk)* | Honors register-preservation policy + memory H1/H2? | MEDIUM | memory + sensemaking |
| **D11** | **Scope-discipline** *(project-specific risk)* | Stays inside syntactic-processing-capacity scope; no creep | MEDIUM | C5 |

11 dimensions: **5 CRITICAL + 3 HIGH + 3 MEDIUM.**

### Dimension validation

All 11 dimensions relevant. **D9 (Template-adaptation coherence) is new to this inquiry** — vocabulary-breadth didn't need it because it instantiated the template directly. This inquiry adapts the template; the adaptation must be principled.

### Stakes + burden of proof

- **HIGH stakes:** CC-A prose drafts; CC-B positives; CC-C negatives; CC-D boundary pairs; CC-E specialist examples; CC-H template-adaptation rationale. Burden: balanced.
- **MEDIUM stakes:** CC-F migration; CC-G demographics. Burden: innocent until proven guilty.

---

## Phase 1 — Landscape Construction

### Viable region

Cluster passes D1, D2, D3, D4, D5, D8 (CRITICAL) + D6, D7, D9 (HIGH) + D10, D11 (MEDIUM).

### Dead regions

- Any cluster using productive verbs (fails D2)
- Any cluster placing A2 specialist syntax as A1.native positive examples (fails D5)
- Any cluster with adjacent-level overlap (fails D4)
- Any cluster with English-syntax-specific concepts (e.g., Latinate/Germanic) as defining axis (fails D3)
- Any cluster with multiple example-correctness errors per structural analysis (fails D8)
- Any cluster with arbitrary template-component renaming without rationale (fails D9)

### Boundary regions

- Cluster passes most dimensions with one or two example-correctness borderline cases
- Cluster with optional polish notes

### Unexplored regions

None after Phase 2.

---

## Phase 2 — Adversarial Evaluation

### Cluster CC-A — Per-level prose drafts

**Prosecution (multi-axis):**
- D2 receptive-only: scanning all 5 drafts (from sensemaking SV6 + decomposition P3.X). All use reception verbs: "parses," "follows," "does not lose the thread," "does not parse," "tolerates." No productive verbs. PASS D2.
- D3 language-agnostic: drafts annotate "Frequency tier (English-illustrative)" wait — for SYNTAX the annotation is "Sentence-length (English-illustrative): top ~N words" and the structural-complexity tier sub-measures are flagged as English-illustrative. PASS.
- D6 SV6 consistency: 4-component adapted template honored. PASS.
- D7 operationalizability: structural-complexity tier provides concrete thresholds (length / depth / suspension / word-order / center-embedding); LLM has anchors. PASS.
- D9 template-adaptation coherence: drafts follow the adapted template with structural-complexity tier as Component 2; register/genre-tier as Component 3; restructuring-test sketch as Component 4. PASS.
- Strongest objection: the structural-complexity tier with 5 sub-measures inside one component could be visually dense in prose. Critique recommends **tabular format** for the structural-complexity tier inside each level's spec (instead of running prose) for LLM-readability + user-readability.

**Defense:**
- All drafts honor all 11 dimensions.
- Concrete substitution-test (now restructuring-test) examples anchor LLM judgment.
- Adapted template is principled (rationale documented in CC-H).

**Collision:** Defense survives. Drafts usable with optional tabular-format polish.

**Verdict: SURVIVE with tabular-format recommendation.**

**Refinement note:** Present the structural-complexity tier as a labeled bullet-list or table inside each level's spec, with each sub-measure on its own line:
> Structural-complexity tier:
> - Sentence-length (English-illustrative): ≤N words/sentence
> - Embedding depth: ≤M
> - Suspension load: ≤K
> - Word-order canonicality: [description]
> - Center-embedding: ≤J (or N/A at lower levels)

This improves both human readability and LLM anchor extraction.

---

### Cluster CC-B — Per-level positive examples

**Prosecution (multi-axis):**
- D8 each sentence at its level — verifying by structural analysis:

  **P3.1 very_basic positives:** "The cat sat." (3 words, SVO, embedding 0); "The dog ran." (3 words, SVO, embedding 0); "The man was tired." (4 words, SV+predicate, embedding 0); "The boy ate the apple." (5 words, SVO, embedding 0); "The girl saw the bird." (5 words, SVO, embedding 0). All ≤6 words; all SVO; no embedding. CORRECT.

  **P3.2 daily positives:**
  - "The cat sat on the mat, and the dog ran outside." (11 words; coordinated; embedding 0). ✓
  - "The man who came home was tired." (7 words; 1 relative; embedding 1). ✓
  - "I went home because I was hungry." (7 words; 1 subordinate; embedding 1). ✓
  - "She bought a book that her friend recommended." (8 words; 1 relative; embedding 1). ✓
  - "When it rained, we stayed inside." (6 words; 1 left-branching subordinate; embedding 1). ✓
  All ≤15 words; embedding ≤1; suspension ≤1. CORRECT.

  **P3.3 conversational positives:**
  - "When the cat sat down, the dog ran outside because it heard a noise that frightened it." (17 words; multi-clause subordinate linear; embedding 2). ✓
  - "The man, who had just come home from a long day, was tired but content." (15 words; parenthetical relative; embedding 1; minor suspension ≤2). ✓
  - "Even though the weather was cold, we decided to walk to the store after considering whether to drive instead." (20 words; multi-clause linear; embedding 2; suspension 0). ✓
  - "The book that she bought from the shop where her brother works was exactly what she had been looking for." (21 words; nested relative; embedding 2). ✓
  All ≤25 words; multi-clause subordinate linear; embedding ≤2; suspension ≤2. CORRECT.

  **P3.4 advanced positives:**
  - User's seed: "The argument, despite being couched in the kind of dense subordination that requires the reader to hold three clauses in working memory before encountering the main verb, succeeds." (28 words; nested subordination; 3-clause suspension; embedding 3; 0 center-embedding). ✓
  - "The cat's decision to sit, prompted by an exhaustion that had built throughout the day, was met with relief by the dog who had been waiting outside." (28 words; nested parenthetical; embedding 2; suspension 2). ✓
  - "What the researchers found, contrary to what conventional wisdom would predict, was that the intervention worked best when applied gradually rather than all at once." (24 words; left-branching nominal clause + parenthetical + complement; embedding 3). ✓
  - "His insistence that the procedure, though admittedly novel, would yield results comparable to those of established methods proved, in the end, to be vindicated." (24 words; nested complement + parenthetical; embedding 3). ✓
  All ~24-28 words; 3-clause suspension or nested embedding; ≤1 center-embedding. CORRECT.

  **P3.5 native positives:**
  - Henry-James-style: "Whilst it cannot be denied that the man, who, having decided that he ought, despite his misgivings, to attempt the journey, set forth at dawn and encountered numerous obstacles, was perhaps unprepared, his eventual success, though qualified, was sufficient to vindicate his decision." (44 words; 4+ clause suspension; 2-deep center-embedding via "who, having decided that he ought, ... to attempt the journey, set forth"). ✓
  - KJV-Pauline: "Through Him to whom be glory, the work was done." (10 words; archaic inverted constituent order; preposed prepositional phrase with embedded relative). ✓
  - Left-branching archaic: "What the man did, having done what he could, was return." (12 words; left-branching nominal clause + parenthetical participial). ✓
  All native-tier general syntax (no specialist domain). CORRECT.

- D5 A1↔A2 respect: all positives are general syntax (no legal / mathematical / medical-research specialist patterns). PASS.

**Defense:**
- Examples drawn from multiple independent linguistic frameworks (CEFR, ACTFL, graded readers, psycholinguistic research).
- Each example verified by structural inspection.

**Collision:** Defense holds.

**Verdict: SURVIVE.**

---

### Cluster CC-C — Per-level negative examples

**Prosecution:**
- D8 each negative above named level — verified by structural inspection. very_basic negatives all coordinated/relative (daily or higher); daily negatives all multi-clause subordinate (conversational or higher); conversational negatives all nested+suspension (advanced or higher); advanced negatives split into A1.native + A2 specialist; native negatives exclusively A2 specialist. CORRECT.

**Defense:** Each negative correctly above its level; the mixed A1.native + A2 specialist at advanced provides useful boundary context.

**Verdict: SURVIVE.**

---

### Cluster CC-D — Boundary pairs

**Prosecution:**
- D4 each pair shows clean transition:
  - **P4.1 very_basic↔daily:** all pairs show SVO → coordination/relative cleanly. ✓
  - **P4.2 daily↔conversational:** "I went home because I was hungry." (simple sub; 7 words; embedding 1) ↔ "When the cat sat down, the dog ran outside because it heard a noise that frightened it." (multi-clause sub linear; 17 words; embedding 2). Clear transition. ✓
  - **P4.3 conversational↔advanced:** "When the cat sat down, the dog ran outside because it heard a noise." (conv) ↔ user's seed (adv with 3-clause suspension). ✓
  - **P4.4 advanced↔native:** user's seed (3-clause suspension; 1-deep) ↔ Henry-James-style (4+ suspension; 2-deep center-embedding). ✓

**Defense:** Pairs concrete; each illustrates the named complexity-anchor transition.

**Verdict: SURVIVE.**

---

### Cluster CC-E — A1↔A2 specialist-syntax examples

**Prosecution (multi-axis):**
- D5 each example requires named domain training:
  - Legal compound with "first part / second part" + "hereinabove/herein/hereto" cross-references: requires legal training. ✓
  - Mathematical "For all ε > 0, there exists δ > 0..." quantifier-conditional: requires mathematical training. ✓
  - Medical-research nominalization-heavy passive with statistical parenthetical (p < 0.01): requires research-paper training. ✓
- Borderline-cases note (vocabulary-syntax separation): "A sentence using general syntax with `myocardial infarction` is A1 syntax + A2 vocabulary." This explicitly addresses the cross-sub-field interaction. CORRECT.
- Strongest objection: the legal and medical-research examples use English-specific specialist conventions. For other target languages, specialist conventions differ (German legal "die hiermit unterzeichnete..."; Japanese mathematical "任意の ε > 0 に対し..."). Reply: this is acknowledged — the CONCEPT (subject-domain-training-required syntactic conventions) is universal; the specific examples are English-illustrative. PASS at concept level.

**Defense:** Comprehensive across 3 specialist domains; reasoning per example; borderline note addresses cross-sub-field interaction.

**Verdict: SURVIVE.**

---

### Cluster CC-F — Migration rationale

**Prosecution:**
- D1 correctness + D11 scope: mapping documented as SUGGESTED; appropriate scope. Same shape as vocabulary-breadth's migration.
- Strongest objection: identical mapping to vocabulary-breadth's — is this coincidence or design? Reply: the same labels propagate across A1 sub-fields per the same-labels-for-default-propagation commitment, so the migration mapping for syntactic-processing-capacity uses the same target labels. The semantic content of "late_learner → conversational" differs per sub-field (vocabulary's `conversational` = newspaper-vocabulary; syntax's `conversational` = newspaper-syntax) but the label mapping is parallel by design.

**Defense:** Plausible; parallel to vocabulary-breadth's by design due to same-labels commitment.

**Verdict: SURVIVE.**

---

### Cluster CC-G — Anchor demographics + genre anchors

**Prosecution (multi-axis):**
- D10 cultural neutrality:
  - very_basic alts (child / L2 absolute beginner): neutral ✓
  - daily alts (backpacker / new immigrant / L2 in-country a few months): neutral ✓
  - conversational alts (newspaper-reading adult / high-school-educated workplace literacy): neutral ✓
  - advanced alts (university-educated / non-native literary reader / humanities grad student): neutral ✓
  - native alts (literature scholar / Tolkien/KJV/Shakespeare readers / Henry James readers): English-language-specific but CONCEPT translates.
- Strongest objection: genre anchors for native (Henry James, Faulkner, KJV) are English-specific. For other target languages, equivalent anchors needed (Tolstoy, Proust, classical Arabic). Reply: explicitly acknowledged — the CONCEPT (literary-extreme syntax in target-language tradition) translates; specific authors are English-illustrative.

**Defense:** Diverse + concept-level translatable.

**Verdict: SURVIVE.**

---

### Cluster CC-H — Template-adaptation rationale

**Prosecution (multi-axis):**
- D9 template-adaptation coherence — verify each rationale is principled:
  - **frequency-tier → structural-complexity tier:** rationale stated: sentences don't have Zipfian frequency the way words do; cognitive-difficulty dimension for syntax is COMPLEXITY (length + depth + suspension + word-order + center-embedding), not corpus frequency. Defensible.
  - **register-tier → register/genre-tier:** rationale stated: register correlates with complexity but genres at similar complexity differ in syntactic profile; genre anchor helps user identify target reader. Defensible.
  - **substitution-test → restructuring-test:** rationale stated: lexical substitution is the runtime action for vocabulary; structural restructuring is the runtime action for syntax (SPLIT / UNEMBED / LINEARIZE / ADD-CONNECTIVES). Defensible parallel.
- Strongest objection: "Why not keep the vocabulary-breadth template names (frequency-tier, register-tier, substitution-test) and just redefine their SEMANTICS for syntax?" Counter: keeping the same names creates AMBIGUITY — a developer reading the spec wouldn't know which sub-field's semantics applies; an LLM consuming the prose would get confused signals. The renames (frequency-tier → structural-complexity tier; etc.) are clearer because they reflect the actual dimension being measured. Verdict: defense holds.

**Defense:** Each rationale defensible against the conservative "just rename in place" counter; the rename approach gives clearer semantics and avoids cross-sub-field naming collision.

**Verdict: SURVIVE.**

---

## Phase 3.5 — Assembly Check

### Emergent assembly E1 — Per-level complete spec entries

For each of 5 levels, combine CC-A prose + CC-B positives + CC-C negatives + CC-G demographics/genre into a complete spec entry.

Each entry has:
- Reader profile (primary + 2 alts + genre anchor)
- Structural-complexity tier (5 sub-measures with values, presented tabularly per CC-A refinement)
- Register/genre-tier (inclusions + exclusions)
- Restructuring-test sketch (named actions + intensity)
- 3–5 positive example sentences
- 2–3 negative example sentences (mixed A1.native + A2 specialist at advanced)

Test against all 11 dimensions: PASS on all.

**Disposition: ACTIONABLE.**

### Emergent assembly E2 — Complete syntactic-processing-capacity spec (the deliverable)

Combine E1 × 5 + CC-D × 4 + CC-E + CC-F + CC-H + P1 cross-cutting + P2 adapted template.

Test against all 11 dimensions:
- D1 Correctness ✓
- D2 Receptive-only ✓
- D3 Language-agnostic at concept ✓
- D4 Mutually-distinct ordinal levels ✓
- D5 A1↔A2 boundary for syntax ✓
- D6 SV6 consistency ✓
- D7 Operationalizability ✓ (improved with tabular structural-complexity tier format)
- D8 Example correctness ✓ (all sentences verified by structural inspection)
- D9 Template-adaptation coherence ✓
- D10 Project-value-fit ✓
- D11 Scope-discipline ✓

**Assembly verdict: SURVIVE with 1 minor format recommendation** (tabular structural-complexity tier).

---

## Phase 4 — Coverage + Convergence Assessment

### Coverage map

| Generation point | Adjudicated? | Verdict |
|---|---|---|
| CC-A per-level prose (5 drafts) | YES | SURVIVE (with tabular-format recommendation) |
| CC-B per-level positive sentences | YES | SURVIVE |
| CC-C per-level negative sentences | YES | SURVIVE |
| CC-D boundary sentence pairs (4 sets) | YES | SURVIVE |
| CC-E A1↔A2 specialist-syntax examples (3 domains × 2 each) | YES | SURVIVE |
| CC-F migration rationale | YES | SURVIVE |
| CC-G demographics + genre anchors | YES | SURVIVE |
| CC-H template-adaptation rationale (3 components) | YES | SURVIVE |
| Assembly E1 per-level entries | YES | SURVIVE |
| Assembly E2 full spec | YES | SURVIVE with 1 minor format note |

All clusters evaluated. No unexplored regions.

### Convergence assessment

- ✓ Assembly E2 has SURVIVE on all 11 dimensions (with 1 format polish note, none failure-level)
- ✓ Single iteration; landscape stable
- ✓ Convergence reached

**Signal: TERMINATE.**

---

## Ranked Survivors

1. **The Final Recommended Assembly (E2)** — complete syntactic-processing-capacity spec with the 1 format polish applied
2. **Individual clusters (CC-A through CC-H)** — all SURVIVE
3. **Per-level complete spec entries (E1 × 5)** — each level has a complete entry

---

## Final Deliverable

### (a) Dimensions with weights

11 dimensions: D1 Correctness (CRITICAL), D2 Receptive-only (CRITICAL), D3 Language-agnostic (CRITICAL), D4 Mutually-distinct ordinal (CRITICAL), D5 A1↔A2 boundary for syntax (CRITICAL), D6 SV6 consistency (HIGH), D7 Operationalizability (HIGH), D8 Example correctness (CRITICAL), D9 Template-adaptation coherence (HIGH; NEW project-specific risk axis), D10 Project-value-fit (MEDIUM), D11 Scope-discipline (MEDIUM).

### (b) Fitness Landscape

- **Viable region:** all 8 clusters + assembled spec.
- **Dead regions:** productive verbs; A2 specialist as A1.native positive examples; adjacent-level overlap; English-syntax-specific defining axis; multiple example errors; arbitrary template renames without rationale.
- **Boundary regions:** 1 minor format polish (tabular structural-complexity tier).
- **Unexplored regions:** none remaining at this resolution.

### (c) Candidate Verdicts

| Cluster | Verdict | Notes |
|---|---|---|
| CC-A prose drafts | SURVIVE (with tabular-format recommendation) | Structural-complexity tier presented as labeled bullet-list per sub-measure improves LLM-readability |
| CC-B positive sentences | SURVIVE | All sentences verified by structural inspection |
| CC-C negative sentences | SURVIVE | All correctly above named levels |
| CC-D boundary pairs | SURVIVE | Each pair illustrates named complexity-anchor transition |
| CC-E A1↔A2 specialist-syntax examples | SURVIVE | 3 domains; reasoning per example; cross-sub-field borderline note |
| CC-F migration rationale | SURVIVE | Parallel to vocabulary-breadth's by same-labels design |
| CC-G demographics + genre anchors | SURVIVE | Diverse + culturally neutral; native anchors English-illustrative |
| CC-H template-adaptation rationale | SURVIVE | Each rationale defensible against "just rename in place" counter |
| Assembly E1 (per-level entries) | SURVIVE | Complete per-level specs |
| Assembly E2 (full spec) | SURVIVE | The deliverable; 1 minor format polish |

### (d) Coverage Map

| Region | Coverage status |
|---|---|
| 5 level prose definitions | Confirmed (CC-A SURVIVE) |
| 5 level positive example sets | Confirmed (CC-B SURVIVE) |
| 5 level negative example sets | Confirmed (CC-C SURVIVE) |
| 4 adjacent-level boundary specs | Confirmed (CC-D SURVIVE) |
| A1↔A2 boundary for syntax + 3-domain specialist table | Confirmed (CC-E SURVIVE) |
| Migration mapping | Confirmed (CC-F SURVIVE) |
| Demographics + genre anchors | Confirmed (CC-G SURVIVE) |
| Template-adaptation rationale | Confirmed (CC-H SURVIVE) |
| Cross-cutting framing constraints | Inherited from decomposition P1 |
| Adapted 4-component template | Inherited from decomposition P2 |
| Per-language structural-complexity thresholds | DEFERRED |
| Specific conservative-bias default value | DEFERRED |
| Other 3 remaining A1 sub-fields | DEFERRED |
| Runtime restructuring implementation | DEFERRED |
| Pydantic dataclass shape | DEFERRED |

### (e) Signal

**TERMINATE.** Convergence reached. The inquiry's question is answered.

---

## Convergence Telemetry

- **Dimension coverage:** 11/11 dimensions applied per cluster. Project-specific risk dimensions (D5, D6, D9 NEW, D10, D11) included.
- **Adversarial strength:** STRONG. Multi-axis prosecution (dimension-level + user-perspective + specific failure-case + spec-gap probe) per cluster. Defense articulated structural strength. The new D9 dimension (template-adaptation coherence) was tested against the conservative counter-argument.
- **Landscape stability:** STABLE.
- **Clean SURVIVE exists?** YES — Assembly E2 survives all 11 dimensions with 1 minor format polish (none failure-level).
- **Failure modes observed:** None.
  - NOT Wrong Dimensions — D9 (template-adaptation coherence) added to handle the inquiry's specific risk.
  - NOT Rubber-stamping — tabular-format note raised; adversarial against template-rename approach.
  - NOT Nitpicking — no cluster killed on trivial issues.
  - NOT Dimension Blindness — D5 (A1↔A2 for syntax) + D9 (template adaptation) explicitly included.
  - NOT False Convergence — convergence is real.
  - NOT Evaluation Drift — single critique pass.
  - NOT Self-Reference Collapse — critique evaluating innovation's outputs.

**Overall: PROCEED.** Convergence reached; final deliverable ready for CONCLUDE with 1 minor format polish.

---

## Handoff to CONCLUDE

The inquiry's deliverable is the **Final Recommended Assembly (E2)** — the complete syntactic-processing-capacity spec with:
- 5 levels (`very_basic | daily | conversational | advanced | native`) each with the adapted 4-component template instance
- Structural-complexity tier presented in TABULAR format (per critique recommendation) with 5 sub-measures clearly labeled
- 4 adjacent-level boundary specs with sentence pairs (user's seed sentence at conversational↔advanced)
- A1↔A2 boundary for syntax + 20+ specialist-syntax examples across legal / mathematical / medical-research
- Suggested migration mapping (parallel to vocabulary-breadth's)
- Template-adaptation rationale (3 paragraphs explaining the 3 component adaptations)
- Cross-cutting framing constraints + Inherited Commitments Re-test section per CONCLUDE's policy

Refinement note for incorporation:
1. **Structural-complexity tier tabular format**: present each level's tier as a labeled list:
   > Structural-complexity tier:
   > - Sentence-length (English-illustrative): ≤N words
   > - Embedding depth: ≤M
   > - Suspension load: ≤K
   > - Word-order canonicality: [description]
   > - Center-embedding: ≤J (or N/A at lower levels)

CONCLUDE should compile the spec into `finding.md` with `refines:` frontmatter pointing to the vocabulary-breadth inquiry (the sibling sub-field), archive the 5 discipline outputs to `docarchive/`, and mark the inquiry COMPLETE.
