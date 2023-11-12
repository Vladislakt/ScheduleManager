from domain.storage.Teacher import Teacher
from domain.storage.TeacherRepository import TeacherRepository

class AddTeacherOperation:
    def __init__(self, teacher_repository: TeacherRepository):
        self.teacher_repository = teacher_repository

    def add_teacher(self, teacher: Teacher):
        self.teacher_repository.teacher_list.append(teacher)