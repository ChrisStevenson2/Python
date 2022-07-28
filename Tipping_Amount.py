#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill_a = input("What was the total bill? $")
tip = input("What percentage amount of tip would you like to give? 10, 12, or 15? ")
tip_calc = float(tip) / 100
#print(float(tip_calc))
total_with_tip = float(bill_a) * (1 + float(tip_calc))
tip_amount = float(total_with_tip) - float(bill_a)
tip_print = "{:.2f}".format(tip_amount)
print("Your suggested tip should be: $ " + tip_print)
#print("Total bill amount with suggest tip: $")
bill_b = float(total_with_tip)
print("Your total bill should be this amount: $",("{:.2f}".format(bill_b)))
#group = input("How many people are in your party? ")
#each_pay = (float(total_with_tip) / float(group))
#payment = round(float(each_pay), 2)
#formatted_payment = "{:.2f}".format(payment) # Converts to float with 2 decimals to the right of the .
#print("Each person should pay $ " + str(formatted_payment))

# ************************* Angela's Solution
#print("Welcome to the tip calculator!")
#bill = float(input("What was the total bill? $"))
#print(bill)
#tip = int(input("How much would you like to tip? 10, 12, or 15?"))
#print(tip)
#people = float(input("How many people to split the bill? "))
#print(people)
#bill_with_tip = tip / 100 * bill + bill
#print(bill_with_tip)
#alternate calculation of bill_with_tip
#bill_with_tip_alt = bill * (1 + tip / 100)
#print(bill_with_tip_alt)
#tip_as_percent = tip / 100
#print(tip_as_percent)
#total_tip_amount = bill * tip_as_percent
#print(total_tip_amount)
#total_bill = bill + total_tip_amount
#print(total_bill)
#bill_per_person = total_bill / people
#print(bill_per_person)
#final_amount = round(bill_per_person, 2)
#final_amount = "{:.2f}".format(bill_per_person)
#print(f"Everyone should contribute: ${final_amount}")
