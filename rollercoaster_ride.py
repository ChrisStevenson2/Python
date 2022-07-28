print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry,  you have to grow taller befor you can ride.") 

print("Condition for someone who is 120 cm")

print("*************** TO INCLUDE SOMEONE who is 120 cm tall  ------ change the if statement to ' >= ' instead of just ' > ' "

if height >= 120:
  print("You can safely ride because you are 120 cm or taller.")
else:
  print("You still need to grow to 120 cm or taller to ride the rollercoaster")

# ELIF Statement tests
if height >= 120: 
  print("you can ride the rollercoaster!")
  age = int(input("What is your age?")
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
 else:
   print("Sorry, you have to grow taller before you can ride the Rollercoaster.")
   