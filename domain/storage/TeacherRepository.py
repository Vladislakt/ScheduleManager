from domain.storage import Teacher


class TeacherRepository:
    def __init__(self):
        self.teacher_list = []

    def add_teacher(self, teacher: Teacher):
        self.teacher_list.append(teacher)

    def list(self):
        return list(self.teacher_list.values())

    def fetch(self, teacher_id: int):
        return self.teacher_list[teacher_id]