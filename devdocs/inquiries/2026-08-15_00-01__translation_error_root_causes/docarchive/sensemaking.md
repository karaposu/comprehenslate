# sensemaking — translation error root causes

## User Input

```
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-08-15_00-01__translation_error_root_causes/_branch.md

Upstream outputs in the same folder, read them in full: articulate_simple.md (cold, HIGH-PROCEED) + surfacing.md (185 items, 16 regions, FLAG) + articulate_warm.md (MED-FLAG, content-conflict ×2 non-severe, FIXPOINT at round 0).

LAYER COMMITMENT: PROCESS. Stabilize a model of what STEPS the translation process lacked. Not what verification *means* (Meaning), not how the SKILL's files should be organized (Structural — surfacing confirmed that region ABSENT: the files' content is already correct).

WHAT WARM COMMITTED (given; do not re-derive) — 11 verified facts, the load-bearing ones:
 F2. The prior inquiry's fix WAS SHIPPED (git diff: SKILL.md Step 5 rewritten from a flat bag into the four ordered passes + "Do not collapse the passes into one motion").
 F3. Recurrence gap = ONE MONTH (translation_method.md created 2026-07-12; failing translation 2026-08-14).
 F4. case_catalog.md contains, in correct form, the principle matching nearly every error (#4 arrangement-carries-meaning incl. "a question instead of a statement"; #20/#37/#38 repetition; l.359 buried-root; #7 preserve-every-valid-meaning; #6 comprehend-then-validate). All 698 lines read into the context. None fired.
 F5. Pass 4 EXCLUDES reader-keyed/config checks BY DESIGN — the HonorificsPolicy violation had no possible catcher anywhere in the method.
 F6. Detection-vantage partition: ~15 source-comparison / 1 config-comparison / 2 target-only / 1 process-timing. The 2 target-only errors are EXACTLY the 2 the assistant never found and the user did.
 F7. Exactly 1 of Pass 4's 4 checks was mechanised (a sentence-boundary script). It held, and additionally discovered a true fact the prose read had missed. The other 3 passed a draft carrying 15 real violations.
 F8. The user's re-scan requests created SEPARATE TURNS — accidental separate calls. Those found 17/19. The in-turn Pass 4 found 0.
 F9. /traverse runs its disciplines as separate calls — a working strong-end instance exists in this same project.
 F10. Chunk size REFUTED as dominant variable (~2.3k and ~2.6k chars vs a ~5,000 limit).
 F11. Fixed-instruction load = 3,489 lines across 8 files, reloaded every run under Rule 1.

LIVE cause-categories: enforcement-position · verification-vantage · trigger/firing · instrument/mechanism · revision-timing · config-check-absence.
DEMOTED (do NOT resurrect without new evidence): transformation-load/chunk-size · knowledge-absence · method-design-content.

MUST DO: (1) extract anchors as process-properties not errors; (2) adjudicate depth-target structural vs meta-structural; (3) adjudicate scope of "our process" across four values; (4) adjudicate explanation-vs-remedy; (5) BUILD the check × mechanism × vantage matrix as the load-bearing artifact; (6) TEST the nesting claim — are there gaps that persist even at the strong end of the gradient?; (7) RESOLVE frontier flag 1 — can the source-blind vantage be occupied inside a single call?; (8) adjudicate the six remedy shapes, not necessarily picking one; (9) handle both content-conflicts as constraints — the knowledge-reading of "missing" is FALSIFIED and that is itself a finding, and apply the SUBSTITUTION TEST to every honest-limits claim; (10) run the Self-Reference Blindness check in earnest; (11) engage bias-balance honestly (X01 / X03 / X09 / X10 / G08 / X11), applying the project's split-the-confidence discipline.

CRITICAL: stay at PROCESS level. Excluded by warm MQ4's eight-item NOT-list: re-translating · re-litigating error verdicts · apology · terminal agent-blame · file reorganization · smaller chunks · more prose in the same call as THE remedy.

Save sensemaking output to: .../sensemaking.md
```

---

## SV1 — Baseline Understanding

A translation ran a four-pass method, self-reported PASS, and shipped with ~19 errors. The passes were run in one forward motion instead of as real separate steps. The obvious reading: the method is sound but was not properly executed, and the fix is to make execution stricter.

*(This reading is what the analysis below dismantles. It is recorded so the SV delta is legible.)*

---

## Phase 1 — Cognitive Anchor Extraction

The anchors are **process-properties the errors reveal**, not the errors themselves.

### Constraints

| ID | Constraint | Source |
|---|---|---|
| **CN1** | The account must name properties of the *arrangement*, not of the agent. | MQ4 |
| **CN2** | The knowledge-absence explanation is **falsified** — the matching principle was present, correct, and read. | F4 |
| **CN3** | The chunk-size explanation is **falsified** by measurement. | F10 |
| **CN4** | The document-content explanation is **falsified** — surfacing confirmed R18 absent. | R18 |
| **CN5** | More prose in the same call is excluded as *the* remedy — it is the intervention whose failure is being diagnosed. | warm MQ4 |
| **CN6** | The recurrence claim rests on n=2 translations. Confidence must be split, not averaged. | G08, FP3 |
| **CN7** | The error set is a **selection-biased sample** — it contains the errors scrutiny found, not the errors that exist. | X09 |
| **CN8** | Caveats that tell the runtime model its own structure is soft *license relaxation* — so no remedy may ship a "this is only guidance" clause into model-facing text. | `project_skill_design_discipline` Rule 2 |

### Key Insights

