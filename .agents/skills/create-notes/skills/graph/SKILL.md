---
name: graph
description: >-
  Builds clean, Obsidian-safe Mermaid.js diagrams for workflows, architectures,
  threat trees, DFDs, and state machines.
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

### 3. Narrative Walkthrough
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

    passenger -->|"Purchases Ticket"| app
    app -->|"Encrypted REST / JSON"| api
    api <-->|"Query / Update"| db
    api -->|"Issues Signed Token"| app
    app -->|"Displays QR + Animation"| driver
    app -->|"Presents QR Barcode"| inspector
    inspector -.->|"Online Verification Query"| api
```
````

### 2. Hierarchical Threat Tree Taxonomy
````markdown
```mermaid
flowchart TD
    Root["Root Threat: Counterfeit Ticket"] --> Insider["Insider Attack"]
    Root --> External["External Attack"]

    Insider --> Petty["Petty Fraud"]
    Insider --> Systemic["Systemic Corruption"]

    Petty --> CustService["Customer Service Staff"]
    Petty --> ITStaff["IT Support Staff"]
    Systemic --> Devs["Software Engineers"]

    External --> Backend["Backend Hacking"]
    External --> ReverseEng["App Reverse Engineering"]

    Backend --> Targeted["Targeted Cybercrime"]
    Backend --> Opportunistic["Opportunistic Exploits"]
```
````
