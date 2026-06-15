---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md
---
# Finding: A4 — Purpose (the 5 Categorical Purposes)

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` (the root architectural finding that established the 4-layer / 4-family / 8-axis configuration framework for Comprehenslate; specified A4 — Purpose as a categorical axis with a special defaults-driver role, with proposed ~5 categories deferred to a later inquiry).

**Revision trigger:** The user directed: "now lets do it for a4 purpose." This is the first of the non-Reader-family axes, following the completion of the Reader family (A1 + A2 + A3). A4 is structurally distinct from the prior 3 inquiries in two foundational ways: A4 is **categorical** (not ordinal); and A4 **drives defaults** for the other 7 axes per the root's 2-tier default principle.

**What's preserved:**
- A4's identity as a categorical axis (the only categorical axis in the framework; all others are plain-ordinal or composite).
- A4's concept (per root): what the translation is FOR — the use-case.
- A4's special role: defaults-driver for other 7 axes per the root's 2-tier default principle first tier.
- A4's scope (per root): drives strategic translation choices via the use-case.
- A4's boundaries (per root): distinct from A2 Domain Expertise, A3 Source Culture, A8 Analysis Depth.
- Skopos theory (Vermeer / Reiss) anchor for the categorical pattern.
- DOMESTICATE-disfavored project policy inherited from `a1_cultural_reference_recognition_levels/finding.md` and extended through `a3_source_culture_levels/finding.md` — now CARRIES THROUGH A4 cross-cutting.
- Language-agnostic at concept level (purposes meaningful across cultures).

**What's changed:**
- **A4 cardinality validated at 5** on substantive grounds. Reiss's 3-type framework (informative / expressive / operative) is theoretically clean but operationally too coarse for translation-config purposes — it groups devotional, performance, and casual under "expressive" / "operative" without distinguishing their distinct translator-AI strategy implications. Newmark's 4-type extends Reiss but still treats language-learning as a special-case. 5 categories `scholarly | devotional | casual | language-learning | performance` cover the project's Said Nursi corpus use cases AND produce 5 distinct per-axis default profiles.

**What's new:**
- **Categorical pattern preserved and explicit.** Three independent tests confirm: semantic (the user-question "what is this translation FOR?" asks for a category not a degree); lexical ("more scholarly than devotional" doesn't make sense); orthogonality (a scholar can want a casual-feel translation; a casual reader can want deep analysis — purposes don't lie on a single intensity scale).

- **NEW 4-component categorical template.** The capacity-graded 4-component template from A1-A3 (reader profile + frequency/canonicity/expertise-depth tier + register-tier + handling-test) doesn't fit categorical A4 — purposes don't have tiers. The new categorical template has 4 different components matching A4's structure: (1) **Use-case profile** (what the reader DOES with the translation); (2) **Strategic implications** (how this purpose shapes translation strategy choices); (3) **Per-axis default mappings** (what this purpose defaults to for each of the other 7 axes); (4) **DOMESTICATE-policy emphasis** (per-category foreignization emphasis within the cross-cutting policy).

- **Per-purpose × per-axis 5 × 7 default matrix.** This is A4's central operational deliverable — for each of 5 purposes, for each of 7 other axes (A1 with 5 sub-fields treated as one headline, A2, A3, A5, A6, A7, A8), what value does this purpose default to. The matrix populates the root's 2-tier default principle first tier: when the user sets A4, that value drives sensible defaults for the other axes; the user can override any cell explicitly.

- **Single-purpose default + manual override path for multi-purpose cases.** Real multi-purpose cases exist (scholarly + devotional academic-spiritual-formation; casual + language-learning popular-textbook; performance + devotional Quran recitation). Resolution: A4 is single-valued (`Literal[5 categories]`); the user picks the PRIMARY purpose; multi-purpose blends handled by manual per-axis override (e.g., scholar wanting devotional access sets A4=devotional but overrides A8 to deep). Multi-purpose configuration as a list is deferred to a future inquiry.

- **Default-when-A4-silent = `casual`.** The categorical equivalent of the A1-A3 chain's conservative-bias-LOWER principle. `casual` is the safest default: lowest assumption about reader effort; broadest reader spectrum; the casual-purpose defaults for other axes (balanced + rich-scaffolding + surface-depth) produce the safest fallback for unconfigured cases.

- **DOMESTICATE-disfavored policy CARRIES THROUGH A4 cross-cutting.** The policy from A1 cultural-reference-recognition (extended through A3) applies to ALL A4 purposes. Per-purpose foreignization EMPHASIS varies (devotional max; scholarly high; language-learning high; casual balanced; performance balanced) but the policy itself is invariant. Foreignization-preserving alternatives (INLINE-GLOSS + EXPLICATE-FUNCTION + TRANSLITERATE-WITH-GLOSS + KEEP-SOURCE-TERM-WITH-GLOSS) handle accessibility needs without DOMESTICATING across all purposes.

- **Receptive-only commitment DOES NOT APPLY to A4.** Explicit non-inheritance. A4 is a USER configuration choice, not a reader property. Receptive vs productive is about what the READER does with content; A4 captures the USER's strategic choice about what the translation is FOR. Different ontological category.

- **Cross-axis boundaries** documented explicitly (A4↔A2, A4↔A3, A4↔A8) — already partially documented in prior siblings.

- **Purpose-family closure marker.** A4 is the SOLE axis in the Purpose family per root. This finding both OPENS and CLOSES the Purpose family in one inquiry. After this: Reader family (3/3) + Purpose family (1/1) = 4/8 axes complete.

**Migration:** No migration needed — first A4 specification. Schema commit: `purpose: Literal["scholarly", "devotional", "casual", "language-learning", "performance"]`.

---

## Question

For A4 — Purpose (the fourth axis, the only axis in the Purpose family, structurally categorical not ordinal, and structurally special as the defaults-driver for other axes per the root architectural finding), what should the categorical levels be, what concept does each capture (what the reader will DO with the translation), what strategic implications follow from each, and what per-purpose × per-other-axis default matrix populates the 2-tier default principle's first tier — with Skopos / Reiss anchor, Said Nursi corpus mapping, multi-purpose handling, default-when-A4-silent decision, A4↔A2/A3/A8 boundaries, and Purpose-family closure marker?

---

## Finding Summary

- **5 categorical purposes:** `scholarly | devotional | casual | language-learning | performance`. Categorical pattern (NOT ordinal) — confirmed by three independent tests (semantic, lexical, orthogonality). Cardinality validated on substantive grounds against Reiss text-typology (3-type too coarse) and against the project's Said Nursi corpus (which uses all 5).

- **Defaults-driver special role.** A4's value drives sensible defaults for the other 7 axes per the root's 2-tier default principle first tier. The user sets A4 once; per-axis defaults propagate; the user can override any axis explicitly.

- **NEW 4-component categorical template** (replaces capacity-graded template from A1-A3). The 4 components: Use-case profile + Strategic implications + Per-axis default mappings + DOMESTICATE-policy emphasis.

- **Per-purpose × per-axis 5 × 7 default matrix.** The central operational deliverable. Each cell is a default value the purpose suggests; user can override per-cell explicitly.

- **Single-purpose default + manual override path.** A4 is single-valued; multi-purpose cases handled by manual per-axis override; multi-purpose configuration deferred to future inquiry.

- **Default-when-A4-silent = `casual`.** Categorical equivalent of conservative-bias-LOWER. Safest assumption about reader effort; broadest reader spectrum.

- **DOMESTICATE-disfavored cross-cutting.** Carries through all A4 categories from A1 chain. Per-purpose foreignization EMPHASIS varies but policy invariant.

- **Receptive-only DOES NOT APPLY to A4.** A4 is configuration not reader-property. Explicit non-inheritance.

- **A4↔A2 boundary:** A4 = WHY (purpose); A2 = HOW MUCH KNOWN (expertise). Specialist + casual; lay + scholarly are both real.

- **A4↔A3 boundary:** A4 = WHY; A3 = WHO (cultural identity). Source-native + casual; outsider + scholarly are both real.

- **A4↔A8 boundary:** A4 = WHY (purpose); A8 = HOW MUCH COMMENTARY (analysis depth). A4 sets DEFAULT for A8 (scholarly → deep; casual → surface) but doesn't subsume it. Scholar wants LOW depth; casual wants HIGH depth — both real.

- **Said Nursi corpus mapped across all 5 purposes:** scholarly (academic Islamic-studies research on Nursi); devotional (Risale-i Nur as spiritual-practice text); casual (general curious reader); language-learning (Turkish learners); performance (Nursi recitation passages).

- **Purpose family CLOSED.** A4 is the sole axis in the Purpose family. After this inquiry: Reader family (3/3) + Purpose family (1/1) = 4/8 axes complete.

---

## Finding

The root architectural inquiry established Comprehenslate's translation-configuration framework with 4 layers, 4 families, 8 axes. The Reader family has 3 axes (A1 Reader Level, A2 Domain Expertise, A3 Source Culture); all 3 are now specified. A4 — Purpose is the fourth axis and the only axis in the Purpose family. This finding specifies A4's categorical levels and the per-purpose × per-axis default matrix.

### 1. The Framework

#### 1.1 5 categorical purposes

The 5 categorical labels are `scholarly | devotional | casual | language-learning | performance`. They are CATEGORICAL — qualitatively distinct use-cases that do not lie on a single intensity scale. Three independent tests confirm categorical (not ordinal):

**Semantic test.** The user-question "what is this translation FOR?" asks for a category, not a degree. Compare with "how fluent is the reader?" (asks a degree → ordinal A1).

**Lexical test.** "More scholarly than devotional" doesn't make sense. Compare with "more advanced than conversational" (makes sense → ordinal A1).

**Orthogonality test.** A scholar can want a CASUAL-feel translation for relaxation; a casual reader can want DEEP analysis to understand a stuck passage. The orthogonality counter-example (root finding) confirms categorical.

#### 1.2 Why 5 categories (not 3 or 6+)

The root finding proposed ~5 categories with a Skopos-theory anchor. This inquiry validates 5 on substantive grounds:

**Rejected: Reiss 3-type framework** (informative / expressive / operative). Theoretically clean but operationally too coarse for translation-config purposes — it groups devotional, performance, and casual under "expressive" / "operative" without distinguishing their distinct translator-AI strategy implications. A devotional translation preserves liturgical form differently than a casual reading; both differ from a performance translation that maximizes cadence-preservation.

**Rejected: Newmark 4-type** (informative / expressive / vocative / auto-attractive). Extends Reiss but still treats language-learning as a pedagogical special-case rather than a primary use-case. The project's env.example AUDIENCE_LEVEL = native / late_learner / late_learner_simple signals that language-learning is a primary use-case the project recognizes.

**Survived: 5-category framework.** Each category maps to a distinct project use-case AND produces a distinct per-axis default profile. Said Nursi corpus uses all 5 (scholarly academic; devotional spiritual practice; casual curious reader; language-learning Turkish learner; performance recitation). Sub-cases (liturgical / comparative-scholarship / reference) fold cleanly into the 5.

#### 1.3 Defaults-driver special role

A4 is the SPECIAL axis. Per the root's 2-tier default principle, the user sets A4 once and per-axis defaults propagate to the other 7 axes. This makes A4 the entry point for "specify only what you care about" — the user picks the purpose and gets a coherent default configuration; they override only what matters.

The per-purpose × per-axis default matrix in Section 3 operationalizes this role.

#### 1.4 NEW 4-component categorical template

The 4-component template from the A1-A3 chain (reader profile + frequency/canonicity/expertise-depth tier + register-tier + handling-test) is capacity-graded — it works for ordinal axes where each level has a tier position. A4 is categorical; purposes don't have tiers. The capacity-graded template doesn't fit.

NEW 4-component categorical template (same 4-component count for structural parity; different composition matching A4's categorical nature):

1. **Use-case profile** — what the reader DOES with the translation (replaces "reader profile" with reader-action-oriented description).
2. **Strategic implications** — how this purpose shapes translation strategy choices (replaces the tier-component with purpose-driven-strategy).
3. **Per-axis default mappings** — what this purpose defaults to for each of the other 7 axes (the matrix row for this purpose).
4. **DOMESTICATE-policy emphasis** — per-purpose foreignization-emphasis within the cross-cutting policy (replaces the handling-test).

#### 1.5 Single-purpose default + manual override path

A4 is single-valued: `purpose: Literal["scholarly", "devotional", "casual", "language-learning", "performance"]`. The user picks ONE primary purpose per translation job.

Real multi-purpose cases exist (scholarly + devotional academic-spiritual-formation; casual + language-learning popular-textbook; performance + devotional Quran recitation). The resolution: the user picks the PRIMARY purpose; multi-purpose blends handled by manual per-axis override (e.g., a scholar wanting devotional access sets A4=devotional but overrides A8 to deep; a Quran-recitation translator sets A4=performance but overrides A6 to maximum and A3 default reflects devotional source-native).

Multi-purpose configuration as a list (`purpose: list[Literal[...]]` with weights) is richer but adds complexity without operational benefit at this layer. Deferred to a future inquiry.

#### 1.6 Default-when-A4-silent = `casual`

When the user's configuration is silent on A4, the default is `casual`. Substantive grounds: lowest assumption about reader effort; broadest reader spectrum; the casual-purpose defaults for other axes (balanced + rich-scaffolding + surface-depth) produce the safest fallback. This is the CATEGORICAL EQUIVALENT of the A1-A3 chain's conservative-bias-LOWER principle.

Adding a "general" 6th category would be unnecessary; `casual` covers it semantically. Requiring explicit A4 setting would violate the root's "specify only what you care about" principle.

#### 1.7 Receptive-only DOES NOT APPLY to A4

The A1-A3 chain committed to receptive-only (the reader RECOGNIZES content; doesn't produce it). This commitment DOES NOT APPLY to A4. A4 is a USER configuration choice, not a reader property. Receptive vs productive is about what the READER does with content; A4 captures the USER's strategic choice about what the translation is FOR. Different ontological category.

This explicit non-inheritance is important — the A1-A3 chain's commitments form a Reader-family lineage; A4 starts the Purpose family with a different set of foundational principles.

#### 1.8 DOMESTICATE-policy CARRIES THROUGH A4

The DOMESTICATE-disfavored project policy from A1 cultural-reference-recognition (extended through A3) CARRIES THROUGH A4. The policy is CROSS-CUTTING (invariant across all A4 categories); per-purpose foreignization EMPHASIS varies but the policy itself does not.

**Per-purpose foreignization emphasis:**
- **Devotional:** MAXIMUM foreignization. Liturgical form is sacred; preserve source rhythm, honorifics, transliteration without compromise.
- **Scholarly:** HIGH foreignization. Source-fidelity matters for study; preserve cultural specificity for analysis.
- **Language-learning:** HIGH foreignization. Source-transparency matters for the learner; preserve structure for pedagogical value.
- **Casual:** BALANCED. Use foreignization-preserving alternatives (INLINE-GLOSS + EXPLICATE-FUNCTION + TRANSLITERATE-WITH-GLOSS) instead of DOMESTICATE.
- **Performance:** BALANCED. Poetic accessibility matters for oral delivery, but cadence-preservation (A6 maximum) means form is preserved.

DOMESTICATE-CULTURAL-FRAME + ANGLICIZE-HONORIFICS + TARGET-LANGUAGE-EQUIVALENT remain LAST RESORTS across all categories. Foreignization-preserving alternatives handle accessibility needs.

#### 1.9 Translator-AI runtime determination

A4 is purely USER-CONFIGURABLE. The translator-AI receives the purpose value and:
1. Applies the per-axis defaults (Section 3 matrix) unless the user has overridden them.
2. Adjusts strategy emphasis per the per-purpose foreignization emphasis (Section 1.8).
3. Reads the per-category prose (Section 2) as part of its system context.

A4 is not AI-runtime-inferred — the AI doesn't try to guess the user's purpose from the source text. (This would mix Layer 1 USER-FACING AXES with Layer 3 SOURCE-DESCRIPTION; the layers are kept separate.)

### 2. The 5 Per-Category Definitions

Each category has the 4 components (use-case profile + strategic implications + per-axis default mappings reference + DOMESTICATE-policy emphasis) plus the Said Nursi corpus anchor + at least one cross-cultural illustration.

#### 2.1 `scholarly`

**Use-case profile.** The reader STUDIES the translation — analyzes structure, traces arguments, cites passages, compares versions, prepares academic work. The translation serves research and analysis. The reader engages the text with notes, marginalia, cross-references.

**Strategic implications.** Source-fidelity is paramount; preserve as much source structure as possible (rhythm, parallelism, word order, multi-meaning, source-language honorifics). Footnoting is expected. Cultural specificity is preserved. Analysis Depth defaults to deep/scholarly.

**Per-axis default mappings reference.** See Section 3 matrix row "scholarly".

**DOMESTICATE-policy emphasis.** HIGH foreignization — source-fidelity for study. INLINE-GLOSS and FOOTNOTE preferred for accessibility; PARAPHRASE and DOMESTICATE-CULTURAL-FRAME are LAST RESORTS only when source-fidelity has been exhausted.

**Said Nursi anchor.** A scholar researching Said Nursi's place in Naqshbandi-Khalidi Sufi theology; a graduate-student writing on Nursi's epistemology.

**Cross-cultural illustration.** A graduate-student writing on the Documentary Hypothesis (Hebrew biblical scholarly); an academic studying Husserl's phenomenology (philosophy scholarly).

#### 2.2 `devotional`

**Use-case profile.** The reader READS for spiritual practice — meditates on passages, memorizes, recites, reflects. The translation serves religious/spiritual formation. The reader returns to favorite passages; daily reading habit; communal study (dersane for Nursi).

**Strategic implications.** Liturgical form is sacred — preserve source rhythm, honorifics, transliteration. Avoid distractions (over-glossing, heavy footnoting at-text). The reader is engaging spiritually, not analytically. Cultural specificity is preserved maximally.

**Per-axis default mappings reference.** See Section 3 matrix row "devotional".

**DOMESTICATE-policy emphasis.** MAXIMUM foreignization. Liturgical specificity is the point. KEEP-HONORIFICS-SOURCE; TRANSLITERATE-FULLY for established devotional vocabulary; PRESERVE-CULTURAL-SPECIFICITY at maximum.

**Said Nursi anchor.** A Risale-i Nur reader doing daily spiritual reading; a dersane study circle.

**Cross-cultural illustration.** A daily prayer reading from the Quran in translation; a Christian using the Bible for lectio divina; a Hindu reading the Gita for meditation.

#### 2.3 `casual`

**Use-case profile.** The reader READS for general comprehension — curiosity, light reading, getting the gist. The translation serves general literary engagement. The reader doesn't return to passages obsessively; reads once or twice; isn't preparing analysis or spiritual practice.

**Strategic implications.** Balance source-fidelity with accessibility. Help the reader where they need it (rich scaffolding); don't overwhelm with footnotes. Cultural references get foreignization-preserving glosses (FLAG-CULTURAL-CONTEXT + TRANSLITERATE-WITH-GLOSS) rather than DOMESTICATE. Analysis depth is surface.

**Per-axis default mappings reference.** See Section 3 matrix row "casual".

**DOMESTICATE-policy emphasis.** BALANCED. Foreignization-preserving alternatives (INLINE-GLOSS + EXPLICATE-FUNCTION) handle accessibility needs. DOMESTICATE remains last-resort.

**Said Nursi anchor.** A general curious reader exploring Risale-i Nur; a non-Muslim with interest in Islamic theology; a convert reading for general orientation.

**Cross-cultural illustration.** A Penguin Classics reader of Plato; a general reader of a literary novel in translation; a curious reader of an introductory Quran translation.

#### 2.4 `language-learning`

**Use-case profile.** The reader LEARNS the source language through the translation — reads to acquire vocabulary, syntax, idiomatic patterns. The translation serves pedagogical clarity. The reader may have an interlinear or parallel-text version; consults the source alongside; back-translates; notes syntactic patterns.

**Strategic implications.** Maximum transparency to source structure. Preserve source word-order, parallelism, structural patterns even at cost of target-language naturalness. Rich scaffolding (vocabulary glosses, grammatical notes, parallel-source alignment). Source-fidelity for pedagogical value.

**Per-axis default mappings reference.** See Section 3 matrix row "language-learning".

**DOMESTICATE-policy emphasis.** HIGH foreignization. Source-transparency is the point — the learner needs to see the source structure. TRANSLITERATE-WITH-GLOSS prominently; KEEP-SOURCE-TERM-WITH-GLOSS for vocabulary acquisition.

**Said Nursi anchor.** A Turkish learner using Nursi as reading material; an advanced student of Ottoman Turkish; an Arabic-students reading Nursi's Quran-citations.

**Cross-cultural illustration.** A Latin student reading Cicero with parallel text; a Greek student reading Plato with vocabulary glosses; a Sanskrit student reading the Gita with grammar notes.

#### 2.5 `performance`

**Use-case profile.** The reader DELIVERS the translation orally — recitation, reading aloud, theatrical performance, sermon delivery. The translation serves oral / aural reception. The reader's audience receives the text through hearing.

**Strategic implications.** Maximum cadence preservation. Form is meaning per the project's harmony_layer commitment (Tier 1-4 system). Rhythm, parallelism, and other structural elements that create oral effect are preserved. Footnotes are off — they break delivery. Clean text for oral flow.

**Per-axis default mappings reference.** See Section 3 matrix row "performance".

**DOMESTICATE-policy emphasis.** BALANCED. Poetic accessibility matters for oral delivery, but cadence preservation (A6 maximum) means form is preserved over substitution. KEEP-HONORIFICS-SOURCE for liturgical performance.

**Said Nursi anchor.** Nursi recitation passages (some are designed for oral delivery); a sermon-translation drawing on Nursi.

**Cross-cultural illustration.** Quran recitation in translation (some translations are designed for recitation); a Greek tragedy in staged English; an opera surtitle translation; a poetry slam translation.

### 3. Per-Purpose × Per-Axis Default Matrix

The matrix is the central operational deliverable. For each of 5 purposes (rows), for each of 7 other axes (columns), the default value the purpose suggests. The user can override any cell explicitly.

| Purpose | A1 Reader Level (headline) | A2 Domain Expertise | A3 Source Culture | A5 Source Fidelity | A6 Form Preservation | A7 Scaffolding | A8 Analysis Depth |
|---|---|---|---|---|---|---|---|
| **scholarly** | advanced | educated | any (often outsider-with-study) | foreignized | high | rich | deep / scholarly |
| **devotional** | conversational | aware-to-educated | source-native / heritage | foreignized (max for liturgical) | high (preserve rhythm) | moderate | standard |
| **casual** | daily | lay-to-aware | outsider-to-acquainted | balanced | moderate | rich (help unfamiliar) | surface |
| **language-learning** | conversational (matched to learner) | lay | outsider | balanced-to-foreignized (transparency) | high (preserve structure) | MAX rich | standard |
| **performance** | conversational | any | any | balanced | MAXIMUM (cadence) | minimal (clean text for delivery) | surface |

**Justification per cell** (key entries):

- **scholarly × A1=advanced**: scholarly readers are typically advanced+ in general fluency; technical-academic register expected.
- **scholarly × A8=deep**: scholarly purpose is for analysis; deep commentary is expected accompaniment.
- **devotional × A5=foreignized (max)**: liturgical specificity is sacred; preserve source-cultural form.
- **devotional × A6=high**: rhythm and parallelism are devotional-experiential.
- **casual × A1=daily**: casual readers span a broad spectrum; daily is the safe central default.
- **casual × A7=rich**: casual readers benefit from rich scaffolding to navigate unfamiliar material.
- **language-learning × A7=MAX**: pedagogy requires maximum scaffolding (vocabulary glosses + grammar notes + parallel-source alignment).
- **language-learning × A6=high**: structural preservation enables learner to see source patterns.
- **performance × A6=MAXIMUM**: cadence preservation is the central performance concern; rhythm = meaning per harmony_layer commitment.
- **performance × A7=minimal**: clean text for oral delivery; footnotes break flow.

**Forward-looking note.** When A5, A6, A7, A8 inquiries complete with their own level definitions, the matrix entries above should be re-validated against the per-axis specifications.

**Override path.** The user can override any matrix cell explicitly: `purpose = "devotional"` defaults A8 to "standard", but the user can override A8 = "deep" for a devotional-yet-analytical reader.

### 4. DOMESTICATE-Policy Carries-Through

The DOMESTICATE-disfavored project policy from `a1_cultural_reference_recognition_levels/finding.md` (extended through `a3_source_culture_levels/finding.md`) CARRIES THROUGH A4 cross-cutting. The policy is INVARIANT across all 5 categories; per-purpose foreignization EMPHASIS varies but the policy itself does not.

**Anchor 1:** User's translation-register-fidelity memory.
**Anchor 2:** Lawrence Venuti's foreignization ethics.

**Per-purpose emphasis variation:**
- Devotional: MAXIMUM foreignization (liturgical sacred).
- Scholarly: HIGH (source-fidelity for study).
- Language-learning: HIGH (source-transparency for pedagogy).
- Casual: BALANCED (foreignization-preserving alternatives over DOMESTICATE).
- Performance: BALANCED (cadence preservation via A6 maximum implies form-preservation).

**Cross-cutting policy preference order:**

```
PRESERVE-CULTURAL-SPECIFICITY > KEEP-HONORIFICS-SOURCE > TRANSLITERATE-WITH-GLOSS > FLAG-CULTURAL-CONTEXT > BRIDGE-CULTURAL-DISTANCE > [TARGET-LANGUAGE-EQUIVALENT / DOMESTICATE-CULTURAL-FRAME / ANGLICIZE-HONORIFICS] (last resorts)
```

This order is invariant across A4 categories. Per-purpose emphasis adjusts the THRESHOLD at which last-resort options become viable.

### 5. Cross-Axis Boundaries

#### 5.1 A4 ↔ A2 (Purpose vs Domain Expertise)

**Criterion.** A4 = WHY (purpose); A2 = HOW MUCH KNOWN (domain expertise). Independent.

**Independence demonstration.** A specialist Islamic-studies professor (A2=expert) may read Nursi for casual purpose (A4=casual) — relaxation, light browsing. A lay reader (A2=lay) may read for scholarly purpose (A4=scholarly) — researching a paper on an unfamiliar tradition.

#### 5.2 A4 ↔ A3 (Purpose vs Source Culture)

**Criterion.** A4 = WHY; A3 = WHO (cultural identity). Independent.

**Independence demonstration.** A source-native Turkish-Muslim (A3=source-native) may read Nursi for casual purpose. An outsider Western-secular reader (A3=outsider) may read for scholarly purpose.

#### 5.3 A4 ↔ A8 (Purpose vs Analysis Depth)

**Criterion.** A4 = WHY (purpose); A8 = HOW MUCH COMMENTARY (analysis depth). A4 sets DEFAULT for A8 (scholarly → deep; casual → surface) per the per-axis matrix, but doesn't subsume it.

**Independence demonstration.** A scholar (A4=scholarly) may want LOW depth for a particular use (clean text only, no commentary cluttering the page). A casual reader (A4=casual) may want HIGH depth to understand a passage they're stuck on. The default matrix sets the starting point; the user overrides per-axis.

### 6. Purpose Family Closure

A4 is the SOLE axis in the Purpose family per the root architectural finding. This inquiry both OPENS and CLOSES the Purpose family.

**What's now spec'd.** After this inquiry:
- **Reader family CLOSED** (A1 + A2 + A3 = 3/3).
- **Purpose family CLOSED** (A4 = 1/1).
- **4/8 axes complete.**

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
```

