````markdown

# Textwrap in Python

The `textwrap` module is used to format and wrap long strings.

It is useful for making long text easier to read and display.

```python
import textwrap
````

---

## `wrap()`

Breaks text into a list of lines based on the given width.

```python
text = "Python is easy to learn"
print(textwrap.wrap(text, width=10))
```

Output:

```text
['Python is', 'easy to', 'learn']
```

---

## `fill()`

Wraps text and returns the result as a single string.

```python
text = "Python is easy to learn"
print(textwrap.fill(text, width=10))
```

Output:

```text
Python is
easy to
learn
```

---

## `shorten()`

Shortens text to fit within a specified width.

```python
text = "Python is a powerful programming language"
print(textwrap.shorten(text, width=25))
```

Output:

```text
Python is a powerful [...]
```

---

## `indent()`

Adds a prefix to every line.

```python
text = "Hello\nPython"
print(textwrap.indent(text, "> "))
```

Output:

```text
> Hello
> Python
```

---

## `dedent()`

Removes common leading whitespace from multiple lines.

```python
text = """
    Hello
    Python
"""
print(textwrap.dedent(text))
```

---

## Common Methods

| Method      | Purpose               |
| ----------- | --------------------- |
| `wrap()`    | Text → List of lines  |
| `fill()`    | Text → Wrapped string |
| `shorten()` | Shorten text          |
| `indent()`  | Add prefix            |
| `dedent()`  | Remove indentation    |

---

## Key Points

* `textwrap` is part of Python's standard library.
* `wrap()` returns a list.
* `fill()` returns a string.
* `shorten()` adds `[...]` when text is shortened.
* `indent()` adds a prefix to lines.
* `dedent()` removes common indentation.

---

## Quick Revision

| Method      | Remember           |
| ----------- | ------------------ |
| `wrap()`    | Break lines        |
| `fill()`    | Wrap into string   |
| `shorten()` | Make text shorter  |
| `indent()`  | Add prefix         |
| `dedent()`  | Remove indentation |

```
