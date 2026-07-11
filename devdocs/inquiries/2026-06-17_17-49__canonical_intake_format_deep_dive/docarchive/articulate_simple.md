# articulate_simple — canonical intake format deep dive

## User Input

```text
The real wrinkles aren't about Arabic per se — they're about three things markdown doesn't carry natively:
  
  - Direction metadata. Plain markdown has no concept of right-to-left. The Unicode bidirectional algorithm (UAX #9) handles RTL display at
  render time based on character properties, so a paragraph that is "mostly Arabic" displays correctly in any compliant renderer. But for
  explicit span-level direction tagging (e.g., a Turkish sentence quoting an Arabic verse, both rendered in the right direction), Pandoc's
  markdown lets you write [هِ─لَّٰ   لِ دُمْحَلْٱ]{lang=ar dir=rtl} — that's Pandoc's bracketed_spans extension with a language + direction
  attribute. The lang attribute is what feeds the NonMainLangPartsPolicy detector in the finding.
  - Diacritic normalization. Arabic uses combining marks (fatha, damma, kasra, sukun, shadda — the harakat). Same visual word can be stored
  as either composed (NFC) or decomposed (NFD) forms — different byte sequences, same display. The finding's C4 normalize stage already
  commits to unicodedata.normalize('NFC', s), which makes diacritic representation deterministic. Without this, two intakes of the same
  Arabic text could produce byte-different IntakeDoc files.
  - Presentation forms vs abstract letters. Some sources (especially badly-OCR'd PDFs) store Arabic as Presentation Forms (the U+FE70 range)
  — pre-shaped glyphs corresponding to a letter's position in a word (initial / medial / final / isolated). The Unicode-correct way is the
  abstract letter (U+0628 BEH) plus shaping at render time. If a source has presentation forms, Pandoc preserves them as-is; renderers
  display them but a search for "ءاهب" won't match if the stored bytes are presentation forms. This is a real risk in the PDF intake path
  and is what concept A3 (OCR sub-pipeline) will need to address (Tesseract has flags for this).

  3. The hand-editing workflow with Arabic is editor-quality dependent. VS Code, Sublime Text 4, BBEdit, modern Vim, and JetBrains editors
  handle UTF-8 + bidi + RTL cursor navigation correctly — the user can edit mixed Turkish/Arabic paragraphs without weirdness. Older editors
  and barebones plain-text editors can make cursor movement and selection across script boundaries confusing. But the bytes are preserved
  correctly by any editor that saves as UTF-8 without re-encoding — which is the failure mode RTF has and markdown doesn't.

  4. The biggest practical Arabic risk in our pipeline is not markdown — it's PDF text extraction. Many religious-text PDFs (including some
  Risale-i Nur editions) store Arabic as glyph IDs that don't map back to Unicode codepoints — pdftotext and Pandoc's PDF reader pull
  garbage out. This is the source-quality problem, not Pandoc's. It's why the OCR sub-pipeline (A3) is its own design-next-inquiry:
  scan-only or text-layer-broken PDFs need Tesseract + Arabic language data (tesseract --lang ara) to re-derive the Unicode, which is more
  reliable than trying to repair the original PDF's text layer.


pdftext extraction is another issue.

we should focus on core representative format which will be used for translations.  i was thinking rtf is good for that. 

md has big limitations. we need sth different maybe? maybe we need to comeup with new format even? or epub or mobi formats are good?

lets dive deep on this
```

---

## Itemize

- **count:** 1
- **items:** `[I1]`

Reasoning: the substrate (paragraphs 1-4 of the input) is the prior assistant turn the user is responding TO — context, not work-items. The user's actual ask is one cohesive deliberation: *dive deep on the canonical intake format choice for translations, considering RTF, markdown's limitations, EPUB / MOBI, or even a custom format.* The multiple format candidates (RTF / EPUB / MOBI / custom / markdown) are alternatives WITHIN the deliberation, not separate work-items. Keep-together holds.

- **I1 — text:** *"Dive deep on the canonical intake format for translations — re-examine the prior Decision 1 (Pandoc's markdown) against the user's intuition that RTF is good + markdown has big limitations, considering EPUB / MOBI / a custom new format as alternatives."*

