---
name: codeblock
description: >-
  Replicates and annotates source code, pseudo-code, and CLI terminal commands
  strictly present in the source PDF.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
include_line_annotations: true
include_complexity_analysis: true
target_language: "match_source"
foldable_callouts: true
---

# Codeblock Skill (`/codeblock`)

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

## Reference Template

```markdown
```bash
# Inspecting X.509 Certificate contents via OpenSSL
openssl x509 -in cert.pem -noout -text
```

> [!info]- Parameter & Command Breakdown
> - `x509`: Subcommand invoking the X.509 certificate display and signing utility.
> - `-in cert.pem`: Specifies the target PEM-formatted certificate file.
> - `-noout`: Suppresses the raw base64-encoded certificate container output.
> - `-text`: Pretty-prints all certificate fields (Issuer, Subject, Validity, Public Key, Extensions, Signature).
```
