---
status: active
model: claude-opus-4-8[1m]
effort: max
refines: devdocs/inquiries/2026-07-11_04-48__mandatory_chunking_char_limit_adherence/finding.md
---
# Finding: Character/Word Count vs Structural Units as the Chunking-Budget Unit

## Changes from Prior

**Prior path:** devdocs/inquiries/2026-07-11_04-48__mandatory_chunking_char_limit_adherence/finding.md (the immediately-prior inquiry, which recommended "chunk by structure, not by a number" and quarantined the ~3,500 figure as having zero empirical support).

**Revision trigger:** User correction plus new evidence. The user disputed the "chunk by structure" recommendation and supplied the empirical provenance the prior finding said was missing (a real successful translation at ~3,500-character scale versus a real failed one at a much larger scale).

**What's preserved:** The prior finding's core structural insight survives intact — chunks must snap to "harmony boundaries" (the whole-passage structures a faithful translation must not break across a cut). Also preserved: the honest recognition that the failure's underlying cause is not cleanly established by the available evidence.

**What's changed:** The prior finding made *structure* the primary thing you chunk by ("chunk by structure, not by a number"). This finding flips the primary/secondary roles: the size **target** is a stable-unit number (characters), and **structure** is where the cut lands (the snap). This is not a reversal of the prior finding so much as a correction that brings its recommendation *prose* back in line with the mechanism the project's own configuration already encoded (a size budget that snaps to a boundary).

**What's new:** (1) a defined unit for the previously-unit-less budget (source characters); (2) real provenance for the ~3,500 figure; (3) a precise account of exactly how much that provenance is worth — which turns out to be less than it first appears; (4) the term "comprehenslation integrity" defined; (5) the recognition that the failure's cause is confounded at least three ways, not two.

**Migration:** No artifact changes ship from this inquiry. The reach is gated — this is a deepen-the-understanding inquiry, and no edit to the translation SKILL happens without explicit user authorization.

---

## Question

The user is building **comprehenslate**, a general-purpose AI translation SKILL (a structured instruction-set that guides a language model through a faithful translation), calibrated on a difficult Turkish source corpus. A recurring problem is that when the model is handed too large a passage at once, translation quality collapses. The immediately-prior inquiry recommended breaking the work into chunks defined by *structure* (translate a section, a paragraph, a self-contained passage) rather than by a character count, and it dismissed the user's proposed ~3,500-character limit as having no empirical basis.

The user pushed back, and this inquiry follows that push-back to the ground. The question has four parts:

1. Is a **character (or word) count** genuinely a better unit for the chunk-size budget than a **structural level** (section / paragraph), given that structural levels vary wildly in size — a paragraph can be 2 sentences or 30?
2. What do the two real translation examples the user cites — one successful at roughly 3,500 characters, one failed at a much larger size — **actually establish** about a ~3,500-character budget?
3. Which specific measure is best: **characters, words, or tokens** (the sub-word units a model actually processes)?
4. What is **"comprehenslation integrity"**, a term the user coined in the same message?

The goal is to deepen the understanding — to get the reasoning right — not necessarily to build anything yet.

## Finding Summary

- **The headline: "characters versus structure" is a false either-or.** The two are not rivals. A size budget sets the *target size* of a chunk; structure sets *where the cut actually lands*. The project's configuration already composes both (a size field, a separate structural-granularity field, and a "fixed-budget-with-snap" mechanism that means exactly "aim for a size, then snap the cut to the nearest safe boundary"). So the user is not choosing between two options; both already belong in the design.

- **The user's real, valid point is narrower and correct:** a structural *level* is too size-variable to be a reliable size *target*. Because one paragraph can be 15 times longer than another, "translate one paragraph" is not a dependable way to control how much the model must hold at once. A stable unit (characters) must be the target; structure stays the snap.

