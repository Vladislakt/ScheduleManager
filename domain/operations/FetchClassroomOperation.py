from typing import Optional
from domain.storage.Classroom import Classroom
from domain.storage.ClassroomRepository import ClassroomRepository

class FetchClassroomOperation:
    def __init__(self, classroom_repository: ClassroomRepository):
        self.classroom_repository = classroom_repository

    def fetch(self, classroom_id: int) -> Optional[Classroom]:
        return self.classroom_repository.fetch(classroom_id)