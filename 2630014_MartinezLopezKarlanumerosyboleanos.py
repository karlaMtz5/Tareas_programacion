
# ================================================================
# COVER PAGE
# Student: Karla Lizeth Martinez Lopez
# Student ID: 2630014
# Group: IM 1-2
# Course: Programming Methodologies
# Assignment: Integer, Float, and Boolean Data Types
# File: 2630014_MartinezLopezKarlanumerosyboleanos.py
# ================================================================

# ================================================================
# EXECUTIVE SUMMARY
# ================================================================
# The int type stores whole numbers, while float stores decimal values.
# Integers are useful for counters, quantities, and whole-number data.
# Floats are useful for temperatures, salaries, weights, and averages.
# A Boolean is a logical value that can be True or False.
# Comparisons such as >=, ==, and < produce Boolean results.
# Input validation helps prevent invalid values and calculation errors.
# Division by zero must be avoided to ensure the program runs correctly.
# This program presents six problems using numeric types and Booleans.
# Each problem includes inputs, outputs, validations, and three test cases.
# The examples demonstrate calculations and decisions using Python.

# ================================================================
# PRINCIPLES AND GOOD PRACTICES
# ================================================================
# 1. Use int for whole-number counters and float for decimal quantities.
# 2. Store intermediate results in variables to avoid repeated expressions.
# 3. Validate inputs before performing calculations.
# 4. Reject negative hours, invalid salaries, and impossible measurements.
# 5. Use descriptive variable names and clear messages in English.
# 6. Interpret True as a condition being satisfied and False otherwise.
# 7. Use and when all conditions must be true.
# 8. Use or when at least one condition must be true.
# 9. Catch conversion errors and prevent division by zero.
# 10. Keep each problem in a separate function for easier maintenance.

import math


# ================================================================
# HELPER FUNCTIONS
# ================================================================

def read_finite_float(prompt):
    """Read a finite floating-point number."""
    value = float(input(prompt))

    if not math.isfinite(value):
        raise ValueError("The number must be finite.")

    return value


def read_integer(prompt):
    """Read an integer."""
    return int(input(prompt))


def display_boolean(value):
    """Display a Boolean using lowercase true or false."""
    return str(value).lower()


# ================================================================
# PROBLEM 1: TEMPERATURE CONVERTER AND RANGE FLAG
# ================================================================
# Description:
# Convert a Celsius temperature to Fahrenheit and Kelvin.
# Determine whether the Celsius temperature is at least 30 degrees.
#
# Inputs:
# - temp_c: finite float representing degrees Celsius.
#
# Outputs:
# - Fahrenheit, Kelvin, and High temperature.
#
# Validations:
# - The input must be numeric and finite.
# - Kelvin must be greater than or equal to zero.
#
# Test cases:
# 1) Normal: temp_c = 35.0
#    Expected: Fahrenheit = 95.0, Kelvin = 308.15,
#    High temperature = true.
# 2) Border: temp_c = 30.0
#    Expected: Fahrenheit = 86.0, Kelvin = 303.15,
#    High temperature = true.
# 3) Error: temp_c = -274.0
#    Expected: Error: invalid input.
#
# Flowchart description:
# Read Celsius -> Validate -> Convert -> Compare -> Display results.
# ================================================================

def problem_1():
    try:
        temp_c = read_finite_float("Enter temperature in Celsius: ")

        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15

        if temp_k < 0.0:
            print("Error: invalid input")
            return

        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print(
            "High temperature:",
            display_boolean(is_high_temperature)
        )

    except (ValueError, OverflowError):
        print("Error: invalid input")


# ================================================================
# PROBLEM 2: WORK HOURS AND OVERTIME PAYMENT
# ================================================================
# Description:
# Calculate regular pay and overtime pay for a workweek.
# Hours above 40 are paid at 150 percent of the normal hourly rate.
#
# Inputs:
# - hours_worked: finite float greater than or equal to zero.
# - hourly_rate: finite float greater than zero.
#
# Outputs:
# - Regular pay, overtime pay, total pay, and Has overtime.
#
# Validations:
# - Hours must be nonnegative.
# - Hourly rate must be positive.
# - Both inputs must be finite numeric values.
#
# Test cases:
# 1) Normal: hours_worked = 45, hourly_rate = 100
#    Expected: Regular pay = 4000, overtime pay = 750,
#    total pay = 4750, Has overtime = true.
# 2) Border: hours_worked = 40, hourly_rate = 100
#    Expected: Regular pay = 4000, overtime pay = 0,
#    total pay = 4000, Has overtime = false.
# 3) Error: hours_worked = -2, hourly_rate = 100
#    Expected: Error: invalid input.
#
# Flowchart description:
# Read hours and rate -> Validate -> Separate hours ->
# Calculate payments -> Display results.
# ================================================================

