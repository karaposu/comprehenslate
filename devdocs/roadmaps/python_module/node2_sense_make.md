# Node 2 — Structural Sensemaking Analysis

## SV1 — Baseline Understanding

Node 2 is about building the data layer and LLM plumbing for Comprehenslate. The user wants:
- Pydantic models for data contracts
- LangChain `with_structured_output` for LLM calls
- A `prompts/` folder with `system_prompt.py` (derived from `notes.md`) and `translate_instruction.py`
- Possibly Proteas for conditional prompt assembly (since features are toggleable)
- Config dataclass to hold everything cleanly
- Scope narrowing: skip indexing and depth profiles for now; audience level IS important

At this stage, the picture is fuzzy — we know the ingredients but not how they combine.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1:** LLM calls must use LangChain's `with_structured_output` — this means Pydantic models serve double duty: data contracts AND LLM response schemas.
- **C2:** Prompts live in a `prompts/` folder as `.py` files (not `.txt` or `.jinja2`) — they're code, not templates.
- **C3:** Indexing is skipped for now — Phase 1's deep comprehension engine is deferred.
- **C4:** Depth profiles are skipped for now — no surface/standard/deep/scholarly switching yet.
- **C5:** Audience level (native/late_learner/late_learner_simple) MUST be implemented — it affects translation output.
- **C6:** Config already exists as a dataclass in `comprehenslate/config.py` from Node 1.

### Key Insights

- **K1:** `with_structured_output` means the Pydantic model IS the prompt's output contract. The LLM is forced to return data matching the model. This eliminates JSON parsing — LangChain handles it.
- **K2:** Proteas is a prompt assembly tool: define reusable `PromptTemplateUnit` blocks, enable/disable them conditionally, compile into a single prompt string. The question is whether Comprehenslate's toggleable features need this level of prompt composition.
- **K3:** `notes.md` contains 300+ design principles — these aren't individual prompts, they're a massive system prompt that teaches the LLM HOW to think about translation. This is a single, large system prompt, not a collection of toggleable units.
- **K4:** The translate instruction is a separate concern from the system prompt — the system prompt establishes the LLM's "expertise," the translate instruction tells it what to do with a specific piece of text.
- **K5:** Audience level affects the translation instruction, not the system prompt. The system prompt is stable; the instruction varies per request.

### Structural Points

- **S1:** Two prompt layers: system prompt (stable, large, from `notes.md`) + instruction prompt (per-request, varies by config).
- **S2:** The instruction prompt has conditional sections: audience level always applies; harmony, poetic mode, quoted content handling are toggleable.
- **S3:** Data flows: source text → LLM (with system prompt + instruction) → Pydantic response model → downstream processing.
- **S4:** Config dataclass already exists — it should be the single source of truth that the prompt builder reads.

### Foundational Principles

- **F1:** The LLM is the engine — Comprehenslate is an orchestrator that crafts the right prompt and parses the structured response.
- **F2:** Prompt quality determines output quality. The system prompt derived from `notes.md` is the core intellectual property.
- **F3:** Pydantic models are the contract between what the LLM returns and what downstream code consumes.

### Meaning-Nodes

- **M1:** "System prompt" = the LLM's translation philosophy, derived from 300+ principles in `notes.md`.
- **M2:** "Translate instruction" = the per-request instruction that includes source text, target language, audience level, and feature toggles.
- **M3:** "Structured output" = Pydantic model that the LLM must conform to.

---

## SV2 — Anchor-Informed Understanding

The picture sharpens: Node 2 is really about three things, not two:

1. **The system prompt** — a large, stable prompt distilled from `notes.md` that makes the LLM think like a Comprehenslate translator. This is NOT toggleable. It's always on.
2. **The instruction builder** — a function that takes `Config` + source text and produces the per-request instruction. This IS where toggleable features live (audience level, harmony, poetic mode, quoted content).
3. **The response models** — Pydantic models that define what the LLM returns. These are the data contracts downstream code depends on.

