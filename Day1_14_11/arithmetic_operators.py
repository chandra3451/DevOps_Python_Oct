# ================================
#  ARITHMETIC OPERATORS IN PYTHON
# ================================
# Python supports arithmetic with integers, floats, and even booleans.
# Booleans behave like numbers internally:
# True  -> 1
# False -> 0


# --------------------------------
# 1. ADDITION (+)
# --------------------------------

print(2 + 3)         # int + int = 5
print(2.5 + 3.8)     # float + float = 6.3
print(2 + 4.2)       # int + float = float result → 6.2

# Booleans behave like integers (True=1, False=0)
print(True + True)    # 1 + 1 = 2
print(True + False)   # 1 + 0 = 1

# String concatenation using +
print("OPQ" + "Tech")          # String + String → concatenation
print("OPQ" + " " + "Tech")    # Adding a space manually

# Invalid operations (uncomment to test)
# print(2 + "2")       # int + str → TypeError
# print(2 + "hello")   # int + str → TypeError


# --------------------------------
# 2. SUBTRACTION (-)
# --------------------------------

print(2 - 3)         # int - int = -1
print(2.5 - 3.8)     # float - float = -1.3
print(2 - 4.2)       # int - float = float result → -2.2

print(True - True)    # 1 - 1 = 0
print(True - False)   # 1 - 0 = 1

# Invalid
# print("OPQ" - "Tech")  # strings cannot be subtracted


# --------------------------------
# 3. MULTIPLICATION (*)
# --------------------------------

print(-2 * 3)        # -2 × 3 = -6
print(2.5 * 3.8)     # float × float
print(2 * 4.2)       # int × float

print(True * True)    # 1 × 1 = 1
print(True * False)   # 1 × 0 = 0
print(True * 5)       # 1 × 5 = 5

# String repetition using *
print("ha" * 3)       # repeats string: "hahaha"

# Invalid
# print("OPQ" * "Tech")   # string × string not allowed
# print(3.3 * "ha")       # float × string → invalid


# --------------------------------
# 4. DIVISION
# --------------------------------

# a) True division (/)
# Always returns a float
print(7 / 2)        # 3.5
print(7.0 / 2)      # 3.5

# Invalid
# print(True / False)      # division by zero, also invalid types


# b) Floor division (//)
# Gives the integer part (floor value)
print(7 // 2)       # 3
print(7.0 // 2)     # 3.0 (float version of floor)


# c) Modulo (%)
# Gives remainder
print(7 % 2)        # remainder = 1
print(5.5 % 2)      # works with floats too → remainder = 1.5


# --------------------------------
# 5. EXPONENTIATION (**)
# --------------------------------

print(3 ** 2)       # 3² = 9
print(3 ** 5)       # 3⁵ = 243
print(pow(3, 2))    # pow(base, exponent) => also 9


# --------------------------------
# 6. ABSOLUTE VALUE (abs)
# --------------------------------
# Converts negative numbers to positive

print(abs(-35))     # 35
print(abs(35))      # 35


# --------------------------------
# 7. ROUNDING (round)
# --------------------------------
# round(number, digits)

print(round(3.14345, 2))   # rounds to 2 decimal places → 3.14
