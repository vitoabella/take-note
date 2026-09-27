---
target_language: "match_source"
foldable_callouts: true
---

# Codeblock Module Specification

Use this module to transcribe verbatim source code, pseudocode, configuration syntax, or CLI terminal commands that explicitly appeared in the lecture material.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:codeblock section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
```<language>
# <Purpose / Context of snippet>
<verbatim_code_or_command_lines>
```

> [!info]- Parameter & Logic Breakdown
> - `<parameter_or_keyword_1>`: <Functional responsibility and semantics.>
> - `<parameter_or_keyword_2>`: <Setup requirement, flag value, or data type.>
> - `<parameter_or_keyword_3>`: <Execution condition, loop invariant, or error handling.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | Raw snippet | Verbatim code/command with 1-line usage comment | Concise, direct | Open codeblock; omit breakdown |
| **`2`** | Snippet + breakdown | Code + folded parameter & command breakdown callout | Standard technical | Code open, callout folded (`-`) |
| **`3`** | Snippet + full analysis | Code + line-by-line annotations + execution invariants / complexity | Exhaustive, formal | Code open, callouts folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the code block/callout directly below it.
- **Strict Source Condition**: ONLY execute if code, pseudocode, or CLI commands appeared explicitly in the source material. Never synthesize speculative code.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **No Conversational Wrapper**: Do not include conversational preambles or greetings.
