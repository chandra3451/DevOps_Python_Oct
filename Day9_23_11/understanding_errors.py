# ============================================
#          Python Errors 
# ============================================

# Python errors are divided into:
# 1. Syntax Errors
# 2. Runtime Errors
# 3. Logical Errors
# --------------------------------------------

# 1️⃣ SYNTAX ERROR
# ----------------
# Happens when you break Python grammar rules.
# Example: missing quotes, missing colon, wrong brackets.

# print("Hello world')   # ❌ Mismatched quotes


# 2️⃣ RUNTIME ERROR
# -----------------
# Error that occurs while the program is running.
# Example: dividing by zero.

# print(10 / 0)          # ❌ ZeroDivisionError


# 3️⃣ LOGICAL ERROR
# -----------------
# The program runs, but output is wrong due to logic mistake.

# def add(a, b):
#     return a - b       # ❌ Wrong logic
# print(add(5, 3))       # Output: 2 (incorrect)


# 4️⃣ NAME ERROR
# --------------
# Using a variable/function that is NOT defined.

# print(message)         # ❌ message is not defined


# 5️⃣ TYPE ERROR
# --------------
# Operation between incompatible data types.

# print('2' + 2)         # ❌ Cannot add string + integer


# 6️⃣ INDEX / KEY ERROR
# ----------------------
# Accessing a list index or dict key that does NOT exist.

# nums = [1, 2, 3]
# print(nums[5])         # ❌ IndexError: index 5 does not exist


# 7️⃣ ATTRIBUTE ERROR
# --------------------
# Calling an attribute/function that the object does NOT have.

# num = 6
# num.append(3)          # ❌ int does not have .append()


# 8️⃣ INDENTATION ERROR
# ----------------------
# Wrong indentation (spaces/tabs are incorrect).

# def gree():
# print("Hello")         # ❌ Missing indentation


# 9️⃣ IMPORT ERROR
# -----------------
# When Python cannot find the module to import.

# import mathy           # ❌ No module named 'mathy'


# 🔟 VALUE ERROR
# ---------------
# When value type is correct but content is invalid.

# print(int("abc"))      # ❌ Cannot convert letters to integer


# ============================================
# End of Notes
# ============================================
