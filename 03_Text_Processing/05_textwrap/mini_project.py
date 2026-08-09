# Mini Project - Text Formatter

import textwrap

text = input("Enter a long sentence: ")

print("\n--- Formatted Text ---")

print("\nWrapped Text:")
print(textwrap.fill(text, width=40))

print("\nShortened Text:")
print(textwrap.shorten(text, width=30))

print("\nIndented Text:")
print(textwrap.indent(textwrap.fill(text, width=40), "> "))