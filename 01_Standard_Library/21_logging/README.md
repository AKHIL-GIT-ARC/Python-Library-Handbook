# logging Module

The `logging` module is a built-in Python library that provides a flexible way to record events, errors, warnings, and debugging information while a program is running.

Unlike `print()`, the `logging` module allows you to categorize messages by severity, save them to files, and customize their format, making it essential for professional software development.

---

# Why Use logging?

Using `print()`:

```python
print("Application Started")
```

Output

```python
Application Started
```

Using `logging`:

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Application Started")
```

Output

```python
INFO:root:Application Started
```

Logging provides more useful information, including the severity level and optional timestamps.

---

# Importing the Module

```python
import logging
```

---

# Functions and Classes Covered

| Function / Class | Purpose |
|------------------|---------|
| `basicConfig()` | Configure logging |
| `debug()` | Log debugging messages |
| `info()` | Log general information |
| `warning()` | Log warning messages |
| `error()` | Log error messages |
| `critical()` | Log critical errors |
| `exception()` | Log exceptions with traceback |
| `getLogger()` | Create a custom logger |
| `FileHandler` | Save logs to a file |
| `Formatter` | Customize log message format |

---

# Why Learn logging?

The `logging` module is widely used in:
- Backend development
- Web applications
- APIs
- Automation scripts
- Banking software
- Cloud applications
- DevOps
- Cybersecurity tools
- Machine learning pipelines

---

# Advantages

- Better than `print()` for debugging
- Supports multiple log levels
- Saves logs to files
- Helps identify errors quickly
- Customizable log formats
- Built into Python

---

# Logging Levels

| Level | Purpose |
|--------|---------|
| `DEBUG` | Detailed debugging information |
| `INFO` | General application events |
| `WARNING` | Something unexpected happened |
| `ERROR` | An operation failed |
| `CRITICAL` | Serious error; program may stop |

---

# Common Operations

## Basic Configuration

```python
import logging
logging.basicConfig(level=logging.INFO)
```

---

## Debug Message

```python
logging.debug("Debug message")
```

---

## Information Message

```python
logging.info("Program started")
```

---

## Warning Message

```python
logging.warning("Low disk space")
```

---

## Error Message

```python
logging.error("File not found")
```

---

## Critical Message

```python
logging.critical("Database connection lost")
```

---

## Logging to a File

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)
```

All log messages are saved in `app.log`.

---

## Custom Log Format

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

Example Output

```text
2026-08-15 10:30:22 - INFO - Program Started
```

---

## Logging Exceptions

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    logging.exception("Division by zero")
```

The traceback is automatically included in the log.

---

## Creating a Custom Logger

```python
logger = logging.getLogger("MyLogger")
logger.info("Custom logger created")
```

---

# Real-World Applications

## Backend Development

- API request logs
- Server monitoring
- Error tracking

---

## Banking

- Transaction logs
- Audit records
- Security monitoring

---

## DevOps

- Deployment logs
- System monitoring
- Automation scripts

---

## Machine Learning

- Model training logs
- Dataset processing
- Performance tracking

---

## Cybersecurity

- Login attempts
- Attack detection
- System audits

---

# Prerequisites

Before learning this module, you should know:
- Variables
- Functions
- Exception handling
- File handling
- Python imports

---

# Mini Project

## Student Management Logger

Features:

- Add Student
- Update Student
- Delete Student
- Record every action
- Save logs to a file
- View log history

---

# Best Practices

- Use `logging` instead of `print()` in production code.
- Choose the correct logging level.
- Store logs in files for future analysis.
- Include timestamps in log messages.
- Log exceptions using `logging.exception()`.
- Create custom loggers for large projects.

---

# Common Mistakes

- Using `print()` for debugging in production.
- Logging sensitive information like passwords.
- Using the wrong logging level.
- Forgetting to configure logging before use.
- Ignoring log files during debugging.

---

# Quick Revision

| Need | Use |
|------|-----|
| Configure logging | `basicConfig()` |
| Debug message | `debug()` |
| Information | `info()` |
| Warning | `warning()` |
| Error | `error()` |
| Critical error | `critical()` |
| Log exceptions | `exception()` |
| Custom logger | `getLogger()` |
| Save logs | `FileHandler` |
| Custom format | `Formatter` |

---
