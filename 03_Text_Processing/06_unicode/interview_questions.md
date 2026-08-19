# Unicode — Interview Questions

## 1. What is Unicode?

Unicode is a standard used to represent characters, symbols, and emojis from different languages.

---

## 2. Does Python 3 support Unicode?

Yes. Python 3 strings support Unicode by default.

    text = "Hello 世界 😀"

---

## 3. What does `ord()` do?

`ord()` converts a character into its Unicode code point.

    print(ord("A"))

Output:

    65

---

## 4. What does `chr()` do?

`chr()` converts a Unicode code point into its character.

    print(chr(65))

Output:

    A

---

## 5. What is the difference between `ord()` and `chr()`?

| Function | Conversion |
|---|---|
| `ord()` | Character → Code point |
| `chr()` | Code point → Character |

---

## 6. How do you represent a Unicode character using an escape sequence?

Use `\u` for four-digit Unicode values.

    print("\u20B9")

Output:

    ₹

For larger values, use `\U`.

    print("\U0001F600")

Output:

    😀

---

## 7. What is a Unicode code point?

A code point is a unique numeric value assigned to a Unicode character.

Example:

    A → U+0041
    ₹ → U+20B9
    😀 → U+1F600

---

## 8. Can Python handle emojis and non-English characters?

Yes.

    text = "Hello नमस्ते 世界 😀"
    print(text)

---

## Quick Revision

| Concept | Remember |
|---|---|
| Unicode | Character representation standard |
| `ord()` | Character → Code point |
| `chr()` | Code point → Character |
| `\uXXXX` | Unicode escape |
| `\UXXXXXXXX` | Large Unicode escape |
| Python 3 | Unicode strings by default |