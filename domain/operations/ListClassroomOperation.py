from typing import List
from domain.storage.Classroom import Classroom
from domain.storage.ClassroomRepository import ClassroomRepository


class ListClassroomOperation:
    def __init__(self, classroom_repository: ClassroomRepository):
        self.classroom_repository = classroom_repository

    def list(self) -> List[Classroom]:
        return self.classroom_repository.list()