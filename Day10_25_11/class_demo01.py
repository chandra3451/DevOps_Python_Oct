# ================================================
#                OOPS – Classes & Objects
# ================================================

# Class → A template or blueprint
# Object → A real instance created from that class

# Analogy:
# Class  = Recipe
# Object = Dish made from that recipe
# The recipe stays the same, but every dish is separate.


# ====================================================
# EXAMPLE 1: Basic Class With Default (Class) Attributes
# ====================================================

class Person:
    # These are class attributes (same for all objects)
    name = "Sam"
    age = 20

# Creating object p1
p1 = Person()
print("P1 Object: ", p1)
print("P1 name: ", p1.name)  # Uses class attribute
print("P1 age: ", p1.age)

# Changing only p1's name (instance attribute)
p1.name = "Ravi"
print("P1 new name: ", p1.name)

print("---" * 10)

# Creating object p2
p2 = Person()
print("P2 name: ", p2.name)  # Still "Sam" → class attribute unchanged
print("P2 age: ", p2.age)

# 👉 Note:
# If you assign value to an attribute using object (p1.name),
# it creates an instance attribute overriding class attribute ONLY for that object.


# ====================================================
# EXAMPLE 2: Methods (Functions inside a class)
# ====================================================

class Person:
    # greet() is a method → function inside a class
    def greet(self):
        print("Hello!")
        return "Hi"

# Creating object
p1 = Person()

# Calling the method
# p1.greet() internally becomes → Person.greet(p1)
print(p1.greet())


# ====================================================
# EXAMPLE 3: Mathematics class with methods
# ====================================================

class Mathematics:
    
    # Factorial method
    def fact(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res
    
    # Product of all elements in a list
    def list_product(self, lst):
        res = 1
        for i in lst:
            res *= i
        return res

# Creating object
math = Mathematics()

print(math.fact(5))  # 5! = 120
print(math.list_product([1, 2, 4, 6, 8]))  # 1*2*4*6*8


# ====================================================
# EXAMPLE 4: __init__ → Constructor
# Called automatically when an object is created
# ====================================================

class Person:
    def __init__(self):  # Constructor
        print("Inside __init__")

    def run(self):
        print("Running!")

# Each object creation calls __init__()
p1 = Person()
p2 = Person()
p3 = Person()


# ====================================================
# EXAMPLE 5: __init__ with parameters
# ====================================================

class Person:
    def __init__(self, name):  # Accepts one parameter
        print("Inside __init__")
        print("Name passed: ", name)

    def run(self):
        print("Running!")

p1 = Person("Darshan")  # Pass value to __init__



# ====================================================
# EXAMPLE 6: Storing values using self
# ====================================================
# self → refers to the current object
# Used to store values inside the object

class Person:
    def __init__(self, name):
        print("Inside __init__")
        self.name = name   # Storing name inside the object

    def run(self):
        print("Running!", self.name)  # Access stored value using self.

p1 = Person("Darshan")
p1.run()  # Prints: Running! Darshan
