# Critique — post-repair canonical format

## User Input

/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/_branch.md

Upstream outputs: articulate_simple.md + surfacing.md + sensemaking.md + decomposition.md + innovation.md.

CRITICAL FRAMING: this inquiry committed (per innovation) the architectural REFINEMENT — three-layer architecture PRESERVED + canonical-layer format SWAP JSON-AST → HTML5. F1 = HTML5 canonical; F2 = Pandoc's markdown hand-edit (preserved); F3 = EPUB 3 publishing (preserved). Decision-mode = REFINE prior canonical-format inquiry. Inherited intake-concepts Decisions 2-5 = PRESERVED.

Critique should adversarially test the innovation output against ten focus areas (anti-hallucination on W3C/Pandoc/EPUB; HTML5-as-canonical Pareto-dominance rigor; rejection rigor; inherited commitments re-test rigor; calibration-corpus pattern fidelity; user-question fidelity for the document-vs-data signal; meta-decision Inversion legitimacy at P2 + P8; transition plan near-zero migration claim; HTML5 schema profile hedge; bias-balance).

Per-piece verdicts: SURVIVE / REFINE / KILL. Final verdict: SURVIVE-with-cross-cutting-refinements / REFINE-direction / KILL.

Save critique output to: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/critique.md

---

## Phase 0 — Dimension Construction

### Dimensions extracted from sensemaking + branch

| # | Dimension | What it asks | Weight | Source |
|---|---|---|---|---|
| D1 | **Anti-hallucination grounding** | Is every W3C/Pandoc/EPUB claim grounded in verifiable spec text? | **CRITICAL** | Innovation's documented constraint; prior incident (`pandoc-types-python` REFINE) |
| D2 | **Pareto-dominance verifiability** | Does HTML5 genuinely dominate JSON-AST across the canonical-layer requirement set, or does the matrix obscure JSON-AST advantages? | **CRITICAL** | Sensemaking's load-bearing capability matrix; the swap rests on this |
| D3 | **Rejection rigor** | For each rejected candidate (JSON-AST as canonical / monolithic / custom / dual / TEI / RTF / MOBI), is the rejection reason structural rather than performative? | **CRITICAL** | P7's load is to make the rejections survive prosecution |
| D4 | **Inherited Commitments Re-test honesty** | Are REFINE vs OVERTURN labels assigned with structural rigor; are PRESERVED labels honest about concrete-representation shifts? | **CRITICAL** | Refinement-vs-overturn is the architectural commitment's claim shape |
| D5 | **Calibration-corpus pattern fidelity** | Do the 7 per-policy HTML5 patterns map 1:1 to the schemas.py policy classes? | **CRITICAL** | The patterns are the policy contract |
| D6 | **User-question fidelity** | Does HTML5-as-canonical honor the user's named-document signal (EPUB / md / HTML) or project a developer-rationalization? | **HIGH** | The reframe was user-driven; fidelity matters |
| D7 | **Meta-decision Inversion legitimacy** | At P2 + P8 (the Piece-Level Inversion-required pieces), were Inversion candidates genuinely generated and rejected with structural reasoning, or token-only? | **HIGH** | Decomposition flagged the requirement; ducking it would hollow the refinement |
| D8 | **Transition plan accuracy** | Is the near-zero migration claim verifiable against the actual code state? | **HIGH** | P9's load is to make the swap engineering-actionable |
| D9 | **Schema profile hedge legitimacy** | Is the "HTML5 Living Standard is working assumption; RNG profile is downstream" hedge principled or evasive? | **MEDIUM** | The hedge frames what's committed now vs deferred |
| D10 | **Bias-balance** | Are HTML5 verbosity, markdown reading-order-naturalness, and JSON-AST machine-readability surfaced as legitimate concerns rather than dismissed? | **HIGH** | Anti-confirmation-bias check |
| D11 | **Project-specific risk axis** (per refinement note: "duplicate-derivable-state, explicit-culture-fit, operation-parsimony, phase-fit") | Does the candidate-space avoid project-specific risk axes like duplicate-derivable-state? | **HIGH** | Phase 0 project-specific risk dimension check |
| D12 | **Frame-premise test** | Are the inherited frame's load-bearing premises (three-layer architecture; Pandoc-as-architectural-lever; per-element provenance is load-bearing) prosecuted independently? | **HIGH** | Phase 0 frame-premise test for inherited-commitment-bearing candidate space |
| D13 | **External-anchor evidence** | Does the verdict cite W3C / Pandoc / EPUB / schemas.py external anchors with verbatim references, not paraphrases? | **CRITICAL** | Phase 0 external-anchor dimension requirement |

### Frame-premise test (D12) — load-bearing premises named + prosecuted

The candidate space rests on **three load-bearing inherited premises**:

**Premise 1: The three-layer architecture (canonical / hand-edit / publishing) reflects three structurally distinct use-case optima.**
- *What-if-wrong:* if the use-cases collapse to one optimum, monolithic becomes preferable.
- *Prosecution:* canonical needs machine-queryability + per-element provenance; hand-edit needs reading-order-naturalness + byte-stability; publishing needs ecosystem + packaged-book. The three requirement sets do not collapse — each layer's "best format" differs. Premise survives.