def problem_2():
    try:
        hours_worked = read_finite_float("Enter weekly hours worked: ")
        hourly_rate = read_finite_float("Enter hourly rate: ")

        if hours_worked < 0 or hourly_rate <= 0:
            print("Error: invalid input")
            return

        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(hours_worked - 40.0, 0.0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40.0

        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        print("Has overtime:", display_boolean(has_overtime))

    except (ValueError, OverflowError):
        print("Error: invalid input")


# ================================================================
# PROBLEM 3: DISCOUNT ELIGIBILITY WITH BOOLEANS
# ================================================================
# Description:
# Determine whether a customer qualifies for a 10 percent discount.
# Eligibility requires student status, senior status, or a purchase
# total of at least 1000.00.
#
# Inputs:
# - purchase_total: finite float greater than or equal to zero.
# - is_student_text: YES or NO.
# - is_senior_text: YES or NO.
#
# Outputs:
# - Discount eligible and Final total.
#
# Validations:
# - Purchase total must be nonnegative.
# - Student and senior responses must be YES or NO.
# - Text responses are normalized to uppercase.
#
# Test cases:
# 1) Normal: purchase_total = 500, student = YES, senior = NO
#    Expected: Discount eligible = true, Final total = 450.
# 2) Border: purchase_total = 1000, student = NO, senior = NO
#    Expected: Discount eligible = true, Final total = 900.
# 3) Error: purchase_total = 100, student = MAYBE, senior = NO
#    Expected: Error: invalid input.
#
# Flowchart description:
# Read purchase and statuses -> Validate -> Determine eligibility ->
# Apply discount if eligible -> Display results.
# ================================================================

def problem_3():
    try:
        purchase_total = read_finite_float("Enter purchase total: ")
        is_student_text = input("Is the customer a student? (YES/NO): ")
        is_senior_text = input("Is the customer a senior? (YES/NO): ")

        is_student_text = is_student_text.strip().upper()
        is_senior_text = is_senior_text.strip().upper()

        if purchase_total < 0:
            print("Error: invalid input")
            return

        if is_student_text not in ("YES", "NO"):
            print("Error: invalid input")
            return

        if is_senior_text not in ("YES", "NO"):
            print("Error: invalid input")
            return

        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = (
            is_student
            or is_senior
            or purchase_total >= 1000.0
        )

        if discount_eligible:
            final_total = purchase_total * 0.90
        else:
            final_total = purchase_total

        print(
            "Discount eligible:",
            display_boolean(discount_eligible)
        )
        print("Final total:", round(final_total, 2))

    except (ValueError, OverflowError):
        print("Error: invalid input")


# ================================================================
# PROBLEM 4: BASIC STATISTICS OF THREE INTEGERS
# ================================================================
# Description:
# Read three integers and calculate their sum and average.
# Also determine the maximum, minimum, and whether all are even.
#
# Inputs:
# - n1, n2, n3: integers; negative values are allowed.
#
# Outputs:
# - Sum, Average, Max, Min, and All even.
#
# Validations:
# - All three inputs must be valid integers.
# - No additional range restrictions apply.
#
# Test cases:
# 1) Normal: n1 = 2, n2 = 4, n3 = 6
#    Expected: Sum = 12, Average = 4, Max = 6,
#    Min = 2, All even = true.
# 2) Border: n1 = 0, n2 = 0, n3 = 0
#    Expected: Sum = 0, Average = 0, Max = 0,
#    Min = 0, All even = true.
# 3) Error: n1 = 2, n2 = hello, n3 = 6
#    Expected: Error: invalid input.
#
# Flowchart description:
# Read three integers -> Validate -> Calculate statistics ->
# Check parity -> Display results.
# ================================================================

def problem_4():
    try:
        n1 = read_integer("Enter the first integer: ")
        n2 = read_integer("Enter the second integer: ")
        n3 = read_integer("Enter the third integer: ")

        sum_value = n1 + n2 + n3
        average_value = sum_value / 3
        max_value = max(n1, n2, n3)
        min_value = min(n1, n2, n3)

        all_even = (
            n1 % 2 == 0
            and n2 % 2 == 0
            and n3 % 2 == 0
        )

        print("Sum:", sum_value)
        print("Average:", round(average_value, 2))
        print("Max:", max_value)
        print("Min:", min_value)
        print("All even:", display_boolean(all_even))

    except (ValueError, OverflowError):
        print("Error: invalid input")


# ================================================================
# PROBLEM 5: LOAN ELIGIBILITY (INCOME AND DEBT RATIO)
# ================================================================
# Description:
# Determine whether an applicant meets three loan eligibility rules.
# The applicant needs sufficient income, a debt ratio of at most 0.4,
# and a credit score of at least 650.
#
# Inputs:
# - monthly_income: finite float greater than zero.
# - monthly_debt: finite float greater than or equal to zero.
# - credit_score: nonnegative integer.
#
# Outputs:
# - Debt ratio and Eligible.
#
# Validations:
# - Income must be greater than zero to prevent division by zero.
# - Debt and credit score must be nonnegative.
# - Inputs must be valid numeric values.
#
# Test cases:
# 1) Normal: income = 10000, debt = 3000, score = 700
#    Expected: Debt ratio = 0.3, Eligible = true.
# 2) Border: income = 8000, debt = 3200, score = 650
#    Expected: Debt ratio = 0.4, Eligible = true.
# 3) Error: income = 0, debt = 100, score = 700
#    Expected: Error: invalid input.
#
# Flowchart description:
# Read income, debt, and score -> Validate -> Calculate ratio ->
# Evaluate all eligibility conditions -> Display results.
# ================================================================

def problem_5():
    try:
        monthly_income = read_finite_float("Enter monthly income: ")
        monthly_debt = read_finite_float("Enter monthly debt payments: ")
        credit_score = read_integer("Enter credit score: ")

        if (
            monthly_income <= 0
            or monthly_debt < 0
            or credit_score < 0
        ):
            print("Error: invalid input")
            return

        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print("Debt ratio:", round(debt_ratio, 4))
        print("Eligible:", display_boolean(eligible))

    except (ValueError, OverflowError):
        print("Error: invalid input")


# ================================================================
# PROBLEM 6: BODY MASS INDEX (BMI) AND CATEGORY FLAG
# ================================================================
# Description:
# Calculate Body Mass Index using weight in kilograms and height
# in meters. Classify the result as underweight, normal, or overweight.
#
# Inputs:
# - weight_kg: finite float greater than zero.
# - height_m: finite float greater than zero.
#
# Outputs:
# - BMI, Underweight, Normal, and Overweight.
#
# Validations:
# - Weight and height must be greater than zero.
# - Inputs must be finite numeric values.
#
# Test cases:
# 1) Normal: weight = 70, height = 1.75
#    Expected: BMI = 22.86, Underweight = false,
#    Normal = true, Overweight = false.
# 2) Border: weight = 56.7, height = 1.75
#    Expected: BMI is approximately 18.51, Normal = true.
# 3) Error: weight = 70, height = 0
#    Expected: Error: invalid input.
#
# Flowchart description:
# Read weight and height -> Validate -> Calculate BMI ->
# Evaluate category ranges -> Display results.
# ================================================================

def problem_6():
    try:
        weight_kg = read_finite_float("Enter weight in kilograms: ")
        height_m = read_finite_float("Enter height in meters: ")

        if weight_kg <= 0 or height_m <= 0:
            print("Error: invalid input")
            return

        bmi = weight_kg / (height_m * height_m)

        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", round(bmi, 2))
        print("Underweight:", display_boolean(is_underweight))
        print("Normal:", display_boolean(is_normal))
        print("Overweight:", display_boolean(is_overweight))

    except (ValueError, OverflowError, ZeroDivisionError):
        print("Error: invalid input")


# ================================================================
# MAIN MENU
# ================================================================
# Select a problem from 1 to 6, or enter 0 to exit.
# Each selection calls its corresponding function.
# Invalid menu entries display an error message.
# ================================================================

def main():
    problems = {
        "1": problem_1,
        "2": problem_2,
        "3": problem_3,
        "4": problem_4,
        "5": problem_5,
        "6": problem_6,
    }

    while True:
        print("\n===== PYTHON PROGRAMMING ASSIGNMENT =====")
        print("1. Temperature converter")
        print("2. Work hours and overtime payment")
        print("3. Discount eligibility")
        print("4. Basic statistics")
        print("5. Loan eligibility")
        print("6. Body Mass Index (BMI)")
        print("0. Exit")

        choice = input("Select a problem (0-6): ").strip()

        if choice == "0":
            print("Program finished.")
            break

        if choice not in problems:
            print("Error: invalid input")
            continue

        problems[choice]()


if __name__ == "__main__":
    main()


# ================================================================
# CONCLUSIONS
# ================================================================
# Integers and floating-point numbers are both necessary for calculations.
# Integers represent whole quantities, while floats represent decimal values.
# Comparisons generate Boolean values that help programs make decisions.
# The if statement executes different actions according to those values.
# Input validation prevents invalid ranges and division-by-zero errors.
# The and, or, and not operators allow conditions to be combined logically.
# These techniques are useful in payroll, discounts, loans, and BMI programs.
# Separating programs into functions improves clarity, testing, and reuse.

# ================================================================
# REFERENCES
# ================================================================
# 1. Python Software Foundation, "Built-in Types."
#    https://docs.python.org/3/library/stdtypes.html
#
# 2. Python Software Foundation, "Built-in Functions."
#    https://docs.python.org/3/library/functions.html
#
# 3. Python Software Foundation, "Errors and Exceptions."
#    https://docs.python.org/3/tutorial/errors.html
#
# 4. Python Software Foundation, "More Control Flow Tools."
#    https://docs.python.org/3/tutorial/controlflow.html
#
# 5. Python Software Foundation, "An Informal Introduction to Python."
#    https://docs.python.org/3/tutorial/introduction.html
#
# 6. Python Software Foundation, "The Python Tutorial."
#    https://docs.python.org/3/tutorial/
# ================================================================
