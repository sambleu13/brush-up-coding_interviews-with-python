from collections import defaultdict

student_grades = defaultdict(list)

grades = [
    ('elliot', 91),
    ('neelam', 98),
    ('bianca', 81),
    ('elliot', 88),
]

for name, grade in grades:
    student_grades[name].append(grade)

print({name: grade for name in student_grades})
