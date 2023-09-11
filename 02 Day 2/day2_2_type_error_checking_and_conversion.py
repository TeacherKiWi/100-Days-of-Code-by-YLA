# Type Error, Type Checking and Type Conversion
# num_char = len(input("What is your name?"))

# 1.Type Error

# print("Your name has " + num_char + "characters.")
# Above shows TypeError: can only concatenate str (not "int") to str

# 2.Type Checking

# print(type(len(input("What is your name?")))) --this also works.
# print(type(num_char))

# 3.Type Conversion

# new_num_char = str(num_char)  # str() function for type conversion
# print("Your name has " + new_num_char + " characters.")

a = str(123)  # integer to string conversion
print(type(a))

a = float(123)  # integer to float conversion
print(type(a))

# print(70+"100.5")
# Above code will show TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(70 + float("100.5"))  # string to float conversion

print(str(70)+str(100))  # string concatenation

# In summary, you can use the type() function to investigate the data type you're working with.