**What's next.** The remaining axes per the root 8-axis architecture:

- **A5 Source Fidelity** (Strategy family) — plain-ordinal, ~3 levels (foreignization ↔ domestication scale).
- **A6 Form Preservation** (Strategy family) — plain-ordinal, ~5 levels (Tier 1-4 harmony-layer system).
- **A7 Scaffolding** (Strategy family) — plain-ordinal, ~5 levels (off / minimal / standard / rich / scholarly).
- **A8 Analysis Depth** (Depth family) — plain-ordinal, ~4 levels (surface / standard / deep / scholarly).

**What's still open per A4 specifically:**

- **Per-axis default matrix re-validation** when A5/A6/A7/A8 inquiries complete with their own level definitions.
- **Multi-purpose configuration** (`purpose: list[Literal[...]]` with weights) — future inquiry if multi-purpose cases become primary use cases.
- **Time-varying purpose** (user changes purpose mid-translation) — snapshot assumption.
- **Source-side intended purpose** (Layer 3 SOURCE-DESCRIPTION concern) — out of A4 scope.

---

## Inherited Commitments Re-test

This finding inherits commitments from 3 prior inquiry outputs: the root architectural finding, the A2 Domain Expertise inquiry, and the A3 Source Culture inquiry (with relevant connections to A1 cultural-reference-recognition for the DOMESTICATE-disfavored policy).

