str1 = "OPQ Tech"
str2 = "Harry"

# + → String concatenation (joining strings)
# print(str1 + str2)
# print(str1 + " " + str2)

# * → Repeat the string multiple times
# print(str2 * 3)

# Multi-line Strings → use ''' ... ''' or """ ... """
# s3 = """I'm learning Python 
# String 
# """
# print(s3)

# len() → gives the number of characters in a string (spaces included)
# print(len(str2))
# print("str1 len", len(str1))


# Indexing → each character has a position (index)
# Index starts from 0 (left to right)
# print(str2[0])  # first character
# print(str2[4])  # last character (for "Harry")
# print(str2[3])
# print("char 4th: ", str1[3])

# Negative indexing → starts from -1 (right to left)
# print(str2[-1])   # last char
# print(str2[-2])   # second last char


# Slicing: [start:end] → returns characters from start up to (end-1)
# s = "OPQ tech"
# print(s[0:3])   # chars from index 0 to 2
# print(s[4:])    # from index 4 to end
# print(s[:3])    # same as 0 to 2
# print(s[:])     # whole string
# print(s[4:6])   # specific range


# String case methods
# s = "OpQ tEch"
# print(s.lower())      # all lowercase
# print(s.upper())      # all uppercase
# print(s.title())      # first letter capital in every word
# print(s.capitalize()) # first letter capital of entire string


# strip → remove spaces from both ends
# lstrip → remove left spaces
# rstrip → remove right spaces
# s = "      Harry           "
# print(s)
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())


# replace → replace some text with new text
# msg = "Hello World"
# print(msg.replace("World", "OPQ"))


# count → counts how many times a substring appears
# text = "abdsfefvaabcrabd"
# print(text.count("a"))
# print(text.count("abd"))


# find() and index() → search inside string
# find() returns -1 if not found
# index() gives error if not found
# s = "OPQ tech"
# print(s.find("te"))
# print(s.find("add"))
# print(s.index("te"))
# print(s.index("add"))   # will cause error if "add" not found


# -------------------------------
# User Input + String Formatting
# -------------------------------

age = int(input("Enter age: "))     # converting input to integer
name = input("Enter name: ")        # input is string by default

print("Name: ", name)
print("Age: ", age)

# Normal string concatenation (convert age to string)
print("Hello : " + name + ", age: " + str(age))

# f-string (modern & recommended way)
print(f"Hello {name}, age {age}")
