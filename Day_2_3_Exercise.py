# ********************** MY Solution ********************
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# There are 365 Days in a year
# There are 52 Weeks in a year
# There are 12 Months in a year
Days = 365
Weeks = 52
Months = 12

current_age_in_months = int(age) * int(Months)
print(f"You are currently  {current_age_in_months} months old")
current_age_in_weeks = round(int(age) * int(Weeks))
print(f"Your have currently lived for   {current_age_in_weeks} weeks")
current_age_in_days = round(int(age) * int(Days))
print(f"Your have experienced {current_age_in_days}  days so far ")
total_months = (90 * 12)
total_days = (90 * 365)
total_weeks = (90 * 52)

remaining_Days = (int(total_days) - int(current_age_in_days))
remaining_Weeks = (int(total_weeks) - int(current_age_in_weeks))
remaining_Months = (int(total_months) - int(current_age_in_months))

print(f"You have {remaining_Days} days, {remaining_Weeks} weeks, and {remaining_Months} months left. \n!!!!! SO MAKE THEM COUNT !!!!!")
# ******************** MY Solution - End ************************************************************************
# ***************************************** Angela's Solution
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = (f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining) months left.")
print(message)

# *************************************** Angela's Solution - End

#  ***************************************** INSTRUCTIONS and HINTS *********************************************
# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#
# https://waitbutwhy.com/2014/05/life-weeks.html
#
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
#
# You have x days, y weeks, and z months left.
#
# Where x, y and z are replaced with the actual calculated numbers.
#
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
#
# Example Input
# 56
#
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.
#
# e.g. When you hit run, this is what should happen:
#
# https://cdn.fs.teachablecdn.com/RjqBViZQpyVTv7XY6cfA
#
# Hint
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.
# Test Your Code
# Before checking the solution, try copy-pasting your code into this repl:
#
# https://repl.it/@appbrewery/day-2-3-test-your-code
#
# This repl includes my testing code that will check if your code meets this assignment's objectives.
#
# Solution
# https://repl.it/@appbrewery/day-2-3-solution
#
# ***********************************************************************************************************************
