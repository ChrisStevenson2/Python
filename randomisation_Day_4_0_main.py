import random
import my_module # created a second file called 'my_module with value of pi

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)

random_float = random.random()
print(random_float)

print(random_float * 5) # to include range from 0.0000000..... to 4.99999999.... 

love_score = random.randint(1, 100)
print(f"Your love score is: {love_score}")