---

## Per-item bundle

### Item I1 — Dive deep on the canonical intake format

#### Stage 2 — Meta-questions + MQA

**MQ1 (verdict-axis) — what is the user asking for?**

Answer shape: **identified-ambiguities-list**.

- `[deep-comparison-of-format-candidates / re-adjudication-of-prior-Decision-1 / new-format-design-from-scratch / evaluation-criteria-articulation-then-selection]` — what kind of "deep dive."
- `[list-of-format-tradeoffs / decision-with-rationale / new-format-spec-if-needed / methodology-for-format-evaluation]` — what shape of deliverable.

**MQ2 (context-need axis) — what context does the response need?**

Answer shape: **identified-ambiguities-list** with verdict / kinds / stance sub-axes.

- **verdict (need-to-know facts):** `[exact-meaning-of-"core-representative-format" (translation-time canonical vs storage canonical vs both); the-calibration-corpus's-actual-structural-richness (Risale-i Nur has Turkish prose + Arabic verses + Mevlana couplets + marginalia + formulaic openings); specific-markdown-limitations-the-user-has-in-mind (beyond direction/diacritics/presentation-forms named in my prior turn); what-RTF-offers-that-markdown-doesn't-in-user's-intuition; EPUB/MOBI's-structural-properties-relevant-to-canonical-storage; whether-"new-format"-means-custom-from-scratch-or-extending-existing]`.
- **kinds (categories the comparison spans):** `[existing-established-formats (Pandoc's markdown / CommonMark / RTF / EPUB / MOBI / docx / HTML5 / LaTeX / TEI-XML / JATS / DocBook); hybrid-or-wrapper-formats (markdown + YAML frontmatter; markdown + side-files; pandoc-md-superset; HTML5 + ARIA; pandoc-AST-as-storage); custom-or-domain-specific (the .compldoc precursor; JSON-schema-driven custom format); serialization-strategies (JSON / XML / msgpack as alternative storage rather than format-as-document)]`.
- **stance (curation posture):** `[skeptical-of-prior-Decision-1 (the user is pushing back; defend or overturn) vs revisit-with-open-mind; engineering-pragmatic (cost-of-engineering / ecosystem-tooling) vs theoretical-completeness (richness-of-source-representation); cost-of-switch-now vs cost-of-staying-wrong-later]`.

**MQ3 (intent-axis, WHAT) — what is the user trying to accomplish?**

Answer shape: **identified-ambiguities-list**. WHAT-axis = action-endpoint shape.

- `[re-decide-the-canonical-format (replace the prior Decision 1 with a new commit) vs validate-prior-Decision-1 (the prior choice survives stronger prosecution) vs find-better-alternative-among-existing (the right format exists; it's not markdown) vs design-new-format-from-requirements (no existing format fits; build one)]`.
- `[understand-the-format-landscape-then-decide vs commit-now-to-a-specific-alternative]`.

**MQ4 (boundary-axis) — what is the user explicitly excluding?**

Answer shape: **identified-ambiguities-list**.

- `[PDF-text-extraction-is-out-of-scope]` — user explicitly said "pdftext extraction is another issue"; this inquiry should not re-litigate OCR / text-extraction.
- `[implied-MQ4-from-prior-inquiry-stands]` — the Mac app's UI surface remains out of frame; the translation-stage algorithm choices remain out of frame. The user's reset-of-focus to canonical format does not re-open those exclusions.

**MQA — Meta-question alignment**

Examine overlaps across MQ1 / MQ2 / MQ3 / MQ4.

- MQ1's "deep-comparison-of-candidates / re-adjudication-of-prior / new-format-design / evaluation-criteria-articulation" and MQ3's "re-decide / validate / find-better / design-new" — these span the **same joint axis**: *decision-mode*. The axis ranges over `[validate-prior / re-decide-with-alternative / find-better-existing / design-from-scratch]`. The two MQs identify the same ambiguity at different surfaces (verdict-axis surface vs intent-axis surface).
- MQ2's stance sub-axis "skeptical-of-prior vs revisit-with-open-mind" also touches the same decision-mode axis (skeptical leans toward re-decide; open-mind leans toward validate-or-re-decide).

