'''
Code Blocks
'''
def greet(name):
    """This function greets the person passed in as a parameter"""
    print(f"Hello, {name}, Good morning!")
   
greet("Alice") # prints "Hello, Alice, Good morning!"

'''
Code Blocks
'''
a = 5
print(type(a)) # prints int

a = "Hello, World!"
print(type(a)) # prints str

'''
Code Blocks
'''
# Procedural
def add_numbers(a, b):
    return a + b
    
result = add_numbers(5, 10)
print(result)

# Object-Oriented
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return delf.length * self.breadth
        
r = Rectangle(5, 10)
print(r.area())

# Functional
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))

''' Each of these scripts will output 15, but each one approaches the problem from a different programming paradigm. '''

''' 
Code Blocks
'''
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

'''
Code Blocks
'''

''' simple example of using pandas and matplotlib together.'''

import pandas as pd
import matplotlib.pyplot as plt

# Creating a simple dataframe
data = {
    'Year': [2015, 2016, 2017, 2018, 2019],
    'Sales': [2000, 3000, 4000, 3500, 6000]
}
df = pd.DataFrame(data)

# Plotting data
plt.plot(df['Year'], df['Sales'])
plt.xlabel('Year')
plt.ylabel('Sales')
plt.show()

'''
Code Blocks
'''

''' example of using scikit-learn to perform linear regression:'''

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd

# Load dataset
url = "http://bit.ly/w-data"
dataset = pd.read_csv(url)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the algorithm
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Make predictions using the test set
y_pred = regressor.predict(X_test)

'''
Code Blocks
'''

''' simple script that renames all files in a directory with a ".txt" extension:'''

import os

folder_path = '/path/to/folder'

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        new_filename = filename.replace('.txt', '.text')
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

'''
Code Blocks
'''
if 5 > 2:
    print("Five is greater that two!")

'''
Code Blocks
'''

# Arithmetic Operators
x = 10
y = 5

print(x + y)  #output: 15
print(x - y)  #output: 5
print(x * y)  #output: 50
print(x / y)  #output: 2.0

# Comparison Operators
print(x > y)  #output: True
print(x < y)  #output: False
print(x == y) #output: False

'''
Code Blocks
'''

# String 1

s1 = 'Hello, World!'
s2 = "Hello, World!"

print(s1)  #output: Hello, World!
print(s2)  #output: Hello, World!

'''
Code Blocks
'''

# String 2 - concatenation & repetition

s1 = 'Hello, '
s2 = 'World!'

print(s1 + s2)  #output: Hello, World!
print(s1 *3)    #output: Hello, Hello, Hello,

'''
Code Blocks
'''

# Lists

list1 = [1, 2, 3, 4, 5]
list2 = ['apple', 'banana', 'cherry']

print(list1)  #output: [1, 2, 3, 4, 5]
print(list2)  #output: ['apple', 'banana', 'cherry']

print(list1[0])  #output: 1
print(list2[1])  #output: banana

'''
Code Blocks
'''

# Conditional Statements

x = 10
y = 5

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")

'''
Code Blocks
'''

# Loops   - While & For

# while loop
i = 0
while i < 5:
    print(i)
    i + 1

#for loop
for i in range(5):
    print(i)

# In both of these loops, the number from 0 to 4 will be printed

'''
Code Blocks
'''

# Functions

def greet(name):
    return f"Hello, {name}!"
    
print(greet("Alice"))  #output: Hello, Alice!

'''
Code Blocks
'''
my_tuple = (1, 2, 'three', True)
print(type(my_tuple)) #output: <class 'tuple'>

'''
Code Blocks
'''
my_dict = {'name': 'Alice', 'age': 25}   # Key Value Pair - Unique 
print(type(my_dict))  #output: <class 'dict'>

'''
Code Blocks
'''
# The following functions can be used to convert Python data types:
#    int(): converts a number to an integer
#    float(): converts a number to a float
#    str(): converts a value to a string
#    list(): converts a sequence to a lisr
#    tuple(): converts a sequence to a tuple
#    dict(): creates a dictionary from a sequence of key-value pairs
#    bool(): converts a value to a Boolean (True or False)
'''
Code Blocks
'''
# converting integer to a float
x = 10
print(float(x))  #output: 10.0

# converting float to integer
y = 20.5
print(int(y))  #output: 20

# converting integer to string
z = 100
print(str(z))  #output: '100'

'''
Code Blocks
'''
# Global Scope

x = 10 # Global variable

def func():
    print(x)  # Accessing the global variable inside a function
    
    func()  #output: 10


# Local scope

def func():
    y = 5 # Local variable
    print(y)  
    
    func() #output: 5
    print(y)  # Raises NameError: name 'y' is not defined

'''
Code Blocks
'''
# Aritmetic Operators

x = 10
y = 5

