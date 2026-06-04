# Surfacing — dissolve_meta_principle_entry_split_research

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-04_02-41__dissolve_meta_principle_entry_split_research/_branch.md`

Purpose: research the S6 candidate (dissolve `harmony_layer.md`'s meta-principle/entry split). Three threads: (1) what does the dissolved form look like concretely; (2) why does the prior meta-principle adoption recommendation feel "too big"; (3) does dissolution meet efficient/elegant/future-proof criteria.

Territory: prior findings (where S6 was parked); `harmony_layer.md` (the doc being redesigned); sibling docs for shape comparison; in-domain knowledge about self-justifying spec design.

## Mode + Entry Point

- **Mode:** hybrid (artifact + possibility). Artifact items pre-exist (prior findings; framework docs); possibility items are dissolved-form design candidates generated for this inquiry's purpose.
- **Entry point:** signal-first.
- **Sub-phase fired:** no.

## Traversal Trace

### Region A — Prior inquiries' context on S6
*(mtimes earlier captured)*

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 1 | A-prior-inquiry-2-S6: "Dissolve meta-principle/entry split" parked as RESEARCH FRONTIER with reasoning "loses the abstraction value (a single principle generating many classifications)" + "heavy restructure violates easy criterion" | core | HIGH | The user is now revisiting this. The "loses abstraction value" objection is what this inquiry must address. |
| 2 | A-prior-inquiry-1-S1: "Rules-with-violations restructure" (each entry is a pattern with positive + negative readings). ACTIONABLE-INCREMENTAL — apply to new entries; defer wholesale. | core | HIGH | Adjacent shape. S1 keeps a doc-level meta-principle but each entry is internally structured as pattern+violation. Different from S6's full dissolution. |
| 3 | A-Tier-3-pattern (≥12 entries with vulnerable template) | core | HIGH | The contradictions are EVIDENCE for dissolution — they show the meta-principle/entry split is failing at the entry-justification level. Each Tier 3 entry's justification IS the kind of self-contained rationale dissolution would make standard. |
| 4 | A-MVD-cost-profile (≈15-30 min day-one + 15-60 min sweep + ~1 min/entry ongoing) | core | HIGH | The cost profile the user says is "too big." Surfacing the actual cost breakdown is needed for diagnosing what specifically feels too big. |
| 5 | A-prior-inquiry-2-FP-1: principle-as-statement vs principle-as-test distinction | core | HIGH | The meta-principle adoption converts statement→test, adding procedural overhead per entry. Dissolution makes this distinction moot — each entry IS its own statement. No conversion needed. |

### Region B — `harmony_layer.md` current state (artifact)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 6 | B-current-structure: meta-principle stated separately (lines ~29-30) + 4 tier sections with per-entry justifications | core | HIGH | The structure to be dissolved. Verified by file inspection earlier in this conversation chain. |
| 7 | B-Tier-1-entries (~10 entries): each has form "X — because [meaning-carrying reason]" | core | HIGH | Tier 1 entries are ALREADY self-justifying in form — each entry's "because" clause is the principle's application. The dissolved form may not need to change Tier 1 entries much. |
| 8 | B-Tier-2-entries (~12 entries): similar form "X — because [comprehension-support reason]" | core | HIGH | Same observation as B-7. Tier 2 entries are already self-justifying. |
| 9 | B-Tier-3-entries (~12 entries): form "X — [positive aspect] but doesn't [meaning-claim]" with vulnerable negative claim | core | HIGH | This is the contested section. The vulnerable template is what dissolution would replace with scoped self-justifying claims. |
| 10 | B-Tier-4-entries: form "X — [technical infeasibility claim]" | core | HIGH | Different vulnerability pattern (technical impossibility, not negative-meaning-claim). Less affected by dissolution. |
| 11 | B-observation: the tier LABELS (1/2/3/4) carry sorting information that the per-entry text doesn't always make explicit | core | HIGH | The tiers' SORTING role is what dissolution must replace with another sorting mechanism (or eliminate the need for sorting). |

### Region C — Sibling docs for shape comparison

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 12 | C-notes.md-shape: flat list of ~60 principles each framed as "Comprehenslate should detect X" | core | HIGH | notes.md is ALREADY in a dissolved-shape form. No meta-principle; each entry stands alone with embedded reasoning. Evidence that dissolution works in the same project. |
| 13 | C-translation_principals.md-shape: similar to notes.md but larger | core | HIGH | Same shape. Both flat self-justifying lists. The user's framework ALREADY uses dissolved-form for principle-shaped content. |
| 14 | C-advanced_principles.md-shape: each entry elaborates one principle with worked example | core | HIGH | Each example IS the principle's application — no separate meta-principle, no separate principle, no tier system. Fully self-justifying. |
| 15 | C-terminology.md-shape: term + canonical definition; "this file wins" authority claim | sub | MEDIUM | Different content but same shape: each entry is self-defining. No meta-principle generating definitions. |
| 16 | **C-observation: harmony_layer.md is the OUTLIER among framework docs — it's the only one with a meta-principle + classification structure. The others are all self-justifying flat lists or expository examples.** | **core** | **HIGH** | **This is a major finding. The user's framework already prefers dissolved form everywhere except harmony_layer.md. Dissolution would bring harmony_layer.md into shape-parity with the other docs.** |

### Region D — Possibility space: dissolved-form designs

| # | Design | Relevance | Conf | Note |
|---|---|---|---|---|
| 17 | D1: pure self-justifying entries with embedded "why" clause. Example: *"Word order — meaning-carrying when source uses syntactic position for emphasis/restriction; sacrifice freely only when target language can't replicate without distortion."* No tier label; the why-clause carries the priority. | core | HIGH | Minimal addition to existing entry shape. Mostly works for Tier 1/2 entries that already have "because" clauses. |
| 18 | D2: PRESERVE-WHEN / SACRIFICE-WHEN structure per entry. Example: *"Register — PRESERVE when source uses register alternation as structural device; SACRIFICE when source is register-uniform."* The clauses ARE the principle application; no separate meta-principle needed. | core | HIGH | Most directly addresses the Tier 3 vulnerability (universal negative claims). Each entry is scoped at authoring time. |
| 19 | D3: pattern catalog (each entry is a named pattern with worked example + failure mode + corrective). Example: *"register-alternation pattern: source uses plain folk register grounding elevated theological register; preserve the contrast; failure mode: register pull-up (uniform target register); corrective: section-by-section register check."* | sub | MEDIUM | Verbose. Resembles the failure-modes catalog from prior inquiry 1's EA-6. Combines well with that work but heavier per entry. |
| 20 | D4: decision-tree-style entries with branching conditions. Example: *"Register: does source use register-alternation? YES → preserve (Tier-1-equivalent). NO → preserve when comfortable; sacrifice when target requires shift."* | sub | LOW | Procedural-feeling; reads less naturally; risks over-formalizing what is essentially a judgment call. |
| 21 | D5: recipe-style "DO/DON'T" entries. Example: *"Register: DO preserve when alternation marks structural device; DON'T preserve when alternation is incidental style drift."* | sub | MEDIUM | Tight; doesn't require "always/sometimes/never" framing. The condition for DO/DON'T is built into the rule. |
| 22 | D6: risk-driven entries paired with their failure modes. Example: *"Register failure mode: register pull-up (plain folk → ornate English). Prevention: per-section register match-check."* | sub | MEDIUM | Restructures the spec around failure modes rather than positive principles. Heavy shift; close to the failure-modes catalog from prior inquiry 1. |
| 23 | D7: hybrid principle-application inline. Example: *"Register — meaning-carrying when alternation present (because alternation IS the rhetorical move). Default: preserve. Sacrifice condition: source is register-uniform AND target requires shift for naturalness."* | core | HIGH | Combines D1's embedded reasoning with D2's preserve/sacrifice condition. Most expressive. Slightly heavier than D2. |

### Region E — In-domain knowledge: self-justifying spec patterns

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 24 | E-style-guides (Strunk & White, Google Style Guide): each rule stated with example + brief rationale; no separate "meta-principle" section; the rules collectively imply the style philosophy | core | HIGH | Established pattern. Successful style guides ARE flat self-justifying rule lists. The meta-principle/entry split is not standard. |
| 25 | E-case-law: each ruling self-contained with reasoning; precedent emerges from accumulation, not from a separate meta-rule doc | core | HIGH | Self-justifying entries scale to enormous corpora (centuries of common law) without needing a meta-principle to generate them. Strong future-proof signal. |
| 26 | E-API-docs: each endpoint documented standalone (parameters, behavior, errors); no meta-principle generating endpoints | sub | HIGH | Engineering convention. API docs grow indefinitely without restructuring the meta-level. |
| 27 | E-recipe-books: instructions include embedded rationale ("knead until smooth; don't overknead because gluten becomes tough") | sub | MEDIUM | Embedded rationale is the norm in instructional writing. |
| 28 | E-wiki-pages: each entry self-contained; categories emerge from links, not from a tiered hierarchy | sub | MEDIUM | Self-organization scales; explicit hierarchy doesn't always scale. |
| 29 | E-pattern-language (Christopher Alexander's "A Pattern Language" for architecture; design patterns in software): each pattern is self-justifying with name + problem + solution + consequences; patterns reference each other but no meta-principle generates them | core | HIGH | The pattern-language form is well-matched to the framework's content. Each pattern stands alone but composes with others. |
| 30 | E-knowledge: a meta-principle's value is AMORTIZED ACROSS ENTRIES — it generates many entries from one statement. If the per-entry overhead of testing against the meta-principle exceeds the amortization benefit, dissolution wins on efficiency | core | HIGH | The break-even analysis: meta-principle is worth it when you have many entries AND the principle is stable. Dissolution wins when entries are FEW or the principle is UNSTABLE. |
| 31 | E-knowledge: meta-principles create READING-TIME coordination cost (reader must understand BOTH meta-principle AND entries; mismatch between the two creates the contradictions this whole chain has been diagnosing) | core | HIGH | Self-justifying entries eliminate the meta-vs-entry coordination problem by removing the meta layer. |
| 32 | E-knowledge: in evolving documents, meta-principles ossify — they're hard to revise without invalidating all derived entries. Self-justifying entries allow per-entry revision without cascading invalidation | core | HIGH | Direct future-proof argument: self-justifying entries handle framework evolution better than meta-principle-derived entries. |

### Region F — Cost profile of meta-principle adoption (what "too big" diagnoses)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 33 | F-cost-1: meta-principle edit in `harmony_layer.md` — ~10 min one-time. SMALL. | sub | HIGH | Not the "too big" cost. |
| 34 | F-cost-2: Doc Consistency Audit section (5 items) — ~5 min one-time. SMALL. | sub | HIGH | Not the "too big" cost. |
| 35 | F-cost-3: retroactive sweep over ≥12 Tier 3 entries — ~15-60 min ONE-TIME. MODERATE. | sub | HIGH | Bounded effort; not the recurring "too big." |
| 36 | F-cost-4: per-entry application trace for new entries — ~30 sec per entry ONGOING. SMALL per entry; ACCUMULATES across the doc's lifetime. | core | HIGH | The user authors entries over time. Each future entry pays ~30 sec for the trace. Over hundreds of entries this adds up but per-entry it's small. |
| 37 | F-cost-5: EXCEPT-WHEN clauses on negative claims — ~1 line per entry where applicable. SMALL per entry but adds to doc length. | sub | HIGH | Affects readability of the doc; not crippling. |
| 38 | **F-cost-6: COGNITIVE LAYERING — the doc now has TWO levels (meta-principle + entries). Reader/author must hold both in mind. Conceptual complexity grows multiplicatively.** | **core** | **HIGH** | **This is likely the dominant "too big" cost. Not effort in minutes — complexity in concepts. The doc was simple (entries with reasons); now it has a layer above plus a procedural overlay (test + audit + trace).** |
| 39 | **F-cost-7: LOCK-IN — once the meta-principle is committed, revising it requires re-validating ALL derived entries. The framework loses the ability to evolve the priority criterion without cascading rework.** | **core** | **HIGH** | **Future-proof concern made concrete. Self-justifying entries don't lock in.** |
| 40 | F-cost-8: VOCABULARY EXPANSION — the framework now has "principle-as-test," "EXCEPT-WHEN," "Doc Consistency Audit," "per-entry application trace." Reader must learn these to use the framework. | core | MEDIUM | Vocabulary creep adds learning cost for any future contributor (or future-self). |

### Region G — User's 3 criteria operationalized

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 41 | G-efficient: minimum authoring overhead per entry; minimum total token count in the doc; minimum cognitive load when reading | core | HIGH | Self-justifying entries (D1/D2/D7) lower per-entry overhead because there's no separate test to run, no trace to record, no audit checklist to maintain. |
| 42 | G-elegant: parsimony (no separate meta-level needed); self-evidence (reading the entry IS understanding the priority); coherence (no risk of meta-vs-entry contradiction by construction) | core | HIGH | Self-justifying entries are inherently more elegant — the priority IS the entry's reason. No two-level coordination needed. |
| 43 | G-future-proof: framework grows without rewriting old entries; new failure modes are absorbed as new entries (or new conditions in existing entries) without restructuring; vocabulary doesn't need to be relearned | core | HIGH | Self-justifying entries handle growth by accretion (add new entry) or refinement (add condition to existing entry); meta-principle approach handles growth by re-deriving from the principle (and risks cascading invalidation on principle revision). |

---

## State Summary

### Territory + Purpose Echo

- **Territory:** prior inquiry contexts (Region A); harmony_layer.md current state (B); sibling doc shapes (C); possibility space of dissolved-form designs (D); in-domain self-justifying-spec patterns (E); cost profile of meta-principle adoption (F); user's criteria operationalized (G).
- **Purpose:** research S6 dissolution + diagnose "too big" + evaluate against efficient/elegant/future-proof.

### Coverage Map

| Region | Coverage | Aggregate relevance | Notes |
|---|---|---|---|
| A | CONFIRMED | core | Prior context and adjacent recommendations clear. |
| B | CONFIRMED | core | harmony_layer.md structure mapped; Tier 1/2 already self-justifying; Tier 3 vulnerable. |
| C | CONFIRMED | core | **MAJOR FINDING C-16: harmony_layer.md is the outlier among framework docs.** |
| D | CONFIRMED | core | 7 dissolved-form designs surfaced (D1-D7); D2 and D7 are the strongest candidates. |
| E | CONFIRMED | core/sub | Self-justifying-spec is the dominant pattern in successful documentation. |
| F | CONFIRMED | core | **MAJOR FINDING F-6/F-7: dominant "too big" cost is cognitive layering + lock-in, not minutes.** |
| G | CONFIRMED | core | Criteria operationalized; favor self-justifying forms. |

### Confirmed-Absent Regions

- No dissolved-form design that outperforms D2/D7 on all three criteria has been surfaced after enumeration. The space appears bounded.

### Concept-Names List

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| dissolved form | coined-term | A-1, D-* | A doc structure where each entry is self-justifying; no separate meta-principle generates classifications. |
| PRESERVE-WHEN / SACRIFICE-WHEN structure | coined-term | D2 | Per-entry scoping format: each entry has explicit conditions for when to preserve vs sacrifice the harmony feature. |
| cognitive layering | vocabulary | F-6 | The cost of having two conceptual levels (meta-principle + entries) that the reader/author must coordinate. |
| amortization break-even | vocabulary | E-30 | A meta-principle's overhead is justified when it generates many entries AND the principle is stable; below break-even, dissolution wins. |
| coordination cost | vocabulary | E-31 | The reader-time cost of holding meta-principle + entries in mind together and verifying their consistency. |
| principle ossification | vocabulary | E-32 | Meta-principles become hard to revise as derived entries accumulate; revision triggers cascading invalidation. |
| shape parity | coined-term | C-16 | The observation that sibling docs in the framework already use the dissolved form; harmony_layer.md is the outlier. |
| pattern-language form | vocabulary | E-29 | Each entry is a self-justifying pattern with name + problem + solution + consequences; well-matched to harmony_layer.md content. |

### Recency Distribution

| Region | files mentioned | mtimes |
|---|---|---|
| A | prior findings | 2026-06-04 |
| B | harmony_layer.md | 2026-03-28 (oldest framework file) |
| C | sibling docs | 2026-03-28 to 2026-04-12 |
| D | n/a (possibility) | — |
| E | n/a (in-domain) | — |
| F | derived from prior inquiry 2's MVD spec | 2026-06-04 |
| G | derived from `_branch.md` | 2026-06-04 |

### Frontier Flags

- **FF-1** — D2 vs D7 head-to-head: PRESERVE-WHEN/SACRIFICE-WHEN structure (tighter) vs embedded principle-application (more expressive). Both are strong; sensemaking should adjudicate which fits the framework's content best.
- **FF-2** — Tier 1/Tier 2 entries are already self-justifying (B-7, B-8). The dissolution mostly affects Tier 3. Does dissolution still require touching Tier 1/2, or can they stay as-is? Sensemaking should address.
- **FF-3** — Sibling docs use dissolved form already (C-16). Does dissolution actually bring harmony_layer.md into shape-parity, or does its content (priority-classification) differ enough that it inherently needs a meta-principle? This is the "loses abstraction value" objection from the prior inquiry — directly testable.
- **FF-4** — The user said "efficient + elegant + future-proof." Is there an OVERLOOKED criterion (e.g., "compatible with existing entries" or "easy to communicate")? Sensemaking should check for completeness.

### Workspace-Populated Status

`{populated: true, populated-at: 2026-06-04T02-44Z, extent: "7 regions traversed; 43 items tagged; 4 frontier flags emitted"}`

---

## Telemetry

- Mode: hybrid (artifact + possibility); entry point: signal-first
- Cycles run: 1
- Items enumerated: 43
- Items tagged: core: 28 | sub: 13 | side: 0 | umbrella: 2 | total HIGH-confidence rejections: 0
- Confidence distribution: HIGH: 37 | MEDIUM: 5 | LOW: 1
- Sub-phase fired: NO
- Convergence: criteria met
- Workspace-overload trigger: NOT FIRED
- `items_with_mtime: 5` / `items_without_mtime: 38`
- Failure modes checked: all; none triggered.

## Self-Assessment Verdict

**PROCEED with FLAG**

Verdict justification: All convergence criteria met. Two MAJOR FINDINGS substantively reshape the inquiry's frame:
- **C-16 (shape parity finding):** harmony_layer.md is the outlier among framework docs — all sibling docs already use dissolved form. This shifts the inquiry from "should we adopt this novel shape?" to "should we bring harmony_layer.md into shape-parity with the rest of the framework?" The "loses abstraction value" objection from the prior inquiry must be re-evaluated against this.
- **F-6/F-7 (cognitive layering + lock-in):** the dominant "too big" cost is conceptual, not effort-in-minutes. Dissolution removes both costs. The user's intuition is empirically anchored.

FLAG for downstream:
- Sensemaking must adjudicate D2 vs D7 (and possibly D1) as the dissolved-form candidate.
- The "loses abstraction value" objection from the prior inquiry's S6 disposition deserves direct adversarial testing — does Tier-system-as-abstraction actually carry load for harmony_layer.md, or is it cargo-culted from spec-design conventions that don't fit this content?
- The shape-parity finding (C-16) may reframe the whole inquiry from "research a research frontier" to "bring an outlier into line with the framework's existing convention."
