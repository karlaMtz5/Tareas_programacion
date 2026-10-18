
# ================================================================
# COVER PAGE
# Student: Karla Lizeth Martinez Lopez
# Student ID: 2630014
# Group: IM 1-2
# Course: Programming Methodologies
# Assignment: String Manipulation in Python
# File: 2630014_MartinezLopezKarla_string_.py
# ================================================================

# ================================================================
# EXECUTIVE SUMMARY
# ================================================================
# A string is a Python data type used to represent text.
# Strings are immutable, which means their characters cannot be
# changed directly; string operations create new strings instead.
# Python supports concatenation, length measurement, slicing,
# searching, splitting, joining, and replacing text.
# Methods such as strip(), lower(), and title() help normalize input.
# Input validation helps detect empty names, invalid emails, and
# incorrect values before processing them.
# This program contains six problems involving string manipulation.
# Each problem documents its inputs, outputs, validations, and tests.
# The examples demonstrate practical text-processing techniques.

# ================================================================
# PRINCIPLES AND GOOD PRACTICES
# ================================================================
# 1. Strings are immutable; operations produce new strings.
# 2. Use strip() to remove leading and trailing whitespace.
# 3. Use lower() or upper() before case-insensitive comparisons.
# 4. Document slices so their purpose is clear.
# 5. Use built-in string methods instead of rewriting basic logic.
# 6. Check that input is not empty before validating its format.
# 7. Use descriptive variable names and clear error messages.
# 8. Define constants for important limits, such as label width.
# 9. Validate numeric input before using it in calculations.
# 10. Test normal, boundary, and invalid inputs.

import math


# ================================================================
# CONSTANTS
# ================================================================

MIN_PALINDROME_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
MIN_LABEL_PRICE = 0.0
LABEL_WIDTH = 30


# ================================================================
# HELPER FUNCTIONS
# ================================================================

def read_finite_float(prompt):
    """Read a finite floating-point number."""
    value = float(input(prompt))

    if not math.isfinite(value):
        raise ValueError("The number must be finite.")

    return value


def display_boolean(value):
    """Return a lowercase Boolean string."""
    return str(value).lower()


# ================================================================
# PROBLEM 1: FULL NAME FORMATTER
# ================================================================
# Description:
# Normalize a full name by removing extra spaces and formatting
# each word in title case. Generate initials separated by periods.
#
# Inputs:
# - full_name: a string containing at least two words.
#
# Outputs:
# - Formatted name.
# - Initials, such as J.C.T.
#
# Validations:
# - The name must not be empty after strip().
# - At least two words must be provided.
#
# Test cases:
# 1) Normal: "  juan   carlos tovar  "
#    Expected: Formatted name: Juan Carlos Tovar
#    Initials: J.C.T.
# 2) Border: "ana lopez"
#    Expected: Formatted name: Ana Lopez
#    Initials: A.L.
# 3) Error: "     "
#    Expected: Error: invalid input
#
# Flowchart description:
# Read name -> Remove extra spaces -> Validate word count ->
# Format name -> Generate initials -> Display results.
# ================================================================

def problem_1():
    full_name = input("Enter the full name: ").strip()

    if not full_name:
        print("Error: invalid input")
        return

    name_parts = full_name.split()

    if len(name_parts) < 2:
        print("Error: invalid input")
        return

    formatted_name = " ".join(name_parts).title()
    initials = ".".join(part[0].upper() for part in name_parts) + "."

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# ================================================================
# PROBLEM 2: SIMPLE EMAIL VALIDATOR
# ================================================================
# Description:
# Check a basic email structure and display its domain if valid.
# The email must contain one @, a nonempty local part, and a
# domain containing a period with text on both sides of that period.
#
# Inputs:
# - email_text: a string representing an email address.
#
# Outputs:
# - Valid email: true or false.
# - Domain when the email is valid.
#
# Validations:
# - The email must not be empty.
# - Exactly one @ must be present.
# - No whitespace is allowed.
# - The local part and domain must not be empty.
# - The domain must contain a correctly positioned period.
#
# Test cases:
# 1) Normal: "student@example.com"
#    Expected: Valid email: true
#    Domain: example.com
# 2) Border: "a@b.co"
#    Expected: Valid email: true
#    Domain: b.co
# 3) Error: "studentexample.com"
#    Expected: Valid email: false
#
# Flowchart description:
# Read email -> Normalize outer spaces -> Check structure ->
# Display validity -> Display domain if valid.
# ================================================================

