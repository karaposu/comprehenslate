# Decomposition — translation_config_axes

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_14-14__translation_config_axes/_branch.md` (with prior outputs `surfacing.md` and `sensemaking.md` in the same folder)

---

## The Whole Being Decomposed

The conceptual whole produced by sensemaking: **the 8-axis user-facing configuration layer of the Comprehenslate translation framework, sitting within a 4-layer architecture, using a set of named patterns (envelope-with-overrides, axis-vs-policy, conservative-bias defaults), with a set of relocated policies (multi-meaning preservation, register alternation, polysemy-via-grammar, nazm-as-meaning, no-smoothing) and 6 deferred frontier questions handed forward.**

The job of decomposition is to perceive the internal coupling topology and partition this conceptual whole into pieces that:
- Can each be specified independently
- Have explicit interfaces
- Order by dependency
- Cover the inquiry's deliverable when reassembled

---

## Step 1 — Perceive Coupling Topology

### Elements identified

| # | Element |
|---|---|
| E1 | The 8 axes (A1 RCL, A2 Domain Expertise, A3 Source-Culture Proximity, A4 Purpose/Use-case, A5 Source-Fidelity Stance, A6 Form-Preservation Strength, A7 Scaffolding Density, A8 Analysis Depth) |
| E2 | The 4 families (Reader, Purpose, Strategy, Depth) |
| E3 | The envelope-with-selective-override pattern (applied to RCL) |
| E4 | Per-axis level enumeration (DEFERRED to next inquiry) |
| E5 | Per-axis default selection (DEFERRED) |
| E6 | Default-derivation mechanism (Purpose → other axes' defaults) (DEFERRED) |
| E7 | Axis-value conflict resolution at runtime (DEFERRED) |
| E8 | POLICY layer (always-on rules, adjacent, out of scope) |
| E9 | SOURCE-DESCRIPTION layer (auto-detected, adjacent) |
| E10 | SYSTEM-FLAG layer (far, out of scope) |
| E11 | Per-axis prose descriptions for AI translator prompts (DEFERRED) |
| E12 | Pydantic schema shape (DEFERRED) |
| E13 | Escape hatch / free-form notes field (DEFERRED) |
| E14 | Envelope-axis NAMING (provisional name, load-bearing concept, refinement IN-SCOPE) |
| E15 | Set-level coverage check against user-side need-space (Region D) |
| E16 | Set-level orthogonality check (four-corners test per pair) |
| E17 | Language-agnosticism check per axis concept |
| E18 | Per-axis default justification mechanism (DEFERRED) |
| E19 | POLICY × axis runtime interaction logic (DEFERRED; cross-references in-scope) |
| E20 | Per-axis cardinality (3, 4, or 5 levels) |

### Coupling map (pairwise propagation analysis)

Strength scale: **STRONG** = change A → must change B; **MODERATE** = change A → may change B's contract; **WEAK** = change A → B unaffected; **NONE** = independent.

| Pair | Strength | Notes |
|---|---|---|
| E1 axis identity ↔ E3 envelope pattern | STRONG (within A1 only) | RCL's identity IS pattern-application; pattern definition affects RCL |
| E1 ↔ E14 envelope-axis naming | MODERATE | Name is the label; identity is conceptual. Rename → relabel |
| E1 ↔ E20 cardinality | MODERATE | Each axis carries its own cardinality; per-axis localized |
| E1 ↔ E4 level enumeration | STRONG (deferred) | Levels operationalize axis; without them the axis is abstract — but DEFERRED per C7 |
| E1 ↔ E5 default selection | STRONG (deferred) | Default is part of axis spec; DEFERRED |
| E1 ↔ E11 prose descriptions | STRONG (deferred) | Prose is how the axis operationalizes for the AI; DEFERRED |
| A4 Purpose ↔ E6 default-derivation | STRONG (deferred) | Purpose drives other axes' defaults |
| E1 ↔ E7 conflict resolution | MODERATE (deferred) | Cross-axis runtime mechanism |
| E1 ↔ E8 POLICY | WEAK-to-MODERATE | Most axes WEAK; A5 Source-Fidelity / A6 Form-Preservation MODERATE (interact with register-policy / nazm-policy) |
| E1 ↔ E9 SOURCE-DESCRIPTION | WEAK | Source-description informs runtime behavior, not axis identity |
| E1 ↔ E15 set-level coverage | MODERATE | Set property, depends on all axes spec'd |
| E1 ↔ E16 orthogonality | MODERATE | Property of pairs |
| E1 ↔ E17 language-agnosticism | WEAK at axis-concept level (universal); STRONG at level-enum level (DEFERRED) |
| E2 families ↔ E1 axes | WEAK | Families are navigational meta-grouping; not config units |
| E12 pydantic shape ↔ E1 | MODERATE (deferred) | Schema reflects identity; DEFERRED |
| E13 escape hatch ↔ E1 | WEAK | Schema-level, not per-axis |
| E18 default justification ↔ E5 | STRONG (both deferred) | Justification is part of default spec |
| E19 POLICY × axis interaction ↔ E8 | STRONG (deferred for logic, in-scope for cross-references) | |
| A1 RCL identity ↔ A2-A8 identities | WEAK | Per-axis identity is local; cross-axis is at set-level |
| A1's 5 sub-fields ↔ each other | MODERATE (within RCL) | Correlated in typical readers but orthogonal in principle |

### Clusters (peaks of high coupling)

- **Cluster 1 — Per-Axis Identity Spec** (each of A1–A8 + their sub-fields + pattern association + cardinality + family-membership + scope + boundary)
- **Cluster 2 — Set-Level Properties** (orthogonality across pairs, coverage of need-space, language-agnosticism check, family meta-grouping justification)
- **Cluster 3 — Patterns as reusable concepts** (envelope-with-overrides, axis-vs-policy distinction, conservative-bias defaults)
- **Cluster 4 — Framework architecture / layer separation** (4-layer architecture: USER-AXIS / POLICY / SOURCE-DESCRIPTION / SYSTEM-FLAG)
- **Cluster 5 — POLICY layer enumeration** (which principles relocate from axis to policy + their grounding)
- **Cluster 6 — Deferred / Future work** (level values, defaults, prose, pydantic, runtime mechanism, escape hatch, source-description schema, default-derivation logic, conflict resolution)

### Valleys (low-coupling regions)

| Boundary | Strength | Crossing traffic |
|---|---|---|
| Cluster 1 (per-axis identity) ↔ Cluster 2 (set-level properties) | MODERATE valley | Set-level checks REFERENCE axis identities; identity doesn't depend on set-level checks |
| Cluster 1 ↔ Cluster 3 (patterns) | LOW within A1 (RCL uses envelope), VOID across A2-A8 | A1 uses the pattern; others use plain ordinal |
| Cluster 1 ↔ Cluster 4 (architecture) | LOW | Architecture frames where axes live; axes don't determine architecture |
| Cluster 1 ↔ Cluster 5 (POLICY enumeration) | LOW | Cross-references named (e.g., A5 has associated register policy) but identities are independent |
| Cluster 1 ↔ Cluster 6 (deferred) | EXPLICIT BOUNDARY | Deferred items reference axes but are scoped out by C7+C8 |
| Cluster 4 ↔ Cluster 5 | LOW | Layer 2 IS POLICY layer; enumeration is downstream of architecture identity |
| Cluster 2 ↔ Cluster 6 | LOW | Set checks are part of THIS inquiry; per-axis runtime / pydantic / etc. are NOT |

---

## Step 2 — Detect Boundaries (Top-Down)

### Boundary set

| # | Boundary | Coupling strength across boundary | Rationale |
|---|---|---|---|
| **B1** | Per-axis identity ↔ Set-level properties | MODERATE (one direction only: set-level reads from axes) | Per-axis Q can be answered without doing set-level checks; set-level Qs depend on per-axis answers |
| **B2** | In-Scope (Layer 1) ↔ Out-of-Scope (Layers 2–4) | LOW | The user explicitly scoped this inquiry to Layer 1 |
| **B3** | This Inquiry's Work (meaning-layer axis identity) ↔ Deferred Future Work (level values, defaults, prose, pydantic, runtime) | EXPLICIT (user-set boundary per C7+C8) | C7+C8: "Again, first lets focus on axises for now." |
| **B4** | Per-axis (8 individual axis specs) ↔ Cross-axis (orthogonality, default-derivation, conflict-resolution) | LOW within Layer 1; defer cross-axis runtime to future | Each of A1–A8 specifiable independently; cross-axis properties grouped |
| **B5** | Pattern definitions ↔ Pattern applications | LOW | Envelope pattern is a reusable concept; its application to RCL is one instance |
| **B6** | A1 ↔ A2 ↔ … ↔ A8 (between individual axes within Cluster 1) | LOW (per-axis local) | Per the orthogonality verified in sensemaking; per-axis identity is independent |

### Initial partition

| Piece | Cluster | Rough description |
|---|---|---|
| **P1** | Cluster 4 | Framework architecture & layer separation (the 4-layer architecture, with Layer 1 in scope) |
| **P2** | Cluster 1 | The 8 axes, individually specified at the identity / meaning level. P2 sub-decomposes into P2.1–P2.8 |
| **P3** | Cluster 3 | The envelope-with-selective-override pattern (intent, application criteria, naming refinement = D6) |
| **P4** | Cluster 2 | Set-level properties (orthogonality, coverage, language-agnosticism, family meta-grouping) |
| **P5** | Cluster 5 | POLICY layer enumeration (which principles relocate, their grounding, cross-reference to axes) |
| **P6** | Cluster 6 + boundary marker | Scope boundaries (what this inquiry produces vs what's deferred, and to which subsequent inquiry) |

---

## Step 3 — Validate Boundaries (Bottom-Up Check)

### Atom identification

Irreducible elements:
- Each of 8 axis names (A1–A8 atoms)
- Each of A1's 5 sub-field names (vocabulary, syntactic processing, idiom recognition, inference, cultural-reference recognition)
- Each axis's core CONCEPT one-sentence (what it captures)
- Each of 4 family labels (Reader, Purpose, Strategy, Depth)
- Each of 4 layer labels (USER-FACING AXES, POLICY, SOURCE-DESCRIPTION, SYSTEM-FLAGS)
- The envelope-with-selective-override pattern (one atom)
- The AXIS-vs-POLICY distinction (one atom-relation)
- The conservative-bias-defaults principle (one atom)
- Each orthogonality claim per axis-pair (28 pairs from C(8,2))
- The language-agnosticism claim per axis (8 atoms)
- The relocated POLICY principles (5 atoms: multi-meaning preservation, register alternation, polysemy via grammar, nazm preservation, no smoothing)

### Atom-to-cluster mapping check

- The 8 axis-name atoms + 5 RCL sub-field atoms + concept-sentence atoms cluster into per-axis identity spec → **matches Cluster 1, B6 boundaries.** ✓
- Family labels (4) cluster as meta-grouping → **matches Cluster 2 P4 piece.** ✓
- Layer labels (4) cluster as architecture → **matches Cluster 4 P1 piece.** ✓
- Envelope pattern atom → **matches Cluster 3 P3 piece.** ✓
- Orthogonality claims (28 pairs) + language-agnosticism claims (8) + coverage check → **matches Cluster 2 P4 piece.** ✓
- AXIS-vs-POLICY distinction + conservative-bias principle → **straddles P3 and P5.** Resolution: AXIS-vs-POLICY belongs in P5's framing; conservative-bias belongs in P3 as a default-principle pattern (or in P6 as a deferred-defaults design rule). The atom-level evidence agrees with placement.
- Relocated POLICY principles (5) → **matches Cluster 5 P5 piece.** ✓

### Soft spot

The envelope-with-overrides pattern (atom) is associated tightly with RCL (Cluster 1, P2.1) but is also a reusable concept (Cluster 3, P3). Top-down put it in P3 (its own piece); bottom-up wants to keep it adjacent to A1. Resolution: P3 owns the pattern DEFINITION (reusable concept), and P2.1 (RCL) REFERENCES P3 as a dependency. The dependency direction is captured in Step 6.

### Confidence verdict

| Boundary | Top-down | Bottom-up | Confidence |
|---|---|---|---|
| B1 (per-axis ↔ set-level) | ✓ | ✓ | HIGH |
| B2 (in-scope ↔ out-of-scope) | ✓ | ✓ | HIGH |
| B3 (this inquiry ↔ deferred) | ✓ | ✓ (user-set) | HIGH |
| B4 (per-axis ↔ cross-axis) | ✓ | ✓ | HIGH |
| B5 (pattern definition ↔ application) | ✓ | ✓ with soft spot above | HIGH (with explicit dependency) |
| B6 (axis ↔ axis within Cluster 1) | ✓ | ✓ | HIGH |

All boundaries confident. Proceed.

---

## Step 4 — Express as Question Tree

### Top-level question (the whole)

**What is the correct set of axes for the Comprehenslate translation-configuration framework — defined at the meaning / identity level only — such that each axis is language-agnostic, ordinal-or-categorical for 3–5 levels, default-bearing in principle, orthogonal, the full set covers the user-side need-space, derivative output-properties are excluded, and the framework's surrounding architecture and policy relocations are clear?**

### Question tree

#### **P1 — Framework architecture & layer separation**

**Question:** What is the layered architecture within which the user-facing axes sit, which layer is in-scope for this inquiry, and what distinguishes USER-AXIS from POLICY at the conceptual level?

**Verification criteria:**
- [ ] The 4 layers are named: USER-FACING AXES / POLICY / SOURCE-DESCRIPTION / SYSTEM-FLAGS.
- [ ] Layer 1 (USER-FACING AXES) is explicitly identified as in-scope for this inquiry.
- [ ] Each out-of-scope layer is described in 1–2 sentences with a "deferred to its own inquiry" marker.
- [ ] The AXIS-vs-POLICY operational distinction is articulated (USER-AXIS = user-choice point with ordinal/categorical levels; POLICY = always-on system rule grounded in project values, applied regardless of any axis value).
- [ ] The criterion for relocation (USER-AXIS → POLICY) is stated: when a translation principle is unanimously prescribed by project values such that opting out would contradict project identity, it is POLICY, not axis.

---

#### **P2 — The 8 axes, individually specified at identity / meaning level**

**Question:** For each of the 8 axes, what is its identity — what concept does it capture, what user-facing question does it answer, what is its scope (what it controls) and boundary (what it doesn't control), what pattern does it use, what cardinality (3 / 4 / 5 levels), what family does it belong to, and does its concept operationalize language-agnostically?

**P2 sub-decomposes into 8 sibling sub-pieces (P2.1 through P2.8), one per axis. Each sub-piece carries the SAME verification shape:**

##### P2.X — Axis A.X identity (template; applied to each of the 8 axes)

**Verification criteria (applied per axis):**
- [ ] Provisional axis name selected (refinable in critique).
- [ ] One-sentence statement of the concept this axis captures.
- [ ] One-sentence statement of the user-facing question this axis answers.
- [ ] Pattern association declared (plain ordinal / categorical / envelope-with-selective-override).
- [ ] Cardinality claim with justification (3, 4, or 5 levels; uniform-5 NOT required).
- [ ] Family membership (Reader / Purpose / Strategy / Depth) with one-line justification.
- [ ] Scope statement: what this axis controls.
- [ ] Boundary statement: what this axis does NOT control (handed to other axes, to policy, or to derivative output-property emergence).
- [ ] Language-agnostic-operationalization claim: the axis concept works for any target language (not just English).

**Per-axis sub-pieces:**

- **P2.1 — A1 Reader Competence Level (RCL).** Additional verification:
  - [ ] The 5 sub-fields are named (vocabulary breadth, syntactic processing capacity, idiom recognition, inference capacity, cultural-reference recognition).
  - [ ] Use of the envelope-with-selective-override pattern is declared (depends on P3 being defined).
  - [ ] Each sub-field has a one-sentence concept statement.
  - [ ] The headline-vs-sub-field relationship is articulated (headline defaults propagate; per-sub-field overrides optional).

- **P2.2 — A2 Domain Expertise.** Verification as above; cardinality 3 (lay / general-educated / specialist).

- **P2.3 — A3 Source-Culture Proximity.** Verification as above; cardinality 3 (outsider / familiar / source-native).
  - [ ] Explicit statement of orthogonality vs A1's cultural-reference-recognition sub-field (competence-vs-identity distinction).

- **P2.4 — A4 Purpose / Use-case.** Verification as above; cardinality ~5 (categorical, not strictly ordinal).
  - [ ] Acknowledgement that A4's value MAY drive defaults for other axes (default-derivation; mechanism DEFERRED to P6).

- **P2.5 — A5 Source-Fidelity Stance.** Verification as above; cardinality 3 (heavily-foreignized / balanced / heavily-domesticated).
  - [ ] Cross-reference: associated POLICY = register-alternation preservation (named in P5).

- **P2.6 — A6 Form-Preservation Strength.** Verification as above; cardinality 5.
  - [ ] Connection to harmony_layer.md's Tier 1–4 system articulated; level enumeration deferred but level-structure principle stated.
  - [ ] Cross-reference: at A6 ≥ light, POLICY nazm-as-meaning preservation becomes active.

- **P2.7 — A7 Scaffolding Density.** Verification as above; cardinality 5 (off / minimal / standard / rich / scholarly).
  - [ ] Statement that A7 subsumes footnote-toggle, transliteration-toggle, parenthetical-gloss decisions from `.env.example` / sketched B2.
  - [ ] Statement that multi-meaning RENDERING (how policy-preserved polysemy surfaces) is controlled by A7's level.

- **P2.8 — A8 Analysis Depth.** Verification as above; cardinality 4 (surface / standard / deep / scholarly).
  - [ ] Connection to existing `.env.example` DEPTH_PROFILE (axis inherits the existing 4 levels).
  - [ ] Statement that A8 controls how much interpretive material accompanies the translation, distinct from A4 Purpose.

---

#### **P3 — The envelope-with-selective-override pattern**

**Question:** What is the envelope-with-selective-override pattern, what problem does it solve, when does it apply, and what is its final name?

**Verification criteria:**
- [ ] Pattern intent stated: one axis with a HEADLINE level + optional sub-field overrides; sub-field defaults propagate from the headline; per-sub-field override is `Optional` semantics.
- [ ] Problem solved stated: collapses N correlated sub-dimensions into one ergonomic configuration knob while preserving sub-dimension orthogonality for rare cases.
- [ ] Application criteria stated: use this pattern for an axis whose sub-dimensions are (i) empirically correlated in typical readers / users such that the joint distribution is clustered AND (ii) genuinely orthogonal in principle so that individual override matters for edge cases.
- [ ] Final name selected from candidates (envelope-with-selective-override / headline-with-sub-field-overrides / bundled-axis / compound-axis / multi-faceted-axis / other). Resolves frontier flag D6.
- [ ] RCL (A1) documented as the canonical instance.
- [ ] Note: the pattern is reusable; future axes that share its structure may adopt it. (No A2–A8 currently use it; this is forward-looking only.)

---

#### **P4 — Set-level properties: orthogonality, coverage, language-agnosticism, family meta-grouping**

**Question:** As a SET, do the 8 axes satisfy orthogonality (every pair is independent), coverage (every user-side need-dimension maps to one axis or to a documented policy / source-layer), language-agnosticism (every axis concept operationalizes for non-English target languages), and is the 4-family meta-grouping (Reader / Purpose / Strategy / Depth) structurally justified as a navigational aid?

**Verification criteria:**
- [ ] **Orthogonality:** For every pair of the 8 axes (28 pairs), the four-corners test is documented (each axis-pair has a populated joint-distribution at all four extremes). Pairs with stress: A1 sub-field "cultural-reference-recognition" × A3 Source-Culture Proximity; A4 Purpose × A5 Source-Fidelity Stance; A2 Domain Expertise × A3 Source-Culture Proximity; A5 × A6; A7 × A8.
- [ ] **Coverage:** Every user-side need-dimension from surfacing Region D (D1 WHO, D2 WHY, D3 source-culture relationship, D4 scaffolding tolerance, D5 source-vs-target priority, D6 medium, D7 action-after-reading, D8 time/intensity, D9 first vs re-reading) maps to one or more axes, OR is documented as out of scope with a reason, OR is documented as belonging to POLICY / SOURCE-DESCRIPTION / SYSTEM-FLAG layer.
- [ ] **Language-agnosticism:** Every axis concept is concrete-tested against ≥2 non-English target-language scenarios (e.g., Russian, Japanese, Arabic). Per-axis pass/fail with rationale; level-enum thresholds are out of scope (deferred per P6).
- [ ] **Family meta-grouping justification:** Each family (Reader / Purpose / Strategy / Depth) is described in one sentence; each axis's assignment is justified; meta-grouping is explicitly documented as navigational, not a configuration unit.

---

#### **P5 — POLICY layer enumeration: principles relocated from user-axis to always-on**

**Question:** Which translation principles, after this inquiry, become POLICY (always-on system rules) rather than user-axes, and what is the project-value grounding for each?

**Verification criteria:**
- [ ] Each relocated principle is named:
  - Multi-meaning preservation (always preserve when grammar permits; rendering controlled by A7 Scaffolding Density)
  - Register alternation preservation (no lifting plain registers to ornate; grounded in memory H1)
  - Polysemy resolution via local construction (local grammatical construction trumps surrounding metaphor; grounded in memory H2)
  - Nazm / form-as-meaning preservation (active when A6 ≥ light; grounded in harmony_layer.md Tier system)
  - No smoothing of difficult / uncomfortable nuances (grounded in `notes.md` / `translation_principals.md` principle on lesser-evil)
- [ ] For each relocated principle, the project source is cited (file or memory identifier).
- [ ] For each principle, the cross-reference to associated axes is documented (e.g., register-policy interacts with A5 but is independent of A5's value).
- [ ] The full OPERATIONAL specification of each policy (what each policy ENFORCES at the translator-runtime layer) is DEFERRED to a separate POLICY-layer inquiry per P6.

---

#### **P6 — Scope boundaries: deliverable vs deferred**

**Question:** What is the deliverable of THIS inquiry, and what is explicitly deferred to which subsequent inquiry?

**Verification criteria:**
- [ ] Deliverable enumerated:
  - The 8 axes specified at meaning / identity level (P2)
  - The envelope-with-selective-override pattern named and defined (P3, incl. D6 resolution)
  - Set-level properties verified (P4)
  - POLICY relocations enumerated (P5)
  - Framework architecture stated (P1)
- [ ] Deferred items enumerated with target inquiry:
  - Per-axis level VALUES → **NEXT inquiry: level enumeration**
  - Per-axis DEFAULT values → **NEXT or NEXT-NEXT inquiry: defaults**
  - Per-axis prose descriptions for AI translator prompts → **FUTURE inquiry: prompt operationalization**
  - Pydantic dataclass shape → **FUTURE inquiry: structural-layer artifact**
  - POLICY layer operational specifications → **SEPARATE inquiry: policy-layer**
  - SOURCE-DESCRIPTION schema → **SEPARATE inquiry: source-description**
  - SYSTEM-FLAG documentation → **SEPARATE inquiry or already in `.env.example`**
  - Runtime conflict-resolution mechanism (frontier D1) → **FUTURE: runtime behavior**
  - Default-derivation mechanism between axes (frontier D2 + Purpose-drives-defaults) → **FUTURE: defaults**
  - POLICY × axis interaction logic (frontier D3) → **FUTURE: policy-layer**
  - Escape hatch design (frontier D4) → **FUTURE: schema-layer**
  - Pydantic shape for envelope pattern (frontier D5) → **FUTURE: structural-layer**
- [ ] Each deferred item has a one-line statement of why it's deferred (the user's explicit scope or downstream dependency).

---

## Step 5 — Map Interfaces

### Interface inventory

| Source → Target | Direction | What flows |
|---|---|---|
| P1 → P2 | one-way | Layer-1 context: "axes live in USER-FACING AXES layer." Provides the architectural frame within which each axis identity is specified. |
| P1 → P5 | one-way | Layer-2 identity: "POLICY is layer 2." P5 enumerates the contents of layer 2. |
| P1 → P6 | one-way | The 4-layer separation underpins scope. P6 consumes for "deferred to layer-X inquiry" annotations. |
| P3 → P2.1 | one-way (strong) | The envelope-with-selective-override pattern DEFINITION. P2.1 (RCL) references the pattern as its association. RCL CANNOT be fully spec'd until P3 is defined. |
| P2.1 → P3 | one-way (provides example) | RCL serves as the canonical instance. P3's "documented example" verification criterion references P2.1. |
| P2.1–P2.8 → P4 | one-way (set-level reads from per-axis) | The 28 orthogonality pairs, coverage check, language-agnosticism check, and family meta-grouping check ALL consume per-axis identity from P2. |
| P2 ↔ P5 | bidirectional | Cross-references between axis (P2.5 A5, P2.6 A6) and associated POLICY items. The axis spec NAMES the policy; the policy enumeration NAMES the associated axis. Neither side defines the other; both reference shared concepts. |
| P2, P3, P4, P5 → P6 | one-way (synthesis) | P6 synthesizes "what this inquiry produces" from all sibling pieces. |
| P2 → deferred-future-inquiry-level-values | one-way (provides) | The axis identity is precondition for level enumeration (next inquiry). |
| P2 → deferred-future-inquiry-defaults | one-way (provides) | The axis identity + cardinality is precondition for default selection. |
| P5 → deferred-policy-layer-inquiry | one-way (provides) | The list of relocated principles is precondition for their operational specification. |

### Assumptions-not-data check (per refinement note)

What ASSUMPTIONS does each piece make about what the others provide?

| Piece | Assumption made about... | Captured? |
|---|---|---|
| P2 (all axis sub-pieces) | …P1's layer separation is correct (axes live in Layer 1 only) | YES — explicit cross-reference |
| P2.1 (RCL) | …P3's pattern definition is general enough that "RCL uses this pattern" is a meaningful claim | YES — P3 verification "application criteria" addresses this |
| P4 | …P2 has spec'd all 8 axes consistently (same shape per axis) | YES — P2 verification template enforces same shape |
| P4 orthogonality check | …per-axis identity is determinate enough to evaluate orthogonality. Risk: if A1's envelope pattern leaves sub-fields underspecified, A1 × A3 orthogonality (RCL.cultural-reference-recognition × Source-Culture Proximity) can't be checked. | CAPTURED — P2.1 verification requires sub-field concept-statements; P2.3 verification requires orthogonality cross-reference to A1 sub-field |
| P5 | …project values cited (notes.md, memory H1, etc.) survive across the inquiry. Risk: if project values change after this inquiry, P5's grounding may become stale. | CAPTURED — each principle's source is cited with timestamp implicit in inquiry date |
| P5 (cross-reference to axes) | …P2 has spec'd the axes that this policy references | YES — explicit dependency on P2 |
| P6 | …all deferred items are TRULY deferred (no hidden coupling that makes the inquiry's deliverable depend on an item P6 claims is out of scope) | CAPTURED — every deferred item has a "why deferred" rationale; the deliverable is meaning-layer only |

No hidden assumptions identified. The interface map is explicit.

---

## Step 6 — Order by Dependency

### Dependency DAG

```
                        ┌─────────────────────────────┐
                        │  P1: Framework architecture │
                        │  & layer separation         │
                        └──────────────┬──────────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
              ▼                        ▼                        ▼
   ┌─────────────────┐       ┌───────────────────┐    ┌──────────────────────┐
   │ P3: Envelope    │       │ P2.2–P2.8         │    │ P5: POLICY           │
   │ pattern         │       │ (axes A2–A8, in   │    │ enumeration          │
   │ definition      │       │ parallel)         │    │                      │
   └────────┬────────┘       └─────────┬─────────┘    └──────────┬───────────┘
            │                          │                          │
            ▼                          │                          │
   ┌─────────────────┐                 │                          │
   │ P2.1: RCL (A1)  │                 │                          │
   │ uses pattern    │                 │                          │
   └────────┬────────┘                 │                          │
            │                          │                          │
            └──────────┬───────────────┘                          │
                       │                                          │
                       ▼                                          │
            ┌──────────────────────┐                              │
            │ P4: Set-level checks │                              │
            │ (orthogonality,      │                              │
            │  coverage, lang-     │                              │
            │  agnostic, family)   │                              │
            └──────────┬───────────┘                              │
                       │                                          │
                       └──────────────┬───────────────────────────┘
                                      │
                                      ▼
                          ┌─────────────────────┐
                          │ P6: Scope synthesis │
                          │ (deliverable +      │
                          │  deferred)          │
                          └─────────────────────┘
