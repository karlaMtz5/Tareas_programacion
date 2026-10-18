
# ================================================================
# COVER PAGE
# Student: Karla Lizeth Martinez Lopez
# Student ID: 2630014
# Group: IM 1-2
# File: 2630014_MartinezLopezKarla.py
# Course: Metodologias de la programacion
# Assignment: Lists, Tuples, and Dictionaries
# ================================================================

# EXECUTIVE SUMMARY
# A list is an ordered, mutable collection that stores multiple values.
# A tuple is an ordered, immutable collection used for fixed records.
# A dictionary stores key-value pairs and allows fast lookups by key.
# Mutable objects can be changed after creation.
# Immutable objects cannot have their elements reassigned.
# This program contains six practical problems using Python collections.
# Each problem includes a description, inputs, outputs, validations,
# and three test cases: normal, boundary, and error.
# The exercises cover shopping lists, coordinates, product catalogs,
# student grades, word frequency, and a contact book.

# PRINCIPLES AND GOOD PRACTICES
# - Use lists for collections that need to change.
# - Use tuples for fixed data, such as coordinates.
# - Use dictionaries for information organized by keys.
# - Validate user input before processing it.
# - Use descriptive variable and function names.
# - Handle invalid input without crashing the program.
# - Keep each problem in a separate function.


# ================================================================
# PROBLEM 1: SHOPPING LIST BASICS
# Collection: List
#
# Description:
# Read products separated by commas, add a new product,
# display the number of products, and search for a product.
#
# Inputs:
# - A comma-separated list of products.
# - A new product to add.
# - A product name to search for.
#
# Outputs:
# - The shopping list.
# - The total number of products.
# - The result of the search.
#
# Validations:
# - The initial list cannot be empty.
# - Product names cannot be empty.
# - Search ignores uppercase and lowercase differences.
#
# Test cases:
# 1. Normal: Add "Milk" to "Bread, Eggs".
# 2. Boundary: Search for the only product in a one-item list.
# 3. Error: Enter an empty initial list or product name.
# ================================================================

def problem_1():
    print("\n--- Problem 1: Shopping List Basics ---")

    products_text = input(
        "Enter products separated by commas: "
    ).strip()

    if not products_text:
        print("Error: the shopping list cannot be empty.")
        return

    products = [
        item.strip()
        for item in products_text.split(",")
        if item.strip()
    ]

    if not products:
        print("Error: enter at least one valid product.")
        return

    new_product = input("Enter a product to add: ").strip()

    if not new_product:
        print("Error: product name cannot be empty.")
        return

    products.append(new_product)

    print("Shopping list:", products)
    print("Total products:", len(products))

    search_product = input("Enter a product to search for: ").strip()

    if not search_product:
        print("Error: search term cannot be empty.")
        return

    found = any(
        product.casefold() == search_product.casefold()
        for product in products
    )

    if found:
        print("Product found:", search_product)
    else:
        print("Product not found:", search_product)


# ================================================================
# PROBLEM 2: POINTS AND DISTANCES
# Collection: Tuples
#
# Description:
# Store two-dimensional points as tuples and calculate
# the distance between two points.
#
# Inputs:
# - X and Y coordinates for the first point.
# - X and Y coordinates for the second point.
#
# Outputs:
# - Both points as tuples.
# - The Euclidean distance between the points.
#
# Validations:
# - Coordinates must be valid numbers.
# - Coordinates must be finite values.
#
# Test cases:
# 1. Normal: Points (0, 0) and (3, 4); distance is 5.
# 2. Boundary: Both points are identical; distance is 0.
# 3. Error: Enter text instead of a coordinate.
# ================================================================

def problem_2():
    print("\n--- Problem 2: Points and Distances ---")

    try:
        x1 = float(input("Enter the first point's X coordinate: "))
        y1 = float(input("Enter the first point's Y coordinate: "))
        x2 = float(input("Enter the second point's X coordinate: "))
        y2 = float(input("Enter the second point's Y coordinate: "))

        import math

        coordinates = (x1, y1, x2, y2)

        if not all(math.isfinite(value) for value in coordinates):
            print("Error: coordinates must be finite numbers.")
            return

        point_1 = (x1, y1)
        point_2 = (x2, y2)

        distance = math.hypot(x2 - x1, y2 - y1)

        print("First point:", point_1)
        print("Second point:", point_2)
        print("Distance:", round(distance, 2))

    except ValueError:
        print("Error: enter valid numeric coordinates.")


