from typing import Optional
from domain.storage.Teacher import Teacher
from domain.storage.TeacherRepository import TeacherRepository

class FetchTeacherOperation:
    def __init__(self, teacher_repository: TeacherRepository):
        self.teacher_repository = teacher_repository

    def fetch(self, teacher_id: int) -> Optional[Teacher]:
        return self.teacher_repository.fetch(teacher_id)