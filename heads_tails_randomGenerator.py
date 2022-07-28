#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

print("--------- Heads or Tails ---------\n 🎲  🎲 Roll the dice game  🎲  🎲  \n\n")

Heads_or_Tails = random.randint(0, 1) 

if Heads_or_Tails == 0:
  print("Tails")
elif Heads_or_Tails == 1:
  print("Heads")