# ================================================================
# PROBLEM 3: PRODUCT CATALOG
# Collection: Dictionary
#
# Description:
# Create a product catalog, add a product with its price,
# and search for a product in the catalog.
#
# Inputs:
# - A product name.
# - Its price.
# - A product name to search for.
#
# Outputs:
# - The updated catalog.
# - The price of a product, if found.
#
# Validations:
# - Product names cannot be empty.
# - Prices must be numeric, finite, and nonnegative.
# - Searches ignore uppercase and lowercase differences.
#
# Test cases:
# 1. Normal: Add "Notebook" with a price of 25.50.
# 2. Boundary: Add a product with a price of 0.
# 3. Error: Enter a negative or nonnumeric price.
# ================================================================

def problem_3():
    print("\n--- Problem 3: Product Catalog ---")

    catalog = {
        "Pencil": 5.00,
        "Notebook": 25.50,
        "Eraser": 4.00
    }

    product_name = input("Enter the product name to add: ").strip()

    if not product_name:
        print("Error: product name cannot be empty.")
        return

    try:
        price = float(input("Enter the product price: "))

        import math

        if not math.isfinite(price) or price < 0:
            print("Error: price must be a finite, nonnegative number.")
            return

    except ValueError:
        print("Error: enter a valid numeric price.")
        return

    catalog[product_name] = price

    print("\nUpdated catalog:")
    for name, product_price in catalog.items():
        print(f"{name}: ${product_price:.2f}")

    search_name = input(
        "\nEnter a product name to search for: "
    ).strip()

    if not search_name:
        print("Error: search term cannot be empty.")
        return

    matching_name = next(
        (
            name for name in catalog
            if name.casefold() == search_name.casefold()
        ),
        None
    )

    if matching_name is not None:
        print(
            f"Product found: {matching_name} - "
            f"${catalog[matching_name]:.2f}"
        )
    else:
        print("Error: product not found.")


# ================================================================
# PROBLEM 4: STUDENT GRADES
# Collections: List and Dictionary
#
# Description:
# Store a student's grades, calculate the average,
# and display the highest and lowest grades.
#
# Inputs:
# - Student name.
# - Grades separated by commas.
#
# Outputs:
# - Student name and grades.
# - Average, highest grade, and lowest grade.
#
# Validations:
# - Student name cannot be empty.
# - At least one grade is required.
# - Grades must be numeric and between 0 and 100.
#
# Test cases:
# 1. Normal: Grades 80, 90, 100; average is 90.
# 2. Boundary: A single grade of 0; average is 0.
# 3. Error: Enter a grade above 100 or nonnumeric text.
# ================================================================

def problem_4():
    print("\n--- Problem 4: Student Grades ---")

    student_name = input("Enter the student's name: ").strip()

    if not student_name:
        print("Error: student name cannot be empty.")
        return

    grades_text = input(
        "Enter grades separated by commas (0-100): "
    ).strip()

    if not grades_text:
        print("Error: at least one grade is required.")
        return

    try:
        grades = [
            float(value.strip())
            for value in grades_text.split(",")
        ]

        import math

        if not all(math.isfinite(grade) for grade in grades):
            print("Error: grades must be finite numbers.")
            return

        if any(grade < 0 or grade > 100 for grade in grades):
            print("Error: every grade must be between 0 and 100.")
            return

    except ValueError:
        print("Error: all grades must be valid numbers.")
        return

    student = {
        "name": student_name,
        "grades": grades
    }

    average = sum(student["grades"]) / len(student["grades"])

    print("\nStudent:", student["name"])
    print("Grades:", student["grades"])
    print(f"Average: {average:.2f}")
    print(f"Highest grade: {max(student['grades']):.2f}")
    print(f"Lowest grade: {min(student['grades']):.2f}")


# ================================================================
# PROBLEM 5: WORD FREQUENCY COUNTER
# Collection: Dictionary
#
# Description:
# Count how many times each word appears in a sentence.
#
# Inputs:
# - A sentence or group of words.
#
# Outputs:
# - Each unique word and its frequency.
#
# Validations:
# - The sentence cannot be empty.
# - The sentence must contain at least one word.
# - Uppercase and lowercase forms count as the same word.
#
# Test cases:
# 1. Normal: "cat dog cat"; cat appears twice.
# 2. Boundary: A single word appears once.
# 3. Error: Enter an empty sentence.
# ================================================================

