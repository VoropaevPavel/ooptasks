class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_in_progress = []

    def _average_grade(self):
        grade = []
        for value in self.grades.items():
            grade.extend(value)
        return round(sum(grade)/len(grade), 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer) and self.grades and other.grades:
            return self._average_grade() < other._average_grade()
        return 'Error'

    def average_lecturers_grade(self, course):
        total_grade = []
        for grades in self.grades.items() and course in self.courses_in_progress:
            total_grade += grades
        return round(sum(total_grade)/len(total_grade), 2)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course == lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        grade = []
        for value in self.grades.items():
            grade += value
        return round(sum(grade)/len(grade), 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student) and self.grades and other.grades:
            return self._average_grade() < other._average_grade()
        return 'Error'

    def average_students_grade(self, course):
        total_grade = []
        for grades in self.grades.items() and course in self.courses_in_progress:
            total_grade += grades
        return round(sum(total_grade)/len(total_grade), 2)


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_1 = Student('Ruoy', 'Eman', 'male')
student_1.finished_courses = ['Tutorial']
student_1.courses_in_progress += ['Python', 'OOP']

student_2 = Student('Chloe', 'Sullivan', 'female')
student_2.finished_courses = ['Git']
student_2.courses_in_progress += ['Python']

students = [student_1, student_2]

lecturer_1 = Lecturer('Elena', 'Nikitina')
lecturer_1.courses_attached = ['Python', 'Git']

lecturer_2 = Lecturer('Oleg', 'Bulygin')
lecturer_2.courses_attached = ['Python', 'Git', 'C++']

lecturers = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Alex', 'Albon')
reviewer_1.courses_attached = ['Python', 'Git', 'Racing']

reviewer_2 = Reviewer('Lewis', 'Hamilton')
reviewer_2.courses_attached = ['Python', 'Git', 'Carting']

student_1.rate(lecturer_2, 'Python', 10)
student_2.rate(lecturer_1, 'Python', 8)

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 8)
print('Эксперты, проверяющие домашние задания:')
print(reviewer_1)
print(reviewer_2)

# student_1._average_grade()
# student_2._average_grade()
student_1.rate(lecturer_1, 'Python', 9)
student_1.rate(lecturer_2, 'Python', 8)
student_2.rate(lecturer_2, 'Python', 10)
student_2.rate(lecturer_1, 'Python', 7)
print('Студенты:')
print(student_1)
print(student_2)
# print(student_2 < student_1)

# lecturer_1._average_grade()
# lecturer_2._average_grade()
print('Лекторы:')
print(lecturer_1)
print(lecturer_2)
# print(lecturer_1 < lecturer_2)

print('Средняя оценка по всем студентам:')
print(average_students_grade(students, 'Python'))

print('Средняя оценка по всем лекторам:')
print(average_lecturers_grade(lecturers, 'Python'))
