# Decomposition — doc_internal_contradiction_cause_and_prevention

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-04_01-36__doc_internal_contradiction_cause_and_prevention/_branch.md`

Whole-to-be-decomposed: the action program implied by sensemaking's SV6 — communicate the two-layer cause stack (PROCEDURAL principle-as-statement + default-case anchoring, amplified by out-of-scope ARCHITECTURAL static-vs-dynamic mismatch), specify the prevention mechanism (principle-as-test + end-of-doc audit + EXCEPT-WHEN clauses + on-demand sub-case decomposition), and address deployment (prospective + retroactive) plus verification (against concrete "easy" criteria) plus integration (composition with prior inquiry's MVF-4) plus scope-extension (sibling docs).

---

## Step 1 — Perceive Coupling Topology

### Elements in the whole

| # | Element |
|---|---|
| e1 | Communicate the two-layer cause stack (procedural cause amplified by architectural cause) to the user |
| e2 | Communicate the widespread-pattern observation (≥12 Tier 3 instances; the register case is one example) |
| e3 | Specify the principle-as-test concept (convert the meta-principle from statement to test that runs at every classification) |
| e4 | Specify the per-entry test procedure (the one-line test: "always meaning-carrying / sometimes (in what cases?) / never") |
| e5 | Specify the end-of-doc audit procedure (one-pass scan: find universal negative meaning-claims, attempt counter-case construction) |
| e6 | Specify the EXCEPT-WHEN clause format (for scoping negative claims at the entry level) |
| e7 | Specify the on-demand sub-case decomposition trigger and procedure (when test/audit finds a context-dependent classification) |
| e8 | Define when the prospective authoring discipline fires (every new tier classification) and how the author records the result |
| e9 | Define the retroactive sweep procedure (one-pass over existing Tier 3 entries; surfacing's enumerated A-8 through A-19 are inputs) |
| e10 | Decide whether to apply the retroactive sweep as part of this inquiry's deliverable OR to defer it as user-action |
| e11 | Verify the mechanism against each of the 5 concrete "easy" criteria from sensemaking |
| e12 | Show how the new prevention mechanism composes with the prior inquiry's MVF-4 (the surgical register tier fix) |
| e13 | Decide whether the prevention extends to `notes.md` and `advanced_principles.md` (which have different doc shapes with different vulnerabilities per surfacing B-27 through C-32) |

### Coupling assessment (pairwise — "change one, must the other change?")

Strong coupling clusters:

- **Cluster A — Cause communication**: e1 ↔ e2. The two-layer cause and the widespread-pattern observation are two faces of the same diagnosis; the user reads them together.
- **Cluster B — Prevention mechanism specification**: e3 ↔ e4 ↔ e5 ↔ e6 ↔ e7. All five describe the procedure in different facets — the abstract reframe (e3), the per-entry test (e4), the audit (e5), the clause format (e6), and the on-demand sub-case decomposition (e7). They form one coherent procedure; changing one likely requires changing the others to stay consistent.
- **Cluster C — Deployment**: e8 ↔ e9 ↔ e10. Prospective and retroactive deployments share the procedure but differ in timing/scale; the apply-now-vs-defer decision (e10) is a policy choice on the retroactive deployment.

Moderate coupling:

- Cluster A → Cluster B: the cause names the target the prevention addresses. The mechanism's shape is derived from the cause's shape (procedural cause → procedural fix).
- Cluster B → Cluster C: deployment is HOW Cluster B's mechanism is applied; depends on the mechanism's content.
- e11 (easy verification) → Cluster B: verification scores Cluster B against the 5 criteria.
- e12 (MVF-4 composition) → Cluster C: composition is about how deployment aligns with the prior inquiry's surgical fix.
- e13 (cross-doc extension) → Cluster B: extension question is "does the procedure transfer to docs with different shapes?"

Weak coupling / independent:

- e13 (cross-doc extension) is loosely coupled to everything else — it's a scope question that can be addressed independently as defer-or-extend.
- e12 (MVF-4 composition) is loosely coupled to most of the rest — it's a one-paragraph integration note.

### Coupling map (visual)

```
                ┌─────────────────────────────────────────┐
                │  Cluster A — CAUSE COMMUNICATION         │
                │   e1 (two-layer cause stack)             │
                │   e2 (widespread pattern observation)    │
                └────────────────┬────────────────────────┘
                                 │ informs target
                                 ▼
                ┌─────────────────────────────────────────┐
                │  Cluster B — MECHANISM SPECIFICATION     │
                │   e3 (principle-as-test concept)         │
                │   e4 (per-entry test procedure)          │
                │   e5 (end-of-doc audit procedure)        │
                │   e6 (EXCEPT-WHEN clause format)         │
                │   e7 (on-demand sub-case decomp.)        │
                └────────────────┬────────────────────────┘
                                 │
                  ┌──────────────┼──────────────┬──────────────┐
                  ▼              ▼              ▼              ▼
       ┌──────────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐
       │ Cluster C —      │  │ e11 — EASY │  │ e12 —      │  │ e13 —      │
       │ DEPLOYMENT       │  │ VERIFY     │  │ MVF-4      │  │ CROSS-DOC  │
       │   e8 (prospect.) │  │            │  │ COMPOSE    │  │ EXTEND     │
       │   e9 (retroact.) │  │            │  │            │  │            │
       │   e10 (now/def.) │  │            │  │            │  │            │
       └──────────────────┘  └────────────┘  └────────────┘  └────────────┘