| ID | Insight |
|---|---|
| **KI1** | **The one check with an instrument is the one that held.** 1 of 1 mechanised checks passed correctly; 0 of 3 prose checks did — and the mechanised one additionally *discovered* a fact the prose read had missed (`..` = internal suspension, not sentence end). |
| **KI2** | **The re-scans that worked were separate calls.** The user's two requests each created a fresh turn with a narrowed task. Those turns found 17 of 19. The in-turn Pass 4 found 0. The user was hand-cranking the engine without either party naming it. |
| **KI3** | **The vantage partition predicts who found what.** The only two errors detectable *solely from the English* are the only two the assistant never found — and they were found by the only participant occupying that vantage. |
| **KI4** | **The fix was written, shipped, and failed inside a month.** This is not a knowledge problem, a diagnosis problem, or a documentation problem. All three were solved in July. |
| **KI5** | **Pass 4 has a scope hole, not a position hole.** It excludes config/policy checks *by its own definition*. Moving it to a separate call changes nothing — it still would not check what it was never asked to check. |
| **KI6** | **The case catalog is a library with no index.** Every entry reads "the comprehension layer should detect/notice/ask/flag X." To retrieve the entry about noticing X you must already have noticed X. The catalog can *confirm* a noticing; it cannot *cause* one. |
| **KI7** | **Fluency is self-evidencing; fidelity is not.** A fluent English sentence emits positive evidence of its own quality and zero evidence about a missing source word. |
| **KI8** | **A self-reported PASS reports that no check fired.** It is not evidence that nothing is wrong; it is evidence that nothing was found. Absent a mechanism, those are the same output. |
| **KI9** | **Error count measures scrutiny, not quality.** 7 in the prior translation under less scrutiny; 19 here under more. Neither number is about the translations. |
| **KI10** | **The revision loop has no gate at all.** Not a weak gate — an absent one. Pass 3's permitted-changes list licenses fluency edits and attaches no re-check to any of them. |
| **KI11** | **Found incidentally, during this inquiry:** `tools/structural_check.sh` is referenced by the `/traverse` spec, does not exist in this repo, and I have been substituting manual prose judgment and logging "9/9 manual" at every discipline handoff. A specified check with no mechanism, executed as prose self-assessment. **This is a third instance of the same pattern, found in the wild, in a different pipeline, while diagnosing the first two.** |

### Structural Points

| ID | Structure |
|---|---|
| **SP1** | The **enforcement gradient**: prose-instruction < emitted-artifact < separate-call ≈ script-gate ≈ human-gate. (Inherited, `project_skill_design_discipline` Rule 3.) |
| **SP2** | The **vantage set**: source+target · target-only · config+target · source-only · fresh-context. A vantage is defined by what is *present in* and *absent from* the checking context. |
| **SP3** | The method's four passes, all of which stand at the source+target or source-only vantage. None stands at target-only or config+target. |
| **SP4** | The **two-lever load model** and its tension: transformation-load (lever = chunking) × fixed-instruction-load (lever = staging); separate-call chunking re-pays the 3,489-line instruction load on every call. |
| **SP5** | **Five independent properties of any check** — *what* it checks · *from what vantage* · *with what instrument* · *at what enforcement position* · *at what time relative to edits*. (Derived below; this is the load-bearing structure.) |

### Foundational Principles (inherited project axioms, held as constraints)

- **FP1** — the enforcement gradient (Rule 3).
- **FP2** — two gates: lock meaning first, then a scoped post-draft check split into a config-independent spine + a config-derived agenda.
- **FP3** — split the confidence: a claim's *structural distinctness* can be HIGH while its *empirical magnitude* stays MED and quarantined until measured.
- **FP4** — caveats belong in authoring docs, never in runtime model-facing text (= CN8).

### Meaning-Nodes

**firing** (as against *presence*) · **vantage** (as against *diligence*) · **instrument** (as against *instruction*) · **enforcement position** · **the unbounded unfound set** · **scope of a check** (what it was defined to look at).

---

### SV2 — Anchor-Informed Understanding

SV1's "sound method, poor execution" collapses on KI1 and KI2. Execution was not uniformly poor: it was *reliably good* wherever a check had an instrument or a separate call, and *reliably useless* wherever a check was prose in the same motion. The variable is not effort — it is what kind of thing each check was.

