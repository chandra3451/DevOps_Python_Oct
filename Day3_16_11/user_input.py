# input() → used to take input from the user
# Whatever we type through the keyboard will be taken as a string by default

# name = input("Enter name: ")
# print("Name: ", name, type(name))
# Here, name will always be a string (text), because input() returns string

# age = int(input("Enter age: "))
# print("Age: ", age, type(age))
# We use int() to convert the input value into an integer number

# Taking temperature as a float value
# float() is used when we want decimal numbers
temp = float(input("Enter temp: "))
print("Temp: ", temp, type(temp))