Emission: **reconcile** — joint axis is **decision-mode** with values `[validate-prior (Decision 1 survives stronger prosecution) / re-decide-with-existing-alternative (swap to RTF, EPUB, MOBI, or other existing format) / design-new-format-from-requirements (custom .compldoc precursor)]`. The decision-mode is the inquiry's load-bearing ambiguity; downstream pipeline operates over the three values, not over a pre-chosen one.

#### Stage 3 — Deconstruct + MultiDepth

**Deconstruct — tuple (deliverable, kinds, bounds):**

- **deliverable:** an analysis + decision/recommendation about the canonical intake format. Shape depends on decision-mode value — a validation argument, a substitution argument with new commitment, or a format-spec sketch.
- **kinds:** comparative analysis of format candidates against requirements + adjudicated decision + (possibly) custom-format requirements list / spec sketch.
- **bounds:** the canonical intake format for comprehenslate's translation pipeline. Excludes PDF-text-extraction (out of scope per the user), app UI surface (inherited MQ4), translation-stage internals (inherited MQ4).

**Late-split check:** does I1's internal structure suggest multiple items? No — the format-candidates within I1 are alternatives, not separate work-items. Single deliverable.

**MultiDepth — literal-statement:**

*"We should focus on the core representative format that will be used for translations. RTF seems good. Markdown has big limitations. We may need something different — maybe a new format, or EPUB or MOBI. Let's dive deep on this."* (Near-verbatim restatement; no expansion, no reframing.)

**MultiDepth — identified-purpose-motivation-ambiguities (WHY-axis):**

Answer shape: **identified-ambiguities-list**. WHY-axis = motivation-chain shape.

- `[prior-Decision-1-doesn't-feel-right (the user has lingering uncertainty about the markdown choice; pushback is a signal worth honoring)]`.
- `[richer-source-fidelity (the user senses markdown loses something important; wants a format that preserves more of the source's structure or richness)]`.
- `[avoid-rework-later (committing to the right format now prevents a costly mid-engineering switch when limitations surface)]`.
- `[match-the-calibration-corpus's-richness (Risale-i Nur's typographic + structural complexity may exceed what markdown handles cleanly)]`.
- `[validate-against-user-intuition (the user's intuition says RTF; the prior inquiry rejected RTF; if we reject again, the rejection should withstand stronger prosecution)]`.
- `[preserve-the-translated-product's-publishability (downstream of intake, the translation's output format matters for distribution — EPUB / MOBI are reader-facing formats; the user may be thinking past intake to publishing)]`.

#### Stage 4 — Rephrase (considered articulations)

Composition sources:
- Deconstruct deliverable-shape: **analysis + decision/recommendation about canonical intake format**.
- Identified ambiguities (post-MQA reconciliation): **decision-mode** axis with values `[validate-prior / re-decide-with-existing / design-new]`; **richness-vs-engineering-cost** trade-off; **storage-canonical-vs-translation-canonical-vs-publishing-canonical** scope.
- MQ4 NOT-list: **PDF-extraction-out**, **app-UI-out**, **translation-internals-out**.
- Substrate: warm — the prior inquiry's Decision 1 (Pandoc's markdown); the comparisons already made (CommonMark / RTF / Pandoc-md-superset / custom-.compldoc); calibration corpus character (Risale-i Nur multi-volume w/ Arabic verses + Mevlana couplets + hashiye + formulaic openings).

Generated variants (5; floor+ side of 2-6 range; each spans a distinct dimension of the decision-mode + scope axes):

1. **Re-adjudicate Decision 1 with a fuller candidate set and richer criteria.** *"Compare Pandoc's markdown (the prior choice), RTF, EPUB, MOBI, plus formats the prior inquiry didn't surface (TEI XML, DocBook, JATS, HTML5 + ARIA, pandoc-AST-as-storage), against criteria that reflect the calibration corpus's richness (Arabic span tagging fidelity; diacritic stability under round-trip; marginalia representation cost; multi-volume containment; hand-edit-after-parse stability; downstream-publishing reusability); produce a verdict that PRESERVES or OVERTURNS the prior Decision 1."*

