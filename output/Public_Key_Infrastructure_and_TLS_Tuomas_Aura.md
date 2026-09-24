---
title: "Public Key Infrastructure & TLS"
course: "CS-C3130 Information Security"
instructor: "Tuomas Aura"
institution: "Aalto University"
year: 2023
tags:
  - lecture-notes
  - information-security
  - cryptography
  - pki
  - x509
  - tls
source: "Public Key Infrastructure & TLS - Tuomas Aura (Aalto University 2023).pdf"
---

> Public Key Infrastructure (PKI) resolves the fundamental cryptographic key distribution challenge by binding public keys to verified identities via digitally signed X.509 certificates. Transport Layer Security (TLS) builds upon this trust foundation to provide end-to-end encryption, authentication, and integrity for internet communications through structured handshakes and modern cryptographic primitives.

# Overview

```
Public Key Infrastructure & TLS
 ├── Cryptographic Foundations & X.509 Certificates
 │     ├── Key Distribution Problem
 │     │     ├── Public Key Binding
 │     │     └── Certificate Anatomy
 │     ├── Certification Authorities & Trust
 │     │     ├── Authority vs Trusted Third Party
 │     │     └── Certificate Verification Mechanics
 │     └── Common Public Key Misconceptions
 │           ├── Signing vs Encryption
 │           └── Proof of Identity
 ├── Public Key Infrastructures & Hierarchies
 │     ├── Trust Hierarchies & Chains
 │     │     ├── Root Certification Authorities
 │     │     ├── Subordinate CAs & Delegation
 │     │     └── Self-Signed Certificates
 │     └── PKI Deployment Scenarios
 │           ├── Single Global CA Myth
 │           ├── Application-Specific Ecosystems
 │           └── Private Enterprise PKI*
 ├── Certificate Revocation & Validation
 │     ├── Revocation Mechanisms
 │     │     ├── Certificate Revocation Lists
 │     │     └── Online Certificate Status Protocol
 │     ├── Web PKI Revocation Challenges
 │     │     ├── Soft-Fail Vulnerabilities
 │     │     └── Undetected CA Compromise
 │     └── Certificate Transparency
 │           ├── Append-Only Public Logs
 │           ├── Signed Certificate Timestamps
 │           └── Domain Identity Proofing*
 └── Transport Layer Security
       ├── Protocol Architecture & Placement
       │     ├── Network Protocol Stack Integration
       │     └── Handshake vs Record Layer
       ├── Authenticated Key Exchange
       │     ├── Ephemeral Diffie-Hellman Exchange
       │     ├── Server Authentication & Signature
       │     └── Session Key Derivation
       └── Evolution & Practical Guarantees
             ├── TLS 1.2 vs TLS 1.3
             ├── Fast Session Resumption*
             └── Trust Chain Resolution & Naming
```

---

## 1. Cryptographic Foundations & X.509 Certificates

### 1.1 Key Distribution Problem
Asymmetric cryptography requires communicating parties to reliably determine an entity's ==**authentic public key**== without vulnerability to ==**active man-in-the-middle impersonation**==. Identity certificates solve this by creating an immutable cryptographic binding between a subject's identity and their public key.

<!-- MODULE:analogy section="1.1" topic="Notary public and signed digital passport analogy for public key binding" importance="2" -->

<!-- MODULE:formula section="1.1" topic="Formal Identity Certificate Signature Definition" importance="4" -->

<!-- MODULE:graph section="1.1" topic="Key Distribution Problem and Certificate Issuance Workflow" importance="3" -->

<!-- MODULE:codeblock section="1.1" topic="OpenSSL Certificate Inspection Command and Parsed Output" importance="2" -->

<!-- MODULE:list section="1.1" topic="Core X.509 Certificate Fields and Standard V3 Extensions" importance="3" -->

### 1.2 Certification Authorities & Trust
The certificate issuer is commonly known as a Certification Authority (CA). Systems must define whether the CA functions as an ==**administrative authority**== commanding obedience or as a ==**trusted third party (TTP)**== relying on ==**universal subjective trust**==.

<!-- MODULE:vs_comparison section="1.2" topic="Administrative Authority vs Trusted Third Party (TTP)" importance="3" -->

### 1.3 Common Public Key Misconceptions
Certificates are public tokens rather than encrypted secrets, and a certificate alone does not authenticate an identity without ==**cryptographic proof**== of private key possession.

<!-- MODULE:list section="1.3" topic="Pervasive Public Key and Certificate Misconceptions" importance="3" -->

---

## 2. Public Key Infrastructures & Hierarchies

### 2.1 Trust Hierarchies & Chains
==**Scalable trust delegation**== relies on hierarchical trees of CAs originating from ==**trusted root authorities**== down through intermediate sub-CAs to end-entity leaf certificates.

