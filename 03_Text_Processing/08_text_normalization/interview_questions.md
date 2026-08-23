# Text Normalization — Interview Questions

## 1. What is text normalization?

Text normalization converts text into a consistent Unicode representation.

It is useful for comparing, searching, and processing text.

---

## 2. Which module is used for Unicode normalization?

Python provides the `unicodedata` module.

    import unicodedata

---

## 3. What does `unicodedata.normalize()` do?

It converts Unicode text into a specified normalization form.

    unicodedata.normalize("NFC", text)

---

## 4. What is the difference between NFC and NFD?

| Form | Purpose |
|---|---|
| `NFC` | Composes characters |
| `NFD` | Decomposes characters |

Example:

    é → e + combining accent

---

## 5. What are NFKC and NFKD?

They perform **compatibility normalization**.

| Form | Purpose |
|---|---|
| `NFKC` | Compatibility + Compose |
| `NFKD` | Compatibility + Decompose |

---

## 6. What does `unicodedata.combining()` do?

It checks whether a character is a combining mark.

    unicodedata.combining(char)

Returns `0` for a non-combining character.

---

## 7. How can you remove accents from text?

Use NFD and remove combining characters.

    normalized = unicodedata.normalize("NFD", text)

    result = "".join(
        char for char in normalized
        if not unicodedata.combining(char)
    )

Example:

    "café" → "cafe"

---

## 8. Why is text normalization useful?

It is useful for:

- Comparing Unicode strings
- Searching text
- Cleaning user input
- Removing accents
- Processing multilingual text

---

## Quick Revision

| Concept | Remember |
|---|---|
| `normalize()` | Normalize Unicode |
| `NFC` | Compose |
| `NFD` | Decompose |
| `NFKC` | Compatibility + Compose |
| `NFKD` | Compatibility + Decompose |
| `combining()` | Identify combining marks |