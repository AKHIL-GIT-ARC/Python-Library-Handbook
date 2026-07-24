# logging Module Cheat Sheet

## Import

```python
import logging
```

The `logging` module is used to record events, errors, warnings, and debugging information while a program is running.

---

# Logging Levels

| Level | Purpose |
|--------|---------|
| `DEBUG` | Detailed debugging information |
| `INFO` | General program information |
| `WARNING` | Something unexpected happened |
| `ERROR` | An operation failed |
| `CRITICAL` | Serious error; application may stop |

---

# 1. basicConfig()

**Purpose:** Configures the logging system.

**Syntax**

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s : %(message)s"
)
```

**Example**

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Program Started")
```

**Output**

```text
INFO:root:Program Started
```

---

# 2. debug()

**Purpose:** Logs debugging information.

**Example**

```python
logging.debug("Checking variable values")
```

**Output**

```text
DEBUG:root:Checking variable values
```

---

# 3. info()

**Purpose:** Logs general application events.

**Example**

```python
logging.info("User logged in")
```

**Output**

```text
INFO:root:User logged in
```

---

# 4. warning()

**Purpose:** Logs warning messages.

**Example**

```python
logging.warning("Low battery")
```

**Output**

```text
WARNING:root:Low battery
```

---

# 5. error()

**Purpose:** Logs error messages.

**Example**

```python
logging.error("File not found")
```

**Output**

```text
ERROR:root:File not found
```

---

# 6. critical()

**Purpose:** Logs serious system errors.

**Example**

```python
logging.critical("Database crashed")
```

**Output**

```text
CRITICAL:root:Database crashed
```

---

# 7. exception()

**Purpose:** Logs an exception along with its traceback.

**Example**

```python
try:
    10 / 0
except ZeroDivisionError:
    logging.exception("Division by zero")
```

**Output**

```text
ERROR:root:Division by zero
Traceback (most recent call last):
...
```

---

# 8. getLogger()

**Purpose:** Creates a custom logger.

**Syntax**

```python
logger = logging.getLogger("LoggerName")
```

**Example**

```python
logger = logging.getLogger("StudentLogger")
logger.info("Student Added")
```

---

# 9. FileHandler

**Purpose:** Saves log messages to a file.

**Example**

```python
handler = logging.FileHandler("app.log")
```

Creates a file named:

```text
app.log
```

---

# 10. Formatter

**Purpose:** Customizes the appearance of log messages.

**Example**

```python
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
```

Example Output

```text
2026-07-25 10:15:30 - INFO - Program Started
```

---

# 11. setLevel()

**Purpose:** Controls which log levels are displayed.

**Example**

```python
logging.getLogger().setLevel(logging.WARNING)
```

Now only these messages are shown:

- WARNING
- ERROR
- CRITICAL

---

# Common Format Variables

| Placeholder | Meaning |
|-------------|---------|
| `%(asctime)s` | Date & Time |
| `%(levelname)s` | Log Level |
| `%(message)s` | Log Message |
| `%(name)s` | Logger Name |
| `%(filename)s` | File Name |
| `%(lineno)d` | Line Number |

---

# Logging Levels Order

```text
DEBUG
   ↓
INFO
   ↓
WARNING
   ↓
ERROR
   ↓
CRITICAL
```

Higher levels indicate more serious events.

---

# File Logging

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)
```

All log messages are saved to `app.log`.

---

# Custom Logger Example

```python
logger = logging.getLogger("Student")
logger.info("Student Added")
```

Useful for large projects with multiple modules.

---

# Exception Logging

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    logging.exception("Error occurred")
```

Automatically logs the complete traceback.

---

# Logging vs print()

| `logging` | `print()` |
|------------|-----------|
| Multiple log levels | Only prints text |
| Save to file | Console only |
| Professional debugging | Simple output |
| Custom formatting | No formatting options |
| Production-ready | Mostly for learning/testing |

---

# Best Practices
- Use `logging` instead of `print()` in production.
- Choose the correct logging level.
- Include timestamps in log messages.
- Store logs in files for later analysis.
- Use custom loggers in large applications.
- Log exceptions with `logging.exception()`.

---

# Common Mistakes

❌ Forgetting to configure logging.

```python
logging.info("Hello")
```

May not display as expected.

---

❌ Using `print()` for debugging.

```python
print(value)
```

Prefer:

```python
logging.debug(value)
```

---

❌ Logging sensitive information.

```python
logging.info(password)
```

Never log passwords, API keys, or personal information.

---

❌ Using the wrong log level.

Use:
- `DEBUG` → Development
- `INFO` → Normal events
- `WARNING` → Potential issues
- `ERROR` → Failures
- `CRITICAL` → Severe failures

---

# Real-World Uses

✅ Backend APIs

✅ Banking Systems

✅ DevOps Scripts

✅ Automation Projects

✅ Cybersecurity Tools

✅ Machine Learning Pipelines

✅ Desktop Applications

---

# Quick Revision

| Need | Function / Class |
|------|------------------|
| Configure logging | `basicConfig()` |
| Debug message | `debug()` |
| Information | `info()` |
| Warning | `warning()` |
| Error | `error()` |
| Critical error | `critical()` |
| Exception logging | `exception()` |
| Create custom logger | `getLogger()` |
| Save logs to file | `FileHandler` |
| Customize format | `Formatter` |
| Change log level | `setLevel()` |

---

# Interview Tip

One of the most common Python interview questions is:

**Why is `logging` preferred over `print()`?**

**Answer:**

`logging` provides multiple severity levels, supports saving messages to files, allows custom formatting, and is suitable for debugging and monitoring production applications. In contrast, `print()` simply displays text on the console and lacks these advanced features.