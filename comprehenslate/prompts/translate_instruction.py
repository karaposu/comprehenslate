"""Translate instruction builder. Produces the user message for each translation chunk.

Contains the source text, target language, and optionally the rendered
Prompt View (memory hints from the Comprehension Index).
"""

from __future__ import annotations

from comprehenslate.memory import PromptMemory


def build_instruction(
    source_text: str,
    target_language: str,
    prompt_memory: PromptMemory | None = None,
) -> str:
    """Build the per-chunk user message for the translation LLM call."""
    parts: list[str] = []

    # Memory hints (if available)
    if prompt_memory is not None:
        rendered = prompt_memory.render()
        if rendered:
            parts.append(rendered)

    # Task instruction
    parts.append(
        f"Translate the following source text into {target_language}. "
        "Translate sentence by sentence. For each sentence, provide the "
        "primary translation. If a word carries multiple valid meanings "
        "in context, identify it as a rich word and list all valid meanings "
        "with confidence scores."
    )

    # Source text
    parts.append(f"=== Source Text ===\n{source_text}")

    return "\n\n".join(parts)
