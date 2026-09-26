---
# Module-specific overrides
include_line_annotations: true
include_complexity_analysis: true
target_language: "match_source"
foldable_callouts: true
---

# Codeblock Module Specification

Use this skill to populate code modules (`<!-- MODULE:codeblock ... -->`) marked in the skeleton.

---

## Core Guidelines & Format Reference

> [!IMPORTANT]
> **Strict Source Condition**:
> The `codeblock` skill is **ONLY** executed if source code, pseudocode, or CLI terminal commands were explicitly present in the source PDF slides.
> Never invent arbitrary code snippets if none appeared in the lecture material.

### 1. Structure
1. **Verbatim Replication**: Transcribe the code or terminal commands faithfully with proper syntax highlighting.
2. **Context & Execution Invariants**: Briefly explain what the code snippet performs and the conditions under which it executes.
3. **Line-by-Line Breakdown**: If `include_line_annotations: true`, annotate critical lines, setup steps, loops, and termination invariants.
4. **Complexity Analysis Callout**: If algorithmic, include a folded info callout: `> [!info]- Algorithmic Complexity`.

---

## Depth Specification

- **`depth="1"` (Mentioned in Passing)**:
  - Replicated code snippet with a 1-line usage comment. Omit breakdown callouts.
- **`depth="2"` (Discussed, but not fleshed out)**:
  - Code snippet with folded parameter and command breakdown callout (`> [!info]- Parameter & Command Breakdown`).
- **`depth="3"` (Explained in-detail in source - Default)**:
  - Full verbatim code replication with line-by-line annotations, execution invariants, and algorithmic complexity callout (`> [!info]- Algorithmic Complexity`).

---

## Expected Output Format

> [!IMPORTANT]
> Worker modules output **ONLY** the body content below. Do not generate section headings (`##`, `###`) or introductory quote callouts (`> [!quote]`).

```bash
# Inspecting X.509 Certificate contents via OpenSSL
openssl x509 -in cert.pem -noout -text
```

> [!info]- Parameter & Command Breakdown
> - `x509`: Subcommand invoking the X.509 certificate display and signing utility.
> - `-in cert.pem`: Specifies the target PEM-formatted certificate file.
> - `-noout`: Suppresses the raw base64-encoded certificate container output.
> - `-text`: Pretty-prints all certificate fields (Issuer, Subject, Validity, Public Key, Extensions, Signature).
