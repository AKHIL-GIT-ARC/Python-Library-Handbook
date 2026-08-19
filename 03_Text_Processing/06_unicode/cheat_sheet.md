# Unicode — Cheat Sheet

## Unicode

Unicode is a standard for representing characters, symbols, and emojis from different languages.

    Python 3 → Unicode strings by default

---

## `ord()`

Converts a character into its Unicode code point.

    ord("A")
    ord("₹")

Output:

    65
    8377

---

## `chr()`

Converts a Unicode code point into a character.

    chr(65)
    chr(8377)

Output:

    A
    ₹

---

## Unicode Escape Sequences

Use `\u` for four-digit Unicode values.

    "\u0041"
    "\u20B9"

Output:

    A
    ₹

Use `\U` for larger Unicode values.

    "\U0001F600"

Output:

    😀

---

## Character ↔ Code Point

    Character → ord() → Code Point
    Code Point → chr() → Character

---

## Common Unicode Values

| Character | Unicode |
|---|---|
| `A` | `U+0041` |
| `a` | `U+0061` |
| `0` | `U+0030` |
| `₹` | `U+20B9` |
| `©` | `U+00A9` |
| `😀` | `U+1F600` |

---

## Key Points

- Python 3 strings support Unicode by default.
- `ord()` → Character to code point.
- `chr()` → Code point to character.
- `\uXXXX` represents Unicode characters.
- `\UXXXXXXXX` represents larger Unicode characters.
- Unicode supports multilingual text, symbols, and emojis.

---

## Quick Revision

| Function / Syntax | Purpose |
|---|---|
| `ord()` | Character → Code point |
| `chr()` | Code point → Character |
| `\uXXXX` | Unicode escape |
| `\UXXXXXXXX` | Unicode escape |
| Unicode | Character representation standard |