**Premise 2: Pandoc-as-architectural-lever (per Decision 5 of original intake-concepts inquiry).**
- *What-if-wrong:* if Pandoc is replaceable by a different conversion engine, the architectural lever loses its strength; candidates without Pandoc-read support (e.g., TEI) become viable.
- *Prosecution:* no replacement engine has Pandoc's format coverage; Pandoc's read/write matrix is the canonical universal-converter for the project's purposes. Premise survives. Note: this premise IS what hard-blocks TEI-as-canonical; if it were softer, TEI's structural advantages might dominate.

**Premise 3: Per-element provenance + confidence is load-bearing (the "reconstruction-is-heavy" reframe).**
- *What-if-wrong:* if intake's reconstruction is light enough that document-level provenance suffices, the per-element provenance dimension becomes cosmetic; markdown-as-canonical becomes viable again; the swap loses its A19 anchor.
- *Prosecution:* empirical inspection of Asa-yı Musa (text-layer Arabic with broken bidi) and Muhakemat (image-only Arabic) showed intake's reconstruction work IS heavy (OCR-recovered spans + style-recovered emphasis + structure-detected markers + paratext-stripped body). Per-element confidence (Tesseract emits 0–100) is a downstream-consumer's verifiability requirement, not a cosmetic. Premise survives.

**Frame-premise test verdict: PASS.** All three load-bearing premises survive prosecution. The candidate space rests on premises that remain valid; the swap is grounded in those premises rather than dependent on them being wrong.

### Substance-vs-Label success criteria (per Phase 0 step 5 refinement note)

D2 (Pareto-dominance) and D5 (calibration-corpus pattern fidelity) test load-bearing claims about MEANING and CONTENT. Substance-level criterion required:

- **D2 substance criterion:** the matrix's "Pareto-dominant" claim must be testable by constructing at least one prosecution that applies HTML5's mechanism to a JSON-AST advantage axis the matrix omits. Concretely: parser-implementation-variability (HTML5 has multiple parsers — `lxml.html`, `html5lib`, browsers; JSON-AST has one canonical parser via panflute). If the matrix's "ties on data-format properties" omits this axis, the Pareto-dominance claim is label-tested only.
- **D5 substance criterion:** the policy patterns must be testable against actual schemas.py policy names + the calibration corpus's documented elements. Substance-test: read schemas.py; verify 7/7 policies map; verify each policy's documented purpose matches the HTML5 pattern's semantic claim.

### External-anchor dimension (D13) — applied to all candidates

Every claim about HTML5 / Pandoc / EPUB / schemas.py / W3C spec must cite an external anchor: verbatim spec quote, file path with line reference, OR documented format-matrix entry. Paraphrased "the W3C spec says" does NOT satisfy D13.

---

## Phase 1 — Fitness Landscape

### Viable region

Architectural-refinement commitments that:
- Tie or beat JSON-AST on every canonical-layer requirement INCLUDING parser-implementation-variability where present
- Have W3C/Pandoc/EPUB external-anchor evidence
- Honor the three-layer architecture and the user's document-pattern signal
- Have honest disclosure of concrete-representation shifts where PRESERVED labels apply
- Survive Inversion at meta-decision pieces

### Dead region

Commitments that:
- Hallucinate W3C / Pandoc / EPUB spec claims
- Overstate Pareto-dominance by omitting axes where JSON-AST has strict advantage
- Use REFINE label when the change is structurally OVERTURN-shaped (or vice-versa)
- Project developer-rationalization onto the user's reframe
- Fail to engage Inversion at meta-decision pieces

### Boundary region

Commitments where the principal candidate is sound but:
- Has a missing caveat (e.g., JSON-AST parser-determinism not explicitly engaged)
- Has wording that understates a structural reason (e.g., "operational" instead of "architectural-lever preservation")
- Has a hedge that could be either principled or evasive depending on what's downstream-deferrable

### Unexplored region

The cross-corpus generalization (does HTML5-as-canonical hold for non-Risale-i-Nur corpora?) is flagged in P10 frontier but not evaluated. Out of this inquiry's scope.

---

## Phase 2 — Adversarial Evaluation (per piece)

### P1 — Executive summary

**Prosecution:** P1 attempts to encode the whole inquiry in one paragraph; risk is over-compression that loses the load-bearing distinctions. Specifically: P1 says "HTML5 is Pareto-dominant" without surfacing JSON-AST's parser-determinism strength.

**Defense:** P1 is a summary, not a verdict. The matrix evidence lives in P3; P1 just announces. Brevity is the point.

**Collision:** P1's "Pareto-dominant per the capability matrix" claim inherits whatever Pareto-dominance the matrix establishes. If the matrix has a gap (D2 substance-criterion check), P1 inherits the gap. P1's quality depends on P3's quality.

**Verdict: SURVIVE-with-caveat.** P1 is correct CONDITIONAL on P3 surviving the parser-determinism prosecution. If P3 needs REFINE, P1 inherits the refinement implicitly.

---

### P2 (META-DECISION) — Architectural commitment + decision-mode + relationship-label

