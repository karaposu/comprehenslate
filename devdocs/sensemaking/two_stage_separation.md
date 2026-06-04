# Sensemaking: Complete Separation of Comprehend vs. Translate

---

## SV1 — Baseline Understanding

The user is asking: what if we go back to the original spec's architecture — two completely separate stages? Stage 1 comprehends the entire text (multi-dimensional understanding, meaning indexing). Stage 2 translates using that comprehension. No mixing. No incremental memory built during translation. Comprehend THEN translate.

This is the original README vision. We drifted from it by designing a single-pass system where the translation memory builds incrementally during translation. The user may be questioning whether that drift was right.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1:** The original spec (README.md) explicitly designed two phases: "Phase 1: Comprehension & Indexing" and "Phase 2: Contextual Translation."
- **C2:** We already have code: `config.py`, `models.py`, `memory.py`. These were designed for incremental memory building during translation. A complete separation would change how they're used.
- **C3:** The `indexing_enabled` toggle exists in config — it was always meant to make Phase 1 optional.
- **C4:** The two-pass approach we designed (pass 1 = translate with incremental memory, pass 2 = retranslate with complete memory) was positioned as "functionally equivalent to indexing + single-pass."

### Key Insights

- **K1:** The incremental approach (build memory during translation) was a PRAGMATIC SHORTCUT, not a design conviction. We chose it because "it requires no separate analysis engine." But the user is now asking whether a separate analysis engine is actually the right path.
- **K2:** Comprehension and translation are genuinely different cognitive operations. Comprehension asks "what does this mean?" Translation asks "how do I express this meaning in another language?" Mixing them forces the LLM to do both simultaneously, which may degrade quality on both.
- **K3:** The translation memory we built (`memory.py`) already has the data structures for a comprehension index — `WordEntry` with lemma, root, surface forms, encounters, meanings. If comprehension runs first and populates this, translation just reads it. The code barely changes.
- **K4:** The `notes.md` design principles STRONGLY favor separation. Principle after principle says "comprehend the whole before interpreting parts." The six-layer meaning extraction framework assumes the full text has been read before any interpretation begins.

### Structural Points

- **S1:** Two stages means two different LLM interactions with different prompts, different response models, and different goals.
- **S2:** Stage 1 (Comprehend) produces a ComprehensionIndex — the full meaning map of the text. Stage 2 (Translate) consumes it.
- **S3:** The ComprehensionIndex IS the TranslationMemory, pre-populated. Our `memory.py` structures already fit — they just get filled by comprehension instead of incrementally during translation.
- **S4:** "Multi-dimensional understanding" in the user's words maps to: word inventory, meaning resolution, synonym analysis, belagat analysis, six-layer extraction — the full Phase 1 from the README.

### Foundational Principles

- **F1:** "Comprehend first. Translate second." — this is literally the project's tagline. The incremental approach violated this principle pragmatically.
- **F2:** A translator who reads the whole book before translating chapter 1 produces better work than one who translates chapter 1 blind. This is universally acknowledged in human translation practice.
- **F3:** Separation of concerns: comprehension and translation are different skills with different quality criteria. Mixing them in one LLM call forces trade-offs.

### Meaning-Nodes

- **M1:** The user is returning to the founding vision after we pragmatically drifted from it.
- **M2:** "Completely separate" means the comprehension stage produces a persistent artifact (the index) that translation consumes. No data flows back from translation to comprehension.
- **M3:** This doesn't eliminate the two-pass translation idea — it replaces it with something cleaner. Instead of pass 1 (translate blind) + pass 2 (retranslate with memory), it's: comprehend (build full index) + translate once (with full knowledge).

---

## SV2 — Anchor-Informed Understanding

The picture is clearer: the user isn't proposing something new — they're proposing we IMPLEMENT THE ORIGINAL SPEC rather than the pragmatic shortcut we designed.

The incremental memory approach was our workaround for "we don't have a comprehension engine yet." But the user is saying: build the comprehension engine. Make it Stage 1. Make translation Stage 2. Complete separation.

This is architecturally cleaner and philosophically aligned with the project's core principle. The question is: does it work technically, and what changes?

---

## Phase 2 — Perspective Checking

### Technical / Logical

**Comprehension as a separate LLM pass:**
- Stage 1 reads the entire text (chunk by chunk if needed) and produces a ComprehensionIndex: every significant word, its lemma, root, all valid meanings in every context, synonym analysis, structural notes.
- Stage 2 reads the ComprehensionIndex + source text and translates, with full knowledge of every word's meaning range across the entire book.

