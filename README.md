# Logic Gate Caesar Cipher (LGCC)

A custom byte-oriented symmetric cryptographic algorithm designed and evaluated as an academic exploration of classical substitution, bitwise logic, ciphertext feedback, and byte-level transformations.

> ## Disclaimer
>
> LGCC is an experimental, educational cryptographic design developed for academic purposes. It has **not** been formally validated for production security and should not be used to protect sensitive or real-world data. The project is intended to demonstrate cryptographic design principles, implementation, testing, and critical security evaluation.

---

# This README only contains the surface of the documentation. To read the full documentation, please refer to [Documentation.pdf](./Documentation.pdf).

## Overview

The **Logic Gate Caesar Cipher (LGCC)** is a custom symmetric encryption algorithm developed to explore how traditional Caesar-style substitution can be extended using modern byte-level operations.

The algorithm operates on data at the byte level and combines multiple transformation stages to produce ciphertext that differs from the original plaintext.

The design incorporates:

* Modular shifting inspired by the Caesar cipher
* XOR-based bitwise mixing
* AND-based logic operations
* Ciphertext feedback
* 8-bit rotation
* Byte-oriented processing
* Reversible encryption and decryption operations

The project was developed not only to implement a working encryption and decryption process, but also to critically evaluate the strengths and limitations of designing a custom cryptographic algorithm.

---

## Objectives

The primary objectives of the project were to:

* Investigate the principles behind classical substitution ciphers.
* Explore how logic-gate operations can be incorporated into cryptographic transformations.
* Design a reversible symmetric encryption and decryption process.
* Implement the algorithm using byte-oriented operations.
* Test the algorithm using multiple plaintext and ciphertext cases.
* Evaluate the algorithm's behaviour and limitations.
* Examine whether a custom cryptographic construction could provide meaningful improvements over a basic Caesar cipher.

---

## Core Design

LGCC extends the concept of a Caesar cipher by introducing additional transformations rather than relying solely on character shifting.

### 1. Modular Shifting

A modular shift is applied to the input data to transform the byte values.

This preserves the reversible nature of the transformation while providing the basic substitution mechanism derived from the classical Caesar cipher.

### 2. XOR Mixing

XOR operations are used to introduce additional bit-level transformation.

Because XOR is reversible when the same value is applied again, it can be incorporated into both encryption and decryption processes.

### 3. AND-Based Logic

Bitwise AND operations are incorporated into the transformation process to experiment with logic-gate-based manipulation of individual bits.

### 4. Ciphertext Feedback

The algorithm incorporates previously generated ciphertext information into subsequent transformations.

This introduces a dependency between processed values rather than treating every byte completely independently.

### 5. 8-Bit Rotation

Bit rotation is applied to individual bytes to further transform their binary representation.

The rotation operation is reversible when the corresponding inverse rotation is performed during decryption.

---

## Data Processing

LGCC processes input at the byte level rather than treating plaintext purely as a sequence of alphabetic characters.

The implementation considers:

* ASCII data
* UTF-8 encoded data
* Hexadecimal byte representations
* 8-bit binary operations
* Reversible byte transformations

This allows the algorithm to operate beyond the limitations of a traditional alphabet-only Caesar cipher.

---

# Encryption Methodology

The encryption process can be summarized as a sequence of reversible transformations:

```text
Plaintext
    │
    ▼
UTF-8 / Byte Conversion
    │
    ▼
Modular Shift
    │
    ▼
XOR / Logic-Gate Mixing
    │
    ▼
Ciphertext Feedback
    │
    ▼
8-Bit Rotation
    │
    ▼
Ciphertext
```

Each stage contributes an additional transformation to the original plaintext before producing the final ciphertext.

The complete algorithm, mathematical operations, pseudocode, and worked examples are documented in the full project report.

---

# Decryption Methodology

The decryption process performs the corresponding inverse operations in reverse order.

```text
Ciphertext
    │
    ▼
Inverse 8-Bit Rotation
    │
    ▼
Reverse Feedback Processing
    │
    ▼
Reverse XOR / Logic Operations
    │
    ▼
Reverse Modular Shift
    │
    ▼
Byte / UTF-8 Conversion
    │
    ▼
Original Plaintext
```