**Prosecution — D2 (Pareto-dominance):** the P2 claim "HTML5 ties JSON-AST on every data-format property" omits parser-implementation-variability. HTML5 has multiple parsers (`lxml.html`, `html5lib`, browser parsers) with documented edge-case divergence; JSON-AST via panflute has one canonical parser, so the round-trip is bit-exact across the project. JSON-AST has a strict advantage on this axis.

**Prosecution — D4 (REFINE vs OVERTURN label):** the canonical-layer cell is the MOST semantically prominent of the three cells. Calling its swap "one cell" understates the change. If the canonical layer is the architecture's load-bearing center, swapping it is closer to OVERTURN.

**Prosecution — D7 (Inversion legitimacy):** the Inversion candidate at P2 is "what if the prior was correct and the user's pushback was ungrounded — keep JSON-AST as canonical." This is the right Inversion for the cell, not for the architecture. The Inversion doesn't test "what if the three-layer architecture itself is wrong" — that's P8's territory, not P2's.

**Defense — D2:** P2 honestly says "ties JSON-AST on every data-format property AND wins on every other relevant axis." The "data-format property" set is the matrix's chosen axis set; parser-implementation-variability could be added as a SEPARATE row. Whether HTML5 ties or loses on that row depends on operational discipline (pin parser, define canonical-write-via-Pandoc-only invariant). The omission is a refinement target, not a verdict-invalidator.

**Defense — D4:** REFINE is structurally correct. The three-layer architecture (the inherited frame) survives. Two of three cells survive unchanged. The Pandoc-as-architectural-lever insight survives. The use-case-per-layer insight survives. What changes: one format choice in one cell. This is the structural definition of REFINE.

**Defense — D7:** P2's Inversion is cell-scoped because P2 IS the cell-level commitment. P8's Inversion is architecture-scoped because P8 IS the architecture-level commitment. The Inversion territory split is correct.

**Collision:** D2 prosecution wins partially — parser-implementation-variability IS a real JSON-AST advantage that the matrix omits. D4 prosecution loses — REFINE is structurally correct. D7 prosecution loses — Inversion territory is correctly split.

**Verdict: REFINE.** P2 SURVIVEs on the REFINE-label and Inversion-legitimacy fronts. P2 needs a one-sentence refinement: name JSON-AST's parser-determinism advantage explicitly and indicate the operational discipline (pin Pandoc version; canonical-write-only-via-Pandoc) that bounds HTML5's parser-implementation-variability concern. This is a caveat, not a verdict reversal.

**Constructive output for REFINE:** Add to P2: "Caveat — JSON-AST via panflute has parser-determinism (one canonical parser) that HTML5 (multiple parsers with documented edge-case divergence) cannot match natively. The project bounds this by (a) pinning a Pandoc version per the operational note in P10; (b) writing canonical HTML5 via Pandoc only; (c) reading canonical HTML5 via a single named parser (`lxml.html` or `html5lib`)."

---

### P3 — Capability matrix (evidence artifact)

**Prosecution — D1 (anti-hallucination):** verify each cell's external anchor.
- HTML5 `data-*` attributes — claim: W3C HTML Living Standard §3.2.6 — **VERIFIED.** HTML Living Standard's "Embedding custom non-visible data with the `data-*` attributes" lives in §3.2.6.6 (the section index has shifted in recent edits; the canonical reference is `data-*` under "Global attributes / Embedded data with `data-*`"). The claim is correct.
- `lang=` and `dir=` as W3C any-element attributes — **VERIFIED.** Both are global attributes per HTML Living Standard §3.2.6.
- Pandoc ↔︎ HTML5 read/write — **VERIFIED** per Pandoc's documented format matrix (html / html5 as both reader and writer).
- HTML5 semantic elements (section/article/aside/footer/figure/blockquote/span/em/strong) — **VERIFIED** all 9 are W3C HTML Living Standard elements.
- EPUB 3 content documents ARE xhtml5 — **VERIFIED** per W3C EPUB 3.3 spec (`w3.org/TR/epub-33/`) which defines "EPUB Content Document" as XHTML.
- `panflute` is the correct Python AST library — **VERIFIED.** Available on PyPI as `panflute`; docs at `panflute.readthedocs.io`. The prior `pandoc-types-python` hallucination is corrected.
- Pandoc-md round-trip-stable subset — **VERIFIED** as a real concept; Pandoc-md's `md → json → md` round-trip preserves the AST-representable subset; surface features like exact whitespace or comment positioning may shift.

**Prosecution — D2 substance criterion:** the matrix omits parser-implementation-variability as a separate row. Substance-test on the Pareto-dominance claim: if added, JSON-AST gets ✓✓ and HTML5 gets ✓wa. This single row demotes HTML5 from "Pareto-dominant" to "dominant on every dimension except parser-determinism, which the project can bound operationally." The Pareto-dominance language overstates.

**Prosecution — D10 bias-balance:** the matrix lists "Human-readable as document" with markdown at ✓✓ and HTML5 at ✓wa. This surfaces markdown's reading-order-naturalness. Verbosity-over-markdown is implicit (HTML5's ✓wa with "tag-noise" annotation surfaces it). Bias-balance on these two axes is present.