**The LLM calls are different:**
- Stage 1 prompt: "Analyze this text. For each significant word, identify: lemma, root, all valid meanings in this context, confidence. Do NOT translate."
- Stage 2 prompt: "Translate this text. Here is the full meaning index. Use it for consistency and multi-meaning awareness."

New anchor: **Stage 1 is CHEAPER than Stage 2.** Comprehension analysis produces structured word-level output — shorter, more constrained responses than full sentence translations with alternative readings. This means the "indexing is expensive" assumption may be wrong.

**What happens to the two-pass idea?**
- With full separation: comprehend → translate (one pass). No need for pass 2.
- The two-pass approach was needed BECAUSE translation was doing comprehension's job incrementally. If comprehension is done properly upfront, one translation pass is enough.

New anchor: **Complete separation ELIMINATES the need for pass 2.** This is a cost saving, not a cost increase.

### Human / User

From the user's perspective, the workflow becomes:
1. "Comprehend my book" — produces a meaning index they can inspect, edit, correct before any translation happens.
2. "Now translate it" — using the validated index.

New anchor: **The comprehension index is a reviewable artifact.** A human expert can review the meaning index, correct wrong lemma assignments, add missing meanings, lock proper noun spellings — BEFORE translation begins. This is enormously valuable for high-stakes texts (scripture, legal documents).

### Strategic / Long-term

Complete separation means:
- The comprehension engine can improve independently of the translation engine.
- The comprehension index is reusable: comprehend once, translate to multiple target languages.
- The index can be shared between translators, reviewed by scholars, versioned.
- Different translation engines (or human translators) can consume the same index.

New anchor: **Comprehend once, translate many.** A book comprehended once can be translated into Turkish, English, French — each translation reads the same index. The comprehension work is language-pair-independent.

### Risk / Failure

- **Risk:** Comprehension without translation context might miss things. When you're translating, you discover meanings you didn't notice during analysis. The incremental approach captured these discoveries.
- **Mitigation:** Translation can still flag "I encountered a meaning not in the index" and the system can update the index. The separation is about the PRIMARY flow, not a prohibition on feedback.
- **Risk:** For long books, comprehension pass over the entire text before any translation is slow. The user has to wait.
- **Mitigation:** Comprehension is cheaper per-chunk than translation. And the user gets a reviewable artifact for their patience.

### Resource / Feasibility

