# Sensemaking: Root Word Grouping in Translation Memory

---

## SV1 — Baseline Understanding

The translation memory needs to group different surface forms of a word under a common root/lemma so that the LLM gets the full history when any form of that word appears. The proposed solution: ask the LLM to output the root as part of its structured response. Language-agnostic. No external dependency.

Seems straightforward. But let's check.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1:** The solution must be language-agnostic. Comprehenslate is not Arabic-only.
- **C2:** No external morphological analyzer dependency. The LLM is the analyzer.
- **C3:** The root must be part of the structured output (Pydantic model) — it's a field the LLM fills per rich word.
- **C4:** The translation memory groups by root. When looking up a word, we find its root, then retrieve all entries under that root.

### Key Insights

- **K1:** "Root" means different things in different language families. In Arabic, it's a trilateral consonant skeleton (ك-ت-ب). In Turkish, it's a stem before agglutination. In English, it's a lemma (the dictionary form). In German, it might be compound decomposition. The word "root" is doing a lot of work across very different linguistic realities.
- **K2:** The grouping doesn't need to be linguistically perfect — it needs to be consistent enough that the same word forms get grouped together across LLM calls. If the LLM calls the root "k-t-b" in chunk 3 and "ktb" in chunk 12, the grouping breaks.
- **K3:** The LLM might not even need to provide a "root" in the linguistic sense. What we actually need is a **grouping key** — a stable identifier that all forms of a word share. Whether that key is a linguistic root, a lemma, a dictionary form, or an arbitrary canonical form doesn't matter. It just needs to be consistent.
- **K4:** Some words don't have meaningful roots or lemmas. Particles, prepositions, conjunctions. These are fixed-form words that don't inflect. They don't need grouping — they're already their own group.

### Structural Points

- **S1:** The system has two moments of root extraction: (a) when a word is first encountered and stored, and (b) when a word is encountered again and needs to be looked up. Both must produce the same key, or the lookup fails.
- **S2:** Root extraction is a per-word operation embedded in the sentence translation output. It's not a separate pass.
- **S3:** The memory has two lookup paths: by surface form (exact match) and by root (group match). Surface form is the fast path. Root is the fallback when surface form doesn't match but a related form exists.

### Foundational Principles

- **F1:** Consistency > linguistic accuracy. A consistently wrong root is more useful than an intermittently correct one, because consistency means the grouping holds.
- **F2:** The LLM is the single source of truth for roots. There's no external validator. If the LLM says the root is X, then it's X for this book.
- **F3:** Language-agnostic means the system treats "root" as an opaque grouping key. The system doesn't know or care whether it's a trilateral root, a lemma, or a stem.

### Meaning-Nodes

- **M1:** "Root" is really "grouping key" — a stable canonical form that all inflections of a word share.
- **M2:** The problem is consistency of LLM output, not linguistic analysis.
- **M3:** The translation memory is a two-index structure: surface form index + root/grouping-key index.

---

## SV2 — Anchor-Informed Understanding

The problem is not "how to extract roots from words." The problem is **how to get a consistent grouping key from the LLM across many independent calls over the course of a book.**

The linguistic details (trilateral roots, agglutinative stems, compound decomposition) are the LLM's problem. Our problem is: will the LLM give us the SAME key for the SAME word family every time?

This reframes the entire discussion from linguistics to LLM output consistency.

---

## Phase 2 — Perspective Checking

### Technical / Logical

The LLM produces a `root` field per rich word. Two concerns:

1. **Format consistency:** Does the LLM always format the root the same way? Arabic roots could be "ك-ت-ب" or "كتب" or "k-t-b" or "ktb". If the format varies, grouping breaks.
   - New anchor: **We should specify the format in the prompt.** E.g., "provide the root as hyphen-separated consonants in the source script."

2. **Semantic consistency:** For edge-case words, does the LLM always assign the same root? Some Arabic words have disputed roots. Some words can be traced to multiple roots.
   - New anchor: **Once a root is assigned to a word family, it should be fed back into subsequent prompts** as part of the translation memory, so the LLM stays consistent with its own prior choice.

3. **Lookup at translation time:** When chunk N contains "يكتبون", the system needs to find that this maps to root "ك-ت-ب" BEFORE sending to the LLM (to include the memory). But we don't have the root yet — the LLM hasn't processed this chunk. Chicken-and-egg.
   - New anchor: **Surface form matching happens first.** If "يكتبون" is an exact match in memory, we're done. If not, we check if any stored entry has "يكتبون" as a known form under a root. If not, we send the chunk without memory for this word, and the LLM tells us the root, which we store for next time.

### Human / User

From the user's perspective, root grouping is invisible plumbing. They don't care about roots — they care that "when the same word appears in different forms, the translations are consistent." The user never sees the root field. It's purely internal.

### Strategic / Long-term

Root grouping becomes more valuable over time:
- Book 1 builds a root-grouped memory
- Book 2 by the same author can reuse it — even if the author uses different forms of the same words
- A domain-specific memory (e.g., Islamic jurisprudence) groups key terms by root, making it reusable across any text in that domain