```

### Ordering summary

| Stage | Pieces (parallelizable within stage) | Dependency |
|---|---|---|
| **Stage 1** | P1 | None (the architectural frame) |
| **Stage 2** | P3, P2.2, P2.3, P2.4, P2.5, P2.6, P2.7, P2.8, P5 (all parallel) | Each depends only on P1 |
| **Stage 3** | P2.1 (RCL) | Depends on P3 (pattern definition) AND P1 |
| **Stage 4** | P4 | Depends on all of P2.1–P2.8 |
| **Stage 5** | P6 | Depends on all prior pieces |

### Circular-dependency check

P2.1 ↔ P3 is BIDIRECTIONAL at the interface level (P3 cites RCL as example; P2.1 references P3 as its pattern). However, the dependency is NOT circular at the work-order level: P3's pattern definition is **conceptual / abstract** (works without RCL's specifics); P2.1 needs the pattern defined before it can be applied. The "RCL as example" verification in P3 can be satisfied by a one-line reference once P2.1 is spec'd; P3 does NOT depend on P2.1's content to define the pattern. Resolved: P3 → P2.1 one-way at the BUILD level.

No other circular dependencies.

---

## Step 7 — Self-Evaluate

### Minimum 3 dimensions

#### Independence — PASS

- **P1**: Can be answered without other pieces. Architectural framing is self-contained. ✓
- **P2.2–P2.8**: Each axis identity is locally specifiable given P1. Per-axis answers do not depend on sibling axis answers (orthogonality moved to P4). ✓
- **P2.1 (RCL)**: Specifiable once P3 is defined. Within-piece coupling to P3 is explicit and ordered. ✓
- **P3**: Pattern definition is conceptually self-contained. Can be defined without specific axis instances. ✓
- **P4**: PASS-WITH-DEPENDENCY (must wait for P2.1–P2.8). Within-stage independence is fine. ✓
- **P5**: Can be answered given P1 + project-value sources. Cross-references to axes are flags, not blocking dependencies. ✓
- **P6**: Synthesis piece; requires all prior outputs. Within its stage, self-contained. ✓

All pieces are independently workable in their dependency order. **PASS.**

#### Completeness — PASS

The inquiry's whole (the 8-axis user-facing layer at meaning level + architecture + policy relocations + scope boundary). Coverage check:

**Against inquiry constraints C1–C11:**
- C1 language-agnostic → P4 set-check ✓
- C2 3–5 levels each → P2 per-axis cardinality ✓
- C3 default-bearing → P3 conservative-bias principle stated; per-axis values DEFERRED via P6 ✓
- C4 orthogonal → P4 four-corners check ✓
- C5 full coverage of user-side need-space → P4 coverage check ✓
- C6 no derivative output-properties → P2 per-axis scope/boundary articulation ✓
- C7 stop at axis identity → P6 scope statement ✓
- C8 stop at axis identity (no pydantic) → P6 scope statement ✓
- C9 register as policy → P5 enumeration ✓
- C10 polysemy as policy → P5 enumeration ✓
- C11 sensible defaults (typical user overrides 1–2) → P3 conservative-bias principle + DEFERRED full defaults to next inquiry per P6 ✓

**Against sensemaking's 6 frontier flags D1–D6:**
- D1 axis-value conflicts at runtime → DEFERRED in P6 ✓
- D2 per-axis default justification mechanism → DEFERRED in P6 ✓
- D3 POLICY × axis interaction logic → PARTIALLY in P5 cross-references; full logic DEFERRED in P6 ✓
- D4 escape hatch → DEFERRED in P6 ✓
- D5 envelope-axis typed structure → DEFERRED in P6 ✓
- D6 envelope-axis naming refinement → IN-SCOPE in P3 ✓

**Against sensemaking's 4 stabilized patterns:**
- Envelope-with-overrides → P3 ✓
- Axis-vs-policy distinction → P1 + P5 ✓
- Family meta-grouping → P4 ✓
- Conservative-bias defaults → P3 (within pattern) and noted in P6 (deferred values) ✓

**Against the 8 axes themselves (Layer 1 USER-FACING):**
- A1 RCL → P2.1 ✓
- A2 Domain Expertise → P2.2 ✓
- A3 Source-Culture Proximity → P2.3 ✓
- A4 Purpose/Use-case → P2.4 ✓
- A5 Source-Fidelity Stance → P2.5 ✓
- A6 Form-Preservation Strength → P2.6 ✓
- A7 Scaffolding Density → P2.7 ✓
- A8 Analysis Depth → P2.8 ✓

**Against POLICY layer items:**
- All 5 relocated principles → P5 ✓

**Against Layer 3 + 4:**
- SOURCE-DESCRIPTION → DEFERRED in P6 ✓
- SYSTEM-FLAG → DEFERRED in P6 ✓

No gaps. **PASS.**

#### Determination-mechanism piece check (per refinement note)

Load-bearing concepts whose use depends on a RUNTIME determination?

| Concept | Determination type | Runtime mechanism needed? |
|---|---|---|
| AXIS identity | Design-time | NO |
| POLICY identity | Design-time | NO |
| Envelope pattern application | Design-time (next inquiry will decide per axis) | NO |
| Orthogonality (per pair) | Design-time (four-corners test) | NO |
| Language-agnostic operationalization | Design-time (concrete check) | NO |
| Cardinality per axis | Design-time | NO |

All load-bearing concepts are settled at design-time. No runtime-determination piece needed. The deferred items (D1 runtime conflict, D3 policy×axis runtime, D5 schema runtime) DO involve runtime determinations, but they are EXPLICITLY DEFERRED via P6 to their own inquiries — the deferral itself addresses the determination-mechanism question for this inquiry. **PASS.**

#### Reassembly — PASS

Given:
- P1 answered: 4-layer architecture + axis-vs-policy distinction
- P2.1–P2.8 answered: each axis with name, concept, question-it-answers, pattern, cardinality, family, scope, boundary, language-agnostic claim
- P3 answered: envelope pattern defined + named (D6 resolved)
- P4 answered: orthogonality, coverage, language-agnosticism, family meta-grouping all verified at set level
- P5 answered: 5 relocated principles named, grounded, cross-referenced
- P6 answered: deliverables enumerated, deferred items handed off with target inquiries

Reconstruct the original inquiry's deliverable: "the correct set of axes, language-agnostic, ordinal/categorical 3–5 levels, default-bearing, orthogonal, covering user-side need-space, excluding derivative output-properties." Each clause maps to a verified verification criterion. **PASS.**

### Optional full evaluation (4 additional dimensions)

#### Tractability — PASS

- P1: 1 focused pass (~½ page).
- P2.X (each of 8): 1 focused pass per axis (~½ page each).
- P3: 1 focused pass (~½ page).
- P4: 1 focused pass with sub-checks (orthogonality is the heaviest sub-check; manageable).
- P5: 1 focused pass (~½ page).
- P6: 1 focused synthesis pass.

Each piece tractable. **PASS.**

#### Interface clarity — PASS

All 10 interfaces in Step 5 are explicit. Assumptions-not-data check found no hidden coupling. **PASS.**

#### Balance — PASS WITH NOTE

| Piece | Approximate complexity |
|---|---|
| P1 | small |
| P2.1 (RCL) | medium-large (envelope pattern + 5 sub-fields) |
| P2.2 – P2.8 | small-medium each |
| P3 | medium (definition + naming refinement) |
| P4 | medium-large (28 orthogonality pairs + coverage + language-agnosticism + family) |
| P5 | medium (5 principles) |
| P6 | small (synthesis / enumeration) |

P2 is the largest cluster but sub-decomposes evenly into 8 pieces. P4 carries dense set-level checks. No single piece is 80% of total work. **PASS** with the note that P4 is concentrated work (28 orthogonality pairs); innovation may want to test whether the 28-pair check needs decomposition into per-pair-family clusters.

#### Confidence — PASS

Top-down and bottom-up agreed on all 6 boundaries (Step 3). **PASS, HIGH confidence.**

---

## Failure Modes Cross-Check

- **Premature Decomposition** — No: sensemaking stabilized the whole at SV6 before decomposition started.
- **Wrong Boundaries** — No: bottom-up validation confirmed the 6 boundaries.
- **Hidden Coupling** — Checked at Step 5; assumptions-not-data check found no hidden coupling.
- **Missing Pieces** — Completeness check passed all 11 constraints + 6 frontier flags + 8 axes + 5 policies.
- **Over-Decomposition** — 6 main pieces (+ 8 P2 sub-pieces) reflects the inquiry's structure; no piece is trivial.
- **Ignoring Dependencies** — Step 6 ordering DAG explicit.
- **Imbalanced Decomposition** — P4 has concentrated work but doesn't dominate; balance acceptable.

---

## Final Deliverable

### Coupling Map (Step 1)

6 clusters, 6 boundaries, all evaluated for coupling strength. Cluster 1 (per-axis identity) holds the bulk of the work; Cluster 6 (deferred future work) is explicitly out of this inquiry.

### Question Tree (Step 4)

```
TOP — What are the correct axes for the framework at meaning level?
├── P1 — Framework architecture & layer separation (4 layers; axis-vs-policy distinction)
├── P2 — The 8 axes individually specified at identity level
│       ├── P2.1 — A1 RCL (uses envelope pattern; 5 sub-fields)
│       ├── P2.2 — A2 Domain Expertise (3 levels)
│       ├── P2.3 — A3 Source-Culture Proximity (3 levels)
│       ├── P2.4 — A4 Purpose/Use-case (~5 levels, categorical)
│       ├── P2.5 — A5 Source-Fidelity Stance (3 levels)
│       ├── P2.6 — A6 Form-Preservation Strength (5 levels; Tier 1–4 tie)
│       ├── P2.7 — A7 Scaffolding Density (5 levels)
│       └── P2.8 — A8 Analysis Depth (4 levels; inherits DEPTH_PROFILE)
├── P3 — Envelope-with-selective-override pattern (definition + naming refinement = D6)
├── P4 — Set-level properties (orthogonality / coverage / language-agnosticism / family)
├── P5 — POLICY layer enumeration (5 relocated principles + grounding + cross-references)
└── P6 — Scope boundaries (deliverable + deferred-with-target-inquiry)
```

### Interface Map (Step 5)

10 explicit interfaces documented. Bidirectional only at the P2 ↔ P5 cross-reference level and at the P3 → P2.1 / P2.1 → P3 example-relationship level — both resolved with one-way build-order in Step 6.

### Dependency Order (Step 6)

5 stages:
1. P1 (alone)
2. P3, P2.2, P2.3, P2.4, P2.5, P2.6, P2.7, P2.8, P5 (all parallel)
3. P2.1 (RCL, after P3)
4. P4 (after all P2.x)
5. P6 (synthesis)

### Self-Evaluation (Step 7)

| Dimension | Verdict |
|---|---|
| Independence | PASS |
| Completeness | PASS |
| Reassembly | PASS |
| Determination-mechanism | PASS (no runtime determinations in scope) |
| Tractability | PASS |
| Interface clarity | PASS |
| Balance | PASS (P2 is largest cluster; sub-decomposes evenly) |
| Confidence | PASS (top-down + bottom-up agree on all 6 boundaries) |

All 8 dimensions pass. Decomposition stable. Ready for Innovation.

---

## Frontier handed to Innovation

Innovation should generate alternatives / candidates for the open design points within the pieces — particularly:

1. **D6 / P3 — Naming of the envelope-with-selective-override pattern.** Candidates to generate: envelope-with-selective-override / headline-with-sub-field-overrides / bundled-axis / compound-axis / multi-faceted-axis / parent-child-axis / aggregate-axis / composite-axis / overridable-default-bundle. Innovation enumerates and Critique selects.

2. **P2 axis naming refinements.** The user's sketched names (Reader Competence Level, Source-Fidelity Stance, Source-Culture Proximity, Domain Expertise) are workable but candidates may improve clarity, brevity, or user-language alignment. Each axis's name is a candidate-generation opportunity.

3. **P4 family naming.** "Reader / Purpose / Strategy / Depth" is the working set. Alternatives might better encode the meta-distinction (e.g., "About-the-Reader / About-the-Goal / About-the-Method / About-the-Material-Surfaced") or might use translation-theory terms.

4. **P6 — Default-bearing principle alternatives.** Conservative-bias was committed but alternative principles exist: opinionated-bias (match the project's typical use); minimal-defaults (no defaults; require the user to set everything); preset-bundles (predefined Purpose-driven defaults). Innovation enumerates; critique selects.

5. **A4 Purpose levels — categorical or ordinal?** The pattern association notes "categorical, not strictly ordinal." Innovation may generate alternatives: pure-categorical / partially-ordinal / preset-bundle-driven / hybrid.

These are the candidate-generation points where Innovation operates. The 8-axis identity itself is settled at sensemaking SV6 + this decomposition; Innovation does not re-open axis identity.