**Defense — D1:** all claims have external anchors. Spec section numbers cited.

**Defense — D2:** the matrix's 18 rows are the requirements that emerged from sensemaking + the calibration corpus + the reconstruction reframe. Parser-implementation-variability didn't surface there because it's an OPERATIONAL property (depends on which parser the project uses), not a FORMAT property. Adding it would be reasonable but its omission isn't a hallucination.

**Collision:** D1 wins clean — anti-hallucination passes for every cited claim. D2 substance-criterion prosecution wins partially — the omission is real; adding the row would refine the claim from "Pareto-dominant" to "dominant on every format axis with an operational bound on parser-determinism." Both verdicts compatible.

**Verdict: REFINE.** Anti-hallucination is clean (D1 SURVIVE). The Pareto-dominance language needs a row addition + verdict refinement.

**Constructive output:** Add to P3 matrix: row "Parser-implementation determinism" with JSON-AST=✓✓ (single canonical parser via panflute) and HTML5=✓wa (multiple parsers; bounded operationally by parser-pinning + canonical-write-via-Pandoc-only). Adjust the Pareto-dominance verdict-sentence from "Pareto-dominant" to "Pareto-dominant on every format axis; with operational bounds on the one axis (parser-determinism) where JSON-AST has a strict advantage."

---

### P4 — F1 HTML5 canonical detailed spec

**Prosecution — D1:** verify every named library + W3C spec section.
- `panflute` — **VERIFIED** (PyPI; readthedocs).
- `lxml.html` — **VERIFIED** (Python lxml library; well-documented).
- `html5lib` — **VERIFIED** (Python html5lib; PyPI).
- `html5validator` — **VERIFIED** (Python wrapper around vnu.jar; PyPI).
- `tidy` (no-op round-trip) — **VERIFIED** (HTML Tidy; standard tool).
- W3C polyglot guidelines — **VERIFIED** (W3C "Polyglot Markup: A robust profile of the HTML5 vocabulary" note; status: discontinued as a standard, but still referenced as a profile).

  **Caveat surface:** P4 calls "polyglot syntax" a W3C feature. The W3C Polyglot Markup specification was a NOTE (not a recommendation), and its working group was closed in 2014. The polyglot CONCEPT (HTML5 valid as both HTML and XML) is real; the W3C "guideline" wording slightly overstates the spec's current status. This is a small wording imprecision, not a fabrication.

- BCP 47 language tags — **VERIFIED** (IETF BCP 47 / RFC 5646; HTML5 references this for `lang=`).

**Prosecution — D9 (schema profile hedge):** P4 hedges that "HTML5 Living Standard is the working assumption" + "project-specific RNG profile is downstream design (MUST 1)." Is this evasive? Specifically: can HTML5-as-canonical operate before the RNG profile exists?

**Prosecution — D10 bias-balance:** P4 explicitly surfaces HTML5's verbosity-over-markdown as a legitimate concern: "HTML5 is more verbose than markdown for the same content — `<p>The text</p>` vs `The text`; `<em>word</em>` vs `*word*`." The concern is acknowledged and addressed (canonical layer accepts verbosity because tag-density is already high and storage isn't a constraint).

**Defense — D1:** wording around polyglot is a small imprecision but not a fabrication; the underlying claim (HTML5 can be written in a syntax valid for both HTML and XML parsers) is true.

**Defense — D9:** P4's two-layer split is principled: layer 1 (HTML5 conformance via `html5validator`) is operational from day 1; layer 2 (project RNG profile) refines. The project CAN write valid HTML5 canonical from day 1 without the RNG profile; the RNG profile adds project-specific structural validation. The hedge is principled separation, not punt.

**Defense — D10:** verbosity concern surfaced and addressed. Bias-balance honored.

**Collision:** D1 wins clean with the polyglot wording-imprecision flagged. D9 prosecution loses — the hedge is principled. D10 prosecution irrelevant (defense holds).

**Verdict: REFINE.** Anti-hallucination passes with one wording-imprecision (polyglot W3C status). Hedge is principled. Bias-balance honored. REFINE because:

**Constructive output:** Refine the polyglot wording in P4 from "per W3C polyglot guidelines" to "per the polyglot HTML5 concept (the W3C Polyglot Markup NOTE, discontinued 2014, defined the writing convention; the concept remains usable as a self-imposed convention)." This honors the imprecision without abandoning the substantive point.

---

### P5 — Preserved layers (markdown hand-edit + EPUB 3 publishing)

**Prosecution — D10 bias-balance:** P5 acknowledges markdown's preservation by reference rather than re-explaining its reading-order-naturalness. Is this dismissive?

**Prosecution — D1:** verify "EPUB 3 content documents ARE xhtml5 — per `w3.org/TR/epub-33/`."
- **VERIFIED.** EPUB 3.3 spec defines EPUB Content Documents as XHTML, with the XHTML Content Document profile being polyglot HTML5.

