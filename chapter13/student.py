class Student(object):
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        return self.name < other.name
    
students = [
    Student('A', 4.0),
    Student('B', 3.0),
    Student('C', 2.0),
    Student('D', 3.2)
]

# this sorts according to __lt__ defined in student. students remains unchanged.
students_sort_by_name = sorted(students)

for s in students:
    print(s.gpa)

# Sort students in-place by gpa
students.sort(key=lambda student: student.gpa)

print()
print()

for s in students:
    print(s.gpa)