2. **Validate prior Decision 1 by constructing the strongest case for RTF and the strongest case against markdown.** *"Take the user's intuition seriously — RTF is good, markdown has big limitations — and steel-man both. Build the strongest defense for RTF (what does RTF actually preserve that markdown loses); build the strongest case against markdown (what specific corpus features does it fail to represent); test Decision 1's defense against these maximally strong prosecutions; conclude PRESERVE (with the steel-manned objections honored as caveats) or OVERTURN (with rationale)."*

3. **Evaluate EPUB and MOBI as canonical book-storage formats specifically.** *"Since the calibration corpus is a multi-volume book, evaluate EPUB and MOBI as packaged-book formats for canonical storage — they carry chapter hierarchy + apparatus + metadata + multi-file containment natively. Compare them against markdown + IntakeDoc and against the prior architecture; surface whether the canonical format should match the source's natural book-shape rather than be a per-volume text representation."*

4. **Design a custom format (`.compldoc` precursor or similar) from intake requirements.** *"Treat existing formats as inherently insufficient; derive a format spec from comprehenslate's actual requirements — the 7 policy targets, the IntakeDoc tree+cross-ref shape, multilingual + RTL + diacritic preservation, the round-trippable on-disk hand-edit workflow, publishing-output considerations. Produce a format spec (likely Markdown-derived with explicit schema, or YAML+markdown hybrid, or JSON-AST-based) that solves what no existing format solves cleanly."*

5. **Explore the format landscape methodologically without committing.** *"Produce a feature-matrix of all serious candidate formats (Pandoc's markdown, CommonMark, GFM, RTF, EPUB, MOBI, docx, HTML5 + ARIA, LaTeX, TEI XML, JATS, DocBook, Pandoc-AST-as-storage, JSON-AST-custom) against the inquiry's requirement set; surface the trade-offs; leave the decision to the user; the deliverable is the matrix + methodology, not a verdict."*

---

## Statement-level fields

- **Itemize count:** 1
- **Per-item identifiers:** `[I1]`
- **Self-assessment verdict:** **HIGH-PROCEED**

LAYER 1 self-check (single LIGHT pass):

| # | Mode | Fire? |
|---|---|---|
| 1 | Premature Itemize split | not-fire |
| 2 | Late-detected multi-item case | not-fire (single deliberation; format candidates are alternatives within it) |
| 3 | MQ extension violates bounded-extensibility | not-fire (only 4 axes) |
| 4 | Per-operation firing missed | not-fire (Itemize / MQ1-4 / MQA / Deconstruct / MultiDepth / Rephrase all fired) |
| 5 | MQ2 answer missing preparation content | not-fire (verdict / kinds / stance all present and substantive) |
| 6 | MQ2 missing kinds-axis or stance-axis | not-fire |
| 7 | 2-shape violation | not-fire (every MQ + MultiDepth emits identified-ambiguities; no commitments at 2-shape positions) |
| 8 | AMBIGUITY-NATURE conflation | not-fire — MQ3 = WHAT-axis (action-endpoint: re-decide / validate / find-better / design-new); MultiDepth = WHY-axis (motivation-chain: pushback-signal / fidelity-want / avoid-rework / corpus-match / validate-intuition / publishing-considerations) |
| 9 | Considered-articulations drift | not-fire (all 5 variants respect deliverable-shape + ambiguity-dimensions + NOT-list + substrate) |

Zero LAYER 1 fires. Perceived friction: **low-moderate** — the request is structurally cohesive (one deliverable), but the format-candidate space is wider than the prior inquiry's (RTF / EPUB / MOBI / custom alongside the prior CommonMark / Pandoc-md / .compldoc), and the decision-mode axis spans validate / re-decide / design-new which need to be downstream-distinguishable. MQA's reconcile on decision-mode is the load-bearing structural commitment that keeps the wider candidate-space tractable.

Verdict: **HIGH-PROCEED**.
