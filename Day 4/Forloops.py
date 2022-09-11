student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_heights = 0
for height in student_heights:
  total_heights += height

number_of_stud = 0
for student in student_heights:
  number_of_stud += 1


print(total_heights)
print(number_of_stud)
print(total_heights / number_of_stud)

