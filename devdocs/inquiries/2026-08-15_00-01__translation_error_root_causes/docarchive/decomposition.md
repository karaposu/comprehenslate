# decomposition — translation error root causes

## User Input

```
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-08-15_00-01__translation_error_root_causes/_branch.md

Upstream outputs in the same folder — read all in full: articulate_simple.md + surfacing.md + articulate_warm.md + sensemaking.md.

The SV6 stabilized model is the substrate to decompose. Sensemaking committed:

CENTRAL CLAIM (meta-structural): the comprehenslate translation method treats "a check" as ONE undifferentiated thing when it is FIVE independently-varying properties — (1) WHAT it checks · (2) from what VANTAGE · (3) with what INSTRUMENT · (4) at what ENFORCEMENT POSITION · (5) at what TIME relative to edits.

THE 19 ERRORS SORT INTO 5 GAP-KINDS: INSTRUMENT (8) · VANTAGE (2, the two that survived) · SCOPE (1, position-INDEPENDENT) · TIMING (1) · POSITION (the rest, and the reason none of the above got fixed).

WHY JULY'S FIX DIDN'T TAKE: it repaired ORDERING — one property adjacent to position — leaving vantage, scope, instrument and timing untouched.

WHAT ACTUALLY ENFORCED ANYTHING: 17/19 found on re-scans, each a fresh turn created by the user asking = structurally a separate call, hand-cranked. In-turn Pass 4 found 0.

LOAD-BEARING ARTIFACTS (reference; let Innovation render): (a) the 15-check × 5-property MATRIX; (b) the FIVE-KIND GAP PARTITION; (c) the SIX-REMEDY AVAILABILITY TABLE (R1 term-lock NOW · R2 policy enumeration NOW · R3 re-run rule NOW · R4 source-blind reader NOW · R5 fresh-context reader · R6 engine GATED). FIVE OF SIX UNBLOCKED.

OTHER COMMITMENTS: nesting PARTIAL; vantage and position ORTHOGONAL; frontier flag 1 RESOLVED (source-blind vantage not occupiable in a call containing the source, but the call is the cheapest in the method; X03 handled by construction — question-list, no edit authority); substitution test 4/4 SURVIVE + the AI-favouring INVERSION; content-conflict 1 resolved ("missing" = missing-from-the-run); THIRD INSTANCE (structural_check.sh) raises n for structure to 3; SPLIT CONFIDENCE (structure HIGH, magnitude MED-quarantined, validation experiment a MUST); SELF-REFERENCE (this loop: strong position, weak vantage, worst instrument); depth-target META-STRUCTURAL; scope = SKILL + human-AI pattern as ONE SYSTEM; explanation AND remedy; CN8/FP4 (nudge-honesty in authoring docs, never runtime text).

DECOMPOSITION SHOULD PRODUCE pieces that honor the five-property frame as primary axis; honor the July→August explanation; identify META-DECISION pieces; show DEPENDENCIES; address the USER'S REGISTER (one piece carries the direct answer in plain language); respect the 8-item NOT-list; produce ~9-12 pieces.

Save decomposition output to: .../decomposition.md
```

---

## Step 1 — Perceive Coupling Topology

**The whole being decomposed:** the finding document that answers *"why did these errors happen, and what was missing in our process — thought about really deeply."*

### Elements enumerated

Fifteen candidate elements, from SV6 and the upstream commitments:

`E1` direct plain-language answer · `E2` the five-property claim · `E3` how to classify a new check/error by the properties · `E4` the 15-check matrix · `E5` the five-kind gap partition over the 19 errors · `E6` the falsification of the "missing knowledge" reading + the library-with-no-index mechanism · `E7` the July→August recurrence explanation · `E8` relationship to the prior inquiry chain · `E9` what actually enforced anything (division of labour) · `E10` honest limits (substitution test + inversion) · `E11` the remedy set typed by property · `E12` next actions · `E13` split confidence + validation experiment · `E14` self-reference scoping · `E15` the third instance (`structural_check.sh`)

