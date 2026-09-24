---
title: "Threat Analysis"
course: "CS-C3130 Information Security"
instructor: "Tuomas Aura"
institution: "Aalto University"
year: 2023
tags:
  - lecture-notes
  - information-security
  - threat-analysis
  - stride
  - dread
  - risk-assessment
source: "Threat analysis - Tuomas Aura (Aalto University 2023).pdf"
---

> Threat analysis is the systematic discipline of identifying potential malicious attacks, vulnerabilities, and security exposures across system architectures, business models, and operational trust boundaries. By decomposing systems through structural viewpoints, data flow diagrams (STRIDE), and threat trees, security engineers prioritize countermeasures against realistic adversaries rather than relying on superficial security pixie dust.

# Overview

```
Threat Analysis
 ├── Security Terminology & Foundations
 │     ├── What is Security?
 │     ├── Fundamental Terminology & Quantitative Risk
 │     ├── Security Goals: The CIA Triad & Beyond
 │     └── The Adversary & Threat Actors
 ├── Viewpoints to Threat Analysis
 │     ├── Multi-Dimensional Perspectives
 │     └── The 5-Step Productive Threat Modeling Process
 ├── Case Study: Public-Transport Ticket App Threat Model
 │     ├── Mobile Ticket System Architecture
 │     ├── Business Model & Boarding Economics
 │     ├── Asset & Actor Classification
 │     ├── Threat Vectors & Attack Scenarios
 │     └── Operational Governance & Security Reporting
 └── Systematic Threat Modeling Frameworks
       ├── Threat Trees & Taxonomies
       ├── The STRIDE Methodology & Data Flow Diagrams
       ├── Risk Assessment & The DREAD Model
       └── Assessment Pitfalls & Security 'Pixie Dust'
```

---

