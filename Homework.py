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
        sum_grades = 0
        len_grades = 0
        for course in self.grades.values():
            sum_grades += sum(course)
            len_grades += len(course)
        avg_grades = round(sum_grades / len_grades, 1)
        return avg_grades

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнивать!")
            return
        return self.average_grade() < other.average_grade()

    def average_grades_for_course(self, course):
        sum_grades = 0
        len_grades = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_grades += sum(self.grades[course])
                len_grades += len(self.grades[course])
        avg_grade_crs = round(sum_grades / len_grades, 1)
        return avg_grade_crs


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        sum_grades = 0
        len_grades = 0
        for course in self.grades.values():
            sum_grades += sum(course)
            len_grades += len(course)
        avg_grade = round(sum_grades / len_grades, 2)
        return avg_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student) and self.grades and other.grades:
            return self._average_grade() < other._average_grade()
        return 'Error'

    def average_grades_for_course(self, course):
        sum_grades = 0
        len_grades = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_grades += sum(self.grades[course])
                len_grades += len(self.grades[course])
        avg_grade_crs = round(sum_grades / len_grades, 2)
        return avg_grade_crs

class Reviewer(Mentor):
    def __int__(self, name, surname):
        super.__init__(name, surname)

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
student_1.finished_courses += ['Tutorial']
student_1.courses_in_progress += ['Python', 'OOP']

student_2 = Student('Chloe', 'Sullivan', 'female')
student_2.finished_courses += ['Git']
student_2.courses_in_progress += ['Python']

lecturer_1 = Lecturer('Elena', 'Nikitina')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Oleg', 'Bulygin')
lecturer_2.courses_attached += ['Python', 'Git', 'C++']

reviewer_1 = Reviewer('Alex', 'Albon')
reviewer_1.courses_attached += ['Python', 'Git', 'Racing']

reviewer_2 = Reviewer('Lewis', 'Hamilton')
reviewer_2.courses_attached += ['Python', 'Git', 'Carting']

student_1.rate(lecturer_2, 'Python', 10)
student_2.rate(lecturer_1, 'Python', 8)
#
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 8)

list_student = [student_1, student_2]
list_lecturer = [lecturer_1, lecturer_2]
list_reviewer = [reviewer_2, reviewer_1]

def average_grade_for_course(course, list_student):
    sum_grades = 0
    qtl_grades = 0
    for student in list_student:
        for course in student.grades:
            student_sum_grades = student.average_grades_for_course(course)
            sum_grades += student_sum_grades
            qtl_grades += 1
    avg_grades = round(sum_grades / qtl_grades, 1)
    return avg_grades

print('=' * 50)
print(f'Средняя оценка за домашнее задание всех студентов: {average_grade_for_course("Python", list_student)}')
print(f'Средняя оценка за проведенные лекции по всем лекторам: {average_grade_for_course("Python", list_lecturer)}')
print('=' * 50)
print('Студенты:\n')
print(student_1)
print('-' * 50)
print(student_2)
print('=' * 50)
print('Лекторы:\n')
print(lecturer_1)
print('-' * 50)
print(lecturer_2)
print('=' * 50)
print('Ревьюеры:\n')
print(reviewer_1)
print('-' * 50)
print(reviewer_2)
print('=' * 50)



