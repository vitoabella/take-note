---
name: example
description: >-
  Provides concrete real-world scenarios, case studies, attack walkthroughs,
  and worked exercises using folded [!example]- callouts.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
callout_type: "example"
foldable_callouts: true
---

# Example Skill (`/example`)

Use this skill to populate concrete real-world examples, case studies, attack scenarios, and worked problems (`<!-- MODULE:example ... -->`) in the lecture note skeleton.

---

## Core Guidelines & Format Reference

### 1. Callout Convention
- Always format examples inside folded callouts: `> [!example]- [Title]`.
- Voice: Strong student explaining to a peer — technically precise, banishing lazy one-sentence stubs.
- Anti-Laziness Rule: Expand named concepts to mechanisms, assumptions, operational workflows, and practical pitfalls.

### 2. Supported Example Modes

#### Mode A: Case Study / Attack Walkthrough
Used for real-world systems, protocols, or concrete attack implementations:
- **Operational Scenario / Context**: Background of the target system.
- **Mechanism / Execution Steps**: Step-by-step trace of how the attack or workflow occurs.
- **Impact & Mitigations**: Real-world consequence and architectural defense.

#### Mode B: Worked Practice Problem / Calculation
Used for quantitative problems or algorithmic executions:
- **Problem:** Clear setup with given numbers and variables.
- **Answer:** Step-by-step algebraic or conceptual solution.

#### Mode C: Conceptual Check
Used for probing trade-offs and boundary conditions:
- **Q:** Precise probing question on limiting cases or trade-offs.
- **A:** Detailed explanation of the underlying mechanism.

---

## Reference Templates

### Case Study / Attack Walkthrough
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

### Conceptual Check
```markdown
> [!example]- Conceptual Check: Ticket Recovery Exploitation
> **Q:** How can a commuter exploit failure-recovery penalty fee cancellation policies without paying for a monthly pass?
> **A:** If a commuter is caught without a ticket and claims their phone battery died, transit policy may allow retroactive cancellation of the penalty fee upon presenting a valid personal monthly subscription within 3 days. A non-paying commuter borrows a friend's monthly pass post-incident to cancel the citation. The countermeasure is binding the subscription strictly to verified national identity tokens or disallowing third-party post-validation.
```