Stage 1 (Comprehension) per chunk:
- Input: source text chunk (~1-3K tokens)
- Output: structured word analysis (~1-2K tokens per chunk — smaller than translation output)
- No need for translation memory injection (it's building the memory, not consuming it)
- Simpler prompt, simpler response model

Stage 2 (Translation) per chunk:
- Input: source text chunk + ComprehensionIndex (filtered to relevant words) + system prompt
- Output: TranslatedSentence with rich words, alternative readings
- ComprehensionIndex replaces the incrementally-built translation memory

New anchor: **The code changes are minimal.** `TranslationMemory` already has the right structure. We add a comprehension ingestion path (LLM analyzes text → populates memory) alongside the existing translation ingestion path (LLM translates → updates memory). The memory structure doesn't change.

### Definitional / Consistency

Does complete separation contradict anything we've established?

Checking against glossary_how.md: The translation memory was designed to "build incrementally during translation." Complete separation changes this to "build during comprehension, read during translation." The data structures are the same — only the lifecycle changes.

Checking against the two-pass design: The second pass was designed because "early chapters are translated with incomplete knowledge." Complete separation solves this problem differently — by doing comprehension first, every chapter has complete knowledge from the start. The second pass becomes unnecessary.

Checking against the critique: The lemma-as-grouping-key decision holds perfectly. Comprehension produces lemmas; translation consumes them. Nothing changes.

**No contradictions found.** The separation is consistent with all established decisions. It changes WHEN the memory is populated, not HOW.

---

## SV3 — Multi-Perspective Understanding

Major reframing: **Complete separation is not a departure — it's a return to the original vision, and it's BETTER than what we designed.**

The incremental approach was a pragmatic shortcut that created problems (early chapters lack knowledge → need pass 2 → doubles cost). Complete separation eliminates these problems by doing comprehension properly upfront.

Key expansions:
1. Comprehension is cheaper than translation per chunk — the "indexing is expensive" assumption was wrong.
2. Complete separation eliminates the need for pass 2 — net cost may be LOWER.
3. The comprehension index is a reviewable, editable, reusable artifact — this is a product feature, not just an implementation detail.
4. "Comprehend once, translate many" — a book comprehended once can be translated to any number of target languages.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: Does comprehension replace the translation memory, or is it a different thing?

**Resolution:** It's the same data structure. The `TranslationMemory` in `memory.py` IS the comprehension index. The difference is lifecycle:
- Incremental mode: memory starts empty, grows during translation
- Separated mode: memory is fully populated by comprehension, then read-only during translation (with minor updates for translation-specific discoveries)

**What is now fixed?** `TranslationMemory` serves both modes. No new data structure needed.

**What is no longer allowed?** Treating the comprehension index and translation memory as separate systems requiring separate models.

**What now depends on this choice?** The ingestion path. Currently `ingest_chunk` takes a `ChunkOutput` (translation result). We need a second ingestion path: `ingest_comprehension` that takes a comprehension analysis result.

**What changed?** The memory is mode-aware: populated by comprehension OR by translation, but the structure is identical.

---

### Ambiguity 2: What does the comprehension LLM call look like?

**Resolution:** A separate response model — `ComprehensionResult` — that captures word-level analysis WITHOUT translation:

```python
class AnalyzedWord(BaseModel):
    word: str          # surface form
    lemma: str         # dictionary headword
    root: str | None   # derivational root
    meanings: list[MeaningCandidate]  # all valid meanings in this context

class MeaningCandidate(BaseModel):
    id: str
    description: str   # meaning described in source language terms, not translated
    confidence: float

class ComprehensionResult(BaseModel):
    source: str        # original sentence
    analyzed_words: list[AnalyzedWord]
```

Note: meanings are described in source-language terms ("to set forth an example" vs "to strike physically"), NOT translated. Translation is Stage 2's job.

**What is now fixed?** Comprehension output is a new Pydantic model. It describes meanings without translating them.

**What is no longer allowed?** Having the comprehension stage produce translations. It produces understanding.

**What now depends on this choice?** A new prompt (`comprehend_instruction.py`) and a new method on `ComprehenslateLLM` (`comprehend()` alongside `translate()`).

**What changed?** The system has two distinct LLM interaction modes with different prompts and response models.

---

### Ambiguity 3: Can comprehension discover things translation can't, and vice versa?

**Resolution:** Yes, both directions. But the primary flow is comprehend → translate. Feedback from translation to comprehension is a secondary, optional loop.

- Comprehension discovers: all word meanings, structural patterns, rhetorical devices, synonym relationships — things visible from reading without the pressure to produce a translation.
- Translation discovers: target-language-specific issues that only surface when you try to express the meaning. E.g., "this Arabic concept has no single English word" — only discoverable during translation.

**What is now fixed?** Primary flow: comprehend → translate. Optional: translation can flag index gaps, triggering a re-comprehension of specific passages.

**What is no longer allowed?** Requiring translation feedback for comprehension to function. Comprehension must stand alone as a complete stage.

**What changed?** The two stages are decoupled but not hermetically sealed. Translation can request index updates, but comprehension doesn't depend on translation.

---

### Ambiguity 4: Does complete separation mean we can't do quick single-pass translation?

Counter-interpretation: sometimes you just want a quick translation without the comprehension overhead. Single-pass (incremental memory) is still useful for casual use.

**Resolution:** Both modes coexist, controlled by `indexing_enabled` in config. LOW CONFIDENCE — the user said "separate them completely" which suggests they want the separated architecture as primary. But the config toggle already exists and the incremental path already works. Keeping both is zero-cost.

**What is now fixed?** `indexing_enabled=True` runs comprehend-then-translate. `indexing_enabled=False` runs single-pass translation with incremental memory.

**What is no longer allowed?** Nothing — both paths remain viable.

**What changed?** The separated architecture is the PRIMARY mode, not a future addition. The incremental mode is the FALLBACK for quick/casual use.

---

## SV4 — Clarified Understanding

The system has two modes:

**Primary mode (indexing_enabled=True):**
```
Source text → [Comprehend all chunks] → ComprehensionIndex → [Translate all chunks] → Output
```
- Comprehension populates TranslationMemory completely before any translation begins
- Translation reads the full memory from the start — every chapter has full-book awareness
- No pass 2 needed
- Comprehension index is a reviewable, editable artifact
- "Comprehend once, translate many" to different target languages

**Fallback mode (indexing_enabled=False):**
```
Source text → [Translate chunk by chunk, building memory incrementally] → Output
```
- The current incremental approach
- Good for quick, casual translations
- Optional pass 2 for refinement

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed Variables

| Variable | Fixed Value |
|---|---|
| Primary architecture | Two completely separate stages |
| Stage 1 output | ComprehensionIndex (= populated TranslationMemory) |
| Stage 2 input | Source text + ComprehensionIndex |
| Data structure | TranslationMemory serves both modes |
| Mode switch | `indexing_enabled` in Config |
| Comprehension output model | New `ComprehensionResult` / `AnalyzedWord` Pydantic models |
| Translation flow | Comprehension populates memory; translation reads it |
| Pass 2 | Not needed when comprehension runs first |

### Eliminated Options

- Comprehension and translation in the same LLM call — eliminated (they have different prompts, different response models, different goals)
- Building a separate "ComprehensionIndex" data structure — eliminated (TranslationMemory already is the index)
- Pass 2 as a required step — eliminated (comprehension makes it unnecessary)

### Remaining Viable Paths

One open question: **how granular is comprehension?**

- **Word-level only:** identify every significant word, its lemma, meanings. Fast, cheap. Populates the word inventory.
- **Sentence-level:** word analysis + sentence structure analysis (which words are connected, what rhetorical devices are used). More expensive, richer index.
- **Passage-level:** word + sentence + inter-sentence relationships (harmony map, argument structure). Most expensive, fullest comprehension.

This maps to the depth profiles: Surface = word-level, Standard = sentence-level, Deep/Scholarly = passage-level.

**For v1:** Word-level comprehension is sufficient. It populates the TranslationMemory with lemmas, meanings, and surface forms — exactly what translation needs for consistency. Sentence-level and passage-level come later as depth profiles are implemented.

---

## SV5 — Constrained Understanding

The implementation adds to what exists:

```
comprehenslate/
├── config.py             # (exists) — indexing_enabled toggle
├── models.py             # (exists) — add ComprehensionResult, AnalyzedWord
├── memory.py             # (exists) — add ingest_comprehension() method
├── prompts/
│   ├── system_prompt.py  # (to build) — translation philosophy
│   ├── comprehend_instruction.py  # (NEW) — "analyze this text, identify words and meanings"
│   └── translate_instruction.py   # (to build) — "translate using this index"
└── llm.py                # (to build) — comprehend() and translate() methods
```

The call chain for primary mode:
```
1. user calls comprehenslate.comprehend(book_chunks)
   → for each chunk: LLM(comprehend_instruction) → ComprehensionResult
   → memory.ingest_comprehension(result) for each chunk
   → TranslationMemory is now fully populated

2. user calls comprehenslate.translate(book_chunks, memory)
   → for each chunk: memory.build_prompt_memory(tokens) → PromptMemory
   → LLM(translate_instruction + prompt_memory) → ChunkOutput
   → output collected
```

---

## SV6 — Stabilized Model

### Final Conceptual Model

**Comprehenslate is two completely separate stages:**

**Stage 1: Comprehend** — Read the entire source text. For every significant word, identify its lemma, root, and all valid meanings in context. Produce a ComprehensionIndex (which IS a populated TranslationMemory). This stage does NOT translate. It understands.

**Stage 2: Translate** — Read the source text again, this time with the full ComprehensionIndex available from the start. Every chapter has full-book awareness. Produce translations with multi-meaning preservation, audience adaptation, and word-level annotations.

**Why this is better than the incremental approach:**
1. Every chapter is translated with complete knowledge — no "early chapters are blind" problem
2. Eliminates the need for pass 2 — comprehension IS the upfront analysis pass
3. Comprehension is cheaper per-chunk than translation — net cost may be lower than two translation passes
4. The comprehension index is a reviewable, editable artifact — humans can correct it before translation
5. "Comprehend once, translate many" — one index serves translations to any number of target languages
6. Philosophically aligned: "Comprehend first. Translate second." — the project's founding principle

### How SV6 Differs from SV1

SV1 treated the user's suggestion as "going back to the original spec." SV6 reveals it's not just going back — it's going FORWARD. The complete separation:

- Eliminates pass 2 (cost saving we didn't expect)
- Creates a reviewable comprehension artifact (product feature we didn't plan)
- Enables multi-language translation from one index (capability we didn't consider)
- Requires minimal code changes (TranslationMemory already has the right structure)
- Was always the design intent — we just pragmatically delayed it

The incremental approach was the shortcut. Complete separation is the destination. And the code we built for the shortcut (`memory.py`, `models.py`) serves the destination perfectly — we just need to add the comprehension ingestion path.
