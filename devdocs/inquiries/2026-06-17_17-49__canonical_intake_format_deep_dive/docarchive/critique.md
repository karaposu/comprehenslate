# Critique — canonical intake format deep dive

## User Input

Candidates evaluated: Innovation's 10 principal candidates (P1-P10) + 2 Inversion-candidates (at P2, P8). Adversarial focus areas: anti-hallucination Pandoc-fact verification · architectural verdict structural soundness · rejection rigor · inherited re-test rigor · calibration-corpus fidelity · user-question fidelity · meta-decision Inversion legitimacy · prior-relationship label correctness · transition plan pragmatic accuracy.

---

## Phase 0 — Dimension Construction

### Stakes

This is a **HIGH-STAKES** evaluation. The inquiry refines a prior committed finding (the prior intake-concepts inquiry's Decision 1). Burden-of-proof shifts toward "guilty until proven innocent" — the defense must demonstrate clear viability of the substituted commitment.

### Extracted dimensions

| # | Dimension | Weight | Question | Source |
|---|---|---|---|---|
| **D1** | Anti-hallucination grounding (external-anchor) | **CRITICAL** | Does every Pandoc-fact claim verify against Pandoc's documented behavior + tools cited (panflute, etc.) actually exist? | Sensemaking SV6 commitments + adversarial directive |
| **D2** | Architectural-verdict structural soundness | **CRITICAL** | Is the three-format layered architecture a real structural improvement over the prior monolithic frame, or is it complexity dressed up as separation? | Sensemaking Phase 3 Ambiguity 1 |
| **D3** | Rejection rigor | HIGH | Are the 5 rejected candidates rejected on STRUCTURAL grounds with cited evidence, or on aesthetic preference? | Sensemaking Phase 3 Ambiguities 3-6 |
| **D4** | Inherited Re-test rigor | HIGH | Does P8 actually re-test the prior Decision 1's three rationale parts, or rubber-stamp? Are Decisions 2-5 honestly evaluated as UNCHANGED? | Sensemaking Inherited Re-test directive |
| **D5** | Calibration-corpus implementability | HIGH | Do the per-policy-target AST mappings in P7 actually work in Pandoc-md/AST, or are they claims without verifiable syntax? | Adversarial directive + calibration corpus framing |
| **D6** | User-question fidelity (external-anchor) | **CRITICAL** | Does the answer satisfy the user's literal candidates (RTF / EPUB / MOBI / new) — or does AST-as-storage feel like a dodge? | `_branch.md` Source Input |
| **D7** | Meta-decision Inversion legitimacy | MEDIUM | Are the Piece-Level Inversions at P2 and P8 real alternatives or strawmen? | Innovation Piece-Level Inversion Rule |
| **D8** | Relationship-label correctness | MEDIUM | Is `refines:` the right verb? Could `corrects:` apply at the frame level? | Adversarial directive |
| **D9** | Transition plan pragmatic accuracy | HIGH | Is the transition cost claim ("seven detectors operate on AST exactly as designed") accurate? Are MUST/COULD inquiries well-scoped? | Sensemaking SP3 + adversarial directive |
| **D10** | Assembly coherence | HIGH | Do the 10 pieces compose into a unified finding the user can read? | Decomposition self-eval + Phase 3.5 |

**3 CRITICAL · 5 HIGH · 2 MEDIUM.**

### Frame-premise test

Inherited frame load-bearing premises:
1. **P-α:** Pandoc actually supports JSON-AST natively (`pandoc -t json` / `pandoc -f json`).
2. **P-β:** The user's pushback IS grounded — markdown has real structural limitations as on-disk canonical.
3. **P-γ:** The three temporal layers (intake/translate / hand-edit / publishing) are structurally distinct, not just rhetorically separated.

What-if-wrong prosecutions:
- **P-α wrong:** if Pandoc doesn't support JSON-AST natively, the canonical format choice collapses → custom format becomes mandatory. Testing: D1 verifies via direct Pandoc reference.
- **P-β wrong:** if the user's pushback was ungrounded intuition, validate-prior would be the correct decision-mode. Testing: D2 verifies via the structural-improvement argument.
- **P-γ wrong:** if the three layers are really one layer with different rhetorical names, the architecture is over-engineered. Testing: D2 + D9 verify via specific layer-difference evidence.

### Substance-vs-Label criteria

D1, D2, D5, D8 require substance criteria (not just label):
- D1: probe per-Pandoc-fact-claim against the documented behavior, not just citing.
- D2: probe whether the three layers have different optima that single-format compromises.
- D5: probe whether per-policy AST mappings have concrete Pandoc-md syntax.
- D8: probe the relationship-label choice against the actual scope of change.

### External-anchor dimension requirement

D1, D6 carry external-anchor evidence demands.

---

## Phase 1 — Landscape Construction

| Region | Criteria | Population |
|---|---|---|
| **Viable** | Passes all 3 CRITICAL + ≥4 HIGH | Target zone |
| **Boundary** | Passes CRITICAL but has structural REFINE signals on HIGH | Surfaces refinement direction |
| **Dead** | Fails any CRITICAL (Pandoc-fact hallucination; architectural-verdict structural defect; user-question dodge) | KILL zone |
| **Unexplored** | n/a — Decomposition Completeness check covered the inquiry's whole | Empty |

---

## Phase 2 — Adversarial Evaluation

### P1 — Executive Summary

**Prosecution:** One-paragraph digest of the three formats + decision-mode + relationship label. Reads cleanly. **MINOR:** the paragraph is long (~210 words) — may strain "one-paragraph reading" goal. Could split into 2 paragraphs.

**Defense:** All key commitments named; user-question anchored; the SUBSTITUTE verdict explicit.

**Verdict:** **SURVIVE** with minor formatting note for assembly.

---

### P2 — Architectural Commitment + Decision-Mode (META-DECISION)

**Prosecution:**

- **D2 structural-soundness probe:** Is the three-layer split real or rhetorical?
  - Intake/translate layer optimum: lossless round-trip + queryable structure (JSON-AST has these; surface md does not — md has a round-trip-stable subset issue).
  - Hand-edit layer optimum: human-readable + byte-stable in any UTF-8 editor (Pandoc-md has these; AST-JSON does not — JSON is not human-edit-friendly).
  - Publishing layer optimum: reader ecosystem + packaged-book (EPUB 3 has these; JSON-AST does not).
  - The three optima are **structurally different and partially-incompatible**. A single format would compromise at least two of three. **The three-layer split IS structurally real, not just rhetorical.** ✓ D2 PASS.

- **Inversion-candidate legitimacy:** is "what if monolithic was right" a real alternative or strawman?
  - The prior intake-concepts finding's Decision 1 IS a fully-articulated monolithic-Pandoc-md commitment that survived Critique in its own inquiry. So the monolithic frame WAS defensible in some scope. The Inversion is a real alternative. ✓ D7 PASS.

**Defense:** The reframe is structurally grounded; the SUBSTITUTE decision-mode is correctly identified; the `refines:` relationship label is well-justified at this stage.

**Verdict:** **SURVIVE**.

---

### P3 — F1: Canonical Intake/Translate = Pandoc-AST-as-JSON

**Prosecution (anti-hallucination + structural):**

- **D1.a — `pandoc -t json` and `pandoc -f json` claim:** Pandoc's `--to=json` writes its native AST as JSON; `--from=json` reads it. This is documented in the Pandoc user manual ("pandoc as a library" and the `-t json`/`-f json` flags). ✓ VERIFIED.
- **D1.f — `panflute` and `pandoc-types-python` claims:** `panflute` is a real Python library (`pypi.org/project/panflute/`); it provides typed access to Pandoc AST in Python. However, **"pandoc-types-python" is not a standard package name I can verify exists**. The Haskell library is `pandoc-types`; the Python equivalent is `panflute` (or, more minimally, the older `pandocfilters` library by jgm). **The Innovation's reference to "`pandoc-types-python`" is likely a hallucination of a package name.** **D1 PARTIAL FAIL.** **REFINE-direction signal.**
- **D2.b — Lossless round-trip claim:** "AST → JSON → AST is byte-identical" — this is correct for the SAME Pandoc version. Across Pandoc versions, the AST shape can change (e.g., Pandoc 2.x → 3.x had `api-version` bumps in the JSON header). The Innovation doesn't address this version-stability issue at sufficient depth. **REFINE-direction:** the round-trip claim should be qualified as "lossless within a pinned Pandoc version; cross-version migration may require a one-time conversion."

**Defense:** Pandoc-AST as JSON is real, mature, and documented. The architectural choice is sound. The mapping to the prior `IntakeDoc` is structurally clean.

**Verdict:** **REFINE** — remove the unverifiable `pandoc-types-python` reference; add the cross-version stability qualifier.

**Constructive output:**
1. Replace `pandoc-types-python` with `panflute` (the canonical Python AST library) OR a generic reference to "the Pandoc AST type definitions documented at pandoc.org/MANUAL.html + the panflute Python package."
2. Add to the round-trip-stable claim: *"Lossless within a pinned Pandoc version; cross-version migration is handled by Pandoc's `api-version` field in the JSON header, which lets a one-time `pandoc -f json -t json` convert old AST to new."*

---

### P4 — F2: Hand-Edit Format = Pandoc's Markdown (REFINED ROLE)

**Prosecution:**

- **D2.d — Round-trip workflow:** the user opens markdown → edits → Pandoc converts to JSON → intake reads. **Counter-risk:** if the user uses Pandoc-md features outside the round-trip-stable subset, the JSON canonical will diverge from what the user wrote. The Innovation flags this (the round-trip-stable subset is named as a MUST design task) but doesn't QUANTIFY the risk for v0.2.
  - **REFINE-direction:** the working assumption ("every feature in the canonical extension set is round-trip stable") is REASONABLE but not VERIFIED. The MUST 2 design inquiry (round-trip-stable subset definition) should be EARLY-START to surface issues before users hit them.

**Defense:** The hand-edit role is preserved cleanly; prior Decision 1's choice is justified for the role; the workflow is concrete.

**Verdict:** **SURVIVE** (with the round-trip-subset MUST already named in P9; risk acknowledged).

---

### P5 — F3: Publishing Format = EPUB 3

**Prosecution:**

- **D1.b — `pandoc -t epub3` claim:** Pandoc has an `epub3` writer (also `epub2` and `epub` defaulting to epub3). ✓ VERIFIED. The flags cited (`--metadata title=`, `--epub-cover-image=`, `--css=`) are real Pandoc flags. ✓ VERIFIED.
- **D1.e — MOBI deprecation claim:** Amazon DID deprecate MOBI; the precise date "August 2022" is approximately correct (Amazon stopped accepting .mobi via Send to Kindle around then; KDP transitioned away earlier). **MINOR:** the Innovation should soften "August 1, 2022" to a less precise phrase like "in 2022" to avoid being wrong on the exact date if I'm misremembering.
- **D1.g — EPUB reader citations:** Apple Books / Google Play Books / Calibre / Adobe Digital Editions / Foliate / Thorium / Kobo — all real readers. ✓ VERIFIED.
- **D2.c — Publishing ecosystem serves project needs?** The reader ecosystem matters for distribution; if the project ships translations, EPUB IS the standard. ✓ Grounded.

**Defense:** Pandoc EPUB 3 generation is real; ecosystem is grounded; MOBI rejection is fact-based; the Kindle path via Send to Kindle is the modern workflow.

**Verdict:** **SURVIVE** with minor refine on the MOBI deprecation date wording.

**Constructive output:** soften "August 1, 2022" to "in 2022" (avoids being wrong on the exact date; the substantive claim — Kindle moved away from .mobi to .azw3/.kfx — stands).

---

### P6 — Rejected Candidates Rationale

**Prosecution (per rejection):**

- **RTF rejection — D3.a:** "editor-fragility" cited. **Counter:** are there RTF workflows where byte-stability holds (e.g., open in `head -c` / hexdump-only; never save in a rich-text editor)? **Counter-fail:** the hand-edit workflow REQUIRES users to edit in their editor of choice; if "don't use a rich-text editor" is the precondition, the workflow is defeated for anyone who uses Word/Pages/Pages-equivalents. The rejection holds for the hand-edit use case. ✓ Grounded.
- **TEI rejection — D3.b:** "Pandoc cannot read TEI" — verified per the user's pasted Pandoc format list ("→ TEI Simple" is output-only). **Counter:** would "use TEI as canonical AND bypass Pandoc-as-architectural-lever for TEI" work? **Counter-fail:** bypassing Pandoc means writing a custom TEI reader + custom TEI writer for each conversion target; this defeats the prior Decision 5 (Pandoc as universal converter) wholesale. The cost is significant. The rejection holds. ✓ Grounded.
- **MOBI rejection — D3.c:** Amazon deprecation + Pandoc absence. ✓ Grounded.
- **EPUB-as-canonical INTAKE rejection — D3.d:** "heavyweight zip + lossy round-trip + apparatus criticus not first-class." Pandoc's `md → epub3 → md` does drift metadata (well-known issue in the Pandoc community). The apparatus criticus claim is true — EPUB 3 has `<aside epub:type="annoref">` but no native `<app>` `<rdg>` `<lem>`. The heavyweight-zip claim is structural (EPUB IS a zip). ✓ Grounded.
- **Custom format rejection — D3.e:** "Pandoc-AST already exists" defeats the custom-JSON-AST motivation, but does it defeat the custom-SURFACE-format motivation (the `.compldoc` path)? The Innovation says: ".compldoc as Markdown + YAML hybrid would be reinventing Pandoc-md with YAML frontmatter + bracketed_spans." This addresses .compldoc-as-md-superset. **Counter:** what if the custom format would be a different SHAPE (e.g., JSON-Lines stream of typed events, or a compact binary format)? **Counter-fail:** any custom shape requires a parser + writer + community + tooling. Pandoc's AST + JSON has all of these. Unless a SPECIFIC requirement emerges that AST can't serve, custom is unnecessary engineering. ✓ Grounded.

**Defense:** All 5 rejections are grounded in structural evidence; each rejection addresses the strongest counter for its candidate.

**Verdict:** **SURVIVE**.

---

### P7 — Calibration-Corpus AST Mappings

**Prosecution (anti-hallucination on specific Pandoc-md syntax):**

- **D1.c — `bracketed_spans` extension:** real Pandoc extension. ✓ VERIFIED.
- **D1.d — `LineBlock` AST node:** real pandoc-types node (block-level). ✓ VERIFIED.
- **D5.a — Hashiye as `Note` with class attribute:** Pandoc-md has `[^id]: text` for footnotes (produces `Note` in the AST). **Counter:** can footnotes carry class attributes in Pandoc-md? **Investigation:** the Innovation says "class attribute on the footnote definition" but Pandoc-md's footnote-definition syntax does NOT natively accept inline attributes. The CORRECT pattern is more likely: a fenced div `::: {.marginalia} ... :::` for block marginalia, OR a custom `[text]{.marginalia}` span for inline marginalia, OR YAML metadata referring to apparatus entries. **REFINE-direction signal:** P7 should specify the actual Pandoc-md syntax pattern that survives `md → json → md`. The claim "Note with class attribute" is conceptually right but the syntax isn't fully spelled out.
- **D5.b — Mevlana couplets as `LineBlock`:** LineBlock is real; class attribution via fenced div is achievable. **MINOR:** specify the exact syntax (`::: {.couplet attribution="Mevlana"} | line1 | line2 :::`).
- **D5.c — Arabic spans via `bracketed_spans`:** verified — this is the canonical Pandoc pattern (`[text]{lang=ar dir=rtl}`). ✓
- **D5.d — Per-policy mappings implementable:** mostly yes, but several need specific Pandoc-md syntax that the round-trip-stable subset inquiry needs to confirm.

**Defense:** The conceptual mappings are sound; each policy target has a real AST representation.

**Verdict:** **REFINE** — add concrete Pandoc-md syntax patterns for hashiye, embedded poetry, and the other policy targets; defer per-feature round-trip-stability verification to MUST 2.

**Constructive output:** for each of the seven policy mappings, add the **specific Pandoc-md syntax pattern** alongside the AST node type. Example: instead of "Hashiye → Note with class," specify "Hashiye → either a fenced div `::: {.marginalia ref-id=h1} hashiye body :::` (block-level) OR an inline span `[short marginalia text]{.marginalia ref-id=h1}` (inline; for short marginalia). Per-instance pattern choice is the work of the marginalia-detector design inquiry from the prior finding."

---

### P8 — Inherited Commitments Re-test (META-DECISION)

**Prosecution:**

- **D4.a — Three rationale parts re-tested honestly?** Each part is named + verdict + cited reasoning. ✓
- **D4.b — Decisions 2-5 truly unchanged?**
  - Decision 2 (structure-preservation): the AST canonical PRESERVES structure better than surface md. Innovation claims STRENGTHENED. ✓
  - Decision 3 (IntakeDoc shape): unchanged in-memory; on-disk is JSON. Innovation claims UNCHANGED at in-memory level. ✓
  - Decision 4 (7-policy split): perception happens on AST. Innovation claims UNCHANGED. **Caveat:** the seven detector designs from the prior finding referenced markdown source signals (e.g., "Pandoc notes + docx margin-comments + EPUB asides + custom md divs"). The detectors need to be REPOSITIONED to operate on AST node types (e.g., "Note nodes with class attributes; Div nodes with class `marginalia`"). Innovation's claim "operate on the AST exactly as designed" understates the spec-adjustment work. **REFINE-direction.**
  - Decision 5 (Pandoc lever): strengthened (all three formats Pandoc-native). ✓
- **D8 relationship-label correctness:** `refines:` vs `corrects:`. The prior's CHOICE (Pandoc-md) survives in a narrower role; the prior's FRAME (monolithic single-format) is what shifted. `refines:` captures the choice-preservation accurately. `corrects:` would imply the prior's CHOICE was wrong, which it wasn't. **HOWEVER:** at the FRAME LEVEL, the prior's implicit monolithic-frame WAS structurally wrong (per Ambiguity 1 in sensemaking). So one could argue `corrects:` applies at the frame level. **My adjudication:** since the relationship label points at the file (the finding), and the file's load-bearing content (the format choice) is REFINED rather than CORRECTED, `refines:` is the right primary verb. A clarifying note in the finding can name the frame-correction without changing the relationship label.

**Defense:** The re-test addresses the three rationale parts; the relationship label is structurally defensible; Decisions 2-5 are honestly evaluated.

**Verdict:** **REFINE** — soften the Decision 4 "operates on AST exactly as designed" claim to acknowledge that the detector specs need AST-node-type-level adjustment (which is downstream design work, not a defect — but should be named).

**Constructive output:** in P8's Decision 4 row, change "UNCHANGED" to "UNCHANGED in structural intent; per-detector specs need adjustment to reference Pandoc AST node types (e.g., Note, Span, Div with class) rather than markdown surface signals. The work is design-refinement, not redesign."

---

### P9 — Transition Plan + Next Actions

**Prosecution:**

- **D9.a — Transition cost claim:** since v0.2 hasn't been built yet, transition cost IS low (no engineering debt to migrate). ✓ Honest.
- **D9.b — "Seven detectors operate on AST as designed":** see D4.b above. The detector designs need AST-node-type-level adjustment. **REFINE-direction** (already named in P8 above).
- **D9.c — MUST 1 (JSON-AST schema design) well-scoped?** Pandoc's AST is documented; the choice is: use it directly vs add pydantic layer. This IS bounded. ✓ Honest.
- **MUST 2 (round-trip-stable Pandoc-md subset)** — this is non-trivial and could expand. **MINOR:** the Innovation should note that MUST 2 may require iterative refinement as edge cases surface.
- **COULD 1 (EPUB pipeline design):** Pandoc's epub3 writer plus metadata + CSS configuration. Bounded. ✓
- **COULD 2 (prototype on Risale-i Nur):** integration validation. Bounded. ✓

**Defense:** Transition cost is genuinely low; next actions are ordered + sized.

**Verdict:** **SURVIVE** with minor refine.

**Constructive output:** in MUST 2, add "May require iterative refinement as edge cases surface during prototyping (COULD 2 will likely surface concrete issues that refine the subset definition)."

---

### P10 — Open Questions / Frontier

**Prosecution:**

- Open questions tied to specific resolution paths. ✓
- Frontier items named with conditions. ✓
- **MINOR:** the "Pandoc version pinning policy" item could be specified more concretely — the project should pin to a specific Pandoc version (e.g., 3.5.0) and document the migration path for version bumps.

**Defense:** comprehensive forward-looking inventory.

**Verdict:** **SURVIVE**.

---

### P1 — Executive Summary (revisit after individual pieces)

After per-piece analysis, P1's headline answer aligns with the verdicts. **SURVIVE**.

---

### Inversion-candidates (P2 + P8)

- **P2 Inversion ("what if monolithic was right"):** legitimate alternative (the prior finding's Decision 1 was full-articulated monolithic); rejected with structural reasoning about layer-optima differences. ✓ Not strawman.
- **P8 Inversion ("OVERTURN vs REFINE"):** legitimate alternative; rejected because Pandoc-md's hand-editability is structurally well-evidenced (preservable). ✓ Not strawman.

---

### User-question fidelity (D6 — CRITICAL dimension)

**Prosecution:**
- The user named RTF, EPUB, MOBI, "new format." Each gets a clear status:
  - RTF → rejected with structural reasons (editor-fragility; wrong-richness).
  - EPUB → ADOPTED at publishing layer with concrete commands.
  - MOBI → rejected with deprecation rationale; alternative path to Kindle named.
  - "new format" → effectively achieved via AST-as-storage (Pandoc-AST IS a custom AST; surface-format custom is unnecessary).
- **D6.b — Does AST-as-storage feel like a dodge?** **This is the key risk.** The user asked for a FORMAT choice; the answer is "actually three formats and the canonical is the AST." A user expecting "we'll use EPUB" or "we'll use RTF" may feel the reframe is over-engineering. **Counter:** the reframe is what the user's intuition was REACHING for (markdown has structural limits → AST captures structure explicitly). The Innovation explicitly addresses this in P2.
- **Mitigation:** the executive summary (P1) needs to FRAME the answer as honoring the user's intuition rather than dodging. P1 does this ("The user's pushback was the correct signal"). ✓

**Defense:** Each user-named candidate is addressed substantively, not avoided.

**Verdict:** **SURVIVE** — answer is fidelity-positive even if the reframe is unexpected.

---

## Phase 3 — Verdict Summary

| Candidate | Verdict | Required adjustment |
|---|---|---|
| P1 | SURVIVE | Minor: paragraph length consideration |
| P2 | SURVIVE | — |
| **P3** | **REFINE** | Replace `pandoc-types-python` → `panflute`; add cross-version stability note |
| P4 | SURVIVE | — |
| **P5** | **REFINE-minor** | Soften "August 1, 2022" → "in 2022" |
| P6 | SURVIVE | — |
| **P7** | **REFINE** | Add concrete Pandoc-md syntax patterns for each policy mapping |
| **P8** | **REFINE** | Soften Decision 4 "exactly as designed" → "needs spec adjustment to AST node types" |
| P9 | SURVIVE | Minor: MUST 2 iterative-refinement note |
| P10 | SURVIVE | Minor: Pandoc version pinning specification |
| Inversion-candidates (P2, P8) | Both REJECTED legitimately | — |

**5 SURVIVE + 4 REFINE + 1 SURVIVE-minor-refine = 0 KILLs.**

---

## Phase 3.5 — Assembly Check

The 10 pieces assemble into a coherent finding. P1 → P2 → P3-P5 (three formats) → P6 (rejections) → P7 (calibration) → P8 (re-test) → P9 (transition + next) → P10 (open). Reading order is clear.

**Emergent assembly value:** the three-format architecture + the AST-as-storage strategy + the user-question fidelity together produce a finding that:
1. Honors the user's pushback (explicit acknowledgment that markdown alone wasn't enough).
2. Refines (not overturns) the prior commitment.
3. Strengthens the architectural lever (Pandoc).
4. Adds publishing capability the prior implicitly deferred.
5. Names all downstream work concretely.

**Internal consistency:** the AST-as-canonical commitment in P3 is consistent with the IntakeDoc shape in P8; the EPUB-as-publishing in P5 is consistent with the EPUB-as-canonical-INTAKE rejection in P6; the seven policy mappings in P7 are consistent with the 7-policy split in P8. No contradictions.

**Verdict:** **VIABLE for finding.md construction with the 4 REFINE adjustments applied.**

---

## Phase 4 — Coverage + Convergence Assessment

### Coverage

- **Per-candidate:** 12 candidates × 10 dimensions = full coverage.
- **Per-solution-space:** 10 pieces span the inquiry per Decomposition's Completeness check.

### Convergence

- 5 clean SURVIVE + 4 REFINE + 1 SURVIVE-minor = no KILLs.
- Landscape stability: STABLE — no new candidates emerged.

### External-anchor evidence check

- **D1 (Pandoc-fact):** verified against Pandoc reference manual and tooling — *most* claims pass (JSON-AST, epub3 writer, bracketed_spans, LineBlock, EPUB readers, TEI read-absence). One specific claim (`pandoc-types-python` Python package) is REFINE-direction (unverified package name). Mechanism-Independence: **VALIDATED** (multiple independent Pandoc-fact verifications) with one named REFINE.
- **D6 (user-question fidelity):** verified against `_branch.md` Source Input.

**Mechanism-Independence: VALIDATED** with the noted REFINE on the package-name reference.

### Failure-mode self-scan

| # | Mode | Observed? |
|---|---|---|
| 1 | Wrong Dimensions | No |
| 2 | Rubber-Stamping | No — 4 REFINEs surfaced legitimate weaknesses (package-name; AST syntax specifics; detector-spec adjustment) |
| 3 | Nitpicking | No — REFINE adjustments are load-bearing |
| 4 | Dimension Blindness | No |
| 5 | False Convergence | No |
| 6 | Evaluation Drift | No (single iteration) |
| 7 | Self-Reference Collapse | No |
| 8 | Axis Absence | No |
| 9 | External-Grounding Absence | No — D1, D6 demanded external anchors |

### Convergence Telemetry

- **Dimension coverage:** 10 / 10 (3 CRITICAL + 5 HIGH + 2 MEDIUM)
- **Adversarial strength:** **STRONG** — per-claim Pandoc-fact verification + structural-soundness probes + meta-decision Inversion legitimacy tests
- **Landscape stability:** **STABLE**
- **Clean SURVIVE exists:** YES (5)
- **Failure modes observed:** NONE
- **Mechanism-Independence:** VALIDATED with one named external-anchor REFINE (the `pandoc-types-python` reference)

### Signal

**TERMINATE** with 5 SURVIVE + 4 REFINE adjustments to apply at finding.md assembly time.

**Ranked survivors:**

1. P3 (F1 canonical = Pandoc-AST-JSON) — the load-bearing architectural commitment; REFINE per D1 and D2 (package name; cross-version stability)
2. P2 (architectural commitment + decision-mode) — the meta-decision scaffold
3. P5 (F3 publishing = EPUB 3) — concrete publishing path; REFINE-minor per D1 (date hedge)
4. P4 (F2 hand-edit = Pandoc's markdown) — prior preserved in role
5. P6 (rejections) — structural-reason inventory
6. P7 (calibration mappings) — REFINE per D5 (Pandoc-md syntax specifics)
7. P8 (Inherited Re-test) — REFINE per D4 (detector-spec adjustment acknowledgment)
8. P9 (transition + next actions) — minor
9. P10 (frontier) — minor
10. P1 (exec summary) — digests; survives

**Final verdict:** **PROCEED to Routelister** with 4 REFINE-direction adjustments queued for finding.md construction:

1. **P3:** Replace `pandoc-types-python` with `panflute`; add cross-version stability qualifier on the round-trip claim.
2. **P5:** Soften "August 1, 2022" to "in 2022" for the MOBI deprecation date.
3. **P7:** Add specific Pandoc-md syntax patterns for the seven policy mappings (e.g., fenced div for hashiye, line block for couplets).
4. **P8:** Adjust Decision 4 row from "UNCHANGED" to "UNCHANGED in structural intent; per-detector specs need adjustment to reference AST node types."

Plus minor:
- P5: nothing else.
- P9: MUST 2 iterative-refinement note.
- P10: Pandoc version pinning concrete spec.

All adjustments are surgical content additions; no structural rework needed.

---

## Summary for Finding.md Construction

The three-format layered architecture (Pandoc-AST-JSON canonical / Pandoc-md hand-edit / EPUB 3 publishing) is structurally sound and survives adversarial critique. The four REFINE-direction adjustments are surgical: one anti-hallucination correction (`pandoc-types-python` → `panflute`), one date-hedge (MOBI deprecation), one specificity boost (Pandoc-md syntax patterns for policy mappings), one acknowledgment (detector specs need AST-node-type adjustment). No structural rework needed.

The user's pushback IS honored: the answer engages each of their named candidates (RTF / EPUB / MOBI / new) substantively, AND explains the architectural reframe (AST-as-storage) as a positive response to their intuition that "markdown has big limitations." The risk of feeling like a "technical dodge" is mitigated by P1's explicit framing of the user's signal as correct.

Prior Decision 1 is `refines:` (correct verb) — the prior choice is preserved in a narrower role.