print(x + y)  # Addition, Output: 15
print(x - y)  # Subtraction, Output: 5
print(x * y)  # Multipliation, Output: 50
print(x / y)  # Division, Output: 2.0
print(x % y)  # Modulus (remainder of x/y), Output: 0
print(x ** y)  # Exponentiation (x to the power y), Output: 100000
print(x // y)  # Floor division (division that results into whole number), Output: 2

'''
Code Blocks
'''
# Comparison Operators

x = 10
y = 5

print(x == y)  # Equal to, Output: False
print(x != y)  # Not equal to, Output: True
print(x > y)   # Greater than, Output: True
print(x < y)   # Less than, Output: False
print(x >= y)  # Greater than or equal to, Output: True
print(x <= y)  # Less than or equal to, Output: False
'''
Code Blocks
'''
# Logical Operators

x = True
y = False

print(x and y) # Logical AND, Output: False
print(x or y)  # Logical OR, Output: True
print(not x)   # Logical NOT, Output: False
'''
Code Blocks
'''
# Assignment Operators

x = 10  # Assign 10 to x
x += 5  # Add 5 to x and assign the result to x (equivalent to x = x + 5)
x -= 5  # Subtract 5 from x and assign the result to x (equivalent to x = x - 5)
x *= 5  # Multiply x by 5 and assign the result to x (equivalent to x = x * 5)
x /= 5  # Divide x by 5 and assign the result to x (equivalent to x = x / 5)
'''
Code Blocks
'''
# Bitwise Operators

x = 10  # binary: 1010
y = 4   # binary: 0100

print(x & y)   # Bitwise AND, Output: 0 (0000)
print(x | y)   # Bitwise OR, Output: 14 (1110)
print(~x)      # Bitwise NOT, Output: -11 (-1011)
print(x ^ y)   # Bitwise XOR, Output: 14 (1110)
print(x >> y)  # Bitwise right shift, Output: 0 (0000)
print(x << y)  # Bitwise left shift, Output: 160 (10100000)
'''
Code Blocks
'''
# Membership Operators

list = [1, 2, 3, 4, 5]

print(1 in list)     # Output: True
print(6 in list)     # Output: False
print(6 not in list) # Output: True
'''
Code Blocks
'''
# Identity Operators

x = 5
y = 5
z = '5'

print(x is y)      # Output: True
print(x is z)      # Output: False
print(x is not z)  # Output: True
'''
Code Blocks
'''
# Order of Operator Precedence in Python

# 01. Parentheses ()
# 02. Exponentiation *
# 03. Bitwise NOT ~
# 04. Multiplication, division, modulo, and floor division ,/,%,//
# 05. Addition and subtraction +,-
# 06. Bitwise shift operators >>,<<
# 07. Bitwise AND &
# 08. Bitwise XOR ^
# 09. Bitwise OR |
# 10. Comparison operators ==,!=,>,>=,<,<=
# 11. Assignment operators =,+=,-=,*=,/=,%=,//=,**=,&=,^=,>>=,<<=,|=
# 12. Identity operators is, is not
# 13. Membership operators in, not in
# 14. Logical NOT not
# 15. Logical AND and
# 16. Logical OR or

x = 5 + 2 * 3  # multiplication has higher precedence, so 2*3 is evaluated first
print(x)  # Output: 11

y = (5 + 2) * 3  # parentneses have the hightes precedence, so 5+2 is evaluated first
print(y)  # Output: 21
'''
Code Blocks
'''
# Exercise 1
# Create a Python program that takes two numbers as inputs from the user, performs all basic arithmetic operations on these numbers, and prints the results.

# taking two numbers as inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# performing arithmetic operations
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2

# printing the results
print(f"The sum of {num1} and {num2} is: {add}")
print(f"The difference between {num1} and {num2} is: {subtract}")
print(f"The product of {num1} and {num2} is: {multiply}")
print(f"The quotient of {num1} and {num2} is: {divide}")

# Exercise 2
# Create a Python program that asks the user for a number and then prints whether the number is even or odd.

# asking the user for a number
num = int(input("Enter a number: ")

# checking whether the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# Exercise 3
# Create a Python program that uses comparison operators to compare two numbers provided by the user and prints whether they are equal, and if not, which one is larger.

# taking two numbers as inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# using comparison operators to compare the numbers 
if num1 == num2:
    print("The numbers are equal.")
elif num1 > num2:
    print(f"The number {num1} is larger.")
else:
    print(f"The number {num2} is larger.")

# Exercise 4
# Create a Python program that uses logical operators to determine whether a number input by the user is within a certain range.

# taking a number as input from the user
num = float(input("Enter a number: "))

# specify the range
lowwer_bound = 10
upper_bound = 20

# checking whether the number is within the range
if num >= lower_bound and num <= upper_bound:
    print(f"The number {num} is within the range of {lower_bound} and {upper_bound}.")
else:
    print(f"The number {num} is outside the range of {lower_bound} and {upper_bound}.")
    
'''
Code Blocks
'''
if condition:
    # code to execute if the condition is True

'''
Code Blocks
'''
x = 10

if x > 0:
    print("x is positive")

'''
Code Blocks
'''
x = -5

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

'''
Code Blocks
'''
x = 10
y = 20

if x == 10:
    print("x equals 10")
    
    if y == 20:
        print("y equals 20")
        print("Bothe conditions are true.")
'''
Code Blocks
'''
# ternary operators

x = 10
message = "Hello" if x == 10 else "Goodbye"
print(message)  # outputs: Hello
'''
Code Blocks
'''
# pass statement - used as a placeholder in the code -

x = 10

if x == 10:
    pass # TODO: add actual code here
'''
Code Blocks
'''
# use intermediate variables or complex conditional statements

# hard to read
if (x > 10 and x < 20) or (y > 30 and y < 40) or z > 50:
    print("Complex condition met")

# easier to read
is_x_in_range = x > 10 and x < 20
is_y_in_range = y > 30 and y < 40
is_z_large = z > 50

if is_x_in_range or is_y_in_range or is_z_large:
    print("Comp;lex condition met")
'''
Code Blocks
'''
# Avoid chaining comparison

# potentially confusing
if 0 < x < 10:
    print("x is a positive single digit number")

# clearer
if x > 0 and x < 10:
    print("x is a positive single digit number")
'''
Code Blocks
'''
# a best practice - to use the 'in' keyword when checking for the existence of a value in a collection in Python.

# Pythonic
if x in my_list:
    print("x is in my_list")

# Non-Pythonic
found = False
for item in my_list:
    if item == x:
        found = True
        break

if found:
    print("x is in my_list")

'''
Code Blocks
'''
# Using the'==' operator
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # Outputs: True    Both have same values inside and are equal

# Using the 'is' operator 
print(list1 is list2)  # Outputs: False    Two different objects (list1 & list2)
'''
Code Blocks
'''
# 'is' operator is often used with None, a singular instance in Python

x = None

if x is None:
    print("x is None")

'''
Code Blocks
'''
# For loops

# Traversing a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Outputs
# apple
# banana
# cherry

# Using range() in for loop
for i in range(5):
    print(i)

# Outputs
# 0
# 1
# 2
# 3
# 4

'''
Code Blocks
'''
# While loop - repeatedly executes a block of code as long as the given condition is true.

# Counting up with a while loop
count = 0
while count < 5:
    print(count)
    count += 1  # equivalent to count = count + 1

# Outputs:
# 0
# 1
# 2
# 3
# 4
'''
Code Blocks
'''
# Nested Loops

# A simple example of nested loops
for i in range(3):  # outer loop
    for j in range(3):  # inner loop
        print(i, j)

# Outputs
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
'''
Code Blocks
'''
# This example - the loop is terminated as soon as i equals 3

# Using break in a for loop
for i in range(5):
    if i == 3:
        break
    print(i)

# Outputs
# 0
# 1
# 2
'''
Code Blocks
'''
# This example - conditional skip of iteration and continuation of loop

# Using continue in a for loop
for i in range(5):
    if i == 3:
        continue
    print(i)

# Outputs
# 0
# 1
# 2
# 4
'''
Code Blocks
'''
# for loop with else clause
for i in range(5):
    print(i)
else:
    print("Loop has ended")

# Outputs:
# 0
# 1
# 2
# 3
# 4
# Loop has ended
'''
Code Blocks
'''
# List Comprehensions

# Using a list comprehension to create a new list
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]

print(squares)  # Outputs: [1, 4, 9, 16, 25]
'''
Code Blocks
'''
# Error handling

# Syntax error

# This line has a syntax erro because it's missing a closing parenthesis
print("Hello, world!"

# when run it will display a messagelike: 'SyntaxError: unexpected EOF while parsing'

# Exception error

# This line will raise an exception because you can't divide by zero
print(5 / 0)

# when run will give the following output:

# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
'''
Code Blocks
'''
# Handling Exceptions with try and except

try:
    # This line will raise an exception
    print(5 / 0)
except ZeroDivisionError:
    # This line will run if a ZeroDivisionError is raised
    print("You can't divide by zero!")
'''
Code Blocks
'''
# The else and finally clause in try/except clause

try:
    # This line won't raise an exception
    print("Hello, world!")
except:
    print("An error occurred!")
else:
    print("No errors occurred!")
finally:
    print("This line runs no matter what.")

# Outputs:
# Hello, world!
# No errors occurred!
# This line runs no matter what.
'''
Code Blocks
'''
# Raising Exceptions

# This line will raise a ValueError
raise ValueError("Tis is a custom error message.")
'''
Code Blocks
'''
# Assert Statement 

x = 5
assert x < 10, "x should be less than 10"

# doesn't show an AssertionError because value of x is less than 10

x = 15
assert x < 10, "x should be less than 10"

# Output:  AssertionError: x should be less than 10
'''
Code Blocks
'''
# Iterators

# Create an iterator object from a list
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# Output: 1
print(next(my_iter))

# Output: 2
print(next(my_iter))

# This will go on until a StopIteration exception is raised
'''
Code Blocks
'''
# Iterator protocol  '__iter__()' and '__next__()'

# Example - simple iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyIterator:
    def __iter__(self):
        self.a = 1
        return self
        
    def __next__(self):
        x = self.a
        self.a += 1
        return x

# Create an object of the iterator
my_iter = MyIterator()

# Use next() to get the next items in the iterator
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
'''
Code Blocks
'''
# Iterating over a string
for char

in "Hello":
    print(char)

# Output:
# H
# e 
# l 
# l
# o 
'''
Code Blocks
'''
# Python Tools   - itertools.chain:

import itertools

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

# Output:
# 1
# 2
# a
# b 
'''
Code Blocks
'''
# Python Tools    - itertools.cycle:

import itertools

for item in itertools.cycle('ABC'):
    if counter == 6:
        break
    print(item)
    counter += 1

# Output:
# A
# B 
# C 
# A 
# B 
# C 
'''
Code Blocks
'''
# Python Tools    - itertools.count:

import itertools

for i in itertools.count(10):
    if i > 15:
        break
    print(i)

# Output:
# 10
# 11
# 12
# 13
# 14
# 15
'''
Code Blocks
'''
# Python Generators

# Generator function
def count_up_to(n):
    i = 1
    while i <= n:
        yield i 
        i += 1

#Create generator by calling it
counter = count_up_to(5)

# iterate over it
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
# and so on...

counter = count_up_to(5)
for num in counter:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# essential for working with data streams and large data files
'''
Code Blocks
'''
#Practice Exercises

# Conditional Statements
# Create a Python program that asks the user for an integer and prints whether the number is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Loops
# Write a Python program that prints all the numbers from 0 to 6 except 3and 6.
for x in range(6):
    if (x == 3 or x == 6):
        continue
    print(x, end=' ')

# Error and Exception Handling
# Write a Python program that prompts the user for an integer and prints the square of it. Use a while loop with a try/except block to account for incorrect inputs.
while True:
    try:
        n = int(input("Enter an integer: "))
        print("The square of the number is", n**2)
        break
    except ValueError:
        print("That was not a valid integer. Please try again...")

# Iterables and Iterators
# Create a Python iterator that returns the Fibonacci series. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
class Fibonacci:
    def __iter__(self):
        self.a = 0
        self-b = 1
        return self
        
    def __next__(self):
        fib = self.a 
        self.a, self.b = self.b, self.a + self.b 
        return fib
    
fib = Fibonacci()
for i in range(10):
    print(next(fib), end=" ")
'''
Code Blocks
'''
# Function 
# def function_name(parameters):
#     function body
#     statements

# Example - a simple function that take two numbers as parameters and prints their sum:
def add_numbers(num1, num2):
    sum = num1 + num2
    print(sum)
# Call the function
add_numbers(3, 5)
# This will output: 8

# can also return a value back
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

result = add_numbers(3, 5)
print(result)  # Output: 8

'''
Code Blocks
'''
# Defining a Default value for a Function
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Alice")  #Outputs: Hello, Alice
greet("Bob", "Good morning")  #Outputs: Good morning, Bob
'''
Code Blocks
'''
# *args and **kwargs  for Modularity of Code
# Example using

def print_args(*args):
    for arg in args:
        print(arg)

print_args("Alice", "Bob", "Charlie")
# Outputs:  Alice
#           Bob
#           Charlie

def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

print_kwargs(name="Alice", age=25)
# Outputs: name = Alice
#          age = 25
'''
Code Blocks
'''
# Variables defined locally or globally

def my_function():
    local_var = "I'm local!"
    print(local_var)

# when calling function
my_function()  # Outputs: I'm local!
# when calling a local function globally
print(local_var)  # Outputs: NameError: name 'local_var' is not defined

global_var = "I'm global!"

def my_function():
    print(global_var)
    
# when calling function
my_function()  # Outputs: I'm global!
print(global_var)  # Outputs: I'm global!
'''
Code Blocks
'''
def outer_func():
    x = 10 # enclosing function variable
    def inner_func():
        nonlocal x
        x = 20  # modifies the variable in the nearest enclosing scope
    inner_func()
    print(x)  # Outputs: 20

outer_func()
'''
Code Blocks
'''
# Use descriptive Variable Names. Best practice is to not name them the same as any Built-In function 

# Good 
def calculate_average(nums):
    return sum(nums) / len(nums)

# Bad
def a(n):
    return sum(n) / len(n)
'''
Code Blocks
'''
# Best practice for a function is to keep it simple. Performs a single task
# Easier to test and debug
'''
Code Blocks
'''
# Modules - individual Python files can be used to define functions, classes, or variables to be used in other Python files or programs

# Create a math_operations file 

# math_operations.py

# Enter the math functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a / b 

# Can be used in some other Python source file

# Some other Python File

import math_operations

result = math_operations.add(10, 5)
print(result)  # Outputs: 15
'''
Code Blocks
'''
# You can specify to add only one of the specific functions
from math_operations import add

result = add(10, 5)
print(result)  # Outputs: 15
'''
Code Blocks
'''
# To create a Package or grouping of Python Files

my_package/
    __init__.py
    module1.py
    module2.py


from my_package import module1, module2

result1 = module1.some_function()
result2 = module2.some_function()
'''
Code Blocks
'''
# Factorial Function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5)) # Outputs: 120

# Another way 

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Outputs: 120

'''
Code Blocks
'''
# Exercises to practice

# Writing and Calling a Function 
# Write a Python function that takes a list of numbers as input and returns their average. Call this function with a list of numbers and print the result.

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
print(calculate_average(numbers)) # Outputs: 30

# Understanding Variable Scope
# Examine the code below and predict what it will output. Then run it to check your understanding.

def my_func():
    inner_variable = "I'm inside the function"
    print(inner_variable)   # Local Variable within a Function

inner_variable = "I'm outside the function"
my_func()
print(inner_variable)       # Global Variable outside a Function

# Importing and Using a Module

# Import the math module and use it to calculate the square root of 16.

import math

print(math.sqrt(16))  # Outputs: 4.0

# Recursive Function
# Write a recursive function to calculate the factorial of a number. Call this function with the number 5 and print the result.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Outputs: 120

# Error Handling
# Modify the function from Exercise 1 (Write a Python function that takes a list of numbers as input and returns their average. Call this function with a list of numbers and print the result.) 
# to handle the case where the input list is empty (and thus the average is undefined). It should raise an exception with an appropriate error message in this case.

def calculate_average(numbers):
    if len(numbers) == 0:
        raise ValueError("The input list is empty")
    return sum(numbers) / len(numbers)

numbers = []
try:
    print(calculate_average(numbers))
except ValueError as e:
    print(e)
    
'''
Code Blocks
'''

# NOTES !!!!!!!!!
#
# Experiment with the concepts introduced. Write functions, explore different modules and packages, and see how far you can push recursion. 
# Use the tools to solve problems, to build something useful, or just to have fun.
# Apply them in more complex situations. The more you use them, the more comfortable you'll become with them, and the better you'll
# understand their potential. Keep experimenting, keep coding, and most importantly, keep learning.
# Remember that every great Pythonista started right where I am now. Keep up the good work.

# DEEP DIVE INTO DATA STRUCTURES

'''
Code Blocks
'''

numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares)  # Outputs: [1, 4, 9, 16, 25]

'''
Code Blocks
'''

numbers = [1, 2, 3, 4, 5]
even_squares = [number**2 for number in numbers if number % 2 == 0]
print(even_squares)  # Outputs: [4, 16]

'''
Code Blocks
'''

# Here's an example of a 2D array (a matrix) represented as a list of lists

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0]}  # Outputs: [1, 2, 3]
print(matrix[1][2])  # Outputs: 6