The LangChain `with_structured_output` integration is straightforward plumbing once 1-3 are defined.

---

## Phase 2 — Perspective Checking

### Technical / Logical

- LangChain's `with_structured_output` works by passing a Pydantic model to the LLM, which constrains the response. This means response model design directly affects what the LLM can express.
- The system prompt from `notes.md` is ~8000+ words. This is fine for modern LLMs with large context windows but needs to be tested for whether it degrades response quality.
- New anchor: **The response model should be minimal for now** — match what we actually need (translated text + audience-adapted output), not the full vision (six-layer output, harmony reports, etc.).

### Human / User

- The user (developer using this module) will call something like `comprehenslate.translate(text, target_lang)` and get back a structured result.
- Audience level is the key differentiator users care about now — "translate this for a native speaker" vs. "translate this for a learner."
- New anchor: **The API surface should be dead simple** — one main function, config controls behavior.

### Strategic / Long-term

- The system prompt is the hardest thing to get right and the most valuable to iterate on.
- The response models will expand over time (add meaning layers, synonym analysis, etc.) — design for extension.
- Proteas becomes more valuable as features multiply. Right now with just audience level + a few toggles, it may be overkill.

### Risk / Failure

- Risk: system prompt too large → LLM ignores parts of it → bad output.
- Risk: Pydantic model too rigid → can't capture the richness of what the LLM wants to say.
- Risk: over-engineering the prompt assembly when simple f-string or string concatenation would work.
- New anchor: **Start simple, add Proteas later when prompt complexity justifies it.**

### Resource / Feasibility

- Proteas is an external dependency owned by the same user — low risk to adopt, but adds complexity.
- LangChain is a heavy dependency. Consider whether `with_structured_output` is worth the full LangChain import or if a lighter approach (direct API + Pydantic + instructor) would suffice.
- New anchor: **LangChain is the chosen tool — the user specified it. Don't second-guess.**

---

## SV3 — Multi-Perspective Understanding

Major shifts from SV2:

1. **Proteas is premature for now.** With only audience level as a must-have toggle and a few optional features, the instruction prompt can be built with simple conditional string building. Proteas becomes valuable when we have 5+ independently toggleable prompt sections — we're not there yet.
2. **The system prompt is a monolithic asset.** It doesn't get toggled or composed. It's a single, carefully crafted document. It lives in `prompts/system_prompt.py` as a constant string.
3. **The response model should be scoped to current needs.** A `TranslationResult` with translated text, per-sentence breakdowns, and audience-level annotations — not the full six-layer vision.
4. **The instruction builder is just a function** that reads `Config` and produces a prompt string. No framework needed yet.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: Do we need Proteas now?

**Resolution:** No. Not for this iteration.

**What is now fixed?** Prompt assembly is done via a plain Python function that reads `Config` and builds the instruction string with conditional sections (if/else on config fields). No external prompt-composition library.

**What is no longer allowed?** Introducing Proteas as a dependency in Node 2. The prompt builder is a function, not a framework.

**What now depends on this choice?** When the number of toggleable prompt sections grows beyond 5-6, we should revisit and migrate to Proteas. For now, the function stays simple.

**What changed in the conceptual model?** Prompt assembly is simpler than initially feared. The complexity lives in the system prompt's CONTENT, not in the prompt's COMPOSITION.

---

### Ambiguity 2: What does the response model look like?

**Resolution:** A `TranslationResult` Pydantic model scoped to current needs:
- `sentences`: list of `TranslatedSentence` (source text, translated text, notes)
- `TranslatedSentence` includes `audience_adaptations` when audience level affects word choice
- No harmony reports, no six-layer output, no synonym maps yet

**What is now fixed?** The response schema. Downstream code (Node 4) consumes `TranslationResult`.

**What is no longer allowed?** Building the full vision's data models now. No `MeaningIndex`, `HarmonyBlueprint`, or `LayeredOutput` until the nodes that need them.

