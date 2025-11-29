num = int(input("Enter a number: "))
print("Initial value: ", num)

# += → Add and assign
# This means: take the current value of num, add 5, and store it back in num
num += 5    # num = num + 5
print("Add assign num: ", num)

# -= → Subtract and assign
# Subtract 2 from the current value of num
num -= 2    # num = num - 2
print("sub num: ", num)

# *= → Multiply and assign
# Multiply num by 3
num *= 3    # num = num * 3
print("Num: ", num)

# /= → Divide and assign (gives decimal number)
# Divide num by 2
num /= 2    # num = num / 2
print("Num: ", num)

# //= → Floor divide and assign (keeps only whole number)
# Divide num by 2 and remove decimal part
num //= 2   # num = num // 2
print("Num: ", num)

# %= → Modulus and assign (store remainder)
# Store remainder when num is divided by 3
num %= 3    # num = num % 3
print("Num: ", num)

# **= → Power and assign
# Raise num to the power 2
num **= 2   # num = num ** 2
print("Num: ", num)
