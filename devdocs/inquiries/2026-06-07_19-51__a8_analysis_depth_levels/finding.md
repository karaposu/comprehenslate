---
status: active
model: claude-opus-4-7[1m]
effort: max
---
# Finding: A8 — Analysis Depth

## Question

**From `_branch.md`.** A8 — Analysis Depth is the sole axis in the Depth family AND the final axis in Comprehenslate's 8-axis translation-configuration framework. With A8 specified, the framework closes at 8/8 axes complete. A8 controls how much interpretive material the system surfaces ALONGSIDE the translation in separate analysis sections — etymology notes, rhetorical analysis, cross-references, exegetical history, lexical-philological apparatus — distinct from A7's text-surface scaffolding which lives on the reading page. A8 inherits from the existing `DEPTH_PROFILE` knob in `.env.example` (the only Layer 1 axis with a pre-existing operational anchor in the project's prior configuration sketch), but the inheritance needed substantive validation rather than rubber-stamping.

A8 carries three distinguishing characteristics: (1) it is the **framework-closing** axis — the only inquiry in the chain whose completion brings the framework to 8/8 and unblocks schema commit + per-purpose default matrix synthesis + downstream Layer 1A/2/3 work; (2) it proposes a different cardinality from other ordinal axes — root proposed 4 levels but substantive validation against the cross-axis pattern surfaces a 5-level structure with explicit `none`; (3) it lives in the **separate-sections apparatus channel** distinct from A7's text-surface channel, making the A7↔A8 boundary the most consequential cross-axis boundary in the framework.

Decide: cardinality (validate or revise root's 4-level proposal); level names; per-level depth specification; content-type-by-level table (the operational substance — what KINDS of analysis fire at each level); A7↔A8 boundary spec; harmony-report-location across A8 levels (resolving A7 finding's frontier flag); multi-meaning analysis at A8 (distinct from A7's render); NEW translator-strategy 4-component template adaptation; A4 matrix cross-validation; A8↔A5/A6/A7 boundaries; Said Nursi corpus mapping per level; edition-tradition exemplars per level; receptive-only applicability; default-when-A8-silent; DEPTH-family-closure marker; FRAMEWORK-closure marker.

**Goal.** Each level operationalizable as an AI prompt instruction — the per-level prose becomes part of the translator-AI's context, telling the AI which content-types fire at each level and at what density. The per-level depth spec, the content-type-by-level table, and the A7↔A8 boundary spec are the operational substance. Framework closes at 8/8; only A8 closes the framework as a whole.

## Finding Summary

- **5 ordinal levels** `none | surface | standard | deep | scholarly`. SUBSTANTIVE REVISION of root's proposed 4 levels — added `none` at position 1 parallel to A6=`off` / A7=`off`, addressing the explicit-zero case that DEPTH_PROFILE silently elided. The original 4 DEPTH_PROFILE labels are preserved at positions 2-5 (`.env.example` should add `none` at next maintenance pass). 4 levels would collapse oral-recitation (zero apparatus) with Penguin-paperback-with-brief-intro (minimal-nonzero apparatus); 6+ over-stratifies. The A4 matrix uses 5 distinct A8 values (surface / standard / deep / scholarly / surface-for-performance) corroborating 5-level cardinality.

- **Per-level depth = qualitative + content-type-density-per-major-passage operational guidance.** (1) Qualitative threshold per level — `none` = pure translation, no separate analysis; `surface` = clean translation with minimal pointers; `standard` = brief introduction + select notes; `deep` = Norton-Critical-style analysis chapter; `scholarly` = full critical apparatus edition. (2) Per-passage operational guidance — `none`=0 content-types active; `surface`=0-2 content-types active minimally (introduction + glossary); `standard`=2-4 content-types active routinely; `deep`=4-10 content-types active per major passage; `scholarly`=all 12 content-types fire as relevant. NOT hard caps; orientation thresholds.

- **Content-type-by-level table** is A8's central operational substance — the structural analog to A7's action-permission table. 12 content-types (Introduction / Glossary entries / Etymology notes / Rhetorical analysis / Cross-references / Exegetical history / Lexical-history / Target-language-equivalent analysis / Theological commentary / Historical-critical context / Philological apparatus / Cross-tradition references) × 5 levels = 60-cell matrix. At each cell: blocked / brief / moderate / extensive / exhaustive density. A8's CONTENT-PRODUCTION role (producing analysis directly) is structurally distinct from A7's CONTENT-GATING role (gating A1/A3 actions); A8 has no action-permission table.

- **A7↔A8 boundary settled with THREE complementary framings** (all three apply; LOCATION is the default tiebreaker at disagreement edge cases): (1) by LOCATION — A7 in-page (footnotes / glosses on reading page); A8 separate-sections (front matter / endnotes / appendix / sidebars); (2) by SCOPE — A7 per-reference (specific cultural reference at this word); A8 per-passage / per-corpus (full passage commentary; cross-references; structural analysis); (3) by AUDIENCE-INTERACTION — A7 inline interruption (reader looks down then back up at same passage); A8 deferred study session (reader reads translation first, then turns to analysis). Operational test for AI: "does this belong on the reading page next to the source word, or in a separate analysis section after the translation?" Resolves A7 finding's deferred frontier flag.

- **Harmony-report-location settled.** A6 harmony report (at A6 Levels 3+) stays in the A6 channel STANDALONE regardless of A8 level. At A8 = `deep` or `scholarly`, cross-references between channels are added (harmony report cites A8 sections; A8 sections cite harmony report) for reader navigation. This preserves A6 finding's apparatus-channel commitment (does not move the harmony report; does not modify A6 finding) AND preserves A6↔A8 orthogonality (each axis owns its channel). Resolves A7 finding's harmony-report-location open question.

- **Multi-meaning analysis at A8** is distinct from A7's multi-meaning render. The polysemy policy is invariant (WHETHER preservation); A7 controls HOW preserved senses render in the translation (footnote / parenthetical / inline-paired / apparatus); A8 produces EXEGETICAL-HISTORY analysis of the polysemous concept in the separate-sections channel at high A8 levels. Per-level rule: `none` = no exegetical-history analysis; `surface` = no exegetical-history analysis; `standard` = brief lexical note in glossary on key polysemy; `deep` = exegetical-history paragraph per major polysemous concept; `scholarly` = full exegetical-history apparatus (commentary tradition + lexical-philological argument + cross-tradition references).

- **Default-when-A8-silent = `standard` via dual-tier resolution.** Tier 1 (A4 chain): A8 silent + A4 explicitly set → A4 matrix's per-purpose A8 value. Tier 2 (conservative-bias fallback): A8 silent + A4 silent → A8 = `standard`. Dual-tier is necessary because A8's A4 matrix is uniquely cold-start-sparse (casual default `surface` is operationally near-empty); conservative-bias `standard` defends at framework-cold-start before any user calibration. As feedback accumulates, the conservative-bias fallback may shift toward typical-use bias.

- **A4 finding refinement note: language-learning A8 = `scholarly`.** A4 matrix used informal verbiage `deep+scholarly` for language-learning A8 default — ambiguous (deep OR scholarly OR both?). A8 maps this cleanly to `scholarly` (full parallel-text apparatus edition). At next A4 maintenance pass, propagate the alignment: A4 matrix language-learning A8 → `scholarly`. This is parallel to A6/A7 finding refinement notes; should ride the same A4 maintenance pass to keep the matrix internally consistent.

- **DEPTH_PROFILE inheritance validated with refinement.** The 4 original DEPTH_PROFILE labels (`surface | standard | deep | scholarly`) are preserved at positions 2-5; `none` is added at position 1. At next .env.example maintenance pass, propagate: `DEPTH_PROFILE` should accept `none` (or document the historical default as `surface` for legacy compatibility while exposing `none` as the explicit-zero case).

- **NEW A8-adapted 4-component template.** Adapted from A5/A6/A7 translator-strategy template with A8-specific 3rd component: (1) Analysis stance description (what KIND of analysis the AI produces at this level; what apparatus channels open); (2) Per-level depth specification (qualitative + content-type-density operational guidance); (3) Content-type-by-level table reference + A7↔A8 boundary spec for this level + harmony-report-location at this level + multi-meaning analysis at this level — the operational substance; (4) Cross-axis interaction note (A4 matrix match + A5/A6/A7 interactions + FRAMEWORK-CLOSURE marker). The 3rd component is the substantive A8 adaptation — replaces A7's action-permission table reference with A8's content-type emphasis.

- **Receptive-only NOT APPLICABLE.** A8 is translator-strategy and user-configuration — analysis depth the user wants the system to produce — not a property of the reader (parallel to A4, A5, A6, A7). Explicit non-inheritance from the Reader-family pattern.

- **Cross-axis orthogonality preserved.** A5↔A8: A5 stance modulates A8 CONTENT KIND (foreignized → etymology emphasis; lightly-domesticated → target-language-equivalent justification emphasis); A8's EXTENT/CHANNEL is independent. A6↔A8: A6 = harmony REPORT in A6 channel; A8 = separate-sections analysis in A8 channel; cross-references at high A8. A7↔A8: 3-framing rule + LOCATION default tiebreaker; rich A7 + surface A8 valid (in-page apparatus + clean post-translation); minimal A7 + scholarly A8 valid (clean translation + heavy analysis); A7=off + A8=none = maximally-clean pure-translation configuration.

- **DEPTH-family CLOSES at 1/1** with A8 (smallest family). **FRAMEWORK CLOSES at 8/8** — UNIQUE meta-closure marker. After this inquiry: Reader 3/3 + Purpose 1/1 + Strategy 3/3 + Depth 1/1 = 8/8 axes complete. Downstream cascades unblocked: schema commit (pydantic dataclasses); per-purpose × per-axis default matrix synthesis; translator-AI prompt assembly with all 8 axes; Layer 1A UX preset catalog (deferred per root); Layer 2 POLICY operational specs (5 deferred); Layer 3 SOURCE-DESCRIPTION schema (deferred); UX-layer runtime conflict surface (deferred); framework-synthesis meta-inquiry (rolling up all 8 findings into single canonical spec — recorded as Next Actions COULD; itself a future inquiry).

## Finding

**Context for the cold reader.** Comprehenslate is an AI-assisted translation system. The user's primary project is the Said Nursi corpus (Risale-i Nur, a 20th-century Turkish Islamic theological work). The 8-axis configuration framework lets the user state, before each translation, what the audience knows (Reader family: A1 Cultural Reference Recognition, A2 Domain Expertise, A3 Source Culture), what the translation is for (Purpose family: A4 Purpose), how the translator should behave strategically (Strategy family: A5 Source Fidelity, A6 Form Preservation, A7 Scaffolding), and how much separate-sections analysis to attach (Depth family: A8 Analysis Depth). Seven of the eight axes were specified in prior inquiries before this one ran. This inquiry, A8, is the final axis — it closes the Depth family at 1/1 and closes the entire Layer 1 framework at 8/8. With A8 specified, the framework becomes ready for schema commit (pydantic dataclasses), per-purpose default matrix synthesis, and translator-AI prompt assembly with all 8 axes. The two substantive decisions A8 had to make beyond simple level-setting were: (a) revise root's 4-level proposal to 5 by adding explicit `none`, motivated by the cross-axis pattern (every other ordinal axis has an explicit-zero level) and by the A4 matrix's performance default needing zero-analysis semantics; (b) make the A7↔A8 boundary operationally clear since A8's apparatus channel is structurally distinct from A7's but they're both "apparatus" and could be confused at the edge.

### 1. Framework

A8 is a plain-ordinal axis with 5 ordinal levels:

```
A8: none | surface | standard | deep | scholarly
```

The level names preserve the original DEPTH_PROFILE labels at positions 2-5 (user-recognizability from `.env.example`) and add `none` at position 1. The cardinality is a substantive REVISION of root's proposed 4 levels. The reason: the cross-axis pattern across A6 (which has `off`) and A7 (which has `off`) expects an explicit-zero level on each ordinal axis, and the A4 matrix performance default `surface` is operationally distinct from casual default `surface` only if `surface` itself means "minimal-but-nonzero" rather than "zero-or-minimal." DEPTH_PROFILE's original knob conflated those two cases; A8 makes the distinction explicit. The substantive validation: 4 levels collapses oral-recitation (zero apparatus) with Penguin-paperback-with-brief-intro (minimal-nonzero apparatus); 5 levels with explicit `none` keeps both cases operationally distinct. The `.env.example` DEPTH_PROFILE knob should be updated at next maintenance pass to accept `none`.

A8's user-facing question is "How much interpretive commentary should accompany the translation?" The AI consults A8 at the major-passage level to determine which content-types fire and at what density.

**Receptive-only NOT APPLICABLE.** A8 is a translator-strategy axis (user-configuration; analysis depth). It is not a reader-property like A1/A2/A3. It does not inherit a receptive-only mode from the Reader family. This parallels A4, A5, A6, A7 non-applicability.

**Default-when-A8-silent = `standard` via dual-tier resolution.** A8's dual-tier default is unique among the Strategy/Depth axes:

- **Tier 1 (A4 chain):** when A8 is silent but A4 is explicitly set, the system uses the A4 matrix's per-purpose A8 value (scholarly → `deep`; devotional → `standard`; casual → `surface`; language-learning → `scholarly`; performance → `surface`).
- **Tier 2 (conservative-bias fallback):** when both A8 and A4 are silent (framework-cold-start), the system uses A8 = `standard` (conservative-bias-fallback midpoint).

The dual-tier exists because A8's A4 matrix casual default `surface` is operationally near-empty — A8 chained-silent through casual default would produce sparse output at framework-cold-start before any user calibration has accumulated. Conservative-bias `standard` defends this case while still allowing A4-driven defaults when A4 is set. As empirical feedback accumulates, the conservative-bias fallback may shift toward typical-use bias.

**DEPTH-family-closure marker (1/1) + FRAMEWORK-closure marker (8/8).** Depth is the smallest family (one axis). A8 closes Depth at 1/1 AND closes the entire 8-axis framework at 8/8: Reader 3/3 + Purpose 1/1 + Strategy 3/3 + Depth 1/1 = 8 axes complete. This is the only inquiry in the chain that closes the framework as a whole; the unique meta-closure marker signals that downstream cascades are unblocked.

### 2. Per-level definitions

Each level uses the NEW A8-adapted 4-component template:

1. **Analysis stance** — what KIND of analysis the AI produces at this level; what apparatus channels open.
2. **Per-level depth specification** — qualitative threshold + per-passage content-type-density operational guidance.
3. **Content-type-by-level table reference + A7↔A8 boundary at this level + harmony-report-location at this level + multi-meaning analysis at this level** — the operational substance consulted at content-production time.
4. **Cross-axis interaction note** — which A4 purposes default here + A5/A6/A7 interactions + FRAMEWORK-CLOSURE marker.

#### Level 1 — `none`

1. **Stance.** No separate-sections apparatus at all. The translation reads as pure target-language prose with no front matter, no endnotes, no appendix, no analysis sections. Just the translation.
2. **Depth.** Zero content-types fire. Qualitative: pure translation only.
3. **Operational substance.** Content-type-by-level table: ALL 12 content-types BLOCKED. A7↔A8 boundary irrelevant at A8=none (no A8 channel content to position). Harmony-report-location: A6 harmony report remains in A6 channel regardless (this level doesn't affect it). Multi-meaning analysis: NONE (the polysemy policy preserves senses via A7's render mechanism only; no A8 exegetical-history analysis produced).
4. **Cross-axis note.** A4 default for `performance` (oral recitation; zero apparatus) and in some configurations for `casual` (when paired with A7=off for utility translation). A5/A6/A7 orthogonal. A7=off + A8=none = maximally-clean pure-translation configuration (oral recitation use case).
5. **Said Nursi exemplar.** An oral recitation passage of Risale-i Nur delivered live; pure translation only, no apparatus.
6. **Edition-tradition exemplar.** A utility translation (road sign / quick UN-style summary / oral interpretation) with no apparatus.

#### Level 2 — `surface`

1. **Stance.** Minimal separate-sections apparatus. Brief publisher's note or minimal glossary for the most-needed terms; no analysis chapters, no extensive front matter.
2. **Depth.** 0-2 content-types fire minimally (introduction + glossary for most-needed terms only).
3. **Operational substance.** Content-type-by-level table: Introduction (none-or-publisher's-note) + Glossary (major terms only) ACTIVE BRIEFLY; all other content-types BLOCKED. A7↔A8 boundary: A7 carries scaffolding in-page; A8 surface keeps separate-sections minimal. Harmony-report-location: A6 harmony report remains in A6 channel standalone (no cross-references at A8=surface). Multi-meaning analysis: NONE (still no exegetical-history; the brief glossary may note polysemy without full analysis).
4. **Cross-axis note.** A4 default for `casual` (per A4 matrix) and `performance` (when slight context needed). A5 typically domesticated or balanced. A6 typically off or minimal.
5. **Said Nursi exemplar.** Pop-translation Risale-i Nur paperback; brief publisher's note; 2-page glossary of the most-needed Sufi/kalam terms only.
6. **Edition-tradition exemplar.** Penguin Classics paperback (no analysis chapter; minimal front matter).

#### Level 3 — `standard`

1. **Stance.** Moderate separate-sections apparatus. Brief scholarly introduction; glossary of major terms; cross-references to other passages; brief exegetical-history footnotes on key concepts.
2. **Depth.** 2-4 content-types fire routinely (Introduction + Glossary + Cross-references + brief Exegetical-history).
3. **Operational substance.** Content-type-by-level table: Introduction (brief) + Glossary (major terms) + Cross-references (major passages) + Exegetical history (brief footnote on key polysemy) ACTIVE; other content-types BLOCKED. A7↔A8 boundary: A7 in-page; A8 separate-sections (LOCATION rule). Harmony-report-location: A6 standalone (no cross-references at A8=standard). Multi-meaning analysis: brief lexical note in glossary on key polysemy (no full exegetical paragraph).
4. **Cross-axis note.** A4 default for `devotional` (per A4 matrix). A5 typically balanced. A6 typically light to standard.
5. **Said Nursi exemplar.** Standard scholarly Risale-i Nur edition; brief introduction; glossary of major Sufi/kalam terms; cross-references to other Words/Letters; brief footnotes on key polysemous concepts (`din`, `nur`, `iman`).
6. **Edition-tradition exemplar.** Oxford World's Classics with brief introduction + select notes; Loeb Classical Library with introduction.

#### Level 4 — `deep`

1. **Stance.** Extensive separate-sections apparatus suitable for a Norton-Critical-style edition. Scholarly introduction; analysis chapter per major passage; extensive cross-references; exegetical-history paragraphs for key concepts; rhetorical analysis of structural elements; target-language-equivalent justification; theological commentary; historical-critical context.
2. **Depth.** 4-10 content-types fire per major passage; full apparatus channels open EXCEPT philological apparatus and cross-tradition references.
3. **Operational substance.** Content-type-by-level table: Introduction (scholarly) + Glossary (extensive) + Etymology (major terms) + Rhetorical analysis (per major passage) + Cross-references (extensive) + Exegetical history (paragraph per major polysemous concept) + Lexical-history (major terms) + Target-language-equivalent analysis (major translation choices) + Theological commentary (major concepts) + Historical-critical context (per major passage) ACTIVE EXTENSIVELY; Philological apparatus + Cross-tradition references BLOCKED. A7↔A8 boundary: in-page (A7) vs separate-sections (A8); LOCATION default tiebreaker. Harmony-report-location: A6 channel standalone with cross-references to A8 analysis chapters (and A8 sections cite harmony report). Multi-meaning analysis: exegetical-history paragraph per major polysemous concept in dedicated analysis section.
4. **Cross-axis note.** A4 default for `scholarly` (per A4 matrix). A5 typically foreignized or balanced. A6 typically standard to maximum.
5. **Said Nursi exemplar.** Norton-Critical-style Risale-i Nur edition; scholarly introduction; analysis chapter per major Word/Letter; extensive cross-references; exegetical-history paragraphs for key concepts (`din`, `nur`, `iman`, `nefs`); rhetorical analysis of nazm; target-language-equivalent justification for major translation choices; theological commentary; historical-critical context.
6. **Edition-tradition exemplar.** Norton Critical Edition (translation + extensive analysis chapter + criticism collection).

#### Level 5 — `scholarly`

1. **Stance.** Full critical apparatus edition. All 12 content-types fire as relevant. Comprehensive introduction; exhaustive glossary; etymology of every key term; rhetorical analysis per passage; full exegetical history; lexical-history; target-language-equivalent analysis; theological commentary; historical-critical context; philological apparatus; cross-tradition references.
2. **Depth.** All 12 content-types fire; full apparatus.
3. **Operational substance.** Content-type-by-level table: ALL 12 content-types ACTIVE with full apparatus density. A7↔A8 boundary: maximum-apparatus configuration in both channels at A7=scholarly + A8=scholarly. Harmony-report-location: A6 channel standalone with cross-references to A8 analysis sections (and A8 sections cite harmony report). Multi-meaning analysis: full exegetical-history apparatus per polysemous concept (commentary tradition + lexical-philological argument + cross-tradition references).
4. **Cross-axis note.** A4 default for `language-learning` (per A4 matrix; refinement note maps language-learning to `scholarly` cleanly — A4 verbiage `deep+scholarly` was ambiguous, now resolved). A5 typically foreignized. A6 typically standard to maximum.
5. **Said Nursi exemplar.** Full critical apparatus Risale-i Nur edition; comprehensive introduction (Said Nursi's life, intellectual context, Risale-i Nur project history); exhaustive glossary; etymology of every key term; rhetorical analysis per passage; exhaustive cross-references; full exegetical history per polysemous concept; lexical-history of target-language equivalents; full target-language-equivalent analysis; extensive theological commentary; full historical-critical apparatus; philological apparatus (manuscript variants if available); cross-tradition references (other Sufi/kalam authors).
6. **Edition-tradition exemplar.** SBL Greek NT critical apparatus edition; Robert Alter scholarly Hebrew Bible translation with apparatus; Brill critical edition; Cambridge Companion + Critical Edition.

### 3. Content-type-by-level table

This is A8's central operational substance — the structural analog to A7's action-permission table, but reflecting A8's content-PRODUCTION role rather than action-GATING role. The translator-AI consults this table at major-passage level to determine which content-types fire and at what density.

| Content-type | `none` | `surface` | `standard` | `deep` | `scholarly` |
|---|---|---|---|---|---|
| Introduction (front matter) | — | publisher's note | brief | scholarly | comprehensive |
| Glossary entries | — | major terms only | major terms | extensive | exhaustive |
| Etymology notes | — | — | — | major terms | every key term |
| Rhetorical analysis (nazm structure) | — | — | — | per major passage | per passage |
| Cross-references (intra-corpus) | — | — | major passages | extensive | exhaustive |
| Exegetical history (polysemy senses) | — | — | brief footnote | paragraph per major concept | full commentary tradition |
| Lexical-history (target-equiv drift) | — | — | — | major terms | every key term |
| Target-language-equivalent analysis | — | — | — | major translation choices | every translation choice |
| Theological/conceptual commentary | — | — | — | major concepts | extensive |
| Historical-critical context | — | — | — | per major passage | full |
| Philological apparatus | — | — | — | — | full |
| Cross-tradition references | — | — | — | — | full |

Reading: `—` = content-type BLOCKED at this level. At `none`: 0 content-types fire; at `surface`: 2 content-types fire minimally; at `standard`: 4 content-types fire routinely; at `deep`: 10 content-types fire extensively; at `scholarly`: all 12 content-types fire with full apparatus.

The 12 content-types cover the recognizable apparatus components of scholarly edition traditions. Distinctions matter operationally:
- **Etymology** = source-language word origins (Arabic-root analysis for Said Nursi).
- **Lexical-history** = target-language equivalent's semantic drift (how "religion" came to mean what it means in English; relevant when translating `din`).
- **Target-language-equivalent analysis** = WHY this English word was chosen over alternatives (translator's justification).
- **Exegetical history** = sense-tradition of polysemous concepts across commentary tradition (how the senses of `din` developed).

These are operationally different concerns even if conceptually adjacent.

### 4. A7↔A8 boundary spec

The A7↔A8 boundary is the most consequential cross-axis boundary in the framework. The spec uses three complementary framings, all of which apply simultaneously; LOCATION is the default tiebreaker at disagreement edge cases.

**Framing 1 — by LOCATION.**
- **A7 = in-page apparatus** — footnotes, glosses, transliterations with parenthetical paraphrase, brief in-line cultural-context flags. Lives on the reading page next to the source text.
- **A8 = separate-sections apparatus** — front matter (introduction, glossary), endnotes, appendix, sidebars, dedicated analysis chapters. Lives in distinct sections of the published edition.

**Framing 2 — by SCOPE.**
- **A7 = per-reference scaffolding** — addresses a specific word or phrase at a specific point in the text.
- **A8 = per-passage / per-corpus analysis** — addresses a full passage, a thematic concept across passages, or the source corpus as a whole (introduction, cross-references, exegetical history).

**Framing 3 — by AUDIENCE-INTERACTION.**
- **A7 = inline interruption** — reader looks down to the footnote/gloss, then back up to continue reading the same passage.
- **A8 = deferred study session** — reader reads the translation first (possibly with A7 in-page apparatus), then turns to separate analysis sections after completing the translation reading.

**LOCATION as default tiebreaker.** When the three framings disagree (e.g., a long footnote that scopes per-passage rather than per-reference), use LOCATION: if it lives on the reading page, it's A7; if it lives in a separate section, it's A8.

**Operational test for AI.** When producing content, ask: "does this belong on the reading page next to the source word (A7) or in a separate analysis section after the translation (A8)?" Worked examples:
- Footnote citing a single word's cultural meaning → A7.
- Multi-paragraph analysis of the passage's rhetorical structure → A8.
- Brief inline gloss of `nefs` → A7.
- Full essay on the development of the `nefs` concept across Sufi tradition → A8.
- Glossary entry for `din` noting "judgment / religion / truth" → A8 (lives in glossary section).
- Inline parenthetical `din [judgment / religion]` → A7 (lives on reading page next to source word).

**All 4×5 = 20 A7×A8 combinations valid.** No combination is structurally invalid. Notable patterns:
- A7=off + A8=none: maximally-clean pure-translation (oral recitation use case).
- A7=off + A8=scholarly: clean translation + heavy analysis section (e.g., Robert Alter Hebrew Bible with analysis behind the text).
- A7=scholarly + A8=surface: extensive in-page apparatus + clean post-translation (e.g., language-learning parallel-text with minimal separate analysis).
- A7=scholarly + A8=scholarly: maximum-apparatus configuration in both channels.

This spec resolves A7 finding's frontier flag (A7↔A8 cross-validation needed).

### 5. Harmony-report-location spec

A6 (Form Preservation) at Levels 3+ produces a **harmony report** — translator's meta-analytic commentary on what was preserved and what was sacrificed at the harmony level (Tier 1-4 from `harmony_layer.md`). The harmony report is a distinct apparatus channel from both A7's text-surface and A8's separate-sections analysis. The question: where does the harmony report live as A8 levels vary?

**Rule.** A6 harmony report stays in the A6 channel STANDALONE regardless of A8 level. At A8 = `deep` or `scholarly`, cross-references between channels are added.

Per-level behavior:
- A8 = `none` / `surface` / `standard`: A6 harmony report standalone in A6 channel; no cross-references.
- A8 = `deep`: A6 harmony report standalone; cross-references between channels (harmony report cites A8 analysis chapters; A8 sections cite harmony report for further detail).
- A8 = `scholarly`: A6 harmony report standalone; cross-references in both directions; A8 analysis sections may incorporate references to harmony report's tier-preservation tracking.

**Why this resolution.** Three alternative candidates were rejected:
- Migrate harmony report to A8 at high A8: erodes A6 finding's apparatus-channel-distinct commitment; conflates translator-perspective (harmony report) with reader-facing analysis (A8 content).
- Merge harmony report with A8 when both high: loses A6's meta-analytic identity; A6 content (Tier preservation tracking) differs from A8 content (rhetorical analysis / exegetical history); they overlap but aren't identical.
- Standalone always with no cross-references: fails reader navigation at high A8 where both apparatus exist.

The chosen rule preserves A6 finding's channel commitment (no modification needed) AND preserves A6↔A8 orthogonality (each axis owns its channel) AND enables reader navigation. This resolves A7 finding's harmony-report-location open question.

### 6. Multi-meaning analysis at A8

The always-on multi-meaning preservation policy fires when a polysemous source word permits multiple senses simultaneously per the local construction. The framework's three-layer treatment:

- **Policy invariant (WHETHER preserved):** the policy preserves both senses regardless of axis settings.
- **A7 controls HOW rendered in translation:** at the text surface — footnote / parenthetical / inline-paired / apparatus-edition render per A7 level.
- **A8 controls HOW analyzed in separate sections at high A8 levels:** exegetical-history of the sense-tradition; commentary tradition; lexical-philological argument.

A7 and A8 are complementary, not redundant. A7 makes the polysemy visible in the translation; A8 (at high levels) explains the sense-tradition in analysis. Per-level rule:

- A8 = `none`: no exegetical-history analysis (no separate sections at all).
- A8 = `surface`: no exegetical-history analysis (separate sections are introduction/glossary only).
- A8 = `standard`: brief lexical note in glossary on key polysemy (e.g., glossary entry for `din` noting "judgment / religion / truth"). No full exegetical paragraph.
- A8 = `deep`: exegetical-history paragraph per major polysemous concept in analysis section (e.g., dedicated paragraph tracing the `din` sense-tradition across Sufi commentary).
- A8 = `scholarly`: full exegetical-history apparatus (commentary tradition + lexical-philological argument + cross-tradition references; cite earlier exegetes; trace sense-tradition).

Multi-meaning POLICY invariant preserved across all configurations; A7 controls render; A8 controls analysis.

### 7. Cross-axis boundaries + A4 matrix cross-validation + DEPTH_PROFILE refinement

#### A5↔A8

A5 (Source Fidelity) sets the strategic stance modulating the KIND of analysis A8 produces, not its EXTENT or CHANNEL.

- A5 foreignized + A8 high: A8 emphasizes etymology (source-language word origins; root analysis), source-language semantic-drift, exegetical history rooted in source-tradition.
- A5 lightly-domesticated + A8 high: A8 emphasizes target-language-equivalent justification (why this English word was chosen), lexical-history of target-language equivalents, target-language reader-context.
- A5 balanced + A8 high: A8 balances source-rooted and target-rooted content-types.

A8's CHANNEL and EXTENT are independent of A5. Orthogonal.

#### A6↔A8

A6 (Form Preservation) determines harmony tier preservation and produces a harmony report at A6 Levels 3+. A8 controls separate-sections analysis on the reading-page-adjacent apparatus. The two apparatus exist in distinct channels:

- A6 harmony report = meta-analytic (translator's perspective on what was preserved at the harmony level).
- A8 separate-sections analysis = reader-facing (interpretive content for the reader: etymology, rhetorical analysis, exegetical history, etc.).

At high A8 (deep / scholarly), cross-references between channels. Orthogonal — each axis owns its channel.

#### A7↔A8

3-framing rule + LOCATION default tiebreaker. See Section 4.

#### A4 matrix cross-validation + refinement note

The A4 finding's matrix gave per-purpose A8 defaults. Mapping to A8's labels:

| A4 Purpose | A4 matrix A8 verbiage | A8 5-level mapping |
|---|---|---|
| scholarly | deep | `deep` |
| devotional | standard | `standard` |
| casual | surface | `surface` |
| language-learning | deep+scholarly | `scholarly` (refined; see below) |
| performance | surface | `surface` (or `none` for pure oral) |

**A4 finding refinement note.** A4's matrix used informal verbiage `deep+scholarly` for language-learning A8 default — ambiguous (does it mean deep OR scholarly OR both depending on context?). A8 resolves this cleanly: `scholarly` (full parallel-text apparatus edition is the natural language-learning default; "deep" is sufficient for many cases but "scholarly" is the canonical language-learning target). At next A4 maintenance pass, propagate: A4 matrix language-learning A8 → `scholarly`. This is parallel to A6's "moderate" → `light` refinement and A7's "moderate" → `standard` / "MAX rich" → `scholarly` refinements; should ride the same A4 maintenance pass.

#### DEPTH_PROFILE refinement

The `.env.example` `DEPTH_PROFILE` knob uses 4 values (`surface | standard | deep | scholarly`). A8 inheritance is validated WITH REFINEMENT:
- Preserve the 4 original DEPTH_PROFILE labels at positions 2-5 of the A8 axis (user recognizability from `.env.example` preserved).
- Add `none` at position 1 (explicit-zero case).
- At next `.env.example` maintenance pass, propagate: `DEPTH_PROFILE` should accept `none` (or document the historical default as `surface` for legacy compatibility while exposing `none` as the explicit-zero case).

This is downstream-implementation work (Next Actions MUST item). The substantive validation: DEPTH_PROFILE silently elided the `none` case because its origin was operational rather than architectural; at Layer 1 axis architecture, the `none` case deserves explicit representation.

## Inherited Commitments Re-test

The `_branch.md` declared a Synthesis Trigger naming six prior outputs (root + A7 + A6 + A5 + A4 + A1, plus A3 by reference). Re-test of each inherited commitment:

| # | Commitment | Source | Re-test status | Evidence |
|---|---|---|---|---|
| IC1 | A8 plain-ordinal | root | RE-TESTED OK | Pattern fits; no categorical / asymmetric / composite structure surfaces |
| IC2 | A8 4-level cardinality proposed | root | RE-TESTED & REVISED to 5 levels | Substantive validation surfaces `none` case (cross-axis pattern + A4 matrix performance default + DEPTH_PROFILE silent-elision); 5 levels with explicit `none` preserves the operational distinction |
| IC3 | A8 inherits from DEPTH_PROFILE knob | root | RE-TESTED & VALIDATED WITH REFINEMENT | 4 original labels preserved at positions 2-5; `none` added at position 1; .env.example update flagged for next maintenance pass |
| IC4 | A8 distinct from A7 (text-surface vs separate-sections) | root | RE-TESTED & EXPANDED to 3 framings | LOCATION + SCOPE + AUDIENCE-INTERACTION; LOCATION default tiebreaker; resolves A7 finding's frontier flag |
| IC5 | A8 distinct from A4 (why-reading vs how-much-commentary) | root | RE-TESTED OK | A4 = purpose; A8 = depth; distinct in mental model |
| IC6 | A4 per-purpose A8 defaults | A4 finding | RE-TESTED & CROSS-VALIDATED with refinement note | language-learning `deep+scholarly` → `scholarly` (resolves ambiguity) |
| IC7 | A7↔A8 cross-validation needed | A7 finding | RE-TESTED & RESOLVED | 3-framing rule + LOCATION default tiebreaker + worked examples |
| IC8 | Harmony report location across A8 levels (tentative: can live either way) | A7 finding | RE-TESTED & RESOLVED | A6 channel standalone regardless; cross-references at A8 deep / scholarly |
| IC9 | NEW translator-strategy 4-component template | A5+A6+A7 | RE-TESTED & ADAPTED | A8's template = analysis stance + per-level depth + content-type-by-level/boundary/harmony/multi-meaning + cross-axis interaction. 3rd component reworked from A7's action-permission to A8's content-type emphasis |
| IC10 | Receptive-only NOT APPLICABLE | A4+A5+A6+A7 | RE-TESTED OK | A8 is translator-strategy / user-configuration; not reader-property |
| IC11 | Chain default via A4 matrix | A5+A6+A7 | RE-TESTED & EXPANDED to dual-tier | A4 chain when A4 set; conservative-bias `standard` when A4 silent (cold-start defense) |
| IC12 | Language-agnostic at concept level | root + chain | RE-TESTED OK | Per-target-language analysis-content feasibility flagged as future inquiry; concept-level is language-agnostic |
| IC13 | DEPTH family 1/1 closure | root | RE-TESTED & DOCUMENTED | DEPTH family closes at 1/1 (smallest family) |
| IC14 | Framework closing at 8/8 | root | RE-TESTED & DOCUMENTED | UNIQUE meta-closure marker; unblocks downstream cascades (schema commit + default matrix synthesis + presets + policies + source-description + UX surface + framework-synthesis meta-inquiry) |

All 14 inherited commitments either re-tested OK, or refined with explicit reasoning, or specified into operational substance. No commitment carried forward without re-test.

## Next Actions

### MUST

- **What:** Commit `analysis_depth: Literal["none", "surface", "standard", "deep", "scholarly"]` to the schema.
  **Who:** schema-implementation step (file TBD — pending root schema-commit inquiry, now unblocked).
  **Gate:** observable — when the schema implementation step happens for the framework, A8 commits alongside all other axes.
  **Why:** Operationalizes A8 as a configurable axis the user can set and the AI can read.

- **What:** Encode the content-type-by-level table (60 cells; 12 content-types × 5 levels with per-cell density) in the translator-AI prompt context.
  **Who:** translator-AI prompt assembly step.
  **Gate:** observable — when the translator-AI is invoked with A8 as a context variable, the content-type-by-level table must be in the prompt.
  **Why:** Without this, the AI doesn't know which content-types fire at each level — the operational substance is lost.

- **What:** Encode the A7↔A8 boundary spec (3 framings + LOCATION default tiebreaker + operational test + worked examples) in the translator-AI prompt context.
  **Who:** translator-AI prompt assembly step.
  **Gate:** observable — when the AI produces apparatus content, the boundary spec must be available to determine A7 vs A8 channel placement.
  **Why:** Without this, channel-bleed risk (A8 content appearing in A7 channel and vice versa).

- **What:** Encode the harmony-report-location rule (standalone in A6 channel; cross-references at A8 deep / scholarly) in the translator-AI prompt context.
  **Who:** translator-AI prompt assembly step + apparatus-assembly logic.
  **Gate:** observable — when A6 Levels 3+ AND A8 deep+ are both active, the cross-reference machinery must engage.
  **Why:** Without this, apparatus structure differs from spec at high-axis-combination configurations.

- **What:** Encode the multi-meaning analysis at A8 rule (no analysis at A8=none/surface; brief glossary note at A8=standard; exegetical-history paragraph at A8=deep; full apparatus at A8=scholarly) in the translator-AI prompt context.
  **Who:** translator-AI prompt assembly step.
  **Gate:** observable — when polysemy policy fires AND A8 ≥ standard, the appropriate analysis level must engage in A8 channel.
  **Why:** Without this, the polysemy policy is incompletely operationalized at A8 layer.

- **What:** A4 finding maintenance pass — propagate language-learning A8 = `scholarly` refinement (not `deep+scholarly` ambiguous); bundle with A6 finding's parallel refinement note (`moderate` → `light`) and A7 finding's refinement notes (`moderate` → `standard`; `MAX rich` → `scholarly`).
  **Who:** A4 finding maintainer.
  **Gate:** time-bound — at the next A4 maintenance pass (preferably bundled with A6 + A7 refinement notes).
  **Why:** Keeps the A4 matrix internally consistent with the precise labels downstream axes settle. All three refinement notes (A6 + A7 + A8) should ride the same pass.

- **What:** `.env.example` `DEPTH_PROFILE` refinement — add `none` to the accepted values (or document historical default as `surface` for legacy compatibility while exposing `none` as the explicit-zero case).
  **Who:** `.env.example` maintainer.
  **Gate:** time-bound — at the next `.env.example` maintenance pass.
  **Why:** Aligns the operational env knob with the Layer 1 axis specification.

### COULD

- **What:** Run the framework-synthesis meta-inquiry — rolling up all 8 axis findings into a single canonical Layer 1 spec covering the complete framework. This would produce the canonical reference document for schema commit + presets + AI prompt assembly.
  **Who:** future meta-inquiry (`/MVLw "synthesize all 8 axes into canonical Layer 1 spec"` or equivalent).
  **Gate:** condition-bound — when all 8 axis findings are in place (now true after this finding).
  **Why:** Provides single-source-of-truth for the framework; consolidates 8 individual findings into a coherent canonical reference.

- **What:** Synthesize the per-purpose × per-axis default matrix (5 A4 purposes × 8 axes = 40-cell matrix) using the per-axis A4 cross-validation tables from each of A1-A8 finding.
  **Who:** future default-matrix-synthesis inquiry.
  **Gate:** condition-bound — after framework closure (now true).
  **Why:** Provides the AI prompt context with the per-purpose default for every axis; one of the inquiry-completion downstream-unblock items.

- **What:** Design Layer 1A UX preset catalog above the 8 axes (named scenarios like `casual-english-reader`, `scholarly-english-reader`, etc., each with all 8 axis values pre-populated).
  **Who:** future UX / presets inquiry.
  **Gate:** condition-bound — after schema commit + default matrix synthesis.
  **Why:** Primary UI for non-power users; root finding's deferred Layer 1A.

- **What:** Specify the operational behavior of each POLICY-layer rule (multi-meaning preservation; register-alternation preservation; polysemy resolution via local construction; nazm preservation; no-smoothing).
  **Who:** separate POLICY-layer inquiry (or 5 inquiries, one per policy).
  **Gate:** condition-bound — can run in parallel with above; framework closure unblocks.
  **Why:** The POLICY layer is enumerated in root finding but operational specs are needed for translator-AI deployment.

- **What:** Define the Layer 3 SOURCE-DESCRIPTION schema.
  **Who:** separate SOURCE-DESCRIPTION inquiry.
  **Gate:** condition-bound — can run in parallel.
  **Why:** Allows source properties to inform translation behavior.

- **What:** Add UX-layer config-time conflict surface (e.g., "A7=scholarly + A8=scholarly may produce overlapping apparatus; consider reducing one").
  **Who:** UX inquiry (future).
  **Gate:** condition-bound — when UX inquiry runs.
  **Why:** Additive to A8 spec; does not change A8 runtime semantics; improves user awareness at configuration time.

### DEFERRED

- **What:** Per-target-language analysis-content feasibility study (does scholarly apparatus differ per target language tradition — Western critical apparatus vs Eastern marginalia vs other?).
  **Gate:** condition-bound — when Comprehenslate adds second target language.
  **Why (if revived):** Allows A8=scholarly to specify language-appropriate apparatus style; otherwise stays Western-default.

- **What:** Polysemy policy operational spec (the always-on policy itself, not A7's render-control or A8's analysis role).
  **Gate:** condition-bound — when a dedicated POLICY inquiry is scoped (per root finding's commitment).
  **Why (if revived):** A7's render rules and A8's analysis rules both assume the polysemy policy fires under specified conditions; those conditions need their own inquiry.

- **What:** Runtime conflict resolution between axis values at the framework level (the now-complete 8-axis framework may produce conflicting axis combinations; UX surface + runtime resolution).
  **Gate:** condition-bound — after schema commit; when conflict-resolution inquiry runs.
  **Why (if revived):** Runtime determinism for axis-combination edge cases.

## Reasoning

### Why 5 levels with explicit `none` (substantive revision of root's 4)

Considered alternatives:

- **Root's 4 levels** `surface | standard | deep | scholarly` — would preserve DEPTH_PROFILE inheritance exactly. KILLED: collapses operationally-distinct cases. A4 matrix performance default `surface` and casual default `surface` operationally differ — performance wants ZERO apparatus (oral recitation; clean text); casual wants minimal-but-nonzero (Penguin-paperback brief intro + glossary). With 4 levels, both map to the same A8 level and the AI can't distinguish them. With 5 levels and explicit `none`, performance can default to `none` for pure oral recitation while casual stays at `surface` for minimal-paperback experience.
- **Cross-axis pattern check** — A6 has `off`; A7 has `off`; every other ordinal Strategy/Depth axis has an explicit-zero level for the "no feature" case. A8 should too.
- **6+ levels** — would over-stratify. KILLED: A4 matrix uses 4-5 distinct values; no use-case need for finer granularity.

The substantive revision is exactly what level-definition inquiries are for. Root's proposal was inherited from a `.env.example` knob; sensemaking's substantive validation surfaces the gap the knob silently elided.

### Why DEPTH_PROFILE labels preserved at positions 2-5 (no naming refactor)

Considered alternatives:

- **Refactor all 4 DEPTH_PROFILE labels** to a new vocabulary (e.g., `clean | brief | substantive | exhaustive` or similar) — KILLED: loses user-recognizability from `.env.example`; gratuitous change without semantic gain.
- **Keep DEPTH_PROFILE labels but rename `none` to something else** (e.g., `off`, `disabled`) — KILLED: `off` is A6/A7's vocabulary; A8 = `none` reads cleaner as "no separate-sections apparatus" (parallel to `none` in academic publishing). `off` would be acceptable but `none` is more natural in the apparatus-edition context.

Preserved labels at positions 2-5; added `none` at position 1.

### Why default `standard` via dual-tier (not single-tier A4 chain)

Considered alternatives:

- **Single-tier A4 chain** — A8 silent → A4 silent → A4 casual default → A4 matrix casual A8 = `surface` → A8 = `surface`. KILLED at framework-cold-start case: `surface` is operationally near-empty; sparse default would hurt cold-start user experience. The A4 chain works when A4 is set, but cold-start (no A4, no A8 set) needs more defense.
- **Single-tier conservative-bias `standard`** — always default to `standard` regardless of A4. KILLED: ignores the A4 matrix's per-purpose tuning. When the user sets A4 = `performance`, the A4 matrix's `surface` default should win; conservative-bias `standard` would over-supply for performance.
- **Dual-tier** — A4 chain when A4 set; conservative-bias when A4 silent. SURVIVED. Preserves both principles; calibrated to A8's unique cold-start sparseness.

### Why 3-framing A7↔A8 boundary (not LOCATION-only)

Considered alternatives:

- **LOCATION-only framing** — simpler. KILLED at edge cases: a long footnote feels like analysis-section content but lives in-page; a brief glossary-style note feels like A7 but lives in glossary section. LOCATION alone is ambiguous at these edges.
- **AI-judge-case-by-case** — let translator-AI decide without formal framings. KILLED: non-deterministic; A7↔A8 channel-bleed risk.
- **3 framings with LOCATION tiebreaker** — SURVIVED. Three converging tests reduce edge-case ambiguity; LOCATION tiebreaker handles disagreement deterministically.

### Why harmony-report stays in A6 channel (not migrate to A8 at high A8)

Considered alternatives:

- **Migrate to A8 at high A8** — consolidates apparatus. KILLED: erodes A6 finding's apparatus-channel-distinct commitment; conflates translator-perspective (harmony report) with reader-facing analysis (A8 content); requires A6 finding modification.
- **Merge when both A6 and A8 high** — deduplication. KILLED: A6 content (Tier preservation tracking, translator's perspective) and A8 content (rhetorical analysis, reader-facing interpretation) overlap but aren't identical; merging loses A6's identity.
- **Standalone always with no cross-references** — simplest. KILLED at high-A8 reader-navigation case: reader has both apparatus but no cross-pointers; suboptimal UX.
- **Standalone with cross-references at high A8** — SURVIVED. Preserves A6 channel; adds navigation when both apparatus exist.

### Why multi-meaning analysis at A8 (not A7-only)

Considered alternatives:

- **A7-only multi-meaning handling** — A7 controls the render at text surface; A8 stays neutral. KILLED: misses the natural A8 use case (scholarly editions DO produce exegetical-history of polysemous concepts; that's apparatus-content). A8 high levels SHOULD produce exegetical-history content; the policy invariant says preserve, A7 renders in translation, A8 analyzes in apparatus.
- **A7 + A8 multi-meaning concerns merged** — collapse the two. KILLED: A7 controls per-word render at text surface; A8 controls per-concept analysis in apparatus. Different operational scopes; merging loses the distinction.
- **A7 render + A8 analysis (three-layer treatment)** — SURVIVED. Policy invariant (WHETHER) + A7 render (HOW in translation) + A8 analysis (HOW in apparatus at high A8). Three layers; each layer has its own operational scope.

### Why A4 finding refinement note (resolving `deep+scholarly` ambiguity)

Considered alternatives:

- **Leave A4 verbiage as-is** (DO-NOTHING) — KILLED: ambiguity propagates downstream; pydantic dataclass commit would have to handle ambiguous string; AI prompt context would have ambiguous level.
- **Refine to `deep`** — KILLED: language-learning canonically needs full parallel-text apparatus (SBL Greek NT / Robert Alter style); `scholarly` is the canonical target.
- **Refine to `scholarly`** — SURVIVED. Canonical language-learning target is full apparatus edition.

### Why FRAMEWORK CLOSURE marker (not just family-closure)

Considered alternatives:

- **Just-another-family-closure** — A8 closes Depth at 1/1 the way A3 closed Reader, A4 closed Purpose, A7 closed Strategy. KILLED at meta-level: A8 closes the WHOLE Layer 1 framework, not just a family. The FRAMEWORK closure marker UNBLOCKS schema commit + per-purpose × per-axis default matrix synthesis + framework-synthesis meta-inquiry. Treating A8 as just-another-family-closure under-articulates the unblock-event.
- **No special closure marker** — terse but loses structural signaling. KILLED: the unblock-event is substantive (Next Actions MUST and COULD items depend on it).

The FRAMEWORK CLOSURE marker is the unique meta-marker only A8 carries.

### Cross-domain illustrations DEFERRED

- **Academic publishing apparatus tiers** (peer-reviewed journal vs textbook vs popular trade) — DEFERRED. Cross-domain illustration with parallel scaffolding spectrum; useful for analogical reasoning but not load-bearing for A8 spec.
- **Software documentation tiers** (no docs / README / API reference / tutorials / full developer guide + design docs + ADRs) — DEFERRED. Same status.

### Research frontiers

- **AI-runtime adaptive analysis depth** — RESEARCH FRONTIER. AI infers reader-need + adjusts A8 dynamically per passage rather than applying a fixed level uniformly. Long-horizon; depends on LLM capability development. Out of scope for A8 spec.
- **Framework-synthesis meta-inquiry** — RESEARCH FRONTIER (immediate successor, not long-horizon). Recorded as Next Actions COULD. Rolls up all 8 axis findings into single canonical Layer 1 spec. Itself a future inquiry; A8 doesn't gate it as required.

## Open Questions

### Monitoring

- Observable after first translations run: do the per-passage content-type-density thresholds hold across real Said Nursi material, or do passages systematically over- or under-shoot the per-level guidance?
- Observable after framework-synthesis meta-inquiry runs: does the canonical Layer 1 spec require any A8 finding adjustment, or does A8 finding survive synthesis intact?
- Observable after schema commit: does the `analysis_depth` enum + `none` addition surface any downstream implementation issues?

### Blocked

- Polysemy policy operational spec — A8's multi-meaning analysis rule assumes the polysemy policy fires under specified conditions; those conditions need their own dedicated POLICY inquiry per root commitment.
- Layer 1A UX preset catalog — depends on schema commit + default matrix synthesis being complete.

### Research Frontiers

- AI-runtime adaptive analysis depth (AI infers reader-need + adjusts A8 dynamically per passage). Long-horizon; out of scope for A8 spec.
- Per-target-language analysis-content feasibility (does scholarly apparatus differ per target language tradition?). Future inquiry when second target language is added.

### Refinement Triggers

- If real translations reveal the per-passage content-type-density thresholds are systematically wrong, revise without changing the qualitative orientation.
- If the harmony-report cross-reference machinery at high A8 proves cumbersome (readers don't use cross-references; channels confuse), revisit the rule.
- If the dual-tier default `standard` consistently over- or under-shoots cold-start, revise toward typical-use bias as feedback accumulates.
- When a second target language is added, revisit per-target-language analysis-content feasibility.
- When the framework-synthesis meta-inquiry runs, revisit A8 finding for alignment with the canonical spec.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
lets dive deep into A8 — Analysis Depth in devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md

(reread it first)
```

</details>