## Table of Contents
- [1. Security Terminology & Foundations](#1-security-terminology--foundations)
  - [1.1 What is Security?](#11-what-is-security)
  - [1.2 Fundamental Terminology & Quantitative Risk](#12-fundamental-terminology--quantitative-risk)
  - [1.3 Security Goals: The CIA Triad & Beyond](#13-security-goals-the-cia-triad--beyond)
  - [1.4 The Adversary & Threat Actors](#14-the-adversary--threat-actors)
- [2. Viewpoints to Threat Analysis](#2-viewpoints-to-threat-analysis)
  - [2.1 Multi-Dimensional Perspectives](#21-multi-dimensional-perspectives)
  - [2.2 The 5-Step Productive Threat Modeling Process](#22-the-5-step-productive-threat-modeling-process)
- [3. Case Study: Public-Transport Ticket App Threat Model](#3-case-study-public-transport-ticket-app-threat-model)
  - [3.1 Mobile Ticket System Architecture](#31-mobile-ticket-system-architecture)
  - [3.2 Business Model & Boarding Economics](#32-business-model--boarding-economics)
  - [3.3 Asset & Actor Classification](#33-asset--actor-classification)
  - [3.4 Threat Vectors & Attack Scenarios](#34-threat-vectors--attack-scenarios)
  - [3.5 Operational Governance & Security Reporting](#35-operational-governance--security-reporting)
- [4. Systematic Threat Modeling Frameworks](#4-systematic-threat-modeling-frameworks)
  - [4.1 Threat Trees & Taxonomies](#41-threat-trees--taxonomies)
  - [4.2 The STRIDE Methodology & Data Flow Diagrams](#42-the-stride-methodology--data-flow-diagrams)
  - [4.3 Risk Assessment & The DREAD Model](#43-risk-assessment--the-dread-model)
  - [4.4 Assessment Pitfalls & Security 'Pixie Dust'](#44-assessment-pitfalls--security-pixie-dust)
- [Appendix A: Mathematical & Quantitative Formulas](#appendix-a-mathematical--quantitative-formulas)
- [Appendix B: Technical Terms & Glossary](#appendix-b-technical-terms--glossary)
- [Appendix C: Comprehensive Summary](#appendix-c-comprehensive-summary)

---

## 1. Security Terminology & Foundations

### 1.1 What is Security?
Security addresses bad events caused with ==**intentional malicious intent**==, distinguishing it from general reliability and safety engineering. It represents a ==**non-functional, qualitative property**== of a system continuously challenged by ==**intelligent, adaptive adversaries**==.

<!-- MODULE:vs_comparison section="1.1" topic="Security vs Reliability: Malicious Intent vs Accidental/Random Failures" importance="3" -->

<!-- MODULE:analogy section="1.1" topic="Security as a moving target: why crime never ends in digital systems" importance="2" -->

### 1.2 Fundamental Terminology & Quantitative Risk
Rigorous security engineering establishes precise boundaries between latent vulnerabilities, active exploits, and threats, quantifying exposure through ==**probabilistic financial risk calculations**==.

<!-- MODULE:formula section="1.2" topic="Quantitative Risk Definition: Probability of Attack x Damage in Currency" importance="4" -->

<!-- MODULE:list section="1.2" topic="Core Security Terminology: Threat, Attack, Vulnerability, Exploit, and Risk" importance="3" -->

### 1.3 Security Goals: The CIA Triad & Beyond
Beyond the classical CIA triad (Confidentiality, Integrity, Availability), enterprise security architecture demands ==**granular access control**== and comprehensive ==**personal data privacy**==.

<!-- MODULE:list section="1.3" topic="Security Goals Taxonomy: CIA Triad, Access Control, and Privacy" importance="3" -->

<!-- MODULE:example section="1.3" topic="Concrete Security Goals in Web Servers and Customer Database Systems" importance="2" -->

### 1.4 The Adversary & Threat Actors
Systems operate within ==**multilateral security environments**== where trust boundaries divide honest participants from adversaries, with ==**privileged insiders**== often posing the most severe exposure.

<!-- MODULE:list section="1.4" topic="Attacker Taxonomy: From Curious Individuals to Nation-State SIGINT" importance="3" -->

<!-- MODULE:example section="1.4" topic="Multilateral Security Partitioning: Telegram messaging privacy scenario" importance="2" -->

<!-- MODULE:vs_comparison section="1.4" topic="Insider Threats vs External Hackers: Access Privileges and Trust Exploitation" importance="3" -->

---

## 2. Viewpoints to Threat Analysis

### 2.1 Multi-Dimensional Perspectives
Comprehensive analysis requires evaluating the target through ==**seven orthogonal viewpoints**==, balancing asset valuation against compliance mandates and engineering constraints.

<!-- MODULE:list section="2.1" topic="The 7 Core Viewpoints: Assets, Attackers, Engineering, Countermeasures, Checklists, Compliance, and Risk Methodology" importance="3" -->

### 2.2 The 5-Step Productive Threat Modeling Process
Effective security modeling rejects bureaucratic formalism, focusing instead on ==**iterative architectural understanding**== and ==**risk-prioritized mitigation**==.

<!-- MODULE:list section="2.2" topic="Iterative 5-Step Productive Threat Modeling Process" importance="3" -->

<!-- MODULE:graph section="2.2" topic="Iterative Threat Modeling Workflow: From Architecture Understanding to Prioritized Mitigation" importance="2" -->

---

## 3. Case Study: Public-Transport Ticket App Threat Model

### 3.1 Mobile Ticket System Architecture
The Helsinki Regional Transport (HSL) mobile ticketing infrastructure orchestrates ==**heterogeneous distributed components**==, connecting passenger mobile apps, onboard bus drivers, roaming ticket inspectors, and transit authority backend APIs across ==**untrusted wireless channels**==.

<!-- MODULE:graph section="3.1" topic="Mobile Ticket System Architecture: Passenger App, Bus Driver, Ticket Inspector, and HSL Backend APIs" importance="4" -->

<!-- MODULE:image section="3.1" topic="Visual Schematic of Mobile Ticket System Architecture and Trust Boundaries" importance="3" -->

### 3.2 Business Model & Boarding Economics
Transit ticketing security is governed by operational throughput and ==**purchaser-provider regulatory economics**==, dictating trade-offs between ==**open boarding validation**== and gated entry control.

<!-- MODULE:vs_comparison section="3.2" topic="Open Boarding vs Closed Boarding: Throughput, Inspection Costs, and Unpaid Fare Trade-Offs" importance="3" -->

<!-- MODULE:example section="3.2" topic="Public Transit Economic Model: 50% Farebox Income and 50% Municipal Subsidies under EU Regulation 1370/2007" importance="2" -->

### 3.3 Asset & Actor Classification
A rigorous inventory categorizes both tangible financial assets and intangible data records, mapping them against diverse stakeholders with ==**conflicting operational incentives**==.

<!-- MODULE:list section="3.3" topic="Transit System Asset Taxonomy: Money, Transport Capacity, Personal Data, and Cryptographic Secrets" importance="3" -->

<!-- MODULE:list section="3.3" topic="Stakeholder Actor Mapping: Passengers, Transit Authority (HSL), Operators, MaaS Providers, and Insiders" importance="3" -->

### 3.4 Threat Vectors & Attack Scenarios
Threat vectors encompass passenger-driven fare evasion, malicious app cloning, and ==**systematic exploitation of human-centered recovery processes**==, as well as insider fraud.

<!-- MODULE:example section="3.4" topic="Passenger Fare Evasion: Riding without tickets on open transit lines (Metro and Bus 550)" importance="2" -->

<!-- MODULE:example section="3.4" topic="Counterfeit Ticket Vectors: Edited screenshots and fake ticket apps replicating dynamic color animations" importance="4" -->

<!-- MODULE:example section="3.4" topic="Ticket Sharing Scenarios: Cryptographic cloning, passback to companions, and timesharing monthly passes" importance="3" -->

<!-- MODULE:example section="3.4" topic="Abuse of Fallback & Recovery Processes: Dead battery excuses and borrowing tickets to cancel penalty fees" importance="3" -->

<!-- MODULE:example section="3.4" topic="Discount Tariff Fraud: Evading student and resident eligibility verification" importance="2" -->

<!-- MODULE:list section="3.4" topic="Insider and Provider Threat Vectors: Driver collusion, unissued ticket billing, and backend ransomware" importance="3" -->

### 3.5 Operational Governance & Security Reporting
Beyond technical defenses, security assessments must audit ==**incentive misalignment**==, such as inspector penalty quotas, while producing balanced, ==**action-oriented audit reports**== for decision-makers.

<!-- MODULE:example section="3.5" topic="Misuse of Authority: Inspector penalty fee bonus quotas and anticompetitive MaaS API throttling" importance="3" -->

<!-- MODULE:example section="3.5" topic="Bulk Travel Data Exploitation: Operator competitive advantage in public transit tender bidding" importance="3" -->

<!-- MODULE:list section="3.5" topic="Professional Threat Analysis Next Steps: Reverse engineering, designer interviews, and balanced reporting" importance="2" -->

---

## 4. Systematic Threat Modeling Frameworks

### 4.1 Threat Trees & Taxonomies
Threat trees decompose primary threats into granular attack paths, functioning primarily as a ==**structured post-analysis taxonomy**== rather than an exploratory discovery tool.

<!-- MODULE:graph section="4.1" topic="Hierarchical Threat Tree Taxonomy for Counterfeit Mobile Tickets (Fake Ticket Root to Leaf Attacks)" importance="4" -->

<!-- MODULE:vs_comparison section="4.1" topic="Threat Trees as Analysis Discovery Tools vs Systematic Post-Analysis Presentation Taxonomies" importance="2" -->

### 4.2 The STRIDE Methodology & Data Flow Diagrams
Microsoft's STRIDE framework couples component-level threat classification with ==**formal Data Flow Diagrams (DFDs)**==, isolating vulnerabilities across ==**explicit trust boundaries**==.

<!-- MODULE:graph section="4.2" topic="High-Level Data Flow Diagram (DFD) for the Transport Ticket App with Trust Boundaries" importance="4" -->

<!-- MODULE:multi_comparison section="4.2" topic="STRIDE Threat Categories vs Security Properties and DFD Component Applicability Matrix" importance="4" -->

### 4.3 Risk Assessment & The DREAD Model
Security prioritization requires balancing qualitative intuition against quantitative metrics, highlighting the limitations of ==**arbitrary numerical scoring**== in frameworks like DREAD.

<!-- MODULE:multi_comparison section="4.3" topic="Risk Assessment Methodologies: Qualitative Matrices, Damage-Probability Formulas, and DREAD Dimensions" importance="3" -->

<!-- MODULE:list section="4.3" topic="The 5 DREAD Dimensions: Damage, Reproducibility, Exploitability, Affected Users, and Discoverability" importance="2" -->

### 4.4 Assessment Pitfalls & Security 'Pixie Dust'
A critical design anti-pattern is treating cryptographic primitives as ==**security pixie dust**==, deploying mechanisms without a valid underlying threat model or operational context.

<!-- MODULE:analogy section="4.4" topic="Security Pixie Dust: The Fallacy of Sprinkling Encryption onto Flawed System Architectures" importance="4" -->

<!-- MODULE:image section="4.4" topic="Security Pixie Dust Illustrated: Photograph of Bicycle Chained to a Short Removable Bollard" importance="3" -->

---

## Appendix A: Mathematical & Quantitative Formulas
<!-- MODULE:table_formulas importance="3" -->

## Appendix B: Technical Terms & Glossary
<!-- MODULE:table_definitions importance="4" -->

## Appendix C: Comprehensive Summary
<!-- MODULE:summary importance="4" -->
