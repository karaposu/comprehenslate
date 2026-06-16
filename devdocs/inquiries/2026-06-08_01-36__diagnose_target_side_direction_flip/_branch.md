# Branch: diagnose_target_side_direction_flip

## Question

**Context.** In the translation of `mytrasnlations/asayi_musa/4_mesele.md` produced under config A1=conversational / A2=lay / A3=outsider-to-acquainted / A4=casual / A5=lightly-domesticated / A6=standard / A7=standard / A8=none (using `harmony_layer.md`, `notes.md`, `advanced_principles.md`, and the canonical Layer 1 spec at `config_base_source.md`), the Turkish phrase `Herkesin İman mukabilinde... Davası başına açılmış` was rendered as `For every person, set against his Faith, a Case has been opened...`. The Turkish `mukabil` means *facing / in exchange for / put up against [as the second side of a barter or stake]* — Nursi's sustained legal-courtroom metaphor: Faith is the *stake* each person puts up, with the eternal estate as the prize. The English `set against his Faith`, however, naturally reads as *in opposition to / hostile to his Faith* — which is the OPPOSITE of the source meaning. The target-language rendering opened a directional reading (oppositional) that the source did not admit (the source's direction was exchange-for / barter-against / counter-stake). The error is not at Pass 1 Meaning Lock — `mukabil` was understood. The error is at Pass 3 Target Reconstruction — the chosen English phrase admits an opposite reading the source doesn't admit.

**The question.** Diagnose what mechanism in the existing translation framework was at fault for not catching this failure, and propose a prevention mechanism. Specifically the user asked: is the issue with `harmony_layer.md` or `notes.md`? Which part?

State the question:

