# Branch: a2_domain_expertise_levels

## Question

**Context.** The root architectural finding `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` (settled the 4-layer / 4-family / 8-axis configuration framework for the Comprehenslate AI-assisted translation project) established A2 — Domain Expertise as the second axis in the Reader family. Per the root: A2's concept is "the reader's specialist knowledge in the source's subject domain (Islamic theology, biblical scholarship, theoretical physics, etc.) — independent of their general reading fluency"; it answers "How much does the reader already know about the subject matter?"; it controls "whether the translator can use technical vocabulary without unpacking"; and it is distinct from A1 (general fluency) AND from A3 (cultural identity-based proximity). The root proposed 3 ordinal levels (`lay / general-educated / specialist`) but explicitly deferred level-value finalization to "the next inquiry."

The 5-sub-field A1 Reader Level chain has now closed (`devdocs/inquiries/2026-06-06_11-47__a1_cultural_reference_recognition_levels/finding.md` and 4 prior siblings), establishing the same-labels-for-default-propagation pattern across A1's 5 sub-fields. The user has now directed: define A2's level values, with the explicit cardinality directive "it should be 5 levels again."

The user's specific framing: defining 5 levels for A2 is structurally easy to deduce (the project's level-count pattern is 5); the REAL DIFFICULTY is defining HOW to DISTINGUISH the 5 levels — explicit definitions with good examples that make each level operationally identifiable.

This inquiry takes the SAME shape applied to A2 instead of an A1 sub-field. But A2 differs structurally from the 5 A1 sub-field inquiries: A2 is a plain ordinal axis, NOT a composite-axis (no sub-fields, no propagation). The 4-component template from the A1 chain may not directly apply; this inquiry must decide what definition template fits an axis whose dimension is DOMAIN-SPECIALIST KNOWLEDGE depth rather than reader-side recognition capacity.