'''
Code Blocks
'''

numbers = [5, 2, 3, 1, 4]
numbers.sort()
print(numbers)  # Outputs: [1, 2, 3, 4, 5]

'''
Code Blocks
'''

# Descending Order

numbers = [5, 2, 3, 1, 4]
numbers.sort(reverse=True)
print(numbers)  # Outputs: [5, 4, 3, 2, 1]

'''
Code Blocks
'''

# Sorted() function is an excellent tool for anyone working with iterables.

numbers = (5, 2, 3, 1, 4)  # A tuple
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Outputs: [1, 2, 3, 4, 5]

'''
Code Blocks
'''

# Slicing Lists

numbers = [1, 2, 3, 4, 5]
middle_two = numbers[1:3]
print(middle_two)  # Outputs: [2, 3]

'''
Code Blocks
'''

last_two = numbers[-2:]
print(last_two)  # Outputs: [4, 5]

'''
Code Blocks
'''

# Tuples are an ordered collection of elements.

coordinates = (4, 5)
x, y = coordinates
print(x)  # Outputs: 4
print(y)  # Outputs: 5

'''
Code Blocks
'''

emplyee_directory = {
    ("John", "Doe"): "Front Desk",
    ("Jane", "Doe"): "Engineering",
}
print(emplyee_directory[("John", "Doe")])  # Outputs: "Front Desk"

'''
Code Blocks
'''

# Set Operations

# | = union
# & = intersection
# '' = difference
# ^ = symmetric difference

# Example:

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2)   # Outputs: {1, 2, 3, 4, 5, 6}
print(set1 & set2)   # Outputs: {3, 4}
print(set1 - set2)   # Outputs: {1, 2}
print(set1 ^ set2)   # Outputs: {1, 2, 5, 6}

'''
Code Blocks
'''

# Dictionary Comprehensions

