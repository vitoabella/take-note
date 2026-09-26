---
name: analogy
description: >-
  Explains complex technical concepts with intuitive mental models, real-world analogies,
  and conceptual unpackings using folded [!tip]- callouts.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
callout_type: "tip"
foldable_callouts: true
---

# Analogy Skill (`/analogy`)

Use this skill to populate conceptual analogy modules (`<!-- MODULE:analogy ... -->`) in the lecture note skeleton.

---

## Core Guidelines & Format Reference

### 1. Callout Convention
- Always use the folded tip callout form: `> [!tip]- Analogy: [Concept Name]` or `> [!tip]- Mnemonic: [Concept Name]`.
- Voice: Strong student explaining to a peer — digestible, intuitive, yet technically grounded.

### 2. Tripartite Structure of an Analogy
Every analogy must be unpacked across three clear dimensions:
1. **The Intuitive Real-World Metaphor**: Ground the abstract mechanism in a familiar physical or operational scenario (e.g., notary public, physical passport, bicycle lock, post office).
2. **Structural Mapping (Isomorphism)**: Explicitly map each element of the real-world metaphor to its technical counterpart (e.g., *seal on envelope* $\rightarrow$ *cryptographic signature*, *notary public* $\rightarrow$ *Certificate Authority*).
3. **Boundary & Breakdown Analysis**: Explicitly call out where the metaphor breaks down and ceases to hold. This prevents false mental models and highlights edge cases.

---

## Reference Template

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
