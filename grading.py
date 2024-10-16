#Eleonora
# 15 october
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = input("Input exam grade two: ")
# was one extra ")"

exam_3 = str(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_3] # missing commas and exam_three instead of exam_3
sum = 0
for grade in grades: # missing one letter in grade's'
  sum = sum + int(grade) # turn into integer

avg = sum / len(grade)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" # ' wrong 
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
elif avg <= 0 and avg >= 59: # avarage info missing
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")

else:
    print ("Student is passing.")
# missing parantaces ()
