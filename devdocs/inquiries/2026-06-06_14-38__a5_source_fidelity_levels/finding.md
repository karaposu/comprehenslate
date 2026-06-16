---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md
---
# Finding: A5 — Source Fidelity (the 4 Asymmetric Levels)

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` (root architectural finding; established A5 as plain-ordinal Venuti-spectrum axis controlling lexical/idiomatic surface; proposed 3 symmetric levels deferred to a next inquiry).

**Revision trigger:** User directed: "now lets do it for a5 source fidelity." A5 is the first axis in the Strategy family, following the completion of Reader family (A1+A2+A3) and Purpose family (A4). The central substantive question this inquiry resolves: how does A5's user-configurable range interact with the cross-cutting DOMESTICATE-disfavored project policy established in `a1_cultural_reference_recognition_levels/finding.md`, extended through `a3_source_culture_levels/finding.md`, and confirmed cross-cutting in `a4_purpose_categories/finding.md`?

**What's preserved:**
- A5's identity as a plain-ordinal axis on the Venuti foreignization↔domestication spectrum (per root).
- A5's concept: the translator's strategic stance on lexical / idiomatic SURFACE choices.
- A5's scope: distinct from A6 Form Preservation (structural — rhythm, parallelism, word order as meaning).
- A5↔A6 four-corners orthogonality demonstrated in root.
- Venuti / Newmark / Nida theoretical anchors.
- DOMESTICATE-disfavored project policy lineage (A1 → A3 → A4 cross-cutting; user's translation-register-fidelity memory + Venuti foreignization).
- Language-agnostic at concept level.

**What's changed:**
- **A5 cardinality refined from 3 (root proposal) to 4** on substantive grounds. Three converging arguments: (1) policy constraint — symmetric 3 (`heavily-foreignized / balanced / heavily-domesticated`) lets the user opt out of the cross-cutting policy by selecting `heavily-domesticated`; symmetric 5 over-extends the conflict; (2) A4-matrix-implied granularity — A4's per-purpose A5 defaults use 3 distinct values plus a "balanced-to-foreignized" hyphenated value, implying an in-between level; (3) user-need spectrum — 4 distinct user needs are operationally distinguishable (devotional-max + scholarly + casual-balanced + light-domestication-for-accessibility); a 5th (heavy domestication) is policy-blocked.
- **A5 levels are ASYMMETRIC** — biased to foreignization with restricted domestication. The policy is embedded in axis structure (the `heavily-domesticated` level doesn't exist as a user-configurable option). Per-corpus policy override (for atypical corpora like children's adaptations) is deferred to a future inquiry.

**What's new:**
- **Labels validated and named:** `foreignized-max | foreignized | balanced | lightly-domesticated`. The 4-level set explicitly excludes `heavily-domesticated`.
- **NEW translator-strategy 4-component template.** The capacity-graded 4-component template from A1-A3 (reader profile + tier + register + handling-test) doesn't fit (A5 is translator-strategy not reader-property). The A4 categorical 4-component template (use-case profile + strategic implications + per-axis defaults + DOMESTICATE-emphasis) partially fits but A5 is ordinal not categorical. NEW template: (1) Strategic stance description; (2) Per-stance handling-action bias; (3) Foreignization-preservation emphasis; (4) Cross-axis interaction note.
- **A5 has NO own implementation actions.** A5 is a STRATEGIC STANCE that MODULATES which A1 cultural-reference-handling-actions and A3 cultural-handling-actions fire per encountered translation choice. A5's level determines preference order over A1 + A3 action vocabularies; A5 doesn't introduce parallel actions.
- **Default-when-A5-silent CHAINS THROUGH A4 matrix.** When A4 is set, A4's per-purpose matrix supplies A5 default. When A4 is silent → A4 defaults to `casual` → casual's A5 = `balanced`. Final A5 default = `balanced`. The categorical equivalent of conservative-bias-LOWER (per A4 IC7 reformulation) propagates through.
- **Receptive-only commitment DOES NOT APPLY to A5.** Parallel to A4 — A5 is translator-strategy / user-configuration choice, not a reader-property. Explicit non-inheritance.
- **Policy EMBEDDED in axis structure.** The DOMESTICATE-disfavored cross-cutting policy isn't a runtime check that can be overridden by setting `heavily-domesticated`; it's structurally embedded by the absence of that level in A5's user-facing range. Per-corpus override is the proper escape hatch.
- **Per-corpus policy override deferred** to a future inquiry. Some corpora (children's adaptations of classics; popular general-audience editions) may legitimately want heavy domestication.
- **A5↔A6 orthogonality re-validated.** Root's four-corners demonstration holds.
- **A5↔A1 boundary: strategy vs per-reference tactics.** A5 is the strategic stance; A1 cultural-reference-recognition's handling actions are per-reference tactics. The strategy modulates which tactics fire.
- **A5↔A4 cross-validated** with a minor refinement note for A4's language-learning A5 default (currently "balanced-to-foreignized" in A4 finding; should be `foreignized` against the 4-level A5 structure).
- **Strategy-family-opens marker.** A5 opens the Strategy family. After this inquiry: 5/8 axes complete (Reader 3/3 + Purpose 1/1 + Strategy 1/3).

**Migration:** No migration needed — first A5 specification. Schema commit: `source_fidelity: Literal["foreignized-max", "foreignized", "balanced", "lightly-domesticated"]`.

---

## Question

For A5 — Source Fidelity (the first axis in the Strategy family, plain-ordinal on the Venuti foreignization↔domestication spectrum at lexical/idiomatic surface, distinct from A6 structural Form Preservation), what should the cardinality and level values be — given that the cross-cutting DOMESTICATE-disfavored project policy (from A1 chain + A4) constrains the user-configurable range, requiring asymmetric design? What's the template, the action-modulation mechanism, the cross-axis cross-validation, and the Strategy-family-opens marker?

---

## Finding Summary

- **4 ordinal levels with asymmetric range:** `foreignized-max | foreignized | balanced | lightly-domesticated`. NO `heavily-domesticated` level. The cardinality is decided on substantive grounds (not by default).

- **Policy EMBEDDED in axis structure.** The DOMESTICATE-disfavored cross-cutting policy from the A1 chain + A4 isn't a runtime overlay — it's structurally embedded by the absence of `heavily-domesticated` from A5's range. The user CANNOT silently opt out by choosing a heavily-domesticated level; that level doesn't exist as a user-facing option. Per-corpus policy override (for atypical corpora) is deferred to a future inquiry.

- **NEW translator-strategy 4-component template.** Replaces both the A1-A3 capacity-graded template (reader-property-based) and the A4 categorical template (use-case-based) with: (1) Strategic stance description; (2) Per-stance handling-action bias; (3) Foreignization-preservation emphasis; (4) Cross-axis interaction note.

- **A5 has NO own implementation actions.** A5 is a STRATEGIC STANCE. A5 modulates which A1 cultural-reference-recognition handling actions and A3 cultural-handling actions fire at runtime. A5's level determines the preference order over A1's 5 actions and A3's 10 actions.

- **Default-when-A5-silent CHAINS THROUGH A4 matrix.** When A4 is set, A4 supplies A5 default. When A4 silent → A4 defaults to `casual` → casual's A5 = `balanced`. Final A5 default = `balanced`.

- **Receptive-only commitment DOES NOT APPLY to A5.** Parallel to A4. A5 is translator-strategy / user-configuration, not reader-property. Explicit non-inheritance.

- **A5↔A6 orthogonality.** A5 = lexical/idiomatic surface; A6 = structural form (rhythm, parallelism, nazm). Four-corners independence from root holds: heavily-foreignized + form-ignored (rare); heavily-foreignized + form-preserved (common scholarly); lightly-domesticated + form-ignored (common casual); lightly-domesticated + form-preserved (poetic translations).

- **A5↔A1 strategy-vs-tactics boundary.** A5 is strategic stance; A1's cultural-reference-handling-actions are per-reference tactics.

- **A5↔A4 cross-validated.** A4's per-purpose A5 defaults map to A5's 4 levels with a minor refinement note for A4's language-learning A5 default (should be `foreignized` rather than the A4-finding's "balanced-to-foreignized" hyphenated value).

- **Per-corpus policy override deferred.** Some corpora (children's adaptations; popular general-audience editions in fields where target-naturalization is standard) may legitimately want heavy domestication. The override mechanism is deferred to a future audience-level or corpus-level inquiry.

- **Strategy family opens with A5.** After this inquiry: 5/8 axes complete (Reader 3/3 + Purpose 1/1 + Strategy 1/3). Remaining in Strategy: A6 Form Preservation + A7 Scaffolding. Then A8 Depth family.

---

## Finding

The root architectural inquiry established A5 — Source Fidelity as the first axis in the Strategy family, on the Venuti foreignization↔domestication spectrum. The Reader family (A1+A2+A3) and Purpose family (A4) are fully specified. The central substantive question this inquiry resolves: A5 IS the axis on the foreignization-domestication spectrum, and the cross-cutting DOMESTICATE-disfavored project policy (from the A1 chain extended through A4) directly constrains A5's user-configurable range. The resolution: asymmetric range with the policy embedded structurally.

### 1. The Framework

#### 1.1 Why 4 levels asymmetric (not 3 symmetric per root)

The root proposed 3 symmetric levels: `heavily-foreignized / balanced / heavily-domesticated`. This inquiry refines to 4 asymmetric levels: `foreignized-max | foreignized | balanced | lightly-domesticated`.

Three converging arguments support the change:

**Policy constraint.** The DOMESTICATE-disfavored project policy is cross-cutting (per A1 chain + A4 confirmation). A symmetric range with `heavily-domesticated` lets the user opt out of the policy by selecting that level. The policy then becomes meaningless — a project commitment the user can simply ignore. Asymmetric range with the policy embedded structurally (by the absence of `heavily-domesticated`) makes the policy load-bearing.

**A4-matrix-implied granularity.** A4's per-purpose A5 defaults use 3 distinct values (`foreignized`, `foreignized-max`, `balanced`) PLUS a "balanced-to-foreignized" hyphenated value for language-learning. The hyphenated value implies a level between `balanced` and `foreignized` — i.e., the matrix already implies more than 3 levels on the foreignization side. The user can also override A5 per-axis. So A5 needs MORE values than just the 3 A4 directly uses.

**User-need spectrum.** Four distinct user needs are operationally distinguishable:
- Devotional max-emphasis: preserve liturgical specificity at maximum (Quran recitation; sacred-text liturgical use).
- Scholarly source-fidelity: preserve cultural specificity for study.
- Casual-balanced: foreignization-preserving alternatives at edges (INLINE-GLOSS + EXPLICATE-FUNCTION + TRANSLITERATE-WITH-GLOSS over DOMESTICATE).
- Light-domestication for accessibility: target-naturalization where source-fidelity isn't load-bearing (e.g., "Master" for "Üstad" in non-pedagogical conversational contexts; A4=casual + per-axis override).

A 5th level (heavy domestication) is policy-blocked. A 3rd level (collapsing the two foreignization tiers) under-distinguishes scholarly from devotional.

Settled cardinality: 4. Settled labels: `foreignized-max | foreignized | balanced | lightly-domesticated`.

#### 1.2 Asymmetric range with policy embedded

The 4 levels are biased toward foreignization. Two foreignization-side levels (`foreignized-max` and `foreignized`) cover the source-fidelity spectrum at different intensities. The `balanced` level uses foreignization-preserving alternatives at edges. The `lightly-domesticated` level permits target-naturalization in narrow cases where source-fidelity isn't load-bearing.

There is NO `heavily-domesticated` level. The omission is the policy-tension resolution. The DOMESTICATE-disfavored cross-cutting policy is structurally embedded by this absence — the user cannot silently opt out by choosing a heavily-domesticated level because that level doesn't exist as a user-facing option.

To override the policy for atypical corpora (children's adaptations of classics; popular general-audience editions in fields where target-naturalization is standard), a future per-corpus or audience-level policy-override mechanism would be needed. This is deferred to a future inquiry. At normal use, A5's 4 levels respect the policy.

#### 1.3 NEW translator-strategy 4-component template

The 4-component templates from prior inquiries don't fit A5:

- The A1-A3 capacity-graded template (reader profile + frequency/canonicity/expertise-depth tier + register-tier + handling-test) is reader-property-based. A5 is translator-strategy, not reader-property.
- The A4 categorical 4-component template (use-case profile + strategic implications + per-axis default mappings + DOMESTICATE-emphasis) is categorical. A5 is ordinal.

NEW translator-strategy 4-component template:
1. **Strategic stance description** — what the AI's overall stance is at this level (preserve everything? balance? lightly naturalize?).
2. **Per-stance handling-action bias** — which A1 cultural-reference-handling-actions and A3 cultural-handling-actions are preferred at this level.
3. **Foreignization-preservation emphasis** — where on the foreignization-domestication spectrum this level sits.
4. **Cross-axis interaction note** — which A4 purposes default to this level + A6 orthogonality reminder.

The 4-component count preserves structural parity with prior templates; the composition adapts to A5's translator-strategy ordinal nature.

#### 1.4 A5 has NO own implementation actions

A5 is a STRATEGIC STANCE. It does not introduce a new vocabulary of handling actions parallel to A1's 5 actions or A3's 10 actions in 4 categories. Instead, A5 MODULATES which A1/A3 actions are preferred per encountered translation choice.

This is operationally important:
- A1 cultural-reference-recognition's actions (INLINE-GLOSS / FOOTNOTE / DOMESTICATE / KEEP-AS-IS / EXPLICATE-FUNCTION) are per-reference TACTICS.
- A3 source-culture's actions (TRANSLITERATE-FULLY / TRANSLITERATE-WITH-GLOSS / TARGET-LANGUAGE-EQUIVALENT / ASSUME-SHARED-CULTURAL-KNOWLEDGE / FLAG-CULTURAL-CONTEXT / BRIDGE-CULTURAL-DISTANCE / PRESERVE-CULTURAL-SPECIFICITY / DOMESTICATE-CULTURAL-FRAME / KEEP-HONORIFICS-SOURCE / ANGLICIZE-HONORIFICS) are per-cultural-item TACTICS.
- A5's level determines the PREFERENCE ORDER over these tactics. At `foreignized-max`, KEEP-AS-IS + TRANSLITERATE-FULLY + KEEP-HONORIFICS-SOURCE + PRESERVE-CULTURAL-SPECIFICITY are heavily preferred. At `lightly-domesticated`, TARGET-LANGUAGE-EQUIVALENT + ANGLICIZE-HONORIFICS become permissible in narrow cases (though still disfavored under cross-cutting policy).

The full A5 → A1/A3 action modulation table is in Section 3.

#### 1.5 Default-when-A5-silent: chain through A4 matrix

A5's default-when-silent inherits from A4's per-purpose matrix. The chain:
1. When A4 is set: A4's matrix supplies A5 default per purpose (scholarly → `foreignized`; devotional → `foreignized-max`; casual → `balanced`; language-learning → `foreignized` [refined from A4-finding's "balanced-to-foreignized"]; performance → `balanced`).
2. When A4 is silent: A4 defaults to `casual` per the A4 finding's default-when-A4-silent commitment. Casual's A5 default = `balanced`.
3. Final A5 default = `balanced`.

This chain inheritance is the CATEGORICAL EQUIVALENT of conservative-bias-LOWER (the A1-A3 ordinal default-when-silent principle) propagating through A4's categorical defaults principle. The A1-A3 chain's conservative-bias-LOWER is the underlying principle; A4 reformulated it as "default-when-A4-silent = casual"; A5 inherits it via A4's matrix → balanced.

#### 1.6 Receptive-only commitment DOES NOT APPLY to A5

The A1-A3 chain's receptive-only commitment (the reader RECOGNIZES content; doesn't produce) DOES NOT APPLY to A5. Parallel to A4 — A5 is a translator-strategy / user-configuration choice, not a reader property. Different ontological category.

This explicit non-inheritance is important for the same reason as A4's non-inheritance: the A1-A3 chain's commitments form a Reader-family lineage; A4 and A5 are non-Reader-family axes with different foundational principles.

#### 1.7 Strategy family opens with A5

A5 is the first axis in the Strategy family per root. After this inquiry: 5/8 axes complete (Reader 3/3 + Purpose 1/1 + Strategy 1/3). Remaining: A6 Form Preservation + A7 Scaffolding in the Strategy family; A8 Analysis Depth in the Depth family.

### 2. The 4 Per-Level Definitions

Each level has the 4 components (strategic stance + handling-action bias + foreignization-preservation emphasis + cross-axis interaction).

#### 2.1 `foreignized-max`

**Strategic stance.** Maximum source-fidelity. Preserve everything source-cultural: transliterations, honorifics, cultural references, source-language phrases. The reader encounters the source culture in its specificity. Domestication is structurally absent at this level.

**Per-stance handling-action bias.** A1: KEEP-AS-IS prioritized for transparent references; EXPLICATE-FUNCTION for opaque-but-load-bearing; FOOTNOTE for context. INLINE-GLOSS minimal; DOMESTICATE never. A3: TRANSLITERATE-FULLY; KEEP-HONORIFICS-SOURCE; PRESERVE-CULTURAL-SPECIFICITY at maximum; ASSUME-SHARED-CULTURAL-KNOWLEDGE when reader is source-native. TARGET-LANGUAGE-EQUIVALENT / DOMESTICATE-CULTURAL-FRAME / ANGLICIZE-HONORIFICS strictly avoided.

**Foreignization-preservation emphasis.** Maximum.

**Cross-axis interaction.** A4 default match: `devotional` (matrix). A6 orthogonality: typically pairs with high A6 (preserve nazm + structural form) but doesn't require it — a `foreignized-max` lexical stance can coexist with low A6 form preservation (rare but possible — preserve the foreign vocabulary while flattening the rhythm).

**Said Nursi anchor.** Risale-i Nur devotional reading for source-culture-fluent reader (A3=source-native). All Sufi honorifics + theological terms preserved; Sufi practice references untranslated; reader brings the cultural fluency.

**Cross-cultural example.** Quran recitation translation; SBL Greek NT scholar-edition; Tanakh Jewish Publication Society edition.

#### 2.2 `foreignized`

**Strategic stance.** Strong source-fidelity. Preserve source-cultural specificity but provide light support (inline glosses, brief footnotes) where reader needs it. The reader does encounter the source culture but with translator help at the edges.

**Per-stance handling-action bias.** A1: INLINE-GLOSS for moderate-difficulty references; EXPLICATE-FUNCTION for opaque-with-explanation-needed; KEEP-AS-IS where reader can catch it. FOOTNOTE for scholarly context. DOMESTICATE explicitly avoided. A3: TRANSLITERATE-FULLY for established terms; TRANSLITERATE-WITH-GLOSS for less-established; KEEP-HONORIFICS-SOURCE; PRESERVE-CULTURAL-SPECIFICITY; FLAG-CULTURAL-CONTEXT briefly where reader benefits.

**Foreignization-preservation emphasis.** High.

**Cross-axis interaction.** A4 default match: `scholarly` and `language-learning` (matrix). A6 orthogonality: typically pairs with high A6 for scholarly use but independent.

**Said Nursi anchor.** Academic Islamic-studies edition of Risale-i Nur with footnotes. Nursi-specific terminology kept; Sufi context briefly explained where reader benefits.

**Cross-cultural example.** Norton Critical Edition of Plato; NRSV biblical edition; M.A.S. Abdel Haleem Quran translation with light apparatus.

#### 2.3 `balanced`

**Strategic stance.** Balance source-fidelity with accessibility. Where source-cultural specificity is load-bearing, preserve with explication. Where not, accept brief foreignization-preserving alternatives (INLINE-GLOSS / EXPLICATE-FUNCTION) for reader comfort. The reader engages source culture in approachable form.

**Per-stance handling-action bias.** A1: INLINE-GLOSS as primary mode; EXPLICATE-FUNCTION for compressed-meaning references; FOOTNOTE selectively for added context. KEEP-AS-IS for transparent + culturally-ubiquitous references. DOMESTICATE still avoided (foreignization-preserving alternatives preferred). A3: TRANSLITERATE-WITH-GLOSS as primary; FLAG-CULTURAL-CONTEXT where reader needs framing; KEEP-HONORIFICS-SOURCE for established source honorifics; BRIDGE-CULTURAL-DISTANCE for broader cultural assumptions.

**Foreignization-preservation emphasis.** Balanced (foreignization-preserving alternatives over DOMESTICATE).

**Cross-axis interaction.** A4 default match: `casual` and `performance` (matrix). A6 orthogonality: typically pairs with moderate A6 form but independent — performance pairs `balanced` A5 with MAXIMUM A6 (cadence preservation).

**Said Nursi anchor.** Penguin-Classics-style edition for general curious reader. Nursi terms glossed in-line on first use; Sufi assumptions briefly framed; reader can follow.

**Cross-cultural example.** Penguin Classics edition of Plato; NIV biblical edition; Penguin Quran (e.g., Tarif Khalidi translation).

#### 2.4 `lightly-domesticated`

**Strategic stance.** Light target-naturalization where source-cultural specificity isn't load-bearing. Source-language honorifics may be selectively anglicized; cultural references may be selectively replaced with target-culture equivalents. The reader engages a more accessible text but with preserved cultural-specificity at load-bearing points.

**Per-stance handling-action bias.** A1: INLINE-GLOSS still preferred for load-bearing references; DOMESTICATE permissible in narrow cases (non-load-bearing cultural references where target-natural reads better and source-otherness doesn't serve the reader). PARAPHRASE-IN-LAYMAN-TERMS becomes more permissible. A3: TARGET-LANGUAGE-EQUIVALENT permissible for proper-noun handling in narrow cases (less common Sufi figures; less-recognized historical figures); ANGLICIZE-HONORIFICS selectively permissible. PRESERVE-CULTURAL-SPECIFICITY still expected for load-bearing points; DOMESTICATE-CULTURAL-FRAME still disfavored but permissible at this level when the cultural frame isn't pedagogically central.

**Foreignization-preservation emphasis.** Light (with policy still disfavoring full DOMESTICATE).

**Cross-axis interaction.** A4 default match: no purpose defaults to `lightly-domesticated` in the A4 matrix (the closest is `casual` defaulting to `balanced`). User would set A5 = `lightly-domesticated` as a per-axis override when more accessibility is wanted than `balanced` provides.

**Said Nursi anchor.** A popular paperback edition of Risale-i Nur for the broadest possible general audience — convert exploring Islam casually; non-Muslim curious reader. Less central Sufi honorifics may be anglicized; cultural assumptions more heavily explicated; load-bearing terms (Allah, Quran, key theological concepts) preserved with light gloss.

**Cross-cultural example.** A trade-paperback edition of a classical text for mass-market reading; popular Penguin "Gateway" series introductory editions.

### 3. A5 → A1/A3 Action Modulation Table

A5 has no own actions. A5 modulates the A1 + A3 action vocabularies. This table specifies per-level preference order.

#### 3.1 A5 → A1 cultural-reference-recognition actions (5 actions)

| A5 Level | Preferred Actions (in order) | Avoided |
|---|---|---|
| `foreignized-max` | KEEP-AS-IS → EXPLICATE-FUNCTION → FOOTNOTE | INLINE-GLOSS minimal; DOMESTICATE never |
| `foreignized` | INLINE-GLOSS → EXPLICATE-FUNCTION → KEEP-AS-IS → FOOTNOTE | DOMESTICATE avoided |
| `balanced` | INLINE-GLOSS → EXPLICATE-FUNCTION → FOOTNOTE → KEEP-AS-IS | DOMESTICATE still avoided (project policy) |
| `lightly-domesticated` | INLINE-GLOSS → EXPLICATE-FUNCTION → PARAPHRASE-IN-LAYMAN-TERMS → FOOTNOTE → DOMESTICATE (permissible in narrow cases) | — |

#### 3.2 A5 → A3 source-culture actions (10 actions in 4 categories)

| A5 Level | Proper-Noun Handling | Cultural-Context | Honorific | Strategic |
|---|---|---|---|---|
| `foreignized-max` | TRANSLITERATE-FULLY | ASSUME-SHARED-CULTURAL-KNOWLEDGE | KEEP-HONORIFICS-SOURCE | PRESERVE-CULTURAL-SPECIFICITY (max) |
| `foreignized` | TRANSLITERATE-FULLY / WITH-GLOSS | FLAG-CULTURAL-CONTEXT briefly | KEEP-HONORIFICS-SOURCE | PRESERVE-CULTURAL-SPECIFICITY |
| `balanced` | TRANSLITERATE-WITH-GLOSS | FLAG-CULTURAL-CONTEXT / BRIDGE-CULTURAL-DISTANCE | KEEP-HONORIFICS-SOURCE | PRESERVE-CULTURAL-SPECIFICITY |
| `lightly-domesticated` | TRANSLITERATE-WITH-GLOSS / TARGET-LANGUAGE-EQUIVALENT (narrow cases) | BRIDGE-CULTURAL-DISTANCE | KEEP-HONORIFICS-SOURCE / ANGLICIZE-HONORIFICS (selective) | PRESERVE-CULTURAL-SPECIFICITY at load-bearing points; DOMESTICATE-CULTURAL-FRAME selectively permissible |

The pattern across both tables: DOMESTICATE / TARGET-LANGUAGE-EQUIVALENT / ANGLICIZE-HONORIFICS become PERMISSIBLE only at `lightly-domesticated` and even there are selective (not default). The project policy carries through all levels via the absence of `heavily-domesticated` as a level.

### 4. Cross-Axis Boundaries

#### 4.1 A5 ↔ A6 (lexical surface vs structural form)

**Criterion.** A5 controls lexical / idiomatic SURFACE choices (word selection, phrase translation, idiomatic substitution). A6 controls structural FORM (rhythm, parallelism, ring composition, word order as meaning — the project corpus's nazm). Distinct dimensions.

**Four-corners independence (per root demonstration):**
- `foreignized-max` + low A6: rare but possible — preserve foreign vocabulary while flattening the rhythm (a translator who prioritizes lexical fidelity but doesn't try to mirror source rhythm).
- `foreignized-max` + high A6: common scholarly — preserve both vocabulary and rhythm.
- `lightly-domesticated` + low A6: common casual — anglicize vocabulary and flatten the rhythm (mass-market trade edition).
- `lightly-domesticated` + high A6: poetic translations that domesticate vocabulary but mirror source rhythm (e.g., a "rhyming Beowulf" in modern English that preserves the alliterative scheme).

#### 4.2 A5 ↔ A1 (strategy vs per-reference tactics)

**Criterion.** A5 is the STRATEGIC stance. A1 cultural-reference-recognition's handling actions are per-reference TACTICS. A5 modulates which A1 actions fire.

This boundary is operational: A5's level determines the PREFERENCE ORDER over A1's 5 actions per encountered reference. A1's action vocabulary doesn't change with A5; A1's action SELECTION at runtime does.

#### 4.3 A5 ↔ A4 (cross-validation with matrix)

**Cross-validation table** (A4 matrix per-purpose A5 default → A5's 4 levels):

| A4 Purpose | A4 matrix A5 default | A5 4-level mapping |
|---|---|---|
| scholarly | foreignized | `foreignized` ✓ |
| devotional | foreignized (max for liturgical) | `foreignized-max` ✓ |
| casual | balanced | `balanced` ✓ |
| language-learning | balanced-to-foreignized | `foreignized` (refined; the hyphenated value resolves to `foreignized` in A5's 4-level structure) |
| performance | balanced | `balanced` ✓ |

**Minor A4-finding refinement note:** A4's language-learning A5 default is listed as "balanced-to-foreignized" — a hyphenated value implying an in-between level. Against A5's 4-level structure (`foreignized-max | foreignized | balanced | lightly-domesticated`), the closest match is `foreignized` (the rich-scaffolding A7 default for language-learning handles the accessibility need; A5 stays at `foreignized` for source-transparency). This refinement note should be propagated back to the A4 finding's matrix at next maintenance pass.

### 5. Per-Corpus Policy Override (Deferred)

Some corpora may legitimately want heavy domestication that A5's 4-level user-facing range doesn't allow:
- Children's adaptations of classical texts (where target-naturalization serves the developmental audience).
- Popular mass-market editions in fields where target-naturalization is standard (e.g., bestseller fiction translations in some markets).
- Translations for accessibility-purpose audiences (e.g., easy-read editions for cognitive accessibility).

The per-corpus policy override mechanism is deferred to a future audience-level or corpus-level inquiry. The natural future schema would be `audience.policy_override: dict[policy_name, override_value]` at the audience level, with policy names including `domesticate_disfavored` and override values including `permitted_for_corpus_X`. Until then, A5's 4-level asymmetric range respects the policy.

### 6. Strategy Family Opens

A5 is the first axis in the Strategy family per root architectural finding. After this inquiry:

- **Reader family CLOSED** (A1 + A2 + A3 = 3/3).
- **Purpose family CLOSED** (A4 = 1/1).
- **Strategy family OPENS** (A5 = 1/3).
- **5/8 axes complete.**

```python
class A1ReaderLevel:  # composite-axis
    vocabulary_breadth: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    syntactic_processing_capacity: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    idiom_recognition: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    inference_capacity: Literal["very_basic", "daily", "conversational", "advanced", "native"]
    cultural_reference_recognition: Literal["very_basic", "daily", "conversational", "advanced", "native"]

