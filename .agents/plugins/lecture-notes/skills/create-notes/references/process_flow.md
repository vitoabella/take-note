---
diagram_engine: "markdown_table"
foldable_callouts: true
---

# Process Flow Module Specification

Use this module to detail algorithmic, protocol, or procedural execution steps that require formal accounting of Input -> Transformation -> Output & Next State.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:process_flow section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
| Step | Action / Phase | Input Parameters | Transformation / Rule | Output & Mutated State |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `<Initial Setup>` | `<input_arguments>` | `<initialization_logic>` | `<initial_state_record>` |
| **2** | `<Core Processing>` | `<intermediate_state>` | `<algorithmic_operation>` | `<transformed_data>` |
| **3** | `<Validation / Check>` | `<transformed_data>` | `<invariant_verification>` | `<valid_boolean_or_error>` |
| **4** | `<Finalization>` | `<verified_data>` | `<storage_or_transmission>` | `<final_state_result>` |

> [!info]- Operational Edge Cases & Preconditions
> - **Precondition**: <Required system state prior to Step 1 execution.>
> - **Invariant Maintained**: <Property that holds true across every step of execution.>
> - **Exception Handling**: <System behavior if validation fails at any intermediate step.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 3 steps | 3-row high-level execution table; omit callout | Concise, procedural | Open table |
| **`2`** | 4–5 steps | Execution table + folded preconditions & invariants callout | Standard operational | Table open, callout folded (`-`) |
| **`3`** | 6+ steps | Granular step table + formal mathematical operations + full edge-case callout | Formal, rigorous | Table open, callout folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the table/callout directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **No Narrative Paragraphs in Cells**: Table cells must use tight, structured technical phrasing.
