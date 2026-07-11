# Sensemaking — Why the translation failed & whether the SKILL was followed

## User Input

`_branch.md`. Warm-settled anchor: errors stem from a declarative-knowledge ↔ procedural-enforcement gap (SKILL contains antidote to 6–7 of 7 but no render-time enforcement gate). Inputs: articulate_simple.md, surfacing.md (10 governing clauses + confirmed-absent regions), articulate_warm.md (non-severe content-conflict = 7 errors span a severity spectrum). Save to `sensemaking.md`.

---

## SV1 — Baseline Understanding

The translation had 7 errors even though a detailed SKILL governs it. Initial read: "I read the SKILL but didn't apply parts of it when actually rendering." (Carelessness framing.)

---

## Phase 1 — Cognitive Anchor Extraction

**Constraints**
- **C1** — Config mandated accessibility: A1=conversational (excludes dense-academic vocab + nested syntax), A2=lay (layman word-choice), A4=casual, A5=lightly-domesticated. These are binding, not advisory.
- **C2** — `harmony_layer.md` Pass-1 Meaning Lock: "Removing information present in the original is FORBIDDEN" — a hard constraint, violated by err-2a.
- **C3** — The "5 always-on Layer-2 policies" fire "regardless of any single axis setting" — including no-smoothing, polysemy-via-local-construction, register-alternation.
- **C4** — A8=none and the workflow ran NO QA/verification step; nothing re-checked the draft.

**Key Insights**
- **K1** — The SKILL demonstrably **contains a specific governing clause for ≥6 of 7 errors** (surfacing confirmed). NOT a knowledge gap; the knowledge was present in context.
- **K2** — Each error maps to a principle that operates at **verification granularity** — a check-the-draft-against-a-standard move (register-exclusion word-audit; source↔draft omission-diff; per-word sense-disambiguation; re-read-the-English-as-English), NOT a generate-forward move.
- **K3** — `harmony_layer.md`'s **3-Pass methodology (Meaning Lock → Harmony Map → Target Reconstruction) names exactly the passes that would catch these** — but `SKILL.md` Step 5 collapses translation into ONE "produce the translation" emit. The passes ran "in spirit" (one integrated pass), not as discrete gated steps.
- **K4** — The errors are the **systematic signature of fluency-first generation**: elevated/literary vocab ("allegorical", "mute tongue"), smoothing-compression that drops a clause ("basit avamın fehmine gelecek"), first-dictionary-sense word-choice ("work" for *iş*), nested literary syntax ("no one lacking…can"). This is precisely the "natural target-language fluency bias" that the SKILL's **no-smoothing policy explicitly names as its counter-bias target**.
- **K5** — Severity spectrum (from warm): 5 are clear clause-violations (err-1, 2a, 4, 5, 6); 2 are defensible-but-off-register judgment calls (err-7 *esbab*; the hal/kal-meaning portion of err-2b).

