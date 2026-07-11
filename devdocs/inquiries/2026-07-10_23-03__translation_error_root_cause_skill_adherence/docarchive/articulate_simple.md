# Articulate-Simple — Root-Cause Diagnosis of Translation Errors vs SKILL Adherence

## User Input

The user is critiquing an English translation (of İKİNCİ HÜCCET-İ İMÂNİYE from Said Nursî's Asa-yı Musa) produced under an explicit TranslationConfig (A1=conversational, A2=lay, A3=outsider-to-acquainted, A4=casual, A5=lightly-domesticated, A6=standard, A7=standard, A8=none), governed by the SKILL folder (config_base_source.md, policy_config_base_source.md, translation_principals.md, advanced_principles.md, harmony_layer.md, notes.md). Seven specific defects were named:

1. "allegorical" — too hard given A1=conversational.
2. "…allegorical dialogue and an imagined debate, giving the mute tongue of a thing's own condition the form of actual speech" (from "basit avamın fehmine gelecek bir muhavere-i temsiliye ve bir münazara-i faraziye tarzında ve lisan-ı hali, lisan-ı kal suretinde söylemiştim") — "weird and wrong"; lisan-ı hal = language of body/state, lisan-ı kal = spoken/voiced language; the rendering is "gibberish"; and "basit avamın fehmine gelecek" (= "that would come to the understanding of the simple common folk") was dropped entirely (omission).
3. "figure" — bad for "bir şahıs" (→ personage / entity / character).
4. "wants to be Lord over some one thing among the beings of the world" — "some one thing among" reads badly.
5. "no one lacking a boundless wisdom and an all-embracing knowledge can poke a finger into our work" — hard to parse (nested negation).
6. "work" — bad for "iş" in "sen benden iş bulamazsın"/"iş bulacağım" (iş = attention/care/foothold, not literal work).
7. "secondary causes" — bad/over-interpreted for "esbab".

Actual question: *"lets dive deep into why this translation had these mistakes. was SKILL folder content followed well or not, what happened?? lets dive deep."* → a ROOT-CAUSE DIAGNOSTIC inquiry, not a fix request.

---

## Stage 1 — Itemize

**count = 1.**

**item-1:** *"Diagnose why the translation produced these errors, and whether/where the SKILL folder's content was followed or broke down."*

Keep-together applies. The seven named defects are **evidence-instances feeding one diagnostic ask**, not seven independent work-items — the user's operative sentence ("why this translation had these mistakes… was SKILL followed… what happened") is a single diagnostic question the seven defects supply data for. Splitting into seven would fabricate independent items where the user framed one investigation. (Asymmetric-failure bias toward keep-together holds cleanly here.)

---

## Stage 2 — Meta-question + MQA (item-1)

### MQ1 — verdict-axis: *"What is the user asking for?"*
**identified-ambiguities-list:**
- `[per-error-diagnosis (7 separate causal accounts) / systemic-diagnosis (one underlying process-failure that produced all 7) / both (per-error accounts + the common thread)]`
- `[diagnosis-only / diagnosis + explicit adherence-verdict ("was SKILL followed": yes/no) / diagnosis + prevention-mechanism / diagnosis + SKILL-or-process repair]`
- `["was SKILL folder content followed" reads three ways: (a) was it READ, (b) was it correctly APPLIED per-principle at render time, (c) is the SKILL itself DEFICIENT (contains the principle but doesn't enforce it) — or all three]`

### MQ2 — context-need axis: *"What context does the response need that isn't in the statement?"*
**identified-ambiguities-list:**
- **verdict** (what must be pulled in): the actual SKILL folder principles + the produced translation + the source Turkish + the resolved config — all present in warm session context, so the diagnosis can check each error against the governing text rather than assert.
- **kinds** (what type of context): the *mapping* from each error-class to the specific SKILL clause that should have prevented it — e.g. A1=`conversational` vocabulary-exclusions & syntactic-complexity ceiling in `config_base_source.md`; the no-smoothing / Tier-1 no-omission commitments in `harmony_layer.md` + the 5 always-on policies; the polysemy / local-construction memory; where `lisan-ı hal`/`lisan-ı kal` is documented.
- **stance** (posture the answer takes): honest fault-finding vs self-justification. The user's register ("so bad", "gibberish", "what happened??") signals they want candid fault attribution, not defense of the choices.

### MQ3 — intent-axis (WHAT): *"What is the user trying to accomplish?"*
**identified-ambiguities-list:**
- `[understand-this-instance (know why THIS passage failed) / prevent-recurrence (extract a reusable render-time mechanism for future chunks) / repair-the-SKILL (edit config/principles/SKILL.md so it self-enforces)]`
- action-endpoint: `[a written diagnosis artifact / a changed translation-process (a QA/verification pass) / changed SKILL files]`

### MQ4 — boundary-axis: *"What is the user explicitly excluding?"*
**identified-ambiguities-list (with NOT-items):**
- `[NOT (for this ask): re-translate/repair the passage now — the operative verb is "dive deep into why", diagnosis not correction; producing the fixed text is a plausible follow-on but out of THIS ask's stated scope]`
- `[NOT: re-litigate whether the 7 defects are real — the ask presupposes them valid and asks for their cause]`
- `[NOT asserted: the config values themselves are wrong — the user targets the *rendering under* the config, not the config choice]`

### MQA
**reconcile.** MQ1's "diagnosis-only ↔ diagnosis+fix ↔ diagnosis+repair" and MQ3's "understand ↔ prevent ↔ repair" span **one joint axis: OUTPUT-REACH beyond diagnosis** — how far past the causal explanation the deliverable should travel (pure root-cause understanding → reusable prevention lesson → concrete SKILL/process repair). The joint axis is confidently identifiable, so MQA folds both overlapping identifications into it. This OUTPUT-REACH axis is the **primary preserved openness** the downstream pipeline must span; it is not adjudicated here.

---

## Stage 3 — Deconstruct + MultiDepth (item-1)

### Deconstruct
**tuple = (deliverable, kinds, bounds):**
- **deliverable:** a diagnostic analysis (a root-cause *understanding* artifact) — not code, not a re-translation.
- **kinds:** causal explanation (per-error + systemic) + an adherence verdict (read / applied / SKILL-deficient) + optionally a prevention or repair proposal (gated by the OUTPUT-REACH axis).
- **bounds:** the 7 named errors × the SKILL folder's actual content × the translation *process* that was run; scoped to this İKİNCİ HÜCCET translation and the SKILL's role in it.

**Late-split check:** the deliverable is ONE diagnosis covering 7 error-instances (data-points inside a single analysis), not 7 diagnoses. No late-split; count = 1 confirmed.

### MultiDepth
**literal-statement:** *"Dive deep into why this translation had these mistakes. Was the SKILL folder content followed well or not — what happened?"*

**purpose-motivation-ambiguities (WHY-axis):**
**identified-ambiguities-list:**
- `[operational: make the NEXT translation chunk measurably better]`
- `[systemic: the SKILL folder IS the product being built — the user needs to know whether the system reliably enforces its own principles, because a SKILL that isn't followed is worthless]`
- `[assurance/trust: verify the translator (the AI) is genuinely operating from the SKILL rather than default-LLM-translating and name-dropping the config]`
- `[general-lesson: locate the declarative-knowledge → procedural-application gap as a transferable finding about the whole comprehenslate approach]`

---

## Stage 4 — Rephrase — Considered Articulations (item-1)

Bounded by: deliverable = diagnostic analysis; ambiguity-dims = {OUTPUT-REACH: understand/prevent/repair; adherence-meaning: read/applied/SKILL-deficient; per-error vs systemic}; NOT-list = {don't re-translate now; don't re-litigate defects}; substrate = warm (SKILL folder + translation + source Turkish + config all in context).

1. **Per-error adherence diagnosis.** For each of the 7 defects, name the specific SKILL principle that should have caught it and explain why it didn't fire — concluding, per error, whether the SKILL was read-but-not-applied, misapplied, or silent on the point.
2. **Systemic root-cause diagnosis.** Identify the single underlying process-failure (candidate: no post-draft verification pass re-checking the draft against the config's register/syntax exclusions and the no-omission policy) that produced all 7 as symptoms; judge whether the SKILL *contains but fails to enforce* the antidotes.
3. **Diagnosis + prevention mechanism.** Diagnose, then propose a concrete render-time/QA verification pass (a checklist bridging principle → clause-level decision: register-exclusion check, no-omission check, word-sense-in-context check, target-naturalness check) to add to the workflow.
4. **Diagnosis + SKILL-repair proposal.** Locate where in the SKILL folder the enforcement gap lives (SKILL.md's single-pass "produce the translation" step; config_base_source register-exclusion enforcement; the no-smoothing/no-omission policies; the polysemy memory) and propose edits that would make the SKILL self-enforcing.
5. **Adherence audit (verdict-first).** Deliver a verdict on whether the SKILL was followed — separating (a) read, (b) applied-per-principle, (c) SKILL-deficient — with cited evidence per error, and no repair beyond the verdict.

---

## Self-Assessment

**LAYER 1 self-check (single LIGHT pass):**
- Mode 1 (premature split): not fired — count=1, keep-together justified.
- Mode 2 (late multi-item): not fired — Deconstruct confirms one deliverable over 7 data-points.
- Mode 3 (MQ extension): not fired — four canonical axes only.
- Mode 4 (per-op missing): not fired — all operations emitted.
- Mode 5 (MQ2 missing verdict/kinds/stance): not fired — all three present.
- Mode 6 (MQ2 kinds/stance absent): not fired — both present.
- Mode 7 (2-shape violation / commitment): not fired — ambiguities preserved as lists; the tempting commitment ("the cause IS the missing verification pass") is held as a *variant/candidate* (art. 2), not adjudicated.
- Mode 8 (WHAT/WHY conflation): not fired — MQ3 = action-endpoints (understand/prevent/repair); MultiDepth = motivations (operational/systemic/assurance/lesson).
- Mode 9 (articulation drift): not fired — all 5 variants preserve diagnostic-deliverable, span the dims, honor NOT-list, stay in substrate.

**Fires: 0. Perceived friction: low–moderate** (the OUTPUT-REACH fork — diagnose only vs also prevent/repair — is a genuine openness, but cleanly captured as the joint MQA axis rather than a source of friction).

**Primary preserved openness for downstream:** the **OUTPUT-REACH axis** (understand → prevent → repair) and the **adherence tri-reading** (read / applied / SKILL-deficient). The pipeline should span these, not collapse to one.

## Verdict

**HIGH-PROCEED** — clean self-check, low–moderate friction; the diagnostic framing is well-formed and its central openness (how far past diagnosis to reach; what "followed the SKILL" means) is explicitly preserved for the pipeline to span.
