# Roadmap: Comprehenslate Python Module

From idea-stage specifications to a working, installable Python module with all features from `how_config_should_be.md`.

---

## ASCII Overview

```
┌──────────────────────────┐     ┌──────────────────────────┐
│ 1. Module Skeleton       │     │ 2. Data Models &         │
│    & Config System       │────▶│    LLM Integration       │
│                          │     │                          │
│ clear / none / none      │     │ fuzzy / none / none      │
│ effort: M                │     │ effort: L                │
└──────────────────────────┘     └─────────────┬────────────┘
                                               │
                                               ▼
┌──────────────────────────┐     ┌──────────────────────────┐
│ 3. Phase 1 Engine        │     │ 4. Phase 2 Engine        │
│    (Comprehension)       │────▶│    (Translation)         │
│                          │     │                          │
│ clear / partial / none   │     │ clear / partial / none   │
│ effort: L                │     │ effort: L                │
└──────────────────────────┘     └─────────────┬────────────┘
                                               │
                                               ▼
┌──────────────────────────┐     ┌──────────────────────────┐
│ 5. Chunking &            │     │ 6. Output Formatting     │
│    Parallel Processing   │────▶│    & Export               │
│                          │     │                          │
│ clear / partial / none   │     │ fuzzy / none / none      │
│ effort: M                │     │ effort: M                │
└──────────────────────────┘     └──────────────────────────┘
```

**Dependency flow:** 1 → 2 → 3 → 4 → 5 → 6 (mostly linear, each builds on prior)

---

## Nodes

- [ ] **Node 1: Module Skeleton & Config System**

  **Description:** Set up the Python package structure (`comprehenslate/`), `pyproject.toml`, entry points, and the full configuration system. This includes all toggles from `how_config_should_be.md`: indexing on/off, harmony on/off, audience level (native/late_learner/late_learner_simple), poetic mode, quoted content handling mode, depth profiles, and chunking strategy selection. Configuration should be settable via Python API kwargs and/or a config dict/file.

  **Idea:** clear — the config requirements are explicitly listed in `how_config_should_be.md`
  **Design:** none — no Python API surface, no config schema, no package structure exists
  **Impl:** none

  **Depends on:** none

  **Produces:** An installable Python package with a `Comprehenslate` class (or equivalent entry point) that accepts all configuration options. No translation logic yet — just the skeleton and config plumbing.

  **Effort:** medium

  **Why this order:** Everything else depends on having a package structure and config system to hang off of. Config is the spine of the module — every downstream node reads config to decide what to do.

---

- [ ] **Node 2: Data Models & LLM Integration Layer**

  **Description:** Define the core data structures (meaning index, word inventory entry, synonym map, harmony blueprint, layered output) as Python dataclasses or Pydantic models. Build the LLM integration layer — a thin abstraction that sends prompts to an LLM and parses structured responses. This is the bridge between the spec's conceptual operations ("analyze word meanings in context") and actual executable code (an LLM call with a crafted prompt that returns structured JSON).

  **Idea:** fuzzy — the specs describe what the meaning index and harmony map *contain* but not their exact schema; the LLM orchestration strategy (which calls, what prompts, how to parse) is unspecified
  **Design:** none
  **Impl:** none

  **Depends on:** Node 1 (needs the package structure and config to know which features are active)

  **Produces:** Importable data models for all intermediate representations. A working `LLMBackend` class that can make structured calls. Prompt templates for core operations.

  **Effort:** large

  **Why this order:** Nodes 3 and 4 (the actual engines) need data models to produce and consume, and they need the LLM layer to do their work. This is the foundation layer between config and logic.

---

- [ ] **Node 3: Phase 1 Engine (Comprehension & Indexing)**

  **Description:** Implement the comprehension pipeline: word inventory extraction, contextual meaning resolution, synonym & word choice analysis, and belagat/i'caz analysis. Each sub-system takes source text + config and produces entries in the meaning index. When indexing is toggled off, this phase does a lighter single-pass analysis. When depth profile is set higher, more analysis layers activate (up to the six-layer extraction from `advanced.md`). Audience level affects which meanings are flagged as "translatable" vs "requires simplification."

  **Idea:** clear — the specs in README.md and advanced.md describe each sub-system in detail
  **Design:** partial — the *what* is well-described but *how* to prompt an LLM for each sub-system needs design
  **Impl:** none

  **Depends on:** Node 2 (needs data models and LLM layer)

  **Produces:** A `ComprehensionEngine` that takes source text and returns a populated `MeaningIndex`. Configurable by depth profile and indexing toggle.

  **Effort:** large

  **Why this order:** Phase 2 (translation) consumes the meaning index produced by Phase 1. You can't translate with comprehension-awareness without first building the comprehension.