- **The measure verdict:** count **characters** for the human-facing budget (stable, legible, works across languages). **Tokens** (the sub-word units the model truly processes) are the more accurate measure of the model's load, but they are opaque to a human and asymmetric between Turkish and English — reserve them for the engine's internal use later. **Words** are the weakest choice (Turkish agglutination makes a "word" wildly variable). Count the **source** side (what the model reads), not the output.

- **The ~3,500 figure now has real provenance, which lifts the prior finding's "zero evidence" dismissal — but only partway, and only on one of two distinct claims.** It is the size of one genuinely successful translation's source (measured at 4,345 characters; the user's 3,500 sits about 24% below it). That is real, so "zero empirical evidence" was too strong.

- **But the lift is scoped precisely.** The evidence lifts the quarantine on the **intervention** ("adopting a size budget is a warranted, cheap bet") — weakly. It does **not** lift the quarantine on the **mechanism** ("length is what *causes* the failure"). Whether size causes the failure stays fully unresolved, because the one success and one failure differ in many ways besides length.

- **The failure's cause is confounded at least three ways,** not two: pure length-overload, an un-wired translation *method* (a known separate problem — the SKILL's careful multi-pass procedure is not actually wired into the instructions), and **local capability** (the model simply cannot render certain Turkish idioms, regardless of chunk size). The documented errors in the failed translation point mostly at the method and at local capability — not distinctively at length.

- **The char-budget survives anyway, because it is "confound-robust" — but in a *scoped* sense.** A smaller chunk helps any *load-sensitive* failure regardless of which mechanism dominates (a shorter passage is easier to hold a method over). It does **not** help errors that are purely local (a mistranslated idiom occurs in a 500-character chunk just as readily as in a 5,000-character one). So the budget is a cheap net-positive bet, but its reach is bounded — it buys down the load-driven share of failures, not all of them.

