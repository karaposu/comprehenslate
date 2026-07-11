# State: multi-format intake acceptance

## Flow-type
articulated-surfacing-routed

## Pipeline
A → Su → S → D → I → C → R (always)

## Progress
- [x] Articulate-Simple
- [x] Surfacing
- [x] Sensemaking
- [x] Decomposition
- [x] Innovation
- [x] Critique
- [x] Routelister

## Iteration
1

## Status
COMPLETE

## Next Discipline
—

## Relationships
- CONTINUES FROM: devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/finding.md (format priority = EPUB-first + PDF-fallback; DEFERRED 1 = Word + plain-text deferred; this inquiry refines DEFERRED 1 by splitting txt + md as accepted from Word as deferred)

## History
- 2026-06-18_10-35: Created. Question: Should intake accept txt + md + pdf + epub all four, with EPUB chosen for complex content? Articulation: HIGH-PROCEED (Itemize count = 1; flagged: none). MQA: surface (2 irreducible overlaps — decision-mode + routing-mechanism).
- 2026-06-18_10-41: Surfacing complete. 59 candidates across 10 sub-regions (A per-format fidelity; B routing-mechanism; C complex-content detection; D DEFERRED 1 re-examination; E "all 3 vs 4" transcription; F acceptance-vs-priority semantic; G EPUB-preference formalization; H use-case scenarios; I Pandoc's role; J quality-tier scheme). 32 core / 18 sub / 9 side / 0 umbrella. 5 frontier flags. Verdict: PROCEED.
- 2026-06-18_10-45: Sensemaking complete. SUBSTANTIVE VERDICT: user's proposal is correct; all 4 formats accepted; EPUB correctly chosen for complex content; prior DEFERRED 1 wording REFINED via acceptance-vs-priority distinction (Word stays priority-deferred; txt + md always accepted at lower quality-tier via Pandoc baseline). Per-format 4×2 matrix committed (acceptance × priority); routing = hybrid auto-detect + warn-and-degrade + UI recommendation; complex-content detection = documentation + UI only; quality-tier flag extends Category 7. 8 ambiguities resolved (HIGH or HIGH-MED confidence). 6 perspectives applied. Inherited Decision 5 (Pandoc + OCR lever) confirmed and strengthened. Verdict: PROCEED.
- 2026-06-18_10-48: Decomposition complete. 8 pieces (P1-P8): P1 exec → P2 (META) acceptance-vs-priority + decision-mode + refines: → P3 per-format 4×2 matrix → (P4 routing+complex-detection ‖ P5 quality-tier flag ‖ P6 inherited re-test) → P7 transition → P8 open questions → P1. 11 interfaces mapped; assumptions-not-data check applied. Self-eval 7/7 PASS. Determination-mechanism check PASS (P2 specifies the distinction's runtime application). Verdict: PROCEED.
- 2026-06-18_10-52: Innovation complete. Per-piece content for all 8 pieces. Full mechanism coverage (4G+3F). 2 meta-decision pieces (P2 + P6) Piece-Level Inversion satisfied. Concrete: per-format matrix; magic-bytes routing; quality-tier flag schema; transition refinements identifying specific prior MUSTs to update. Anti-hallucination: Pandoc format matrix (epub/html/md/docx native; pdf via pdftotext) verified; python-magic library confirmed real. Inherited Frame Audit did not fire. Verdict: PROCEED.
- 2026-06-18_10-56: Critique complete. SURVIVE-with-cross-cutting-refinements. Architecture SURVIVES (acceptance-vs-priority distinction + per-format matrix + routing + quality-tier flag + refines: label). 6 piece-level REFINEs (P2 verbatim citation; P3 Word row consistency; P4 mismatch-flag downstream consequence; P6 Decision 5 PRESERVED not STRENGTHENED; P7 update-prior MUST rewording; P8 add 4 frontier items). 1 clean SURVIVE (P5). 12 dimensions FULL; STRONG adversarial; STABLE landscape; mechanism-independence VALIDATED via verbatim grep of prior's DEFERRED 1 wording. No failure modes. Verdict: PROCEED.
- 2026-06-18_11-00: Routelister complete. 17 onward concept-identities (R1-R17): 3 MUSTs (R1-R3) + 1 critique-refinements bundle (R4) + 2 COULDs (R5-R6) + 1 DEFERRED cross-reference (R7) + 4 onward-engineering (R8-R10, R17) + 6 frontier (R11-R16). 3 cross-references to prior inquiry's routes (R7↔prior R11; R9↔prior R19; R15↔prior R20). No LAYER 1/2 failure modes. Verdict: PROCEED.
- 2026-06-18_11-03: CONCLUDE complete. Finding answer (one sentence): yes, intake accepts all 4 user-named formats (txt + md + pdf + epub) and EPUB is correctly chosen for complex content; the user's proposal and the prior commitment both hold under the load-bearing acceptance-vs-priority distinction (the prior's DEFERRED 1 was priority-deferred, not acceptance-deferred); per-format 4×2 matrix committed; hybrid auto-detect + warn-and-degrade + UI recommendation routing; quality-tier flag extends prior Category 7 schema. 6 critique refinements applied during finding composition. Six discipline outputs archived to docarchive/; routelister.md + _route.md remain in root. Status: COMPLETE.
