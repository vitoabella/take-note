---
name: graph
description: >-
  Builds clean, Obsidian-safe Mermaid.js diagrams for workflows, architectures,
  threat trees, DFDs, and state machines with verb-object edge phrasing.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
diagram_engine: "mermaid"
orientation: "TD"
foldable_callouts: true
---

# Graph Skill (`/graph`)

Use this skill to convert architectural schematics, threat trees, data flow diagrams, and protocol workflows (`<!-- MODULE:graph ... -->`) into clean Mermaid.js diagrams.

---

## Core Guidelines & Format Reference

### 1. Triggered Visual Conditions
Generate a graph whenever the material involves:
- Multi-component system architecture and trust boundaries.
- Sequential protocol handshakes and message flows.
- Hierarchical threat decompositions and taxonomies (e.g., threat trees).
- Data Flow Diagrams (DFDs) crossing process/storage boundaries.

### 2. Obsidian-Safe Mermaid Syntax Rules
- **Node IDs**: Strictly alphanumeric and underscores only (`node_A`, `auth_server`). Never include spaces or dashes in node IDs.
- **Labels**: Always quote labels containing special characters, brackets, or parentheses: `client["Passenger App (Android / iOS)"]`.
- **No Raw HTML**: Do not use `<br>` or `<b>` inside node strings. Use standard text or clean punctuation.
- **Trust Boundaries**: Use Mermaid `subgraph` blocks to demarcate security domains, administrative jurisdictions, and trust boundaries.

### 3. Verb-Object Phrasing on Flowchart Edges

> [!IMPORTANT]
> **Verb-Object Phrasing for Edge Labels**:
> For all Mermaid flowcharts and state diagrams, edge labels describing transitions, message passing, or step movements MUST strictly use **verb-object phrases** detailing how entities/data move along the flow:
> - **Good**: `-->|"Transmits signed token"|`, `-->|"Validates public key"|`, `-->|"Issues challenge nonce"|`, `-->|"Logs inspection event"|`
> - **Bad**: `-->|"Token"|`, `-->|"Public key"|`, `-->|"Yes"|`, `-->|"Next"|`

### 4. Narrative Walkthrough
Every diagram must be followed immediately by a concise narrative explaining:
- The operational roles of the depicted entities.
- How data and control signals transition across boundaries.
- Critical single points of failure or adversarial exposure points.

---

## Reference Templates

### 1. Architectural Diagram with Trust Boundaries
````markdown
```mermaid
flowchart TD
    subgraph ClientDomain["Passenger Domain (Untrusted)"]
        app["Mobile Ticket App"]
        passenger["Passenger"]
    end

    subgraph TransportDomain["Transit Authority (Trusted Backend)"]
        api["Sales & Validation API"]
        db[("Customer & Ticket DB")]
    end

    subgraph InspectionDomain["Field Inspection (Semi-Trusted)"]
        driver["Bus Driver (Visual Check)"]
        inspector["Inspector Scanner (Online / Offline)"]
    end

    passenger -->|"Initiates ticket purchase"| app
    app -->|"Sends encrypted payment request"| api
    api <-->|"Queries customer account balance"| db
    api -->|"Issues cryptographically signed token"| app
    app -->|"Displays dynamic color animation"| driver
    app -->|"Presents optical QR barcode"| inspector
    inspector -.->|"Verifies ticket status online"| api
```
````

### 2. Hierarchical Threat Tree Taxonomy
````markdown
```mermaid
flowchart TD
    Root["Root Threat: Counterfeit Ticket"] -->|"Originates through"| Insider["Insider Attack"]
    Root -->|"Originates through"| External["External Attack"]

    Insider -->|"Manifests as"| Petty["Petty Fraud"]
    Insider -->|"Manifests as"| Systemic["Systemic Corruption"]

    Petty -->|"Executed by"| CustService["Customer Service Staff"]
    Petty -->|"Executed by"| ITStaff["IT Support Staff"]
    Systemic -->|"Executed by"| Devs["Software Engineers"]

    External -->|"Targets"| Backend["Backend Hacking"]
    External -->|"Performs"| ReverseEng["App Reverse Engineering"]

    Backend -->|"Organized by"| Targeted["Targeted Cybercrime"]
    Backend -->|"Exploited by"| Opportunistic["Opportunistic Exploits"]
```
````
