# Starting State

## References
- [README.md](/README.md) — core concept, two-phase architecture, feature descriptions
- [advanced.md](/advanced.md) — six-layer meaning extraction framework
- [harmony_layer.md](/harmony_layer.md) — harmony preservation 3-pass system with 4-tier priorities
- [how_config_should_be.md](/how_config_should_be.md) — configuration requirements (the target feature set)
- [notes.md](/notes.md) — 300+ design principles from classical interpretation science
- [my_notes.md](/my_notes.md) — audience-level translation notes

## What exists
- 6 markdown specification documents covering the full conceptual design
- Two-phase architecture described (Comprehension → Translation)
- Six-layer meaning extraction framework fully specified
- Harmony preservation layer fully specified with 4-tier priority system
- Configuration requirements documented
- 300+ design principles extracted
- Git repo with 3 commits

## What's designed but not built
- Core engine (word inventory, context analysis, synonym mapping, belagat)
- Meaning index data structure
- Translation engine (sentence-level translation, multi-meaning combiner)
- Harmony preservation 3-pass system
- Six-layer extraction pipeline
- All configuration options (depth profiles, toggles, audience level, chunking, output formats)
- No Python code, no pyproject.toml, no module structure, no tests

## What's incomplete
- LLM integration strategy — specs describe what, not how (prompts, orchestration, model choice)
- Input parsing / document ingestion pipeline
- Data models / schemas for meaning index, harmony map, layered output
- API surface design for the Python module