def problem_2():
    email_text = input("Enter an email address: ").strip()

    if not email_text:
        print("Error: invalid input")
        return

    is_valid_email = False
    domain_part = ""

    if (
        email_text.count("@") == 1
        and not any(character.isspace() for character in email_text)
    ):
        at_index = email_text.find("@")
        local_part = email_text[:at_index]
        domain_part = email_text[at_index + 1:]
        dot_index = domain_part.find(".")

        is_valid_email = (
            bool(local_part)
            and bool(domain_part)
            and dot_index > 0
            and dot_index < len(domain_part) - 1
        )

    print(f"Valid email: {display_boolean(is_valid_email)}")

    if is_valid_email:
        print(f"Domain: {domain_part}")


# ================================================================
# PROBLEM 3: PALINDROME CHECKER
# ================================================================
# Description:
# Determine whether a phrase reads the same forward and backward.
# Spaces and letter case are ignored during the comparison.
#
# Inputs:
# - phrase: a nonempty string with at least three non-space characters.
#
# Outputs:
# - Is palindrome: true or false.
# - Normalized phrase.
#
# Validations:
# - The phrase must not be empty after strip().
# - At least three characters must remain after removing spaces.
#
# Test cases:
# 1) Normal: "Anita lava la tina"
#    Expected: Is palindrome: true
# 2) Border: "aba"
#    Expected: Is palindrome: true
# 3) Error: " a "
#    Expected: Error: invalid input
#
# Flowchart description:
# Read phrase -> Normalize case and spaces -> Validate length ->
# Reverse normalized phrase -> Compare -> Display result.
# ================================================================

def problem_3():
    phrase = input("Enter a phrase: ").strip()

    if not phrase:
        print("Error: invalid input")
        return

    normalized_phrase = phrase.lower().replace(" ", "")

    if len(normalized_phrase) < MIN_PALINDROME_LENGTH:
        print("Error: invalid input")
        return

    is_palindrome = normalized_phrase == normalized_phrase[::-1]

    print(f"Normalized phrase: {normalized_phrase}")
    print(f"Is palindrome: {display_boolean(is_palindrome)}")


# ================================================================
# PROBLEM 4: SENTENCE WORD STATISTICS
# ================================================================
# Description:
# Analyze a sentence and display its word count, first word,
# last word, shortest word, and longest word.
#
# Inputs:
# - sentence: a nonempty string.
#
# Outputs:
# - Word count, first word, last word, shortest word, longest word.
#
# Validations:
# - The sentence must not be empty after strip().
# - Splitting the sentence must produce at least one word.
#
# Test cases:
# 1) Normal: "Python makes learning programming easier"
#    Expected: Word count = 5
#    First word = Python
#    Last word = easier
#    Shortest word = makes or easier? See note below.
#    Longest word = programming
# 2) Border: "Hello"
#    Expected: Word count = 1
#    First word = Hello; Last word = Hello
#    Shortest word = Hello; Longest word = Hello
# 3) Error: "     "
#    Expected: Error: invalid input
#
# Flowchart description:
# Read sentence -> Strip outer spaces -> Split into words ->
# Calculate statistics -> Display results.
# ================================================================

def problem_4():
    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: invalid input")
        return

    words = sentence.split()

    if not words:
        print("Error: invalid input")
        return

    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# ================================================================
# PROBLEM 5: PASSWORD STRENGTH CLASSIFIER
# ================================================================
# Description:
# Classify a password as weak, medium, or strong using its length
# and character types.
#
# Rules:
# - Strong: at least 8 characters, one uppercase letter, one
#   lowercase letter, one digit, and one non-alphanumeric symbol.
# - Weak: fewer than 8 characters, or all characters are lowercase
#   letters, or the password contains only letters.
# - Medium: any other password that does not meet the strong rules.
#
# Inputs:
# - password_input: a nonempty string.
#
# Outputs:
# - Password strength: weak, medium, or strong.
#
# Validations:
# - The password must not be empty.
# - Password length is checked with len().
# - The password is not stripped or changed, because spaces can
#   be part of a password and affect its actual contents.
#
# Test cases:
# 1) Normal: "Hello123!"
#    Expected: Password strength: strong
# 2) Border: "Abc12345"
#    Expected: Password strength: medium
# 3) Error: an empty password
#    Expected: Error: invalid input
#
# Flowchart description:
# Read password -> Check empty input -> Inspect character types ->
# Apply strength rules -> Display classification.
# ================================================================

