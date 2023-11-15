class TeacherRepository:
    def __init__(self):
        self.teacher_list = []

    def add_teacher(self, teacher):
        self.teacher_list.append(teacher)