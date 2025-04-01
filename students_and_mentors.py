class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self._average_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''
    
    def _average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        return round(sum(all_grades)/len(all_grades), 1) if len(all_grades) > 0 else 0

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'
    
    def _average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        return round(sum(all_grades)/len(all_grades), 1) if len(all_grades) > 0 else 0

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

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


studen_Ivan = Student('Ivan', 'Petrov', 'male')
studen_Ivan.courses_in_progress += ['Python', 'Git']

studen_Max = Student('Max', 'Storm', 'male')
studen_Max.courses_in_progress += ['Python']
studen_Max.finished_courses += ['Введение']

reviewer_Jhon = Reviewer('Jhon', 'Cena')
reviewer_Jhon.courses_attached += ['Python', 'Git']

reviewer_Donald = Reviewer('Donald', 'Trump')
reviewer_Donald.courses_attached += ['Python']

lecturer_Pit = Lecturer('Pit', 'Rock')
lecturer_Pit.courses_attached += ['Python']

lecturer_Matt = Lecturer('Matt', 'DD')
lecturer_Matt.courses_attached += ['Git', 'Python']


studen_Ivan.add_courses('Введение')
studen_Max.add_courses('Git')

studen_Ivan.rate_lecturer(lecturer_Pit, 'Python', 10)
studen_Ivan.rate_lecturer(lecturer_Matt, 'Git', 10)
studen_Max.rate_lecturer(lecturer_Matt, 'Python', 9)

reviewer_Jhon.rate_hw(studen_Ivan, 'Python', 10)
reviewer_Jhon.rate_hw(studen_Ivan, 'Git', 10)
reviewer_Donald.rate_hw(studen_Ivan, 'Python', 9)
reviewer_Jhon.rate_hw(studen_Max, 'Python', 9)
reviewer_Donald.rate_hw(studen_Max, 'Python', 7)


print(studen_Ivan)
print(studen_Max)
print(reviewer_Jhon)
print(reviewer_Donald)
print(lecturer_Pit)
print(lecturer_Matt)


def average_grade_of_all_students(students, course):
    course_grades = []
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            course_grades += student.grades[course]
    return round(sum(course_grades)/len(course_grades), 1) if len(course_grades) > 0 else 0

def average_grade_of_all_lecturers(lecturers, course):
    course_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            course_grades += lecturer.grades[course]
    return round(sum(course_grades)/len(course_grades), 1) if len(course_grades) > 0 else 0


# print(average_grade_of_all_students([studen_Ivan, studen_Max], 'Python'))
# print(average_grade_of_all_lecturers([lecturer_Matt, lecturer_Pit], 'Python'))