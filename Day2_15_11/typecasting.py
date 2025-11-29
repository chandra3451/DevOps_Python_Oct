# converting a value from one data type to another

# int, float,str, bool

# int 

print(int(3.14))
print(int(True))
print(int(False))
print(int("123"))

# float 

print(float(3))
print(float(True))
print(float("13.5"))
# print(float("1,000"))
# print(float("abc"))

# str

print(str(123))
print(str(True))
print(str(123.345))

# bool

# 0 or 0.0 -> False
# other numbers (+ve, -ve ) -> True

# "" -> False
# "abc", "a" -> True 

print(bool(0)) 
print(bool(123))
print(bool(0.0)) 
print(bool(0.00001))

print(bool(""))
print(bool(" "))
print(bool("False"))
print(bool("0"))

# two - step 
print(int("3.14"))
print(int(float("3.14")))

print(int("123 45"))
print(int("  12345   "))