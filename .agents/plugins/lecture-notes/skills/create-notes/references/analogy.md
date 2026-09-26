---
# Module-specific overrides
callout_type: "tip"
foldable_callouts: true
---

# Analogy Module Specification

Use this skill to populate conceptual analogy modules (`<!-- MODULE:analogy ... -->`) in the lecture note skeleton.

---

## Core Guidelines & Format Reference

### 1. Callout Convention
- Always use the folded tip callout form: `> [!tip]- Analogy: [Concept Name]` or `> [!tip]- Mnemonic: [Concept Name]`.
- Voice: Strong student explaining to a peer — digestible, intuitive, yet technically grounded.

### 2. Tripartite Structure of an Analogy
1. **The Intuitive Real-World Metaphor**: Ground the abstract mechanism in a familiar physical or operational scenario.
2. **Structural Mapping (Isomorphism)**: Explicitly map each element of the real-world metaphor to its technical counterpart.
3. **Boundary & Breakdown Analysis**: Explicitly call out where the metaphor breaks down and ceases to hold.

---

## Depth Specification

- **`depth="1"` (Mentioned in Passing)**:
  - 1–2 sentence intuitive real-world metaphor in a folded tip callout; omit structural mapping and breakdown.
- **`depth="2"` (Discussed, but not fleshed out)**:
  - Folded tip callout (`> [!tip]- Analogy: [Concept]`) with metaphor and concise bulleted structural mapping.
- **`depth="3"` (Explained in-detail in source - Default)**:
  - Full tripartite structure: Intuitive Real-World Metaphor, Granular Structural Mapping / Isomorphism, and Explicit Boundary & Breakdown Analysis.

---

## Expected Output Format

> [!IMPORTANT]
> Worker modules output **ONLY** the body content below. Do not generate section headings (`##`, `###`) or introductory quote callouts (`> [!quote]`).

```markdown
> [!tip]- Analogy: Public Key Infrastructure as a Notary & Passport Office
> Think of asymmetric key distribution like issuing and verifying passports:
> 
> - **The Metaphor**: Alice cannot simply walk up to Bob and claim to be Bob's trusted banker based solely on a self-printed business card. Instead, a recognized sovereign government (the **Certificate Authority**) verifies Alice's physical identity and stamps an official passport containing her name and photo with an unforgeable holographic seal (**digital signature**). When Bob inspects the passport, he does not need to know Alice personally; he only needs to recognize and trust the government's official seal (**pre-installed Root CA public key**).
> - **Structural Mapping**:
>   - *Citizen Identity*: Subject Distinguished Name (e.g., `CN=alice.bank.com`).
>   - *Holographic Seal*: Asymmetric cryptographic signature computed with CA's private key.
>   - *Passport Document*: X.509 Digital Identity Certificate.
>   - *Border Control Scanner*: Verifying software checking the signature chain against the trusted root store.
> - **Where the Analogy Breaks Down**: Unlike physical passports, digital certificates can be replicated with bit-for-bit perfection. Possessing the certificate alone does not authenticate an identity—the presenter must also provide cryptographic proof of private key possession (e.g., via a challenge-response handshake).
```