**What now depends on this choice?** Nodes 3 and 4 will extend these models. The base `TranslatedSentence` will gain fields as features are added.

**What changed in the conceptual model?** Node 2 is smaller than originally scoped. It produces the minimum viable data models, not the complete set.

---

### Ambiguity 3: What goes in the system prompt vs. the instruction?

**Resolution:**
- **System prompt** = translation philosophy, principles from `notes.md`, the "how to think" layer. Stable across requests.
- **Instruction** = source text, target language, audience level, feature flags, "what to do now" layer. Varies per request.

**What is now fixed?** The boundary between system prompt and instruction. System prompt is a constant. Instruction is built per-request from config.

**What is no longer allowed?** Putting per-request config into the system prompt, or putting philosophy into the instruction.

**What now depends on this choice?** The system prompt file is written once and iterated on for quality. The instruction builder is a function that evolves as features are added.

**What changed in the conceptual model?** Clear separation of concerns: knowledge (system prompt) vs. task (instruction).

---

### Ambiguity 4: How much of `notes.md` goes into the system prompt?

**Resolution:** `notes.md` is a design document for US, not a prompt for the LLM. The system prompt should be a distilled, focused version — the principles that directly affect translation behavior, written as instructions to the LLM, not as analytical notes. Probably 30-50 key principles condensed into clear directives.

**What is now fixed?** `system_prompt.py` is an authored artifact, not a copy-paste of `notes.md`. It draws FROM `notes.md` but is written FOR the LLM.

**What is no longer allowed?** Dumping all 300+ notes into the system prompt verbatim.

**What now depends on this choice?** The quality of the system prompt is a manual authoring task. It's the most important creative work in the project.

**What changed in the conceptual model?** `notes.md` is the source material; `system_prompt.py` is the refined product.

---

### Ambiguity 5: What is the LLM backend abstraction?

**Resolution:** A thin wrapper class `ComprehenslateLLM` that:
- Takes a LangChain chat model (user provides their own — OpenAI, Anthropic, etc.)
- Stores the system prompt
- Has a `translate(text, config) -> TranslationResult` method that builds the instruction, calls `with_structured_output`, and returns the parsed result

**What is now fixed?** The LLM backend is not model-specific. The user passes in their LangChain model. Comprehenslate doesn't manage API keys or model selection.

**What is no longer allowed?** Hardcoding a specific LLM provider. Comprehenslate is model-agnostic.

**What now depends on this choice?** The user must install LangChain and their chosen provider package. Comprehenslate declares `langchain-core` as a dependency.

**What changed in the conceptual model?** Comprehenslate is a translation ORCHESTRATOR, not an LLM wrapper. It adds value through its prompts and structured output, not through LLM access.

---

## SV4 — Clarified Understanding

Node 2 is now clear and scoped:

1. **`prompts/system_prompt.py`** — A distilled translation philosophy derived from `notes.md`. A carefully authored system prompt that teaches the LLM the Comprehenslate approach. ~30-50 key principles as LLM-facing directives.

2. **`prompts/translate_instruction.py`** — A `build_instruction(config, source_text, target_language)` function that produces the per-request instruction. Conditionally includes audience level directives, quoted content handling mode, poetic mode flag. Simple if/else logic, no Proteas.

3. **`models.py`** — Pydantic models: `TranslatedSentence` and `TranslationResult`. Minimal, extendable. These are the response schemas for `with_structured_output`.

4. **`llm.py`** — `ComprehenslateLLM` class. Takes a LangChain chat model. Has `translate()` method. Wires system prompt + instruction + response model together.

No `MeaningIndex`, no `HarmonyBlueprint`, no `SynonymMap` yet — those come with their respective engine nodes.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed Variables

| Variable | Fixed Value |
|---|---|
| Data modeling library | Pydantic |
| LLM integration | LangChain `with_structured_output` |
| Prompt storage | Python files in `prompts/` |
| Prompt composition | Plain Python function (no Proteas) |
| System prompt source | Distilled from `notes.md`, authored manually |
| LLM provider | User-supplied (model-agnostic) |
| Scope of response models | Translation output only (no indexing, no harmony) |
| Must-implement feature | Audience level (native/late_learner/late_learner_simple) |

