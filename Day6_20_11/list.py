# ---------------------------
# LISTS — Class Notes & Examples
# ---------------------------

# Storing student info using separate variables is NOT scalable:
# name_1 = "Darshan"
# roll_no = 123
# marks1 = 35
# For many students / many fields we use lists (or dicts later).

# ---------------------------
# BASIC IDEA / DEFINITION
# ---------------------------
# list -> ordered, mutable collection that can store different data types
# syntax: [item1, item2, item3]
# Example:
lst = ["milk", "eggs", "bread"]

# ---------------------------
# CREATING LISTS
# ---------------------------
# empty list
empty_list = []
print("empty_list:", empty_list)

# list of strings
stds = ["Asha", "Sam", "Ravi"]
print("stds:", stds)

# list of numbers
marks = [12, 45, 65, 90]
print("marks:", marks)

# mixed-type list for a student (name, phone, dob, marks, flag)
std_12 = ["Sam", 88767887, "12-04-2019", 45, True]
print("std_12:", std_12)

# ---------------------------
# ACCESSING ITEMS (INDEXING)
# ---------------------------
lst = ["milk", "eggs", "bread"]
print("first item:", lst[0])   # index 0
print("third item:", lst[2])   # index 2
print("last item:", lst[-1])   # negative index: last element

# ---------------------------
# CONVERT OTHER ITERABLES TO LIST USING list()
# ---------------------------
# string -> list of characters
name = "Asha"
res = list(name)
print(name, "->", res)

# range -> list of numbers
r = range(1, 6)
print("range to list:", list(r))

# sentence -> list of words (use .split())
sent = "Python is fun"
print("as characters:", list(sent))   # characters
print("as words:", sent.split())      # words

# ---------------------------
# SLICING: list[start:end:step]  (end excluded)
# ---------------------------
a = [0, 1, 2, 3, 4, 5, 6]
print("a[2:5]:", a[2:5])   # elements at indexes 2,3,4
print("a[:3]:", a[:3])     # from start to index 2
print("a[2:]:", a[2:])     # from index 2 to end
print("a[0:7:3]:", a[0:7:3])  # step 3
print("a[::2]:", a[::2])      # every 2nd element
print("a[::-1] (reverse):", a[::-1])

# ---------------------------
# MODIFYING LISTS (mutable)
# ---------------------------
lst = ["milk", "eggs", "bread"]
print("before:", lst)
lst[1] = "jam"       # change element at index 1
print("after modify:", lst)

# ---------------------------
# ADDING ITEMS
# ---------------------------
items = ["milk", "eggs", "bread"]
items.append("jam")                 # add single element at end
print("after append:", items)

items.extend(["sugar", "salt"])     # add multiple elements
print("after extend:", items)

items.insert(1, "butter")           # insert at position 1
print("after insert:", items)

# ---------------------------
# REMOVAL METHODS
# ---------------------------
items = ["milk", "eggs", "bread", "milk"]
items.remove("milk")    # removes first occurrence of "milk"
print("after remove('milk'):", items)

# pop -> remove by index and return the element (default last)
items = ["milk", "eggs", "bread"]
last = items.pop()      # removes "bread"
print("popped:", last, "remaining:", items)
second = items.pop(1)   # removes index 1 ("eggs")
print("popped index 1:", second, "remaining:", items)

# clear -> remove all elements
items = ["milk", "eggs", "bread", "milk"]
items.clear()
print("after clear:", items)

# ---------------------------
# COUNT, INDEX & FREQUENCY
# ---------------------------
a = [0, 1, 2, 2, 3, 2, 4, 3, 5, 4]
print("count of 2:", a.count(2))    # how many times 2 appears

# ---------------------------
# SORTING
# ---------------------------
nums = [5, 2, 8, 4]
nums.sort()               # sorts in place (permanently changes nums)
print("sorted in place:", nums)

nums.sort(reverse=True)   # descending
print("sorted descending:", nums)

# sorted() -> returns a new sorted list (original unchanged)
nums = [5, 2, 8, 4]
new_list = sorted(nums)
print("original:", nums, "sorted(new):", new_list)

# ---------------------------
# REVERSE
# ---------------------------
letters = ["a", "b", "c", "d"]
letters.reverse()   # in-place reverse
print("letters reversed:", letters)

# ---------------------------
# LENGTH and AGGREGATES
# ---------------------------
letters = ["a", "b", "c", "d"]
print("len(letters):", len(letters))

nums = [5, 2, 8, 4]
print("min:", min(nums), "max:", max(nums), "sum:", sum(nums))

# manual sum (same result)
total = 0
for n in nums:
    total += n
print("manual total:", total)

# ---------------------------
# MEMBERSHIP: in / not in
# ---------------------------
fruits = ["apple", "banana", "mango"]
print("'apple' in fruits?", "apple" in fruits)
print("'kiwi' in fruits?", "kiwi" in fruits)

if "kiwi" not in fruits:
    print("kiwi is not available")

# ---------------------------
# LOOPING / ITERATION
# ---------------------------
fruits = ["apple", "banana", "mango"]
# simple iteration (value only)
for i in fruits:
    print("value:", i)

# index + value using range
for i in range(len(fruits)):
    print("index", i, "value", fruits[i])

# enumerate -> index and value together
for i, j in enumerate(fruits):
    print("enumerate:", i, j)

# print only names starting with "A"
names = ["Asha", "Sam", "Ravi", "Arun"]
for name in names:
    if name.startswith("A"):
        print("starts with A:", name)

print("-" * 20)

# ---------------------------
# LIST COMPREHENSIONS (one-line list creation)
# ---------------------------
# syntax: [expression for item in iterable if condition]

# example: squares using loop
nums = [1, 2, 3, 4, 5]
res = []
for num in nums:
    res.append(num * num)
print("squares (loop):", res)

# same with list comprehension
result = [num * num for num in nums]
print("squares (comprehension):", result)

# filter example: even numbers squared (loop)
nums = [1, 2, 3, 4, 5, 6, 8, 10, 5]
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num * num)
print("even squares (loop):", evens)

# same with comprehension
even_sq = [num * num for num in nums if num % 2 == 0]
print("even squares (comprehension):", even_sq)

# ---------------------------
# TERNARY INSIDE COMPREHENSION (value_if_true if cond else value_if_false)
# ---------------------------
nums = []
labels = []
for x in range(6):
    nums.append(x)
    if x % 2 == 0:
        labels.append("Even")
    else:
        labels.append("Odd")

print("nums:", nums)
print("labels (loop):", labels)

# list comprehension with ternary operator produces same labels
labels_list = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print("labels (comprehension):", labels_list)


