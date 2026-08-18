# CSV — Interview Questions

## 1. What is CSV?

CSV stands for **Comma-Separated Values**. It is a simple format used to store tabular data.

---

## 2. Which module is used to work with CSV files?

Python provides the built-in `csv` module.

    import csv

---

## 3. What does `csv.reader()` do?

It reads CSV rows and returns each row as a list.

    reader = csv.reader(file)

---

## 4. What does `csv.writer()` do?

It writes lists of data into a CSV file.

    writer = csv.writer(file)
    writer.writerow(["Akhil", 20, "CSE"])

---

## 5. What is the difference between `writerow()` and `writerows()`?

| Method | Purpose |
|---|---|
| `writerow()` | Writes one row |
| `writerows()` | Writes multiple rows |

---

## 6. What is `DictReader`?

`DictReader` reads each CSV row as a dictionary using the header names as keys.

    reader = csv.DictReader(file)

---

## 7. What is `DictWriter`?

`DictWriter` writes dictionaries into a CSV file.

    writer = csv.DictWriter(file, fieldnames=["name", "age"])

---

## 8. Why is `newline=""` used?

It helps prevent unwanted blank lines when reading or writing CSV files, especially on Windows.

    open("students.csv", "w", newline="")

---

## 9. What does `writeheader()` do?

It writes the field names as the first row of the CSV file.

    writer.writeheader()

---

## 10. What are common CSV file modes?

| Mode | Purpose |
|---|---|
| `"r"` | Read |
| `"w"` | Write / overwrite |
| `"a"` | Append |

---

## Quick Revision

| Concept | Remember |
|---|---|
| `csv` | Python CSV module |
| `reader()` | Read rows as lists |
| `writer()` | Write rows |
| `writerow()` | One row |
| `writerows()` | Multiple rows |
| `DictReader` | Read as dictionaries |
| `DictWriter` | Write dictionaries |
| `writeheader()` | Write column names |
| `newline=""` | Avoid blank lines |