numbers = [1, 2, 3, 4, 5]
squares = {number: number**2 for number in numbers}
print(squares)  # Outputs: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''
Code Blocks
'''



# Sorted() function is an excellent tool for anyone working with iterables.

numbers = (5, 2, 3, 1, 4)  # A tuple
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Outputs: [1, 2, 3, 4, 5]

'''
Code Blocks
'''

# Slicing Lists

numbers = [1, 2, 3, 4, 5]
middle_two = numbers[1:3]
print(middle_two)  # Outputs: [2, 3]

'''
Code Blocks
'''

last_two = numbers[-2:]
print(last_two)  # Outputs: [4, 5]

'''
Code Blocks
'''

# Tuples are an ordered collection of elements.

coordinates = (4, 5)
x, y = coordinates
print(x)  # Outputs: 4
print(y)  # Outputs: 5

'''
Code Blocks
'''

employee_directory = {
    ("John", "Doe"): "Front Desk",
    ("Jane", "Doe"): "Engineering",
}
print(employee_directory[("John", "Doe")])  # Outputs: "Front Desk"

'''
Code Blocks
'''

# Set Operations

# | = union
# & = intersection
# '' = difference
# ^ = symmetric difference

# Example:

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2)   # Outputs: {1, 2, 3, 4, 5, 6}
print(set1 & set2)   # Outputs: {3, 4}
print(set1 - set2)   # Outputs: {1, 2}
print(set1 ^ set2)   # Outputs: {1, 2, 5, 6}

'''
Code Blocks
'''

# Dictionary Comprehensions

numbers = [1, 2, 3, 4, 5]
squares = {number: number**2 for number in numbers}
print(squares)  # Outputs: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''
Code Blocks
'''

employee_directory = {
    ("John", "Doe"): "Front Desk",
    ("Jane", "Doe"): "Engineering",
}
print(employee_directory.keys())  # Outputs: dict_keys(['John Doe', 'Jane Doe'])
print(employee_directory.values())  # Outputs: dict_values(['Front Desk', 'Engineering'])
print(employee_directory.items())  # Outputs: dict_items([('John Doe', 'Front Desk'), ('Jane Doe', 'Engineering')])

'''
Code Blocks
'''

employee_skills = {
    "John": ["Python", "Java"],
    "Jane": ["C++", "JavaScript"],
}
print(employee_skills["John"])  # Outputs: ["Python", "Java"]

'''
Code Blocks
'''

# Mutable data structures - can be changed after creation
# lists, sets, and dictionaries
# lists can be modified as needed
# sets are similar to lists but guarantee that each element is unique
# dictionaries allow you to associate values with keys

# Immutable data structures - cannot be changed - can only create a new data structure that is based on the original one.
# tuples and strings
# useful where you need to store data that should not be modified accidentally or intentionally,
# tuple - coordinates in two-dimensional space
# string - name of a person or the title of a book

'''
Code Blocks
'''

# enumerate() function

languages = ["Python", "Java", "C++", "JavaScript"]
for i, language in enumerate(languages):
    print(f"Language (i): {language}")

'''
Code Blocks
'''

# items() method

employee_skills = {
    "John": ["Python", "Java"],
    "Jane": ["C++", "JavaScript"],
}
for name, skills in employee_skills.items():
    print(f"{name} knows {', '.join(skills)}.")

'''
Code Blocks
'''
# useful built-in fuctions
# len()
# min()
# max()
# sorted()

# can be extremely helpful when working with data. Whether need is to determine length of a collection,
# find its maximum or minimum values, or sort it in a particular order. These functions can save time and make code more efficient.

numbers = [4, 2, 9, 7]
print(len(numbers))  # Outputs: 4
print(max(numbers))  # Outputs: 9
print(min(numbers))  # Outputs: 2
print(sorted(numbers))  # Outputs: [2, 4, 7, 9]

'''
Code Blocks
'''

# Implementing Data Structures (Stack, Queue, Linked List, etc.)

# Stack = collection of elements that can be added or removed in a specific order
# Queues = similar to stacks but operate on a "first-in, first-out" basis
# Linked List = chains of nodes that can be traversed and manipulated

# Stack Example

stack = []

# Push elements onto stack
stack.append('A')
stack.append('B')
stack.append('C')
print(f"Stack: {stack}")  # Outputs: ['A', 'B', 'C']

# Pop elements from stack
print(f"Popped: {stack.pop()}")  # Outputs: 'C'
print(f"Stack after pop: {stack}")  # Outputs: ['A', 'B']

# Queue Example

from collections import deque

Queue = deque()

# Enqueue elements
queue.append('A')
queue.append('B')
queue.append('C')
print(f"Queue: {list(queue)}")  # Outputs: ['A', 'B', 'C']

# Dequeue elements
print(f"Dequeued: {queue.popleft()}")  # Outputs: 'A'
print(f"Queue after dequeue: {list(queue)}")  # Outputs: ['B', 'C']

# Linked List Example

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        new_node = Node(data)
        if self.head.data is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
    def display(self):
        elements = []
        cur_node = self.head
        while cur_node:
            elements.append(cur_node.data)
            cur_node = cur_node.next
        return elements
        
my_list = LinkedList()
my_list.append('A')
my_list.append('B')
my_list.append('C')
print(my_list.display())  # Outputs: ['A', 'B', 'C']

'''
Code Blocks
'''

# Tree Data Structure

class Node:
    def __init__(self, data=None):
        self.data = dataself.children = []
        
def add_child(node, data):
    node.children.append(Node(data))

root = Node('A')
add_child(root, 'B')
add_child(root, 'C')

'''
Code Blocks
'''

# Python's built-in functions and methods

# len():  Returns the number of items in a container

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # outputs: 5

# sort(): Sorts items in a list in ascending order

my_list = [5, 3, 1, 4, 2]
my_list.sort()
print(my_list)  # Outputs: [1, 2, 3, 4, 5]

# min() and max(): Returns the smallest and largest items, respectively

my_list = [5, 3, 1, 4, 2]
print(min(my_list))  # Outputs: 1
print(max(my_list))  # Outputs: 5

# List Comprehensions: Provides a compact way to filter and modify the elements in a list

my_list = [1, 2, 3, 4, 5]
squares = [x**2 for x in my_list if x % 2 == 0]  # Only calculates 'even' square root results
print(squares)  # Outputs: [4, 16]

'''
Code Blocks
'''

# Define a class
class Dog:
    # A simple class attribute
    species = "Canis Familiaris"
    
    # Initializer / instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create instances of the Dog class
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

# Access the instance attributes
print(buddy.description())  # Outputs: Buddy is 9 years old
print(miles.description())  # Outputs: Miles is 4 years old

# Call our instance methods
print(buddy.speak("Woof Woof"))  # Outputs: Buddy says Woof Woof
print(miles.speak("Bow Wow"))  # Outputs: Miles says Bow Wow

 '''
Code Blocks
'''
# Inheritance class example

# Parent class
class Bird:
    def __init__(self):
        print("Bird is ready")
    
    def whoisThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")

# Child class
class Penguin(Bird):
    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")
    
    def whoisThis(self):
        print("Penguin")
    
    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()  # Outputs: Penguin
peggy.swim()   # Outputs: Swim faster
peggy.run()   # Outputs: Run faster

'''
Code Blocks
'''

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

'''
Code Blocks
'''
# Another example of Class Inheritance

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

square = Square(4)
print(square.area())  # Outputs: 16
print(square.perimeter())  # Otputs: 16

'''
Code Blocks
'''

# Overriding class

class Bird:
    def intro(self):
        print("There are many types of birds.")
    
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

b1 = Bird()
b2 = Sparrow()
b3 = Ostrich()

b1.intro()
b1.flight()

b2.intro()
b2.flight()

b3.intro()
b3.flight()

'''
Code Blocks
'''
# Example of Polymorphism

class Bird:
    def intro(self):
        print("There are many types of birds.")
    
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
    
'''
Code Blocks
'''   

# Encapsulation - a way to protect data and ensure proper use within a program - leading double underscore

class Computer:
    
    def __init__(self):
        self.__maxprice = 900   #note double underscore in front of maxprice
    
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the pricec.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

'''
Code Blocks
'''

# __str__ & __repr__   Methods for string representation of a class

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'Employee[name={self.name}, age={self.age}]'
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.age!r})'
    
    emp = Employee('John Doe', 30)
    print(str(emp))  # Outputs: Employee[name=John Doe, age=30]
    print(repr(emp))  # Outputs: Employee('John Doe', 30)

'''
Code Blocks
'''

# __add__ and __sub__    Methods used to overload the + and - operator

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __str__(self):
        return f'{self.real} + {self.imag}i'

c1 = Complex(1, 2)
c2 = Complex(2, 3)
c3 = c1 + c2
c4 = c1 - c2
print(c3)  # Outputs: 3 + 5i
print(c4)  # Outputs: -1 - 1i

'''
Code Blocks
'''
# __len__    Method " returns the length (number of items in a collection) Should only be implemented for classes that are collections.

