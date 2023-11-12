from typing import Optional
from domain.storage.Lesson import Lesson
from domain.storage.LessonRepository import LessonRepository

class FetchClassroomOperation:
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    def fetch(self, id: int) -> Optional[Lesson]:
        return self.lesson_repository.fetch(id)