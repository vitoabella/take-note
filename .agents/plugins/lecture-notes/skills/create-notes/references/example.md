---
# Module-specific overrides
callout_type: "example"
foldable_callouts: true
---

# Example Module Specification

Use this skill to populate concrete real-world examples, case studies, attack scenarios, and worked problems (`<!-- MODULE:example ... -->`) in the lecture note skeleton.

---

## Core Guidelines & Format Reference

### 1. Callout Convention
- Format examples inside folded callouts: `> [!example]- [Title]`.
- Voice: Strong student explaining to a peer — technically precise, banishing lazy one-sentence stubs.
- Anti-Laziness Rule: Expand named concepts to mechanisms, assumptions, operational workflows, and practical pitfalls.

### 2. Supported Example Modes
- **Mode A: Case Study / Attack Walkthrough**: Context, Step-by-Step Attack Mechanism, Vulnerability Analysis & Mitigations.
- **Mode B: Worked Practice Problem / Calculation**: Problem setup with given numbers, step-by-step Answer.
- **Mode C: Conceptual Check**: Q&A probing limiting cases and trade-offs.

---

## Depth Specification

- **`depth="1"` (Mentioned in Passing)**:
  - 1-paragraph brief relatable scenario in a callout; no multi-step breakdown.
- **`depth="2"` (Discussed, but not fleshed out)**:
  - Folded example callout (`> [!example]- [Title]`) with a concise 3-step mechanism trace.
- **`depth="3"` (Explained in-detail in source - Default)**:
  - Comprehensive 4-part case study / attack walkthrough (Context, Step-by-Step Attack Mechanism, Vulnerability Analysis, Architectural Mitigations).

---

## Expected Output Format

> [!IMPORTANT]
> Worker modules output **ONLY** the body content below. Do not generate section headings (`##`, `###`) or introductory quote callouts (`> [!quote]`).

```markdown
> [!example]- Passenger Attack Vector: Dynamic Animation Replication in Counterfeit Tickets
> **System Context**: Helsinki Regional Transport (HSL) mobile ticketing relies on visual inspection by bus drivers alongside QR code verification by roaming inspectors.
> 
> **Attack Mechanism**:
> 1. *Screen Recording / HTML Extraction*: An attacker observes that authentic tickets display dynamic cycling colors, moving visual animations, and a real-time countdown timer generated via HTML5 canvas/CSS.
> 2. *Counterfeit Web Application*: The attacker builds a lightweight standalone Progressive Web App (PWA) mimicking the exact font, color palettes, and animation sequences of the genuine HSL ticket.
> 3. *Social Engineering at Boarding*: Upon entering the bus, the passenger flashes the animated screen to the driver. Because bus drivers conduct rapid visual checks without scanning the QR barcode to maintain schedule headway, the counterfeit passes inspection.
> 
> **Vulnerability & Countermeasure**:
> - *Vulnerability*: Decoupling visual validation (unauthenticated eye check) from cryptographic validation (digital signature verification).
> - *Mitigation*: Closed boarding gates or mandatory optical barcode scanning connected to an offline cryptographic public-key verifier.
```
