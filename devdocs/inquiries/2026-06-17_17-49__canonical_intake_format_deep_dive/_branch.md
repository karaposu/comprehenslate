# Branch: canonical intake format deep dive

## Source Input

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

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-17_17-49__canonical_intake_format_deep_dive/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** `[I1]`
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**Item I1 — Dive deep on the canonical intake format for translations.**

Literal statement (from MultiDepth, near-verbatim):
> *"We should focus on the core representative format that will be used for translations. RTF seems good. Markdown has big limitations. We may need something different — maybe a new format, or EPUB or MOBI. Let's dive deep on this."*

The Question carries **two open verdict-axis ambiguities (MQ1)** about what kind of "deep dive" is being asked for:

1. *Kind of deliberation* — `[deep-comparison-of-format-candidates / re-adjudication-of-prior-Decision-1 / new-format-design-from-scratch / evaluation-criteria-articulation-then-selection]`.
2. *Shape of deliverable* — `[list-of-format-tradeoffs / decision-with-rationale / new-format-spec-if-needed / methodology-for-format-evaluation]`.

And **two open intent-axis ambiguities (MQ3)** about action-endpoint:

1. *Decision-mode* — `[re-decide-the-canonical-format (replace the prior Decision 1) vs validate-prior-Decision-1 (it survives stronger prosecution) vs find-better-alternative-among-existing (an existing format other than markdown) vs design-new-format-from-requirements (no existing format fits; build one)]`.
2. *Commitment-timing* — `[understand-the-landscape-then-decide vs commit-now-to-a-specific-alternative]`.

The **MQA reconciliation** identifies that MQ1's "deep comparison / re-adjudication / new-format-design / evaluation-criteria" and MQ3's "re-decide / validate / find-better / design-new" both span a single joint axis: **decision-mode** with values `[validate-prior / re-decide-with-existing-alternative / design-new-format]`. This is the inquiry's load-bearing ambiguity; the downstream pipeline operates over the three values, not over a pre-chosen one.

## Goal

For Item I1:

**Deliverable shape (from Deconstruct):**

- **deliverable:** an analysis + decision/recommendation about the canonical intake format. Shape depends on which decision-mode value the inquiry commits to — a validation argument (prior Decision 1 stands), a substitution argument with a new commitment (e.g., RTF or EPUB or MOBI replaces markdown), or a format-spec sketch (a new custom format derived from requirements).
- **kinds:** comparative analysis of format candidates against intake requirements + adjudicated decision + (possibly) custom-format requirements list / spec sketch.
- **bounds:** the canonical intake format for comprehenslate's translation pipeline. Excludes PDF-text-extraction (the user explicitly said "pdftext extraction is another issue"), app UI surface (inherited from prior MQ4), translation-stage internals (inherited from prior MQ4).

**Motivations a good answer might serve (WHY-axis, from MultiDepth — preserved as ambiguities, not collapsed):**

- `[prior-Decision-1-doesn't-feel-right]` — the user has lingering uncertainty about the markdown choice; the pushback is a signal worth honoring rather than dismissing.
- `[richer-source-fidelity]` — the user senses markdown loses something important; wants a format that preserves more of the source's structure or richness.
- `[avoid-rework-later]` — committing to the right format now prevents a costly mid-engineering switch when limitations surface.
- `[match-the-calibration-corpus's-richness]` — Risale-i Nur's typographic + structural complexity may exceed what markdown handles cleanly.
- `[validate-against-user-intuition]` — the user's intuition says RTF; the prior inquiry rejected RTF; if the rejection holds, it should withstand stronger prosecution.
- `[preserve-the-translated-product's-publishability]` — downstream of intake, the translation's output format matters for distribution; EPUB / MOBI are reader-facing formats and the user may be thinking past intake to publishing.

**Context the downstream consumers need (MQ2 — preserved as ambiguities):**

- *verdict (need-to-know facts):* `[exact-meaning-of-"core-representative-format" (translation-time canonical vs storage canonical vs both); the-calibration-corpus's-actual-structural-richness (Risale-i Nur has Turkish prose + Arabic verses + Mevlana couplets + marginalia + formulaic openings); specific-markdown-limitations-the-user-has-in-mind (beyond what was named in the prior assistant turn); what-RTF-offers-that-markdown-doesn't-in-user's-intuition; EPUB/MOBI's-structural-properties-relevant-to-canonical-storage; whether-"new-format"-means-custom-from-scratch-or-extending-existing]`.
- *kinds (categories the comparison spans):* `[existing-established-formats (Pandoc's markdown / CommonMark / RTF / EPUB / MOBI / docx / HTML5 / LaTeX / TEI-XML / JATS / DocBook); hybrid-or-wrapper-formats (markdown + YAML frontmatter; markdown + side-files; pandoc-md-superset; HTML5 + ARIA; pandoc-AST-as-storage); custom-or-domain-specific (the .compldoc precursor; JSON-schema-driven custom format); serialization-strategies (JSON / XML / msgpack as alternative storage rather than format-as-document)]`.
- *stance (curation posture):* `[skeptical-of-prior-Decision-1 vs revisit-with-open-mind; engineering-pragmatic vs theoretical-completeness; cost-of-switch-now vs cost-of-staying-wrong-later]`.

