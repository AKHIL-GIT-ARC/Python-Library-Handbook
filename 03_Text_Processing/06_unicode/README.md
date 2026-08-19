# Unicode in Python

Unicode is a standard used to represent characters from different languages, symbols, and emojis.

Python 3 strings support Unicode by default.

---

## Unicode Characters

Python can directly store Unicode characters.

    text = "Hello 世界 🌍"

    print(text)

Output:

    Hello 世界 🌍

---

## `ord()`

Returns the Unicode code point of a character.

    print(ord("A"))
    print(ord("₹"))

Output:

    65
    8377

---

## `chr()`

Converts a Unicode code point into a character.

    print(chr(65))
    print(chr(8377))

Output:

    A
    ₹

---

## Unicode Escape Sequence

Unicode characters can be represented using `\u`.

    print("\u0041")
    print("\u20B9")

Output:

    A
    ₹

For code points above `FFFF`, use `\U`.

    print("\U0001F600")

Output:

    😀

---

## Character ↔ Unicode

```text
Character → ord() → Unicode code point
Code point → chr() → Character