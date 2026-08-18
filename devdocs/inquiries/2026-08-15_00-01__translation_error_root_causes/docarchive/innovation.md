# innovation — translation error root causes

## User Input

```
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-08-15_00-01__translation_error_root_causes/_branch.md

Upstream outputs — read all in full: articulate_simple.md + surfacing.md + articulate_warm.md + sensemaking.md + decomposition.md.

PRODUCTION-TASK MODE. Decomposition's 13 pieces (P1–P13) are the seed structure. Generate the actual finding content for each. Dependency order: P2 → P3 → P4 → P5 → {P6, P7, P8} → P10 → P11 → P12 → P13 → P1 (P9 parallel from the start; P1 authored last, positioned first).

[P1–P13 briefs as given: P1 direct answer in plain language, register piece · P2 META the five-property claim · P3 the determination mechanism with decidability contract · P4 EVIDENCE the 15-check matrix · P5 the five-kind gap partition · P6 what "missing" means · P7 META why July's fix failed + relationship label · P8 REGISTER-CRITICAL what actually enforced anything · P9 which limits are real · P10 what repairs what and what's available now · P11 next actions · P12 META how much weight this carries · P13 open questions]

PIECE-LEVEL INVERSION REQUIRED on P2, P7, P12.

CRITICAL CONSTRAINTS: anti-hallucination (every claim grounded in F1–F11, a file read, a session-record fact, or a flagged extrapolation) · the 8-item NOT-list (no re-translating · no re-litigating error verdicts · no apology · no terminal agent-blame · no file reorganization · no smaller chunks · no more-prose-in-the-same-call as THE remedy · no shallow account) · bias-balance surfaced not buried (X01→P8, X03→P10, X09/X10/G08→P12, X11→P13) · the decomposition contracts (P4 owns check IDs; P5 owns gap-kind names; P1 standalone-readable; P10 marks availability with no blanks; P1 gets ONE sentence on the recurrence; P3 must demonstrate decidability against P4) · register: an answer to a person who asked a genuine question and said "i understand you are ai but i am wondering what was missing."

Save innovation output to: .../innovation.md
```

---

## Phase 1 — Seed + Methodology-Mode Consideration

