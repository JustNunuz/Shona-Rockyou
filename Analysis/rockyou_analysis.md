# 📊 RockYou Dataset Analysis — README

## 📌 Overview

This project applies a **linguistic and structural analysis algorithm** to the widely known **RockYou password dataset**.

The dataset contains:

* **14.3 million raw passwords**
* **5.7 million unique cleaned entries**

The goal of this analysis is to understand:

* How passwords are structured
* How predictable they are
* How much they resemble natural language patterns

---

## 🔤 1. Character Distribution

The dataset is dominated by common letters such as:

* **a (11.6%)**
* **e (9.2%)**
* **i (7.4%)**
* **o (6.8%)**

👉 What this means:

Even in passwords, people tend to use **natural language characters**, especially vowels.
This reflects strong influence from **names, words, and familiar phrases**, rather than random strings.

---

## 📍 2. Letter Position Patterns

Most characters appear **in the middle of words**, with fewer at the start or end.

👉 What this means:

Passwords are not random character sequences.
They are often built like **real words**, following familiar writing patterns.

---

## 🧠 3. “Vowel” Detection Insight

The model attempts to infer vowels based on position patterns.

In this dataset, it incorrectly classifies **almost every letter as a vowel**.

👉 What this means:

* The dataset is **highly irregular**
* Passwords do not follow clean linguistic rules
* Many entries include **mixed formats, substitutions, and noise**

This highlights how **messy real-world password data is**

---

## 🔁 4. Repeated Patterns (N-grams)

Common prefixes and suffixes include:

* Prefixes: `ma`, `ch`, `mi`, `sa`, `ja`
* Suffixes: `ing`, `man`, `son`, `love`, `girl`, `123-style patterns`

👉 What this means:

Passwords are often built from:

* Names (e.g. *maria*, *daniel*)
* Words (e.g. *love*, *baby*)
* Internet-style patterns (*xxx*, *lol*, etc.)

This shows **heavy reuse of familiar building blocks**

---

## 🔐 5. Structural Predictability

### Compression Test

* Dataset is **~41% more compressible than random data**

👉 Meaning:

There is a **high level of repetition and structure** in passwords.

---

### Language Model (Predictability)

* Model predicts real passwords **3× better than random strings**

👉 Meaning:

Even a simple model can learn patterns and make **reasonable guesses**

---

## 🔀 6. Character Transitions (Entropy)

* Conditional entropy: **3.97 bits**

👉 Meaning:

* Higher than structured language (like Shona)
* Lower than fully random data

This places RockYou passwords in a **middle ground**:
➡️ Not random
➡️ Not fully structured
➡️ But still predictable

---

## 🧩 7. Pattern Complexity

* Average syllables per word: **8.32**
* Nearly all patterns classified as simple structures

👉 What this means:

Despite appearing complex, many passwords are:

* Long but **pattern-based**
* Built from repeated or predictable components

---

## 🔄 8. Zipf’s Law (Natural Language Behavior)

* Strong Zipf fit (R² = 0.97)

👉 Meaning:

The dataset behaves similarly to **natural language**, where:

* A few patterns are very common
* Many patterns are rare

---

## 📉 9. Entropy (Information Content)

* Average entropy is slightly lower than random data
* Distribution is more consistent than random

👉 Meaning:

Passwords are:

* **Less random than expected**
* More predictable due to repeated patterns

---

## 🧠 Key Takeaways

1. **Passwords are not random**

   * They strongly resemble natural language and human habits

2. **Patterns dominate**

   * Common prefixes, suffixes, and words appear repeatedly

3. **Predictability is real**

   * Even simple models can learn and exploit these patterns

4. **Complex ≠ Secure**

   * Long passwords can still be predictable if built from familiar structures

---

## 📊 Visualisations

This project includes two dashboards:

* **Structural Dashboard** — shows patterns, compression, and entropy
* **Linguistic Dashboard** — shows character distribution and structure

These images provide a **visual representation of the patterns** described above.

---

## 🚀 Final Note

This analysis highlights a key idea:

> Password weakness is not just about users — it is about **language, habits, and structure**

Understanding these patterns is essential for:

* Better password policies
* Stronger security tools
* More realistic attack simulations

## **Visualisations**

Two visual outputs are included in this folder:

* **Structural dashboard** — showing frequency, entropy, and distribution patterns
* **Linguistic dashboard** — showing phonetic and morphological structure

These provide a visual representation of the patterns described above.