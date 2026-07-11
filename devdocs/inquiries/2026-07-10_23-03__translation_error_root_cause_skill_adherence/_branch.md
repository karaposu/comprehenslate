# Branch: Translation Error Root Cause & SKILL Adherence

## Source Input

The user's raw request, preserved verbatim (also in `articulate_simple.md` `## User Input`):

```text
[Critique of the İKİNCİ HÜCCET-İ İMÂNİYE translation produced under A1=conversational, A2=lay, A3=outsider-to-acquainted, A4=casual, A5=lightly-domesticated, A6=standard, A7=standard, A8=none, governed by the SKILL folder.]

Seven named defects:
1. "allegorical" — too hard given A1=conversational; "obvious this word shouldn't be used."
2. "and set it out as an allegorical dialogue and an imagined debate, giving the mute tongue of a thing's own condition the form of actual speech" (from "basit avamın fehmine gelecek bir muhavere-i temsiliye ve bir münazara-i faraziye tarzında ve lisan-ı hali, lisan-ı kal suretinde söylemiştim") — "weird and wrong at the same time." lisan-i hal = language of body/state; lisan-i kal = language expressed with voice. Translation doesn't cover this, "makes things gibberish." [Also: "basit avamın fehmine gelecek" dropped entirely.]
3. "figure" — bad for "bir şahıs" (→ personage / entity / character).
4. "This imaginary figure wants to be Lord over some one thing among the beings of the world" — "some one thing among" reads badly.
5. "For there is such flawless order in our duties and our movements that no one lacking a boundless wisdom and an all-embracing knowledge can poke a finger into our work" — reads badly, hard to parse.
6. "work" — bad for "iş" in "sen benden iş bulamazsın"/"iş bulacağım" (iş = attention/care/foothold).
7. "secondary causes" — bad/over-interpreted for "esbab".

"lets dive deep into why this translation had these mistakes. was SKILL folder content followed well or not, what happened?? lets dive deep."
```

## Articulation Reference

- **File:** `articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** item-1 (root-cause diagnostic)
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**item-1 (literal):** *"Dive deep into why this translation had these mistakes. Was the SKILL folder content followed well or not — what happened?"*

The ask carries these identified ambiguities (preserved, not adjudicated):

- **MQ1 verdict-axis** — `[per-error-diagnosis / systemic-diagnosis / both]`; `[diagnosis-only / diagnosis+adherence-verdict / diagnosis+prevention / diagnosis+repair]`; and "was the SKILL followed" reads three ways: `[(a) was it READ / (b) was it correctly APPLIED per-principle / (c) is the SKILL itself DEFICIENT]`.
- **MQ3 intent-axis (WHAT)** — action-endpoint is open across `[understand-this-instance / prevent-recurrence / repair-the-SKILL]` and `[written diagnosis / changed process / changed SKILL files]`.

The seven defects are the diagnostic's evidence-set, spanning error-classes: **register-too-high** (1: "allegorical"), **omission** (2: dropped "basit avamın fehmine gelecek"), **term-mangled/unclear** (2: lisan-ı hal / lisan-ı kal), **flat-literal word-sense** (3: "figure"; 6: "work" for iş), **awkward target syntax** (4: "some one thing among"; 5: "no one lacking…can"), **over-interpretation** (7: "secondary causes" for esbab).

## Goal

- **Deliverable shape (Deconstruct):** a diagnostic *understanding* artifact — causal explanation (per-error + systemic) + an adherence verdict (read / applied / SKILL-deficient), with a prevention/repair proposal **gated by the OUTPUT-REACH axis**. Not a re-translation.
- **Bounds:** the 7 named errors × the SKILL folder's actual content × the translation *process* that was run.
- **WHY-axis motivations (preserved, not chosen):** `[operational: make the next chunk better / systemic: verify the SKILL-as-product is actually enforced / assurance: confirm the AI translates FROM the SKILL not from default-LLM habit / general-lesson: locate the declarative-knowledge → procedural-application gap]`.
- **Context the answer needs (MQ2):** check each error against the *specific* governing SKILL clause — A1=`conversational` vocab-exclusions & syntactic ceiling; no-smoothing / Tier-1 no-omission; the 5 always-on policies; the polysemy / local-construction memory; where `lisan-ı hal`/`kal` is documented. **Stance:** honest fault-finding, not self-justification.

## Considered Articulations

**Item item-1 — the root-cause diagnostic:**
1. **Per-error adherence diagnosis** — per defect, name the SKILL principle that should have caught it and why it didn't fire; classify read-but-not-applied / misapplied / silent.
2. **Systemic root-cause diagnosis** — one underlying process-failure (candidate: no post-draft verification pass against config register/syntax exclusions + no-omission) producing all 7; judge whether the SKILL *contains but fails to enforce* the antidotes.
3. **Diagnosis + prevention mechanism** — propose a concrete render-time/QA verification pass (register-exclusion, no-omission, word-sense-in-context, target-naturalness checks).
4. **Diagnosis + SKILL-repair proposal** — locate the enforcement gap in the SKILL files and propose self-enforcing edits.
5. **Adherence audit (verdict-first)** — verdict separating read / applied / SKILL-deficient, evidence per error, no repair beyond the verdict.

## Scope Check

**Question covers goal: YES**, with one preserved fork. The IN-scope core (per Deconstruct bounds) is the *diagnosis* + *adherence verdict*. The OUT-of-scope-for-now (per MQ4) is *re-translating the passage* and *re-litigating whether the defects are real*.

**The preserved fork (OUTPUT-REACH, from MQA reconcile):** how far past diagnosis the deliverable travels — pure understanding → reusable prevention mechanism → concrete SKILL/process repair. The pipeline should **span** this (produce the diagnosis, and carry the prevention/repair as clearly-labeled reach), not silently collapse to one end.

**Specific-vs-pattern:** the 7 errors are specific instances, but the user's "why… what happened" asks for the **broader pattern** they illustrate (the process/adherence failure mode). Default to the broader pattern while grounding every claim in the specific 7. Confirmed by MultiDepth's systemic + general-lesson motivations.
