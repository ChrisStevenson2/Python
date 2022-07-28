# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇 

total_height = 0
for height in student_heights:
  total_height += height
#print(total_height)

number_of_students = 0
for student in student_heights:
  number_of_students += 1
#print(number_of_students)

print(round(total_height / number_of_students))

# End of figuring them out using for loops

#

# Shorter version(s) using functions
student_heights1 = [180, 124, 165, 173, 189, 169, 146]

print("Number of students = ", len(student_heights1))
print("Total of everyone's height combined = ", sum(student_heights1))

print("Average height between all students in list = ", round(sum(student_heights1) / len(student_heights1)))
#
#
total_height2 = sum(student_heights1)
number_of_students2 = len(student_heights1)
average_height = round(total_height2 / number_of_students2)
print(average_height)




