---
status: active
model: claude-opus-4-8[1m]
effort: max
refines: devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md
---
# Finding: Semantic Priority Before Harmony Generation

## Changes from Prior

**Prior path:** devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md
**Revision trigger:** Stronger framing — the user proposed a deeper generative cause than the prior finding's "no post-draft checkpoint," and it holds up.

**What's preserved:** The prior finding's description of the failure is not wrong. The seven translation errors really are the signature of one fluency-first pass, and its proposed remedy (a post-draft verification check) survives intact — this finding relocates it, it does not discard it.

**What's changed:** The prior finding treated "the translation ran as one fluent motion with no post-draft checkpoint" as the root cause. This finding demotes that to a *symptom* of a deeper cause: the SKILL's translation workflow never runs the three-pass method its own reference file describes. The "no checkpoint" gap is now one of *two* missing gates, both downstream of that single cause.

**What's new:** The concrete fix — wire the existing three-pass method into the workflow as ordered steps, meaning-first — plus the finding that this one change delivers both the generation-time gate (missing from the prior finding) and the post-draft check (the prior finding's remedy).

**Migration:** The prior finding stands as historical record; its "no checkpoint" claim should be read as "one of two gates." See the Inherited Commitments Re-test section below for the per-commitment reconciliation.

## Question

