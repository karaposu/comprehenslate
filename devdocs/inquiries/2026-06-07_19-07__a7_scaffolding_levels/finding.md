---
status: active
model: claude-opus-4-7[1m]
effort: max
---
# Finding: A7 — Scaffolding

## Question

**From `_branch.md`.** A7 — Scaffolding is the third and final axis in the Strategy family of Comprehenslate's 8-axis translation-configuration framework, established by the root finding `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md`. A7 controls how much explanatory material accompanies the translation at the text surface — footnotes, parenthetical glosses, transliterations, brief in-line explanations. It carries two distinguishing roles beyond simple level-setting: it is the **scaffolding budget** that determines which A1 cultural-reference-recognition actions and A3 source-culture handling actions can fire (some actions like INLINE-GLOSS and FOOTNOTE consume budget; others like KEEP-AS-IS and EXPLICATE-FUNCTION don't), and it is the **render-control surface** for the always-on multi-meaning preservation policy when polysemy fires (the user controls HOW preserved senses appear; the policy controls WHETHER).

Decide: cardinality, level names, per-level scaffolding-budget specification, A1/A3 action-permission table, multi-meaning render rules, runtime conflict resolution when budget conflicts with required actions, A4 matrix cross-validation, A5↔A7 and A6↔A7 and A7↔A8 boundaries, NEW translator-strategy 4-component template adaptation, Said Nursi corpus mapping per level, edition-tradition exemplars per level, receptive-only applicability, default-when-A7-silent, Strategy-family-closure marker.

**Goal.** Each level operationalizable as an AI prompt instruction — the per-level prose becomes part of the translator-AI's context, telling the AI its scaffolding budget per page/chapter/passage, which A1/A3 actions can fire, and how multi-meaning preservation renders. The per-level scaffolding-budget spec, the A1/A3 action-permission table, and the multi-meaning render rules are the operational substance. Strategy family closes at 3/3; 7/8 axes complete after this inquiry; only A8 Analysis Depth remains.

## Finding Summary

- **5 ordinal levels** `off | minimal | standard | rich | scholarly`. Plain-ordinal (no categorical / asymmetric / composite structure). Confirmed against edition-tradition exemplars (utility translation → Penguin Classics → NIV+study → Norton Critical → SBL Greek NT or Robert Alter scholarly editions); 4 levels collapse Norton Critical with SBL apparatus-editions (loses operational distinction), 6+ over-stratifies. The A4 matrix uses 5 distinct values (minimal, moderate, rich, MAX rich, performance-zero-implicit), corroborating 5-level cardinality.

- **Per-level scaffolding budget = two complementary components.** (1) Qualitative orientation (the verbal threshold per level — "extensive footnotes per page" for `rich`; "sparse only for hardest references" for `minimal`). (2) Per-page operational guidance (concrete unit the AI can monitor — `off`=0/page, `minimal`=0-1/page, `standard`=1-3/page, `rich`=3-6/page, `scholarly`=6+/page including endnote/appendix references). Per-page numbers are NOT hard caps but orientation thresholds — some passages legitimately need more, and the AI uses them as sanity-check budget rather than enforcement gates.

- **A1/A3 action permission table per level** — the central operational substance. At each level, the table specifies which budget-consuming A1 actions (INLINE-GLOSS, FOOTNOTE) and budget-consuming A3 actions (TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT, BRIDGE-CULTURAL-DISTANCE) can fire and at what density (blocked / sparingly / moderate / routine / extensive / full-apparatus). Budget-FREE actions (KEEP-AS-IS, EXPLICATE-FUNCTION, DOMESTICATE-disfavored-but-available, ASSUME-SHARED, TARGET-LANGUAGE-EQUIVALENT, PRESERVE-CULTURAL-SPECIFICITY, etc.) are available at every level, subject to A5 policy bias. `off` STRICTLY blocks all budget-consuming actions — making A7=off operationally distinct from A7=minimal — and the AI falls back to budget-FREE alternatives.

- **5 multi-meaning render rules per level + a 6th case for A7=off**. When the always-on multi-meaning preservation policy fires (a polysemous source word permits multiple senses simultaneously per the local construction), A7's level controls how the preserved senses render: `off` → EXPLICATE-FUNCTION fallback (preserve polysemy via paraphrase combining senses into the body; no scaffolding); `minimal` → PRIMARY + MINIMAL FOOTNOTE noting other senses; `standard` → INLINE PARENTHETICAL PAIRED (`din [judgment / religion]`); `rich` → INLINE PAIRED WITHOUT BRACKETS or FULL FOOTNOTE PAIRED; `scholarly` → APPARATUS-EDITION RENDER (body + footnote + scholarly apparatus citing exegetical/linguistic literature + glossary entry). The user controls HOW (per A7 level); policy controls WHETHER (preservation is invariant).

- **Runtime conflict resolution.** When A7 is too low to accommodate the A1/A3 actions a low-A1 reader-level + foreignization-preferring A5 would otherwise want, the AI applies a deterministic three-step rule: (1) strict budget enforcement (A7 BLOCKS budget-consuming actions; the AI does not exceed); (2) fallback to budget-FREE actions (EXPLICATE-FUNCTION, KEEP-AS-IS, ASSUME-SHARED-CULTURAL-KNOWLEDGE, PRESERVE-CULTURAL-SPECIFICITY); (3) flag the trade-off in the harmony report at A6 levels 3+ (records that source-cultural specificity was preserved via paraphrase/non-scaffolding rather than via gloss). UX-layer surface-at-config-time ("A7=off + foreignized A5 may produce uncomfortable text") is valuable but deferred to a future UX inquiry — it is additive to the A7 spec, not part of it.