**IC1 — A4 categorical pattern.**
- **Source:** root architectural finding.
- **Re-test status:** RE-TESTED OK.
- **Evidence:** 3 independent tests pass (semantic, lexical, orthogonality) per sensemaking KI3.

**IC2 — A4 defaults-driver role.**
- **Source:** root.
- **Re-test status:** RE-TESTED OK.
- **Evidence:** Section 3's 5 × 7 default matrix operationalizes the role.

**IC3 — A4 ~5 cardinality.**
- **Source:** root.
- **Re-test status:** RE-TESTED & CONFIRMED at 5 on substantive grounds.
- **Evidence:** Section 1.2 documents the substantive argument (Reiss 3-type too coarse; Newmark misses language-learning; project Said Nursi maps fully to 5).

**IC4 — Skopos / Reiss anchor.**
- **Source:** root.
- **Re-test status:** RE-TESTED & EXTENDED.
- **Evidence:** Section 1.2 documents the 5-vs-3-type substantive justification.

**IC5 — A4 ↔ A2 / A3 / A8 boundaries.**
- **Source:** root + A2 + A3 findings.
- **Re-test status:** RE-TESTED & DOCUMENTED.
- **Evidence:** Section 5 documents all 3 boundaries with criterion + independence demonstrations.

**IC6 — Receptive-only commitment (A1-A3 chain).**
- **Source:** A1-A3 chain.
- **Re-test status:** **NOT APPLICABLE TO A4.**
- **Evidence:** Section 1.7. A4 is USER configuration not reader-property. The receptive vs productive distinction applies to reader-content interactions; A4 captures the user's strategic choice. Different ontological category. Explicit non-inheritance — important because the A1-A3 chain's commitments form a Reader-family lineage; A4 starts the Purpose family with a different foundational set.

