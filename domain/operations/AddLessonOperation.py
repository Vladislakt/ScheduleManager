from domain.storage.Lesson import Lesson
from domain.storage.LessonRepository import LessonRepository

class AddLessonOperation:
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    def add_lesson(self, lesson: Lesson):
        self.lesson_repository.lesson_list.append(lesson)
