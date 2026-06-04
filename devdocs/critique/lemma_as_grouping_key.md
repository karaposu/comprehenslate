# Critique: "Lemma" as the Grouping Key for Translation Memory

## Problem Context

The translation memory needs to group related word forms so that consistency is maintained across a book. The current proposal: use a field called `lemma` as a language-neutral grouping key, provided by the LLM as part of structured output.

The user raised a critical challenge: **In Turkish, "kitap" (book) and "kitaplık" (bookcase/library) — are these the same lemma?** They're clearly related (same root "kitap") but they're NOT the same word. One is a noun, the other is a derived noun with a different meaning. Should the glossary group them together or keep them separate?

This challenge exposes a deeper problem with the entire "lemma as grouping key" approach.

---

## Phase 0 — Dimension Construction

### Evaluation Dimensions

| Dimension | Weight | Success Criteria | Extracted From |
|---|---|---|---|
| **Semantic Correctness** | Critical | Grouping must reflect actual meaning relationships. Words with the same meaning are grouped. Words with different meanings are NOT grouped, even if morphologically related. | Core Comprehenslate principle: meaning over form |
| **Grouping Granularity** | Critical | The grouping level must be "right-sized" — neither so broad that unrelated meanings collapse together, nor so narrow that obvious variants are separated. | The kitap/kitaplık challenge |
| **Language Agnosticism** | High | The solution must work across language families without language-specific code. | Project constraint C1 |
| **Consistency** | High | The same word forms must always be grouped the same way across LLM calls. | Translation memory reliability requirement |
| **Simplicity** | Medium | The solution should be implementable without excessive complexity in the data model or prompt engineering. | V1 pragmatism |
| **Extensibility** | Medium | The solution should accommodate future improvements (external analyzers, hierarchical grouping) without architectural rewrites. | Long-term viability |

---

## Phase 1 — Landscape Construction

### The Core Problem: Grouping Granularity Is Not a Single Level

Languages have multiple levels of word relationship:

```
Level 0: Exact form     "kitaplık"
Level 1: Lemma           "kitaplık" (the dictionary headword)
Level 2: Derivation root "kitap" (the word it was derived from)
Level 3: Etymology       "kitab" (Arabic origin كتاب)
```

The proposal says "use lemma as grouping key." But look at what happens:

- **At Level 1 (lemma):** "kitap" and "kitaplık" are SEPARATE entries. They're different dictionary headwords with different meanings. "kitaplık" means bookcase/library, not book. The glossary correctly separates them.

- **At Level 2 (derivation root):** "kitap" and "kitaplık" are GROUPED. They share a derivational base. The glossary would show them together, which might cause the LLM to confuse their translations.

**The proposal is actually correct IF "lemma" truly means "dictionary headword" — because kitap and kitaplık ARE different lemmas.** The user's concern is valid only if "lemma" is confused with "root" or "derivation base."

This is the crux: **the word "lemma" was chosen to AVOID this exact problem, but the proposal's own documentation sometimes slips into root-level thinking.**

### Viable Region

Solutions where grouping happens at the lemma (dictionary headword) level, NOT the root level. "kitap" and "kitaplık" are separate entries that can cross-reference each other.

### Dead Region

Solutions where grouping happens at the root level, collapsing "kitap" and "kitaplık" into one entry. This loses meaning distinctions.

### Boundary Region

Solutions where multiple grouping levels coexist — lemma-level entries with root-level cross-references. More complex but more powerful.

---

## Phases 2-3 — Adversarial Evaluation

### Candidate: "Lemma as flat grouping key"

The current proposal: one field called `lemma`, one level of grouping. Every word form maps to exactly one lemma. The memory groups by lemma.

#### Prosecution

**Killer objection: "lemma" is ambiguous and the LLM will inconsistently choose the grouping level.**

Consider Turkish:
- "kitap" → lemma is "kitap" ✓
- "kitaplar" (books) → lemma is "kitap" ✓ (plural inflection, same lemma)
- "kitaplık" (bookcase) → lemma is... "kitaplık"? or "kitap"?

If the LLM is told "provide the lemma," it might correctly return "kitaplık" (the dictionary headword). But it might also return "kitap" (the derivational base), especially if the prompt says "the root or base form that all inflections share."