domain_expertise: Literal["lay", "aware", "educated", "trained", "expert"]
source_culture: Literal["outsider", "acquainted", "familiar", "heritage", "source-native"]
purpose: Literal["scholarly", "devotional", "casual", "language-learning", "performance"]
source_fidelity: Literal["foreignized-max", "foreignized", "balanced", "lightly-domesticated"]
```

**What's next.** A6 Form Preservation (next inquiry — ties directly to the project's harmony_layer Tier 1-4 system) and A7 Scaffolding complete the Strategy family. Then A8 Analysis Depth opens and closes the Depth family.

**What's still open per A5 specifically:**

- **Per-corpus policy override** (Section 5) — deferred to future inquiry.
- **A4-finding minor refinement** for language-learning A5 default (Section 4.3) — propagate `foreignized` to A4 matrix.
- **A5↔A6 cross-check** when A6 inquiry completes.
- **A5↔A7 runtime interaction spec** — A5 stance + A7 Scaffolding level jointly shape per-reference handling at runtime.

---

## Inherited Commitments Re-test

This finding inherits commitments from 4 prior inquiry outputs: root, A1 cultural-reference-recognition, A3 source-culture, and A4 purpose. Per the Synthesis Trigger, each is re-tested.

**IC1 — A5 plain-ordinal pattern.** Source: root. RE-TESTED OK. (Section 1.1)

**IC2 — A5 cardinality (root proposed 3).** Source: root. **RE-TESTED & REFINED to 4 asymmetric** on substantive grounds. (Section 1.1)

**IC3 — A5 controls lexical/idiomatic SURFACE.** Source: root. RE-TESTED OK. (Sections 1.1, 4.1)

**IC4 — A5↔A6 orthogonality.** Source: root. RE-TESTED & DOCUMENTED. (Section 4.1 — four-corners independence)

**IC5 — Venuti foreignization↔domestication framework.** Source: root + A1+A3+A4. RE-TESTED OK. (Section 1.1; Venuti anchor preserved)

**IC6 — DOMESTICATE-disfavored cross-cutting policy.** Source: A1 → A3 → A4. **RE-TESTED & EMBEDDED IN A5 STRUCTURE.** (Section 1.2 — no `heavily-domesticated` level)

**IC7 — A4 per-purpose A5 defaults.** Source: A4 finding. **RE-TESTED & CROSS-VALIDATED** with minor refinement note for language-learning. (Section 4.3)

**IC8 — 4-component template adapts.** Source: A1-A3 + A4. **RE-TESTED & ADAPTED — NEW translator-strategy 4-component template.** (Section 1.3)

**IC9 — Receptive-only commitment.** Source: A1-A3 chain. **NOT APPLICABLE TO A5** — translator-strategy, not reader-property. (Section 1.6)

**IC10 — Conservative-bias-LOWER default-when-silent.** Source: A1-A3 + A4 reformulation. **RE-TESTED & INHERITED via A4 chain** — default = `balanced`. (Section 1.5)

**IC11 — Language-agnostic at concept level.** Source: root + chain. RE-TESTED OK.

**IC12 — 4 ordinal levels asymmetric `foreignized-max | foreignized | balanced | lightly-domesticated`.** NEW. (Section 1.1, 1.2)

**IC13 — Policy embedded in axis structure.** NEW. (Section 1.2)

**IC14 — A5 has NO own actions; modulates A1/A3.** NEW. (Section 1.4, Section 3)

**IC15 — NEW translator-strategy 4-component template.** NEW. (Section 1.3)

**IC16 — Per-corpus policy override deferred.** NEW. (Section 5)

**IC17 — Strategy-family-opens marker.** NEW. (Section 1.7, Section 6)

---

## Next Actions

### MUST

- **What:** Commit the A5 enum to schema: `source_fidelity: Literal["foreignized-max", "foreignized", "balanced", "lightly-domesticated"]`.
  - **Who:** User.
  - **Gate:** Condition-bound.
  - **Why:** Enables AI to receive A5 + modulate A1/A3 action selection at runtime.

- **What:** Update A4 finding's matrix to refine language-learning A5 default from "balanced-to-foreignized" to `foreignized` (per Section 4.3 refinement note).
  - **Who:** Maintenance pass on A4 finding.
  - **Gate:** At next A4-finding maintenance opportunity.
  - **Why:** Ensures A4 matrix matches A5's 4-level structure exactly.

### COULD

- **What:** Add an `audience.policy_override` field for per-corpus DOMESTICATE-policy override.
  - **Who:** Future audience-level inquiry.
  - **Why:** Enables heavy domestication for legitimate corpora (children's adaptations etc.) where A5's 4-level user-facing range over-restricts.
  - **Depends-on:** MUST item "Commit the A5 enum". GATED.

- **What:** Add a translator-AI prompt-engineering pass that embeds Sections 1-4 as system-context.
  - **Gate:** After schema commit.

### DEFERRED

- **What:** Per-corpus policy override mechanism (Section 5).
- **What:** Music historically-informed-performance cross-domain illustration (HIP).
- **What:** AI-runtime adaptive A5 (long-horizon).

---

## Reasoning

### Why 4 asymmetric (not 3 symmetric)

Root's 3-symmetric proposal lets the user opt out of the DOMESTICATE-disfavored cross-cutting policy by choosing `heavily-domesticated`. The policy then becomes meaningless. Asymmetric 4 (no `heavily-domesticated`) embeds the policy structurally. Three converging arguments justify this on substantive grounds (Section 1.1).

### Why A5 has no own actions

A1's 5 cultural-reference-handling-actions and A3's 10 cultural-handling-actions in 4 categories already cover the lexical-and-idiomatic handling vocabulary. A5 adding parallel actions would duplicate. A5 as STRATEGIC STANCE modulating which existing actions fire is operationally cleaner and avoids action-vocabulary redundancy.

### Why receptive-only doesn't apply

Parallel reasoning to A4. Receptive-only is about reader-content interactions; A5 is translator-strategy / user-configuration. Different ontological category. Explicit non-inheritance prevents silent assumptions.

### Why per-corpus override is deferred

Most translation jobs in the project's corpus orientation (Said Nursi primary; biblical / Quranic / classical secondary) align with foreignization policy. Rare legitimate exceptions (children's adaptations) don't warrant adding complexity to A5's user-facing range. The escape hatch belongs at the audience or corpus level — a future inquiry.

---

## Open Questions

### Monitoring

- A4 matrix refinement (language-learning A5 default → `foreignized`) needs propagation.
- A5↔A6 cross-check when A6 inquiry completes.
- A5↔A7 runtime interaction spec when A7 inquiry completes.

### Blocked

- Per-corpus policy override blocked by future audience-level inquiry.

### Research Frontiers

- AI-runtime adaptive A5 (translator-AI infers reader-need + adjusts A5 stance from feedback) — long-horizon.

### Refinement Triggers

- If user feedback shows the 4-level asymmetric range over-restricts legitimate use cases, revisit cardinality / range.
- If A6 inquiry refines what "structural form" means in a way that affects A5↔A6 orthogonality, revisit.

---

## Source Input

<details>
<summary>Raw user input</summary>

```text
now lets do it for a5 source fidelity
```

</details>
