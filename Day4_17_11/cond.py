# ----------------------------------------------------
# CONDITIONAL STATEMENTS IN PYTHON
# ----------------------------------------------------
# Conditional statements allow our program to make decisions.
# Based on a condition (True/False), different code will run.
# ----------------------------------------------------


# ----------------------------------------------------
# IF STATEMENT (single condition)
# ----------------------------------------------------
# Syntax:
# if condition:
#     code_to_run

# if + else format:
# if condition:
#     code_block_1
# else:
#     code_block_2
# ----------------------------------------------------

# a = int(input("Enter a number: "))

# if a > 0:
#     print("Positive Number")        # this runs only when condition is True
#     # print("This is inside the block")
# else:
#     print("Not a positive number")  # runs only when condition is False

# print("Outside the if...else")      # runs always



# ----------------------------------------------------
# IF + ELIF + ELSE  
# Used when we have multiple conditions
# Python checks conditions from TOP to BOTTOM.
# As soon as one condition becomes True → it stops checking further.
# ----------------------------------------------------

# Example 1: Temperature-based dressing
# temp = int(input("Enter Temp: "))

# if temp > 30:
#     print("Wear T-shirt")
# elif temp > 20:
#     print("Wear light Jacket")
# else:
#     print("Wear heavy Jacket")

# Example 2: Number type
# a = int(input("Enter a number: "))

# if a > 0:
#     print("Positive Number")
# elif a == 0:
#     print("Number is zero")
# else:
#     print("Negative Number")

# Note:
# if True  → executes and stops.
# if False → moves to next condition (elif).
# If all fail → final else runs.



# ----------------------------------------------------
# NESTED IF (if inside another if)
# Use when a second check depends on the first condition.
# ----------------------------------------------------

# marks = int(input("Enter marks: "))

# if marks >= 40:
#     print("Pass")
    
#     # grade checking only if student has passed
#     if marks >= 85:
#         print("Grade: A+")
#     elif marks >= 75:
#         print("Grade: A")
#     elif marks >= 60:
#         print("Grade: B")
#     else:
#         print("Grade: C")

# else:
#     print("Fail")



# ----------------------------------------------------
# SAME LOGIC USING if / elif / else (no nested if)
# ----------------------------------------------------

# if marks < 40:
#     print("Fail")
# elif marks >= 75:
#     print("Pass")
#     print("Grade A")
# else:
#     print("Pass")
#     print("Grade B")



# ----------------------------------------------------
# ONE-LINE IF ELSE (TERNARY OPERATOR)
# Use ONLY for short & simple conditions.
# Syntax:
# value_if_true  if condition  else value_if_false
# ----------------------------------------------------

# Example 1
# x = -10
# result = "Positive" if x > 0 else "Non-positive"
# print(result)

# Example 2
# age = int(input("Enter age: "))
# print("Child" if age < 13 else "Teenager" if age <= 19 else "Adult")
