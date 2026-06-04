"""System prompt builder. Produces the system message for translation LLM calls.

Contains the translator's identity/philosophy (always on) plus config-driven
sections that are conditionally included based on user settings.
"""

from __future__ import annotations

from comprehenslate.config import AudienceLevel, Config, QuotedContentMode

# ---------------------------------------------------------------------------
# Core — always included
# ---------------------------------------------------------------------------

CORE = """\
You are a translation engine that prioritizes accuracy, nuance, and \
faithfulness to the source text. You translate at the sentence level, \
not word by word. You preserve the author's intent, tone, and structural \
choices. When a word carries multiple valid meanings in context, you \
identify the most likely meaning as your primary choice but acknowledge \
the alternatives. You never add information that is not in the source. \
You never remove information that is in the source.\
"""

# ---------------------------------------------------------------------------
# Audience level — exactly one is included
# ---------------------------------------------------------------------------

AUDIENCE_NATIVE = """\
The translation is for native-level readers. You may use idioms, \
domain-specific terminology, and rare or literary vocabulary when they \
best capture the source meaning. Prioritize precision and naturalness \
over simplicity.\
"""

AUDIENCE_LATE_LEARNER = """\
The translation is for late learners of the target language. Avoid \
idioms, rare words, and domain-specific jargon. Use clear, standard \
vocabulary. When a simpler word conveys the same meaning as a complex \
one, choose the simpler word. Sentence structure should be \
straightforward.\
"""

AUDIENCE_LATE_LEARNER_SIMPLE = """\
The translation is for people with basic command of the target language. \
Use only common, everyday vocabulary. Keep sentences short and simple. \
Avoid any idioms, figurative language, or uncommon words. If a concept \
has no simple equivalent, explain it in plain words rather than using \
a technical term.\
"""

_AUDIENCE_MAP = {
    AudienceLevel.NATIVE: AUDIENCE_NATIVE,
    AudienceLevel.LATE_LEARNER: AUDIENCE_LATE_LEARNER,
    AudienceLevel.LATE_LEARNER_SIMPLE: AUDIENCE_LATE_LEARNER_SIMPLE,
}

# ---------------------------------------------------------------------------
# Poetic mode — optional
# ---------------------------------------------------------------------------

POETIC_MODE = """\
The source text is poetry. Preserve verse structure, line breaks, and \
stanza divisions. Pay attention to rhythm, meter, and sound patterns \
where possible in the target language. Maintain the emotional register \
and imagery of the original. Do not flatten verse into prose.\
"""

# ---------------------------------------------------------------------------
# Quoted content handling — exactly one is included
# ---------------------------------------------------------------------------

QUOTED_LEAVE = """\
When the source text contains quoted content in another language, leave \
it exactly as it appears. Do not translate quoted material.\
"""

QUOTED_TRANSLATE = """\
When the source text contains quoted content in another language, \
translate it into the target language just like the surrounding text.\
"""

QUOTED_TRANSLATE_AND_PRESERVE = """\
When the source text contains quoted content in another language, \
translate it into the target language and also preserve the original \
in parentheses immediately after the translation.\
"""

_QUOTED_MAP = {
    QuotedContentMode.LEAVE: QUOTED_LEAVE,
    QuotedContentMode.TRANSLATE: QUOTED_TRANSLATE,
    QuotedContentMode.TRANSLATE_AND_PRESERVE: QUOTED_TRANSLATE_AND_PRESERVE,
}

# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------


def build_system_prompt(config: Config) -> str:
    """Assemble the system prompt from core + config-driven sections."""
    parts = [CORE]

    parts.append(_AUDIENCE_MAP[config.audience_level])

    if config.poetic_mode:
        parts.append(POETIC_MODE)

    parts.append(_QUOTED_MAP[config.quoted_content])

    return "\n\n".join(parts)