- **Default `rich` via A4 chain.** When A7 is silent, the system chains A7 → A4 → casual default → A4 matrix's "casual A7 = rich (help unfamiliar)" → A7 = `rich`. This is intentionally HIGHER than A6's default `light` — it reflects the project's accessibility commitment for outsider/uninitiated readers (casual readers of Said Nursi or similar source-cultural texts benefit from rich scaffolding, not minimal). The default is chain-derived, not arbitrary.

- **A4 finding refinement note (parallel to A6's).** A4's matrix uses informal verbiage ("moderate," "MAX rich"); A7 uses precise labels `off | minimal | standard | rich | scholarly`. At next A4 maintenance pass, propagate the naming alignment: A4 "moderate" → A7 `standard`; A4 "MAX rich" → A7 `scholarly`. This is the same kind of carry-forward refinement that A6's finding logged, and it should ride the same A4 maintenance pass.

- **NEW A7-adapted 4-component template.** Adapted from the A5/A6 translator-strategy template: (1) Scaffolding stance description (what the AI does at this level — how much explanatory material on the reading page); (2) Per-level budget specification (qualitative + per-page operational guidance); (3) A1/A3 action permission table reference + multi-meaning render rule for this level (the operational substance); (4) Cross-axis interaction note (A4 matrix match + A5/A6 orthogonality reminders + A8 forthcoming-validation marker).

- **Receptive-only NOT APPLICABLE.** A7 is translator-strategy and user-configuration — a budget on what the translation surfaces — not a property of the reader (parallel to A4, A5, A6). Explicit non-inheritance from the Reader-family pattern.

- **Cross-axis orthogonality preserved.**
  - **A5↔A7** — A5 (Source Fidelity) sets the strategic stance modulating which A1/A3 actions to SELECT; A7 sets the budget constraining which of those actions the budget can AFFORD. Distinct mechanisms. A5=foreignized + A7=off forces the AI to use scaffolding-free foreignization-preserving alternatives (EXPLICATE-FUNCTION over INLINE-GLOSS).
  - **A6↔A7** — A6 (Form Preservation) determines which harmony_layer tiers are preserved and produces the harmony REPORT as a separate apparatus channel at Levels 3+; A7 controls text-surface scaffolding (footnotes/glosses) on the reading page. Both A6's harmony report and A7's footnotes live in apparatus, but in DIFFERENT apparatus channels — A6's is meta-analytic (translator's commentary), A7's is reader-facing scaffolding. Orthogonal.
  - **A7↔A8** (forward-looking) — A7 = text-surface scaffolding on the reading page; A8 = separate-sections analysis depth (separate sections after the translation, not in-line). Distinct surfaces per the root architecture; to be re-validated when the A8 inquiry runs.

- **Strategy family CLOSES at 3/3** with A7. After this inquiry: Reader 3/3 + Purpose 1/1 + Strategy 3/3 = 7/8 axes complete; only A8 Analysis Depth (Depth family, 1/1) remains.

## Finding

**Context for the cold reader.** Comprehenslate is an AI-assisted translation system. The user's primary translation project is the Said Nursi corpus (Risale-i Nur, a 20th-century Turkish Islamic theological work). The 8-axis configuration framework lets the user state, before each translation, what the audience knows (Reader family: A1 Cultural Reference Recognition, A2 Domain Expertise, A3 Source Culture), what the translation is for (Purpose family: A4 Purpose), how the translator should behave strategically (Strategy family: A5 Source Fidelity, A6 Form Preservation, A7 Scaffolding), and how much separate-sections analysis to attach (Depth family: A8 Analysis Depth). Six of those eight axes were specified in prior inquiries before this one ran. The two distinguishing complications for A7 — that it is a *budget* on actions belonging to other axes, and a *render-control surface* for an always-on policy — make A7 substantively different from a simple level-setting axis, and this is why the finding goes deep on operational substance rather than just naming five levels.

### 1. Framework

A7 is a plain-ordinal axis with 5 ordinal levels:

```
A7: off | minimal | standard | rich | scholarly
```

The level names match the user's intuitions in everyday language AND map cleanly to recognizable edition-tradition exemplars: a utility translation with no apparatus (`off`); a Penguin Classics paperback with sparse footnotes only for the hardest references (`minimal`); a standard scholarly edition with moderate footnotes and inline glosses (`standard`); a Norton-Critical-style edition with extensive footnotes per page (`rich`); a SBL Greek NT or Robert Alter scholarly edition with full apparatus, endnotes, introduction, glossary, and critical apparatus (`scholarly`). Going to 4 levels collapses operationally-different editions (Norton Critical is not SBL Greek NT); going to 6+ over-stratifies in a way the A4 matrix never asks for.

A7 subsumes the user's original "feature activation" sketch MINUS the harmony component, which became A6: footnote toggle + transliteration toggle + parenthetical glosses + brief in-line explanations. The root finding's commitment that "this isn't a heterogeneous bundle; it's one ordinal dial" stands. Higher levels mean more explanatory aid.

**Receptive-only NOT APPLICABLE.** A7 is a translator-strategy axis (user-configuration; scaffolding budget). It is not a reader-property like A1/A2/A3. It does not inherit a receptive-only mode from the Reader family. This parallels the same non-applicability declared in A4 (Purpose), A5 (Source Fidelity), and A6 (Form Preservation).

**Default-when-A7-silent = `rich` via A4 chain.** When the user does not specify A7, the system chains through A4: silent → A4 default = `casual` → A4 matrix's "casual A7 = rich (help unfamiliar)" → A7 = `rich`. The casual default reflects the project's accessibility commitment for outsider/uninitiated readers, and it is intentionally HIGHER than A6's default `light` — even casual readers of source-cultural texts benefit from rich scaffolding, not minimal. The default is chain-derived from prior commitments, not chosen in isolation.

