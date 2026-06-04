# Sensemaking: Do We Need Custom Terminology?

---

## SV1 — Baseline Understanding

The project has accumulated many terms across design docs — some standard (lemma, root), some borrowed from classical Arabic linguistics (belagat, i'caz, iltifat), some invented during design discussions (meaning space, prompt injection view, comprehension index). The question: should we formalize a terminology document, and which terms need custom definitions?

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1:** The project bridges multiple domains: NLP, translation studies, classical Arabic rhetoric, software engineering, LLM engineering. Each domain has its own vocabulary.
- **C2:** We've been using terms in design docs that mean specific things in our context but different things in standard usage (e.g., "index" doesn't mean database index here).
- **C3:** Future contributors, users, and even future-us need to understand what we mean without re-reading 10 design documents.

### Key Insights

- **K1:** We're already experiencing terminology drift. "Translation memory" vs. "comprehension index" vs. "glossary" — these have been used at different points to describe overlapping but distinct concepts. A new reader would be confused.
- **K2:** Some terms we invented during design are genuinely novel (no standard equivalent exists):
  - "Meaning space" — the set of all known possible meanings of a word, assembled from index + lexicon + LLM knowledge
  - "Prompt injection view" — a compressed snapshot of the index for LLM context injection
  - "Rich word" — a word carrying multiple valid meanings in a specific context
