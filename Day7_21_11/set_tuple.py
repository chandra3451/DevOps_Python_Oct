# =====================================================================
#                                   SET
# =====================================================================
# Set -> A collection of UNIQUE and UNORDERED elements.
# Syntax → { }
# No duplicate values allowed.
# Order is not guaranteed.

my_set = {1, 2, 3, 4, 5}
print(my_set, type(my_set))

# ---------------------------------------------------------------------
# ADDING ELEMENTS
# ---------------------------------------------------------------------
# add() → inserts a new element
my_set.add(6)
print("After adding 6:", my_set)

# ---------------------------------------------------------------------
# POP ELEMENT
# ---------------------------------------------------------------------
# pop() → removes and returns a RANDOM element (because set is unordered)
value = my_set.pop()
print("Popped value:", value)
print("After pop:", my_set)

# ---------------------------------------------------------------------
# DISCARD ELEMENT
# ---------------------------------------------------------------------
# discard() → removes element if present (no error if element missing)
my_set.discard(3)
print("After discarding 3:", my_set)

# ---------------------------------------------------------------------
# MEMBERSHIP TESTING
# ---------------------------------------------------------------------
print(2 in my_set)     # True if present
print(10 in my_set)    # False

# ---------------------------------------------------------------------
# LOOPING THROUGH A SET
# ---------------------------------------------------------------------
for x in my_set:
    print("Value:", x)

# =====================================================================
# REMOVE DUPLICATES FROM LIST USING SET
# =====================================================================

a = [1, 2, 4, 4, 3, 5, 6, 4, 7, 9, 9]
print("Original list:", a)

uq_set = set(a)       # Removes duplicates
print("Unique set:", uq_set)

uq_lst = list(uq_set) # Convert back to list
print("Unique list:", uq_lst)

# =====================================================================
#                         MAJOR SET OPERATIONS
# =====================================================================

a = {1, 2, 3, 4, 5}
b = {4, 3, 7, 8, 9}

# ---------------------------- UNION ----------------------------------
# All elements from both sets (duplicates removed)
u1 = a | b
print("Union using | :", u1)

u2 = a.union(b)
print("Union using .union():", u2)

# ------------------------- INTERSECTION -------------------------------
# Common elements from both sets
i1 = a & b
print("Intersection using &:", i1)

i2 = a.intersection(b)
print("Intersection using .intersection():", i2)

# --------------------------- DIFFERENCE -------------------------------
# Elements present in one set but NOT in the other
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}

print("a - b:", a - b)    # items in a but not in b
print("b - a:", b - a)    # items in b but not in a

# ---------------------- SYMMETRIC DIFFERENCE --------------------------
# Elements NOT common in both sets
print("Symmetric Difference (a ^ b):", a ^ b)

# =====================================================================
#                                   TUPLE
# =====================================================================
# Tuple -> IMMUTABLE sequence of elements.
# Syntax → ( ... )
# You cannot modify (add/remove/update) once created.

my_tuple = (1, 2, 3, 4, 5, 2)
my_tuple2 = (6, 7, 8)

# Accessing items using index
print(my_tuple[0])
print(my_tuple[2])

# ---------------------------------------------------------------------
# CONCATENATION (creates a NEW tuple)
# ---------------------------------------------------------------------
print("Concatenated tuple:", my_tuple + my_tuple2)

# ---------------------------------------------------------------------
# COUNT VALUE OCCURRENCES
# ---------------------------------------------------------------------
# count() → how many times a value appears
print("Count of 2 in tuple:", my_tuple.count(2))

# =====================================================================
#                              END OF NOTES
# =====================================================================