**Strategy-family-closure marker.** A7 is the third and final Strategy axis. With this finding, the family closes at 3/3. The framework's overall progress: 7/8 axes complete. Only A8 Analysis Depth (Depth family, 1/1) remains.

### 2. Per-level definitions

Each level uses the NEW A7-adapted 4-component template:

1. **Scaffolding stance** — what the AI does at this level (how much explanatory material on the reading page).
2. **Budget specification** — qualitative threshold + per-page operational guidance.
3. **A1/A3 action permission + multi-meaning render rule** — the operational substance the AI consults at every reference and at every polysemous passage.
4. **Cross-axis interaction note** — which A4 purposes default here + A5/A6 orthogonality reminders + A8 forthcoming-validation marker.

#### Level 1 — `off`

1. **Stance.** No text-surface scaffolding. The translation reads as plain target-language prose. No footnotes, no inline glosses, no transliterations with parenthetical paraphrase, no flagged cultural-context markers.
2. **Budget.** Zero footnotes per page; zero inline glosses; zero apparatus. Qualitative: clean text only.
3. **Action permission + render rule.** STRICTLY BLOCKED: INLINE-GLOSS, FOOTNOTE, TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT, BRIDGE-CULTURAL-DISTANCE. Available: all budget-FREE actions (KEEP-AS-IS, EXPLICATE-FUNCTION, DOMESTICATE-disfavored-but-available, TRANSLITERATE-FULLY, ASSUME-SHARED-CULTURAL-KNOWLEDGE, PRESERVE-CULTURAL-SPECIFICITY, TARGET-LANGUAGE-EQUIVALENT, KEEP-HONORIFICS-SOURCE, ANGLICIZE-HONORIFICS, DOMESTICATE-CULTURAL-FRAME). Multi-meaning render rule: when the polysemy policy fires, AI uses EXPLICATE-FUNCTION (paraphrase combining senses into the body) — preserves WHETHER per policy, uses budget-FREE render. Harmony report flags at A6 Levels 3+ if source-cultural-specificity is preserved via paraphrase rather than gloss.
4. **Cross-axis note.** A4 default for `performance` (oral recitation, clean text). A5/A6 orthogonal. A7=off + foreignization-preferring A5 forces budget-FREE foreignization-preserving alternatives (EXPLICATE-FUNCTION over INLINE-GLOSS) and may produce uncomfortable text; harmony report flags. A8 future inquiry needed for boundary re-validation.
5. **Said Nursi exemplar.** An oral-recitation passage of Risale-i Nur for live audience delivery — clean text only, no apparatus.
6. **Edition-tradition exemplar.** A utility translation (e.g., a road sign, a quick UN-style summary translation, oral interpretation) with no apparatus.

#### Level 2 — `minimal`

1. **Stance.** Sparse text-surface scaffolding for the HARDEST references only. The translation reads as a pop-translation general-audience paperback with rare footnotes and first-use-only transliteration glosses.
2. **Budget.** 0-1 footnotes per page (orientation, not cap); sparse inline glosses; first-use transliteration only ("Bediuzzaman (wonder of the age)" once, then "Bediuzzaman").
3. **Action permission + render rule.** ALLOWED SPARINGLY (1-2 per page for hardest): INLINE-GLOSS. RARE: FOOTNOTE. FIRST-USE-ONLY: TRANSLITERATE-WITH-GLOSS. SPARINGLY: FLAG-CULTURAL-CONTEXT. BLOCKED: BRIDGE-CULTURAL-DISTANCE. Multi-meaning render rule: PRIMARY + MINIMAL FOOTNOTE NOTING OTHER SENSES (primary sense in body; brief footnote like "also: judgment / religion / truth"). One footnote per polysemous-passage maximum.
4. **Cross-axis note.** A4 default for none (no A4 purpose defaults here in the matrix; reserved for edge cases). A5 typically foreignized or balanced. A6 typically off or minimal.
5. **Said Nursi exemplar.** A pop-translation general-audience Risale-i Nur paperback — sparse footnotes only for the hardest Sufi/kalam terms; first-use transliteration gloss.
6. **Edition-tradition exemplar.** Penguin Classics paperback or NIV pew Bible (no study apparatus).

#### Level 3 — `standard`