**Negative spec — what would explicitly fail (MQ4 exclusions):**

- `[PDF-text-extraction-is-out-of-scope]` — the user explicitly bounded this out; the inquiry should not re-litigate OCR or text-extraction issues.
- `[app-UI-surface-still-out-of-frame]` — inherited from the prior inquiry's MQ4 exclusion ("appification-out"); the canonical-format decision does not re-open the app surface.
- `[translation-stage-internals-still-out-of-frame]` — inherited from the prior MQ4.

## Considered Articulations

**Item I1 — Dive deep on the canonical intake format:**

1. **Re-adjudicate Decision 1 with a fuller candidate set and richer criteria.** *"Compare Pandoc's markdown (the prior choice), RTF, EPUB, MOBI, plus formats the prior inquiry didn't surface (TEI XML, DocBook, JATS, HTML5 + ARIA, pandoc-AST-as-storage), against criteria that reflect the calibration corpus's richness (Arabic span tagging fidelity; diacritic stability under round-trip; marginalia representation cost; multi-volume containment; hand-edit-after-parse stability; downstream-publishing reusability); produce a verdict that PRESERVES or OVERTURNS the prior Decision 1."*

2. **Validate prior Decision 1 by constructing the strongest case for RTF and the strongest case against markdown.** *"Take the user's intuition seriously — RTF is good, markdown has big limitations — and steel-man both. Build the strongest defense for RTF (what does RTF actually preserve that markdown loses); build the strongest case against markdown (what specific corpus features does it fail to represent); test Decision 1's defense against these maximally strong prosecutions; conclude PRESERVE (with the steel-manned objections honored as caveats) or OVERTURN (with rationale)."*

3. **Evaluate EPUB and MOBI as canonical book-storage formats specifically.** *"Since the calibration corpus is a multi-volume book, evaluate EPUB and MOBI as packaged-book formats for canonical storage — they carry chapter hierarchy + apparatus + metadata + multi-file containment natively. Compare them against markdown + IntakeDoc and against the prior architecture; surface whether the canonical format should match the source's natural book-shape rather than be a per-volume text representation."*

4. **Design a custom format (`.compldoc` precursor or similar) from intake requirements.** *"Treat existing formats as inherently insufficient; derive a format spec from comprehenslate's actual requirements — the 7 policy targets, the IntakeDoc tree+cross-ref shape, multilingual + RTL + diacritic preservation, the round-trippable on-disk hand-edit workflow, publishing-output considerations. Produce a format spec (likely Markdown-derived with explicit schema, or YAML+markdown hybrid, or JSON-AST-based) that solves what no existing format solves cleanly."*

5. **Explore the format landscape methodologically without committing.** *"Produce a feature-matrix of all serious candidate formats (Pandoc's markdown, CommonMark, GFM, RTF, EPUB, MOBI, docx, HTML5 + ARIA, LaTeX, TEI XML, JATS, DocBook, Pandoc-AST-as-storage, JSON-AST-custom) against the inquiry's requirement set; surface the trade-offs; leave the decision to the user; the deliverable is the matrix + methodology, not a verdict."*

## Scope Check

**Question covers goal.** The Question asks for a deep dive on canonical intake format; the Goal specifies the deliverable shape (analysis + decision/recommendation), the motivations a good answer serves (pushback-signal / fidelity / avoid-rework / corpus-match / validate-intuition / publishing-considerations), the context categories (existing formats / hybrid wrappers / custom domain-specific / serialization strategies), and the exclusions (PDF-extraction, app-UI, translation-internals). All Goal facets are inflected aspects of the same deep-dive question.

**Specific-vs-pattern check:** the user named SPECIFIC candidate formats (RTF, EPUB, MOBI, "new format") in addition to the prior commitment (Pandoc's markdown). The inquiry should address **both the specific candidates the user named AND the broader landscape** (per articulate_simple's MQ2 kinds-axis which surfaced TEI XML, DocBook, JATS, HTML5 + ARIA, pandoc-AST-as-storage as adjacent candidates not previously considered). Treating only the user's named candidates would risk false-narrow framing; the user's intent is "dive deep" which warrants broader landscape coverage.

## Synthesis Trigger

This inquiry's primary substrate is the prior intake-concepts finding's Decision 1, which the user is pushing back on. While only ONE prior inquiry output is being directly re-tested (so the strict "≥2 priors synthesized" trigger does not fire by letter), the inquiry IS structurally a re-adjudication of a load-bearing prior commitment. The downstream finding (when CONCLUDE produces it) should respect the prior context:

- `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md` — the prior Decision 1 (canonical intake format = Pandoc's markdown / Pandoc-md-superset) is the load-bearing commitment being re-tested. The downstream finding's relationship to this prior should be one of `refines:` (if Decision 1 survives with caveats) / `supersedes:` (if Decision 1 is overturned and replaced) / `corrects:` (if Decision 1's rationale is found load-bearingly wrong).

The Inherited Commitments Re-test section is therefore optional-but-recommended for the downstream finding. The Sensemaking + Critique disciplines should plan to actually re-test the prior Decision 1's rationale (not just record the inheritance).