*Meta-inspection, H4 + H5 (post-SV2).* **H4 (concept names):** "vantage," "instrument," "enforcement position" are load-bearing labels. Two are inherited project vocabulary ("enforcement position" from Rule 3; "mechanism/instrument" implicit in the memory's "mechanically-checkable"). "Vantage" is loop-coined and must be tested at Phase 3 — does it name a real structural distinction, or is it a restatement of "who checks"? **H5 (motivating examples):** the whole model is built from 19 errors in 2 chunks of 1 text by 1 model. The specific-vs-pattern test is mandatory at Phase 3 and CN7 already limits what the sample can support.

---

## Phase 2 — Perspective Checking

### Technical / Logical

The five properties of SP5 are separable **iff** each can vary while the others are held fixed. Test against the evidence:

- *Vantage vs instrument.* Check "sentence boundaries" (source+target, script) and check "content dropped" (source+target, prose): same vantage, different instrument, opposite outcomes. → separable.
- *Instrument vs position.* The re-scans (F8) used prose instruments at a separate-call position and found errors; the in-turn Pass 4 used prose instruments at a prose position and found none. Same instrument, different position, opposite outcomes. → separable.
- *Vantage vs position.* A separate call *containing the source* is at a strong position and the wrong vantage for the referent check. Position moved, vantage didn't. → separable.
- *Scope vs everything.* Policy conformance (F5) has no vantage, instrument, position, or timing problem — it has no *definition*. The check does not exist. → separable.
- *Timing vs everything.* The regression (KI10) passed every check that ran; the check simply ran before the edit. → separable.

**New anchor — SP5 confirmed as five independently-varying axes, each demonstrated by a pair in the evidence.**

### Human / User — *the uncomfortable perspective*

If the scope includes the working pair, part of the answer is: **a structurally necessary role was being performed by a participant the process never assigned it to.** The user occupied the target-only vantage (KI3) and manufactured the separate calls (KI2). This is uncomfortable because it can be read as deflection.

It is not deflection, and the test is what happens if the user stops. Remove the two requests and the delivered artifact carries 19 errors under a PASS verdict; the method as specified caught 0 of 19 after Pass 4. The user's contribution was not *additional diligence on top of a working process* — it was **the only functioning enforcement in the loop.** Naming that is the precondition for either staffing it deliberately or automating it. Leaving it unnamed is what makes it fragile: an unnamed dependency cannot be maintained.

**New anchor — the process has an unstaffed position that was staffed by accident.**

### Strategic / Long-term

The method currently claims more than any single call can enforce: 3,489 lines of instruction, ~139 catalog principles, 4 harmony tiers with per-entry conditional clauses, 8 config axes, 7 policies — all reloaded per run (F11), all executed inside one forward motion. Under FP4's two-lever tension, every line of that load is re-paid per call, and separate-call architecture *increases* that cost.

The uncomfortable strategic reading: **the honest long-term move may be to shrink what the method claims per call rather than add to it** — fewer things checked per call, each with an instrument, rather than everything checked per call, none with an instrument. This argues against expansion of the user's own build and must be surfaced rather than smoothed.

**New anchor — instruction-load and enforcement are in tension; adding enforcement per call costs load per call.**

### Risk / Failure

Three risks in the leading remedies:

1. **X03 — a source-blind reader invents content.** A reader who cannot see the source, asked to fix unclear English, will resolve ambiguity by guessing — producing exactly error class C04 (invention). Real.
2. **Checklist theatre.** A policy-conformance checklist run as prose becomes seven more things to nod at. The remedy only works if the checklist *forces an enumeration* (name the honorific, quote its rendering, name the policy value) rather than asking for a verdict.
3. **KI11's warning.** A specified-but-unbuilt mechanism degrades silently into prose. Any remedy that names a script without shipping one becomes the thing it was meant to replace.

**New anchor — a remedy's failure mode is usually its own degradation into the thing it replaced.**

### Resource / Feasibility

Sorting the six remedies by what they actually cost:

- A per-document term-lock = one extra generation pass over the source before drafting. Cheap.
- A policy-conformance enumeration = seven rows. Trivial.
- A post-revision re-run rule = zero cost; it is a rule, not work.
- A source-blind reader = one extra call with *less* context than any other call in the pipeline (it holds only the English draft). **Cheaper than every existing pass.**
- A fresh-context adversarial reader = orchestration, not a bespoke engine.
- Full engine (all passes as separate calls) = real build.

**New anchor — the vantage remedy, which addresses the errors nobody could catch, is the cheapest call in the entire method.** This inverts the intuitive ordering, in which the hardest-to-catch errors look like they need the heaviest machinery.

### Definitional / Internal Consistency

Does the model contradict the method's own strongest anchors?

- `translation_method.md`'s Enforcement note already commits SP1. Consistent.
- FP2 (two gates) is consistent with the model but **under-specified against it**: it names *when* checks fire and *whether config matters*, and says nothing about vantage, instrument, or scope. The model does not contradict FP2 — it identifies FP2 as covering two of the five axes.
- **Internal gap found in the method itself:** Pass 4 is titled "Whole-draft Verification (config-independent)" and its stated purpose is to catch what must never happen. But the config-independent framing *excludes* the policy checks, and the policies are defaults-in-force even when the user never chose them (SKILL.md Step 4 presents policies only on request). So the method silently activates seven policies and then defines its only post-draft verification to exclude them. The definition's purpose and its structure are in tension — the check is not protected here.

**New anchor — Pass 4's config-independence is a scope decision that creates a permanent blind region, not merely an unenforced one.**

### Definitional / Frame-exit Completeness

*Gating: fires — the inquiry inherits multi-value terms ("check," "pass," "verification") and uses them across ≥2 distinct values in its own committed structures (the matrix below).*

1. **Existence enumeration for "check", project-wide:** (a) a Pass-4 verification item; (b) a harmony-tier preservation judgment; (c) a policy-conformance determination; (d) a reader-keyed config-appropriateness judgment; (e) a hard-constraint compliance test; (f) **`structural_check.sh` run on this inquiry's discipline outputs.** The frame includes a–e; (f) sits in a different pipeline.
2. **Role assessment for (f):** its role is *a mechanised structural check on an emitted artifact* — precisely the remedy shape the finding proposes. Is the operation coherent if (f) is ignored? **No** — because (f) is a live instance of the very pattern under diagnosis, occurring in a different pipeline, discovered during this run (KI11).
3. **Verdict rigor.** The counter-argument to excluding (f) is that it is the same phenomenon in different clothing. Tested on structural grounds: (f) is a check that is *specified* in a spec, has *no mechanism* in the repo, and is consequently executed as *prose self-assessment* by the same context that produced the artifact — three of the five SP5 properties matching exactly. The exclusion **fails**. → **RE-LOCATE (f) into the frame as independent evidence**, not exclude it.
4. **Residual.** Any frame-exit concern the three categories missed? One: the term "verification" in the memory files refers to a *post-draft* operation only, while the model treats meaning-lock (a pre-draft operation) as also a checkable step. That is a scope widening, stated here, not smuggled.

**New anchor (major) — n for the *pattern* is 3, not 2: the translation method (July→August), the prior İKİNCİ HÜCCET translation, and this inquiry's own missing checker. All three are "specified check, no mechanism, executed as prose by the producing context."**

### Phase / Calibration-State

*Required: the remedy set is phase-dependent.*

- Term-lock, policy enumeration, re-run rule, source-blind reader: require **no calibration and no engine**. Available at the project's current state.
- Full separate-call engine: requires a build the project has not done. Later phase.
- The **validation experiment** (does a term-lock actually reduce error count?) is runnable *now* against the calibration corpus — the project has both the corpus and a fresh untranslated section.

**New anchor — the early-stage default is the four zero-infrastructure remedies; the engine is a named later position, not a blocker.**

---

### SV3 — Multi-Perspective Understanding

Six perspectives produced new anchors and three produced genuine discomfort (Human/User's unstaffed position; Strategic's argument for shrinking the method; Frame-exit's discovery that this inquiry is itself an instance). The model has shifted from "a missing pass" to **"a method that treats 'a check' as one undifferentiated thing when it is five independently-varying properties."**

*Meta-inspection, H1 + H2 + H3 + H7 (post-SV3).* **H1 (candidate set):** the six remedies were framed as competitors; the perspectives show they address *different axes* and are largely non-overlapping — the candidate set was mis-framed as rivalrous. **H2 (frame scope):** widened by Frame-exit to include this inquiry's own missing checker. **H3 (question framing):** "what was *missing*" pre-biases toward absence; the evidence says most things were *present but inert*, which is a different failure than absence — flagged and handled at Phase 3. **H7:** fired above.

---

## Phase 3 — Ambiguity Collapse

### The load-bearing artifact — the check × scope × vantage × instrument × position matrix

Every check the method performs or should perform. **Vantage** = what must be present in the checking context. **Instrument** = script / forced-enumeration / prose-only / absent. **Position** = where it sits on SP1. **Result** = what happened in the observed run.

#### A. Checks the method currently performs (Pass 4)

| # | Check | Vantage | Instrument | Position | Would catch | Result |
|---|---|---|---|---|---|---|
| A1 | Was source content dropped? | source+target | **prose-only** | prose-instruction | `içyüzü` · `dirhem`×3 · dropped subject · `zarurî` | **FAILED** — passed all four |
| A2 | Was anything invented or added? | source+target | **prose-only** | prose-instruction | doubled verb · totalizer "never" | **FAILED** — passed both |
| A3 | Were sentence boundaries preserved? | source+target | **script** | script-gate | boundary merge/split | **HELD** — and found a true fact besides |
| A4 | Did large-scale structure survive? | source+target | **prose-only** | prose-instruction | section/order loss | passed (arguably correctly — none occurred) |

**1 of 4 instrumented. That one held. The other three passed a draft carrying 15 real violations.**

#### B. Checks the method does not perform

| # | Check | Vantage | Instrument available | Would catch | Why absent |
|---|---|---|---|---|---|
| B1 | Word-sense adjudication per polysemous term | **source-only** | forced enumeration | `bitiyor` · `dirilmek` · `kadîm` · `bazı`/`sair` (4) | Pass 1 nominally does this but **emits nothing**, so no artifact exists to check against later |
| B2 | Repetition-count comparison | source+target | forced enumeration / script | `dirhem`×3 | no trigger; harmony Tier 3 states the rule with no firing condition |
| B3 | Cognate / shared-root cluster consistency | source+target | forced enumeration | `hâsiyet`/`hâssa` | same |
| B4 | Multi-sense / pun preservation | source-only → source+target | forced enumeration | `eşeklik` | catalog entry exists (l.359); **no index** (KI6) |
| B5 | Quantifier / intensifier inventory diff | source+target | forced enumeration | "never" · `zarurî` | not specified |
| B6 | Source-form preservation (transliteration, diacritics) | source+target, char-level | **script** | silent normalization | not specified |
| B7 | **Policy conformance** (7 policies × draft) | **config+target** | forced enumeration | `Cenab-ı Hak` | **excluded by Pass 4's own definition** (F5) — a scope hole |
| B8 | **Referent resolution** | **target-only** | forced enumeration | the bare "it" | **no pass occupies this vantage** |
| B9 | **Naive-reader parse** (does the English assert what the source asserts, read cold?) | **target-only** | prose, but from a controlled context | `istifham-ı inkârî` inversion | same |
| B10 | **Post-revision re-run** | inherits the original check's | **a rule, not a judgment** | the regression, as a class | not specified at all (KI10) |
| B11 | Config-licensed-drift adjudication | **config+target** | forced enumeration | *would classify* `İslâm ordusu` · `bozmak` · `istimdad` as licensed-or-drifted | nothing compares draft against config (X11) |

**Matrix reading.** Of 15 checks that should exist, the method specifies 4, instruments 1, and stands at only 2 of the 5 vantages. Three checks (B7, B8, B9) address error classes for which **no vantage in the entire method is capable of detection** — and those are exactly the errors that survived to delivery.

---

### Ambiguity 1 — Are the causes NESTED under one enforcement-position claim, or parallel?

**Strongest counter-interpretation.** They are nested. Every gap in the matrix was knowable, several were written down, and all persisted because they lived at the weakest gradient position — prose read inside the same forward motion it was meant to interrupt. One positional fact explains everything; the rest is detail.

**Why the counter fails (structural grounds).** Three gaps survive a move to the strong end of the gradient:

- **B7 (policy conformance) is position-independent.** Pass 4 excludes config checks *by definition*. Run Pass 4 as a separate call, as a script, as a human gate — it still does not check what it was never defined to check. This is a **scope** failure, and scope is upstream of position.
- **B8/B9 (target-only) require position AND construction.** A separate call is at the strong position; a separate call *containing the source* is still at the wrong vantage. Position buys you the *ability* to control what is in the context; it does not exercise it. **Position and vantage are orthogonal**, and the gradient collapses them only because separate calls conventionally have controlled inputs.
- **B10 (post-revision re-run) is a missing rule.** At any position, a rule that is not stated does not run. Position affects *detectability* of the omission — in a call-based pipeline an edit after verification visibly invalidates the verification's input — but the rule must exist either way.

Conversely the nesting **does** hold for A1, A2, A4: correctly specified, correctly scoped, right vantage, failed purely on instrument+position — and F8 shows they succeed when moved to a separate call.

**Confidence: HIGH** — the counter is refuted by exhibiting specific gaps that survive the proposed unifier, not by precedent.

**Resolution.** The nesting is **PARTIAL, and its partition is the finding.** Gaps sort into five kinds by *which of the five check-properties* failed:

| Kind | Failed property | Instances | Fixed by |
|---|---|---|---|
| **Positional** | enforcement position | A1, A2, A4 | moving up the gradient |
| **Scope** | what the check is defined to look at | B7 | defining the check (position-independent) |
| **Vantage** | what is present in the checking context | B8, B9 | constructing a context that lacks the source (position necessary, not sufficient) |
| **Instrument** | how the check is performed | B1–B6 | forced enumeration (works at any position) |
| **Timing** | when the check runs relative to edits | B10 | a rule (position-independent; position aids detection) |

**What is now fixed.** A single-root-cause account is excluded. So is a flat list of parallel causes. The committed shape is a **typed partition over one structural claim: the method treats "a check" as one undifferentiated thing when it is five independently-varying properties.**

**What is no longer allowed.** Presenting the enforcement gradient as the whole answer. Presenting "add a source-blind pass" as sufficient (it addresses one kind of three-to-five).

**What depends on this.** The remedy adjudication (Ambiguity 5); the depth-target (Ambiguity 3); the finding's whole organizing structure.

**What changed in the model.** The unifier moved up a level: not "one cause," but **one conflation** — and the July fix's failure becomes predictable rather than surprising. July's fix addressed *ordering*, a sixth property adjacent to position. It said nothing about vantage, scope, instrument, or timing. August's failure is what that fix predicts.

---

### Ambiguity 2 — Can the target-only (source-blind) vantage be occupied inside a single call?

**Strongest counter-interpretation.** Yes. Instruct the model: "now read the English alone, as a reader with no access to the Turkish, and flag anything unresolvable." Models follow framing instructions competently; the vantage is a stance, and stances are adoptable.

**Why the counter fails (structural grounds).** The vantage is constituted by an **absence**, and no instruction removes information from a context. The specific mechanism: the check's output is a judgment — *is this referring expression resolvable?* — and that judgment is made by a reader who already holds the referent. The reader does not consult the source to resolve "it"; the referent is simply not experienced as missing. This is not a compliance failure that more emphasis could fix; it is that the question being answered has already been answered by the context before the check begins. The direct evidence: the assistant re-scanned the same text twice under explicit instruction to find errors, found 17 source-comparison errors, and found **zero** of the two target-only errors on either pass.

**Confidence: HIGH.**

**Resolution — but with a practical inversion.** The vantage is **not occupiable within a call that contains the source.** However — the call required to occupy it is **the cheapest call in the entire method**: it holds only the English draft and one instruction. It needs no engine, no orchestration, no build; it needs a second turn with *less* context than any existing pass. F8 shows the user manufactures such turns by asking. So the answer to "is this remedy available now?" is **yes** — the barrier was never cost, it was that nobody had named the requirement.

**Handling X03 (the source-blind reader invents content) — by construction, not by exhortation.** The source-blind reader is given **no edit authority.** Its output is a *question list*: "the referent of 'it' at ¶4 is not recoverable from this text"; "this sentence asserts P — is P what the source says?" Every fix is then made in a source-present context, which is the vantage that demonstrably works. A reader that cannot write cannot invent.

**What is now fixed.** Source-blind checking requires a separate call with controlled input, and that call outputs questions rather than edits.

**What is no longer allowed.** "Read it as a fresh reader" as an in-call instruction. It is not a weak version of the remedy; it is a different operation that does not perform the check.

**What depends on this.** The availability classification of remedies 4 and 5; the claim that vantage and position are orthogonal.

---

### Ambiguity 3 — Depth-target: does the account stop at structural, or go to meta-structural?

**Strongest counter-interpretation.** Stop at structural. Name the missing steps, show the matrix, propose the checks. Going meta-structural risks philosophizing about why fixes fail instead of fixing anything, and the user asked what was missing — a list of missing things is a direct answer.

**Why the counter fails (structural grounds).** A structural-only account has already been produced once, in July, and its artifact is the thing that failed in August. F2+F3 are not background — they are a **completed experiment on the structural-only answer**, with a recorded negative result. An account that stops at "you are missing a source-blind pass" produces a fifth correctly-worded prose instruction in the same file that already contains four, and CN5 excludes exactly that. The meta layer is not optional depth; it is the layer at which the previous answer's failure is explicable.

**Confidence: HIGH.**

**Resolution: META-STRUCTURAL.** The account goes to the layer that explains why a correct, shipped fix did not take — and the answer at that layer is the conflation (Ambiguity 1): the July fix improved one property of a check (ordering/position) while the method continued to treat all five as one thing, so four remained untouched and the errors those four produce recurred on schedule.

**What is now fixed.** The finding must explain the July→August recurrence, not merely list gaps.

**What is no longer allowed.** A gap list as the terminal deliverable.

---

### Ambiguity 4 — Scope of "our process"

**Strongest counter-interpretation.** Restrict to the SKILL's written method. Widening to the human-AI working pattern risks reading as blame-shifting, and the user asked what was missing from the *process*, which most naturally means the specified one.

**Why the counter fails (structural grounds).** The SKILL-only frame cannot represent the load-bearing evidence. F8's mechanism — the re-scans that found 17 of 19 were separate turns created by the user's requests — is invisible inside a frame containing only the written method. Under that frame, the correct description of the run is "Pass 4 passed and the translation shipped," which omits everything that actually found the errors. A frame that cannot describe the functioning enforcement in the system is the wrong frame.

**Confidence: HIGH.**

**Resolution.** **The SKILL + the human-AI working pattern, as one system** — with the non-existent runner layer named as the *position* one remedy waits on, not as a member of the diagnosed system. The primary frame is the pair, because the pair is what ran.

**What is now fixed.** The finding must state the division of labour explicitly, including the position the user occupied without assignment.

**What is no longer allowed.** Describing the run as if the method's specified steps were the only steps that executed.

**Framing constraint carried forward (CN1).** The user's role is named as an *unstaffed position accidentally staffed*, never as a performance judgment. The test that keeps this honest: the finding must be equally true if the human participant is replaced by any other — it is a claim about the arrangement's shape.

---

### Ambiguity 5 — Explanation or remedy? And are the six remedies rivals?

**Strongest counter-interpretation (two-part).** (i) Explanation only: the honest-limits evidence is strong, prose has been tried and failed, and proposing remedies invites a repeat of July. (ii) And the six remedies are rivals competing for one slot; picking wrong is worse than picking none.

**Why both fail (structural grounds).** (i) fails because the honest limits, once tested (Ambiguity 6), turn out to bound *self-verification by the producing context* — not to bound *building a differently-constructed check*. Nothing in the limits argues against a term-lock, a policy enumeration, or a cheap source-blind call; those are not the failed intervention, they occupy different positions on the gradient. (ii) fails against the matrix: the six map to **different rows** with almost no overlap.

**Confidence: HIGH** on non-rivalry; **MED** on the completeness of the remedy set.

**Resolution.** Remedy is owed, and the six are complements sorted by which check-property they repair:

| # | Remedy | Repairs | Catches | Position | Available? |
|---|---|---|---|---|---|
| R1 | **Per-document term-lock** — before drafting, enumerate from the source: every polysemous term with its candidate senses, every deliberate repetition with its count, every cognate cluster, every named rhetorical device, every honorific | **Instrument + trigger** (the index the catalog lacks, KI6) | B1–B5 → 8 of 19 | emitted-artifact | **NOW** |
| R2 | **Policy-conformance enumeration** — 7 rows: policy · its value · where it applies in this source · how the draft rendered it | **Scope** (B7's definitional hole) | 1 of 19, plus reclassifies 3 more via B11 | emitted-artifact | **NOW** |
| R3 | **Post-revision re-run rule** — any edit after verification re-runs the checks its span touched | **Timing** | the regression class | a rule | **NOW** (free) |
| R4 | **Source-blind reader, question-list only, no edit authority** | **Vantage** | B8, B9 → the 2 nobody could catch | separate call, controlled input | **NOW** — cheapest call in the method |
| R5 | **Fresh-context adversarial reader** | Vantage + position, generally | broad | separate call | needs orchestration, not a bespoke engine |
| R6 | **The engine** — passes as separate calls with real intermediate artifacts | **Position**, systematically | A1, A2, A4 | separate call | **ENGINE-GATED** |

**Five of six are unblocked.** Only R6 requires a build — and R6 repairs the property the July fix already targeted with prose.

**What is now fixed.** The deliverable carries a remedy set typed by check-property, with availability marked.

**What is no longer allowed.** Selecting one remedy as *the* fix; deferring the whole remedy set on the engine.

---

### Ambiguity 6 — The honest-limits claims: process property or agent property? (Substitution test)

*Per warm's content-conflict 2. Restate each claim with a human translator as its subject. Survives → property of the arrangement → IN. Collapses → property of this agent → OUT per MQ4.*

| Claim | With a human translator as subject | Verdict |
|---|---|---|
| A producer cannot reliably detect its own omissions by re-reading in the same context | A translator re-reading their own draft with the source open reliably misses their own omissions — which is why publishers employ separate copy-editors and why proofreading one's own writing is proverbially unreliable | **SURVIVES → IN** |
| A producer cannot occupy the source-blind vantage while the source is in its context | A translator who has just rendered a passage cannot read the English as someone who has never seen the Turkish; they know what it means | **SURVIVES → IN** |
| A self-reported PASS is evidence that no check fired, not that nothing is wrong | "I checked it" without a checklist reports that the checker found nothing, not that nothing was there | **SURVIVES → IN** |
| Fluency is self-evidencing; fidelity is not | A fluent English paragraph reads as correct to its author regardless of what the source said | **SURVIVES → IN** |

**All four survive. Content-conflict 2 resolves: these are process claims and are in scope.**

**And the test yields an inversion worth carrying into the finding.** For the second claim, the human case is *strictly worse*: a model's context can be emptied by constructing a new call; a human's memory of what they just translated cannot be. **The source-blind vantage is more occupiable for an AI-executed process than for a human one** — the remedy is *available here in a form unavailable to human translation workflows*, which normally solve it by hiring a second person. This is not a limitation being excused; it is a capability the process is failing to use.

**Confidence: HIGH.**

---

### Ambiguity 7 — What does "missing" mean, given that the knowledge was present? (Content-conflict 1)

*Warm flagged the knowledge-reading as falsified and required that the falsification not vanish.*

**Strongest counter-interpretation.** Something *was* missing from the documents — no file contains "check that referring expressions resolve without the source." The falsification is too strong; the specific check was absent even if adjacent principles were present.

**Why the counter partly holds and is absorbed rather than refuted.** It is correct for B8/B9 and B10 — those checks are genuinely unwritten. It is false for the majority: catalog #4 covers the arrangement error, #20/#37/#38 the repetition, l.359 the pun, #7 the polysemy, and harmony Tier 2 the pronoun chain. So "missing" splits: **a minority of checks were absent from the documents; a majority were present and inert.**

**Confidence: HIGH** on the split; **MED** on the exact proportion (CN7's selection bias affects the denominator).

**Resolution.** "Missing" means **missing from the run, not missing from the corpus.** The corrected statement: *what was missing was not the principle but the condition under which the principle fires* — and the specific missing condition is an **enumeration keyed to this source** that makes the noticing unavoidable instead of optional. A principle phrased "the comprehension layer should notice X" is retrievable only by a reader who has noticed X (KI6); it can confirm a noticing, never cause one. R1 is the direct answer to this, and it is the reason R1 leads the remedy set.

**What is now fixed.** The finding must state the falsification explicitly. "You didn't know" is excluded as an account, and any remedy that consists of *writing the principle down more clearly* is excluded with it.

**What is no longer allowed.** Treating the catalog's completeness as evidence of the method's adequacy — completeness of a library is orthogonal to retrievability from it.

---

### Ambiguity 8 — Load-bearing concept test on "vantage" *(required refinement)*

**Ambiguity.** Is "vantage" a real structural distinction, or a loop-coined relabelling of "who does the checking"?

**Strongest counter-interpretation.** It is a proxy. What actually varies is *who* checks — the producer versus someone else — and "vantage" dresses a personnel fact in spatial metaphor.

**Why the counter fails (structural grounds).** Vantage and identity vary independently in the evidence. The *same* checker (this assistant, same session) occupied the source+target vantage in Pass 4 and would occupy the target-only vantage in a call constructed without the source — same identity, different vantage, and the matrix predicts different detection capability. Conversely a *different* checker (the user) occupying the source+target vantage would face the same curse of knowledge if they had just produced the draft. What determines detection is **what is present in the checking context**, not who is holding it. Vantage is the structural variable; identity is a common proxy for it.

**Discoverability sub-aspect.** The concept's use depends on a runtime determination — *which vantage does this check require?* — so the determination must be specified, not implicit. It is: a check requires the target-only vantage iff its question can be answered without the source, and answering it *with* the source available changes the answer. B8 and B9 satisfy this; A1–A4 do not.

**User-language alignment (H9).** The user's own words were *"it refers to what? … it is also not clear there?"* — a question about whether the English resolves on its own. That is the target-only vantage stated in plain language. The concept name is a formalization of the user's observation, not a neologism imposed on it.

**Confidence: HIGH.**

---

### Ambiguity 9 — Specific-vs-pattern *(required refinement; CN7 + H5)*

**Ambiguity.** Are these 19 errors the whole problem, or a sample of a wider one?

**Strongest counter-interpretation.** They are a biased and unrepresentative sample, and the matrix generalizes from them illegitimately. The class distribution reflects what re-scans find, not what exists; errors visible only from an unoccupied vantage are, by construction, under-represented.

**Why the counter partly holds — and which way it cuts.** It holds for **proportions** and fails for **direction**. Any error detectable only from a vantage nobody occupied could only enter the sample if the user happened to notice it. So the observed 2 target-only errors are a **lower bound**, and the true count is ≥2 and plausibly higher. The selection bias therefore *understates* the vantage gap while making the 15/1/2/1 ratio unusable as a measurement.

**Confidence: HIGH** on direction; **the proportions are explicitly quarantined.**

**Resolution — split the confidence per FP3.**

- **Structural distinctness of the five check-properties: HIGH.** It follows from what a check *is*, and each axis is demonstrated varying independently by a pair in the evidence (Phase 2, Technical). No error-count is required to support it.
- **Empirical magnitude — how much any remedy reduces errors: MED, QUARANTINED.** Unmeasured. n=2 for the translation instances (n=3 for the *pattern*, per KI11 + Frame-exit, which raises confidence in the structure and not in the magnitude).
- **A validation experiment is therefore a MUST, not a nice-to-have**: translate one comparable section with R1–R4 in force and one without, and count. The project has the corpus and the untranslated remainder; the experiment is runnable now.

---

### SV4 — Clarified Understanding

Nine ambiguities collapsed. What is now clear: the method conflates five independently-varying properties of a check; the gaps sort into five kinds by which property failed; the nesting under enforcement-position is partial and the residue is the informative part; the source-blind vantage is unoccupiable in-call but its call is the cheapest in the method; the remedies are complements, five of six unblocked; all four honest-limit claims survive the substitution test as process claims, one of them inverting in the AI process's favour; and "missing" means missing-from-the-run, with a minority genuinely absent and a majority present-and-inert.

What is no longer viable: single-root-cause accounts · the enforcement gradient as a total explanation · "add a source-blind pass" as sufficient · in-call instructions to adopt a source-blind stance · deferring the remedy set on the engine · any account that reads the run as if only the specified steps executed · any claim resting on the 15/1/2/1 proportions.

---

## Phase 4 — Degrees-of-Freedom Reduction

**Fixed:**

1. The organizing structure is the **five check-properties** (what · vantage · instrument · position · timing) and the five gap-kinds that follow.
2. Depth-target = **meta-structural**; the finding must explain the July→August recurrence.
3. Scope = **SKILL + human-AI working pattern as one system**; the runner layer is a named position, not a diagnosed member.
4. Explanation **and** remedy; remedy typed by property and marked by availability.
5. The matrix (15 checks × 5 properties) is the evidence artifact.
6. The source-blind vantage requires a separate call with controlled input; its output is a question list with no edit authority.
7. All four honest-limit claims are IN as process claims.
8. Confidence is split: structure HIGH, magnitude MED-quarantined, validation experiment a MUST.
9. `structural_check.sh`'s absence is IN-frame as a third independent instance.

**Eliminated:** chunk-size remedies · file reorganization · knowledge-restatement · more prose in the same call as the terminal fix · single-cause framing · one-winner remedy selection · engine-gating of the whole remedy set · in-call source-blind instruction · agent-capability as terminal explanation.

**Remaining viable paths (for Decomposition/Innovation):** how the finding orders the five gap-kinds for presentation · how R1's term-lock artifact is shaped concretely · whether R2's enumeration lives in Pass 4 or a new Pass 5 · how the validation experiment is specified · how much of the division-of-labour statement belongs in the SKILL versus in an authoring doc (constrained by CN8/FP4 — the "this is only a nudge" honesty goes in authoring notes, never in runtime text).

---

### SV5 — Constrained Understanding

The problem is fully typed and the solution space is bounded. Every remaining decision is about **presentation and specification**, not about diagnosis. The one genuinely open empirical question — how much each remedy is worth — is explicitly quarantined with a runnable experiment attached.

---

## Phase 5 — Conceptual Stabilization

*Accommodation-trigger check (H6): did perspectives keep forcing revisions? The model was revised **once**, substantially, at Phase 2 Technical (single-cause → five properties), and every subsequent perspective **added rows to that structure without altering it**. Frame-exit added an instance; Human/User added a role; Strategic added a tension; Risk added failure modes; Resource inverted a cost ordering. That is refinement, not patching. The Accommodation trigger does not fire.*

### Self-Reference Blindness — run in earnest (H8, failure mode #6)

This inquiry is a model-executed, prose-specified method diagnosing a model-executed, prose-specified method. Applying the finding to itself:

- **Position:** the loop scores **strong**. Its disciplines ran as genuinely separate calls, each loading its own spec, each emitting an artifact the next reads. That is R6's architecture, already built, for inquiry. The two pipelines are **not identically positioned**, so the finding is not self-refuting in the way it would be if this were one prose pass.
- **Vantage:** the loop scores **weak**, and identically weak to the thing it diagnoses. Every discipline in this pipeline ran in one context — mine. No discipline occupied a vantage blind to the previous disciplines' output. Critique is adversarial *by instruction*, which is precisely the construction Ambiguity 2 ruled inadequate for the source-blind check. The loop has the position without the vantage.
- **Instrument:** the loop scores **worst** — KI11. Its one specified mechanical check does not exist in this repo, and I have been substituting prose self-assessment and recording "manual, N/N passed" at every handoff. That is A1–A2's exact failure shape, live, in this document's own audit trail.

**Consequence for this finding's confidence, stated concretely rather than as disclaimer:**

- Claims checkable against **artifacts** — the matrix cells, the five properties' independent variation, the git-verified July→August sequence, F5's scope exclusion, the substitution-test results — are **well-supported**. They can be re-derived by anyone reading the same files, and a reader who disagrees can point at a cell.
- Claims resting on **judgment inside the producing context** — that the five properties are *exhaustive*, that R1 is the highest-value remedy, that the nesting partition is the *best* organizing structure — carry the same weakness the translation method carried. They should be read as this context's best account, not as verified.
- **The available correction is the same one the finding prescribes:** a reader occupying a vantage this loop does not have. Critique is the nearest thing available, and it is instruction-constructed, so it is a partial instrument. The finding should say so where it commits.

### SV6 — Stabilized Model

**What was missing was not knowledge, not diligence, and not a pass. What was missing was a distinction.**

The method treats "a check" as one undifferentiated thing. A check is actually five independently-varying properties: **what** it checks · **from what vantage** (what must be present in, and absent from, the checking context) · **with what instrument** (script, forced enumeration, or prose judgment) · **at what enforcement position** (prose instruction, emitted artifact, or separate call) · **at what time** relative to edits. Because the method never separates them, it cannot specify them, cannot audit them, and cannot repair them one at a time.

Every one of the nineteen errors is a failure of one of those five properties, and they sort cleanly:

- **Instrument** — eight errors. The one check with an instrument held perfectly and additionally *discovered* a fact the prose reads had missed; the three prose checks passed a draft carrying fifteen real violations. The catalog holds the matching principle for nearly every one of these eight, correctly worded, fully read into context — and inert, because a principle phrased "notice X" is retrievable only by a reader who has already noticed X. What was missing is not the principle but the **enumeration keyed to this source** that would make the noticing unavoidable.
- **Vantage** — two errors, and they are the two that survived everything. No pass in the method stands where the English can be read alone, so the errors visible only from there were structurally invisible to every check that ran. The one participant who *did* stand there found both. That is not a coincidence; it is what the matrix predicts.
- **Scope** — one error. Pass 4 excludes config and policy checks by its own definition, while the SKILL activates seven policy defaults the user was never shown. The violation had no possible catcher anywhere in the method — not an unenforced check, an undefined one.
- **Timing** — one error. A fluency-motivated revision after verification broke a rendering the first draft had right. No rule attaches a re-check to an edit; Pass 3's permitted-changes list licenses exactly that kind of edit and gates nothing.
- **Position** — the rest, and the reason none of the above got fixed. Every one of these gaps was addressable, and several were already written down.

**And this is why July's fix did not take.** The prior inquiry diagnosed correctly, the fix was written, and the fix shipped — Step 5 was rewritten from a flat bag into four ordered passes with an explicit instruction not to collapse them. One month later the same class recurred. The fix repaired **ordering**, one property adjacent to position, and left vantage, scope, instrument and timing exactly as they were. The errors those four produce recurred on schedule. A correct answer delivered against one property of a five-property object leaves four-fifths of the object untouched — which is the meta-structural reason a shipped, correct fix failed, and the reason this account cannot stop at naming another missing step.

**What actually enforced anything.** Seventeen of nineteen errors were found on re-scans, and each re-scan was a fresh turn created by the user asking — structurally, a separate call, the strong end of the gradient, hand-cranked. The in-turn Pass 4 found none. The two errors the user found unaided are precisely the two only their vantage can reach. So the working enforcement in this system was a participant standing in a position the process never assigned to anyone, using a mechanism the process does not know it depends on. Remove the two requests and the artifact ships with nineteen errors under a PASS verdict. Error count in this arrangement measures how many times the user asked.

**What is honestly fixed and what is not.** Four claims about self-verification survive restatement with a human translator as subject and are therefore properties of the arrangement, not of the agent: a producer cannot reliably detect its own omissions by re-reading in the same context; a producer cannot occupy the source-blind vantage while holding the source; a self-reported PASS reports that no check fired, not that nothing is wrong; fluency is self-evidencing and fidelity is not. One of them inverts in this process's favour — a model's context can be emptied by constructing a new call, and a human translator's memory cannot, so **the source-blind vantage is more occupiable here than in a human workflow**, which normally has to hire a second person to get it. The process is failing to use a capability it has.

**And five of the six remedies need nothing built.** A per-document term-lock is one enumeration pass over the source. A policy-conformance check is seven rows. A re-run-after-editing rule is free. A source-blind reader — which addresses the only errors nobody could otherwise catch — is the *cheapest* call in the entire method, holding one text and one instruction, and it must output questions rather than edits, because a reader that cannot write cannot invent. Only the full separate-call engine requires a build, and it repairs the one property July already tried to reach with prose.

**Held with split confidence.** That the five properties are structurally distinct is HIGH — it follows from what a check is, and each axis is shown varying independently by a pair in the evidence. How much any remedy is worth is MED and **quarantined**: two translation instances, and a sample biased toward what re-scans find, which understates the vantage gap while making its proportions unusable. A validation experiment is therefore a MUST and is runnable now against the same corpus. The pattern itself has a third instance, found while this inquiry was running: `structural_check.sh` is specified by the `/traverse` spec, absent from this repo, and has been substituted with prose self-assessment at every handoff in this document — the same shape, in a different pipeline, discovered by accident. This loop scores strong on position, weak on vantage, and worst on instrument, which is exactly the pattern it diagnoses; its artifact-checkable claims should be read as well-supported and its judgment claims as this context's best account.

**How SV6 differs from SV1.** SV1 said: sound method, poor execution, fix by making execution stricter. SV6 says: execution was reliably good wherever a check had an instrument or a separate call and reliably useless everywhere else, so the variable was never effort; the method's real defect is that it cannot *name* the difference between those two situations, because it treats a check as one thing when it is five; and "make it stricter" is the intervention that was already tried, in July, and is on record as having failed.

---

## Telemetry

- **Perspective saturation:** not reached at Phase 2 — six of nine perspectives produced new anchor *types* (Technical: axis-separability; Human: the unstaffed position; Strategic: the load/enforcement tension; Risk: remedy self-degradation; Resource: the cost inversion; Frame-exit: the third instance). Three uncomfortable perspectives fired and two changed the model materially. Saturation approached only after Frame-exit; Phase/Calibration confirmed without adding a type.
- **Ambiguity resolution ratio:** 9 identified / 9 resolved. Two carry explicit quarantines rather than clean closure (A9's proportions; A5's remedy-set completeness at MED). Zero silently dropped.
- **SV delta:** large. SV1 = "sound method, poor execution." SV6 = "a method that cannot distinguish five independently-varying properties of a check, one of which the previous fix addressed." The organizing claim inverted from *compliance* to *specification*.
- **Anchor diversity:** all five anchor types present — 8 constraints, 11 key insights, 5 structural points, 4 foundational principles, 6 meaning-nodes — drawn from nine perspectives.
- **Failure modes checked:** Status Quo Bias (the SKILL is the user's own build and its documents are correct; the finding still concludes its central abstraction is wrong — the instinct to protect was noticed and overridden on the F5 internal-gap evidence) · Premature Stabilization (the model was revised once at Phase 2 and refined thereafter; the Accommodation trigger was checked and does not fire) · Anchor Dominance (**noted as a live risk** — the enforcement gradient is a very strong inherited anchor and Ambiguity 1 exists specifically to test whether everything resolves toward it; the test partially refuted it, which is the evidence that the anchor is not doing all the work) · Perspective Blindness (three uncomfortable perspectives fired deliberately, including the user's own role and the argument for shrinking the method) · Clean Resolution Trap (every ambiguity carries a stated counter refuted on structural grounds, not on precedent; the two that could only be partly refuted are recorded as partial — A7, A9) · Self-Reference Blindness (run in earnest above, with a three-way position/vantage/instrument scoring of this loop against its own finding).
- **Meta-inspection hooks fired:** H4, H5 (post-SV2) · H1, H2, H3, H7 (post-SV3) · H4 sub-aspects incl. H9 (Ambiguity 8) · H5 (Ambiguity 9) · H6 (Phase 5) · H8 (Phase 5). All nine.

**Load-bearing artifact for downstream:** the 15-check × 5-property matrix (Phase 3), the five-kind gap partition (Ambiguity 1), and the six-remedy availability table (Ambiguity 5).
