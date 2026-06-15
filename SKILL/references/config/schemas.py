from typing import Literal

from pydantic import BaseModel


class TranslationConfig(BaseModel):
    """User-facing translation strategy."""
    reader_level:      Literal["very_basic", "daily", "conversational", "advanced", "native"]            = "conversational"
    domain_expertise:  Literal["lay", "aware", "educated", "trained", "expert"]                          = "aware"
    source_culture:    Literal["outsider", "acquainted", "familiar", "heritage", "source-native"]        = "acquainted"
    purpose:           Literal["scholarly", "devotional", "casual", "language-learning", "performance"]  = "casual"
    source_fidelity:   Literal["foreignized-max", "foreignized", "balanced", "lightly-domesticated"]     = "balanced"
    form_preservation: Literal["off", "minimal", "light", "standard", "maximum"]                         = "standard"
    scaffolding:       Literal["off", "minimal", "standard", "rich", "scholarly"]                        = "minimal"
    analysis_depth:    Literal["none", "surface", "standard", "deep", "scholarly"]                       = "none"


class NonMainLangPartsPolicy(BaseModel):
    """Policy for quotes, mentions, and references in a non-main language in the text.

    Edge case: one chapter can have canon language A while another chapter
    has canon language B; and a single chapter can carry two canon languages.
    """
    policy: Literal[
        "preserve-original",
        "preserve-original-and-add-translation-as-a-note",
        "replace-original-with-translation",
        "replace-original-with-translation-add-original-as-a-note",
        "replace-original-with-infamous-translation",  # use the accepted famous rendering when the quote is famous
    ] = "preserve-original-and-add-translation-as-a-note"


class SourceApparatusPolicy(BaseModel):
    """How to handle the source's pre-existing apparatus (author's marginal
    annotations, glosses). Edge case: Said Nursi's hashiye; Talmud's marginal
    commentary; critical-edition apparatus criticus."""
    policy: Literal[
        "drop",
        "translate-inline-bracketed",
        "translate-as-footnote",
        "preserve-as-source-channel",
    ] = "translate-as-footnote"


class VoiceMarkingPolicy(BaseModel):
    """How to mark transitions between author voice and cited authorities or
    student-voice additions."""
    policy: Literal[
        "off",
        "as-in-original",
        "implicit-typographic",
        "explicit-attribution-inline",
        "scholarly-apparatus-marking",
    ] = "as-in-original"


class ArchaicRegisterPolicy(BaseModel):
    """How to render archaic source-language register in the target translation.

    Carries the source_temporal_register field re-homed from the dropped
    SourceDescriptor. Distinct from AnachronismHandlingPolicy: this is about
    archaic language; that is about archaic referents.
    """
    policy: Literal[
        "preserve-archaic-throughout",
        "modernize-fully",
        "hybrid-by-register-domain",
        "mark-archaisms-explicitly",
    ] = "hybrid-by-register-domain"


class HonorificsPolicy(BaseModel):
    """How to render theological honorifics that follow names.

    Edge case: Islamic SAW/AS/RA/PBUH family; Jewish ZT"L/RA/OBM family;
    Hindu śrī and analogous conventions in other traditions.
    """
    policy: Literal[
        "preserve-original-script",
        "transliterate-with-original",
        "translate-meaning",
        "abbreviate-translated",
        "drop",
    ] = "transliterate-with-original"


class FormulaicOpeningPolicy(BaseModel):
    """How to render formulaic openings (invocations, basmala, dedicatory
    formulae).

    Edge case: Islamic Bismillah; Jewish Shema; Christian invocations;
    Vedic mantras and similar dedicatory formulae.
    """
    policy: Literal[
        "preserve-original-with-translation",
        "transliterate-with-translation",
        "translate-only",
        "preserve-original-untranslated",
    ] = "preserve-original-with-translation"


class EmbeddedPoetryPolicy(BaseModel):
    """How to render embedded poetry, distinct from prose embedded language
    (which NonMainLangPartsPolicy governs).

    Edge case: Mevlana couplets embedded in Nursi's prose; Tanakh psalms in
    prose-Bible commentary; Sanskrit slokas in Hindu prose.
    """
    policy: Literal[
        "preserve-original-with-prose-gloss",
        "translate-as-verse",
        "translate-as-prose",
        "facing-original-with-meter-notes",
    ] = "preserve-original-with-prose-gloss"


class PipelineConfig(BaseModel):
    """Runtime engine knobs. Not user-facing translation strategy."""
    chunking_budget: int | None = None
    chunking_granularity: Literal[
        "sentence", "paragraph", "passage", "subchapter", "chapter"
    ] | None = None
    chunking_mechanism_override: Literal[
        "structural", "harmony-tier-aware", "passage-typology-aware",
        "llm-detected", "fixed-budget-with-snap", "hybrid",
    ] | None = None

    parallel_mode: Literal["off", "intra-chapter", "full"] = "off"
    """How parallel the translation pipeline runs.

    'off' — strict sequential; preserves terminology consistency end-to-end.
    'intra-chapter' — chunks within a chapter parallelize; chapters sequential.
    'full' — maximum parallelism; risk of cross-section terminology drift.

    Default 'off' is conservative — opt into parallelism explicitly because
    it has real semantic consequences (terminology consistency vs latency).
    """

    parallel_batch_size: int | None = None
    """Max concurrent LLM calls when parallel_mode != 'off'. None = engine default."""

    output_format: Literal["md", "html", "plain", "json"] = "md"
    """Output format the translation pipeline produces."""
