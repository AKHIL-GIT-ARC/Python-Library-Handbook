# Encoding and Decoding — Cheat Sheet

## Basic Concept

    String → encode() → Bytes
    Bytes → decode() → String

---

## `encode()`

Converts a string into bytes.

    text = "Hello"
    data = text.encode("utf-8")

---

## `decode()`

Converts bytes back into a string.

    data = b"Hello"
    text = data.decode("utf-8")

---

## UTF-8

UTF-8 is the most commonly used text encoding.

    text = "Hello ₹ 😀"
    data = text.encode("utf-8")

---

## `str` vs `bytes`

| Type | Meaning |
|---|---|
| `str` | Text |
| `bytes` | Binary data |

---

## Error Handling

    text.encode("ascii", errors="ignore")

Skips unsupported characters.

    text.encode("ascii", errors="replace")

Replaces unsupported characters.

---

## Common Errors

| Error | Cause |
|---|---|
| `UnicodeEncodeError` | Character cannot be encoded |
| `UnicodeDecodeError` | Bytes cannot be decoded |

---

## Key Points

- `encode()` → `str` to `bytes`.
- `decode()` → `bytes` to `str`.
- UTF-8 supports Unicode characters.
- `str` represents text.
- `bytes` represents binary data.
- `errors="ignore"` skips invalid characters.
- `errors="replace"` replaces invalid characters.

---

## Quick Revision

| Operation | Method |
|---|---|
| String → Bytes | `encode()` |
| Bytes → String | `decode()` |
| Common encoding | UTF-8 |
| Text | `str` |
| Binary data | `bytes` |
| Skip errors | `errors="ignore"` |
| Replace errors | `errors="replace"` |