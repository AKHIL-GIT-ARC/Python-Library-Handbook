# Time Module

## Introduction

The `time` module is a built-in Python library that provides functions for working with time. It allows you to pause program execution, measure execution time, work with timestamps, and retrieve local or UTC time.

Unlike the `datetime` module, which focuses on dates and times as objects, the `time` module mainly deals with timestamps and low-level time-related operations.

---

# Why Learn This Library?

The `time` module is widely used in:

- Automation Scripts
- Performance Testing
- Benchmarking Algorithms
- Game Development
- Countdown Timers
- Stopwatch Applications
- Scheduling Tasks
- Delaying Program Execution

---

# Features

- Pause program execution
- Measure execution time
- Work with Unix timestamps
- Access local and UTC time
- Format time into readable strings
- Build timers and stopwatches

---

# Installation

The `time` module is built into Python.

No installation is required.

---

# Import

```python
import time
```

---

# Important Functions

We'll learn:

- time.time()
- time.sleep()
- time.ctime()
- time.localtime()
- time.gmtime()
- time.strftime()
- time.perf_counter()
- time.process_time()
- time.monotonic()

---

# Real-world Applications

The `time` module is commonly used in:

- Measuring program performance
- Benchmarking code
- Delaying tasks
- Stopwatch applications
- Countdown timers
- Automation scripts
- Logging execution time

---

# Advantages

- Easy to use
- Built into Python
- High-precision timing
- Useful for performance measurement
- Supports local and UTC time

---

# Limitations

- Limited date manipulation (use `datetime` instead)
- Not suitable for advanced calendar calculations
- `sleep()` blocks the current thread

---

# Best Practices

- Use `time.sleep()` only when a delay is required.
- Use `time.perf_counter()` to measure execution time.
- Use `datetime` when working with dates.
- Use `time.monotonic()` for elapsed time measurements.

---

# Common Mistakes

- Confusing timestamps with formatted dates.
- Using `time.time()` instead of `perf_counter()` for benchmarking.
- Expecting `sleep()` to pause only part of a program.

---

# Mini Project

## Productivity Timer

A command-line productivity utility that includes a stopwatch, countdown timer, Pomodoro timer, execution time measurement, and a live clock.

Features:

- Stopwatch
- Countdown Timer
- Pomodoro Timer
- Execution Time Calculator

**Concepts Used**

- Functions
- Loops
- User Input
- `time.sleep()`
- `time.perf_counter()`
- `time.strftime()`

---

# References

Official Python Documentation

https://docs.python.org/3/library/time.html