**Structural Points**
- **S1** — Two distinct failure *locations*: (a) render-time non-application (principles didn't fire per-clause during generation), (b) no post-draft verification (nothing checked after). Related but distinct.
- **S2** — SKILL architecture = huge declarative reference files + a thin workflow whose "apply" step (Step 5) is monolithic. The declarative→procedural bridge is absent.
- **S3** — The config's own "Per-axis order of consultation" ("read A1/A5/A6/A7 at EVERY reference/choice/passage") is a procedural instruction that was present but **unverifiable / unverified** in execution.

**Foundational Principles (assumptions to test)**
- **F1** — (assumed) "Reading the SKILL fully = applying it." Suspect FALSE: reading loads declarative knowledge; applying needs per-decision retrieval + a check.
- **F2** — (assumed) "A capable LLM with the principles in context will naturally honor them." Suspect PARTIALLY false: generation-shaped principles were honored; verification-shaped ones were not, because generation doesn't self-audit.

**Meaning-Nodes**
- **M1** declarative↔procedural gap · **M2** fluency bias (project vocabulary — in the no-smoothing policy) · **M3** verification-shaped vs generation-shaped principles (the discriminator) · **M4** severity spectrum.

### SV2 — Anchor-Informed Understanding
Not a knowledge gap and not mere carelessness: the errors are the predictable output of fluency-first single-pass generation. The SKILL's antidotes exist but are **verification-shaped** — they need a post-draft audit to fire, which the workflow never runs.

*Meta-inspection (H4 concept-names, H5 examples):* "fluency bias" is validated project vocabulary (no-smoothing policy). "Verification-shaped vs generation-shaped" is loop-coined — but it is **structural, not a proxy**: it predicts WHICH errors happened (every verification-shaped principle failed; every generation-shaped one held). The 7 errors are motivating examples of a wider pattern (tested in Phase 3, Ambiguity 3), not the whole problem.

---

## Phase 2 — Perspective Checking

- **Technical/Logical.** Pipeline ran: read-refs → single-pass translate → emit. Principles requiring a check-against (register-exclusion, omission-detection, sense-disambiguation, naturalness-reread) had **no execution point**. Mechanically inevitable.
- **Human/User.** The user (SKILL owner) is running, by hand and after the fact, exactly the verification pass the workflow lacks. Their critique *is* the missing QA step. New anchor: the fix already exists as a human behavior; it needs to be internalized into the process.
- **Strategic/Long-term.** If the SKILL is the product, "read it and translate well" is unreliable — it reproduces the same failure on every chunk, so the SKILL's detailed principles never reach the output. Strategic fix = an enforcement point, not "try harder."
- **Risk/Failure.** Risk of mis-diagnosis: if the true cause were attention-saturation or LLM incapacity, a verification pass wouldn't help. → tested in Phase 3.
- **Resource/Feasibility.** A full re-verification is token-costly; a **scoped** checklist (register-exclusion; source↔draft omission-diff; word-sense flags; naturalness reread) is cheap vs a re-translation. Feasibility supports the prevention reach. New anchor: the pass must be **scoped/narrow**.
- **Definitional/Internal-Consistency.** By the SKILL's OWN Rules (Rule 1 "always read all reference files" ✓; Rule 5 "Tier 1-2 non-negotiable" ✓ — structure largely preserved), the SKILL WAS "followed." But those Rules **do not mandate** the verification-shaped checks. So the SKILL is internally consistent yet **incomplete**: its detailed config *promises* accessible/faithful/natural output, but its workflow *structure* delivers no enforcement — a definition whose stated purpose outruns its mechanisms. **This is a SKILL deficiency finding, not merely user error** (guards against Status-Quo Bias).
- **Self-Reference (H8).** I am evaluating my own failure. External grounding used throughout: the literal source ("basit avamın fehmine gelecek" is *in* content0020.xhtml and *absent* from my output — a verifiable diff, not opinion); the literal config (A1=conversational literally lists dense-academic exclusions); the user's independent critique. The diagnosis rests on text-diffs, not self-report.
- **Phase/Calibration-State.** comprehenslate is early-stage (calibration-corpus phase). The declarative content is mature; procedural enforcement is not yet built. "The workflow lacks a verification pass" is a **calibration-appropriate finding about an un-operationalized tool**, not a permanent indictment.

### SV3 — Multi-Perspective Understanding
The SKILL was "followed" by its own stated rules (read + preserve structure), but those rules don't cover the failure modes that occurred. The failures are the systematic signature of fluency-first single-pass generation striking verification-shaped principles that had no execution point. The SKILL is internally consistent but **structurally incomplete** (declarative-rich, procedurally-thin) — a tool deficiency compounding an application gap, not simple user error.

*Meta-inspection (H1 candidate-set, H3 question-framing):* candidate causes = {missing verification pass, render-time non-application, SKILL volume/saturation, LLM incapacity, fluency bias}. "Missing pass" and "render-time non-application" are two facets of ONE thing (no enforcement point, during OR after). Fluency-bias is the DRIVER; missing-pass is the absent GUARD. Volume and incapacity are rival root-causes → adjudicated next. Question reframed from binary "followed?" to "followed-by-which-principle-type?"

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — "Was the SKILL followed?" (binary vs graded)
**Strongest counter-interpretation:** the SKILL was simply NOT followed — the AI ignored it and default-translated.
**Why it fails (structural):** the generation-shaped principles WERE honored — Arabic preserved, Tier-1/2 harmony (escalation, ring composition, convergence) preserved, footnote apparatus per A7, dialogue register mostly kept. Wholesale ignoring would have failed these too. The **selective signature** (structure-principles held, verification-principles failed) is only producible by partial, principle-type-selective adherence — verifiable in the output.
**Confidence:** HIGH.
**Resolution:** adherence is **graded and principle-type-selective**: READ=yes, generation-shaped-applied=yes, verification-shaped-applied=no.
**Fixed:** adherence is not binary. **No longer allowed:** "the SKILL was/wasn't followed" as yes/no. **Depends:** the whole per-principle-type diagnosis.

### Ambiguity 2 — LOAD-BEARING: is the cause the missing verification PASS, or SKILL volume/saturation?
**Strongest counter-interpretation:** the config alone is 1752 lines; the AI can't hold all exclusions in attention while translating — it's saturation, not a missing pass, and a pass would saturate identically.
**Why it fails (structural):** (1) a verification pass is **scoped** — one dimension at a time against the SMALL draft (register-only; then omission-diff; then word-sense) — which is exactly what defeats saturation; you never hold 1752 lines at once. (2) err-2a is **definitionally not saturation**: "basit avamın fehmine gelecek" was dropped in fluent compression, and a mechanical source↔draft clause-diff (zero attention load) catches it. So ≥1 error is a missing mechanical check, not saturation. The counter has PARTIAL merit — volume is *why* single-pass per-clause application is unreliable — but that makes volume the reason the fix must be **scoped**, not a replacement for the missing-pass explanation.
**Confidence:** HIGH (that scoped-verification is the primary lever; volume acknowledged as contributing pressure, not dismissed → guards against Clean-Resolution Trap).
**Resolution:** primary cause = **no scoped post-draft verification point**; contributing pressure = SKILL volume (which mandates the pass be narrow/scoped).
**Fixed:** the fix is a SCOPED pass. **No longer allowed:** "just re-read the whole SKILL harder" (re-saturates). **Depends:** the prevention-mechanism design.

### Ambiguity 3 — SPECIFIC-vs-PATTERN: are the 7 errors the whole problem?
**Strongest counter-interpretation:** they're 7 isolated slips; fix them and you're done.
**Why it fails (structural):** the 7 share ONE generative mechanism (fluency-first single-pass, verification-shaped principle un-fired). Hand-fixing the 7 leaves the mechanism intact, so the next chunk yields a fresh 7 of the same types. (Indeed the two chunks already produced almost certainly carry more instances.) The **pattern**, not the instances, is the problem.
**Confidence:** HIGH.
**Resolution:** target the mechanism, grounded in the 7 as evidence. **Fixed:** deliverable addresses the pattern.

### Ambiguity 4 — LLM incapacity?
**Strongest counter-interpretation:** an LLM just can't do register/word-sense reliably; no process fixes it.
**Why it fails (structural):** the fixes are within immediate reach once pointed at — "allegorical"→"parable/comparison", restore the dropped clause, "work"→"foothold/purchase". Incapacity would mean the AI *couldn't* produce these even when asked — false. The capability is present; the **trigger to deploy it** is absent.
**Confidence:** HIGH.
**Resolution:** capability present, trigger absent → reinforces the verification-pass fix.

### SV4 — Clarified Understanding
The cause is a shared mechanism: fluency-first single-pass generation honors generation-shaped principles but leaves verification-shaped principles un-fired because the workflow has no scoped post-draft check. SKILL volume is the contributing pressure that makes single-pass per-clause application unreliable and dictates that the fix be **scoped**. The 7 errors are reproducible symptoms spanning a severity spectrum. The SKILL was followed by its own (incomplete) stated rules.

---

## Phase 4 — Degrees-of-Freedom Reduction

**Now fixed:** knowledge was present (not a content gap); failure is selective by principle-type; primary lever = scoped post-draft verification; contributing pressure = volume; adherence is graded; severity spectrum across the 7; capability present / trigger absent.
**Eliminated:** "SKILL ignored entirely" (disproven by selective signature); "LLM incapacity" (within-reach fixes); "attend harder / re-read whole SKILL" (re-saturates); "fix the 7 by hand = done" (mechanism reproduces); "the config values were wrong" (confirmed-absent — not in dispute); "policy-layer failed" (confirmed-absent).
**Viable remaining paths (for Innovation/Critique):** design a scoped verification pass (checklist keyed to the surfaced clauses); and/or edit SKILL.md Step 5 to force the 3-Pass as discrete gates; OUTPUT-REACH (diagnose-only vs also-build) stays open for the user/Critique.

### SV5 — Constrained Understanding
Solution space is constrained to **enforcement-mechanism designs** (a scoped post-draft verification pass and/or a gated 3-Pass in SKILL.md Step 5), grounded in "the knowledge exists but has no execution point."

---

## Phase 5 — Conceptual Stabilization

*Accommodation check (H6):* the model did NOT require repeated patching — each perspective and each ambiguity-collapse reinforced or refined the same structural model (verification-shaped principles un-fired for lack of an enforcement point). Stable, not force-fit.

### SV6 — Stabilized Model

**The 7 errors are the structural signature of running a declarative-rich, procedurally-thin SKILL as a single fluency-first pass.** The SKILL's principles divide by *how they must fire*:

- **Generation-shaped** (preserve Arabic; Tier-1/2 harmony; escalation; ring composition; footnote apparatus) — fire DURING fluent generation → **honored** ✓
- **Verification-shaped** (A1 register-exclusion; Pass-1 no-omission; policy-3 word-sense-in-context; A1 target-syntax naturalness) — require CHECKING THE DRAFT against a standard, have **no execution point** in a single generative pass → **failed** ✗

Every error is a verification-shaped principle left un-fired: err-1 = A1 register-exclusion un-checked · err-2a = Pass-1 no-remove un-diffed · err-2b = target-naturalness un-checked (+ the omission compounding) · err-3 = word-connotation un-checked · err-4/5 = A1 target-syntax naturalness un-checked · err-6 = policy-3 word-sense-in-context un-checked · err-7 = A2-lay register un-checked (defensible rendering, wrong register).

**"Was the SKILL followed?"** — READ: **yes** (fully). GENERATION-shaped applied: **yes**. VERIFICATION-shaped applied: **no**. SKILL DEFICIENT: **yes, partially** — internally consistent and its stated Rules honored, but Rules + workflow never mandate the verification checks, so it "promises more than its structure delivers." The declarative antidote to ≥6/7 exists; the procedural trigger does not.

**Driver** = fluency bias (which the SKILL's own no-smoothing policy names as its counter-bias target — the SKILL predicted this failure). **Contributing pressure** = SKILL volume, which makes holistic single-pass per-clause application unreliable and is exactly why the fix must be a **scoped** verification pass, not "attend harder."

**Difference from SV1:** SV1 = "I read it but slipped on applying parts" (carelessness). SV6 = adherence is **selective by principle-type** (a structural discriminator, not carelessness); the SKILL is **procedurally incomplete** (a tool deficiency, not just user error); the process architecture **guarantees this class of slip until an enforcement point is added**; the fix is a **scoped verification pass** targeting verification-shaped principles; and the 7 span a **severity spectrum**.

**Open ambiguities (flagged, not dropped):**
- OUTPUT-REACH — deliver the diagnosis only, or also build the verification-pass / SKILL-edit (→ Critique / user).
- Fix-home — a new post-draft QA pass vs gating SKILL.md Step 5's 3-Pass vs both (→ Innovation to generate, Critique to adjudicate).

**Saturation telemetry:** perspectives produced new anchor TYPES through Feasibility (scoped) and Definitional (internal-gap) — not saturated early. SV1→SV6 delta large. Anchors span all 5 types × 8 perspectives. Ambiguity-resolution ratio 4/4 resolved + 2 OUTPUT/fix-home flagged OPEN.