class Stack:
    def __init(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def __len__(self):
        return len(self.items)

s = Stack()
s.push('Hello')
s.push('World')
print(len(s))  # Outputs:  2

'''
Code Blocks
'''

#  __getitem__ and __setitem__   Methods used to implement self[key] for access (get) and assignment to self[key]  (set) respectively

class CustomDict:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, key):
        return self.items[key]
    
    def __setitem__(self, key, value):
        self.items[key] = value

custom_dict = CustomDict({'one': 1, 'two':2})
print(custom_dict['one'])  # Outputs: 1
custom_dict['three'] = 3
print(custom_dict['three'])  # Outputs: 3

'''
Code Blocks
'''

# __eq__ and __ne__  Methods used to overload the (==) and (!=) operators respectively

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __eq__(self, other):
        return self.id == other.id
    
    def __ne__(self, other):
        return self.id != other.id

emp1 = Employee('John', 'E101')
emp2 = Employee('Jane', 'E102')
emp3 = Employee('David', 'E101')

print(emp1 == emp2)  # Outputs:  False
print(emp1 == emp3)  # Outputs:  True
print(emp1 != emp3)  # Outputs:  False

'''
Code Blocks
'''

# __del__   Method known as a destructor method. Called when all references to the object have been deleted or garbage collected

class Test:
    def __init__(self):
        print('Constructor Executed')
    
    def __del__(self):
        print('Destructor Executed')

t1 = Test()  # Outputs: Constructor Executed
t1 = None  # Outputs: Destructor Executed

'''
Code Blocks
'''

# Decorators - Modify the behavior  of a function, method, or class definition

# Basic example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# When you run this code you will see:
# 
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
#

'''
Code Blocks
'''
  
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
    
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("World")   # Outputs:  
                 # Hello World
                 # Hello World
                 # Hello World

'''
Code Blocks
'''

# Abstract Base Class

from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    
    @abstractmethod
    def do_something(self):
        pass
        
class AnotherSubclass(AbstractClassExample):
    def do_something(self):
        super().do_something()
        print("The subclass is doing something")

x = AnotherSubclass()
x.do_something()

'''
Code Blocks
'''

from collections.abc import MutableSequence

class MyList(MutableSequence):
    def __init__(self, data[]):
        self.data = data
    
    def __delitem__(self, index):
        self.data[index]
        
    def __getitem__(self, data[]):
        self.data[index]
        
    def __len__(self):
        return len(self.data)
        
    def __setitem__(self, index, value):
        self.data[index] = value
        
    def insert(self, index, value):
        self.data.insert(index, value)
 
 mylist = MyList([1, 2, 3, 4])
 print(mylist[2])  # Outputs: 3
 mylist[2] = 7
 print(mylist[2])  # Outputs: 7
 
 '''
 Code Blocks
 '''
 
 # Overloading Operator
 
 class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    
    def __add__(self, other):   # special method defined to overload the + operator
        x = self.x + other.x
        y = self.y + other.y 
        return Point(x, y)

p1 = Point(2, 3)
p2 = Point(-1, 2)
print(p1 + p2)  # Outputs: (1,5)

'''
Code Blocks
'''

# Metaclasses  - a class that defines the behavior of other classes
# They're the mechanism behind many of Python's "magic" features
# Can give deeper understanding of Python's object model, and be beneficial in understanding of how advanced
# Python libraries work under the hood.

class Meta(type):
    def __new__(meta, name, bases, dct):
        x = super().__new__(meta, name, bases, dct)
        x.attr = 100
        return x

class MyClass(metaclass=Meta):
    pass

print(MyClass.attr)  # Outputs: 100

'''
Code Blocks
'''

# Practical Exercises

# Class Definition and Object Creation

# Define a class Student with two attributes: name and grade. The grade should be a float between 0 and 100. 
# Implement a method pass_or_fail that prints "Pass" if the grade is 60 or above, and "Fail" otherwise.

class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def pass_or_fail(self):
        if self.grade >= 60:
            print("Pass")
        else:
            print("Fail")

# Test the Student class
student1 = Student("Alice", 85)
student1.pass_or_fail()  # Outputs: Pass

# Next Exercise

# Inheritance and Polymorphism

# Create a class Animal with a method speak that prints "I don't know what I say". Then create two classes
# Dog and Cat that inherit from Animal and override the speak method to put "Woof" and "Meow" respectively.

class Animal:
    
    def speak(self):
        print("I don't know what I say")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

# Test the Dog and Cat classes
dog = Dog()
dog.speak()  # Outputs: Woof

cat = Cat()
cat.speak()  # Outputs: Meow

# Next Exercise

# Encapsulation

# Create a class Car with two attributes: speed and max_speed. The speed should be initially 0 and the
# max_speed should be set during the initialization. Implement methods accelerate and brake that
# increase and decrease the speed, respectively. The accelerate method should not allow the speed
# to go over the max_speed.

class Car:
    def __init__(self, max_speed):
        self.speed = 0
        self.max_speed = max_speed
    
    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += 10
            if self.speed > self.max_speed:
                self.speed = self.max_speed
    
    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            if self.speed < 0:
                self.speed = 0

# Test the Car class
car = Car(100)
car.accelerate()
print(car.speed)  # Outputs: 10
car.accelerate()
print(car.speed)  # Outputs: 20
car.brake()
print(car.speed)  # Outputs: 10

'''
Code Blocks
'''

# Opening a file

file = open('example.txt')  # Opens example.txt file in default mode of read only

# open(filename, mode) 
# modes:  
# 'r'  = read-only
# 'w' = write 
# 'a' = append
# 'r+' = read/write mode

# Reading from a file

content = file.read()  # Reads the entire file
print(content)  # Outputs: entire file info is displayed

# Writing to a file

file = open('example.txt', 'w')  # Opens the file in write mode
file.write('Hello, world!')  # Writes 'Hello, world!' to the file

# Closing a file

file.close()

'''
Code Blocks
''' 

# Exception Handling

try:
    file = open('non_existent_file.txt', 'r')
    file.read()
except FileNotFoundError:
    print('The file does not exist.')
finally:
    file.close()

# With Statement - for better resource management

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Binary File operations

with open('example.bin', 'wb') as file:
    file.write(b'\\x00\x0F')  # writes two bytes into the file

# Example of serialization with pickle

import pickle

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# To load data back in from pickle

with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)

print(data_loaded)

'''
Code Blocks
'''

# File Path 

import os

# Get the current working directory
cwd = os.getcwd()
print(f'Current working directory: {cwd}')

# Change the current working directory
os.chdir('/path/to/your/directory')
cwd = os.getcwd()
print(f'Current working directory: {cwd}')

# Join path components and split path components

# Join two or more pathname components
path = os.path.join('/path/to/your/directory', 'myfile.txt')
print(f'Path: {path}')

# Split the pathname path into a pair, (head, tail)
head, tail = os.path.split('/path/to/your/directory/myfile.txt')
print(f'Head: {head}, Tail: {tail}')

# pathlib 

from pathlib import Path

# Creating a path object
p = Path('/path/to/your/directory/myfile.txt')

#Different parts of the path
print(p.parts)

# Name of file
print(p.name)

# Suffix of file
print(p.suffix)

# Parent directory
print(p.parent)

'''
Code Blocks
'''

# Context managers  __enter__  and __exit__

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('hello.txt') as f:
    content = f.read()
    print(content)

'''
Code Blocks
'''

# os module

import os

# Get the current working directory
print(os.getcwd())

# List all files and directories in the current directory
print(os.listdir())

# Change the current working directory
os.chdir('/path/to/your/directory')
print(os.cwd())

'''
Code Blocks
'''

# shutil

import shutil

# Copy the file at 'source' to 'destination'
shutil.copy2('path/to/source/file', '/path/to/destination/directory')

# This function shutil.copy2() preserves file metadata, like timestamps

'''
Code Blocks
'''

# Pickling Python objects

import pickle

# Define a Python object (a dictionary)
data = {"name": "John", "age": 30, "city": "New York"}

# Pickle the Python object to a file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

'''
Code Blocks
'''
# Un-pickle
import pickle
 
# Unpickle the Python object from a file
with open("data.pkl", "rb") as file:
    data_loaded = pickle.load(file)

print(data_loaded)  # Outputs: {"name": "John", "age": 30, "city": "New York"}

'''
Code Blocks
'''

# Using JSON to serialize Python data

import json

