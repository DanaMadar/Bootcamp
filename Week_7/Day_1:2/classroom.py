import faker
from datetime import datetime
import json
f = faker.Faker()
# text, int/numbers, bool, list, dictionary/object


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = {}
        self.absences = []

    def to_json(self, format_code):
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'grades': self.grades,
            'absences': [absence.strftime(format_code) for absence in self.absences]
        }
        return data

    @classmethod
    def from_json(cls, data, format_code):
        student = cls(data['first_name'], data['last_name'])
        student.grades = data['grades']
        student.absences = [datetime.strptime(
            absence, format_code) for absence in data['absences']]
        return student

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'Student object: {self.full_name()}'

    def __str__(self):
        return f'Student object: {self.full_name()}'


class ClassRoom:
    format_code = '%Y/%m/%d'

    def __init__(self, subject, teacher_name):
        self.subject = subject
        self.teacher = teacher_name
        self.students = []
        self.attendace_list = []

    def to_json(self, file_name):
        attendance_copy = self.attendace_list
        print(self.attendace_list)
        for attendance in attendance_copy:
            print(attendance['date'])
            if isinstance(attendance['date'], datetime):

                attendance['date'] = attendance['date'].strftime(
                    self.format_code)

        data = {
            'subject': self.subject,
            'teacher': self.teacher,
            'students': [stu.to_json(self.format_code) for stu in self.students],
            'attendance_list': attendance_copy
        }

        print(data)
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2)
        print(f'file {file_name} was created successfully')

    @classmethod
    def from_json(cls, file_name):
        with open(file_name) as f:
            data = json.load(f)

        instance = cls(data['subject'], data['teacher'])
        instance.attendace_list = data['attendance_list']
        instance.students = [Student.from_json(
            stu, cls.format_code) for stu in data['students']]
        for attendance in instance.attendace_list:
            attendance['date'] = datetime.strptime(
                attendance['date'], cls.format_code)
        print(instance.attendace_list)
        return instance

    def take_student_name_input(self):
        full_name = input(
            'What\'s the students full name? (seperated by spaces)').lower().split()
        return ' '.join(full_name[0:-1]), full_name[-1]

    def add_student(self):
        self.students.append(Student(*self.take_student_name_input()))

    def populate_class(self, num):
        for _ in range(num):
            self.students.append(Student(f.first_name(), f.last_name()))

    def remove_student(self):
        fname, lname = self.take_student_name_input()
        for student in self.students:
            if fname == student.first_name and lname == student.last_name:
                idx = self.students.index(student)
                print('student removed successfully', student.full_name())
                del self.students[idx]
                return

        print('that student doesnt exist')

    def take_attendance(self):
        today = datetime.today()
        attendance = {
            'date': today,
            'attendees': []
        }
        for student in self.students:
            while True:
                user_input = input(f'is {student.full_name()} present? Y/N:')
                if user_input in ['y', 'n', 'Y', 'N']:
                    break

            if user_input in 'Yy':
                attendance['attendees'].append(student.full_name())
            else:
                print(type(today))
                student.absences.append(today)
        self.attendace_list.append(attendance)

    def show_students(self):
        for student in self.students:
            print(
                f'{student.full_name()}, learning {self.subject}, has {len(student.absences)} absences')

    def __repr__(self):
        return f'Class by {self.teacher}: {self.subject}, {len(self.students)} students registered'

    def __str__(self):
        return f'Class by {self.teacher}: {self.subject}, {len(self.students)} students registered'
