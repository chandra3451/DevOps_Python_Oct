# ----------------------------------------------------------
# ITERATORS & GENERATORS 
# ----------------------------------------------------------
# Iterators and Generators help Python give values "one at a time".
# This makes loops efficient, memory-friendly, and fast.
# ----------------------------------------------------------


# ----------------------------------------------------------
# 1. ITERABLES
# ----------------------------------------------------------
# An iterable is something you can loop over.
# Examples: list, tuple, string, dictionary, set, range, file...
# If you can use a 'for' loop on it, it is an iterable.
# ----------------------------------------------------------

nums = [10, 20, 30]

# for num in nums:
#     print(num)
# This works because 'nums' is an iterable.


# ----------------------------------------------------------
# 2. ITERATORS
# ----------------------------------------------------------
# An iterator is an object that gives values ONE-BY-ONE.
# We get an iterator from an iterable using iter().
# We fetch values using next().
# ----------------------------------------------------------

it = iter(nums)   # creating iterator from the list

# print(next(it))  # -> 10
# print(next(it))  # -> 20
# print(next(it))  # -> 30
# print(next(it))  # ERROR: StopIteration (no more values)


# ----------------------------------------------------------
# 2A. How for-loop works internally
# ----------------------------------------------------------
# A for-loop secretly uses iter() and next() behind the scenes.
# Python stops the loop when next() raises StopIteration.
# ----------------------------------------------------------

# while True:
#     try:
#         value = next(it)
#         print(value)
#     except StopIteration:
#         break
# This is exactly how Python's for-loop works internally.


# ----------------------------------------------------------
# 3. GENERATORS
# ----------------------------------------------------------
# A generator is a special type of function that uses 'yield'.
# 'yield' pauses the function and returns a value.
# Next time, it continues from where it paused.
#
# Generators give one value at a time (like iterators).
# They do NOT store all values in memory — very efficient!
# ----------------------------------------------------------


# ----------------------------------------------------------
# Example 1: Simple generator
# ----------------------------------------------------------

def simple_gen():
    yield 1          # produces 1, then pauses
    yield 2          # produces 2
    yield 3          # produces 3

g = simple_gen()     # g is a generator object


# Using for-loop to get values from generator
# for val in g:
#     print(val)
#
# Using next() manually:
# print(next(g))    # -> 1
# print(next(g))    # -> 2
# print(next(g))    # -> 3


# ----------------------------------------------------------
# Example 2: Generator for even numbers
# ----------------------------------------------------------
# This generator yields even numbers from 0 to 'limit'.
# It does NOT store the entire list. It gives one number each time.
# ----------------------------------------------------------

def even_nums(limit):
    for i in range(0, limit + 1, 2):
        yield i

g = even_nums(10)

for val in g:
    print(val)   # prints: 0 2 4 6 8 10


# ----------------------------------------------------------
# Example 3: Same logic WITHOUT generator (bad approach)
# ----------------------------------------------------------
# This version stores ALL even numbers in a list first.
# Uses more memory. Not efficient for DevOps/log files.
# ----------------------------------------------------------

res = []

def even_nums_n(limit):
    for i in range(0, limit + 1, 2):
        res.append(i)
    return res

# print(even_nums_n(10))  # -> [0, 2, 4, 6, 8, 10]

# ----------------------------------------------------------
# Important Difference:
# even_nums() -> generator → gives values one by one → memory efficient
# even_nums_n() -> normal function → stores all values → uses extra memory
# ----------------------------------------------------------