def problem_5():
    print("\n--- Problem 5: Word Frequency Counter ---")

    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: sentence cannot be empty.")
        return

    words = sentence.casefold().split()

    if not words:
        print("Error: enter at least one word.")
        return

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("\nWord frequencies:")

    for word, count in frequency.items():
        print(f"{word}: {count}")


# ================================================================
# PROBLEM 6: SIMPLE CONTACT BOOK
# Collection: Dictionary
#
# Description:
# Add, search for, and delete contacts using a dictionary.
#
# Inputs:
# - Action: ADD, SEARCH, or DELETE.
# - Contact name.
# - Phone number when adding a contact.
#
# Outputs:
# - Contact saved, phone number, contact deleted,
#   or an error message.
#
# Validations:
# - Action must be ADD, SEARCH, or DELETE.
# - Contact name cannot be empty.
# - Phone number must contain 7 to 15 digits.
# - Contact searches are case-insensitive.
# - A contact must exist before it can be deleted or searched.
#
# Test cases:
# 1. Normal: ADD Dana with phone 5551234567.
# 2. Boundary: SEARCH Alice, an initial contact.
# 3. Error: Invalid action or DELETE an unknown contact.
# ================================================================

def problem_6():
    print("\n--- Problem 6: Simple Contact Book ---")

    contacts = {
        "Alice": "5551112233",
        "Ben": "5552223344",
        "Carla": "5553334455"
    }

    action = input(
        "Enter action (ADD, SEARCH, DELETE): "
    ).strip().upper()

    if action not in ("ADD", "SEARCH", "DELETE"):
        print("Error: invalid action.")
        return

    name = input("Enter contact name: ").strip()

    if not name:
        print("Error: contact name cannot be empty.")
        return

    matching_name = next(
        (
            contact_name for contact_name in contacts
            if contact_name.casefold() == name.casefold()
        ),
        None
    )

    if action == "ADD":
        phone = input("Enter phone number: ").strip()

        if not phone.isdigit() or not 7 <= len(phone) <= 15:
            print("Error: phone number must contain 7 to 15 digits.")
            return

        if matching_name is not None:
            contacts[matching_name] = phone
            print("Contact updated:", matching_name, phone)
        else:
            contacts[name] = phone
            print("Contact saved:", name, phone)

    elif action == "SEARCH":
        if matching_name is not None:
            print("Contact:", matching_name)
            print("Phone:", contacts[matching_name])
        else:
            print("Error: contact not found.")

    elif action == "DELETE":
        if matching_name is not None:
            del contacts[matching_name]
            print("Contact deleted:", matching_name)
        else:
            print("Error: contact not found.")

    print("Current contacts:", contacts)


# ================================================================
# MAIN MENU
# Select a problem from 1 to 6.
# Enter 0 to exit the program.
# ================================================================

def main():
    problem_functions = {
        "1": problem_1,
        "2": problem_2,
        "3": problem_3,
        "4": problem_4,
        "5": problem_5,
        "6": problem_6
    }

    while True:
        print("\n===== Python Collection Problems =====")
        print("1. Shopping List Basics")
        print("2. Points and Distances")
        print("3. Product Catalog")
        print("4. Student Grades")
        print("5. Word Frequency Counter")
        print("6. Simple Contact Book")
        print("0. Exit")

        choice = input("Choose a problem (0-6): ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        selected_problem = problem_functions.get(choice)

        if selected_problem is None:
            print("Error: invalid input. Choose a number from 0 to 6.")
        else:
            selected_problem()


if __name__ == "__main__":
    main()


# ================================================================
# CONCLUSIONS
#
# Lists are useful for storing ordered collections that can change.
# Tuples are appropriate for fixed records such as coordinates.
# Dictionaries organize information through key-value pairs.
# Combining these collections helps solve different programming tasks.
# Input validation prevents common errors and improves reliability.
# Functions make the program easier to read, test, and maintain.
#
# REFERENCES
#
# 1. Python Software Foundation, "Built-in Types."
#    https://docs.python.org/3/library/stdtypes.html
#
# 2. Python Software Foundation, "Data Structures."
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 3. Python Software Foundation, "Built-in Functions."
#    https://docs.python.org/3/library/functions.html
#
# 4. Python Software Foundation, "Errors and Exceptions."
#    https://docs.python.org/3/tutorial/errors.html
#
# 5. Python Software Foundation, "More on Defining Functions."
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#
# 6. Python Software Foundation, "Input and Output."
#    https://docs.python.org/3/tutorial/inputoutput.html
# ================================================================
