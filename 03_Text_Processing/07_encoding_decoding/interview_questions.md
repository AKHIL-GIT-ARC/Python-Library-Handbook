# Encoding and Decoding — Interview Questions

## 1. What is encoding?

Encoding converts a string into bytes using a character encoding.

    text = "Hello"
    data = text.encode("utf-8")

---

## 2. What is decoding?

Decoding converts bytes back into a string.

    data = b"Hello"
    text = data.decode("utf-8")

---

## 3. What is UTF-8?

UTF-8 is a widely used character encoding that supports Unicode characters, including different languages, symbols, and emojis.

---

## 4. What is the difference between `str` and `bytes`?

| Type | Represents |
|---|---|
| `str` | Text |
| `bytes` | Binary data |

---

## 5. What does `encode()` do?

Converts `str` into `bytes`.

    "Python".encode("utf-8")

---

## 6. What does `decode()` do?

Converts `bytes` into `str`.

    b"Python".decode("utf-8")

---

## 7. What happens if an encoding cannot represent a character?

Python raises a `UnicodeEncodeError`.

Example:

    "₹".encode("ascii")

---

## 8. What is `errors="ignore"`?

It skips characters that cannot be encoded or decoded.

    text.encode("ascii", errors="ignore")

---

## 9. What is `errors="replace"`?

It replaces characters that cannot be encoded or decoded.

    text.encode("ascii", errors="replace")

---

## 10. What is the encoding and decoding flow?

    String
       ↓
    encode()
       ↓
    Bytes
       ↓
    decode()
       ↓
    String

---

## Quick Revision

| Concept | Remember |
|---|---|
| Encoding | `str` → `bytes` |
| Decoding | `bytes` → `str` |
| UTF-8 | Common Unicode encoding |
| `encode()` | Convert to bytes |
| `decode()` | Convert to string |
| `str` | Text |
| `bytes` | Binary data |
| `errors="ignore"` | Skip errors |
| `errors="replace"` | Replace errors |