# CSV in Python

CSV (Comma-Separated Values) is a simple format used to store tabular data.

Python provides the built-in `csv` module for reading and writing CSV files.

    import csv

---

## CSV Structure

Example:

    name,age,course
    Akhil,20,CSE
    Rahul,21,IT

Each line represents a row, and commas separate the values.

---

## `csv.reader()`

Reads rows from a CSV file.

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

Output:

    ['name', 'age', 'course']
    ['Akhil', '20', 'CSE']
    ['Rahul', '21', 'IT']

---

## `csv.writer()`

Writes rows to a CSV file.

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["name", "age", "course"])
        writer.writerow(["Akhil", 20, "CSE"])

---

## `writerows()`

Writes multiple rows at once.

    rows = [
        ["Akhil", 20, "CSE"],
        ["Rahul", 21, "IT"]
    ]

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

---

## `csv.DictReader`

Reads CSV rows as dictionaries.

    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row["name"], row["course"])

Output:

    Akhil CSE
    Rahul IT

---

## `csv.DictWriter`

Writes dictionaries to a CSV file.

    with open("students.csv", "w", newline="") as file:
        fields = ["name", "age", "course"]

        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()

        writer.writerow({
            "name": "Akhil",
            "age": 20,
            "course": "CSE"
        })

---

## `newline=""`

Use `newline=""` when opening CSV files.

    open("students.csv", "r", newline="")

This helps avoid unwanted blank lines, especially on Windows.

---

## Common CSV Tools

| Tool | Purpose |
|---|---|
| `csv.reader()` | Read rows as lists |
| `csv.writer()` | Write rows |
| `writerow()` | Write one row |
| `writerows()` | Write multiple rows |
| `csv.DictReader` | Read rows as dictionaries |
| `csv.DictWriter` | Write dictionaries |
| `writeheader()` | Write column names |

---

## Key Points

- CSV stores tabular data in plain text.
- Use the built-in `csv` module.
- `reader()` returns rows as lists.
- `DictReader` returns rows as dictionaries.
- `writer()` writes lists.
- `DictWriter` writes dictionaries.
- Use `newline=""` when opening CSV files.

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
| `writeheader()` | Write column names |