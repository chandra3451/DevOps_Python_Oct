# ---------------------------------------------------------
# NESTED FOR LOOPS → A "for" inside another "for"
# Used when we want combinations or pairs.
# Example: Rolling 2 dice -> (1,1), (1,2)...(6,6)
# ---------------------------------------------------------

# Example 1: All pairs of 2 dice
# for i in range(1, 7):      # die 1: 1..6
#     for j in range(1, 7):  # die 2: 1..6
#         print(i, j)


# ---------------------------------------------------------
# Example 2: Print only pairs whose sum matches a target
# ---------------------------------------------------------
# target = 5
# for i in range(1, 7):
#     for j in range(1, 7):
#         if i + j == target:
#             print(i, j)  # only pairs that add up to 5


# ---------------------------------------------------------
# Example 3: Count how many pairs sum to target (2 dice)
# ---------------------------------------------------------
# target = 5
# count = 0
# total = 6 * 6    # total possible outcomes = 36

# for i in range(1, 7):
#     for j in range(1, 7):
#         if i + j == target:
#             count += 1

# print("Count:", count)

# prob = (count / total) * 100
# print("Probability:", round(prob, 2), "%")


# ---------------------------------------------------------
# Example 4: 3 nested loops (3 dice)
# Count combinations where sum == target
# ---------------------------------------------------------
# target = 5
# count = 0
# total = 6 * 6 * 6   # 216 total outcomes for 3 dice

# for k in range(1, 7):
#     for i in range(1, 7):
#         for j in range(1, 7):
#             if i + j + k == target:
#                 count += 1
#                 print(k, i, j)

# print("Count:", count)
# prob = (count / total) * 100
# print("Probability:", round(prob, 2), "%")


# ---------------------------------------------------------
# BREAK → stops loop immediately (premature exit)
# ---------------------------------------------------------
# target = 5
# for i in range(1, 11):
#     if i == target:
#         print("Stopped at:", target)
#         break   # exit the loop


# ---------------------------------------------------------
# CONTINUE → skip the current iteration, go to next
# ---------------------------------------------------------

# Example 1: print odd numbers using step
for i in range(1, 11, 2):
    print("Odd nums:", i)

# Example 2: skip even numbers using continue
for i in range(1, 11):
    if i % 2 == 0:      # if number is even
        continue        # skip printing it
    print("Odd nums:", i)

# Example 3: direct odd condition (no continue)
for i in range(1, 11):
    if i % 2 != 0:      # if number is odd
        print("Odd nums:", i)


# ---------------------------------------------------------
# FOR / ELSE → else runs ONLY if loop finishes normally
# (i.e., NOT interrupted by break)
# ---------------------------------------------------------

target = 15
for i in range(1, 11):
    if i == target:
        print("Found", target)
        break
else:
    # this else runs only if break never happened
    print("Not found")
