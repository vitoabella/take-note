---
diagram_engine: "ascii_or_unicode"
foldable_callouts: true
---

# Layered Stack Module Specification

Use this module to visualize vertical abstraction hierarchies, encapsulation layers, protocol stacks, and architectural boundary transitions.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:layered_stack section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
```text
+-------------------------------------------------------------------+
| Layer N: <Topmost Abstraction / User Interface / Application>     |
| Responsibilities: <High-level data representation and user logic> |
+-------------------------------------------------------------------+
| Layer N-1: <Intermediate Service / Transport / Protocol>         |
| Responsibilities: <Session management, routing, or serialization> |
+-------------------------------------------------------------------+
| Layer 1: <Foundation / Hardware / Physical / Kernel Primitive>    |
| Responsibilities: <Raw signal execution, hardware registers, IO>  |
+-------------------------------------------------------------------+
```

> [!info]- Encapsulation & Boundary Crossings
> - **<Layer N> -> <Layer N-1>**: <How data artifact is wrapped, formatted, or handed off across boundary.>
> - **<Layer N-1> -> <Layer 1>**: <How intermediate state is converted into physical or foundational primitives.>
> - **Cross-Layer Leakage / Risks**: <Potential abstraction leaks, performance friction, or security vulnerabilities.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 3 layers | Ascending layer table with names and core duties; omit callout | Clean, structural | Open ASCII table |
| **`2`** | 4–5 layers | Layer table + folded encapsulation walkthrough | Standard technical | Table open, callout folded (`-`) |
| **`3`** | Full stack + boundaries | Full stack + encapsulation headers, boundaries, and leakage risks | Rigorous, architectural | Table open, callout folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the ASCII table/callout directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **Strict Vertical Ordering**: Hardware/physical layer must be at the bottom; highest user/application layer must be at the top.
- **No Flat Relationships**: Only use when components exhibit genuine vertical encapsulation or tiered abstraction.
