# Text Normalization — Cheat Sheet

## Import

    import unicodedata

---

## `normalize()`

Normalizes Unicode text.

    unicodedata.normalize("NFC", text)

---

## Normalization Forms

| Form | Purpose |
|---|---|
| `NFC` | Compose characters |
| `NFD` | Decompose characters |
| `NFKC` | Compatibility + compose |
| `NFKD` | Compatibility + decompose |

---

## NFC

Combines characters into a composed form.

    unicodedata.normalize("NFC", "cafe\u0301")

Result:

    café

---

## NFD

Separates characters into base characters and combining marks.

    unicodedata.normalize("NFD", "é")

Result:

    e + combining accent

---

## NFKC / NFKD

Used for compatibility normalization.

    unicodedata.normalize("NFKC", text)
    unicodedata.normalize("NFKD", text)

Example:

    "①" → "1"

---

## `combining()`

Checks whether a character is a combining mark.

    unicodedata.combining(char)

Returns:

    0 → Not a combining character
    Non-zero → Combining character

---

## Remove Accents

    normalized = unicodedata.normalize("NFD", text)

    result = "".join(
        char for char in normalized
        if not unicodedata.combining(char)
    )

Example:

    "café" → "cafe"

---

## Key Points

- Normalization makes Unicode text consistent.
- `NFC` → Compose.
- `NFD` → Decompose.
- `NFKC` → Compatibility + compose.
- `NFKD` → Compatibility + decompose.
- `combining()` identifies combining marks.
- NFD + `combining()` can remove accents.

---

## Quick Revision

    normalize() → Normalize Unicode
    NFC         → Compose
    NFD         → Decompose
    NFKC        → Compatibility + Compose
    NFKD        → Compatibility + Decompose
    combining() → Check combining mark