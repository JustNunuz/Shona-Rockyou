# **Shona Wordlist Analysis**

## **Overview**

This folder contains the results of a **detailed structural and linguistic analysis** of a Shona wordlist.

The wordlist itself is constructed from a **combination of Shona given names and surnames**, providing a dataset that reflects real-world naming conventions and commonly used linguistic patterns.

The purpose of this analysis is to understand:

* how Shona words are structured
* how predictable those structures are
* and how linguistic patterns influence repetition and variation

This is especially relevant in contexts such as password analysis, where human language directly shapes how people construct memorable strings.

---

## **1. Global Letter Frequency**

The dataset shows that character usage is highly uneven.

* The letter **“a” accounts for ~18%** of all characters
* Other dominant letters include **i, m, n, e, u**
* Several letters (such as x, j, f) appear very rarely

This confirms that the wordlist is **not random in character distribution**. Instead, it follows a clear frequency pattern where a small subset of letters dominates usage.

This kind of imbalance reduces the effective search space when modelling or predicting word formation.

---

## **2. Positional Distribution of Letters**

The positional heatmap shows that letters are not used uniformly across positions in a word.

* Certain letters (e.g. **m, c, j**) appear more frequently at the beginning
* Vowels such as **e, i, o, a** are strongly represented at the end of words
* Most letters are concentrated in the middle positions

This indicates that **word structure is position-dependent**, meaning that where a letter appears is just as important as how often it appears.

These positional constraints further reduce randomness and reinforce predictable patterns.

---

## **3. Inferred Vowel System**

Using positional behaviour, the analysis infers a vowel set primarily consisting of:

**{ a, e, i, o, u }**

with additional edge cases emerging from the dataset.

A key observation is that vowels dominate word endings:

* Over **99% of entries end in a vowel**

This highlights a strong phonological rule within the dataset, where vowel-final structures are overwhelmingly preferred.

---

## **4. Morphological Structure (Prefixes and Suffixes)**

The wordlist exhibits strong repetition of common prefixes and suffixes.

### Common prefixes:

* **ma-, mu-, chi-, ta-, ny-, ru-, ti-**

### Common suffixes:

* **-she, -ayi, -nga, -nda, -mba, -iwa**

These elements are not arbitrary — they are **meaningful linguistic units** that are reused across many names.

Type-Token Ratio (TTR) values are low, indicating:

* a small number of structural patterns
* reused across many words

This confirms that the dataset is **morphologically productive but structurally repetitive**.

---

## **5. Phonetic Consistency**

The dataset demonstrates strong phonetic regularity:

* **99.1% of words end in a vowel**

* The majority of syllables follow simple patterns such as:

  * Consonant–Vowel (CV)
  * Vowel-only (V)

* Over **87% of all syllables are CV or V**

Additionally, common consonant clusters such as:

* **ch, mb, dz, gw, zv**

appear frequently and consistently.

This indicates that the language follows **strict phonotactic rules**, which constrain how words can be formed and pronounced.

---

## **6. Character Transition Predictability**

The bigram transition analysis shows a **conditional entropy of ~2.75 bits**.

This means:

* the next character in a sequence is not independent
* transitions between characters follow predictable patterns

Some characters (such as “c”) have extremely low entropy, meaning they are almost always followed by specific letters.

This demonstrates that **character sequences are highly structured and learnable**.

---

## **7. Positional Entropy Profile**

Entropy varies across positions in a word:

* Middle positions have higher entropy (more variation)
* Beginning and ending positions have lower entropy (more predictable)

This suggests that:

* word boundaries are more constrained
* variation is concentrated within the internal structure of words

---

## **8. Syllable Structure**

The dataset contains:

* **5,507 total syllables**
* An average of **~4 syllables per word**

Distribution:

* **CV (56.1%)**
* **V (31.5%)**
* **CCV (12.1%)**

This confirms that most words follow **simple, repetitive syllable patterns**, reinforcing phonetic consistency and predictability.

---

## **9. Vowel Interaction Patterns**

The analysis shows:

* No strong vowel harmony effect (observed ≈ expected)
* However, certain vowel combinations are significantly more frequent, such as:

  * **a-n, a-i, a-a, a-e**

This indicates that while vowels are not strictly harmonised,
they still follow **preferred co-occurrence patterns** within words.

---

## **10. Zipf Distribution**

The dataset shows a **moderate Zipfian distribution (R² ≈ 0.93)**.

This confirms that the wordlist behaves like **natural language**, where:

* a few patterns occur very frequently
* many patterns occur rarely

---

## **11. Structural Redundancy (Compression Analysis)**

* Wordlist compresses to **~41.9% of its original size**
* Random data compresses to **~62.8%**

This means the dataset is **~33% more structured than random text**.

This is strong evidence of:

* repetition
* regularity
* predictable construction

---

## **12. Language Model Predictability**

A simple bigram model trained on the wordlist shows:

* **Perplexity ≈ 8.02 for real data**
* **Perplexity ≈ 315.29 for random data**
* ~**39× difference in predictability**

This demonstrates that:

* the structure of the dataset can be learned efficiently
* real words are far more predictable than random sequences

---

## **13. Information Theory (Entropy)**

* Mean entropy is nearly identical to random data
* However, variance is lower (more consistency)

This suggests:

* overall complexity appears similar
* but internal structure is more stable and predictable

---

## **Visualisations**

Two visual outputs are included in this folder:

* **Structural dashboard** — showing frequency, entropy, and distribution patterns
* **Linguistic dashboard** — showing phonetic and morphological structure

These provide a visual representation of the patterns described above.
