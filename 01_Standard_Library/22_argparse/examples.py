"""
examples.py
Module: argparse

"""

import argparse
# -----------------------------------------
# Create Argument Parser
# -----------------------------------------
parser = argparse.ArgumentParser(
    description="Argparse Module Examples"
)

# -----------------------------------------
# 1. Positional Argument
# -----------------------------------------
parser.add_argument(
    "name",
    help="Enter your name"
)

# -----------------------------------------
# 2. Optional Argument
# -----------------------------------------
parser.add_argument(
    "--city",
    help="Enter your city"
)

# -----------------------------------------
# 3. Argument with Data Type
# -----------------------------------------
parser.add_argument(
    "--age",
    type=int,
    help="Enter your age"
)

# -----------------------------------------
# 4. Default Value
# -----------------------------------------
parser.add_argument(
    "--country",
    default="India",
    help="Enter your country"
)

# -----------------------------------------
# 5. Choices
# -----------------------------------------
parser.add_argument(
    "--department",
    choices=["CSE", "ECE", "ME", "CE"],
    help="Select your department"
)

# -----------------------------------------
# 6. Boolean Flag
# -----------------------------------------
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Display additional information"
)

# -----------------------------------------
# Parse Arguments
# -----------------------------------------
args = parser.parse_args()

# -----------------------------------------
# Display Values
# -----------------------------------------
print("\n" + "=" * 20)
print("  ARGPARSE RESULTS")
print("=" * 20)
print("Name       :", args.name)
print("Age        :", args.age)
print("City       :", args.city)
print("Country    :", args.country)
print("Department :", args.department)
print("Verbose    :", args.verbose)

# -----------------------------------------
# Using Boolean Flag
# -----------------------------------------
if args.verbose:
    print("\nVerbose mode is enabled.")
    print("All argument details are displayed.")