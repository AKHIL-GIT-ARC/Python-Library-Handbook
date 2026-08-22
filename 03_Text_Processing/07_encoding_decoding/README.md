# Encoding and Decoding in Python

Encoding converts a string into bytes.

Decoding converts bytes back into a string.

    String → Encode → Bytes
    Bytes → Decode → String

---

## Encoding

Use `encode()` to convert a string into bytes.

    text = "Hello"
    data = text.encode("utf-8")
    print(data)

Output:

    b'Hello'

---

## UTF-8

UTF-8 is the most commonly used character encoding.

It supports:

- English
- Indian languages
- International languages
- Symbols
- Emojis

Example:

    text = "Hello ₹ 😀"
    data = text.encode("utf-8")
    print(data)

---

## Decoding

Use `decode()` to convert bytes back into a string.

    data = b"Hello"
    text = data.decode("utf-8")
    print(text)

Output:

    Hello

---

## Encoding and Decoding Flow

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

## `str` vs `bytes`

| Type | Represents |
|---|---|
| `str` | Text |
| `bytes` | Binary data |

Example:

    text = "Python"
    data = text.encode("utf-8")

    print(type(text))
    print(type(data))

Output:

    <class 'str'>
    <class 'bytes'>

---

## Encoding Errors

Some characters may not be supported by certain encodings.

    text = "₹"
    data = text.encode("ascii")

This raises:

    UnicodeEncodeError

UTF-8 supports the character:

    data = text.encode("utf-8")

---

## Error Handling

Use `errors` to control encoding errors.

### `errors="ignore"`

Skips unsupported characters.

    text = "Hello ₹"

    print(text.encode("ascii", errors="ignore"))

### `errors="replace"`

Replaces unsupported characters.

    print(text.encode("ascii", errors="replace"))

---

## Key Points

- Encoding converts `str` → `bytes`.
- Decoding converts `bytes` → `str`.
- UTF-8 is the most commonly used encoding.
- Use `encode()` for encoding.
- Use `decode()` for decoding.
- `str` represents text.
- `bytes` represents binary data.
- `errors` controls encoding errors.

---

## Quick Revision

| Operation | Method |
|---|---|
| String → Bytes | `encode()` |
| Bytes → String | `decode()` |
| Common encoding | UTF-8 |
| Text type | `str` |
| Binary type | `bytes` |
| Ignore errors | `errors="ignore"` |
| Replace errors | `errors="replace"` |