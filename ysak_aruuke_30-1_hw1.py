class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print("Full Name:", self.fullname)
        print("Age:", self.age)
        print("Marital Status:", "Married" if self.is_married else "Single")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average(self):
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        return total_marks / num_subjects


class Teacher(Person):
    salary = 35000
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def calculate_salary(self):
        salary = self.salary
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * salary
            salary += bonus
        return salary


def create_students():
    student1 = Student("Justin Bieber", 16, False, {"Math": 90, "Science": 85, "History": 92})
    student2 = Student("Selena Gomez", 15, False, {"Math": 95, "Science": 87, "History": 88})
    student3 = Student("Ariana Grande", 17, False, {"Math": 88, "Science": 91, "History": 90})

    students = [student1, student2, student3]
    return students


teacher = Teacher("Taylor Swift", 35, True, 7, 35000)
teacher.introduce_myself()
print("Salary:", teacher.calculate_salary())


students = create_students()
for student in students:
    student.introduce_myself()
    print("Marks:", student.marks)
    print("Average Mark:", student.calculate_average())
    print()