# logging Module Interview Questions

## Beginner Level

### 1. What is the `logging` module?

**Answer:**

The `logging` module is a built-in Python library used to record events, debugging information, warnings, errors, and critical issues while a program is running.

---

### 2. Why is `logging` preferred over `print()`?

**Answer:**

`logging` provides:
- Different log levels
- File logging
- Custom formatting
- Better debugging
- Production-ready monitoring
`print()` only displays text on the console.

---

### 3. How do you import the logging module?

**Answer**

```python
import logging
```

---

### 4. What does `basicConfig()` do?

**Answer:**

It configures the logging system.

Example

```python
logging.basicConfig(level=logging.INFO)
```

---

### 5. Name the five standard logging levels.

**Answer**

```
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

---

## Intermediate Level

### 6. What is the purpose of the `DEBUG` level?

**Answer:**

It records detailed information useful for developers while debugging the program.

Example

```python
logging.debug("Variable x = 10")
```

---

### 7. When should `INFO` be used?

**Answer:**

For normal application events.

Example

```python
logging.info("User logged in")
```

---

### 8. When should `WARNING` be used?

**Answer:**

When something unexpected happens but the program can continue.

Example

```python
logging.warning("Disk space is low")
```

---

### 9. What is the difference between `ERROR` and `CRITICAL`?

| ERROR | CRITICAL |
|--------|----------|
| A specific operation failed | Entire application may fail |
| Program may continue | Program may stop |
| Less severe | Most severe |

---

### 10. What is `logging.exception()`?

**Answer:**

It logs an exception along with its complete traceback.

Example

```python
try:
    10 / 0

except ZeroDivisionError:
    logging.exception("Division by zero")
```

---

## Advanced Level

### 11. What is a custom logger?

**Answer:**

A custom logger is created using:

```python
logging.getLogger()
```

It helps organize logs for different modules.

Example

```python
logger = logging.getLogger("StudentModule")
```

---

### 12. What is a `FileHandler`?

**Answer:**

A `FileHandler` writes log messages to a file instead of displaying them on the console.

Example

```python
handler = logging.FileHandler("app.log")
```

---

### 13. What is the purpose of a `Formatter`?

**Answer:**

A `Formatter` controls the appearance of log messages.

Example

```python
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
```

---

### 14. How can you change the logging level?

**Answer**

```python
logging.getLogger().setLevel(logging.WARNING)
```

Only `WARNING` and higher-level messages will be displayed.

---

### 15. Which placeholder displays the current date and time?

**Answer**

```python
%(asctime)s
```

---

## Scenario-Based Questions

### 16. You want to record every user login in a file. Which logging component should you use?

**Answer**

```python
FileHandler
```

---

### 17. You need to display only warnings and errors. Which method should you use?

**Answer**

```python
setLevel(logging.WARNING)
```

---

### 18. Your application crashes due to an exception. Which function should you use to record the full traceback?

**Answer**

```python
logging.exception()
```

---

### 19. You are working on a large project with separate modules. Which function helps create separate loggers?

**Answer**

```python
logging.getLogger()
```

---

### 20. You want every log message to include the timestamp. Which class should you use?

**Answer**

```python
Formatter
```

---

## Coding Questions

### 21. Configure logging with the INFO level.

```python
logging.basicConfig(level=logging.INFO)
```

---

### 22. Log an information message.

```python
logging.info("Program Started")
```

---

### 23. Log a warning message.

```python
logging.warning("Low Memory")
```

---

### 24. Create a custom logger.

```python
logger = logging.getLogger("MyLogger")
```

---

### 25. Save logs to a file.

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)
```

---

### 26. Log an exception with traceback.

```python
try:
    10 / 0

except ZeroDivisionError:
    logging.exception("Error")
```

---

## Frequently Used Functions

| Function / Class | Purpose |
|------------------|---------|
| `basicConfig()` | Configure logging |
| `debug()` | Debug messages |
| `info()` | Information messages |
| `warning()` | Warning messages |
| `error()` | Error messages |
| `critical()` | Critical messages |
| `exception()` | Log exceptions |
| `getLogger()` | Create custom logger |
| `FileHandler` | Save logs to file |
| `Formatter` | Customize log format |
| `setLevel()` | Change logging level |

---

## Best Practices

- Configure logging before writing log messages.
- Use appropriate logging levels.
- Save logs to files in production.
- Include timestamps in logs.
- Use custom loggers for large applications.
- Never log sensitive information such as passwords or API keys.

---

## Common Mistakes

- Using `print()` instead of `logging`.
- Forgetting to call `basicConfig()`.
- Logging confidential data.
- Using the wrong log level.
- Ignoring log files during debugging.
- Not using `logging.exception()` for exceptions.

---

## Memory Trick

```
basicConfig()
↓

Configure

DEBUG
↓

Development

INFO
↓

Information

WARNING
↓

Potential Problem

ERROR
↓

Operation Failed

CRITICAL
↓

Application Failure

exception()
↓

Traceback

getLogger()
↓

Custom Logger

FileHandler
↓

Save to File

Formatter
↓

Customize Logs
```

---

## Quick Revision

| Need | Function / Class |
|------|------------------|
| Configure logging | `basicConfig()` |
| Debug message | `debug()` |
| Information | `info()` |
| Warning | `warning()` |
| Error | `error()` |
| Critical error | `critical()` |
| Log exception | `exception()` |
| Create custom logger | `getLogger()` |
| Save logs | `FileHandler` |
| Customize format | `Formatter` |
| Change log level | `setLevel()` |

---

## Interview Tip

**Question:** Why is `logging` considered better than `print()` in production applications?

**Answer:**

`logging` allows developers to categorize messages using different severity levels, write logs to files, customize the output format, and track application behavior over time. It is designed for debugging, monitoring, and maintaining production systems, whereas `print()` simply displays text on the console without these capabilities.