The proposal's own prompt instruction says: *"For each rich word, provide the root or base form that all inflections of this word share."* This is WRONG for the kitap/kitaplık case. "kitaplık" is not an inflection of "kitap" — it's a derivation. Inflection (kitap → kitaplar) preserves meaning. Derivation (kitap → kitaplık) changes meaning.

**The prompt conflates inflection and derivation.** This will cause the LLM to over-group.

**Second objection: Arabic makes this worse, not better.**

In Arabic, the trilateral root system is extremely productive. The root ك-ت-ب (k-t-b) produces:
- كِتَاب (kitāb) — book
- كَاتِب (kātib) — writer
- مَكْتَبَة (maktaba) — library
- مَكْتُوب (maktūb) — letter/written thing
- كُتُب (kutub) — books (plural)

"kitāb" and "kātib" have the SAME trilateral root but DIFFERENT meanings. If the prompt asks for "the root," the LLM returns ك-ت-ب for both, and the memory collapses book/writer/library/letter into one entry. This is catastrophically wrong for translation consistency — you do NOT want the translation of "writer" to influence the translation of "library."

But "kitāb" and "kutub" (book/books) DO share a lemma and SHOULD be grouped.

**The proposal chose "lemma" to avoid this, but the prompt instruction still says "root."** The name is right but the instruction is wrong.

#### Defense

**Core strength: the concept of a grouping key is exactly right.**

The proposal correctly identifies that:
1. Surface form matching misses obvious variants (kitap/kitaplar)
2. Some grouping is needed for consistency
3. The LLM can provide this grouping
4. No external dependency is needed

**The fix is narrow, not architectural.** The problem is not with the concept of a lemma-based grouping key. The problem is with the prompt instruction that says "root or base form" when it should say "dictionary headword." The architecture (lemma field in Pydantic model, memory indexed by lemma, two-path lookup) is sound.

**Defense of lemma-level grouping specifically:**

"kitap" and "kitaplık" SHOULD be separate lemmas. They have different dictionary entries, different meanings, different translations. The lemma-level grouping correctly separates them.

"kitap" and "kitaplar" SHOULD be the same lemma. They're the same word, one is just plural. The lemma-level grouping correctly merges them.

This is the right level. The defense holds.

#### Collision

Prosecution wins on one specific point: **the prompt instruction is wrong.** It says "root or base form" which invites the LLM to over-group (collapsing derivations, not just inflections).

Defense wins on the architecture: lemma-level grouping is the right level. The data model, lookup strategy, and feedback loop are sound.

**The fix:** Change the prompt instruction. Don't say "root or base form." Say "dictionary headword" or "the form you would look up in a dictionary."

#### Verdict: REFINE

**What passes:** The architecture (lemma field, memory indexing, two-path lookup, feedback loop). The choice of lemma-level grouping over root-level grouping.

**What fails:** The prompt instruction. It currently invites over-grouping by saying "root or base form."

**What "right" looks like:**

The prompt should say something like:

> For each rich word, provide its `lemma` — the dictionary headword form. This is the form you would look up in a dictionary to find this word.
> - For "kitaplar" (books), the lemma is "kitap" (book) — same word, different inflection.
> - For "kitaplık" (bookcase), the lemma is "kitaplık" — different word, different meaning.
> - For "يكتبون" (they write), the lemma is "كتب" (to write) — same verb, different conjugation.
> - For "كاتب" (writer), the lemma is "كاتب" — different word derived from the same root.
> Do NOT return the trilateral root or derivational base. Return the dictionary headword.

---

### Candidate: "Root as grouping key" (the thing we said we'd avoid)

Brief evaluation for completeness.

#### Prosecution

Collapses distinct meanings. "book" and "writer" and "library" all become one entry under ك-ت-ب. The translation memory would tell the LLM "this root was translated as 'book' before" when it's looking at "writer." Catastrophic for translation quality.

#### Defense

Captures more relationships. The LLM would know that "book" and "writer" are related concepts. For scholarly analysis (belagat, word choice analysis), seeing the full root family is valuable.

#### Collision

Prosecution destroys defense on Semantic Correctness (critical weight). Over-grouping is worse than under-grouping — wrong information in the memory is worse than missing information.

#### Verdict: KILL

**What killed it:** Semantic Correctness. Root-level grouping destroys meaning distinctions that are critical for translation.

