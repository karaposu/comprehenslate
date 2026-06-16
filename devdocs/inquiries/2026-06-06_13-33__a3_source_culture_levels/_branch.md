# Branch: a3_source_culture_levels

## Question

**Context.** The root architectural finding `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` (settled the 4-layer / 4-family / 8-axis configuration framework for Comprehenslate) established A3 — Source Culture as the third axis in the Reader family. Per the root, A3's concept is "the reader's IDENTITY-BASED proximity to the source's cultural milieu"; it answers "Does this reader come from inside the source's culture, or from outside?"; it controls "how many cultural references need explanation, transliteration choices for proper names, etc."; and it is **explicitly distinguished from A1's cultural-reference-recognition sub-field** (A1's sub-field is COMPETENCE-based — does the reader know the references?; A3 is IDENTITY-based — does the reader live inside the source's culture?). The root proposed 3 ordinal levels (`outsider / familiar / source-native`) but explicitly deferred level-value finalization to "the next inquiry."

The Reader family now has 2 of 3 axes fully specified: A1 Reader Level (5 sub-fields × 5 levels each, completed in the A1 chain ending with `a1_cultural_reference_recognition_levels/finding.md`) and A2 Domain Expertise (5 levels `lay | aware | educated | trained | expert`, completed in `a2_domain_expertise_levels/finding.md`). This inquiry takes the same shape applied to A3.

A3 differs structurally from A1 and A2 in two ways:
1. A3 is **identity-based**, not competence-based. Identity has natural discrete categories (born into a culture vs not; raised in it vs not) that may not stratify into 5 ordinal levels the way competence does.
2. The root finding proposed 3 levels for A3 (vs A2 which it also proposed 3 for and the user later directed to refine to 5).

The user did NOT explicitly direct A3's cardinality (unlike A2 where they explicitly said "should be 5 levels"). So the cardinality question — should A3 be 3 (per root) or 5 (per pattern across A1 sub-fields and A2) or some other count — is itself an OPEN question for this inquiry to settle on substantive grounds.

