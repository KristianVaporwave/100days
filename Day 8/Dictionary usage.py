student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score < 90 and score >= 81:
        student_grades[student] = "Exceedes expectations"
    elif score < 81 and score >= 71:
        student_grades[student] = "Acceptable"
    elif score < 71:
        student_grades[student] = "Fail"

print(student_grades)