Successful decryption should reproduce the original plaintext exactly.

---

# Testing & Validation

The implementation was tested using multiple test cases to verify that:

* Plaintext can be successfully encrypted.
* Encrypted ciphertext can be decrypted.
* Decryption produces the original plaintext.
* Byte-level transformations behave consistently.
* Different input values produce different ciphertext.
* The algorithm remains reversible across the tested cases.

The report contains the detailed test cases, intermediate transformations, and worked examples.

---

# Critical Security Evaluation

A major part of the project was evaluating LGCC rather than simply demonstrating that it works.

The analysis identified several limitations associated with custom cryptographic constructions.

### Key Management

The security of a symmetric encryption system depends heavily on how encryption keys are generated, protected, exchanged, and reused.

LGCC does not provide a complete real-world key-management system.

### Authentication

LGCC focuses on confidentiality through encryption and does not provide a dedicated authenticated encryption mechanism.

As a result, encryption alone should not be interpreted as protection against modification or tampering.

### Cryptanalysis

The project was not subjected to the level of formal cryptanalysis required to establish security against modern cryptographic attacks.

Working encryption and successful decryption do not, by themselves, demonstrate cryptographic security.

### Custom Cryptographic Design

Designing cryptographic algorithms requires significantly more than combining reversible mathematical and logical operations.

A construction may function correctly while still containing structural weaknesses that could be exploited through cryptanalysis.

For this reason, LGCC should be considered an **educational cryptographic experiment rather than a replacement for established cryptographic standards**.

---

# What I Learned

This project provided practical experience with:

* Symmetric cryptography
* Classical cipher mechanisms
* Byte-level data processing
* XOR and bitwise operations
* Modular arithmetic
* Bit rotation
* Ciphertext feedback
* Encryption and decryption design
* Algorithm testing
* Pseudocode development
* Cryptographic limitations and threat considerations
* Critical evaluation of custom security mechanisms

One of the main conclusions from the project was that **creating an encryption algorithm that works is considerably easier than demonstrating that the algorithm is secure**.

---

# Technologies & Concepts

| Category               | Technologies / Concepts            |
| ---------------------- | ---------------------------------- |
| Programming            | Python                             |
| Cryptography           | Symmetric Encryption               |
| Classical Cryptography | Caesar Cipher                      |
| Bitwise Operations     | XOR, AND, Bit Rotation             |
| Data Processing        | ASCII, UTF-8, Hexadecimal          |
| Mathematics            | Modular Arithmetic                 |
| Design                 | Custom Cryptographic Algorithm     |
| Testing                | Encryption / Decryption Test Cases |

---

# Project Structure

```text
LGCC/
├── README.md
├── Documentation.pdf
├── src/
│   └── LGCC.py
├── pseudocode/
│   └── Flowchart of Decryption process.png
│   └── Flowchart of Encryption process.png
│   └── LGCC Encryption and Decryption pseudocode.pdf

```
---


# Academic Context

**Module:** CC5009NI – Cyber Security in Computing
**Project:** Logic Gate Caesar Cipher (LGCC)
**Institution:** Islington College
**Programme:** BSc (Hons) Computer Networking & IT Security

This project was completed as part of academic coursework exploring cybersecurity and cryptographic concepts.

---

# Documentation

For the complete technical documentation, including:

* Cryptographic background
* Design rationale
* Algorithm specification
* Pseudocode
* Worked examples
* Encryption and decryption process
* Test cases
* Critical evaluation
* Limitations
* Potential applications
* References

please refer to:

[Documentation.pdf](./Documentation.pdf)

---

# Conclusion

LGCC demonstrates how a simple classical cipher can be extended into a more complex byte-oriented transformation by combining modular arithmetic, bitwise logic, ciphertext feedback, and byte rotation.

The project successfully demonstrated reversible encryption and decryption across the tested cases while also highlighting an important principle of cybersecurity: **functional correctness does not establish cryptographic security**.

LGCC is therefore best understood as an academic exploration of cryptographic algorithm design, implementation, testing, and security evaluation rather than a production-ready encryption standard.