New anchor: **The root is the long-term identity of a word. Surface forms are ephemeral; roots persist across books.**

### Risk / Failure

- **Risk 1: LLM inconsistency.** The LLM assigns different roots to the same word in different calls. Mitigation: feed prior root assignments back into the prompt.
- **Risk 2: Over-grouping.** The LLM groups unrelated words under the same root because they share surface-level similarity. E.g., in Arabic, some words from different roots look similar. Mitigation: trust the LLM — it knows Arabic morphology better than a simple stemmer.
- **Risk 3: Under-grouping.** The LLM treats the same word as having different roots because the forms are very different. E.g., irregular verbs. Mitigation: the memory accumulates forms over time. Once a root has 5 surface forms associated with it, the coverage is broad enough.

### Resource / Feasibility

Zero additional cost. The root is one extra field in the structured output. The LLM already analyzes the word to translate it — extracting the root is negligible marginal work.

### Definitional / Consistency

Does "root" contradict any established definition in the project?

Checking against `notes.md`: The document discusses root-based meaning extensively — "a single root (ض-ر-ب) can produce 30+ surface forms" and how root meaning informs word meaning. The project's own philosophy treats roots as fundamental semantic units. Using roots as grouping keys is consistent with the project's foundational view of language.

No contradiction found.

---

## SV3 — Multi-Perspective Understanding

Major shift: **The root field is not just a grouping key — it's the first piece of the meaning index.** The project's philosophy (from `notes.md`) treats roots as primary semantic carriers. By collecting roots per word, we're building the foundation of the Phase 1 comprehension engine as a side effect of translation.

This means the "root" field in the structured output is doing double duty:
1. **Immediate use:** grouping key for translation memory consistency
2. **Long-term use:** the beginning of the word inventory and meaning index from the original spec

Also clarified: the chicken-and-egg problem (needing the root to look up memory, but needing the LLM to get the root) is solved by **two-path lookup** — surface form first (fast, no LLM needed), root-based second (uses stored root mappings from previous encounters). New words that have never been seen simply don't get memory on their first appearance, and that's fine.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: What exactly is a "root"?

The term "root" means different things across languages (trilateral consonant skeleton in Arabic, stem in Turkish, lemma in English, compound head in German).

**Resolution:** We don't call it "root" in the data model. We call it `lemma` — the canonical dictionary form of the word. This is the most universally applicable term. For Arabic, the LLM can provide the trilateral root as the lemma. For Turkish, the stem. For English, the dictionary form. The field name is language-neutral.

**Strongest counter-interpretation:** "Lemma" is technically different from "root" in Arabic linguistics. The lemma of "كاتب" (writer) is "كاتب" itself, while the root is "ك-ت-ب". Using "lemma" might cause the LLM to return the dictionary headword instead of the deeper root.

**Assessment:** This counter-interpretation is valid. In Arabic, root-level grouping captures more relationships than lemma-level grouping. But for other languages, "root" is either meaningless or overly narrow. **Resolution holds but with a nuance:** the prompt should ask for "the base root or lemma that groups all forms of this word" — letting the LLM choose the appropriate level of abstraction for the source language.

**What is now fixed?** The field is called `lemma` in the Pydantic model. The prompt asks for "the root or base form that all inflections of this word share."

**What is no longer allowed?** Language-specific root extraction logic. The system treats the lemma as an opaque string.

**What now depends on this choice?** The memory's root index uses lemma strings as keys. Consistency of these strings across LLM calls is critical.

**What changed?** "Root" is no longer a linguistic term in our system — it's a grouping key with a language-neutral name.

---

### Ambiguity 2: How to ensure LLM consistency for the lemma?

The LLM might produce "ك-ت-ب" in one call and "كتب" in another for the same root.

**Resolution:** Two mechanisms:

1. **Prompt specification:** The instruction tells the LLM exactly how to format lemmas: "For each rich word, provide the lemma (root or base form) in the source language script. For Semitic languages, use the bare root consonants separated by hyphens (e.g., ك-ت-ب). For other languages, use the dictionary headword."

2. **Feedback loop:** The prompt injection view includes known lemmas with their associated surface forms. When the LLM sees "ك-ت-ب: كتاب، كاتب، مكتوب" already established, it will use the same format.

**What is now fixed?** Lemma format is prompt-specified, not left to LLM discretion. Prior lemma assignments are fed back.

**What is no longer allowed?** Hoping the LLM will be consistent without guidance.

**What now depends on this choice?** The prompt instruction must include lemma formatting rules. The prompt injection view must include known lemmas.

**What changed?** Consistency is engineered through prompt design, not assumed.

---

### Ambiguity 3: The chicken-and-egg lookup problem

To inject memory for a word, we need its lemma. To get its lemma, we need the LLM. But we're building the prompt BEFORE calling the LLM.

**Resolution:** Two-pass lookup:

1. **Surface form match (pre-LLM):** Scan the source chunk for tokens. Check each against the memory's surface form index. If found, we already have the lemma → include the memory entry.

2. **Lemma match (pre-LLM):** For tokens not found by surface form, check if the token appears as a known surface form under any lemma in the memory. This works because previous LLM calls have already mapped surface forms to lemmas.

