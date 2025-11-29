# Comparison Operators -> True or False


# Equality (==)

print(1==1)
print(1==2)
print(1.0==1)
print(True==1)

print("Darshan" == "darshan")
print("Darshan" == "Darshan")

print("---------------------------------")
# Inequality (!=)

print(1!=1)
print(1!=2)
print(1.0!=1)
print(True!=1)

print("Darshan" != "darshan")
print("Darshan" != "Darshan")

print("---------------------------------")

# Greater than (>)

print(3>2)
print(3>3.0)
print(3>4)

# Greater than Equality (>=)

print(3>=2)
print(3>=3.0)
print(3>=4)

# Less than (>)

print(3<2)
print(3<3.0)
print(3<4)

# Less than Equality (<=)

print(3<=2)
print(3<=3.0)
print(3<=4)

# Not allowed
print(1>"A")

# Logical Operators 

# and -> Both conditions must be True
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# or -> At least one condition must be True
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# not -> negates the bool value

print(not True)
print(not False)


print("---------------------------------")

# Python precedence - order of operations

# Highest to lowest priority

# 1. Parentheses ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. Comparison Operators 
# 6. not
# 7. and 
# 8. or 
# left to right 
print(2+3*4) # -> 3 * 4 = 12 -> 12 + 2 =14 
print(10-2+5) # 10 -2 = 8 -> 8+5= 13

print(5+ 2 * 3 ** 2)
#Order
# 3 ** 2= 9
# 2 * 9 = 18 
# 5 + 18 = 23


print(5+2 *3) # 3*2 = 6 -> 6+5 = 11
print((5+2) *3) # 7 * 3-> 21

print(10>5 and 3*2 ==6)
# Order
# 3*2 = 6
# 10 > 5 = True
# 6 == 6 -> True 
# True and True -> True


print(5+3 >6 or not 2==2)
# true or not true
# true or false
# true