- **A deeper open question surfaced:** the char-budget might be a **temporary crutch** (needed only because the SKILL's method is currently un-wired — fix the method and large chunks might succeed again) or a **permanent safeguard** (load degrades quality even with a perfect method). This is genuinely undecidable today but empirically decidable later: wire the method, then re-test large chunks.

- **"Comprehenslation integrity"** (the user's coinage) = the unified outcome the whole SKILL protects: the source both *comprehended* and *faithfully rendered*, held together under load. It is broader than the existing "Tier-1/2 preservation" idea (which is one component) and names the thing that collapses when a translation fails.

## Finding

### Why this came up

The practical worry is simple and real: hand the model too much at once and the translation degrades. The prior inquiry's fix was to chunk the work by structural units and to reject the user's ~3,500-character number as unsupported. This inquiry re-examines both moves against the actual translation files and the project's actual configuration, and it lands somewhere more precise than either "structure is right" or "the number is proven."

### 1. The dispute dissolves — a size budget and structural snapping are not rivals

The framing "should we chunk by characters *or* by structure?" presupposes the two are competing answers to one question. They are not. They answer two different questions:

- **How big should a chunk be?** — that is the *budget*, and it needs a stable unit.
- **Where exactly should the cut fall?** — that is the *snap*, and it must land on a structural boundary so that a whole-passage structure (an argument, a metaphor that runs across sentences — what the project calls a "harmony boundary") is never sliced in half.

The project's own configuration already carries both as separate things: a size field, a separate structural-granularity field, and a mechanism option literally named "fixed-budget-with-snap" — which means *aim for a target size, then move the cut to the nearest safe structural boundary*. The prior finding even described this ("chunk by structure, snapping to harmony boundaries") — but then its headline prose, "chunk by structure, not by a number," contradicted the very mechanism it rested on. So the correction here is partly just realigning the recommendation's words to the design that already existed.

### 2. The user's valid, narrower point

Stripped of the false either-or, what the user is actually right about is this: a structural *level* is a bad *size target*. A paragraph can be 2 sentences or 30; a section likewise. Empirically the variation is on the order of 15-fold. So "translate one paragraph at a time" does not reliably control how much the model must hold — some paragraphs are perfectly safe, others are as overloaded as the whole failed document. A **stable unit** (a character count) is what gives a dependable target. Structure does not disappear — it remains exactly where the cut snaps to. The user's instinct is sound; only the "characters *replace* structure" framing needed correcting to "characters set the target, structure sets the cut."

### 3. The measure — characters, not words, with tokens held in reserve

Three candidate units, judged on how stably they track the model's actual processing load across different texts and across the Turkish-to-English asymmetry:

- **Characters** — the best *human-facing* choice. Stable, legible, trivial to count, and reasonably consistent across texts. This is what a budget stated in the SKILL and in the configuration should use.
- **Tokens** (the sub-word fragments a model actually reads) — the *truest* measure of the model's load, but opaque to a human author and asymmetric between languages (the same meaning is a different token count in Turkish versus English). Reserve tokens for the engine's internal accounting later, not for the human-facing budget.
- **Words** — the weakest. Turkish is agglutinative (it packs what English needs several words for into one long inflected word), so a "word" is a wildly variable amount of content. Rejected.

Count the **source** side — the Turkish the model reads — because that is the control point that exists *before* generation and that stands in for the whole working-set the model must hold. (The output side is discussed in section 7.)

### 4. What the two examples actually establish — and what they do not

The measured reality of the files:

- **The successful translation** (`4_mesele`): source 4,345 characters, output 7,080 (an expansion of 1.63×). The user judged it good.
- **A second small translation** (`5th_word`): source 4,148 characters, output 6,164 (1.49×). No stated judgment — so it is a *candidate* second success, not a confirmed one.
- **The failed translation** (`ikinci_huccet`): output 28,330 characters; **its source file is absent**. The user's remembered "~11,000 characters" most likely refers to that missing source. Notably, the output is 2.57× the (missing) source if the ~11,000 figure is right — a far larger expansion than the healthy 1.5–1.6× of the good examples, which is itself a symptom of a translation going wrong (padding, over-elaboration).

From these points, here is the honest accounting of what is and is not established:

- **Established — an existence proof:** a large translation failed and small ones succeeded. Size and success are correlated in the data.
- **Established — a direction:** bigger is, on this evidence, more likely to fail.
- **Established — real provenance for ~3,500:** the number is not invented. It is a conservative choice sitting just below the one genuinely-demonstrated-safe source size (4,345). This directly refutes the prior finding's "zero empirical evidence."
- **NOT established — a validated threshold:** no failure was ever observed *near* 3,500, so nothing locates a cliff there. 3,500 is simply "below the one size we know worked," not "the point where failure begins."
- **NOT established — the mechanism:** whether *length itself* caused the failure is unresolved, and cannot be resolved by these points alone (see section 5).

### 5. The confound is three-way, and the char-budget's robustness is scoped

This is the most important — and the most easily over-claimed — part of the finding.

The failed translation comes with a failure log (`mistakes.md`). Its documented errors are: a **register** violation (using a hard word the configuration forbids), several **word-sense** errors (a Turkish idiom, *lisan-ı hal / lisan-ı kal*, collapsed into gibberish; other words mistranslated by picking the wrong sense), and **fluency** problems. Crucially, these are *not* distinctively "the model ran out of room and skipped instructions" errors. They are the same class of error a separate prior inquiry attributed to the SKILL's careful multi-pass translation method not actually being wired into the instructions (the "un-wired method" problem). So the data cannot tell apart:

- **length-overload** (the chunk was too big to hold), from
- **un-wired method** (the procedure that would have caught these errors never fired), from
- **local capability** (the model genuinely cannot render *lisan-ı hal*, and no chunk size changes that).

That is a **three-way** confound. The prior framing considered only the first two; reading the actual errors surfaces the third. And the third matters because it is *chunk-invariant* — shrinking the chunk does nothing for an idiom the model simply doesn't know.

So why keep the char-budget at all? Because of a property worth stating carefully: **it helps regardless of which of the load-sensitive mechanisms is the true cause.** A smaller chunk is easier to hold a method over — so whether the failure is raw overload *or* a method straining for room, a smaller chunk improves the odds. The clinching observation: the short `4_mesele` succeeded *despite* the un-wired method. That is real evidence that small size is protective.

But this robustness is **scoped, not total.** It covers the *load-sensitive* share of failures. It does **not** cover the genuinely local, competence-limited errors — those occur at any chunk size. The earlier internal framing ("a smaller chunk lets *any* method survive") over-reached; the honest form is "a smaller chunk gives any *load-sensitive* failure more room to survive, and may do nothing for purely local errors — and which errors are which is itself confounded." The budget remains a cheap, net-positive bet; its reach is simply bounded.

**The precise consequence for the prior finding's quarantine.** The prior inquiry quarantined the number as unproven. This inquiry lifts that quarantine **only on the intervention** ("adopt a size budget" — warranted, weakly) and **not on the mechanism** ("length causes failure" — still fully unresolved). The provenance establishes that 3,500 is a *real successful size*, not that 3,500 is a *threshold* or that *size is the cause*. Any statement that the evidence "partially lifts the quarantine" must carry that split, or it silently borrows evidence about the method to underwrite a claim about length.

### 6. The number itself — a band, not a cliff

Given all of the above, the defensible statement about the number is deliberately modest:

- For the current top-tier model (Opus 4.8), a conservative **source-character budget in the ~3,500–4,000 range** is sound. The user's 3,500 is a reasonable conservative floor — it sits below the single demonstrated-safe size (4,345).
- It should be held as a **band**, not a precise cliff: a floor around 3,500, a demonstrated-safe point at 4,345, and genuinely unknown territory above that until data fills it in. There is no basis for a sharper number, and it should not be dressed up as a computed "safety factor" — that would imply we know where the failure boundary sits, which we do not.
- "Lower for smaller models" is correct and is best expressed as a **fraction of that model's own demonstrated-safe size**, calibrated upward as evidence arrives — not as a fixed absolute.

### 7. The output side — a symptom to watch, not a limit to set

The failed translation's over-expansion (2.57× versus the healthy ~1.5–1.6×) is a real signal. But you cannot *budget* the output the way you budget the source: the output is *generated*, not an input you hand in. Trying to cap it is a category error. The right use of the signal is detection, not control: an **expansion-ratio watch** — if a chunk's output runs materially above the healthy band, flag it for review, because the model is probably already padding or failing. This is a cheap tripwire that should feed the existing whole-draft quality check rather than stand as its own gate (that check already inspects the produced translation's content and would catch a bad one anyway). The ">2×" figure is one data point — treat it as "notably above the healthy band," not a hard constant.

### 8. "Comprehenslation integrity" defined

The user's coined term names the thing all of this protects. **Comprehenslation integrity is the unified outcome of the source being both fully *comprehended* and faithfully *rendered* — held together under load.** It is degraded whenever any translation principle drops out (register, word-sense, harmony, fidelity), whether that drop comes from load or from the un-wired method. It is *broader* than the project's existing "Tier-1/2 preservation" idea (preserving the most important whole-passage structures), which is one component of it, and it is the positive counterpart to the "collapse-in-one-motion" failure mode (the whole translation degrading at once). It is a useful umbrella term — it names what is at stake — not a rename of anything that already existed.

### 9. What this means for the SKILL (gated)

The intervention that survives is: **adopt a source-character budget (~3,500–4,000 for the top model, per-model as a fraction) that snaps to a harmony boundary, reusing the configuration's existing "fixed-budget-with-snap" mechanism.** It is cheap, net-positive, and confound-robust in the scoped sense above.

Realizing it has a known shape (from the prior inquiries): a model-facing instruction *now* ("translate in source-chunks of ~N characters, snapping to the nearest boundary") is a weak, one-run nudge the model can ignore — the *real* enforcement is the engine actually performing the chunking. Typing the currently-unit-less configuration field as source-characters is worth doing (it prevents exactly the character-versus-token-versus-structure confusion this inquiry had to untangle), but it is documentation, not enforcement — it changes nothing at runtime until the engine is wired. All of this is **gated**: no SKILL edit ships without explicit user authorization.

## Inherited Commitments Re-test

This inquiry declared a Synthesis Trigger — it consumes and re-tests commitments from three prior inquiries. Each is re-tested below.

- **Commitment:** "Chunk by structure, not by a number."
  **Source:** devdocs/inquiries/2026-07-11_04-48__mandatory_chunking_char_limit_adherence/finding.md
  **Re-test status:** RE-TESTED — commitment confirmed but frame revised.
  **Evidence:** Structure survives as the *snap* (the cut must land on a harmony boundary — unchanged). But the *primary* role flips: the size target must be a stable unit, not a structural level, because structural levels vary ~15× in size and cannot serve as a reliable target. The prior finding's own configuration ("fixed-budget-with-snap") already encoded budget-primary/snap-secondary, so the prior *prose* was inconsistent with its *mechanism*; this is the correction.

- **Commitment:** "~3,500 is reasoned-not-measured, with zero empirical evidence" (the quarantine).
  **Source:** devdocs/inquiries/2026-07-11_04-48 finding.md.
  **Re-test status:** RE-TESTED — commitment confirmed but frame revised.
  **Evidence:** "Zero evidence" is now too strong — 3,500 has real provenance (it sits just below the measured 4,345-character source of a genuine success). But the lift is only on the *intervention-warrant*, and only weakly; the *length-as-cause mechanism* stays fully quarantined (the one success and one failure differ in many ways besides size, and the failure's errors point at method and local-capability, not distinctively at length). So the quarantine largely stands, re-scoped: lifted on "a budget helps," intact on "length causes the failure."

- **Commitment:** "Chunking and the SKILL's translation method are complementary, not rival explanations of failure."
  **Source:** devdocs/inquiries/2026-07-11_00-24 (the inquiry that diagnosed the un-wired multi-pass method as the root cause of the error pattern).
  **Re-test status:** RE-TESTED — commitment confirmed.
  **Evidence:** The scoped confound-robustness re-confirms complementarity: a smaller chunk helps whether the failure is load or a method needing room, and the short success *despite* the un-wired method shows the two act as independent protective factors. New nuance: whether the char-budget remains necessary *after* the method is wired is now an explicit open question (see Open Questions), which re-tests — without overturning — the independence of the two levers.

- **Commitment:** The chunking design's "granularity ladder" (sentence → paragraph → section → chapter) as the way to size a chunk.
  **Source:** devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md and devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md (the two inquiries that designed the chunking mechanism).
  **Re-test status:** RE-TESTED — commitment confirmed but frame revised.
  **Evidence:** The ladder is real and useful, but it is the *snap target* (the set of boundaries a cut can land on), not the *size target*. The size target is the character budget; the ladder tells you where to snap once the budget sets how big to aim.

- **Commitment:** The diagnosis that the failed translation's errors are "un-wired-method-class" (the load-bearing assumption behind the confound analysis).
  **Source:** devdocs/inquiries/2026-07-11_00-24 finding.md.
  **Re-test status:** RE-TESTED — commitment confirmed but frame revised.
  **Evidence:** Reading the failure log confirms the errors are indeed method-class (register, word-sense, fluency). But the same reading revealed the frame was incomplete: some errors (a specific mistranslated idiom) are better explained as *local capability* — a third cause, chunk-invariant, that neither chunking nor method-wiring fixes. The diagnosis holds; the two-way (length/method) frame it sat inside is now a three-way frame.

*(Note: these statuses are mostly "confirmed but frame revised," not "confirmed" — the frame-testing is genuine, not rubber-stamped inheritance.)*

## Next Actions

The inquiry is deepen-only; its understanding-value is realized now. The actions below harden it and would let the intervention ship — all subject to the standing gate.

### MUST

- **What:** Any onward finding, memory, or SKILL text that cites this result must carry the quarantine split verbatim — the evidence lifts the quarantine on *adopting a size budget* (weakly), not on *length being the cause*.
  **Who:** whoever authors the next inquiry or the SKILL edit.
  **Gate:** condition-bound — on any reuse of this finding's evidence claim.
  **Why:** prevents the single most likely corruption — borrowing method-evidence to underwrite a length-claim, which would silently over-state what is known.

- **What:** Keep the intervention gated — no edit to the translation SKILL (`SKILL.md`, the harmony layer, or the configuration schema) without explicit user authorization.
  **Who:** the implementing agent.
  **Gate:** condition-bound — until the user authorizes a specific edit.
  **Why:** the standing project constraint; deepen-only reach.

### COULD

- **What:** Close the evidence anchor — read the successful `4_mesele_en` translation independently to confirm it is actually clean, and classify each failure-log error as load-driven versus competence-limited.
  **Who:** a focused review pass.
  **Gate:** observable — doable now; needs only the existing files.
  **Why:** the cheapest honesty win available; it is what would lift (or confirm) the mechanism quarantine, which currently rests on inference rather than a checked reading.

- **What:** Calibrate the number — judge the second small translation (`5th_word`, ~4,148 source), locate and measure the absent `ikinci_huccet` source, and translate one medium (~7,000–10,000 character) source to bisect the large gap between the known-safe 4,345 and the known-fail ~28,330.
  **Who:** the never-run calibration experiment, now provenance-anchored.
  **Gate:** observable — turns the band into a located point.
  **Why:** discharges the "band not cliff" imprecision by finding where failure actually begins.

- **What:** Adopt the source-character budget in the SKILL — type the configuration field as source-characters, add the model-facing instruction, and wire the engine to chunk, reusing "fixed-budget-with-snap."
  **Who:** the implementing agent.
  **Gate:** condition-bound — on user authorization.
  **Why:** realizes the surviving intervention.
  **Depends-on:** MUST item "keep the intervention gated." This COULD is GATED — do not act until the user authorizes.

- **What:** Fold an output expansion-ratio tripwire (flag drafts materially above the ~1.5–1.6× band) into the existing whole-draft quality check.
  **Who:** the implementing agent.
  **Gate:** condition-bound — on user authorization; soften the threshold rather than hard-coding 2×.
  **Why:** a cheap over-expansion smoke-signal, complementary to the source budget.
  **Depends-on:** MUST item "keep the intervention gated." This COULD is GATED — do not act until the user authorizes.

### DEFERRED

- **What:** Decide crutch-versus-permanent — after the SKILL's multi-pass method is wired, re-test a previously-failing large chunk. If it recovers, the budget was a crutch (relax it); if it still fails, load-degradation is real (keep it permanently).
  **Gate:** condition-bound — revives when the un-wired method is wired (a separate inquiry's work).
  **Why (if revived):** decides whether the char-budget is a stopgap or a standing safeguard, and re-tests whether size and method are truly independent levers.

- **What:** State "confound-robust conservative safeguard" as a reusable decision-principle (adopt a cheap intervention that helps under all confounded mechanisms without resolving the confound).
  **Gate:** condition-bound — revives on a genuine third instance beyond this budget and the prior low-regret bet.
  **Why (if revived):** would earn a named heuristic; premature at two instances, and its flagship instance here is imperfect (blind to the local-capability leg).

## Reasoning

The critique produced no outright kills — every candidate design survived — but it applied five real refinements, and understanding *why nothing died yet nothing passed unchanged* is the substance of this finding.

**Why nothing was killed:** the surviving intervention (a source-character budget that snaps to structure) is cheap and net-positive under every reading of the confounded evidence. Even in the worst case for it — the failure being purely a method problem with length merely correlated — a smaller chunk still helps the method survive. There is no reading of the evidence under which adopting the budget makes things worse. That is what carried it through.

**Why nothing passed unchanged:** the analysis, before critique, was systematically a half-notch too clean — it consistently stated each result slightly stronger than the evidence bore, and always tilted toward the "size is the story" reading. The two sharpest corrections:

- The claim that the evidence "partially lifts the quarantine" was borrowing evidence about the method to prop up a claim about length. The small-good/big-fail pattern is *exactly* what a pure-method failure also predicts if the big text simply contained more traps. So the lift had to be split: real on the intervention, null on the mechanism.

- The claim that a smaller chunk "lets any method survive" over-reached. The failed translation's errors include a mistranslated idiom that a 500-character chunk would fumble just as badly as a 5,000-character one. Chunking helps *load-driven* drops; it does nothing for *local, competence-limited* errors. That forced the three-way confound and the scoped robustness.

The other three refinements: the "safety factor" framing was false precision (one success point cannot yield a factor); the output expansion-watch was redundant with the existing whole-draft check unless demoted to a cheap tripwire feeding it; and the "REFINES the prior finding" claim had to be sized honestly — the prior finding's snap-to-structure survives, and the genuine new contribution is the unit-definition plus anecdotal provenance plus the scoped-robustness argument, not a new mechanism and not an overturn.

The deepest yield was reframing *how the budget is held*: not as a proven load-limit, but as a cheap bet adopted under an unresolved confound, whose long-run necessity is itself an empirical question for later. That honesty is the finding's real advance over the prior one.

## Open Questions

### Monitoring
- Whether the second small translation (`5th_word`) is judged good — if so, it becomes a confirmed second success point and strengthens the ~4,000-character safe region.

### Blocked
- Whether the char-budget is a temporary crutch or a permanent safeguard — cannot be answered until the SKILL's multi-pass method is actually wired, after which large chunks can be re-tested.
- The failed translation's true source size — blocked until the absent `ikinci_huccet` source file is located or reconstructed.

### Research Frontiers
- Separating length from local-capability as failure causes — would require translating the same text at several chunk sizes and watching which error-types fade with smaller chunks and which persist at every size.

### Refinement Triggers
- **Re-open the "length-mechanism stays quarantined" conclusion** when the same-text-different-chunk-size experiment runs and shows error-rates changing with size independent of content. Until that specific experiment exists, the mechanism stays quarantined — not on generic "if things change."
- **Re-open the ~3,500–4,000 band** when the bisection experiment locates an actual failure onset between 4,345 and ~28,000 characters. Name the blocker: the missing mid-range data point.
- **Re-open "characters, not tokens, for the human-facing budget"** if the engine's internal accounting is built out and a token budget proves materially more stable in practice.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
u said

Chunk by structure, not by a number — with the honest caveat that this relocates the unknown rather than removing it. [...] That is more tractable, and still ultimately a calibration question the experiment must answer.

i feel like section paragrapgh etc are too changing in their sizes, a paragrah can be 20 sentence or 2 or 30 even. similar to section.
this is why we need better approaximations such as character and word count, 3500 character is similar in most situations or the word count

and 3500 comes from past good translation example of mytrasnlations/asayi_musa/4_mesele.md and mytrasnlations/asayi_musa/4_mesele_en.md which was succesfull in my judgment unlike our last example , our last source file translation was approximately 11000 char long (mytrasnlations/asayi_musa/ikinci_huccet_en.md) and i thought that was too much since it failed and i come up with this safe number of 3500 for opus 4.8 model. For smaller models it should be lower to protect the comprehenslation integrity (a new term)

lets dive deep into this understanding
```

</details>
