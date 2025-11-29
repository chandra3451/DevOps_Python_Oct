# <name> = <value>
a = 10
b = 6

print(a, type(a))

print(a + b)
print(a * b)
print(a - b)
print(a / b)
print(a // b)

x = 10 
print(x)
x = 20
print(x, type(x))
x = "20"
print(x, type(x))

x= y= z = 0
print(x, y, z)

a, b = 1, 2
print(a, b)

# swap numbers
x, y = 5, 7
print(x, y)
x, y = y, x
print(x, y)

# Naming rules

# must start with a letter or _ 
# value, _value -> allowed
# 1value, $value -> not allowed
# contain letter, digits and _
# value_age12 -> allowed
# value@age -> not 

# can not be keyword

# snake_case -> my_var_name
# PascalCase -> MyVarName
# camelCase  -> myVarName

name = "My name is Darshan"
print(name)



x, y, z = 5, 7, 10
print(x,y,z, end=" ")
print(x,y,z, sep="|")