# Branch: translation error root causes

## Source Input

```text
hmm, why u made these errors u think?? what was missing in our process that these errors were made? i understand you are ai  but i am wondering what was missing, think really deep and try to uncover the most core issues...
```

**Context supplied with the invocation (the referent of "these errors"):** the assistant translated two ~1-page chunks of Said Nursî's ÜÇÜNCÜ HÜCCET-İ ÎMÂNİYE from an EPUB into English using the comprehenslate SKILL (`translation_method.md`'s 4 passes; `harmony_layer.md`'s tiers; `config_base_source.md`'s 8 axes; `schemas.py`'s policies). ~19 errors were found AFTER delivery, in three waves:

- **Wave 1** (assistant self-caught on a user-requested re-scan): dropped `içyüzü` that echoed across two sentences; invented a doubled verb; lost `dirilmek`'s "come back to life" sense; `bazı` → "other" (conflating with `sair`); added totalizer "never"; lost `zarurî` intensifier in an escalation; skipped HonorificsPolicy's transliterate-with-original for `Cenab-ı Hak`; `İslâm ordusu` → "the Muslim army".
- **Wave 2** (assistant self-caught on a second user-requested re-scan): wrong word-sense for `bitiyor`; silently normalized the source's own transliteration; flattened `kadîm` (beginningless) → "eternal"; dropped a 3× repetition of `dirhem`; dropped an explicit subject; rendered cognates `hâsiyet`/`hâssa` with different words; missed a two-sense pun on `eşeklik`.
- **Wave 3** (USER caught, assistant did not): (a) "a question that is really a denial" for `istifham-ı inkârî` — false English root-link with `münkir`/`mülhid`, object of denial unstated, sentence read as if the verse denies God (the exact inverse); (b) unresolvable pronoun — "it" pointing 20+ words back across an em-dash aside; the FIRST draft had it right, a later "tightening" revision broke it.

Notable: Pass 4 (whole-draft verification) was run and reported PASS. Only the sentence-boundary check had a mechanism (a script); the other three checks were prose-level and passed everything. Also: a stored memory (`feedback_translation_verification_pass.md`) already names this failure mode; `translation_method.md`'s own Enforcement note predicts it.

## Articulation Reference