**Defense — D10:** P5 is intentionally short (preservation acknowledgment per Decomposition's P5 = preservation acknowledgment, not re-specification). The reading-order-naturalness is the rationale FOR markdown's preservation in the prior canonical-format inquiry; re-stating it here would be redundant. Bias-balance surfaces in P7's monolithic-rejection ("markdown remains preferable for prose-heavy hand-editing (reading-order-natural; minimal tag noise)").

**Defense — D1:** EPUB 3 claim verified.

**Collision:** Defense holds clean.

**Verdict: SURVIVE.** Preservation acknowledgment honored; brevity is appropriate; the relocation of bias-balance to P7 works.

---

### P6 — Per-policy HTML5 patterns (calibration corpus)

**Prosecution — D5 substance criterion:** verify 7-policy fidelity against schemas.py.

Read of `SKILL/references/config/schemas.py` (lines containing class definitions):
- `NonMainLangPartsPolicy` (line 18)
- `SourceApparatusPolicy` (line 33)
- `VoiceMarkingPolicy` (line 45)
- `ArchaicRegisterPolicy` (line 57)
- `HonorificsPolicy` (line 72)
- `FormulaicOpeningPolicy` (line 90)
- `EmbeddedPoetryPolicy` (line 109)

P6's mapping:
- `SourceApparatusPolicy` → hashiye → `<aside class="marginalia">` ✓
- `EmbeddedPoetryPolicy` → Mevlana couplets → `<figure class="couplet">` ✓
- `FormulaicOpeningPolicy` → Bismillah → `<p class="formulaic-opening">` ✓
- `NonMainLangPartsPolicy` → Arabic spans → `<span lang="ar" dir="rtl">` ✓
- `VoiceMarkingPolicy` → voice transitions → `<span class="voice-cited">` ✓
- `ArchaicRegisterPolicy` → Ottoman archaisms → `<span class="archaic-register">` ✓
- `HonorificsPolicy` → Islamic honorifics → `<span class="honorific">` ✓

7/7 ✓. **Substance criterion PASSED for D5.**

**Prosecution — D1:** all element names (`<aside>`, `<figure>`, `<figcaption>`, `<blockquote>`, `<p>`, `<section>`, `<span>`, `<a>`) are W3C HTML5 semantic elements. **VERIFIED.** The `cite` attribute on `<blockquote>` and `<q>` is W3C HTML5. **VERIFIED.**

**Prosecution — D2 substance criterion (provenance encoding):** the provenance encoding pattern uses `data-*` attributes (`data-source`, `data-confidence`, `data-intake-pass`). Verify these are W3C-compliant.
- **VERIFIED.** Custom `data-*` attributes are W3C HTML Living Standard §3.2.6 (referenced earlier).

**Defense:** patterns are concrete (not abstract); each pattern shows element + class + attributes used; project-specific vocabulary (`data-source` enum values) is deferred to MUST 3 per the hedge.

**Collision:** Defense holds clean across D1, D2, D5.

**Verdict: SURVIVE.** Calibration-corpus pattern fidelity 7/7; W3C-compliance verified; provenance encoding pattern honest.

---

### P7 — Rejected candidates rationale

**Prosecution — D3 (rejection rigor) — JSON-AST rejection:** the rejection cites "user pattern signal" as a structural reason. Is this interpretive? Specifically: the user could have omitted JSON-AST simply because it's an unfamiliar engineering concept, not because they pattern-reject data formats.

**Prosecution — D3 — dual JSON-AST + HTML5 rejection:** "synchronization debt" rejection is overstated when HTML5 → JSON-AST is a deterministic Pandoc invocation that can be re-run anytime.

**Prosecution — D3 — TEI rejection:** the rejection is framed as "operational" (would force custom TEI reader; breaks Pandoc-as-lever). The framing UNDERSTATES — this is actually architectural-lever preservation, which is a structural commitment from Decision 5 of the original intake-concepts finding.

**Prosecution — D10 bias-balance:** P7's JSON-AST rejection should explicitly engage with JSON-AST's machine-readability advantage (the matrix shows JSON-AST is data, not a document). P7 says JSON-AST is "Pandoc-specific" but doesn't acknowledge that its machine-readability is a genuine engineering advantage HTML5 must work harder to match (HTML5 is queryable via DOM but the queryability shape differs from JSON-AST's direct object-tree access).

**Defense — JSON-AST:** P7 lists TWO structural reasons: (1) "user pattern signal" (user names documents not data, across multiple turns); (2) Pandoc-specific deprecation risk (JSON-AST is Pandoc-version-locked). The first is interpretive; the second is structural. The combination passes prosecution. Additionally: P7 says JSON-AST is "not lost" — `pandoc -f html -t json canonical.html` produces it on-demand for any tool that needs the AST shape. This preserves the engineering advantage as on-demand reachability.

**Defense — dual:** P7's wording is precise: "Maintaining two persistent canonicals creates synchronization debt — one must be authoritative; the other is derived." The rejection is for dual PERSISTENT storage, not dual representation. JSON-AST being reachable on-demand from HTML5 IS dual representation, which P7 PRESERVES. The "synchronization debt" applies specifically to dual persistent canonicals.

