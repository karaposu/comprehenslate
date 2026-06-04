# Translation Memory & Glossary System

## The Problem

When translating a book chunk by chunk (chapter by chapter, page by page), each chunk goes to the LLM as an independent call. The LLM has no memory of previous chunks. This causes:

**Terminology drift** — the same word gets translated differently across chunks not because the meaning changed, but because the LLM rolled differently:
- Chapter 1: "تقوى" → "God-consciousness"
- Chapter 5: "تقوى" → "piety"
- Chapter 12: "تقوى" → "mindfulness of God"

All valid translations. But the reader sees three English words and thinks three different concepts are being discussed.

**Tone/register drift** — early chunks formal, later chunks casual.

**Named entity inconsistency** — "Husayn" in one chunk, "Hussein" in another.

---

## The Tension: Consistency vs. Multi-Meaning

A naive glossary that says "always translate X as Y" solves drift but kills multi-meaning — which is the core philosophy of Comprehenslate.

The distinction that matters:
- **Arbitrary drift** (bad) — same word, same meaning, different translation because the LLM was non-deterministic
- **Contextual variation** (good) — same word, genuinely different meaning because the context changed, deliberately translated differently

A flat glossary cannot tell these apart. We need something smarter.

---

## The Solution: Contextual Translation Memory

Instead of a flat `word → translation` map, we build a **per-word translation history with full context**. For each word we've encountered, we store every context it appeared in and what translation was chosen.

When the LLM encounters the word again, it receives this history and can decide: "this new occurrence looks like context A — stay consistent" or "this is a genuinely different usage — translate differently and note why."

### Format

```
تقوى has appeared before:

1. "اتقوا الله في أنفسكم" → translated as "God-consciousness"
   (context: personal spiritual awareness)

2. "والتقوى خير الزاد" → translated as "mindful restraint"
   (context: provision for a journey, self-discipline sense)
```

When chunk N is being translated, the translation memory for all significant words encountered in chunks 1 through N-1 is injected into the instruction prompt.

### What the LLM is told

The instruction is NOT "use these translations." The instruction is:

> Here are words you've encountered before in this book, the contexts they appeared in, and how they were translated. When you encounter these words again:
> - If the meaning in the current context matches a previous context, use the same translation for consistency.
> - If the meaning is genuinely different due to context, translate differently and explain why.
> - If you're unsure, present both options with a note.

This preserves multi-meaning while preventing arbitrary drift.

---

## How It Grows

The translation memory starts empty and builds incrementally:

1. **Chunk 1:** No memory exists. LLM translates freely. After translation, significant words and their chosen translations are extracted and stored.
2. **Chunk 2:** Memory from chunk 1 is injected into the prompt. LLM translates with awareness of prior choices. New words are added, existing entries gain new contexts if meanings differ.
3. **Chunk N:** Memory from chunks 1 through N-1 is available. The memory is a living, growing artifact.

After the entire book is translated, the translation memory is a complete word-meaning map — essentially the word inventory and meaning index from Phase 1, built as a byproduct of translation rather than as an upfront analysis pass.

**This is the seed of indexing.** The full indexing feature (Phase 1 comprehension) does this analysis upfront before any translation begins. The translation memory does it incrementally during translation. Both produce similar artifacts; they differ in when the work happens.

---

## Multi-Meaning Preservation Per Sentence

### The problem with picking one translation

A sentence with rich words doesn't have one meaning — it has many. Each rich word carries multiple valid meanings, and when combined, the possible sentence-level meanings multiply.

Example: a sentence with 3 rich words, each carrying 3 possible meanings, produces up to 27 possible sentence-level readings. Picking one "best" translation discards 26.

### Structured multi-meaning output

Every sentence should be translated in a structured way that preserves all valid meanings:

```
Sentence: "ضرب مثلاً في الأرض"

Primary translation (meaning 1):
  "He set forth a parable on earth"

Rich words in this sentence:

  ضرب (3 meanings in this context):
    m1: "set forth" (to present/establish) ← chosen for primary
    m2: "struck" (to hit/impact)
    m3: "traveled" (to journey)

  مثلاً (2 meanings):
    m1: "a parable" (illustrative story) ← chosen for primary
    m2: "a likeness" (comparison/analogy)

  في الأرض (2 meanings):
    m1: "on earth" (surface/world) ← chosen for primary
    m2: "in the earth" (embedded within)

Alternative sentence readings:
  [ضرب=m2, مثلاً=m1, في الأرض=m1]: "He struck a parable on earth"
  [ضرب=m1, مثلاً=m2, في الأرض=m1]: "He set forth a likeness on earth"
  [ضرب=m1, مثلاً=m1, في الأرض=m2]: "He set forth a parable in the earth"
  [ضرب=m3, مثلاً=m2, في الأرض=m2]: "He traveled as a likeness in the earth"
  ... (all valid combinations)
```

### Why this matters for the glossary

Each meaning discovered per word feeds back into the translation memory. The glossary entry for "ضرب" doesn't just say "translated as 'set forth' in this sentence" — it records ALL meanings that were valid in that context:

```
ضرب — translation memory:

  Context 1: "ضرب مثلاً في الأرض" (chapter 3, sentence 14)
    chosen: "set forth" (m1)
    also valid: "struck" (m2), "traveled" (m3)

  Context 2: "فضرب بيده على الباب" (chapter 7, sentence 3)
    chosen: "struck" (m2)
    also valid: none — context restricts to physical action
```

Now when "ضرب" appears in chapter 20, the LLM sees not just what was chosen before, but the full semantic range this word has exhibited across the book. It can make a richer, more informed decision.

### The user experience

A reader of the translated book can:
- Read the primary translation straight through (the "best fit" reading)
- For any sentence, expand to see which words were rich (had multiple meanings)
- For any rich word, see all meanings that were valid in that context
- See how alternative word meanings change the full sentence
- Navigate to the glossary to see how that word was translated everywhere else in the book

This transforms translation from "one person's interpretation" into a **translation workspace** — the reader can explore the meaning space the translator navigated.

### Combinatorial explosion

