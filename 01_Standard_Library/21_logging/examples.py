"""
examples.py
Module: logging

"""
import logging

# ==========================================================
# Example 1: Basic Configuration
# ==========================================================

print("\n========== Example 1: Basic Configuration ==========")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s : %(message)s"
)
logging.info("Logging configured successfully.")

# ==========================================================
# Example 2: Debug Message
# ==========================================================

print("\n========== Example 2: DEBUG ==========")
logging.debug("This is a debug message.")

# ==========================================================
# Example 3: Information Message
# ==========================================================

print("\n========== Example 3: INFO ==========")
logging.info("Application started successfully.")

# ==========================================================
# Example 4: Warning Message
# ==========================================================

print("\n========== Example 4: WARNING ==========")
logging.warning("Low disk space detected.")

# ==========================================================
# Example 5: Error Message
# ==========================================================

print("\n========== Example 5: ERROR ==========")
logging.error("Unable to open the requested file.")

# ==========================================================
# Example 6: Critical Message
# ==========================================================

print("\n========== Example 6: CRITICAL ==========")
logging.critical("Database connection lost!")

# ==========================================================
# Example 7: Logging Exception
# ==========================================================

print("\n========== Example 7: Exception Logging ==========")
try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Division by zero occurred.")

# ==========================================================
# Example 8: Custom Logger
# ==========================================================

print("\n========== Example 8: Custom Logger ==========")
logger = logging.getLogger("StudentLogger")
logger.info("Student record added.")

# ==========================================================
# Example 9: Different Log Levels
# ==========================================================

print("\n========== Example 9: Logging Levels ==========")
logging.debug("Debug Level")
logging.info("Info Level")
logging.warning("Warning Level")
logging.error("Error Level")
logging.critical("Critical Level")

# ==========================================================
# Example 10: Logging to a File
# ==========================================================

print("\n========== Example 10: File Logging ==========")
file_logger = logging.getLogger("FileLogger")
file_handler = logging.FileHandler("app.log")
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
file_logger.addHandler(file_handler)
file_logger.setLevel(logging.INFO)
file_logger.info("Application Started")
file_logger.warning("Memory usage is increasing")
file_logger.error("Unable to connect to server")
print("Log messages saved to app.log")

# ==========================================================
# Example 11: Logging Variable Values
# ==========================================================

print("\n========== Example 11: Variables ==========")
username = "Akhil"
age = 19
logging.info(f"User: {username}, Age: {age}")

# ==========================================================
# Example 12: Logging Inside Functions
# ==========================================================

print("\n========== Example 12: Functions ==========")
def calculate_square(number):
    logging.info(f"Calculating square of {number}")
    return number ** 2
result = calculate_square(8)
print("Square =", result)

# ==========================================================
# Example 13: Using Logger Name
# ==========================================================

print("\n========== Example 13: Logger Name ==========")
student_logger = logging.getLogger("StudentModule")
student_logger.info("Student login successful.")

# ==========================================================
# Example 14: Disable Lower-Level Logs
# ==========================================================

print("\n========== Example 14: Log Level Filtering ==========")
logging.getLogger().setLevel(logging.WARNING)
logging.debug("This will NOT be shown.")
logging.info("This will NOT be shown.")
logging.warning("Only warning and above are shown.")
logging.error("Error message.")
logging.critical("Critical message.")

# ==========================================================
# Example 15: Summary
# ==========================================================

print("\n========== Summary ==========")
print("""
Topics Covered
✓ basicConfig()
✓ debug()
✓ info()
✓ warning()
✓ error()
✓ critical()
✓ exception()
✓ getLogger()
✓ FileHandler
✓ Formatter
✓ Log Levels
✓ File Logging
✓ Logging Variables
✓ Logging Inside Functions
""")