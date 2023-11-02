class Diary:
    def init(self, student):
        self.student = student
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

class Subject:
    def init(self, name):
        self.name = name

class Student:
    def init(self, name):
        self.name = name


student1 = Student("Adil")
math_subject = Subject("Math")
russian_subject = Subject("russ")
diary = Diary(student1)

diary.add_subject(math_subject)
diary.add_subject(russian_subject)

print(f"Student: {diary.student.name}")
print("Subjects:")
for subject in diary.subjects:
    print(f"- {subject.name}")