3. **No match (post-LLM):** If neither lookup finds the word, it goes to the LLM without memory. The LLM returns the lemma in the response, and it gets stored for next time.

**What is now fixed?** New words don't get memory hints on first encounter. This is acceptable — they haven't been seen before, so there's nothing to hint.

**What is no longer allowed?** Requiring the LLM to provide lemmas before translation (a separate pre-processing call). That would double the LLM calls.

**What now depends on this choice?** The memory must maintain a reverse index: surface form → lemma. This is populated as a side effect of each translation.

**What changed?** The lookup is gracefully degraded: known words get full memory, unknown words get none, and the gap closes with each chunk translated.

---

## SV4 — Clarified Understanding

The "root word problem" is now three solved sub-problems:

1. **What to call it:** `lemma` — a language-neutral grouping key. The prompt tells the LLM what level of abstraction to use per source language.
2. **How to keep it consistent:** Prompt specification (format rules) + feedback loop (prior lemma assignments included in prompt).
3. **How to use it before having it:** Two-path pre-LLM lookup (surface form → lemma → memory). Unknown words get no memory on first encounter, which is fine.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed Variables

| Variable | Fixed Value |
|---|---|
| Field name | `lemma` |
| Who extracts it | The LLM, as part of structured output |
| Format specification | In the prompt instruction, language-family-aware |
| Consistency mechanism | Prior lemma assignments fed back in prompt injection |
| Lookup strategy | Surface form first, then lemma-based reverse lookup |
| Handling of unknown words | No memory on first encounter; stored after |
| External dependencies | None |

### Eliminated Options

- External morphological analyzer (any language) — eliminated
- Separate pre-processing LLM call for root extraction — eliminated
- Language-specific root extraction code — eliminated
- Hoping for LLM consistency without prompt engineering — eliminated
- Calling the field "root" (too linguistically loaded) — eliminated

### Remaining Viable Paths

Only one open question: **should the prompt injection view include the lemma-to-surface-forms mapping?**

Option A: Yes — show "ك-ت-ب: كتاب، كاتب، مكتوب" so the LLM sees the full family.
Option B: No — just show the lemma and let the LLM figure out the relationship.

Option A is better — it costs few tokens and helps the LLM stay consistent. **Fixed: include the mapping.**

---

## SV5 — Constrained Understanding

The implementation is fully constrained:

**In the Pydantic response model (`RichWord`):**
```python
class RichWord(BaseModel):
    word: str          # surface form as it appears in text
    lemma: str         # grouping key (root/base form, LLM-provided)
    position: int
    meanings: list[WordMeaning]
```

**In the translation memory storage:**
```python
class WordEntry(BaseModel):
    lemma: str                         # the grouping key
    surface_forms: set[str]            # all forms seen: {كتاب, كاتب, مكتوب, ...}
    encounters: list[WordEncounter]    # all contexts, all meanings
```

**In the prompt injection view:**
```
ك-ت-ب (forms: كتاب، كاتب، مكتوب):
  - "book/writing" — 8 occurrences (ch.1-6)
  - "writer/scribe" — 3 occurrences (ch.2, ch.5)
```

**In the prompt instruction:**
```
For each rich word, provide its lemma — the root or base form
that all inflections share. For Semitic languages, use bare root
consonants with hyphens (e.g., ك-ت-ب). For other languages, use
the dictionary headword (e.g., "escribir" not "escribió").
```

**Lookup chain:**
```
source chunk token
  → exact surface form match in memory? → yes → use that entry
  → known surface form under any lemma? → yes → use that entry
  → no match → send without memory → LLM returns lemma → store for next time
```

---

## SV6 — Stabilized Model

### Final Conceptual Model

The "root word problem" is a **grouping key consistency problem**, not a linguistics problem. The solution:

1. **The field is `lemma`** — a language-neutral grouping key provided by the LLM as part of every rich word in the structured output. The system treats it as an opaque string. The prompt tells the LLM what level of abstraction to use based on the source language.

2. **Consistency is engineered, not hoped for.** The prompt specifies the format. Prior lemma assignments are fed back in the prompt injection view alongside their known surface forms. The LLM stays consistent with its own prior choices.

3. **Lookup is gracefully degraded.** Known words get full memory through two-path lookup (surface form, then lemma). Unknown words get no memory on first encounter but are stored immediately after, closing the gap chunk by chunk.

4. **Zero external dependencies.** The LLM is the morphological analyzer for every language. No stemmer, no root extractor, no language-specific tooling.

5. **Double duty.** The lemma field serves as both a translation memory grouping key (immediate use) and the foundation of the word inventory / meaning index (long-term use for indexing/Phase 1).

### How SV6 Differs from SV1

SV1 said: "ask the LLM for the root, group by root, done."

SV6 says: the concept is correct but the word "root" was hiding three sub-problems (naming, consistency, lookup timing) that each needed explicit solutions. The field is `lemma` not `root`. Consistency requires prompt engineering + feedback loops, not just asking. Lookup requires a two-path strategy with graceful degradation for unknown words. And the lemma field is secretly the first brick of the meaning index — it's doing more than just grouping.