A sentence with 5 rich words, each with 4 meanings, produces 1024 combinations. Most are nonsensical (conflicting meanings that don't form a coherent sentence). The LLM should:

1. Identify which words in the sentence are "rich" (carry multiple contextually valid meanings)
2. List each rich word's valid meanings
3. Generate only the coherent combinations — not all permutations, but the ones where the meanings work together as a sentence
4. Rank them by contextual likelihood

This keeps the output manageable — typically 3-10 meaningful alternative readings, not hundreds.

### What gets stored

For each sentence, the structured output is:

```
{
  "source": "original text",
  "primary_translation": "the best-fit translation",
  "rich_words": [
    {
      "word": "ضرب",
      "position": 0,
      "meanings": [
        {"id": "m1", "translation": "set forth", "chosen": true, "confidence": 0.85},
        {"id": "m2", "translation": "struck", "chosen": false, "confidence": 0.10},
        {"id": "m3", "translation": "traveled", "chosen": false, "confidence": 0.05}
      ]
    }
  ],
  "alternative_readings": [
    {
      "combination": {"ضرب": "m2", "مثلاً": "m1"},
      "translation": "He struck a parable on earth",
      "coherence": 0.7
    }
  ]
}
```

This structure feeds the glossary (each meaning is recorded), supports the reader's exploration, and provides the data for the second pass (pass 2 has access to every meaning every word carried throughout the book).

---

## Edge Cases

### 1. Memory grows too large for the prompt

A full book may have hundreds or thousands of significant words, each with multiple contexts. At some point, the translation memory exceeds what fits in the LLM's context window alongside the system prompt, instruction, and source chunk.

**Possible solutions:**
- **Relevance filtering:** Before sending chunk N, scan its source text and only include memory entries for words that actually appear in this chunk. Words from chapter 1 that never appear again don't need to travel forever.
- **Frequency cutoff:** Only include words that appeared more than once — hapax legomena (one-time words) don't need consistency tracking.
- **Compression:** After many occurrences, collapse the history into a summary: "تقوى: primarily 'God-consciousness' (12 occurrences), occasionally 'mindful restraint' in journey/provision contexts (2 occurrences)."
- **Tiered memory:** Keep a "core glossary" (always included, high-frequency terms) and an "extended memory" (included only when the current chunk contains matching words).

### 2. The LLM disagrees with a prior translation

Chunk 15's LLM call might produce a translation for a word that contradicts what was established in chunk 3. The LLM was given the history but chose differently anyway.

**Options:**
- **Trust the LLM:** If it chose differently despite seeing the history, maybe the context genuinely warranted it. Log the divergence for human review.
- **Flag and ask:** Return the divergence to the user with both options: "In chapter 3 this was translated as X. In chapter 15 the context suggests Y. Which do you prefer?"
- **Enforce strictly:** Override the LLM and force consistency. This is the safest but kills the LLM's contextual judgment. Probably wrong for Comprehenslate's philosophy.

**Recommended:** Trust the LLM but log all divergences. Produce a "consistency report" at the end showing every word that was translated differently across the book, with contexts. The human reviewer can then decide.

### 3. The same word appears with the same meaning but a better translation exists

By chunk 20, the translator (human or LLM) might realize that the translation chosen in chunk 1 was suboptimal. The meaning is the same, but a better English word exists.

**Options:**
- **Retroactive update:** Go back and retranslate chunks 1-19 with the new word. Expensive but produces the best book.
- **Switch forward:** Use the better word from chunk 20 onward and note the inconsistency for a revision pass. Cheaper, produces a draft that needs one more pass.
- **Flag for revision:** Continue with the original word for consistency, but log "consider replacing X with Y throughout" for the revision pass.

**Recommended:** Flag for revision. First-pass consistency matters more than first-pass perfection. Revision is a separate step.

### 4. Proper nouns and transliteration

Names, place names, and technical terms need strict consistency — there's no "contextual variation" for a person's name. These should be in a separate, strict glossary that IS enforced without flexibility.

**Two-tier system:**
- **Strict glossary:** Proper nouns, names, places, fixed technical terms. Always enforce exact match.
- **Contextual memory:** Content words with meaning. Provide history, let the LLM decide.

### 5. Multi-word expressions and idioms

Some translation units are phrases, not single words. "ضرب مثلاً" (set forth a parable) is a two-word unit that should be tracked as one entry, not as "ضرب" and "مثلاً" separately.

The memory system needs to handle multi-word entries and match them before falling back to single-word lookup.

### 6. Source language has different scripts or spellings

The same word might appear in different morphological forms: "تقوى" / "اتقوا" / "يتقون" / "المتقين" — all from the same root ق-و-ي. The memory should ideally group by root, not by surface form. This requires Arabic morphological analysis (root extraction) which is a non-trivial dependency.

**Options:**
- **Surface matching only (v1):** Match exact word forms. Miss some connections but simple to implement.
- **Root-based matching (v2):** Extract roots and group by root. Catches all forms but requires a morphological analyzer.
- **Hybrid:** Surface matching with a manually maintained root-grouping table for high-frequency roots.

### 7. Audience level interacts with memory

If the audience level is "late_learner_simple," the translation memory might contain words that are too complex. The memory entry says "تقوى → God-consciousness" but for a simple audience, simpler phrasing is needed.

**Solution:** Translation memory entries should be tagged with audience level. Or: the memory provides the history, and the audience level instruction overrides word complexity independently. The LLM sees "this was translated as 'God-consciousness' before" but also "use simple daily vocabulary" — and reconciles by choosing "awareness of God" or similar.

### 8. Chapter context vs. book context

Some words have book-wide consistency needs (character names, core concepts) and others have chapter-local meaning (a metaphor used only in one chapter). The memory should distinguish between:
- **Global terms:** Appear across multiple chapters, need book-wide consistency.
- **Local terms:** Appear only within one chapter/section, don't need to persist.

This can be derived automatically: if a word only appeared in one chunk, it's local. If it appears in 3+ chunks, it's global and gets promoted to the core glossary.

---

## The Second Pass: Retranslation with Complete Knowledge

### The core problem with linear translation

When translating a book linearly (chunk by chunk, front to back), every chunk is translated with incomplete knowledge. Chapter 1 is translated knowing nothing. Chapter 10 is translated knowing what chapters 1-9 contained. Only the very last chapter is translated with full awareness of the entire book.

This means early chapters are always at a disadvantage. A word that seemed straightforward in chapter 1 might reveal unexpected depth in chapter 15. A metaphor that appeared isolated in chapter 3 might turn out to be a recurring motif by chapter 20. The translator of chapter 1 didn't know any of this.

### How the second pass works

After pass 1 completes, the translation memory is fully built — every word, every context, every meaning encountered across the entire book. The second pass retranslates with this complete picture:

**Pass 1 (discovery):**
- Translate linearly, chunk by chunk
- Build translation memory incrementally
- Each chunk has more context than the last, but early chunks have the least
- Output: a complete draft + a complete translation memory

**Pass 2 (refinement):**
- Retranslate with the full translation memory available from the start
- Chapter 1 now knows every meaning that every word will carry throughout the entire book
- The LLM can make informed choices: "this word will carry three meanings across this book — here in chapter 1, meaning A is active, so translate accordingly"
- Output: a refined translation where every chapter was translated with full-book awareness

### What changes between pass 1 and pass 2

Not every sentence changes. Many translations will be identical. What changes:

1. **Words with meanings discovered later** — chapter 1 used a narrow translation; pass 2 can choose a word that accommodates the full semantic range, or add a translator's note acknowledging the word's breadth.

2. **Foreshadowing awareness** — if a word in chapter 3 turns out to be a deliberate echo of a word in chapter 25, pass 2 can translate both in a way that preserves the echo. Pass 1 couldn't know the echo existed.

3. **Terminology stabilization** — pass 1 might have drifted before settling on the best translation for a key term. Pass 2 uses the settled term from the start.

4. **Tone and register alignment** — pass 2 knows the book's overall tone and can apply it uniformly, instead of discovering it gradually.

### Relationship to indexing

This two-pass approach is functionally equivalent to indexing + single-pass translation:

| Approach | How it works | Cost |
|---|---|---|
| **Indexing (Phase 1 → Phase 2)** | Analyze entire book first, build meaning index, then translate once with full knowledge | 1 full analysis pass + 1 translation pass |
| **Two-pass translation** | Translate once (building memory as you go), then retranslate with complete memory | 2 translation passes |

Both achieve the same result: every chapter translated with full-book awareness. They differ in cost structure:
- Indexing is cheaper if analysis is lighter than translation (likely true)
- Two-pass is simpler to implement (no separate analysis pipeline)
- They can combine: index first (builds the meaning index), translate once (builds translation memory from the index), then optionally do a refinement pass

For our first implementation, the two-pass approach is the pragmatic choice — it requires no separate analysis engine, just running the same translation pipeline twice with different starting knowledge.

### When to skip the second pass

Not every book needs it:
- **Short texts** — if the whole book fits in a few chunks, the drift is minimal
- **Simple vocabulary** — if the book doesn't use words with deep multi-meaning, pass 1 is probably fine
- **Time-sensitive work** — pass 2 doubles the cost (LLM calls, time). Sometimes a good-enough pass 1 is the right trade-off

The second pass should be an option, not a requirement. Controlled by config, like everything else.

---

## Future Considerations

### Translation memory as a reusable asset

After translating one book, the translation memory is a valuable artifact. If you translate another book by the same author, or in the same domain, the memory from the first book can serve as a starting point — pre-loading established terminology.

### Human-in-the-loop editing

The translation memory should be editable by the user. A human reviewer should be able to:
- Override a translation choice retroactively
- Mark certain entries as "locked" (never deviate)
- Add entries manually before translation begins (pre-seeding)
- Delete entries that are causing problems

### Relationship to full indexing

Full indexing (Phase 1) analyzes the entire source text upfront before any translation. It produces a complete meaning index. The translation memory builds incrementally during translation.

These can coexist:
- **Without indexing:** Translation memory builds from scratch, chunk by chunk.
- **With indexing:** Phase 1 produces a meaning index upfront. This index pre-seeds the translation memory. When translation begins, the memory is already populated with the full word inventory. Chunks still add to it (recording which translations were actually chosen), but the foundation is already there.

Indexing doesn't replace the translation memory — it gives it a head start.

### Consistency report as a quality metric

After translation, the consistency report (all divergences, all multi-meaning words, all overrides) is itself a quality artifact. It tells you:
- How consistent the translation is
- Where the hard decisions were made
- Which words carried multiple meanings (and where)
- What needs human attention in revision

This report could become a standard output alongside the translated book.
