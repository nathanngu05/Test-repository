name = []
all_name = []
student_name = ""
number = 0
total_grade = 0

student_name = input("Name of student: ").upper()
grade = int(input("Student grade: "))
highest_grade = grade
name.append(student_name)
all_name.append(student_name)
total_grade += grade
number += 1


while student_name != "X":
    student_name = input("Name of student: ").upper()
    if student_name == "X":
        break
    grade = int(input("Student grade: "))
    total_grade += grade
    number += 1
    if grade >= highest_grade:
        highest_grade = grade
        name.clear()
        name.append(student_name)
        all_name.append(student_name)
    elif grade == highest_grade:
        name.append(student_name)
        all_name.append(student_name)

average = total_grade / number

for i in name:
    print("Highest mark: ", i, ":", highest_grade)
    print(f"average grade is: {average:.2f}" )