# Define a Python object (a dictionary)
data = {"name": "John", "age": 30, "city": "New York"}

# Serialize the Python object to a JSON String
data_json = json.dumps(data)

print(data_json)  # Outputs: {"name": "John", "age": 30, "city": "New York"}

# Using JSON to deserialize a JSON string back into a Python object

import json

# JSON string
data_json = '{"name": "John", "age": 30, "city": "New York"}'

# Deserialize the JSON string to a Python object
data_loaded = json.loads(data_json)

print(data_loaded)  # Outputs: {"name": "John", "age": 30, "city": "New York"}

'''
Code Blocks
'''

# Network tools

# Example of creating a simple server that listens for incoming connections:

import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
s.bind(('localhost', 12345))

# Listen for incoming connections (max 5 connections)
s.listen(5)

while True:
    # Establish a connection with the client
    c, addr = s.accept()
    print('Got connection from', addr)
    
    # Send a thank you message to the client
    c.send(b'Thank you for connecting')
    
    # Close the connection
    c.close()

'''
Code Blocks
'''

# Client Side connection example

import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect(('localhost', 12345))

# Receive data from the server
print(s.recv(1024))

# Close the connection
s.close()

'''
Code Blocks
'''

# Reference Counting and Garbage Collection

# Python program to explain memory management

# creating object
list1 = [1, 2, 3, 4] # memory is allocated

# reference count becomes zero
list1 = None

# When we set: 'list1 = None' the reference count of the list becomes zero and Python's memory manager deallocates the list from memory.

# garbage collection uses a combination of reference counting and cycle detection to identify objects that are no longer needed.

# Here is a simple example of the gc module in action

# Python program to illustrate
# use of gc module

import gc

# create a cycle
list = ['Python', 'Java', 'C++']
list.append(list)

print("Garbage collection thresholds:",
          gc.get_threshold())

'''
Code Blocks
'''

# Practical Examples

# Write a Python program to write the following lines to a file and then read the file.

lines = [
    "Python is an interpreted, high-level, general-purpose programming language.\\n",
    "It was created by Guido van Rossum and first released in 1991.\\n",
    "Python's design philosophy emphasizes code readability.\\n"
]

with open('myfile.txt', 'w') as f:
    f.writelines(lines)

with open('myfile.txt', 'r') as f:
    print(f.read())


# Use the contextlib's contextmanager decorator to create a context manager that prints "Entering" 
# when entering the context and "Exiting" when exiting the context.

import contextlib

@contextlib.contextmanager
def my_context():
    print("Entering")
    yield
    print("Exiting")

with my_context():
    print("In the context")


# Write a Python program to create a circular reference and show the reference count of the objects
# involved in the circular reference. Also, use the gc module to show that the garbage collector
# properly deallocates the circular reference.

import gc
import sys

class MyClass:
    def __init__(self, name):
        self.name = name
    
# Create a circular reference
a = MyClass('a')
b = MyClass('b')

a.other = b
b.other = a 

# Print reference counts
print("Reference count for a: ", sys.getrefcount(a))
print("Reference count for b: ", sys.getrefcount(b))

# Remove references
a = None
b = None

# Force garbage collection
gc.collect()

print("Garbage collector has run.")

'''
Code Blocks
'''

# Error and Exception Handling

# Basic example of an error
print(0 / 0)

# We get a ZeroDivisionError when we run this code

# Outputs: Traceback (most recent call last):
#            File "<stdin>", line 1, in <module>
#          ZeroDivisionError: division by zero

# This error will sto our program from running

# Sometimes we want out program to continue running
# This is where try/except block can be used

try:
    print(0 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Can handle multiple exceptions

try:
    # some code here
except (TypeError, ValueError) as e:
    print("Caught an exception:", e)
else:
    print("No exceptions were thrown.")
finally:
    print("This will always run.")
    
'''
Code Blocks
'''

# Custom Exception

pythonCopy code
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception")
except CustomError as e:
    print("Caught a custom exception:", e)

'''
Code Blocks
'''

class MyAppException(Exception):
    pass

'''
Code Blocks
'''

# Example of a custom exception that stores an error message

class MyAppException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

'''
Code Blocks
'''
# Exception example

def do_something():
    # something goes wrong
    raise MyAppException("Something went wrong in do_something!")

try:
    do_something()
except MyAppException as e:
    print(e)

'''
Code Blocks
'''

# Logging Example 

import logging

# By default, the logging module logs the message with a severity level of WARNING or above.
# You can configure the logging module to log events of all levels if you want.
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# These will not get logged because by default the severity level is WARNING
loging.info('This is an info message')
logging.debug('This is a debug message')

# This will output:
#    WARNING:root:This is a warning message
#    ERROR:root:This is an error message
#    CRITICAL:root:This is a critical message
 
# To configure logging

import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

# Another Example of logging

import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

'''
Code Blocks
'''

# Exercises

# 1. Creating a custom exception

# Define a new exception class called TooColdError that inherits from the built-in Exception class.
# Raise this exception in a function called check_temperature that takes a temperature value as an
# argument and raises TooColdError if the temperature is below 0.

class TooColdError(Exception):
    pass

def check_temperature(temp):
    # your code here

# Test your function
try:
    check_temperature(-5)
except TooColdError:
    print("Caught a TooColdError!")

# 2. Adding exception handling

# Modify the check_temperature function to handle the case where the argument passed is not a number.
# If this happens, print a friendly error message and return None.

def check_temperature(temp):
    # your code here

# Test your function with a non-number argument
result = check_temperature("hot")

# 3. Logging

# Create a logger and use it to log messages of various levels. Then, adjust the logging level of 
# the logger and observe how the logged messages change.

import logging

logger = logging.getLogger(__name__)
logger.setLevel(loging.INFO)

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Change the logging level and log some more messages
logger.setLevel(logging.ERROR)
# log the same set of messages and see what changes

# 4. Advanced logging

# Set up a logger to log messages to both the console and a file. Try adding a time stamp to the log messages.

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set up console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# Set up file handler
fh = logging.FileHandler("debug.log")
fh.setLevel(logging.DEBUG)

# Add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

'''
Code Blocks
'''
# Python Standard Libraries

# Text Processing Services

# Category of modules - essential for working with text and binary data
# formats include JSON and CSV
# string module - string manipulation functions
# re module - for working with regular expressions
# difflib module - useful for comparing sequences
# textwrap module - for wrapping and fill text
# unicodedata module - to access the unicode database
# stringprep - internet string preparation

# there are many others available for more specialized text processing

# Example
import string

# Get all printable characters
print(string.printable)

'''
Code Blocks
'''
# Binary Data Services

# essential for working with binary data formats.
# can mamipulate data in a way not possible for text data.
# struct module - useful for working with C-style binary data formats
# codecs module - used for encoding and decoding data between different character sets
# array module - for working with arrays of numeric data
# pickle module - for serializing objects
# io module - for working with binary data streams

# Example

import struct

# Pack data into binary format
binary_data = struct.pack('i', 12345)
print(binary_data)

'''
Code Blocks
'''
# Data Types

# Allows for greater flexibility in handling data of different types.
# datetime module - provides a range of tools for working with dates and times, including formatting and parsing
# collectons module - range of container types deque, defaultdict, OrderedDict - useful for complex data structures
# heapq module - provides heap queue algorithm
# queue module - used for implementing queues of various types
# array and struct module - used for working with binary data
# decimal module - precise decimal arithmetic

# Example

from datetime import datetime

# Get current date and time
now = datetime.now()
print(now)

'''
Code Blocks
'''
# Mathematical Modules

# math module - various math functions  like trigonometric, logarithmic, and exponential functions
# cmath module - for working with complex numbers
# random module - to generate pseudorandom numbers
# statistics module - functions like mean, median, and mode - help analyze data

# Example

import math

# Calculate the square root of a number
print(math.sqrt(16))

'''
Code Blocks
'''
# File and Directory Access

# pathlib module - allows manipulation of paths, files, and directories
# os.path module - perform common operations on file paths, joining and splitting
# tempfile module - convenient for creating temporary files and directories, useful for storing intermediate results or running tests
# These modules provide a range of functionality

# Example

import os

# Get the current working directory
print(os.getcwd())

'''
Code Blocks
'''

# JSON module - provides methods for manipulating JSON data, which is often used when interacting with many web APIs

# Example

import json

# Here is a dictionary
data = {"Name": "John", "Age": 30, "City": "New York")

# We can easily convert it into a JSON string
json_data = json.dumps(data)
print(json_data)  # Outputs: {'Name': 'John', 'Age': 30, 'City': 'New York'}

# And we can convert a JSON string back into a dictionary
original_data = json.loads(json_data)
print(original_data)  # Outputs: {'Name': 'John', 'Age': 30, 'City': 'New York'}

# Here is datetime module
from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(now)  # Outputs: current date and time

# Add 5 days to the current date
future_date = now + timedelta(days=5)
print(future_date)  # Outputs: date and time five days from now

'''
Code Blocks
'''

# Functional Programming Modules

# A programming paradigm that emphasizes the use of pure functions. Functions with no side effects that always returns the same output for the same input. 
# Focus is on the definition of a problem and the computation of the solution, which means, that instead of specifying how to perform a task,
# we specify what the task should achieve.

# functools module
# itertools module

# reduce() function from functools module - used to apply a function iteratively to a sequence of elements
# map() function can be used to apply a function to each element of a sequence and return a new sequence with results

# functools: one of the most widely used, decorator - functools.lru_cache    
# A decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls.

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(16)])