1. **Stance.** Moderate text-surface scaffolding suitable for a standard scholarly edition. Inline glosses for technical terms on first use; moderate footnotes for context; routine transliteration with gloss; routine cultural-context flagging.
2. **Budget.** 1-3 footnotes per page (orientation); moderate inline glosses; transliteration with parenthetical paraphrase routine; cultural-context flags routine; bridge-cultural-distance moderate.
3. **Action permission + render rule.** MODERATE (3-5 per page): INLINE-GLOSS. FOR CONTEXT: FOOTNOTE. ROUTINE: TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT. MODERATE: BRIDGE-CULTURAL-DISTANCE. Multi-meaning render rule: INLINE PARENTHETICAL PAIRED ("din [judgment / religion]" or "judgment (also religion / truth)") — used for high-load polysemous passages where both senses matter for the reading.
4. **Cross-axis note.** A4 default for `devotional` (the A4 matrix's "moderate" maps here; see refinement note in section 6). A5 typically balanced. A6 typically light to standard. Orthogonal to A6's harmony report channel.
5. **Said Nursi exemplar.** A standard scholarly Risale-i Nur edition — moderate footnotes; inline glosses for Sufi/kalam terms on first use; inline parenthetical for major polysemous concepts.
6. **Edition-tradition exemplar.** NIV Study Bible, Loeb Classical Library bilingual edition (with apparatus on facing page).

#### Level 4 — `rich`

1. **Stance.** Extensive text-surface scaffolding suitable for a Norton-Critical-style edition or a scholarly-but-readable casual edition. Inline glosses routine and extensive; footnotes extensive; transliteration with full paraphrase routine; cultural-context flagging routine; bridge-cultural-distance extensive.
2. **Budget.** 3-6 footnotes per page (orientation); extensive inline glosses; appendix-light material; full inline parentheticals for polysemy.
3. **Action permission + render rule.** ROUTINE + EXTENSIVE: INLINE-GLOSS. EXTENSIVE: FOOTNOTE. ROUTINE: TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT. EXTENSIVE: BRIDGE-CULTURAL-DISTANCE. Multi-meaning render rule: INLINE PAIRED WITHOUT BRACKETS (where syntactically possible — "the day of judgment, of religion, of truth") OR FULL FOOTNOTE PAIRED (when inline pairing is awkward — full footnote explaining all senses with brief exegesis).
4. **Cross-axis note.** A4 default for `scholarly` AND `casual` (the A4 matrix's "rich (help unfamiliar)" for casual reflects the project's accessibility commitment; this is also the chain default when A7 is silent). A5 anywhere from foreignized to lightly-domesticated. A6 anywhere from minimal to standard.
5. **Said Nursi exemplar.** A Norton-Critical-style Risale-i Nur edition — extensive footnotes per page, inline glosses, light appendix material, inline parentheticals for polysemy.
6. **Edition-tradition exemplar.** Norton Critical Edition, Oxford World's Classics with critical introduction and notes.

#### Level 5 — `scholarly`

1. **Stance.** Full text-surface scaffolding apparatus suitable for a critical apparatus edition. All scaffolding-consuming actions fire freely; full apparatus channels engaged (introduction + glossary + endnotes + appendix + critical apparatus + exegetical history).
2. **Budget.** 6+ footnotes per page (orientation); full inline glosses; appendix; introduction; glossary; endnotes; critical apparatus; exegetical-history notes for major polysemous terms.
3. **Action permission + render rule.** ALL ACTIONS FREE: INLINE-GLOSS, FOOTNOTE, TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT, BRIDGE-CULTURAL-DISTANCE. Multi-meaning render rule: APPARATUS-EDITION RENDER — body + full footnote + scholarly apparatus citing exegetical/linguistic literature on the polysemy + glossary entry. Each polysemous concept receives a glossary entry; each major polysemous passage receives an exegetical-history footnote tracing the sense-tradition.
4. **Cross-axis note.** A4 default for `language-learning` (the A4 matrix's "MAX rich" maps here; see refinement note in section 6). A5 typically foreignized. A6 typically standard to maximum.
5. **Said Nursi exemplar.** A full scholarly apparatus Risale-i Nur edition — extensive footnotes, endnotes, scholarly introduction, glossary of Sufi/kalam terms, appendix, critical apparatus, exegetical history for major polysemous concepts like `din`, `nur`, `iman`.
6. **Edition-tradition exemplar.** SBL Greek NT critical apparatus edition; Robert Alter scholarly Hebrew Bible translation with apparatus; Brill critical edition.

### 3. A1/A3 action permission table per level

This is the central operational substance the translator-AI consults at every reference. At each A7 level, the table specifies which budget-consuming actions can fire and at what density.

**Budget-consuming actions** (these consume A7 budget; their permission is gated by A7 level):

| Action | `off` | `minimal` | `standard` | `rich` | `scholarly` |
|---|---|---|---|---|---|
| A1 INLINE-GLOSS | BLOCKED | sparingly (1-2/page for hardest) | moderate (3-5/page) | routine + extensive | free |
| A1 FOOTNOTE | BLOCKED | rare | for context | extensive | free + full apparatus |
| A3 TRANSLITERATE-WITH-GLOSS | BLOCKED (use TRANSLITERATE-FULLY) | first-use only | routine | routine | free |
| A3 FLAG-CULTURAL-CONTEXT | BLOCKED | sparingly | routine | routine | free |
| A3 BRIDGE-CULTURAL-DISTANCE | BLOCKED | BLOCKED | moderate | extensive | free |

**Budget-FREE actions** (available at every A7 level, subject to A5 policy bias):

- A1: KEEP-AS-IS, EXPLICATE-FUNCTION, DOMESTICATE (project policy DOMESTICATE-disfavored — used only as last-resort fallback per A1 finding), ASSUME-SHARED-CULTURAL-KNOWLEDGE.
- A3: KEEP-HONORIFICS-SOURCE, PRESERVE-CULTURAL-SPECIFICITY, TARGET-LANGUAGE-EQUIVALENT, ANGLICIZE-HONORIFICS, DOMESTICATE-CULTURAL-FRAME (project policy disfavors heavy domestication), TRANSLITERATE-FULLY (without gloss), and the other A3 actions not in the budget-consuming list.

**Why `off` is STRICT.** Permitting "minimal scaffolding for essential cases" at A7=off would make A7=off operationally indistinguishable from A7=minimal and would defeat the budget semantics. Strict blocking forces fallback to budget-FREE actions, which is precisely the operational distinction A7 needs to preserve.

### 4. Multi-meaning render rules per level + A7=off fallback

When the always-on multi-meaning preservation policy fires (a polysemous source word permits multiple senses simultaneously per the local construction — see root finding's Layer 2 POLICY section), A7's level controls HOW the preserved senses render at the text surface. The policy controls WHETHER (preservation is invariant); the user controls HOW.

| A7 Level | Render mechanism |
|---|---|
| `off` | EXPLICATE-FUNCTION fallback (6th case) — preserve polysemy via paraphrase combining senses into the body; no scaffolding |
| `minimal` | PRIMARY + MINIMAL FOOTNOTE noting other senses (primary in body; brief footnote like "also: judgment / religion / truth") |
| `standard` | INLINE PARENTHETICAL PAIRED (`din [judgment / religion]` or `judgment (also religion / truth)`) |
| `rich` | INLINE PAIRED WITHOUT BRACKETS (where syntactically possible, e.g. "the day of judgment, of religion, of truth") OR FULL FOOTNOTE PAIRED |
| `scholarly` | APPARATUS-EDITION RENDER (body + footnote + scholarly apparatus citing exegetical/linguistic literature + glossary entry) |

**The A7=off + polysemy policy interaction is the resolution-via-EXPLICATE-FUNCTION case.** The policy says preserve multiple senses; A7=off blocks the scaffolding-render mechanisms (footnote, parenthetical, apparatus). EXPLICATE-FUNCTION (a budget-FREE action) provides the preservation by paraphrasing rather than bracketing — both senses fit into the body text as plain prose. The polysemy POLICY (preservation) is invariant; the RENDER falls back to the only mechanism A7=off permits.

### 5. Runtime conflict resolution

When A7 is too low to accommodate the A1/A3 actions a low-A1 reader-level + foreignization-preferring A5 would otherwise demand (canonical case: A7=off + A1=very_basic + A5=foreignized), the AI applies a deterministic three-step rule:

1. **STRICT budget enforcement.** A7 BLOCKS budget-consuming actions per the action permission table; the AI does not exceed.
2. **FALLBACK to budget-FREE actions.** EXPLICATE-FUNCTION, KEEP-AS-IS, ASSUME-SHARED-CULTURAL-KNOWLEDGE, PRESERVE-CULTURAL-SPECIFICITY, etc. are available — the AI selects per A5 stance.
3. **FLAG in harmony report at A6 Levels 3+.** Records that source-cultural specificity was preserved via paraphrase or budget-FREE action rather than via scaffolding, so the user can see the trade-off in the apparatus.

**Worked examples.**

- A7=off + A1=very_basic + A5=foreignized: AI wants to use INLINE-GLOSS for unfamiliar references but A7=off blocks. AI falls back to EXPLICATE-FUNCTION (paraphrases the cultural reference into the body). Harmony report at A6 Level 3+ flags: "source-cultural specificity preserved via paraphrase rather than gloss (A7=off budget constraint)."

- A7=off + polysemy policy fires (e.g., `din` in Said Nursi): AI cannot use INLINE PARENTHETICAL PAIRED or footnote (A7=off blocks). AI uses EXPLICATE-FUNCTION to combine senses ("the day of judgment, of religion, of true reckoning") into the body. Multi-meaning POLICY satisfied (WHETHER — preservation); render forced budget-FREE (HOW — paraphrase).

- A7=off + DOMESTICATE-disfavored project policy + lay reader: AI may settle for compromise. EXPLICATE-FUNCTION when possible; PARAPHRASE-IN-LAYMAN-TERMS as last resort (still respects DOMESTICATE-disfavored policy at lower priority than scaffolding budget).

**UX-layer surface-at-config-time is DEFERRED.** A future UX inquiry should consider surfacing the conflict at configuration time ("you've selected A7=off + A5=foreignized; this may produce uncomfortable text for your A1=very_basic reader"). This is additive to the A7 spec, not part of it — the runtime resolution must be deterministic regardless of UX-layer presence.

### 6. Cross-axis boundaries + A4 matrix cross-validation

#### A5↔A7

A5 (Source Fidelity) sets the strategic stance modulating which A1/A3 actions to SELECT in the first place — foreignized-max biases toward KEEP-AS-IS and TRANSLITERATE-FULLY; balanced biases toward EXPLICATE-FUNCTION and TARGET-LANGUAGE-EQUIVALENT; lightly-domesticated biases toward TARGET-LANGUAGE-EQUIVALENT and DOMESTICATE-CULTURAL-FRAME.

A7 sets the budget constraining which of those selected actions the budget can AFFORD. A5=foreignized + A7=off forces the AI to use budget-FREE foreignization-preserving alternatives (EXPLICATE-FUNCTION over INLINE-GLOSS — both preserve source specificity but EXPLICATE-FUNCTION doesn't consume scaffolding budget).

Distinct mechanisms; orthogonal axes.

#### A6↔A7

A6 (Form Preservation) determines which harmony_layer tiers (Tier 1 Meaning Core / Tier 2 Pragmatic Function / Tier 3 Cultural-Aesthetic / Tier 4 Acoustic-Material) are preserved during the 3-Pass methodology (Meaning Lock → Harmony Map → Target Reconstruction). At A6 Levels 3+, A6 produces a **harmony REPORT** as a separate meta-analytic apparatus channel — the translator's commentary on what was preserved and what was sacrificed at the harmony level.

A7 controls **text-surface scaffolding** (footnotes, glosses, transliterations) on the reading page itself.

Both A6's harmony report and A7's footnotes live "in apparatus," but in DIFFERENT apparatus channels. A6's is meta-analytic (post-translation commentary on the form-preservation work). A7's is reader-facing scaffolding (in-page explanation of references and senses). They can coexist at the same level without conflict.

This resolves A6 finding's frontier flag (A6↔A7 cross-validation needed): orthogonality holds; the cross-validation is the separation-of-apparatus-channels.

#### A7↔A8 (forward-looking)

A7 controls text-surface scaffolding on the reading page. A8 Analysis Depth controls separate-sections analysis (sections appended after the translation, not in-line). Per the root architecture, these are distinct surfaces — A7 is in-page; A8 is post-translation. The boundary must be re-validated when the A8 inquiry runs.

Potential edge case for A8 to handle: when A8 is high (extensive separate-sections analysis), does the harmony report (A6) or the in-page scaffolding (A7) move to the analysis section? Tentative answer: A6 harmony report can live either in A8's analysis section or as standalone apparatus; A7 in-page scaffolding stays in-page regardless of A8. To be confirmed in A8 inquiry.

#### A4 matrix cross-validation + refinement note

The A4 finding's matrix gave per-purpose A7 defaults using informal verbiage. The mapping to A7's precise labels:

| A4 Purpose | A4 matrix A7 verbiage | A7 5-level mapping |
|---|---|---|
| scholarly | rich | `rich` |
| devotional | moderate | `standard` (A4 "moderate" → A7 `standard`) |
| casual | rich (help unfamiliar) | `rich` |
| language-learning | MAX rich | `scholarly` (full apparatus parallel-text) |
| performance | minimal | `minimal` (or `off` for pure oral) |

**A4 finding refinement note (parallel to A6 finding's).** A4 used informal verbiage; A7 uses precise labels. At the next A4 maintenance pass, propagate the naming alignment:

- A4 matrix's "moderate" → A7 `standard`.
- A4 matrix's "MAX rich" → A7 `scholarly`.

This is the same kind of carry-forward refinement A6's finding logged for A4's harmony verbiage. Both refinements should ride the same A4 maintenance pass to keep the matrix internally consistent with the precise labels the downstream axes settle.

## Inherited Commitments Re-test

The `_branch.md` declared a Synthesis Trigger naming five prior outputs (root + A6 + A5 + A4 + A1, plus A3 by reference). Re-test of each inherited commitment:

| # | Commitment | Source | Re-test status | Evidence |
|---|---|---|---|---|
| IC1 | A7 plain-ordinal | root | RE-TESTED OK | Pattern fits; A4 matrix uses ordinal positions; no categorical / asymmetric / composite structure surfaces |
| IC2 | A7 5-level cardinality | root | RE-TESTED & CONFIRMED | Edition-tradition exemplars (utility / Penguin / NIV-study / Norton Critical / SBL) confirm 5 operationally-distinct levels; A4 matrix uses 5 distinct values (minimal, moderate, rich, MAX rich, performance-zero-implicit); 4 collapses Norton Critical with SBL apparatus; 6+ over-stratifies |
| IC3 | A7 subsumes feature-activation bundle minus harmony | root | RE-TESTED OK | Footnote toggle, transliteration toggle, parenthetical glosses, brief in-line explanations all live as per-level density gradients; A6 took harmony |
| IC4 | A7 multi-meaning render control role | root POLICY section | RE-TESTED & SPECIFIED | 5 render mechanisms per level + A7=off → EXPLICATE-FUNCTION fallback (6th case); policy preserves WHETHER, A7 controls HOW |
| IC5 | A4 per-purpose A7 defaults | A4 finding | RE-TESTED & CROSS-VALIDATED with naming refinement note | A4 matrix's "moderate" → A7 `standard`; "MAX rich" → A7 `scholarly`; refinement note propagation at next A4 maintenance pass |
| IC6 | A7 interaction with A1/A3 actions | A1 + A3 + chain | RE-TESTED & SPECIFIED | Full action permission table per level operationalizes; budget-consuming vs budget-FREE classification |
| IC7 | NEW translator-strategy 4-component template | A5 + A6 | RE-TESTED & ADAPTED | A7's template = scaffolding stance + budget spec + A1/A3 action permission/render rule + cross-axis interaction. Same shape as A5/A6; A7-specific composition |
| IC8 | Receptive-only NOT APPLICABLE | A4 + A5 + A6 | RE-TESTED OK | A7 is translator-strategy / user-configuration; not a reader-property |
| IC9 | Chain default via A4 matrix | A5 + A6 | RE-TESTED & APPLIED | Default `rich` via A4 chain (silent → casual → A4 matrix's "rich help unfamiliar" → `rich`) |
| IC10 | Language-agnostic at concept level | root + chain | RE-TESTED OK | Per-target-language scaffolding feasibility flagged as future inquiry (FF4); concept-level is language-agnostic |
| IC11 | A6↔A7 cross-validation needed | A6 finding | RE-TESTED & DOCUMENTED | Orthogonality holds; A6 = harmony report (meta-analytic apparatus); A7 = text-surface scaffolding (reader-facing apparatus); distinct apparatus channels at the same level. Resolves A6's frontier flag |

All 11 inherited commitments either re-tested OK, or refined with explicit reasoning, or specified into operational substance. No commitment carried forward without re-test.

## Next Actions

### MUST

- **What:** Commit `scaffolding: Literal["off", "minimal", "standard", "rich", "scholarly"]` to the schema.
  **Who:** schema-implementation step (file TBD — pending root schema-commit inquiry).
  **Gate:** observable — when the schema implementation step happens for any Strategy axis, A7 commits alongside A5 and A6.
  **Why:** Operationalizes A7 as a configurable axis the user can set and the AI can read.

- **What:** Encode the A1/A3 action permission table per A7 level in the translator-AI prompt context.
  **Who:** translator-AI prompt assembly step.
  **Gate:** observable — when the translator-AI is invoked with A7 as a context variable, the action permission table must be in the prompt.
  **Why:** Without this, the AI doesn't know which actions can fire at each level — the operational substance is lost.

- **What:** Encode the 5 multi-meaning render rules + A7=off → EXPLICATE-FUNCTION fallback in the translator-AI prompt context.
  **Who:** translator-AI prompt assembly step.
  **Gate:** observable — when the polysemy policy fires, the render rule for the current A7 level must be in the prompt.
  **Why:** Without this, the user controls WHETHER but not HOW; the policy is incomplete.

- **What:** Implement the runtime conflict resolution rule (strict budget + fallback to budget-FREE + harmony-report flag at A6 Levels 3+).
  **Who:** translator-AI runtime logic + harmony-report assembly step.
  **Gate:** condition-bound — when A7's blocked-action list intersects with the AI's preferred A1/A3 action for the current reference, the fallback must engage.
  **Why:** Without deterministic resolution, A7=off becomes operationally lax and loses budget semantics.

### COULD

- **What:** Propagate the A4 finding refinement note (A4 "moderate" → A7 `standard`; A4 "MAX rich" → A7 `scholarly`) at the next A4 maintenance pass; bundle with A6's parallel A4 refinement note.
  **Who:** A4 finding maintainer.
  **Gate:** time-bound — at the next A4 maintenance pass.
  **Why:** Keeps the matrix internally consistent with the precise labels downstream axes settle. Parallel to A6's refinement note; should ride the same pass.

- **What:** Add a UX-layer config-time conflict surface ("A7=off + A5=foreignized + A1=very_basic may produce uncomfortable text").
  **Who:** UX inquiry (future).
  **Gate:** condition-bound — when UX inquiry runs.
  **Why:** Additive to A7 spec; does not change A7 runtime semantics; improves user awareness at configuration time.
  **Depends-on:** None — UX layer is additive and decoupled from A7 runtime. No MUST-dependency.

### DEFERRED

- **What:** Per-target-language scaffolding feasibility study (does scholarly apparatus differ per target language tradition — Western footnoting vs Eastern marginalia?).
  **Gate:** condition-bound — when Comprehenslate adds second target language.
  **Why (if revived):** Allows A7=scholarly to specify language-appropriate apparatus style; otherwise stays Western-default.

- **What:** Polysemy policy operational spec (the always-on policy itself, not A7's render-control role).
  **Gate:** condition-bound — when a dedicated POLICY inquiry is scoped (per root finding's commitment that always-on policies need separate specs).
  **Why (if revived):** A7's multi-meaning render rules assume the polysemy policy fires under specified conditions; those conditions need their own inquiry.

- **What:** A7↔A8 cross-validation.
  **Gate:** condition-bound — when A8 Analysis Depth inquiry runs.
  **Why (if revived):** Confirms in-page (A7) vs post-translation-sections (A8) boundary; resolves where harmony report (A6) lives when A8 is high.

## Reasoning

### Why these five level names

Considered alternatives:

- **`none / low / standard / high / max`** — generic ordinal labels. KILLED: lose the apparatus-edition signal at "max" (`scholarly` evokes Brill/SBL/Robert-Alter, `max` doesn't). The user benefits from the edition-tradition anchor.
- **`off / sparse / standard / extensive / apparatus`** — descriptive density labels. KILLED: lose the casual-reader-help signal that `rich` carries (the A4 matrix's "rich help unfamiliar" reading); `extensive` is more clinical.
- **`off / minimal / standard / rich / scholarly`** — root proposal. SURVIVED: maps to edition-tradition exemplars (each label has a recognizable edition behind it); reads cleanly in user-facing schema and AI prompt context; preserves the casual-reader-help signal at `rich`.

### Why 5 levels, not 4 or 6

- **4 levels** — would merge `minimal` + `standard` or `rich` + `scholarly`. KILLED: Norton Critical (rich) vs SBL Greek NT (scholarly) are operationally different editions — the per-page footnote density, the presence of critical apparatus, and the inclusion of exegetical-history glossary entries differ meaningfully. Merging loses the operational distinction.
- **6+ levels** — would over-stratify. KILLED: the A4 matrix uses 5 distinct A7 values (minimal, moderate, rich, MAX rich, performance-implicit-zero); 6+ has no natural anchor in the use cases.

### Why default `rich` over default `standard`

- **`standard` as safer baseline** — would be the more conservative choice. KILLED: A4 matrix's casual A7 = "rich (help unfamiliar)" is the project's commitment to accessibility for outsider/uninitiated readers; defaulting to `standard` would silently downgrade the matrix's intent. The chain pattern (A7 silent → A4 silent → A4 = casual → A4 matrix → A7 = `rich`) settles it.
- **`rich` is non-obvious but chain-derived** — the user might intuit "casual → low scaffolding." The matrix says otherwise: casual readers of source-cultural texts (Said Nursi, Russian novels in translation) benefit from rich scaffolding precisely because they're casual outsiders who need help. The default reflects this.

### Why STRICT A7=off blocks all budget-consuming actions

- **Lax A7=off (permit minimal scaffolding for cases the AI deems essential)** — would feel more pragmatic. KILLED: makes A7=off operationally identical to A7=minimal and dissolves the axis distinction. The strict version forces fallback to budget-FREE actions, which preserves the semantics and creates a clear edge case (A7=off + foreignized A5 may produce uncomfortable text; user can re-set to minimal if uncomfortable).

### Why budget = qualitative + per-page operational guidance (not hard caps)

- **Qualitative only** — would be too loose. KILLED: AI has no sanity-check unit; "rich" could mean anywhere from 1 to 50 footnotes per page.
- **Hard caps** — would over-constrain. KILLED: some passages legitimately need more (a dense polysemy-heavy paragraph might warrant 5 footnotes even at `minimal` if all 5 are for hardest references). Hard caps would force the AI to drop necessary scaffolding.
- **Qualitative + per-page orientation guidance** — SURVIVED. Per-page numbers are orientation thresholds, not enforcement gates; AI uses them as sanity-check budget; qualitative gives prompt-clear stance.

### Why STRICT budget + fallback runtime resolution over budget-exceed

- **Budget-exceed for must-haves (AI can exceed scaffolding budget for must-have references)** — would feel pragmatic. KILLED: defeats budget semantics; A7 becomes advisory not operational; the per-level distinction collapses.
- **STRICT budget + fallback to budget-FREE + harmony-report flag at A6 Levels 3+** — SURVIVED. Deterministic; preserves A7 axis semantics; harmony report communicates the trade-off to the user; UX-layer can be added later without changing A7 runtime.

### Why UX-layer config-time surface is DEFERRED

- **Include UX-layer in A7 spec** — would mean specifying when and how to surface conflicts. KILLED: this is a UX inquiry concern; for A7 axis spec, the runtime resolution must be deterministic regardless of UX-layer; UX-layer is additive. Including would over-couple A7 to UX surface choices.

### Why 5 multi-meaning render rules + A7=off fallback (not 2 mechanisms)

- **2 mechanisms (footnote vs inline)** — would simplify. KILLED: loses operational distinction between PRIMARY-ONLY-WITH-FOOTNOTE (minimal) and INLINE PARENTHETICAL PAIRED (standard) and INLINE PAIRED WITHOUT BRACKETS (rich); these are visually and pedagogically different choices. 5 mechanisms map naturally to 5 levels; A7=off forces the 6th case (EXPLICATE-FUNCTION fallback) because no scaffolding-render mechanism is available.

### Why A6↔A7 orthogonality holds (resolving A6's flagged frontier)

- **A6 and A7 both produce apparatus → suspected coupling** — A6 finding flagged this as needing cross-validation. KILLED (cross-validation succeeded): A6 produces a harmony REPORT (meta-analytic apparatus channel — post-translation commentary on what was preserved); A7 produces text-surface scaffolding (reader-facing apparatus channel — in-page footnotes and glosses). Different channels at the same level. The two apparatus are distinguishable by purpose, audience, and placement.

### Why receptive-only NOT APPLICABLE

- **Maintain parity with A1-A3 receptive-only mode** — would be schema-uniform. KILLED: A7 is translator-strategy / user-configuration / scaffolding-budget, not a reader-property. Parallel to A4/A5/A6 non-applicability. Schema can carry the explicit non-inheritance marker.

### Why Strategy-family-closure marker

- **Skip the closure marker (just produce the level definitions)** — would be more terse. KILLED: the closure marker is a synthesis-trigger value — it tells the next inquiry (A8) where it sits in the framework and what's still open (A8 + UX-layer + polysemy policy spec + per-target-language scaffolding); without it, A8's inquiry has less context for orientation. Parallel to Reader-family-closure and Purpose-family-closure markers.

### Innovations rejected at the structural level

Five Piece-Level Inversions were tested in the innovation discipline; all were rejected on structural grounds:

- **A7-template ≡ A5-template verbatim** — rejected: doesn't fit A7's action-permission + render-rule emphasis. A7 needs its own composition.
- **Permissive A7=off** — rejected: as above (Lax A7=off dissolves axis distinction).
- **A7=off + polysemy → primary-only render (override policy)** — rejected: violates always-on policy; EXPLICATE-FUNCTION respects policy AND budget.
- **Budget-exceed for must-haves** — rejected: defeats budget semantics.
- **Strategy family extended beyond 3/3** — rejected: root architecture commits to 3 Strategy axes; extending requires root revision.

### Cross-domain illustrations DEFERRED

- **Academic publishing apparatus tiers (peer-reviewed journal vs textbook vs popular trade)** — DEFERRED. Cross-domain illustration with parallel scaffolding spectrum; useful for analogical reasoning but not load-bearing for A7 spec.
- **Software documentation tiers (tooltip vs inline help vs full docs vs API reference vs developer guide)** — DEFERRED. Same status.

### Research frontier

- **AI-runtime adaptive scaffolding** — RESEARCH FRONTIER. AI infers reader-need + adjusts A7 dynamically per passage rather than applying a fixed level uniformly. Long-horizon research; out of scope for A7 spec.

## Open Questions

### Monitoring

- Observable after A8 Analysis Depth inquiry runs: A7↔A8 boundary re-validation. Confirms in-page (A7) vs post-translation-sections (A8) surface distinction; resolves where harmony report (A6) lives when A8 is high.
- Observable after first translation runs: do the per-page operational guidance thresholds (0-1, 1-3, 3-6, 6+ footnotes per page) hold across real Said Nursi material, or do passages drift consistently above or below?

### Blocked

- Polysemy policy operational spec — A7's multi-meaning render rules assume the polysemy policy fires under specified conditions; those conditions need their own dedicated POLICY inquiry per root commitment. Until that inquiry runs, A7's render rules cite the policy without being able to verify the firing conditions.

### Research Frontiers

- AI-runtime adaptive scaffolding (AI infers reader-need + adjusts A7 dynamically per passage). No known path; requires new investigation. Out of scope for A7 spec.

### Refinement Triggers

- If a future translation reveals the per-page operational guidance thresholds are systematically wrong (e.g., `rich` consistently produces 8-10 footnotes/page instead of 3-6), revise the thresholds without changing the qualitative orientation.
- If the harmony-report-flag mechanism for runtime conflict resolution proves insufficient (users miss the flag and produce uncomfortable text), revisit the UX-layer config-time surface decision.
- When a second target language is added, revisit per-target-language scaffolding feasibility (Western footnoting vs Eastern marginalia, etc.).

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
lets dive deep into Strategy │ A7 Scaffolding
```

</details>