---

- [ ] **Node 4: Phase 2 Engine (Translation + Harmony)**

  **Description:** Implement the translation pipeline: sentence-level contextual translation using the meaning index, multi-meaning combination generation, word choice annotation, and the optional 3-pass harmony preservation layer (meaning lock → harmony map → target language reconstruction). Audience level controls vocabulary and idiom usage in output. Poetic mode adjusts translation strategy for verse. Quoted content handling applies the configured mode (leave/translate/translate+preserve).

  **Idea:** clear — README.md describes the translation engine, harmony_layer.md fully specifies the 3-pass system with tier priorities
  **Design:** partial — translation prompting strategy and harmony pass orchestration need design
  **Impl:** none

  **Depends on:** Node 3 (needs the meaning index from Phase 1)

  **Produces:** A `TranslationEngine` that takes a `MeaningIndex` + source text and returns translated output with annotations. Harmony layer is toggleable. Output respects audience level, poetic mode, and quoted content settings.

  **Effort:** large

  **Why this order:** Translation is the consumer of comprehension. It also needs to exist before chunking/parallelism can be layered on top (you need a working single-document pipeline before you can split and parallelize).

---

- [ ] **Node 5: Chunking & Parallel Processing**

  **Description:** Implement document chunking strategies: semantic chunking (split by chapter/section/approximate page length) and heuristic chunking with overlapping windows. Build the consistency layer that passes context between chunks so terminology and style remain coherent. Implement parallel batch processing — chapter-threaded mode (each thread starts at a chapter boundary to preserve context) and naive parallel mode (split arbitrarily, merge results). This wraps the Phase 1 → Phase 2 pipeline and orchestrates it across chunks.

  **Idea:** clear — `how_config_should_be.md` specifies the chunking strategies and parallel modes
  **Design:** partial — overlap strategy, context-passing mechanism, and merge logic need design
  **Impl:** none

  **Depends on:** Node 4 (needs the full single-document pipeline to wrap and parallelize)

  **Produces:** A `DocumentProcessor` that handles arbitrarily long documents by chunking, parallel-processing, and merging. Configurable chunking strategy and parallelism mode.

  **Effort:** medium

  **Why this order:** Chunking and parallelism are orchestration layers around the core pipeline. The pipeline must work end-to-end on a single chunk before you can split documents into chunks and run them in parallel.

---

- [ ] **Node 6: Output Formatting & Export**

  **Description:** Implement output rendering: markdown output (with annotations, multi-meaning variants, belagat notes, harmony report), PDF export (using a library like weasyprint or reportlab), and original format preservation (detecting and replicating source document fonts, colors, layout). This is the final layer that takes the structured translation output and renders it into the user's desired format.

  **Idea:** fuzzy — markdown output is straightforward but PDF generation and especially original format preservation are underspecified (what input formats? how to detect fonts/colors?)
  **Design:** none
  **Impl:** none

  **Depends on:** Node 4 (needs structured translation output to format), Node 5 (needs merged multi-chunk output)

  **Produces:** Formatted output files (`.md`, `.pdf`). Format preservation for supported input types. The final user-facing artifact.

  **Effort:** medium

  **Why this order:** Output formatting is the last mile. It consumes the final translation output and renders it. It can't be built until the output data structure is stable, which requires the engines and chunking to be in place.

---

## Summary

**Total nodes:** 6

**By idea:** clear: 4 | fuzzy: 2 | unclear: 0
**By design:** partial: 3 | none: 3 | mostly done: 0 | crystal clear: 0
**By impl:** none: 6

**Recommended next action:** Start with **Node 1 (Module Skeleton & Config System)**. The config requirements are the clearest part of the entire project — they're explicitly listed. Building the skeleton first gives you something installable immediately and forces early decisions about API surface that inform everything downstream.

**Biggest risk:** Node 2 (LLM integration) is the highest-uncertainty node. The entire engine depends on being able to coax structured, reliable output from LLM calls — word inventories, meaning resolution, synonym analysis, harmony mapping. If the LLM can't produce consistent structured output for these tasks, the architecture needs rethinking. Prototype Node 2 early with real Arabic text samples before investing heavily in Nodes 3-4.