**IC7 — Conservative-bias-LOWER default (A1-A3 chain).**
- **Source:** root + A1-A3 chain.
- **Re-test status:** **RE-TESTED & REFORMULATED.**
- **Evidence:** Section 1.6. The categorical equivalent is "default-when-A4-silent = `casual`" — lowest assumption about reader effort; broadest reader spectrum. The principle survives but is reformulated for categorical pattern.

**IC8 — Single-X default (A2 + A3 pattern).**
- **Source:** A2 + A3 inquiries.
- **Re-test status:** RE-TESTED & APPLIED as single-purpose default.
- **Evidence:** Section 1.5. Single-purpose configuration; multi-purpose deferred.

**IC9 — 4-component template adapts (A1-A3 chain).**
- **Source:** A1-A3 chain.
- **Re-test status:** **RE-TESTED & ADAPTED.** NEW categorical template (same 4-component count for structural parity; different composition).
- **Evidence:** Section 1.4. New 4 components: use-case profile + strategic implications + per-axis default mappings + DOMESTICATE-policy emphasis.

**IC10 — DOMESTICATE-disfavored policy.**
- **Source:** `a1_cultural_reference_recognition_levels/finding.md` → A3 chain.
- **Re-test status:** **RE-TESTED & CARRIES-THROUGH CROSS-CUTTING.**
- **Evidence:** Section 4. Policy invariant across all 5 A4 categories; per-purpose foreignization emphasis varies.

