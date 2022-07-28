#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
passworda = ""
# empty string generated

for char in range(1, nr_letters + 1):
  passworda += random.choice(letters)

for char in range(1, nr_symbols + 1):
  passworda += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  passworda += random.choice(numbers)

print(passworda)

# End of easy version

# Begin of harder version

password_list = [] # empty list

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters)) 
  # determined by number of letters requested will 
  # add both upper and lower case letters to list

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols) 
  # determined by number of symbols you want to 
  # include and will add these to the list

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers) 
  # determined by the number of numeric values 
  # you want in your password and then add them 
  # to the list

#print(password_list)

random.shuffle(password_list) 
# shuffle the list to randomize it even further

#print(password_list)

password = ""
for char in password_list:
  password += char 
  # gather the random result and put it into 
  # a new unique string 

print(f"Your hard password is: {password}")
# display the newly generated password

# End of Harder version