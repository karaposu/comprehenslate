## User Input

Routelister exhaust step of the /traverse inquiry `2026-07-11_04-48`. Territory = this inquiry's own finished artifacts (_branch, articulate_simple, surfacing [DF1-8/FF1-5], articulate_warm, sensemaking [pivot/flip-on/whole-span-remainder], decomposition [A/B/C(C1+C2)/D + I7], innovation [S1/S2/S4 ACTIONABLE + S3 RE-TEST + S5 DEFERRED], critique [7 REFINEs + pivot-confidence-split + lever-interaction + quarantine]). Goal (from _branch.md): evaluate whether mandatory-chunking-for-adherence is real and, if so, design how — gated evaluate-only → design → apply-the-SKILL-edit, NO SKILL edits without explicit user authorization. Enumerate the onward route-field; be prescriptive, never choose (the reach decision + any SKILL edit belong to the user). Route-seeds: the research-frontier magnitude-validation (doubly-motivated; lifts the quarantine); the apply-the-edit phase-split (instruction-now ADD-CONTENT + engine-later config-flip, both gated on authorization); the co-design dependency (C2 gated on the un-wired 3-Pass via Pass-2 = I7 + 00-24; sibling-lever to 04-12 + the lever-interaction); the whole-draft-check-after (01-09, 3-Pass-independent); the de-quarantine/re-test. Write routelister.md + _route.md, both stay in inquiry root.

---

# Route-Map — the onward route-field of inquiry `2026-07-11_04-48` (mandatory-chunking-for-adherence)

## Map Header

- **Identities enumerated:** 6 live (+ 4 excluded, with reasons)
- **High-priority (Priority HIGH):** 1  (R1 — the empirical validation)
- **Essential-count (`core` routes):** 3  (R1 core · R3 core·@engine-built · R4 core·@3-pass-wired) — the "what can't the goal skip?" triage number
- **Grain:** project-space (breadth) · **Entry point:** fresh · **Mode:** root
- **Standing gate on the whole APPLY sub-field:** the reach decision (evaluate-only → design → apply) + any SKILL-file edit belong to the **user**. R2/R3 are cast as prescriptive directions **downstream of that authorization**, not as things to do now.

## Route Index

| # | Direction | engagement-type | Priority | Essentiality | ✓ |
|---|---|---|---|---|---|
| R1 | Empirical magnitude-validation of adherence-decay-under-load | TEST | HIGH | core | |
| R2 | Instruction-now chunking clause in SKILL.md | DEVELOP | MED | supporting | |
| R3 | Engine-later chunking-policy flip in PipelineConfig | DEVELOP | MED | core · @engine-built | |
| R4 | Chunking↔3-Pass co-design (the Pass-2 "before" bracket) | CONSOLIDATE | MED | core · @3-pass-wired | |
| R5 | Bounded-load sibling-principle with 04-12 staging | CONSOLIDATE | LOW | supporting | |
| R6 | Whole-draft-check "after" bracket (01-09), 3-Pass-independent | PURSUE-SEED | MED | supporting | |

*(`grain` omitted — constant `project-space`; `kind` omitted — derivable from engagement-type; `Confidence` on the records, not a triage signal. `✓` is consumer-filled; routelisting authors it empty and never reads it.)*

---

## Route Records