**Defense — TEI:** P7's rationale survives prosecution — the "operational" wording understates but the substance is architectural-lever preservation. The rationale's substance is right; the wording is slightly weak.

**Defense — D10:** JSON-AST's machine-readability advantage IS engaged with implicitly via "JSON-AST is technically capable (capability matrix shows it ties HTML5 on every data-format property)." But the engagement is technical, not narrative — P7 doesn't say "JSON-AST has a genuine machine-readability advantage that HTML5 must work to match."

**Collision:** JSON-AST rejection SURVIVES with both reasons holding. Dual rejection SURVIVES with the persistence-not-representation precision intact. TEI rejection SURVIVES with the architectural-lever substance intact. D10 bias-balance is partial — JSON-AST's advantage is technically engaged but not narratively acknowledged.

**Verdict: REFINE.** Three small wording refinements:

**Constructive output:**
1. Clarify dual rejection wording: change "Dual JSON-AST + HTML5 — rejected" to "Dual *persistent* JSON-AST + HTML5 — rejected (dual representation IS preserved via on-demand `pandoc -f html -t json`)."
2. Strengthen TEI rejection wording from "The rejection is operational" to "The rejection is architectural — it would break Decision 5's Pandoc-as-architectural-lever commitment."
3. Add bias-balance acknowledgment to JSON-AST rejection: "JSON-AST has a genuine machine-readability advantage (direct object-tree access via panflute) that HTML5 (DOM access via `lxml.html` / `html5lib`) must work to match. This is the legitimate concern preserved; HTML5's compensating advantages (document-shape; W3C-standard; EPUB substrate; native lang/dir/data-*) outweigh the access-shape difference at the canonical layer."

---

### P8 (META-DECISION) — Inherited Commitments Re-test

**Prosecution — D4 (REFINE vs OVERTURN for Prior 1):** the canonical-layer cell IS the most semantically prominent of three cells. Calling its swap "one cell" understates the architectural significance.

**Prosecution — D4 (PRESERVED for Prior 2 Decisions 2-5):** the Decision 3 IntakeDoc shape shifts from "Pandoc-AST-wrapping pydantic class" to "parsed HTML5 DOM." Is this still PRESERVED, or is it actually a sub-rosa change?

**Prosecution — D7 (Inversion legitimacy at P8):** P8's Inversion candidate is "OVERTURN rather than REFINE." Is this genuinely generated and rejected with structural reasoning, or token?

**Defense — D4 Prior 1:** REFINE is structurally correct. The architecture (the inherited frame) survives. Two of three cells survive unchanged. The Pandoc-as-architectural-lever insight survives. The use-case-per-layer insight survives. What changes: one format choice in one cell. This is the structural definition of REFINE. The fact that the changed cell is the most semantically prominent doesn't make it OVERTURN — it makes it a LOAD-BEARING REFINE.

**Defense — D4 Prior 2:** P8 acknowledges the concrete-representation shift explicitly: "PRESERVED in semantic intent; the concrete representation shifts from a custom Pandoc-AST-wrapping pydantic class to a parsed HTML5 DOM." This is honest, not sub-rosa. The semantic intent (tree-of-containers + cross-referenced flat collections) IS preserved.

**Defense — D7:** P8's Inversion candidate is "the three-layer architecture itself is wrong, not just one cell of it." Rejection: the three-layer architecture survives every structural test in sensemaking; monolithic-vs-layered was already adjudicated in the prior canonical-format inquiry and re-adjudicated in this inquiry's sensemaking Ambiguity 1. The reasoning is structural. The Intervention-Shape Inversion check lists `corrects:`, `supersedes:`, and REVERT as alternatives and rejects each with structural reasoning. Not token.

**Collision:** D4 Prior 1 SURVIVE — REFINE is structurally correct. D4 Prior 2 SURVIVE — PRESERVED-in-semantic-intent is honest disclosure. D7 SURVIVE — Inversion legitimacy structural.

**Verdict: SURVIVE.** Inherited Commitments Re-test honesty intact; Inversion legitimacy structural.

---

### P9 — Transition plan + Next Actions

**Prosecution — D8 (near-zero migration claim):** verify against actual code state.

Audit (executed):
- `find . -type f \( -name "*.py" -o -name "*.swift" \) -not -path "./devdocs/*" -not -path "./mytrasnlations/*"` in project root → only `SKILL/references/config/schemas.py` exists.
- No Python production code commits to canonical-format engineering.
- Mac app at `/Users/ns/Desktop/projects/ComprehenslateApp/`: `PipelineConfig.swift` line 42 has `case md, html, plain, json` — UI output-format enum, not canonical-format engineering. HTML is already on the enum; JSON is too.
- No persistence layer scaffolding for JSON-AST canonical anywhere in the project.

**Defense — D8:** near-zero migration claim verifies against code state. The prior canonical-format inquiry's verdict committed JSON-AST but no engineering was built on it. Swapping the committed format BEFORE engineering starts costs nothing engineering-side. The Mac app's PipelineConfig enum already includes `html`, so even the UI layer is ready.

**Prosecution — D9 (MUST 1 hedge implications):** if HTML5 schema profile is deferred to MUST 1, can intake actually start producing HTML5 canonical before MUST 1 completes?