State the question:
- **Subject:** A3 — Source Culture level definitions.
- **Action:** Decide level cardinality (3 per root vs 5 per pattern vs other), then define each level with concept + distinguishing logic + examples + operational definition usable as translator-AI prompt context.
- **Level:** Axis-level (one axis, plain-ordinal per the root architecture; not composite-axis like A1).
- **Observation targets** (multiple, preserved separately):
  1. The level CARDINALITY decision (3 vs 5 vs other) — substantive grounds for the count, not just consistency with neighbors.
  2. The level NAMES (labels open; should be identity-meaningful).
  3. The CONCEPT each level captures (one sentence per level: what identity-based proximity to the source's cultural milieu the reader has).
  4. The distinguishing LOGIC between adjacent levels (what specifically separates outsider from familiar; familiar from source-native; what intermediate levels mean if cardinality > 3).
  5. CONCRETE EXAMPLES per level spread across multiple source cultures (Turkish-Ottoman-Islamic for the project's Said Nursi corpus; Hebrew biblical; Greek classical; Hindu Sanskrit; Chinese Confucian; etc.) so the level identity travels across source cultures.
  6. The OPERATIONAL DEFINITION usable as translator-AI prompt context: what cultural-context handling the AI does per level (transliteration choices for proper names; cultural-context flagging; assumption-of-shared-cultural-knowledge calibration).
  7. The A3 DEFINITION TEMPLATE (does the 4-component template from A1 sub-fields / A2 adapt, or does A3 need its own template? The dimension is IDENTITY, not capacity).
  8. The DOMAIN-SCOPE question (parallel to A2's): does A3 specify proximity to one specific source culture (the source's culture) or a profile across multiple cultures?
  9. The A3↔A1 BOUNDARY: A3 vs A1's cultural-reference-recognition (identity vs competence). The root finding's four-corners test passes for this — but make it explicit and operational.
  10. The A3↔A2 BOUNDARY: A3 (identity in source's CULTURE) vs A2 (competence in source's DOMAIN). The Said Nursi corpus has both a SOURCE CULTURE (Turkish-Ottoman-Naqshbandi-Khalidi-Islamic) and a SOURCE DOMAIN (Islamic theology / Risale-i Nur subfield) — A3 and A2 stratify different things.
  11. The A3 IDENTITY DIMENSION decision: what specifically is being measured? Birth in the source culture? Lived years in it? Linguistic native-ness in source language? Religious identity (for religious-text sources)? Familial heritage? A combination?
  12. The diaspora / convert / long-resident edge cases: how does A3 handle (a) a second-generation diaspora reader (born in target culture but raised by source-culture parents)? (b) a convert who grew up outside the religion but spent decades inside? (c) a non-native-language spouse who has lived in the source country for 30 years? These are real configurations and the level framework must accommodate them.

- **Deliverable shape:** N named ordinal levels (where N is decided in the inquiry) with per-level definition + distinguishing logic + 3-5 concrete examples spread across multiple source cultures; operational specification for translator-AI prompt context; A3 definition template (adapted from A1/A2 if applicable, or new); explicit A3↔A1 and A3↔A2 boundary statements; domain-scope decision; identity-dimension decision; diaspora/convert/long-resident edge-case handling.

**State the question:** **For A3 — Source Culture (the third axis in the Reader family per the root architectural finding), what should the level cardinality be (3 per root proposal vs 5 per the A1+A2 pattern, on substantive grounds), what should each level's name and concept be, what logic distinguishes each level from its neighbors, what concrete examples spread across multiple source cultures (Turkish-Ottoman-Islamic / Hebrew biblical / Greek classical / Hindu Sanskrit / Chinese Confucian / etc.) make each level operationally identifiable, defined language-agnostically at the concept level — AND resolving the A3↔A1 boundary (identity vs competence), the A3↔A2 boundary (cultural identity vs domain expertise), the IDENTITY-DIMENSION decision (what specifically is being measured: birth, lived years, language, religion, heritage, or combination), the domain-scope question (single source culture vs profile), and the diaspora/convert/long-resident edge cases?**

## Goal

- **Criterion.** N (3 or 5 or other) mutually distinct, ordinally meaningful, spectrum-covering levels for A3 Source Culture — each operationalizable as a translator-AI prompt instruction (so the AI knows when to keep transliterations vs Anglicize names; when to assume shared cultural knowledge; when to flag cultural context; how much to bridge cultural distance vs preserve cultural specificity). Each level needs an EXPLICIT definition (the cardinality decision must be principled, not default).

- **Use case.** The user will commit these as the `source_culture: Literal[...]` enum values; the per-level prose becomes part of the translator-AI's prompt context; the boundaries guide the AI in deciding cultural-context handling per level.

- **Desired outcome.** A stable, named, defined set of N A3 Source Culture levels with definition + distinguishing logic + 3-5 concrete examples per level spread across multiple source cultures; A3↔A1 and A3↔A2 boundary statements; domain-scope decision; identity-dimension decision; ready for the user to commit to the schema and complete the Reader family (3 of 3 axes specified).

- **What would fail.**
  - Forcing cardinality to 5 just to match A2 without substantive justification (or forcing 3 just to match the root proposal without reconsideration).
  - Levels defined only by example without explicit distinguishing logic.
  - Levels that overlap.
  - Levels that aren't ordinal (mixing categorical identity types alongside ordinal proximity depth).
  - Identity-dimension decision left ambiguous (the inquiry must commit on whether A3 measures birth, lived years, language, religion, heritage, or a combination).
  - Examples that lock to one source culture (Said Nursi / Islamic only); must span multiple source cultures.
  - Conflating A3 with A1's cultural-reference-recognition (identity vs competence).
  - Conflating A3 with A2 Domain Expertise (cultural identity vs domain knowledge).
  - Failure to handle the diaspora / convert / long-resident edge cases explicitly.
  - Failure to address the domain-scope question.
  - Examples drawn only from Western canon, missing the project's primary corpus (Said Nursi → Turkish-Ottoman-Islamic).

## Source Input

```text
now lets do it for A3 Source Culture in devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md
```

## Scope Check

Question covers goal: YES.

The Question targets the cardinality decision (open question, not pre-determined) + level definitions + cross-cultural examples + identity-dimension decision + A3↔A1 and A3↔A2 boundaries + domain-scope + edge-case handling. The Goal asks for all of those plus operationalizability and scope discipline.

**Specific-vs-pattern check.** User said "now lets do it for A3 Source Culture" — apply the broader pattern of "define the levels for this axis" to the specific axis A3. The scope is the broader PATTERN of A3 Source Culture across multiple source cultures (Turkish-Ottoman-Islamic / Hebrew biblical / Greek classical / etc.), not a single source-culture anchor case.

**Cardinality openness.** Unlike A2 where the user explicitly directed 5 levels, the user did NOT specify cardinality for A3. This inquiry must decide on substantive grounds whether 3 (per root proposal) or 5 (per A1+A2 pattern) or some other count fits A3's identity-based dimension best.

**Decoupling from prior chain commitments.** The root finding's A3 commitments (plain-ordinal pattern, scope, boundaries vs A1 and A2) are inherited and re-tested. The A1 chain + A2 inquiry commitments (receptive-only, conservative-bias-LOWER, language-agnostic, 4-component template adapts as needed) are inherited and re-tested for applicability to A3.

**Template-adaptation in scope.** Whether the 4-component template (reader profile + tier-component + register-component + handling-test) applies to A3 is an open question for sensemaking. A3's identity-based dimension may need different template adaptation than A1's frequency/canonicity dimensions or A2's expertise-depth dimension.

## Synthesis Trigger

This inquiry consolidates / synthesizes commitments from at least 2 prior inquiry outputs (triggers Synthesis Trigger per MVLw protocol):

- `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — root architectural finding. Commits to: A3's concept (identity-based proximity to source's cultural milieu); A3's plain-ordinal pattern (3 levels proposed, deferred to next inquiry); A3 boundary vs A1's cultural-reference-recognition (competence-based) — four-corners independence demonstrated in the root; A3 scope (cultural references needing explanation; transliteration choices); 8-axis architecture; conservative-bias-defaults principle.

- `devdocs/inquiries/2026-06-06_12-37__a2_domain_expertise_levels/finding.md` — the most recent sibling Reader-family axis (A2 specified with 5 levels). Commits to: receptive-only commitment; conservative-bias-LOWER default; language-agnostic-at-concept-level; 4-component MEDIUM-adapted template (reader profile + expertise-depth-tier + discourse-register-tier + domain-handling-test); single-domain default for domain-scope (parallel question for A3); cross-axis boundary statements (A2↔A1; A2↔A3); domain-meaningful labels (vs A1-consistency labels); 9 handling actions in 2 categories + 1 bridge; translator-AI runtime determination mechanism explicit.

- `devdocs/inquiries/2026-06-06_11-47__a1_cultural_reference_recognition_levels/finding.md` — the A1 chain's final sub-field, which most directly intersects with A3 conceptually (cultural-reference recognition is competence-based; A3 is identity-based). Commits to: 5 canonicity tiers + 5 handling actions (INLINE-GLOSS / FOOTNOTE / DOMESTICATE / KEEP-AS-IS / EXPLICATE-FUNCTION); DOMESTICATE-disfavored project policy (per user's translation-register-fidelity memory + Venuti foreignization); A1↔A2 boundary criterion forward-tagging 5 specialist canons to A2 (already received); reader-relative canon; canon-choice out-of-scope (audience-level config concern).

Inherited commitments to re-test (non-exhaustive; the finding's `## Inherited Commitments Re-test` section will enumerate fully):
- Receptive-only commitment.
- Conservative-bias-for-reader-axes = LOWER default.
- Language-agnostic at concept level (with cultural-specificity caveat parallel to canon-choice for A1 cultural-reference-recognition).
- A3 plain-ordinal pattern (no sub-fields).
- A3 cardinality (root proposed 3; this inquiry settles substantively).
- A3 boundary vs A1's cultural-reference-recognition (identity vs competence; four-corners independence).
- A3 boundary vs A2 Domain Expertise (cultural identity vs domain knowledge).
- A3 scope (cultural references; transliteration choices; cultural-context flagging).
- 4-component template adapts as needed.
- DOMESTICATE-disfavored project policy (from A1's cultural-reference-recognition; A3 may interact with this policy at cultural-context handling decisions — re-test).
- Translator-AI runtime determination mechanism (from A2 finding) — re-test for A3 applicability.
- Single-domain default analog (from A2 inquiry) — re-test for A3 (single source culture vs profile).

Sensemaking will adjudicate these commitments; Critique will re-test the adjudication. The discipline work will actually re-test these commitments, not merely record the inheritance.