**IC11 — Translator-AI runtime determination.**
- **Source:** A2 + A3 inquiries.
- **Re-test status:** RE-TESTED OK.
- **Evidence:** Section 1.9. A4 is user-config; AI receives + applies defaults + adjusts strategy emphasis.

**IC12 — Language-agnostic at concept level.**
- **Source:** root + A1-A3 chain.
- **Re-test status:** RE-TESTED OK.
- **Evidence:** Purposes meaningful across cultures (cross-cultural illustration in Section 2 per category).

**IC13 — 5 categorical purposes** (NEW).
- **Source:** Sensemaking Ambiguity A1.
- **Re-test status:** NEW.
- **Anchor:** Section 1.1, 1.2. Labels validated against Skopos + Said Nursi.

**IC14 — Full 5 × 7 per-purpose × per-axis default matrix** (NEW).
- **Source:** Sensemaking KI4 + root's 2-tier default principle.
- **Re-test status:** NEW.
- **Anchor:** Section 3. 35-cell matrix with per-cell justification.

**IC15 — Default-when-A4-silent = `casual`** (NEW).
- **Source:** Sensemaking A6.
- **Re-test status:** NEW.
- **Anchor:** Section 1.6.

**IC16 — NEW 4-component categorical template** (NEW).
- **Source:** Sensemaking KI7.
- **Re-test status:** NEW.
- **Anchor:** Section 1.4.

