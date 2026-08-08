# Mini Project - Contact Extractor

import re

text = """
Contact us:
Email: student@example.com
Phone: 9876543210
Email: admin@python.org
Phone: 9123456780
"""

emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
phones = re.findall(r"\b\d{10}\b", text)
print("----- Contact Extractor -----")
print("\nEmails:")
for email in emails:
    print("-", email)
print("\nPhone Numbers:")
for phone in phones:
    print("-", phone)