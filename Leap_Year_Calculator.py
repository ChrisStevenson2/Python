# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print("This solution uses elif entries to differentiate whether the year is a leap year or not.")
if (year%400 == 0): # input_year
  print("%d is a Leap Year" %year) # input_year
elif (year%100 == 0): # input_year
  print("%d is Not a Leap Year" %year) # input_year
elif (year%4 == 0): #input_year
  print("%d is a Leap Year" %year) # input_year
else:
  print("%d is Not a Leap Year" %year) # input_year

print("another solution could be this for nested if statements *** ANGELA'S Demonstration ***** - code results below:")
input_year = int(input("Enter the Year to be checked: "))
if(input_year%4 == 0):
  if(input_year%100 == 0):
    if(input_year%400 == 0):
      print("%d is Leap Year" %input_year)
    else:
      print("%d is Not a Leap Year" %input_year)
  else:
    print("%d is Leap Year" %input_year)
else:
  print("%d is Not a Leap Year" %input_year)

print("A third option would be to use Conditional statement - result below")
input_year2 = int(input("Enter the Year to be checked: "))
if (( input_year2%400 == 0)or (( input_year2%4 == 0 ) and ( input_year2%100 != 0))):
  print("%d is Leap Year" %input_year2)
else:
  print("%d is Not the Leap Year" %input_year2)

print("fourth option would be to use it as a function")

#function defined
def LeapYearCheck(input_year3):
  if (input_year3 % 4) == 0:
    if (input_year3 % 100) == 0:
      if (input_year3 % 400) == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
# Driver Code
input_year3 = int(input("Enter the Year to be checked: "))
if(LeapYearCheck(input_year3)):
  print(f" {input_year3} is a Leap Year")
else:
  print(f" {input_year3} is Not a Leap Year")