```

Three strong clusters (A, B, C) plus three relatively independent pieces (e11, e12, e13).

---

## Step 2 — Detect Boundaries (Top-Down)

Cutting at low-coupling valleys:

- **B1**: between Cluster A and Cluster B. Diffuse boundary — the cause informs the mechanism but doesn't dictate every detail.
- **B2**: between Cluster B and Cluster C. The mechanism is content; deployment is timing/scale. Different functional roles.
- **B3**: between Cluster B/C and e11 (easy verification). Easy verification is a check on Cluster B; it doesn't modify the mechanism.
- **B4**: between everything-else and e12 (MVF-4 composition). Single-point clean cut — a one-paragraph integration note.
- **B5**: between everything-else and e13 (cross-doc extension). Single-point clean cut — a scope decision.

Initial piece candidates:

| Candidate | Composition |
|---|---|
| **P1** | Cluster A (e1 + e2 — cause communication) |
| **P2** | Cluster B (e3 + e4 + e5 + e6 + e7 — mechanism specification) |
| **P3** | Cluster C's prospective half (e8) |
| **P4** | Cluster C's retroactive half (e9 + e10) |
| **P5** | e11 (easy verification) |
| **P6** | e12 (MVF-4 composition) |
| **P7** | e13 (cross-doc extension) |

7 pieces from top-down boundary detection.

Note on P3/P4 split: Cluster C contains e8 + e9 + e10, but e8 (prospective) and e9+e10 (retroactive) serve different deployment modes with different timing semantics. Splitting them keeps each piece tractable as a single-focused pass. The shared procedure (from P2) ensures consistency.

---

## Step 3 — Validate Boundaries (Bottom-Up Check)

Irreducible atoms:

| Atom | Description |
|---|---|
| a1 | Author the cause-explanation text (two-layer stack + widespread pattern) |
| a2 | Author the principle-as-test concept reframe |
| a3 | Specify the per-entry test (one-line procedure) |
| a4 | Specify the end-of-doc audit procedure |
| a5 | Specify the EXCEPT-WHEN clause format |
| a6 | Specify the on-demand sub-case decomposition (trigger + procedure) |
| a7 | Define when prospective discipline fires + how the author records the result |
| a8 | Specify the retroactive sweep procedure |
| a9 | Make the apply-now-vs-defer decision (or surface the choice) |
| a10 | Score the mechanism against each of the 5 "easy" criteria |
| a11 | Specify how the new mechanism composes with MVF-4 |
| a12 | Decide cross-doc extension (extend / defer / not-applicable) |

Atom-to-piece mapping:

- P1 = {a1} ✓
- P2 = {a2, a3, a4, a5, a6} ✓ (the five facets of the mechanism specification)
- P3 = {a7} ✓
- P4 = {a8, a9} ✓
- P5 = {a10} ✓
- P6 = {a11} ✓
- P7 = {a12} ✓

No atoms split across pieces. No atoms missing from a piece. **Top-down and bottom-up agree.**

**Boundary confidence: HIGH across all 7 pieces.**

---

## Step 4 — Express as Question Tree

### P1 — How should the two-layer cause and the widespread-pattern observation be communicated to the user?

**Verification criteria:**
- [ ] The two-layer cause stack is named explicitly: Layer 1 PROCEDURAL (meta-principle stated separately from application; implicit application via default-case anchoring), Layer 2 ARCHITECTURAL (static framework can't represent context-dependent principle).
- [ ] The widespread-pattern observation is named: surfacing identified ≥12 Tier 3 entries with the same vulnerability shape ("X — [positive aspect] but doesn't [meaning-claim]" at universal scope).
- [ ] Layer 1 is identified as the in-scope cause; Layer 2 is identified as out-of-scope and inherited from the prior inquiry's S7 RESEARCH FRONTIER.
- [ ] Cause connects to surfacing's evidence (A-7, A-20, A-22) without requiring the user to read surfacing.
- [ ] Personal-author framings ("just be careful") are explicitly ruled out with the structural argument.

### P2 — What is the operational procedure for the prevention mechanism?

**Verification criteria:**
- [ ] The principle-as-test concept is specified: the meta-principle is converted from a statement (held in the author's working memory) into a test (a procedure that runs at every classification).
- [ ] The per-entry test is specified at line-level detail: at each new tier classification, the author records the answer to: "By the meta-principle, does this feature carry meaning? Always / Sometimes (in what cases?) / Never?" The "Sometimes" answer requires sub-case specification.
- [ ] The end-of-doc audit procedure is specified: scan for universal negative meaning-claims ("X doesn't [Y-meaning-claim]"); for each, attempt to construct a counter-case where the claim would fail; if a counter-case exists, the claim must be scoped or the entry split.
- [ ] The EXCEPT-WHEN clause format is specified: when a negative claim is scoped, the entry takes the form "X doesn't [Y-meaning-claim] EXCEPT WHEN [sub-case]" or "X doesn't [Y-meaning-claim] in the default case; X DOES [Y-meaning-claim] in [sub-case]."
- [ ] The on-demand sub-case decomposition is specified: when the test or audit reveals a sub-case where the classification would differ, the entry splits into two sub-entries with separate tier assignments (e.g., "register-as-style" → Tier 3, "register-as-alternation" → Tier 1).
- [ ] The procedure is concrete enough to apply without further interpretation.

### P3 — How is the prevention applied prospectively (to new entries the user authors going forward)?

**Verification criteria:**
- [ ] Trigger specified: every new tier classification fires the per-entry test from P2.
- [ ] Recording format specified: where the test answer is written (inline with the entry's justification? as a separate annotation?). The format must be authoring-friendly (low friction).
- [ ] Estimated per-entry overhead: ≤2 minutes (per sensemaking's "easy" criterion 1).
- [ ] How "Sometimes" answers trigger sub-case decomposition is clear.

### P4 — How is the prevention applied retroactively to existing Tier 3 entries, and is the sweep performed now or deferred?

**Verification criteria:**
- [ ] Sweep procedure specified: one-pass audit using P2's audit procedure across the ≥12 surfaced Tier 3 entries (A-8 through A-19 in `surfacing.md`).
- [ ] Estimated sweep effort: ~15-60 minutes total (per sensemaking's "easy" criterion 2).
- [ ] Decision documented: apply the sweep now as part of this inquiry's deliverable, OR defer with explicit revival trigger, OR surface the choice to the user.
- [ ] If applied now: the sweep's output is a list of ≥12 corrected entries.
- [ ] If deferred: the revival trigger is specific (time-bound / condition-bound / observable).

### P5 — Does the mechanism meet the 5 concrete "easy" criteria from sensemaking?

**Verification criteria:**
- [ ] Criterion 1 (per-entry cost ≤2 min): scored.
- [ ] Criterion 2 (audit cost ≤15 min one-time): scored.
- [ ] Criterion 3 (no new tooling): scored.
- [ ] Criterion 4 (user-solo-applicable): scored.
- [ ] Criterion 5 (preserves doc shape): scored.
- [ ] If any criterion fails, refinement direction specified.

### P6 — How does this inquiry's prevention compose with the prior inquiry's MVF-4 (the surgical register tier fix)?

**Verification criteria:**
- [ ] Independence verified: MVF-4 and this prevention can be applied independently without conflict.
- [ ] Composition order specified: which to apply first, or whether they can be applied in any order.
- [ ] If applied together: the combined effect is documented (MVF-4 fixes the specific register entry; this prevention's retroactive sweep would have found and fixed the same entry; there's no double-correction).

### P7 — Does the prevention extend to `notes.md` and `advanced_principles.md`?

**Verification criteria:**
- [ ] Surfacing's observation re-acknowledged: `notes.md` and `advanced_principles.md` have different doc shapes (flat principle list vs expository examples) with different vulnerability patterns from `harmony_layer.md`'s tier system.
- [ ] Decision documented: extend the mechanism, defer with revival trigger, or mark not-applicable (different vulnerabilities need different mechanisms).
- [ ] If defer: the revival trigger is specific.

---

## Step 5 — Map Interfaces

| Source | Target | What flows | Direction |
|---|---|---|---|
| P1 | User | Cause communication (two-layer stack + widespread pattern) | one-way (output to user) |
| P1 | P2 | Cause naming — the target the prevention addresses; the mechanism's shape derives from the cause's shape | one-way data dependency |
| P2 | P3 | The procedure that prospective deployment applies | one-way data dependency |
| P2 | P4 | The procedure that retroactive sweep applies | one-way data dependency |
| P2 | P5 | The mechanism that gets scored against the 5 criteria | one-way data dependency |
| P2 | P6 | The procedure that composes with MVF-4 | one-way data dependency |
| P2 | P7 | The procedure considered for cross-doc extension | one-way data dependency |
| Surfacing A-8 through A-19 | P4 | Enumerated Tier 3 entries that are inputs to the retroactive sweep | one-way (from surfacing's workspace) |
| User | P4 | Apply-now-vs-defer decision (if P4 surfaces the choice) | one-way (input) |
| P5 | User | "Easy" verdict — the mechanism is adopt-ready or needs refinement | one-way (output to user) |
| P6 | User | Composition note — order of operations | one-way (output) |
| P7 | User | Cross-doc scope decision | one-way (output) |

### Assumptions-not-data check (Step 5 refinement)

What does each piece ASSUME?

- **P3 assumes** the per-entry overhead estimate (≤2 minutes) holds in practice. If actual authoring overhead exceeds the estimate, the "easy" claim weakens. Mitigation: P5's verification scores Criterion 1 with the estimate; if subsequent use reveals a higher real cost, the mechanism gets revisited.
- **P4 assumes** surfacing's A-8 through A-19 enumeration is complete. If MORE Tier 3 entries have the same vulnerability that surfacing missed, the sweep's expected effort grows beyond the 15-60 min estimate. Mitigation: surfacing's traversal coverage map confirmed all Tier 3 entries were examined; no umbrella tags; coverage CONFIRMED at the region level.
- **P5 assumes** the 5 "easy" criteria from sensemaking's Ambiguity 5 resolution are operationally sufficient. If the user has additional unstated criteria, the verification is incomplete. Mitigation: the criteria were derived from the user's stated use case in `_branch.md`; alignment is best-effort.
- **P6 assumes** the user will apply MVF-4. If they don't, P6's composition concern is moot. Mitigation: P6's role is integration-only; absence of MVF-4 application doesn't affect P2's mechanism.
- **P7 assumes** different doc shapes have different vulnerabilities. This is well-grounded in surfacing's observations (B-27, B-28, C-30, C-31, C-32). Low risk.

All assumptions surfaced and mitigated.

---

## Step 6 — Order by Dependency

### Dependency-ordered execution

**LEVEL 0 — Must come first:**
- **P1 (cause communication)** — provides cause naming that P2 derives from.

**LEVEL 1 — After P1:**
- **P2 (mechanism specification)** — depends on P1's cause naming.

**LEVEL 2 — Parallel after P2:**
- **P3 (prospective deployment)** — depends on P2.
- **P4 (retroactive deployment + apply-or-defer decision)** — depends on P2; also depends on surfacing's A-8 through A-19 enumeration (already available from prior discipline).
- **P5 (easy verification)** — depends on P2.
- **P6 (MVF-4 composition)** — depends on P2.
- **P7 (cross-doc extension)** — depends on P2 (the procedure being extended).

Critical path: P1 → P2 → any L2 piece. 3 levels deep.

### Visual dependency order

```
LVL 0:        P1 (cause communication)
                    │
                    ▼