**IC17 — Single-purpose default + manual override path** (NEW).
- **Source:** Sensemaking A5.
- **Re-test status:** NEW.
- **Anchor:** Section 1.5.

**IC18 — Purpose-family closure (A4 sole axis)** (NEW).
- **Source:** root + this inquiry as closure event.
- **Re-test status:** NEW.
- **Anchor:** Section 6.

---

## Next Actions

### MUST

- **What:** Commit the A4 enum to the schema: `purpose: Literal["scholarly", "devotional", "casual", "language-learning", "performance"]`.
  - **Who:** User.
  - **Gate:** Condition-bound.
  - **Why:** Enables AI to receive purpose + apply per-axis defaults.

- **What:** Implement the per-purpose × per-axis 5 × 7 default matrix as a lookup at config-resolution time.
  - **Who:** Configuration layer.
  - **Gate:** After schema commit.
  - **Why:** Operationalizes the defaults-driver role per the root's 2-tier default principle.

### COULD

- **What:** Re-validate the matrix entries for A5 / A6 / A7 / A8 columns when those inquiries complete.
  - **Gate:** Condition-bound — when A5-A8 inquiries finish.
  - **Why:** Matrix entries for axes-not-yet-specified are working hypotheses; re-validation tightens the per-purpose defaults.
  - **Depends-on:** MUST item. GATED.

