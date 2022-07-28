# Write your code below
# Fizz Buzz game - if divisible by 3 "FIZZ" \n
# if divisible by 5 "BUZZ" \n 
# if divisible by both 3 & 5 "FIZZBUZZ"

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: 
  # Divisible or modulo by number (3 or 5)
    print("FizzBuzz") 
    # Replace number with word
  elif number % 3 == 0: 
  # Divisible or modulo by number 3
    print("Fizz") 
    # Replace number with word
  elif number % 5 == 0: 
  # Divisible or modulo by number 5
    print("Buzz") 
    # Replace number with word
  else:
    print(number) 
    # print all other numbers in sequence in range selection 
    # - reminder that range must be + 1 for top end number 
    # to be included inside range
    