class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'fullname: {self.fullname}\n'
              f'age: {self.age}\n'
              f'is_married: {self.is_married}\n')


class Student(Person):
    marks = {}

    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def introduce_myself(self):
        print(f'fullname: {self.fullname}\n'
              f'age: {self.age}\n'
              f'is_married: {self.is_married}\n'
              f'marks: {self.marks}\n')

    def average_rating_math(self):
        quantity = 0
        for i in self.marks.values():
            quantity += i
        print(quantity // len(self.marks.values()))

    def create_students(self):
        student1 = Student("asan", 19, True, {"english": 3, "rasha": 5})
        student2 = Student("ren", 20, False, {"math": 2, "history": 2})
        student3 = Student("han", 90, False, {"math": 5, "history": 5})
        quantity_spisok = student1, student2, student3
        for i in quantity_spisok:
            print(Student.introduce_myself(i))
            print(Student.average_rating_math(i))



class Teacher(Person):

    procent_experience = 5
    experience = 0
    salary = 0

    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married,)
        self.experience = experience
        self.salary = salary

    def opyt_raboty(self):
        if self.experience >= 3:
            zarplata = self.salary + self.procent_experience * 100
            print(zarplata)






chelovek1 = Person('Aleksandra', 22, True)

chelovek1.introduce_myself()

student1 = Student("Aktan", 17, False, {"math": 5, 'drawing': 5, 'chemistry': 4, 'biology': 5, 'literature': 5, 'history': 5})
student1.create_students()
student1.introduce_myself()
student1.average_rating_math()
#
print(len(student1.marks // zarplata))

teacher1 = Teacher("teacher", 29, True, 6, 40000)
teacher1.opyt_raboty()