### Eliminated Options

- Proteas for prompt assembly (deferred)
- Full data model suite (deferred to Nodes 3-4)
- Direct API calls without LangChain (rejected — user chose LangChain)
- Copying `notes.md` verbatim as system prompt (rejected — needs distillation)
- Hardcoded LLM provider (rejected — model-agnostic)
- Indexing implementation (explicitly deferred)
- Depth profile implementation (explicitly deferred)

### Remaining Viable Paths

The only real decision left is how detailed to make the `TranslatedSentence` model:
- **Minimal:** `source`, `translation` only
- **With audience awareness:** `source`, `translation`, `audience_notes` (why a word was simplified or kept)
- **With word-level detail:** `source`, `translation`, `word_choices` (list of word-level decisions)

**Decision:** Go with audience awareness level. It directly serves the must-implement feature without over-engineering.

---

## SV5 — Constrained Understanding

The implementation is now a bounded, ordered set of tasks:

```
prompts/
├── __init__.py
├── system_prompt.py          # SYSTEM_PROMPT constant (distilled from notes.md)
└── translate_instruction.py  # build_instruction(config, text, target_lang) -> str

comprehenslate/
├── __init__.py               # (exists)
├── config.py                 # (exists)
├── models.py                 # TranslatedSentence, TranslationResult (Pydantic)
├── llm.py                    # ComprehenslateLLM class
└── prompts/                  # prompt files (see above)
```

The call chain:
```
user code
  → ComprehenslateLLM.translate(text, target_lang)
    → build_instruction(self.config, text, target_lang)  # builds instruction string
    → langchain_model.with_structured_output(TranslationResult)
    → invoke([system_message(SYSTEM_PROMPT), human_message(instruction)])
    → returns TranslationResult
```

---

## SV6 — Stabilized Model

### Final Conceptual Model

Node 2 delivers **four files** that form the bridge between config and the future engines:

1. **System Prompt** (`prompts/system_prompt.py`) — The soul of Comprehenslate. A distilled set of translation principles authored from `notes.md`. Teaches the LLM to comprehend before translating, preserve multi-meaning, analyze word choice, respect structural meaning, and adapt to audience level. This is a living document that improves over time.

2. **Instruction Builder** (`prompts/translate_instruction.py`) — A function that reads `Config` and produces the per-request prompt. Audience level is the primary variable: native gets full richness, late_learner avoids idioms and rare words, late_learner_simple uses only daily vocabulary. Other toggles (poetic mode, quoted content) are conditional additions.

3. **Response Models** (`models.py`) — Pydantic schemas that define what the LLM returns. `TranslatedSentence` has source text, translation, and audience-specific notes. `TranslationResult` is a list of these plus metadata. These models will grow as Nodes 3-4 add features.

4. **LLM Orchestrator** (`llm.py`) — `ComprehenslateLLM` takes any LangChain chat model, wires the system prompt and instruction builder together, calls `with_structured_output`, and returns typed results. Model-agnostic, provider-agnostic.

### How SV6 Differs from SV1

SV1 imagined Node 2 as a large, ambitious data modeling + LLM integration effort covering ALL data structures (meaning index, harmony blueprint, synonym maps, layered output). SV6 scopes it to what's actually needed NOW:

- **Dropped:** Full data model suite, Proteas dependency, indexing models, harmony models, depth profile logic
- **Focused:** System prompt authoring, audience-level instruction building, minimal response models, clean LLM wiring
- **Clarified:** `notes.md` is source material for humans; `system_prompt.py` is the distilled product for the LLM
- **Decided:** No Proteas yet (too few toggleable sections to justify), no provider lock-in, Pydantic models start minimal and grow

The node is now small, focused, and implementable without ambiguity.