**Seed type:** *Failure* — "this didn't work, but why?" — with an unusual property: the failure recurred one month after a correct fix was shipped, which makes the seed doubly loaded (the failure, and the fix's failure).

**Seed framing's central assumption:** the five-property claim is correct, and Innovation's job is to elaborate it into finding text.

- **(a) Inherited methodology mode:** **Standard default** (balanced 4G + 3F). Text signals in the seed framing: "generate the actual finding content," "produce," an explicit piece list with per-piece briefs.
- **(b) Alternative mode named:** **Contrarian-rethink (Framer-weighted).**
- **(c) What follows under the alternative:** mechanisms would weight toward challenging the five-property claim rather than elaborating it — candidates would ask whether "a check" is the right unit at all, whether the five are the right cut, and whether the whole frame should be discarded for something simpler. The candidate space would be thinner on finding-text and thicker on frame-alternatives, and the run would not produce a shippable finding.
- **(d) Decision — DEFAULT (Standard).** Reason: the Piece-Level Inversion Rule already forces contrarian pressure at every meta-decision piece, which is precisely where a Contrarian-rethink run would aim. Running Standard mode *with* the piece-level rule captures the alternative's value without sacrificing the production output. The contrarian pressure is recorded per piece below, not suppressed.

---

## Phase 2 — Generate

### M1 · Absence Recognition *(Generator — both levels + bidirectional, mandatory)*

- **Patch-level (generic).** Missing from the current design: a check that reads the English alone; a check that compares draft against config; a rule that re-runs a check after an edit; an index from source-features to principles. → feeds **P4, P5, P10**.
- **Redesign-level, "what's missing" (focused).** If the method were designed from scratch today, a check would be **declared as a tuple** — `(what, vantage, instrument, position, invalidated-by)` — rather than written as a sentence. A sentence cannot be audited for its vantage; a tuple can. → feeds **P2, P3, P10**.
- **Redesign-level, "what's already present in different form" (focused).** The project **already does this**, in the inquiry pipeline. `/traverse` declares per discipline: which spec is loaded (*what*), a separate call (*position*), a structural check (*instrument*), an emitted artifact, and a handoff order (*timing*). The capability exists in articulated form one directory away from the translation method, which has no equivalent declaration for any of its checks. → feeds **P2, P12**. **High signal.**
- **Contrarian.** Perhaps nothing is missing and the correct move is **removal** — shrink the method's claims to what a single call can actually enforce, and state honestly what it does not catch. → feeds **P10's shape-inversion, P13**.

### M2 · Combination *(Generator)*

- **Generic.** five-properties × the 19-error set → **the matrix** (P4) and **the partition** (P5).
- **Focused.** enforcement gradient × vantage → **they are orthogonal**, from which follows a non-obvious consequence: *building the engine does not subsume the source-blind reader.* A separate call that contains the source is the strong position at the wrong vantage. → feeds **P2, P10**.
- **Contrarian.** substitution test × the AI/human asymmetry → an inversion neither contains alone: **a model's context can be emptied by constructing a new call; a human translator's memory cannot.** Human translation workflows solve this by hiring a second person. This process can get the same vantage for the price of one cheap call and is not using it. → feeds **P9**.

### M3 · Domain Transfer *(Generator — native source mandatory)*

- **Native #1 (software process).** *Separation of duties / four-eyes*: the author of a change cannot approve it — not because authors are careless, but because approval requires a vantage the author cannot occupy. → **P8, P9**.
- **Native #2 (software testing).** *A test with no assertion passes.* A check with no instrument is an assertion-free test: it runs, reports green, and proves nothing. → **P4, P6**.
- **Different-field (publishing).** Copy-editing is a separate role for structural reasons, not moral ones. → **P9**.
- **Different-field (aviation/medicine).** A checklist is **read, not recalled** — a recalled checklist is not a checklist. This is exactly the forced-enumeration point, and it is why R2 must name items rather than ask for a verdict. → **P10 (R2)**.
- **Contrarian (law).** Discovery obligations require **producing a list**, not answering "is there anything relevant?" The list *is* the mechanism. → **P10 (R1)**.

### M4 · Extrapolation *(Generator)*

- **Generic.** If nothing changes, the next translation produces a similar error count under similar scrutiny, and the count will again be read as a quality signal when it is a scrutiny signal. → **P12**.
- **Focused — a falsifiable prediction.** If only R6 (the engine) is pursued and R1–R4 are deferred, the engine will be built, will repair **position**, and vantage / scope / timing / instrument errors will survive it — producing a **third recurrence with the engine in place**. → **P7, P11**. *(Flagged: extrapolation, not evidence.)*
- **Contrarian.** If the five-property frame is adopted and then written into the SKILL **as prose**, it becomes the fourth instance of the pattern it describes. The frame must ship as an artifact-emitting requirement, not as a description. → **P10, P12**.

### M5 · Lens Shifting *(Framer)*

- **Generic.** Under a *quality* lens this is "the translation had errors." Under a *specification* lens it is "the method could not state what its checks were." The second lens is where the answer lives, and it is the lens under which the July fix's failure stops being surprising. → **P1, P2**.
- **Focused.** Under the *user's* lens: they asked twice, and both asks worked. They had already found the remedy empirically. The finding's job is to name what they were doing so it can be done on purpose. → **P8**.
- **Contrarian.** Under a *research-artifact* lens (this is a method under development, not a production system), 19 errors in a first-pass literary translation is unremarkable and the diagnosis is over-engineering. → **P12, P13**. Surfaced, not buried.

### M6 · Constraint Manipulation *(Framer — both directions mandatory)*

- **ADD (generic).** Add: *no new prose may be added to any runtime file.* What survives? R1 (an artifact), R2 (an enumeration artifact), R4 (a call construction), R6 (an architecture). R3 survives as an invalidation rule attached to an artifact rather than as a sentence. **The remedy set satisfies the constraint** — which is the test that it isn't secretly more-prose-in-the-same-call. → **P10**.
- **REMOVE (focused).** Remove: *verification happens after drafting.* Then R1 is not a verification at all — it is a **pre-commitment**. You cannot fail to notice a polysemous word you enumerated before you started writing. This reframes the highest-value remedy from detection to **prevention**. → **P10 (R1)**. **High signal.**
- **Contrarian ADD.** Add: *the human is unavailable.* Everything that actually enforced anything disappears. This is P8's counterfactual made structural. → **P8**.

### M7 · Inversion *(Framer — piece-level at meta-decision pieces, with depth-check)*

**P2 · framing-semantic property.** Assumption: *checks have five separable properties, and the method's defect is failing to distinguish them.*
- **L1 (component):** "the method distinguishes *too much* already — 3,489 lines of distinctions — and a five-way taxonomy makes it worse." Component-level; invert again.
- **L2 (system):** "the defect is not the number of distinctions but that **none of them are declarative** — the method *describes* checks in prose rather than *declaring* them as data." This does not replace the principal candidate; it gives it its correct remedy shape: **declare, don't describe.**
- **L3 (existence axis):** "what if the count should be **zero** — no 'checks' at all, and correctness should be structural (you cannot produce an output that violates the constraint) rather than inspectional?" Partially achievable, and it yields the run's sharpest insight: **R1 is prevention, not detection.** A term-lock does not make an error easier to catch; it makes it harder to commit. Survives and refines the principal candidate.

**P7 · relationship-label property.** Assumption: *this finding REFINES the prior chain.*
- **Inversion:** "the prior diagnosis was **wrong**, and this finding CORRECTS it." What follows: the prior located the root cause in the un-run 3-Pass method; if wrong, running the passes separately would not help. But **F8 shows separate calls did help** (17/19 found in exactly those turns). The inversion **fails on evidence**. REFINES holds.
- **SUPERSEDES tested separately:** does this finding replace the prior? No — the prior's Gate 1 (lock meaning first, config-blind) is still correct and is not restated here. Not SUPERSEDES.
- **Depth-check → system level:** "the relationship isn't between two findings; it's that **the inquiry corpus has no mechanism for testing whether a shipped fix took**." A fix was written, shipped, and its failure was discovered only because a *new* failure prompted a *new* inquiry. Survives → **P13 frontier**.

**P12 · framing-semantic + evaluation-criterion.** Assumption: *split the confidence — structure HIGH, magnitude quarantined.*
- **Inversion:** "don't split — the whole thing is MED, because the structural claim also rests on this context's judgment." Partially holds, but fails on a real difference: the structural claims are **artifact-checkable by a third party** (anyone can open `translation_method.md` and read that Pass 4 excludes config checks). Judgment claims are not. The split survives and the inversion **sharpens its criterion**: HIGH is warranted only where a disagreeing reader could point at a file.
- **Existence axis:** "zero confidence discussion — state the claims and let the reader judge." Rejected with reason: the project's own FP3 discipline requires the split, and without it the magnitude claim reads as measured when it is not.

**P10 · intervention-shape commitment property (fires retrospectively; see audit).** Assumption: the remedies commit to **ADD-CONTENT / ADD-TEST** shapes.
- **Shape-axis inversion → REMOVE.** Delete the method's unenforceable claims rather than adding enforcement to them. What follows: the method shrinks to the handful of checks it can actually instrument, and everything else moves to an explicit "this method does not catch X, Y, Z" statement.
- **Both tested (Phase 3).** ADD survives — five of six remedies are cheap and one is preventive rather than additive-checking. REMOVE **partially survives** and is carried as **DEFERRED with a revival trigger**: *if the validation experiment shows R1–R4 produce no measurable reduction, REMOVE becomes the honest move.*

---

## Inherited Frame Audit

**Step (i) — seed-level central assumption:** *the five-property claim is correct; elaborate it.*

**Step (iii) — challenge scan:** challenged explicitly by **M7-P2 L1** ("the method distinguishes too much already"), **M7-P2 L3** (existence axis: zero checks), **M5-contrarian** ("research artifact — the diagnosis is over-engineering"), and **M1-contrarian** ("nothing is missing; remove instead"). → **not un-challenged.**

**Step (ii/iii) — piece-level commitments:**

| Piece | Property | Load-bearing commitment | Explicitly challenged by |
|---|---|---|---|
| P2 | framing-semantic | the five-property frame | M7-P2 L1 / L3; M5-contrarian |
| P5 | lesson-vocabulary | exactly five gap-kind names | M7-P2 L1 (count challenge); carried into P13 as exhaustiveness-unprovable |
| P7 | relationship-label | REFINES | M7-P7 (CORRECTS + SUPERSEDES both tested) |
| P10 | **intervention-shape** *(fires retrospectively — P11 operates under it)* | ADD-CONTENT / ADD-TEST | M7-P10 shape-axis inversion → REMOVE; M1-contrarian |
| P12 | evaluation-criterion | split confidence | M7-P12 (don't-split; zero-discussion) |

**Step (iv) — firing condition: the audit does NOT fire.** Every seed-level and piece-level commitment has at least one explicit challenge in the candidate set. Proceed to Phase 3.

*Note: P10's property (v) was not visible at initial classification and was caught by the retrospective self-audit, which the Meta-Decision-Piece Criterion's edge-case clause requires. Its shape-axis inversion was generated and tested before publication, as the Intervention-Shape-Axis Inversion rule requires.*

---

## Phase 3 — Test

The 5-test cycle on the principal survivors. Compact form; the strongest objection is stated for each.

| # | Candidate | Novelty | Scrutiny survival — strongest objection and response | Fertility | Actionability | Mechanism independence | Disposition |
|---|---|---|---|---|---|---|---|
| C1 | **The five-property frame** | Yes — no upstream artifact states it; the project had only the one-dimensional gradient | *"It's an invented decomposition; the real story is non-compliance."* Fails: the mechanised check and the separate-call re-scans both succeeded. If the story were compliance, those would have failed too. The differentiator is the property, not the effort | High — generates the matrix, the partition, the remedy typing, and a forward classification rule | Yes — P3 makes it applicable to unseen checks | M2 (combination), M1 (redesign-level), M7 (inversion refines it) — **three, from different grounds** | **ACTIONABLE** |
| C2 | **Vantage ⊥ position** | Yes — the inherited gradient collapses them | *"A separate call always has controlled inputs, so the distinction is academic."* Fails: the re-scans *were* separate calls with the source included and found zero of the two target-only errors. The distinction is observed, not theoretical | High — it is why R6 does not subsume R4 | Yes — it changes the remedy ordering | M2-focused, M7-P2; also independently implied by M3's four-eyes transfer | **ACTIONABLE** |
| C3 | **R1 is prevention, not detection** | Yes — reframes the leading remedy's category | *"An enumeration can be produced and then ignored."* Partially holds — which is why R1's artifact must be produced *before* drafting, so the draft is written against it rather than checked by it | High — reframes the whole remedy set from detection to a mix | Yes — specifies when R1 runs | M6-REMOVE and M7-P2-L3 reach it independently; M3-law (produce a list) supports | **ACTIONABLE** |
| C4 | **Declare, don't describe** | Yes | *"Declaration is just prose in a table."* Fails on a structural difference: a tuple has slots, and an empty slot is visible. A sentence has no empty slots — a check with no stated vantage looks complete | High — it is the shape any SKILL change must take | Yes | M1-redesign and M7-P2-L2 | **ACTIONABLE** |
| C5 | **The AI-favouring inversion** (a model's context can be emptied; a human's memory cannot) | Yes — inverts the expected direction of an AI limitation | *"It's a rhetorical flourish."* Fails: it has an operational consequence — the vantage costs one cheap call here and a second salaried person in a human workflow | Medium-high | Yes — it is the argument for R4's priority | M2-contrarian, M3-publishing | **ACTIONABLE** |
| C6 | **The engine-only prediction** (build R6 alone → a third recurrence) | Yes | *"Unfalsifiable until someone builds it."* Holds as an objection — it is a prediction, not evidence | High — it is testable | Yes — it changes build ordering | M4-focused only, single-mechanism | **DEFERRED** — revival trigger: *if R6 is scheduled before R1–R4* |
| C7 | **REMOVE instead of ADD** (shrink the method to what it can enforce) | Yes | *"It abandons the method's ambition."* Partially holds — and the counter (five remedies are cheap) is currently stronger, but is itself unmeasured | High — it is the honest fallback | Yes | M1-contrarian, M7-P10 shape inversion | **DEFERRED** — revival trigger: *if the validation experiment shows no measurable reduction from R1–R4* |
| C8 | **The corpus has no post-ship verification** | Yes | *"Out of scope — this is about translation."* Holds as a scope objection; the observation is real but belongs to a different layer | High | Not here | M7-P7 depth-check only | **RESEARCH FRONTIER** → P13 |
| C9 | **HIGH confidence requires pointability** (a disagreeing reader can open a file) | Yes — sharper than "follows from what a check is" | *"Artifact-checkability isn't the same as correctness."* Correct, and conceded — it is a *transferability* criterion, not a truth criterion, and is stated as such | Medium | Yes — it sorts the finding's own claims | M7-P12 inversion | **ACTIONABLE** |

### Artifact-grounding (6th test, conditional — fires: the run produces committed cell values about project state)

Every matrix cell and every gap-kind assignment was checked against project artifacts read this session: `translation_method.md`, `SKILL.md`, `harmony_layer.md`, `case_catalog.md`, `schemas.py`, the git diff, filesystem mtimes, and the delivered translation. **One contradiction found — see the RE-TEST TRIGGER below.**

### RE-TEST TRIGGER (fires)

Performing the per-error assignment (P5) rather than estimating it contradicts a headline count committed at Sensemaking. Sensemaking stated *instrument 8 / vantage 2 / scope 1 / timing 1 / position the rest* **before** the assignment was carried out. The actual assignment yields **instrument 10 / position 6 / scope 1 / vantage 1 / timing 1 = 19**, and finds that Sensemaking's "vantage 2" **double-counted the pronoun error**, which is both target-only-detectable and revision-caused.

**Re-test result:** the corrected counts are adopted; the pronoun error is assigned to **timing** (proximate — it did not exist in the first draft) with **vantage** recorded as its secondary property, and it is the only error with two. **The direction of every argument is unchanged; only the counts move**, and the vantage count moving *down* is handled honestly in P12 rather than smoothed — with X09's note that the observed vantage count is a lower bound by construction.

---

## THE FINDING CONTENT

*Generated per piece, in dependency order. Reading order is P1 first.*

---

### P1 — The direct answer

*(authored last; positioned first)*

You asked why these errors happened and what was missing in the process. Here is the honest answer.

**Nothing was missing from what we knew.** The rule that would have caught the dropped repetition is written in the catalog, correctly. So is the one about a question that is really an assertion. So is the one about a word's buried root carrying a second meaning. All 698 lines of that file were read into context before the translation started, along with 2,791 more lines of method, tiers, axes, and policies. The knowledge was there and it did not fire.

**What was missing was a distinction.** The method talks about "checks" as if a check were one kind of thing. It isn't. Any check has five separate properties: *what* it looks at, *from what position* — meaning what has to be in front of the checker and what has to be absent — *with what instrument*, meaning whether it produces something you can look at or just a verdict, *with what force*, meaning whether the checker could have ignored it, and *when*, meaning what makes its result stale. These five vary independently. The method never separates them, so it can't specify them, can't audit them, and can't fix them one at a time.

Every one of the nineteen errors is a failure of one of those five, and they sort cleanly. Ten happened because the check that would have caught them **had no instrument** — no list to work through, just an instruction to be thorough. Six happened because the right check existed, was correctly aimed, and was **prose inside the same forward motion** that produced the text; it ran and found nothing. One happened because Pass 4 **excludes** policy checks by its own definition, so nothing anywhere in the method was looking. One happened because a check that catches it would have to read the English **without the Turkish in front of it**, and no step in the method stands there. And one was correct in the first draft and broken by a later tidying edit, because **nothing re-checks after an edit**.

**What was not wrong:** not the chunk size — both chunks ran at about half the stated limit. Not the reference documents — their content is right. Not the diagnosis from last time — it was correct as far as it went. And not a lack of care; the pattern in the evidence is not that effort varied, it's that effort produced results wherever a check had an instrument or its own call, and produced nothing everywhere else.

**One more thing, and it is the part that matters most.** The same failure was diagnosed in July, a fix was written, and the fix was shipped into the SKILL — and the same class of error recurred a month later, because that fix repaired the *ordering* of the passes and left the other four properties exactly as they were.

**And you were the enforcement.** Seventeen of the nineteen surfaced on re-scans, and every re-scan was a fresh turn because you asked for one — which is structurally the strong form of checking that the method describes but cannot perform inside a single motion. The two you found unaided are exactly the two that can only be seen by reading the English on its own, which is the one position nothing in the method occupies. If you hadn't asked twice, the translation would have shipped with nineteen errors under a verdict of PASS.

The rest of this document shows the evidence, and lists what repairs what. Five of the six repairs need nothing built.

---

### P2 — The central claim

**A check is not one thing. It is five.**

| Property | What it is | The question it answers |
|---|---|---|
| **What** | the check's subject — the thing it is defined to look at | *is this check named anywhere, or assumed?* |
| **Vantage** | what must be **present in**, and **absent from**, the checking context | *can this question be answered without the source — and does having the source change the answer?* |
| **Instrument** | script · forced enumeration · prose judgment | *does this check produce something you can look at, or only a verdict?* |
| **Position** | prose-instruction · emitted-artifact · separate-call | *could the checker act on material this check forbids?* |
| **Time** | the check's validity window relative to edits | *what invalidates this result, and does anything re-run it?* |

**These vary independently, and the evidence demonstrates each pair.**

- *Vantage vs instrument.* A3 (sentence boundaries: source+target, script) and A1 (content dropped: source+target, prose). Same vantage, different instrument, opposite outcomes.
- *Instrument vs position.* The user-prompted re-scans used prose instruments at a separate-call position and found 17 errors; the in-turn Pass 4 used prose instruments at a prose position and found none.
- *Vantage vs position.* Those same re-scans were at the strong position **with the source present**, and found **zero** of the two target-only errors.
- *Scope vs everything.* The policy check has no vantage problem, no instrument problem, no position problem, and no timing problem. It has no definition.
- *Time vs everything.* The regression passed every check that ran. The check simply ran before the edit.

**Vantage ⊥ position.** This is the consequence that is easy to miss and expensive to miss. A separate call is a *positional* move — it buys you the ability to control what is in the context. Removing the source from that call is a *vantage* move — it exercises that ability. The enforcement gradient inherited from this project's own design notes collapses the two, because separate calls conventionally have controlled inputs. They are not the same, and the evidence separates them: a strong-position call that still contained the source found none of the errors only the empty-context vantage can reach.

**Why this is the core rather than one more gap.** A gap list of any length still leaves the reader without a way to tell whether the list is complete, and without a way to place a gap that isn't on it. The five properties are the abstraction under which every gap in the evidence, every remedy, and — critically — **every previous fix** becomes classifiable. It is the level at which the July fix's failure stops being a surprise and becomes a prediction. That is what makes it the answer to "most core" rather than another entry in the same register as the thing that already failed.

**Relationship to the enforcement gradient.** The gradient (prose-instruction < emitted-artifact < separate-call), committed by this project's own design notes, is **one of the five axes** — the *position* axis — not the whole object. It remains correct. It is not sufficient, and the next section says exactly where it stops being sufficient.

**The nesting is PARTIAL, and the residue is the informative part.** It is tempting to fold everything under position: every gap was knowable, several were written down, and all persisted because they sat at the weakest gradient position. That holds for the six position-kind errors. **Three gaps survive a move to the strong end:**

1. **Scope is position-independent.** Pass 4 excludes config checks *by definition*. Run it as a separate call, as a script, as a human gate — it still does not check what it was never defined to check. Scope is upstream of position.
2. **Vantage requires position *and* construction.** Position gives the ability; only construction exercises it.
3. **Timing is a missing rule.** At any position, a rule that is not stated does not run. Position affects how *visible* the omission is — in a call-based pipeline, editing a draft after verification visibly invalidates the verification's input — but the rule has to exist either way.

**Confidence: HIGH.** The ground is not the error count. It is that each axis is shown varying while the others are held fixed, by a specific pair in the evidence, and that a disagreeing reader can check every pair against a file or a session record.

**Inversion-candidate, generated and tested.** *Assumption reversed: that the method's defect is failing to distinguish, rather than distinguishing too much.* The method already carries 3,489 lines of distinctions across eight files; adding a five-way taxonomy could plausibly make the load worse rather than better. Driven to system level, this does not overturn the claim — it corrects its remedy shape. The defect is not the *number* of distinctions but that **none of them are declarative**: the method *describes* checks in sentences rather than *declaring* them as data. A sentence has no empty slots, so a check with no stated vantage looks complete; a tuple has slots, and an empty one is visible. Driven one level further, on the existence axis — *what if there should be no checks at all, and correctness should be structural rather than inspectional?* — the inversion yields this run's sharpest result and is carried into P10: **the highest-value remedy is preventive, not detective.**

---

### P3 — How to classify a check that has never been run

The frame is only worth something if it applies forward. Five determination questions, each answerable about a check nobody has performed:

| Property | Determination question | Values |
|---|---|---|
| **What** | Is this check named in a document, or is it assumed by the person running it? | named · assumed |
| **Vantage** | Can the question be answered without the source? **And** does having the source available change the answer? | *no / n.a.* → source+target · *yes / yes* → **target-only** · needs the config → config+target · needs only the source → source-only |
| **Instrument** | Does the check produce an artifact you can inspect afterwards, or only a verdict? | script · forced enumeration · prose-only |
| **Position** | Could the checker act on material this check forbids? | *yes* → prose-instruction · *only via an emitted artifact* → emitted-artifact · *no, the material isn't in the call* → separate-call |
| **Time** | What invalidates this result, and does anything re-run it when that happens? | *(the invalidator; and whether a re-run rule exists)* |

**The vantage rule is the one that matters and the one that is easy to get wrong.** Both halves are required. "Can it be answered without the source?" alone is not enough — plenty of checks *could* be answered without the source but are not damaged by having it. The second half is the discriminator: **if having the source changes the answer, the check requires the source's absence.** That is what makes it a different vantage rather than a different mood.

**Decidability demonstration** *(the contract this piece owes: reproduce cells from P4 without looking at them)*

**A1 — "was source content dropped?"**
*What:* named, in Pass 4. *Vantage:* answerable without the source? No — you need the source to know what is missing → **source+target**. *Instrument:* produces a verdict ("nothing dropped"), no artifact → **prose-only**. *Position:* could the checker act on material the check forbids? Yes — the same context that dropped the word asserts nothing was dropped → **prose-instruction**. *Time:* invalidated by any edit; nothing re-runs it.
→ **Reproduces P4's A1 row exactly.**

**B8 — "does every referring expression have a recoverable antecedent?"**
*What:* not named anywhere → **assumed/absent**. *Vantage:* answerable without the source? **Yes** — "does 'it' have an antecedent in this English text" is fully answerable from the English. Does having the source change the answer? **Yes** — with the source present the checker already holds the referent and reads it as resolvable → **target-only**. *Instrument:* would produce a list of referring expressions with their antecedents → **forced enumeration available**. *Position:* the vantage requires an absence, so → **separate call with controlled input**. *Time:* invalidated by any edit touching a referring expression.
→ **Reproduces P4's B8 row exactly.**

**Worked example on a check that is not among the nineteen.** *"Is the footnote density right for this config?"* — the run used A7 = standard, which specifies 1–3 footnotes per page.
*What:* not named anywhere. *Vantage:* answerable without the source? Yes. Does the source change the answer? No — but the **config** is required → **config+target**. *Instrument:* count footnotes, count pages → **trivially scriptable**. *Position:* nowhere — Pass 3 applies the config without verifying it and Pass 4 excludes config checks. *Time:* invalidated by adding or removing any footnote.
→ Classifies as a **scope** gap: the same kind as the honorifics violation, in a check nobody has ever run and no error in this set revealed. The frame predicts a gap rather than only labelling known ones.

---

### P4 — The evidence: fifteen checks, scored

*This piece owns the check IDs. Every cell traces to a file read or a session record.*

**A. Checks the method performs (Pass 4)**

| ID | Check | Vantage | Instrument | Position | Would catch | Observed result |
|---|---|---|---|---|---|---|
| A1 | Was source content dropped? | source+target | prose-only | prose-instruction | `içyüzü` · dropped subject · `dirhem`×3 · `zarurî` | **FAILED** — passed all |
| A2 | Was anything invented or added? | source+target | prose-only | prose-instruction | doubled verb · "never" | **FAILED** — passed both |
| A3 | Were sentence boundaries preserved? | source+target | **script** | script-gate | merges / splits | **HELD** — and discovered that `..` marks internal suspension, not sentence end |
| A4 | Did large-scale structure survive? | source+target | prose-only | prose-instruction | section / order loss | passed — arguably correctly; none occurred |

**1 of 4 instrumented. That one held. The other three passed a draft carrying fifteen real violations.**

**B. Checks the method does not perform**

| ID | Check | Vantage | Instrument available | Would catch | Why absent |
|---|---|---|---|---|---|
| B1 | Word-sense adjudication per polysemous term | source-only | forced enumeration | `dirilmek` · `bazı` · `bitiyor` · `kadîm` | Pass 1 nominally does this but **emits nothing**, so no artifact survives to check against |
| B2 | Repetition-count comparison | source+target | forced enumeration / script | `dirhem`×3 | harmony Tier 3 states the rule with no firing condition |
| B3 | Cognate / shared-root cluster consistency | source+target | forced enumeration | `hâsiyet`/`hâssa` | same |
| B4 | Multi-sense / pun preservation | source-only → source+target | forced enumeration | `eşeklik` | catalog entry exists (l.359); no index to retrieve it by |
| B5 | Quantifier / intensifier inventory diff | source+target | forced enumeration | (covered by A1/A2 in this set) | not specified |
| B6 | Source-form preservation (transliteration, diacritics) | source+target, char-level | **script** | silent normalization | not specified |
| B7 | **Policy conformance** (7 policies × draft) | **config+target** | forced enumeration | `Cenab-ı Hak` | **excluded by Pass 4's own definition** |
| B8 | **Referent resolution** | **target-only** | forced enumeration | the bare "it" | no pass occupies this vantage |
| B9 | **Naive-reader parse** — does the English assert what the source asserts, read cold? | **target-only** | prose, from a controlled context | the `istifham-ı inkârî` inversion | same |
| B10 | **Post-revision re-run** | inherits the original check's | **a rule, not a judgment** | the regression, as a class | not specified at all |
| B11 | Config-licensed-drift adjudication | **config+target** | forced enumeration | would *classify* `İslâm ordusu` · `bozmak` · `istimdad` as licensed or drifted | nothing compares draft against config |

**Coverage:** of fifteen checks that should exist, the method specifies four, instruments one, and stands at **two of five vantages**. The three checks addressing error classes for which **no vantage in the method is capable of detection** — B7, B8, B9 — are exactly the ones whose errors survived to delivery.

---

### P5 — Which kind is each of the nineteen

*This piece owns the gap-kind names. It classifies; it does not argue, and it does not revisit whether any item is an error.*

| Gap kind | Failed property | Errors | Count |
|---|---|---|---|
| **Instrument** | no artifact-producing check existed to surface the feature | `dirilmek` sense · `bazı`→"other" · `bitiyor` sense · `kadîm` flattened · transliteration normalized · `hâsiyet`/`hâssa` split · `eşeklik` pun · `bozmak`→"spoil" · `İslâm ordusu`→"the Muslim army" · `istimdad`→"drew on" | **10** |
| **Position** | the right check existed, correctly scoped and aimed, and ran as prose inside the producing motion | `içyüzü` dropped · doubled verb invented · "never" added · `zarurî` flattened · `dirhem`×3 dropped · explicit subject dropped | **6** |
| **Scope** | no check was ever defined for this class | `Cenab-ı Hak` honorific policy | **1** |
| **Vantage** | detectable only from a context the method never occupies | the `istifham-ı inkârî` inversion | **1** |
| **Timing** | correct when written; broken by a later edit that nothing re-checked | the unresolvable pronoun | **1** |
| | | **total** | **19** |

**What repairs each kind**

- **Instrument** → a forced enumeration that surfaces the feature before or alongside the check. Not more instruction — an artifact.
- **Position** → move the check up the gradient: an emitted artifact, or its own call.
- **Scope** → *position-independent.* Define the check. No amount of enforcement reaches a check that was never specified.
- **Vantage** → *position-necessary-but-not-sufficient.* A separate call, **constructed without the source**.
- **Timing** → *position-independent as a rule; position-sensitive in detectability.* State the re-run rule; a call-based architecture makes its absence visible but does not supply it.

**Notes on the classification.** The pronoun error is the only one with two properties: it is **timing**-caused (proximate — the first draft had it right) and **vantage**-detectable (secondary — had it been present from the start, only the target-only vantage would have found it). It is counted once, under timing. Three of the instrument-kind entries — `bozmak`, `İslâm ordusu`, `istimdad` — are register renderings that check B11 would **classify** rather than catch; whether each is an unlicensed flattening or a domestication licensed by the config's A5 setting is currently undecidable, and that is itself a finding (see P13).

One classification result, stated without argument: **the vantage-kind and timing-kind errors are the two that the assistant never found and the user did.** The argument is P8's.

---

### P6 — What "missing" means

The word in the question was *missing*, and the most natural reading of it is falsified by the evidence.

**The knowledge was not missing.** For nearly every error in the instrument kind, the principle that identifies it is written in `case_catalog.md`, in correct and unambiguous form, and all 698 lines were read into context before the translation began:

| Error | The principle that covers it |
|---|---|
| the `istifham-ı inkârî` inversion | **#4** — arrangement carries meaning; "a question instead of a statement… the arrangement is a primary carrier, not packaging" |
| `dirhem` ×3 dropped | **#20 / #37 / #38** — repetition marks independence · sustaining repetition is not redundancy · repeated wording does different work in each spot |
| the `eşeklik` pun | **l.359** — "a word's buried root can be activated by context to carry a second meaning" |
| the polysemy errors | **#7** — preserve every valid meaning rather than forcing one |
| the whole method's premise | **#6** — comprehension first, then validation against the rules |

The pronoun error is covered too, by `harmony_layer.md`'s Tier 2 entry on pronoun chain continuity.

**Why none of it fired.** Every entry in that catalog has the same grammatical shape: *"The comprehension layer should detect / notice / ask / flag X."* It is a library of things worth noticing, indexed by nothing. To retrieve the entry about noticing X, you must already have noticed X. **The catalog can confirm a noticing. It cannot cause one.**

This is the same structure as an assertion-free test: it runs, it reports green, and it proves nothing — not because it is wrong, but because nothing in it can fail.

**So "missing" splits.** A **minority** of checks are genuinely absent from the corpus: nothing anywhere says "check that referring expressions resolve without the source" (B8), or "read the English cold and ask whether it asserts what the source asserts" (B9), or "re-run the checks a revision touched" (B10). A **majority** were present and inert.

**The corrected sense: what was missing was missing from the *run*, not from the corpus — and specifically, what was missing was the condition under which a written principle fires.** For this source, that condition is an enumeration keyed to *this text*: these are its polysemous words and their candidate senses, this word repeats three times, these two words share a root, this device is named in the source itself.

**One remedy class is excluded by this.** Writing the principles down more clearly, or more emphatically, or in a better-organised file, cannot fix a retrievability failure. The principles are already clear. They were already read. The problem is that nothing pointed at them at the moment they applied.

---

### P7 — Why the July fix failed, and what this finding does to it

**The evidence.** On 2026-07-12, `translation_method.md` was created — the four passes, the six hard constraints, the chunking bracket, and an honest note about enforcement. On the same day, `SKILL.md` Step 5 was rewritten. The git diff shows the change precisely: the old text read *"Then produce the translation. Apply:"* followed by a flat list. The new text reads *"produce the translation by running the four-pass method… in order. **Do not collapse the passes into one motion**; do not concrete the translation until Pass 3,"* followed by all four passes inlined with their rationale.

That is not a half-measure. The prior inquiry diagnosed the failure correctly, prescribed a fix, and the fix was shipped into the runtime file the model reads.

**On 2026-08-14 — one month later — the same class of error recurred.** Not a different failure: the same class. Dropped content, wrong word-senses, a lost repetition, a flattened intensifier, and a policy skipped, under a Pass 4 that ran and reported PASS.

**The mechanism.** The July fix repaired **ordering**. Ordering is one property, adjacent to position: it says *when* each pass runs relative to the others. It said nothing about vantage — no pass was moved to a context without the source. Nothing about scope — Pass 4's config exclusion was left in place, and is in fact restated in the new text. Nothing about instrument — all four Pass 4 checks remained prose. Nothing about timing — no rule was attached to post-draft edits.

**Four of five properties were untouched, and the errors those four produce came back on schedule.**

Stated generally: *a correct answer delivered against one property of a five-property object leaves four-fifths of the object unrepaired.* July's fix was not wrong. It was **under-dimensioned** — and it could not have known it was, because the dimensions had not been named.

**This is why this account cannot stop at naming another missing step.** A structural answer to this question has already been produced once. Its artifact is the thing that failed. An account that concludes "you are missing a source-blind pass" would produce a fifth correctly-worded instruction in a file that already contains four — the same intervention, at the same position, with the same expected result.

**Relationship to the prior chain: REFINES.**

Two alternatives were tested and both fail:

- **CORRECTS** — was the prior diagnosis wrong? It located the root cause in the 3-Pass method going un-run, which implies that running the passes as genuinely separate steps would help. The evidence supports that: the two re-scans were structurally separate calls, and they found seventeen of nineteen errors. The prior's core claim is **confirmed**, not refuted.
- **SUPERSEDES** — does this finding replace the prior? No. Its Gate 1 — lock meaning first, config-blind, at sentence granularity — is still correct and is not restated here.

**What survives from the prior chain, unchanged:** the enforcement gradient (prose-instruction < emitted-artifact < separate-call); the two-gate structure; the config-independent spine; the meaning-lock-first principle; the observation that word-sense correctness is config-independent.

**What is subsumed:** the enforcement gradient, which the prior chain treated as *the* axis of intervention strength, becomes **one of five**. Every claim it makes remains true. Its sufficiency does not.

**Inversion-candidate, generated and tested.** *Assumption reversed: that this finding refines rather than corrects.* Driven to system level, the inversion produces something neither label captures: the relationship is not really between two findings at all — **the inquiry corpus has no mechanism for testing whether a shipped fix took.** July's fix was written, shipped, and its failure was discovered a month later only because a new failure prompted a new inquiry. Nothing checked. That is the same shape as the finding itself, one layer up, and it is carried to P13 as a frontier item rather than resolved here.

---

### P8 — What actually enforced anything

This section is about the shape of an arrangement. It is not about anyone's performance, and it stays true if you substitute any participant for any other.

**The facts.** Of the nineteen errors, seventeen surfaced on re-scans. Each re-scan happened because you asked for one, and each ask created a fresh turn. A fresh turn is, structurally, a **separate call** — a new context, with a narrowed task, at the strong end of the same enforcement gradient the method's own honest note says is the only place its passes are physically enforced. The in-turn Pass 4, which ran inside the same motion that produced the draft, found **none of the nineteen**.

The remaining two you found by reading. They are the vantage-kind and timing-kind errors — the two whose detection requires reading the English without the Turkish in front of you. That is the one position no pass in the method occupies, and you were the only participant standing in it.

**The counterfactual is the whole argument.** Remove the two asks. The delivered artifact carries nineteen errors under a verdict of PASS. The method as specified caught zero after Pass 4.

**So the structural statement is this: a necessary position in the process was staffed by accident and never assigned.** Two things were being supplied that the method requires and cannot produce for itself — the separate call, manufactured by asking; and the source-blind vantage, occupied by reading. Neither is written down anywhere. Neither has an owner. The process does not know it depends on them.

**This is why the framing matters more than the finding.** An unnamed dependency cannot be maintained, cannot be automated, and cannot be handed to anyone else. Naming it is the precondition for either assigning it deliberately or building something that occupies it — and P10's R4 is the second option, costing one cheap call.

**The strongest counter, and its answer.** *Seventeen of nineteen were caught before the final read — perhaps the process worked.* This is a real reading and it deserves a straight response. It measures the **working pair's** performance, and by that measure the pair did well. It does not measure the **method's**, and the two are being conflated. The method's contribution to those seventeen catches was the instruction to look; the mechanism that made looking effective was a structural property of the turn, which the method neither specifies nor knows about. A process whose error-detection rate is a function of how many times someone asks is not a process with a detection rate — it has a **requesting rate**, and the number of errors found measures how hard anyone looked.

**What an assigned division of labour would have to specify:** who occupies the target-only vantage and when; whether the re-scan is a step or a request; what makes a draft ready to deliver as distinct from finished being written; and what happens when nobody asks.

---

### P9 — Which limits are real

Some of what this diagnosis rests on sounds like a claim about being an AI, and you explicitly set that aside as an answer. So each such claim is put through one test: **restate it with a human translator as the subject.** If it still holds, it is a property of the arrangement and belongs in a process diagnosis. If it collapses, it is a property of this agent and is out of bounds.

| The claim | Restated with a human translator | Verdict |
|---|---|---|
| A producer cannot reliably detect its own omissions by re-reading in the same context | A translator re-reading their own draft with the source open reliably misses their own omissions — which is why publishers employ copy-editors and why proofreading your own writing is proverbially unreliable | **holds — IN** |
| A producer cannot occupy the source-blind vantage while holding the source | A translator who has just rendered a passage cannot read the English as someone who has never seen the Turkish. They know what it means | **holds — IN** |
| A self-reported PASS is evidence that no check fired, not that nothing is wrong | "I checked it," with no checklist, reports that the checker found nothing — not that there was nothing to find | **holds — IN** |
| Fluency is self-evidencing and fidelity is not | A fluent English paragraph reads as correct to its author regardless of what the source said. Nothing about a well-formed sentence signals that a source word is missing from it | **holds — IN** |

All four survive. They are structural facts about who is checking what from where, and the same four are why the four-eyes principle exists in software review, why copy-editing is a separate role in publishing, and why aviation checklists are read aloud by one party and confirmed by another. None of that exists because the first party is careless.

**And one of them inverts in this process's favour.** The second claim is *strictly worse for a human*. A translator's memory of what they just rendered cannot be emptied — it goes home with them. A model's context can be emptied by constructing a new call: give it the English and nothing else, and the vantage is genuinely occupied, not simulated.

**Human translation workflows pay for that vantage with a second person. This process can have it for the cost of one small call — and is not using it.** That is not a limitation being excused. It is a capability being left on the table.

**The in-call impossibility, and why the instruction version does not work.** Within a call that contains the source, "read this as a fresh reader who has never seen the original" cannot be executed. Not through unwillingness — through the shape of the question. The check asks *is this referring expression resolvable?*, and that question has already been answered by the context before the check begins. The reader does not consult the source to resolve "it"; the referent is simply not experienced as missing. There is no operation that removes information from a context.

**The direct evidence.** The same text was re-scanned twice, under explicit instruction to hunt for errors, with full attention. Those two passes found seventeen source-comparison errors — and **zero** of the two that require the source's absence. Not one, on either pass. If the vantage were adoptable by instruction, at least one of those two passes should have caught at least one of them.

---

### P10 — What repairs what, and what is available now

Six remedies. They are not competing for one slot — they repair **different properties**, and their overlap is small.

| # | Remedy | Repairs | Catches | Position | Available |
|---|---|---|---|---|---|
| **R1** | **Per-document term-lock** | instrument (and the missing index) | the 10 instrument-kind errors | emitted-artifact | **NOW** |
| **R2** | **Policy-conformance enumeration** | scope | the 1 scope-kind error; reclassifies 3 more | emitted-artifact | **NOW** |
| **R3** | **Post-revision re-run rule** | timing | the regression class | rule attached to artifact invalidation | **NOW — free** |
| **R4** | **Source-blind reader** | vantage | the errors nobody else can catch | separate call, controlled input | **NOW — cheapest call in the method** |
| **R5** | **Fresh-context adversarial reader** | vantage + position, generally | broad | separate call | needs orchestration, not a bespoke engine |
| **R6** | **The engine** — passes as separate calls with real intermediate artifacts | position | the 6 position-kind errors | separate call | **ENGINE-GATED** |

**Five of six require nothing to be built.**

**R1 — the term-lock, and why it is first.** Before drafting, produce one artifact from the source: every polysemous term with its candidate senses and the sense the local construction picks · every word that repeats, with its count · every cognate cluster · every rhetorical device the source names in its own vocabulary · every honorific · every source-form (transliteration, diacritics) to be carried unchanged.

The important thing about R1 is that it **is not a check.** It runs *before* drafting, which makes it a **pre-commitment rather than a verification**. You cannot fail to notice a polysemous word you enumerated before you started writing. It converts the majority of these errors from things that must be *caught* into things that are *harder to commit* — and that is why it sits first despite the vantage gap being the more dramatic finding. It is also the exact answer to P6: it is the index the catalog does not have, built per-source rather than per-principle.

**R2 — an enumeration, not a verdict.** Seven rows: policy · its value · where it applies in this source · how the draft rendered it. It must force naming, not ask for a judgment. A checklist that asks "are the policies satisfied?" becomes seven more things to nod at; a checklist that requires you to write down the honorific and its rendering cannot be nodded at. Aviation checklists are read, not recalled, for exactly this reason.

**R3 — a rule, and it costs nothing.** Any edit made after verification re-runs the checks whose span it touched. This is not work; it is a statement about when a result expires.

**R4 — the vantage remedy, and its construction.** One call. Contents: the English draft, and nothing else. Task: list every referring expression and state what it refers to using only this text; state what each sentence asserts; flag anything that cannot be resolved.

**Its output is a question list. It has no authority to edit.** This is not a stylistic preference — it is what answers the obvious objection. A reader who cannot see the source and is asked to *fix* unclear English will resolve ambiguity by guessing, which manufactures exactly the invention-class error this whole diagnosis is about. A reader that cannot write cannot invent. Every fix is then made in a source-present context, which is the vantage that demonstrably works.

**The cost inversion.** The remedy addressing the errors that nothing else can catch is the **cheapest call in the entire method** — it holds one text and one instruction, less context than any existing pass. The intuition that the hardest-to-catch errors need the heaviest machinery is exactly backwards here.

**A constraint test the remedy set has to pass.** Add the constraint: *no new prose may be added to any runtime file.* R1 survives (it is an artifact). R2 survives (an enumeration). R3 survives (an invalidation rule attached to an artifact). R4 survives (a call construction). R6 survives (an architecture). **The set satisfies the constraint** — which is the check that it is not secretly the intervention that already failed. And the honest note that any of this is a nudge rather than a guarantee belongs in authoring notes, never in the runtime text the model executes: a caveat telling the model its own structure is optional licenses it to relax.

**Shape-inversion, generated and tested.** *Assumption reversed: that the intervention shape is ADD.* The alternative shape is **REMOVE** — delete the method's unenforceable claims rather than adding enforcement to them, shrinking it to the handful of checks it can actually instrument and stating plainly what it does not catch. This is not absurd: 3,489 lines of instruction reloaded per run is a real cost, and a method that claims less and delivers all of it may beat one that claims everything and delivers a quarter. It is **not adopted now**, because five of six remedies are cheap and the leading one is preventive rather than additive. It is **carried as DEFERRED with an explicit revival trigger: if the validation experiment shows no measurable reduction from R1–R4, REMOVE becomes the honest move.**

---

### P11 — Next actions

**MUST**

1. **Ship R1 (term-lock) as a required pre-draft artifact.** *(repairs instrument · 10 errors · available now)* Specify what it enumerates; require it to exist before Pass 3 concretes anything.
2. **Ship R3 (post-revision re-run).** *(repairs timing · free)* One rule: any edit after verification re-runs the checks its span touched.
3. **Ship R4 (source-blind reader) as a named step with its construction fixed.** *(repairs vantage · available now)* Separate call · target text only · question-list output · no edit authority.
4. **Run the validation experiment.** Translate one comparable section of the same work twice — once with R1–R4 in force, once without — and count errors by gap-kind. The corpus and the untranslated remainder both exist; nothing blocks this. It is a MUST because every magnitude claim in this finding is currently unmeasured, and because its result is the revival trigger for the REMOVE alternative.

**SHOULD**

5. **Ship R2 (policy-conformance enumeration).** *(repairs scope · available now)* Seven rows, naming required. Also fixes the related oddity that seven policy defaults are in force on every run and are never shown to the user.
6. **Declare checks as tuples rather than sentences.** Whatever changes, changing it as `(what, vantage, instrument, position, invalidated-by)` makes an unspecified property visible. A sentence with no vantage looks complete; a tuple with an empty slot does not.

**COULD**

7. **R5 — a fresh-context adversarial reader** for broader coverage. Orchestration, not a build.
8. **Write the division of labour down**, per P8 — who occupies which vantage, and what happens when nobody asks.

**DEFERRED**

9. **R6 — the engine.** *Gate: build capacity.* With a warning that follows directly from P7: **if R6 is built first and R1–R4 are deferred, it will repair position and leave the other four properties untouched — the same shape as July's fix, one level up.** *(Extrapolation, flagged as prediction rather than evidence.)*
10. **REMOVE — shrink the method to what it can enforce.** *Gate: the validation experiment showing no measurable reduction from R1–R4.*

**Changes to the SKILL vs changes to the working pattern.** Items 1, 2, 3, 5, 6 are SKILL changes. Item 8 is a working-pattern change. Item 4 is neither — it is the measurement both depend on.

---

### P12 — How much weight this carries

**The structural claim is HIGH confidence, and the criterion is pointability.** That the five properties are distinct and vary independently does not rest on how many errors there were. It rests on five specific pairs in the evidence, each of which a disagreeing reader can check against a file or a session record: open `translation_method.md` and read that Pass 4 excludes config checks; open the git log and read what Step 5 said before and after; look at which check had a script and which did not. **HIGH is warranted where a reader who disagrees can point at something.** That is a claim about transferability, not about truth — but it is the difference between this claim and the ones below.

**Every magnitude claim is MED and quarantined.** How much R1 reduces errors, whether R4 catches most vantage-kind errors, whether the remedy set is complete — none of this is measured. It is why the validation experiment is a MUST rather than a suggestion.

**The n's are different, and conflating them would overstate the case.** For the **pattern** — a check specified in prose, with no instrument, executed by the producing context, reporting green — n = 3. The translation method in July→August; the prior İKİNCİ HÜCCET translation; and a third instance found while this inquiry was running: **`tools/structural_check.sh` is referenced by the `/traverse` spec, does not exist in this repository, and has been substituted with manual prose judgment at every discipline handoff in this very investigation, logged as "N/N passed, manual."** Same shape, different pipeline, discovered by accident rather than by looking. For the **translation-specific magnitude**, n = 2. The third instance raises confidence in the structure and none in the numbers.

**The sample is biased, and the direction matters.** The nineteen errors are the ones scrutiny found. Any error visible only from a vantage nobody occupied could enter the sample only if you happened to notice it — so the observed vantage count (one purely, two including the regression's secondary property) is a **lower bound**, and the true count is at least that and plausibly higher. The bias therefore **understates the vantage gap while making the proportions unusable**. The counts in P5 should be read as a partition of what was found, not as a measurement of what exists.

**And error counts track scrutiny, not quality.** Seven errors were found in the prior translation under less scrutiny; nineteen here under more. Neither number is about the translations, and no argument in this document rests on the comparison.

**One reading this document does not refute.** Under a research-artifact lens — a method under development, not a production system — nineteen errors in a first-pass literary translation from Ottoman-inflected Turkish is unremarkable, and this diagnosis is over-engineering. That reading is coherent. What it does not explain is why the mechanised check held perfectly and the prose checks caught nothing, or why the two errors that survived are exactly the two requiring a vantage nobody occupied. Those patterns need accounting for under any lens.

**This inquiry, scored against its own finding.**

- **Position: strong.** The disciplines ran as genuinely separate calls, each loading its own spec, each emitting an artifact the next reads. That is R6's architecture, already built — for inquiry.
- **Vantage: weak, and identically weak to what it diagnoses.** Every discipline here ran in one context. No step occupied a position blind to the previous steps' output. Critique is adversarial *by instruction*, which is precisely the construction P9 rules inadequate for the source-blind check.
- **Instrument: worst.** The one specified mechanical check does not exist, and prose self-assessment was substituted for it throughout — the failure this document is about, occurring inside this document.

**What follows.** The artifact-checkable claims — the matrix cells, the five pairs, the git sequence, the substitution-test results — are well-supported and re-derivable by anyone. The judgment claims — that the five properties are exhaustive, that R1 is the highest-value remedy, that this partition is the best organizing structure — carry exactly the weakness the translation method carried, and should be read as this context's best account rather than as verified. **The correction this finding cannot apply to itself is the one it prescribes: a reader occupying a vantage this loop does not have.**

---

### P13 — What remains open

**Resolvable downstream**

1. **The exact shape of the term-lock artifact** — what it enumerates, in what form, and where it lives. Resolvable in P11's MUST 1.
2. **Whether R2's enumeration belongs inside Pass 4 or as a new pass.** Pass 4 currently defines itself as config-independent; either that definition changes or the check goes elsewhere. A design question, not a diagnostic one.
3. **How much of the division of labour belongs in the SKILL versus in authoring notes.** Constrained by the project's own rule that caveats about softness belong where the human reads them, never in runtime text.

**Genuine frontier**

4. **Whether the five properties are exhaustive.** Unprovable from nineteen errors. They are five *observed* properties, each demonstrated varying independently — not five *necessary and sufficient* ones. A sixth may exist.
5. **Config-licensed drift.** Nothing currently distinguishes a domestication licensed by the config's A5 setting from an unlicensed flattening. Three of the nineteen (`bozmak`, `İslâm ordusu`, `istimdad`) sit in that undecidable region, which means **part of the error count is not resolvable in principle** until check B11 exists. This is not a caveat about the count — it is a missing check that the count's ambiguity revealed.
6. **Whether an adversarial reader can be constructed adversarially rather than instructed to be adversarial.** P9 establishes that the source-blind vantage requires an absence rather than an instruction. The same question applies to adversarial review generally — including to this inquiry's own Critique step.
7. **The corpus has no mechanism for testing whether a shipped fix took.** July's fix was written, shipped, and its failure discovered a month later only because a new failure prompted a new inquiry. Nothing checked in between. This is the same shape as the finding itself, one layer up, and it is out of scope here.
8. **Whether the method claims more than any single call can enforce.** 3,489 lines of instruction reloaded per run, against a two-lever tension in which separate-call architecture re-pays that load on every call. The REMOVE alternative in P10 is the live form of this question, and the validation experiment is what would settle it.

---

## Telemetry

- **Generators applied: 4 / 4** — Absence Recognition (both levels, bidirectional) · Combination · Domain Transfer (2 native + 2 different-field + contrarian) · Extrapolation
- **Framers applied: 3 / 3** — Lens Shifting · Constraint Manipulation (both directions) · Inversion (piece-level ×4, with depth-check to system level and existence-axis)
- **Convergence: YES** — five mechanisms converge on the core innovation (a check is a multi-property object and the method cannot declare its properties): M1-redesign, M2-focused, M7-P2-L2, M4-contrarian, M3-native-testing. Shared-input check: these do **not** all derive from the upstream five-property commitment — M3's assertion-free-test transfer and M1's already-present-in-different-form observation reach it from independent grounds (software-testing convention; the `/traverse` architecture). Convergence judged **independent, not spurious**.
- **Survivors tested: 9 / 9** — 6 ACTIONABLE, 2 DEFERRED with revival triggers, 1 RESEARCH FRONTIER
- **RE-TEST TRIGGER fired once** — the per-error assignment contradicted a Sensemaking headline count; re-tested and corrected to 10/6/1/1/1, with the double-count named. Argument direction unchanged.
- **Artifact-grounding (6th test) applied** — fired (committed cell values about project state); one contradiction found and routed through the re-test trigger.
- **Axis coverage** — the candidate set varies along four axes: content (the five properties) · intervention-shape (ADD vs REMOVE) · timing (detection vs prevention) · scope (this SKILL vs the corpus). No axis without a variant.
- **Per-row mechanism trace** — all 15 matrix rows and all 5 gap-kinds have at least one mechanism output constructing or referencing their cell values.
- **Failure modes observed: none.** Premature evaluation — avoided (generation completed before testing). Single-mechanism trap — avoided (7/7). Early frame lock — avoided (the P2 inversion ran to three levels after the principal candidate was already viable). Innovation without grounding — avoided (9/9 tested, plus artifact-grounding). Mechanism exhaustion — not applicable. Survival bias — the prior-step never-generate variant was specifically guarded: the uncomfortable directions (REMOVE the method's claims; the research-artifact lens; CORRECTS instead of REFINES; don't-split-the-confidence) were all **generated**, not merely tested.

### Production-task telemetry

**Per-piece mechanism log**

```
P1:  [M5:content, M2:content]                          content-production
P2:  [M2:content, M1:content, M7:content, M7:existence] meta-decision (framing-semantic)
P3:  [M1:content, M2:content]                          content-production
P4:  [M2:content, M3:content]                          content-production
P5:  [M2:content]                                      meta-decision (lesson-vocabulary)
P6:  [M1:content, M3:content]                          content-production
P7:  [M4:content, M7:relationship-label, M7:system]    meta-decision (relationship-label)
P8:  [M5:content, M6:content, M3:content]              content-production
P9:  [M2:content, M3:content]                          content-production
P10: [M6:content, M3:content, M7:intervention-shape]   meta-decision (intervention-shape, property v)
P11: [M4:content]                                      content-production
P12: [M1:content, M4:content, M5:content, M7:criterion] meta-decision (evaluation-criterion)
P13: [M1:content, M7:system]                           content-production
```

**Piece-level Inversion compliance**

| Piece | Property | Compliance |
|---|---|---|
| P2 | framing-semantic | **satisfied** — inversion generated, depth-checked to system level and existence axis, tested; refined the principal candidate rather than replacing it |
| P5 | lesson-vocabulary | **satisfied** — the count/exhaustiveness challenge was generated at M7-P2 L1 and carried into P13 item 4 |
| P7 | relationship-label | **satisfied** — CORRECTS and SUPERSEDES both generated and tested; both failed on evidence; the depth-check produced a surviving system-level candidate |
| P10 | **intervention-shape (property v)** | **satisfied on the correct axis** — the Inversion-candidate names ADD as the reversed assumption, names REMOVE as the alternative shape from the Vocabulary, states what follows, and both were tested; REMOVE dispositioned DEFERRED with a named revival trigger |
| P12 | evaluation-criterion | **satisfied** — don't-split and zero-discussion both generated; the split survived and its criterion was sharpened |

**Overall: PROCEED.** Full mechanism coverage (7/7); independent convergence on the core innovation; all survivors tested; all five meta-decision pieces satisfied at piece level, with P10's on the required intervention-shape axis; one re-test trigger fired and resolved with the correction stated openly rather than absorbed.