### Propagation test — "if I change A, must B change?"

| Pair | Propagates? | Strength |
|---|---|---|
| E2 → E5 | Yes, wholly — the partition IS the claim applied to the evidence | **Strong, one-way** |
| E2 → E3 | Yes — the classification rule is per-property | **Strong, one-way** |
| E2 → E4 | Yes — the properties are the matrix's columns | **Strong, one-way** |
| E2 → E7 | Yes — "July touched one of five" is unstatable without the five | **Strong, one-way** |
| E5 → E11 | Yes — remedies are typed by gap-kind | **Strong, one-way** |
| E5 → E9 | Partly — E9 consumes the vantage classification only | **Moderate, one-way** |
| E5 → E6 | Partly — E6 explains E5's instrument row; E6 also stands on F4 alone | **Moderate, one-way** |
| E4 ↔ E5 | Shared check IDs; changing an ID propagates both ways | **Moderate, bidirectional (naming contract)** |
| E10 → E11 | Yes for R4's construction; the limits shape what a remedy may be | **Moderate, one-way** |
| E11 → E12 | Yes — next actions are the remedies ordered and owned | **Strong, one-way** |
| E7 → E8 | Weak — the explanation stands under any relationship label | **Weak, one-way** |
| E13 ↔ E14 | Both scope the finding's weight, by different mechanisms (evidence quantity vs producing vantage) | **Moderate, mutual** |
| E15 → E13 | Yes — the third instance is what raises n for the structure | **Strong, one-way** |
| E15 → E14 | Yes — it is also the live self-reference demonstration | **Strong, one-way** |
| E10 ↮ E2/E4/E5 | No — the substitution test runs on its own evidence | **None** |
| E1 ← all | E1 consumes everything; nothing consumes E1 | **Consumption-only** |

### Coupling map — clusters and valleys

```
                     ┌──────────────────────────────────────┐
   CLUSTER α         │   E2  the five-property claim        │
   "the abstraction" │   E3  how to classify by it          │   ← root
                     └───────────────┬──────────────────────┘
                                     │  thin interface: 5 names + defs
                     ┌───────────────▼──────────────────────┐
   CLUSTER β         │   E4  the matrix   ⇄  E5  partition  │
   "the evidence"    │        (shared check-ID contract)    │
                     └──────┬──────────────┬────────────────┘
                            │              │
              ┌─────────────▼──┐    ┌──────▼──────────────┐
   CLUSTER γ  │ E6 "missing"   │    │ E11 remedies        │  CLUSTER δ
   "the two   │    redefined   │    │ E12 next actions    │  "what to do"
    stories"  │ E7 July→Aug+E8 │    └──────▲──────────────┘
              │ E9 who enforced│           │
              └────────────────┘           │
                                  ┌────────┴─────────┐
   CLUSTER ε (independent) ───────│ E10 honest limits│
                                  └──────────────────┘
              ┌───────────────────────────────────────┐
   CLUSTER ζ  │ E13 split confidence + E15 third inst │
   "how much  │ E14 self-reference scoping            │
    to trust" └───────────────────────────────────────┘
                     ┌──────────────────────────────────────┐
   CLUSTER η         │   E1 the direct answer (consumes all) │
                     └──────────────────────────────────────┘
```

**Valleys (low-coupling regions where cuts are natural):**

- Between α and β — the interface is five names and their definitions. Nothing else crosses.
- Between β and γ — γ consumes classifications, produces narrative. No back-flow.
- Between β/ε and δ — δ consumes gap-kinds and limits, produces prescriptions.
- Around ε — the substitution test is grounded in its own four claims; it touches nothing upstream.
- Around ζ — pure meta-epistemics; it scores the others but changes none of them.
- Around η — consumption-only by construction.

**Peaks (must stay together):** E4+E5 share a check-ID naming contract and must be authored against one identifier set. E13+E14+E15 all answer "how much weight does this carry" and split into fragments if separated.

---

