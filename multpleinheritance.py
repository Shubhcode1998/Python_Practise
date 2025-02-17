class teacher:
    def teacher_func(self):
        print("i am a teacher")


class student:
    def student_func(self):
        print("I am a student")

class youtuber:
    def youtuber_func(self):
        print("I am a youtuber")


class person(teacher,student,youtuber):
    pass

coder = person()

coder.teacher_func()
coder.student_func()
coder.youtuber_func()
