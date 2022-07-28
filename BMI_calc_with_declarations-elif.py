# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)
print("Your BMI value is: ")
print(bmi)
#print("Your BMI value as a whole number is: ")
#bmi_as_int = int(bmi)
#print(bmi_as_int)

if bmi < 18.5:
  print(f"Your bmi is {bmi}, You are underweight!")
elif bmi < 25:
  print(f"Your bmi is {bmi}, You are normal.")
elif bmi < 30:
  print(f"Your bmi is {bmi}, You are slightly overweight.")
elif bmi < 35:
  print(f"Your bmi is {bmi}, You are obese!")
else:
  print("You are clinically obese!!!")