## Step 2 — Detect Boundaries (Top-Down)

Cutting at the valleys yields this initial boundary set:

| Cut | Where | Rationale |
|---|---|---|
| 1 | α │ β | Claim vs its application to evidence. Interface = the five names. |
| 2 | within α: E2 │ E3 | Claim vs its runtime classification procedure. E3 is what makes the frame usable on a *new* check rather than post-hoc on 19 known ones. |
| 3 | within β: E4 │ E5 | Artifact vs argument. The matrix is a table anyone can check; the partition is a claim about the 19. |
| 4 | β │ γ | Classification vs narrative. |
| 5 | within γ: E6 │ E7+E8 │ E9 | Three distinct stories: what "missing" means · why the last fix failed · who actually enforced anything. |
| 6 | ε standalone | Independently grounded. |
| 7 | β/ε │ δ | Diagnosis vs prescription. |
| 8 | within δ: E11 │ E12 | What exists and repairs what vs what to do first. |
| 9 | ζ standalone, merged internally | E13+E14+E15 as one piece. |
| 10 | η standalone, authored last | Executive answer. |
| 11 | Frontier | Open questions — what is *not* claimed. |

**Merge decision — E8 into E7.** The relationship label (REFINES / SUPERSEDES / EXTENDS the prior chain) is one paragraph alone: an over-decomposition signal. It is the natural closing move of the piece that explains why the prior fix failed. Merged.

**Merge decision — E13 + E14 + E15 into one piece.** Each is a fragment alone. All three answer one question: *how much weight does this finding carry, and why*. E15 does double duty as evidence for E13 and as a live demonstration for E14 — splitting it would duplicate it.

**Initial boundary set: 13 pieces.**

---

## Step 3 — Validate Boundaries (Bottom-Up Check)

Irreducible atoms, and where each lands:

| Atom | Piece | Split across pieces? |
|---|---|---|
| the five property names + definitions | P2 | no |
| the determination question per property (5) | P3 | no |
| each matrix row (15) | P4 | no |
| each error's gap-kind assignment (19) | P5 | no |
| F4 — the catalog held the matching principle, read, inert | P6 | no |
| KI6 — a "notice X" principle is retrievable only by a reader who noticed X | P6 | no |
| the git diff (flat bag → four ordered passes) | P7 | no |
| the one-month gap (2026-07-12 → 2026-08-14) | P7 | no |
| 17/19 found on re-scans that were separate turns | P8 | no |
| **the 2 target-only errors are the 2 the user found** | **P5 and P8** | **YES — see below** |
| each substitution-test row (4) | P9 | no |
| the AI-favouring inversion | P9 | no |
| "not occupiable in a call containing the source" | P9 | no |
| each remedy (6) + availability mark | P10 | no |
| R4's construction (question-list, no edit authority) | P10 | no |
| `structural_check.sh` absent, prose-substituted | P12 | no |
| n=3 for structure / n=2 for magnitude | P12 | no |
| this loop's position/vantage/instrument scoring | P12 | no |
| vantage ⊥ position | P2 (asserted) → P10 (consumed) | interfaced |

**The one split atom.** The fact that the two target-only errors are exactly the two the user found appears in both P5 (as the vantage classification's confirmation) and P8 (as the division-of-labour argument's hinge). This is a genuine dual-use fact, not a boundary error — but it needs an explicit contract or the two pieces will each tell the whole story. **Contract: P5 states it as a classification result in one line; P8 develops it as the argument. P5 does not argue; P8 does not re-classify.**

**Second check — atoms grouped that are actually independent?** P9's four substitution-test rows are independent of everything upstream, confirming ε's standalone boundary. P12's three atoms are mutually reinforcing, confirming the merge.

**Confidence:** top-down and bottom-up agree on 12 of 13 boundaries; the thirteenth (the P5/P8 shared fact) is resolved by an explicit contract rather than a re-cut. **HIGH confidence.**

---

## Step 4 — Question Tree

Thirteen pieces. Each is a question with verification criteria.

