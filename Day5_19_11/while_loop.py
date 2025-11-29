# ---------------------------------------------------------
# WHILE LOOP
# ---------------------------------------------------------
# while loop repeats a block of code as long as the condition is TRUE.
# Useful when we do NOT know how many times the loop will run.
# ---------------------------------------------------------

# Syntax:
# while condition:
#     # block of code (must be indented)


# ---------------------------------------------------------
# Example 1: Simple while loop (print numbers)
# ---------------------------------------------------------

# i = 1
# while i <= 5:        # loop runs while condition is True
#     print(i)
#     i += 2           # update i (important to avoid infinite loop)



# ---------------------------------------------------------
# Example 2: Keep adding numbers until sum reaches target
# ---------------------------------------------------------

# target = 30

# i = 1
# count = 0            # running total

# while count < target:
#     count += i       # add next number
#     print(f"After adding {i} -> count = {count}")
#     i += 1           # increase number for next addition



# ---------------------------------------------------------
# Example 3: Login System with Maximum Attempts (while + break + else)
# ---------------------------------------------------------

# user_name = "admin"
# user_pass = "admin123"

# attempts = 0
# max_attempts = 3

# while attempts < max_attempts:
#     user = input("Username: ")
#     password = input("Password: ")

#     if user == user_name and password == user_pass:
#         print("Login successful!")
#         break                      # exit the loop immediately
#     else:
#         attempts += 1
#         print("Incorrect username or password")
#         print("Attempts left:", max_attempts - attempts)

# # This ELSE runs ONLY if loop ends normally (i.e., no break happened)
# else:
#     print("Account locked!")



# ---------------------------------------------------------
# FOR vs WHILE – When to use which?
# ---------------------------------------------------------

# For loop:
# - Use when the number of repetitions is KNOWN.
# - Works with sequences (range, list, string).
# - Low risk of infinite loop.

# While loop:
# - Use when the number of repetitions is UNKNOWN.
# - Depends on a TRUE/FALSE condition.
# - High chance of infinite loop if condition is not updated.

# Quick Summary:
# For → fixed steps       (e.g., run 10 times)
# While → run until done  (e.g., ask password until correct)
