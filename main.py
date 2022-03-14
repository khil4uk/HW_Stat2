class Student:
    def __init__(self, name, surname, gender):
        """Инициализация класса студента"""
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_from_students(self, lecturer, course, grade):
        """Оценивание лектора студентом"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grades(self):
        """Функция подсчета средней оценки"""
        sum = 0
        count = 0
        if len(self.grades) != 0:
            for value in self.grades.values():
                for grade in value:
                    sum += grade
                    count += 1
                    average = sum / count
                return round(average)
        else:
            return 0

    def __str__(self):
        """Магический метод для вывода информации"""
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за домашние задания: {self.avg_grades()} \n" \
               f"Курсы в процессе изучения: {self.courses_in_progress} \n" \
               f"Завершенные курсы: {self.finished_courses}"

    def __lt__(self, other):
        """Магический метод для сравнения студента с лектором по средней оценке"""
        if not isinstance(other, Student):
            print('Сравниваются разные классы')
        return self.avg_grades() < other.avg_grades()

class Mentor:
    def __init__(self, name, surname):
        """Инициализация класса ментора"""
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname):
        """Инициализация класса проверяющего преподавателя"""
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        """Оценивание студента проверяющим преподавателем"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Магический метод для вывода информации"""
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        """Инициализация класса лектора"""
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def avg_grades(self):
        """Функция подсчета средней оценки"""
        sum = 0
        count = 0
        if len(self.grades) != 0:
            for value in self.grades.values():
                for grade in value:
                    sum += grade
                    count += 1
                    average = sum / count
                return round(average)
        else:
            return 0

    def __str__(self):
        """Магический метод для вывода информации"""
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {self.avg_grades()}"

    def __lt__(self, other):
        """Магический метод для сравнения студента с лектором по средней оценке"""
        if not isinstance(other, Lecturer):
            print('Сравниваются разные классы')
        return self.avg_grades() < other.avg_grades()

# Вводные данные

# 1-й студент
first_student = Student('Ruoy', 'Eman', 'your_gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['SQL']
first_student.finished_courses += ['Git']

# 2-й студент
second_student = Student('Ivan', 'Ivanov', 'man')
second_student.courses_in_progress += ['Math']
second_student.courses_in_progress += ['SQL']
second_student.finished_courses += ['Culture']

# 1-й лектор
first_lecturer = Lecturer('Another', 'One')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['SQL']

# 2-й лектор
second_lecturer = Lecturer('Sergey', 'Petrov')
second_lecturer.courses_attached += ['SQL']
second_lecturer.courses_attached += ['Math']

# 1-й проверяющий преподаватель
first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['SQL']

# 2-й проверяющий преподаватель
second_reviewer = Reviewer('Some', 'Buddy')
second_reviewer.courses_attached += ['Math']
second_reviewer.courses_attached += ['SQL']

#Оценивание лекторов 1-м студентом
first_student.rate_from_students(first_lecturer, 'Python', 8)
first_student.rate_from_students(first_lecturer, 'Python', 10)
first_student.rate_from_students(first_lecturer, 'Python', 7)
first_student.rate_from_students(second_lecturer, 'SQL', 10)
first_student.rate_from_students(second_lecturer, 'SQL', 10)
first_student.rate_from_students(second_lecturer, 'SQL', 7)

#Оценивание лекторов 2-м студентом
second_student.rate_from_students(first_lecturer, 'SQL', 4)
second_student.rate_from_students(first_lecturer, 'SQL', 5)
second_student.rate_from_students(first_lecturer, 'SQL', 6)
second_student.rate_from_students(second_lecturer, 'Math', 7)
second_student.rate_from_students(second_lecturer, 'Math', 9)
second_student.rate_from_students(second_lecturer, 'Math', 7)

#Оценивание студентов 1-м проверяющим
first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'SQL', 7)
first_reviewer.rate_hw(second_student, 'SQL', 5)
first_reviewer.rate_hw(second_student, 'SQL', 9)

#Оценивание студентов 2-м проверяющим
second_reviewer.rate_hw(second_student, 'Math', 4)
second_reviewer.rate_hw(second_student, 'Math', 7)
second_reviewer.rate_hw(second_student, 'Math', 10)
second_reviewer.rate_hw(first_student, 'SQL', 8)
second_reviewer.rate_hw(first_student, 'SQL', 5)
second_reviewer.rate_hw(first_student, 'SQL', 6)

# print(first_reviewer)
# print()
# print(second_lecturer)
# print()
# print(second_student)
# print()
# print(first_student < second_student)
# print()
# print(first_lecturer < second_lecturer)

#Далее функции из 4-го задания

#Создаю список студентов
student_list = [first_student, second_student]

def avg_grades_all_students(student_list, course):
    """Функция подсчета средней оценки за курс по всем студентам"""
    sum = 0
    count = 0
    for Student in student_list:
        for value in Student.grades.values():
            for grade in value:
                sum += grade
                count += 1
                average = sum / count
    return round(average)

# print(first_student.grades)
# print(second_student.grades)
# print(avg_grades_all(student_list, "SQL"))

#Создаю список лекторов
lecturer_list = [first_lecturer, second_lecturer]

def avg_grades_all_lecturers(lecturer_list, course):
    """Функция подсчета средней оценки за курс по всем лекторам"""
    sum = 0
    count = 0
    for Lecturer in lecturer_list:
        for value in Lecturer.grades.values():
            for grade in value:
                sum += grade
                count += 1
                average = sum / count
    return round(average)

print(first_lecturer.grades)
print(second_lecturer.grades)
print(avg_grades_all_lecturers(lecturer_list, "SQL"))