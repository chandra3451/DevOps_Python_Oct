# =====================================================================
#                               DICTIONARIES
# =====================================================================

# Dictionary Syntax:
# ------------------
# { key : value, key : value, ... }
# Keys must be UNIQUE
# Values can be duplicate
# Keys must be meaningful (labels)

# List  → index-based (ordered)
# Dict  → key-based (labelled data)


# =====================================================================
#                           CREATING DICTIONARIES
# =====================================================================

students = {1: "Darshan", 2: "ravi", 3: "Sam"}
print(students, type(students))

emp = {}        # empty dictionary

profile = {"name": "Darshan", "age": 30, "Phone": 768787}

# Duplicate key example
students01 = {1: "Darshan", 2: "ravi", 1: "Sam"}
# key 1 appears twice → last value kept ("Sam")
print(students01)


# =====================================================================
#                       ACCESSING DICTIONARY VALUES
# =====================================================================

students = {1: "Darshan", 2: "ravi", 3: "Sam"}
profile = {"name": "Darshan", "age": 30, "Phone": 768787}

# Direct access (throws error if key not found)
print(students[2])
print(profile["Phone"])
# print(students[6])   # ❌ KeyError

# Safe access using .get()
print(students.get(2))                 # returns value
print(students.get(6))                 # returns None
print(students.get(6, "Not found"))    # default message


# =====================================================================
#                     ADDING & UPDATING VALUES
# =====================================================================

students[2] = "Priya"    # update existing
students[4] = "Rahul"    # add new
print(students)

# update() → merge another dictionary
students.update({6: "name1", 7: "name2"})
print(students)

# setdefault() → add only if key does not exist
students.setdefault(8, "New")
print(students)


# =====================================================================
#                           REMOVING ITEMS
# =====================================================================

profile = {"name": "Darshan", "age": 30, "Phone": 768787}

res = profile.pop("name")    # remove key + return value
print(res)
print(profile)

del profile["age"]           # remove key-value
print(profile)

res = profile.pop("marks", "Not found")   # key missing → returns default
print(res)

profile.clear()              # remove all entries
print(profile)


# =====================================================================
#                       IMPORTANT DICTIONARY METHODS
# =====================================================================

profile = {"name": "Darshan", "age": 30, "Phone": 768787}

print(profile.keys())        # all keys
print(profile.values())      # all values
print(profile.items())       # all (key, value) pairs


# =====================================================================
#                          LOOPING IN DICTIONARY
# =====================================================================

profile = {"name": "Darshan", "age": 30, "Phone": 768787}

for k in profile.keys():
    print(k)                 # print only keys

for v in profile.values():
    print(v)                 # print only values

for k, v in profile.items():
    print(k, v)              # print key + value pairs


# =====================================================================
#                   MEMBERSHIP OPERATOR → checks ONLY keys
# =====================================================================

print("name" in profile)       # True
print("Darshan" in profile)    # False (values NOT checked)


# =====================================================================
#                              MERGING DICTS
# =====================================================================

# Using update()
a = {"x":1, "y":20}
b = {"a":11, "b":234}
a.update(b)
print(a)
print(b)

# update() overwrites same keys
a = {"x":1, "y":20}
b = {"a":11, "y":234}
a.update(b)        # y becomes 234
print(a)

# Using ** unpacking
a = {"x":1, "y":20}
b = {"a":11, "b":234}
combined = {**a, **b}
print(combined)


print("-----------------------------------------------------------")


# =====================================================================
#                     NESTED DICTIONARIES (DICT inside DICT)
# =====================================================================

students = {
    101: {
        "name": "kavya",
        "age": 30,
        "marks": [23, 3, 2, 343, 100],
        "present": True
    },
    102: {
        "name": "Sam",
        "age": 35,
        "marks": {"maths": 45, "social": 65},
        "present": True
    }
}

# Accessing nested values
print(students[101]["name"])
print(students[101]["marks"])
print(students[101]["marks"][2])        # list index
print(students[102]["marks"]["maths"])  # dict inside dict


# =====================================================================
#                     UPDATING NESTED DICTIONARY
# =====================================================================

students[101]["name"] = "Asha"
print(students)


# =====================================================================
#                  DELETING FROM NESTED DICTIONARY
# =====================================================================

del students[102]                  # remove entire record
del students[101]["name"]          # remove inner field
print(students)


# =====================================================================
#                     pop() INSIDE NESTED DICTIONARY
# =====================================================================

students = {
    102: {
        "name": "Sam",
        "marks": {"maths": 45, "social": 65}
    }
}

res = students[102]["marks"].pop("social")
print(res)
print(students)

res = students[102]["marks"].pop("english", "Not found")
print(res)
print(students)


# =====================================================================
#                 LOOPING THROUGH NESTED DICTIONARY
# =====================================================================

students = {
    101: {"name": "kavya", "age":30},
    102: {"name": "Sam", "age":35},
}

for k, v in students.items():
    print(k, v["name"])


# =====================================================================
#                   DICTIONARY COMPREHENSION
# =====================================================================

# Normal way
res = {}
for i in range(1, 6):
    res[i] = i * i
print(res)

# Comprehension way
result = {i: i*i for i in range(1, 6)}
print(result)

# =====================================================================
#                          END OF NOTES
# =====================================================================