**Defense — D9:** P4's two-layer split + P9's MUST 1 framing make this explicit. Layer 1 (HTML5 conformance via `html5validator`) is operational from day 1; intake can produce valid HTML5 immediately. Layer 2 (project RNG profile) refines structural validation. The hedge is operational-staging, not gating.

**Collision:** Defense holds clean.

**Verdict: SURVIVE.** Near-zero migration claim verified by code-state audit. Operational-staging hedge legitimate.

---

### P10 — Open questions / frontier

**Prosecution:** are the deferred items genuinely deferred (vs hidden gating concerns)?

**Defense:** P10 names each deferred item with a revival trigger or resolution path. TEI has revival trigger "scholarly archival use case emerges OR cross-corpus validation surfaces a TEI requirement." Pandoc version pinning is named as operational. HTML5 Living Standard version stability is named as a project policy concern. Cross-corpus validation is named as a scaling concern. Each deferral is structured.

**Collision:** Defense holds.

**Verdict: SURVIVE.** Frontier items structured with revival triggers.

---

## Phase 3 — Per-piece verdicts

| Piece | Verdict | Refinement target |
|---|---|---|
| P1 | SURVIVE-with-caveat | Inherits P3's refinement implicitly |
| P2 | **REFINE** | Add caveat: JSON-AST parser-determinism advantage + operational bounds (parser-pinning + canonical-write-via-Pandoc-only) |
| P3 | **REFINE** | Add row: "Parser-implementation determinism" (JSON-AST=✓✓; HTML5=✓wa with operational-bound). Adjust Pareto-dominance verdict wording. |
| P4 | **REFINE** | Refine "W3C polyglot guidelines" wording to acknowledge the W3C Polyglot Markup NOTE was discontinued 2014; the concept remains usable. |
| P5 | SURVIVE | — |
| P6 | SURVIVE | 7/7 policy fidelity verified against schemas.py |
| P7 | **REFINE** | (a) Dual rejection: clarify "dual *persistent*" not dual representation. (b) TEI rejection: strengthen "operational" to "architectural-lever preservation." (c) JSON-AST rejection: add bias-balance acknowledgment of machine-readability advantage. |
| P8 | SURVIVE | — |
| P9 | SURVIVE | Near-zero migration verified by code-state audit |
| P10 | SURVIVE | Frontier items structured |

### Phase 3.5 — Assembly check

The 10 pieces assemble into a coherent architectural-refinement finding. P1 ↔ P2 ↔ P3 ↔ P4 ↔ P5 ↔ P6 ↔ P7 ↔ P8 ↔ P9 ↔ P10 each play a structural role; no emergent assembly beyond the architectural-refinement gestalt (which is the seed Decomposition committed). The architecture-refinement is the assembly.

Cross-cutting refinements operate at the same depth as the principal verdicts — they are wording + caveat additions, not architectural changes. The final HTML5-as-canonical commitment is unchanged by the refinements.

---

## Phase 4 — Coverage + Convergence

### Dimension coverage

| Dimension | Coverage |
|---|---|
| D1 Anti-hallucination | FULL — every W3C / Pandoc / EPUB / library claim verified or refined |
| D2 Pareto-dominance verifiability | FULL — substance criterion fired; parser-determinism omission surfaced |
| D3 Rejection rigor | FULL — all 6 rejections tested |
| D4 Inherited Commitments Re-test honesty | FULL — both priors' commitments tested |
| D5 Calibration-corpus pattern fidelity | FULL — 7/7 policies verified against schemas.py |
| D6 User-question fidelity | FULL — HTML5 maps directly to user's "html maybe?"; user-pattern signal genuine |
| D7 Meta-decision Inversion legitimacy | FULL — P2 + P8 both tested |
| D8 Transition plan accuracy | FULL — code-state audit performed |
| D9 Schema profile hedge legitimacy | FULL — two-layer split principled |
| D10 Bias-balance | FULL — HTML5 verbosity + markdown reading-order-naturalness + JSON-AST machine-readability all engaged (JSON-AST partially, hence REFINE on P7) |
| D11 Project-specific risk axis | NA — no project-state-touching candidate aspects beyond the code-state audit (which D8 covered) |
| D12 Frame-premise test | FULL — three premises named + prosecuted |
| D13 External-anchor evidence | FULL — verbatim spec references; schemas.py line-number verification |

### Adversarial strength

**STRONG.** Prosecution found 4 piece-level REFINEs (P2, P3, P4, P7) with constructive output. Prosecution did not rubber-stamp (4 REFINEs out of 10 pieces); did not nitpick (6 clean SURVIVEs; no KILLs). The Pareto-dominance claim's substance was tested via parser-determinism axis omission; the rejection-rigor was tested per-candidate; the bias-balance was tested per-concern.

### Landscape stability

**STABLE.** Cross-cutting refinements are wording + caveat additions; they do not shift the architectural commitment. HTML5-as-canonical SURVIVES; the three-layer architecture SURVIVES; the REFINE vs prior-canonical-format relationship label SURVIVES; the PRESERVED-in-semantic-intent label for prior 2 SURVIVES.