- **Subject.** The framework mechanism (in `harmony_layer.md`, `notes.md`, `advanced_principles.md`, and/or the canonical Layer 1 spec) that *should have* caught the target-side directional-flip ambiguity in `set against his Faith` but did not.
- **Action.** Diagnose + propose prevention (gap identification + concrete addition or refinement).
- **Level.** Framework-artifact level (cross-cutting harmony_layer.md, notes.md, advanced_principles.md, canonical Layer 1 spec) — specifically diagnosing whether the existing 3-Pass methodology + Tier 1-4 system + 5 always-on policies + Pass-3 target reconstruction principles catch this case.
- **Observation targets** (multiple, preserved separately):
  1. **NAME the failure mode** — what KIND of failure this is. Candidate names: "target-side accidental polysemy"; "target-rendering false-friend"; "direction-flip risk"; "target opens a reading source doesn't admit"; "target-side opposite-sense leakage." Settle a canonical name.
  2. **STRUCTURAL DIFFERENCE from existing principles** — explicitly distinguish from: (a) source-side polysemy preservation (notes.md "local-construction trump"); (b) multi-meaning preservation policy (Layer 2 always-on policy in canonical spec); (c) Pass 1 Meaning Lock semantic-content preservation (harmony_layer.md hard constraint); (d) Tier 1 cause-effect chaining preservation (harmony_layer.md); (e) hasr/word-order encoding (notes.md). The failure here is INVERSE to source-side polysemy: source had a CLEAR sense; target rendering introduced ACCIDENTAL ambiguity in the target language. Existing principles address source→target preservation; the missing principle addresses target-side ACCIDENTAL ADDITION of an unintended sense.
  3. **LOCATE the gap** — answer the user's explicit question: which artifact and which part has the gap? Candidates: (a) `harmony_layer.md` hard-constraints section (currently lists "anything that changes semantic content is forbidden" but doesn't explicitly cover "target rendering admits a sense source doesn't admit"); (b) `harmony_layer.md` 3-Pass methodology (Pass 3 Target Reconstruction has rules for HOW to use target-language tools but no explicit DON'T-let-target-open-opposite-senses check); (c) `notes.md` polysemy section (covers source-side polysemy but inverse case missing); (d) `advanced_principles.md` (none of the listed principles address this); (e) canonical Layer 1 spec Layer 2 policies (5 policies enumerated — multi-meaning preservation, register-alternation, polysemy-via-local-construction, nazm preservation, no-smoothing — none cover this case). Likely the gap is in MULTIPLE places; the user's question about harmony_layer.md vs notes.md needs a structural answer: which one is the right home for the fix?
  4. **WHY did the 3-Pass methodology not catch it at Pass 3** — Pass 3 says "you may change HOW a meaning is expressed, but never WHAT meaning is expressed." The translator (me) interpreted "set against" as a valid HOW-expression of the WHAT (the exchange-for meaning). But the resulting English actually CHANGED the WHAT for English readers — admitted "opposed to" as a valid reading. So Pass 3's hard constraint failed to fire because its check is "did the translator preserve the source meaning?" not "does the target rendering open an unintended sense?" The check direction is wrong: it tests Pass 1→Pass 3 preservation (source-side), not target-side accidental addition.
  5. **PROPOSE THE PREVENTION MECHANISM** — concrete text addition to the right artifact(s). Likely a new principle in `notes.md` (target-side accidental polysemy as counterpart to source-side polysemy preservation) AND a hard-constraint refinement in `harmony_layer.md` (target rendering must not admit a sense — especially an opposite one — that source doesn't admit). May also propose a 6th Layer 2 always-on policy in the canonical spec ("target-side false-friend prevention") with v1.1 increment.
  6. **TEST/CHECK procedure** — concrete check the translator (AI or human) applies at Pass 3: "Read the target rendering as if you didn't know the source. Does it admit a reading the source doesn't admit? Especially: does it admit the OPPOSITE direction (in-favor-of vs against, in-exchange-for vs opposed-to, with vs contra)? If yes, re-render."
  7. **SCOPE CHECK on the broader pattern** — is the "deathbed-room" failure (the second case discussed in the conversation, where `sekerat` = death-agonies got rendered as a physical location compound) an instance of the same pattern or a different failure mode? Brief check; if different, flag for separate inquiry.
- **Deliverable shape.** Diagnosis with reasoning (named failure mode + gap location + why-existing-principles-missed-it) + concrete prevention proposal (proposed text addition + which artifact it lives in + how it composes with existing principles + check procedure for translators).

**State the question.** **For the `set against his Faith` translation failure where the target English rendering opened an opposite-direction reading (in opposition to) not present in the Turkish source `İman mukabilinde` (in exchange for / put up as stake), diagnose what KIND of failure mode this is (named), locate the gap in the existing framework (harmony_layer.md / notes.md / advanced_principles.md / canonical Layer 1 spec — answering the user's specific harmony_layer-vs-notes question), explain why existing principles (source-side polysemy / Pass 1 Meaning Lock / Tier 1-4 / 5 Layer-2 policies) didn't catch it, and propose a concrete prevention mechanism (text addition + location + check procedure) that prevents recurrence of target-side direction-flip ambiguity?**

## Goal

- **Criterion.** Precise diagnosis (named failure mode + specific gap location + clear gap analysis) + concrete prevention proposal (proposed principle text + which artifact + how it composes with existing principles + translator check procedure). Should answer the user's specific harmony_layer.md vs notes.md question structurally.

- **Use case.** The user will likely apply the fix to the framework (refine harmony_layer.md hard constraints; add new principle to notes.md; potentially increment canonical spec v1.0 → v1.1 with a new Layer 2 policy) so future translations catch similar cases automatically.

- **Desired outcome.** Framework gains a missing principle (or refines existing) that catches target-side directional-flip / accidental-polysemy ambiguity. Translator (AI or human) has a concrete check at Pass 3 that fires for this case.

- **What would fail.**
  - Generic "be more careful at Pass 3" answer (not actionable).
  - Answer that doesn't locate the gap in a specific file part.
  - Answer that names the failure mode but doesn't propose a concrete prevention mechanism.
  - Answer that confuses this case with source-side polysemy (they are STRUCTURALLY INVERSE).
  - Answer that doesn't acknowledge the user's specific harmony_layer-vs-notes question.
  - Conflating "set against his Faith" (target-side direction-flip) with "deathbed-room" (over-naturalization of source technical term) — these are DIFFERENT failure modes.

## Source Input

```text
we discussed 

For every person, set against his Faith,                                                                                                  
                                                                                                                                            
                                                                                                                                            
  what this means ?                                                                                                                         
                                                                                                                                            
  (dont make any edits just tell me)                                                                                                        

⏺ The Turkish source is Herkesin İman mukabilinde... bir tarla ve mülkü kazanmak veya kaybetmek Davası başına açılmış.

  The phrase doing the work is İman mukabilinde. Mukabil means facing, in exchange for, in return for, put up against — like the second side
  of a barter or a stake in a bet. It does not mean "opposed to / hostile to."

  So Nursi's intended sense is:
  
  ▎ With his Faith put up as the stake — Faith being what each person is offering against the prize — a Case has been opened in which he 
  ▎ either wins or loses an eternal estate the size of the Earth.

  The legal-courtroom metaphor is sustained: there's a Case, there's a prize (the eternal estate), and there's the currency you put up as
  your side of the trade — that currency is your Faith. If you have valid Faith (the "Faith-Certificate firmly in hand," as the next
  sentence says), you win the estate. If you don't have it, you lose.

  My English set against his Faith is ambiguous and that's a real problem — in English set against more naturally reads as opposed to / 
  hostile to, which is the opposite of what the Turkish means. A cleaner rendering of the same meaning would be something like with his 
  Faith put up as the stake or with his Faith as what he stakes against the prize or Faith being the price-tag of — anything that keeps the
  in-exchange-for sense rather than letting the reader hear in-opposition-to.

i want to identify what mechanism is fault of not catching that...  and how can we prevent further similar cases..
is the issue with harmony_layer.md or notes.md ? what part?
```

## Scope Check

Question covers goal: YES.

**Specific-vs-pattern check.** The "set against his Faith" case is the SPECIFIC example; the inquiry addresses the BROADER PATTERN of "target-side directional-flip / accidental-polysemy / false-friend" failures. The user's framing is diagnostic (identify the mechanism + prevent further similar cases), so the broader-pattern reading is correct.

**Companion failure case (deathbed-room).** A second failure case was discussed in the conversation just before this MVLw invocation — "deathbed-room" for `sekerat`. The user did NOT include that case in the MVLw args. Treating the inquiry as scoped to the SET-AGAINST case only. The deathbed-room failure is structurally DIFFERENT (over-naturalization of a source technical term; failure to use KEEP-SOURCE-TERM-WITH-GLOSS for a load-bearing specialist term — `sekerat` is a state/moment, not a location, and the English compound `deathbed-room` doesn't exist). A frontier flag will note this for a separate inquiry.

**Decoupling.** The canonical Layer 1 spec v1.0 + harmony_layer.md + notes.md + advanced_principles.md + the 4_mesele_en.md translation finding are all referenced but NOT being synthesized — the inquiry is diagnostic, examining whether existing principles caught this case. Not a Synthesis Trigger.
