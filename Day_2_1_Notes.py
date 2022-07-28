#Data Types
# String = characters
# can be identified by ""
# example
print("Hello"[0]) # prints the first letter 'H'
print("Hello"[4]) # prints the letter in the fifth position 'o'
print("Hello"[-1]) # prints the last character 'o'
print("Hello World"[-1]) # prints the last character 'd'
print("123" + "456") # numbers in quotes are treated as strings not integers or floats

# Integer = Whole Numbers
print(123 + 345)
print(123_456_789) # to show that underscore is ignored - just for visual separation numerically

# Float = Numbers with decimal points

3.14159

# Boolean = True | False values

True
False

# notes
num_char = len(input("What is your name?"))
print(type(num_char)) # identifies the Data Type of num_char in this scenario

# converting a int type to a String 
num_char = len(input("What is your name?"))

new_num_char = str(num_char) #convert an integer to string

print("Your name has " + new_num_char + " letters in it.")

# to comment out code quickly 
# highlight code and press CTRL + /

a = (123)
b = str(123)
c = float(123)
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'>
print(type(c)) # <class 'float'>

print(70 + float(100.5)) # gives you value 170.5
print(str(123) + str(456)) # gives you concatenated 123456

# REMINDER for Math Operation and importance in calculations Keep track of 'PEMDASLR'
# Parenthesis
# Multiplaction or Division (by order Left to Right)
# Division
# Addition or Subtraction (by order Left to Right)
# Subtraction
# Direction to follow in determination of result - Left to Right

