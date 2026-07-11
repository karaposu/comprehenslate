# Decomposition — The Diagnostic, Partitioned

## User Input

`_branch.md`. Stabilized model (sensemaking.md): 7 errors = signature of a declarative-rich/procedurally-thin SKILL run as one fluency-first pass; principles split generation-shaped (honored) vs verification-shaped (failed — no execution point); adherence graded; driver = fluency-bias, pressure = volume → scoped fix. Span the OUTPUT-REACH fork. Save to `decomposition.md`.

---

## Step 1 — Coupling Topology (coupling map)

**Elements** of the diagnostic-plus-reach whole:
E1 per-error adherence mapping (7 errors → clause → verdict) · E2 generation-shaped vs verification-shaped taxonomy (the discriminator) · E3 systemic root-cause (single-pass, no enforcement point; fluency-driver; volume-pressure) · E4 adherence verdict (READ/gen/verification/deficient) · E5 severity spectrum (clear-violation vs defensible) · E6 prevention mechanism (scoped pass) · E7 SKILL-repair (where/how to embed) · E8 OUTPUT-REACH decision.

**Coupling gradient (change-A→change-B?):**
- E1↔E5 **strong** (E5 is E1's severity column). → one cluster.
- E2↔E3 **strong** (E3 is the conclusion drawn FROM the taxonomy). → one cluster.
- E1→E2 **moderate** (taxonomy generalizes the tagged errors; distinct claim).
- E3→E6 **strong** (the fix targets the named cause).
- E6→E7 **strong** (repair = embed the pass into the SKILL).
- {E1,E2,E3,E4,E5}→{E6,E7} **weak** — the diagnosis is complete without the fix; the fix is the *reach*. **This is the dominant boundary (OUTPUT-REACH valley).**
- E8 is a **scope gate**, weakly coupled to content, that governs whether E6/E7 are in final scope.

**Clusters → pieces:** A = {E1,E5} diagnosis core · B = {E2,E3} the mechanism · C = {E4} the verdict · D = {E6} prevention · E = {E7} repair · F = {E8} reach gate.

## Step 2 — Boundaries (top-down)
Lowest-coupling cut = the **OUTPUT-REACH valley** between the diagnosis {A,B,C} and the reach {D,E}, gated by F. Secondary cuts: A|B (data vs discriminator), B|C (cause vs graded-verdict), D|E (design vs embed).

## Step 3 — Boundary validation (bottom-up)
Irreducible atoms: {the 7 errors}, {the taxonomy}, {the systemic cause}, {the graded verdict}, {the pass design}, {the SKILL-edit locus}, {the reach choice}. These group exactly into A/B/C/D/E/F — top-down and bottom-up **agree** → HIGH confidence. No atom is split; none wrongly merged.

## Step 4 — Question Tree

**Q-A — Diagnosis Core** *(always in scope):* For each of the 7 errors, what SKILL clause governs it, was it violated, and where on the severity spectrum does it sit?
- [ ] all 7 have a named governing clause (from surfacing's 10)
- [ ] each tagged violated vs defensible
- [ ] each placed clear-violation / defensible-but-off-register
- [ ] each grounded in a verifiable source↔draft↔config diff, not assertion

**Q-B — The Mechanism** *(always):* WHY did the clauses fail to fire — the structural discriminator + the single systemic cause?
- [ ] principles partitioned generation-shaped (fired) vs verification-shaped (failed)
- [ ] all 7 errors shown to be verification-shaped-un-fired
- [ ] systemic cause stated (single fluency-first pass; no enforcement point)
- [ ] driver (fluency-bias — named in the SKILL's own no-smoothing policy) + pressure (volume → scoped) identified
- [ ] rival causes (saturation / incapacity / ignored-entirely / config-wrong) shown eliminated

**Q-C — The Adherence Verdict** *(always; this is the user's explicit question):* Was the SKILL followed?
- [ ] answered graded, not binary
- [ ] READ verdict + evidence · generation-shaped-applied + evidence · verification-shaped-applied + evidence
- [ ] SKILL-deficient verdict (internal gap: promises > delivers) + evidence
- [ ] explicitly separates "AI-application error" from "tool deficiency"

**Q-D — Prevention Mechanism** *(gated by F):* What scoped verification pass catches this error-class before emit?
- [ ] narrow, per-dimension checklist: register-exclusion · source↔draft omission-diff · word-sense-in-context · target-naturalness reread
- [ ] each check keyed to its surfaced governing clause
- [ ] scoped (defeats volume/saturation pressure)
- [ ] token-feasible vs a re-translation

**Q-E — SKILL Repair** *(gated by F):* Where does the fix live and what edits make it self-enforcing?
- [ ] locates the gap (SKILL.md Step 5 monolithic emit; un-gated harmony_layer 3-Pass)
- [ ] proposes discrete 3-Pass gates OR an added verification step
- [ ] names which file(s) change
- [ ] additive — preserves existing declarative content

**Q-F — Reach Gate** *(scope decision, surfaced to user):* How far past diagnosis should the deliverable travel?
- [ ] the three reaches named (diagnose-only / +prevention / +repair)
- [ ] default recommended (A+B+C always delivered; D+E offered for user authorization)
- [ ] gate presented to the user, not silently resolved

## Step 5 — Interface Map

| Source | Target | What flows | Dir |
|---|---|---|---|
| surfacing (10 clauses) | A, D | governing clauses (prerequisite) | → |
| A | B | 7 errors tagged {clause, severity} (data) | → |
| A | C | per-error verification/generation tags (data) | → |
| B | C | taxonomy + systemic cause (claim) | → |
| B | D | systemic cause + driver (dependency — pass targets cause) | → |
| B, C | E | systemic cause + deficiency verdict (dependency) | → |
| D | E | the prevention-pass design (dependency — E embeds D) | → |
| F | D, E | reach authorization (gate) | → |

**Assumptions-not-data check (hidden-coupling guard):** D assumes B's cause is right (explicit, B's output). E assumes a workflow insertion point exists (explicit, from surfacing: SKILL.md Step 5). C assumes A's severity tags (explicit A→C interface). No unstated format/timing/state assumptions across boundaries. **No hidden coupling.**

## Step 6 — Dependency Order

1. **surfacing** (done) → 10 clauses.
2. **A** (evidence table) — first.
3. **B** (mechanism) — after A.
4. **C** (graded verdict) — after A+B.  ← *A→B→C is the always-delivered diagnosis.*
5. **F** (reach gate) — decidable early; its resolution GATES D/E. Default: deliver A+B+C, offer D+E.
6. **D** (prevention) — after B, if F authorizes.
7. **E** (repair) — after C+D, if F authorizes.

No circular dependencies. For the pipeline: **Innovation** works the reach design-space (D, and E's fix-home options); **Critique** adjudicates them + tests A/B/C's claims; **CONCLUDE** delivers A+B+C and presents F with D+E as the offered reach.

## Step 7 — Self-Evaluation

| Dimension | Verdict | Note |
|---|---|---|
| **Independence** | PASS | each Q answerable via defined interfaces alone (A from errors+clauses; B from A's tags; C from A+B; D from B+surfacing; E from C+D; F standalone) |
| **Completeness** | PASS | user's question = A+B+C; OUTPUT-REACH = D+E+F; nothing falls through |
| **Reassembly** | PASS | A+B+C (+F-gated D+E) + interfaces = full diagnostic with preserved reach |
| **Determination-mechanism** | PASS | the generation/verification classification lives in B; the reach-determination lives in F — no runtime determination lacks a piece |
| **Tractability** | PASS | each piece = one focused pass |
| **Interface clarity** | PASS | all flows explicit; assumptions checked; no hidden coupling |
| **Balance** | PASS (mild) | A+B carry the weight (appropriate — the diagnosis IS the deliverable); C light; D/E moderate; F light. Not one-piece-80% |
| **Confidence** | HIGH | top-down (OUTPUT-REACH valley) and bottom-up (7 atoms) agree |

**Decomposition version:** DV1 (single pass sufficient). No hidden coupling or wrong-boundary signals → no DV2 trigger.
