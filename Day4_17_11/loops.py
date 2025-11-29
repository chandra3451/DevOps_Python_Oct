# ----------------------------------------------------
# LOOPS IN PYTHON
# ----------------------------------------------------
# Loops allow us to repeat a block of code multiple times.
# Very useful when performing repeated tasks (tables, printing,
# calculations, automation tasks, DevOps scripts etc.)
# ----------------------------------------------------


# ----------------------------------------------------
# FOR LOOP
# ----------------------------------------------------
# Syntax:
# for variable in sequence:
#     # code that runs for each item in the sequence
#
# In Python, the most common sequence used with loops is range().
# ----------------------------------------------------


# ----------------------------------------------------
# range() FUNCTION
# ----------------------------------------------------
# range() generates a sequence of integers.
#
# range(end)
#   → numbers from 0 to end-1
#   Example: range(5) → 0,1,2,3,4
#
# range(start, end)
#   → numbers from start to end-1
#   Example: range(1, 10) → 1,2,3,4,5,6,7,8,9
#
# range(start, end, step)
#   → increments by step value
#   Example: range(1, 10, 3) → 1,4,7
# ----------------------------------------------------


# ----------------------------------------------------
# Example 1: range(end)
# ----------------------------------------------------
# Prints 0 to 4
# for i in range(5):     # 0,1,2,3,4
#     print(i)


# ----------------------------------------------------
# Example 2: Printing multiplication table
# ----------------------------------------------------
# for i in range(1, 51):     # 1 to 50
#     print(10, "*", i, "=", 10 * i)


# ----------------------------------------------------
# Example 3: Using step value
# ----------------------------------------------------
# Prints numbers by skipping 3 each time → 1, 4, 7
# for i in range(1, 10, 3):
#     print(i)
