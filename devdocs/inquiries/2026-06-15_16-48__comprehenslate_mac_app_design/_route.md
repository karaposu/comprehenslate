# _route.md — Persistent concept-map

**Territory:** comprehenslate_mac_app_design inquiry artifacts
**Goal:** design what Comprehenslate would look like as a Mac app (architectural sketch + feature inventory + cross-cutting concerns + MVP roadmap)

## Identity-set

- **I1** Build v1 MVP — essential tier across 5 layers + 2 providers + local LLM per Critique REFINE (HIGH; schema/UI code)
- **I2** Build v2 — differentiating tier + ~10 principle-derived features + extended exports (MED; schema/UI code; gated on v1)
- **I3** Build v3+ — deferrable tier + power-user surfaces (LOW; gated on v2)
- **I4** Choose Mac platform tech stack (SwiftUI vs AppKit; persistence layer; concurrency model) (MED; engineering decision)
- **I5** Design `.compldoc` file format (directory bundle + per-chunk schema) (HIGH; load-bearing for all layers)
- **I6** Implement multi-provider LLM abstraction (Swift protocol + 3 adapters) (HIGH; load-bearing for Execution layer)
- **I7** Produce UI/UX mockups (visual design pass; necessary before code) (HIGH; design)
- **I8** User research / persona validation (interview translators to test design assumptions) (MED; epistemic)
- **I9** Cost / feasibility validation (estimate API costs for full Nursi-corpus translation) (HIGH; risk-mitigation)
- **I10** Pick monetization model (one-time / open-source / donation-ware) (MED; business)
- **I11** Pick distribution channel (Mac App Store / direct download / both) (MED; business; gated on I10)
- **I12** Extend pattern to other Comprehenslate products (Web / Mobile) — AE1 revival (LOW; gated)
- **I13** Surface user-visible roadmap (AE2 revival) (LOW; gated on user demand)
- **I14** Extend project templates to non-Islamic corpora (LOW; gated on scope expansion)
- **I15** Implement schemas.py-aware migration tooling (MED; gated on schemas.py evolution)
- **I16** Mobile / iPad expansion (Catalyst port vs native iPad app) (LOW; deferred)
- **I17** App UI localization beyond English (Arabic at v2; others at v3+) (LOW; gated on market demand)
- **I18** Plugin / scripting API (LOW; deferred to v3+)
- **I19** Policy-class co-application precedence UX (inherited from chunk_types_vs_mechanisms inquiry; resurfaces in Config UI) (MED; epistemic)

## Invocation log

| Run | Date | Mode | Entry | Identities | Verdict |
|---|---|---|---|---|---|
| 1 | 2026-06-15_19-02 | root / breadth | fresh | 19 (all new) | PROCEED |
