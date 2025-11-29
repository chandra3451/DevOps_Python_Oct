# ================================
#  INTEGER (int)
# ================================
# Integers are whole numbers (positive, negative, or zero).
# They do NOT have a decimal point.

print(0)        # Zero
print(10)       # Positive integer
print(-5)       # Negative integer
print(12345)    # Large integer

# type() shows the data type of the value or variable
print(type(12345))  # <class 'int'>
print(type(1))      # <class 'int'>

print("------------------------------")


# ================================
#  FLOAT (float)
# ================================
# Float represents decimal numbers.

print(1.5, type(1.5))   # Float value → <class 'float'>
print(1.0, type(1.0))   # Even if .0 → still a float
print(0.0, type(0.0))

print("------------------------------")


# ================================
#  STRING (str)
# ================================
# Strings represent text. Anything inside "" or '' is a string.

print("Apple", type("Apple"))   # Simple string
print("OPQ Tech")               # Another string

# "123" is a string → contains digits but still text
# 123 is an integer → actual number
print("123", type("123"))       # <class 'str'>
print(123, type(123))           # <class 'int'>

print('hello')                  # Single quotes also allowed

# To use apostrophes inside strings, prefer double-quotes
print("This is Darshan's laptop")

print("------------------------------")


# ================================
#  BOOLEAN (bool)
# ================================
# Boolean values → True or False (case-sensitive)
# They are used in conditions, comparisons, logic, etc.

print(True, type(True))   # Actual boolean value
print("true", type("true"))  # Not boolean → just a string

print(False, type(False))   # Boolean
print("false", type("false"))  # String, not boolean
print("False", type("False"))  # Still a string
