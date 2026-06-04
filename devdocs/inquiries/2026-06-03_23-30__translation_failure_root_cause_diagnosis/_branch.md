# Branch: translation_failure_root_cause_diagnosis

## Question

- **Subject** — the observed translation failures in `mytrasnlations/5th_word/eng.md` (register pull-up across at least 8 lexical items: corvée, cauldron, morsel, parable, mess-tin/scrubs, Padishah, wave-tossed, wayward; plus polysemy mis-resolution on *nefer*), assessed against the three framework documents that were loaded and consulted (`advanced_principles.md`, `notes.md`, `harmony_layer.md`) and the AI translation behavior that produced them.
- **Action** — diagnose (root-cause analysis); distinguish the actual causal contributor(s) from the non-causes among three user-offered hypotheses and any others that emerge.
- **Level** — cross-cutting: artifact layer (the three docs), process layer (the AI translation step), meta layer (the failure-mode catalog or its absence). Each hypothesis lives at a different level.
- **Observation targets** — preserving all three user-offered hypotheses as separate items:
  1. **What is/was wrong with the docs themselves?** Specifically: did `advanced_principles.md`, `notes.md`, and `harmony_layer.md` fail to contain the guidance that would have prevented the register pull-up and polysemy failures? If so, what is missing or mis-framed in them?
  2. **Was the cause an AI translation issue — specifically bulk-translation behavior across "all pages at once"?** The user notes the text is short (not 20 pages), which is evidence against this hypothesis; weigh that evidence.
  3. **Was the cause the lack of explicit failure modes in the framework?** The user raises a sub-question: do the principles and translation logic already in the docs implicitly count as failure modes, or is there a meaningful distinction between "stated principles" and "stated failure modes" that the framework is missing?
- **Deliverable shape** — a diagnosis that (a) tests each of the three offered hypotheses against the actual evidence, (b) ranks them by causal contribution, (c) names any additional cause not in the offered three, and (d) recommends what specifically to change and *where* (docs / process / failure-mode catalog / framing).

Then: what is the actual root cause of the translation failures (register pull-up across 8+ words; *nefer* polysemy mis-resolution) that occurred despite the comprehenslate framework documents being loaded and consulted — is the fault in the documents themselves, in AI bulk-translation behavior, in the absence of an explicit failure-mode catalog, or somewhere else?

## Goal

- **Criterion** — precision (correctly identify the cause, not a plausible-sounding wrong cause); honesty (do not deflect to "AI limitation" if the docs were actually deficient, and do not blame the docs if the issue was process-shaped); actionability (the answer must tell the user *what to change* and *where*).
- **Use case** — improve the comprehenslate framework so that future translations don't repeat the register pull-up and polysemy failures. The user is treating this failure as a diagnostic instrument for fixing the system, not as a one-off bug.
- **Desired outcome** — knowing the *layer* where the fix belongs (docs / process / catalog / framing), the *specific change* required at that layer, and the *causal chain* that produced the failure so future symptoms can be traced.
- **What would fail** — vague generalities ("be more careful"); blame-deflection ("AI models do that"); diagnosing the wrong layer (e.g., saying "add more principles" when the actual issue is process or framing); failing to distinguish among the three offered hypotheses; treating the failure as isolated rather than as evidence of a systemic gap.

## Source Input

```text
read this , and tried to understand what was wrong with  advanced_principles.md notes.md and harmony_layer.md 

or it was ai translation issue, maybe because it was a bulk translation all pages? (but there are not so much text, not like 20 pages...)

or it was lack of failure modes? but we have principles and how tranlation shold be logic ,they dont count as failure modes?
```

Context preserved: the user is referring to the prior diagnostic exchange in this conversation where I (the AI) admitted to:
- Register pull-up: corvée, cauldron, morsel, parable, scrubs-the-mess-tin (round 1); Padishah, wave-tossed, wayward (round 2).
- Polysemy mis-resolution: translating *nefer* as "foot-soldier" when the construction required the general sense "one individual of [the species]."

Two feedback memories were saved: `feedback_translation_register.md` and `feedback_translation_polysemy.md`.

## Scope Check

Question covers goal. The question asks "what is the root cause" and the goal asks "knowing what to fix and where" — these are dual sides of root-cause diagnosis.

Specific-vs-pattern check: the user's flagged words (corvée, Padishah, etc.) are specific examples of the failure. The question is about the BROADER PATTERN those examples illustrate (why the framework didn't prevent that class of failure), not just about those specific words. Default applies: address the broader pattern.

Multi-hypothesis preservation: the user offered three competing hypotheses joined by "or." All three must be tested separately, not compressed into one general diagnosis. Each is preserved as a separate observation target above.

## Territory boundary (for Surfacing)

This inquiry's bounded territory:

- `/Users/ns/Desktop/projects/comprehenslate/advanced_principles.md`
- `/Users/ns/Desktop/projects/comprehenslate/notes.md`
- `/Users/ns/Desktop/projects/comprehenslate/harmony_layer.md`
- `/Users/ns/Desktop/projects/comprehenslate/mytrasnlations/5th_word/org.md` (Turkish source)
- `/Users/ns/Desktop/projects/comprehenslate/mytrasnlations/5th_word/eng.md` (failed translation, including its translator's harmony report)
- The prior diagnostic exchanges in this conversation (the user's flagged words; the AI's admitted failure analyses)
- The saved feedback memories: `feedback_translation_register.md`, `feedback_translation_polysemy.md` (these are *consequences* of the failure, not part of the territory under diagnosis — but they document what the AI extracted as the lesson, which is itself evidence)

Out of scope: the broader Risale-i Nur translation tradition; other translation theory literature; other inquiries.