# itertools

# function itertools.count(10) returns an iterator that generates integers, indefinitely.

import operator
print(operator.add(1, 2)) # Output: 3
print(operator.mul(2, 3)) # Output: 6

'''
Code Blocks
'''
# Python Crash Course Exercises

# What is 7 to the power of 4 ? 
7 ** 4

# Split this string:    s = "Hi there Sam!"  
# into a list.
s = "Hi there Sam!"
s.split()

# Given the variables:  planet = "Earth"  , diameter = 12742
# Use .format() to print the following string:
# The diameter of Earth is 12742 kilometers.
planet = "Earth"
diameter = 12742

print('The diameter of {} is {} kilometers'.format(planet,diameter))
# or
print('The diameter of {a} is {b} kilometers'.format(a=planet,b=diameter))

# Given this nested list, use indexing to grab the word "hello"
lst = [1,2[3,4],[5,[100,200,['hello']],23,11]1,7]
# solution
lst[3][1][2][0]

# Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
# solution
d['k1'][3]['tricky'][3]['target'][3]

# What is the main difference between a tuple and a list?

# a tuple is immutable, wheras a list is mutable  - mutable objects can be changed

# Create a function that grabs he email website domain from a string in the form:
# user@domain.com
# So for example, passing "user@domain.com" would return: domain.com
def domainGet(email):
    return email.split('@')[1]
domainGet('user@domain.com')  # Outputs: domain.com

# Create a basic function that returns True if the word 'dog' is contained in the input string.
# Don't worry about edge cases like a punctuation being attached to the word dog, but do 
# account for capitalization.
def findDog(s):
    return 'dog' in s.lower().split()
findDog('Is there a dog here?')     # Outputs: True

s = 'Is there a dog here?'
'dog' in s.lower().split()  # Outputs: True

# Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.
def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count

countDog('This dog runs faster than the other dog dude!')   # Outputs: 2

# Use lambda expressions and the filter() function to filter out words from a list that don't started
# with the letter 's'. For example: 
#   seq = ['soup','dog','salad','cat','great']

# should be filtered down to: 
#   ['soup','salad']

seq = ['soup','dog','salad','cat','great']

list(filter(lambda word: word[0]=='s',seq))  # Outputs:  ['soup','salad']

# Final Problem
# You are driving a little too fast, and a police officer stops you. Write a function to return one
# of 3 possible results: "No ticket","Small ticket", or "Big Ticket". If your speed is 60 or less,
# the result is ""No Ticket". If speed is between 61 and 80 inclusive, the result is  "Small Ticket".
# If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean 
# value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed -5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'
    
caught_speeding(81, True)  # Outputs: 'Small Ticket'  because it is your birthday
caught_speeding(81, False) # Outputs: 'Big Ticket' because it is not your birthday and you are speeding

# NUMPY

# Anaconda install - conda install numpy
# Python install - pip install numpy

# NumPy Exercises

import numpy as np

# Create an array of 10 zeros
np.zeros(10)

# Create an array of 10 ones
np.ones(10)

# Create an array of 10 fives
np.ones(10) * 5
np.zeros(10) + 5

# Create an array of integers from 10 to 50
np.arange(10,51)

# Create an array of all the even integers from 10 to 50
np.aragne(10,51,2)

# Create a 3x3 matrix with values ranging from 0 to 8
np.arange(9).reshape(3,3)
# or
a = np.arange(9)
a.reshape(3,3)

# Create a 3x3 identity matrix
np.eye(3)

# Use NumPy to generate a random number between 0 and 1
np.random.rand(1)

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
np.random.randn(25)

# Create the following matrix: 
np.arange(1,101).reshape(10,10)/100
# another way
np.linspace(0.01,1,100).reshape(10,10)

# Create an array of 20 linearly spaced points between 0 and 1
np.linspace(0,1,20)

# NumPy Indexing and Selection
# Now you will be given a few matrices, and be asked to replicate te resulting matrix outputs
mat = np.arange(1,26).reshape(5,5)
mat

mat[2:,1:]
mat[3,4]
mat[:3,1:2]
mat[4,:]
mat[-1,:]
mat[3:5,:]

# Get the sum of all the values in mat
mat.sum()

# Get the standard deviation of the values in mat
np.std(mat)
# or
mat.std()

# Get the sum of all the columns in mat
mat.sum(axis=0)

# Pandas

# Anaconda install - conda install pandas
# Python install - pip install pandas

import numpy as np
import pandas as pd
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}
pd.Series(data = my_data)
pd.Series(data = my_data,index = labels)
# or a shorter way
pd.Series(my_data,labels)
pd.Series(arr,labels)
pd.Series(d)

# Pandas - DataFrames

import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)   # create a list of 100 random numbers 

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])  # A - E == Rows in table, W - Z == Columns in table

df    # Displays your table output to the screen

df['W'] # Displays just the W columns numbers

type(df['W'])  # pandas.core.series.Series

df[['W','Z']] # Displays both the W column and Z column

df['new'] = df['W'} + df['Y']  # Creates a new column in the Series

df.drop('new', axis=1,inplace=True)  # removes the new column

df.shape  # Outputs: (5, 4)    'a tuple'

df.loc['A']

df.iloc[2] # Gives the 'C' row info

df.loc['B','Y']  # a specific cell within the dataframe

df.loc[['A','B'],['W','Y']] # gives just the specific values in those corresponding cells

booldf = df > 0  # returns a display of the values in Boolean format True, False

df[booldf]  # passes values into dataframe where only positive integers are displayed, all others are NaN (not a number or less than zero)

df['W']>0  # returns Boolean values just for the W column

df[df['W']>0] # displays only values that are True

df[df['W']>0]['X']  # will show the X column

df[df['W']>0[['Y','X']]

# long version of the one line above

boolser = df['W']>0
result = df[boolser]
mycols = ['Y','X']
result[mycols]

#

df[(df['W']>0) & (df['Y']>1)]   # and operand

df[(df['W']>0) | (df['Y']>1)]   # or operand

df.reset_index()

newind = 'CA NY WY OR CO'.split()

df['States'] = newind

df

df.set_index('States')

#
# To work with SQL need to install tools

# install with pip or conda

# conda install sqlalchemy
# conda install lxml
# conda install html5lib
# conda install BeautifulSoup4
# conda install xlrd

# for pip just replace conda with pip
#

pd.read_csv('filename.csv')

df.to_excel('Excel_Sample2.xlsx',sheet_name='NewSheet')  # copies dataframe to a new excel spreadsheet in the working directory  (pwd)
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')  # reads a webpage into a dataframe and places it in memory under the label data

# to work with SQL 
from sqlalchemy import create_engine
engine = creat_engine('sqlite:///:memory:')   # for sqlite usage - other sql engines may differ 
df.to_sql('my_table',engine)
sqldf = pd.read_sql('my_table',con=engine)
sqldf

# SF Salaries 

import pandas as pd

sal = pd.read_csv('Salaries.csv')
sal.head()
sal.info()
sal['BasePay'].mean()
sal['OvertimePay'].max()
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]
# another way to find max 
sal.loc[sal['TotalPayBenefits'].idxmax()]
sal.iloc[sal['TotalPayBenefits'].argmax()]
sal.groupby('Year').mean()['BasePay']
sal.['JobTitle'].nunique()
# or
len(sal.['JobTitle'].unique())
sal['JobTitle'].value_counts().head(5)
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)
def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