This inquiry is a follow-up. A previous inquiry (the "translation error root cause" inquiry at `devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/`) diagnosed seven specific errors in a Turkish→English translation the comprehenslate SKILL produced. (The comprehenslate SKILL is the project's AI-translation instruction set, living at `SKILL/`, with reference files under `SKILL/references/`.) That prior inquiry concluded the errors came from running the SKILL as a single fluency-first pass with no checkpoint between draft and final output.

The user then asked a deeper question. Paraphrased: *the "harmony layer" is supposed to sit on top of an already-correct understanding of the meaning — it should only pick which of several semantically-valid phrasings best fits the desired style, never drive the translation itself. So how were these errors even possible? Maybe the SKILL is missing an explicit instruction: first comprehend and lock the meaning, then generate the translation under the nudge of the style configuration. Maybe that instruction wasn't obvious, so the harmony/style layer ended up doing the translation without semantic priority. How can this be fixed?*

("Harmony layer" refers to `SKILL/references/core/harmony_layer.md`, the reference file that governs how the translation preserves the source's structural and stylistic relationships — its rhythm, parallelism, sound-echoes, and so on.)

The goal was two things: (1) a diagnostic understanding — does a missing or unenforced "meaning-first" ordering actually explain the errors? — and (2) a fix design for how to make meaning-first ordering explicit and enforced. Not a re-translation.

## Finding Summary

- **The user's instinct is right, but the location of the problem is more precise than the user guessed.** Meaning *should* come first and it wasn't operative when the translation was generated — that part of the instinct holds. But the fix is not "add a missing instruction," because the instruction is not missing.

- **The meaning-first ordering is already stated in the SKILL — in at least three places — as a principle.** The harmony reference file's "Pass 1 — Meaning Lock" calls strict semantic fidelity "the foundation that cannot be violated." Its "Pass 3" says you may change *how* a meaning is expressed but never *what* meaning is expressed. A separate principles file states translation is "a two-step process: generate interpretation from deep comprehension first, then validate." So meaning-first is not absent as a **principle**.

- **What is missing is the ordering as an executed procedure.** The harmony reference file describes a three-pass method (Meaning Lock → Harmony Map → Target Reconstruction). But the SKILL's actual workflow file (`SKILL.md`), at its translate step (Step 5), never runs that method. It says "Then produce the translation. Apply:" followed by a flat list of things to apply all at once — and it pulls the harmony file in *only* for that file's "Tier 1-4 preservation policy" (a list of what to preserve), never for its three-pass method.

- **So the three-pass method is read but never executed.** The SKILL's own rules require reading all reference files before translating, so the method is in front of the model every time — it is simply never turned into ordered steps. It is present as description, absent as procedure.

- **This is why the errors are possible.** With no step that produces a locked-meaning foundation first, meaning and style get decided in one forward-generating motion — exactly the state in which a fluent-sounding word gets written, an awkward clause gets silently dropped, and the first/most-common sense of a word gets taken.

- **Relationship to the prior finding: this REFINES it (does not replace it), with an honest demotion.** The prior finding's "no post-draft checkpoint" is one of *two* gates the un-run method would have provided — a meaning-lock gate at generation time, and a check gate after drafting. Both are missing for the *same* single reason. The prior finding saw only the second gate.

- **The fix: make the workflow actually run the three-pass method, meaning-first.** Rewire `SKILL.md` Step 5 from its flat "apply everything at once" into the three ordered passes, and restructure the harmony file so its method and its preservation-policy are separable (so a future workflow can't import the policy while orphaning the method again). One wiring hosts both gates.

- **Two important design constraints, both grounded in the SKILL's own text.** (1) The meaning-lock foundation is *sentence-level* ("translate every sentence… the accurate but choppy version"); the SKILL explicitly forbids splitting sentences, so the fix must not chop below the sentence. (2) The meaning-lock pass should run without the style configuration in view, so style can't contaminate comprehension — and that "config-blindness" is only genuinely enforceable if the meaning-lock is produced as a real separate step, not merely narrated in one motion.

- **The reach is gated for the user to decide** (see Next Actions): diagnose-only, or diagnosis + fix-design, or diagnosis + actually editing the SKILL.

## Finding

### Why this inquiry exists

The prior inquiry had already answered "what went wrong" at one level: the translation was generated in a single fluent pass, and the SKILL had no step to catch the resulting errors. The user's follow-up pushed on a genuine tension in that answer. If the SKILL's design puts meaning first and treats the style/harmony layer as something that only operates on top of a settled meaning, then how did style/fluency end up driving the translation at all? Either the design doesn't actually say meaning comes first, or it says so but nothing makes it happen. Resolving that tension is what this inquiry did.

### What the SKILL actually says (the evidence)

The decisive facts are all in the SKILL's own files, quoted verbatim during the critique step.

The harmony reference file (`SKILL/references/core/harmony_layer.md`) opens by describing a method: *"The idea is to create a translation mode that works in three passes."* The three passes are:

1. **Pass 1 — Meaning Lock:** *"Translate every sentence with strict semantic fidelity. No meaning added, removed, or altered. This produces the 'accurate but choppy' version. This is the foundation that cannot be violated."*
2. **Pass 2 — Harmony Map:** analyze the original's inter-sentence relationships (sound-echoes, parallelism, rhythm, and so on) into a "harmony blueprint."
3. **Pass 3 — Target Language Reconstruction:** using that blueprint, adjust the Pass 1 translation with the target language's own tools — *"you may change HOW a meaning is expressed, but never WHAT meaning is expressed."*

So the meaning-first ordering is stated plainly. Pass 1 is the comprehend-and-lock phase; it is called the foundation that cannot be violated; Pass 3 explicitly operates on top of that locked meaning. A separate file, the translation principles (`SKILL/references/core/translation_principals.md`), says the same thing in different words: translation is *"a two-step process: generate interpretation from deep comprehension first, then validate against formal linguistic rules."*

Now the other half. The workflow that actually runs a translation is `SKILL.md`, and its translate step is Step 5. Step 5 says: *"Then produce the translation. Apply:"* — followed by a bulleted list (the user's chosen configuration, the default policies, the translation principles, the harmony file, and any project notes). Everything is applied at once, in one "produce the translation" instruction. There are no ordered passes and no gate between drafting and output.

And critically, the one line where Step 5 pulls in the harmony file reads: *"The harmony-layer Tier 1-4 preservation policy from `references/core/harmony_layer.md`."* It imports that file **only** as a preservation policy — a list of what to preserve and how strongly. It never names or invokes the three-pass method that sits at the top of the very same file.

### The mechanism: a method that is read but never executed

Here is the structural heart of the diagnosis. The harmony file plays *two roles at once*: it is both a **method** (the three-pass procedure) and a **policy** (the Tier 1-4 list of what to preserve). The workflow wires in only the policy. The method is left as orphaned prose.

It would be a mistake to say the model "never saw" the method. The SKILL's Rule 1 states: *"Always read all reference files before translating."* So the three-pass method is in the model's context on every run. It is not unseen — it is un-*proceduralized*. Nothing in the executed workflow turns it into ordered steps with a gate between them.

This is the precise sense in which the meaning-first ordering is **present as a principle but absent as a procedure**. The principle is stated (three times over). The procedure that would enforce it is described but never called. A described-but-uncalled procedure does not run on its own; it runs "in spirit," folded into whatever step *is* called — which here is the single "produce the translation" instruction.

And that single instruction is exactly the condition the prior inquiry identified: one forward-generating motion in which the model reaches for the next natural-sounding English phrase. In that state, a slightly literary word gets written because it feels natural; an awkward-to-carry clause gets smoothed away and quietly dropped; the first and most common sense of a word gets taken; a dense construction gets produced because it mirrors the source. The meaning-lock foundation that Pass 1 was supposed to build first is never built, so there is nothing holding the meaning fixed while the fluent phrasing is chosen.

### Was the user right? A graded verdict

The user proposed three things. Taken one at a time:

- *"Meaning should be locked first and it wasn't operative when the translation was generated."* **Correct.** This is the real cause, and it is deeper than "no post-draft checkpoint" — it explains why the generation produced the errors, not just why nothing caught them.

- *"Maybe the instructions are missing."* **Not quite.** The instruction (meaning-first) is present as a principle in at least three files. What is missing is its execution as a procedure. This distinction matters because it changes the fix from "author a new instruction" to "run the method you already have."

- *"Maybe the harmony layer, without semantic priority, did the translation."* **Right instinct, wrong location.** The harmony file does not grab priority over meaning — it emphatically declares itself subordinate to meaning (Pass 3: change *how*, never *what*; the Tier 1 preservation entries say meaning *is* carried by the harmony and must be preserved even at the cost of everything else). Harmony did not override semantics by design. What happened is that the layered procedure that would have enforced meaning-first was simply never run, so meaning and harmony were decided together in one motion.

That last point needs one honest addition, or it risks letting the SKILL off the hook. "Harmony is designed subordinate" is a true statement about the SKILL's *design intent*. But the SKILL's *executed behavior* did give fluency the wheel. So the accurate framing states both halves: **designed subordinate (intent, true) + executed as co-equal (because the passes were never run as steps).** This mirrors the prior inquiry's "co-equal blame" shape — here it is a SKILL deficiency (the SKILL never proceduralizes its own method) working together with an execution failure (the passes collapsed into one motion). Neither the SKILL's design nor the act of running it is blameless.

### The fix: run the three-pass method, meaning-first

The fix follows directly from the diagnosis. Because the method already exists and is already in context, the fix is *promotion* — turning described prose into an executed procedure — not authoring something new. It has two parts.

**Part 1 — Rewire `SKILL.md` Step 5.** Replace the flat "produce the translation. Apply: [everything at once]" with the three-pass method as an ordered spine:

- **Pass 1 (Meaning Lock)** produces an accurate-but-choppy translation that holds the meaning fixed. This is the "locked-meaning foundation" the rest builds on.
- **Pass 2 (Harmony Map)** identifies the source's structural/stylistic relationships over that locked meaning, without changing meaning.
- **Pass 3 (Target Reconstruction)** rebuilds fluent English under the style configuration and the Tier preservation policy, with the meaning held to the Pass 1 foundation — and this is where a post-draft check runs, comparing the fluent output back against the locked meaning to catch anything dropped or altered.

**Part 2 — Restructure the harmony file** so its **method** (the three passes) is separated from its **policy** (the Tier 1-4 list). Right now the two are fused in one file, which is exactly what let the workflow import one (the policy) while orphaning the other (the method). Separating them means a future workflow reference has to name which part it is pulling, so the method can't silently go un-run again. This part also involves rewriting the three-pass description from its current descriptive voice (*"The idea is to create a mode…"*) into imperative, gated steps — because a workflow that points at rationale-prose imports rationale, not instructions.

**Why one fix delivers both gates.** The prior inquiry's remedy was a post-draft verification check. That check needs something to check *against* — a reference for what the meaning is supposed to be. The Pass 1 locked-meaning foundation *is* that reference. So wiring in the three-pass method produces, from one change, both the generation-time gate the prior finding lacked (meaning is locked before fluent phrasing is chosen) and the after-drafting gate the prior finding wanted (the draft is compared back against the locked meaning). One architecture hosts two gates. They are not the same gate — one operates during generation, the other after drafting — but they share the single locked-meaning artifact, and they go missing together for the single reason that the method is never run.

### Two design constraints the fix must respect

Both come straight from the SKILL's own text, and both were sharpened during the critique step.

**Constraint 1 — the meaning-lock is sentence-level, and the fix must not chop below the sentence.** Pass 1 says *"translate every **sentence**,"* and the harmony file's hard constraints state: *"Splitting one sentence into two is forbidden… sentence boundaries are structural meaning."* An early version of the fix design described the locked-meaning foundation at "word/clause granularity" — that was an error, corrected here. The foundation is a sentence-level accurate-but-choppy translation. The *check* that runs against it can compare at the finer word/clause level (to catch a dropped clause), but the foundation itself keeps sentences whole. This also honors the prior inquiry's constraint that the successful harmony work happens *across* sentences, not by breaking them apart.

**Constraint 2 — the meaning-lock should run without the style configuration in view.** If Pass 1 can see the style settings (for example, "conversational register, lightly domesticated"), those settings can leak backward and bias what the model records as the meaning — reintroducing the exact disease. So Pass 1 should be "config-blind": lock the meaning first, let the style configuration enter only at Pass 3. The critique surfaced an important caveat here: config-blindness is only genuinely enforceable if Pass 1 is a *real* separate step (run where the configuration literally isn't present). If the three passes are merely narrated in one motion, "ignore the config for now" is as easy to skip as any other instruction — the same reason the three passes collapsed in the first place. This links the config-blindness question to an open empirical question (below) about whether the meaning-lock must be produced as a real intermediate artifact or can be a simulated in-one-pass sequence.

## Inherited Commitments Re-test

This finding refines the prior "translation error root cause" finding (`devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md`), which carries four load-bearing commitments. Each is re-tested below against this inquiry's evidence.

- **Commitment (a): "The seven errors = one fluency-first pass with no post-draft checkpoint."**
  - **Source:** prior finding, its diagnosis and Finding Summary.
  - **Re-test status:** RE-TESTED — commitment confirmed but frame revised.
  - **Evidence:** The description is accurate — `SKILL.md` Step 5 does collapse translating into one "produce the translation" instruction (verified verbatim), and the errors are the natural output of that single motion. But "no post-draft checkpoint" is not the root cause; it is one of two gates missing for a single deeper reason (the three-pass method is never run as steps). The frame shifts from "the cause is a missing check" to "a missing check is one symptom of a missing procedure."

- **Commitment (b): "Blame is co-equal — application-failure plus tool-deficiency."**
  - **Source:** prior finding, its adherence verdict.
  - **Re-test status:** RE-TESTED — commitment confirmed.
  - **Evidence:** The co-equal shape holds and in fact sharpens. On the tool side, the SKILL is deficient in a specific, newly-located way: it never proceduralizes its own three-pass method (`SKILL.md` Step 5 imports the harmony file only as a preservation policy). On the application side, the execution collapsed the passes into one motion even though the method was in context (Rule 1 forces reading it). Both are real; neither alone accounts for the errors.

- **Commitment (c): "The fix is a scoped post-draft verification pass."**
  - **Source:** prior finding, its Next Actions / prevention design.
  - **Re-test status:** RE-TESTED — commitment confirmed but frame revised.
  - **Evidence:** The post-draft check survives — but as *one component* of the three-pass wiring (it lives at Pass 3, comparing the fluent draft against the Pass 1 locked meaning), not as a standalone fix. This finding adds the gate the prior fix lacked: the generation-time meaning-lock. The prior fix caught errors after the fact; it did not prevent fluency-first generation. Wiring the whole method delivers both.

- **Commitment (d): "The SKILL's principles are dual-natured — un-fired at generation, with no backstop."**
  - **Source:** prior finding (critique-corrected in that inquiry from "verification-shaped" to "dual-shaped").
  - **Re-test status:** RE-TESTED — commitment confirmed.
  - **Evidence:** This inquiry locates *why* the principles went un-fired: they are stated (as principles) but the procedure that would fire them (the three-pass method) is never invoked by the workflow. The "dual-natured, no backstop" observation is the symptom; "the method is read but not proceduralized" is the mechanism underneath it.

None of the four commitments is dropped. Two are confirmed outright; two are confirmed with an explicit frame revision (the demotion of "no checkpoint" from cause to symptom). The refinement is genuine, not silent inheritance.

## Next Actions

The finding proposes a change to the SKILL, but how far to go is the user's call. The three reaches are: **diagnose-only** (stop here — the question is answered), **+ fix-design** (produce the concrete edit specification without applying it), or **+ apply** (actually edit `SKILL.md` and the harmony file). The MUST item below is the decision itself; the fix-implementation items are COULDs gated on that decision.

### MUST

- **What:** Decide the output reach — diagnose-only, or + fix-design, or + apply the SKILL edit.
  - **Who:** the user.
  - **Gate:** before any edit to `SKILL.md` or `harmony_layer.md` is made.
  - **Why:** the diagnosis (this finding) is complete and stands on its own; editing the SKILL is a larger, harder-to-reverse step that changes how every future translation runs. The user should authorize that scope explicitly rather than have it inferred.

### COULD

- **What:** Implement the three-pass wiring — rewire `SKILL.md` Step 5 into the ordered Meaning Lock → Harmony Map → Target Reconstruction spine, and split the harmony file's method from its Tier policy (rewriting the method into imperative steps).
  - **Who:** a SKILL-editing pass (human or AI).
  - **Gate:** condition-bound — after the user authorizes the "+ apply" reach.
  - **Why:** turns the diagnosed cause into a prevented one; delivers both the meaning-lock gate and the post-draft check from one change.
  - **Depends-on:** MUST item "decide the output reach." This COULD is GATED — do not act until the MUST resolves.

- **What:** Validate the fix by re-translating the same passage (the İKİNCİ HÜCCET chunk) under the same configuration but with the three-pass method wired in, and check whether the seven named errors recur.
  - **Who:** a translation-plus-comparison pass.
  - **Gate:** observable — after the wiring (the COULD above) exists.
  - **Why:** the fix's claim is unproven until run against the very passage that produced the errors; this is the direct test.
  - **Depends-on:** MUST item "decide the output reach." This COULD is GATED — do not act until the MUST resolves.

- **What:** Add a project memory capturing the general lesson — a SKILL can state a method as a principle yet never wire it into its executable workflow, and a described-but-uninvoked method runs "in spirit as one motion" and fails silently.
  - **Who:** the memory system.
  - **Gate:** none — this is adoption-ready now.
  - **Why:** the pattern generalizes past this one SKILL to any instruction set that is rich in principles but thin in procedure; capturing it enables catching the class earlier.
  - **Depends-on:** MUST item "decide the output reach." OVERRIDE: this COULD is adoption-ready despite the open MUST. Reason: the lesson is about spec-authoring in general and has standalone value regardless of whether this particular SKILL edit is applied.

### DEFERRED

- **What:** Resolve empirically whether the meaning-lock must be a *real* emitted intermediate (produced in a separate step/context) or can be a *simulated* in-one-pass sequence, by comparing matched test translations done both ways.
  - **Gate:** revival — when the fix is being implemented and the real-vs-simulated choice must be made concrete (it is the highest-uncertainty part of the design).
  - **Why (if revived):** the critique found config-blindness and rubber-stamp-resistance are both robust only in the real-intermediate variant; evidence would confirm the default rather than leaving it assumed.

## Reasoning

**Why this finding over the alternatives considered.**

The central fork was whether this inquiry **supersedes**, **refines**, or merely **complements** the prior finding. Supersede was rejected on evidence: a superseded finding's remedy does not survive, but the prior's post-draft check *does* survive (it becomes Pass 3's gate), and the prior's description of the failure is not false. Merely-complements was also rejected: that would treat the two as independent parallel causes, when in fact they share one cause (the un-run method) and the prior's cause is downstream of this one. Refines-with-demotion is the accurate relationship — same direction, deeper location, with the prior's "no checkpoint" explicitly re-scoped from root-cause to one-of-two-gates.

**Why the locus is "un-run procedure," not the two alternatives the user floated.** The critique stress-tested both. "Missing principle" was killed by the verbatim text: the meaning-first ordering is stated in at least three places. "Harmony given priority over semantics" was killed by the harmony file's own subordination language (Pass 3 changes *how* not *what*; Tier 1 says meaning *is* the thing being preserved). What remained was the procedure gap — the method is stated and even read, but never executed as steps.

**On the fix, the critique landed several genuine hits that shaped the final design** (rather than rubber-stamping it):

- The claim "one wiring delivers both gates" was softened to "one architecture *hosts* two distinct gates" — the two gates operate at different times (during generation, and after drafting) and the post-draft comparison is still real work, not free.
- The "real intermediate artifact" requirement was challenged with a sharp objection: won't the same fluency-biased model just write the locked-meaning foundation with the same bias, so Pass 3 faithfully reconstructs a *wrong* foundation? The defense held but narrowed the claim: producing a config-blind, deliberately-choppy, literal foundation puts generation in a mode where the specific seven errors (silent clause-drop, fluency-word capture, register-lift) are structurally *harder* — it *relocates* generation to an error-resistant mode; it does not *eliminate* mis-comprehension. And that narrowing is itself informative: because the meaning-lock gate is necessary-but-not-sufficient, the post-draft check gate is genuinely load-bearing rather than redundant. The objection that looked fatal actually vindicated the two-gate design.
- The "config-blind Pass 1" idea was found implementable but *coupled* to the real-vs-simulated question — robust only when Pass 1 runs where the configuration truly isn't present.
- A factual error was caught and corrected: the locked-meaning foundation is sentence-level (per the harmony file's "translate every sentence" and its ban on splitting sentences), not the "word/clause" granularity an earlier draft of the fix stated. The word/clause granularity belongs to the *check*, not to the foundation.

All of the surviving claims are grounded in verbatim quotes from `SKILL.md` (Step 5 line 73, the harmony-import line 78, Rule 1) and `harmony_layer.md` (the three-pass description, the "translate every sentence" foundation, the ban on splitting sentences, the "how not what" rule) — so the diagnosis rests on the SKILL's actual text, not on structural argument about what it "should" say.

## Open Questions

### Research Frontiers

- **Real intermediate artifact vs simulated sequence.** Whether the meaning-lock must be produced as a genuinely separate step (its own context, the configuration absent) or can be a simulated in-one-pass sequence is ultimately an empirical question. It needs matched test translations compared for the seven-error signature. There is no way to settle it by reasoning alone, because it turns on how reliably a single model can hold a self-imposed pass boundary — the very reliability the original failure calls into doubt.

### Refinement Triggers

- **If a prose-only ordering fails to fire.** If the fix is implemented by writing the ordered passes into `SKILL.md` as prose and a subsequent translation *still* collapses the passes into one motion (the seven-error signature recurs), that is the trigger to escalate — encode the ordering more forcibly (for example, a real emitted intermediate, or a stage field in the pipeline configuration) rather than relying on instruction-following.

- **If other reference files show the same pattern.** If a scan finds that other reference files besides the harmony file also contain methods the workflow imports only partially (as what-to-preserve content, never as executed steps), the fix generalizes beyond the three-pass method to a workflow-wide "proceduralize the methods you import" principle.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
But the SKILL's workflow file (SKILL.md) collapses the actual translating into a single instruction — "produce the translation." So the three passes ran in spirit, as one integrated motion, not as three distinct steps with a gate between draft and output. In a single fluent motion, the mind (or model) is generating forward — reaching for the next natural-sounding English phrase. That is exactly the state in which:

a slightly literary word ("allegorical," "mute tongue") feels natural and gets written;
a clause that is a little awkward to carry ("basit avamın fehmine gelecek") gets smoothed away and quietly dropped;
the first, most common sense of a word ("work" for iş) gets taken;
a faithful-but-dense construction ("no one lacking… can…") gets produced because it mirrors the source's shape.
Each of these is the natural output of fluency-first generation. And the SKILL predicted this: one of its own always-on policies is a no-smoothing rule that explicitly names "natural target-language fluency" as the bias to guard against. The SKILL knew this failure was coming. It just had no step that would catch it.

but how these are possible? harmony layer is sth that should work on top of the base accurate  semantic understanding and translation options and pick harmony config suitable one,  it shouldnt meddle with semantic correct understanding part directly,

maybe instructions are missing? it should be explicit that first comprehend the text understand the meaning, and then with the nudge  of harmonic  config given you must generate a trasnlation

maybe problem was this instruction was not obvious and harmony layer without semantic priority did translation ?

how this can be fixed?
```

</details>