- **File:** `devdocs/inquiries/2026-08-15_00-01__translation_error_root_causes/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** `[I1]`
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**Item I1 — Why were these errors made, and what was missing in our process that let them be made — thought about really deeply, to uncover the most core issues?**

Literal statement (from MultiDepth, near-verbatim):
> *"Why do you think you made these errors? What was missing in our process, that these errors were made? I understand you are AI — but I am wondering what was missing. Think really deep, and try to uncover the most core issues."*

The Question carries **three open verdict-axis ambiguities (MQ1)**:

1. *Kind of deliverable:* `[causal-diagnosis (name the mechanism) / process-gap-audit (enumerate gaps) / spec-change-proposal (what to add to the SKILL) / taxonomy-of-the-errors (classify, then derive causes) / single-root-cause-commitment (drive to ONE core issue) / epistemic-honesty-account (name the limit, propose nothing)]`.
2. *Scope of "our process":* `[the SKILL's written method only / the SKILL + the runner-engine layer that would enforce it / the SKILL + the human-AI working pattern in this session (who checks, when, how chunks were sized, how revisions were made) / all of the above as one system]`.
3. *Depth-target of "most core":* `[proximate causes (each error's local mechanism) / structural cause (one property of the method that generates the whole class) / meta-structural cause (why the method has that property — why the already-written fix didn't take)]`.

And **six open intent-axis ambiguities (MQ3)** about action-endpoint:

1. *Improve the SKILL* — get concrete spec changes that reduce recurrence.
2. *Calibrate trust* — learn what an assistant's own PASS verdict is worth.
3. *Decide the QA workflow* — work out who checks what, and when, going forward.
4. *Understand the failure shape* — satisfy an explanatory itch about mechanism, no action attached.
5. *Test whether the assistant can self-diagnose honestly* — see whether the account names a structural blind spot rather than promising more care.
6. *Locate the enforcement-layer decision* — surface whether an engine running passes as separate calls is now warranted.

The **MQA reconciliation** surfaces **three irreducible overlaps:**

- **Depth-target joint axis** (joint across MQ1's depth-target, MQ3's understand-vs-improve, MQ2's descriptive-vs-prescriptive stance): how far down must the answer go before it may stop, and does reaching bottom obligate a fix? "Most core" pushes downward without naming a floor.
- **Scope-of-"our-process" joint axis** (joint across MQ1's scope, MQ2's cause-kinds, MQ2's bounded-vs-generalisable stance): what is the boundary of the system under diagnosis? "Our" is load-bearing and unresolved — it may include the human-AI working pair, in which case the user's own QA role and the deliver-before-independent-read pattern are inside the frame.
- **Explanation-vs-remedy joint axis** (joint across MQ1's epistemic-honesty-account vs spec-change-proposal, MQ3's understand vs improve, MQ2's honest-about-limits vs solution-optimistic stance): whether the deliverable owes a remedy at all. Distinct from depth — one can go maximally deep and still decline to prescribe.

## Goal

For Item I1:

**Deliverable shape (from Deconstruct):**

- **deliverable:** a causal account of why the ~19 errors occurred, pitched at the depth "most core" demands — naming what the *process* lacked rather than what the *agent* lacked; shape depends on the depth-target and explanation-vs-remedy values (a single committed root cause, a layered cause-structure, a gap-audit, or an epistemic-limits account, possibly with spec-change implications attached).
- **kinds:** diagnostic analysis + (conditionally) error-class taxonomy + (conditionally) process-gap enumeration + (conditionally) proposed method/enforcement changes.
- **bounds:** the process that produced these translations — its written method, its enforcement (or absence), its verification vantage, and the human-AI working pattern around it.

**Motivations a good answer might serve (WHY-axis, from MultiDepth — preserved as ambiguities):**

- `[wanting-the-SKILL-to-actually-work]` — the SKILL is the user's own build; this error rate means it isn't yet doing its job.
- `[deciding-whether-to-build-the-engine]` — the method says passes are only physically enforced as separate calls, and that layer doesn't exist; is this the evidence that justifies building it?
- `[calibrating-how-much-to-trust-a-PASS-verdict]` — Pass 4 reported PASS on a draft with many errors.
- `[working-out-their-own-QA-role]` — the user caught exactly the two errors source-comparison structurally cannot catch.
- `[intellectual-curiosity-about-the-failure-mechanism]` — "i am wondering" reads as genuine curiosity, possibly action-free.
- `[testing-for-honest-self-diagnosis]` — will the account name a blind spot it cannot fix by effort?
- `[frustration-seeking-explanation-rather-than-apology]` — an implicit "this shouldn't have taken three passes to find."
- `[wanting-to-know-if-the-known-fix-failing-is-significant]` — a memory file and the spec both already named this mode; why didn't written knowledge prevent recurrence?

**Context the downstream consumers need (MQ2 — preserved as ambiguities):**

- *verdict (need-to-know facts):*
  - the actual text of `translation_method.md`'s Pass 4 and its Enforcement note — the note appears to predict this failure, changing whether this is discovery or a known-and-unfixed condition
  - the stored memory `feedback_translation_verification_pass.md`, a prior instance of the same diagnosis
  - whether the three waves are causally different classes or one class found at three depths of scrutiny
  - the user's own role — they ran the QA and caught precisely the errors source-comparison cannot catch
  - whether an engine/runner layer exists or is planned that could run passes as separate calls
  - which checks had mechanisms (the sentence-count script) vs which were prose — and that the mechanised one held
  - that error 19 was a *regression* introduced by a later revision — the revision loop has no re-verification
- *kinds (categories of cause available):* method-design (a missing pass; a pass with no mechanism) · enforcement (prose vs separate call; single context collapsing ordered passes) · epistemic (curse-of-knowledge; the translator cannot see what a source-blind reader cannot resolve) · trigger (no signal for polysemy, repetition, config-vs-constraint collision) · verification-vantage (verifier is the producing context) · workflow (chunk size; revision without re-check; delivery before independent read) · instrument (which checks got scripts) · attention (fluency masking fidelity).
- *stance (curation posture):* blame-free process-diagnosis vs candid account of model limits · single committed root cause vs ranked multi-cause · descriptive vs prescriptive · bounded-to-this-SKILL vs generalisable to any AI-executed method · honest-about-what-prose-cannot-fix vs solution-optimistic.

**Negative spec — what would explicitly fail (MQ4 exclusions):**

- `[agent-blame-as-explanation-OUT]` — "i understand you are ai" pre-empts "because I am an LLM" as a terminal answer; AI-ness is granted as premise, not accepted as diagnosis.
- `[shallow-or-surface-account-OUT]` — "think really deep", "most core issues" rule out a proximate-cause list that stops at the first layer.
- `[re-translating-the-passage-OUT]` — the ask is about process; corrections are already applied.
- `[re-litigating-individual-error-verdicts-OUT]` — the errors are given as established.
- `[apology-or-reassurance-OUT]` — the register is investigative, not a request for contrition or promises of care.

## Considered Articulations

**Item I1 — Why were these errors made, and what was missing in our process?**

1. **Single-root-cause commitment (verification-vantage).** "Drive the whole 19-error set to one structural cause: every verification pass in the method is source-anchored, and the verifier is the same context that produced the text — so the knowledge that enabled the translation is precisely the knowledge that made its failures invisible. Show how each error class falls out of that one property, and stop there."

2. **Instrument-audit: mechanised checks held, prose checks didn't.** "Diagnose by sorting the method's checks into those with a mechanism and those without. The one check with a script (sentence boundaries) held perfectly; every check left as prose (content dropped / invented / structure survived; the harmony tiers; the schema policies) passed everything including actual violations. The core issue is that the method states its checks at the right level but operationalises almost none of them."

3. **Error-class taxonomy driving a per-class gap.** "Classify the 19 into classes — omission, invention, word-sense, register/policy, echo-and-repetition, target-comprehensibility, regression — and for each class name the specific missing trigger or pass. The core issue emerges as a pattern across the classes rather than as one named cause."

4. **The enforcement gap: the spec predicted its own failure.** "Center the account on the fact that `translation_method.md`'s Enforcement note already says the passes collapse into one forward motion unless run as separate calls, and a stored memory already recorded this exact failure once before. The core issue is not that the process lacked knowledge but that the knowledge was written at a layer with no power to compel — so the diagnosis is about where enforcement has to live, not about what the method should say."

5. **The missing pass: no source-blind reader.** "Locate the gap at a specific absent pass. All four passes look at the source; none reads the English alone as a monolingual reader would. Wave 1 and 2 errors are source-comparison-detectable and were eventually caught; Wave 3 errors are only detectable without the source, which is why the user caught them and the assistant could not. The remedy is a fifth pass run source-blind."

6. **Whole-system account including the human-AI working pattern.** "Widen 'our process' to the working pair: chunk sizing, delivering before any independent read, revising without re-verifying (which introduced the pronoun regression), and the user occupying the only verification vantage the method lacks. The core issue is a division of labour that was never made explicit — the human was doing a structurally necessary job that the process never assigned to anyone."

## Scope Check

**Question covers goal.** The Question asks why the errors were made and what the process lacked; the Goal specifies the deliverable shape (causal account, sectioning conditional on the open axes), the motivations a good answer serves (SKILL-improvement / engine-decision / trust-calibration / QA-role / curiosity / honest-self-diagnosis / explanation-not-apology / known-fix-failing), the cause-categories available, and the exclusions (no agent-blame, no surface account, no re-translation, no re-litigating verdicts, no apology). All Goal facets are inflected aspects of the same diagnostic question.

**Specific-vs-pattern check:** the Question points at ~19 specific errors from two specific chunks. Per the default, the inquiry should address the **BROADER PATTERN** these errors illustrate — the properties of the process that generate errors of these kinds — rather than only these 19 instances. The 19 are evidence, not the subject. Both readings are live, however: a purely instance-bound reading ("what specifically went wrong on these 19") is coherent and cheaper. The pipeline should operate over the broader-pattern reading while keeping the instances as the grounding evidence, since the user's "most core issues" language points past the instances.

**Note on the reflexive risk:** this inquiry diagnoses a process failure using a process of the same family (a written, model-executed, model-verified method). Whatever verification-vantage limitation is found in the translation method plausibly applies to this diagnosis too. Downstream disciplines — Sensemaking's Self-Reference Blindness check and Critique's Self-Reference Collapse mode — should treat that as live rather than incidental.

## Layer Commitment

**Required** — the Question targets a discipline/framework artifact (the comprehenslate SKILL's `translation_method.md` and its verification architecture) for diagnosis that may entail redefinition, and MQ1's ambiguities include `spec-change-proposal`.

**Primary layer declared: PROCESS.**

The question is "what was missing in our process" — it adjudicates the *steps the method runs*: which passes exist, in what order, with what enforcement, run by which vantage, with what triggers firing. The named candidate causes (a missing pass, a pass with no mechanism, prose-vs-separate-call enforcement, revision without re-verification) are all process-layer objects.

Other layers considered and out of scope for THIS run:

- **Meaning** — what translation-verification *is* as a cognitive operation. Out: the user is not asking what verification means; they are asking why the verification that exists did not fire.
- **Structural** — what the SKILL's spec files should *look like* (sections, file organisation, schema shape). Out: reorganising the documents does not address a failure that the documents already correctly describe. If the diagnosis lands on enforcement, a structural follow-up may be warranted — that is a subsequent inquiry, not this one.

**Sequential plan if multiple layers prove necessary:** Process first (this run — locate the missing/unenforced step). If the finding commits a new pass or a new enforcement site, a Structural follow-up would specify where it lives in the spec files and how it is invoked. Meaning-layer work is not anticipated.

## Synthesis Trigger

**Omitted** — this inquiry does not consolidate two or more prior *inquiry outputs* (findings/specs/drafts) into a single output. Its substrate is the SKILL's reference files, two translation artifacts, and this session's working record — evidence, not prior findings carrying commitments to inherit.

Two stored memories are nonetheless load-bearing context and should be treated as prior-art the diagnosis must engage rather than re-derive:

- `feedback_translation_verification_pass.md` — already names "one fluent pass leaves the SKILL's principles un-fired" and locates the root cause in the 3-Pass method going un-run. That this diagnosis existed and did not prevent recurrence is itself primary evidence for the depth-target question.
- `project_skill_design_discipline.md` — already commits an enforcement gradient: "one-run prose instruction = weak probability-raiser the model can ignore; separate call/pass = real enforcer (engine-only)." This is the exact distinction the instrument-audit and enforcement-gap articulations turn on.

Sensemaking and Critique should test these against the current evidence rather than assume them.
