# CSV — Cheat Sheet

## Import
    import csv
---

## `csv.reader()`

Reads CSV rows as lists.

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

---

## `csv.writer()`

Creates a CSV writer.

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

---

## `writerow()`

Writes one row.

    writer.writerow(["Akhil", 20, "CSE"])

---

## `writerows()`

Writes multiple rows.

    rows = [
        ["Akhil", 20, "CSE"],
        ["Rahul", 21, "IT"]
    ]
    writer.writerows(rows)

---

## `csv.DictReader`

Reads rows as dictionaries.

    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"])

---

## `csv.DictWriter`

Writes dictionaries to CSV.

    fields = ["name", "age", "course"]
    writer = csv.DictWriter(file, fieldnames=fields)

---

## `writeheader()`

Writes column names.

    writer.writeheader()

---

## File Modes

| Mode | Purpose |
|---|---|
| `"r"` | Read |
| `"w"` | Write / overwrite |
| `"a"` | Append |

---

## Common Tools

| Tool | Purpose |
|---|---|
| `reader()` | Read rows as lists |
| `writer()` | Write rows |
| `writerow()` | Write one row |
| `writerows()` | Write multiple rows |
| `DictReader` | Read dictionaries |
| `DictWriter` | Write dictionaries |
| `writeheader()` | Write column names |

---

## Key Points

- CSV stores tabular data as plain text.
- Use Python's built-in `csv` module.
- `reader()` returns lists.
- `DictReader` returns dictionaries.
- `writer()` writes lists.
- `DictWriter` writes dictionaries.
- Use `newline=""` when opening CSV files.
- Use `with open()` for safe file handling.

---

## Quick Revision

| Method | Remember |
|---|---|
| `reader()` | CSV → Lists |
| `writer()` | Write Lists |
| `writerow()` | One row |
| `writerows()` | Multiple rows |
| `DictReader` | CSV → Dictionaries |
| `DictWriter` | Write Dictionaries |
| `writeheader()` | Column names |