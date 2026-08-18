---
status: active
model: claude-opus-4-7[1m]
effort: unknown
refines: devdocs/inquiries/2026-07-11_20-41__skillmd_edit_coverage_of_prior_inquiries/finding.md
---
# Finding: Why the translation errors happened, and what was missing in the process

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-07-11_20-41__skillmd_edit_coverage_of_prior_inquiries/finding.md` — the audit that checked whether a hand-edit to the translation skill's workflow file covered the shortfalls the earlier diagnostic chain had identified.

**Revision trigger:** New evidence. The audit's recommended fixes were subsequently applied to the skill, and one month later the same class of translation error recurred. That recurrence is evidence the prior chain could not have had.

**What's preserved:** The prior chain's diagnosis is confirmed, not overturned. The **enforcement gradient** — the claim that a written instruction inside a single model run is a weak nudge, while a separate model call physically constrains what the model can do — holds. So does the **meaning-lock-first** principle, and the **post-draft verification** idea, and the observation that word-sense correctness does not depend on reader settings.

**What's changed:** The prior chain treated the enforcement gradient as *the* axis along which an intervention gets stronger or weaker. This finding demotes it to **one axis of five**. That is why the prior chain's fix — which was correct, and which was shipped — did not prevent the recurrence: it repaired the ordering of the translation passes and left four other properties of those passes untouched.

**What's new:** A five-property account of what a "check" actually is; a classification of the observed errors by which property failed; a diagnosis of why a correct, shipped fix failed within a month; a remedy set typed by property, of which five of six require nothing to be built; and a connecting principle — *replace judgment with construction* — that the prior chain did not have.

**Migration:** No prior commitment is retracted. The prior chain's recommendations remain valid and their scope narrows: each addresses a specific property rather than the whole problem. See the **Inherited Commitments Re-test** section for each commitment's status.

**MUST/COULD drift check:** The prior finding was an evaluation and issued no MUST/COULD items; there is no drift to record.

---

## Question

The user asked, after a translation delivered with roughly nineteen errors:

> *"why u made these errors u think?? what was missing in our process that these errors were made? i understand you are ai but i am wondering what was missing, think really deep and try to uncover the most core issues..."*

The context: **comprehenslate** is a general-purpose AI translation project. It carries a written method — a sequence of four ordered "passes" a translation runs through — plus several thousand lines of supporting reference material (a catalogue of translation principles, a set of tiers describing which structural features of a text must be preserved, eight configuration axes describing the intended reader, and seven policy settings for recurring editorial decisions). Said Nursî's *Risale-i Nur*, a multi-volume Turkish work with embedded Arabic, is the project's calibration corpus — the text used to tune the method, not the method's purpose.

Two roughly one-page sections of that work were translated into English. Errors surfaced afterwards in three waves: ten found when the user asked for a re-scan, seven more when the user asked for a second re-scan of the same text, and two the user found directly and the assistant never found. The fourth of the four passes — whole-draft verification — had been run before delivery and had reported PASS.

**The goal** was a causal account of why this happened, pitched at the depth the phrase "most core" demands, naming what the *process* lacked rather than what the *agent* lacked. The user explicitly granted the assistant's nature as a premise and refused it as an answer, which rules out "because I am an AI" as a terminal explanation. Also ruled out: re-translating the passage, re-arguing whether each item is really an error, apologising, and any account that stops at the first layer.

---

## Finding Summary

- **Nothing was missing from what the process knew.** The specific principle that identifies each of most of these errors is written in the project's own reference material, correctly worded, and all of it was read into the model's working context before the translation began. The knowledge was present and inert.

- **What was missing was a distinction.** The method talks about "checks" as though a check were one kind of thing. A check is actually five separable properties, and they can fail independently of one another.

- **The five properties are:** what the check is **specified** to look at · from what **vantage** it is made, meaning what must be present in and absent from the checker's context · with what **instrument**, meaning whether it produces something inspectable or only a verdict · at what **enforcement position**, meaning whether the checker could have ignored it · and at what **time** relative to edits, meaning what makes its result stale.

- **Every error is a failure of one of those five**, and they sort cleanly. Most failed on **instrument** — the check that would catch them produced a verdict rather than a list. About half a dozen failed on **position** — the right check existed and ran as prose inside the same forward motion that produced the text. One failed on **specification** — the verification pass excludes policy checks by its own definition, so nothing anywhere was looking. One failed on **vantage** — catching it requires reading the English without the Turkish in view, and no step in the method stands there. One failed on **timing** — it was correct in the first draft and broken by a later tidying edit that nothing re-checked.

- **This is why the previous fix did not take.** A month before this translation, the same failure was diagnosed, a fix was written, and the fix was shipped into the skill's workflow file — the translate step was rewritten from a flat list into four ordered passes with an explicit instruction not to collapse them. That fix repaired **ordering**, which is one property adjacent to position. It left vantage, specification, instrument and timing exactly as they were, and the errors those four produce came back.

- **What actually found the errors was not in the method.** Seventeen of nineteen surfaced on re-scans, and each re-scan happened because the user asked for one. Their request supplied three things at once: a fresh turn, an instruction to check against the policy file and the configuration, and an instruction to work sentence by sentence and paragraph by paragraph. Those are fixes for **position**, **specification** and **instrument** respectively — supplied in one sentence, by someone with no theory, with the error yield going from zero to ten.

- **The method reported complete while depending on a step it does not contain.** That is the defect — not that the method is useless, but that its verification pass emitted PASS on a draft carrying fifteen undetected errors, with no indication that anything was outstanding.

- **Four claims about self-verification are real limits, and one of them favours this process.** Each was tested by restating it with a human translator as the subject; all four survive, which makes them properties of the arrangement rather than of the agent. One inverts: a model's context can be emptied by constructing a new call, and a human translator's memory of what they just translated cannot. Human translation workflows buy that vantage by hiring a second person. This process can have it for the cost of one small call and is not using it.

- **Five of the six repairs need nothing built.** A pre-draft term list, a seven-row policy check, a rule that re-runs a check after an edit, and a source-blind reader that outputs questions rather than edits are all available now. Only the full separate-call engine requires a build — and it repairs the one property the previous fix already tried to reach with prose.

- **The connecting principle is: replace judgment with construction.** Every check that held was construction-shaped; every check that failed was judgment-shaped; and every remedy that survives adversarial scrutiny survives by making that same substitution. This is the finding's most portable output — it is a test that can be run on any future proposal.

- **Confidence is split.** That the five properties are separable is well-supported and re-derivable by anyone who opens the same files. How much any repair is worth is unmeasured, and a validation experiment is a MUST rather than a suggestion.

---

## Finding

### Why this question is worth answering carefully

The user built this translation method. It is not a generic tool being critiqued from outside — it is a method that has been diagnosed once before, whose diagnosis was correct, whose fix was written and shipped, and which then failed again in the same way one month later. That sequence is what makes a shallow answer useless here. "Be more careful" and "run the passes properly" have both already been tried, in writing, in the file the model reads. The question is what a correct fix could have missed.

The account below is organised around the answer to that: the fix could not have known what it was missing, because the thing it was aimed at had not been distinguished into its parts.

---

### 1. The knowledge was not missing

The first thing to establish, because it rules out the most natural reading of the question, is that nothing relevant was absent from the project's written material.

`case_catalog.md` — the project's catalogue of translation principles, about 139 entries over 698 lines — contains, in correct and unambiguous form, the principle that identifies most of these errors:

| The error | The principle already written down |
|---|---|
| A rhetorical question read as though it asserted the opposite of what it asserts | **#4** — arrangement carries meaning; "a question instead of a statement… the arrangement is a primary carrier, not packaging" |
| A word repeated three times in the source, rendered once | **#20 / #37 / #38** — repetition marks independence · sustaining repetition is not redundancy · repeated wording does different work in each spot |
| A two-sense pun flattened to one sense | line 359 — "a word's buried root can be activated by context to carry a second meaning" |
| Four wrong word-senses | **#7** — preserve every valid meaning rather than forcing one |
| The method's own governing premise | **#6** — comprehension first, then validation |

A broken pronoun reference is covered too, by the "pronoun chain continuity" entry in `harmony_layer.md`, the file describing which structural features of a text must be preserved.

All of it was read into the model's working context before the translation began — the skill's first rule requires reading every reference file in full, which is roughly 3,489 lines across eight files, reloaded on every run.

**Why none of it fired.** Every entry in that catalogue has the same grammatical shape: *"The comprehension layer should detect / notice / ask / flag X."* It is a library of things worth noticing, indexed by nothing. To retrieve the entry about noticing X, you must already have noticed X. The catalogue can confirm a noticing. It cannot cause one.

So "missing" splits in two. A minority of checks are genuinely absent from the written material — nothing anywhere says "check that referring expressions resolve without the source," or "read the English cold and ask whether it asserts what the source asserts," or "re-run the checks a revision touched." But the majority were present and inert.

**The corrected sense of the question is therefore: what was missing from the run, not from the material — and specifically, what was missing was the condition under which a written principle fires.**

This immediately rules out one whole class of repair. Writing the principles more clearly, or more emphatically, or in a better-organised file, cannot fix a retrievability failure. The principles are already clear. They were already read.

---

### 2. A check is five things, not one

Here is the core of the answer.

The method — and, as far as the evidence shows, the way anyone talks about verification in this project — treats "a check" as a single kind of object. It is not. Any check has five properties, and they vary independently:

| Property | What it is | The question that determines it |
|---|---|---|
| **Specification** | whether the check is defined at all, and over what | *Is this check named anywhere, or is it assumed by whoever runs it?* |
| **Vantage** | what must be **present in**, and **absent from**, the checking context | *Can this question be answered without the source — and does having the source available change the answer?* |
| **Instrument** | script · forced enumeration · prose judgment | *Does this check produce something you can inspect afterwards, or only a verdict?* |
| **Position** | prose instruction · emitted artifact · separate call | *Could the checker act on material this check forbids?* |
| **Time** | the check's validity window relative to edits | *What invalidates this result, and does anything re-run it when that happens?* |

Two of these deserve a note. **Vantage** is not a synonym for "who checks" — it is about what is in the checking context. The same checker, in a context that contains the source and a context that does not, is at two different vantages with two different detection capabilities. And **position** is the project's already-established enforcement gradient (an instruction inside one model run is weak; a separate call physically constrains what the model can act on) — it survives intact here, as one property among five.

**Vantage and position are separate axes.** This is the least obvious of the claims and the most consequential. A separate call is a *positional* move — it buys the ability to control what is in the context. Removing the source from that call is a *vantage* move — it exercises that ability. In practice separate calls usually have controlled inputs, which is why the two get collapsed. The evidence separates them: the re-scans were structurally separate calls that still contained the source, and they found none of the errors that require the source's absence.

**How this claim is warranted, honestly.** The natural way to argue for five independent properties would be to show each one varying while the other four are held fixed. That argument does not work here, and it is worth saying why rather than leaving it for a reader to discover:

- The cleanest case is **time**: the pronoun regression passed every check that ran, with the same specification, vantage, instrument and position — only the timing relative to the edit differed. That one is a genuine controlled comparison.
- **Specification** admits no such comparison at all. A check that does not exist has no values on any axis. Its independence follows logically instead: a check must be defined before it can be positioned or instrumented.
- The remaining comparisons are confounded, most notably the one between instrument and position — see §4, where the confound turns out to carry the finding's best evidence.

**So the accurate ground is independent failure, not independent variation: each of the five is shown able to fail while the other four are satisfied.** That is true of all five, and it is what the evidence supports. The stronger-sounding claim is not available and is not made.

**What this buys that a list of gaps does not.** A list of gaps of any length leaves a reader unable to tell whether the list is complete, and unable to place a gap that is not on it. The five properties are a frame under which every gap in the evidence, every remedy, and — critically — **every previous fix** becomes classifiable. It is also generative: applying the determination questions to a check nobody has ever run (*"is the footnote density right for the configured reader?"*) classifies it immediately as a **specification** gap, with no error having prompted the question.

**Confidence.** That the properties are separable is HIGH — a reader who disagrees can open `translation_method.md` and read that the verification pass excludes configuration checks, or open the git log and read what the translate step said before and after the July edit. That vantage and position are *orthogonal* is an inference drawn from confounded comparisons, and is held at MED. That the five are **exhaustive** is not claimed at all; they are five observed properties, and a sixth may exist.

---

### 3. Which property failed, for each error

Errors were classified by a stated rule rather than by convenience: **absence is detectable by alignment; wrongness inside an alignment is not.** A missing word is visible to anyone comparing the two texts — there is a source word with no counterpart. A wrong sense is not — the counterpart exists and the error is inside it. That line decides whether an existing check could have caught the error at all.

| Gap kind | Property that failed | Errors | Count |
|---|---|---|---|
| **Instrument** | no inspectable artifact existed to surface the feature | four wrong word-senses · a weakened intensifier · a silently normalised transliteration · two cognates rendered with unrelated words · a lost pun · three register renderings | ~11 |
| **Position** | the right check existed, was correctly specified and aimed, and ran as prose inside the producing motion | a dropped word that echoed across two sentences · an invented doubled verb · an added totaliser · a dropped explicit subject · a three-times repetition rendered once | ~5 |
| **Specification** | no check was ever defined for this class | one honorific rendered against the policy setting | 1 |
| **Vantage** | detectable only from a context the method never occupies | a rhetorical question rendered so that it read as denying what it affirms | 1 |
| **Time** | correct when written; broken by a later edit that nothing re-checked | an unresolvable pronoun | 1 |

**The counts are approximate and should not carry weight.** They shift under any defensible re-reading of the classification rule — several items sit near the instrument/position boundary, and three of the instrument-kind items are, as §7 explains, currently undecidable as errors at all. The **kinds** are the payload; the numbers are an artefact of where one line is drawn.

**What repairs each kind, and which repairs are position-independent:**

- **Instrument** → a forced enumeration that surfaces the feature. Not more instruction; an artifact.
- **Position** → move the check up the gradient: an emitted artifact, or its own call.
- **Specification** → **position-independent.** Defining the check is upstream of enforcing it. Run the verification pass as a separate call, as a script, as a human review — it still does not check what it was never defined to check.
- **Vantage** → **position is necessary but not sufficient.** A separate call gives you the ability to control the context; only construction exercises it.
- **Time** → **position-independent as a rule.** A rule that is not stated does not run at any position. A call-based architecture makes the omission *visible* — an edit after verification obviously invalidates the verification's input — but it does not supply the rule.

Those three position-independent or partly-position-independent cases are why the account cannot be reduced to "everything was at the wrong enforcement position." That reduction would be tidier, and it is not what the evidence shows.

---

### 4. What actually enforced anything

This section is about the shape of an arrangement. It stays true if any participant is substituted for any other.

Seventeen of the nineteen errors surfaced on re-scans. The first of those re-scans happened because the user wrote this:

> *"can u do another scan on this and make sure it followed SKILL/references/config/schemas.py and our config selections ? and make sure you first read the original and understand **sentence by sentence and paragraph by paragraph** and then check if english translation has some weird translations or not?"*

Read against the five properties, that request supplies three fixes at once:

- **a fresh turn** — structurally a separate call, which is the strong end of the enforcement gradient (**position**);
- **"make sure it followed schemas.py and our config selections"** — a check against the policy file and the configuration, which is exactly the class the verification pass excludes by its own definition (**specification**);
- **"sentence by sentence and paragraph by paragraph"** — a forced enumeration, stated in plain language (**instrument**).

The error yield went from zero to ten.

**That is the strongest evidence in this finding, and it arrived independently of the theory it supports.** A person with no framework supplied repairs for three of five properties in a single sentence. It also protects the account against the obvious objection that the five properties are an invented decomposition dressed up as a discovery — the decomposition was not needed to produce the repairs; it was needed to notice that three different repairs had been made.

The two errors the user found unaided are the vantage-kind and time-kind ones — the two whose detection requires reading the English without the Turkish in view. That is the one position no pass in the method occupies.

**The counterfactual, stated with the right subject.** The method had no step that would have found these errors. The only thing that did was a request the method does not know it needs. Remove that request and the translation ships with nineteen errors under a verdict of PASS.

**The structural statement: a necessary position in the process was staffed by accident and never assigned.** Two things were being supplied that the method requires and cannot produce for itself — a separate call, manufactured by asking; and a source-blind vantage, occupied by reading. Neither is written down anywhere. Neither has an owner. An unnamed dependency cannot be maintained, cannot be automated, and cannot be handed to anyone else.

**The strongest objection, and a straight answer.** *Seventeen of nineteen were caught before the final read — perhaps the process worked.* The distinction that matters is not "the method caught zero," which sounds like the method is useless. It is that **the method reported complete while depending on a step it does not contain and does not name.** The verification pass emitted PASS. A process that signals completion while silently depending on an unspecified action is misreporting, and that is a defect regardless of who is executing it.

---

### 5. Why the previous fix did not take

On 2026-07-12, `translation_method.md` was created — the four passes, the hard constraints, the chunking policy, and an honest note about enforcement. On the same day the skill's workflow file was rewritten. The git diff shows exactly what changed. The old text read *"Then produce the translation. Apply:"* followed by a flat list of things to apply. The new text reads *"produce the translation by running the four-pass method… in order. **Do not collapse the passes into one motion**; do not concrete the translation until Pass 3,"* followed by all four passes inlined with their rationale.

That is not a half-measure. A chain of seven prior inquiries had diagnosed the failure, an audit had checked whether an earlier hand-edit covered the shortfall and found it did not, and the remaining shortfall was then fixed in the runtime file the model actually reads.

**On 2026-08-14 — one month later — the same class of error recurred**, under a verification pass that ran and reported PASS.

**The mechanism.** The fix repaired **ordering**: when each pass runs relative to the others, and that the configuration should not be in view during the first. Ordering is one property, adjacent to position. It said nothing about **vantage** — no pass was moved to a context without the source. Nothing about **specification** — the verification pass's exclusion of configuration checks was left in place, and is in fact restated in the new text. Nothing about **instrument** — all four verification checks remained prose. Nothing about **time** — no rule was attached to post-draft edits.

Four of five properties were untouched, and the errors those four produce came back on schedule.

Stated generally: **a correct answer delivered against one property of a five-property object leaves four-fifths of the object unrepaired.** The July fix was not wrong. It was under-dimensioned, and it could not have known it was, because the dimensions had not been named.

**This is retrospective, and the honest thing is to say so.** A decomposition-shaped explanation of a one-property fix is cheap to construct — pick any decomposition into N parts, observe that the fix touched one, and the "it only fixed one!" shape follows. What distinguishes this one is that it also sorts the errors and generates a prediction it could lose on:

> **If the separate-call engine is built first and the other repairs deferred, it will repair position and the other four kinds will recur.**

That is falsifiable, dated by the build, and would embarrass this account if an engine alone cleaned things up. It is the reason this finding recommends the cheap repairs first, and it is offered as the account's own refutation condition rather than as a rhetorical flourish.

**This is also why the account cannot stop at naming another missing step.** A structural answer to this question has already been produced once. Its artifact is the thing that failed. An account concluding "you are missing a source-blind pass" would produce a fifth correctly-worded instruction in a file that already contains four.

---

### 6. Which limits are real

Parts of this diagnosis sound like claims about being an AI, and the user set that aside as an answer. So each such claim was put through one test: **restate it with a human translator as the subject.** If it still holds, it is a property of the arrangement and belongs in a process diagnosis. If it collapses, it is a property of this agent and is out of bounds.

| The claim | With a human translator as subject | Verdict |
|---|---|---|
| A producer cannot reliably detect its own omissions by re-reading in the same context | A translator re-reading their own draft with the source open reliably misses their own omissions — which is why publishers employ copy-editors and why proofreading one's own writing is proverbially unreliable | **holds — in scope** |
| A producer cannot occupy the source-blind vantage while holding the source | A translator who has just rendered a passage cannot read the English as someone who has never seen the Turkish. They know what it means | **holds — in scope** |
| A self-reported PASS is evidence that no check fired, not that nothing is wrong | "I checked it," with no checklist, reports that the checker found nothing — not that there was nothing to find | **holds — in scope** |
| Fluency is self-evidencing and fidelity is not | A fluent English paragraph reads as correct to its author regardless of what the source said. Nothing about a well-formed sentence signals that a source word is missing from it | **holds — in scope** |
| *(control)* A model cannot tell when it is confabulating a meaning it does not actually know | A translator who does not know a word experiences not-knowing, and looks it up or flags it. The not-knowing is available to them in a way it is not straightforwardly available to a model | **collapses — excluded as agent-property** |

The control case matters: the test does reject things, and this claim — which would have been convenient — is not admitted.

The four that hold are structural facts about who is checking what from where. They are why separation of duties exists in software review, why copy-editing is a separate role in publishing, and why aviation checklists are read aloud by one party and confirmed by another. None of that exists because the first party is careless. **One limit of the test should be stated too: passing establishes that a claim is about the arrangement, not that the claim is load-bearing for this particular failure.**

**And one of the four inverts in this process's favour.** The second claim is *strictly worse for a human*. A translator's memory of what they just rendered cannot be emptied — it goes home with them. A model's context can be emptied by constructing a new call: give it the English and nothing else, and the vantage is genuinely occupied rather than simulated.

**Human translation workflows pay for that vantage with a second person. This process can have it for the cost of one small call — and is not using it.** That is not a limitation being excused; it is a capability being left on the table.

**Why the instruction version does not work.** Within a call that contains the source, "read this as a fresh reader who has never seen the original" cannot be executed — not through unwillingness, but through the shape of the question. The check asks *is this referring expression resolvable?*, and the context has already answered it before the check begins. The reader does not consult the source to resolve "it"; the referent is simply not experienced as missing.

**The direct evidence:** the same text was re-scanned twice, under explicit instruction to hunt for errors. Those two passes found seventeen source-comparison errors and **zero** of the one target-only error that existed throughout. If the vantage were adoptable by instruction, at least one of those passes should have caught it.

**A precision worth keeping:** the claim needed here is not that information cannot be removed from a context — it is that the *judgment* is contaminated by the information. Those come apart, and the gap between them is useful: the mechanical half of the check (*list every referring expression and its nearest antecedent*) is producible identically with or without the source, and only the evaluative half (*is this recoverable?*) requires the source's absence. That makes the repair cheaper than it first appears.

---

### 7. What repairs what, and what is available now

Six repairs. They are not competing for one slot — they address **different properties**, and their overlap is small.

| # | Repair | Property | Position on the gradient | Available |
|---|---|---|---|---|
| **R1** | **Per-document term list**, built before drafting | instrument | emitted artifact | **now** |
| **R2** | **Policy-conformance enumeration** — seven rows | specification | emitted artifact | **now** |
| **R3** | **Post-revision re-run**, carried by a verification record | time | artifact-carried rule | **now** |
| **R4** | **Source-blind reader** — questions only, no edit authority | vantage | separate call, controlled input | **now** |
| **R5** | **Fresh-context adversarial reader** | vantage + position, broadly | separate call | needs orchestration |
| **R6** | **The engine** — passes as separate calls with real intermediate artifacts | position | separate call | **needs a build** |

**Five of six require nothing to be built.**

#### R1 — the term list, and the objection it has to survive

Before drafting, produce one artifact from the source: every word of a detectable loan-word form with its candidate senses · every word that repeats, with its count · every cognate cluster · every technical term the source names in its own vocabulary · every honorific form · every transliterated string to be carried unchanged.

R1 is **not a check.** It runs before drafting, which makes it a pre-commitment rather than a verification. You cannot fail to notice a polysemous word you enumerated before you started writing. It converts most of these errors from things that must be *caught* into things that are *harder to commit*.

**The objection this has to survive, stated plainly: who decides which words are polysemous?** If the answer is "the same context, using the same noticing that failed," then R1 produces a list that omits exactly the words that go on to cause errors, and the noticing problem has simply moved one step back.

**The answer is a restriction, not a hope.** The objection is fatal to *judgment-keyed* enumerations and harmless to *form-keyed* ones:

- *"List every polysemous word"* — requires the noticing. **Fails.**
- *"List every Arabic- or Ottoman-derived word in this passage, then give each one's senses"* — requires a morphological filter. The class is identifiable **by form**, not by whether ambiguity was noticed; sense-listing then runs over the whole set, exhaustively rather than selectively. **Survives.**
- *"List every word appearing more than once, with counts"* — mechanical. **Survives.**
- *"List every technical term the source names in its own vocabulary"* — the source literally contains the string `istifhâm-ı inkârî`. **Survives.**

**So R1's specification rule is: no line may read "list every X that is [semantic property]." Every line must read "list every X of [detectable form], then state its [semantic property]."** That single rewrite is the difference between a repair that works and one that reproduces the failure it is meant to fix.

#### R2 — an enumeration, not a verdict

Seven rows: policy · its value · where it applies in this source · how the draft rendered it. It must force *naming*, not ask for a judgment. A checklist that asks "are the policies satisfied?" becomes seven more things to assent to; a checklist that requires you to write down the honorific and its rendering cannot be assented to. Aviation checklists are read aloud, not recalled, for exactly this reason.

This also fixes a related oddity: the seven policy defaults are in force on every run and are never shown to the user. An honorific policy was violated in a run where nobody had seen it.

#### R3 — a rule that needs a carrier

The rule itself is free: *any edit made after verification re-runs the checks whose span it touched.*

But as a bare sentence in a runtime file, R3 sits at the weakest position on the enforcement gradient — which would make it the next instance of the pattern this finding is about, inside this finding's own remedy set. **It needs a carrier: the verification emits a record naming the draft-state it verified** (a hash, a line count, a quoted span). An edit changes the state, and the record is then *visibly* stale rather than notionally invalid. That is a construction rather than a reminder, and it costs almost nothing.

#### R4 — the vantage repair, split in two

- **Mechanical half, runs in-call:** list every referring expression and its nearest preceding antecedent, without evaluating resolvability. This output is producible identically with or without the source.
- **Evaluative half, requires its own call:** the English draft and nothing else. *Is each antecedent recoverable from this text alone? What does each sentence assert?*

**Its output is a question list. It has no authority to edit.** That is what answers the obvious risk — a reader who cannot see the source and is asked to *fix* unclear English will resolve ambiguity by guessing, which manufactures precisely the invention-class error this whole diagnosis is about. A reader that cannot write cannot invent. Every fix is then made in a source-present context, which is the vantage that demonstrably works.

**R4 depends on R3, and the dependency is not optional.** R4 generates quality concerns, and quality-motivated edits are exactly what produced the pronoun error. R4 without a post-edit re-check manufactures the edit-pressure that caused one of the nineteen. **Ship R3 before or alongside R4, never after.**

The cost profile inverts the intuition: the repair addressing the errors nothing else can catch is the **cheapest call in the method** — it holds one text and one instruction, less context than any existing pass. The real cost is not tokens; it is the routing step that gets the question list back into a source-present context and acted on.

#### A test the repair set has to pass

Add the constraint: *no new prose may be added to any runtime file.* R1 survives (an artifact). R2 survives (an enumeration). R3 survives once it has a carrier. R4 survives (a call construction). R6 survives (an architecture). **The set satisfies the constraint** — which is the check that it is not secretly the intervention that already failed. And the honest note that any of this is a nudge rather than a guarantee belongs in authoring notes, never in the runtime text: a caveat telling the model its own structure is optional licenses it to relax.

---

### 8. The principle underneath all of it

Reading the repairs together, one move appears in every single one — and in the one check that worked:

**Replace judgment with construction.**

- The one verification check that held was a **sentence-boundary count**. Counting is a construction; *"was anything dropped?"* is a judgment. The other three verification checks were judgments and passed a draft carrying fifteen violations.
- **R1** works only when its enumerations are keyed to detectable form rather than to the judgment *"is this word ambiguous?"*
- **R2** works only as an enumeration that forces naming, never as a verdict.
- **R3** works only when a record makes staleness visible, rather than a sentence asking someone to remember.
- **R4** works only because the vantage is *constructed* by controlling what is in the call, never by instructing a stance.
- And the negative instance holds too: **every check that failed was judgment-shaped.**

As a test to run on any future proposal: **does this ask someone to notice, or does it construct the set?**

This is the finding's most portable output. The five-property frame is the diagnosis; this is the prescription, and it is what connects them. Two things about its scope are honestly open: some checks may be irreducibly evaluative — whether a register is appropriate, whether a preservation tier applies — and whether the principle reaches them is unresolved. And its relation to the project's existing enforcement gradient is plainly close and not worked out; they are not rivals, but the account does not yet say precisely how they compose.

---

### 9. How much of this to trust

**HIGH, and the criterion is pointability.** That the five properties are separable does not rest on how many errors there were. It rests on evidence a disagreeing reader can check independently: open `translation_method.md` and read that the verification pass excludes configuration checks; open the git log and read what the translate step said before and after the July edit; look at which check had a script and which did not; read the user's re-scan request and count the three things it supplies. **HIGH is warranted where a reader who disagrees can point at something.** That is a claim about transferability, not about truth — but it is the difference between this claim and the ones below.

**MED on the inferences.** That vantage and position are *orthogonal* is drawn from comparisons that are confounded, and is held one tier lower than the pointable premises it rests on.

**MED and quarantined on all magnitudes.** How much R1 reduces errors, whether R4 catches most vantage-kind errors, whether the repair set is complete — none of this is measured. That is why the validation experiment is a MUST.

**The evidence is small and biased, and the bias has a direction.** Nineteen errors, from one text, under one model. And they are the errors scrutiny *found* — any error visible only from a vantage nobody occupied could enter the sample only if the user happened to notice it. So the observed vantage count is a **lower bound**; the bias understates the vantage gap while making the proportions unusable. Error counts also track scrutiny rather than quality: seven errors were found in a prior translation under less scrutiny, nineteen here under more, and no argument in this finding rests on that comparison.

**A related instance, and what it does and does not support.** While this inquiry was running, `tools/structural_check.sh` — a checker the inquiry pipeline's own specification calls for — was found to be absent from this repository, with manual prose judgment substituted at every step and recorded as passed. That is the same *outcome* as the pattern under diagnosis, and it supports the **instrument-axis** claim specifically. It is a weaker instance than it first appears, and the disanalogy should be stated: the specification anticipates the absence and sanctions the manual fallback, whereas the translation method's verification pass never contemplated an instrument at all. It does not straightforwardly raise the evidence count for the five-property structure.

**One reading this finding does not refute.** Under a research-artifact lens — a method under development, not a production system — nineteen errors in a first-pass literary translation from Ottoman-inflected Turkish is unremarkable, and this diagnosis is over-engineering. That reading is coherent. What it does not explain is why the one mechanised check held perfectly while the prose checks caught nothing, or why the errors that survived are exactly the ones requiring a vantage nobody occupied.

**This inquiry, scored against its own finding.** Its steps ran as genuinely separate calls, each loading its own specification and emitting an artifact the next reads — strong on **position**. Every step ran in one context, and its adversarial review step is adversarial *by instruction*, which is precisely the construction §6 rules inadequate — weak on **vantage**. Its one specified mechanical check does not exist and prose self-assessment was substituted throughout — worst on **instrument**.

**So the specific claims an outside reader should check first are:**

1. the five evidence comparisons in §2 — three are confounded and the finding says so, but a reader should verify the ones it keeps;
2. the error counts in §3 — unstable under the classification rule;
3. the attribution in §4 — that the user's request supplied three property-fixes rather than one;
4. R1's restriction in §7 — whether "detectable form" is actually detectable in Ottoman-inflected Turkish, which is asserted and untested.

That list is the consequence of the self-assessment, not decoration attached to it.

---

## Inherited Commitments Re-test

This finding refines a chain of prior inquiries and inherits commitments from them. Each is re-tested rather than absorbed.

- **Commitment:** *The enforcement gradient* — an instruction inside one model run is a probability-raiser the model can ignore; a separate call physically bounds what it can act on.
  **Source:** `devdocs/inquiries/2026-07-11_04-12__staged_skill_borders_and_middleware/finding.md`, and carried forward through the chain.
  **Re-test status:** **RE-TESTED — commitment confirmed but frame revised.**
  **Evidence:** confirmed by this inquiry's central observation — the in-turn verification pass found none of the nineteen errors, while the user-prompted re-scans, which were structurally separate calls, found seventeen. The frame revision: the gradient is **one of five properties of a check**, not the axis along which interventions get stronger. Three gaps in this evidence survive a move to its strong end (specification, time, and vantage-without-construction).

- **Commitment:** *The root cause is the skill's own multi-pass method going un-run; the fix is to wire it into the translate step, meaning-lock first and configuration-blind.*
  **Source:** `devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md`.
  **Re-test status:** **RE-TESTED — commitment confirmed but frame revised.**
  **Evidence:** the fix was shipped (git-verified; the translate step rewritten from a flat list into four ordered passes on 2026-07-12) and the same class of error recurred one month later. The diagnosis was correct — the passes were indeed being collapsed — and the frame revision is that "running the passes in order" repairs ordering only. See §5.

- **Commitment:** *A post-draft verification pass, split into a configuration-independent spine and a configuration-derived reader-keyed agenda.*
  **Source:** `devdocs/inquiries/2026-07-11_01-09__firing_time_categories_for_principles/finding.md`.
  **Re-test status:** **RE-TESTED — commitment confirmed but frame revised.**
  **Evidence:** the pass exists in the current method and ran. The split it prescribed had an unintended consequence: making the pass configuration-independent means it **excludes policy checks by definition**, which is why the honorific violation had no possible catcher anywhere in the method. The split is right about *what varies with the reader*; it needs a companion check that runs at the configuration-plus-target vantage. This is R2.

- **Commitment:** *Word-sense correctness is configuration-independent — the right sense is fixed by the local source construction, not by the reader.*
  **Source:** `2026-07-11_01-09`, and `feedback_translation_polysemy` in project memory.
  **Re-test status:** **RE-TESTED — commitment confirmed.**
  **Evidence:** four wrong-word-sense errors recurred in this translation, all resolvable from the local construction. The commitment holds and is unchanged; what it lacked was a firing condition, which is R1.

- **Commitment:** *The two-lever bounded-load frame* — adherence load splits into per-unit transformation load (lever: chunking) and fixed instruction load (lever: staging), and the two interact with tension because separate-call chunking re-pays the instruction load per call.
  **Source:** `devdocs/inquiries/2026-07-11_04-48__mandatory_chunking_char_limit_adherence/finding.md`.
  **Re-test status:** **RE-TESTED — commitment confirmed, with one lever ruled out for this evidence.**
  **Evidence:** chunk size is refuted as the operative variable here — both chunks ran at roughly 2,340 and 2,609 characters against a stated ~5,000 limit, so the transformation-load lever was not binding. The tension the commitment names remains live and becomes a real constraint on the engine (R6): 3,489 lines of instruction re-paid per call.

- **Commitment:** *Caveats about softness belong in authoring documents, never in the runtime text the model executes* — telling the model its structure is optional licenses relaxation.
  **Source:** `2026-07-11_04-12`.
  **Re-test status:** **RE-TESTED — commitment confirmed**, and applied as a live constraint on this finding's own recommendations. No repair in §7 ships a "this is only a nudge" clause into runtime text; that honesty lives here instead.

- **Commitment:** *Split the confidence* — a claim's structural distinctness can be HIGH while its empirical magnitude stays MED and quarantined until measured.
  **Source:** `2026-07-11_04-12`.
  **Re-test status:** **RE-TESTED — commitment confirmed and sharpened.**
  **Evidence:** applied throughout §9. The sharpening: the criterion for HIGH is **pointability** — a disagreeing reader can open a file and check the premise. That distinguishes premises from inferences drawn on them, and it moved one claim (vantage and position being orthogonal) down a tier.

- **Commitment:** *A prose workflow file can only nudge; the failure class is closed only at the engine layer.*
  **Source:** `devdocs/inquiries/2026-07-11_20-41__skillmd_edit_coverage_of_prior_inquiries/finding.md` (the prior this finding refines).
  **Re-test status:** **RE-TESTED — commitment found PARTIALLY INVALID.**
  **Evidence:** the claim is true for the **position** property and false as a general statement. Four of the five properties admit repairs that are neither prose nor the engine: an emitted artifact, a forced enumeration, a call with controlled input, and a record that makes staleness visible. Treating the engine as the only real close is what makes the cheap repairs invisible — and, per §5's prediction, building the engine alone would repair position and leave the other four kinds intact.

---

## Next Actions

### MUST

- **What:** Ship R1 — a per-document term list produced before drafting, with **every enumeration keyed to a detectable form** and none to a semantic judgment.
  **Who:** the comprehenslate skill (`SKILL.md` Step 5 and `translation_method.md`).
  **Gate:** condition-bound — before the next translation run.
  **Why:** addresses the largest error kind by converting most of it from detection into prevention; and the form-keyed restriction is what makes it survive the objection that it just moves the noticing problem one step back.

- **What:** Ship R3 — a post-revision re-run rule **with a carrier**: verification emits a record naming the draft-state it verified, so an edit makes the record visibly stale.
  **Who:** the comprehenslate skill.
  **Gate:** condition-bound — before or alongside R4, never after.
  **Why:** repairs the time property, and without it R4 manufactures the exact edit-pressure that produced one of the nineteen errors.

- **What:** Ship R4 — a source-blind reader as a named step, split into a mechanical in-call enumeration and an evaluative separate call holding only the English draft, with **question-list output and no edit authority**.
  **Who:** the comprehenslate skill plus whatever routes its output back into a source-present context.
  **Gate:** condition-bound — after or with R3.
  **Why:** it is the only repair that reaches the error class nothing else can detect, and it is the cheapest call in the method.

- **What:** Run the validation experiment — translate one comparable section of the same work twice, once with R1–R4 in force and once without, counting errors by gap kind. **Fix the counting protocol before translating, not after.**
  **Who:** the user, against the calibration corpus.
  **Gate:** observable — after R1, R3 and R4 exist.
  **Why:** every magnitude claim in this finding is unmeasured and honestly quarantined, and this is the only route that lifts the quarantine. It is also the revival trigger for two deferred items. Run it even if the repairs look obviously right — obviousness is what the July fix had.

### COULD

- **What:** Ship R2 — a seven-row policy-conformance enumeration that requires each policy's rendering to be **written out**, not judged.
  **Who:** the comprehenslate skill.
  **Gate:** condition-bound — resolvable once the placement question is settled (inside the existing verification pass, or as a new pass).
  **Why:** repairs the specification property; the only error class with no possible catcher anywhere in the method acquires one, and three currently-undecidable items become decidable.

- **What:** Declare checks as tuples — `(specification, vantage, instrument, position, invalidated-by)` — rather than as sentences.
  **Who:** the comprehenslate skill's method file.
  **Gate:** condition-bound — whenever a check is next added or edited.
  **Why:** a sentence with no stated vantage looks complete; a tuple with an empty slot does not. This is what makes the five properties auditable rather than merely described.

- **What:** Show the seven policy defaults at configuration time instead of applying them silently.
  **Who:** the comprehenslate skill, `SKILL.md` Step 4.
  **Gate:** condition-bound — alongside R2.
  **Why:** an honorific policy was violated in a run where the policy had never been shown to anyone. One line per policy in the configuration echo that already exists for the eight axes.
  **Depends-on:** MUST item "Ship R1." Not gated — this is independent of R1 and can proceed alone.

- **What:** Write down the division of labour — who occupies which vantage, whether a re-scan is a step or a request, and what happens when nobody asks.
  **Who:** the project's authoring documents, not the runtime text.
  **Gate:** condition-bound — after R4 exists, since R4 is what would occupy the currently-unstaffed position.
  **Depends-on:** MUST item "Ship R4." This COULD is GATED — do not act until R4 resolves, because what remains unstaffed depends on what R4 takes over.
  **Why:** an unnamed dependency cannot be maintained or handed to anyone else.

### DEFERRED

- **What:** Build R6 — the engine that runs the method's passes as physically separate calls with real intermediate artifacts.
  **Gate:** condition-bound — after R1, R3 and R4 are in force and the validation experiment has run.
  **Why (if revived):** it repairs the position property systematically rather than per-check. **With the warning this finding stakes its credibility on:** built first, with the others deferred, it will repair position and leave vantage, specification, instrument and time untouched — the same shape as the July fix, one level up. If that prediction turns out wrong, this finding's central claim is in trouble, and that is the point of stating it.

- **What:** Build R5 — a fresh-context adversarial reader for coverage beyond the specific target-only checks.
  **Gate:** condition-bound — once the constructed-versus-instructed question is settled (see Research Frontiers).
  **Why (if revived):** it generalises the vantage repair beyond referring expressions.

- **What:** Shrink the method to what a single call can enforce, and state plainly what it does not catch.
  **Gate:** observable — if the validation experiment shows no measurable reduction from R1–R4.
  **Why (if revived):** a smaller method that delivers all of what it claims may beat a larger one that claims everything and enforces a fraction. 3,489 lines of instruction re-paid every run is a real cost. This is the honest fallback, and it argues against expanding the user's own build — which is why it stays on the record rather than lapsing quietly.

---

## Reasoning

### What was rejected, and why

**A single root cause.** The most rhetorically satisfying version of this account would fold everything under the enforcement gradient: every gap was knowable, several were written down, all persisted because they sat at the weakest position. This was tested and **partially refuted**. Three gaps survive a move to the gradient's strong end — specification (a check that does not exist is not enforced by being run as a separate call), time (a rule that is not stated does not run at any position), and vantage (a separate call still containing the source is the strong position at the wrong vantage). The single-cause account was rejected because it cannot represent those three, and because the tidier version would have made exactly the error the July fix made.

**"Independent variation, demonstrated by controlled pairs."** This was the finding's originally-claimed warrant for the five properties, and it was **killed** during adversarial review. Checking each comparison literally: one holds cleanly (time), one is not a comparison at all (specification — a non-existent check has no values on any axis), and three are confounded. The most damaging confound was also the most useful discovery — see below. The warrant was replaced with the weaker and true claim: **independent failure**, which all five support.

**Attributing the re-scan effect to the separate turn alone.** This was the account's original reading of its own strongest evidence, and adversarial review **overturned it**. The user's request supplied three property-fixes, not one — a fresh turn, a check against the policy file and configuration, and a sentence-by-sentence granularity. The corrected attribution is better evidence than the original claim: a person with no framework repaired three of five properties in one sentence.

**R1 as originally specified.** The lead repair said *"list every polysemous term."* The objection — that this requires the same noticing whose absence it is meant to fix, and therefore recurses one step back — was raised in review and had not been raised by the account against itself. It is fatal to the specification as written, and it is answered by a restriction rather than a hope: enumerations keyed to detectable form, never to a semantic judgment. This was the single strongest objection available to the whole account.

**R3 without a carrier.** The re-run rule was originally a sentence. Review noted that a sentence in a runtime file sits at the weakest position on the very gradient this finding is about, which would have made the finding's own remedy set the next instance of the pattern it diagnoses. Rejected in that form; kept with a carrier.

**Chunk size as an explanation.** Refuted by measurement — both chunks ran at roughly half the stated limit, so the transformation-load lever was not binding. Dismissed on evidence, not on judgment.

**Missing knowledge as an explanation.** Refuted by reading the reference material: the matching principle exists for most of these errors, correctly worded, and was read into context. This falsification is not a disposal — it is what forces the account's actual claim, that what was missing was a firing condition rather than a principle.

**Reorganising the reference files.** Probed and found empty. Their content is already correct; reorganising them changes nothing about whether a principle fires.

**More or clearer instruction in the method file.** Excluded as the terminal remedy, because it is precisely the intervention that was tried in July and failed in August. Prose is not forbidden as part of an answer; proposing it as *the* answer would have the finding recommending the intervention whose failure it is diagnosing.

**Agent capability as a terminal answer.** Excluded by the user's own framing, and enforced by the substitution test rather than by good intentions — every limit claim was restated with a human translator as subject, and one candidate claim was rejected by that test.

### What held, and why

**The five-property frame** held against the objection that any N-way decomposition produces the same rhetorical effect. It held because a rival decomposition (who checks / what / how carefully / how often / with what authority) does not sort the errors — "how carefully" absorbs everything — and because this frame classifies a check nobody has run, which a purely retrospective story cannot do.

**Vantage as a real property, distinct from who is checking**, held against the objection that it merely relabels a personnel fact. It held because the same checker at two vantages has different detection capability, and a different checker at the same vantage has the same limitation. What determines detection is what is present in the checking context.

**The substitution test** held, and was strengthened by being required to exhibit a rejection. A test where every candidate passes is indistinguishable from a licence; showing it reject a convenient claim is what makes it a screen.

**"Replace judgment with construction"** emerged only when the surviving repairs were examined together, and it survived its own review: it is grounded in five positive instances and one negative one, it is falsifiable, and it is itself construction-shaped rather than exhortation-shaped.

### A note on this inquiry's own method

This is a model-executed, prose-specified process diagnosing a model-executed, prose-specified process. The mitigation used throughout was external anchoring — every decisive claim cites a quoted file, a quoted message, or a measurement, rather than a structural argument about what something must contain. The residual weakness is real and unfixable from inside: a claim that neither this account nor its review thought to check remains unchecked, and neither would know. §9 names the four claims most worth an outside look.

---

## Open Questions

### Monitoring

- **Whether the five properties are exhaustive.** They are five *observed* properties, not five necessary and sufficient ones. The productive trigger is an error that refuses to classify; none has appeared. Observable across the next several translations.
- **Which enumerated facts are corpus-constant rather than per-document.** The honorifics, the seven policies, and much of the recurring Ottoman vocabulary are facts about a multi-volume work, and a per-document term list re-derives them each time with the chance of failing differently each time. Observable once R1 has run three or more times — the repetitions answer the question for free.

### Blocked

- **How much any repair is worth.** Blocked on the validation experiment. Every magnitude in this finding is unmeasured, and the experiment is the only route that lifts the quarantine.
- **Whether "detectable form" is actually detectable for this corpus.** R1's whole restriction rests on Arabic- and Ottoman-derived word forms being identifiable morphologically rather than semantically. Asserted here, untested, and directly load-bearing. Blocked on R1 existing.
- **The false-positive rate of a source-blind reader.** A reader that flags resolvable references creates edit-pressure on correct text, which is the regression mechanism. Unknown, and it determines how much R3 has to carry. Blocked on R4 existing.

### Research Frontiers

- **Whether an adversary can be constructed adversarial rather than instructed to be.** §6 establishes that an instructed source-blind stance does not occupy the vantage. The same question applies to adversarial review generally — including to this inquiry's own review step, which is instructed rather than constructed. No known path.
- **Configuration-licensed drift.** Nothing currently distinguishes a domestication licensed by the configured fidelity setting from an unlicensed flattening, which means three of the nineteen items are undecidable as errors *in principle* rather than merely unmeasured. The configuration's calibration document defines a level, not a decision procedure, and the check needs the latter.
- **Nothing in the inquiry corpus tests whether a shipped fix took.** The July fix was written, shipped, and its failure discovered a month later only because a new failure prompted a new inquiry. This is the same shape as the finding itself, one layer up — either the account's most interesting extension or a coincidence of framing, which is what makes it a frontier rather than a claim. Deliberately not folded into this finding; it is a different layer, and this account is already at its committed depth.

### Refinement Triggers

- **If the validation experiment shows no measurable reduction from R1–R4**, the "shrink the method to what it can enforce" alternative revives and this finding's additive direction re-opens.
- **If the engine (R6) is built before R1, R3 and R4, and the non-position error kinds do *not* recur**, the central claim of §5 is falsified and the five-property account requires re-examination.
- **If an error appears that refuses to classify into the five kinds**, the exhaustiveness question moves from Monitoring to an active re-opening of §2.
- **If `tools/structural_check.sh` is built and the inquiry pipeline's handoff quality visibly changes**, the instrument-axis claim gains a fourth instance from a different domain, and §9's confidence split should be revisited.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
hmm, why u made these errors u think?? what was missing in our process that these errors were made? i understand you are ai  but i am wondering what was missing, think really deep and try to uncover the most core issues...
```

</details>
