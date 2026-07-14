# Shona-Rockyou
<img width="1536" height="1024" alt="20260112_2053_Image Generation_simple_compose_01kesrsj1dfz3a3ytdd15s9yzh" src="https://github.com/user-attachments/assets/03f4db7c-e27f-45df-8d8e-28e2d0b6402e" />


## Overview

**Shona RockYou** is a research-oriented linguistic corpus project focused on the Shona language and Shona cultural naming systems. Inspired structurally by large-scale leaked password datasets such as *rockyou.txt*, this project repurposes the concept ethically and academically to study **human-generated linguistic patterns**, **cultural naming conventions**, and **predictability in meaningful strings**.

Rather than containing credentials or sensitive material, Shona RockYou is composed entirely of **public, culturally derived lexical items** such as personal names, surnames, totems (mitupo), place names, companies, brands, and social media text. The dataset is intended for **linguistic analysis**, **cultural documentation**, and **security research** — particularly in understanding how meaning, culture, and language structure influence human choice patterns.

This project sits at the intersection of **African language studies**, **computational linguistics**, and **cybersecurity research**, and forms a core component of the broader [Z3r0 Nois3](https://github.com/JustNunuz/z3r0-Noise) research ecosystem.

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

## Repository Structure

```
shona-rockyou/
├── Analysis/
│   ├── readme.md                          # Detailed linguistic analysis write-up
│   ├── NGM_readme.txt                     # Given Names morphological analysis
│   ├── NSM_readme.txt                     # Surnames morphological analysis
│   ├── rockyou_analysis.md                # RockYou comparative analysis
│   ├── shona_linguistic_dashboard.png     # Linguistic analysis visualisation
│   └── shona_structural_dashboard.png     # Structural analysis visualisation
├── Wordlists/
│   ├── cleaned/                           # Manually curated, clean datasets
│   │   ├── cleaned_tweets.txt             #   Cleaned Shona tweets (15,690 entries)
│   │   ├── names_given.txt                #   Clean given names (461 entries)
│   │   └── names_surnames.txt             #   Clean surnames (999 entries)
│   ├── uncleaned/                         # Raw, unprocessed source data
│   │   └── tweets.txt                     #   Raw Shona tweet corpus (17,016 entries)
│   ├── names_given.txt                    # Shona given names (461 entries)
│   ├── names_surnames.txt                 # Shona surnames (999 entries)
│   ├── names_given_mutations.txt          # Morphological name mutations (17,584 entries)
│   ├── names_surnames_mutations.txt       # Morphological surname mutations (22,124 entries)
│   ├── Given_names_Leet.txt               # Leetspeak given name permutations (17,584 entries)
│   ├── Surnames_Leet.txt                  # Leetspeak surname permutations (22,124 entries)
│   ├── combined first and surnames.txt    # Cartesian product of names × surnames (462,000 entries)
│   ├── cleaned_tweets.txt                 # Cleaned Shona tweet corpus (15,690 entries)
│   ├── companies_and_brands.txt           # Zimbabwean companies & brands (992 entries)
│   ├── geography.txt                      # Zimbabwean place names & landmarks (243 entries)
│   ├── popculture.txt                     # Zimbabwean celebrities & cultural figures (203 entries)
│   ├── totems.txt                         # Shona clan totems / mitupo (24 entries)
│   └── dates_1900_2200.txt                # Date strings for combinatorial testing (301 entries)
├── LICENSE
└── README.md
```

---

## Dataset Categories

### Core Name Data
| Wordlist | Entries | Description |
|---|---|---|
| `names_given.txt` | 461 | Curated Shona given names |
| `names_surnames.txt` | 999 | Curated Shona surnames |
| `combined first and surnames.txt` | 462,000 | Full Cartesian product of given names × surnames |

### Mutated & Leet Variants
| Wordlist | Entries | Description |
|---|---|---|
| `names_given_mutations.txt` | 17,584 | Morphological mutations of given names |
| `names_surnames_mutations.txt` | 22,124 | Morphological mutations of surnames |
| `Given_names_Leet.txt` | 17,584 | Leetspeak permutations of given names |
| `Surnames_Leet.txt` | 22,124 | Leetspeak permutations of surnames |

### Cultural & Contextual Data
| Wordlist | Entries | Description |
|---|---|---|
| `companies_and_brands.txt` | 992 | Zimbabwean companies, brands, and products |
| `geography.txt` | 243 | Zimbabwean cities, towns, and landmarks |
| `popculture.txt` | 203 | Zimbabwean celebrities, artists, and influencers |
| `totems.txt` | 24 | Shona clan totems (mitupo) |
| `dates_1900_2200.txt` | 301 | Year strings for combinatorial password testing |

### Social Media Corpus
| Wordlist | Entries | Description |
|---|---|---|
| `tweets.txt` (uncleaned) | 17,016 | Raw Shona-language tweet corpus |
| `cleaned_tweets.txt` | 15,690 | Processed and de-duplicated tweet corpus |

**Total corpus size: ~594,000+ entries**

---

## Analysis & Findings

The `Analysis/` directory contains detailed structural and linguistic analysis of the wordlists, including:

* **Letter frequency analysis** — character distribution follows strong Shona phonological rules (e.g. `a` accounts for ~18% of all characters)
* **Morphological structure** — common prefixes (`ma-`, `mu-`, `chi-`, `ta-`) and suffixes (`-she`, `-ayi`, `-nga`, `-nda`) are systematically identified
* **Phonetic consistency** — 99.1% of entries end in a vowel; 87%+ of syllables follow CV or V patterns
* **Predictability metrics** — bigram conditional entropy of ~2.75 bits; language model perplexity of ~8.02 (vs. ~315 for random data — a 39× difference)
* **Structural redundancy** — the corpus compresses to ~41.9% of its original size, ~33% more structured than random text
* **Zipf compliance** — R² ≈ 0.93, confirming natural language distribution

Visual dashboards are included for both structural and linguistic pattern analysis.

---

## Example Seed Data

### Sample Given Names

* Tinashe, Tendai, Farai, Nyasha, Tapiwa
* Kudakwashe, Ropafadzo, Tatenda, Munashe, Anesu

These names are semantically meaningful and demonstrate common morphological patterns such as:

* `-ashe` (God / grace)
* `-enda` (thanks)
* `-wa` (passive or bestowed)

### Sample Companies & Brands

* Cerevita, Mazoe, Zambezi, Econet, Delta Corporation

### Sample Totems

* Shumba, Nzou, Moyo, Shava, Mbizi

---

## Intended Use Cases

* **Password security research** — understanding how cultural and linguistic patterns influence password selection in Bantu-language communities
* **CTF & penetration testing** — wordlists for brute-forcing or enumerating passwords with Shona linguistic characteristics
* **Computational linguistics** — morphological analysis, tokenization research, and entropy modelling of agglutinative languages
* **Cultural documentation** — preserving and cataloguing Shona naming conventions and cultural identifiers
* **AI/NLP research** — benchmarking tokenizer performance and quantifying the "Bantu Tax" in large language models

---

## Project Scope and Future Work

Planned expansions include:

* Additional morphological mutation generation
* Common Shona phrases and idiomatic expressions
* Cross-language comparison with other Bantu languages (Zulu, Ndebele, Xhosa)
* Expanded social media corpus collection
* Visualization of naming patterns and cultural trends
* Academic write-ups on cultural entropy

---

## Part of Z3r0 Nois3

Shona-Rockyou is a submodule of the [Z3r0 Nois3](https://github.com/JustNunuz/z3r0-Noise) project, which investigates tokenization inefficiency (the "Bantu Tax") in large language models when processing Bantu languages. The Bridge engine within Z3r0 Nois3 uses these wordlists to benchmark and mitigate tokenization bias.

---

## Project Name Rationale

The name **Shona RockYou** is intentionally provocative but reframed. It references the structural inspiration of large-scale human-generated datasets while explicitly rejecting unethical data sources. The contrast highlights how culture, meaning, and language shape predictability in ways similar to — but distinct from — password datasets.

---

## Disclaimer

This project is for educational and research purposes only. Any misuse of the data is outside the intent and responsibility of the author.
