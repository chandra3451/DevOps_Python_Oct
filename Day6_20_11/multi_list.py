# -----------------------------------------
# 2D LISTS (LIST OF LISTS) — CLASS NOTES
# -----------------------------------------
# A 2D list is simply a list where each element is another list.
# This is commonly used to represent:
# - matrices
# - tables
# - student records
# - grids (rows & columns)

# -----------------------------------------
# BASIC SYNTAX
# -----------------------------------------
# 2D list = [ [row1_values], [row2_values], ... ]

matrix = [
    [1, 2, 3],   # row 0
    [4, 5, 6],   # row 1
    [7, 8, 9]    # row 2
]

# -----------------------------------------
# ACCESSING ELEMENTS
# -----------------------------------------
# matrix[row][col]
print(matrix[0][0])   # 1 (row0, col0)
print(matrix[1][1])   # 5 (row1, col1)
print(matrix[2][0])   # 7 (row2, col0)

# -----------------------------------------
# ACCESSING AN ENTIRE ROW
# -----------------------------------------
print("Row 1:", matrix[1])   # prints [4,5,6]


# -----------------------------------------
# IRREGULAR (JAGGED) 2D LISTS
# -----------------------------------------
# Different rows can have different lengths.
matrix1 = [
    [1, 2, 3],
    [4, 5],            # only 2 elements
    [7, 8, 9, 8]       # 4 elements
]
print("matrix1:", matrix1)


# -----------------------------------------
# EXAMPLE: STUDENT TABLE
#  [roll, name, marks]
# -----------------------------------------
students = [
    [1, "Asha", 85],
    [2, "Kavya", 65]
]

# Accessing a value
print("Student 1 name:", students[0][1])     # "Asha"

# Modifying nested list value
students[0][1] = "Sam"                       # change name
print("Updated name:", students[0][1])

# Replacing entire row
students[0] = [4, "Arun", 45]
print("Updated students table:", students)

# Deleting a row
del students[1]
print("After deleting row 1:", students)


# -----------------------------------------
# LOOPING THROUGH A 2D LIST
# -----------------------------------------
matrix = [
    [1, 2, 3],   # row 0
    [4, 5, 6],   # row 1
    [7, 8, 9]    # row 2
]

# Print matrix row by row
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()         # new line after each row

# Output:
# 1 2 3
# 4 5 6
# 7 8 9


# -----------------------------------------
# KEY POINTS SUMMARY
# -----------------------------------------
# 1. 2D list is a list containing other lists.
# 2. Access element → matrix[row][col]
# 3. Entire row → matrix[row]
# 4. You can modify and delete inner lists.
# 5. Nested loops are used to iterate through all values.
# 6. Rows can have different lengths (jagged list).

