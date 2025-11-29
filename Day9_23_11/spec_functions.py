# ============================================
#   Lambda, map(), filter(), zip()
# ============================================

# 1. LAMBDA FUNCTIONS
# -------------------
# Lambda: small anonymous function (function without a name)
# Used when we need a simple one-line function.
# Syntax: lambda arguments: expression

# Square of a number
sq = lambda x: x * x
print("Square of 2 =", sq(2))

# Add two numbers
add = lambda a, b: a + b
print("Add 2 + 3 =", add(2, 3))

# Even or Odd using lambda
# Here we directly call lambda without storing it in a variable
print("Even/Odd for 10 =", (lambda x: "Even" if x % 2 == 0 else "Odd")(10))


# 2. map() FUNCTION
# -------------------
# map() applies a function to every element of a sequence (list, tuple, etc.)
# It basically performs a loop internally and returns a map object.
# Syntax: map(function, sequence)

# Square each number in a list
nums = [1, 2, 3, 4, 5]
res = map(lambda x: x * x, nums)
print("Squares:", list(res))

# Convert names to uppercase
names = ['sam', 'ravi', 'darshan']
output = map(lambda x: x.upper(), names)
print("Uppercase names:", list(output))

# Multiply elements of two lists element-wise
# map() stops at the shortest list
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x * y, a, b)
print("Multiply two lists:", list(res))


# 3. filter() FUNCTION
# ----------------------
# filter() keeps only the elements that satisfy a given condition.
# It removes all the elements for which the function returns False.
# Syntax: filter(function, sequence)

# Filter even numbers
nums = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, nums)
print("Even numbers:", list(evens))

# Keep names starting with "D"
names = ["Sam", "Darshan", "Ravi", "Deepak"]
d_names = filter(lambda n: n.startswith("D"), names)
print("Names starting with D:", list(d_names))

# Keep marks greater than 50
marks = [25, 45, 24, 56, 76, 12, 98]
high_scores = filter(lambda n: n > 50, marks)
print("Scores > 50:", list(high_scores))


# 4. zip() FUNCTION
# -------------------
# zip() combines elements from multiple lists into pairs based on their index (tuples).
# Works like zipping two chains together.
# Syntax: zip(list1, list2, ...)

roll = [1, 2, 3, 4]
names = ["Sam", "Darshan", "Ravi", "Deepak"]

combined = zip(roll, names)
print("Zipped list:", list(combined))  # [(1, 'Sam'), (2, 'Darshan'), ...]

# Convert zipped result into a dictionary
print("Roll-Name dictionary:", dict(zip(roll, names)))


# --------------------------------------------
# Summary Table (for quick revision)
# --------------------------------------------
# | Function     | Purpose                           | Example                       |
# | ------------ | --------------------------------- | ----------------------------- |
# | lambda       | create small one-line function    | lambda x: x*x                 |
# | map()        | transform all items in a list     | map(lambda x: x+1, nums)      |
# | filter()     | keep items that meet condition    | filter(lambda x: x>0, nums)   |
# | zip()        | combine lists element-wise        | zip(a, b)                     |
# --------------------------------------------