**Seed extracted:** Root-level relationships ARE valuable — just not as the primary grouping key. They belong in a separate layer: a "related words" cross-reference, not the identity key.

---

### Candidate: "Hierarchical grouping — lemma primary, root as cross-reference"

What if the memory has lemma-level entries as the primary grouping (kitap, kitaplık, kātib are all separate entries), but also maintains a root-level cross-reference layer that links related lemmas?

```
Lemma entries (primary, used for consistency):
  kitap: {encounters: [...], translations: [...]}
  kitaplık: {encounters: [...], translations: [...]}

Root cross-references (secondary, used for awareness):
  k-t-p family: [kitap, kitaplık]
```

#### Prosecution

**Objection: complexity for v1.** Two indexing levels, two lookup paths, two things to maintain. The cross-reference layer is useful for scholarly analysis but not essential for basic translation consistency. Over-engineering for a first implementation.

**Objection: the LLM now needs to provide TWO fields** — lemma AND root. More structured output, more room for inconsistency, more prompt engineering.

#### Defense

**Core strength: it preserves the option of root-level awareness without sacrificing lemma-level correctness.** The primary grouping (lemma) is semantically correct. The cross-reference (root) provides the broader view without corrupting the primary index.

**This is also the architecture that supports future indexing.** When Phase 1 comprehension is built, the root cross-reference is already there — the word inventory can be viewed at both lemma level and root level.

**The complexity cost is low.** The root cross-reference is just a `dict[str, list[str]]` mapping root → lemma list. It's a few lines of code. The LLM already identifies roots naturally when doing Arabic analysis — adding a `root` field alongside `lemma` is marginal effort.

#### Collision

Prosecution's complexity objection is valid but weak — the actual implementation cost is minimal. Defense wins on extensibility and correctness.

However, for v1, the cross-reference layer can be **stored but not actively used.** Collect the root field from the LLM, store the mapping, but don't use it in prompt injection or lookup. It's data we accumulate for later use. Zero runtime complexity, future value.

#### Verdict: SURVIVE (with caveat)

**Passes:** Semantic Correctness (lemma-level primary), Language Agnosticism (works for any language), Extensibility (root layer ready for Phase 1).

**Caveat:** For v1, the root cross-reference is **stored but inactive.** The prompt injection and lookup use only the lemma level. The root cross-reference becomes active when Phase 1 indexing is built.

---

## Phase 4 — Coverage + Convergence

### Accumulator Update

| Candidate | Verdict | Key Finding |
|---|---|---|
| Lemma as flat grouping key | REFINE | Architecture sound, prompt instruction wrong. Fix: say "dictionary headword" not "root or base form." |
| Root as grouping key | KILL | Destroys meaning distinctions. Seed: root relationships are valuable as cross-references, not as primary keys. |
| Hierarchical (lemma + root cross-ref) | SURVIVE | Lemma primary for correctness, root as stored-but-inactive cross-reference for future use. |

### Coverage Assessment

The solution space for "how to group words in translation memory" has three main regions:

- **Surface form only (no grouping):** Not evaluated as a candidate but understood as the baseline. Under-groups — misses obvious variants.
- **Lemma-level grouping:** Evaluated. Correct level for translation consistency. Refined: prompt must say "dictionary headword."
- **Root-level grouping:** Evaluated. Over-groups. Killed.
- **Hierarchical (lemma + root):** Evaluated. Survives. Best balance of correctness and future value.
- **Language-specific analyzers:** Not evaluated (deferred per user's instruction — "maybe for later"). Known to exist as a future option.

No major unexplored regions remain.

### Convergence Signal: TERMINATE

One candidate survives cleanly. The landscape is mapped. The key distinction (lemma vs. root as primary key) is resolved.

### Ranked Survivors

1. **Hierarchical (lemma primary, root cross-reference stored but inactive)** — the v1 implementation. Prompt asks for both `lemma` (dictionary headword) and `root` (derivational base). Memory groups by lemma. Root mapping is stored for future indexing use.

### Critical Takeaway

**The user's "kitap/kitaplık" challenge exposed the real issue:** the proposal was RIGHT in choosing "lemma" but WRONG in its prompt instruction which still said "root or base form." The fix is specific: the prompt must clearly distinguish inflection (same lemma) from derivation (different lemma) and ask for the dictionary headword, not the morphological root.
