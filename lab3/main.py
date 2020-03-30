from statistics import mean
class Student:
    def __init__(self, name, surname):
        self.name = name    
        self.surname = surname
        self.grades = []
        self.being_on_lessons = []
    def average_grade(self):
        self.average = mean(self.grades)
    def count_total_attendance(self):
        self.frequency = mean(self.being_on_lessons)

class Class:
    def __init__(self, name_of_class, name_of_teacher, students):
        self.name_of_class = name_of_class
        self.name_of_teacher = name_of_teacher
        self.students = students
    def total_average_grade_of_students(self):
        average_of_class = []
        for student in self.students:
            average_of_class.append(student.average)
        self.total_average_of_class  = mean (average_of_class)
    def check_attendance(self,attendance):
        for is_present in attendance:
            for student in self.students:
                student.being_on_lessons.append(is_present)
    def add_grades(self, grades):
        for grade in grades:
            for student in self.students:
                student.grades.append(grade)
student1 = Student("Ala","XXX")
students = [student1]
class1 = Class("1C","MK",students)    
class1.add_grades([1])
student1.average_grade()
print(student1.average)
class1.total_average_grade_of_students()
print(class1.total_average_of_class)