---

### **P1 — What is the direct answer, in plain language, to a person who asked "why did this happen"?**
*Register piece. Written last, read first.*

- [ ] Answers the user's actual question in prose, not in framework vocabulary — a reader who stops here has a real answer
- [ ] States the one-sentence core: the method treats "a check" as one thing when it is five, so a fix aimed at one property leaves four untouched
- [ ] States the recurrence in **one sentence as conclusion** (evidence lives in P7 — see interface contract)
- [ ] Names what was *not* wrong: not knowledge, not diligence, not chunk size, not the documents
- [ ] Does not require the reader to have seen the matrix
- [ ] Contains no apology, no reassurance, no "I will be more careful"
- [ ] Register check: reads as an explanation to a person, not as a spec preamble

---

### **P2 — META-DECISION: What is the central structural claim, and why is it the answer to "most core"?**
*Root piece. Framing-semantic.*

- [ ] States the five properties with definitions: **what** is checked · from what **vantage** (what must be present in, and absent from, the checking context) · with what **instrument** (script / forced enumeration / prose judgment) · at what **enforcement position** (prose-instruction / emitted-artifact / separate-call) · at what **time** relative to edits
- [ ] Demonstrates independent variation with the evidence pair for each axis (vantage vs instrument; instrument vs position; vantage vs position; scope vs all; timing vs all)
- [ ] Asserts **vantage ⊥ position** explicitly — a separate call containing the source is the strong position at the wrong vantage
- [ ] Says why this is the *core* rather than one more gap: it is the abstraction under which every gap and every past fix becomes classifiable
- [ ] States the claim's relationship to the inherited enforcement gradient — the gradient is one of the five axes, not the whole object
- [ ] Marks the nesting as **PARTIAL** and names the three gaps that survive a move to the strong gradient end
- [ ] Confidence marked HIGH with its ground stated (follows from what a check *is*; no error-count required)

---

### **P3 — How does someone classify a new check, or a new error, using this frame?**
*The determination mechanism. Without this the frame is a post-hoc taxonomy rather than a tool.*

- [ ] One determination question per property, answerable about a check that has never been run
- [ ] The vantage rule stated operationally: *a check requires the target-only vantage iff its question can be answered without the source AND having the source available changes the answer*
- [ ] The instrument rule: *is there an artifact this check produces, or only a verdict?*
- [ ] The position rule: *could the checker act on material this check forbids? if yes, it is prose*
- [ ] The scope rule: *is this check named anywhere, or is it assumed?*
- [ ] The timing rule: *what invalidates this check's result, and does anything re-run it?*
- [ ] At least one worked example on a check **not** among the 19 errors, showing the frame applies forward
- [ ] Verification that the rules are decidable — no rule requires knowing the answer to apply

---

### **P4 — EVIDENCE ARTIFACT: What does the full check inventory look like, scored on all five properties?**

- [ ] All 4 performed checks (A1–A4) with vantage / instrument / position / errors-catchable / observed result
- [ ] All 11 absent-or-unspecified checks (B1–B11) with the same columns plus *why absent*
- [ ] The 1-of-4 instrumentation ratio stated, with the mechanised check's dual result (held **and** discovered a fact the prose reads missed)
- [ ] Vantage coverage stated: the method stands at 2 of 5 vantages
- [ ] Compact table form — this is an artifact to check, not an essay
- [ ] Check IDs match P5's exactly (naming contract)
- [ ] Every cell traceable to a file read or a session fact; no cell inferred

---

### **P5 — Which gap-kind does each of the 19 errors belong to, and what fixes each kind?**

- [ ] All 19 assigned to exactly one of: instrument (8) · vantage (2) · scope (1) · timing (1) · position
- [ ] Per kind: what property failed, and what class of intervention repairs it
- [ ] **Scope marked position-independent** — defining the check is upstream of enforcing it
- [ ] **Vantage marked position-necessary-but-not-sufficient**
- [ ] **Timing marked position-independent as a rule, position-sensitive in detectability**
- [ ] States the P5/P8 shared fact **as a classification result, one line, without arguing it**
- [ ] Does **not** re-litigate whether any item is an error (MQ4 exclusion)
- [ ] Uses P4's check IDs

