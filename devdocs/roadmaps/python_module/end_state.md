# End State

A working, installable Python module (`comprehenslate`) that implements the full translation engine with all configuration options from `how_config_should_be.md`.

## Required Capabilities

1. **Optional/toggleable indexing** — Phase 1 comprehension & indexing can be skipped for quick translations
2. **Optional/toggleable harmony layer** — 3-pass harmony preservation can be enabled/disabled
3. **Target audience level** — translation adapts to: native (idioms, rare words allowed), late learner (no idioms), late learner simple (daily language only)
4. **Poetic translation mode** — specialized mode for poetry
5. **Quoted content handling** — three modes: leave as-is, translate only, translate with original preserved
6. **Chunking strategies** — semantic chunking (chapter/section/page) and heuristic chunking with overlapping
7. **Context-aware consistency** — awareness of past context and translations across chunks
8. **Parallel batch processing** — chapter-threaded parallel processing + naive parallel processing
9. **Output formatting** — supports markdown and PDF output
10. **Original format preservation** — preserve fonts, formats, colors, backgrounds from source

## Module Qualities
- Installable via pip
- Clean Python API for programmatic use
- Configurable via code or config file
- LLM-powered (uses an LLM backend for comprehension and translation)
