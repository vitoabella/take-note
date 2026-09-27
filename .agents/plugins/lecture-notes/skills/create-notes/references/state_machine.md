---
diagram_engine: "ascii_or_mermaid"
foldable_callouts: true
---

# State Machine Module Specification

Use this module to model systems with discrete lifecycle states, transition triggers (events/actions), and valid execution paths.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:state_machine section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
```text
[ <STATE_INITIAL> ]
         │
         │  ( <Trigger Event 1> / <Resulting Action 1> )
         ▼
[ <STATE_INTERMEDIATE> ] ─── ( <Trigger Event 2> / <Action 2> ) ───> [ <STATE_ACTIVE> ]
         │                                                                   │
         │  ( <Error Event> / <Reset Action> )                               │  ( <Close Event> )
         ▼                                                                   ▼
[ <STATE_HALTED> ]                                                  [ <STATE_TERMINATED> ]
```

> [!info]- State Transition Table
> | Current State | Trigger Event / Condition | Action Executed | Next State |
> | :--- | :--- | :--- | :--- |
> | `<STATE_INITIAL>` | `<event_1>` | `<action_1>` | `<STATE_INTERMEDIATE>` |
> | `<STATE_INTERMEDIATE>` | `<event_2>` | `<action_2>` | `<STATE_ACTIVE>` |
> | `<STATE_ACTIVE>` | `<event_close>` | `<action_cleanup>` | `<STATE_TERMINATED>` |
> | `<STATE_INTERMEDIATE>` | `<event_error>` | `<action_abort>` | `<STATE_HALTED>` |
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 2–3 states | High-level state transition diagram only; omit table | Clear, structural | Open ASCII diagram |
| **`2`** | 3–5 states | Transition diagram + folded transition table with triggers & actions | Standard operational | Diagram open, table folded (`-`) |
| **`3`** | Full lifecycle | Full diagram with loops/error states + transition table + invalid transition guards | Comprehensive, formal | Diagram open, table folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the state diagram/table directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **Annotated Transitions**: Every state transition arrow must document the trigger event and resulting action `(Event / Action)`.