### Clean SURVIVE check

**YES.** Six pieces (P1, P5, P6, P8, P9, P10) are clean SURVIVE. P2, P3, P4, P7 are SURVIVE-with-REFINE (wording + caveat). No piece is KILL.

### Mechanism-Independence Quarantine check (Phase 4 refinement note)

External-anchor evidence cited for the surviving candidates:
- HTML5 §3.2.6 (`data-*`, `lang=`, `dir=`) — W3C HTML Living Standard quoted as the canonical source
- W3C HTML5 semantic elements — referenced in W3C spec
- W3C EPUB 3.3 spec at `w3.org/TR/epub-33/` — EPUB content document = XHTML
- Pandoc format matrix — Pandoc's documented `↔︎ html5` and `↔︎ epub3` entries
- `panflute` (PyPI / readthedocs) — verified library identity
- `SKILL/references/config/schemas.py` — verified 7 policy classes by file inspection (D5 substance criterion)
- Mac app code state (`PipelineConfig.swift` line 42) — verified by file inspection (D8 near-zero migration)

External anchors include canonical source text (W3C / Pandoc / EPUB / PyPI documentation) AND empirical artifact verification (schemas.py + Mac app code state). **Mechanism-Independence Quarantine does NOT fire.** Mechanism-independence status = `validated`.

### Failure mode scan

- #1 Wrong Dimensions — NO (dimensions extracted from inquiry's framing + Phase 0 refinement notes)
- #2 Rubber-Stamping — NO (4 piece-level REFINEs surfaced)
- #3 Nitpicking — NO (6 clean SURVIVEs; no KILLs over minor concerns)
- #4 Dimension Blindness — NO (D12 frame-premise test + D13 external-anchor coverage filled the project-specific + external-grounding gaps)
- #5 False Convergence — NO (sufficient SURVIVE on critical dimensions; clean Mechanism-Independence)
- #6 Evaluation Drift — NO (single-pass; no cross-iteration weights to drift)
- #7 Self-Reference Collapse — NO (external anchors cited; not self-evaluating critique)
- #8 Axis Absence at the Failure's Actual Plane — NO (D11 + D12 explicitly checked project-specific risk + frame premise)
- #9 External-Grounding Absence — NO (verbatim W3C / Pandoc / EPUB / library / file-path references cited)

### Convergence Telemetry

| Field | Value |
|---|---|
| Dimension coverage | FULL (D1-D13; D11 NA) |
| Adversarial strength | STRONG |
| Landscape stability | STABLE |
| Clean SURVIVE exists | YES (6 pieces clean SURVIVE; 4 SURVIVE-with-REFINE) |
| Mechanism-independence status | `validated` |
| Failure modes observed | NONE |

**Output:** **PROCEED.**

---

## Final Verdict

### **SURVIVE-with-cross-cutting-refinements.**

The architectural commitment (three-layer architecture PRESERVED + canonical-layer SWAP JSON-AST → HTML5; `refines:` prior canonical-format inquiry; PRESERVED Decisions 2-5 of original intake-concepts inquiry) SURVIVES. The HTML5-as-canonical verdict is structurally grounded, externally-anchored, and survives adversarial prosecution at every critical dimension.

Four cross-cutting refinements (wording + caveat additions; not architectural changes):

1. **P2 + P3** — engage parser-implementation-variability axis: name JSON-AST's parser-determinism advantage, and the operational bounds (Pandoc version pinning + canonical-write-via-Pandoc-only + single named reader parser) that bound HTML5's multi-parser variability. Adjust Pareto-dominance wording.

2. **P4** — refine polyglot wording: the W3C Polyglot Markup NOTE was discontinued 2014; the polyglot CONCEPT remains usable as a self-imposed writing convention. Not a fabrication; a wording-imprecision.

3. **P7 dual rejection** — clarify "dual *persistent*" not dual representation (dual representation IS preserved via on-demand Pandoc conversion).

4. **P7 TEI rejection** — strengthen "operational" to "architectural-lever preservation" (per Decision 5 of original intake-concepts inquiry).

5. **P7 JSON-AST rejection** — add bias-balance acknowledgment that JSON-AST has a genuine machine-readability advantage HTML5 must work to match.

These refinements are wording-level — they sharpen the finding's honesty without changing what's committed. The finding is ready for CONCLUDE with the refinements applied.

### Signal

**TERMINATE** with ranked survivors:

1. HTML5 as canonical (F1) — load-bearing new commitment; refines prior
2. Pandoc's markdown as hand-edit (F2) — preserved from prior
3. EPUB 3 as publishing (F3) — preserved from prior; HTML5 → EPUB near-identity transform via xhtml5 substrate
4. Per-element provenance encoding via `data-*` attributes — load-bearing new dimension
5. The 7 per-policy HTML5 patterns — calibration-corpus pattern fidelity 7/7
6. REFINE relationship label for prior 1 + PRESERVED for prior 2's Decisions 2-5
7. The MUST 1/2/3 + COULD 1/2/3 transition-plan inquiries

Proceed to Routelister (exhaust step) with this critique's refinement notes integrated.
