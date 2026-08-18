# Route Engagements — translation_error_root_causes

> Run-log for this inquiry's routes. Append-only; routelog-owned. The source of truth for
> WHAT was engaged and what came of it — not a record of decisions about what to run next
> (that is the Selector's queue), and not process state for `_route.md`. Current state of a
> route = the last row that mentions it.

| timestamp (UTC) | route | event | status | reason | artifacts | outcome | source |
|---|---|---|---|---|---|---|---|
| 2026-08-15T08:07Z | 1 · the five-property frame's own precision | done | closed | done | `finding.md` §2, §3 | axis renamed `what` → `specification`; count re-derived and holds at 5 | — |

---

## Engagement notes

**Route 1 done (2026-08-15T08:07Z)** — recorded retroactively; no prior `start` row, because the rename half of this route was executed inside CONCLUDE while compiling the finding, before the route-map existed as a separate artifact.

*What was engaged.* Two sub-tasks, per the route's guidance.

1. **The rename — completed during CONCLUDE.** Slot 1 of the five-property frame carried three different concepts: its name said *subject* ("the check's subject — the thing it is defined to look at"), its determination question asked *existence* ("is this check named anywhere, or assumed?"), and the gap-kind table called it *scope*. All three now read as one thing — **specification**, defined as "whether the check is defined at all, and over what." Verified by grep: `scope` no longer appears anywhere in `finding.md` as an axis or gap-kind name (the two remaining hits are ordinary English). The merge is legitimate because existence is the degenerate case of extent — a check defined over nothing is a check that does not exist.

2. **The count re-derivation — completed at this engagement, and it corrects the critique that prompted the route.** The critique's C13-3 reasoned: *"either `what` and `scope` are one axis under two names — in which case the frame is four properties plus a naming error, and 'July fixed one of five' becomes 'one of four'."* That inference assumed two separate slots were being conflated. Checking the pre-rename tables in `docarchive/innovation.md`: the property list ran **What** · Vantage · Instrument · Position · Time, and the gap-kind list ran Instrument · Position · **Scope** · Vantage · Timing — already 1:1, one slot named inconsistently across two tables. Merging the names removes no slot. **The count was never at risk; it holds at five.** The repair the critique proposed is right; the arithmetic alarm attached to it was not.

*What this unblocks.* The `one of five` arithmetic in `finding.md` §5 — the whole meta-structural explanation of why the July fix failed — was resting on an unverified count and is now safe to state. The frame's first slot also becomes usable in the forward-classification procedure (§3): with the name and the question disagreeing, "what is this check's subject?" sorted nothing; "is it defined, and over what?" classifies an unrun check immediately. And the tuple proposed in the finding's COULD item — `(specification, vantage, instrument, position, invalidated-by)` — now has a coherent first slot.

*Residual surfaced, not closed.* The merged axis covers two situations the frame flattens: **narrow-by-design** (the verification pass excludes config checks deliberately — the method file says so, so repairing it means arguing with a design decision) and **absent-by-oversight** (nothing checks footnote density — repairing it means writing the check). Both classify as specification gaps, which is correct at the diagnosis layer. The difference will bite at the repair layer, and the *repair* guidance should split even though the axis stays single. Not carried into `finding.md`; noted here.

*Goal served.* `_branch.md`'s goal — a causal account naming what the process lacked. This route was `core` because the account's arithmetic depends on the count and its forward-classification depends on slot 1 being applicable.
