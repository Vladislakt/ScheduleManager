from typing import List
from domain.storage.Lesson import Lesson
from domain.storage.LessonRepository import LessonRepository


class ListLessonOperation:
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    def list(self) -> List[Lesson]:
        return self.lesson_repository.list()