<!-- MODULE:graph section="2.1" topic="X.509 CA Delegation Hierarchy and Certificate Chain Path" importance="4" -->

<!-- MODULE:list section="2.1" topic="Certificate Path Construction and Self-Signed Root Properties" importance="3" -->

### 2.2 PKI Deployment Scenarios
While early standards envisioned a single unified ==**global CA hierarchy**== (X.500), modern computing relies on fragmented ==**application-specific ecosystems**== and ==**private organizational PKIs**== with high operational overhead.

<!-- MODULE:multi_comparison section="2.2" topic="Comparison of PKI Ecosystems: Web PKI, S/MIME, Smart-Cards, and Enterprise PKI" importance="3" -->

<!-- MODULE:list section="2.2" topic="Operational Costs and Real-World Friction of Self-Hosted Private PKI" importance="2" -->

---

## 3. Certificate Revocation & Validation

### 3.1 Revocation Mechanisms
Certificates must be cancelled when ==**issuing conditions invalidate**==, private keys suffer ==**cryptographic compromise**==, or algorithms face ==**asymptotic obsolescence**==. Unlike offline verification, revocation mandates ==**low-latency online status checks**==.

<!-- MODULE:vs_comparison section="3.1" topic="Certificate Revocation Lists (CRL) vs Online Certificate Status Protocol (OCSP)" importance="4" -->

<!-- MODULE:formula section="3.1" topic="OCSP Request and Signed Response Message Protocol" importance="3" -->

<!-- MODULE:list section="3.1" topic="Conditions Necessitating Certificate Revocation and Verification Failure Modes" importance="2" -->

### 3.2 Web PKI Revocation Challenges
In web browsers, practical network constraints have led to ==**soft-fail revocation defaults**==, where unreachable revocation responders result in bypassed checks, creating severe window-of-vulnerability risks during ==**undetected CA compromises**==.

<!-- MODULE:list section="3.2" topic="Soft-Fail Browser Defaults and Undetected Sub-CA Compromises" importance="3" -->

### 3.3 Certificate Transparency
Certificate Transparency (CT) mitigates ==**rogue CA issuance**== by mandating ==**public append-only cryptographic logs**==, monitored by domain owners and verified by browsers via ==**Signed Certificate Timestamps (SCT)**==.

<!-- MODULE:graph section="3.3" topic="Certificate Transparency Log Workflow and SCT Validation" importance="4" -->

<!-- MODULE:codeblock section="3.3" topic="Automated Domain Control Validation with ACME and DNS TXT Challenge" importance="2" -->

<!-- MODULE:list section="3.3" topic="CT Log Verification Mechanics and Automated Identity Proofing via ACME" importance="3" -->

---

## 4. Transport Layer Security

### 4.1 Protocol Architecture & Placement
Transport Layer Security (TLS) operates as a ==**secure socket abstraction**== between the application layer and TCP, establishing an ==**authenticated, confidential channel**== for web protocols.

<!-- MODULE:graph section="4.1" topic="TLS Protocol Stack Placement and Secure Socket API" importance="3" -->

<!-- MODULE:image section="4.1" topic="Web Browser Certificate Viewer and Trust Chain Resolution" importance="2" -->

### 4.2 Authenticated Key Exchange
Network security protocols split into an asymmetric handshake phase to negotiate parameters and establish ==**ephemeral shared secrets**==, followed by a ==**symmetric session protocol**== protecting application data with ==**authenticated encryption (AEAD)**==.

<!-- MODULE:graph section="4.2" topic="TLS 1.2 DHE_DSS Handshake Message Exchange Sequence" importance="4" -->

<!-- MODULE:formula section="4.2" topic="Diffie-Hellman Shared Secret and Master Secret Derivation Formulas" importance="4" -->

<!-- MODULE:list section="4.2" topic="The Six Stages of the Classical TLS Handshake" importance="3" -->

### 4.3 Evolution & Practical Guarantees
TLS 1.3 redesigns the handshake for ==**minimal round-trip latency**== and enhanced security by removing ==**obsolete cryptographic primitives**==, enforcing ==**mandatory forward secrecy**==, and introducing ==**0-RTT session resumption**==.

<!-- MODULE:vs_comparison section="4.3" topic="TLS 1.2 vs TLS 1.3: Round-Trip Latency, Cryptographic Suites, and Privacy" importance="4" -->

<!-- MODULE:list section="4.3" topic="Core Axiom: Cryptography Turns Security into Key Distribution, and PKI Turns Key Distribution into Naming" importance="4" -->

---

## Appendix A: Mathematical & Cryptographic Formulas
<!-- MODULE:table_formulas importance="3" -->

## Appendix B: Technical Terms & Glossary
<!-- MODULE:table_definitions importance="4" -->

## Appendix C: Comprehensive Summary
<!-- MODULE:summary importance="4" -->
