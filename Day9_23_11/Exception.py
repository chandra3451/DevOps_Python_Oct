# ============================================
#      Exception Handling - Class Notes
# ============================================

# What is an Exception?
# ----------------------
# An exception is an event that interrupts the normal flow of a program.
# Example:
#   - Entering wrong input (ValueError)
#   - Dividing by zero (ZeroDivisionError)
#   - File not found (FileNotFoundError)
#   - Using undefined variable (NameError)
#
# Python handles these using try-except blocks.


# --------------------------------------------
# 1️⃣ Basic try–except
# --------------------------------------------
# try block -> code that MAY cause an error
# except block -> runs ONLY if an error happens

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("Not a valid number (Only digits allowed)")


# --------------------------------------------
# 2️⃣ Multiple except blocks
# --------------------------------------------
# Use separate except blocks for different error types.

# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(result)
# except ValueError:
#     print("Not a valid number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# --------------------------------------------
# 3️⃣ else block
# --------------------------------------------
# else runs ONLY when there is NO exception.

# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
# except ValueError:
#     print("Not a valid number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("Division successful! Result =", result)


# --------------------------------------------
# 4️⃣ finally block
# --------------------------------------------
# finally ALWAYS runs
# - exception happened -> still runs
# - no exception -> still runs
# Used for cleanup tasks like:
#   - closing files
#   - closing database connections

# try:
#     file = open("demo123.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found")
# finally:
#     # Check if file variable exists before closing
#     try:
#         file.close()
#         print("File Closed")
#     except:
#         print("File could not be closed")


# --------------------------------------------
# 5️⃣ Raising Exceptions Manually
# --------------------------------------------
# Use 'raise' to generate your own custom error message.

# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     print("Age:", age)

# try:
#     age = int(input("Enter age: "))
#     check_age(age)
# except ValueError as ve:
#     print("Error:", ve)


# --------------------------------------------
# 6️⃣ Final Example: try + multiple except + else + finally
# --------------------------------------------

# Explanation:
# - try: take age and calculate ticket price
# - if age < 0 → raise ValueError manually
# - if age == 0 → ZeroDivisionError (cannot divide by zero)
# - else: runs only when no errors
# - finally: always runs (used for cleanup or concluding messages)

try:
    age = int(input("Enter age: "))

    # Manually raising an error
    if age < 0:
        raise ValueError("Age cannot be -ve")

    # This line may cause ZeroDivisionError if age = 0
    ticket = 500 / age

except ValueError as ve:
    print("Error:", ve)

except ZeroDivisionError:
    print("Age cannot be zero")

else:
    print("Age:", age, "| Ticket Price:", ticket)

finally:
    print("Program finished (finally block executed)")