- **What:** Add a translator-AI prompt-engineering pass that embeds Sections 1, 2, 3, 4, 5 of this finding as system-context.
  - **Gate:** After schema commit.
  - **Why:** Makes A4 level definitions + matrix operationally available.

### DEFERRED

- **What:** Multi-purpose configuration (`purpose: list[Literal[...]]` with weights).
  - **Gate:** Revival — if multi-purpose cases become primary use cases (e.g., when project explicitly supports academic-spiritual-formation editions).
  - **Why (if revived):** Richer expressiveness for genuine multi-purpose use cases.

- **What:** Recipe categorization cross-domain illustration (cooking analogies for purpose-driven defaults).
  - **Gate:** Revival — if future inquiries need additional cross-domain anchors.

- **What:** AI-runtime purpose inference (translator-AI infers purpose from source-text + feedback).
  - **Gate:** Revival — when AI capability matures (5-10 years).
  - **Why (if revived):** Removes static configuration burden.

---

## Reasoning

### Why categorical (not ordinal)

The root finding committed to categorical pattern; this inquiry confirms on substantive grounds via 3 independent tests (semantic, lexical, orthogonality). Forcing ordinality would create artificial distinctions and would fail the orthogonality counter-example (scholar wants casual-feel; casual wants deep analysis).

