from typing import List
from domain.storage.Teacher import Teacher
from domain.storage.TeacherRepository import TeacherRepository


class ListTeacherOperation:
    def __init__(self, teacher_repository: TeacherRepository):
        self.teacher_repository = teacher_repository

    def list(self) -> List[Teacher]:
        return self.teacher_repository.list()