State the question:
- **Subject:** A2 — Domain Expertise level definitions (5 ordinal levels).
- **Action:** Define each level's concept, distinguishing logic, examples across multiple domain types, and operational definition usable as translator-AI prompt context.
- **Level:** Axis-level (one axis, not a sub-field chain). A2 is plain-ordinal per the root architecture; this inquiry settles its 5 level values.
- **Observation targets** (multiple, preserved separately):
  1. The 5 LEVEL NAMES (cardinality fixed at 5 per user directive; label choice open — same-labels-for-default-propagation does NOT apply since A2 is not composite-axis).
  2. The CONCEPT each level captures (one sentence per level: what depth of domain-specialist knowledge the reader has).
  3. The distinguishing LOGIC between adjacent levels (what specifically separates lay from informed, informed from studied, studied from specialist — the explicit "you can tell which level a reader is at" criterion).
  4. CONCRETE EXAMPLES per level spread across multiple domains (Islamic theology — the project's primary corpus for Said Nursi; biblical scholarship; classical philosophy; theoretical physics; legal scholarship; etc.) so the level identity travels across subject-matter without being defined narrowly.
  5. The OPERATIONAL DEFINITION usable as translator-AI prompt context: what technical vocabulary the AI can use without unpacking at each level; what discourse-level moves (school references, debate references, lineage references) the AI can leave un-explicated at each level.
  6. The A2 DEFINITION TEMPLATE (does the 4-component template from A1 sub-fields adapt, or does A2 need its own template? The dimension is NOT recognition-capacity; it's knowledge-DEPTH in a specific domain).
  7. The DOMAIN-SCOPE question: does A2 specify a single domain (per-translation-job) or a domain SET (the reader's expertise across multiple domains)? — touches the same axis-vs-config question that cultural-reference-recognition faced with canon-choice.
  8. The A2↔A1 BOUNDARY: A2 is NOT general reading fluency (A1 covers that). A2's specialist vocabulary is distinct from A1's vocabulary-breadth. A2's specialist discourse is distinct from A1's syntactic-processing-capacity. Boundary clarity is required.
  9. The A2↔A3 BOUNDARY: A2 is competence-based domain knowledge; A3 is identity-based cultural proximity. A reader can be A2=specialist + A3=outsider (a Western academic specialist in Islamic theology who is not from the source culture) OR A2=lay + A3=source-native (a cultural insider with no formal training). Boundary clarity is required.

- **Deliverable shape:** 5 named ordinal levels with per-level definition + distinguishing logic + 3-5 concrete examples spread across multiple domains; operational specification for translator-AI prompt context; A2 definition template (adapted from A1 sub-field template if applicable, or new); explicit A2↔A1 and A2↔A3 boundary statements; domain-scope (single vs set) decision.

**State the question:** **For A2 — Domain Expertise, what should the 5 ordinal levels be — what concept does each level capture (how much domain-specialist knowledge the reader has in the source's subject domain), what logic distinguishes each level from its neighbors, what concrete examples of domain-specialist vs general-reader knowledge make each level operationally identifiable (across multiple domains: Islamic theology, biblical scholarship, philosophy, science, law), defined language-agnostically at the concept level (the framework works for any source domain), with explicit definitions usable as translator-AI prompt context — AND settling the A2↔A1 boundary (vs general fluency), the A2↔A3 boundary (vs cultural identity), and the domain-scope question (single-domain config vs domain-set config)?**

## Goal

- **Criterion.** Five mutually distinct, ordinally meaningful, spectrum-covering levels for A2 Domain Expertise — each operationalizable as a translator-AI prompt instruction (so the AI knows which technical vocabulary it can leave un-glossed at each level, which discourse-level references it can leave un-explicated, which specialist debates it can invoke without unpacking). Each level needs an EXPLICIT definition and concrete examples across multiple domains; the user has explicitly flagged this as the inquiry's main challenge.

- **Use case.** The user will commit these as the `domain_expertise: Literal[...]` enum values in the schema; the per-level prose becomes part of the translator-AI's prompt context; the boundaries guide the AI in deciding domain-vocabulary-unpacking and specialist-reference-handling per level.

- **Desired outcome.** A stable, named, defined set of 5 A2 Domain Expertise levels with definition + distinguishing logic + 3-5 concrete examples per level spread across multiple domains; A2↔A1 and A2↔A3 boundary statements; domain-scope decision; ready for the user to commit to the schema and proceed to the next axis (A3 — Source Culture is the natural follow-on).

- **What would fail.**
  - Levels defined only by example without explicit distinguishing logic. (The user explicitly flagged this risk: "we need some good, explicit definitions with good examples.")
  - Levels that overlap in scope.
  - Levels that aren't ordinal (mixing categorical domain types alongside ordinal expertise depth).
  - Levels that lock to one domain (Islamic theology only, or biblical only) and fail to generalize to other domains.
  - Examples that don't span multiple domains.
  - Conflating A2 Domain Expertise with A1's vocabulary-breadth sub-field (knowing "ratiocination" is a general-vocabulary fact; knowing "isnād" is a domain-specialist fact — same axis-level concept but different scope).
  - Conflating A2 with A1's cultural-reference-recognition sub-field (knowing "a Cassandra moment" is general cultural literacy; knowing what "tafsīr" is is specialist domain knowledge).
  - Conflating A2 with A3 Source Culture (specialist Western academic vs cultural insider — both real configurations).
  - Conflating A2 with A4 Purpose (a scholarly purpose ≠ a specialist reader).
  - Failure to address the domain-scope question (single-domain per config vs domain-set per config).
  - Failure to define the A2 template (does it inherit from A1 sub-field template? does it need its own?).
  - Examples drawn only from Western canon, missing the project's primary corpus (Islamic theology / Said Nursi).
  - Same-labels-for-default-propagation forced where it doesn't apply (A2 is NOT composite-axis; it doesn't propagate to sub-fields; the labels need not match A1's `very_basic | daily | conversational | advanced | native` if domain-meaningful labels work better).

## Source Input

```text
now do it for A2 — Domain Expertise
first of all reread devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md fully.
it is a bit challanging, it should be 5 level again. this is easy to deduct. But the real question is the definitions of how to distinguish these 5 levels, we need some good, explicit definitions with good examples i think
```

## Scope Check

Question covers goal: YES.

The Question targets the 5 levels of A2 Domain Expertise with names, concepts, distinguishing logic, examples (cross-domain), operational prompt-context definitions, template adaptation, A2↔A1 and A2↔A3 boundaries, and the domain-scope question. The Goal asks for those plus operationalizability and scope discipline (avoid conflations with A1, A3, A4).

**Specific-vs-pattern check.** User said "now do it for A2 — Domain Expertise" — apply the broader pattern of "define the 5 ordinal levels for this axis" to the specific axis A2. Scope is the BROADER PATTERN of A2 Domain Expertise across multiple domains (not just one specific domain like Islamic theology). The user has explicitly emphasized examples need to be "good" — implying they should span domains sufficiently to make the level framework language-/domain-agnostic.

**Multi-clause transcription check.** The user's input contains multi-sentence framing:
- Sentence 1: "now do it for A2 — Domain Expertise" → preserved in Question's "Subject."
- Sentence 2: "first of all reread devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md fully" → preserved as the inquiry's pre-condition (reading the root architectural finding has been performed before this _branch.md was written).
- Sentence 3: "it is a bit challanging, it should be 5 level again. this is easy to deduct" → preserved in Question's cardinality directive (5 levels) and the framing that the user perceives this as challenging.
- Sentence 4: "But the real question is the definitions of how to distinguish these 5 levels, we need some good, explicit definitions with good examples i think" → preserved in Question's "real difficulty" framing and in Goal's "What would fail" (levels defined only by example without distinguishing logic).
All clauses' semantic content survives transcription into Question + Goal. PASS.

**Decoupling from A1 chain.** The A1 chain is closed; this is a NEW inquiry on a SEPARATE axis. Same-labels-for-default-propagation DOES NOT inherit here because A2 is not a composite-axis. Whether the labels should match A1's labels is an open design question for this inquiry to settle (it may be sensible for consistency, or it may be better to use domain-meaningful labels).

**Decoupling from root finding's commitments.** The root finding committed to A2 with 3 levels; this inquiry refines that to 5 levels per user directive. The root's other A2 commitments (plain-ordinal pattern, scope, boundary vs A1/A3) are inherited and re-tested.

**Template-adaptation in scope.** Whether the 4-component template from A1 sub-fields applies here is an open question for sensemaking. A2's dimension (domain-specialist knowledge depth) differs from A1's dimensions (recognition capacity). The template may need significant adaptation or replacement.

## Synthesis Trigger

This inquiry consolidates / synthesizes commitments from at least 2 prior inquiry outputs (triggers Synthesis Trigger per MVLw protocol):

- `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — root architectural finding. Commits to: A2's concept (specialist domain knowledge); A2's plain-ordinal pattern (3 levels proposed, deferred to next inquiry); A2 boundary vs A1 and A3; 8-axis architecture; Skopos / Venuti / formal-vs-dynamic-equivalence anchors; conservative-bias-defaults principle.

- `devdocs/inquiries/2026-06-06_11-47__a1_cultural_reference_recognition_levels/finding.md` — the most recent sibling inquiry closing the A1 chain. Commits to: receptive-only commitment; conservative-bias-for-reader-axes; language-agnostic-at-concept-level (with culture-bound caveat for canon-choice); 4-component template adaptation (`reader profile + canonicity-tier + register/canon-tier + cultural-reference-handling test`); per-sub-field A1↔A2 boundary criterion (general cultural literacy vs domain-specialist canon training); 5 specialist-domain canons listed at the A1↔A2 boundary (legal precedents, mathematical figures, scientific figures, medical eponyms, specialist philosophy) — these are RELEVANT to A2's identity but apply differently here.

Inherited commitments to re-test (non-exhaustive; the finding's `## Inherited Commitments Re-test` section will enumerate fully):
- Receptive-only commitment.
- Conservative-bias-for-reader-axes = LOWER default.
- Language-agnostic at concept level.
- The 5 specialist-domain canons from A1's cultural-reference-recognition (legal / mathematical / scientific / medical / specialist-philosophical) — A1 routed these to A2; this inquiry RECEIVES them and validates that A2's framework handles them.
- A2 cardinality (proposed 3 → committed 5 per user directive).
- A2's plain-ordinal pattern (no sub-fields).
- A2's boundary vs A1 (general fluency) and A3 (cultural identity).
- A2's special role in the framework (controls technical vocabulary unpacking; specialist debate reference handling).
- The root's anchor on Skopos / formal-vs-dynamic equivalence (more general translation-theory context).

Sensemaking will adjudicate these commitments; Critique will re-test the adjudication. The discipline work will actually re-test these commitments, not merely record the inheritance.
