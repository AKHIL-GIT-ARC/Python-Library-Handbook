"""
mini_project.py
Module: enum
Task Status Manager using Python Enum.
"""
from enum import Enum, auto
# -----------------------------------------
# Task Status Enum
# -----------------------------------------
class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELLED = auto()

# -----------------------------------------
# Task Class
# -----------------------------------------
class Task:
    def __init__(
        self,
        title: str,
        status: TaskStatus = TaskStatus.PENDING
    ) -> None:
        self.title = title
        self.status = status

    # -------------------------------------
    # Update Status
    # -------------------------------------
    def update_status(
        self,
        new_status: TaskStatus
    ) -> None:
        self.status = new_status
        print(
            f"Status updated to: "
            f"{self.status.name}"
        )

    # -------------------------------------
    # Display Task
    # -------------------------------------
    def display(self) -> None:
        print("\n" + "=" * 15)
        print(" TASK DETAILS")
        print("=" * 15)
        print("Task   :", self.title)
        print("Status :", self.status.name)

    # -------------------------------------
    # Check Completion
    # -------------------------------------
    def is_completed(self) -> bool:
        return self.status == TaskStatus.COMPLETED

# -----------------------------------------
# Display Available Statuses
# -----------------------------------------
def show_available_statuses() -> None:
    print("\nAvailable Statuses:")
    for status in TaskStatus:
        print(
            status.value,
            "-",
            status.name
        )

# -----------------------------------------
# Create Task
# -----------------------------------------
task = Task(
    "Complete Python Handbook"
)

# -----------------------------------------
# Display Initial Task
# -----------------------------------------
task.display()

# -----------------------------------------
# Show Available Statuses
# -----------------------------------------
show_available_statuses()

# -----------------------------------------
# Update to IN_PROGRESS
# -----------------------------------------
print("\nStarting task...")
task.update_status(
    TaskStatus.IN_PROGRESS
)
task.display()

# -----------------------------------------
# Update to COMPLETED
# -----------------------------------------
print("\nCompleting task...")
task.update_status(
    TaskStatus.COMPLETED
)
task.display()

# -----------------------------------------
# Check Completion
# -----------------------------------------
if task.is_completed():
    print("\nTask completed successfully!")
else:
    print("\nTask is not completed.")