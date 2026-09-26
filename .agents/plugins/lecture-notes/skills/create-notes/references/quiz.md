---
# Module-specific overrides
callout_type: "question"
foldable_callouts: true
---

# Quiz Module Specification

Use this skill to construct concise self-assessment quiz callouts (`<!-- MODULE:quiz ... -->`) to reinforce core mechanisms, limiting cases, and trade-offs.

---

## Core Guidelines & Format Reference

### 1. Callout Convention
- Format the quiz inside a folded question callout:
  ```markdown
  > [!question]- Self-Assessment Quiz: [Topic]
  ```

### 2. Question & Answer Structure
- Numbered list of questions probing understanding, followed by an indented concise answer:
  ```markdown
  > 1. **[Question prompt]**
  >    - *Answer*: [Concise explanation explaining mechanism, invariant, or trade-off].
  ```
- Keep questions focused on mechanisms and trade-offs rather than trivial trivia.

---

## Depth Specification

- **`depth="1"` (Mentioned in Passing)**:
  - 2 simple recall questions probing core definitions and terminology.
- **`depth="2"` (Discussed, but not fleshed out)**:
  - 3 conceptual questions probing operational mechanisms and key trade-offs.
- **`depth="3"` (Explained in-detail in source - Default)**:
  - 4–5 rigorous scenario-based questions probing edge cases, failure modes, and architectural decisions.

---

## Expected Output Format

> [!IMPORTANT]
> Worker modules output **ONLY** the body content below. Do not generate section headings (`##`, `###`) or introductory quote callouts (`> [!quote]`).

```markdown
> [!question]- Self-Assessment Quiz: Storage Encryption & Key Recovery
> 1. **Why does administrative password reset cause permanent EFS data loss in non-domain environments?**
>    - *Answer*: Windows DPAPI encrypts the user's master key with a hash of the user's login password. An administrative reset changes the account password without decrypting and re-encrypting the DPAPI master key, permanently severing access to the user's private EFS key unless a recovery certificate is configured.
> 2. **What platform changes trigger BitLocker recovery console lockout during boot?**
>    - *Answer*: Any modification altering PCR measurements—such as installing a new bootloader, replacing the motherboard/TPM, moving the drive to a different PC, or clearing the TPM—causes the TPM to refuse to unseal the Volume Master Key.
> 3. **How does BitLocker solve the recovery problem without exposing volume encryption keys in plaintext?**
>    - *Answer*: It derives a 128-bit key from a 48-digit recovery password, encrypts the Volume Master Key with it, and stores this encrypted copy in the volume metadata while escrowing the password to Active Directory or Azure AD.
```