sum(sal['Jobtitle'].apply(lambda x: chief_string(x)))
sal['title_len'] = sal['JobTitle.].apply(len)
sal[['TotalPayBenefits','title_len']].corr()

#
#
# Pandas Exercises - E-commerce Purchases Solutions
#
#

import pandas as pd                         # import pandas
ecom = pd.read_csv('Ecommerce Purchases')   # read a csv file into memory
ecom.head()                                 # show the header info
ecom.info()                                 # show the data information - more detail
ecom.columns                                # show the column titles
ecom['Purchase Price'].mean()               # show the average price
ecom['Purchase Price'].max()                # show the maximum price
ecom['Purchase Price'].min()                # show the minimum price
ecom['Language']=='en'                      # show values with english language only
ecom[ecom['Language']=='en'].count()        # count the number of english language values
len(ecom[ecom['Job']=='Lawyer'].index)      # count the number of job's that are lawyers
ecom['AM or PM'].value_counts()             # count the sales AM or PM
ecom['Job'].value_counts().head(5)          # display the top 5 jobs
ecom[ecom['Lot']=='90 WT']['Purchase Price']   # display the purchase price for a specific sale
ecom[ecom['Credit Card']==4926535242672853]['Email']  # display the email address of a specific customer
ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95].count()  # lists the customers with American Express credit cards that made purchases of 95 or higher
sum(ecom['CC Exp Date'].apply(lambda exp: exp[3:]== '25'))  # find all credic card expiring in 2025
ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)  # displays top 5 email providers of customers

# Python for Data Analysis - Matplotlib

# to install 
# conda install matplotlib
# pip install matplotlib

# official website for matplotlib   = matplotlib.org/index.html
# important page inside is the gallery tab - you can select the type of visualization and it will give you code samples to apply

# matplotlib concepts lecture in jupyter notebooks

import matplotlib.pyplot as plt
%matplotlib inline                   # for use with jupyter notebooks
plt.show()                           # to display the plot outside of jupyter notebooks in a python terminal

import numpy as np
x = np.linspace(0,5,11)  # create array 
y = x ** 2               # create array based off previous array only with squared values
x                        # display array x 
y                        # display array y 

# Functional plot
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.show()

plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()

# Object Oriented plot
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
plt.show()

fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes1.set_title('Larer Plot')
axes2.plot(y,x)
axes2.set_title('Smaller Plot')
plt.show()

fig,axes = plt.subplots(nrows=1,ncols=2)
axes.plot(x,y)
plt.show()

fig,axes = plt.subplots(nrows=3,ncols=3)
axes.plot(x,y)
plt.tight_layout()   # used to fix spacing concerns between plots
plt.show()

fig,axes = plt.subplots(nrows=1,ncols=2)
for current_ax in axes
current_ax.plot(x,y)
plt.show()

fig,axes = plt.subplots(nrows=1,ncols=2)

axes[0].plot(x,y)
axes[0].set_title('First Plot')
axes[1].plot(y,x)
axes[1].set_title('Second Plot')
plt.tight_layout()
plt.show()

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,x**2,label='X Squared')
ax.plot(x,x**3,label='X Cubed')

ax.legend(loc=0)  # loc=0 for best location
plt.show()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='purple',lw=3,ls='--',marker='0',alpha=0.5)  

# Seaborn

# install steps after pandas install

# conda install seaborn
# pip install seaborn

# to find seaborn documentation - google search - github seaborn python 

# Distribution Plots

import seaborn sns
%matplotlib inline

tips = sns.load_dataset('tips')
tips.head()
sns.distplot(tips['total_bill'])
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')  #hex plot
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')  #linear regression plot
sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')  # heat plot

sns.pairplot(tips)
sns.pairplot(tips,hue='sex',palette='coolwarm')

sns.kdeplot(tips['total_bill'])

sns.barplot(x'sex',y='total_bill',data=tips)
sns.boxplot(x='day',y='total_bill',data=tips)
sns.violinplot(x='day',y='total_bill',data=tips)
sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)
sns.stripplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips)

import seaborn sns
%matplotlib inline

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()
flights.head()
tc = tips.corr()
sns.heatmap(tc,annot=True)
flights.pivot_table(index='month',columns='year',values='passengers')
fp = flights.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(fp)
sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=1)
sns.clustermap(fp)

import seaborn sns
%matplotlib inline
iris = sns.load_dataset('iris')
iris.head()
g = sns.PairGrid(iris)
g.map(plt.scatter)

g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.distplot,'total_bill')

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'], scatter_kws={'s':50})

import seaborn sns
%matplotlib inline
tips = sns.load_dataset('tips')
tips.head()
sns.set_style('whitegrid')
sns.countplot(x='sex',data=tips)

# colormapping = matplotlib.org/examples/color/colormaps_reference.html


# Plotly and Cufflinks  data visualization

# Install them in Python

# pip install plotly
# pip install cufflinks

# website: https://plotly
# github for cufflinks:  https://github.com/santosjorge/cufflinks

import pandas as pd
inport numpy as np
from plotly import __version__
print(__version__)
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()


# Choropleth - Mapping

import plotly.plotly as py
import plotly.graph_objs as go

from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

init_notebook_mode(connected=True)

data = dict(type = 'choropleth',
           locations = ['AZ','CA','NY'],
           locationmode = 'USA-states',
           colorscale = 'Portland',
           text = ['text 1','text 2','text 3'],
           z = [1.0,2.0,3.0],
           colorbar = {'title':'Colorbar Title Goese Here'})

layout = dict(geo={'scope':'usa'})

choromap = go.Figure(data = [data],layout=layout)

iplot(choromap)

# Second Choropleth example

import pandas as pd
df = pd.read_csv('2011_US_AGRI_Exports')

df.head()

import plotly.plotly as py
import plotly.graph_objs as go

from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

init_notebook_mode(connected=True)

data = dict(type = 'choropleth',
           colorscale = 'YIOrRd',
           locations = df['code'],
           locationmode = 'USA-states',
           z = df['total exports'],
           text = df['text'],
           marker = dict(line = dict(color = 'rgb(255,255,255)',width=2)),
           colorbar = {'title':'Millions USD'})

layout = dict(title = '2011 US Agriculture Exports by State',
             geo = dict(scope='usa',showlakes = True,lakecolor='rgb(85,173,240)'))

layout

choromap2 = go.Figure(data = [data],layout=layout)

iplot(choromap2)

# Choropleth Maps - World

data = dict(type = 'choropleth',
           locations = df['CODE'],
           z = df['GDP (BILLIONS)'],
           text = df['COUNTRY'],
           colorbar = {'title':'GDP in Billions USD'})

layout = dict(title = '2014 Global GDP',
             geo = dict(showframe= False,
                       projection = {'type':"natural earth"}))

choromap3 = go.Figure(data=[data],layout=layout)

iplot(choromap3)

#

# Choropleth Maps Exercises - Solutions

# Global map to show power consumption in KWH

import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True)
import pandas as pd
df = pd.read_csv('2014_World_Power_Consumption')
df.head()
data = dict(type = 'choropleth',
           locations= df['Country'],
           colorscale = 'Viridis',
           reversescale = True,
           locationmode = 'country names',
           z = df['Power Consumption KWH'],
           text = df['Country'],
           colorbar = {'title':'Power Consumption KWH'})
           
layout = dict(title='2014 Power Consumption',
             geo = dict(showframe=False,projection={'type':'Mercator'}))

choromap = go.Figure(data = [data],layout=layout)
iplot(choromap,validate=False)

# USA map to show Election Values

import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True)
import pandas as pd

usdf = pd.read_csv('2012_Election_Data')
usdf.head()
data = dict(type='choropleth',
           colorscale='Viridis',
           reversescale = True,
           locations = usdf['State Abv'],
           z = usdf['Voting-Age Population (VAP)'],
           locationmode='USA-states',
           text = usdf['State'],
           colorbar={'title':'Voting Age Population'})

layout = dict(title='2012 Election Data',
             geo = dict(scope='usa',showlakes=True,lakecolor='rgb(85,173,240)'))

choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)

# 911 Calls Solutions