### R1 — Empirical magnitude-validation of adherence-decay-under-load
- **Goal:** confirm-or-refute that mandatory-chunking-for-adherence is *real at the claimed scale* — the evaluation half of the inquiry's goal
- **engagement-type:** TEST *(epistemic)*
- **Move:** run matched-size translation trials that hold the *method* constant (same SKILL, same 3-Pass state) and vary only the per-unit **transformation working-set** size, per model, measuring instruction-adherence (dropped clauses / skipped principles) as the response
- **Lands:** an evidence curve of adherence-vs-working-set-size per model → **lifts the quarantine** on the pivot's magnitude (distinctness is already HIGH/structural; this supplies the missing MED→magnitude evidence) and fixes the adherence-safe granularity level + numeric cap that R2/R3 need
- **Touches:** the pivot's variable claim (source-unit + output + local-tracking working-set, *not* source-char-count alone — isolate which sub-component drives decay) · the ~3500-char estimate (test as *real-in-kind / approximate / model-dependent*, not as an exact threshold) · the 06-14 never-run validation MUST (this is that same experiment, now *also* adherence-motivated)
- **WHY:** the whole finding ships as *a reasoned design conditional on an unvalidated-but-plausible magnitude* (critique's central FLAG) — running the trials is what converts the conditional into a confirmed driver, so the **end goal gains** its evaluation-half actually landing rather than staying a hypothesis; without it every downstream design route rests on an unmeasured premise
- **Priority:** HIGH   **Confidence:** MED   **Essentiality:** core
- **Guidance Mode:** full
  - "isolate the variable: vary source-size, output-size, and active-rule-count *independently* so the trial says *which* load component drives decay" (bc the pivot claims the transformation-working-set, not raw source chars — the design's budget only makes sense if that's right)
  - "hold the method constant — same 3-Pass wiring state across arms" (bc otherwise adherence-decay confounds with the un-wired-3-Pass, exactly the rival the sensemaking separated on the load-magnitude-vs-method-structure axis)
  - "sweep per-model (Opus-4.8-max + at least one smaller model)" (bc the 'lower for smaller models' instinct is a per-model curve, not a constant — R3's per-model dim consumes this)
  - "report the adherence-safe *granularity level* + a numeric cap, not just a char number" (bc the budget is structure-first with the number as a later cap — R2/R3 both need the level)
- **Depth-link:** none (not yet drilled)

### R2 — Instruction-now chunking clause in SKILL.md
- **Goal:** raise translation-adherence *now*, before the engine exists — the earliest-available slice of the design half
- **engagement-type:** DEVELOP *(teleological)*
- **Move:** add a clean, actionable model-facing instruction to SKILL.md — "translate one structural unit at a time, snapping to structure" — expressed in **structural units** (mesele / section / paragraph), not a token count
- **Lands:** SKILL.md carries a budget-gated-conditional chunking instruction (short texts pass through; never always-split); the honest "this is a probability-raiser, not enforcement — the real bound needs separate calls" caveat lives in the **authoring notes**, not the model-facing text
- **Touches:** SKILL.md Step 5 (currently translates whole, no chunking) · the authoring-notes layer (where the caveat-audience split puts the "it's a nudge" honesty) · the 04-12 caveat-audience lesson ([[project_skill_design_discipline]] — a runtime caveat that says "this isn't enforced" *licenses* relaxation, so it must not sit in the model-facing text)
- **WHY:** instruction-now is a **weak** one-run probability-raiser (same softness as 04-12 staged borders — the model still sees the whole source in one context), but it is the *only* lever available before the engine, so the **end goal gains** an immediate, positive-EV adherence nudge; its weakness is *why* it is `supporting` not `core` — the real enforcement is R3
- **Priority:** MED   **Confidence:** MED   **Essentiality:** supporting
- **Guidance Mode:** full
  - "keep the model-facing text a clean imperative; route the 'it's only a nudge' honesty to authoring notes" (bc per 04-12, telling the model its own instruction is unenforced is self-undermining)
  - "express the budget in structural units the model can *read*, with R1's numeric cap as a later refinement" (bc the model chunks by perceiving structure, not by counting tokens)
  - Meaning-gaps:
    - exact placement + wording in Step 5 (whole-read-then-unit-translate sequencing) — mid — wrong sequencing could collide with the un-wired-3-Pass's whole-text Pass-2 (R4)
    - the budget-gate threshold expressed as a structural level — mid — needs R1's granularity result to be non-arbitrary; stub with a conservative default (e.g. section-level) until then
    - whether this belongs in SKILL.md now vs waiting for R3 — low — a disposition the reach decision settles, not a design gap

### R3 — Engine-later chunking-policy flip in PipelineConfig
- **Goal:** *enforce* the transformation-working-set bound — the design half's real prize
- **engagement-type:** DEVELOP *(teleological)*
- **Move:** when the pipeline engine is built, flip the dormant `PipelineConfig.chunking_budget` from `None` to a structural-default, add the per-model dimension, and drive generation as **separate calls per chunk** (harmony-boundary-snapping, reusing the designed harmony-tier-aware / fixed-budget-with-snap mechanism)
- **Lands:** chunk generation runs in separate calls that **physically bound** the source the model sees per generation (the model *cannot* see the other chunks' source) → the adherence prize the instruction-now version only gestures at
- **Touches:** `schemas.py` PipelineConfig chunking apparatus (dormant: `chunking_budget` / `chunking_granularity` / `chunking_mechanism_override` / `parallel_mode`) · the unbuilt engine (the wiring that turns the knobs into separate calls) · the per-model budget dim (consumes R1's per-model curve)
- **WHY:** separate calls are the STRONG end of the enforcement gradient (prose-instruction < emitted-artifact < separate-call) and chunking's natural home is that strong end — so the **end goal gains** actual enforcement of the transformation-load bound, which is *why* this is `core`; the coreness is phase-deferred to when the engine exists (`@engine-built`), not weakened
- **Priority:** MED   **Confidence:** MED   **Essentiality:** core · @engine-built
- **Guidance Mode:** full
  - "scope the enforcement claim honestly: separate calls bound the *transformation* load, NOT the fixed instruction/rule load — each call reloads the full ~80-principle stack" (bc that's the critique's lever-interaction — see R5; over-claiming 'chunking enforces adherence' hides that staging still owns the other component)
  - "carry Pass-2's whole-text harmony blueprint into each chunk's generation as read-only shared context" (bc R4 — safe separate-call chunking presumes the before-bracket)
  - Meaning-gaps:
    - the parallel_mode choice (off / intra-chapter / full) vs cross-section terminology drift — high — 'full' parallelism risks the drift the design already flagged; wrong pick builds in a consistency bug
    - how separate-call chunking multiplies fixed-instruction reloads (cost + the lever-interaction) — mid — affects the cost model (~$10-20 one-shot baseline) and interacts with staging (R5)
    - the structural-default budget value per model — mid — stub from R1; a wrong default over- or under-chunks

### R4 — Chunking↔3-Pass co-design (the Pass-2 "before" bracket)
- **Goal:** make chunked generation *safe* for whole-span Tier-1/2 structure (havuz / ring / arc) — the whole-span-remainder half of the design
- **engagement-type:** CONSOLIDATE *(epistemic)*
- **Move:** design chunking's whole-text "before" bracket **together with** the un-wired 3-Pass, recognizing that the bracket *is* Pass-2 (the whole-text Harmony Map) — comprehension + Pass-2 map BEFORE → chunked generation consulting the blueprint slice MIDDLE
- **Lands:** a co-designed architecture where wiring the 3-Pass and turning on safe chunking share one whole-text-harmony component (Pass-2), rather than two bolted-on whole-text passes; the harmony FLOOR on the budget (a Tier-1 span that can't be fragmented) is structure-derived from the blueprint
- **Touches:** `harmony_layer.md` Pass-2 (the whole-text Harmony Map — the shared component) · the un-wired-3-Pass (00-24's fix — I7: C2 presumes it wired) · the harmony-floor-vs-adherence-ceiling budget negotiation (failure-mode-10, PARTIAL) · `chunking_mechanism_override: harmony-tier-aware`
- **WHY:** in *this* SKILL the only whole-text-harmony mechanism is Pass-2, so safe chunking's before-bracket and the 3-Pass fix are the *same component* — co-designing them (not bolting) is what lets the **end goal gain** chunked generation that doesn't shatter whole-span structure; that shared-component necessity is why it's `core`, phase-activated when the 3-Pass is wired (`@3-pass-wired`)
- **Priority:** MED   **Confidence:** MED   **Essentiality:** core · @3-pass-wired
- **Guidance Mode:** full
  - "treat 'entangled with 00-24' as *shares-a-component / co-design*, not logical necessity" (bc the critique downgraded the label — any whole-text harmony pass would formally do; it's *this SKILL's* Pass-2 that makes it concrete, not a manufactured unification)
  - "the before-pass is compact ANALYSIS (a blueprint), not a full translation — its whole-text load is read/analysis-load, distinct from generation/transformation-load" (bc that's why the bracket nets positive; but note the net-positive is *conditional* on generation being the dominant failure locus — R1 tests that)
  - Meaning-gaps:
    - carry-slice vs keep-whole for the blueprint into each chunk — high — failure-mode-10's open residual; a wrong choice either bloats each chunk (re-introducing load) or starves it of the whole-span context
    - how the harmony floor and the adherence ceiling negotiate one budget — mid — a very-long Tier-1 span + a very-small adherence budget is a genuine bounded trade with no free resolution
    - whether the before-pass net-positive holds if read-load (not generation-load) dominates — mid — chains to R1's variable-isolation

### R5 — Bounded-load sibling-principle with 04-12 staging
- **Goal:** sharpen the understanding the design rests on — how chunking relates to the staging lever, as a unifying frame
- **engagement-type:** CONSOLIDATE *(epistemic)*
- **Move:** aggregate this inquiry (chunk the *transformation* load) with 04-12 staging (stage the *fixed-instruction/rule* load) into a "bounded-load translation" two-lever frame — carrying the critique's **new** point that the levers *interact with tension*, not merely partition
- **Lands:** a stated (but modest, two-instance) design principle: adherence-load has ≥2 partitionable components with different levers — AND separate-call chunking (R3) *re-pays* the per-call instruction load that staging tries to cut, so the two levers pull against each other on cost/instruction-reloads
- **Touches:** 04-12 staging finding (the sibling lever + the caveat-audience lesson) · the fixed instruction stack (~80 principles + Tier 1-4 + 8 axes, reloaded per chunk) · the lever-interaction (chunking multiplies the reloads staging reduces)
- **WHY:** naming the two-lever frame + the interaction is what lets the **end goal gain** a non-double-counted picture of *why chunking alone isn't the whole adherence answer* — but the principle is thin at two instances (S5 was DEFERRED), so its line of sight to the goal is indirect: a later-phase consolidation nice-to-have, which is why it's `supporting` / LOW
- **Priority:** LOW   **Confidence:** LOW   **Essentiality:** supporting
- **Guidance Mode:** compact
  - "state it modestly as a partition-WITH-interaction observation, not a law; revive if a third lever appears" (bc two instances is over-generalization territory — the specific-vs-pattern humility the innovation already flagged)
  - Meaning-gaps:
    - whether the lever-interaction (reload-multiplication) is a real cost problem or marginal — mid — determines whether the frame is a genuine design constraint or just a tidy observation; needs R3's cost model
    - the third-lever question (is there a load component neither chunking nor staging touches?) — low — would move the frame from DEFERRED to live, but not needed for the current goal

### R6 — Whole-draft-check "after" bracket (01-09), 3-Pass-independent
- **Goal:** protect assembled-output fidelity across chunk seams — the back-end of the bracket architecture, available *without* the 3-Pass
- **engagement-type:** PURSUE-SEED *(teleological)*
- **Move:** develop the prior 01-09 whole-draft structural check as chunking's **post-assembly** bracket — run it over the *reassembled* translation to catch cross-chunk seams (escalation-chain / ring / havuz spanning boundaries)
- **Lands:** a whole-draft check that runs after chunk reassembly, catching cross-boundary structural breaks that per-chunk generation cannot see — and it works **regardless** of whether the 3-Pass is wired (unlike R4's before-bracket)
- **Touches:** the 01-09 config-independent whole-draft structural-fidelity check (the mechanical spine) · the reassembly step (where chunks rejoin) · the cross-chunk seam risk (Tier-1 spans split across boundaries)
- **WHY:** the after-bracket is the one piece of the whole-span architecture that is *not* gated on the un-wired 3-Pass, so the **end goal gains** a working back-stop for chunk-seam damage even in today's SKILL state; it's `supporting` because the goal's fidelity can land rougher without it (the before-bracket + boundary-snapping already prevent most breaks), but it meaningfully hardens the result
- **Priority:** MED   **Confidence:** MED   **Essentiality:** supporting
- **Guidance Mode:** compact
  - "pair it with R4's before-bracket but ship it independently — it needs no 3-Pass wiring" (bc that's its distinguishing value; the critique explicitly separated it from the deferred C2 core)
  - "target it at cross-boundary structures specifically, not a whole re-review" (bc the per-chunk generation already handles within-chunk fidelity; the seam is the new risk chunking introduces)
- **Depth-link:** none (not yet drilled)

---

## Excluded (candidates considered, not routed — with reasons)

- **"CONCLUDE must carry the 4-cluster Inherited Commitments Re-test (00-24 / 01-09 / 06-14 / 04-12)."** — This is a **process-control move** of the /traverse pipeline (a step of the CONCLUDE protocol), not a concept-direction in the territory. Routing it would be Process-coupling (LAYER 2, §4.3). The *concepts* those clusters point at are already routed (R4/R6/R1/R5); the re-test *obligation* belongs to CONCLUDE, not to the onward route-field.
- **The reach decision itself (evaluate-only → design → apply).** — A **selection / disposition** decision belonging to the user (NOT-list §1.3). Routelisting enumerates the field under whatever reach the user picks; it does not choose the reach. Recorded here as the standing gate in the Map Header, not as a route.
- **Re-derive the "how to chunk" mechanism (3-operation disaggregation, split-placement, granularity ladder, hybrid harmony-aware mechanism).** — Already comprehensively designed in the two 2026-06-14 findings; the inquiry's settled stance is REUSE, not re-derive. Engaging it advances nothing new toward the goal → not a route.
- **Re-derive the un-wired-3-Pass fix.** — That is 00-24's job; this inquiry only *depends on* it (R4 co-design). Re-opening it is out of scope for the chunking goal.

## Telemetry

- **Mode:** root / project-space (breadth) · **Entry point:** fresh (no prior `_route.md` for this inquiry)
- **Identities enumerated:** 6 live · **Excluded:** 4 (with reasons)
- **Routes by kind:** teleological 3 (R2 DEVELOP · R3 DEVELOP · R6 PURSUE-SEED) · epistemic 3 (R1 TEST · R4 CONSOLIDATE · R5 CONSOLIDATE)
- **High-priority count:** 1 (R1) · **Essential-count:** 3 core (R1 · R3 @engine-built · R4 @3-pass-wired; 2 phase-qualified)
- **Essentiality spread:** core 3 · supporting 3 · peripheral 0
- **Individuations made:** R2≠R3 (phase/mechanism/enforcement-strength split — the critique's load-bearing S3 reframe) · R4≠R6 (before-bracket 3-Pass-gated vs after-bracket 3-Pass-independent — different prior, different gating) · R4≠R5 (component-sharing-with-00-24 vs load-partition-siblings-with-04-12 — different relation-type). All lean-to-split.
- **Uncertain individuations:** R1 absorbed the variable-isolation + granularity-calibration + de-quarantine-evidence as facets rather than separate routes (they are the same experiment's design surface) — flagged as the one merge worth a consumer's review.
- **Stale entries:** none (fresh run).
- **Convergence:** reached — territory swept at identity resolution; a second sweep yielded no new identities.
- **Frontier flags:** none (the territory is a single finished inquiry, fully swept).
- **LAYER 1 checked:** no Over-merge (lean-to-split applied) · no Under-coverage (all 5 route-seeds + the derived R5/R6 covered) · no Wrong-grain (identities, not manifestations) · no Goal-loss (every route carries the gated evaluate→design→apply bias) · no Type-misassignment (each engagement-type partitions by kind) · no Index-drift (fresh).
- **LAYER 2 checked:** no Selection-creep (the reach + SKILL-edit decisions are Excluded as the user's; attributive Priority/Essentiality only) · no Process-coupling (the CONCLUDE re-test obligation is Excluded; no control-flow routes) · no Description-collapse (routes are prescriptive moves, not explanations) · no Manifestation-dump (compact identity-level map).
- **Self-assessment:** **FLAG** — the map is complete and swept at identity resolution, but two flags for the consumer: (i) the entire APPLY sub-field (R2/R3) is gated on the user's reach decision + authorization (nothing to run now without it), and (ii) R1 (the empirical validation) is `core` and its absence leaves the finding's magnitude-claim quarantined — the consumer should weigh running R1 before treating the design routes as grounded.
