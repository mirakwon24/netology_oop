class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = float()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_counter = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for grades_key in self.grades:
            grades_counter += len(self.grades[grades_key])
        self.average_grades = sum(map(sum, self.grades.values())) / grades_counter
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grades}\n' \
              f'Курсы в процессе изучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.average_grades < other.average_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
#название род.класса в скобках
#Класс менторы становится родительским от него реализутся Лекторы и Ревьюверы
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = float()

    def __str__(self):
        grades_counter = 0
        for grades_key in self.grades:
            grades_counter += len(self.grades[grades_key])
        self.average_grades = sum(map(sum, self.grades.values())) / grades_counter
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_grades}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
            return
        return self.average_grades < other.average_grades


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

student_1 = Student('Emma', 'Watson', 'female')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Peter', 'Parker', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Tony', 'Soprano')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Stiven', 'King')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Jon', 'Alex')
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(best_student, 'Python', 10)


student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 9)
best_student.rate_lecturer(lecturer_1, 'Git', 9)

print(lecturer_1.grades, lecturer_1.name)
print(lecturer_2.grades, lecturer_2.name)
print(student_1.grades, student_1.name)
print(student_2.grades, student_2.name)
print(best_student.grades, best_student.name)
print(f'Студенты:\n{student_1}\n{student_2}\n{best_student}')
print(f'Лекторы:\n{lecturer_1}\n{lecturer_2}')
print(f'Проверяющие:\n{reviewer_1}\n{reviewer_2}')
print(student_1 < student_2)
print(lecturer_1 > lecturer_2)

student = (best_student, student_1, student_2)
lecturer = (lecturer_1, lecturer_2)

#оценка студентов
def students():
    grades_all = []
    for current_student in student:
        for key, value in current_student.grades.items():
            if key == 'Python':
                for grade in value:
                    grades_all.append(grade)
    average_grades = round(sum(grades_all) / len(grades_all), 2)
    print(f'Средняя оценка для всех студентов по курсу "Python": {average_grades} ')

#оценка для лекторов
def lecturers():
    grades_all = []
    for current_lecturer in lecturer:
        for key, value in current_lecturer.grades.items():
            if key == 'Python':
                for grade in value:
                    grades_all.append(grade)
    average_grades = round(sum(grades_all) / len(grades_all), 2)
    print(f'Средняя оценка для всех лекторов по курсу "Python": {average_grades} ')


students()
lecturers()
