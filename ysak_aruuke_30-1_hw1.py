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
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def calculate_salary(self):
        base_salary = self.salary
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * base_salary
            base_salary += bonus
        return base_salary


def create_students():
    student1 = Student("John Smith", 16, False, {"Math": 90, "Science": 85, "History": 92})
    student2 = Student("Alice Johnson", 15, False, {"Math": 95, "Science": 87, "History": 88})
    student3 = Student("David Williams", 17, False, {"Math": 88, "Science": 91, "History": 90})

    students = [student1, student2, student3]
    return students


# Создание учителя и распечатка информации о нем
teacher = Teacher("Mary Thompson", 35, True, 7, 5000)
teacher.introduce_myself()
print("Salary:", teacher.calculate_salary())

# Создание учеников и вывод информации о них
students = create_students()
for student in students:
    student.introduce_myself()
    print("Marks:", student.marks)
    print("Average Mark:", student.calculate_average())
    print()