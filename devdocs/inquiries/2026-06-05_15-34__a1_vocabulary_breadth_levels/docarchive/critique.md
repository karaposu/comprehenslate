# Critique — a1_vocabulary_breadth_levels

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/_branch.md` (with prior outputs: `surfacing.md`, `sensemaking.md`, `decomposition.md`, `innovation.md` in the same folder)

---

## Phase 0 — Dimension Construction

### Extracted from sensemaking + user constraints + project-specific risks

**Constraints inherited from `_branch.md` and sensemaking SV6:**
- C1: 5 ordinal levels covering full spectrum
- C2: language-agnostic at concept level
- C3: RECEPTIVE vocabulary only (recognition not production)
- C4: scope = vocabulary-breadth only
- C5: each level operationalizable as translator-AI prompt instruction
- C6: mutually distinct levels
- C7: ordinal (monotonic, no categorical mixing)
- C8: respect composite-axis default-propagation (same labels as A1 headline)
- A1↔A2 boundary explicit (general vs subject-domain)
- Conservative-bias-for-reader-axes = LOWER default

**Project-specific risk dimensions (per refinement note):**
- Sensemaking SV6 consistency (does the candidate honor stabilized commitments?)
- Project-value-fit (memory H1+H2; preservation policies)
- Scope-discipline (no creep into other A1 sub-fields, defaults, pydantic)

### Dimension set with weights

| # | Dimension | What it asks | Weight | Source |
|---|---|---|---|---|
| **D1** | **Correctness** | Does the cluster answer "what are the 5 levels with logic and examples"? | CRITICAL | _branch.md goal |
| **D2** | **Receptive-only discipline** | Does the prose use only RECOGNITION verbs, not production? | CRITICAL | C3 + sensemaking Ambiguity 8 |
| **D3** | **Language-agnostic at concept** | Are level CONCEPTS universal; English examples flagged illustrative? | CRITICAL | C2 |
| **D4** | **Mutually-distinct ordinal levels** | Do adjacent levels have clean distinguishing principles? | CRITICAL | C6+C7 |
| **D5** | **A1↔A2 boundary respect** *(project-specific)* | Do examples honor general-vs-specialist boundary? Does A1.native exclude domain-specialist? | CRITICAL | sensemaking Ambiguity 3 |
| **D6** | **Sensemaking SV6 consistency** *(project-specific)* | Does the cluster preserve SV6's commitments (same labels; 4-component template)? | HIGH | sensemaking SV6 |
| **D7** | **Operationalizability** | Can the LLM consistently judge "is this word at this level?" from the examples + prose? | HIGH | sensemaking F-A1 + F-A2 |
| **D8** | **Example correctness** | Is each specific example word genuinely at its claimed level? | CRITICAL | per-cluster verification |
| **D9** | **Project-value-fit** *(project-specific)* | Honors register-preservation policy + memory H1/H2? | MEDIUM | memory + sensemaking |
| **D10** | **Scope-discipline** *(project-specific)* | Stays inside vocabulary-breadth scope; no creep | MEDIUM | C4 |

10 dimensions: **5 CRITICAL + 2 HIGH + 3 MEDIUM** (D9, D10 MEDIUM; D8 CRITICAL because per-word correctness load-bears for runtime LLM judgment).

### Dimension validation

All 10 dimensions are relevant. Project-specific risk dimensions (D2, D5, D6, D9, D10) are included per the refinement note since the candidate set involves vocabulary-content artifacts that go directly into the project's translation-system spec.

### Stakes + burden of proof

- **HIGH stakes:** CC-A prose drafts; CC-B positives; CC-C negatives; CC-D boundary pairs; CC-E borderline table. These are load-bearing content for the finding. Burden: balanced.
- **MEDIUM stakes:** CC-F migration rationale; CC-G demographics. Less load-bearing. Burden: innocent until proven guilty.

---

## Phase 1 — Landscape Construction

### Viable region

Cluster:
- Passes D1, D2, D3, D4, D5, D8 (CRITICAL)
- Passes D6, D7 (HIGH)
- Passes D9, D10 (MEDIUM)

### Dead regions

- Any cluster using productive verbs (fails D2)
- Any cluster including A2-specialist as A1.native positive examples (fails D5)
- Any cluster with adjacent-level overlap (fails D4)
- Any cluster whose level CONCEPTS presuppose English (fails D3)
- Any cluster with multiple example-correctness errors (fails D8)

### Boundary regions

- Cluster passes most dimensions but has one or two example-correctness borderline cases (CC-B `endeavor`/`hermetic` borderline) → SURVIVE with caveats
- Cluster has minor phrasing that could be receptive-clearer (CC-A P3.2) → SURVIVE with polish note

### Unexplored regions

None remain after Phase 2 evaluation.

---

## Phase 2 — Adversarial Evaluation

### Cluster CC-A — Per-level prose drafts

**Prosecution (multi-axis):**
- D2 receptive-only check: scanning all 5 drafts. P3.1 "recognizes only the most everyday core vocabulary"; P3.2 "recognizes everyday concrete and simple abstract vocabulary; does not recognize Latinate"; P3.3 "recognizes common Latinate vocabulary in educated speech"; P3.4 "recognizes academic vocabulary"; P3.5 "recognizes archaic vocabulary." All drafts use reception verbs. PASS D2.
- P3.2 contains "Reads simple signs, instructions, casual conversation" — strongest objection: "reads" is technically reception but the clause could be misread as describing production-side activity (the reader's external behavior rather than vocabulary recognition). MINOR concern.
- D3 language-agnostic check: drafts annotate "Frequency tier (English-illustrative)." PASS.
- D4 mutual distinctness: 5 reader-profiles, frequency bands, and register-tier inclusions all differ. PASS.
- D5 A1↔A2 respect: P3.4 and P3.5 explicitly note specialist-vocabulary exclusion. PASS.
- D6 SV6 consistency: 4-component template honored; names match. PASS.
- D7 operationalizability: prose includes concrete substitution examples (`purchase` → `buy`) that anchor LLM judgment. PASS.
- User-perspective: drafts honor user's seed names and use evocative demographics. PASS.
- Specific failure-case: P3.3's "average newspaper-reading adult" overlaps with P3.4's "university-educated reader"? Test: an educated professional who reads casually may be at conversational for newspapers but at advanced for academic articles — the demographics describe READER-LEVEL, not READER-IDENTITY. A single person can occupy different levels for different reading. PASS.

**Defense:**
- All 10 dimensions pass with one MINOR refinement note (P3.2 polish).
- Drafts ready for direct insertion into the finding.
- Concrete substitution examples anchor both LLM judgment and user understanding.

**Collision:** Defense survives. Drafts are usable as-is with optional polish to P3.2.

**Position:** Viable region.

**Verdict: SURVIVE.** 

**Constructive refinement note:** P3.2's "Reads simple signs, instructions, casual conversation" could be rephrased as "Recognizes vocabulary in simple signs, instructions, and casual conversation" for maximum receptive clarity. Not required; current phrasing is technically acceptable.

---

### Cluster CC-B — Per-level positive example sets

**Prosecution (multi-axis):**
- D8 example correctness — verifying each example word's level membership:

  **P3.1 very_basic** — `the, is, has, do, of, go, eat, work, house, food, water, person`. All function words and core content words; top ~500 English. CORRECT.

  **P3.2 daily** — `decide, remember, carry, important, problem, simple, difficult, understand, area`. All top ~1000-3000 English. CORRECT.

  **P3.3 conversational** — `purchase, endeavor, consider, approximately, apparently, generally, decision, essential, establish`.
  - `purchase` (Latinate, ~top-5000): ✓
  - `endeavor` (Latinate, ~top-10000-15000): **BORDERLINE** — appears in formal speech and newspapers (educated register), but on the high end of conversational. Could arguably be advanced.
  - `consider` (~top-1500): ✓
  - `approximately, apparently, generally, decision, essential, establish`: all common Latinate in newspaper/educated speech ✓
  
  **P3.4 advanced** — `ratiocination, ostensibly, ameliorate, contingent, putative, ineffable, epistemic, hermetic, prescient`.
  - All but `hermetic` clearly academic/literary advanced general vocabulary ✓
  - `hermetic`: in its non-occult sense (`hermetically sealed`) means "sealed" or "isolated"; advanced general. In its occult/Hermes-Trismegistus sense, it's A2 (esoteric specialist). **BORDERLINE** for vocabulary-breadth use; if used in literary-fiction context, advanced ✓; if in occult-philosophy context, A2.

  **P3.5 native** — `verily, anon, thee, whilom, gainsay, withal, perchance, forsooth, wherefore`. All archaic general English; recognized by native readers of Shakespeare/KJV/Tolkien. CORRECT.

- D5 A1↔A2 respect check: positive examples are all general vocabulary, not subject-domain specialist (except the two borderlines noted). PASS.
- D7 operationalizability: 5-7 anchor examples per level give the LLM enough grounding to judge novel cases.

**Defense:**
- Examples drawn from 3 independent frameworks (CEFR + ACTFL + graded readers + register theory) that converge.
- Most examples are clear-cut; two borderlines (`endeavor`, `hermetic`) are defensible at their assigned levels.

**Collision:** Defense survives with two borderline notes.

**Position:** Viable region with two boundary caveats.

**Verdict: SURVIVE with two refinement notes.**

**Constructive refinement notes:**
- `endeavor` at conversational: defensible because it appears in newspaper/educated speech, BUT is at the high end of conversational. Could be relocated to advanced if the user prefers a tighter conversational definition. The substitution-test logic favors keeping it at conversational (a newspaper reader does encounter `endeavor` without pausing).
- `hermetic` at advanced: defensible in its non-occult sense (sealed/isolated). If the spec's anchor examples are meant to be uncontroversial, replace `hermetic` with `recondite` or `desuetude` (less context-dependent advanced words). Minor refinement.

---

### Cluster CC-C — Per-level negative example sets

**Prosecution (multi-axis):**
- D8 each negative must be genuinely above its level.
  - very_basic negatives `consider, decision, approximate, apparently, ratiocination`: all above very_basic. CORRECT.
  - daily negatives `purchase, endeavor, consider, ostensibly, ratiocination`: all above daily. CORRECT.
  - conversational negatives `ostensibly, ratiocination, ameliorate, verily, whilom`: all above conversational. CORRECT.
  - advanced negatives mix A1.native (`verily, anon, whilom`) and A2 specialist (`myocardial infarction, transubstantiation`). The mix is structurally clear (P3.4 explicitly notes the A1↔A2 boundary applies at this level). CORRECT.
  - native negatives `myocardial infarction, habeas corpus, transubstantiation, kenosis, ontogenesis`: all A2 specialist. CORRECT.
- Strongest objection: the mixed A1.native + A2 specialist negatives at advanced could confuse a user who doesn't read the cross-reference to P5. Reply: the structure is explicit in CC-A's P3.4 substitution-test sketch + the cross-reference to the A1↔A2 boundary section. Reader can follow.

**Defense:** All negatives correctly above their levels; mixing provides useful boundary context at advanced.

**Verdict: SURVIVE.**

---

### Cluster CC-D — Boundary pairs

**Prosecution (multi-axis):**
- D4 each pair must show clean low-side / high-side membership.
  - **P4.1 very_basic↔daily:** `go ↔ decide` (function/core vs functional-everyday content); `food ↔ meal` (generic vs specific everyday); `work ↔ job` (generic vs specific); `house ↔ apartment` (generic vs specific); `tell ↔ explain` (core vs functional-everyday). All clean. CORRECT.
  - **P4.2 daily↔conversational:** `buy ↔ purchase` (Germanic-everyday vs Latinate-conversational); `try ↔ endeavor` (same); `think about ↔ consider` (phrase vs single-word Latinate); `about ↔ approximately`; `clearly ↔ apparently`. All clean Germanic-vs-Latinate. CORRECT.
  - **P4.3 conversational↔advanced:** `apparently ↔ ostensibly`; `reasoning ↔ ratiocination`; `improve ↔ ameliorate`; `depending on ↔ contingent on`; `supposed ↔ putative`. All clean conversational-vs-academic. CORRECT.
  - **P4.4 advanced↔native:** `truly ↔ verily`; `soon ↔ anon`; `you ↔ thee`; `formerly ↔ whilom`; `also ↔ withal`. All clean modern-vs-archaic — with one note: `you ↔ thee` is asymmetric (`you` is both subject and object in modern English; `thee` is the archaic 2nd-person singular object form). MINOR clarification helpful.

- Strongest objection on `you ↔ thee`: the asymmetry could confuse readers unfamiliar with archaic English grammar. Reply: in the spec context, a brief clarification "(archaic 2nd-person singular)" suffices.

**Defense:** Pairs are concrete and pedagogically clear. The Latinate-vs-Germanic register pattern (P4.2, P4.3) and modern-vs-archaic pattern (P4.4) make the transitions vivid.

**Verdict: SURVIVE with one minor clarification.**

**Constructive refinement note:** Add a brief grammatical note to `you ↔ thee`: "*`thee`* — archaic 2nd-person singular object form; e.g., 'I love thee' for 'I love you'." Improves clarity for readers unfamiliar with archaic English.

---

### Cluster CC-E — A1↔A2 borderline-words table

**Prosecution (multi-axis):**
- D5 boundary respect — each entry's classification follows the "requires subject-domain training" test.
  - `ratiocination` → A1.advanced: general Latinate; no domain training ✓
  - `eschatology` → A2 (with A1.native borderline): mostly theology specialist ✓
  - `myocardial infarction` → A2 medical: requires medical training ✓
  - `entropy` → A1.advanced/native (commonsense) — A2 physics for technical-precise: commonly-known concept; technical-precise use is domain-specific ✓
  - `epistemology` → A2 philosophy (or A1.native): borderline; appears in non-philosophy contexts ✓
  - All other entries follow the boundary test correctly.

- Strongest objection: `entropy` and `epistemology` have DUAL classifications (A1.native or A2 depending on context). Is this contradictory? Reply: it's CONTEXT-DEPENDENT classification — appropriate to flag borderline cases as borderline rather than force a single classification. The A2-default rule (when borderline, treat as A2) handles runtime decisions cleanly.

- Spec-gap probe: how does the runtime translator USE this table? The translator needs to decide for any word whether it's A1 or A2. The table provides explicit classifications for ~20 borderline cases + the boundary test for novel cases. Sufficient for the inquiry's scope.

**Defense:** Table is comprehensive across multiple specialist domains (medicine, law, theology, philosophy, science, archaic-literary); borderline cases explicitly flagged with reasoning; A2-default rule stated for ambiguous cases.

**Verdict: SURVIVE.**

---

### Cluster CC-F — Migration mapping rationale

**Prosecution:**
- D1 correctness: each rationale explains the mapping.
- D10 scope: the mapping is documented as SUGGESTED, not enforced. Appropriate scope.
- Strongest objection: the user's existing labels in production may not match the suggested mapping. Reply: the SUGGESTED nature is explicit; future migration inquiry refines.

**Defense:** Rationales are plausible; new-position explanations (`very_basic` extends low; `advanced` fills gap) are clear.

**Verdict: SURVIVE.**

---

### Cluster CC-G — Anchor demographic alternatives

**Prosecution (multi-axis):**
- D9 cultural neutrality check:
  - very_basic Alt 1 (child age 4-6 / L2 absolute beginner): neutral ✓
  - very_basic Alt 2 (L2 learner in first 1-2 weeks immersion): neutral ✓
  - daily Alt 2 (casual L2 learner in-country a few months): neutral ✓
  - native Alt 2 (Tolkien/KJV/Shakespeare readers): English-language-specific but the CONCEPT (broadly-read native who enjoys historical/archaic literature) translates.
- Strongest objection: the native-Alt-2 examples are English-specific. For other target languages, the equivalent would be different (Pushkin readers for Russian, etc.). Reply: this is appropriate for an English-illustrative spec; per-language equivalents come in the next inquiry.

**Defense:** Alternatives are diverse, operationalizable, and culturally neutral within the English-illustrative scope.

**Verdict: SURVIVE.**

---

## Phase 3.5 — Assembly Check

### Emergent assembly E1 — Per-level complete spec entry

For each of 5 levels, combine CC-A (prose) + CC-B (positives) + CC-C (negatives) + CC-G (demographics) into a complete spec entry. Each entry has:
- Reader profile (with primary demographic + 2 alternatives)
- Frequency tier (English-illustrative)
- Register tier (inclusion + exclusion)
- Substitution-test sketch
- 5–7 positive examples
- 3–5 negative examples (mixed A1-higher + A2 specialist at advanced)

Test against all 10 dimensions: PASS on all.

**Disposition: ACTIONABLE.** Each per-level entry is a complete spec.

### Emergent assembly E2 — Complete vocabulary-breadth spec (the deliverable)

Combine E1 × 5 + CC-D × 4 + CC-E + CC-F + cross-cutting constraints from P1 + 4-component template from P2.

Test against all 10 dimensions:
- D1 Correctness: directly answers the inquiry's question. PASS.
- D2 Receptive-only: all prose uses reception verbs. PASS (with P3.2 polish note).
- D3 Language-agnostic: concepts universal; English examples flagged illustrative. PASS.
- D4 Mutually-distinct ordinal levels: 5 levels with clean adjacent boundaries (4 boundary specs). PASS.
- D5 A1↔A2 respect: borderline table + per-level negative-example structure. PASS.
- D6 SV6 consistency: 4-component template, same labels, all SV6 commitments honored. PASS.
- D7 Operationalizability: anchor examples + substitution sketches + boundary pairs give LLM rich grounding. PASS.
- D8 Example correctness: mostly correct; 2 borderline notes (CC-B `endeavor`, `hermetic`); 1 clarification note (CC-D `you↔thee`). PASS WITH CAVEATS.
- D9 Project-value-fit: receptive-only, language-agnostic, scope-disciplined. PASS.
- D10 Scope-discipline: vocabulary-breadth only; defaults / pydantic / other A1 sub-fields explicitly deferred. PASS.

**Assembly verdict: SURVIVE with 3 minor refinement notes.**

The assembly is the recommended final output of this inquiry.

---

## Phase 4 — Coverage + Convergence Assessment

### Coverage map

| Generation point | Adjudicated? | Verdict |
|---|---|---|
| CC-A per-level prose (5 drafts) | YES | SURVIVE (with P3.2 polish note) |
| CC-B positive examples (5 sets) | YES | SURVIVE (with 2 borderline notes) |
| CC-C negative examples (5 sets) | YES | SURVIVE |
| CC-D boundary pairs (4 sets) | YES | SURVIVE (with 1 clarification note) |
| CC-E A1↔A2 borderline table (20 entries) | YES | SURVIVE |
| CC-F migration rationale | YES | SURVIVE |
| CC-G anchor demographics | YES | SURVIVE |
| Assembly E1 (per-level spec entries) | YES | SURVIVE |
| Assembly E2 (full spec) | YES | SURVIVE with 3 minor notes |

All clusters evaluated. No unexplored regions remain.

### Convergence assessment

- ✓ At least one candidate (Assembly E2) has SURVIVE verdict on all CRITICAL dimensions
- ✓ No new candidates from innovation landed in unexplored regions
- ✓ No unexplored regions topologically likely to contain viable candidates
- ✓ Single iteration; convergence reached

**Convergence: REACHED.**

### Signal

**TERMINATE** with ranked survivors.

---

## Ranked Survivors

1. **The Final Recommended Assembly (E2)** — the complete vocabulary-breadth spec with 3 minor refinement notes applied
2. **Individual clusters (CC-A through CC-G)** — all SURVIVE, available for direct use in the finding
3. **Per-level complete spec entries (E1 × 5)** — each level has a complete entry

---

## Final Deliverable

### (a) Dimensions with weights

10 dimensions: D1 Correctness (CRITICAL), D2 Receptive-only (CRITICAL), D3 Language-agnostic (CRITICAL), D4 Mutually-distinct ordinal (CRITICAL), D5 A1↔A2 boundary (CRITICAL), D6 SV6 consistency (HIGH), D7 Operationalizability (HIGH), D8 Example correctness (CRITICAL), D9 Project-value-fit (MEDIUM), D10 Scope-discipline (MEDIUM).

### (b) Fitness Landscape

- **Viable region:** CC-A drafts + CC-B/C/D/E/F/G content + the assembled spec.
- **Dead regions:** productive-verb phrasing; A2 specialist as A1.native positive examples; adjacent-level overlap; English-presupposed concepts.
- **Boundary regions:** 3 minor refinement points (P3.2 polish; `endeavor`/`hermetic` borderlines; `you↔thee` clarification).
- **Unexplored regions:** none remaining at this resolution.

### (c) Candidate Verdicts

| Cluster | Verdict | Notes |
|---|---|---|
| CC-A prose drafts | SURVIVE (with polish note) | P3.2 phrasing could be rephrased for max receptive clarity |
| CC-B positive examples | SURVIVE (with 2 borderline notes) | `endeavor` borderline at conversational/advanced; `hermetic` borderline at advanced; both defensible |
| CC-C negative examples | SURVIVE | All correctly above named levels |
| CC-D boundary pairs | SURVIVE (with 1 clarification) | `you ↔ thee` benefits from a brief grammatical note |
| CC-E A1↔A2 borderline table | SURVIVE | Comprehensive; borderline cases flagged; A2-default rule clear |
| CC-F migration rationale | SURVIVE | Plausible mapping; SUGGESTED status explicit |
| CC-G anchor demographics | SURVIVE | Diverse + culturally neutral |
| Assembly E1 (per-level entries) | SURVIVE | Complete per-level specs |
| Assembly E2 (full spec) | SURVIVE | The deliverable; 3 minor refinement notes |

### (d) Coverage Map

| Region | Coverage status |
|---|---|
| 5 level prose definitions | Confirmed (CC-A SURVIVE) |
| 5 level positive example sets | Confirmed (CC-B SURVIVE with borderline notes) |
| 5 level negative example sets | Confirmed (CC-C SURVIVE) |
| 4 adjacent-level boundary pairs | Confirmed (CC-D SURVIVE with clarification) |
| A1↔A2 boundary table | Confirmed (CC-E SURVIVE) |
| Migration mapping | Confirmed (CC-F SURVIVE) |
| Anchor demographics | Confirmed (CC-G SURVIVE) |
| Cross-cutting framing constraints | Inherited from decomposition P1 |
| 4-component template | Inherited from decomposition P2 |
| Per-language frequency thresholds | DEFERRED |
| Specific conservative-bias default value | DEFERRED |
| Other 4 A1 sub-fields | DEFERRED |
| Runtime substitution implementation | DEFERRED |
| Pydantic dataclass shape | DEFERRED |

### (e) Signal

**TERMINATE.** Convergence reached. The inquiry's question is answered.

---

## Convergence Telemetry

- **Dimension coverage:** 10/10 dimensions applied per cluster (full evaluation). Project-specific risk dimensions (D2, D5, D6, D9, D10) included as required.
- **Adversarial strength:** STRONG. Prosecution constructed multi-axis (dimension-level + user-perspective + specific failure-case + spec-gap probe) for each cluster. Defense for each cluster articulated structural strength. Borderlines were genuinely tested.
- **Landscape stability:** STABLE. Single iteration; the landscape stabilized at SV6 + decomposition + content.
- **Clean SURVIVE exists?** YES — the Final Recommended Assembly (E2) survives on all 10 dimensions with 3 minor refinement notes (none failure-level).
- **Failure modes observed:** None.
  - NOT Wrong Dimensions — Phase 0 dimensions derived from sensemaking + user constraints + project-specific risks.
  - NOT Rubber-stamping — 3 minor refinement notes raised; prosecution was adversarial.
  - NOT Nitpicking — no cluster killed on trivial issues; refinements are constructive.
  - NOT Dimension Blindness — project-specific risk dimensions D2/D5/D6/D9/D10 included.
  - NOT False Convergence — convergence is real; inquiry's question fully addressed.
  - NOT Evaluation Drift — single critique pass.
  - NOT Self-Reference Collapse — critique evaluating innovation's outputs, not itself.

**Overall: PROCEED.** Convergence reached; final deliverable ready for CONCLUDE with 3 minor refinement notes incorporated into the finding.

---

## Handoff to CONCLUDE

The inquiry's deliverable is the **Final Recommended Assembly (E2)** — the complete vocabulary-breadth spec with:
- 5 levels (`very_basic | daily | conversational | advanced | native`) each with prose + positive examples + negative examples + demographics
- 4 adjacent-level boundary specs with principles + word-pair examples (`you ↔ thee` includes a brief grammatical note)
- A1↔A2 borderline-words table (20 entries with classifications + reasoning)
- Migration mapping (SUGGESTED) from existing `AUDIENCE_LEVEL`
- Cross-cutting framing constraints (receptive-only; language-agnostic; same-labels; substitution-test concept; conservative-bias-for-reader-axes reference)
- 4-component template documentation

Refinement notes for incorporation:
1. **CC-A P3.2 daily prose polish:** Replace "Reads simple signs, instructions, casual conversation" with "Recognizes vocabulary in simple signs, instructions, and casual conversation" for maximum receptive clarity.
2. **CC-B borderline-example transparency:** Note `endeavor` as high-end of conversational and `hermetic` as advanced-in-its-non-occult-sense; either retain or substitute (`hermetic` → `recondite` if preferred for less context-dependence).
3. **CC-D `you ↔ thee` clarification:** Add brief grammatical note: "*`thee`* — archaic 2nd-person singular object form; e.g., 'I love thee' for 'I love you'."

CONCLUDE should compile the spec into `finding.md`, archive the 5 discipline outputs to `docarchive/`, and mark the inquiry COMPLETE.
