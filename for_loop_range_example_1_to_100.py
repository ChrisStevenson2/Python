# For Loop with Range
# for number in range(1, 11, 3): #Steps through range of 1 to 10 skipping 3 e.g. 1 4 7 10
#   print(number)

total = 0
for number in range(1, 101):
  total += number
print(total)

# prints total of numbers between 1 - 100 
# another way to look at is that it is 50 pairs of 101
# write 1,    2,  3,  4,  5 ... 100
# write 100, 99, 98, 97, 96 ... 1
# they add to 101 and thus are 50 pairs of 101 == 5050  (50 * 101)