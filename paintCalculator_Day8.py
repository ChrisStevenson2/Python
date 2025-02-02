#Write your code below this line 👇

import math 

def paint_calc(height, width, cover): # function parameters
    num_cans = (height * width) / cover # math calculation for paint coverage
    print(num_cans) # result of calculation
    round_up_cans = math.ceil(num_cans) # rounding up to the nearest whole can of paint
    print(f"You'll need {round_up_cans} cans of paint.") # Display result of total cans needed for coverage

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: ")) # input question for height of wall
test_w = int(input("Width of wall: ")) # input question for width of wall
coverage = 5 # value of how much a can of paint will cover in meters
paint_calc(height=test_h, width=test_w, cover=coverage) # function with values differentiated by parameters


#Area Calc
#Instructions
#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#
#number of cans = (wall height ✖️ wall width) ÷ coverage per can.
#
#e.g. Height = 2, Width = 4, Coverage = 5
#
#number of cans = (2 ✖️ 4) ÷ 5
#
#                     = 1.6
#                     = 1.6
#But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
#
#IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.
#
#Example Input
#test_h = 3
#test_h = 3
#test_w = 9
#test_w = 9
#Example Output
#You'll need 6 cans of paint.
#You'll need 6 cans of paint.
#Hint
#1. To round up a number:
#
#https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
#
#Make sure you name your function/parameters the same as when it's called on the last line of code.
#Test Your Code
#Before checking the solution, try copy-pasting your code into this repl:
#
#https://repl.it/@appbrewery/day-8-1-test-your-code
#
#This repl includes my testing code that will check if your code meets this assignment's objectives.
#
#Solution
#https://repl.it/@appbrewery/day-8-1-solution
#
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

