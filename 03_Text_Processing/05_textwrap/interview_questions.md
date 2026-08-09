````markdown
# Textwrap — Interview Questions

## 1. What is the `textwrap` module?

`textwrap` is a Python standard library module used to format and wrap long text.

```python
import textwrap
````

---

## 2. What does `wrap()` do?

It breaks text into a list of lines.

```python
textwrap.wrap("Python is easy to learn", width=10)
```

Returns:

```text
['Python is', 'easy to', 'learn']
```

---

## 3. What is the difference between `wrap()` and `fill()`?

| Method   | Returns |
| -------- | ------- |
| `wrap()` | List    |
| `fill()` | String  |

---

## 4. What does `shorten()` do?

It shortens text to fit within a specified width.

```python
textwrap.shorten("Python is a powerful language", width=20)
```

---

## 5. What does `indent()` do?

It adds a prefix to every line.

```python
textwrap.indent("Hello\nPython", "> ")
```

Output:

```text
> Hello
> Python
```

---

## 6. What does `dedent()` do?

It removes common leading whitespace from multiline text.

```python
textwrap.dedent(text)
```

---

## 7. Where is `textwrap` useful?

It is useful for:

* Formatting long text
* Console output
* Reports
* Text previews
* Readable documentation

---

## Quick Revision

| Method      | Purpose               |
| ----------- | --------------------- |
| `wrap()`    | Break text into lines |
| `fill()`    | Wrap text as a string |
| `shorten()` | Shorten text          |
| `indent()`  | Add prefix            |
| `dedent()`  | Remove indentation    |

```