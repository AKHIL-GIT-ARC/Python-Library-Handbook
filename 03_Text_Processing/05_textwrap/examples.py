# Textwrap - Examples

import textwrap

# 1. wrap()
text = "Python is easy to learn"
print("wrap():")
print(textwrap.wrap(text, width=10))


# 2. fill()
print("\nfill():")
print(textwrap.fill(text, width=10))


# 3. shorten()
long_text = "Python is a powerful programming language"
print("\nshorten():")
print(textwrap.shorten(long_text, width=25))


# 4. indent()
text = "Hello\nPython"
print("\nindent():")
print(textwrap.indent(text, "> "))


# 5. dedent()
text = """
    Hello
    Python
"""
print("\ndedent():")
print(textwrap.dedent(text))


# 6. Custom Width
text = "Python makes programming simple and enjoyable"
print("Custom width:")
print(textwrap.fill(text, width=20))