- **K3:** Some terms we use non-standardly:
  - "Lemma" — we use it as "dictionary headword as grouping key," which is close to standard usage but we're explicit about what it's NOT (it's not the root)
  - "Root" — we use it as "derivational base stored as cross-reference," which is narrower than its standard Arabic linguistics meaning
  - "Comprehension" — we use it as a specific pipeline (extract → detect → resolve), not the general concept
- **K4:** Some terms come from classical Arabic sciences and need explanation for non-specialists:
  - belagat, i'caz, meani, beyan, bedi, iltifat, hasr, nazm, etc.

### Structural Points

- **S1:** Terms fall into categories: pipeline stages, data structures, linguistic concepts, configuration concepts, Arabic rhetoric terms.
- **S2:** The terminology serves two audiences: developers (who need precise technical definitions) and users (who need to understand what the tool does).
- **S3:** The terminology document is a reference — it should be scannable, not narrative.

### Foundational Principles

- **F1:** A term is worth defining custom if: it's used in 3+ documents, AND (it's novel OR we use it non-standardly OR it's domain-specific and our audience may not know it).
- **F2:** If a standard term exists and we use it standardly, just note it — don't redefine.
- **F3:** The terminology doc should be the SINGLE SOURCE OF TRUTH for what each term means in Comprehenslate. If a design doc uses a term differently, the terminology doc wins.

### Meaning-Nodes

- **M1:** The terminology doc is not documentation — it's a contract. It locks meaning.
- **M2:** Creating it forces us to audit our own language and find inconsistencies.
- **M3:** It becomes a shared vocabulary for prompts too — the LLM system prompt can reference these terms.

---

## SV2 — Anchor-Informed Understanding

Yes, a terminology document is clearly needed. We're already drifting. The question isn't "should we?" but "what terms, and how to organize them?"

The audit of our design docs reveals ~30 terms that need formal definition. They cluster into clear categories.

---

## Phase 2 — Perspective Checking

### Technical / Logical

A terminology doc prevents bugs. If "index" means different things in `memory.py` vs `llm.py`, someone will write code that connects the wrong structures. Locked definitions prevent this.

### Human / User

For someone reading the README or using the tool: "What's a meaning space? What's a rich word? What's the difference between comprehension and translation in this tool?" The terminology doc answers these without requiring them to read the full design docs.

### Strategic / Long-term

If the project grows (contributors, users, documentation), terminology drift accelerates. Catching it now while there are only two people (the user and the design docs) is far cheaper than catching it later.

### Definitional / Consistency

Scanning across our design documents, I found these inconsistencies:

- "Translation memory" was the original term. Then we renamed Structure A to "Comprehension Index." But `memory.py` still uses `TranslationMemory` as the class name. Which is canonical?
- "Prompt injection view" / "Prompt View" / "Structure B" / "Prompt Memory" / "Prompt Index" — five names for the same thing across different docs.
- "Meaning" vs "interpretation" — in the comprehension pipeline, an ambiguity has "interpretations." In the translation output, a word has "meanings." Are these the same concept at different stages?

These NEED resolution. The terminology doc is where they get resolved.

---

## SV3 — Multi-Perspective Understanding

The terminology doc is not just useful — it's urgent. We have active inconsistencies that will cause confusion as we build. The doc should:
1. Audit every term used across design docs
2. Pick ONE canonical name for each concept
3. Define it precisely
4. Note what it's NOT (to prevent confusion with standard usage)

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: What should the data structure names be canonically?

We've used multiple names for the same structures across documents.

**Resolution:**

| Concept | Canonical Name | Also Known As (retire these) |
|---|---|---|
| The full persistent word-meaning map | **Comprehension Index** | Translation memory, glossary, Structure A, meaning index |
| The compressed per-chunk view for LLM prompts | **Prompt View** | Prompt injection view, Prompt Memory, PromptIndex, Structure B |
| The rich per-sentence translation output | **Translation Output** | Sentence output, ChunkOutput, Structure C |
| The per-chunk comprehension analysis | **Comprehension Output** | ComprehensionResult, Structure D |

**What is now fixed?** Four canonical names. Code class names may differ (Python naming conventions), but documentation uses these names.

**What is no longer allowed?** Using "translation memory" to refer to the Comprehension Index. Using "glossary" to refer to the index. Using "Structure A/B/C/D" without also using the canonical name.

---

### Ambiguity 2: What's the difference between "meaning" and "interpretation"?

In the comprehension pipeline, ambiguities have "interpretations." In the translation output, words have "meanings." Both describe "a possible reading."

**Resolution:**

- **Meaning** = a word-level concept. One possible semantic value a word carries. Exists in both stages. In comprehension: described (not translated). In translation: translated.
- **Interpretation** = a higher-level concept. One possible reading of an ambiguity (which may span word, sentence, or sense level). An interpretation may involve multiple word meanings working together.

A word has meanings. An ambiguity has interpretations. Interpretations are composed of meanings (and structural/contextual analysis).

**What is now fixed?** "Meaning" is word-level. "Interpretation" is ambiguity-level. They're different granularities of the same phenomenon.

---

### Ambiguity 3: Should we define the Arabic rhetoric terms?

The project uses belagat, i'caz, meani, beyan, bedi, iltifat, etc. These come from classical Arabic sciences.

**Resolution:** Yes, define them — but in a separate "Arabic Rhetoric" section of the terminology doc. They're not core to the pipeline (you can use Comprehenslate without knowing these terms) but they're essential for understanding the project's intellectual foundation and the system prompt content.

---

## SV4 — Clarified Understanding

The terminology document should have these sections:

1. **Pipeline Stages** — comprehension, translation, and what each means in Comprehenslate
2. **Data Structures** — the four canonical structures and their roles
3. **Linguistic Concepts** — lemma, root, surface form, meaning, meaning space, rich word
4. **Comprehension Pipeline** — meaning space, ambiguity levels, interpretation, resolution
5. **Configuration** — audience level, depth profile, and what each setting controls
6. **Arabic Rhetoric** — belagat terms for those who want the intellectual foundation

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed

| Decision | Fixed Value |
|---|---|
| Do we need a terminology doc? | Yes |
| Location | `terminology.md` in project root (already started by user) |
| Structure | Categorized by domain, not alphabetical |
| Canonical naming for data structures | Comprehension Index, Prompt View, Translation Output, Comprehension Output |
| Meaning vs. interpretation distinction | Meaning = word-level, interpretation = ambiguity-level |

### The terms that need custom definitions (not standard anywhere)

| Term | Why custom |
|---|---|
| **Meaning space** | Novel. The set of all known possible meanings of a word, assembled from index + lexicon + LLM knowledge |
| **Rich word** | Novel. A word identified as carrying multiple valid meanings in a specific context |
| **Prompt view** | Novel. A compressed, filtered snapshot of the index for LLM prompt injection |
| **Comprehension Index** | Semi-standard. We use "index" in a specific way — not a database index, not a book index |
| **Comprehended** | Custom definition. Our 4-point criterion, not the general English word |
| **Resolution** (of ambiguity) | Custom definition. Means "enumerate interpretations," not "pick one answer" |

---

## SV5 — Constrained Understanding

The terminology doc is a flat reference file with categorized sections. Each entry has: term, definition, what it's NOT (if confusable), and where it's used.

---

## SV6 — Stabilized Model

### Final Conceptual Model

**Yes, create a terminology document.** It serves three functions:

1. **Locks meaning** — resolves the inconsistencies we've already accumulated (5 names for the same data structure, meaning vs. interpretation confusion)
2. **Defines novel terms** — "meaning space," "rich word," "comprehended" have no standard definitions. We invented them. They need formal definitions.
3. **Onboards future readers** — anyone reading the code, design docs, or using the tool can look up what we mean

**The doc goes in `terminology.md` (project root, already started).** Organized by category, not alphabetically. Each entry: term, definition, what-it's-NOT, where-used.

### How SV6 Differs from SV1

SV1 asked "would it be useful?" SV6 says "it's urgent — we already have naming inconsistencies that will cause confusion during implementation." The audit found 5 different names for Structure B, conflation of "meaning" and "interpretation," and the word "comprehended" used both colloquially and as a precise 4-point criterion. The terminology doc resolves all of these.
