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


first_student = Student('Ruoy', 'Eman', 'your_gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['SQL']
first_student.finished_courses += ['Git']

first_lecturer = Lecturer('Another', 'One')
first_lecturer.courses_attached += ['Python']

first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']

first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Python', 10)

first_student.rate_from_students(first_lecturer, 'Python', 8)
first_student.rate_from_students(first_lecturer, 'Python', 10)
first_student.rate_from_students(first_lecturer, 'Python', 7)

#print(first_student)
#print()
#print(first_lecturer)
#print()
#print(first_reviewer)

print(first_student < first_lecturer)
