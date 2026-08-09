# Textwrap — Cheat Sheet

## Import

```python
import textwrap
````

---

## `wrap()`

Converts text into a list of wrapped lines.

```python
textwrap.wrap(text, width=20)
```

```text
Returns → list
```

---

## `fill()`

Wraps text and returns a single string.

```python
textwrap.fill(text, width=20)
```

```text
Returns → string
```

---

## `shorten()`

Shortens text to a specified width.

```python
textwrap.shorten(text, width=20)
```

Adds `[...]` when text is shortened.

---

## `indent()`

Adds a prefix to every line.

```python
textwrap.indent(text, "> ")
```

---

## `dedent()`

Removes common leading whitespace.

```python
textwrap.dedent(text)
```

---

## Common Methods

| Method      | Purpose            |
| ----------- | ------------------ |
| `wrap()`    | Text → List        |
| `fill()`    | Text → String      |
| `shorten()` | Shorten text       |
| `indent()`  | Add prefix         |
| `dedent()`  | Remove indentation |

---

## Key Points

* `wrap()` returns a list.
* `fill()` returns a string.
* `shorten()` creates a shortened preview.
* `indent()` adds a prefix.
* `dedent()` removes common indentation.

---

## Quick Revision

```text
wrap()     → Break into lines
fill()     → Wrap as string
shorten()  → Shorten text
indent()   → Add prefix
dedent()   → Remove indentation
```

```