### Why 5 categories (not 3 or 6+)

**Rejected: 3-type Reiss framework.** Too coarse for translation-config; groups devotional + performance + casual together without distinguishing their translator-AI strategy implications.

**Rejected: 4-type Newmark.** Misses language-learning as a primary use-case. The project's env.example AUDIENCE_LEVEL signal recognizes language-learning informally; the framework formalizes it.

**Rejected: 6+ categories.** Adds complexity without coverage. Sub-cases (liturgical / comparative / reference) fold cleanly into the 5.

**Survived: 5 categories** that cover the project's Said Nursi corpus + produce 5 distinct per-axis default profiles.

### Why receptive-only DOES NOT APPLY to A4

The A1-A3 chain's receptive-only commitment is about reader-content interactions (reader RECOGNIZES content; doesn't produce). A4 is a USER configuration choice, not a reader-content interaction. Different ontological category. Explicit non-inheritance documented to prevent silent inheritance assumptions.

### Why DOMESTICATE policy carries through

The project policy from A1 cultural-reference-recognition is grounded in cross-cutting commitments (user memory + Venuti). These commitments don't depend on A4's value — they apply whatever the purpose. Per-purpose foreignization EMPHASIS varies (devotional max; casual balanced) but the policy itself is invariant.

### Why single-purpose default (not multi-purpose configuration)

Most translation jobs have ONE primary purpose. Multi-purpose blends are real but handled by manual per-axis override (scholar-wanting-devotional sets A4=devotional but overrides A8 manually). Multi-purpose configuration as a list adds complexity without proportional operational benefit. Deferred to future inquiry if multi-purpose cases become primary.

---

## Open Questions

### Monitoring

- **AI prompt-context calibration.** Observe per-purpose handling at runtime; calibrate defaults if needed.
- **Default matrix re-validation triggers.** When A5/A6/A7/A8 inquiries complete, re-validate the matrix entries for those columns.

### Blocked

- **Multi-purpose configuration** deferred until multi-purpose cases become primary use cases.

### Research Frontiers

- **AI-runtime purpose inference.** Long-horizon. Translator-AI infers purpose from source + feedback. Removes static config burden but conflicts with current Layer 1/Layer 3 separation.

### Refinement Triggers

- **Refinement trigger for cardinality.** If user feedback indicates 5 categories don't fit (e.g., they need a 6th category that doesn't fold into existing 5), revisit.

- **Refinement trigger for category names.** If user feedback indicates the labels read oddly, revisit.

- **Refinement trigger for default matrix.** When A5/A6/A7/A8 inquiries finish, the matrix entries for those columns need re-validation.

- **Refinement trigger for DOMESTICATE-policy carries-through.** If the project expands beyond foreignization-preferring corpora (e.g., children's adaptations), the per-purpose policy emphasis may need per-corpus overrides.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
now lets do it for a4 purpose
```

</details>
