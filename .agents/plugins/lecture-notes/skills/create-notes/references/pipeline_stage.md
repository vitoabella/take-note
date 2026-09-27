---
diagram_engine: "ascii_or_unicode"
foldable_callouts: true
---

# Pipeline Stage Module Specification

Use this module to model multi-stage artifact transformation pipelines where data or work items progressively evolve across distinct processing stages.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:pipeline_stage section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
```text
[ 1. <Stage Name A> ] ──( <Artifact AB> )──> [ 2. <Stage Name B> ] ──( <Artifact BC> )──> [ 3. <Stage Name C> ]
```

| Stage | Input Artifact & Format | Processing Operation | Output Artifact & Format |
| :--- | :--- | :--- | :--- |
| **1. <Stage A>** | `<input_data_type>` | `<core_transformation_algorithm>` | `<intermediate_data_type>` |
| **2. <Stage B>** | `<intermediate_data_type>` | `<core_transformation_algorithm>` | `<intermediate_data_type_2>` |
| **3. <Stage C>** | `<intermediate_data_type_2>` | `<final_reduction_or_formatting>` | `<final_output_artifact>` |

> [!info]- Artifact Invariants & Reversibility
> - **State Preservation**: <Whether intermediate representations preserve full source information or lose fidelity.>
> - **Failure & Validation Points**: <Which stage enforces validation checks or rejects malformed artifacts.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 2–3 stages | Horizontal stage diagram only; omit table and callout | High-level, structural | Open ASCII diagram |
| **`2`** | 3–4 stages | Stage diagram + Input/Transform/Output table | Standard operational | Diagram and table open |
| **`3`** | 4+ stages | Diagram + table + folded artifact invariant & reversibility callout | Comprehensive, formal | Diagram/table open, callout folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the pipeline diagram/table directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **Explicit In/Out Formats**: Table must specify the concrete representation format entering and leaving each stage.