LVL 1:        P2 (mechanism specification)
                    │
        ┌───────┬───┴───┬───────┬───────┐
        ▼       ▼       ▼       ▼       ▼
LVL 2: P3      P4      P5      P6      P7
       (pro-   (retro- (easy   (MVF-4  (cross-
        spect.) active) verify) compose) doc ext.)
```

---

## Step 7 — Self-Evaluate

### Minimum 3-dimension evaluation

| Dimension | Check | Verdict |
|---|---|---|
| **Independence** | Each piece's question is answerable without reading sibling pieces (except through defined interfaces) | **PASS** — each piece is independently scope-defined; cross-piece references go through the interface map. |
| **Completeness** | No aspect of the whole falls through the gaps | **PASS** — cause communication [P1], mechanism [P2], deployment prospective [P3] and retroactive [P4], easy verification [P5], MVF-4 composition [P6], cross-doc extension [P7]. The 2-layer cause and the two deployment modes are both covered. |
| **Reassembly** | Pieces + interfaces reconstruct the whole | **PASS** — given all 7 pieces answered, the user has: the cause [P1], the procedure [P2], how to apply now-forward [P3] and to existing entries [P4], confidence the mechanism is easy [P5], composition with prior fix [P6], scope clarity for sibling docs [P7]. The deliverable is complete. |

### Full 7-dimension evaluation

| Dimension | Check | Verdict |
|---|---|---|
| **Independence** | Per above | PASS |
| **Completeness** | Per above | PASS |
| **Reassembly** | Per above | PASS |
| **Tractability** | Each piece small enough for a single focused pass? | **PASS** — P2 is the largest (5-facet mechanism specification) but still single-pass-shaped because the facets share a coherent structure. Other pieces are smaller. |
| **Interface clarity** | Cross-piece flows explicit, no hidden dependencies | **PASS** — 12 interfaces listed; 5 hidden-coupling assumptions surfaced and mitigated. |
| **Balance** | Complexity roughly proportional across pieces | **PASS** — P2 is the largest; others are roughly small-to-medium. P2's size is ~2-3× the smallest pieces, not 10×. |
| **Confidence** | Top-down and bottom-up agree on boundaries | **PASS** — Step 3 verified atom-to-piece mapping; HIGH confidence on all 7 boundaries. |

### Determination-mechanism piece check (Step 7 refinement)

Load-bearing concepts with runtime determinations:

| Concept | Runtime determination | Determination-mechanism piece |
|---|---|---|
| "Universal negative meaning-claim" | Does this entry's justification assert a negative meaning-claim at universal scope? | **P2** (the audit procedure specifies this check) |
| "Counter-case" | Can the author construct a counter-case for this claim? | **P2** (the audit procedure specifies the counter-case construction step) |
| "Sometimes" answer | Does this feature carry meaning sometimes (in what cases)? | **P2** + **P3** (the per-entry test specifies the answer set and triggers sub-case decomposition) |
| "Easy" criteria satisfaction | Does the mechanism meet each of the 5 criteria? | **P5** (explicit scoring of each criterion) |
| "Cross-doc applicability" | Does the mechanism transfer to a doc with a different shape? | **P7** (decision: extend / defer / not-applicable) |

All runtime determinations have explicit determination-mechanism pieces. PASS.

### Failure-mode self-check

| Failure mode | Risk | Mitigation status |
|---|---|---|
| 1. Premature decomposition | Decomposing before sensemaking clarified the whole | NO — sensemaking SV6 was produced and is the input. |
| 2. Wrong boundaries | Cutting through high-coupling regions | NO — boundaries cut at low-coupling valleys; bottom-up validation agreed. |
| 3. Hidden coupling | Pieces share unstated assumptions | LOW — 5 latent assumptions surfaced; each mitigated. |
| 4. Missing pieces | Whole's aspects fall through gaps | NO — Completeness check confirmed cause + mechanism + deployment (both modes) + verification + integration + extension are all covered. |
| 5. Over-decomposition | Pieces too small to be coherent | LOW — 7 pieces for the inquiry's scope is reasonable; no piece is trivial. |
| 6. Ignoring dependencies | Wrong execution order | NO — explicit 3-level dependency order. |
| 7. Imbalanced | One piece is 80% | NO — P2 is the largest at ~2-3× the smallest, not 10×. |

No failure modes triggered.

---

## Final Deliverable Summary

| # | Piece | Question | Level |
|---|---|---|---|
| **P1** | Cause communication | How should the two-layer cause stack and the widespread-pattern observation be communicated to the user? | 0 |
| **P2** | Mechanism specification | What is the operational procedure (principle-as-test + audit + EXCEPT-WHEN + on-demand sub-case decomposition)? | 1 |
| **P3** | Prospective deployment | How is the prevention applied to new entries going forward? | 2 |
| **P4** | Retroactive deployment + apply-or-defer | How is the prevention applied to existing Tier 3 entries, and is the sweep performed now or deferred? | 2 |
| **P5** | Easy verification | Does the mechanism meet the 5 concrete "easy" criteria? | 2 |
| **P6** | MVF-4 composition | How does this prevention compose with the prior inquiry's MVF-4 (surgical register tier fix)? | 2 |
| **P7** | Cross-doc extension | Does the prevention extend to `notes.md` and `advanced_principles.md`? | 2 |

7 pieces; 3 levels; critical path = 3 levels deep. All pieces have verification criteria. All interfaces explicit. All assumptions surfaced.

**Decomposition verdict: PROCEED.**
