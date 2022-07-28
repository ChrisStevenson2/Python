# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(type(two_digit_number)) # string data type
print(str(two_digit_number[0]))
print(str(two_digit_number[1]))
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])
print("convert string value of first number to an integer")
print(first_number)
print(type(first_number))
print("convert string value of second number to an integer")
print(second_number)
print(type(second_number))
print("Add the two values")
print(first_number + second_number) # Addition
print("Multiply the two values")
print(first_number * second_number) #multiplication
print("Divide the two values")
print(first_number / second_number) #division
print("Subtract the two values")
print(first_number - second_number) #subtraction
print("Below is and Alternative way to Add / Multilpy / Divide / Subtract the two values")
# Alternate way to accomplish this - Begin Code block
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result1 = int(first_digit) + int(second_digit) # by declaring these as int it converts them to numbers and then adds them together
result2 = int(first_digit) * int(second_digit) # by declaring these as int it converts them to numbers and then multiplies them together
result3 = int(first_digit) / int(second_digit) # by declaring these as int it converts them to numbers and then divides them 
result4 = int(first_digit) - int(second_digit) # by declaring these as int it converts them to numbers and then subtracts them together
result5 = int(first_digit) ** int(second_digit) # by declaring these as int it converts them to numbers and then raises them to the exponent or power designated by the second digit
print("Converts them in one line as Integers and then Adds the two values - displaying them in Results return")
print(result1) # displays the result
print(result2) # displays the result
print(result3) # displays the result
print(result4) # displays the result
print(result5) # displays the result
# Alternate way - End Code block

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# Try to find out the data type of two_digit_number.
# Think about what you learnt about subscripting.
# Think about type conversion.


print("# for numerical calculations remenber PEMDAS rule of the order of importance"\n"Parenthesis - Exponents - Multiplication - "\n"Division - Addition - Subtraction")  