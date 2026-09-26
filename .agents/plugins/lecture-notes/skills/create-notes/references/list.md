---
# Module-specific overrides
list_style: "hybrid"
foldable_callouts: true
---

# List & Taxonomy Module Specification

Use this skill to convert slide bullet points, categorizations, operational procedures, taxonomies, and unexpounded enumerations (`<!-- MODULE:list ... -->`) into scannable, structured Markdown lists and callout expansions.

---

## Core Guidelines & Format Reference

### 1. Formatting Conventions
- **Bold Lead-in Labels**: Every bullet must lead with a bold term or action verb (`- **Term**: Explanation...`).
- **Nesting Limit**: Nest at most 2–3 levels to preserve readability.
- **Voice**: Strong student explaining to a peer — digestible, technically precise.

### 2. Callout Expansion Rule for Unexpounded Enumerations
When the source material enumerates items without expounding (e.g., scenarios, asset categories, or threat lists with no elaboration in the slide), provide the expanded definitions, mechanisms, and operational details inside semantic callouts:
- **Scenario / Case Example Enumerations**:
  ```markdown
  > [!example] Lost and Stolen Notebook Computers
  > Portable client machines operating outside secure facilities; physical drive access allows bypassing operating system access controls.
  ```
- **Technical Concept / Dimension Enumerations**:
  ```markdown
  > [!info] Data at Rest Encryption
  > File and disk-level cryptographic protection preventing offline disclosure from decommissioned or stolen media.
  ```

---

## Depth Specification

- **`depth="1"` (Mentioned in Passing)**:
  - Simple flat bullet list using simple, relatable, easy-to-remember terms.
  - Do not over-elaborate; omit nested sub-bullets and deep callouts.
- **`depth="2"` (Discussed, but not fleshed out)**:
  - Concise bulleted taxonomy using short phrases.
  - If expanding unexpounded enumerations, use folded callouts by default (`> [!example]- <Item>`, `> [!info]- <Item>`).
- **`depth="3"` (Explained in-detail in source - Default)**:
  - Comprehensive hierarchical taxonomy with detailed sub-bullets dissecting invariants and failure modes.
  - If expanding unexpounded enumerations, provide full, in-depth callout expansions detailing context, attack vectors, and mitigations.

---

## Expected Output Format

> [!IMPORTANT]
> Worker modules output **ONLY** the body content below. Do not generate section headings (`##`, `###`) or introductory quote callouts (`> [!quote]`).

### Format A: Structured Taxonomy / Procedure
```markdown
- **Confidentiality**: Protection of sensitive secrets against unauthorized reading or disclosure.
  - *Data at Rest*: Encrypted storage, file-level ACLs, and cryptographic databases.
  - *Data in Transit*: TLS sessions, forward secrecy, and authenticated encryption.
- **Integrity**: Assurance that data and system state are modified only through authorized, audited transactions.
- **Availability**: Guarantee that services remain operational and accessible under legitimate user demand.
- **Access Control**: Enforcement mechanisms verifying authorization before granting resource operations.
- **Privacy**: Policy and technical boundaries allowing individuals to control personal data dissemination.
```

### Format B: Callout Expansion for Unexpounded Enumerations
```markdown
> [!example] Lost and Stolen Notebook Computers
> Portable machines operating in untrusted physical environments. Physical possession allows attackers to mount the storage drive onto an external machine, bypassing OS user authentication and NTFS file permissions.

> [!example] Stolen Workstations and Servers
> Fixed enterprise infrastructure removed during physical facility intrusions. Servers host aggregated organizational databases, configuration files, and authentication tokens, creating high-consequence data breach vectors.

> [!example] Decommissioning Hard Drives
> Storage media retired at end-of-life or transferred between departments. Without cryptographic sanitization or full disk encryption, residual magnetic or flash state allows reconstruction of confidential files.
```
