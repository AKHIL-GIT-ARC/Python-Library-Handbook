# Text Normalization in Python

Text normalization converts text into a consistent form.

It is useful when comparing, searching, and processing Unicode text.

Python provides the `unicodedata` module for Unicode normalization.

    import unicodedata

---

## `unicodedata.normalize()`

Normalizes Unicode text using a specified normalization form.

    text = "café"
    result = unicodedata.normalize("NFC", text)
    print(result)

---

## NFC

NFC combines characters into their standard composed form.

    unicodedata.normalize("NFC", text)

Useful for keeping equivalent Unicode text in a consistent form.

---

## NFD

NFD separates characters into their base character and combining marks.

    unicodedata.normalize("NFD", text)

Example:

    "é" → "e" + combining accent

---

## NFKC

NFKC performs compatibility normalization and converts compatible characters into a standard form.

    unicodedata.normalize("NFKC", text)

---

## NFKD

NFKD performs compatibility normalization and decomposes characters.

    unicodedata.normalize("NFKD", text)

---

## Normalization Forms

| Form | Purpose |
|---|---|
| `NFC` | Compose characters |
| `NFD` | Decompose characters |
| `NFKC` | Compatibility + compose |
| `NFKD` | Compatibility + decompose |

---

## Removing Accents

NFD can be combined with `combining()` to remove accent marks.

    text = "café"

    normalized = unicodedata.normalize("NFD", text)

    result = "".join(
        char for char in normalized
        if not unicodedata.combining(char)
    )

    print(result)

Output:

    cafe

---

## Why Normalize Text?

Normalization helps when:

- Comparing Unicode strings
- Searching text
- Cleaning user input
- Removing accents
- Processing multilingual text

---

## Key Points

- Unicode characters can have different representations.
- `unicodedata.normalize()` creates a consistent representation.
- `NFC` composes characters.
- `NFD` decomposes characters.
- `NFKC` applies compatibility normalization and composes.
- `NFKD` applies compatibility normalization and decomposes.
- `combining()` can identify combining marks.

---

## Quick Revision

| Function / Form | Remember |
|---|---|
| `normalize()` | Normalize Unicode text |
| `NFC` | Compose |
| `NFD` | Decompose |
| `NFKC` | Compatibility + compose |
| `NFKD` | Compatibility + decompose |
| `combining()` | Identify combining marks |