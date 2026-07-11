# Critique — Adjudicating the Diagnosis (A/B/C) and the Reach Designs (D/E)

## User Input

`_branch.md` (root-cause diagnostic, Critique step). Territory = this inquiry's own artifacts (sensemaking.md stabilized model; decomposition.md pieces A–F; innovation.md candidates C1–C8 + assembled design; surfacing.md 10 clauses; articulate_warm.md severity spectrum). **Two jobs:** (1) adjudicate the reach designs D/E; (2) stress-test the diagnosis claims A/B/C — find where the diagnosis is too clean, over-fitted to 7 examples, or lets the AI off the hook. Save to `critique.md`.

**Self-reference hazard acknowledged (Failure Mode #7 + #9):** I am critiquing my own diagnosis of my own errors. To avoid self-validation, every verdict below is anchored to **external evidence** — the literal source Turkish (`content0020.xhtml`), the literal config text, the draft text, and the user's independent critique — not to internal structural agreement.

---

## Phase 0 — Dimension Construction

The territory holds **two candidate-classes**: diagnostic *claims* (A/B/C — assertions about what happened) and proposed *solutions* (D/E — enforcement designs). Dimensions must span both.

### Dimensions + weights (by purpose-fitness)

| # | Dimension | What it asks | Weight | Applies to |
|---|---|---|---|---|
| **D1** | **Evidential grounding** *(external-anchor)* | Is each claim tied to a verifiable source↔draft↔config diff, not assertion? | **CRITICAL** | A, B, C |
| **D2** | **Taxonomic load-bearing** *(substance-vs-label)* | Does generation-shaped/verification-shaped actually *predict which errors happened*, or just relabel them? | **CRITICAL** | B |
| **D3** | **Non-self-exculpation** *(frame-premise + self-reference)* | Does the diagnosis let the AI off the hook by routing blame to the tool? | **CRITICAL** | C (and B's framing) |
| **D4** | **Fit-not-overfit** *(robustness)* | Is the model over-fitted to the 7, or does it generalize / predict unseen instances? | HIGH | A, B |
| **D5** | **Correctness-of-catch** | Would the reach design actually catch the error-class before emit (esp. the rubber-stamp objection)? | **CRITICAL** | D/E |
| **D6** | **SKILL-coherence** *(project-specific risk: explicit-culture-fit / phase-fit)* | Does it fit the SKILL's architecture without breaking the generation-shaped work that currently succeeds? | **CRITICAL** | D/E |
| **D7** | **Parsimony** *(operation-parsimony / elegance)* | Scoped and token-feasible, or over-engineered / over-claimed? | HIGH | D/E |

**Project-specific risk dimension check:** candidate set involves project artifacts (SKILL files, config, workflow) → D6 (explicit-culture-fit / phase-fit) and D7 (operation-parsimony) included. ✓

**Frame-premise test (candidate-space rests on inherited sensemaking commitments) — 3 load-bearing premises named + prosecuted independently of the candidates:**

- **P1 — "the generation-shaped / verification-shaped split is real and load-bearing."** *What-if-wrong:* if several of the 7 are actually *generation*-shaped (bad word chosen at generation, no draft-check would have differed), the taxonomy is a relabel and the verification-pass fix misses them. → tested at D2.
- **P2 — "the SKILL contains the antidote to 6–7 of 7."** *What-if-wrong:* if for some error the SKILL has no specific governing clause (only a generic principle), that error is a *knowledge/judgment* gap, not a *verification* gap, and the diagnosis mis-locates the cause. → tested at D1/D4 (err-3, err-7).
- **P3 — "the fix is a scoped verification pass, not 'attend harder' or LLM-incapacity."** *What-if-wrong:* already adversarially eliminated in sensemaking Ambiguities 2 & 4 (scoped pass defeats saturation; within-reach fixes disprove incapacity). Re-verified as externally grounded — NOT re-opened, but P3's residue (does the *same fluent model* running the check rubber-stamp?) is prosecuted at D5.

---

## Phase 1 — Fitness Landscape

- **Viable region:** claims grounded in a literal source↔draft diff (D1) that *also* survive the "could this be generation-shaped / could the SKILL lack the clause / am I exculpating myself" prosecutions (D2/D3/D4); designs that catch the error-class (D5) without damaging supra-sentential harmony (D6) at feasible cost (D7).
- **Dead region:** any claim asserted without a source/config anchor; any design whose reliability depends on the *same* fluency-biased judgment that produced the error, applied in the *same* frame (naive self-review).
- **Boundary region:** claims that are *directionally* right but *too clean* (the taxonomy) or *too generous to the author* (err-2b "defensible"); the "config self-enforcing" claim (right mechanism, over-strong label).
- **Unexplored (flagged for coverage):** errors beyond the user's 7 — the diagnosis is built on 7 user-selected instances; the two produced chunks contain more untested instances (sensemaking Ambiguity 3 conceded this). No candidate tests the *unsurfaced* error population.

---

## Phase 2–3 — Adversarial Evaluation + Verdicts

### CAND-A — Per-error adherence mapping (7 errors → clause → severity)

**Prosecution.** Two of the seven mappings are weaker than the artifact's confident tone implies:
- **err-3 "figure" for "bir şahıs".** Source: *"…tevehhüm ettikleri şeriklerin namına **bir şahıs** farzediyoruz."* The governing clause offered (surfacing #13, `dimensional-compression/iltizamiye`) was rated **sub / MED-confidence** — it is a *generic* principle ("word choice activates attribute-sets"), not a *specific* exclusion of "figure." "figure" is a mildly flat choice; "personage/entity/character" are *judgment* alternatives, not clause-mandated ones. Calling this a verification-shaped SKILL-violation over-reads a generic principle as a specific antidote.
- **err-2b hal/kal "defensible-in-meaning".** Source: *"…**lisan-ı hali, lisan-ı kal suretinde** söylemiştim."* The draft: *"giving the mute tongue of a thing's own condition the form of actual speech."* The warm severity-spectrum filed the *meaning* as "approximately correct." **This is too generous to the author (me).** The user's verdict is external and explicit: *"your translation doesn't cover this and makes things gibberish."* For a diagnosis about **output**, "my internal meaning was roughly right" is a weak defense when the reader demonstrably does not receive the hal (state-testimony) vs kal (voiced-speech) distinction. The delivery failed even if the gloss was close.

**Defense.** The *mechanical* mappings are externally airtight: err-2a — *"**basit avamın fehmine gelecek**"* is literally present in `content0020.xhtml` and literally absent from the draft (a diff, not an opinion); err-1 "allegorical" sits on the wrong side of A1's literal `vocabulary_breadth` exclusion of dense-academic tokens; err-4/err-5 violate A1's literal `syntactic_processing: multi-clause LINEAR`. Five of seven are strongly grounded.

**Collision → Verdict: SURVIVE with REFINE.** The mapping stands for 5/7. Two require correction: **err-3 → downgrade from "SKILL-violation" to "generation-quality judgment call, weak/generic clause"** (moves it beside err-7 on the severity spectrum); **err-2b → upgrade the delivery axis to clear-violation** ("the reader does not receive hal/kal") while keeping the note that the internal gloss was near. *Constructive:* the severity spectrum is not 5-clear + 2-defensible; it is **4 clear-violation (err-1, 2a, 4, 5) + 1 clear-on-delivery (err-2b) + 2 defensible-but-off-register (err-6 borderline, err-7)** — with err-3 reclassified as weak-mapping generation-quality.

### CAND-B — The generation-shaped / verification-shaped taxonomy + systemic cause

**Prosecution (the load-bearing attack, D2).** The dichotomy is **too clean.** Test it literally against err-1 and err-6:
- err-1 "allegorical": is a register-exclusion *verification*-shaped ("check the draft for hard words") or *generation*-shaped ("choose easy words as you write")? **Both.** A properly A1-conditioned generation would never emit "allegorical" in the first place. The claim that this principle is *inherently* verification-shaped is a post-hoc convenience.
- err-6 "work" for "iş": polysemy-via-local-construction. Source: *"**sen benden iş bulamazsın**."* If the principle had fired *during* generation, the AI picks "foothold/purchase," not "work." It is equally a generation-time principle that simply didn't fire.

So P1 is partly wrong: several principles are **dual-shaped** (fireable at generation *or* verification), not verification-shaped by nature. If the taxonomy is read as "these principles are verification-only," it mislabels their nature.

**Defense.** The *empirical* fact rescues the practical conclusion: the AI **had A1=conversational and policy-3 in context and still emitted "allegorical" and "work"** in a single fluent pass. Whatever their nature, these principles **demonstrably did not fire at generation under fluency pressure.** A pass that has no post-draft checkpoint therefore has *no second chance* to catch them. The fix (a verification point) is correct regardless of the nature-label.

**Collision → Verdict: REFINE (mechanism-claim softened; practical conclusion intact).** Recast B from *"the principles are verification-shaped"* to: **"the principles are dual-shaped, but in a single fluency-first pass they went un-fired at generation and had no verification backstop; the reliable place to catch them is therefore a verification checkpoint."** This is a real correction — it stops the diagnosis from claiming a cleaner mechanism than exists — but it does **not** overturn the fix. err-2a remains the one *purely* verification-shaped case (you cannot notice-at-generation a clause you dropped), which is why the mechanical omission-diff is the strongest single check. *External-anchor validated (D1): the un-firing is proven by config-in-context + draft output, not asserted.*

### CAND-C — The graded adherence verdict ("READ:yes / gen:yes / verification:no / SKILL-deficient:partially")

**Prosecution (D3 — the self-exculpation attack, and the heart of the user's "what happened").** The verdict's *framing* risks letting the AI off the hook. "SKILL-deficient: partially" + "the workflow has no enforcement gate" can read as **systems-level deflection**: a competent translator with every principle in context *should* produce better output in one pass; routing the account toward "the tool lacks a gate" subordinates the plainer fact — **the AI under-applied knowledge it demonstrably held.** An unsympathetic external reader (the user) asked "what happened??" and deserves the un-hedged version first.

**Defense.** The verdict is *not* actually exculpatory in content: **"verification-shaped-applied: NO" IS the application-failure admission** — it says the AI failed to apply principles it had. And the tool-deficiency finding is externally real, not invented: by the SKILL's own literal Rules (Rule 1 "read all references" ✓, Rule 5 "Tier 1-2 non-negotiable" ✓) the SKILL *was* followed, yet those Rules never mandate the verification checks — a genuine gap between what the config *promises* (accessible/faithful output) and what the workflow *structurally enforces* (nothing).

**Collision → Verdict: REFINE (re-order the emphasis, keep the grading).** Both are true and co-equal; the current artifact *subordinates* the application-failure to the systemic framing. **Foreground them as co-equal:** *"What happened = BOTH (a) I did not apply verification-shaped principles I had in context — an application failure — AND (b) the SKILL provides no gate that would have forced that application — a tool deficiency. (a) is not excused by (b)."* Do not let "the SKILL has no gate" become a hiding place for "I had the principles and didn't deploy them." This directly answers the user's question in the register they asked it.

### CAND-D/E — The assembled ACTIONABLE enforcement design

*("config-keyed scoped verification gate, pre-committed, embedded in the 3-Pass, adversarially run, granularity-bounded")*

**Prosecution.**
- **D5 (rubber-stamp, the killer objection):** the *same* fluency-biased model runs the checklist on its *own* draft. For **judgment** checks (register, naturalness) this is the exact cognition that failed — a model that found "allegorical" acceptable at generation may rate it acceptable at review. The "adversarial stance" mitigates but does not eliminate this; naive self-review lands in the **dead region**.
- **D7 (over-claim):** "config **self-enforcing**" overreaches. Deriving a *reliable* check from "A1 excludes dense-academic vocab" requires the model to know which tokens are dense-academic — **the same judgment that failed.** The label promises mechanical enforcement the mechanism doesn't deliver for judgment axes.

**Defense.**
- The **mechanical** checks are genuinely reliable and independent of fluency-bias: the **source↔draft omission-diff** is near-zero-judgment and catches the *clearest, most consequential* violation (err-2a) — it would have caught the dropped clause with certainty. This check alone justifies the design.
- **Scoping + reframing** measurably shifts the judgment checks: "list every word a tired A1 lay reader trips on" (the simulated-reader frame, C6) is a *different cognitive act* than "review your translation," and empirically more likely to surface "allegorical." Not perfect, but strictly better than the single fluent pass that has no checkpoint at all.
- **D6 (SKILL-coherence):** embedding in the existing 3-Pass + the granularity bound (word/clause level, never sentence-chop) means it does **not** damage the supra-sentential harmony work that currently succeeds. Good phase-fit.

**Collision → Verdict: SURVIVE with REFINE (two corrections).**
1. **Drop "self-enforcing"; adopt "config-derived check-agenda with tiered reliability."** Be honest that reliability is **tiered**: *mechanical* (omission-diff, source-presence) = high, fluency-independent; *adversarial-judgment* (register/naturalness via simulated-reader) = medium, partly defeats rubber-stamping; *naive self-review* = low, excluded by design.
2. **Lead with the mechanical checks.** The omission-diff is the highest-value, most-reliable, cheapest check and catches the single worst error — it should be the design's spine, with judgment checks as the fallible-but-worthwhile second tier. This also right-sizes the "config self-enforcing" ambition to what the mechanism actually delivers.

*Caveat carried (D-unexplored):* the design is validated against the 7; it is *not* validated against the unsurfaced error population in the two produced chunks. SURVIVE is on the mechanism, not on "solves all translation error."

### CAND-C4 — Deferred-emit / provisional-draft (structural end)
**SURVIVE (structural-end option).** Prosecution: heavier than the checklist for the same checks. Defense: buys a *hard gate* (cannot emit without the check-artifact) — the correct high-assurance variant. Correctly positioned as the "how-strong" knob, not the default. No change.

### CAND-C5 (passage-level incremental) / CAND-C7 (fluency-weighting)
**Agree with innovation's DEFERRED disposition.** C5's pure form correctly killed (would trade supra-sentential harmony for verification — externally grounded in the fact that the harmony work is what *succeeded*); the passage-level hybrid is the right revival target. C7 is a thin single-mechanism heuristic; DEFERRED is right. No change.

---

## Phase 3.5 — Assembly Check

The REFINE directions on A, B, C, D/E assemble into **one coherent sharpening** of the diagnosis, emergent beyond any single correction:

> **The honest through-line:** *In a single fluency-first pass, dual-shaped principles the AI held in context went un-fired at generation (application failure) and had no verification backstop (tool deficiency) — co-equally. The fix is a scoped verification point whose spine is the mechanical source↔draft omission-diff (fluency-independent, catches the worst error with certainty), with adversarially-reframed judgment checks as a fallible second tier. Severity across the 7 is graded, and two of the seven (err-3, err-7) are generation-quality/register judgment calls the SKILL never specifically governed — the diagnosis must not inflate them into clause-violations to make the pattern look cleaner than it is.*

This assembly SURVIVES its own prosecution: it is *less* clean than the pre-critique model (concedes dual-shaped principles, weak mappings, co-equal blame) and therefore *more* externally faithful. Cleanliness was the thing to be suspicious of; removing it is the value.

---

## Phase 4 — Coverage + Convergence

**Coverage map:** D1 (grounding) ✓ across all claims via literal source/config/draft anchors · D2 (taxonomy) ✓ — surfaced the dual-shaped correction · D3 (self-exculpation) ✓ — surfaced the co-equal-blame correction · D4 (overfit) ✓ — flagged err-3 weak-mapping + the unsurfaced-error caveat · D5/D6/D7 ✓ on the designs. **Unexplored region flagged, not closed:** the error population beyond the user's 7 (no artifact tests it — correctly out of this inquiry's scope, named for honesty).

**Convergence:** the diagnosis core (fluency-first single pass, no enforcement point, graded adherence, scoped fix) **survived** every prosecution — no KILL, because prosecution won on *cleanliness/emphasis/two-weak-mappings*, not on the core mechanism, and each win produced a REFINE the core can absorb. Landscape STABLE (the refinements sharpen, they do not relocate any candidate to the dead region). A clean SURVIVE exists (the mechanical omission-diff spine; the co-equal-blame verdict).

**Signal: TERMINATE with ranked survivors.**
1. **CAND-B/C refined** — the honest through-line (co-equal application-failure + tool-deficiency; dual-shaped principles un-fired) — *the answer to "what happened."*
2. **CAND-A refined** — per-error mapping with corrected severity (4 clear + 1 clear-on-delivery + 2 defensible + err-3 reclassified).
3. **CAND-D/E refined** — config-derived check-agenda, mechanical-spine-first, tiered reliability, granularity-bounded, embedded in the 3-Pass; C4 as the hard-gate variant.
4. DEFERRED: C5 passage-hybrid, C7 fluency-weighting (triggers as in innovation.md).

No ITERATE: the refinements are terminal corrections deliverable by CONCLUDE, not new seeds requiring another innovation pass.

---

## Convergence Telemetry

- **Dimension coverage:** 7 dimensions; D1–D3 + D5–D6 critical, all applied; project-specific risk axes (D6 phase-fit, D7 operation-parsimony) present; frame-premise prosecution run on P1/P2/P3.
- **Adversarial strength: STRONG.** Prosecution won real ground on every diagnostic claim (taxonomy too clean; err-2b too generous; err-3 weak mapping; self-exculpation framing; "self-enforcing" overreach; rubber-stamp on judgment checks) — not a rubber-stamp. Each win is a REFINE with a constructive target, not a nitpick KILL.
- **Landscape stability: STABLE** (refinements sharpen positions; none relocated to dead region).
- **Clean SURVIVE exists:** YES (mechanical omission-diff spine; co-equal-blame verdict).
- **External-grounding / mechanism-independence:** **VALIDATED, not quarantined.** Evidence cites canonical source text verbatim (`basit avamın fehmine gelecek`, `lisan-ı hali lisan-ı kal suretinde`, `sen benden iş bulamazsın`, `bir şahıs`), the literal config (A1 vocabulary/syntax exclusions), the draft diff, and the user's independent critique — the 3 external-anchor sub-types are present.
- **Self-Reference Collapse (#7) check:** actively defended — the critique's sharpest findings (co-equal blame; err-2b too-generous) *increase* the author's culpability rather than validating the author's framing, which is the signature of non-circular self-critique.
- **Failure modes observed:** none. (Not rubber-stamping — 4 REFINEs with won ground; not nitpicking — no KILL on minor issues, severity-weighted; not self-reference collapse — externally anchored + self-implicating; not external-grounding absence — source/config/draft/user all cited.)
- **Overall: PROCEED** — strong adversarial pass, stable landscape, clean survivor, external grounding validated; hands CONCLUDE a diagnosis that is *less clean and more honest* than it entered.