---

### **P6 — What does "missing" mean, given that the knowledge was present?**

- [ ] States the falsification plainly: the catalog held the matching principle for nearly every error, correctly worded, fully read, and inert
- [ ] Names the specific principles (#4 arrangement · #20/#37/#38 repetition · l.359 buried root · #7 preserve-every-valid-meaning) against the errors they match
- [ ] States the mechanism: a principle phrased "the comprehension layer should notice X" is retrievable only by a reader who has already noticed X — the catalog can confirm a noticing, never cause one
- [ ] Splits "missing": a **minority** of checks genuinely absent from the corpus (B8/B9/B10); a **majority** present-and-inert
- [ ] Commits the corrected sense: missing **from the run**, not from the corpus — the missing thing is the condition under which a principle fires
- [ ] Draws the consequence that excludes a remedy class: writing the principle down more clearly cannot fix a retrievability failure
- [ ] Explains the instrument kind; does **not** re-classify errors (P5's job)

---

### **P7 — META-DECISION: Why did the July fix, which was correct and shipped, fail within a month? And what does this finding do to that finding?**
*The meta-structural payload. This is the piece that makes the account more than a gap list.*

- [ ] The evidence: the git diff (flat bag → four ordered passes + "do not collapse the passes into one motion"), `translation_method.md` created 2026-07-12, failing translation 2026-08-14
- [ ] The mechanism: the fix repaired **ordering**, one property adjacent to position, leaving vantage / scope / instrument / timing untouched — so the recurrence is what that fix *predicts*
- [ ] States why this forecloses stopping at the structural layer: a structural-only answer has already been produced once and its artifact is what failed
- [ ] Names the general form: a correct answer delivered against one property of a five-property object leaves four-fifths untouched
- [ ] **Relationship label to the prior inquiry chain committed** (REFINES / EXTENDS / SUPERSEDES) with its reason — the prior diagnosis is not wrong; it is under-dimensioned
- [ ] Says explicitly what of the prior chain **survives** (the enforcement gradient; the two-gate structure) and what is **subsumed** (the gradient becomes one axis of five)
- [ ] Contains no apology and no agent-blame

---

### **P8 — What actually enforced anything in the observed run, and who was doing it?**
*Register-sensitive. Highest misread risk in the finding.*

- [ ] The mechanism: 17/19 found on re-scans; each re-scan was a fresh turn created by the user asking; a fresh turn is structurally a separate call at the strong gradient end
- [ ] The in-turn Pass 4 found 0 of 19
- [ ] Develops the P5/P8 shared fact as the argument: the two errors the user found unaided are exactly the two only their vantage reaches
- [ ] The counterfactual: remove the two asks and the artifact ships with 19 errors under a PASS verdict
- [ ] The structural statement: **a necessary position was staffed by accident and never assigned**
- [ ] Framed as the arrangement's shape, never as a performance judgment — must remain true with any participant substituted
- [ ] States the consequence for scope: a frame containing only the written method cannot describe the enforcement that actually worked
- [ ] Explicitly names what an assigned division of labour would have to specify

---

### **P9 — Which limits are real, and which are excuses?**
*Independently grounded; parallelisable.*

- [ ] All four honest-limit claims run through the **substitution test** (restated with a human translator as subject), each verdict shown
- [ ] The result stated: 4/4 survive → these are properties of the arrangement, not of the agent
- [ ] The **inversion** developed: a model's context can be emptied by constructing a new call; a human translator's memory cannot — so the source-blind vantage is *more* occupiable here than in a human workflow, which normally solves it by hiring a second person
- [ ] States that the process is failing to use a capability it has
- [ ] The in-call impossibility stated with its mechanism: no operation removes information from a context; the check's question has already been answered by the context before the check begins
- [ ] The direct evidence: two explicit re-scans of the same text found 17 source-comparison errors and **zero** of the two target-only ones
- [ ] Every claim admitted here passes the substitution test; any that would fail is excluded and said to be excluded

---

### **P10 — What repairs what, and what is available now?**

- [ ] All six remedies, each typed by the property it repairs, with what it catches and its gradient position
- [ ] Availability marked per remedy; the headline stated: **five of six require nothing to be built**
- [ ] R1 (term-lock) specified concretely enough to act on: what is enumerated from the source, before drafting, in what artifact
- [ ] R2 specified as an enumeration, not a verdict — the checklist must force naming, or it degrades into checklist theatre
- [ ] R4 specified with its construction: separate call, target text only, **question-list output, no edit authority** — a reader that cannot write cannot invent
- [ ] X03 addressed by that construction and said to be so addressed
- [ ] R6 (the engine) marked as repairing the property July already tried to reach with prose
- [ ] The cost inversion stated: the remedy for the errors nobody could catch is the **cheapest call in the method**
- [ ] Remedies presented as complements typed by property, **not** as rivals for one slot
- [ ] No remedy consists of more prose in the same call (MQ4 exclusion)
- [ ] CN8/FP4 honoured: any "this is only a nudge" honesty is routed to authoring notes, never into runtime model-facing text

---

### **P11 — What should be done, in what order?**

- [ ] MUST / SHOULD / COULD / DEFERRED, each traced to a remedy in P10
- [ ] The **validation experiment** elevated to a MUST, specified concretely: a comparable section translated with R1–R4 in force and one without, counting errors — runnable now against the calibration corpus
- [ ] DEFERRED items each carry the gate that would un-defer them
- [ ] Availability marks from P10 drive MUST-vs-DEFERRED (contract)
- [ ] Distinguishes what changes in the SKILL from what changes in the working pattern
- [ ] No action proposes file reorganization or chunk-size change (MQ4 exclusions)

---

### **P12 — META-DECISION: How much weight does this finding carry, and where is it weakest?**

- [ ] **Split confidence** per the project's own discipline: structural distinctness of the five properties = HIGH, with its ground; empirical magnitude of any remedy = MED and **quarantined**
- [ ] The n split stated precisely: n=3 for the *pattern*, n=2 for the *translation-specific magnitude*
- [ ] The **third instance** reported: `structural_check.sh` specified by the traverse spec, absent from this repo, substituted with prose self-assessment at every handoff in this very inquiry
- [ ] Selection bias handled with its direction: the sample understates the vantage gap while making its proportions unusable
- [ ] **Self-reference scored concretely**: this loop is strong on position, weak on vantage, worst on instrument
- [ ] Consequence split: artifact-checkable claims are well-supported and re-derivable; judgment claims carry the same producing-context weakness the translation method carried
- [ ] Names the correction this finding cannot apply to itself, and what would supply it
- [ ] Reads as calibration, not as hedging — every caveat names what it would take to lift

---

### **P13 — What remains open?**

- [ ] Whether the five properties are **exhaustive** — flagged as unprovable from n=19
- [ ] Whether the remedy set is complete
- [ ] What the term-lock artifact's exact shape should be (resolvable in P11's MUST)
- [ ] Whether R2's enumeration belongs inside Pass 4 or as a new pass — noted as a downstream design question, not settled here
- [ ] Config-licensed drift: nothing currently distinguishes a licensed domestication from an unlicensed flattening, so part of the error count is unresolvable
- [ ] How much of the division-of-labour statement belongs in the SKILL versus in authoring notes, under CN8
- [ ] Whether an adversarial reader can be constructed adversarially rather than by instruction
- [ ] Each open item marked resolvable-here / resolvable-downstream / genuine frontier

---

## Step 5 — Interface Map

| From | To | What flows | Direction |
|---|---|---|---|
| P2 | P3 | the five properties, as the things to write determination rules for | one-way |
| P2 | P4 | the five properties, as the matrix's columns | one-way |
| P2 | P5 | the five properties, as the partition's kinds | one-way |
| P2 | P7 | "one property of five," the premise of the recurrence explanation | one-way |
| P2 | P10 | **vantage ⊥ position** — the reason R4 is not covered by R6 | one-way |
| P3 | P4 | the classification rules that make each cell reproducible | one-way |
| P4 | P5 | check IDs A1–A4 / B1–B11 + per-check property values | one-way (naming contract, bidirectional constraint) |
| P5 | P6 | the instrument kind, as the thing P6 explains | one-way |
| P5 | P8 | the vantage classification + the shared dual-use fact | one-way, contracted |
| P5 | P10 | the gap-kinds, as the remedy typing | one-way |
| P9 | P10 | the in-call impossibility → R4's separate-call construction | one-way |
| P10 | P11 | remedy set + availability marks → MUST/SHOULD/COULD/DEFERRED | one-way |
| P2 | P12 | the claim whose confidence is being split | one-way |
| all | P13 | what each piece left unresolved | one-way |
| all | P1 | conclusions only, no evidence | one-way |

### Assumptions-not-data check *(required refinement — hidden coupling hides in assumptions)*

| Assumption | Held by | About | Made explicit as |
|---|---|---|---|
| Check IDs are stable across P4 and P5 | P5 | P4 | **naming contract** — P4 owns the IDs; P5 cites, never renames |
| The gap-kinds are exactly five and identically named | P10, P11 | P5 | **vocabulary contract** — P5 owns the kind names |
| The scope adjudication (SKILL + working pair) is settled | P8 | *upstream, not a sibling* | flagged: this comes from Sensemaking, not from another piece — P8 must not re-adjudicate it |
| The reader has not seen the matrix | P1 | P4 | **register contract** — P1 must be readable standalone |
| Availability marks are load-bearing for prioritisation | P11 | P10 | **contract** — P10 must mark every remedy, no blanks |
| The claim's shape is what confidence attaches to | P12 | P2 | **contract** — if P2's property count changes, P12's scoping is invalid |
| The recurrence story is told once as evidence and once as conclusion | P1, P7 | each other | **redundancy contract** — P1 gets one sentence; P7 gets the evidence and mechanism |
| Classification is decidable without knowing the answer | P4, P5 | P3 | **decidability contract** — if a P3 rule requires the answer to apply, P4/P5's cells are unreproducible |

The last row is the highest-risk hidden coupling: P4 and P5 were populated during Sensemaking by direct judgment. If P3's rules cannot reproduce those cells, the frame is post-hoc and P3 fails. **P3 must be validated against at least two P4 rows.**

---

## Step 6 — Dependency Order

```
TIER 0  (root, blocks everything)
        P2  the five-property claim
              │
TIER 1  ──────┼──────────────────┐
        P3 determination      ┌──┴─ P9 honest limits  (INDEPENDENT — parallel from the start)
        mechanism             │
              │               │
TIER 2  ──────▼───────────────│
        P4  the matrix        │
              │               │
TIER 3  ──────▼───────────────│
        P5  gap partition     │
         ┌────┼────┬──────────│──────┐
TIER 4   ▼    ▼    ▼          │      │
        P6   P7   P8          │      │   (parallel — three independent narratives)
                              │      │
TIER 5  ──────────────────────▼──────▼
        P10  remedies typed + availability
              │
TIER 6  ──────▼
        P11  next actions
              │
TIER 7  ──────▼
        P12  weight and weakness   ←  scores everything above
              │
TIER 8  ──────▼
        P13  open questions
              │
TIER 9  ──────▼
        P1   the direct answer   (authored LAST, positioned FIRST)
```

**Parallelisable:** P9 from tier 0 alongside the whole α→β chain. P6 / P7 / P8 with each other at tier 4.
**Circularity check:** none. Every edge is one-way; the two bidirectional-looking constraints (P4↔P5 IDs, P1↔P7 redundancy) are naming/redundancy contracts resolved by ownership assignment, not by mutual dependency.
**Critical path:** P2 → P4 → P5 → P10 → P11. Five tiers; everything else hangs off it.

---

## Step 7 — Self-Evaluation

### Minimum three dimensions

| Dimension | Check | Verdict |
|---|---|---|
| **Independence** | Each piece's question answerable without reading siblings, except through defined interfaces | **PASS** — P9 is fully independent; the α→β→δ chain flows through thin, named interfaces; P1 and P13 are consumption-only by design |
| **Completeness** | No aspect of the whole falls through the gaps | **PASS with one repair** — the initial 13-element enumeration had no piece for *how to classify a new check*. The Determination-mechanism check fired and added **P3**. Without it the frame would be a post-hoc taxonomy of 19 known errors, and Reassembly would fail: reconstructing the whole requires the classification, and no piece supplied it |
| **Reassembly** | Pieces + interfaces reconstruct the original problem's solution | **PASS** — a reader who has P1 (the answer), P2+P3 (the frame and how to use it), P4+P5 (the evidence and its sorting), P6+P7+P8 (what "missing" means, why the last fix failed, what actually enforced anything), P9 (which limits are real), P10+P11 (what repairs what and what to do), P12 (how much to trust it) and P13 (what is open) has the user's question answered at the committed depth |

### Full evaluation — remaining four

| Dimension | Verdict |
|---|---|
| **Tractability** | **PASS** — every piece is one focused pass. P4 is the largest but is tabular; P10 is the largest prose piece and is bounded at six entries |
| **Interface clarity** | **PASS** — 15 interfaces mapped, 8 assumptions surfaced and converted to named contracts. Highest residual risk is the **decidability contract** (P3 must reproduce P4's cells); flagged for Innovation, not hidden |
| **Balance** | **PASS with a note** — P2, P7 and P10 carry the most weight; P6, P9, P12 are mid-weight; P1, P3, P5, P11, P13 are lighter. No piece approaches 80%. P4's bulk is tabular rather than analytical, so its apparent size overstates its cost |
| **Confidence** | **HIGH** — top-down and bottom-up agreed on 12 of 13 boundaries; the thirteenth (the P5/P8 dual-use fact) was resolved by an ownership contract rather than a re-cut |

### Failure modes checked

- **Premature decomposition** — not fired. Sensemaking produced a stable SV6 with a single major revision and no Accommodation-trigger fire.
- **Wrong boundaries** — not fired. Every cut is at a valley; interface traffic is thin everywhere (names, IDs, classifications — never bodies of argument).
- **Hidden coupling** — **actively hunted**: the Assumptions-not-data check surfaced eight, all converted to explicit contracts. The decidability contract is the one worth watching.
- **Missing pieces** — **fired and repaired.** P3 was absent from the initial enumeration; the Determination-mechanism check caught it.
- **Over-decomposition** — **fired twice and repaired**: E8 merged into P7, and E13+E14+E15 merged into P12. Both would have been sub-paragraph fragments alone.
- **Ignoring dependencies** — not fired. Nine tiers, no cycles, critical path named.
- **Imbalanced decomposition** — not fired; see Balance.

---

## Final Deliverable

**13 pieces**, dependency-ordered, with 15 mapped interfaces and 8 named contracts.

Three are **META-DECISION** pieces requiring piece-level inversion at Innovation:

- **P2** — the five-property claim (framing-semantic; the whole finding rests on it)
- **P7** — why July's fix failed + the relationship label to the prior inquiry chain
- **P12** — split confidence, the third instance, and the self-reference scoping

One is **register-critical**: **P8** (what actually enforced anything) carries the highest misread risk in the document and must remain a statement about the arrangement's shape under any substitution of participant.

One is **evidence-artifact**: **P4** (the 15-check matrix), to be rendered compactly with every cell traceable.

One was **added by a self-evaluation check** rather than by the initial reading: **P3** (the determination mechanism), without which the frame is a post-hoc taxonomy rather than a tool.