def problem_5():
    password_input = input("Enter a password: ")

    if password_input == "":
        print("Error: invalid input")
        return

    has_upper = any(character.isupper() for character in password_input)
    has_lower = any(character.islower() for character in password_input)
    has_digit = any(character.isdigit() for character in password_input)
    has_symbol = any(
        not character.isalnum() for character in password_input
    )

    is_strong = (
        len(password_input) >= MIN_PASSWORD_LENGTH
        and has_upper
        and has_lower
        and has_digit
        and has_symbol
    )

    is_all_lowercase = (
        password_input.islower()
        and password_input.isalpha()
    )

    is_letters_only = password_input.isalpha()

    if is_strong:
        password_strength = "strong"
    elif (
        len(password_input) < MIN_PASSWORD_LENGTH
        or is_all_lowercase
        or is_letters_only
    ):
        password_strength = "weak"
    else:
        password_strength = "medium"

    print(f"Password strength: {password_strength}")


# ================================================================
# PROBLEM 6: PRODUCT LABEL FORMATTER
# ================================================================
# Description:
# Create a product label containing its name and positive price.
# The final label is exactly 30 characters long.
# Short labels are padded with spaces; long labels are truncated.
#
# Inputs:
# - product_name: a nonempty product name.
# - price_value: a positive finite numeric value.
#
# Outputs:
# - Label enclosed in quotation marks.
# - Label length, which must equal 30.
#
# Validations:
# - The product name must not be empty after strip().
# - The price must be numeric, finite, and greater than zero.
#
# Test cases:
# 1) Normal: name = "Pen", price = 2.50
#    Expected: a label of exactly 30 characters.
# 2) Border: name = "Notebook", price = 1
#    Expected: a label of exactly 30 characters.
# 3) Error: name = "Pen", price = -1
#    Expected: Error: invalid input.
#
# Flowchart description:
# Read name and price -> Validate -> Format base label ->
# Truncate or pad -> Display label and length.
# ================================================================

def problem_6():
    try:
        product_name = input("Enter product name: ").strip()
        price_value = read_finite_float("Enter product price: ")

        if not product_name or price_value <= MIN_LABEL_PRICE:
            print("Error: invalid input")
            return

        price_text = f"{price_value:.2f}"
        base_label = f"Product: {product_name} | Price: ${price_text}"

        # Slice to the fixed width, then pad any missing characters.
        label = base_label[:LABEL_WIDTH].ljust(LABEL_WIDTH)

        print(f'Label: "{label}"')
        print(f"Length: {len(label)}")

    except (ValueError, OverflowError):
        print("Error: invalid input")


# ================================================================
# MAIN MENU
# ================================================================
# Select a problem from 1 to 6.
# Enter 0 to exit the program.
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
        print("\n===== STRING MANIPULATION ASSIGNMENT =====")
        print("1. Full name formatter")
        print("2. Simple email validator")
        print("3. Palindrome checker")
        print("4. Sentence word statistics")
        print("5. Password strength classifier")
        print("6. Product label formatter")
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
# Strings are essential for processing user input and displaying results.
# strip() removes outer whitespace, while lower() normalizes letter case.
# split() separates text into words, and join() combines words again.
# Normalizing text helps comparisons work consistently.
# Validation prevents empty or incorrectly formatted input from being used.
# Strings are immutable, so methods return new strings rather than
# modifying the original string directly.
# Slicing provides a convenient way to reverse or truncate text.
# These techniques are useful for names, emails, passwords, and labels.

# ================================================================
# REFERENCES
# ================================================================
# 1. Python Software Foundation, "Text Sequence Type — str."
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# 2. Python Software Foundation, "Built-in Functions."
#    https://docs.python.org/3/library/functions.html
#
# 3. Python Software Foundation, "An Informal Introduction to Python."
#    https://docs.python.org/3/tutorial/introduction.html
#
# 4. Python Software Foundation, "More Control Flow Tools."
#    https://docs.python.org/3/tutorial/controlflow.html
#
# 5. Python Software Foundation, "Errors and Exceptions."
#    https://docs.python.org/3/tutorial/errors.html
#
# 6. Python Software Foundation, "The Python Tutorial."
#    https://docs.python.org/3/tutorial/
# ================================================================
