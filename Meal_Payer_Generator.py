import random # Import Module

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


num_items = len(names) # Identify the number of items 
#print(num_items)
random_choice = random.randint(0, num_items -1) # include the total of items in choice
#print(random_choice)
person_who_will_pay = names[random_choice] # Determine the individual from list that will pay based on random result
print(person_who_will_pay + " is going to buy the meal today.")

print("Alternate way usingthe .choice function")

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today. Using the choice function.")

