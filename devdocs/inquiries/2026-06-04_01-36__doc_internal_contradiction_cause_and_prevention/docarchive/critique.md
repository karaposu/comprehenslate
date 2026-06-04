# Critique — doc_internal_contradiction_cause_and_prevention

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-04_01-36__doc_internal_contradiction_cause_and_prevention/_branch.md`

Critique-target candidates: the 11 surviving outputs from `innovation.md` (S1–S11) + the Emergent Assembly. Coverage-gap analysis will surface MVD (Minimum Viable Discipline = S1 + S2) as a critique-elevated sub-assembly. Stakes: HIGH (framework-doc changes touch all future entries).

---

## Phase 0 — Dimension Construction

### Extracted from sensemaking

From sensemaking's anchors:
- **Constraints CON-3, CON-4:** the user's "easy" criterion + user-maintained framework → operationalize "easy" as a critical-weight dimension.
- **Key insights KI-1, KI-2, KI-3:** widespread pattern across ≥12 Tier 3 entries + the procedural cause (implicit application + default-case anchoring) → prevention must address the *pattern*, not just instances, AND must address the *procedural* cause.
- **Foundational principles FP-1, FP-3, FP-4:** principle-as-statement vs principle-as-test + negative-claims-at-universal-scope as contradiction-prone + "easy" criteria are concrete → these directly seed the evaluation dimensions.
- **Meaning-nodes MN-5 to MN-8:** EXCEPT-WHEN, end-of-doc audit, counter-example seeking, principle-as-test → form the candidate-space the evaluation operates over.

### Evaluation dimensions (8 total: 6 default + 2 project-specific)

| # | Dimension | What it asks | Weight | Source |
|---|---|---|---|---|
| D1 | **Correctness** | Does the candidate actually prevent the procedural cause (implicit application + default-case anchoring)? | **5 (critical)** | KI-3 + procedural cause from SV6 |
| D2 | **Coherence** | Does it fit with the existing doc structure without breaking valid parts? | 3 (medium) | CON-5 (preserve doc shape) |
| D3 | **Feasibility** | Can the user actually implement this with their available time and resources? | 4 (high) | "Easy" criterion |
| D4 | **Completeness** | Does it cover the procedural cause layer fully? | **4 (high)** | Layer-1 cause (procedural; in scope) |
| D5 | **Robustness** | Does it work for FUTURE unknown contradictions, not just the observed Tier 3 pattern? | 3 (medium-high) | KI-7 (cross-deployment) + frontier F-4 (generalize to other principles) |
| D6 | **Elegance** | Minimum sufficient intervention? | 3 (medium) | "Smallest viable change" framing |
| D7 | **Recurrence prevention** *(project-specific)* | Does it specifically prevent the widespread Tier 3 contradiction pattern from recurring? | **5 (critical)** | Explicit user goal in _branch.md |
| D8 | **"Easy" criterion fit** *(project-specific)* | Does it meet the 5 concrete sub-criteria (≤2 min/entry, ≤15 min audit, no tooling, user-solo, preserves doc shape)? | **5 (critical)** | Sensemaking Ambiguity 5 resolution |

**Project-specific risk dimension check (Phase 0 refinement):** the candidate set involves project artifacts (`harmony_layer.md` and sibling docs), operations (doc authoring/editing), and state (the cause-pattern itself). D7 (recurrence prevention) and D8 ("easy" criterion fit) are the project-specific risk axes; both included.

**Dimension validation:** would a candidate passing all 8 dimensions perfectly solve the problem? YES — it would address the procedural cause (D1), fit the doc (D2), be implementable (D3), cover the procedural layer (D4), survive future unknown contradictions (D5), avoid over-engineering (D6), prevent the documented widespread pattern (D7), and satisfy the user's hard "easy" constraint (D8). Dimensions sufficient.

---

## Phase 1 — Fitness Landscape

### Viable region

A candidate is viable when it passes all **critical-weight** dimensions (D1, D4, D7, D8) AND has acceptable feasibility (D3). Weaknesses on D2, D5, D6 can be managed via refinement or composition.

### Dead region

A candidate is dead if it fails on D1 (doesn't address the cause), D7 (doesn't prevent recurrence), or D8 (fails the user's "easy" criterion). D8 is non-negotiable per the user's framing.

### Boundary regions

| Boundary | Characterization |
|---|---|
| **Strong cause-alignment, weak elegance** | Addresses the cause but adds significant per-entry overhead. Resolution: refine for parsimony. |
| **Strong feasibility, weak robustness** | Cheap to implement but doesn't generalize beyond Tier 3. Resolution: compose with extension candidate. |
| **Strong recurrence-prevention, weak coherence** | Catches contradictions but feels foreign to the doc's existing shape. Resolution: adapt format to match doc conventions. |

### Unexplored regions

- **Tooling-based fixes** (Lens Shifting contrarian): structurally rejecting non-passing entries via a doc-as-code checker. Out of scope per D8 ("no new tooling"). Inherited unexplored from sensemaking.
- **Architectural redesign** (Inversion Level 3 / S6): dissolving the meta-principle/entry split. Out of scope per "easy" criterion. Inherited unexplored.
- **Cross-doc full extension**: applying the mechanism wholesale to `notes.md` and `advanced_principles.md`. Partially explored via S8 (per-entry trigger); whole-doc extension remains unexplored.

---

## Phase 2 — Adversarial Evaluation per Candidate

### S1 — Lightweight principle-as-test edit + short procedure spec

**Prosecution.** Killer objection: "lightweight" is subjective. If the procedure spec takes the author 5+ min per entry to follow, D8 criterion 1 (≤2 min/entry) fails. **Specific failure-case (per multi-axis prosecution depth):** author edits an entry under time pressure; skips the test; commits a contradiction-prone classification. The lightweight nature doesn't *enforce* application. **Specification-gap probe:** HOW does the lightweight edit look exactly? Innovation said "edit the existing meta-principle to include the test instruction" but did not specify the exact replacement text. Without the text, the user can't apply. **User-perspective objection:** the user might experience the per-entry test as authoring friction even at 2 min per entry; across ≥12 retroactive entries, that's 24+ min.

**Defense.** Deepest strength: directly addresses the procedural cause; converts the meta-principle from statement to test; minimal content addition (preserves doc shape, satisfying D8 criterion 5). The simplest possible intervention that addresses the cause.

**Collision.** Defense wins on cause-alignment (D1). Prosecution's specification-gap is real and addressable: the deliverable should include the *exact* meta-principle edit text and the *exact* procedure spec. Prosecution's "≤2 min per entry" concern is plausible — the test is one-line ("always / sometimes / never"); typical authoring takes seconds, not minutes, to record this. The retroactive 24+ min concern is bounded and one-time.

**Dimension scoring.** D1: strong. D2: strong (minimal change preserves shape). D3: strong. D4: covers procedural cause directly. D5: strong (generalizable). D6: strong. D7: strong (catches future negative-claim patterns). D8: strong (within all 5 sub-criteria).

**Verdict: SURVIVE.** Refinement: the deliverable specifies the exact meta-principle edit text and the exact procedure spec content. Position: viable region (strong across critical dimensions).

---

### S2 — End-of-doc audit checklist (≤5 items)

**Prosecution.** Killer objection: checklists get skipped under time pressure (well-documented in aviation safety research before checklist culture was institutionalized; cf. Gawande's "Checklist Manifesto"). **Specific failure-case:** author edits the doc, completes the editing pass, marks "done" without running the checklist. The audit becomes a deferrable task that never gets done. **Specification-gap:** where in the doc does the checklist live? At the bottom (visible only at end-of-edit)? Standalone file? Innovation says "one-page checklist"; location is unspecified.

**Defense.** Deepest strength: serves as safety net for per-entry test (S1) inconsistencies. The audit catches what authoring discipline misses; one-time cost per doc-edit; ~15 min runtime.

**Collision.** Defense wins on safety-net role. Prosecution's "checklists get skipped" is real and addressable by integration: the checklist becomes the LAST entry in `harmony_layer.md` itself (a permanent "Doc Consistency Audit" section that the author marks completed-with-date on each substantive edit). Located in the doc, not separate. Specification-gap addressed.

**Dimension scoring.** D1: strong. D2: strong. D3: very strong (5 items, ~15 min). D4: covers retroactive sweep + ongoing safety net. D5: strong. D6: strong. D7: strong. D8: strong.

**Verdict: SURVIVE.** Refinement: the checklist lives as a permanent section at the bottom of `harmony_layer.md` with a completed-date field updated on each substantive edit. Position: viable region.

---

### S3 — EXCEPT-WHEN clause format

**Prosecution.** Killer objection: forcing EXCEPT-WHEN clauses on every Tier 3 entry might produce false-precision — entries with genuinely universal negative claims get padded with "EXCEPT WHEN [none]" verbiage. **Specific failure-case:** an entry's negative claim IS genuinely universal (in case any exist); the format requires a clause that adds noise without adding meaning. **Specification-gap:** innovation provided two forms (EXCEPT-WHEN or "always; no exception because [reason]"), addressing this — but doesn't explicitly state that confirmed-universal cases are acceptable.

**Defense.** Deepest strength: directly scopes negative claims (the vulnerable authoring template identified by sensemaking). Scoped negative claims are an established technical-writing technique. Per-entry length increase: ~1 line.

**Collision.** Defense wins. Prosecution's "false-precision" concern is addressed by the two-form spec. Refinement: explicit acknowledgment that confirmed-universal cases use the second form, not forced EXCEPT-WHEN.

**Dimension scoring.** D1: strong. D2: strong. D3: strong. D4: covers the negative-claim sub-case directly. D5: medium (specific to negative claims; doesn't generalize to other contradiction shapes). D6: strong. D7: strong (specifically prevents the Tier 3 pattern's vulnerability). D8: strong.

**Verdict: SURVIVE.** Refinement: explicit two-form spec with examples. Position: viable region.

---

### S4 — Principle-application trace per entry

**Prosecution.** Killer objection: visible bulk in each entry. The doc becomes longer; readability decreases. **Specific failure-case:** a Tier 1 entry has obvious meaning-carrying status; the trace ("ranking-test: always carries meaning → Tier 1") adds redundant text. Reader skips the trace after a few entries; eventually the trace is just noise. **Specification-gap:** the trace format — one-line in italics? in parens? as a separate field? Innovation suggested parens or italics but didn't commit.

**Defense.** Deepest strength: makes the principle's application observable; supports auditing (S2). Without the trace, the principle's application is invisible — can't be verified retroactively, can't be audited.

**Collision.** Defense wins on observability — the trace is what makes S2's audit operationally possible. Prosecution's bulk concern addressed by short format: one-line italicized annotation, ≤80 chars.

**Dimension scoring.** D1: medium-strong (supports the procedural cause's fix indirectly via observability). D2: medium (adds a new field; small shape change). D3: strong. D4: strong (the observability is what completes the procedural layer). D5: medium. D6: medium (adds content; not pure minimum). D7: medium-strong. D8: medium-strong (preserves shape barely; close to but not breaking D8 criterion 5).

**Verdict: SURVIVE.** Refinement: commit to format (one-line italics annotation, ≤80 chars per entry). Position: viable region.

---

### S5 — Specification-language axiom/theorem framing

Already merged into S4 by innovation. No standalone evaluation needed.

**Verdict: MERGED into S4 (formal vocabulary dropped; derivation idea retained).**

---

### S6 — Dissolve meta-principle/entry split

Already parked as RESEARCH FRONTIER by innovation (loses abstraction value).

**Verdict: RESEARCH FRONTIER (confirmed by critique).**

---

### S7 — Recognize-latent-mechanism framing

**Prosecution.** Killer objection: "framing" alone doesn't prevent anything. The mechanism (S1+S2+S3+S4) is what prevents; the framing is descriptive. **Specific failure-case:** the framing is correct but produces no behavior change without the underlying mechanisms. **Specification-gap:** the framing is communicated to the user but doesn't translate to action without the mechanisms it shapes.

**Defense.** Deepest strength: shapes the implementation toward MINIMUM CONTENT ADDITION; without this framing, the temptation is to add heavy new specs. The framing IS the design constraint that keeps the mechanisms lightweight.

**Collision.** Defense wins on the shaping role. Prosecution's "framing alone doesn't prevent" is technically correct but misses S7's actual role: it's a design constraint on S1-S4, not a standalone mechanism. Implementing S1-S4 *without* the latent-mechanism framing risks over-engineering each piece.

**Dimension scoring.** D1: indirect (shapes the mechanisms that address the cause). D2: very strong (forces alignment with existing doc). D3: very strong (no per-entry or per-doc cost). D4: indirect. D5: strong (shapes future mechanism additions too). D6: very strong (parsimony is the framing). D7: indirect. D8: very strong (the framing is what keeps the discipline "easy").

**Verdict: SURVIVE** as a design constraint shaping the implementation of S1-S4, not as a standalone deliverable. Position: viable region (as shaper).

---

### S8 — Cross-doc extension via per-entry trigger

**Prosecution.** Killer objection: the user didn't ask about cross-doc extension. Including it in the deliverable scope-creeps the inquiry. **Specific failure-case:** user reads about cross-doc extension; feels overwhelmed by scope; doesn't apply *any* of the mechanism even to `harmony_layer.md`. **Specification-gap:** how does the user identify which entries in `notes.md` / `advanced_principles.md` have the principle/application split structure? Innovation says "per-entry trigger" but doesn't specify the trigger predicate operationally. **User-perspective objection:** the user's question explicitly named `harmony_layer.md`; extending to other docs may not be wanted now.

**Defense.** Deepest strength: aligns with the pattern-level diagnosis from sensemaking. The mechanism's trigger is the *structural pattern*, not the doc identity. If sibling docs exhibit the pattern, the mechanism applies; if not, it doesn't.

**Collision.** Defense wins on generalizability (D5). Prosecution's "scope creep" concern is real and addressable: S8 is presented as an OPTIONAL extension clearly marked, with the trigger predicate specified operationally ("any entry that derives a classification from a stated principle in the same doc"). The user opts in or skips.

**Dimension scoring.** D1: indirect for harmony_layer.md, direct for sibling docs. D2: strong. D3: medium (requires per-entry assessment when extending). D4: strong (covers cross-doc dimension of the cause). D5: very strong. D6: medium. D7: strong. D8: medium-strong.

**Verdict: REFINE.** Direction: mark as optional extension; specify the trigger predicate operationally; do not include in MUST. Position: boundary → viable after refinement.

---

### S9 — Surface apply-now-vs-defer choice

**Prosecution.** Killer objection: surfacing the choice without recommendation puts cognitive load on the user. **Specific failure-case:** decision paralysis — user reads both options, can't decide, defers indefinitely; existing ≥11 contradictions persist. **Specification-gap:** should the inquiry recommend one option as default?

**Defense.** Deepest strength: respects user agency; the user knows their time constraints better than the inquiry does.

**Collision.** Both arguments have merit. Refinement: provide both options PLUS a default recommendation that the user can override. The default is "apply now" (15-60 min one-time produces immediate consistency; effort is bounded; surfacing's enumeration A-8 through A-19 provides the input set). User can override to "defer."

**Dimension scoring.** D1: indirect (deployment decision, not mechanism). D2: strong. D3: strong. D4: strong (covers retroactive deployment). D5: medium. D6: strong. D7: medium-strong (depends on whether user chooses apply-now). D8: strong (the choice respects "easy" by not forcing application).

**Verdict: REFINE.** Add default recommendation ("apply now"; user can override with reason). Position: boundary → viable after refinement.

---

### S10 — MVF-4 composition (independent + coexisting)

**Prosecution.** Killer objection: this is a one-paragraph clarification, not really a candidate. **Specific failure-case:** user doesn't read the composition note, applies both MVF-4 and the retroactive sweep, redundantly fixes register. Minor cost. **Specification-gap:** trivial.

**Defense.** Strength: prevents confusion about whether the new prevention obsoletes MVF-4; preserves continuity with prior inquiry.

**Collision.** Defense wins trivially. The intervention is small but the integration value is real.

**Dimension scoring.** D1: not applicable (integration note, not mechanism). D2: strong. D3: very strong. D4: integration coverage. D5: low. D6: very strong. D7: indirect. D8: very strong.

**Verdict: SURVIVE.** Position: viable region (small but real).

---

### S11 — Terse cause communication

**Prosecution.** Killer objection: terseness assumes the user has the prior inquiry's finding in working memory. **Specific failure-case:** user reads this finding 6 months from now without re-reading the prior; terse cause is incomprehensible. **Specification-gap:** how terse is too terse?

**Defense.** Deepest strength: the user explicitly continues from the prior inquiry; their working memory IS loaded with the diagnostic background; redundant re-explanation has cost.

**Collision.** Defense wins for the immediate case; prosecution's "6 months later" case is real. Refinement: terse summary PLUS an explicit cross-reference to the prior inquiry's finding for context-loading by future readers.

**Dimension scoring.** D1: not applicable (communication choice). D2: strong. D3: very strong. D4: framing coverage. D5: low. D6: very strong. D7: indirect. D8: very strong.

**Verdict: REFINE.** Add explicit cross-reference to `devdocs/inquiries/2026-06-03_23-30__translation_failure_root_cause_diagnosis/finding.md`. Position: viable region after refinement.

---

### Emergent Assembly — "lightweight in-doc consistency discipline"

**Prosecution.** Killer objection: ≥4 coordinated pieces (S1 + S2 + S3 + S4) might exceed the "easy" criterion when summed. Each is individually easy; together they constitute a discipline shift. **Specific failure-case:** user implements S1 (the principle-as-test edit) but defers S2 (audit) and S4 (trace); the procedural test without observable record and end-of-edit audit doesn't get applied consistently. Partial implementation → partial protection. **Specification-gap:** implementation order? Innovation gave the procedure but not the staged-introduction order.

**Defense.** Deepest strength: addresses the procedural cause completely; meets the 5 "easy" criteria as composite; produces internal consistency without architectural change. Each piece is independently valuable; partial implementation still produces partial value.

**Collision.** Defense wins on coverage. Prosecution's partial-implementation concern is addressable by specifying staged implementation order:
1. **S1 (meta-principle edit + short procedure spec)** — smallest immediate change; ~10 min one-time.
2. **S2 (audit checklist as permanent doc section)** — ~5 min one-time to author the checklist.
3. **S3 (EXCEPT-WHEN format)** — applied only to Tier 3 entries with negative claims; specified once, applied incrementally as entries get re-touched.
4. **S4 (per-entry application trace)** — applied to new entries going forward; optional retroactive application.

Total day-one effort: ~15 min (S1 + S2). Ongoing effort: ~1 min per new entry (S3 + S4).

**Dimension scoring.** D1: very strong. D2: strong. D3: strong (staged). D4: very strong (full procedural-layer coverage). D5: strong. D6: medium (composite of 4 pieces). D7: very strong. D8: strong as composite (verified within all 5 sub-criteria when staged).

**Verdict: SURVIVE.** Refinement: explicit staged implementation order in the deliverable. Position: dominates individual-survivor space.

---

### Critique-surfaced — Minimum Viable Discipline (MVD): S1 + S2

**Critique-observed:** what if the user implements only S1 + S2? Is that enough?

Structurally, yes. S1 makes the test instruction explicit; S2 catches inconsistencies at end-of-edit. Together they constitute a minimum viable consistency discipline. S3 (EXCEPT-WHEN format) and S4 (per-entry trace) are observability and explicit-scope additions that improve the mechanism but aren't strictly required for the cause to be addressed.

**Estimated effort:** ~15 minutes total day-one (S1 + S2 authoring). Per-entry overhead ≤1 min (the test is one-line). Retroactive sweep effort ~15-60 min for the ≥12 Tier 3 entries.

**Dimension scoring.** D1: strong (addresses cause). D2: strong. D3: very strong. D4: covers procedural cause minimally. D5: medium (less robust to unknown future patterns than the Emergent Assembly). D6: very strong (true minimum). D7: strong. D8: very strong.

**Verdict: SURVIVE** as a user-choice sub-option for users who want absolute minimum effort. Position: viable region (parsimony-dominant).

---

## Phase 3.5 — Assembly Check (cross-survivor)

Two assemblies emerge as user-choice sub-options:

| Sub-Assembly | Composition | Effort | Coverage |
|---|---|---|---|
| **MVD — Minimum Viable Discipline** | S1 + S2 + (S9 default: apply now) + (S10 MVF-4 note) + (S11 terse cause) | ~15-30 min day-one + ~15-60 min retroactive sweep | Procedural cause covered minimally; ≥12 Tier 3 contradictions identified at retroactive sweep; ongoing protection via S1+S2 |
| **Full Emergent Assembly — Lightweight In-Doc Consistency Discipline** | MVD + S3 + S4 + (S7 framing) + (S8 cross-doc extension as optional) | ~30 min day-one + retroactive sweep + ~1 min/entry going forward | Procedural cause covered fully; observability via S4; scope clarity via S3; cross-doc generalizability via S8 |

Both are viable; both meet the "easy" criterion (with the Full Emergent Assembly meeting it as composite, not per-piece). The user picks based on appetite.

---

## Phase 4 — Coverage + Convergence Assessment

### Coverage map

**Cause-layer coverage:**
| Layer | Surviving candidates that address it |
|---|---|
| **Procedural (Layer 1; in-scope)** | S1 ✓, S2 ✓, S3 ✓, S4 ✓ (all SURVIVE) |
| **Architectural (Layer 2; out of scope)** | S6 RESEARCH FRONTIER; Lens Shifting contrarian RESEARCH FRONTIER; inherited from prior S7 |

**Deployment-mode coverage:**
| Mode | Surviving candidates |
|---|---|
| Prospective (new entries) | S1 + S4 + S3 |
| Retroactive (existing Tier 3) | S2 + S3; S9 (apply-now vs defer choice) |
| Cross-doc extension (sibling docs) | S8 (optional) |

**"Easy" criterion coverage:**
| Sub-criterion | Verified by |
|---|---|
| Per-entry cost ≤2 min | S1 + S4 design; verified in S1 dimension scoring |
| Audit cost ≤15 min one-time | S2 design (5 items); verified in S2 dimension scoring |
| No new tooling | Confirmed across all SURVIVE candidates |
| User-solo-applicable | Confirmed across all SURVIVE candidates |
| Preserves doc shape | S1 + S4 lightweight design; confirmed across all SURVIVE candidates |

All 5 "easy" sub-criteria met by both MVD and Full Emergent Assembly. **Coverage complete.**

### Unexplored regions assessment

- **Tooling-based fixes:** intentionally out of scope per D8 (no new tooling). No coverage need.
- **Architectural redesign:** intentionally out of scope per "easy" criterion. Inherited unexplored.
- **Whole-doc cross-extension:** partially addressed via S8 (per-entry trigger); whole-doc remains unexplored. Not critical; the per-entry trigger is the correct shape per the pattern-level diagnosis.

No critical unexplored regions.

### Convergence assessment

- **Clean SURVIVE on critical dimensions?** YES — multiple candidates (S1, S2, S3, S4 individually; MVD and Full Emergent Assembly as composites) survive clean on D1, D4, D7, D8 (all critical-weight).
- **Two consecutive iterations land in new regions?** UNLIKELY. Innovation produced 11 individual candidates + 1 emergent; critique surfaced 1 sub-assembly; total 13 evaluated. Innovation's mechanism coverage was full (4G + 3F). Inherited Frame Audit did not fire in innovation. Additional iteration would land in already-mapped regions.
- **Unexplored regions critical?** NO (all out-of-scope or already-covered).
- **Accumulator decreasing rate?** YES — innovation reported convergence with ≥3 mechanisms converging on "lightweight edit + audit + per-entry trace"; critique confirmed via 13 candidates with consistent landscape positions.

**All convergence criteria met.**

### Signal: TERMINATE

Coverage sufficient. Convergence reached. Clean SURVIVE exists. Output ranked survivors below.

---

## Ranked Survivors

| Rank | Candidate | Verdict | Position | Effort |
|---|---|---|---|---|
| 1 | **Full Emergent Assembly** (MVD + S3 + S4 + S7 framing + S8 optional + S10 + S11) | SURVIVE | Central viable region | ~30 min day-one + sweep + ~1 min/entry |
| 2 | **MVD — Minimum Viable Discipline** (S1 + S2 + S9 default + S10 + S11) | SURVIVE | Viable region (parsimony-dominant) | ~15-30 min day-one + sweep |
| 3 | **S1 — Lightweight principle-as-test edit + short procedure spec** | SURVIVE | Viable region | ~10 min one-time |
| 4 | **S2 — End-of-doc audit checklist as permanent section** | SURVIVE | Viable region | ~5 min to author; ~15 min per audit |
| 5 | **S3 — EXCEPT-WHEN clause format** | SURVIVE | Viable region | per-entry on Tier 3 |
| 6 | **S4 — Principle-application trace per entry** | SURVIVE | Viable region | ~30 sec per new entry |
| 7 | **S7 — Recognize-latent-mechanism framing** | SURVIVE (as design constraint) | Viable region | zero direct cost |
| 8 | **S9 — Surface apply-now-vs-defer with default "apply now"** | SURVIVE after refinement | Viable region | user decision |
| 9 | **S10 — MVF-4 composition note** | SURVIVE | Viable region | one paragraph |
| 10 | **S11 — Terse cause + cross-reference** | SURVIVE after refinement | Viable region | one short section |
| 11 | **S8 — Cross-doc extension as optional** | REFINE → conditional SURVIVE | Boundary → viable | per-entry trigger when extending |
| 12 | **S5 — Specification-language framing** | MERGED into S4 | n/a | n/a |
| 13 | **S6 — Dissolve principle/entry split** | RESEARCH FRONTIER | Unexplored long-term | n/a |

**0 KILLs.** Every candidate either SURVIVEs, REFINEs to viable form, or is parked as long-term research.

---

## Constructive Output Summary

**For the user:**

The cause has been diagnosed and the prevention is two-faced (prospective + retroactive). Two user-choice paths:

**Path A — Minimum Viable Discipline (MVD, ~15-30 min day-one + ~15-60 min retroactive sweep):** S1 + S2 + S9 default + S10 + S11. Edit the meta-principle in `harmony_layer.md` to include the test instruction. Add a 5-item Doc Consistency Audit section as the permanent last section of `harmony_layer.md`. Run the audit once over existing Tier 3 entries (surfacing's A-8 through A-19 provide the input set; user can override default and defer if pressed). The cause is addressed minimally.

**Path B — Full Emergent Assembly (Lightweight In-Doc Consistency Discipline, ~30 min day-one + sweep + ~1 min/entry ongoing):** MVD + S3 (EXCEPT-WHEN format) + S4 (per-entry application trace) + S7 framing + S8 optional cross-doc extension. The cause is addressed fully; observability via per-entry trace; explicit scope via EXCEPT-WHEN; cross-doc pattern-based extension available if user opts in.

**Future research:**
- S8 wholesale cross-doc extension if desired (notes.md + advanced_principles.md): revival trigger = user opts in.
- S6 dissolution of principle/entry split (RESEARCH FRONTIER): structurally interesting; not actionable now.
- Architectural Layer-2 fix (inherited from prior S7): unchanged; remains RESEARCH FRONTIER.

---

## Convergence Telemetry

- **Dimension coverage:** 8 dimensions (6 default + 2 project-specific risk per Phase 0 refinement). All relevant; all discriminate; weights assigned per HIGH-stake context.
- **Adversarial strength:** STRONG. Every candidate received both prosecution and defense. Multi-axis prosecution depth applied (user-perspective objections; specific failure-case scenarios; specification-gap probes). Multiple REFINE verdicts; no rubber-stamps.
- **Landscape stability:** STABLE. 13 candidates cluster into 3 regions: viable (10), boundary-to-viable-via-refinement (2), unexplored-long-term (1).
- **Clean SURVIVE exists:** YES. S1, S2, S3, S4, MVD, Full Emergent Assembly all survive clean on critical-weight dimensions.
- **Failure modes observed:**
  - Wrong Dimensions: NO (extracted from sensemaking; project-specific risk axes included).
  - Rubber-stamping: NO (multiple REFINEs; defense did not pass everything).
  - Nitpicking: NO (no KILLs; defense applied to every candidate).
  - Dimension Blindness: NO (cross-referenced sensemaking perspectives; the "easy" criterion explicitly operationalized as D8).
  - False Convergence: NO (clean SURVIVE present; coverage adequate).
  - Evaluation Drift: NO (consistent dimensions across all candidates).
  - Self-Reference Collapse: NO (external grounding via the empirically verifiable contradictions in the doc).

### Overall verdict: **PROCEED**

All gates passed. Termination signal valid. The MVD and the Full Emergent Assembly both qualify as deliverables meeting the user's "easy" criterion. The user picks based on their preferred depth of intervention.
