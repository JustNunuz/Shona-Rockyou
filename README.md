# Shona-Rockyou
<img width="1536" height="1024" alt="20260112_2053_Image Generation_simple_compose_01kesrsj1dfz3a3ytdd15s9yzh" src="https://github.com/user-attachments/assets/03f4db7c-e27f-45df-8d8e-28e2d0b6402e" />


## Overview

**Shona RockYou** is a research-oriented linguistic corpus project focused on the Shona language and Shona cultural naming systems. Inspired structurally by large-scale leaked password datasets such as *rockyou.txt*, this project repurposes the concept ethically and academically to study **human-generated linguistic patterns**, **cultural naming conventions**, and **predictability in meaningful strings**.

Rather than containing credentials or sensitive material, Shona RockYou is composed entirely of **public, culturally derived lexical items** such as personal names, surnames, totems (mitupo), and place names. The dataset is intended for **linguistic analysis**, **cultural documentation**, and **security research**, particularly in understanding how meaning, culture, and language structure influence human choice patterns.

This project sits at the intersection of **African language studies**, **computational linguistics**, and **cybersecurity research**.

---

## Research Motivation

Human-generated strings are rarely random. In many African languages, including Shona, names and words carry semantic meaning, moral intention, family history, or social context. This makes them especially valuable for studying:

* Linguistic structure and morphology
* Cultural repetition and inheritance
* Predictability introduced by meaning
* Entropy reduction in semantically rich languages

By analyzing this corpus using tools such as **pipal**, researchers can observe how culture and language shape patterns in human-generated text.

---

## Ethical Framework

This project follows a strict ethical boundary:

* No leaked passwords or credentials
* No personal or private datasets
* No association with credential stuffing or unauthorized access

All data included is:

* Publicly known
* Culturally documented
* Linguistically relevant

The goal is analysis and preservation, not exploitation.

---

## Dataset Schema

The corpus is structured into discrete, analyzable components. Each category may be studied independently or combined for comparative analysis.

```
data/
 ├── names_given.txt        # Shona given names
 ├── names_surnames.txt    # Common Shona surnames
 ├── totems.txt            # Mitupo (clan totems)
 ├── towns.txt             # Towns, cities, and place names
 ├── prefixes.txt          # Common linguistic prefixes
 ├── suffixes.txt          # Common linguistic suffixes
 ├── combined_raw.txt      # All entries combined (raw)
 └── combined_mutated.txt  # Generated morphological variants
```

### 1. Given Names

Personal names reflecting:

* Meaning-based naming
* Gender-neutral structures
* Religious and traditional overlap

### 2. Surnames

Family names with strong cultural and clan associations, often tied to totems or geography.

### 3. Totems (Mitupo)

Clan identifiers that encode lineage, taboo, praise poetry, and cultural identity.

### 4. Place Names

Geographic identifiers reflecting:

* Pre-colonial language
* Colonial influence
* Urban vs rural naming patterns

### 5. Morphological Components

Prefixes and suffixes commonly reused across names and words, enabling structural analysis and variant generation.

---

## Example Seed Data

### Sample Given Names

* Tinashe
* Tendai
* Farai
* Nyasha
* Tapiwa
* Kudakwashe
* Ropafadzo
* Tatenda
* Munashe
* Anesu

These names are semantically meaningful and demonstrate common morphological patterns such as:

* `-ashe` (God / grace)
* `-enda` (thanks)
* `-wa` (passive or bestowed)

---

## Intended Analysis

Using tools such as **pipal**, this corpus can be analyzed to explore:

* Frequency of base morphemes
* Repeated substrings and suffix dominance
* Entropy differences between name types
* Predictability introduced by cultural meaning

Comparative studies may include:

* Given names vs surnames
* Totems vs place names
* Shona corpus vs other linguistic datasets

---

## Project Scope and Future Work

Planned expansions include:

* Morphological mutation generation
* Cross-language comparison with other Bantu languages
* Visualization of naming patterns
* Academic write-ups on cultural entropy

---

## Project Name Rationale

The name **Shona RockYou** is intentionally provocative but reframed. It references the structural inspiration of large-scale human-generated datasets while explicitly rejecting unethical data sources. The contrast highlights how culture, meaning, and language shape predictability in ways similar to — but distinct from — password datasets.

---

## Disclaimer

This project is for educational and research purposes only. Any misuse of the data is outside the intent and responsibility of the author.
