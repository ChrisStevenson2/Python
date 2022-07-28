############DEBUGGING#####################

# Describe Problem
#def my_function():
# #for i in range(1, 20): upper bound is
# #really 19 and the print statement will
# #not be performed. Unless it is changed
# #to be 21 as shown below. 
#  for i in range(1, 21):
#    if i == 20:
#      print("You got it")
#my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) # solution 
# #dice_num = randint(1, 6)
# #dice_num = 6 #- to reproduce error
# print(dice_imgs[dice_num])

# Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1944 and year <= 1980:
#   print("You are a Baby Boomer.")
# elif year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# else:
#   print("How old are you????")

# Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# #word_per_page == int(input("Number of words per page: ")) # problem looks to be the '==' should only be one '='
# word_per_page = int(input("Number of words per page: ")) # problem looks to be the '==' should only be one '='
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(f"total words in book are: {total_words}")

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])